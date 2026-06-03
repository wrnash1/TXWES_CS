# Video Script: Module 11 — Transfer Learning and Fine-Tuning

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: TensorFlow Developer Certificate

---

## SEGMENT 1 — Introduction and Motivation (0:00–2:30)

**[ON CAMERA]**

Welcome back. I'm Professor Nash, and this is Module 11 of CIS-4345.

Here is a question I want you to sit with for a moment. Training a state-of-the-art image classifier from scratch on ImageNet — 1.2 million images, 1000 classes — takes roughly two to three weeks on a cluster of high-end GPUs. The research teams at Google and Microsoft that built VGG16, ResNet, and MobileNet spent months and enormous computational budgets developing those models.

Now here is the good news: you do not need to do any of that.

Transfer learning is the practice of taking a model that was already trained on a large dataset and reusing it — either partially or fully — for a new, related task. Instead of starting from random weights, you start from weights that already encode rich, generalizable features: edges, textures, shapes, object parts.

This is not a shortcut or a cheat. It is how nearly all modern deep learning applications in industry actually work. If your company wants an image classifier for a custom product, no engineer is training ResNet50 from scratch. They are fine-tuning a pretrained model on their specific data.

In this module we will cover:

- Why and how pretrained features transfer between tasks

- Feature extraction: using a pretrained model as a frozen feature extractor

- Fine-tuning: selectively unfreezing and retraining deeper layers

- The major pretrained architectures: VGG16, ResNet50, MobileNetV2

- TensorFlow Hub for accessing community-maintained pretrained models

Let's get started.

---

## SEGMENT 2 — Why Transfer Learning Works (2:30–5:30)

**[SLIDE: Feature Hierarchy in CNNs]**

To understand why transfer learning works, we need to revisit what CNNs actually learn.

In Module 7 we studied convolutional networks. You learned that early layers learn low-level features — edges, colors, gradients. Middle layers combine those into textures and shapes. Deep layers learn high-level, task-specific representations — "this looks like a wheel" or "this is a face."

Here is the key insight: **low- and mid-level features are generic**. An edge detector is useful whether you are classifying dogs, cars, X-rays, or satellite images. The network has already learned a general visual vocabulary. Only the deepest layers are highly task-specific.

So when we transfer a model trained on ImageNet to classify, say, medical chest X-rays, we are reusing the 90% of the network that encodes generic visual features. We only need to adapt the final layers to the new task.

**[SLIDE: Transfer Learning Spectrum]**

There is a spectrum from pure feature extraction to full fine-tuning:

- **Frozen feature extraction**: All pretrained layers are frozen. Only the new classification head is trained.

- **Partial fine-tuning**: Freeze early layers, unfreeze later layers plus the new head.

- **Full fine-tuning**: Unfreeze the entire network and train end-to-end on the new dataset.

The right choice depends on two factors: how similar the new task is to the original training task, and how much new training data you have.

---

## SEGMENT 3 — Feature Extraction in Keras (5:30–9:30)

**[SCREEN SHARE — Code Editor]**

Let me show you feature extraction with VGG16.

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import VGG16

# Load VGG16 pretrained on ImageNet, exclude the top classification layers
base_model = VGG16(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# Freeze ALL pretrained layers
base_model.trainable = False

print(f"VGG16 base layers: {len(base_model.layers)}")
print(f"Trainable params: {base_model.count_params():,}")
```

When we set `base_model.trainable = False`, we freeze every layer in VGG16. Their weights will not change during training. We are using VGG16 purely as a fixed feature extractor.

Now we add our own classification head on top:

```python
# Build the full model
inputs = keras.Input(shape=(224, 224, 3))
x = base_model(inputs, training=False)   # training=False keeps BN layers frozen
x = keras.layers.GlobalAveragePooling2D()(x)
x = keras.layers.Dense(256, activation='relu')(x)
x = keras.layers.Dropout(0.5)(x)
outputs = keras.layers.Dense(10, activation='softmax')(x)

model = keras.Model(inputs, outputs)
model.summary()
```

Notice `training=False` in `base_model(inputs, training=False)`. This is critical when the base model contains BatchNormalization layers. Without it, the BN running statistics would update during your training, corrupting the pretrained statistics.

Compile and train — only the new head's weights are updated:

```python
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(train_dataset, epochs=10, validation_data=val_dataset)
```

This is fast. Because the base model is frozen, we only backpropagate through the small classification head.

---

## SEGMENT 4 — Fine-Tuning (9:30–13:30)

**[SLIDE: Fine-Tuning Strategy]**

After the classification head converges, we can improve accuracy further by **fine-tuning** — carefully unfreezing some of the pretrained layers and retraining them with a very low learning rate.

The word "carefully" matters. If you unfreeze everything immediately and use a high learning rate, you will destroy the pretrained weights through catastrophic forgetting. The general principle is: unfreeze only the deeper (later) layers, and use a learning rate 10 to 100 times smaller than what you used for the head.

**[SCREEN SHARE — Code Editor]**

Here is the fine-tuning workflow for VGG16:

```python
# Step 1: Unfreeze the base model
base_model.trainable = True

# Step 2: Freeze all layers except the last 4
for layer in base_model.layers[:-4]:
    layer.trainable = False

# Confirm trainable state
print(f"Trainable layers: {sum(1 for l in model.layers if l.trainable)}")

# Step 3: Recompile with a much lower learning rate
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Step 4: Continue training
model.fit(
    train_dataset,
    epochs=20,
    validation_data=val_dataset,
    callbacks=[
        keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
    ]
)
```

The learning rate `1e-5` is critical. It is small enough that we gently nudge the pretrained weights toward the new task without overwriting them.

---

## SEGMENT 5 — Architecture Overview: VGG16, ResNet50, MobileNetV2 (13:30–17:00)

**[SLIDE: VGG16]**

**VGG16**, developed by Oxford's Visual Geometry Group in 2014, was one of the first very deep CNNs. It uses 16 weight layers — all 3x3 convolutions stacked sequentially. Simple and interpretable. The downside is its size: 138 million parameters, 528 MB. Excellent for teaching and prototyping, not ideal for mobile deployment.

**[SLIDE: ResNet50]**

**ResNet50** solved the degradation problem of very deep networks with **residual connections** — skip connections that allow gradients to bypass entire blocks. Trained at 50 layers, it achieves better accuracy than VGG16 with far fewer parameters: about 25 million. ResNet is the backbone of choice for many production vision systems.

**[SLIDE: MobileNetV2]**

**MobileNetV2** was designed specifically for mobile and embedded devices. It uses **depthwise separable convolutions** that dramatically reduce computation. Only 3.4 million parameters. Accuracy is somewhat lower than ResNet on ImageNet, but it is 10 times smaller and much faster at inference. If you are deploying to a mobile app or edge device, MobileNetV2 is usually the right starting point.

**[SLIDE: Comparison Table]**

| Model | Parameters | Top-5 Accuracy | Input Size | Best For |
|---|---|---|---|---|
| VGG16 | 138M | 92.7% | 224x224 | Learning, prototyping |
| ResNet50 | 25M | 93.0% | 224x224 | General production |
| MobileNetV2 | 3.4M | 91.0% | 224x224 | Mobile / edge |

---

## SEGMENT 6 — TensorFlow Hub (17:00–19:30)

**[SCREEN SHARE — Code Editor]**

TensorFlow Hub is a repository of pretrained models maintained by Google and the community. You can load models directly from a URL without managing weight files manually.

```python
import tensorflow_hub as hub

# Load a MobileNetV2 feature extractor from TF Hub
mobilenet_url = (
    "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
)

feature_extractor = hub.KerasLayer(
    mobilenet_url,
    input_shape=(224, 224, 3),
    trainable=False
)

# Build classifier on top
model = keras.Sequential([
    feature_extractor,
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(5, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.summary()
```

The `hub.KerasLayer` wraps any TF Hub module as a standard Keras layer. Setting `trainable=False` freezes it for feature extraction. Set `trainable=True` for fine-tuning.

TF Hub provides models for images, text, audio, and video. For the certificate exam, be familiar with loading image feature extractors from Hub and wrapping them in a Sequential or Functional model.

---

## SEGMENT 7 — Data Augmentation for Transfer Learning (19:30–21:30)

**[SLIDE: Augmentation Pipeline]**

Transfer learning reduces your data requirements significantly, but augmentation still matters — especially when your dataset is small (hundreds to low thousands of images per class).

Here is a standard augmentation pipeline for fine-tuning:

```python
data_augmentation = keras.Sequential([
    keras.layers.RandomFlip("horizontal"),
    keras.layers.RandomRotation(0.1),
    keras.layers.RandomZoom(0.1),
    keras.layers.RandomContrast(0.1),
], name="data_augmentation")

# Integrate into model
inputs = keras.Input(shape=(224, 224, 3))
x = data_augmentation(inputs)
x = keras.applications.mobilenet_v2.preprocess_input(x)
x = base_model(x, training=False)
x = keras.layers.GlobalAveragePooling2D()(x)
outputs = keras.layers.Dense(num_classes, activation='softmax')(x)
```

Notice the `preprocess_input` call — each pretrained model family expects its inputs normalized in a specific way. VGG16 uses BGR channel order and subtracts ImageNet means. MobileNetV2 expects values in `[-1, 1]`. Always use the model-specific preprocessing function, not a generic rescaling layer.

---

## SEGMENT 8 — Wrap-Up and Certification Alignment (21:30–24:00)

**[ON CAMERA]**

Let's wrap up.

Transfer learning reuses features learned on large datasets for new tasks. Feature extraction freezes the base model and trains only the new head — fast and safe with limited data. Fine-tuning carefully unfreezes deeper layers with a low learning rate to adapt the pretrained features to the new domain. VGG16, ResNet50, and MobileNetV2 are the three architectures you need to know for the TensorFlow Developer Certificate. TensorFlow Hub provides a clean API for loading any of these as a Keras layer.

For the certificate exam, make sure you can:

- Load a pretrained model with `include_top=False`
- Freeze the base with `base_model.trainable = False`
- Build a classification head using GlobalAveragePooling2D and Dense layers
- Implement fine-tuning by selectively unfreezing layers
- Use the correct `preprocess_input` function for each model family

The lab for this module has you build a flower classifier using MobileNetV2 with both feature extraction and fine-tuning phases. Pay close attention to how validation accuracy improves between the two phases — that delta is the value that fine-tuning adds.

See you in Module 12, where we tackle model optimization, Keras Tuner, and TensorFlow Lite.

---

*[End of Script — Module 11]*

# Lab: Module 11 — Transfer Learning and Fine-Tuning

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Lab Overview

In this lab you will build a flower species classifier using MobileNetV2 pretrained on ImageNet. You will implement the complete two-phase transfer learning workflow: feature extraction followed by fine-tuning. You will compare accuracy between phases, visualize the feature maps learned by the pretrained network, and practice the preprocessing patterns required by the TensorFlow Developer Certificate exam.

**Estimated Time:** 90–120 minutes

**Prerequisites:** Module 11 video and reading guide completed

---

## Learning Objectives

By completing this lab you will be able to:

- Load a pretrained MobileNetV2 model with `include_top=False`
- Build and train a classification head using GlobalAveragePooling2D
- Correctly freeze and unfreeze layers for the two-phase fine-tuning workflow
- Apply model-specific preprocessing using `preprocess_input`
- Evaluate and compare accuracy across training phases
- Visualize intermediate feature maps from pretrained layers

---

## Setup

```python
# Cell 1 — Imports
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import matplotlib.pyplot as plt
import os

print(f"TensorFlow: {tf.__version__}")
print(f"GPU available: {len(tf.config.list_physical_devices('GPU')) > 0}")
```

---

## Step 1 — Load and Explore the Dataset

You will use the `tf_flowers` dataset — 3,670 labeled flower photos across 5 classes: daisy, dandelion, roses, sunflowers, tulips.

```python
# Cell 2 — Load tf_flowers
import tensorflow_datasets as tfds

(raw_train, raw_val), metadata = tfds.load(
    'tf_flowers',
    split=['train[:80%]', 'train[80%:]'],
    with_info=True,
    as_supervised=True
)

class_names = metadata.features['label'].names
NUM_CLASSES = len(class_names)
print(f"Classes ({NUM_CLASSES}): {class_names}")
print(f"Train examples: {metadata.splits['train'].num_examples}")
```

```python
# Cell 3 — Visualize sample images
plt.figure(figsize=(12, 6))
for i, (image, label) in enumerate(raw_train.take(10)):
    plt.subplot(2, 5, i + 1)
    plt.imshow(image)
    plt.title(class_names[label.numpy()], fontsize=9)
    plt.axis('off')
plt.suptitle("Sample tf_flowers Images (before preprocessing)", y=1.01)
plt.tight_layout()
plt.show()
```

**Expected output:** A 2x5 grid of flower photos with class name titles.

> **Checkpoint 1:** Verify you see 5 distinct flower classes across the 10 images. Note the variation in image sizes — this is why we resize in preprocessing.

---

## Step 2 — Build the Preprocessing Pipeline

```python
# Cell 4 — Preprocessing and augmentation
IMG_SIZE   = 224
BATCH_SIZE = 32
AUTOTUNE   = tf.data.AUTOTUNE

# Augmentation (training only — Keras applies it only during model.fit)
data_augmentation = keras.Sequential([
    keras.layers.RandomFlip("horizontal"),
    keras.layers.RandomRotation(0.15),
    keras.layers.RandomZoom(0.1),
], name="augmentation")

def preprocess_train(image, label):
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    image = preprocess_input(image)   # MobileNetV2-specific: scales to [-1, 1]
    return image, label

def preprocess_val(image, label):
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    image = preprocess_input(image)
    return image, label

train_ds = (raw_train
            .map(preprocess_train, num_parallel_calls=AUTOTUNE)
            .batch(BATCH_SIZE)
            .prefetch(AUTOTUNE))

val_ds = (raw_val
          .map(preprocess_val, num_parallel_calls=AUTOTUNE)
          .batch(BATCH_SIZE)
          .prefetch(AUTOTUNE))

print(f"Train batches: {len(train_ds)}")
print(f"Val batches:   {len(val_ds)}")
```

> **Note:** Augmentation is applied inside the model graph (added to the model in Step 3), so it automatically activates only during `model.fit` and is skipped during `model.evaluate` and `model.predict`.

---

## Step 3 — Phase 1: Feature Extraction

```python
# Cell 5 — Build the model with frozen base
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(IMG_SIZE, IMG_SIZE, 3)
)
base_model.trainable = False  # Freeze all pretrained weights

# Build full model using Functional API
inputs  = keras.Input(shape=(IMG_SIZE, IMG_SIZE, 3))
x       = data_augmentation(inputs)              # augment during training only
x       = base_model(x, training=False)          # training=False keeps BN frozen
x       = keras.layers.GlobalAveragePooling2D()(x)
x       = keras.layers.Dense(128, activation='relu')(x)
x       = keras.layers.Dropout(0.4)(x)
outputs = keras.layers.Dense(NUM_CLASSES, activation='softmax')(x)

model = keras.Model(inputs, outputs, name="transfer_mobilenetv2")
model.summary()

# Count trainable vs frozen parameters
trainable_count = sum(
    tf.size(w).numpy() for w in model.trainable_weights
)
total_count = sum(
    tf.size(w).numpy() for w in model.weights
)
print(f"\nTrainable parameters: {trainable_count:,}")
print(f"Frozen parameters:    {total_count - trainable_count:,}")
print(f"Total parameters:     {total_count:,}")
```

**Expected output:** ~135,000 trainable parameters (the head only) vs ~2.2 million frozen (MobileNetV2 base).

```python
# Cell 6 — Train Phase 1
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history_phase1 = model.fit(
    train_ds,
    epochs=15,
    validation_data=val_ds,
    callbacks=[
        keras.callbacks.EarlyStopping(
            monitor='val_accuracy',
            patience=4,
            restore_best_weights=True
        )
    ]
)

phase1_val_acc = max(history_phase1.history['val_accuracy'])
print(f"\nPhase 1 best validation accuracy: {phase1_val_acc:.4f}")
```

**Expected output:** Validation accuracy in the range 0.82–0.90 after Phase 1.

---

## Step 4 — Phase 2: Fine-Tuning

```python
# Cell 7 — Unfreeze top layers for fine-tuning
base_model.trainable = True

# How many total layers in the base?
print(f"Total layers in base_model: {len(base_model.layers)}")

# Freeze all layers except the last 30
FINE_TUNE_FROM = len(base_model.layers) - 30
for i, layer in enumerate(base_model.layers):
    layer.trainable = (i >= FINE_TUNE_FROM)

# Confirm layer trainability
trainable_names = [l.name for l in base_model.layers if l.trainable]
print(f"Layers being fine-tuned ({len(trainable_names)}): {trainable_names[:5]} ...")
```

```python
# Cell 8 — Recompile with low learning rate and continue training
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),  # 100x smaller
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history_phase2 = model.fit(
    train_ds,
    epochs=20,
    validation_data=val_ds,
    callbacks=[
        keras.callbacks.EarlyStopping(
            monitor='val_accuracy',
            patience=5,
            restore_best_weights=True
        ),
        keras.callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=3,
            min_lr=1e-7
        )
    ]
)

phase2_val_acc = max(history_phase2.history['val_accuracy'])
print(f"\nPhase 2 best validation accuracy: {phase2_val_acc:.4f}")
print(f"Accuracy gain from fine-tuning:   {phase2_val_acc - phase1_val_acc:.4f}")
```

**Expected output:** Fine-tuning typically adds 2–6 percentage points over Phase 1.

---

## Step 5 — Visualize Training History

```python
# Cell 9 — Plot combined training curves
phase1_epochs = len(history_phase1.history['accuracy'])
phase2_epochs = len(history_phase2.history['accuracy'])
total_epochs  = phase1_epochs + phase2_epochs

acc     = history_phase1.history['accuracy']     + history_phase2.history['accuracy']
val_acc = history_phase1.history['val_accuracy'] + history_phase2.history['val_accuracy']
loss    = history_phase1.history['loss']         + history_phase2.history['loss']
val_loss= history_phase1.history['val_loss']     + history_phase2.history['val_loss']

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Accuracy plot
axes[0].plot(acc,     label='Train Accuracy',      color='steelblue')
axes[0].plot(val_acc, label='Val Accuracy',         color='steelblue', linestyle='--')
axes[0].axvline(x=phase1_epochs, color='gray', linestyle=':', label='Fine-tune start')
axes[0].set_title("Accuracy — Phase 1 + Phase 2")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Accuracy")
axes[0].legend()
axes[0].grid(alpha=0.3)

# Loss plot
axes[1].plot(loss,     label='Train Loss', color='darkorange')
axes[1].plot(val_loss, label='Val Loss',   color='darkorange', linestyle='--')
axes[1].axvline(x=phase1_epochs, color='gray', linestyle=':', label='Fine-tune start')
axes[1].set_title("Loss — Phase 1 + Phase 2")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Loss")
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Step 6 — Visualize Predictions

```python
# Cell 10 — Show predictions on validation images
sample_images, sample_labels = next(iter(val_ds))
preds = model.predict(sample_images[:9], verbose=0)
pred_classes = np.argmax(preds, axis=1)

# Reverse MobileNetV2 preprocess_input for display: scale [-1,1] back to [0,1]
def deprocess(img):
    img = (img + 1.0) / 2.0
    return np.clip(img, 0, 1)

plt.figure(figsize=(12, 12))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(deprocess(sample_images[i].numpy()))
    true_label = class_names[sample_labels[i].numpy()]
    pred_label = class_names[pred_classes[i]]
    confidence = preds[i][pred_classes[i]]
    color = 'green' if true_label == pred_label else 'red'
    plt.title(f"True: {true_label}\nPred: {pred_label} ({confidence:.0%})",
              color=color, fontsize=9)
    plt.axis('off')
plt.suptitle("Validation Predictions (green=correct, red=incorrect)", y=1.01)
plt.tight_layout()
plt.show()
```

---

## Step 7 — Experiment: Replace MobileNetV2 with ResNet50

```python
# Cell 11 — ResNet50 feature extraction for comparison
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess

def preprocess_resnet(image, label):
    image = tf.image.resize(image, (224, 224))
    image = resnet_preprocess(image)
    return image, label

train_ds_r = raw_train.map(preprocess_resnet, num_parallel_calls=AUTOTUNE).batch(BATCH_SIZE).prefetch(AUTOTUNE)
val_ds_r   = raw_val.map(preprocess_resnet,   num_parallel_calls=AUTOTUNE).batch(BATCH_SIZE).prefetch(AUTOTUNE)

resnet_base = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
resnet_base.trainable = False

inputs_r  = keras.Input(shape=(224, 224, 3))
x_r       = resnet_base(inputs_r, training=False)
x_r       = keras.layers.GlobalAveragePooling2D()(x_r)
x_r       = keras.layers.Dense(128, activation='relu')(x_r)
outputs_r = keras.layers.Dense(NUM_CLASSES, activation='softmax')(x_r)
resnet_model = keras.Model(inputs_r, outputs_r, name="transfer_resnet50")

resnet_model.compile(
    optimizer=keras.optimizers.Adam(1e-3),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history_resnet = resnet_model.fit(
    train_ds_r, epochs=10, validation_data=val_ds_r, verbose=1
)

resnet_val_acc = max(history_resnet.history['val_accuracy'])
print(f"\nMobileNetV2 Phase 1 accuracy: {phase1_val_acc:.4f}")
print(f"ResNet50 feature extraction:  {resnet_val_acc:.4f}")
print(f"ResNet50 parameters:          {resnet_model.count_params():,}")
print(f"MobileNetV2 parameters:       {model.count_params():,}")
```

---

## Deliverables

Submit a Jupyter notebook (.ipynb) with all cells executed. Your submission must include:

1. Dataset visualization grid (Cell 3)
2. `model.summary()` output showing trainable vs. frozen parameter counts
3. Phase 1 training log showing best validation accuracy
4. Phase 2 training log showing best validation accuracy and accuracy gain
5. Combined training curve plot with the fine-tune boundary marked (Cell 9)
6. Prediction visualization grid with correct/incorrect color coding (Cell 10)
7. ResNet50 comparison table: validation accuracy and total parameter count vs. MobileNetV2

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Dataset loaded and visualized correctly | 10 |
| Model built with correct frozen base and GlobalAveragePooling2D head | 20 |
| Phase 1 trains and achieves validation accuracy above 0.75 | 15 |
| Phase 2 fine-tunes with correct low learning rate and improves accuracy | 20 |
| Combined training curve plot present and annotated | 15 |
| Prediction grid with correct/incorrect labeling | 10 |
| ResNet50 comparison completed with written observation | 10 |
| **Total** | **100** |

---

*End of Lab — Module 11*

---

## Part 9 — Challenge Exercise

### Challenge 1: Gradual Layer Unfreezing

Instead of unfreezing all fine-tuning layers at once (as in Part 2), implement a gradual unfreezing schedule that trains one additional convolutional block per epoch.

1. After completing Phase 1 (feature extraction), unfreeze only the last convolutional block of MobileNetV2. Compile with `optimizer=Adam(1e-5)` and train for 5 epochs. Record validation accuracy.
2. Unfreeze one additional block (now the last 2 blocks are trainable). Recompile with `Adam(5e-6)` and train 3 more epochs. Record validation accuracy.
3. Unfreeze one more block (last 3 blocks trainable). Recompile with `Adam(2e-6)` and train 3 more epochs. Record validation accuracy.
4. Plot validation accuracy across all three unfreezing stages as a single connected curve. Compare the final accuracy against the single-shot unfreezing approach from Part 2 and note whether gradual unfreezing provided a smoother improvement trajectory.

### Challenge 2: Domain Shift Analysis with Grad-CAM

Implement Gradient-weighted Class Activation Mapping (Grad-CAM) to visualize which image regions your transfer-learned model attends to when making predictions.

1. Implement the Grad-CAM computation using the last convolutional layer of your MobileNetV2 model:

   ```python
   import tensorflow as tf
   import numpy as np

   def grad_cam(model, img_array, layer_name, class_idx):
       grad_model = tf.keras.Model(
           inputs=model.input,
           outputs=[model.get_layer(layer_name).output, model.output]
       )
       with tf.GradientTape() as tape:
           conv_outputs, predictions = grad_model(img_array)
           loss = predictions[:, class_idx]
       grads = tape.gradient(loss, conv_outputs)
       pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
       heatmap = conv_outputs[0] @ pooled_grads[..., tf.newaxis]
       heatmap = tf.squeeze(heatmap)
       heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-8)
       return heatmap.numpy()
   ```

2. Apply Grad-CAM to 5 correctly classified and 5 incorrectly classified test images. Overlay the heatmap on the original image using `cv2.applyColorMap` or `matplotlib.cm`.
3. For the incorrectly classified images, identify whether the model attended to background regions, irrelevant objects, or low-contrast areas. Write a short analysis of what each misclassified image's heatmap reveals about the model's failure mode.
4. Use `layer_name` from `model.get_layer` by iterating over `model.layers` to find the name of the last `Conv2D` layer inside the MobileNetV2 base.

### Reflection Questions

1. In your gradual unfreezing experiment, did releasing earlier (lower-level) convolutional blocks improve validation accuracy, or did performance plateau or degrade after a certain number of unfrozen blocks? What does this tell you about how many layers need to be fine-tuned for your specific target dataset?
2. From your Grad-CAM visualizations, describe one correctly classified image where the model attended to the correct discriminative region and one misclassified image where it attended to an irrelevant region. What augmentation or training strategy might help correct the misclassification you identified?

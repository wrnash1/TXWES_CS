# Reading Guide: Module 07 — Convolutional Neural Networks

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Introduction

Welcome to Module 07 — **Convolutional Neural Networks (CNNs)**! CNNs are the backbone of modern computer vision. They are one of the four core task categories explicitly tested on the TensorFlow Developer Certificate exam, and they underpin nearly every production image classification, object detection, and image segmentation system in use today.

In this reading guide you will build a thorough understanding of the CNN computational graph — from the raw convolution operation through pooling, flattening, and classification — and learn how to implement each component using `tf.keras`. You will also study the key hyperparameters that control CNN behavior, how to count parameters, and how to read a `model.summary()` output.

---

## 1. High-Yield Glossary

Review these definitions carefully. The certification exam expects precision.

**Convolutional layer (`Conv2D`)**: A layer that applies a set of learnable filters (kernels) to an input tensor by sliding each filter across the spatial dimensions and computing dot products. In Keras: `keras.layers.Conv2D(filters, kernel_size, activation, padding, strides)`. The output is a 3D tensor called a **feature map** (or activation map) with shape `(height, width, filters)`.

**Filter (kernel)**: A small 2D matrix of learnable weights — typically `3x3` or `5x5` — shared across all spatial locations in the input. Each filter detects one type of pattern (e.g., a horizontal edge, a color gradient). A layer with `filters=32` learns 32 independent filters simultaneously.

**Feature map**: The output produced by sliding one filter across the input. If a layer has 32 filters, it produces 32 feature maps stacked along the depth axis, resulting in an output tensor of depth 32.

**Stride**: The number of pixels the filter moves at each step. `strides=1` (default) moves one pixel at a time; `strides=2` halves the spatial dimensions of the output without pooling.

**Padding**: Controls how the filter handles image borders. `padding='valid'` (no padding) produces a smaller output; `padding='same'` pads the input with zeros so the output has the same spatial dimensions as the input.

**Max pooling (`MaxPooling2D`)**: A downsampling operation that replaces each `pool_size x pool_size` region with its maximum value. Default: `pool_size=(2,2)`, `strides=2`, which halves both spatial dimensions. Provides translation invariance and reduces computation.

**Global Average Pooling (`GlobalAveragePooling2D`)**: Averages each entire feature map into a single scalar. Converts a tensor of shape `(H, W, C)` to `(C,)`. Used in modern architectures as a replacement for `Flatten() + Dense` to dramatically reduce parameters.

**Flatten**: Reshapes a 3D tensor `(H, W, C)` into a 1D vector of length `H * W * C`. Required before a `Dense` classification head unless `GlobalAveragePooling2D` is used.

**Parameter sharing**: The core CNN efficiency principle — the same filter weights are used at every spatial position. A `3x3` filter on a `3`-channel input has only `3*3*3 + 1 = 28` parameters regardless of image size, compared to a dense connection which would scale with `H * W`.

**ReLU activation**: `Rectified Linear Unit — f(x) = max(0, x)`. Applied after each convolution to introduce non-linearity. Prevents the vanishing gradient problem that plagues sigmoid/tanh in deep networks.

**Batch Normalization (`BatchNormalization`)**: Normalizes the outputs of a layer to have zero mean and unit variance across the current mini-batch. Placed between the convolution and the activation. Allows higher learning rates and acts as a regularizer.

**Dropout**: A regularization technique that randomly sets a fraction of activations to zero during training. Applied after pooling layers (`rate=0.25`) and before the output (`rate=0.5`) in typical CNN configurations.

**Translation invariance**: The property that a CNN can detect a feature (e.g., an edge) regardless of where it appears in the image. Parameter sharing creates translation equivariance; pooling adds invariance by discarding precise location.

---

## 2. The Convolution Operation in Detail

### Spatial Output Size Formula

For a single spatial dimension:

```
output_size = floor((input_size - kernel_size + 2 * padding) / stride) + 1
```

With `padding='same'` and `stride=1`, `output_size = input_size`.

With `padding='valid'` and `stride=1`, `output_size = input_size - kernel_size + 1`.

### Architecture Dimension Table

The table below traces a `32x32` RGB image through a standard 3-block CNN.

| Layer | Input Shape | Output Shape | Parameters |
|---|---|---|---|
| Conv2D(32, 3x3, same) | (32, 32, 3) | (32, 32, 32) | 896 |
| MaxPooling2D(2x2) | (32, 32, 32) | (16, 16, 32) | 0 |
| Conv2D(64, 3x3, same) | (16, 16, 32) | (16, 16, 64) | 18,496 |
| MaxPooling2D(2x2) | (16, 16, 64) | (8, 8, 64) | 0 |
| Conv2D(128, 3x3, same) | (8, 8, 64) | (8, 8, 128) | 73,856 |
| MaxPooling2D(2x2) | (8, 8, 128) | (4, 4, 128) | 0 |
| Flatten | (4, 4, 128) | (2048,) | 0 |
| Dense(128) | (2048,) | (128,) | 262,272 |
| Dense(10) | (128,) | (10,) | 1,290 |

**Parameter calculation for Conv2D(32, 3x3) on 3-channel input:**

`filters * (kernel_h * kernel_w * input_depth) + filters = 32 * (3*3*3) + 32 = 288 + 32 = 896`

This is the parameter sharing efficiency: 896 parameters handle the entire `32x32x3` input spatial detection task.

---

## 3. Architecture Patterns and Design Choices

### The Standard Block Pattern

```python
# Preferred modern block pattern
keras.layers.Conv2D(filters, (3, 3), padding='same'),
keras.layers.BatchNormalization(),
keras.layers.Activation('relu'),
keras.layers.MaxPooling2D((2, 2)),
keras.layers.Dropout(0.25),
```

Note that `BatchNormalization` is placed **before** the activation in this pattern. Some architectures place it after; both are valid, but the pre-activation order is common in ResNet-style networks.

### Filter Count Convention

Filter counts typically follow powers of two (32, 64, 128, 256) and double with each block. This compensates for the spatial dimension halving from max pooling, maintaining total representational capacity.

### Kernel Size Choices

| Kernel Size | Use Case |
|---|---|
| 1x1 | Channel mixing, dimensionality reduction (used in Inception) |
| 3x3 | Most common — good balance of receptive field and efficiency |
| 5x5 | Larger receptive field — more expensive, less common today |
| 7x7 | Stem layer of ResNet and similar architectures (first layer only) |

Two stacked `3x3` convolutions have the same receptive field as one `5x5` convolution but use fewer parameters: `2*(3*3) = 18` vs `5*5 = 25` weights per channel pair.

---

## 4. Complete Keras Implementation

### CIFAR-10 Classifier with Batch Normalization

```python
import tensorflow as tf
from tensorflow import keras

def build_cifar_cnn(input_shape=(32, 32, 3), num_classes=10):
    model = keras.Sequential([
        # Block 1
        keras.layers.Conv2D(32, (3, 3), padding='same',
                            input_shape=input_shape),
        keras.layers.BatchNormalization(),
        keras.layers.Activation('relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Dropout(0.25),

        # Block 2
        keras.layers.Conv2D(64, (3, 3), padding='same'),
        keras.layers.BatchNormalization(),
        keras.layers.Activation('relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Dropout(0.25),

        # Block 3
        keras.layers.Conv2D(128, (3, 3), padding='same'),
        keras.layers.BatchNormalization(),
        keras.layers.Activation('relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Dropout(0.25),

        # Classifier head
        keras.layers.Flatten(),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.BatchNormalization(),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(num_classes, activation='softmax')
    ])
    return model

model = build_cifar_cnn()
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.summary()
```

### Data Loading and Normalization

```python
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
x_train = x_train.astype('float32') / 255.0
x_test  = x_test.astype('float32')  / 255.0

# CIFAR-10 class names for reference
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
```

### Training with Callbacks

```python
callbacks = [
    keras.callbacks.EarlyStopping(
        monitor='val_accuracy', patience=5, restore_best_weights=True),
    keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6),
    keras.callbacks.ModelCheckpoint(
        'best_cifar_cnn.h5', save_best_only=True,
        monitor='val_accuracy')
]

history = model.fit(
    x_train, y_train,
    epochs=50,
    batch_size=64,
    validation_split=0.1,
    callbacks=callbacks
)
```

---

## 5. Feature Map Visualization

Understanding what a trained CNN has learned is a key TF Certificate skill. Here is how to extract and display feature maps from any layer:

```python
# Create a sub-model that outputs a specific layer's activations
activation_model = keras.Model(
    inputs=model.input,
    outputs=model.get_layer('conv2d').output   # use layer name from summary
)

# Get feature maps for one test image
img = x_test[0:1]                              # shape (1, 32, 32, 3)
feature_maps = activation_model.predict(img)   # shape (1, 32, 32, 32)

# Display first 16 feature maps
import matplotlib.pyplot as plt
fig, axes = plt.subplots(4, 4, figsize=(10, 10))
for idx, ax in enumerate(axes.flat):
    ax.imshow(feature_maps[0, :, :, idx], cmap='plasma')
    ax.set_title(f'Filter {idx}')
    ax.axis('off')
plt.suptitle('Layer 1 Feature Maps', fontsize=14)
plt.tight_layout()
plt.show()
```

---

## 6. Performance Comparison Table

The table below shows typical CIFAR-10 accuracy for different model configurations (approximate, trained 30 epochs, batch size 64).

| Architecture | Params | Val Accuracy | Notes |
|---|---|---|---|
| Dense only (2 layers) | ~3.9M | ~52% | No spatial structure |
| 1-block CNN | ~200K | ~62% | Baseline |
| 3-block CNN (no BN) | ~360K | ~74% | Standard |
| 3-block CNN + BatchNorm | ~363K | ~80% | With regularization |
| 3-block CNN + Augmentation | ~363K | ~84% | See Module 08 |
| ResNet-50 (pretrained) | ~25M | ~93%+ | Transfer learning |

---

## 7. TensorFlow Developer Certificate Exam Tips

**Tip 1 — Know the input shape format.** Keras `Conv2D` requires `input_shape=(height, width, channels)`. A `28x28` grayscale image is `(28, 28, 1)`. A `32x32` color image is `(32, 32, 3)`. Forgetting the channel dimension is a common exam error.

**Tip 2 — `padding='same'` is your friend.** When you want to preserve spatial dimensions through a conv layer, use `padding='same'`. This makes the architecture predictable: only pooling layers reduce spatial size.

**Tip 3 — `sparse_categorical_crossentropy` vs `categorical_crossentropy`.** Use `sparse_categorical_crossentropy` when labels are integers (e.g., `[0, 3, 7]`). Use `categorical_crossentropy` when labels are one-hot encoded (e.g., `[0,0,0,1,0,0,0,0,0,0]`). CIFAR-10 from `keras.datasets` gives integer labels.

**Tip 4 — `model.summary()` is your map.** The output shape column in `model.summary()` tells you the tensor shape after each layer. Practice reading it to verify your architecture is correct before training.

**Tip 5 — The Flatten transition.** Before a `Dense` layer, you must either `Flatten()` or use `GlobalAveragePooling2D()`. Forgetting this step produces a shape incompatibility error that the exam frequently tests.

**Tip 6 — Normalization before training.** Always normalize pixel values to `[0, 1]` or `[-1, 1]` by dividing by 255.0 (or using a `Rescaling` layer). Un-normalized inputs cause slow convergence and instability.

---

## 8. Common Errors and Fixes

| Error | Cause | Fix |
|---|---|---|
| `ValueError: Input 0 is incompatible` | Wrong `input_shape` format | Ensure shape is `(H, W, C)` including channels |
| `ValueError: Shapes not compatible` | Missing Flatten before Dense | Add `Flatten()` or `GlobalAveragePooling2D()` |
| Low accuracy, slow convergence | Un-normalized inputs | Divide by `255.0` before `model.fit()` |
| Overfitting (train acc >> val acc) | No regularization | Add `Dropout`, `BatchNormalization`, augmentation |
| IndexError in feature map extraction | Wrong layer name | Use `model.layers[i].name` to find correct name |

---

## 9. Study Checklist

Work through each item before attempting the quiz.

- [ ] Write the formula for Conv2D output size from memory and verify it against the table in Section 2.

- [ ] Calculate the parameter count for a `Conv2D(64, (3,3))` layer receiving a `(16,16,32)` input.

- [ ] Build and train the CIFAR-10 CNN from Section 4 in a notebook; confirm `model.summary()` output matches the dimension table.

- [ ] Visualize feature maps from at least two different layers and describe what each appears to detect.

- [ ] Identify the difference between `padding='same'` and `padding='valid'` by inspecting output shapes.

- [ ] Review the six exam tips and verify you can recall each one without looking.

- [ ] Complete the Module 07 Lab.

- [ ] Proceed to the Module 07 Quiz.

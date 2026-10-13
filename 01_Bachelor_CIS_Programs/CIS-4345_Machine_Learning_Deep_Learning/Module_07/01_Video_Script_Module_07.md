# Video Script: Module 07 — Convolutional Neural Networks

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: TensorFlow Developer Certificate

---

## SEGMENT 1 — Introduction and Motivation (0:00–2:30)

Welcome back, everyone. I'm Professor Nash, and today we're diving into one of the most transformative ideas in modern machine learning: **Convolutional Neural Networks**, or CNNs.

Before CNNs, if you wanted to classify an image using a neural network, you would flatten the image — a `28 x 28` pixel photo becomes 784 individual numbers — and feed that into a dense network. That works for simple cases. But for a `224 x 224` color image, you suddenly have `224 * 224 * 3 = 150,528` inputs. And the first hidden layer alone would need tens of millions of parameters. Dense networks simply do not scale to images.

CNNs solve this elegantly by exploiting **spatial structure**. The key insight is that a cat's ear looks like a cat's ear whether it appears in the top-left or bottom-right of a photo. We don't need separate weights to detect every feature at every location. We learn one filter — and slide it across the entire image.

By the end of this video you will be able to:

- Describe the architecture of a CNN and the role of each layer type.

- Explain how convolution, pooling, and flattening transform an input image.

- Build and train a CNN in Keras for image classification.

- Interpret feature maps and understand what filters learn.

Let's get started.

---

## SEGMENT 2 — The Convolution Operation (2:30–6:00)

### What Is a Filter?

A **filter** (also called a kernel) is a small matrix of learnable weights — typically `3x3` or `5x5`. During the forward pass, we slide this filter across the input image, computing a dot product at each position.

Imagine our filter is a `3x3` matrix:

```
[ 1  0 -1 ]
[ 2  0 -2 ]
[ 1  0 -1 ]
```

This is actually a Sobel edge-detection filter. When you slide it across a grayscale image, regions where pixel values change sharply — edges — produce large activations. Flat regions produce values near zero.

Here is the mechanics: at each position, you multiply the filter values element-wise with the overlapping patch of the image, then sum all nine products into a single number. That number goes into the corresponding position of the **feature map** (also called an activation map).

### Stride and Padding

Two important hyperparameters control how the filter moves.

**Stride** is how many pixels the filter moves at each step. A stride of 1 moves one pixel at a time; a stride of 2 skips every other pixel, halving the spatial dimensions of the output.

**Padding** addresses what happens at the edges. With `padding='valid'`, the filter never goes outside the image, so the output is slightly smaller. With `padding='same'`, we add zeros around the border so the output has the same spatial dimensions as the input.

### Output Size Formula

For an input of size `H x W`, filter size `F x F`, stride `S`, and padding `P`, the output height is `(H - F + 2*P) / S + 1`.

For a `28 x 28` image, a `3x3` filter, stride 1, valid padding: output = `(28 - 3 + 0) / 1 + 1 = 26`. So we get a `26 x 26` feature map from one filter.

### Multiple Filters Create Depth

A convolutional layer doesn't use just one filter — it uses many. If we apply 32 filters to a `28x28` grayscale image, we get an output of shape `26 x 26 x 32`. Each of the 32 feature maps represents a different learned pattern.

---

## SEGMENT 3 — Pooling Layers (6:00–8:30)

After convolution, we typically apply a **pooling layer**. The most common type is **max pooling** with a `2x2` window and stride 2.

Max pooling takes a `2x2` region of the feature map and keeps only the maximum value. This does three things:

1. Reduces spatial dimensions by half (saves computation).

2. Provides a degree of **translation invariance** — if the feature shifts by one pixel, the max value is likely still captured.

3. Reduces overfitting by discarding precise spatial information.

Average pooling takes the mean instead of the maximum. It is less common in image classification but useful in some architectures.

### Global Average Pooling

Modern architectures like MobileNet use **global average pooling** instead of fully connected layers at the end. Instead of a `2x2` window, it averages an entire feature map into a single number. This dramatically reduces parameters.

```
Feature map: 7 x 7 x 512  →  Global Avg Pool  →  1 x 1 x 512  →  flatten  →  512 values
```

---

## SEGMENT 4 — Full CNN Architecture (8:30–12:00)

Let's look at the classic pattern:

```
Input → [Conv2D → ReLU → MaxPool] x N → Flatten → Dense → Softmax
```

Each `Conv2D → ReLU → MaxPool` block is a **feature extraction stage**. Early layers learn low-level features — edges, corners, color gradients. Later layers combine these into higher-level concepts — textures, parts of objects, whole objects.

Here is a complete CNN in Keras for classifying the CIFAR-10 dataset (10 classes, `32x32` color images):

```python
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    # Block 1
    keras.layers.Conv2D(32, (3, 3), activation='relu',
                        padding='same', input_shape=(32, 32, 3)),
    keras.layers.MaxPooling2D((2, 2)),

    # Block 2
    keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    keras.layers.MaxPooling2D((2, 2)),

    # Block 3
    keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
    keras.layers.MaxPooling2D((2, 2)),

    # Classifier head
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()
```

Let me walk through what each block is doing.

**Block 1**: 32 filters of size `3x3`. Input is `32x32x3`. Output after conv (same padding) is `32x32x32`. After max pooling: `16x16x32`.

**Block 2**: 64 filters. Input `16x16x32`, output `16x16x64`. After pooling: `8x8x64`.

**Block 3**: 128 filters. Input `8x8x64`, output `8x8x128`. After pooling: `4x4x128`.

**Flatten**: `4 * 4 * 128 = 2,048` values.

**Dense(128)**: Fully connected layer — combines all extracted features.

**Dense(10, softmax)**: Output probabilities for 10 classes.

Why do we increase filter counts (32 to 64 to 128) as we go deeper? Spatial dimensions shrink, so we compensate by increasing depth — maintaining representational capacity while reducing computation.

---

## SEGMENT 5 — Parameter Count and Efficiency (12:00–14:30)

Let's compare parameter counts.

A dense layer from `32*32*3 = 3,072` inputs to 128 hidden units needs `3,072 * 128 + 128 = 393,344` parameters.

Our entire first Conv2D layer with 32 filters of `3x3` on a 3-channel input: `3*3*3*32 + 32 = 896` parameters. Same job, roughly 439 times fewer parameters.

This is the power of **parameter sharing**. The same filter weights apply everywhere in the image. This is not just efficiency — it's a powerful inductive bias that says: features are location-independent.

---

## SEGMENT 6 — Training a CNN (14:30–17:30)

Let's load CIFAR-10 and train:

```python
# Load and preprocess data
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

# Normalize to [0, 1]
x_train = x_train.astype('float32') / 255.0
x_test  = x_test.astype('float32')  / 255.0

# Train
history = model.fit(
    x_train, y_train,
    epochs=20,
    batch_size=64,
    validation_split=0.1
)
```

Expected output after 20 epochs: roughly 75–80% validation accuracy on CIFAR-10 with this architecture. Not state-of-the-art, but a solid baseline.

### Visualizing Feature Maps

To understand what the CNN learned, let's visualize the feature maps from the first conv layer:

```python
import numpy as np
import matplotlib.pyplot as plt

# Build a model that outputs the first conv layer's activations
feature_model = keras.Model(
    inputs=model.input,
    outputs=model.layers[0].output
)

# Pick one test image
sample = x_test[0:1]
feature_maps = feature_model.predict(sample)  # Shape: (1, 32, 32, 32)

# Plot first 16 feature maps
fig, axes = plt.subplots(4, 4, figsize=(8, 8))
for i, ax in enumerate(axes.flat):
    ax.imshow(feature_maps[0, :, :, i], cmap='viridis')
    ax.axis('off')
plt.suptitle("Feature Maps — Conv Layer 1")
plt.tight_layout()
plt.show()
```

You will see that different filters activate on different visual patterns — some respond to horizontal edges, some to colors, some to diagonal lines. This is emergent behavior; we never told the network what to look for.

---

## SEGMENT 7 — Batch Normalization and Best Practices (17:30–20:00)

Modern CNNs almost always include **Batch Normalization** between the convolution and activation:

```python
keras.layers.Conv2D(64, (3, 3), padding='same'),
keras.layers.BatchNormalization(),
keras.layers.Activation('relu'),
keras.layers.MaxPooling2D((2, 2)),
```

Batch normalization normalizes the activations of each layer, which:

- Allows higher learning rates.

- Reduces sensitivity to weight initialization.

- Acts as a mild regularizer.

### Learning Rate Scheduling

Adding a learning rate scheduler improves convergence:

```python
lr_schedule = keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=3,
    min_lr=1e-6
)

model.fit(
    x_train, y_train,
    epochs=30,
    callbacks=[lr_schedule]
)
```

---

## SEGMENT 8 — Production-Style Pipeline (20:00–22:30)

Here is a complete production-style build function:

```python
def build_cnn(input_shape=(32, 32, 3), num_classes=10):
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

        # Classifier
        keras.layers.Flatten(),
        keras.layers.Dense(256, activation='relu'),
        keras.layers.BatchNormalization(),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(num_classes, activation='softmax')
    ])
    return model
```

Notice the pattern: Conv then BatchNorm then ReLU then Pool then Dropout. This is the standard template you will see across production CNN implementations.

---

## SEGMENT 9 — Wrap-Up and TF Certificate Alignment (22:30–24:00)

Let's recap what we covered today:

- Convolution slides learnable filters across images to produce feature maps.

- Pooling reduces spatial dimensions and provides translation invariance.

- CNN architectures stack these blocks, increasing filter depth while reducing spatial size.

- Parameter sharing makes CNNs vastly more efficient than dense networks for images.

- Batch normalization and dropout are standard regularization tools.

For the TensorFlow Developer Certificate exam, you should be able to build a CNN from scratch using `keras.Sequential`, compile it with appropriate loss and optimizer, and achieve reasonable accuracy on standard datasets.

Next module, we will discuss **data augmentation** — how to artificially expand your training dataset and improve generalization even further.

See you then.

---

*End of Script — Module 07*

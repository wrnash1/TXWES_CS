# Lab 07 — Convolutional Neural Networks: CIFAR-10 Image Classifier

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Objective

By the end of this lab you will be able to:

- Build a multi-block CNN using `keras.Sequential` with Conv2D, MaxPooling2D, BatchNormalization, and Dropout layers.

- Train the model on CIFAR-10 and achieve at least **72% validation accuracy**.

- Visualize training history and interpret overfitting vs. underfitting curves.

- Extract and display feature maps from a trained convolutional layer.

- Count parameters from a `model.summary()` output and explain why CNNs are more efficient than dense networks for images.

---

## Prerequisites

- Python 3.8+ with TensorFlow 2.x installed (`pip install tensorflow matplotlib numpy`).

- A Jupyter Notebook or Google Colab environment is recommended.

- You have completed the Module 07 Video Script and Reading Guide.

---

## Starter Code

Copy the following starter code into a new notebook. Each section has a `# TODO` comment where you must add your implementation.

```python
# Lab 07 Starter Code
# CIS-4345 Machine Learning and Deep Learning
# Texas Wesleyan University

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

print("TensorFlow version:", tf.__version__)

# -------------------------------------------------------
# STEP 1: Load and Preprocess CIFAR-10
# -------------------------------------------------------
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# TODO 1a: Normalize pixel values from [0, 255] to [0.0, 1.0]
# x_train = ...
# x_test  = ...

print(f"Train shape: {x_train.shape}, Test shape: {x_test.shape}")

# -------------------------------------------------------
# STEP 2: Visualize Sample Images
# -------------------------------------------------------
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(x_train[i])
    ax.set_title(class_names[int(y_train[i])])
    ax.axis('off')
plt.suptitle("CIFAR-10 Sample Images")
plt.tight_layout()
plt.show()

# -------------------------------------------------------
# STEP 3: Build the CNN
# -------------------------------------------------------
# TODO 3a: Build a CNN with exactly the following architecture:
#   Block 1: Conv2D(32, 3x3, same) -> BatchNorm -> ReLU -> MaxPool(2x2) -> Dropout(0.25)
#   Block 2: Conv2D(64, 3x3, same) -> BatchNorm -> ReLU -> MaxPool(2x2) -> Dropout(0.25)
#   Block 3: Conv2D(128, 3x3, same) -> BatchNorm -> ReLU -> MaxPool(2x2) -> Dropout(0.25)
#   Head:    Flatten -> Dense(256, relu) -> BatchNorm -> Dropout(0.5) -> Dense(10, softmax)

model = keras.Sequential([
    # Block 1 — TODO: fill in
    # Block 2 — TODO: fill in
    # Block 3 — TODO: fill in
    # Head    — TODO: fill in
])

# -------------------------------------------------------
# STEP 4: Compile the Model
# -------------------------------------------------------
# TODO 4a: Compile with Adam optimizer, sparse_categorical_crossentropy, accuracy metric
model.compile(
    # optimizer=...
    # loss=...
    # metrics=...
)

model.summary()

# -------------------------------------------------------
# STEP 5: Define Callbacks and Train
# -------------------------------------------------------
# TODO 5a: Add EarlyStopping (patience=5, monitor='val_accuracy', restore_best_weights=True)
# TODO 5b: Add ReduceLROnPlateau (monitor='val_loss', factor=0.5, patience=3)
callbacks = [
    # TODO: fill in
]

history = model.fit(
    x_train, y_train,
    epochs=40,
    batch_size=64,
    validation_split=0.1,
    callbacks=callbacks,
    verbose=1
)

# -------------------------------------------------------
# STEP 6: Evaluate and Plot History
# -------------------------------------------------------
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\nTest Accuracy: {test_acc:.4f}  |  Test Loss: {test_loss:.4f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(history.history['accuracy'],     label='Train Accuracy')
ax1.plot(history.history['val_accuracy'], label='Val Accuracy')
ax1.set_title('Training vs Validation Accuracy')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Accuracy')
ax1.legend()

ax2.plot(history.history['loss'],     label='Train Loss')
ax2.plot(history.history['val_loss'], label='Val Loss')
ax2.set_title('Training vs Validation Loss')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss')
ax2.legend()

plt.tight_layout()
plt.show()

# -------------------------------------------------------
# STEP 7: Feature Map Visualization
# -------------------------------------------------------
# TODO 7a: Build a sub-model that outputs the activation of the FIRST Conv2D layer
# TODO 7b: Pass x_test[0:1] through the sub-model
# TODO 7c: Display the first 16 feature maps in a 4x4 grid

# activation_model = keras.Model(inputs=model.input, outputs=...)
# feature_maps = activation_model.predict(x_test[0:1])

# -------------------------------------------------------
# STEP 8: Predictions and Confusion Matrix
# -------------------------------------------------------
# TODO 8a: Generate predictions on x_test
# TODO 8b: Print a classification report using sklearn

from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# y_pred = ...
# print(classification_report(y_test, y_pred, target_names=class_names))

# TODO 8c: Plot confusion matrix as a heatmap
```

---

## Step-by-Step Instructions

### Step 1 — Load and Preprocess

Complete `TODO 1a`. Divide `x_train` and `x_test` by `255.0` and cast to `float32`. Verify the print statement shows shapes `(50000, 32, 32, 3)` and `(10000, 32, 32, 3)`.

**Expected output:**

```
Train shape: (50000, 32, 32, 3), Test shape: (10000, 32, 32, 3)
```

### Step 2 — Visualize Samples

Run the visualization cell. Confirm you see a `2x5` grid of color images with correct class name labels. This verifies the data loaded correctly.

### Step 3 — Build the CNN

Complete `TODO 3a`. Follow the architecture specification exactly. Key rules:

- Use `padding='same'` on all Conv2D layers.

- Add `input_shape=(32, 32, 3)` only on the first Conv2D layer.

- Use `keras.layers.Activation('relu')` as a separate layer (not `activation='relu'` in Conv2D) so that BatchNormalization comes between the convolution and the activation.

### Step 4 — Compile

Complete `TODO 4a`. Use `optimizer=keras.optimizers.Adam(learning_rate=1e-3)`.

After running `model.summary()`, record the total parameter count in your deliverable. It should be approximately **360,000–410,000** trainable parameters.

### Step 5 — Train

Complete `TODO 5a` and `TODO 5b`. Training will run up to 40 epochs but should stop early. Expect training to take 3–8 minutes on CPU or under 2 minutes on GPU/Colab.

**Target**: validation accuracy of at least **72%** by the end of training.

### Step 6 — Evaluate and Plot

Run the evaluation and plotting cell. In your deliverable, answer:

1. What was your final test accuracy?

2. Is there a gap between train and val accuracy? What does this indicate?

3. At what epoch did EarlyStopping trigger (if at all)?

### Step 7 — Feature Map Visualization

Complete `TODO 7a` through `TODO 7c`. Build the activation sub-model using `keras.Model(inputs=model.input, outputs=model.layers[0].output)`. Display the first 16 of the 32 feature maps for one test image.

**Expected output**: A `4x4` grid of grayscale/colormap images where different filters respond to different visual patterns in the input image.

### Step 8 — Classification Report

Complete `TODO 8a` through `TODO 8c`. Generate predictions with `model.predict()`, then use `np.argmax(predictions, axis=1)` to get class indices. Print the classification report and plot the confusion matrix.

---

## Expected Outputs Summary

| Check | Expected Value |
|---|---|
| x_train shape | (50000, 32, 32, 3) |
| Total trainable params | ~360K–410K |
| Test accuracy (target) | >= 72% |
| Feature map grid | 4x4 grid, 16 filters |
| Classification report | Per-class precision/recall printed |

---

## Deliverables

Submit a single Jupyter Notebook (`.ipynb`) file to Canvas with all cells executed and outputs visible. Your notebook must include:

1. **Completed code** for all TODO sections.

2. **model.summary() output** with the exact parameter count recorded.

3. **Training/validation accuracy and loss plots** (Step 6).

4. **Feature map visualization** showing a `4x4` grid of filter activations (Step 7).

5. **Classification report and confusion matrix heatmap** (Step 8).

6. **Written responses** (in a Markdown cell) answering the three questions from Step 6.

---

## Grading Rubric (100 Points)

| Criterion | Points |
|---|---|
| Data normalization correct, shapes verified | 10 |
| CNN architecture matches specification exactly | 25 |
| Model compiles and trains without errors | 15 |
| Validation accuracy >= 72% achieved | 20 |
| Feature map visualization correct (4x4 grid) | 15 |
| Classification report and confusion matrix present | 10 |
| Written reflection answers three questions thoughtfully | 5 |

**Total: 100 points**

---

## Troubleshooting Guide

**Error: `ValueError: Input 0 is incompatible with layer`**

Your `input_shape` is likely missing the channel dimension. For CIFAR-10 use `input_shape=(32, 32, 3)`, not `(32, 32)`.

**Error: `ValueError: Shapes are incompatible`**

You likely connected a Conv2D block directly to a Dense layer without `Flatten()` or `GlobalAveragePooling2D()` in between.

**Test accuracy stuck below 50%**

Verify normalization was applied — check that `x_train.max()` returns `1.0`, not `255.0`. Also verify the optimizer and loss function are set correctly.

**Training is extremely slow**

Switch to Google Colab (Runtime > Change runtime type > GPU). CPU training for 40 epochs on CIFAR-10 takes approximately 6–10 minutes, which is acceptable.

---

## Part 9 — Challenge Exercise

### Challenge 1: Depthwise Separable Convolutions vs Standard Convolutions

Replace each standard `Conv2D` block in your trained model with a depthwise separable equivalent using Keras's `SeparableConv2D` layer, then compare parameter counts and accuracy.

1. Create a second model `model_sep` by replacing every `Conv2D` call with `keras.layers.SeparableConv2D` using identical filter counts, kernel sizes, and padding. Keep BatchNorm, ReLU, MaxPooling, and Dropout unchanged.
2. Call `model_sep.summary()` and record the total parameter count. Compare it to your original model's parameter count — separable convolutions should reduce parameters by roughly 8–9x per layer.
3. Train `model_sep` with the same hyperparameters and callbacks. Record the final validation accuracy and training time. Plot the accuracy curves for both models on the same axes.
4. In a Markdown cell, explain why `SeparableConv2D` uses fewer parameters and discuss the accuracy/efficiency tradeoff you observed.

```python
# Hint: replace Conv2D blocks with SeparableConv2D
keras.layers.SeparableConv2D(32, (3, 3), padding='same', use_bias=False),
keras.layers.BatchNormalization(),
keras.layers.Activation('relu'),
keras.layers.MaxPooling2D((2, 2)),
keras.layers.Dropout(0.25),
```

### Challenge 2: Visualizing Filters and Maximally Activating Inputs

Instead of only visualizing feature maps (what a filter produces), directly inspect what each filter has learned by visualizing the filter weights themselves.

1. Extract the weights of the first `Conv2D` layer using `weights, biases = model.layers[0].get_weights()`. The `weights` array has shape `(3, 3, 3, 32)` — 32 filters of shape `(3, 3, 3)`.
2. Normalize each filter to `[0, 1]` for display: `f = (f - f.min()) / (f.max() - f.min() + 1e-8)`. Display all 32 filters in a `4x8` grid using `plt.imshow(filter_weights[:,:,:])` (RGB filters display as color patches).
3. Compare the filter visualization from an untrained (randomly initialized) model vs your trained model. Run the following before training a fresh model:

```python
untrained_model = build_cifar_cnn()
untrained_weights = untrained_model.layers[0].get_weights()[0]
```

4. Identify at least two filters in the trained model that appear to detect specific visual patterns (e.g., edges in a particular direction, color blobs). Annotate your grid with titles describing what each selected filter appears to detect.

### Reflection Questions

1. After replacing `Conv2D` with `SeparableConv2D`, did your model's validation accuracy drop, stay the same, or improve? What does this suggest about the original model's parameter efficiency, and in what deployment scenario would you choose separable convolutions despite any accuracy tradeoff?
2. Comparing the filter visualizations of the untrained vs trained model, describe the structural change you observe. What does this tell you about what gradient descent "teaches" a convolutional filter, and why do trained filters often resemble Gabor filters or color-opponent detectors found in the biological visual system?

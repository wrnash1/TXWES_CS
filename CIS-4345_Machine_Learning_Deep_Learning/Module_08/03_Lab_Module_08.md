# Lab: Module 08 — Data Augmentation and Image Preprocessing

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Overview

In this lab you will build two image classification pipelines for the Cats vs. Dogs dataset: one with no augmentation and one with full augmentation and class-weight handling. You will compare their validation accuracy curves to measure the regularization effect of augmentation.

**Estimated time:** 75–90 minutes

**Environment:** Google Colab (recommended) or local Python 3.9+ environment with TensorFlow 2.12+

---

## Learning Outcomes

After completing this lab you will be able to:

- Configure `ImageDataGenerator` for training and validation splits
- Build a `tf.data` pipeline with normalization, augmentation, cache, shuffle, and prefetch
- Embed Keras preprocessing layers inside a model graph
- Apply `class_weight` to handle imbalanced class distributions
- Interpret training/validation accuracy curves to diagnose overfitting

---

## Setup

### Part A — Install Dependencies and Download Data

```python
# Run this cell first in Colab or your local environment
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import zipfile
import urllib.request

print(f"TensorFlow version: {tf.__version__}")

# Download a subset of Cats vs. Dogs
URL = "https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip"
zip_path = "cats_and_dogs_filtered.zip"

if not os.path.exists(zip_path):
    urllib.request.urlretrieve(URL, zip_path)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(".")

BASE_DIR = "cats_and_dogs_filtered"
TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR   = os.path.join(BASE_DIR, "validation")

# Inspect the directory structure
for split in ["train", "validation"]:
    for cls in ["cats", "dogs"]:
        path = os.path.join(BASE_DIR, split, cls)
        count = len(os.listdir(path))
        print(f"{split}/{cls}: {count} images")
```

---

## Part 1 — Baseline Model (No Augmentation)

### Step 1.1 — Build the Data Generators

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

IMG_SIZE = (150, 150)
BATCH_SIZE = 32

# TODO: Create train_datagen with ONLY rescaling (no augmentation)
train_datagen = ImageDataGenerator(rescale=______)

# TODO: Create val_datagen with ONLY rescaling
val_datagen = ImageDataGenerator(rescale=______)

train_gen = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

val_gen = val_datagen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary'
)
```

### Step 1.2 — Define the Baseline Model

```python
def build_baseline():
    model = tf.keras.Sequential([
        # TODO: Add three Conv2D + MaxPooling2D blocks
        # Block 1: 32 filters, 3x3, relu, padding='same'
        tf.keras.layers.Conv2D(_______, _______, activation='relu',
                               padding='same', input_shape=(150, 150, 3)),
        tf.keras.layers.MaxPooling2D(),

        # Block 2: 64 filters, 3x3, relu, padding='same'
        tf.keras.layers.Conv2D(_______, _______, activation='relu', padding='same'),
        tf.keras.layers.MaxPooling2D(),

        # Block 3: 128 filters, 3x3, relu, padding='same'
        tf.keras.layers.Conv2D(_______, _______, activation='relu', padding='same'),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

baseline = build_baseline()
baseline.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
baseline.summary()
```

### Step 1.3 — Train the Baseline Model

```python
baseline_history = baseline.fit(
    train_gen,
    epochs=15,
    validation_data=val_gen,
    verbose=1
)
```

---

## Part 2 — Augmented Model

### Step 2.1 — Build Augmented Data Generators

```python
# TODO: Fill in augmentation parameters
augmented_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=______,      # try 20
    width_shift_range=______,   # try 0.1
    height_shift_range=______,  # try 0.1
    zoom_range=______,          # try 0.15
    horizontal_flip=______,     # True
    fill_mode='nearest'
)

val_datagen_aug = ImageDataGenerator(rescale=1.0 / 255)

aug_train_gen = augmented_datagen.flow_from_directory(
    TRAIN_DIR, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode='binary'
)
aug_val_gen = val_datagen_aug.flow_from_directory(
    VAL_DIR, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode='binary'
)
```

### Step 2.2 — Define the Augmented Model

```python
def build_augmented_model():
    inputs = tf.keras.Input(shape=(150, 150, 3))

    # TODO: Add Keras preprocessing layers for augmentation
    x = tf.keras.layers.RandomFlip("horizontal")(inputs)
    x = tf.keras.layers.RandomRotation(______)(x)   # fraction of 2*pi; try 0.1
    x = tf.keras.layers.RandomZoom(______)(x)        # try 0.15

    # Rescaling embedded in the model
    x = tf.keras.layers.Rescaling(1.0 / 255)(x)

    x = tf.keras.layers.Conv2D(32, 3, activation='relu', padding='same')(x)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same')(x)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.Conv2D(128, 3, activation='relu', padding='same')(x)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(256, activation='relu')(x)
    x = tf.keras.layers.Dropout(0.4)(x)
    outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)

    return tf.keras.Model(inputs, outputs)

aug_model = build_augmented_model()
aug_model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
aug_model.summary()
```

### Step 2.3 — Train the Augmented Model

```python
aug_history = aug_model.fit(
    aug_train_gen,
    epochs=15,
    validation_data=aug_val_gen,
    verbose=1
)
```

---

## Part 3 — tf.data Pipeline

### Step 3.1 — Build a tf.data Pipeline from Scratch

```python
AUTOTUNE = tf.data.AUTOTUNE

# Load using the high-level utility
raw_train = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMG_SIZE,
    batch_size=None,       # unbatched so we can map per-image
    label_mode='binary',
    shuffle=True,
    seed=42
)

raw_val = tf.keras.utils.image_dataset_from_directory(
    VAL_DIR,
    image_size=IMG_SIZE,
    batch_size=None,
    label_mode='binary',
    shuffle=False
)

# TODO: Complete the normalize function
def normalize(image, label):
    image = tf.cast(image, tf.float32) / ______
    return image, label

# TODO: Complete the augment function using tf.image operations
def augment_fn(image, label):
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_brightness(image, max_delta=______)  # try 0.2
    image = tf.image.random_contrast(image, lower=______, upper=______)  # try 0.8, 1.2
    return image, label

# TODO: Build the full pipeline with all 6 stages
train_ds = (
    raw_train
    .map(______, num_parallel_calls=AUTOTUNE)   # normalize
    .map(______, num_parallel_calls=AUTOTUNE)   # augment
    .cache()
    .shuffle(buffer_size=______)                # try 500
    .batch(BATCH_SIZE)
    .prefetch(______)                           # AUTOTUNE
)

val_ds = (
    raw_val
    .map(normalize, num_parallel_calls=AUTOTUNE)
    .cache()
    .batch(BATCH_SIZE)
    .prefetch(AUTOTUNE)
)

print("Pipeline built. Verifying shape...")
for images, labels in train_ds.take(1):
    print(f"Batch shape: {images.shape}, labels shape: {labels.shape}")
```

---

## Part 4 — Class Imbalance Experiment

### Step 4.1 — Simulate Imbalance and Apply class_weight

```python
# Create an artificially imbalanced dataset by taking more cats than dogs
cats_dir = os.path.join(TRAIN_DIR, "cats")
dogs_dir = os.path.join(TRAIN_DIR, "dogs")

cat_files = [os.path.join(cats_dir, f) for f in os.listdir(cats_dir)]
dog_files  = [os.path.join(dogs_dir,  f) for f in os.listdir(dogs_dir)]

# Use all cats but only 20% of dogs
imbalanced_files  = cat_files + dog_files[:len(dog_files) // 5]
imbalanced_labels = [0] * len(cat_files) + [1] * (len(dog_files) // 5)

print(f"Cats: {len(cat_files)}, Dogs (subset): {len(dog_files) // 5}")

# TODO: Compute class weights
total = len(imbalanced_labels)
n_cats = imbalanced_labels.count(0)
n_dogs = imbalanced_labels.count(1)

# Formula: weight_for_class = total / (n_classes * count_for_class)
weight_cats = total / (2 * n_cats)
weight_dogs = total / (2 * n_dogs)

class_weight_dict = {0: weight_cats, 1: weight_dogs}
print(f"Class weights: {class_weight_dict}")

# Train a small model with class_weight
imbalanced_model = build_baseline()
imbalanced_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Use the standard generators but pass class_weight to fit()
imbalanced_history = imbalanced_model.fit(
    train_gen,
    epochs=10,
    validation_data=val_gen,
    class_weight=class_weight_dict,
    verbose=1
)
```

---

## Part 5 — Visualization and Analysis

### Step 5.1 — Plot Accuracy Curves

```python
def plot_history(histories, names):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for hist, name in zip(histories, names):
        axes[0].plot(hist.history['accuracy'],     label=f"{name} train")
        axes[0].plot(hist.history['val_accuracy'], label=f"{name} val", linestyle='--')
        axes[1].plot(hist.history['loss'],         label=f"{name} train")
        axes[1].plot(hist.history['val_loss'],     label=f"{name} val", linestyle='--')

    axes[0].set_title("Accuracy")
    axes[0].set_xlabel("Epoch")
    axes[0].legend()

    axes[1].set_title("Loss")
    axes[1].set_xlabel("Epoch")
    axes[1].legend()

    plt.tight_layout()
    plt.savefig("module08_results.png", dpi=120)
    plt.show()

plot_history(
    [baseline_history, aug_history],
    ["Baseline (no aug)", "Augmented"]
)
```

---

## Deliverables

Submit the following to Canvas:

1. Your completed Jupyter notebook (`.ipynb`) with all cells executed and outputs visible.
2. The saved plot `module08_results.png` showing both accuracy curves.
3. A written response (150–200 words) answering:
   - What was the final validation accuracy gap between baseline and augmented models?
   - At which epoch did the baseline model begin to clearly overfit?
   - Did `class_weight` improve performance on the imbalanced experiment? Cite specific accuracy numbers.

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Part 1 baseline model trains without errors | 15 |
| Part 2 augmented generators and model configured correctly | 20 |
| Part 3 tf.data pipeline with all 6 stages complete | 20 |
| Part 4 class weights computed and applied correctly | 15 |
| Part 5 plots generated and saved | 10 |
| Written analysis with specific accuracy numbers | 20 |
| **Total** | **100** |

---

Texas Wesleyan University — CIS-4345 Machine Learning and Deep Learning

Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.

---

## Part 9 — Challenge Exercise

### Challenge 1: MixUp Augmentation from Scratch

Implement MixUp augmentation manually inside the `tf.data` pipeline and compare it against standard augmentation.

1. Build a MixUp function that operates on a batched dataset. After calling `.batch(32)`, apply the following map function. Use `ds_train = ds_train.batch(32).map(mixup)`. Since MixUp produces soft labels, set `loss=tf.keras.losses.BinaryCrossentropy(label_smoothing=0.0)`.

   ```python
   def mixup(images, labels, alpha=0.2):
       batch_size = tf.shape(images)[0]
       lam = tf.random.uniform(shape=[], minval=0.0, maxval=alpha)
       indices = tf.random.shuffle(tf.range(batch_size))
       images_mixed = lam * images + (1 - lam) * tf.gather(images, indices)
       labels_a = tf.cast(labels, tf.float32)
       labels_b = tf.cast(tf.gather(labels, indices), tf.float32)
       labels_mixed = lam * labels_a + (1 - lam) * labels_b
       return images_mixed, labels_mixed
   ```

2. Train the MixUp model for 20 epochs and record validation accuracy. Plot its accuracy curve alongside the standard augmentation model from Part 2.
3. In a Markdown cell, explain why MixUp can improve generalization even when the model never sees a "pure" image during training.

### Challenge 2: Learning Rate Finder

Implement a manual learning rate range test to identify the optimal learning rate for your CNN.

1. Train a freshly initialized model for 100 steps while exponentially increasing the learning rate from `1e-7` to `1e-1` using a `LearningRateScheduler` callback. Record the loss at each step using a custom callback or by inspecting `history.history['loss']`.

   ```python
   import numpy as np

   def lr_schedule(epoch, lr):
       return 1e-7 * (1e6 ** (epoch / 100))

   lr_finder_cb = tf.keras.callbacks.LearningRateScheduler(lr_schedule)
   ```

2. Plot learning rate (log scale on x-axis) vs. training loss (y-axis). The optimal learning rate is typically just before the loss reaches its minimum — the steepest descent region.
3. Retrain your augmented model using the identified optimal learning rate and compare final validation accuracy to the model trained with `lr=1e-3`.
4. In a Markdown cell, explain the concept of the "loss landscape" and why finding the right learning rate matters more for small datasets than for large ones.

### Reflection Questions

1. After applying MixUp augmentation, did your model's validation accuracy improve, stay the same, or decrease compared to standard augmentation? Propose a hypothesis for why MixUp may or may not be well-suited for binary image classification with a small dataset.
2. Based on your learning rate range test, what visual signal in the loss-vs-LR plot tells you the learning rate is too large? What does a too-small learning rate look like in the same plot, and why does this matter for choosing a starting point for training?

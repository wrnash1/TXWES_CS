# Reading Guide: Module 08 — Data Augmentation and Image Preprocessing

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Learning Objectives

By the end of this module you will be able to:

1. Explain why data augmentation reduces overfitting in image models.
2. Configure `ImageDataGenerator` with multiple augmentation parameters.
3. Build a performant `tf.data` pipeline with map, cache, shuffle, and prefetch.
4. Apply normalization and standardization to image tensors.
5. Implement augmentation using Keras preprocessing layers inside a model.
6. Address class imbalance using `class_weight` and dataset resampling.

---

## Section 1 — The Case for Data Augmentation

### Why More Data Beats More Parameters

Convolutional neural networks learn spatial hierarchies of features. Given enough unique examples, they generalize well. The problem is that acquiring labeled image data is expensive and time-consuming. Augmentation solves this by generating synthetic variations of existing images at training time.

The core insight is that many real-world image variations are semantically irrelevant: a dog photographed from slightly to the left is still a dog. By exposing the model to these variations, we teach it invariance — the ability to recognize objects despite minor transformations.

### What Augmentation Prevents

Without augmentation, a model trained on a limited dataset will memorize the specific pixel patterns in the training images. The symptom is a large gap between training accuracy and validation accuracy. This is overfitting, and augmentation is one of the most effective regularization techniques available for image data.

Augmentation works alongside other regularizers like Dropout and L2 weight decay. They address different aspects of the same problem: augmentation increases the effective diversity of the training distribution, while Dropout and weight decay reduce model complexity.

---

## Section 2 — ImageDataGenerator

### Basic Configuration

`ImageDataGenerator` is the original Keras image augmentation API. It operates as a Python generator, yielding batches of augmented images on demand. The augmentation is applied on-the-fly using CPU threads while the GPU trains.

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.15,
    horizontal_flip=True,
    fill_mode='nearest'
)
```

### Key Parameters Explained

| Parameter | Type | Description |
|---|---|---|
| `rescale` | float | Multiplier applied to pixel values. Use `1.0/255` to map [0,255] to [0,1]. |
| `rotation_range` | int (degrees) | Maximum rotation angle in either direction. |
| `width_shift_range` | float (0–1) | Maximum horizontal translation as fraction of total width. |
| `height_shift_range` | float (0–1) | Maximum vertical translation as fraction of total height. |
| `shear_range` | float | Shear intensity in counter-clockwise direction. |
| `zoom_range` | float or [lower, upper] | Range for random zoom. |
| `horizontal_flip` | bool | Randomly flip images left-right. |
| `vertical_flip` | bool | Randomly flip images up-down. |
| `brightness_range` | [lower, upper] | Range for random brightness adjustment. |
| `fill_mode` | str | How to fill pixels after rotation or shift. |

### Separate Generators for Train and Validation

Always use a separate generator for validation data that applies only rescaling:

```python
# Training generator — augmentation + rescaling
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    horizontal_flip=True,
    zoom_range=0.15
)

# Validation generator — rescaling ONLY
val_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_gen = train_datagen.flow_from_directory(
    'data/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

val_gen = val_datagen.flow_from_directory(
    'data/val',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
```

### flow_from_directory vs flow

`flow_from_directory` reads images from a directory structure where each subdirectory is a class. `flow` takes a NumPy array already loaded into memory. For large datasets, always prefer `flow_from_directory` to avoid loading everything into RAM.

---

## Section 3 — tf.data Pipelines

### The Pipeline Architecture

A `tf.data` pipeline is a sequence of lazy transformations applied to a dataset. "Lazy" means no data is processed until the model requests a batch. This architecture allows TensorFlow to overlap CPU preprocessing with GPU training.

The canonical pipeline order is:

```text
load → decode → normalize → augment → cache → shuffle → batch → prefetch
```

```python
import tensorflow as tf

AUTOTUNE = tf.data.AUTOTUNE

def load_and_preprocess(path, label):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [224, 224])
    image = tf.cast(image, tf.float32) / 255.0
    return image, label

def augment(image, label):
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_brightness(image, max_delta=0.2)
    image = tf.image.random_contrast(image, lower=0.8, upper=1.2)
    return image, label

dataset = tf.data.Dataset.from_tensor_slices((file_paths, labels))

train_ds = (
    dataset
    .map(load_and_preprocess, num_parallel_calls=AUTOTUNE)
    .map(augment, num_parallel_calls=AUTOTUNE)
    .cache()
    .shuffle(buffer_size=500)
    .batch(32)
    .prefetch(AUTOTUNE)
)
```

### Pipeline Stage Responsibilities

| Stage | Purpose | Notes |
|---|---|---|
| `.map(load_and_preprocess)` | Decode files, resize, normalize | CPU-bound; parallelize with `AUTOTUNE` |
| `.map(augment)` | Apply random transformations | Must come after normalization |
| `.cache()` | Store decoded images in memory | Place after expensive ops, before shuffle |
| `.shuffle(buffer_size)` | Randomize order each epoch | Buffer size trades memory for randomness |
| `.batch(n)` | Group into mini-batches | Usually after shuffle |
| `.prefetch(AUTOTUNE)` | Prepare next batch while GPU trains | Always the last stage |

### image_dataset_from_directory

For directory-based datasets, `tf.keras.utils.image_dataset_from_directory` creates a `tf.data.Dataset` automatically:

```python
train_ds = tf.keras.utils.image_dataset_from_directory(
    'data/train',
    image_size=(224, 224),
    batch_size=32,
    label_mode='categorical',
    shuffle=True,
    seed=42
)
```

This is the preferred high-level API when your data is organized in class subdirectories.

---

## Section 4 — Normalization Techniques

### Comparison of Normalization Methods

| Method | Formula | Range | Best For |
|---|---|---|---|
| Min-Max (rescaling) | `pixel / 255.0` | [0, 1] | General use; simple and predictable |
| Standardization | `(pixel - mean) / std` | ~[-3, 3] | When pixel distribution varies across datasets |
| ImageNet preprocess | Model-specific | Varies | Transfer learning with pretrained models |
| Tanh normalization | `pixel / 127.5 - 1` | [-1, 1] | Some pretrained models (MobileNetV2) |

### Keras Normalization Layer

The `Normalization` layer computes mean and variance from training data using `adapt()`:

```python
normalization_layer = tf.keras.layers.Normalization(axis=-1)

# adapt() computes mean and variance from training data
normalization_layer.adapt(train_ds.map(lambda x, y: x))

model = tf.keras.Sequential([
    normalization_layer,
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
])
```

### Rescaling Layer

For simple [0, 1] normalization:

```python
rescaling_layer = tf.keras.layers.Rescaling(scale=1.0/255, offset=0.0)
```

For the MobileNetV2 / MobileNetV3 range of [-1, 1]:

```python
rescaling_layer = tf.keras.layers.Rescaling(scale=1.0/127.5, offset=-1.0)
```

---

## Section 5 — Augmentation with Keras Preprocessing Layers

### Available Layers (TensorFlow 2.x)

| Layer | Key Parameter | Effect |
|---|---|---|
| `RandomFlip` | `"horizontal"`, `"vertical"`, `"horizontal_and_vertical"` | Mirror the image |
| `RandomRotation` | factor (fraction of `2 * pi`) | Rotate by random angle |
| `RandomZoom` | height_factor, width_factor | Zoom in or out |
| `RandomTranslation` | height_factor, width_factor | Shift image position |
| `RandomBrightness` | factor | Adjust brightness |
| `RandomContrast` | factor | Adjust contrast |
| `RandomCrop` | height, width | Crop to fixed size |

### Embedding Augmentation in the Model

```python
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(factor=0.1),
    tf.keras.layers.RandomZoom(height_factor=0.15, width_factor=0.15),
    tf.keras.layers.RandomBrightness(factor=0.2),
    tf.keras.layers.RandomContrast(factor=0.2),
], name="augmentation_block")

inputs = tf.keras.Input(shape=(224, 224, 3))
x = data_augmentation(inputs)           # active during training only
x = tf.keras.layers.Rescaling(1.0/255)(x)
x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same')(x)
x = tf.keras.layers.MaxPooling2D()(x)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)

model = tf.keras.Model(inputs, outputs)
```

### Train-Only Behavior

Keras `Random*` preprocessing layers automatically operate in pass-through mode during inference. You do not need to pass `training=False` — calling `model.predict()` will never augment test images.

---

## Section 6 — Handling Class Imbalance

### Recognizing Imbalance

Class imbalance occurs when one class has significantly more training samples than another. In a dataset with 90% class A and 10% class B, a model that always predicts class A achieves 90% accuracy but has learned nothing about class B.

Indicators of imbalance problems:

- High overall accuracy but low recall on minority classes
- Confusion matrix shows near-zero true positives for minority classes
- Training loss decreases but validation F1 score does not improve

### Method 1 — Class Weights

```python
from sklearn.utils.class_weight import compute_class_weight
import numpy as np

class_labels = np.array([0, 0, 0, 1, 0, 1, 0, 0, 1, 0])
classes = np.unique(class_labels)

weights = compute_class_weight(
    class_weight='balanced',
    classes=classes,
    y=class_labels
)
class_weight_dict = dict(zip(classes, weights))

model.fit(train_ds, class_weight=class_weight_dict, epochs=20)
```

### Method 2 — Dataset Resampling with tf.data

```python
pos_ds = train_ds.filter(lambda x, y: tf.equal(tf.squeeze(y), 1))
neg_ds = train_ds.filter(lambda x, y: tf.equal(tf.squeeze(y), 0))

pos_ds = pos_ds.repeat()
neg_ds = neg_ds.repeat()

balanced_ds = tf.data.Dataset.sample_from_datasets(
    [pos_ds, neg_ds],
    weights=[0.5, 0.5]
)
balanced_ds = balanced_ds.batch(32).prefetch(tf.data.AUTOTUNE)
```

### Choosing the Right Strategy

| Situation | Recommended Strategy |
|---|---|
| Mild imbalance (up to 4:1) | `class_weight` |
| Moderate imbalance (4:1 – 20:1) | `class_weight` + targeted augmentation |
| Severe imbalance (>20:1) | Oversampling via `sample_from_datasets` + heavy augmentation |
| Very small minority class | Synthetic data generation (GANs for images) |

---

## Section 7 — Complete Pipeline Reference

### Production-Ready Training Setup

```python
import tensorflow as tf

IMG_SIZE = (224, 224)
BATCH_SIZE = 32
AUTOTUNE = tf.data.AUTOTUNE

train_ds = tf.keras.utils.image_dataset_from_directory(
    'data/train', image_size=IMG_SIZE, batch_size=None,
    label_mode='int', shuffle=True, seed=42
)
val_ds = tf.keras.utils.image_dataset_from_directory(
    'data/val', image_size=IMG_SIZE, batch_size=None,
    label_mode='int', shuffle=False
)

augment_layers = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.15),
])

def prepare_train(image, label):
    image = tf.cast(image, tf.float32) / 255.0
    image = augment_layers(image, training=True)
    return image, label

def prepare_val(image, label):
    image = tf.cast(image, tf.float32) / 255.0
    return image, label

train_ds = (train_ds
            .map(prepare_train, num_parallel_calls=AUTOTUNE)
            .cache()
            .shuffle(1000)
            .batch(BATCH_SIZE)
            .prefetch(AUTOTUNE))

val_ds = (val_ds
          .map(prepare_val, num_parallel_calls=AUTOTUNE)
          .cache()
          .batch(BATCH_SIZE)
          .prefetch(AUTOTUNE))
```

---

## Key Vocabulary

| Term | Definition |
|---|---|
| Augmentation | Applying random transformations to training images to increase diversity |
| Overfitting | Model performs well on training data but poorly on unseen data |
| Normalization | Scaling pixel values to a standard range |
| Standardization | Transforming data to zero mean and unit variance |
| `ImageDataGenerator` | Legacy Keras API for on-the-fly image augmentation |
| `tf.data.Dataset` | TensorFlow's pipeline API for efficient data loading |
| `AUTOTUNE` | TensorFlow constant that selects optimal parallelism at runtime |
| Prefetching | Preparing the next batch while the GPU processes the current one |
| Class imbalance | When training classes have unequal sample counts |
| `class_weight` | Dictionary passed to `model.fit()` to reweight loss by class frequency |

---

## Review Questions

1. What is the primary reason augmentation is applied only to training data?
2. Name three augmentation operations provided by `tf.image`.
3. What is the correct order of stages in a `tf.data` pipeline?
4. How does `cache()` affect training speed, and where should it be placed?
5. Compare `class_weight` and dataset resampling — when would you choose each?
6. What happens to `RandomFlip` and `RandomRotation` layers during model inference?
7. What does `AUTOTUNE` do when passed to `num_parallel_calls`?
8. Describe the directory structure expected by `flow_from_directory`.

---

Texas Wesleyan University — CIS-4345 Machine Learning and Deep Learning

Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.

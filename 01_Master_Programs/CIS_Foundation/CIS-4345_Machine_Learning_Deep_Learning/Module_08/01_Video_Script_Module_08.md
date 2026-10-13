# Video Script: Module 08 — Data Augmentation and Image Preprocessing

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: TensorFlow Developer Certificate

---

### [00:00 – 01:30] Opening and Module Overview

**Visual:** Title card — "Module 08: Data Augmentation and Image Preprocessing"

**Audio:**
Welcome back, everyone. I'm Professor Nash, and in Module 08 we tackle one of the most practical skills you will use on every real-world computer-vision project: data augmentation and image preprocessing.

Here is what we will cover today:

- Why augmentation matters and how it fights overfitting
- The legacy `ImageDataGenerator` API
- The modern `tf.data` pipeline with `map()` and prefetching
- Normalization and standardization techniques
- Augmentation operations — flip, rotation, zoom, and brightness
- Handling class imbalance with weights and oversampling
- Keras preprocessing layers baked into the model graph

All of these topics appear directly on the TensorFlow Developer Certificate exam. Let's get started.

---

### [01:30 – 04:00] Why Augmentation Matters

**Visual:** Side-by-side: a training set of 1,000 cat photos vs. a training set of 1,000 cats with augmented variants.

**Audio:**
Imagine you are training a cat-vs-dog classifier. You have 1,000 images of cats and 1,000 images of dogs. That sounds reasonable until you realize that a cat photographed from slightly above, or in dim light, or flipped horizontally looks different to a neural network even though it is the same animal.

Augmentation synthetically expands your dataset by applying random but realistic transformations to each training image during the training loop. The network sees a slightly different version of every image on every epoch, which forces it to learn features that generalize rather than memorizing pixel values.

The benefits are significant:

- Reduces overfitting without collecting more data
- Improves accuracy on unseen orientations and lighting conditions
- Effectively multiplies your dataset size for free

A key rule: augmentation is applied **only during training**. Validation and test sets use the original images.

---

### [04:00 – 07:30] ImageDataGenerator — The Legacy API

**Visual:** Code editor showing `ImageDataGenerator` configuration.

**Audio:**
TensorFlow and Keras have supported `ImageDataGenerator` since the early Keras days. You will still see it on the certification exam and in many production codebases, so you need to know it well.

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,          # normalize pixel values to [0, 1]
    rotation_range=20,          # random rotation up to 20 degrees
    width_shift_range=0.1,      # horizontal shift up to 10%
    height_shift_range=0.1,     # vertical shift up to 10%
    zoom_range=0.15,            # random zoom up to 15%
    horizontal_flip=True,       # flip left-right randomly
    brightness_range=[0.8, 1.2] # brightness jitter
)

val_datagen = ImageDataGenerator(rescale=1.0 / 255)  # no augmentation

train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)

val_generator = val_datagen.flow_from_directory(
    'data/validation',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)
```

Notice we create **two** generator objects — one for training with all augmentations, and one for validation with only rescaling. This is a very common mistake on the exam: students accidentally augment their validation data. Never do that.

The `flow_from_directory` method reads images directly from a folder hierarchy where each subfolder name becomes a class label. This is the standard directory layout assumed by Keras generators.

---

### [07:30 – 11:00] tf.data Pipelines — The Modern Approach

**Visual:** Diagram showing dataset pipeline stages: load → map → cache → shuffle → batch → prefetch.

**Audio:**
The modern TensorFlow way to handle image data is through `tf.data.Dataset`. It is more flexible, more performant, and integrates seamlessly with TPU training. The TensorFlow Developer Certificate exam now emphasizes `tf.data` patterns heavily.

Here is a complete pipeline from image files to batched tensors:

```python
import tensorflow as tf
import pathlib

AUTOTUNE = tf.data.AUTOTUNE
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# Load file paths and labels
data_dir = pathlib.Path('data/train')
dataset = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode='binary'
)

# Normalization function
def normalize(image, label):
    image = tf.cast(image, tf.float32) / 255.0
    return image, label

# Augmentation function (applied per image, before batching)
def augment(image, label):
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_brightness(image, max_delta=0.2)
    image = tf.image.random_contrast(image, lower=0.8, upper=1.2)
    return image, label

# Build the pipeline
train_ds = (
    dataset
    .map(normalize, num_parallel_calls=AUTOTUNE)
    .map(augment,    num_parallel_calls=AUTOTUNE)
    .cache()
    .shuffle(buffer_size=1000)
    .prefetch(buffer_size=AUTOTUNE)
)
```

Let me walk through each stage:

**`.map(normalize)`** — applies the normalization function to every element. `num_parallel_calls=AUTOTUNE` tells TensorFlow to use as many CPU threads as optimal.

**`.cache()`** — after the first epoch, keeps the preprocessed images in memory. This dramatically speeds up training.

**`.shuffle(buffer_size=1000)`** — randomly reorders elements. The buffer size controls how many samples are held in memory for shuffling.

**`.prefetch(AUTOTUNE)`** — prepares the next batch on CPU while the GPU is processing the current batch, eliminating idle time.

---

### [11:00 – 13:30] Normalization Techniques

**Visual:** Table comparing pixel value ranges before and after each technique.

**Audio:**
Normalization is not optional — it is required for stable neural network training. Raw pixel values range from 0 to 255. Without normalization, gradient updates will be extremely unbalanced.

There are three common approaches:

**Min-Max Scaling (rescaling to [0, 1]):** Divide by 255. Simple, predictable.

```python
image = tf.cast(image, tf.float32) / 255.0
```

**Standardization (zero mean, unit variance):** Subtract the dataset mean and divide by the standard deviation. Best when your model needs to generalize across very different image distributions.

```python
# Using a Keras layer — computed on training data
normalization_layer = tf.keras.layers.Normalization()
normalization_layer.adapt(train_ds.map(lambda x, y: x))
```

**Feature-wise normalization with Rescaling layer:** The recommended Keras approach for production, because the normalization becomes part of the model graph.

```python
rescale = tf.keras.layers.Rescaling(scale=1.0/255)
```

For transfer learning with pretrained ImageNet models, always use the model's own `preprocess_input` function rather than plain rescaling:

```python
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
image = preprocess_input(image)  # scales to [-1, 1] for MobileNetV2
```

---

### [13:30 – 16:30] Augmentation Operations in Detail

**Visual:** Grid of the same image with different augmentations applied.

**Audio:**
Let me show you each augmentation operation you need to know for the exam.

Using `tf.image` functions directly inside a `map()` call:

```python
def augment_image(image, label):
    # Horizontal flip — most common augmentation
    image = tf.image.random_flip_left_right(image)

    # Vertical flip — useful for satellite/aerial imagery
    image = tf.image.random_flip_up_down(image)

    # Brightness — simulates lighting variation
    image = tf.image.random_brightness(image, max_delta=0.2)

    # Contrast — simulates camera/exposure variation
    image = tf.image.random_contrast(image, lower=0.7, upper=1.3)

    # Saturation — color intensity variation
    image = tf.image.random_saturation(image, lower=0.8, upper=1.2)

    # Hue — slight color shift
    image = tf.image.random_hue(image, max_delta=0.05)

    # Crop and resize — simulates zoom
    image = tf.image.random_crop(image, size=[200, 200, 3])
    image = tf.image.resize(image, [224, 224])

    return image, label
```

Using the Keras preprocessing layers API, which is the preferred approach for the certification:

```python
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),      # fraction of 2*pi
    tf.keras.layers.RandomZoom(0.15),
    tf.keras.layers.RandomBrightness(0.2),
    tf.keras.layers.RandomContrast(0.2),
    tf.keras.layers.RandomTranslation(0.1, 0.1)
], name="data_augmentation")
```

When these layers are placed at the top of your model, they are automatically disabled during inference — no `training=False` flag needed.

---

### [16:30 – 18:30] Handling Class Imbalance

**Visual:** Bar chart showing imbalanced class distribution (e.g., 900 cats vs. 100 dogs).

**Audio:**
Class imbalance is a real problem in production datasets. If 90% of your training images are class A, a naive model can reach 90% accuracy by predicting class A every time — which is useless.

**Strategy 1 — Class weights:** Tell Keras to penalize errors on the minority class more heavily.

```python
import numpy as np

# Suppose class 0 has 900 samples, class 1 has 100 samples
total = 1000
class_counts = {0: 900, 1: 100}
class_weight = {
    cls: total / (len(class_counts) * count)
    for cls, count in class_counts.items()
}
# class_weight = {0: 0.556, 1: 5.0}

model.fit(train_ds, class_weight=class_weight, epochs=20)
```

**Strategy 2 — Oversampling with tf.data:**

```python
minority_ds = train_ds.filter(lambda x, y: tf.equal(y, 1))
majority_ds = train_ds.filter(lambda x, y: tf.equal(y, 0))

# Repeat minority class to balance ratio
balanced_ds = tf.data.Dataset.sample_from_datasets(
    [majority_ds, minority_ds],
    weights=[0.5, 0.5]
)
```

**Strategy 3 — Augment the minority class more aggressively.** Combine oversampling with heavier augmentation on underrepresented classes.

---

### [18:30 – 20:30] Preprocessing Layers Inside the Model

**Visual:** Model summary showing augmentation layers at the top.

**Audio:**
One of the most powerful patterns in modern Keras is embedding preprocessing — including augmentation — directly into the model graph. This means when you save and export the model, the preprocessing logic travels with it.

```python
import tensorflow as tf

def build_model(input_shape=(224, 224, 3), num_classes=2):
    inputs = tf.keras.Input(shape=input_shape)

    # Preprocessing layers — disabled at inference time automatically
    x = tf.keras.layers.RandomFlip("horizontal")(inputs)
    x = tf.keras.layers.RandomRotation(0.1)(x)
    x = tf.keras.layers.RandomZoom(0.15)(x)
    x = tf.keras.layers.Rescaling(1.0 / 255)(x)

    # Convolutional backbone
    x = tf.keras.layers.Conv2D(32, 3, activation='relu', padding='same')(x)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same')(x)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    x = tf.keras.layers.Dropout(0.4)(x)
    outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

    return tf.keras.Model(inputs, outputs)

model = build_model()
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.summary()
```

When you call `model.predict()` or deploy this model, the `RandomFlip`, `RandomRotation`, and `RandomZoom` layers are automatically in inference mode and pass the image through unchanged. Rescaling still applies. This is the clean, production-ready pattern.

---

### [20:30 – 22:00] Certification Exam Tips

**Visual:** Bullet list of common exam pitfalls.

**Audio:**
Before we wrap up, let me give you the key exam tips for this module:

- **Never augment validation or test data.** Only `rescale` or `preprocess_input` on val/test.
- **`flow_from_directory` vs `image_dataset_from_directory`** — know both. The former is Python-generator-based; the latter returns a `tf.data.Dataset`.
- **`AUTOTUNE`** — always use `tf.data.AUTOTUNE` for `num_parallel_calls` and `prefetch` buffer size.
- **`cache()` placement** — cache after expensive transformations that do not change epoch-to-epoch, but before `shuffle()` and `prefetch()`.
- **Keras preprocessing layers are disabled at inference time** — this is a frequently tested fact.
- **`class_weight` goes in `model.fit()`** — not in the dataset pipeline.

---

### [22:00 – 24:00] Module Summary and Lab Preview

**Visual:** Summary slide with key API checklist.

**Audio:**
Excellent work today. Here is what you learned in Module 08:

- `ImageDataGenerator` with `flow_from_directory` for legacy pipelines
- `tf.data.Dataset` with `.map()`, `.cache()`, `.shuffle()`, `.prefetch()` for modern pipelines
- Normalization strategies: rescaling, standardization, and `preprocess_input`
- Augmentation with `tf.image` functions and Keras preprocessing layers
- Class imbalance: `class_weight`, oversampling, and targeted augmentation
- Embedding preprocessing inside the Keras model graph

In the lab, you will build a complete image classification pipeline using the Cats vs. Dogs dataset. You will compare a baseline model with no augmentation to one with full augmentation and class-weight handling, and measure the difference in validation accuracy.

Head over to the Lab file to get started. I will see you in Module 09 where we move into Natural Language Processing with TensorFlow.

---

End of Module 08 Video Script

Texas Wesleyan University — CIS-4345 Machine Learning and Deep Learning

Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.

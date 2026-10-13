# Reading Guide: Module 11 — Transfer Learning and Fine-Tuning

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4345 &BULL; MACHINE LEARNING & DEEP LEARNING SYSTEMS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Overview

Transfer learning is the practice of reusing a model trained on one task as the starting point for a model on a different but related task. In computer vision, this almost always means starting from a model pretrained on ImageNet — 1.2 million images across 1000 classes — and adapting it to a smaller, specialized dataset. This module covers the theory behind feature transferability, the two primary strategies (feature extraction and fine-tuning), the major pretrained architectures, and TensorFlow Hub.

---

## Section 1 — The Case for Transfer Learning

### Training From Scratch Is Rarely Justified

Training a modern CNN from random weights requires:

- Hundreds of thousands to millions of labeled examples

- Days to weeks of GPU computation

- Careful regularization to avoid overfitting at scale

For most real-world projects — medical imaging, industrial inspection, custom product recognition — neither the data volume nor the compute budget is available. Transfer learning solves this by reusing features that were learned at enormous cost by well-resourced research organizations.

### What Transfers?

Research by Yosinski et al. (2014) showed that CNN features transfer on a spectrum:

- **Layers 1–3**: Highly generic. Edge detectors, color blobs, Gabor-like filters. Transfer well to almost any visual task.

- **Layers 4–6**: Moderately generic. Textures, patterns, object parts. Transfer well when source and target domains are related.

- **Final layers**: Task-specific. Class-level representations tied to the original labels. These are replaced for a new task.

The practical implication: the earlier the layer, the safer it is to freeze it and reuse it as-is.

---

## Section 2 — Feature Extraction

### Concept

In feature extraction mode, the entire pretrained network is frozen. The network acts as a fixed transformation that converts raw images into high-dimensional feature vectors. A new, small classification head is trained on top of these features.

Because only the head is trained, feature extraction is:

- **Fast**: Backpropagation stops at the head — far fewer gradient computations

- **Stable**: Pretrained weights cannot be corrupted

- **Data-efficient**: Works well with as few as 100–500 images per class

### Implementation Pattern

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import MobileNetV2

# Load base model without classification head
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# Freeze the entire base
base_model.trainable = False

# Add classification head
inputs  = keras.Input(shape=(224, 224, 3))
x       = base_model(inputs, training=False)
x       = keras.layers.GlobalAveragePooling2D()(x)
x       = keras.layers.Dense(128, activation='relu')(x)
x       = keras.layers.Dropout(0.4)(x)
outputs = keras.layers.Dense(5, activation='softmax')(x)

model = keras.Model(inputs, outputs)
```

### The `training=False` Argument

When calling `base_model(inputs, training=False)`, you force all BatchNormalization layers inside the base model into **inference mode**. In inference mode, BN layers use their stored running mean and variance rather than computing new statistics from the current batch. This is critical — without it, BatchNormalization would update its running statistics during your training, corrupting the pretrained normalization.

### GlobalAveragePooling2D vs. Flatten

| Method | Output Size | Risk |
|---|---|---|
| `GlobalAveragePooling2D` | `(batch, channels)` | None — compact, regularizing |
| `Flatten` | `(batch, H * W * channels)` | Very large, prone to overfitting |

`GlobalAveragePooling2D` averages each spatial feature map to a single value, producing a compact feature vector. It is strongly preferred over `Flatten` in transfer learning heads.

---

## Section 3 — Fine-Tuning

### Concept

After training the classification head until convergence, fine-tuning unfreezes some of the pretrained layers and continues training the entire network end-to-end. The goal is to adapt the pretrained features to the new domain, not just bolt a new head onto frozen features.

Fine-tuning is most valuable when:

- The new domain is somewhat different from ImageNet (e.g., medical images, satellite imagery, microscopy)

- You have enough data to train the unfrozen layers without overfitting (typically 1,000+ images per class)

### Two-Phase Workflow

**Phase 1 — Feature Extraction** (train head only):

```python
base_model.trainable = False
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-3),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(train_ds, epochs=10, validation_data=val_ds)
```

**Phase 2 — Fine-Tuning** (unfreeze top layers, use low learning rate):

```python
base_model.trainable = True

# Freeze all layers except the last 20
for layer in base_model.layers[:-20]:
    layer.trainable = False

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(train_ds, epochs=20, validation_data=val_ds,
          callbacks=[keras.callbacks.EarlyStopping(patience=5,
                                                   restore_best_weights=True)])
```

### Why the Low Learning Rate Matters

The pretrained weights already encode excellent visual representations. Fine-tuning wants to nudge them toward the new task — not overwrite them. A learning rate of `1e-5` produces small gradient steps that preserve most of the pretrained structure while allowing gradual adaptation.

Using `1e-3` for fine-tuning causes **catastrophic forgetting**: the new gradients overwrite the pretrained feature representations within a few epochs, effectively reinitializing the deep layers.

### How Many Layers to Unfreeze?

| Scenario | Recommendation |
|---|---|
| New dataset is similar to ImageNet; small (< 1K/class) | Unfreeze last 10–20% of layers |
| New dataset is similar; large (> 5K/class) | Unfreeze last 30–50% of layers |
| New dataset is very different; small | Feature extraction only — do not fine-tune |
| New dataset is very different; large | Fine-tune from scratch or use all layers |

---

## Section 4 — Pretrained Model Architectures

### VGG16

VGG16 was introduced by Simonyan and Zisserman (Oxford, 2014) and placed second in ILSVRC 2014. Its defining characteristic is **simplicity**: 13 convolutional layers using only 3x3 filters with ReLU, followed by 3 fully connected layers. The depth achieves a large receptive field while keeping individual filters small.

Key facts:

- 138 million parameters (528 MB)

- Top-5 ImageNet accuracy: 92.7%

- Input: 224x224x3

- Use case: Learning transfer learning concepts; debugging — the simple architecture is easy to reason about

```python
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input

base = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
```

### ResNet50

ResNet (He et al., 2015) introduced **residual connections** (skip connections) that add the input of a block directly to its output:

```text
output = F(x) + x
```

This allows gradients to bypass entire blocks, enabling networks of 50, 101, or 152 layers to train stably. ResNet50 achieves better accuracy than VGG16 with 82% fewer parameters.

Key facts:

- 25 million parameters (98 MB)

- Top-5 ImageNet accuracy: 93.0%

- Input: 224x224x3

- Use case: General production baseline; best accuracy-to-size ratio in the VGG/ResNet tier

```python
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input

base = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
```

### MobileNetV2

MobileNetV2 (Sandler et al., Google, 2018) was designed for mobile and embedded deployment. It uses **depthwise separable convolutions** that factorize a standard convolution into:

1. A depthwise convolution (filter each channel independently)

2. A pointwise 1x1 convolution (combine channels)

This reduces computation by approximately 8–9 times compared to standard convolutions with minimal accuracy loss.

Key facts:

- 3.4 million parameters (14 MB)

- Top-5 ImageNet accuracy: 91.0%

- Input: 224x224x3 (also supports 96x96, 128x128, 160x160, 192x192)

- Use case: Mobile apps, edge devices, TensorFlow Lite deployment

```python
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

base = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
```

### Architecture Comparison

| Model | Parameters | Size (MB) | Top-1 Acc | Inference Speed | Best Use |
|---|---|---|---|---|---|
| VGG16 | 138M | 528 | 71.3% | Slow | Education, prototyping |
| ResNet50 | 25M | 98 | 74.9% | Moderate | Production baseline |
| MobileNetV2 | 3.4M | 14 | 71.8% | Fast | Mobile, edge, TF Lite |
| InceptionV3 | 23M | 92 | 77.9% | Moderate | High accuracy needs |
| EfficientNetB0 | 5.3M | 29 | 77.1% | Fast | Accuracy + efficiency |

---

## Section 5 — Preprocessing for Pretrained Models

Each model family was trained with a specific input normalization. Using the wrong preprocessing function will significantly degrade performance because the frozen layers expect inputs in the same range they were trained on.

```python
# VGG16 — subtracts ImageNet channel means, converts to BGR
from tensorflow.keras.applications.vgg16 import preprocess_input as vgg_preprocess

# ResNet50 — same mean subtraction as VGG
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess

# MobileNetV2 — scales to [-1, 1]
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input as mobilenet_preprocess

# Usage in a preprocessing pipeline
inputs  = keras.Input(shape=(224, 224, 3))
x       = mobilenet_preprocess(inputs)   # apply BEFORE the base model
x       = base_model(x, training=False)
```

Never use a generic `Rescaling(1./255)` layer when working with a pretrained model unless you have confirmed the model expects that range.

---

## Section 6 — TensorFlow Hub

TensorFlow Hub (`tensorflow_hub`) is Google's repository of reusable pretrained model components. It provides two types of modules:

- **Feature vector modules**: Output a feature vector (no classification head)

- **Classification modules**: Include the full head for the original task

```python
import tensorflow_hub as hub

# MobileNetV2 feature vector (1280-dim output)
hub_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"

model = keras.Sequential([
    hub.KerasLayer(hub_url, input_shape=(224, 224, 3), trainable=False),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

### Key TF Hub Details

- `trainable=False`: frozen feature extractor

- `trainable=True`: full fine-tuning of the Hub module

- The module handles its own preprocessing internally for many Hub-hosted models — check the module documentation

- Hub models are cached locally after first download

---

## Section 7 — Data Augmentation in Transfer Learning Pipelines

Data augmentation is applied **only during training**, not validation or inference. In Keras, augmentation layers placed inside the model apply augmentation automatically during `model.fit` and skip it during `model.predict` or `model.evaluate`.

```python
data_augmentation = keras.Sequential([
    keras.layers.RandomFlip("horizontal"),
    keras.layers.RandomRotation(0.15),
    keras.layers.RandomZoom(0.15),
    keras.layers.RandomBrightness(0.1),
], name="augmentation")

# Place augmentation BEFORE preprocessing and base model
inputs  = keras.Input(shape=(224, 224, 3))
x       = data_augmentation(inputs)
x       = mobilenet_preprocess(x)
x       = base_model(x, training=False)
x       = keras.layers.GlobalAveragePooling2D()(x)
outputs = keras.layers.Dense(num_classes, activation='softmax')(x)
```

---

## Section 8 — Complete Transfer Learning Pipeline

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import tensorflow_datasets as tfds

# Load flowers dataset
(train_ds, val_ds), info = tfds.load(
    'tf_flowers',
    split=['train[:80%]', 'train[80%:]'],
    as_supervised=True,
    with_info=True
)
NUM_CLASSES = info.features['label'].num_classes  # 5

def preprocess(image, label):
    image = tf.image.resize(image, (224, 224))
    image = preprocess_input(image)
    return image, label

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.map(preprocess, num_parallel_calls=AUTOTUNE).batch(32).prefetch(AUTOTUNE)
val_ds   = val_ds.map(preprocess, num_parallel_calls=AUTOTUNE).batch(32).prefetch(AUTOTUNE)

# Build model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False

inputs  = keras.Input(shape=(224, 224, 3))
x       = base_model(inputs, training=False)
x       = keras.layers.GlobalAveragePooling2D()(x)
x       = keras.layers.Dense(128, activation='relu')(x)
x       = keras.layers.Dropout(0.3)(x)
outputs = keras.layers.Dense(NUM_CLASSES, activation='softmax')(x)
model   = keras.Model(inputs, outputs)

# Phase 1 — feature extraction
model.compile(optimizer=keras.optimizers.Adam(1e-3),
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_ds, epochs=10, validation_data=val_ds)

# Phase 2 — fine-tuning
base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False

model.compile(optimizer=keras.optimizers.Adam(1e-5),
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_ds, epochs=20, validation_data=val_ds,
          callbacks=[keras.callbacks.EarlyStopping(patience=5,
                                                   restore_best_weights=True)])
```

---

## Exam Tips — TensorFlow Developer Certificate

- Know the three-step pattern: load with `include_top=False`, freeze with `trainable=False`, add GlobalAveragePooling2D + Dense head

- The exam often asks about `training=False` in the base model call — know why it is necessary (BatchNormalization behavior)

- `GlobalAveragePooling2D` is the standard pooling choice for transfer learning heads — not `Flatten`

- Fine-tuning uses a learning rate roughly 100 times smaller than the head-training phase

- When unfreezing for fine-tuning, always freeze early layers and only unfreeze later layers

- Know how to load a TF Hub module as a `hub.KerasLayer` and integrate it into a Sequential or Functional model

- Each pretrained family has its own `preprocess_input` function — never use generic `1./255` rescaling with pretrained models

---

*End of Reading Guide — Module 11*

---

## 9. Supplemental Resources

**1. [Transfer Learning and Fine-Tuning — TensorFlow Tutorial](https://www.tensorflow.org/tutorials/images/transfer_learning)**
Official TensorFlow tutorial demonstrating the complete two-phase transfer learning workflow: Phase 1 feature extraction with a frozen MobileNetV2 base, followed by Phase 2 fine-tuning of the top layers. Includes data augmentation, the critical `training=False` argument, and learning rate reduction for fine-tuning.

**2. [TensorFlow Hub — Image Feature Extraction](https://www.tensorflow.org/hub/tutorials/image_feature_vector)**
Official TF Hub tutorial showing how to use pre-built image feature vector modules in a Keras model with `hub.KerasLayer`. Demonstrates how to swap different architectures (MobileNetV2, EfficientNet, ResNet) by changing only the Hub URL, without rewriting any model code.

**3. [Papers With Code — ImageNet Benchmark](https://paperswithcode.com/sota/image-classification-on-imagenet)**
State-of-the-art ImageNet classification leaderboard tracking accuracy, parameter count, and FLOPs for all major architectures including EfficientNet, ViT, ConvNeXt, and others. Useful for comparing the accuracy-efficiency tradeoffs of pretrained models when selecting a base for transfer learning.

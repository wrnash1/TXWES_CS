# Reading Guide: Module 12 — Model Optimization and Hyperparameter Tuning

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

This reading guide covers four interconnected topics that bridge model development and production deployment: learning rate tuning, automated hyperparameter search with Keras Tuner, model compression with TensorFlow Lite quantization and pruning, and an introduction to TFX production pipelines. These topics represent the final stage of the ML development lifecycle — moving from "model works in a notebook" to "model is optimized, compressed, and running on real hardware."

---

## Section 1 — Learning Rate Tuning

### Why Learning Rate Is the Most Important Hyperparameter

The learning rate controls the step size the optimizer takes along the loss surface at each gradient update. It has an outsized effect on training compared to most other hyperparameters because:

- Too high: The optimizer overshoots minima, causing oscillation or divergence. Loss increases or fluctuates wildly.
- Too low: Gradients are tiny — training converges correctly but requires orders of magnitude more epochs.
- Just right: Loss decreases smoothly and reaches a good minimum within a reasonable number of epochs.

Small changes in learning rate — even within one order of magnitude — can mean the difference between a model that converges and one that never trains.

### The Learning Rate Range Test

The LR range test (Smith, 2017) is a one-epoch diagnostic that finds a good learning rate range:

1. Set learning rate to a very small value (e.g., `1e-7`)
2. Train for one epoch, linearly or exponentially increasing the LR each batch up to a large value (e.g., `1e-1`)
3. Plot loss vs. learning rate
4. Choose the LR at the steepest loss decline as the maximum learning rate for training

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

class LRFinderCallback(keras.callbacks.Callback):
    def __init__(self, min_lr=1e-7, max_lr=0.1, num_steps=100):
        self.min_lr    = min_lr
        self.max_lr    = max_lr
        self.num_steps = num_steps
        self.lrs       = []
        self.losses    = []
        self._step     = 0

    def on_train_batch_begin(self, batch, logs=None):
        ratio = self._step / self.num_steps
        lr    = self.min_lr * (self.max_lr / self.min_lr) ** ratio
        keras.backend.set_value(self.model.optimizer.learning_rate, lr)
        self.lrs.append(lr)
        self._step += 1

    def on_train_batch_end(self, batch, logs=None):
        self.losses.append(logs.get('loss', 0))

    def plot(self):
        plt.figure(figsize=(10, 4))
        plt.semilogx(self.lrs, self.losses)
        plt.xlabel('Learning Rate (log scale)')
        plt.ylabel('Loss')
        plt.title('LR Range Test')
        plt.grid(True, alpha=0.3)
        plt.show()
```

### Learning Rate Schedules

| Schedule | Keras API | Description | Best For |
|---|---|---|---|
| Constant | `Adam(learning_rate=1e-3)` | No decay | Quick experiments |
| Step decay | `LearningRateScheduler` | Multiply by factor every N epochs | When decay epochs are known |
| Exponential decay | `ExponentialDecay` | Smooth continuous decay | General training |
| Cosine annealing | `CosineDecay` | Smooth cosine curve to near zero | Final fine-tuning |
| Reduce on plateau | `ReduceLROnPlateau` | Reactive: reduces when val_loss plateaus | Noisy or slow convergence |
| Warmup + decay | Custom schedule | Low start, ramp up, then decay | Large models, large batches |

### ReduceLROnPlateau — The Safe Default

For most Keras training workflows, `ReduceLROnPlateau` is a robust default:

```python
keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,       # multiply LR by 0.5 when triggered
    patience=3,       # wait 3 epochs of no improvement
    min_lr=1e-7,      # floor — never reduce below this
    verbose=1
)
```

### Cosine Decay Schedule

```python
lr_schedule = keras.optimizers.schedules.CosineDecay(
    initial_learning_rate=1e-3,
    decay_steps=10000,
    alpha=1e-6          # minimum learning rate at end of decay
)
optimizer = keras.optimizers.Adam(learning_rate=lr_schedule)
```

---

## Section 2 — Keras Tuner

### Concept

Keras Tuner (`keras-tuner` package) provides automated hyperparameter optimization. Instead of manually trying combinations, you define a search space and Keras Tuner systematically explores it, tracking results and identifying the best configuration.

### Defining a Hypermodel

The core pattern is a `build_model(hp)` function that uses the `HyperParameters` object `hp` to define searchable values:

```python
import keras_tuner as kt

def build_model(hp):
    inputs = keras.Input(shape=(224, 224, 3))

    # Searchable number of dense units
    units = hp.Int('dense_units', min_value=64, max_value=512, step=64)

    # Searchable dropout rate
    dropout = hp.Float('dropout', min_value=0.2, max_value=0.5, step=0.1)

    # Searchable learning rate from a discrete set
    lr = hp.Choice('learning_rate', values=[1e-4, 5e-4, 1e-3])

    # Searchable boolean — include an extra layer or not
    use_extra = hp.Boolean('use_extra_layer')

    x = keras.layers.Flatten()(inputs)
    x = keras.layers.Dense(units, activation='relu')(x)
    x = keras.layers.Dropout(dropout)(x)
    if use_extra:
        x = keras.layers.Dense(units // 2, activation='relu')(x)
    outputs = keras.layers.Dense(10, activation='softmax')(x)

    model = keras.Model(inputs, outputs)
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=lr),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model
```

### HyperParameter Types

| Method | Description | Example |
|---|---|---|
| `hp.Int(name, min, max, step)` | Integer range | Units, layer count |
| `hp.Float(name, min, max, step)` | Float range | Dropout, L2 weight |
| `hp.Choice(name, values)` | Discrete choices | Learning rate, optimizer |
| `hp.Boolean(name)` | True/False toggle | Include layer or not |
| `hp.Fixed(name, value)` | Constant — not searched | Pin known-good values |

### Search Strategies

#### RandomSearch

Randomly samples combinations from the hyperparameter space. Simple and surprisingly effective when the space is not too large.

```python
tuner = kt.RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=20,
    directory='kt_results',
    project_name='my_project'
)
```

#### Hyperband

Based on the Hyperband algorithm (Li et al., 2017). Trains many configurations for a small number of epochs, keeps the top performers, and reallocates compute to them. Much more efficient than random search for large spaces.

```python
tuner = kt.Hyperband(
    build_model,
    objective='val_accuracy',
    max_epochs=30,
    factor=3,           # reduction factor
    directory='kt_results',
    project_name='hyperband_project'
)
```

#### BayesianOptimization

Builds a probabilistic surrogate model of the objective function and selects the next trial based on expected improvement. Most sample-efficient — finds good configurations with fewer trials than random search.

```python
tuner = kt.BayesianOptimization(
    build_model,
    objective='val_accuracy',
    max_trials=15,
    directory='kt_results',
    project_name='bayes_project'
)
```

### Running a Search

```python
stop_early = keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

tuner.search(
    x_train, y_train,
    epochs=20,
    validation_split=0.2,
    callbacks=[stop_early]
)

# Get best hyperparameters
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
print(f"Best LR: {best_hps.get('learning_rate')}")
print(f"Best units: {best_hps.get('dense_units')}")

# Build and train final model with best hyperparameters
final_model = tuner.hypermodel.build(best_hps)
final_model.fit(x_train, y_train, epochs=50, validation_split=0.2,
                callbacks=[stop_early])
```

### Search Space Summary

Always call `tuner.search_space_summary()` before running the search to confirm the space is defined as expected:

```python
tuner.search_space_summary()
# Output: lists all hyperparameters and their ranges/choices
```

---

## Section 3 — TensorFlow Lite

### What TFLite Does

TFLite is a runtime optimized for inference (not training) on resource-constrained devices. The `.tflite` format:

- Stores the model graph in FlatBuffers (efficient binary format)
- Eliminates training-only operations (gradient computation, optimizer states)
- Supports quantization natively
- Runs on Android, iOS, Linux-based embedded systems, and microcontrollers (TFLM)

### Standard Conversion

```python
# Save your trained Keras model first
model.save('my_model')

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_saved_model('my_model')
tflite_model = converter.convert()

with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
```

You can also convert directly from a Keras model object without saving first:

```python
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
```

### Quantization Options

| Type | Weights | Activations | Calibration Data | Size Reduction | Speed |
|---|---|---|---|---|---|
| None (float32) | float32 | float32 | Not needed | Baseline | Baseline |
| Dynamic range | int8 | float32 (at runtime) | Not needed | ~4x | ~2x on CPU |
| Full integer | int8 | int8 | Required (100+ samples) | ~4x | ~4x on int hardware |
| Float16 | float16 | float32 | Not needed | ~2x | GPU-optimized |

### Dynamic Range Quantization (Default Recommended)

```python
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant = converter.convert()
```

### Full Integer Quantization

```python
def representative_dataset():
    for sample in calibration_data[:200]:
        yield [sample[np.newaxis, ...].astype(np.float32)]

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type  = tf.int8
converter.inference_output_type = tf.int8
tflite_int8 = converter.convert()
```

### Running TFLite Inference

```python
interpreter = tf.lite.Interpreter(model_content=tflite_quant)
interpreter.allocate_tensors()

input_details  = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def tflite_predict(interpreter, input_data):
    interpreter.set_tensor(
        input_details[0]['index'],
        input_data.astype(input_details[0]['dtype'])
    )
    interpreter.invoke()
    return interpreter.get_tensor(output_details[0]['index'])

pred = tflite_predict(interpreter, x_val[0:1])
print(f"Predicted class: {pred.argmax()}, Confidence: {pred.max():.3f}")
```

---

## Section 4 — Model Pruning

### Concept

Magnitude-based weight pruning sets weights with the smallest absolute values to exactly zero. The resulting sparse model:

- Compresses well with standard compression algorithms (zip, gzip) — zeros compress efficiently
- Can exploit sparse matrix operations on hardware that supports them
- Maintains accuracy when pruning is applied gradually with fine-tuning

### TF Model Optimization Toolkit

```python
pip install tensorflow-model-optimization
```

```python
import tensorflow_model_optimization as tfmot

# Define a polynomial decay pruning schedule
pruning_params = {
    'pruning_schedule': tfmot.sparsity.keras.PolynomialDecay(
        initial_sparsity=0.0,
        final_sparsity=0.50,
        begin_step=0,
        end_step=2000
    )
}

# Wrap model for pruning
model_to_prune = tfmot.sparsity.keras.prune_low_magnitude(
    model, **pruning_params
)

model_to_prune.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# REQUIRED callback — updates pruning masks each step
model_to_prune.fit(
    x_train, y_train,
    epochs=5,
    validation_data=(x_val, y_val),
    callbacks=[tfmot.sparsity.keras.UpdatePruningStep()]
)

# Remove pruning wrappers before saving/exporting
model_pruned = tfmot.sparsity.keras.strip_pruning(model_to_prune)
model_pruned.save('pruned_model')
```

### Pruning + Quantization Combined

For maximum compression, apply pruning first, then convert with TFLite quantization:

```python
# After stripping pruning wrappers:
converter = tf.lite.TFLiteConverter.from_keras_model(model_pruned)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_pruned_quant = converter.convert()
```

### Expected Size and Accuracy Tradeoffs

| Strategy | Typical Size Reduction | Typical Accuracy Loss |
|---|---|---|
| No optimization (float32 TFLite) | Baseline | 0% |
| Dynamic range quantization | ~4x | < 1% |
| Full integer quantization | ~4x | < 1% |
| 50% pruning + quantization | ~8x | 1–2% |
| 80% pruning + quantization | ~15x | 2–5% |

---

## Section 5 — TFX Pipeline Overview

### Why Production ML Needs a Pipeline

A model trained in a notebook must be retrained periodically as new data arrives. Without a pipeline:

- Training steps are manual and error-prone
- There is no systematic validation before a new model version is deployed
- Data quality issues are discovered only after deployment
- Model versions are not tracked or reproducible

TFX addresses all of these with a structured component-based pipeline.

### Core TFX Components

| Component | Purpose |
|---|---|
| ExampleGen | Ingest raw data; split into train and evaluation sets |
| StatisticsGen | Compute descriptive statistics for each feature |
| SchemaGen | Infer a schema (feature types, value ranges) from statistics |
| ExampleValidator | Detect anomalies: missing features, out-of-range values, schema violations |
| Transform | Feature engineering using TF Transform; ensures train/serve consistency |
| Trainer | Train the model using a `trainer_fn` function |
| Evaluator | Evaluate model against a baseline; produce metrics; gate promotion |
| Pusher | Deploy a validated model to TF Serving, TF Lite, or a file system |

### Minimal TFX Example Structure

```python
from tfx.components import CsvExampleGen, StatisticsGen, SchemaGen
from tfx.components import ExampleValidator, Transform, Trainer, Evaluator, Pusher
from tfx.orchestration.experimental.interactive.interactive_context import InteractiveContext

context = InteractiveContext()

# Ingest data
example_gen = CsvExampleGen(input_base='data/train_csv/')
context.run(example_gen)

# Compute statistics
statistics_gen = StatisticsGen(examples=example_gen.outputs['examples'])
context.run(statistics_gen)

# Infer schema
schema_gen = SchemaGen(statistics=statistics_gen.outputs['statistics'])
context.run(schema_gen)
```

### Trainer Function Pattern

```python
def run_fn(fn_args):
    import tensorflow as tf
    from tensorflow import keras

    # fn_args provides train_files, eval_files, serving_model_dir, etc.
    model = build_and_compile_model()

    train_dataset = get_dataset(fn_args.train_files)
    eval_dataset  = get_dataset(fn_args.eval_files)

    model.fit(
        train_dataset,
        epochs=10,
        validation_data=eval_dataset
    )

    model.save(fn_args.serving_model_dir)
```

---

## Section 6 — Optimization Decision Framework

Use this framework to decide which optimizations to apply:

```text
Deployment target?
├── Server / cloud: No size constraint
│   └── Focus on accuracy — use larger model, tune hyperparameters
├── Mobile (iOS/Android): < 50 MB target
│   ├── Use MobileNetV2 or EfficientNet base
│   ├── Apply dynamic range quantization
│   └── Consider TFLite conversion
└── Microcontroller (< 1 MB):
    ├── Use pruning to 80%+ sparsity
    ├── Apply full integer quantization
    └── Use TensorFlow Lite for Microcontrollers (TFLM)

Dataset size for hyperparameter tuning?
├── < 10K samples: RandomSearch, 10–20 trials, small search space
├── 10K–100K: Hyperband — efficient elimination
└── > 100K: BayesianOptimization or Hyperband with large epoch budget
```

---

## Exam Tips — TensorFlow Developer Certificate

- Know the complete `build_model(hp)` pattern with `hp.Int`, `hp.Float`, `hp.Choice`, and `hp.Boolean`

- Know how to instantiate `kt.RandomSearch` and `kt.Hyperband` with the correct arguments

- Know `tuner.search()`, `tuner.get_best_hyperparameters()`, and `tuner.hypermodel.build(best_hps)`

- TFLite conversion: `TFLiteConverter.from_keras_model(model)` followed by `converter.convert()`

- Quantization: `converter.optimizations = [tf.lite.Optimize.DEFAULT]` enables dynamic range quantization

- TFLite inference: `Interpreter`, `allocate_tensors()`, `get_input_details()`, `set_tensor()`, `invoke()`, `get_tensor()`

- Know the difference between dynamic range, full integer, and float16 quantization modes

- `ReduceLROnPlateau` parameters: `monitor`, `factor`, `patience`, `min_lr`

---

*End of Reading Guide — Module 12*

---

## 9. Supplemental Resources

**1. [Keras Tuner Documentation — Getting Started](https://keras.io/keras_tuner/)**
Official Keras Tuner documentation covering `RandomSearch`, `Hyperband`, and `BayesianOptimization` tuners with complete code examples for `build_model(hp)`, `tuner.search()`, and `tuner.get_best_hyperparameters()`. The primary reference for all Keras Tuner exam questions.

**2. [TensorFlow Model Optimization Toolkit — Post-Training Quantization](https://www.tensorflow.org/model_optimization/guide/quantization/post_training)**
Official TF documentation covering all three post-training quantization modes: dynamic range, full integer, and float16. Includes the `representative_dataset` generator pattern and step-by-step TFLite conversion workflow with accuracy benchmarks on MobileNetV2.

**3. [scikit-learn Hyperparameter Tuning — GridSearchCV and RandomizedSearchCV](https://scikit-learn.org/stable/modules/grid_search.html)**
Scikit-learn's comprehensive guide to hyperparameter search for classical ML models. Covers `GridSearchCV`, `RandomizedSearchCV`, cross-validation scoring, and `pipeline` integration. Provides a useful contrast to Keras Tuner's approach and is directly applicable to the scikit-learn portions of the course.

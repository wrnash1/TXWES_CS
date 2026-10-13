# Video Script: Module 12 — Model Optimization and Hyperparameter Tuning

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: TensorFlow Developer Certificate

---

## SEGMENT 1 — Introduction (0:00–2:00)

**[ON CAMERA]**

Welcome back. I'm Professor Nash, and this is Module 12 of CIS-4345.

In the previous two modules we built sequence models with LSTMs and image classifiers with transfer learning. Both of those modules focused on getting a model working. This module is about getting a model working *well* — and then getting it small enough and fast enough to actually deploy.

We are going to cover four major topics today:

- Learning rate tuning — the most important hyperparameter you will ever configure

- Keras Tuner — the automated hyperparameter search tool used in the TensorFlow ecosystem

- TensorFlow Lite — Google's framework for deploying models to mobile and embedded devices

- Model compression techniques: quantization and pruning

- A brief introduction to TFX pipelines for production ML

This module is directly aligned with the TensorFlow Developer Certificate exam. Keras Tuner, TF Lite conversion, and quantization appear explicitly in the exam guide. Let's get into it.

---

## SEGMENT 2 — Learning Rate: The Most Important Hyperparameter (2:00–5:30)

**[SLIDE: Learning Rate Effects]**

If I had to name the single most impactful hyperparameter to tune, it is the learning rate. Too high, and the optimizer overshoots the minimum — loss oscillates or diverges. Too low, and the optimizer creeps so slowly that training never converges in a reasonable time. Getting this right matters more than model architecture choices in many cases.

**[SLIDE: Learning Rate Range Test]**

The learning rate range test, popularized by Leslie Smith in 2017, is a practical diagnostic. You train for one epoch while linearly increasing the learning rate from a very small value like `1e-7` to a large value like `1e-1`. You plot loss versus learning rate and look for the rate at which loss drops most steeply. That is your target learning rate — or slightly below it for stability.

```python
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Learning rate range test
class LRFinder(keras.callbacks.Callback):
    def __init__(self, min_lr=1e-7, max_lr=1e-1, steps=100):
        self.min_lr = min_lr
        self.max_lr = max_lr
        self.steps  = steps
        self.lrs, self.losses = [], []
        self.step = 0

    def on_train_batch_begin(self, batch, logs=None):
        lr = self.min_lr * (self.max_lr / self.min_lr) ** (self.step / self.steps)
        tf.keras.backend.set_value(self.model.optimizer.learning_rate, lr)
        self.lrs.append(lr)
        self.step += 1

    def on_train_batch_end(self, batch, logs=None):
        self.losses.append(logs['loss'])

lr_finder = LRFinder()
```

**[SLIDE: Learning Rate Schedules]**

Beyond finding the right initial rate, scheduling the learning rate during training is standard practice. The most common schedules are:

- **Constant**: Simple, set once, never changes. Works for short experiments.

- **Step decay**: Reduce by a factor every N epochs. Easy to reason about.

- **Cosine annealing**: Smoothly decreases following a cosine curve. Often gives the best final accuracy.

- **ReduceLROnPlateau**: Adaptive — reduces when validation loss stops improving. Keras built-in.

- **Warmup**: Start very low, ramp up for a few epochs, then decay. Standard for large models.

---

## SEGMENT 3 — Keras Tuner (5:30–10:00)

**[SLIDE: Why Automated Hyperparameter Search?]**

Manual hyperparameter tuning is time-consuming and unsystematic. You try a few values, form intuitions, adjust, and repeat. The problem is that hyperparameters interact — the optimal number of units in a layer depends on the learning rate, the dropout rate, the number of layers. Manual search rarely finds the global optimum.

Keras Tuner provides structured automated search over a hyperparameter space you define.

**[SCREEN SHARE — Code Editor]**

```python
import keras_tuner as kt

def build_model(hp):
    model = keras.Sequential()
    model.add(keras.layers.Flatten(input_shape=(28, 28)))

    # Search over number of layers
    for i in range(hp.Int('num_layers', 1, 3)):
        model.add(keras.layers.Dense(
            units=hp.Int(f'units_{i}', min_value=32, max_value=256, step=32),
            activation='relu'
        ))
        model.add(keras.layers.Dropout(
            rate=hp.Float(f'dropout_{i}', min_value=0.0, max_value=0.5, step=0.1)
        ))

    model.add(keras.layers.Dense(10, activation='softmax'))

    model.compile(
        optimizer=keras.optimizers.Adam(
            learning_rate=hp.Choice('lr', values=[1e-4, 5e-4, 1e-3, 5e-3])
        ),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model
```

The `build_model` function takes an `hp` (HyperParameters) object. Every `hp.Int`, `hp.Float`, and `hp.Choice` call defines a dimension of the search space. Keras Tuner will automatically sample and evaluate combinations.

**[SCREEN SHARE — Tuner Setup]**

```python
# RandomSearch tuner
tuner = kt.RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=20,
    executions_per_trial=1,
    directory='tuner_results',
    project_name='mnist_tuning'
)

tuner.search_space_summary()

# Run the search
(x_train, y_train), (x_val, y_val) = keras.datasets.mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_val   = x_val.astype('float32') / 255.0

tuner.search(
    x_train, y_train,
    epochs=10,
    validation_data=(x_val, y_val),
    callbacks=[keras.callbacks.EarlyStopping(patience=3)]
)

# Retrieve best model
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
best_model = tuner.hypermodel.build(best_hps)
print(f"Best LR: {best_hps.get('lr')}")
print(f"Best units_0: {best_hps.get('units_0')}")
```

**[SLIDE: Search Strategies]**

Keras Tuner supports three main search strategies:

- **RandomSearch**: Randomly samples from the hyperparameter space. Simple and surprisingly effective.

- **Hyperband**: An efficient elimination-based method. Quickly discards poor configurations and allocates more resources to promising ones.

- **BayesianOptimization**: Builds a probabilistic model of the objective function and selects the next point to evaluate based on expected improvement. Most sample-efficient.

For the certificate exam, know `RandomSearch` and `Hyperband` — these are the two explicitly mentioned in TensorFlow documentation.

---

## SEGMENT 4 — TensorFlow Lite (10:00–14:30)

**[SLIDE: The Deployment Gap]**

You have trained a model that achieves 94% accuracy. Now what? Most real applications do not run TensorFlow in a Python process on a server. They run on mobile phones, IoT sensors, microcontrollers, or edge devices. These environments have:

- Limited RAM (kilobytes to megabytes, not gigabytes)

- No GPU or specialized accelerators

- Battery constraints requiring minimal computation

TensorFlow Lite is Google's solution. It converts a standard TF/Keras model into a compact `.tflite` format optimized for inference on constrained hardware.

**[SCREEN SHARE — Code Editor]**

```python
# Standard TFLite conversion
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the .tflite file
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

import os
original_size = os.path.getsize('saved_model') if os.path.isdir('saved_model') else 0
tflite_size   = os.path.getsize('model.tflite')
print(f"TFLite model size: {tflite_size / 1024:.1f} KB")
```

Now let me show you post-training quantization — the single most impactful optimization for deployment:

```python
# Dynamic range quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant = converter.convert()

with open('model_quant.tflite', 'wb') as f:
    f.write(tflite_quant)

print(f"Original TFLite: {tflite_size / 1024:.1f} KB")
print(f"Quantized:       {len(tflite_quant) / 1024:.1f} KB")
```

Dynamic range quantization converts float32 weights to int8 at save time — typically reducing model size by 4x with minimal accuracy loss.

---

## SEGMENT 5 — Quantization in Depth (14:30–17:30)

**[SLIDE: Three Types of Quantization]**

There are three main quantization approaches in TF Lite:

**Dynamic Range Quantization** — weights are stored as int8, but inference happens in float32. Easiest to apply, no calibration data needed. Typically 2–4x size reduction.

**Full Integer Quantization** — both weights and activations are int8 during inference. Requires a small representative calibration dataset. Maximum speedup on integer-only hardware like Coral Edge TPU.

**Float16 Quantization** — weights stored as float16. GPU-friendly. 2x size reduction, minimal accuracy loss, good for GPU-accelerated edge devices.

```python
# Full integer quantization with representative dataset
def representative_data_gen():
    for sample in x_train[:100]:
        yield [sample.reshape(1, 28, 28).astype('float32')]

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_data_gen
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type  = tf.int8
converter.inference_output_type = tf.int8

tflite_int8 = converter.convert()
print(f"INT8 quantized size: {len(tflite_int8) / 1024:.1f} KB")
```

**[SLIDE: Running Inference with TFLite]**

```python
# TFLite inference
interpreter = tf.lite.Interpreter(model_content=tflite_quant)
interpreter.allocate_tensors()

input_details  = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Run one sample
interpreter.set_tensor(input_details[0]['index'],
                       x_val[0:1].reshape(1, 28, 28).astype('float32'))
interpreter.invoke()
output = interpreter.get_tensor(output_details[0]['index'])
print(f"Predicted class: {output.argmax()}")
```

---

## SEGMENT 6 — Pruning (17:30–19:30)

**[SLIDE: What Is Pruning?]**

Neural network pruning removes weights whose absolute values are near zero — weights that contribute almost nothing to the model's output. A well-pruned model can have 50–90% of its weights set to zero (sparse), resulting in a smaller file size after compression and faster inference on hardware that supports sparse computation.

TensorFlow Model Optimization Toolkit provides Keras-integrated pruning:

```python
import tensorflow_model_optimization as tfmot

pruning_schedule = tfmot.sparsity.keras.PolynomialDecay(
    initial_sparsity=0.0,
    final_sparsity=0.5,
    begin_step=0,
    end_step=1000
)

model_for_pruning = tfmot.sparsity.keras.prune_low_magnitude(
    model,
    pruning_schedule=pruning_schedule
)

model_for_pruning.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

callbacks = [tfmot.sparsity.keras.UpdatePruningStep()]

model_for_pruning.fit(
    x_train, y_train,
    epochs=5,
    validation_data=(x_val, y_val),
    callbacks=callbacks
)

# Strip pruning wrappers before export
model_pruned = tfmot.sparsity.keras.strip_pruning(model_for_pruning)
```

---

## SEGMENT 7 — TFX Pipelines Introduction (19:30–22:00)

**[SLIDE: From Notebook to Production]**

Everything we have built in this course has been in notebooks or scripts. In production, ML systems require:

- Repeatable data ingestion and validation

- Automated retraining when data distributions shift

- Model versioning and serving infrastructure

- Monitoring for prediction quality and data drift

TensorFlow Extended, or TFX, is Google's end-to-end platform for production ML. A TFX pipeline is a directed acyclic graph of components.

**[SLIDE: TFX Core Components]**

The core components you need to know:

- **ExampleGen**: Ingests raw data and splits into train/eval sets

- **StatisticsGen**: Computes dataset statistics

- **SchemaGen**: Infers a data schema for validation

- **ExampleValidator**: Detects anomalies against the schema

- **Transform**: Feature engineering using TF Transform

- **Trainer**: Trains the model using your model function

- **Evaluator**: Evaluates against a baseline; gates promotion

- **Pusher**: Deploys a validated model to a serving target

You do not need to implement a full TFX pipeline for this course or the certificate exam — but you should understand what each component does and why productionizing ML requires more than just `model.fit`.

---

## SEGMENT 8 — Wrap-Up and Certification Alignment (22:00–24:00)

**[ON CAMERA]**

Let's bring everything together.

Learning rate is the most impactful hyperparameter — use learning rate schedules and the range test to find good values. Keras Tuner automates hyperparameter search with `RandomSearch`, `Hyperband`, and `BayesianOptimization`. TensorFlow Lite converts trained models to a compact format for edge deployment. Quantization reduces model size 2–4x with minimal accuracy loss. Pruning sparsifies weights for further compression. TFX provides the infrastructure for repeatable, production-grade ML pipelines.

For the TensorFlow Developer Certificate, focus on:

- Building a `build_model(hp)` function with `hp.Int`, `hp.Float`, and `hp.Choice`

- Running `tuner.search()` and retrieving best hyperparameters

- Converting a Keras model to TFLite with `TFLiteConverter.from_keras_model`

- Applying dynamic range quantization with `converter.optimizations = [Optimize.DEFAULT]`

The lab for this module takes you through all of these steps on a real dataset. Pay special attention to the before-and-after model size comparison when you apply quantization — it is one of the most satisfying experiments in the course.

I will see you in Module 13. Take care.

---

*[End of Script — Module 12]*

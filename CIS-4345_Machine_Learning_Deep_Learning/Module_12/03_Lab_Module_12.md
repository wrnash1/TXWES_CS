# Lab: Module 12 — Model Optimization and Hyperparameter Tuning

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Lab Overview

In this lab you will apply the full optimization pipeline: automated hyperparameter search with Keras Tuner, TensorFlow Lite conversion, and post-training quantization. Working on the Fashion-MNIST dataset, you will find the best model architecture automatically, convert it to TFLite, apply dynamic range and full integer quantization, benchmark size and accuracy tradeoffs, and run inference through the TFLite interpreter.

**Estimated Time:** 90–120 minutes

**Prerequisites:** Module 12 video and reading guide completed

---

## Learning Objectives

By completing this lab you will be able to:

- Define a hypermodel using `hp.Int`, `hp.Float`, and `hp.Choice`
- Run `kt.RandomSearch` and `kt.Hyperband` searches and compare results
- Convert a trained Keras model to TFLite format
- Apply dynamic range and full integer quantization
- Measure and compare model size and validation accuracy across optimization stages
- Run inference using the TFLite `Interpreter` API

---

## Setup

```python
# Cell 1 — Install packages and import
import subprocess
subprocess.run(['pip', 'install', 'keras-tuner', '-q'])

import numpy as np
import tensorflow as tf
from tensorflow import keras
import keras_tuner as kt
import os
import matplotlib.pyplot as plt

print(f"TensorFlow: {tf.__version__}")
print(f"Keras Tuner: {kt.__version__}")
```

---

## Step 1 — Load and Prepare Data

```python
# Cell 2 — Load Fashion-MNIST
(x_train_full, y_train_full), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

# Normalize to [0, 1]
x_train_full = x_train_full.astype('float32') / 255.0
x_test        = x_test.astype('float32') / 255.0

# Reserve last 10,000 of training set for validation
x_train, x_val = x_train_full[:50000], x_train_full[50000:]
y_train, y_val = y_train_full[:50000], y_train_full[50000:]

CLASS_NAMES = [
    'T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

print(f"Train: {x_train.shape}, Val: {x_val.shape}, Test: {x_test.shape}")
```

```python
# Cell 3 — Visualize samples
plt.figure(figsize=(12, 4))
for i in range(12):
    plt.subplot(2, 6, i + 1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(CLASS_NAMES[y_train[i]], fontsize=8)
    plt.axis('off')
plt.suptitle("Fashion-MNIST Samples")
plt.tight_layout()
plt.show()
```

**Expected output:** A 2x6 grid of grayscale clothing images with class name titles.

---

## Step 2 — Define the Hypermodel

```python
# Cell 4 — Hypermodel definition
def build_model(hp):
    """
    Builds a dense classifier for Fashion-MNIST with searchable hyperparameters.
    """
    model = keras.Sequential(name="fashion_hypermodel")
    model.add(keras.layers.Flatten(input_shape=(28, 28)))

    # Search over number of hidden layers (1 to 3)
    n_layers = hp.Int('n_layers', min_value=1, max_value=3)

    for i in range(n_layers):
        units = hp.Int(
            f'units_{i}',
            min_value=64,
            max_value=512,
            step=64
        )
        activation = hp.Choice(
            f'activation_{i}',
            values=['relu', 'elu']
        )
        model.add(keras.layers.Dense(units, activation=activation))
        model.add(keras.layers.BatchNormalization())
        model.add(keras.layers.Dropout(
            hp.Float(f'dropout_{i}', min_value=0.1, max_value=0.5, step=0.1)
        ))

    # Output layer — always 10 classes
    model.add(keras.layers.Dense(10, activation='softmax'))

    # Searchable learning rate
    lr = hp.Choice('learning_rate', values=[1e-4, 5e-4, 1e-3, 3e-3])

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=lr),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

# Preview the search space
tuner_preview = kt.RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=1,
    directory='kt_preview',
    project_name='preview'
)
tuner_preview.search_space_summary()
```

**Expected output:** A summary listing all hyperparameters with their names, types, and ranges.

---

## Step 3 — Run RandomSearch

```python
# Cell 5 — RandomSearch tuner
rs_tuner = kt.RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=15,
    executions_per_trial=1,
    directory='kt_random',
    project_name='fashion_random',
    overwrite=True
)

stop_early = keras.callbacks.EarlyStopping(
    monitor='val_accuracy',
    patience=3,
    restore_best_weights=True
)

rs_tuner.search(
    x_train, y_train,
    epochs=15,
    validation_data=(x_val, y_val),
    callbacks=[stop_early],
    verbose=0
)

rs_best_hps = rs_tuner.get_best_hyperparameters(num_trials=1)[0]
print("\nRandomSearch — Best Hyperparameters:")
print(f"  n_layers:       {rs_best_hps.get('n_layers')}")
print(f"  learning_rate:  {rs_best_hps.get('learning_rate')}")
print(f"  units_0:        {rs_best_hps.get('units_0')}")
print(f"  dropout_0:      {rs_best_hps.get('dropout_0')}")
```

---

## Step 4 — Run Hyperband and Compare

```python
# Cell 6 — Hyperband tuner
hb_tuner = kt.Hyperband(
    build_model,
    objective='val_accuracy',
    max_epochs=20,
    factor=3,
    directory='kt_hyperband',
    project_name='fashion_hyperband',
    overwrite=True
)

hb_tuner.search(
    x_train, y_train,
    epochs=20,
    validation_data=(x_val, y_val),
    callbacks=[stop_early],
    verbose=0
)

hb_best_hps = hb_tuner.get_best_hyperparameters(num_trials=1)[0]
print("\nHyperband — Best Hyperparameters:")
print(f"  n_layers:       {hb_best_hps.get('n_layers')}")
print(f"  learning_rate:  {hb_best_hps.get('learning_rate')}")
print(f"  units_0:        {hb_best_hps.get('units_0')}")
```

```python
# Cell 7 — Build and train final models with best HPs
def train_best(tuner, best_hps, name):
    model = tuner.hypermodel.build(best_hps)
    history = model.fit(
        x_train, y_train,
        epochs=30,
        validation_data=(x_val, y_val),
        callbacks=[
            keras.callbacks.EarlyStopping(
                patience=5, restore_best_weights=True
            )
        ],
        verbose=0
    )
    val_acc = max(history.history['val_accuracy'])
    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
    print(f"{name}: val_acc={val_acc:.4f}, test_acc={test_acc:.4f}")
    return model, history

rs_model, rs_history   = train_best(rs_tuner, rs_best_hps, "RandomSearch")
hb_model, hb_history   = train_best(hb_tuner, hb_best_hps, "Hyperband  ")

# Choose the best model for the next steps
best_model = rs_model  # replace with hb_model if Hyperband wins
```

> **Checkpoint:** Record the test accuracy of both search strategies. They should both exceed 0.88. Note which strategy found a better configuration.

---

## Step 5 — TFLite Conversion (Float32 Baseline)

```python
# Cell 8 — Standard TFLite conversion (no quantization)
converter_fp32 = tf.lite.TFLiteConverter.from_keras_model(best_model)
tflite_fp32    = converter_fp32.convert()

with open('model_fp32.tflite', 'wb') as f:
    f.write(tflite_fp32)

size_fp32 = os.path.getsize('model_fp32.tflite')
print(f"Float32 TFLite size: {size_fp32 / 1024:.1f} KB")
```

---

## Step 6 — Dynamic Range Quantization

```python
# Cell 9 — Dynamic range quantization
converter_drq = tf.lite.TFLiteConverter.from_keras_model(best_model)
converter_drq.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_drq = converter_drq.convert()

with open('model_drq.tflite', 'wb') as f:
    f.write(tflite_drq)

size_drq = os.path.getsize('model_drq.tflite')
print(f"Dynamic range quantized size: {size_drq / 1024:.1f} KB")
print(f"Reduction vs float32: {size_fp32 / size_drq:.1f}x")
```

---

## Step 7 — Full Integer Quantization

```python
# Cell 10 — Full integer quantization with representative dataset
def representative_data_gen():
    for sample in x_val[:200]:
        yield [sample.reshape(1, 28, 28).astype('float32')]

converter_int8 = tf.lite.TFLiteConverter.from_keras_model(best_model)
converter_int8.optimizations = [tf.lite.Optimize.DEFAULT]
converter_int8.representative_dataset = representative_data_gen
converter_int8.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter_int8.inference_input_type  = tf.float32  # keep float I/O for simplicity
converter_int8.inference_output_type = tf.float32

tflite_int8 = converter_int8.convert()

with open('model_int8.tflite', 'wb') as f:
    f.write(tflite_int8)

size_int8 = os.path.getsize('model_int8.tflite')
print(f"Full INT8 quantized size: {size_int8 / 1024:.1f} KB")
print(f"Reduction vs float32: {size_fp32 / size_int8:.1f}x")
```

---

## Step 8 — Evaluate All TFLite Models

```python
# Cell 11 — TFLite accuracy evaluation helper
def evaluate_tflite(tflite_content, x_data, y_data, n_samples=1000):
    interpreter = tf.lite.Interpreter(model_content=tflite_content)
    interpreter.allocate_tensors()
    input_idx  = interpreter.get_input_details()[0]['index']
    output_idx = interpreter.get_output_details()[0]['index']

    correct = 0
    for i in range(n_samples):
        interpreter.set_tensor(
            input_idx,
            x_data[i].reshape(1, 28, 28).astype('float32')
        )
        interpreter.invoke()
        output = interpreter.get_tensor(output_idx)
        if output.argmax() == y_data[i]:
            correct += 1
    return correct / n_samples

print("Evaluating TFLite models on 1,000 test samples...")
acc_fp32 = evaluate_tflite(tflite_fp32, x_test, y_test)
acc_drq  = evaluate_tflite(tflite_drq,  x_test, y_test)
acc_int8 = evaluate_tflite(tflite_int8, x_test, y_test)

print(f"\nFloat32 TFLite accuracy:  {acc_fp32:.4f}")
print(f"Dynamic range accuracy:   {acc_drq:.4f}")
print(f"Full INT8 accuracy:       {acc_int8:.4f}")
```

---

## Step 9 — Summary Comparison Table and Plot

```python
# Cell 12 — Print comparison table
print("\n" + "="*60)
print(f"{'Model':<30} {'Size (KB)':>10} {'Accuracy':>10}")
print("="*60)
keras_acc = best_model.evaluate(x_test, y_test, verbose=0)[1]
print(f"{'Keras (float32)':<30} {'N/A':>10} {keras_acc:>10.4f}")
print(f"{'TFLite float32':<30} {size_fp32/1024:>10.1f} {acc_fp32:>10.4f}")
print(f"{'TFLite dynamic range':<30} {size_drq/1024:>10.1f} {acc_drq:>10.4f}")
print(f"{'TFLite full INT8':<30} {size_int8/1024:>10.1f} {acc_int8:>10.4f}")
print("="*60)
```

```python
# Cell 13 — Bar chart of model sizes
labels  = ['TFLite FP32', 'Dynamic Range', 'Full INT8']
sizes   = [size_fp32 / 1024, size_drq / 1024, size_int8 / 1024]
accuracies = [acc_fp32, acc_drq, acc_int8]
colors  = ['steelblue', 'darkorange', 'seagreen']

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(labels, sizes, color=colors)
axes[0].set_title("Model Size (KB)")
axes[0].set_ylabel("Size (KB)")
axes[0].grid(axis='y', alpha=0.3)

axes[1].bar(labels, accuracies, color=colors)
axes[1].set_ylim(0.8, 1.0)
axes[1].set_title("Test Accuracy")
axes[1].set_ylabel("Accuracy")
axes[1].grid(axis='y', alpha=0.3)

plt.suptitle("TFLite Quantization Comparison — Fashion-MNIST")
plt.tight_layout()
plt.show()
```

**Expected output:** Sizes should decrease significantly across the three variants. Accuracy should remain within 1–2 percentage points of the Keras baseline for both quantization methods.

---

## Deliverables

Submit a Jupyter notebook (.ipynb) with all cells executed containing:

1. The search space summary from Cell 4
2. Best hyperparameters from both RandomSearch and Hyperband (Cell 6–7)
3. Test accuracy for both tuned models
4. The comparison table from Cell 12 (all four rows filled in)
5. The bar chart comparing size and accuracy across quantization strategies (Cell 13)
6. A written paragraph (3–5 sentences) comparing the two tuning strategies and explaining which quantization method you would choose for a mobile deployment and why

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Data loaded and normalized correctly | 5 |
| Hypermodel defined with at least 3 searchable hyperparameter types | 15 |
| RandomSearch completes and best HPs are printed | 15 |
| Hyperband completes and best HPs are printed | 15 |
| TFLite float32 conversion succeeds with size printed | 10 |
| Dynamic range quantization applied and size printed | 10 |
| Full integer quantization applied with representative dataset | 10 |
| Comparison table complete with all four model rows | 10 |
| Bar chart present and correctly labeled | 5 |
| Written paragraph addresses tuning and quantization tradeoffs | 5 |
| **Total** | **100** |

---

*End of Lab — Module 12*

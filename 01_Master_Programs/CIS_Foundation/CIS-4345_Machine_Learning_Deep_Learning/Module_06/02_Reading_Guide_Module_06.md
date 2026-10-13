# Reading Guide: Module 06 — Training Deep Neural Networks

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

Knowing how to build a Keras model is necessary but not sufficient. This module covers the techniques that determine whether a trained model actually generalizes to new data. Callbacks, learning rate schedules, batch normalization, dropout, and proper evaluation are all tested on the TensorFlow Developer Certificate and appear in every serious production ML system.

---

## Section 1 — The Training Loop and History Object

`model.fit()` executes the training loop and returns a `History` object.

```python
history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_data=(X_val, y_val),
    callbacks=[...],
    verbose=1
)
```

The `history.history` attribute is a dictionary mapping metric names to lists of per-epoch values:

```python
# Keys present when validation_data is provided
print(history.history.keys())
# dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])
```

### Plotting Training Curves

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.title('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.title('Accuracy')
plt.legend()

plt.tight_layout()
plt.show()
```

### Diagnosing from Training Curves

| Observation | Diagnosis | Action |
|---|---|---|
| Both losses high | Underfitting | Increase model capacity, train longer |
| Train loss low, val loss high | Overfitting | Add dropout, L2 reg, or more data |
| Both losses decrease together | Healthy training | Continue or fine-tune |
| Val loss increases after plateau | Overfitting onset | Use EarlyStopping |
| Loss oscillates wildly | LR too high | Reduce learning rate |
| Loss barely changes | LR too low | Increase learning rate |

---

## Section 2 — Callbacks

Callbacks are objects passed to `model.fit()` that can intercept the training loop and execute logic at defined points — end of batch, end of epoch, end of training.

### EarlyStopping

Halts training when a monitored metric stops improving.

```python
tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',      # metric to watch
    patience=10,             # epochs to wait before stopping
    restore_best_weights=True,  # revert to best epoch on stop
    min_delta=1e-4           # minimum change to count as improvement
)
```

Key parameters:

- `monitor`: almost always `'val_loss'` — use validation, not training metric
- `patience`: how many non-improving epochs to tolerate before stopping
- `restore_best_weights=True`: critical — without this, you keep the final (potentially overfit) weights, not the best ones

### ModelCheckpoint

Saves the model to disk when the monitored metric improves.

```python
tf.keras.callbacks.ModelCheckpoint(
    filepath='best_model.keras',
    monitor='val_loss',
    save_best_only=True,
    save_weights_only=False,
    verbose=1
)
```

`save_best_only=True` overwrites the saved file only when the monitored metric improves. `save_weights_only=True` saves only the weights (smaller file) rather than the full model.

### ReduceLROnPlateau

Reduces the learning rate by a factor when improvement stalls.

```python
tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,       # multiply LR by this when triggered
    patience=5,       # epochs to wait before reducing
    min_lr=1e-7,      # lower bound on learning rate
    verbose=1
)
```

Typical usage: pair with EarlyStopping. ReduceLROnPlateau fires first (patience=5), then EarlyStopping fires later (patience=15) if the reduced LR still does not help.

### LearningRateScheduler

Applies a custom function to update the learning rate each epoch.

```python
def schedule(epoch, lr):
    if epoch < 10:
        return lr
    else:
        return float(lr * 0.95)

tf.keras.callbacks.LearningRateScheduler(schedule, verbose=1)
```

### Custom Callback

You can write your own callback by subclassing `tf.keras.callbacks.Callback`:

```python
class PrintLR(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        current_lr = self.model.optimizer.learning_rate
        print(f"\nEpoch {epoch+1}: LR = {float(current_lr):.6f}")
```

### Callback Methods Available

| Method | When it fires |
|---|---|
| `on_train_begin` | Start of `model.fit()` |
| `on_epoch_begin(epoch, logs)` | Start of each epoch |
| `on_batch_end(batch, logs)` | End of each training batch |
| `on_epoch_end(epoch, logs)` | End of each epoch |
| `on_train_end(logs)` | End of `model.fit()` |

---

## Section 3 — Learning Rate Schedules

### Why Schedule the Learning Rate?

A fixed learning rate is a compromise between exploration (high LR, fast but unstable) and exploitation (low LR, precise but slow). Scheduling lets you have both: explore early, refine late.

### ExponentialDecay

```python
schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.01,
    decay_steps=1000,
    decay_rate=0.96,
    staircase=False    # True = step-wise, False = smooth decay
)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=schedule), ...)
```

LR at step `t` = `initial_lr * decay_rate ^ (t / decay_steps)`

### CosineDecay

Decays the learning rate following a cosine curve, which tends to give smooth convergence.

```python
schedule = tf.keras.optimizers.schedules.CosineDecay(
    initial_learning_rate=0.01,
    decay_steps=5000
)
```

### Comparison of Schedule Types

| Schedule | Shape | Best For |
|---|---|---|
| Constant | Flat line | Baselines, simple problems |
| Exponential Decay | Smooth curve downward | General-purpose default |
| Cosine Decay | S-curve downward | Fine-tuning, modern training |
| ReduceLROnPlateau | Step-wise, reactive | When plateau timing is unpredictable |
| Warm-up + Decay | Rise then fall | Transformer models, large LR training |

---

## Section 4 — Batch Normalization

### The Problem It Solves

As training progresses, the distribution of each layer's inputs shifts because the weights of previous layers change. This is called **internal covariate shift**. Layers must constantly adapt to changing input distributions, which slows training.

Batch normalization normalizes each layer's pre-activation (or post-activation, depending on placement) across the training batch.

### The Computation

For a mini-batch of activations `x`:

```
mu = mean(x over batch)
sigma = std(x over batch)
x_norm = (x - mu) / (sigma + epsilon)
output = gamma * x_norm + beta
```

`gamma` (scale) and `beta` (shift) are learnable parameters — the network can undo the normalization if needed.

During inference, batch statistics are replaced with running statistics accumulated during training (exponential moving average).

### Placement

```python
# Style 1: BN before activation (original paper)
tf.keras.layers.Dense(128),
tf.keras.layers.BatchNormalization(),
tf.keras.layers.Activation('relu'),

# Style 2: BN after activation (common in practice)
tf.keras.layers.Dense(128, activation='relu'),
tf.keras.layers.BatchNormalization(),
```

Both styles are acceptable. Style 1 (before activation) is the original formulation. Use either consistently within a model.

### Benefits of Batch Normalization

- Allows higher learning rates without instability
- Reduces sensitivity to weight initialization
- Provides mild regularization effect
- Significantly accelerates training convergence

### Exam Tip

BatchNormalization adds `4 * features` parameters to a model: gamma, beta (learnable) and mean, variance (non-trainable moving averages). A `BatchNormalization()` layer after a `Dense(128)` adds `4 * 128 = 512` parameters, of which `2 * 128 = 256` are trainable and `256` are non-trainable.

---

## Section 5 — Dropout

Dropout is a regularization technique that randomly sets a fraction of neuron outputs to zero during each training step.

### How It Works

During training: each unit is independently zeroed with probability `p` (the dropout rate).

During inference: all units are active, but their outputs are scaled by `(1 - p)` to maintain the same expected output magnitude. Keras handles this scaling automatically.

```python
tf.keras.layers.Dropout(rate=0.5)   # 50% of neurons zeroed each step
```

### Why It Works

Dropout forces the network to learn redundant representations. No single neuron can be relied upon to carry critical information because it might not be present in the next training step. This produces more robust, distributed feature representations.

### Placement Guidelines

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(256, activation='relu', input_shape=(100,)),
    tf.keras.layers.Dropout(0.4),       # after large hidden layers

    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.3),       # lower rate deeper in network

    tf.keras.layers.Dense(1, activation='sigmoid')
    # no dropout on output layer
])
```

### Dropout Rate Guidelines

| Layer Position | Typical Rate |
|---|---|
| First hidden layer | 0.2–0.4 |
| Middle hidden layers | 0.3–0.5 |
| Final hidden layer | 0.1–0.3 |
| Output layer | Never use dropout |

### training=True vs. training=False

Dropout behaves differently during training and inference. In `model.fit()`, Keras passes `training=True` automatically. In `model.predict()` and `model.evaluate()`, it passes `training=False`. In custom training loops, you must pass this argument explicitly:

```python
# Training step — dropout active
output = model(x_batch, training=True)

# Inference — dropout disabled
output = model(x_batch, training=False)
```

---

## Section 6 — Model Evaluation

### evaluate()

```python
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
```

Returns the values of all compiled metrics on the test set. This is the definitive performance measurement — always evaluate on a held-out test set that was never used during training or validation.

### predict()

```python
probabilities = model.predict(X_test)           # raw output
labels = (probabilities > 0.5).astype(int)      # binary threshold
class_ids = np.argmax(probabilities, axis=1)    # multi-class argmax
```

### Beyond Accuracy

```python
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

y_pred = (model.predict(X_test) > 0.5).astype(int).flatten()
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=['Class 0', 'Class 1']))
```

Classification report gives precision, recall, F1-score, and support for each class. For imbalanced datasets this is far more informative than accuracy alone.

---

## Section 7 — Combining Techniques: A Reference Template

```python
# Architecture with BatchNorm + Dropout
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape=(n_features,)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.Dropout(0.3),

    tf.keras.layers.Dense(64),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.Dropout(0.2),

    tf.keras.layers.Dense(n_outputs, activation='softmax')
])

# Compile
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Callbacks
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=15, restore_best_weights=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.5, patience=5, min_lr=1e-7
    ),
    tf.keras.callbacks.ModelCheckpoint(
        'best_model.keras', monitor='val_loss', save_best_only=True
    )
]

# Train
history = model.fit(
    X_train, y_train,
    epochs=300,
    batch_size=32,
    validation_data=(X_val, y_val),
    callbacks=callbacks,
    verbose=1
)
```

---

## Section 8 — Exam Tips

- `restore_best_weights=True` in EarlyStopping is critical. Without it, training stops but keeps the final (potentially worse) weights rather than the best ones.
- `save_best_only=True` in ModelCheckpoint prevents disk from filling with every epoch's weights.
- BatchNormalization adds non-trainable parameters (moving mean and variance). `model.summary()` shows these separately under "Non-trainable params."
- Dropout is automatically disabled during `model.predict()` and `model.evaluate()`. You never need to manually toggle it.
- `model.evaluate()` returns values in the order they were specified in `metrics=[]` during compile, preceded by the loss value.
- The `patience` parameter in both EarlyStopping and ReduceLROnPlateau is in units of epochs, not batches.

---

## Study Checklist

- [ ] Implement EarlyStopping with `restore_best_weights=True` and verify training stops before the specified epoch count
- [ ] Add BatchNormalization to a model and check `model.summary()` for non-trainable parameter count
- [ ] Add Dropout and verify predictions do not change between two calls to `model.predict()` (dropout is off during inference)
- [ ] Plot training and validation loss curves and identify the epoch where overfitting begins
- [ ] Complete Module 06 Lab
- [ ] Complete Module 06 Quiz
- [ ] Post to Module 06 Discussion Board by Wednesday 11:59 PM

---

## 9. Supplemental Resources

**1. Keras Callbacks API Reference**
<https://www.tensorflow.org/api_docs/python/tf/keras/callbacks>
Complete API documentation for all built-in Keras callbacks: `EarlyStopping`, `ModelCheckpoint`, `ReduceLROnPlateau`, `LearningRateScheduler`, `TensorBoard`, and `CSVLogger`. Each entry includes all constructor parameters with types, defaults, and usage examples — the authoritative reference when configuring callbacks for TF Developer Certificate exam tasks.

**2. Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift (original paper)**
<https://arxiv.org/abs/1502.03167>
The Ioffe and Szegedy (2015) paper that introduced batch normalization. Section 3 explains the mathematical formulation (gamma, beta, running mean, running variance) used in Keras `BatchNormalization`. Reading the abstract and Section 3 directly supports the parameter count and placement questions in this module's quiz and lab.

**3. Dropout: A Simple Way to Prevent Neural Networks from Overfitting (original paper)**
<https://jmlr.org/papers/v15/srivastava14a.html>
The Srivastava et al. (2014) JMLR paper introducing dropout. Section 2 explains inverted dropout scaling (why `model.predict()` does not need to scale outputs) and Section 3 covers placement guidelines. The experiments in Section 5 provide concrete evidence for the dropout rates recommended in this module's placement guidelines table.

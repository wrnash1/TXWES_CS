# Lab: Module 06 — Training Deep Neural Networks

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Lab Overview

In this lab you will train three versions of the same neural network on a real dataset — a baseline model with no regularization, a model with dropout only, and a model with both batch normalization and dropout. You will add callbacks to each training run, plot and compare training curves, evaluate all three on a held-out test set, and analyze the results.

**Estimated Time:** 75–100 minutes

**Tools Required:** Python 3.9+, TensorFlow 2.x, NumPy, Matplotlib, scikit-learn, Google Colab or local Jupyter environment

---

## Learning Objectives

By the end of this lab you will be able to:

- Configure EarlyStopping, ModelCheckpoint, and ReduceLROnPlateau callbacks
- Apply dropout regularization to a Sequential model
- Insert BatchNormalization layers correctly in a model architecture
- Compare training curves across three model variants
- Evaluate models using `model.evaluate()` and `classification_report`
- Interpret the relationship between training and validation metrics

---

## Part 1 — Dataset and Preprocessing

### Step 1.1 — Setup

```python
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

np.random.seed(42)
tf.random.set_seed(42)

print("TensorFlow:", tf.__version__)
```

### Step 1.2 — Generate Dataset

```python
X, y = make_classification(
    n_samples=5000,
    n_features=30,
    n_informative=15,
    n_redundant=5,
    n_classes=2,
    class_sep=0.8,
    random_state=42
)

y = y.astype(np.float32)

X_temp, X_test, y_temp, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42
)
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.18, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train).astype(np.float32)
X_val   = scaler.transform(X_val).astype(np.float32)
X_test  = scaler.transform(X_test).astype(np.float32)

print(f"Train: {X_train.shape}, Val: {X_val.shape}, Test: {X_test.shape}")
```

### Step 1.3 — Check Class Balance

```python
unique, counts = np.unique(y_train, return_counts=True)
print("Class distribution (train):", dict(zip(unique.astype(int), counts)))
```

**Checkpoint:** Confirm the class distribution is roughly balanced (around 50/50). Imbalanced classes would require different evaluation strategies.

---

## Part 2 — Baseline Model (No Regularization)

### Step 2.1 — Build and Compile

```python
def build_baseline(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(256, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64,  activation='relu'),
        tf.keras.layers.Dense(1,   activation='sigmoid')
    ], name='baseline')
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

model_baseline = build_baseline(X_train.shape[1])
model_baseline.summary()
```

### Step 2.2 — Define Callbacks

```python
callbacks_baseline = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=15,
        restore_best_weights=True,
        verbose=1
    ),
    tf.keras.callbacks.ModelCheckpoint(
        filepath='baseline_best.keras',
        monitor='val_loss',
        save_best_only=True,
        verbose=0
    )
]
```

### Step 2.3 — Train

```python
history_baseline = model_baseline.fit(
    X_train, y_train,
    epochs=200,
    batch_size=64,
    validation_data=(X_val, y_val),
    callbacks=callbacks_baseline,
    verbose=0
)

print(f"Baseline stopped at epoch: {len(history_baseline.history['loss'])}")
```

---

## Part 3 — Dropout Model

### Step 3.1 — Build and Compile

```python
def build_dropout(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(256, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dropout(0.4),

        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.3),

        tf.keras.layers.Dense(64,  activation='relu'),
        tf.keras.layers.Dropout(0.2),

        tf.keras.layers.Dense(1, activation='sigmoid')
    ], name='dropout_model')
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

model_dropout = build_dropout(X_train.shape[1])
model_dropout.summary()
```

### Step 3.2 — Train with Full Callback Suite

```python
callbacks_dropout = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=15, restore_best_weights=True, verbose=1
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.5, patience=5, min_lr=1e-7, verbose=1
    ),
    tf.keras.callbacks.ModelCheckpoint(
        filepath='dropout_best.keras', monitor='val_loss', save_best_only=True
    )
]

history_dropout = model_dropout.fit(
    X_train, y_train,
    epochs=200,
    batch_size=64,
    validation_data=(X_val, y_val),
    callbacks=callbacks_dropout,
    verbose=0
)

print(f"Dropout model stopped at epoch: {len(history_dropout.history['loss'])}")
```

---

## Part 4 — BatchNorm + Dropout Model

### Step 4.1 — Build and Compile

```python
def build_batchnorm_dropout(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(256, input_shape=(input_dim,)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Activation('relu'),
        tf.keras.layers.Dropout(0.3),

        tf.keras.layers.Dense(128),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Activation('relu'),
        tf.keras.layers.Dropout(0.2),

        tf.keras.layers.Dense(64),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Activation('relu'),

        tf.keras.layers.Dense(1, activation='sigmoid')
    ], name='batchnorm_dropout')
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

model_bn = build_batchnorm_dropout(X_train.shape[1])
model_bn.summary()
```

**Checkpoint:** In `model_bn.summary()`, locate the "Non-trainable params" row. This counts the BatchNormalization moving mean and variance tensors. Calculate how many non-trainable parameters you expect: each BatchNorm layer on a Dense(N) adds `2*N` non-trainable params (mean + variance per feature).

### Step 4.2 — Train

```python
callbacks_bn = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=15, restore_best_weights=True, verbose=1
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.5, patience=5, min_lr=1e-7, verbose=1
    ),
    tf.keras.callbacks.ModelCheckpoint(
        filepath='bn_best.keras', monitor='val_loss', save_best_only=True
    )
]

history_bn = model_bn.fit(
    X_train, y_train,
    epochs=200,
    batch_size=64,
    validation_data=(X_val, y_val),
    callbacks=callbacks_bn,
    verbose=0
)

print(f"BN+Dropout model stopped at epoch: {len(history_bn.history['loss'])}")
```

---

## Part 5 — Compare Training Curves

### Step 5.1 — Plot All Three Models Side by Side

```python
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

configs = [
    (history_baseline, 'Baseline', 0),
    (history_dropout,  'Dropout',  1),
    (history_bn,       'BN+Dropout', 2)
]

for hist, title, col in configs:
    n_epochs = len(hist.history['loss'])

    axes[0, col].plot(hist.history['loss'],     label='Train Loss')
    axes[0, col].plot(hist.history['val_loss'], label='Val Loss')
    axes[0, col].set_title(f'{title} — Loss (stopped ep {n_epochs})')
    axes[0, col].set_xlabel('Epoch')
    axes[0, col].legend()

    axes[1, col].plot(hist.history['accuracy'],     label='Train Acc')
    axes[1, col].plot(hist.history['val_accuracy'], label='Val Acc')
    axes[1, col].set_title(f'{title} — Accuracy')
    axes[1, col].set_xlabel('Epoch')
    axes[1, col].legend()

plt.tight_layout()
plt.savefig('module06_comparison_curves.png', dpi=150)
plt.show()
```

---

## Part 6 — Evaluate All Three Models

### Step 6.1 — Test Set Evaluation

```python
results = {}
for model, name in [(model_baseline, 'Baseline'),
                    (model_dropout,  'Dropout'),
                    (model_bn,       'BN+Dropout')]:
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    results[name] = {'loss': loss, 'accuracy': acc}
    print(f"{name:15s}  Test Loss: {loss:.4f}  Test Accuracy: {acc:.4f}")
```

### Step 6.2 — Classification Reports

```python
for model, name in [(model_baseline, 'Baseline'),
                    (model_dropout,  'Dropout'),
                    (model_bn,       'BN+Dropout')]:
    preds = (model.predict(X_test, verbose=0) > 0.5).astype(int).flatten()
    print(f"\n--- {name} ---")
    print(classification_report(y_test.astype(int), preds,
                                 target_names=['Class 0', 'Class 1']))
```

---

## Part 7 — Dropout Inference Verification

This step verifies that dropout is correctly disabled during inference.

```python
sample = X_test[:1]

pred_1 = model_dropout.predict(sample, verbose=0)
pred_2 = model_dropout.predict(sample, verbose=0)
pred_3 = model_dropout.predict(sample, verbose=0)

print("Prediction 1:", pred_1[0][0])
print("Prediction 2:", pred_2[0][0])
print("Prediction 3:", pred_3[0][0])
print("All identical:", np.allclose(pred_1, pred_2) and np.allclose(pred_2, pred_3))
```

**Expected result:** All three predictions should be identical. If they differ, dropout is incorrectly active during inference — this indicates a custom layer or training mode issue.

---

## Deliverables

Submit the following to Canvas by the module deadline:

1. Completed notebook (.ipynb) with all cells executed
2. Comparison plot saved as `module06_comparison_curves.png`
3. Table in a markdown cell comparing test loss and test accuracy for all three models
4. Written answers to the three reflection questions below
5. Output of the dropout inference verification (Step 7) confirming identical predictions

---

## Reflection Questions

Answer these in a markdown cell in your notebook:

1. Looking at your training curves, which model shows the clearest overfitting in the baseline? At approximately which epoch does the validation loss begin to diverge from training loss? What does this tell you about the appropriate number of epochs to train this architecture without regularization?

2. The BatchNorm + Dropout model has more parameters than the Dropout-only model, yet it may converge faster. Explain the mechanism by which BatchNormalization accelerates convergence, referencing the concept of internal covariate shift.

3. ReduceLROnPlateau fired during training for at least one of your models. Describe what happened to the training loss curve after the learning rate was reduced. Did the reduction help, or did EarlyStopping fire soon after? What does this suggest about the relationship between these two callbacks?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| All three models train without errors and stop via EarlyStopping | 20 |
| Comparison plot generated with all 6 subplots labeled | 20 |
| Test evaluation table with all three model results | 15 |
| Dropout inference verification shows identical predictions | 10 |
| Non-trainable parameter calculation for BN model (Part 4 checkpoint) | 10 |
| Three reflection questions answered in complete sentences | 25 |
| **Total** | **100** |

---

## Common Errors and Fixes

**EarlyStopping does not trigger before epoch 200:** Increase `patience` or check that `monitor='val_loss'` is spelled correctly. A typo like `'val_loss '` (with a space) causes the callback to silently ignore the metric.

**restore_best_weights has no effect:** Ensure `restore_best_weights=True` is set. Without it, training stops but the model retains the last epoch's weights, not the best ones.

**BatchNorm non-trainable params seem too high or low:** Each BatchNorm layer on `Dense(N)` adds `2*N` non-trainable params (mean and variance). A model with three BatchNorm layers on Dense(256), Dense(128), Dense(64) adds `2*(256+128+64) = 896` non-trainable params.

**Dropout inference predictions differ between calls:** Verify you are calling `model.predict()` not `model(x, training=True)`. The `predict()` method always runs in inference mode.

---

## Part 9 — Challenge Exercise

### Challenge 1: Comparing EarlyStopping Patience Values

Train the same dropout model four times with `patience` values of 5, 10, 20, and 50, and compare how the chosen stopping epoch and final test accuracy differ across runs.

```python
import numpy as np
import tensorflow as tf
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

np.random.seed(42)
tf.random.set_seed(42)

X, y = make_classification(n_samples=5000, n_features=30, n_informative=15,
                            n_redundant=5, random_state=42)
y = y.astype(np.float32)

X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.18, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train).astype(np.float32)
X_val   = scaler.transform(X_val).astype(np.float32)
X_test  = scaler.transform(X_test).astype(np.float32)

def build_dropout(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(256, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dropout(0.4),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

patience_values = [5, 10, 20, 50]
results = {}

for p in patience_values:
    tf.random.set_seed(42)
    model = build_dropout(X_train.shape[1])
    cb = [
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss', patience=p, restore_best_weights=True
        )
    ]
    hist = model.fit(X_train, y_train, epochs=300, batch_size=64,
                     validation_data=(X_val, y_val), callbacks=cb, verbose=0)
    stopped_epoch = len(hist.history['loss'])
    _, test_acc = model.evaluate(X_test, y_test, verbose=0)
    results[p] = {'stopped_epoch': stopped_epoch, 'test_acc': test_acc}
    print(f"patience={p:3d} | stopped at epoch {stopped_epoch:3d} | test acc={test_acc:.4f}")

# Plot: stopped epoch and test accuracy by patience
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.bar([str(p) for p in patience_values], [results[p]['stopped_epoch'] for p in patience_values], color='steelblue')
ax1.set_title('Stopped Epoch by Patience')
ax1.set_xlabel('Patience')
ax1.set_ylabel('Epoch')

ax2.bar([str(p) for p in patience_values], [results[p]['test_acc'] for p in patience_values], color='coral')
ax2.set_ylim(0.8, 1.0)
ax2.set_title('Test Accuracy by Patience')
ax2.set_xlabel('Patience')
ax2.set_ylabel('Accuracy')

plt.tight_layout()
plt.savefig('patience_comparison.png', dpi=100)
plt.show()
```

1. Which patience value produced the best test accuracy? Was there a large difference between the best and worst?
2. Did higher patience consistently lead to better test accuracy, or did diminishing returns appear? Explain why a very high patience value (50) might not always outperform a moderate one (10 or 20).

### Challenge 2: Learning Rate Schedule vs. ReduceLROnPlateau

Compare two training runs on the same architecture: one using a fixed Adam learning rate of 0.001, and one using `ExponentialDecay`. Plot the learning rate over epochs for the scheduled run and compare final validation accuracy.

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Reuse X_train, X_val, X_test, y_train, y_val, y_test from Challenge 1

def build_model(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(256, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

# Run 1: Fixed LR
tf.random.set_seed(42)
model_fixed = build_model(X_train.shape[1])
model_fixed.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                    loss='binary_crossentropy', metrics=['accuracy'])
hist_fixed = model_fixed.fit(X_train, y_train, epochs=80, batch_size=64,
                              validation_data=(X_val, y_val), verbose=0)

# Run 2: ExponentialDecay schedule
tf.random.set_seed(42)
steps_per_epoch = len(X_train) // 64
schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.005,
    decay_steps=steps_per_epoch * 10,   # decay every 10 epochs
    decay_rate=0.7,
    staircase=True
)
model_sched = build_model(X_train.shape[1])
model_sched.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=schedule),
                    loss='binary_crossentropy', metrics=['accuracy'])

# Track LR per epoch with a custom callback
lr_history = []
class LRTracker(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        lr_history.append(float(self.model.optimizer.learning_rate(
            self.model.optimizer.iterations)))

hist_sched = model_sched.fit(X_train, y_train, epochs=80, batch_size=64,
                              validation_data=(X_val, y_val),
                              callbacks=[LRTracker()], verbose=0)

# Plot comparison
fig, axes = plt.subplots(1, 3, figsize=(18, 4))

axes[0].plot(hist_fixed.history['val_accuracy'], label='Fixed LR')
axes[0].plot(hist_sched.history['val_accuracy'], label='Exp Decay')
axes[0].set_title('Val Accuracy Comparison')
axes[0].set_xlabel('Epoch')
axes[0].legend()

axes[1].plot(hist_fixed.history['val_loss'], label='Fixed LR')
axes[1].plot(hist_sched.history['val_loss'], label='Exp Decay')
axes[1].set_title('Val Loss Comparison')
axes[1].set_xlabel('Epoch')
axes[1].legend()

axes[2].plot(lr_history, color='green')
axes[2].set_title('Learning Rate (Exp Decay)')
axes[2].set_xlabel('Epoch')
axes[2].set_ylabel('LR')

plt.tight_layout()
plt.savefig('lr_schedule_comparison.png', dpi=100)
plt.show()

print(f"Fixed LR  final val_acc: {hist_fixed.history['val_accuracy'][-1]:.4f}")
print(f"Exp Decay final val_acc: {hist_sched.history['val_accuracy'][-1]:.4f}")
```

1. At which epoch does the `ExponentialDecay` schedule produce its largest step-down in learning rate? Does the validation loss curve show a corresponding improvement after that step-down?
2. `ReduceLROnPlateau` is reactive (fires when improvement stalls) while `ExponentialDecay` is proactive (fires on a fixed schedule). Describe a training scenario where each approach would be preferable over the other.

### Part 9 Reflection Questions

1. In Challenge 1, setting `patience=5` stops training quickly but may discard a model that would have improved further. Setting `patience=50` risks overfitting before stopping. What is the practical tradeoff, and how does `restore_best_weights=True` change this tradeoff?
2. In Challenge 2, the `LRTracker` callback reads `self.model.optimizer.learning_rate(self.model.optimizer.iterations)` to get the current scheduled LR. Why is calling the schedule object as a function (passing the step count) necessary rather than reading `learning_rate` directly as a scalar attribute?

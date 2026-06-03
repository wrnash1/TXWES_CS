# Video Script: Module 06 — Training Deep Neural Networks

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: TensorFlow Developer Certificate

---

## Pre-Roll Slide (on screen while intro plays)

**Topic:** Training Deep Neural Networks

**Objectives:** Master callbacks, learning rate schedules, batch normalization, dropout, early stopping, and model evaluation.

---

## SEGMENT 1 — Introduction (0:00–1:30)

[Camera: Instructor on screen]

Welcome to Module 6 of CIS-4345. I am Professor Nash. In Modules 4 and 5 you learned how neural networks work mathematically and how to build them in Keras. Today we focus on training them well.

There is a significant gap between a model that runs and a model that generalizes. The tools we cover today are what close that gap. Every concept in this module directly maps to questions on the TensorFlow Developer Certificate exam.

Here is what we are covering:

- Callbacks — intercepting and controlling training
- Early stopping — halting training at the right moment
- Learning rate schedules — adjusting the learning rate during training
- Batch normalization — stabilizing layer activations
- Dropout — regularization through random deactivation
- Model evaluation — interpreting loss, accuracy, and generalization

Let us get into it.

---

## SEGMENT 2 — The model.fit() Training Loop (1:30–3:30)

[Screen: Code demonstration]

Before we discuss the techniques, let me show you the full `model.fit()` call with all its parameters so you understand what we are working with.

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

`model.fit()` returns a `History` object. The `history.history` dictionary contains training metrics by epoch:

```python
print(history.history.keys())
# dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])

import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label='Train')
plt.plot(history.history['val_loss'], label='Validation')
plt.legend()
plt.show()
```

[Camera: Instructor]

The gap between training loss and validation loss is your primary diagnostic. A small gap means the model is generalizing. A large gap means overfitting. We will use all the tools in this module to manage that gap.

---

## SEGMENT 3 — Callbacks (3:30–7:00)

[Screen: Code demonstration]

A **callback** is an object that can intercept the training loop at specific points — at the start of an epoch, at the end of an epoch, at the end of a batch — and execute custom logic.

Callbacks are passed as a list to the `callbacks` parameter of `model.fit()`.

### ModelCheckpoint

Saves the model whenever a monitored metric improves:

```python
checkpoint = tf.keras.callbacks.ModelCheckpoint(
    filepath='best_model.keras',
    monitor='val_loss',
    save_best_only=True,
    verbose=1
)
```

`save_best_only=True` means only the best version is kept on disk — not every epoch. This is almost always what you want.

### EarlyStopping

Stops training when a monitored metric stops improving:

```python
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)
```

`patience=10` means training continues for 10 more epochs after the metric stops improving, giving it a chance to recover. `restore_best_weights=True` resets the model weights back to the best epoch after stopping.

### ReduceLROnPlateau

Reduces the learning rate when a metric has stopped improving:

```python
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=5,
    min_lr=1e-6,
    verbose=1
)
```

`factor=0.5` cuts the learning rate in half when triggered. `min_lr` prevents it from shrinking below a useful threshold.

### TensorBoard

Logs training metrics for visualization in the TensorBoard dashboard:

```python
tensorboard = tf.keras.callbacks.TensorBoard(
    log_dir='./logs',
    histogram_freq=1
)
```

[Camera: Instructor]

In practice, a typical training call looks like this:

```python
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=10, restore_best_weights=True
    ),
    tf.keras.callbacks.ModelCheckpoint(
        'best_model.keras', monitor='val_loss', save_best_only=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.5, patience=5
    )
]

history = model.fit(
    X_train, y_train,
    epochs=200,
    batch_size=32,
    validation_data=(X_val, y_val),
    callbacks=callbacks
)
```

You set `epochs=200` as an upper bound and let EarlyStopping decide when to actually stop.

---

## SEGMENT 4 — Learning Rate Schedules (7:00–10:00)

[Slide: Learning rate vs. epoch curves]

Beyond ReduceLROnPlateau, which reacts to plateaus, you can also schedule the learning rate proactively with a predefined schedule.

### Exponential Decay

```python
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.01,
    decay_steps=1000,
    decay_rate=0.96,
    staircase=True
)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=lr_schedule),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

The learning rate decays by a factor of 0.96 every 1000 steps. `staircase=True` makes the decay step-wise rather than continuous.

### Learning Rate Warm-up

A common trick in modern deep learning: start with a very small learning rate and increase it for the first few epochs, then decay. This avoids large, destabilizing updates at initialization when weights are random.

```python
def warmup_schedule(epoch, lr):
    if epoch < 5:
        return float(epoch + 1) * 1e-4   # ramp up
    else:
        return lr * 0.95                  # decay

lr_callback = tf.keras.callbacks.LearningRateScheduler(warmup_schedule)
```

[Camera: Instructor]

The key intuition: a high learning rate early in training explores the loss landscape broadly. A lower learning rate later finds the precise minimum. Scheduling exploits both phases deliberately rather than committing to one rate throughout.

---

## SEGMENT 5 — Batch Normalization (10:00–13:30)

[Slide: Network diagram showing batch norm layer placement]

Batch normalization is one of the most impactful techniques in deep learning. It normalizes the activations of a layer across each training batch, keeping them in a stable range during training.

What it does mathematically: for each activation in a layer, it computes the mean and variance across the batch, normalizes to zero mean and unit variance, then scales and shifts with learnable parameters gamma and beta.

`x_normalized = (x - batch_mean) / (batch_std + epsilon)`

`output = gamma * x_normalized + beta`

The gamma and beta parameters are learned during training, allowing the network to undo the normalization if that is optimal.

### Benefits

- Allows higher learning rates — normalized activations are less sensitive to initialization
- Reduces the problem of internal covariate shift
- Acts as a mild regularizer, sometimes reducing the need for dropout
- Significantly speeds up training in many architectures

### Placement in Keras

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape=(50,)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),

    tf.keras.layers.Dense(64),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),

    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

[Camera: Instructor]

There is an ongoing debate about whether BatchNorm should go before or after the activation function. The original paper placed it before. Many practitioners today place it after. For the exam, either placement is acceptable — just be consistent within a model.

An important detail for inference: during `model.predict()` or `model.evaluate()`, batch normalization uses running statistics accumulated during training rather than the current batch statistics. This means BatchNorm behaves slightly differently during training and inference — always pass `training=False` when making predictions if you are using a custom training loop.

---

## SEGMENT 6 — Dropout (13:30–17:00)

[Slide: Network diagram with neurons crossed out]

Dropout is a regularization technique that randomly deactivates a fraction of neurons during each training step. This prevents the network from relying too heavily on any single neuron and forces it to learn more distributed, redundant representations.

During training: each neuron is independently set to zero with probability `p` (the dropout rate).

During inference: dropout is turned off. All neurons are active, but their outputs are scaled down by `1 - p` to compensate for the larger number of active neurons compared to training.

Keras handles this automatically — you never need to manually scale.

### Dropout in Keras

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(256, activation='relu', input_shape=(100,)),
    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.3),

    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

Common dropout rates: 0.2 to 0.5 for dense layers. Higher dropout rates provide more regularization but can slow learning.

### When to Use Dropout

- When you observe overfitting — training accuracy significantly higher than validation accuracy
- Less common in convolutional layers (spatial dropout exists but is less used)
- After large dense layers where the model has excess capacity

[Camera: Instructor]

A crucial point: dropout only applies during training. When you call `model.predict()` or `model.evaluate()`, Keras automatically disables dropout. If you use `model(x, training=True)` in a custom loop, you must pass `training=False` for inference to disable it correctly.

---

## SEGMENT 7 — Model Evaluation (17:00–20:00)

[Screen: Code demonstration]

After training, evaluate your model on held-out test data:

```python
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")
```

`model.evaluate()` runs a forward pass over the test set in batches and returns the compiled metrics.

### Predictions

```python
# Probabilities (for classification)
probs = model.predict(X_test)

# Convert to class labels (binary)
binary_preds = (probs > 0.5).astype(int)

# Convert to class labels (multi-class)
import numpy as np
class_preds = np.argmax(probs, axis=1)
```

### Beyond Accuracy — Confusion Matrix and Classification Report

```python
from sklearn.metrics import classification_report, confusion_matrix

y_pred = (model.predict(X_test) > 0.5).astype(int)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

[Camera: Instructor]

Accuracy alone is misleading for imbalanced datasets. If 95% of your samples are class 0, a model that always predicts class 0 achieves 95% accuracy while being completely useless. Always look at precision, recall, and the confusion matrix for classification tasks.

---

## SEGMENT 8 — Putting It All Together (20:00–22:30)

[Screen: Complete training pipeline code]

Let me show you a complete, production-quality training setup using everything from this module:

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, input_shape=(n_features,)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.Dropout(0.3),

    tf.keras.layers.Dense(64),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.Dropout(0.2),

    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=15, restore_best_weights=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', factor=0.5, patience=5, verbose=1
    ),
    tf.keras.callbacks.ModelCheckpoint(
        'best_model.keras', monitor='val_loss', save_best_only=True
    )
]

history = model.fit(
    X_train, y_train,
    epochs=300,
    batch_size=32,
    validation_data=(X_val, y_val),
    callbacks=callbacks,
    verbose=1
)

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Final Test Accuracy: {test_acc:.4f}")
```

[Camera: Instructor]

This is the template I use as a starting point for almost every classification task. Adjust the architecture, dropout rates, and patience values based on your dataset.

---

## SEGMENT 9 — Wrap-Up and Preview (22:30–24:00)

[Camera: Instructor]

Today we covered the complete training toolkit: callbacks including EarlyStopping, ModelCheckpoint, and ReduceLROnPlateau; learning rate schedules; batch normalization; dropout regularization; and model evaluation with `evaluate()` and `predict()`.

In Module 7 we move into convolutional neural networks — the architecture that revolutionized computer vision. You will use everything from this module as the training foundation for your CNNs.

Your lab this week has you train a model on a real dataset three ways: without any regularization, with dropout only, and with BatchNorm plus dropout. You will plot training curves and compare test performance across all three setups.

Quiz and discussion are due Sunday at midnight.

See you in Module 7.

---

## Production Notes

- Screen capture: all code at 1080p, font size 18 or larger
- Pause on training output logs to let students read epoch-by-epoch metrics
- Show ReduceLROnPlateau verbose output on screen during the callbacks demo
- Closed captions required for all segments

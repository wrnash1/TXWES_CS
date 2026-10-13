# Lab Activity: Module 16 - Final Exam Submission
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

## Objective
Schedule and complete the official **TensorFlow Developer Certificate** industry certification exam, and submit your score verification report to Professor Nash.

## Instructions
1.  Register for the exam at the on-campus testing center or an authorized provider.
2.  Complete the exam.
3.  Obtain your official score report PDF showing your name, passing status, and date.
4. Upload the official score report PDF to the Canvas LMS assignment box for this module to receive final credit.

---

## Part 9 — Challenge Exercise

These exercises simulate the TF Developer Certificate exam under timed, open-book conditions. Complete all four problems within a five-hour window using only tensorflow.org and keras.io documentation. Save each trained model as a `.h5` file and verify it meets the stated accuracy or MAE threshold before saving.

### Challenge 1 — Four-Problem Mock Exam

Simulate all four TF Developer Certificate exam task categories. For each problem, build, compile, train, and save the model using the build-compile-fit pattern with `EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)`.

#### Problem 1 — Basic Dense Classifier (Fashion MNIST)

```python
import tensorflow as tf

(x_train, y_train), (x_val, y_val) = tf.keras.datasets.fashion_mnist.load_data()
x_train, x_val = x_train / 255.0, x_val / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=3, restore_best_weights=True
    )
]
model.fit(x_train, y_train, epochs=30, validation_data=(x_val, y_val),
          callbacks=callbacks)
loss, acc = model.evaluate(x_val, y_val)
print(f'Validation accuracy: {acc:.4f}')
assert acc >= 0.87, f'Threshold not met: {acc:.4f} < 0.87'
model.save('problem1_dense.h5')
```

#### Problem 2 — CNN Image Classifier with Data Augmentation

```python
import tensorflow as tf

(x_train, y_train), (x_val, y_val) = tf.keras.datasets.cifar10.load_data()
x_train, x_val = x_train / 255.0, x_val / 255.0

data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip('horizontal'),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1),
])

model = tf.keras.Sequential([
    data_augmentation,
    tf.keras.layers.Conv2D(32, 3, activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(128, 3, activation='relu', padding='same'),
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.4),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=3, restore_best_weights=True
    )
]
model.fit(x_train, y_train, epochs=40, batch_size=64,
          validation_data=(x_val, y_val), callbacks=callbacks)
loss, acc = model.evaluate(x_val, y_val)
print(f'Validation accuracy: {acc:.4f}')
assert acc >= 0.70, f'Threshold not met: {acc:.4f} < 0.70'
model.save('problem2_cnn.h5')
```

#### Problem 3 — NLP Text Classifier (IMDB Sentiment)

```python
import tensorflow as tf
import numpy as np

VOCAB_SIZE = 10000
MAX_LENGTH = 120
EMBEDDING_DIM = 16

(train_data, train_labels), (val_data, val_labels) = (
    tf.keras.datasets.imdb.load_data(num_words=VOCAB_SIZE)
)

train_padded = tf.keras.preprocessing.sequence.pad_sequences(
    train_data, maxlen=MAX_LENGTH, padding='post', truncating='post'
)
val_padded = tf.keras.preprocessing.sequence.pad_sequences(
    val_data, maxlen=MAX_LENGTH, padding='post', truncating='post'
)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(VOCAB_SIZE + 1, EMBEDDING_DIM,
                              input_length=MAX_LENGTH),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=3, restore_best_weights=True
    )
]
model.fit(train_padded, train_labels, epochs=20,
          validation_data=(val_padded, val_labels), callbacks=callbacks)
loss, acc = model.evaluate(val_padded, val_labels)
print(f'Validation accuracy: {acc:.4f}')
assert acc >= 0.85, f'Threshold not met: {acc:.4f} < 0.85'
model.save('problem3_nlp.h5')
```

#### Problem 4 — LSTM Time Series Forecaster

```python
import tensorflow as tf
import numpy as np

# Generate a synthetic time series
np.random.seed(42)
time = np.arange(500)
series = (np.sin(0.05 * time) + 0.1 * np.random.randn(500)).astype(np.float32)

WINDOW_SIZE = 30
BATCH_SIZE = 32

def windowed_dataset(series, window_size, batch_size):
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
    ds = ds.flat_map(lambda w: w.batch(window_size + 1))
    ds = ds.map(lambda w: (w[:-1], w[-1]))
    ds = ds.shuffle(1000).batch(batch_size).prefetch(1)
    return ds

split = 400
train_ds = windowed_dataset(series[:split], WINDOW_SIZE, BATCH_SIZE)
val_ds = windowed_dataset(series[split:], WINDOW_SIZE, BATCH_SIZE)

model = tf.keras.Sequential([
    tf.keras.layers.Lambda(lambda x: tf.expand_dims(x, axis=-1),
                           input_shape=[WINDOW_SIZE]),
    tf.keras.layers.LSTM(64, return_sequences=True),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer=tf.keras.optimizers.Adam(1e-3),
              loss='mae',
              metrics=['mae'])
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=5, restore_best_weights=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss', patience=3, factor=0.5, verbose=1
    )
]
model.fit(train_ds, epochs=100, validation_data=val_ds, callbacks=callbacks)
naive_mae = np.mean(np.abs(np.diff(series[split:])))
results = model.evaluate(val_ds)
val_mae = results[1]
print(f'Model MAE: {val_mae:.4f}  |  Naive MAE: {naive_mae:.4f}')
assert val_mae < naive_mae, 'Model MAE must beat naive baseline'
model.save('problem4_ts.h5')
```

After completing all four problems, verify each saved `.h5` file loads and produces the correct output shape:

```python
for fname, input_shape in [
    ('problem1_dense.h5', (1, 28, 28)),
    ('problem2_cnn.h5', (1, 32, 32, 3)),
    ('problem3_nlp.h5', (1, 120)),
    ('problem4_ts.h5', (1, 30)),
]:
    m = tf.keras.models.load_model(fname)
    dummy = tf.zeros(input_shape)
    out = m.predict(dummy)
    print(f'{fname}: output shape = {out.shape}')
```

#### Threshold Summary

| Problem | Dataset | Threshold |
|---------|---------|-----------|
| 1 — Dense classifier | Fashion MNIST | val_accuracy >= 0.87 |
| 2 — CNN image classifier | CIFAR-10 | val_accuracy >= 0.70 |
| 3 — NLP sentiment | IMDB | val_accuracy >= 0.85 |
| 4 — LSTM time series | Synthetic sine | val_MAE < naive_MAE |

---

### Challenge 2 — Transfer Learning with Fine-Tuning (MobileNetV2)

Build a two-stage transfer learning pipeline using MobileNetV2 on CIFAR-10 (resized to 96×96). Stage 1 trains only the classification head with the base frozen. Stage 2 unfreezes the top 30 layers of MobileNetV2 and fine-tunes with a very low learning rate.

```python
import tensorflow as tf

(x_train, y_train), (x_val, y_val) = tf.keras.datasets.cifar10.load_data()
x_train = tf.image.resize(x_train / 255.0, (96, 96))
x_val = tf.image.resize(x_val / 255.0, (96, 96))

# Stage 1 — train head only
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(96, 96, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False

inputs = tf.keras.Input(shape=(96, 96, 3))
x = base_model(inputs, training=False)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dense(128, activation='relu')(x)
x = tf.keras.layers.Dropout(0.3)(x)
outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
model = tf.keras.Model(inputs, outputs)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10, batch_size=64,
          validation_data=(x_val, y_val),
          callbacks=[tf.keras.callbacks.EarlyStopping(
              monitor='val_loss', patience=3, restore_best_weights=True)])

stage1_acc = model.evaluate(x_val, y_val)[1]
print(f'Stage 1 validation accuracy: {stage1_acc:.4f}')

# Stage 2 — fine-tune top 30 layers
base_model.trainable = True
for layer in base_model.layers[:-30]:
    layer.trainable = False

# MANDATORY recompile after changing trainable attributes
model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-5),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(x_train, y_train, epochs=10, batch_size=64,
          validation_data=(x_val, y_val),
          callbacks=[tf.keras.callbacks.EarlyStopping(
              monitor='val_loss', patience=3, restore_best_weights=True)])

stage2_acc = model.evaluate(x_val, y_val)[1]
print(f'Stage 2 validation accuracy: {stage2_acc:.4f}')
print(f'Fine-tuning improvement: {(stage2_acc - stage1_acc)*100:.2f}%')
assert stage2_acc > stage1_acc, 'Stage 2 should improve over Stage 1'
model.save('challenge2_mobilenet.h5')
```

---

### Reflection Questions

Answer the following in 2–3 sentences each before your exam attempt.

1. The four TF Developer Certificate task categories each require a different output layer configuration. Without looking at notes, state the correct output activation and loss function for: (a) regression, (b) binary classification, (c) multi-class classification with integer labels, and (d) time series one-step-ahead forecasting.

2. Explain why `restore_best_weights=True` in `EarlyStopping` is critical for exam submissions. What specific failure mode does it prevent, and what would happen to a submitted `.h5` file if this argument were omitted?

3. Describe the mandatory step between Stage 1 and Stage 2 of the transfer learning fine-tuning pattern. Why does Keras require this step, and what happens if it is skipped?

4. A time series LSTM receives a flat `(batch, window_size)` input tensor instead of `(batch, window_size, 1)`. Describe two ways to fix the input shape and explain which approach integrates the fix directly into the model architecture so the saved `.h5` handles reshaping automatically at inference time.

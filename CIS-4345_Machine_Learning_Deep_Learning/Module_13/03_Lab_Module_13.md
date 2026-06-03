# Lab Activity: Module 13 — Time Series Forecasting with TensorFlow

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Lab Overview

**Title:** Time Series Forecasting — Windowed Datasets, CNNs, and LSTMs

**Duration:** 90–120 minutes

**Platform:** Google Colab (no local setup required)

**Deliverable:** Completed Colab notebook exported as `.ipynb` and submitted to Canvas

**Points:** 100

---

## Learning Objectives

By the end of this lab you will have:

- Constructed a windowed `tf.data.Dataset` from a synthetic time series
- Trained a Dense baseline, a 1D CNN, and a stacked LSTM model
- Computed MAE and RMSE on a held-out validation set
- Compared all models against a naive baseline in a results table
- Plotted validation forecasts for each model

---

## Prerequisites

Review the Module 13 video and reading guide before beginning. You should be comfortable with:

- NumPy array slicing
- Basic `tf.keras.Sequential` model construction
- `model.fit()` with callbacks

---

## Part 1 — Environment Setup (10 minutes)

### Step 1.1 — Install and Import

Open a new Colab notebook. Run the following cell first:

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

print("TensorFlow version:", tf.__version__)
tf.random.set_seed(42)
np.random.seed(42)
```

Confirm TensorFlow 2.x is installed. If it shows 1.x, run `!pip install --upgrade tensorflow` and restart the runtime.

### Step 1.2 — Generate the Synthetic Dataset

```python
def generate_time_series(n_steps=1500, seed=42):
    np.random.seed(seed)
    time = np.arange(n_steps, dtype=np.float32)
    trend = 0.04 * time
    annual = 12 * np.sin(2 * np.pi * time / 365)
    weekly = 4 * np.sin(2 * np.pi * time / 7)
    noise = np.random.randn(n_steps).astype(np.float32) * 3
    return time, trend + annual + weekly + noise

time, series = generate_time_series()
plt.figure(figsize=(12, 3))
plt.plot(time, series)
plt.title("Synthetic Time Series")
plt.xlabel("Time Step")
plt.ylabel("Value")
plt.tight_layout()
plt.show()
```

**Checkpoint:** Your plot should show an upward trend with sinusoidal oscillations and noise.

---

## Part 2 — Data Preparation (15 minutes)

### Step 2.1 — Temporal Split

```python
SPLIT = 1200
time_train, series_train = time[:SPLIT], series[:SPLIT]
time_val, series_val = time[SPLIT:], series[SPLIT:]

print(f"Training samples: {len(series_train)}")
print(f"Validation samples: {len(series_val)}")
```

### Step 2.2 — Normalize Using Training Statistics

```python
mean = series_train.mean()
std = series_train.std()
series_train_n = (series_train - mean) / std
series_val_n = (series_val - mean) / std
print(f"Train mean: {mean:.2f}, std: {std:.2f}")
```

### Step 2.3 — Build the Windowed Dataset Function

```python
WINDOW_SIZE = 30
BATCH_SIZE = 32
SHUFFLE_BUFFER = 500

def windowed_dataset(series, window_size, batch_size, shuffle_buffer, expand=False):
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
    ds = ds.flat_map(lambda w: w.batch(window_size + 1))
    ds = ds.shuffle(shuffle_buffer)
    if expand:
        ds = ds.map(lambda w: (tf.expand_dims(w[:-1], axis=-1), w[-1]))
    else:
        ds = ds.map(lambda w: (w[:-1], w[-1]))
    return ds.batch(batch_size).prefetch(1)

train_ds = windowed_dataset(series_train_n, WINDOW_SIZE, BATCH_SIZE, SHUFFLE_BUFFER)
val_ds = windowed_dataset(series_val_n, WINDOW_SIZE, BATCH_SIZE, 100)
```

---

## Part 3 — Naive Baseline (10 minutes)

### Step 3.1 — Compute Naive Forecast

```python
def evaluate_forecast(actual, predicted, label="Model"):
    actual = np.array(actual)
    predicted = np.array(predicted)
    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))
    print(f"{label:20s} | MAE: {mae:.4f} | RMSE: {rmse:.4f}")
    return mae, rmse

# Naive: predict previous value (in original scale)
naive_pred = series_val[WINDOW_SIZE - 1:-1]
naive_actual = series_val[WINDOW_SIZE:]
naive_mae, naive_rmse = evaluate_forecast(naive_actual, naive_pred, "Naive Baseline")
```

Record these values. Every subsequent model must beat this baseline to be considered useful.

---

## Part 4 — Dense Baseline Model (15 minutes)

### Step 4.1 — Build and Train

```python
model_dense = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=[WINDOW_SIZE]),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

model_dense.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(1e-3))

history_dense = model_dense.fit(
    train_ds, epochs=50, validation_data=val_ds,
    callbacks=[tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)],
    verbose=0
)
print("Dense training complete. Best val loss:", min(history_dense.history['val_loss']))
```

### Step 4.2 — Evaluate

```python
dense_preds_n = model_dense.predict(
    series_val_n[:-1].reshape(-1, WINDOW_SIZE, 1)[:, :, 0], verbose=0
).flatten()

# Denormalize
dense_preds = dense_preds_n * std + mean
dense_actual = series_val[WINDOW_SIZE:]
dense_mae, dense_rmse = evaluate_forecast(dense_actual[:len(dense_preds)],
                                          dense_preds, "Dense Baseline")
```

---

## Part 5 — 1D CNN Model (20 minutes)

### Step 5.1 — Build

```python
train_ds_cnn = windowed_dataset(series_train_n, WINDOW_SIZE, BATCH_SIZE,
                                SHUFFLE_BUFFER, expand=True)
val_ds_cnn = windowed_dataset(series_val_n, WINDOW_SIZE, BATCH_SIZE, 100, expand=True)

model_cnn = tf.keras.Sequential([
    tf.keras.layers.Conv1D(64, kernel_size=5, activation='relu',
                           input_shape=[WINDOW_SIZE, 1]),
    tf.keras.layers.MaxPooling1D(pool_size=2),
    tf.keras.layers.Conv1D(32, kernel_size=3, activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

model_cnn.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(1e-3))
model_cnn.summary()
```

### Step 5.2 — Train and Evaluate

```python
history_cnn = model_cnn.fit(
    train_ds_cnn, epochs=100, validation_data=val_ds_cnn,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(patience=8, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(patience=3, factor=0.5)
    ],
    verbose=0
)

# Generate predictions over validation set using rolling window
cnn_inputs = series_val_n[:WINDOW_SIZE].reshape(1, WINDOW_SIZE, 1)
cnn_preds_n = []
for i in range(len(series_val) - WINDOW_SIZE):
    window = series_val_n[i:i + WINDOW_SIZE].reshape(1, WINDOW_SIZE, 1)
    pred = model_cnn.predict(window, verbose=0)[0, 0]
    cnn_preds_n.append(pred)

cnn_preds = np.array(cnn_preds_n) * std + mean
cnn_mae, cnn_rmse = evaluate_forecast(series_val[WINDOW_SIZE:], cnn_preds, "1D CNN")
```

---

## Part 6 — Stacked LSTM Model (20 minutes)

### Step 6.1 — Build

```python
model_lstm = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, return_sequences=True, input_shape=[WINDOW_SIZE, 1]),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1)
])

model_lstm.compile(
    loss='mse',
    optimizer=tf.keras.optimizers.Adam(1e-3, clipnorm=1.0)
)
model_lstm.summary()
```

### Step 6.2 — Train and Evaluate

```python
history_lstm = model_lstm.fit(
    train_ds_cnn, epochs=100, validation_data=val_ds_cnn,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(patience=4, factor=0.5, min_lr=1e-6)
    ],
    verbose=0
)

lstm_preds_n = []
for i in range(len(series_val) - WINDOW_SIZE):
    window = series_val_n[i:i + WINDOW_SIZE].reshape(1, WINDOW_SIZE, 1)
    pred = model_lstm.predict(window, verbose=0)[0, 0]
    lstm_preds_n.append(pred)

lstm_preds = np.array(lstm_preds_n) * std + mean
lstm_mae, lstm_rmse = evaluate_forecast(series_val[WINDOW_SIZE:], lstm_preds, "Stacked LSTM")
```

---

## Part 7 — Results Table and Visualization (10 minutes)

### Step 7.1 — Summary Table

```python
results = {
    "Model": ["Naive Baseline", "Dense", "1D CNN", "Stacked LSTM"],
    "MAE": [naive_mae, dense_mae, cnn_mae, lstm_mae],
    "RMSE": [naive_rmse, dense_rmse, cnn_rmse, lstm_rmse]
}

print(f"\n{'Model':<20} {'MAE':>8} {'RMSE':>8}")
print("-" * 38)
for i in range(len(results["Model"])):
    print(f"{results['Model'][i]:<20} {results['MAE'][i]:>8.4f} {results['RMSE'][i]:>8.4f}")
```

### Step 7.2 — Forecast Plot

```python
plot_start = 50
t_plot = time_val[WINDOW_SIZE + plot_start: WINDOW_SIZE + plot_start + 200]
a_plot = series_val[WINDOW_SIZE + plot_start: WINDOW_SIZE + plot_start + 200]
c_plot = cnn_preds[plot_start: plot_start + 200]
l_plot = lstm_preds[plot_start: plot_start + 200]

plt.figure(figsize=(14, 4))
plt.plot(t_plot, a_plot, label="Actual", color='black')
plt.plot(t_plot, c_plot, label="CNN Forecast", linestyle='--')
plt.plot(t_plot, l_plot, label="LSTM Forecast", linestyle=':')
plt.legend()
plt.title("Forecast Comparison — CNN vs LSTM")
plt.tight_layout()
plt.show()
```

---

## Submission Checklist

Before submitting, confirm your notebook contains:

- [ ] All 6 code parts completed and executed without errors
- [ ] Naive baseline MAE and RMSE values recorded
- [ ] Summary results table printed with all four models
- [ ] Forecast comparison plot showing CNN and LSTM overlaid on actuals
- [ ] Brief written reflection (3–5 sentences) in a Markdown cell: Which model performed best, and why do you think that is?

Submit your `.ipynb` file to the Module 13 Lab assignment on Canvas.

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| Windowed dataset implemented correctly | 20 |
| All three models trained and evaluated | 30 |
| Results table with all four rows (including naive) | 20 |
| Forecast visualization | 15 |
| Written reflection | 15 |
| **Total** | **100** |

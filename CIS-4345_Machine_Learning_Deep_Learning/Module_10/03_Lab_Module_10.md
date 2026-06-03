# Lab: Module 10 — Recurrent Neural Networks and LSTMs

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Lab Overview

In this lab you will build a complete time series forecasting pipeline using LSTM and GRU networks in TensorFlow/Keras. You will preprocess a real-world weather dataset, implement the windowed dataset pattern required by the TensorFlow Developer Certificate exam, train stacked recurrent models, compare their performance, and visualize predictions against ground truth.

**Estimated Time:** 90–120 minutes

**Prerequisites:** Module 10 video and reading guide completed

---

## Learning Objectives

By completing this lab you will be able to:

- Normalize and window a real-world time series for sequence modeling
- Build, train, and evaluate stacked LSTM and GRU models in Keras
- Apply `EarlyStopping` and `ReduceLROnPlateau` callbacks correctly
- Compare model performance using MAE and visual inspection
- Identify and correct the `return_sequences` error common in stacked RNNs

---

## Setup

### Environment

This lab runs in Google Colab or a local Jupyter environment with TensorFlow 2.x installed.

```python
# Cell 1 — Install and import
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

print(f"TensorFlow version: {tf.__version__}")
```

### Dataset

You will use the Jena Climate dataset, a publicly available hourly weather recording from 2009–2016. It contains 14 features including temperature, pressure, and humidity.

```python
# Cell 2 — Download dataset
import urllib.request
import os

url = "https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip"
zip_path = "jena_climate.zip"
csv_path = "jena_climate_2009_2016.csv"

if not os.path.exists(csv_path):
    urllib.request.urlretrieve(url, zip_path)
    import zipfile
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(".")
    print("Dataset downloaded and extracted.")

df = pd.read_csv(csv_path)
print(df.shape)
print(df.head(3))
```

**Expected output:** `(420551, 15)` — over 420,000 hourly readings across 15 columns.

---

## Step 1 — Exploratory Data Analysis

```python
# Cell 3 — Inspect temperature column
print(df.columns.tolist())

# Use temperature in Celsius: column "T (degC)"
temp = df["T (degC)"].values
print(f"Min: {temp.min():.2f}, Max: {temp.max():.2f}, Mean: {temp.mean():.2f}")

# Plot first 1500 readings (about 2 months)
plt.figure(figsize=(12, 4))
plt.plot(temp[:1500], color='steelblue', linewidth=0.8)
plt.title("Jena Temperature — First 1,500 Hours")
plt.xlabel("Hour")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
```

**Expected output:** A noisy time series with a clear daily cycle visible in the first 1,500 points.

> **Checkpoint 1:** Does the plot show periodic oscillations roughly every 24 data points? If yes, the daily temperature cycle is visible — proceed to Step 2.

---

## Step 2 — Preprocessing

### Subsample and Normalize

```python
# Cell 4 — Subsample to every 6 hours to reduce sequence length
SUBSAMPLE = 6
temp_sub = temp[::SUBSAMPLE]
print(f"Subsampled length: {len(temp_sub)}")

# Normalize with MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
temp_norm = scaler.fit_transform(temp_sub.reshape(-1, 1)).flatten()

# Train / validation split (80/20)
split_idx = int(len(temp_norm) * 0.8)
train_series = temp_norm[:split_idx]
val_series   = temp_norm[split_idx:]
print(f"Train: {len(train_series)}, Val: {len(val_series)}")
```

### Create Windowed Dataset

```python
# Cell 5 — Windowing function
WINDOW_SIZE = 60   # 60 six-hour steps = 15 days of context
HORIZON = 1        # predict the next single value

def make_windows(series, window_size, horizon):
    """
    Converts a 1-D time series into supervised (X, y) arrays.
    X shape: (samples, window_size, 1)
    y shape: (samples, horizon)
    """
    X, y = [], []
    for i in range(len(series) - window_size - horizon + 1):
        X.append(series[i : i + window_size])
        y.append(series[i + window_size : i + window_size + horizon])
    return np.array(X)[..., np.newaxis], np.array(y)

X_train, y_train = make_windows(train_series, WINDOW_SIZE, HORIZON)
X_val,   y_val   = make_windows(val_series,   WINDOW_SIZE, HORIZON)

print(f"X_train: {X_train.shape}, y_train: {y_train.shape}")
print(f"X_val:   {X_val.shape},   y_val:   {y_val.shape}")
```

**Expected shapes:**

- `X_train: (N_train, 60, 1)`
- `y_train: (N_train, 1)`

---

## Step 3 — Build and Train the LSTM Model

```python
# Cell 6 — Stacked LSTM
def build_lstm(window_size, units_1=64, units_2=32, dropout=0.2):
    model = keras.Sequential([
        keras.layers.LSTM(
            units_1,
            return_sequences=True,
            input_shape=(window_size, 1)
        ),
        keras.layers.Dropout(dropout),
        keras.layers.LSTM(units_2),
        keras.layers.Dense(1)
    ], name="stacked_lstm")
    return model

lstm_model = build_lstm(WINDOW_SIZE)
lstm_model.summary()
```

```python
# Cell 7 — Compile and train LSTM
lstm_model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='mse',
    metrics=['mae']
)

callbacks = [
    keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=5,
        restore_best_weights=True
    ),
    keras.callbacks.ReduceLROnPlateau(
        monitor='val_loss',
        factor=0.5,
        patience=3,
        min_lr=1e-6,
        verbose=1
    )
]

lstm_history = lstm_model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=128,
    validation_data=(X_val, y_val),
    callbacks=callbacks,
    verbose=1
)
```

**Expected behavior:** Training loss decreases steadily. `EarlyStopping` typically triggers between epoch 10 and 25. Final validation MAE should be in the range 0.03–0.08 (normalized units).

---

## Step 4 — Build and Train the GRU Model

```python
# Cell 8 — Stacked GRU (same architecture, different cell)
def build_gru(window_size, units_1=64, units_2=32, dropout=0.2):
    model = keras.Sequential([
        keras.layers.GRU(
            units_1,
            return_sequences=True,
            input_shape=(window_size, 1)
        ),
        keras.layers.Dropout(dropout),
        keras.layers.GRU(units_2),
        keras.layers.Dense(1)
    ], name="stacked_gru")
    return model

gru_model = build_gru(WINDOW_SIZE)
gru_model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='mse',
    metrics=['mae']
)

gru_history = gru_model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=128,
    validation_data=(X_val, y_val),
    callbacks=callbacks,
    verbose=1
)
```

---

## Step 5 — Compare Results

```python
# Cell 9 — Evaluate both models
lstm_results = lstm_model.evaluate(X_val, y_val, verbose=0)
gru_results  = gru_model.evaluate(X_val, y_val, verbose=0)

print(f"LSTM  — Val Loss (MSE): {lstm_results[0]:.5f} | Val MAE: {lstm_results[1]:.5f}")
print(f"GRU   — Val Loss (MSE): {gru_results[0]:.5f}  | Val MAE: {gru_results[1]:.5f}")

# Count parameters
lstm_params = lstm_model.count_params()
gru_params  = gru_model.count_params()
print(f"\nLSTM parameters: {lstm_params:,}")
print(f"GRU  parameters: {gru_params:,}")
print(f"GRU uses {(1 - gru_params / lstm_params) * 100:.1f}% fewer parameters")
```

```python
# Cell 10 — Plot training curves
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, hist, name, color in zip(
    axes,
    [lstm_history, gru_history],
    ["LSTM", "GRU"],
    ["steelblue", "darkorange"]
):
    ax.plot(hist.history['mae'],     label='Train MAE', color=color, linewidth=2)
    ax.plot(hist.history['val_mae'], label='Val MAE',   color=color,
            linewidth=2, linestyle='--')
    ax.set_title(f"{name} Training Curve")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("MAE (normalized)")
    ax.legend()
    ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()
```

```python
# Cell 11 — Visual prediction comparison
n_plot = 200
lstm_preds = lstm_model.predict(X_val[:n_plot], verbose=0).flatten()
gru_preds  = gru_model.predict(X_val[:n_plot], verbose=0).flatten()
actual     = y_val[:n_plot].flatten()

plt.figure(figsize=(14, 5))
plt.plot(actual,     label='Actual',    color='black',      linewidth=1.5)
plt.plot(lstm_preds, label='LSTM Pred', color='steelblue',  linewidth=1, alpha=0.8)
plt.plot(gru_preds,  label='GRU Pred',  color='darkorange', linewidth=1, alpha=0.8)
plt.title("Temperature Forecast: LSTM vs GRU (first 200 validation windows)")
plt.xlabel("Time Step")
plt.ylabel("Normalized Temperature")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

---

## Step 6 — Debugging Exercise

The following model has a bug. Identify and fix it before running.

```python
# Cell 12 — Find and fix the bug
broken_model = keras.Sequential([
    keras.layers.LSTM(64, input_shape=(WINDOW_SIZE, 1)),   # BUG IS HERE
    keras.layers.LSTM(32),
    keras.layers.Dense(1)
])

# What error occurs when you run broken_model.summary()?
# Fix the model and confirm it builds correctly.
```

> **Hint:** The first LSTM layer in a stacked architecture must pass its full output sequence to the next layer.

---

## Deliverables

Submit a single Jupyter notebook (.ipynb) containing all cells above, executed with visible output. Your notebook must include:

1. The EDA plot of temperature over the first 1,500 hours
2. Printed train/validation shapes confirming correct windowing
3. Training logs showing EarlyStopping triggered for both models
4. A comparison table of LSTM vs. GRU: Val MAE, parameter count, epochs trained
5. The prediction overlay plot (Cell 11)
6. The corrected Cell 12 with a comment explaining the bug and the fix

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Dataset downloaded, subsampled, and normalized correctly | 15 |
| Windowing function produces correct X and y shapes | 15 |
| LSTM model builds, trains, and converges | 20 |
| GRU model builds, trains, and converges | 15 |
| Comparison table with MAE and parameter counts | 15 |
| Prediction overlay plot present and labeled | 10 |
| Cell 12 bug identified and corrected with explanation | 10 |
| **Total** | **100** |

---

*End of Lab — Module 10*

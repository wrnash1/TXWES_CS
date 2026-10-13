# Video Script: Module 13 — Time Series Forecasting with TensorFlow

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Production Notes

- **Runtime target:** 20–24 minutes
- **Format:** Screencast with code walkthroughs; whiteboard diagrams for windowed datasets
- **Visual aids:** Matplotlib plots of synthetic time series; TensorBoard loss curves
- **Code environment:** Google Colab, TensorFlow 2.x

---

## SEGMENT 1 — Introduction and Motivation (0:00–2:30)

Welcome to Module 13. Over the past twelve modules you have learned to classify images, process natural language, and build regression models. Today we turn to a fundamentally different data structure: the time series.

A time series is any sequence of observations indexed by time. Think about daily temperature readings, hourly electricity demand, weekly stock prices, or monthly website traffic. These datasets share one critical property — the order of observations matters. A temperature reading from Tuesday is not independent of Monday's reading. That dependency is exactly what makes time series both challenging and fascinating.

By the end of this module you will be able to:

- Construct windowed TensorFlow datasets for sequence modeling
- Apply 1D convolutional networks to sequence data
- Build LSTM-based forecasting models
- Handle multivariate time series inputs
- Evaluate forecast quality using MAE and RMSE

Let's start by understanding what makes time series data unique.

---

## SEGMENT 2 — Anatomy of a Time Series (2:30–5:00)

[SLIDE: Components of a time series — trend, seasonality, noise]

Every time series can be decomposed into three components. The **trend** is the long-run direction — is the signal generally rising, falling, or flat? **Seasonality** captures repeating periodic patterns — electricity demand peaks on hot summer days every year. **Noise** or residual is everything left over after you remove trend and seasonality.

Understanding these components matters because your model needs to learn all three. A naive model that simply predicts "tomorrow equals today" handles trend moderately well but completely misses seasonal peaks.

Let me show you a synthetic time series we will use throughout this module:

```python
import numpy as np
import matplotlib.pyplot as plt

def generate_time_series(n_steps=4 * 365, seed=42):
    np.random.seed(seed)
    time = np.arange(n_steps)
    trend = 0.05 * time
    seasonality = 10 * np.sin(2 * np.pi * time / 365)
    noise = np.random.randn(n_steps) * 3
    return time, trend + seasonality + noise

time, series = generate_time_series()
plt.plot(time, series)
plt.title("Synthetic Time Series")
plt.show()
```

[PAUSE — show the plot on screen]

You can see all three components: a gentle upward slope for trend, a yearly sinusoidal wave for seasonality, and random fluctuations for noise. Your model must learn to separate signal from noise and project forward.

---

## SEGMENT 3 — Windowed Datasets (5:00–9:00)

[SLIDE: Diagram of a sliding window]

The central preprocessing step for time series in TensorFlow is creating a **windowed dataset**. The idea is to slide a fixed-length window across your series, treating each window as one training example. The input is the window of length W, and the label is the next value at position `W + 1`.

Here is the canonical TensorFlow pattern:

```python
import tensorflow as tf

def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True)
    dataset = dataset.flat_map(lambda w: w.batch(window_size + 1))
    dataset = dataset.shuffle(shuffle_buffer)
    dataset = dataset.map(lambda w: (w[:-1], w[-1]))
    dataset = dataset.batch(batch_size).prefetch(1)
    return dataset
```

Let me walk through each line. `from_tensor_slices` converts the NumPy array into a stream of individual time steps. `window` creates overlapping sub-sequences of length `window_size + 1` — the extra one is the label. `flat_map` with `.batch` materializes each window into a tensor. `shuffle` randomizes order to reduce gradient correlation between neighboring batches. `map` splits each window into features `w[:-1]` and label `w[-1]`. Finally `batch` and `prefetch` pipeline the data for GPU throughput.

[VISUAL: Animate the sliding window moving across the series]

Why do we use `+ 1` for the window? Because we want the model to see W time steps and predict the next one. If your window is 30 days, the model sees days 1–30 and predicts day 31.

Let me demonstrate a quick split:

```python
split_time = 3 * 365
time_train, series_train = time[:split_time], series[:split_time]
time_val, series_val = time[split_time:], series[split_time:]

WINDOW_SIZE = 30
BATCH_SIZE = 32
SHUFFLE_BUFFER = 1000

train_ds = windowed_dataset(series_train, WINDOW_SIZE, BATCH_SIZE, SHUFFLE_BUFFER)
val_ds = windowed_dataset(series_val, WINDOW_SIZE, BATCH_SIZE, 100)
```

We reserve the last year for validation. This is called a **temporal split** — always split time series by time, never randomly. Random splits would leak future information into training, giving you artificially optimistic metrics.

---

## SEGMENT 4 — 1D CNNs for Sequence Data (9:00–13:00)

[SLIDE: 1D convolution diagram]

Convolutional layers are not just for images. A 1D convolution slides a kernel across a sequence in time, learning local patterns. For time series, this is equivalent to asking: "Is there a pattern in any consecutive W time steps that predicts what comes next?"

1D CNNs are fast, parallelizable, and surprisingly effective for many forecasting tasks:

```python
model_cnn = tf.keras.Sequential([
    tf.keras.layers.Conv1D(
        filters=64, kernel_size=5,
        activation='relu',
        input_shape=[WINDOW_SIZE, 1]
    ),
    tf.keras.layers.MaxPooling1D(pool_size=2),
    tf.keras.layers.Conv1D(filters=32, kernel_size=3, activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1)
])
```

Notice the `input_shape=[WINDOW_SIZE, 1]`. Your windowed dataset returns 1D slices, so you need to add a channel dimension. Let me show the reshape:

```python
def windowed_dataset_cnn(series, window_size, batch_size, shuffle_buffer):
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True)
    dataset = dataset.flat_map(lambda w: w.batch(window_size + 1))
    dataset = dataset.shuffle(shuffle_buffer)
    dataset = dataset.map(lambda w: (
        tf.expand_dims(w[:-1], axis=-1), w[-1]
    ))
    dataset = dataset.batch(batch_size).prefetch(1)
    return dataset
```

`tf.expand_dims` adds the channel dimension the Conv1D layer expects.

Now let us compile and train:

```python
model_cnn.compile(
    loss='mse',
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3)
)

history = model_cnn.fit(
    train_ds, epochs=50,
    validation_data=val_ds,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
    ]
)
```

We use MSE as training loss because we want squared-error minimization, but we evaluate with MAE for interpretability.

---

## SEGMENT 5 — LSTM Forecasting (13:00–17:30)

[SLIDE: LSTM cell diagram — cell state, hidden state, gates]

Long Short-Term Memory networks are the classic solution for sequential data. Unlike a standard RNN that suffers from vanishing gradients over long sequences, LSTMs maintain a **cell state** that acts like a memory highway. Three gates — input, forget, and output — control what information enters, persists, and exits the memory cell.

For time series forecasting, an LSTM can theoretically capture dependencies spanning hundreds of time steps. Here is a standard LSTM forecasting model:

```python
model_lstm = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, return_sequences=True,
                         input_shape=[WINDOW_SIZE, 1]),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1)
])

model_lstm.compile(
    loss='mse',
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3)
)
```

The first LSTM layer uses `return_sequences=True` so it passes a sequence of hidden states to the second LSTM. The second LSTM uses the default `return_sequences=False`, returning only the final hidden state. Then two dense layers produce the scalar forecast.

[PAUSE — run and show training curves]

A practical tip: LSTMs often converge faster if you use a learning rate schedule. Let me add a `ReduceLROnPlateau` callback:

```python
lr_schedule = tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6
)

history_lstm = model_lstm.fit(
    train_ds, epochs=100,
    validation_data=val_ds,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True),
        lr_schedule
    ]
)
```

[VISUAL: Compare CNN vs LSTM validation loss curves side by side]

In practice, 1D CNNs and LSTMs often achieve similar accuracy on univariate forecasting. CNNs win on speed; LSTMs can win when long-range patterns exist. Many production systems combine both.

---

## SEGMENT 6 — Multivariate Time Series (17:30–20:30)

[SLIDE: Multiple feature channels flowing into LSTM]

So far we have used a single observation per time step. Real-world problems often have multiple correlated signals. For example, predicting electricity demand might use temperature, day of week, and hour of day simultaneously.

Extending to multivariate input requires only a change in the feature dimension:

```python
def generate_multivariate(n_steps=4 * 365, seed=42):
    np.random.seed(seed)
    time = np.arange(n_steps)
    temp = 15 + 10 * np.sin(2 * np.pi * time / 365) + np.random.randn(n_steps)
    demand = 50 + 0.8 * temp + 5 * np.sin(2 * np.pi * time / 7) \
             + np.random.randn(n_steps) * 2
    return np.stack([temp, demand], axis=-1)

mv_series = generate_multivariate()
print(mv_series.shape)  # (1460, 2)
```

The shape is now `(timesteps, n_features)`. When you build the windowed dataset, each window will be `(WINDOW_SIZE, 2)`. The LSTM model handles this automatically:

```python
model_mv = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, return_sequences=True,
                         input_shape=[WINDOW_SIZE, 2]),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(1)
])
```

The `input_shape=[WINDOW_SIZE, 2]` tells the model to expect two features at each time step.

---

## SEGMENT 7 — Evaluation Metrics and Wrap-Up (20:30–23:00)

[SLIDE: MAE vs RMSE formulas]

Two metrics dominate time series evaluation. **Mean Absolute Error (MAE)** is the average absolute difference between forecast and actual. It is easy to interpret: an MAE of 5.2 means you are off by 5.2 units on average. **Root Mean Squared Error (RMSE)** squares the errors before averaging, so large errors are penalized more heavily.

```python
def evaluate_forecast(actual, predicted):
    mae = np.mean(np.abs(actual - predicted))
    rmse = np.sqrt(np.mean((actual - predicted) ** 2))
    print(f"MAE:  {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    return mae, rmse
```

Always compare your model against a **naive baseline** — typically the "last value" forecast where you predict `y_t = y_{t-1}`. If your deep learning model cannot beat the naive baseline, something is wrong.

```python
naive_forecast = series_val[WINDOW_SIZE - 1:-1]
print("Naive baseline:")
evaluate_forecast(series_val[WINDOW_SIZE:], naive_forecast)
```

In this module's lab, you will benchmark three model architectures against the naive baseline and present a table of results.

To summarize: time series forecasting with TensorFlow involves building windowed datasets via `tf.data`, choosing between CNN or LSTM architectures, extending to multivariate inputs when needed, and always evaluating against a meaningful baseline. In Module 14 we move from training models to deploying them in production. See you there.

---

## End of Script

**Total estimated runtime:** 23 minutes

**Key code files referenced:** `module13_timeseries.ipynb`

**TF Developer Certificate alignment:** Category 4 — Time Series, Sequences, and Predictions

# Reading Guide: Module 13 — Time Series Forecasting with TensorFlow

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Overview

This reading guide accompanies Module 13 of CIS-4345. Time series forecasting is one of the four primary categories on the TensorFlow Developer Certificate exam. This guide synthesizes material from the TensorFlow documentation, the Hands-On Machine Learning textbook, and the TF Certificate curriculum. Work through each section in order — later sections build on concepts introduced earlier.

**Estimated study time:** 2.5–3 hours

---

## Learning Objectives

After completing the readings and activities in this guide, you will be able to:

1. Explain the components of a time series and why temporal ordering matters
2. Implement a windowed `tf.data.Dataset` from a raw NumPy array
3. Build and train a 1D CNN for univariate forecasting
4. Build and train a stacked LSTM model for univariate and multivariate forecasting
5. Compare model performance to a naive baseline using MAE and RMSE
6. Recognize common pitfalls — data leakage, overfitting, and incorrect input shapes

---

## Section 1 — What Is a Time Series?

### 1.1 Definition and Examples

A **time series** is an ordered sequence of values `{x_1, x_2, ..., x_T}` where the index represents time. The key property distinguishing time series from other datasets is **temporal dependence** — the value at time t is correlated with past values. This violates the i.i.d. (independent and identically distributed) assumption of standard supervised learning.

Common examples include:

- Financial data: daily closing prices, exchange rates
- IoT sensor data: temperature, vibration, power consumption
- Web analytics: daily active users, page load times
- Environmental data: precipitation, CO2 levels

### 1.2 Decomposition

Most time series can be written as:

```
x_t = Trend(t) + Seasonality(t) + Residual(t)
```

Understanding each component guides model design:

- **Trend**: A smooth, long-term increase or decrease. Linear models handle trends well; neural networks need enough data to learn them.
- **Seasonality**: Periodic fluctuations with a known cycle length (daily, weekly, annual). The cycle length informs your choice of window size.
- **Residual**: Random noise. No model can predict pure noise — the goal is to minimize residual uncertainty.

### 1.3 Stationarity

A time series is **stationary** if its statistical properties (mean, variance) do not change over time. Many classical forecasting models (ARIMA) require stationarity. Deep learning models are more tolerant of non-stationarity, but normalizing your series still helps training.

**Practice:** Plot a sample time series and visually identify trend, seasonality, and noise. Can you estimate the period of the seasonal component?

---

## Section 2 — Data Preparation and Windowed Datasets

### 2.1 The Sliding Window Approach

Supervised learning requires (input, label) pairs. For time series, we create these pairs using a **sliding window**:

- Input: `[x_{t-W}, x_{t-W+1}, ..., x_{t-1}]` — the last W observations
- Label: `x_t` — the next observation

Each position in the series produces one training example. If the series has T observations and the window size is W, you get `T - W` examples.

### 2.2 Temporal Train/Validation Split

**Critical rule:** Never use random shuffling for the train/validation split in time series. Always split by time:

```python
split_time = int(0.8 * len(series))
train_series = series[:split_time]
val_series = series[split_time:]
```

Using a random split would include future observations in training, a form of **data leakage** that inflates validation metrics.

### 2.3 Building a `tf.data` Pipeline

The canonical pipeline for time series uses five chained operations:

```python
def windowed_dataset(series, window_size, batch_size, shuffle_buffer):
    dataset = tf.data.Dataset.from_tensor_slices(series)
    dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True)
    dataset = dataset.flat_map(lambda w: w.batch(window_size + 1))
    dataset = dataset.shuffle(shuffle_buffer)
    dataset = dataset.map(lambda w: (w[:-1], w[-1]))
    dataset = dataset.batch(batch_size).prefetch(1)
    return dataset
```

Understand the purpose of each operation:

| Operation | Purpose |
|-----------|---------|
| `from_tensor_slices` | Convert array to element-wise stream |
| `window` | Create overlapping sub-sequences |
| `flat_map + batch` | Materialize window into tensors |
| `shuffle` | Break sequential correlation between batches |
| `map` | Split into (features, label) pairs |
| `batch + prefetch` | GPU-friendly batching |

### 2.4 Normalization

Before building the dataset, normalize your series using training statistics only:

```python
mean = train_series.mean()
std = train_series.std()
train_norm = (train_series - mean) / std
val_norm = (val_series - mean) / std
```

Apply validation normalization using training `mean` and `std` — never compute separate stats on the validation set.

---

## Section 3 — 1D Convolutional Networks

### 3.1 How 1D Convolution Works

A `Conv1D` layer applies a 1D kernel of length K across the time dimension, producing a new sequence. Each position in the output is a weighted sum of K consecutive input values. This is equivalent to a learnable moving average — but the model learns which patterns matter.

**Key hyperparameters:**

- `filters`: Number of distinct patterns to learn (output channels)
- `kernel_size`: Length of the temporal receptive field per filter
- `activation`: Typically `'relu'`

### 3.2 Architecture for Forecasting

```python
model = tf.keras.Sequential([
    tf.keras.layers.Conv1D(64, kernel_size=5, activation='relu',
                           input_shape=[window_size, 1]),
    tf.keras.layers.MaxPooling1D(pool_size=2),
    tf.keras.layers.Conv1D(32, kernel_size=3, activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])
```

Note the `input_shape=[window_size, 1]` — the trailing `1` is the channel dimension required by Conv1D. Use `tf.expand_dims(w, axis=-1)` in your dataset map function.

### 3.3 Advantages of CNNs for Sequences

- Fully parallelizable (unlike RNNs, no recurrent dependency)
- Excellent at detecting local patterns
- Faster to train than LSTMs on most hardware

### 3.4 Limitations

CNNs capture only patterns within the receptive field of the top layer. For a two-layer CNN with kernel sizes 5 and 3, the effective receptive field is `(5 - 1) + (3 - 1) = 6` time steps. Long-range dependencies require either very deep CNNs or a different architecture.

---

## Section 4 — LSTM Networks for Forecasting

### 4.1 The LSTM Cell

The LSTM cell maintains two states: the **hidden state** `h_t` and the **cell state** `c_t`. Three gates regulate information flow:

- **Forget gate**: Decides what to discard from cell state
- **Input gate**: Decides what new information to write to cell state
- **Output gate**: Decides what part of cell state to expose as hidden state

The cell state acts as a long-term memory, enabling LSTMs to model dependencies across hundreds of time steps without vanishing gradients.

### 4.2 Stacked LSTM Architecture

```python
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, return_sequences=True,
                         input_shape=[window_size, 1]),
    tf.keras.layers.LSTM(32, return_sequences=False),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1)
])
```

The `return_sequences=True` argument in the first LSTM passes the full sequence of hidden states to the next layer. The second LSTM returns only the final state.

### 4.3 Bidirectional LSTMs

For non-causal applications (where you can look at the full sequence before predicting), wrapping LSTM in `Bidirectional` doubles capacity:

```python
tf.keras.layers.Bidirectional(
    tf.keras.layers.LSTM(32), input_shape=[window_size, 1]
)
```

For online forecasting (predicting one step ahead in real time), Bidirectional is not appropriate — you cannot see the future.

### 4.4 Training Tips

- Use `ReduceLROnPlateau` or cosine annealing to avoid stalling
- Clip gradients with `clipnorm=1.0` to prevent exploding gradients
- Start with fewer units (32–64) before scaling up
- Always use `EarlyStopping(restore_best_weights=True)`

---

## Section 5 — Multivariate Time Series

### 5.1 When to Use Multiple Features

Add features when they have predictive power beyond the target series alone. Good candidates:

- Calendar features (hour of day, day of week, month) — always useful for seasonal series
- Exogenous variables (weather forecasts for energy demand, marketing spend for sales)
- Related series (cross-correlations across sensors in a network)

### 5.2 Input Shape Changes

For M features at each time step, the input shape becomes `[window_size, M]`:

```python
# Multivariate dataset builder
def mv_windowed_dataset(mv_series, target_col, window_size, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices(mv_series)
    dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True)
    dataset = dataset.flat_map(lambda w: w.batch(window_size + 1))
    dataset = dataset.map(lambda w: (w[:-1, :], w[-1, target_col]))
    dataset = dataset.batch(batch_size).prefetch(1)
    return dataset
```

Here `target_col` is the column index of the variable you are forecasting. The model sees all M features but predicts only one.

### 5.3 Feature Engineering for Time Series

Standard feature engineering techniques:

- **Lag features**: `x_{t-1}`, `x_{t-7}`, `x_{t-365}` as explicit inputs
- **Rolling statistics**: Mean and standard deviation over the past N steps
- **Differencing**: `delta_t = x_t - x_{t-1}` to remove trend
- **One-hot day-of-week**: Explicit seasonal encoding

These manual features complement learned representations in deep models.

---

## Section 6 — Evaluation and Baselines

### 6.1 Evaluation Metrics

| Metric | Formula | When to Use |
|--------|---------|-------------|
| MAE | `mean(|y - y_hat|)` | Interpretable; robust to outliers |
| RMSE | `sqrt(mean((y - y_hat)^2))` | Penalizes large errors more |
| MAPE | `mean(|y - y_hat| / y) * 100` | Percentage error; avoid when y near zero |

### 6.2 Baseline Models

Always benchmark against:

- **Naive forecast**: `y_hat_t = y_{t-1}`
- **Seasonal naive**: `y_hat_t = y_{t - period}`
- **Moving average**: `y_hat_t = mean(y_{t-W}...y_{t-1})`

If your deep learning model cannot improve on the naive forecast, revisit your data pipeline, window size, or normalization.

### 6.3 Visualizing Forecasts

Always plot forecasts against actuals:

```python
def plot_forecast(time, actual, predicted, start=None):
    if start:
        time = time[start:]
        actual = actual[start:]
        predicted = predicted[start:]
    plt.figure(figsize=(12, 4))
    plt.plot(time, actual, label='Actual')
    plt.plot(time, predicted, label='Forecast', linestyle='--')
    plt.legend()
    plt.show()
```

A model with acceptable MAE but systematic bias (always under- or over-forecasting) will be obvious from the plot.

---

## Section 7 — TF Developer Certificate Alignment

The exam includes a dedicated time series category. Key competencies tested:

- Building a `windowed_dataset` function from scratch
- Training a single-layer LSTM on a windowed series
- Training a CNN + LSTM hybrid model
- Computing MAE on validation set
- Achieving MAE below a specified threshold

Practice building these models without referring to notes. The exam provides a dataset and asks you to reach a target MAE.

---

## Key Terms

- **Time series:** Ordered sequence of values indexed by time
- **Windowed dataset:** Training data created by sliding a fixed window across a series
- **Temporal split:** Train/validation division by time, not random sampling
- **Seasonality:** Repeating periodic patterns in a time series
- **LSTM:** Long Short-Term Memory — recurrent architecture with gated memory
- **Conv1D:** 1D convolutional layer; applies learned kernels along the time axis
- **MAE:** Mean Absolute Error — average absolute forecast error
- **RMSE:** Root Mean Squared Error — error metric that penalizes large deviations
- **Naive baseline:** Simplest possible forecast used as a performance floor

---

## Self-Check Questions

Answer these before the quiz:

1. Why must you use a temporal split rather than random splitting for time series?
2. What does `drop_remainder=True` do in `dataset.window(...)`?
3. Why is `return_sequences=True` needed in the first LSTM of a stacked model?
4. What input shape does Conv1D expect, and how do you add the channel dimension?
5. What is the naive baseline, and why is it important as a benchmark?
6. How does multivariate input change the LSTM's `input_shape`?

---

## Recommended Resources

- TensorFlow Time Series Tutorial: [tensorflow.org/tutorials/structured_data/time_series](https://www.tensorflow.org/tutorials/structured_data/time_series)
- Coursera TF Developer Certificate Course 4 — Sequences, Time Series and Prediction
- Hands-On ML, Chapter 15 — Processing Sequences Using RNNs and CNNs
- Google Developers: Introduction to Time Series with TensorFlow (YouTube)

---

## Next Module Preview

Module 14 covers deploying trained models: TensorFlow Serving, the SavedModel format, TFLite for mobile, and REST API wrapping. You will take the models trained in Module 13 and serve them via a local Flask endpoint.

---

## 9. Supplemental Resources

**1. [TensorFlow Time Series Forecasting Tutorial](https://www.tensorflow.org/tutorials/structured_data/time_series)**
The definitive official TensorFlow tutorial for time series, covering single-step and multi-step forecasting with dense networks, CNNs, LSTMs, and autoregressive RNNs on the Jena climate dataset. Directly aligned with TF Developer Certificate exam content including windowing, normalization, and the `WindowGenerator` utility class.

**2. [fast.ai Practical Deep Learning — Tabular and Time Series](https://course.fast.ai/Lessons/lesson6.html)**
fast.ai's practical approach to time series with PyTorch, covering feature engineering, seasonality, embeddings for temporal features, and the `TimeseriesDataLoaders` API. Provides a valuable alternative perspective on the same core concepts covered in this module.

**3. [Papers With Code — Time Series Forecasting Benchmark](https://paperswithcode.com/task/time-series-forecasting)**
State-of-the-art benchmark tracking for time series forecasting tasks, including N-BEATS, Temporal Fusion Transformer, PatchTST, and other modern architectures. Useful for understanding how far beyond basic LSTM/CNN the research frontier has progressed.

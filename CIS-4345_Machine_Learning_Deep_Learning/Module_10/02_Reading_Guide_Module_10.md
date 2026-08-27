# Reading Guide: Module 10 — Recurrent Neural Networks and LSTMs

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Overview

This reading guide covers the theory and implementation of Recurrent Neural Networks (RNNs), Long Short-Term Memory (LSTM) cells, and Gated Recurrent Units (GRUs). By the end of this module you will understand why sequential data requires a different architecture, how LSTM gates solve the vanishing gradient problem, and how to implement production-quality sequence models in TensorFlow/Keras.

---

## Section 1 — Why Sequences Require a Different Architecture

Standard feedforward and convolutional networks process each input independently. This works for images but fails for data where context accumulates across time. Consider predicting the word that comes after "The cat sat on the ___." A model that ignores the prior words has no hope of predicting "mat."

### The i.i.d. Assumption Violation

Most classical ML algorithms assume that training examples are **independent and identically distributed** (i.i.d.). Sequence data violates this. The value at time step `t` is statistically dependent on values at `t-1`, `t-2`, and potentially much earlier.

### Fixed-Input-Size Problems

A dense network requires a fixed-size input vector. If you want to process sequences of variable length — sentences of 5 words or 50 words — you cannot simply concatenate all inputs into one vector. You need an architecture that processes inputs one at a time and accumulates state.

---

## Section 2 — Vanilla RNN Architecture

### The Recurrence Equation

At each time step `t`, a SimpleRNN cell computes:

```text
h_t = tanh(W_hh * h_(t-1) + W_xh * x_t + b_h)
y_t = W_hy * h_t + b_y
```

Where:

- `x_t` is the input at time `t`
- `h_t` is the hidden state (memory) at time `t`
- `h_(t-1)` is the hidden state from the previous time step
- `W_xh`, `W_hh`, `W_hy` are learned weight matrices shared across all time steps
- `b_h`, `b_y` are bias vectors

The hidden state is the mechanism of memory. It carries a compressed summary of all previous inputs into the current computation.

### Keras Implementation

```python
import tensorflow as tf
from tensorflow import keras

model = keras.Sequential([
    keras.layers.SimpleRNN(64, activation='tanh', input_shape=(50, 1)),
    keras.layers.Dense(1)
])
model.summary()
```

The `input_shape=(50, 1)` means 50 time steps with 1 feature each. Keras internally loops the cell 50 times and returns only the final hidden state.

### Sequence-to-Sequence vs. Sequence-to-One

| Mode | `return_sequences` | Output Shape | Use Case |
|---|---|---|---|
| Sequence-to-one | `False` (default) | `(batch, units)` | Classification, regression |
| Sequence-to-sequence | `True` | `(batch, timesteps, units)` | Stacked RNNs, translation |

---

## Section 3 — The Vanishing Gradient Problem

### Backpropagation Through Time (BPTT)

Training an RNN requires computing the gradient of the loss with respect to weights that are applied at every time step. The gradient at step `t` depends on the gradient at step `t+1`, which depends on `t+2`, and so on back to the beginning of the sequence.

At each step, the gradient is multiplied by `W_hh`. If the largest singular value of `W_hh` is less than 1:

```text
gradient at step 1 ≈ (W_hh)^T * ... (W_hh)^T * gradient at step T
```

With T = 50 steps and values slightly below 1, this product approaches zero exponentially. Early time steps receive virtually zero gradient — the network cannot learn from them.

### Exploding Gradients

The symmetric problem occurs when values exceed 1. The gradient grows exponentially, causing numerical overflow or wild parameter updates. This is handled with gradient clipping:

```python
optimizer = keras.optimizers.Adam(clipnorm=1.0)
model.compile(optimizer=optimizer, loss='mse')
```

### Why Vanishing Is the Harder Problem

Exploding gradients are detectable (NaN loss, wildly oscillating training curves) and fixable with clipping. Vanishing gradients are silent — training appears to proceed normally but the model simply fails to learn long-range dependencies. This motivated the LSTM.

---

## Section 4 — Long Short-Term Memory (LSTM)

### Architecture Overview

An LSTM cell maintains two state vectors:

- **Cell state** `C_t`: long-term memory, the "conveyor belt"
- **Hidden state** `h_t`: short-term working memory, also the output

The cell state pathway allows gradients to flow backward across many time steps with minimal decay, directly addressing the vanishing gradient problem.

### The Three Gates

**Forget Gate** — Controls what fraction of the previous cell state to retain:

```text
f_t = sigmoid(W_f * [h_(t-1), x_t] + b_f)
```

Output range: 0 (forget all) to 1 (keep all).

**Input Gate and Candidate Cell** — Controls what new information to write:

```text
i_t  = sigmoid(W_i * [h_(t-1), x_t] + b_i)
g_t  = tanh(W_g * [h_(t-1), x_t] + b_g)
C_t  = f_t (elem-wise) C_(t-1) + i_t (elem-wise) g_t
```

**Output Gate** — Controls what portion of the cell state to expose as `h_t`:

```text
o_t = sigmoid(W_o * [h_(t-1), x_t] + b_o)
h_t = o_t (elem-wise) tanh(C_t)
```

### Why This Solves Vanishing Gradients

The cell state update equation is additive: `C_t = f_t (elem) C_(t-1) + i_t (elem) g_t`. An additive update means the gradient can flow backward through `C_t` to `C_(t-1)` directly, without being multiplied by a weight matrix. This is analogous to the skip connections in ResNet — both architectures create gradient highways that bypass the multiplicative weight layers.

### Keras LSTM

```python
model = keras.Sequential([
    keras.layers.LSTM(128, return_sequences=True, input_shape=(50, 1)),
    keras.layers.Dropout(0.2),
    keras.layers.LSTM(64),
    keras.layers.Dense(1)
])
```

### Parameter Count for LSTM

An LSTM with `n` units receiving input of dimension `d` has:

```text
parameters = 4 * ((d + n) * n + n)
```

The factor of 4 accounts for the four weight matrices (forget, input, candidate, output). A layer with `n=64` units and `d=1` input has `4 * ((1 + 64) * 64 + 64) = 16,896` parameters.

---

## Section 5 — Gated Recurrent Unit (GRU)

### Architecture Overview

The GRU, introduced by Cho et al. (2014), simplifies the LSTM by:

- Merging the cell state and hidden state into a single state vector `h_t`
- Using only two gates: **reset gate** and **update gate**

### GRU Equations

```text
z_t = sigmoid(W_z * [h_(t-1), x_t])     # update gate
r_t = sigmoid(W_r * [h_(t-1), x_t])     # reset gate
g_t = tanh(W_g * [r_t (elem) h_(t-1), x_t])  # candidate
h_t = (1 - z_t) (elem) h_(t-1) + z_t (elem) g_t
```

The update gate acts like a combined forget and input gate. When `z_t` is near 1, the GRU strongly updates its state. When near 0, it mostly carries the previous state forward.

### LSTM vs. GRU Comparison

| Property | LSTM | GRU |
|---|---|---|
| States | Cell state + Hidden state | Hidden state only |
| Gates | 3 (forget, input, output) | 2 (reset, update) |
| Parameters | ~4x(d+n)n | ~3x(d+n)n |
| Training speed | Slower | ~25% faster |
| Long sequences | Excellent | Good |
| Short sequences | Good | Often matches LSTM |
| Default choice | Complex tasks | Start here |

### Keras GRU

```python
model = keras.Sequential([
    keras.layers.GRU(64, return_sequences=True, input_shape=(50, 1)),
    keras.layers.GRU(32),
    keras.layers.Dense(1)
])
```

---

## Section 6 — Bidirectional RNNs

### Concept

A standard RNN reads the sequence in one direction: time step 1 to time step T. A **Bidirectional RNN** runs two RNN cells simultaneously — one forward and one backward — and concatenates their outputs:

```text
h_t = [h_t_forward ; h_t_backward]
```

This doubles the effective hidden dimension at each time step. The model gains access to both past and future context at every position.

### When to Use Bidirectional

- **Use**: NLP classification, named entity recognition, sequence labeling — any task where the full sequence is available at inference time

- **Avoid**: Real-time forecasting, online streaming applications — future data is genuinely unavailable

### Keras Bidirectional Wrapper

```python
model = keras.Sequential([
    keras.layers.Bidirectional(
        keras.layers.LSTM(64, return_sequences=True),
        input_shape=(50, 1)
    ),
    keras.layers.Bidirectional(keras.layers.LSTM(32)),
    keras.layers.Dense(1, activation='sigmoid')
])
```

---

## Section 7 — Time Series Forecasting Pipeline

### Data Preparation

The key preprocessing step for time series is creating a **windowed dataset**. For a sequence of `N` values, window size `W`, and forecast horizon `H`:

```python
def make_windows(series, window_size, horizon):
    X, y = [], []
    for i in range(len(series) - window_size - horizon + 1):
        X.append(series[i : i + window_size])
        y.append(series[i + window_size : i + window_size + horizon])
    return np.array(X)[..., np.newaxis], np.array(y)
```

### Normalization

Always normalize sequences before feeding them to an RNN. The hidden state accumulates values across many steps — unnormalized inputs cause the hidden state to grow unboundedly.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
series_scaled = scaler.fit_transform(series.reshape(-1, 1)).flatten()
```

### Evaluation Metrics for Forecasting

| Metric | Formula | Interpretation |
|---|---|---|
| MAE | mean(abs(y_pred - y_true)) | Average absolute error |
| MSE | mean((y_pred - y_true)^2) | Penalizes large errors more |
| RMSE | sqrt(MSE) | Same units as target |
| MAPE | mean(abs((y_true - y_pred) / y_true)) | Percentage error |

### Full Forecasting Example

```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

# Synthetic dataset
np.random.seed(0)
time = np.linspace(0, 100, 2000)
series = np.sin(0.5 * time) + 0.3 * np.sin(2.0 * time) + 0.1 * np.random.randn(2000)

# Normalize
scaler = MinMaxScaler()
series_norm = scaler.fit_transform(series.reshape(-1, 1)).flatten()

# Window the data
WINDOW = 60
HORIZON = 1

def make_windows(series, window_size, horizon):
    X, y = [], []
    for i in range(len(series) - window_size - horizon + 1):
        X.append(series[i : i + window_size])
        y.append(series[i + window_size : i + window_size + horizon])
    return np.array(X)[..., np.newaxis], np.array(y)

X, y = make_windows(series_norm, WINDOW, HORIZON)
split = int(len(X) * 0.8)
X_train, X_val = X[:split], X[split:]
y_train, y_val = y[:split], y[split:]

# Model
model = keras.Sequential([
    keras.layers.LSTM(64, return_sequences=True, input_shape=(WINDOW, 1)),
    keras.layers.Dropout(0.2),
    keras.layers.LSTM(32),
    keras.layers.Dense(HORIZON)
])

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss='mse',
    metrics=['mae']
)

callbacks = [
    keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
    keras.callbacks.ReduceLROnPlateau(factor=0.5, patience=3)
]

history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=64,
    validation_data=(X_val, y_val),
    callbacks=callbacks,
    verbose=1
)

# Evaluate
y_pred = model.predict(X_val)
mae = np.mean(np.abs(y_pred.flatten() - y_val.flatten()))
print(f"Validation MAE: {mae:.4f}")
```

---

## Section 8 — Regularization for Recurrent Networks

### Standard Dropout

Apply Dropout between LSTM layers to regularize inter-layer activations:

```python
keras.layers.Dropout(0.3)
```

### Recurrent Dropout

The `recurrent_dropout` parameter applies dropout to the recurrent connections (the `W_hh` path) inside the LSTM cell. This is different from standard dropout, which applies to the input:

```python
keras.layers.LSTM(64, dropout=0.2, recurrent_dropout=0.1)
```

Note: using `recurrent_dropout` disables CuDNN acceleration, making training significantly slower on GPU. Use sparingly and only when overfitting is a documented problem.

### L2 Regularization

```python
from tensorflow.keras import regularizers

keras.layers.LSTM(64, kernel_regularizer=regularizers.l2(0.001))
```

---

## Section 9 — Architecture Comparison Summary

| Architecture | Memory Mechanism | Parameters | Long-Range | Speed |
|---|---|---|---|---|
| SimpleRNN | Hidden state only | Low | Poor | Fastest |
| LSTM | Cell state + hidden state | High | Excellent | Moderate |
| GRU | Single gated state | Medium | Good | Fast |
| Bidirectional LSTM | Forward + backward | 2x LSTM | Excellent | Slowest |
| Stacked LSTM | Hierarchical states | 2x+ | Excellent | Slow |

---

## Exam Tips — TensorFlow Developer Certificate

- The certificate exam commonly asks you to build a complete time series model including the windowing function

- Know the difference between `return_sequences=True` and `return_sequences=False` and when each is required

- Stacked LSTM layers require `return_sequences=True` on all layers except the final one

- Bidirectional wraps any recurrent layer: `Bidirectional(LSTM(64))` or `Bidirectional(GRU(64))`

- Data normalization before feeding sequences to an RNN is a standard exam expectation — use `MinMaxScaler` or `StandardScaler`

- The certificate exam tests `model.compile`, `model.fit`, and callback usage — know `EarlyStopping` parameters (`patience`, `restore_best_weights`)

- GRU and LSTM have identical Keras APIs — you can swap them by changing only the layer class name

---

*End of Reading Guide — Module 10*

---

## 9. Supplemental Resources

**1. [Understanding LSTM Networks — colah's blog](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)**
Christopher Olah's landmark blog post explaining LSTM architecture with detailed annotated diagrams of the forget gate, input gate, cell state update, and output gate. Widely regarded as the clearest explanation of LSTM internals available online and essential reading before the TF Developer Certificate exam.

**2. [TensorFlow Time Series Forecasting Tutorial](https://www.tensorflow.org/tutorials/structured_data/time_series)**
Official TensorFlow tutorial covering the complete time series pipeline: windowing, normalization, baseline models, linear models, dense networks, CNNs, LSTMs, and multi-step forecasting. Directly aligned with the time series task category on the TF Developer Certificate exam.

**3. [Illustrated Guide to LSTMs and GRUs — Towards Data Science](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)**
Step-by-step visual walkthrough of LSTM and GRU computations with animated diagrams. Covers the intuition behind each gate and the mathematical update equations. Particularly useful for understanding the GRU's simplified two-gate structure compared to LSTM's four-gate design.

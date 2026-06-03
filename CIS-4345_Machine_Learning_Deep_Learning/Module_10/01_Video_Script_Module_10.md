# Video Script: Module 10 — Recurrent Neural Networks and LSTMs

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: TensorFlow Developer Certificate

---

## SEGMENT 1 — Introduction and Motivation (0:00–2:30)

**[ON CAMERA]**

Welcome back, everyone. I'm Professor Nash, and this is Module 10 of CIS-4345.

So far in this course we have studied feedforward networks and convolutional networks. Both of those architectures share a key assumption: each input is independent of every other input. Feed in an image, get a prediction — done. The model has no memory of what it saw before.

But what about problems where order matters?

Think about predicting tomorrow's stock price. You need to know what happened over the last 30 days, not just today in isolation. Think about translating a sentence from English to Spanish. The word "bank" means something entirely different depending on whether you just read "river" or "money." Think about generating the next word in a sentence — you need the context of everything that came before it.

All of those problems involve **sequences** — data where position and history carry meaning. And that is exactly the problem that Recurrent Neural Networks, or RNNs, were designed to solve.

In this module we are going to cover:

- The architecture of a vanilla RNN and how it maintains a hidden state

- The vanishing gradient problem and why it cripples long sequences

- LSTM and GRU cells — the two solutions the field landed on

- How to implement all of this in Keras with real code

- Time series forecasting as our hands-on example

Let's get into it.

---

## SEGMENT 2 — Sequence Data and the Core RNN Idea (2:30–6:00)

**[SLIDE: Sequence Data Examples]**

Before we look at architecture, let's nail down what we mean by sequence data.

A sequence is any dataset where the **order of observations** carries predictive information. Examples include:

- **Time series**: temperature readings, stock prices, sensor data sampled over time

- **Natural language**: words or characters in a sentence or paragraph

- **Audio**: sampled amplitude values over time

- **Video**: frames ordered temporally

- **DNA sequences**: nucleotide bases in a gene

In all of these cases, feeding observations one at a time in order is critical.

**[SLIDE: Vanilla RNN Diagram]**

Here is the key insight behind a recurrent neural network. A standard feedforward layer computes:

```
output = activation(W * input + b)
```

An RNN layer computes:

```
h_t = activation(W_hh * h_(t-1) + W_xh * x_t + b)
```

There are two weight matrices instead of one. `W_xh` is the input-to-hidden weight — same concept as before. But `W_hh` is the hidden-to-hidden weight. It takes the **previous hidden state** and mixes it into the current computation.

The hidden state `h_t` acts as the network's **memory**. At each time step, the RNN reads the new input and updates its memory based on both the new input and everything it has seen so far.

**[SLIDE: Unrolled RNN]**

When we visualize an RNN unrolled through time, it looks like a chain of identical cells, each sharing the same weights. Time step 1 reads `x_1` and produces `h_1`. Time step 2 reads `x_2` and `h_1` to produce `h_2`. And so on.

This weight sharing is powerful because the same pattern-matching logic applies at every position in the sequence. The RNN does not need separate learned filters for position 1 versus position 10 — it learns one set of recurrent weights that applies everywhere.

---

## SEGMENT 3 — Code Demo: Vanilla RNN in Keras (6:00–9:00)

**[SCREEN SHARE — Code Editor]**

Let me show you what this looks like in Keras.

```python
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Simulated time series: 1000 samples, 30 timesteps, 1 feature
np.random.seed(42)
X = np.random.randn(1000, 30, 1).astype(np.float32)
y = np.random.randn(1000, 1).astype(np.float32)

# Vanilla RNN model
model = keras.Sequential([
    keras.layers.SimpleRNN(32, activation='tanh', input_shape=(30, 1)),
    keras.layers.Dense(1)
])

model.summary()
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=5, batch_size=32, validation_split=0.2)
```

Notice the input shape: `(30, 1)`. That means 30 time steps, 1 feature per step. Keras handles the unrolling automatically — you define the cell, and Keras loops it through all 30 steps internally.

The `SimpleRNN` layer outputs the final hidden state by default. That single vector summarizes the entire 30-step sequence, and we feed it into a Dense layer for the final prediction.

Run that and you will see the model trains. But here is the problem — let me explain why vanilla RNNs rarely work well in practice.

---

## SEGMENT 4 — The Vanishing Gradient Problem (9:00–12:30)

**[SLIDE: Gradient Flow Through Time]**

When we train an RNN with backpropagation, we compute gradients and push them backward through time. This process is called **Backpropagation Through Time**, or BPTT.

Here is the issue. At each time step, the gradient is multiplied by the recurrent weight matrix `W_hh`. If the values in that matrix are slightly less than 1, multiplying the gradient by it repeatedly across 30, 50, or 100 time steps drives the gradient exponentially toward zero. That is the **vanishing gradient**.

If the values are slightly greater than 1, the gradients explode exponentially. That is the **exploding gradient**.

The practical result: with vanilla RNNs, only the last few time steps have meaningful gradients. Steps far in the past contribute almost nothing to learning. The model cannot learn long-range dependencies.

**[SLIDE: Gradient Clipping for Exploding Gradients]**

The exploding gradient problem can be handled with **gradient clipping** — you cap the gradient norm at some maximum value. In Keras:

```python
optimizer = keras.optimizers.Adam(clipnorm=1.0)
```

But gradient clipping does not fix vanishing gradients. For that, we need a fundamentally different cell architecture.

**[SLIDE: LSTM Cell Diagram]**

Enter the **Long Short-Term Memory** cell, proposed by Hochreiter and Schmidhuber in 1997. The LSTM adds a second internal state called the **cell state** `C_t`, which runs alongside the hidden state `h_t`.

The cell state acts like a conveyor belt — information can flow across many time steps with minimal modification. Gradients can propagate back through the cell state path without being multiplied by the same weight matrix repeatedly, which breaks the vanishing gradient cycle.

---

## SEGMENT 5 — LSTM Architecture Deep Dive (12:30–16:00)

**[SLIDE: LSTM Gates]**

The LSTM controls information flow using three learned **gates**. Each gate is a small neural network that outputs values between 0 and 1.

**Forget Gate** — decides what to erase from the cell state:

```
f_t = sigmoid(W_f * [h_(t-1), x_t] + b_f)
```

A value near 0 means "forget everything." Near 1 means "keep everything."

**Input Gate** — decides what new information to add:

```
i_t = sigmoid(W_i * [h_(t-1), x_t] + b_i)
g_t = tanh(W_g * [h_(t-1), x_t] + b_g)
C_t = f_t (elem-wise) C_(t-1) + i_t (elem-wise) g_t
```

The cell state is updated by forgetting some old content and adding some new candidate content.

**Output Gate** — decides what to expose as the hidden state:

```
o_t = sigmoid(W_o * [h_(t-1), x_t] + b_o)
h_t = o_t (elem-wise) tanh(C_t)
```

These gates give the LSTM fine-grained control over what to remember, what to forget, and what to output at each step.

**[SLIDE: GRU Cell]**

The **Gated Recurrent Unit**, or GRU, introduced by Cho et al. in 2014, is a simplified version of the LSTM. It merges the cell state and hidden state into one, and uses only two gates: a reset gate and an update gate.

GRUs have fewer parameters than LSTMs — typically 25% fewer — and often match LSTM performance on shorter sequences. They are faster to train and a good default when you are unsure which to use.

---

## SEGMENT 6 — Code Demo: LSTM and GRU in Keras (16:00–19:30)

**[SCREEN SHARE — Code Editor]**

Let me show you a real time series forecasting example using LSTM.

```python
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Generate a synthetic sine wave with noise
time = np.arange(0, 1000, 0.1)
series = np.sin(time) + 0.1 * np.random.randn(len(time))

# Create windowed dataset
def make_windows(series, window_size, horizon=1):
    X, y = [], []
    for i in range(len(series) - window_size - horizon + 1):
        X.append(series[i : i + window_size])
        y.append(series[i + window_size : i + window_size + horizon])
    return np.array(X)[..., np.newaxis], np.array(y)

X, y = make_windows(series, window_size=50, horizon=1)
split = int(len(X) * 0.8)
X_train, X_val = X[:split], X[split:]
y_train, y_val = y[:split], y[split:]

# Stacked LSTM model
lstm_model = keras.Sequential([
    keras.layers.LSTM(64, return_sequences=True, input_shape=(50, 1)),
    keras.layers.LSTM(32),
    keras.layers.Dense(1)
])

lstm_model.compile(optimizer='adam', loss='mse', metrics=['mae'])
history = lstm_model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=64,
    validation_data=(X_val, y_val),
    callbacks=[keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)]
)
```

Notice the first LSTM layer uses `return_sequences=True`. This means it outputs the hidden state at **every** time step, not just the last one. That full sequence feeds into the second LSTM layer, which then outputs only the final hidden state. Stacking gives each layer the chance to learn patterns at a different level of abstraction.

The GRU equivalent is a one-word swap:

```python
# GRU model — identical structure, swap LSTM for GRU
gru_model = keras.Sequential([
    keras.layers.GRU(64, return_sequences=True, input_shape=(50, 1)),
    keras.layers.GRU(32),
    keras.layers.Dense(1)
])
```

Same architecture. Fewer parameters. Often trains faster.

---

## SEGMENT 7 — Bidirectional RNNs and Practical Tips (19:30–22:00)

**[SLIDE: Bidirectional LSTM]**

One powerful extension is the **Bidirectional LSTM**. Instead of reading the sequence only left to right, you run two LSTMs — one forward and one backward — and concatenate their outputs. This gives the model context from both directions simultaneously.

In Keras:

```python
keras.layers.Bidirectional(keras.layers.LSTM(64))
```

Bidirectional LSTMs are especially useful for NLP tasks, where words at the end of a sentence can clarify the meaning of words at the beginning. For real-time forecasting where future data is unavailable, stick with unidirectional.

**[SLIDE: Practical Tips]**

Practical tips for working with RNNs in production:

- Start with GRU before LSTM — it is usually sufficient and trains faster

- Use `return_sequences=True` on all layers except the final LSTM or GRU layer

- Apply Dropout between recurrent layers. Use `recurrent_dropout` inside the cell for temporal regularization

- Normalize your input sequences — RNNs are sensitive to feature scale

- Use `EarlyStopping` with `restore_best_weights=True` to avoid overfitting on training time steps

- Gradient clipping with `clipnorm=1.0` guards against exploding gradients

---

## SEGMENT 8 — Wrap-Up and Certification Alignment (22:00–24:00)

**[ON CAMERA]**

Let's bring this all together.

Recurrent Neural Networks extend feedforward networks to handle sequential data by maintaining a hidden state that accumulates information across time steps. The vanishing gradient problem makes vanilla RNNs ineffective for long sequences. LSTMs solve this with a cell state and three learned gates: forget, input, and output. GRUs offer a lighter alternative with two gates. Both are available in Keras with a single layer call.

For the TensorFlow Developer Certificate, you need to be able to:

- Build single and stacked LSTM models for time series

- Use `return_sequences=True` correctly in stacked architectures

- Apply the `Bidirectional` wrapper

- Normalize and window time series data for sequence modeling

All of these appear directly in the exam. In the lab for this module, you are going to build a full time series forecasting pipeline on real-world data. Take your time with the windowing function — that is where most people make mistakes.

I will see you in the discussion board, and I will see you in Module 11 where we move into Transfer Learning. Take care.

---

*[End of Script — Module 10]*

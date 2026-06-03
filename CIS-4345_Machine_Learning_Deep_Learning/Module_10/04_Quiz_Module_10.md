# Quiz: Module 10 — Recurrent Neural Networks and LSTMs

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points (100 points total).

---

## Question 1

What distinguishes a Recurrent Neural Network from a standard feedforward network?

A. RNNs use convolutional filters to detect spatial patterns in input data.
B. RNNs maintain a hidden state that is updated at each time step, allowing information to persist across the sequence.
C. RNNs use batch normalization to stabilize training on sequential inputs.
D. RNNs replace the activation function with a gating mechanism at every layer.

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Convolutional filters are the defining feature of CNNs, not RNNs. CNNs detect spatial patterns; RNNs process temporal sequences through recurrent connections.
- **B — Correct.** The hidden state `h_t` is the memory mechanism of an RNN. It is computed from both the current input `x_t` and the previous hidden state `h_(t-1)`, enabling information to persist across time steps.
- **C — Incorrect.** Batch normalization is a regularization technique applicable to many architectures but is not what distinguishes RNNs from feedforward networks.
- **D — Incorrect.** Gating mechanisms are a feature of LSTM and GRU cells specifically, not of RNNs in general. A SimpleRNN uses a plain activation function (typically tanh) with no gating.

---

## Question 2

During Backpropagation Through Time (BPTT), the vanishing gradient problem occurs when:

A. The learning rate is set too high, causing the optimizer to overshoot the minimum.
B. The gradient is multiplied by the recurrent weight matrix at each time step, causing it to shrink exponentially toward zero over many steps.
C. The batch size is too small, introducing excessive noise into gradient estimates.
D. The activation function produces outputs greater than 1, amplifying gradients at each step.

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** A high learning rate causes divergence or oscillation, which is a separate optimization problem unrelated to the structural cause of vanishing gradients.
- **B — Correct.** In BPTT, the gradient at each step is multiplied by the transpose of `W_hh`. When the singular values of this matrix are less than 1, repeated multiplication drives the gradient exponentially toward zero, making it impossible for early time steps to contribute to learning.
- **C — Incorrect.** Small batch size introduces gradient noise (high variance), which is a different problem. Vanishing gradients are a structural property of deep or long recurrent networks, not a batch-size effect.
- **D — Incorrect.** Outputs greater than 1 amplify gradients — that describes the exploding gradient problem, which is the opposite of vanishing gradients.

---

## Question 3

In a stacked two-layer LSTM model in Keras, which configuration is correct?

A. Both LSTM layers should have `return_sequences=False`.
B. Both LSTM layers should have `return_sequences=True`.
C. The first LSTM layer should have `return_sequences=True`; the second should have `return_sequences=False`.
D. The first LSTM layer should have `return_sequences=False`; the second should have `return_sequences=True`.

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** If the first LSTM layer returns only the final hidden state (shape `(batch, units)`), the second LSTM layer receives a 2-D tensor. LSTM layers expect a 3-D input `(batch, timesteps, features)` and will raise a shape error.
- **B — Incorrect.** Having the second LSTM return sequences would output a 3-D tensor `(batch, timesteps, units)` that cannot be fed directly to a Dense layer without flattening or another reduction step.
- **C — Correct.** The first LSTM layer uses `return_sequences=True` to pass the full sequence `(batch, timesteps, units)` to the second layer. The second LSTM uses `return_sequences=False` (default) to output only the final hidden state `(batch, units)` for the Dense layer.
- **D — Incorrect.** This is reversed. Returning only the final state from the first layer gives the second LSTM a 2-D input, which is invalid.

---

## Question 4

Which statement accurately describes the cell state in an LSTM?

A. The cell state is equivalent to the hidden state and is passed to the next layer as the output.
B. The cell state stores short-term working memory and is reset to zero at each time step.
C. The cell state acts as a long-term memory conveyor belt, updated additively through the forget and input gates, which allows gradients to flow backward without repeated weight-matrix multiplication.
D. The cell state is a scalar value that tracks the cumulative loss across all time steps.

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** The cell state `C_t` and the hidden state `h_t` are two distinct vectors in an LSTM. The hidden state `h_t` is the output passed to the next layer; the cell state is internal.
- **B — Incorrect.** The hidden state is closer to "short-term working memory" in the LSTM analogy. The cell state persists across time steps and is not reset each step.
- **C — Correct.** The cell state is updated as `C_t = f_t (elem) C_(t-1) + i_t (elem) g_t`. This additive update creates a gradient highway: gradients can flow from `C_t` back to `C_(t-1)` directly, avoiding the vanishing gradient problem that plagued vanilla RNNs.
- **D — Incorrect.** The cell state has nothing to do with loss tracking. It is a learned vector of the same dimensionality as the hidden state.

---

## Question 5

A GRU has fewer parameters than an LSTM of the same hidden size because:

A. GRUs use smaller weight matrices by applying weight sharing across gates.
B. GRUs eliminate the cell state and reduce from three gates to two, decreasing the number of weight matrices from four to three.
C. GRUs apply dropout internally, which prunes unused parameters during training.
D. GRUs use integer weights instead of floating-point weights to reduce memory usage.

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Both GRUs and LSTMs share weights across time steps. GRUs do not apply additional weight sharing across gates — the parameter reduction comes from having fewer gates.
- **B — Correct.** An LSTM has four weight matrices (forget, input, candidate, output). A GRU has three (reset, update, candidate) and merges the cell and hidden states into one. This reduces the parameter count by roughly 25% for the same hidden dimension.
- **C — Incorrect.** Dropout is a regularization technique that sets activations to zero during training but does not remove or prune model parameters.
- **D — Incorrect.** Both GRUs and LSTMs use standard floating-point weights. Integer quantization is a separate post-training optimization technique.

---

## Question 6

What is the purpose of the `Bidirectional` wrapper in Keras?

A. It trains two separate models and averages their predictions at inference time.
B. It runs the recurrent cell forward through the sequence and backward through the sequence simultaneously, concatenating both output states.
C. It alternates the direction of gradient flow each epoch to prevent vanishing gradients.
D. It enables the model to process two input sequences at the same time through parameter sharing.

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** A Bidirectional layer is a single layer, not an ensemble of two separately trained models. Both directions share the same forward and training pass.
- **B — Correct.** `Bidirectional(LSTM(64))` creates two LSTM cells: one reads the sequence from left to right, the other from right to left. Their hidden states are concatenated, doubling the effective output dimension to 128. This gives the model access to both past and future context at every position.
- **C — Incorrect.** The Bidirectional wrapper does not alter gradient flow direction. It simply processes the sequence in two temporal directions.
- **D — Incorrect.** Bidirectional processes a single sequence in two directions. It does not accept or process two separate sequences.

---

## Question 7

When preparing a time series for an LSTM model, why is normalization important?

A. Normalization converts categorical labels to numerical values required by LSTM gates.
B. Normalization prevents the hidden state from growing unboundedly, since values are accumulated across many time steps, and large inputs destabilize the sigmoid and tanh activations in LSTM gates.
C. Normalization is required by TensorFlow internally and will raise an error if skipped.
D. Normalization improves the interpretability of the model's hidden states.

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Label encoding is a preprocessing step for categorical variables and is unrelated to time series normalization or LSTM behavior.
- **B — Correct.** LSTM gates use sigmoid and tanh activations that saturate outside the range roughly (-3, 3). If raw inputs are in the hundreds or thousands, these activations saturate immediately, producing near-zero gradients and preventing learning. Normalization keeps inputs in a range where the gates remain sensitive and gradients flow.
- **C — Incorrect.** TensorFlow does not enforce normalization. Unnormalized inputs will run without errors but will typically produce poor training dynamics.
- **D — Incorrect.** Normalization affects numerical scale, not interpretability. Hidden states in LSTMs are not directly interpretable regardless of input scaling.

---

## Question 8

Which Keras callback combination is most appropriate for training an LSTM on a noisy time series?

A. `ModelCheckpoint` with `save_best_only=False` and `LearningRateScheduler` with a fixed step decay.
B. `EarlyStopping` with `restore_best_weights=True` and `ReduceLROnPlateau` to reduce the learning rate when validation loss plateaus.
C. `TensorBoard` and `CSVLogger` only, to monitor training without interfering with the optimization process.
D. `TerminateOnNaN` and `LambdaCallback` to print weights after each epoch.

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** `save_best_only=False` saves every epoch checkpoint, wasting disk space and not restoring best weights. Fixed step decay is less adaptive than `ReduceLROnPlateau` on noisy data.
- **B — Correct.** `EarlyStopping` with `restore_best_weights=True` stops training when validation loss stops improving and reverts to the best epoch's weights, preventing overfitting. `ReduceLROnPlateau` adapts the learning rate dynamically when progress stalls, helping the optimizer escape flat regions in the loss landscape.
- **C — Incorrect.** Logging callbacks are useful for monitoring but provide no optimization benefit. They are supplementary, not primary training control mechanisms.
- **D — Incorrect.** `TerminateOnNaN` is a safety callback for catastrophic failure. Printing weights each epoch is a debugging tool, not a training strategy.

---

## Question 9

A colleague trains a SimpleRNN on a sequence with 200 time steps and reports that the model learns short patterns well but fails to capture dependencies longer than 10–15 steps. What is the most likely cause?

A. The batch size is too large, causing the model to memorize training examples.
B. The hidden dimension is too small to store information about 200 time steps.
C. The vanishing gradient problem prevents gradients from propagating back beyond the most recent time steps, so the model cannot learn long-range dependencies.
D. The learning rate is too high, causing the model to skip over the optimal weights for long-range patterns.

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** Large batch size is associated with generalization issues, not the inability to learn long-range patterns within a sequence. This is a sequence modeling problem, not a memorization problem.
- **B — Incorrect.** While hidden dimension size affects model capacity, the described failure pattern — learning short patterns but not long ones — is the classic signature of the vanishing gradient problem, not a capacity limitation.
- **C — Correct.** This is the defining failure mode of vanilla RNNs. BPTT multiplies gradients by `W_hh` at each step; after 15–20 steps the gradient for earlier positions is effectively zero. The model receives no learning signal from inputs more than ~15 steps back, which is exactly the symptom described.
- **D — Incorrect.** A high learning rate causes instability or oscillation uniformly across all time steps. It would not selectively prevent learning of long-range dependencies while allowing short-range learning.

---

## Question 10

In the TensorFlow Developer Certificate context, what does the windowing function `make_windows(series, window_size=30, horizon=1)` produce?

A. A dataset of 30 independent samples, each with one time step and one label.
B. Overlapping input windows of length 30 with corresponding target values at `horizon` steps ahead, formatted as `(X, y)` arrays suitable for supervised sequence learning.
C. A sliding average of the series over 30-step windows, reducing the sequence length by a factor of 30.
D. A dataset split into 30 training folds for cross-validation with one held-out fold per iteration.

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** The function creates windows of 30 time steps each, not 30 one-step samples. Each row of X contains a full 30-step window, not a single time step.
- **B — Correct.** The windowing function slides a window of size 30 across the series, creating overlapping input sequences. For each window at position `i`, the input `X[i]` is `series[i:i+30]` and the target `y[i]` is `series[i+30]` (for horizon=1). This converts the raw series into a supervised learning problem suitable for LSTM or GRU training.
- **C — Incorrect.** That describes a moving average smoothing operation. The windowing function creates training examples, not a smoothed series.
- **D — Incorrect.** That describes k-fold cross-validation splitting. The windowing function is a data preparation step for sequence modeling, not a cross-validation scheme.

---

*End of Quiz — Module 10*

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

---

### Question 11 (5 points)

An LSTM layer is configured as `LSTM(128, dropout=0.2, recurrent_dropout=0.1)`. What do the `dropout` and `recurrent_dropout` parameters control?

- A) `dropout` randomly drops input connections; `recurrent_dropout` randomly drops connections between LSTM layers in a stacked architecture.
- B) `dropout` drops a fraction of the input-to-hidden connections at each time step; `recurrent_dropout` drops a fraction of the hidden-to-hidden (recurrent) connections at each time step.
- C) `dropout` removes entire time steps from the input sequence; `recurrent_dropout` removes entire hidden state dimensions.
- D) Both parameters are equivalent and either can be used independently to achieve the same regularization effect.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In Keras LSTM layers, `dropout` applies a dropout mask to the input-to-hidden weight matrix `W_x` connections, while `recurrent_dropout` applies a separate mask to the hidden-to-hidden weight matrix `W_h` connections. Crucially, in Keras the same mask is applied across all time steps within a sequence (not re-sampled each step), which is the "variational dropout" approach that improves regularization quality.
  - *Why A is incorrect:* `recurrent_dropout` affects the recurrent connection within a single LSTM cell (hidden state to hidden state), not connections between stacked LSTM layers. Inter-layer dropout is handled by a separate `Dropout` layer placed between the two LSTM layers.
  - *Why C is incorrect:* Neither parameter removes entire time steps or hidden dimensions. They apply a fractional binary mask to the weight connections, zeroing a random subset of the corresponding values at each forward pass during training.
  - *Why D is incorrect:* The two parameters regularize different weight matrices. `dropout` addresses input-to-hidden overfitting; `recurrent_dropout` addresses recurrent weight overfitting. They have complementary but distinct effects on the model.

---

### Question 12 (5 points)

For a univariate time series with 5,000 daily observations, a developer creates windows of size 60 with a horizon of 1. After windowing, what is the shape of the `X` array (before batching)?

- A) `(5000, 60)`
- B) `(4940, 60, 1)`
- C) `(4940, 60)`
- D) `(60, 5000, 1)`

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* For each starting position `i` from `0` to `4939`, the window `series[i:i+60]` becomes one row of `X`, and `series[i+60]` becomes the corresponding label. This produces `5000 - 60 = 4940` windows. Each window contains 60 time steps of scalar values, giving shape `(4940, 60)`.
  - *Why A is incorrect:* `(5000, 60)` would imply all 5,000 observations can start a window of length 60, which is impossible — the last valid window start is at index 4939 (requiring observations up to index 4999).
  - *Why B is incorrect:* `(4940, 60, 1)` is the correct shape for the expanded 3D tensor needed by LSTM (which expects `(batch, timesteps, features)`). The raw `X` array from windowing is 2D `(4940, 60)` for a univariate series. You must call `X = X.reshape(-1, 60, 1)` before passing to LSTM.
  - *Why D is incorrect:* `(60, 5000, 1)` transposes the intended dimensions. The first axis should be the number of samples (4940), not the window size.

---

### Question 13 (5 points)

Which statement about the GRU's reset gate is correct?

- A) The reset gate controls how much of the previous hidden state to forget before computing the candidate hidden state.
- B) The reset gate controls whether to update the hidden state with the new candidate or retain the old hidden state.
- C) The reset gate replaces the cell state from LSTM, providing a separate long-term memory pathway.
- D) The reset gate is applied to the input, filtering out irrelevant input features before they enter the recurrent computation.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* The GRU reset gate `r_t = sigmoid(W_r * [h_(t-1), x_t])` modulates how much of the previous hidden state `h_(t-1)` influences the computation of the candidate hidden state `h~_t`. When `r_t` is close to 0, the candidate hidden state is computed largely from the current input alone, effectively "resetting" the memory contribution of the past.
  - *Why B is incorrect:* The behavior described (deciding whether to update or retain) is the function of the **update gate** `z_t`, not the reset gate. The update gate determines how much the new candidate state replaces the old hidden state.
  - *Why C is incorrect:* The GRU has no separate cell state — that is an LSTM concept. The GRU merges cell and hidden state into a single hidden state, which is one of its architectural simplifications compared to LSTM.
  - *Why D is incorrect:* The reset gate operates on the hidden state, not the input. The input `x_t` is incorporated directly into both gate computations without a pre-filtering step.

---

### Question 14 (5 points)

A developer trains a stacked LSTM model and observes that the training loss decreases steadily but the validation loss increases after epoch 5. What is the most appropriate response?

- A) Increase the number of LSTM layers from 2 to 4 to give the model more capacity to generalize.
- B) Apply `recurrent_dropout` and `dropout` in each LSTM layer, and use `EarlyStopping(patience=5, restore_best_weights=True)`.
- C) Reduce the sequence window size from 60 to 10 to make the problem easier.
- D) Switch from Adam to SGD with no momentum to slow down training and prevent overfitting.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Diverging training and validation loss is the signature of overfitting. For recurrent networks, `recurrent_dropout` regularizes the hidden-to-hidden connections (the primary source of overfitting in LSTMs), while `dropout` regularizes the input connections. `EarlyStopping` with `restore_best_weights=True` stops training at the best generalization point (epoch 5 in this case) and restores those weights.
  - *Why A is incorrect:* Adding more LSTM layers increases model capacity, which will worsen overfitting for a model that is already overfitting. More layers should only be added if the model is currently underfitting.
  - *Why C is incorrect:* Reducing the window size throws away temporal context that may be valuable for the prediction task. It addresses the symptom by reducing problem complexity, not the root cause (model overfitting). Also, it may simply cause underfitting.
  - *Why D is incorrect:* SGD without momentum is generally slower and less effective than Adam for LSTM training. Slowing training does not address overfitting — it just extends the time before the overfitting becomes apparent. Regularization is the appropriate intervention.

---

### Question 15 (5 points)

What is the output shape of `Bidirectional(LSTM(64, return_sequences=True))` given an input shape of `(32, 100, 1)`?

- A) `(32, 64)`
- B) `(32, 100, 64)`
- C) `(32, 100, 128)`
- D) `(32, 200, 64)`

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* `Bidirectional` concatenates the forward and backward LSTM outputs. Each LSTM has 64 units, so each direction produces shape `(32, 100, 64)`. Concatenating along the last axis (units dimension) gives `(32, 100, 128)`. The sequence length (100) and batch size (32) are preserved by `return_sequences=True`.
  - *Why A is incorrect:* `(32, 64)` would be the output of a non-bidirectional `LSTM(64)` with `return_sequences=False`. Bidirectional doubles the output dimension, and `return_sequences=True` preserves the time axis.
  - *Why B is incorrect:* `(32, 100, 64)` would be the output of a non-bidirectional `LSTM(64, return_sequences=True)`. The `Bidirectional` wrapper doubles the last dimension from 64 to 128.
  - *Why D is incorrect:* `(32, 200, 64)` incorrectly doubles the sequence length. `Bidirectional` doubles the hidden state dimension, not the number of time steps. The temporal dimension remains 100.

---

### Question 16 (5 points)

When evaluating a time series forecasting model, why is Mean Absolute Error (MAE) often preferred over Mean Squared Error (MSE)?

- A) MAE is differentiable everywhere, making it more compatible with gradient-based optimizers than MSE.
- B) MAE penalizes errors in the original units of the prediction (e.g., dollars, degrees) making it directly interpretable, while MSE penalizes squared units and disproportionately punishes large errors.
- C) MAE automatically handles class imbalance in the time series by weighting rare extreme values more heavily.
- D) MAE is lower-bounded at zero and therefore cannot produce negative values, unlike MSE which can produce negative values.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* MAE measures the average absolute deviation in the original scale of the series. If you are predicting daily temperature in degrees Fahrenheit, an MAE of 2.5 means predictions are on average 2.5°F off — directly interpretable. MSE yields squared units (°F²), which are difficult to interpret intuitively. Additionally, MSE gives more weight to outliers by squaring the error, which may or may not be desirable depending on the application.
  - *Why A is incorrect:* MAE is actually NOT differentiable at zero (it has a kink). MSE is smooth everywhere, which makes it mathematically more convenient for gradient descent. Despite this, MAE is still used in practice because its interpretability outweighs the non-differentiability concern at zero.
  - *Why C is incorrect:* Neither MAE nor MSE provides automatic class-imbalance handling for time series. Addressing rare extreme events in time series requires domain-specific weighting, not a choice of error metric.
  - *Why D is incorrect:* Both MAE and MSE are lower-bounded at zero for any real-valued predictions. Neither can produce negative values. The zero lower bound is a property of both metrics, not a distinguishing factor.

---

### Question 17 (5 points)

A developer wants to make multi-step forecasts — predicting the next 7 days from a window of 30 days. Which output layer configuration is correct?

- A) `Dense(1, activation='linear')` — the model predicts one step at a time and is called 7 times.
- B) `Dense(7, activation='linear')` — the model predicts all 7 future steps in a single forward pass.
- C) `Dense(7, activation='softmax')` — softmax distributes probability mass across the 7 future time steps.
- D) `LSTM(7, return_sequences=True)` — the LSTM's 7 hidden states serve as the 7-step forecast.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* For a direct multi-step forecast, a `Dense(7)` output layer predicts all 7 future values simultaneously in a single forward pass. The target `y` is a vector of 7 consecutive values. The loss is typically MAE or MSE computed over all 7 predictions at once. This is the most common approach for fixed-horizon multi-step forecasting.
  - *Why A is incorrect:* While iterative single-step forecasting (option A) is a valid approach, it compounds errors — each prediction uses the previous (potentially erroneous) prediction as input. The question asks for an output layer configuration for a model that makes all 7 predictions at once, which is option B.
  - *Why C is incorrect:* `softmax` normalizes outputs to a probability distribution summing to 1. Future time step values are continuous real numbers, not probabilities. Using softmax on a regression target is incorrect.
  - *Why D is incorrect:* Using `LSTM(7, return_sequences=True)` would require 7 input time steps (not 30) and would output the hidden state at each of those 7 steps — not a forecast. The LSTM's hidden states are not directly interpretable as future values.

---

### Question 18 (5 points)

When using `tf.data.Dataset.window()` to create training windows, what does the `shift` parameter control?

- A) The number of time steps predicted into the future (the forecast horizon).
- B) The step size between consecutive window start positions — a `shift=1` creates maximally overlapping windows.
- C) The proportion of data reserved for the validation window at the end of the series.
- D) The number of time steps to skip between the input window and the target label.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In `tf.data.Dataset.window(size=window_size+1, shift=1)`, the `shift` parameter controls how many positions the window slides forward between consecutive windows. With `shift=1`, the window moves one step at a time, creating the maximum number of overlapping windows from the dataset. With `shift=window_size`, windows are non-overlapping. For most time series training pipelines, `shift=1` is standard.
  - *Why A is incorrect:* The forecast horizon (how many steps ahead to predict) is determined by how the window is split into input and target after creation — typically taking `window[:-1]` as input and `window[-1:]` as the target. It is not controlled by `shift`.
  - *Why C is incorrect:* Train/validation splitting for time series is done by slicing the series at a specific index (temporal split), not by the `shift` parameter of the window function.
  - *Why D is incorrect:* The gap between the last input time step and the target is determined by how the window array is indexed into `X` and `y` components. The `shift` parameter only controls window start position spacing.

---

### Question 19 (5 points)

What is the difference between `stateful=False` (default) and `stateful=True` LSTM layers in Keras?

- A) `stateful=True` enables the LSTM to use attention mechanisms, while `stateful=False` uses standard recurrent connections.
- B) With `stateful=False`, the hidden state is reset to zero at the start of each batch; with `stateful=True`, the hidden state from the last batch is passed as the initial state for the next batch.
- C) `stateful=True` causes the LSTM to share weights across all batches, reducing the parameter count to the size of a single batch.
- D) `stateful=False` uses MAE as the loss function, while `stateful=True` uses MSE for better gradient flow.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In the default stateless mode (`stateful=False`), each new batch is treated independently — the hidden state is zeroed before processing each batch. In `stateful=True` mode, the hidden and cell states from the end of batch N are used as the initial states for batch N+1. This is useful when sequences are too long to fit in a single window and must be split across multiple batches, but it requires careful data ordering and manual state resetting between epochs.
  - *Why A is incorrect:* Attention mechanisms are a separate architectural component, unrelated to the `stateful` parameter. Both stateful and stateless LSTMs can be combined with attention mechanisms.
  - *Why C is incorrect:* `stateful` has no effect on weight sharing or parameter count. LSTM weights are shared across time steps regardless of the `stateful` setting — that is standard parameter sharing in recurrent layers.
  - *Why D is incorrect:* The `stateful` parameter has no effect on the loss function. Loss functions are configured in `model.compile()` independently of the LSTM's state management mode.

---

### Question 20 (5 points)

A developer normalizes a time series using a `MinMaxScaler` fitted on the training set. After training and generating predictions, they reverse the normalization on the predictions. What is the correct tool for reversing the transformation?

- A) `scaler.inverse_fit(predictions)` — re-fits the scaler to the prediction range and reverses scaling.
- B) `scaler.inverse_transform(predictions.reshape(-1, 1))` — applies the inverse of the min-max transformation using the training statistics.
- C) `predictions * 255.0` — multiplies by the inverse of the standard normalization divisor.
- D) `predictions + scaler.mean_` — adds back the mean that was subtracted during normalization.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `MinMaxScaler.inverse_transform()` applies the inverse scaling formula: `x_original = x_scaled * (max - min) + min`, where `max` and `min` are the training set statistics captured when `.fit()` was called. The `reshape(-1, 1)` is required because `inverse_transform` expects a 2D array `(n_samples, n_features)`.
  - *Why A is incorrect:* `inverse_fit()` is not a method of scikit-learn scalers. The correct method name is `inverse_transform()`. Calling a non-existent method raises an `AttributeError`.
  - *Why C is incorrect:* Multiplying by 255.0 is the inverse of dividing by 255 for image pixel normalization. `MinMaxScaler` uses the min and max of the training data, not a fixed constant like 255. Applying an image normalization inverse to time series predictions would produce meaningless values.
  - *Why D is incorrect:* `scaler.mean_` is an attribute of `StandardScaler`, not `MinMaxScaler`. The inverse of z-score normalization is `x = x_scaled * scale_ + mean_`, which requires both the standard deviation and the mean. `MinMaxScaler` uses `data_min_` and `data_max_` attributes, not `mean_`.

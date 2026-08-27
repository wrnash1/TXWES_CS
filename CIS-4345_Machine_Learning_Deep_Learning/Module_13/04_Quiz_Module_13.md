# Quiz: Module 13 — Time Series Forecasting with TensorFlow

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Instructions

This quiz contains 10 multiple-choice questions. Each question is worth 10 points. Select the single best answer. Distractors are analyzed for each question to support exam preparation.

**Time limit:** 20 minutes

---

## Question 1

You have a time series with 2,000 observations. You want to create a windowed `tf.data.Dataset` with `window_size=20` and `shift=1`. How many training examples will the dataset contain (before batching)?

- A) 2,000
- B) 1,980
- C) 1,979
- D) 20

**Correct Answer:** C — 1,979

**Distractor Analysis:**

- **A (2,000):** Incorrect. A window of size 21 (`window_size + 1`) cannot start at positions 1,980 or later without running off the end (with `drop_remainder=True`).
- **B (1,980):** Close but off by one. After splitting into `(features, label)`, the first valid example uses positions 1–21, and the last uses positions 1,980–2,000. That is 1,980 windows, but with `drop_remainder=True` and the map step, it is 1,979 usable pairs.
- **C (1,979):** Correct. With 2,000 elements and `window_size + 1 = 21`, drop_remainder leaves `2000 - 21 + 1 = 1980` windows; after the map split each has 20 features and 1 label, so 1,980 examples. (Note: exact count depends on implementation; accept 1,979–1,980 in practice.)
- **D (20):** Incorrect. This is the window size, not the number of examples.

---

## Question 2

Which of the following is the correct way to perform a train/validation split for a time series dataset?

- A) Use `sklearn.model_selection.train_test_split` with `shuffle=True`
- B) Randomly assign 80% of time steps to training and 20% to validation
- C) Split by index so that all training observations occur before all validation observations
- D) Use k-fold cross-validation with 5 folds

**Correct Answer:** C

**Distractor Analysis:**

- **A:** Incorrect. `shuffle=True` randomizes the split, which causes data leakage by allowing future observations into the training set.
- **B:** Equivalent to A — random assignment violates temporal ordering.
- **C:** Correct. A **temporal split** ensures training data comes entirely before validation data, preventing leakage.
- **D:** Incorrect. Standard k-fold cross-validation shuffles data; time series cross-validation requires specialized walk-forward or expanding-window folds, not discussed in this module.

---

## Question 3

You call `dataset.window(window_size + 1, shift=1, drop_remainder=True)`. What is the purpose of `drop_remainder=True`?

- A) To drop batches smaller than the batch size
- B) To discard windows that would be shorter than `window_size + 1` due to end-of-series truncation
- C) To remove duplicate windows from the dataset
- D) To prevent shuffling from creating incomplete batches

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. `drop_remainder` in `.window()` applies to the window operation, not batching. Batch-level dropping is a parameter of `.batch()`.
- **B:** Correct. Without `drop_remainder=True`, the last window(s) at the end of the series may be shorter than `window_size + 1`, causing shape errors downstream.
- **C:** Incorrect. Windows naturally overlap by design; drop_remainder does not de-duplicate them.
- **D:** Incorrect. Shuffling has no interaction with drop_remainder in the window context.

---

## Question 4

A `Conv1D` layer requires its input to have shape `[batch, timesteps, channels]`. Your windowed dataset produces tensors of shape `[batch, window_size]`. Which operation adds the missing channel dimension?

- A) `tf.reshape(w, [window_size, 1, -1])`
- B) `tf.expand_dims(w, axis=0)`
- C) `tf.expand_dims(w, axis=-1)`
- D) `tf.squeeze(w, axis=-1)`

**Correct Answer:** C

**Distractor Analysis:**

- **A:** Incorrect. `tf.reshape` with these arguments produces the wrong shape and requires knowing the batch size.
- **B:** Incorrect. `axis=0` inserts a dimension at the front (batch axis), doubling the batch dimension.
- **C:** Correct. `axis=-1` appends a trailing dimension, transforming `[window_size]` into `[window_size, 1]`.
- **D:** Incorrect. `tf.squeeze` removes dimensions, which is the opposite of what is needed.

---

## Question 5

In a stacked LSTM model, the first LSTM layer uses `return_sequences=True`. What does this argument do?

- A) Returns the cell state in addition to the hidden state
- B) Returns the hidden state at every time step, not just the last
- C) Doubles the number of LSTM units in the layer
- D) Enables the layer to process sequences in reverse order

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. `return_sequences` does not expose the cell state; the cell state remains internal.
- **B:** Correct. With `return_sequences=True`, the LSTM outputs a tensor of shape `[batch, timesteps, units]` instead of `[batch, units]`.
- **C:** Incorrect. The number of units is set by the `units` argument, not `return_sequences`.
- **D:** Incorrect. Bidirectional processing requires wrapping the LSTM in `tf.keras.layers.Bidirectional`.

---

## Question 6

Your LSTM forecasting model achieves a validation MAE of 4.8. The naive baseline (predict previous value) achieves MAE of 5.2. What conclusion is most appropriate?

- A) The model is unusable because deep learning should achieve near-zero error
- B) The LSTM provides a modest improvement over the naive baseline
- C) The LSTM is overfitting and should be regularized
- D) MAE is not an appropriate metric for time series evaluation

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Near-zero error is only achievable when the series is nearly noise-free. Improvement over baseline is the correct standard.
- **B:** Correct. A 7.7% improvement `(5.2 - 4.8) / 5.2` over the naive baseline indicates the model has learned useful structure.
- **C:** Incorrect. Overfitting would be indicated by a large gap between training and validation MAE, not by the comparison to naive baseline.
- **D:** Incorrect. MAE is a standard, interpretable metric for time series forecasting.

---

## Question 7

Which of the following describes **data leakage** in the context of time series forecasting?

- A) Using more features than necessary in a multivariate model
- B) Including future observations in the training set
- C) Training on a series that has not been normalized
- D) Using the same window size for training and validation datasets

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Including extra features may cause overfitting but is not called data leakage.
- **B:** Correct. Leakage occurs when information from the future is available during training, leading to overly optimistic metrics that do not generalize.
- **C:** Incorrect. Lack of normalization is a preprocessing problem, not leakage.
- **D:** Incorrect. Consistent window sizes are standard practice and do not cause leakage.

---

## Question 8

You want to forecast electricity demand using both temperature readings and hour-of-day as inputs. Your window size is 24 hours. What should the `input_shape` argument be for an LSTM layer?

- A) `[24]`
- B) `[24, 1]`
- C) `[24, 2]`
- D) `[2, 24]`

**Correct Answer:** C

**Distractor Analysis:**

- **A:** Incorrect. This shape is for a univariate series used with a Dense layer (no channel dimension).
- **B:** Incorrect. This shape indicates one feature per time step; you have two features (temperature + hour).
- **C:** Correct. The LSTM input shape is `[timesteps, features]`, so `[24, 2]` represents 24 time steps with 2 features each.
- **D:** Incorrect. TensorFlow expects `[timesteps, features]`, not `[features, timesteps]`.

---

## Question 9

You are normalizing a time series for training and validation. Which normalization approach is correct?

- A) Compute mean and std from the full series (train + validation combined) and apply to both splits
- B) Compute mean and std from training data only; apply those same values to normalize the validation data
- C) Compute separate mean and std for training and validation independently
- D) No normalization is needed for LSTM models

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Using the full dataset (including validation) to compute statistics leaks validation information into preprocessing.
- **B:** Correct. This follows the principle of fitting transformations on training data only, then applying them to validation.
- **C:** Incorrect. Independent normalization of validation creates a different scale, making metrics incomparable and denormalization incorrect.
- **D:** Incorrect. Normalization stabilizes gradients and accelerates convergence for LSTMs, just as it does for other architectures.

---

## Question 10

Which metric penalizes large forecast errors more severely than small ones?

- A) MAE (Mean Absolute Error)
- B) MAPE (Mean Absolute Percentage Error)
- C) RMSE (Root Mean Squared Error)
- D) R-squared

**Correct Answer:** C

**Distractor Analysis:**

- **A:** Incorrect. MAE treats all errors proportionally (linear in error magnitude).
- **B:** Incorrect. MAPE is proportional to the percentage deviation, weighting errors relative to the actual value rather than squaring them.
- **C:** Correct. RMSE squares errors before averaging, so a single large error contributes disproportionately compared to many small errors.
- **D:** Incorrect. R-squared is a goodness-of-fit measure, not primarily a penalization metric for large errors.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | C |
| 2 | C |
| 3 | B |
| 4 | C |
| 5 | B |
| 6 | B |
| 7 | B |
| 8 | C |
| 9 | B |
| 10 | C |

---

## TF Certificate Exam Notes

Questions 1, 4, 5, and 8 directly mirror problem types observed in the TensorFlow Developer Certificate exam. Practice writing the windowed dataset function from memory and verifying input shapes before submitting exam code.

---

### Question 11 (5 points)

A developer uses `tf.data.Dataset.window(size=21, shift=1)` followed by `.flat_map(lambda w: w.batch(21, drop_remainder=True))`. What does the `flat_map` accomplish here?

- A) It batches the outer dataset into groups of 21 windows for mini-batch training.
- B) It flattens each nested window dataset into a single fixed-length tensor of shape `(21,)` so the windows can be used in a `model.fit()` call.
- C) It removes all windows that contain NaN values in any of their 21 time steps.
- D) It randomly shuffles the contents of each window before flattening.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `tf.data.Dataset.window()` creates a dataset of datasets — each element is itself a small `Dataset` containing the window elements. To use these with `model.fit()`, they must be converted into fixed-length tensors. `.flat_map(lambda w: w.batch(21, drop_remainder=True))` converts each inner `Dataset` window into a batch tensor of shape `(21,)`, producing a dataset of flat tensors that can then be split into features and labels.
  - *Why A is incorrect:* Batching the outer dataset is done with `.batch(batch_size)` applied to the final dataset. `flat_map` here operates on the inner window datasets, not the outer dataset of windows.
  - *Why C is incorrect:* NaN filtering would require `.filter(lambda x: tf.reduce_all(tf.math.is_finite(x)))`. The `flat_map` with `batch` does not inspect or filter individual values.
  - *Why D is incorrect:* Shuffling within a window would destroy the temporal ordering of each sequence, which would be harmful for time series models. `flat_map` with `batch` is a shape transformation, not a randomization operation.

---

### Question 12 (5 points)

A seasonal time series has daily observations with a strong 7-day weekly pattern. What `window_size` would best allow an LSTM model to capture this weekly seasonality?

- A) `window_size=1` — a single time step captures the most recent value
- B) `window_size=7` — exactly one week allows the model to see a full seasonal cycle
- C) `window_size=14` or larger — at least two full seasonal cycles provides context for comparing current behavior to the same point in previous weeks
- D) `window_size=365` — the full year is needed to capture any seasonal pattern

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* To recognize a weekly seasonal pattern, the model benefits from seeing at least two complete cycles (14+ days) so it can compare the current day to the same weekday in the previous week. With only 7 days, the model sees one cycle but cannot compare it to previous cycles. Larger windows (14–28 days) help the LSTM build an internal representation of the periodic pattern.
  - *Why A is incorrect:* A window of 1 step provides no sequential context. The model has no information about whether the current value is part of a rising or falling segment of the weekly cycle.
  - *Why B is incorrect:* While 7 days covers exactly one weekly period, the model cannot compare the current week's pattern to previous weeks with only one cycle of context. LSTMs generally benefit from multiple periods of context for accurate seasonal forecasting.
  - *Why D is incorrect:* While `window_size=365` would allow the model to see a full annual cycle, it dramatically increases input dimensionality and computational cost. For a 7-day weekly pattern, 2–4 weeks of context (14–28 steps) is typically sufficient and computationally practical.

---

### Question 13 (5 points)

When building a `Conv1D` model for time series forecasting, what is the key difference between `padding='causal'` and `padding='same'`?

- A) `padding='causal'` adds zeros at the end of the sequence; `padding='same'` adds zeros at the beginning.
- B) `padding='causal'` ensures that the convolution at time step `t` only uses inputs from time steps `≤ t`, preventing future information leakage; `padding='same'` uses inputs from both before and after each time step.
- C) `padding='causal'` reduces the sequence length by `kernel_size - 1`; `padding='same'` preserves the sequence length.
- D) Both padding modes produce identical output for time series forecasting — the choice only matters for NLP tasks.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In causal convolutions (also called masked convolutions), zero padding is applied only at the beginning of the sequence. This ensures that the output at time step `t` is computed only from inputs at time steps `1` through `t`. This is the correct approach for time series forecasting because the model should not "see" future values when making predictions — a real-time forecasting system would never have access to future data points.
  - *Why A is incorrect:* `padding='causal'` adds zeros at the beginning (left-side padding), not the end. This shifts the receptive field backward in time, making each output position look only at past inputs.
  - *Why C is incorrect:* Both `padding='causal'` and `padding='same'` preserve the sequence length in the output (both produce output length equal to input length). `padding='valid'` reduces the sequence length by `kernel_size - 1`.
  - *Why D is incorrect:* The choice between causal and same padding has critical implications for time series forecasting. Using `padding='same'` in an autoregressive forecasting model introduces future data leakage, producing optimistically biased training metrics that don't generalize to real-time inference.

---

### Question 14 (5 points)

A developer applies a `MinMaxScaler` to a training time series, trains an LSTM, generates predictions in the normalized range, and then calls `scaler.inverse_transform(predictions)`. The predictions are in the range `[0, 1]` but the original series ranged from 100 to 500. After inverse transform, the predictions are in the range `[98, 505]`. What is the most likely interpretation?

- A) The scaler inverse transform failed because the predictions slightly exceeded the `[0, 1]` range due to LSTM output non-linearity.
- B) The predictions are successfully denormalized to approximately the original scale, with slight overshoot beyond `[100, 500]` because the model predicted values slightly outside the training range.
- C) The model is overfitting — predictions should always stay within `[100, 500]` and any extrapolation beyond this range indicates memorization of training bounds.
- D) The inverse transform multiplied predictions by 255, indicating the wrong scaler (image normalization) was applied.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `MinMaxScaler` maps the training range `[100, 500]` to `[0, 1]`. Inverse transform maps `[0, 1]` back to `[100, 500]`. If the LSTM predicts values slightly outside `[0, 1]` (e.g., `-0.005` or `1.01`), the inverse transform legitimately maps these to values slightly below 100 or above 500. This is normal model behavior — the LSTM's output layer has no constraint forcing predictions within the training range.
  - *Why A is incorrect:* LSTM output with a linear final layer can indeed produce values outside `[0, 1]`. However, the inverse transform does not "fail" in this case — it correctly maps these extrapolated predictions back to the original scale, producing values slightly outside `[100, 500]`.
  - *Why C is incorrect:* Slight extrapolation beyond the training range is not evidence of overfitting. Overfitting is indicated by a large gap between training and validation MAE. Extrapolation is an expected property of regression models — they are not constrained to only predict within the training value range.
  - *Why D is incorrect:* Multiplication by 255 would produce values in the range `[25245, 128775]` — far beyond the observed `[98, 505]` range. The inverse transform produced values near `[100, 500]`, confirming the correct MinMaxScaler was applied.

---

### Question 15 (5 points)

In a `tf.data` pipeline for time series, why is `.shuffle()` applied BEFORE `.batch()`, not after?

- A) Shuffling after batching is more computationally expensive because it shuffles larger tensors.
- B) Shuffling before batching ensures that each mini-batch contains a random mix of time windows from different periods, preventing the optimizer from processing entire temporal segments as consecutive batches.
- C) Shuffling is required before batching in TensorFlow because `.batch()` raises an error if the input dataset is not already shuffled.
- D) Shuffling after batching would shuffle the individual time steps within each window, destroying the sequential order of inputs.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* If the windows are not shuffled before batching, consecutive batches will contain sequential windows — batch 1 contains windows 1–32, batch 2 contains windows 33–64, etc. This creates a highly correlated sequence of gradient updates that can cause the model to overfit to recent temporal patterns and converge poorly. Shuffling the individual windows before batching produces batches with a diverse mix of time periods, improving training stability and generalization.
  - *Why A is incorrect:* While shuffling a dataset of individual windows is computationally lighter than shuffling batches, this is not the primary reason for the ordering. The reason is gradient diversity during training, not computational efficiency.
  - *Why C is incorrect:* TensorFlow's `.batch()` does not require pre-shuffled input. It will batch whatever order of elements it receives. Applying `.shuffle()` after `.batch()` is technically valid but shuffles complete batches (not individual samples) — reducing intra-batch diversity.
  - *Why D is incorrect:* Shuffling after batching shuffles the ordering of complete batches, not the time steps within each window. Individual window time ordering is never affected by the `.shuffle()` operation because each window is a single tensor at the dataset element level.

---

### Question 16 (5 points)

A developer creates a naive "last value" baseline forecast for a time series. The MAE of this baseline is 8.3. An LSTM model achieves MAE of 9.1. What is the correct interpretation?

- A) The LSTM should be used because it is a more sophisticated model that will improve with more training data.
- B) The naive baseline outperforms the LSTM — the model adds no value and should not be deployed; investigate whether the architecture or hyperparameters need adjusting.
- C) An MAE of 9.1 is not statistically significantly worse than 8.3, so the models are equivalent.
- D) The LSTM is acceptable because the naive baseline is considered a trivial model that no real model should be compared against.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A baseline that simply predicts the previous observation achieves lower MAE than the LSTM, meaning the LSTM has not learned a useful pattern. The naive "last value" predictor is a meaningful benchmark — if a deep learning model cannot beat it, the model is failing to extract value from the data. Deployment of such a model would be wasteful and potentially harmful. Investigation should focus on window size, normalization, architecture, or dataset size.
  - *Why A is incorrect:* Model sophistication does not guarantee better performance. An LSTM that underperforms a naive baseline requires investigation and fixing, not blind deployment with the hope it will improve later.
  - *Why C is incorrect:* While statistical significance testing is valid for comparing models, a MAE of 9.1 vs 8.3 (an 8.7% degradation) is a practically meaningful difference for most forecasting applications. Worse performance than a zero-parameter baseline is always a red flag regardless of statistical significance.
  - *Why D is incorrect:* The naive baseline is one of the most important benchmarks in time series forecasting. It represents the simplest possible model and defines the minimum bar that a more complex model must clear to justify its computational cost.

---

### Question 17 (5 points)

When applying `StandardScaler` to a multivariate time series with 4 features (temperature, humidity, wind speed, pressure), what shape should the scaler's `fit` data be?

- A) Shape `(n_timesteps,)` — flatten all features into one array before fitting
- B) Shape `(n_timesteps, 4)` — one row per time step with all 4 features as columns
- C) Shape `(4, n_timesteps)` — transpose so each row is one feature's time series
- D) Shape `(n_timesteps, window_size, 4)` — include the windowing dimension for correct scaling

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `StandardScaler` computes per-feature mean and standard deviation. It expects a 2D array where rows are samples and columns are features. With shape `(n_timesteps, 4)`, it fits one mean and one standard deviation per column (per feature), correctly normalizing each of the 4 features independently. The fitted scaler is then applied to the full dataset before windowing.
  - *Why A is incorrect:* Flattening all 4 features into a single array computes one global mean and standard deviation across all features and all time steps. This incorrectly applies the same normalization to all features, ignoring that temperature (range ~0–40°C) and pressure (range ~950–1050 hPa) have completely different scales.
  - *Why C is incorrect:* `StandardScaler` expects samples as rows and features as columns — the opposite of `(4, n_timesteps)`. Passing a transposed array would compute statistics over individual features as if they were separate samples, producing incorrect normalization.
  - *Why D is incorrect:* Windowing creates overlapping sequences and should happen after scaling. Scaling the 3D windowed array `(n_windows, window_size, 4)` is technically possible but requires special handling and is not the standard approach. The correct order is: split → scale (on training data only) → window → batch.

---

### Question 18 (5 points)

What does the `horizon` parameter represent in a time series windowing function like `make_windows(series, window_size=30, horizon=3)`?

- A) The total length of each training example including both input and output: `30 + 3 = 33` time steps.
- B) The number of future time steps the model predicts — the target `y[i]` contains the 3 values immediately following the input window.
- C) The number of time steps to skip between consecutive windows to reduce dataset overlap.
- D) The maximum allowed error in the forecast before the model is considered to be failing.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In the `make_windows` convention used in TF Developer Certificate preparation, `horizon` specifies how many steps ahead to predict. For `horizon=3` and `window_size=30`, each training example has input `X[i] = series[i:i+30]` (30 steps) and target `y[i] = series[i+30:i+33]` (the next 3 steps). The model's output layer would be `Dense(3)` to predict all 3 future values simultaneously.
  - *Why A is incorrect:* The total window length for data loading is indeed `window_size + horizon = 33`, but `horizon` specifically refers to the number of output (target) steps, not the combined length. The model sees only the first 30 steps as input and predicts the next 3.
  - *Why C is incorrect:* Spacing between consecutive windows is controlled by the `shift` parameter in `tf.data.Dataset.window()`. `horizon` is about prediction depth (how far ahead to forecast), not sampling frequency.
  - *Why D is incorrect:* `horizon` is a data structuring parameter, not an evaluation threshold. Error thresholds are defined by the application domain (e.g., "forecast must be within ±5 degrees") and are separate from dataset construction.

---

### Question 19 (5 points)

A developer trains a time series model on data from 2015 to 2022 and evaluates on 2023. The model achieves excellent 2023 MAE. They then deploy the model, and its real-time accuracy is much worse. What is the most likely cause?

- A) The model overfit to the 2023 evaluation data because it was used for hyperparameter tuning.
- B) The 2024 real-time data has a distribution shift (new trends, changed seasonality, or regime changes) relative to the 2015–2022 training distribution.
- C) The model's `stateful=False` setting causes it to forget all patterns between deployment batches.
- D) The normalization scaler was not saved with the model, so real-time data is incorrectly scaled.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* If the 2023 evaluation set was used for hyperparameter selection (choosing window size, architecture, learning rate), then the model's reported 2023 metrics are overly optimistic — the model was effectively "tuned" on 2023 data. This is data leakage at the model selection level. When deployed to truly unseen 2024 data, performance degrades. This is a subtle but critical form of the train-test contamination problem.
  - *Why B is incorrect (but plausible):* Distribution shift between 2022 and 2024 is a genuine concern, but the question specifically says the 2023 evaluation was excellent and real-time accuracy is much worse. If the evaluation set (2023) was used for tuning decisions, the gap is explained by overfitting to the selection set.
  - *Why C is incorrect:* `stateful=False` means each batch is processed independently with a fresh hidden state — this is the standard behavior and does not cause accuracy degradation in deployment compared to evaluation.
  - *Why D is incorrect:* If the scaler were missing, all predictions would be in the normalized `[0, 1]` range rather than the original scale — this would be immediately obvious as catastrophically wrong outputs, not a subtle accuracy degradation.

---

### Question 20 (5 points)

In a `tf.data` time series pipeline, what does `.repeat()` do, and why is it sometimes necessary?

- A) It repeats each window element N times in the dataset to artificially increase dataset size for oversampling rare events.
- B) It makes the dataset loop indefinitely (or for a specified count), which was historically required when passing a dataset generator to `model.fit()` without specifying `steps_per_epoch`.
- C) It applies the same augmentation transformation N times to each window to generate diverse training examples.
- D) It prevents the dataset from being shuffled on repeated access, ensuring deterministic data ordering across all epochs.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Early TensorFlow 2.x required calling `.repeat()` on a dataset when passing it to `model.fit()` with `steps_per_epoch` specified — the dataset needed to be infinite (looping) so `fit()` could draw exactly `steps_per_epoch` batches per epoch for as many epochs as needed. In modern TF 2.x, `model.fit()` can handle finite datasets directly (it automatically loops over epochs), so `.repeat()` is less commonly required. However, when using `steps_per_epoch` for large streaming datasets, `.repeat()` is still needed.
  - *Why A is incorrect:* Oversampling specific elements is not what `.repeat()` does. It repeats the entire dataset sequence, not individual elements. Oversampling rare events would require `.filter()` + sampling logic or a manual class-weighted dataset.
  - *Why C is incorrect:* Augmentation is applied via `.map()` operations that include random transformations. `.repeat()` does not apply transformations — it simply loops the dataset. Each time through a repeated dataset, any random augmentation in `.map()` would produce different results because the random seed advances.
  - *Why D is incorrect:* `.repeat()` has no interaction with `.shuffle()`. Both operations are independent pipeline stages. Shuffling behavior is controlled entirely by the `.shuffle(buffer_size, seed)` parameters.

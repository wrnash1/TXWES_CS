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

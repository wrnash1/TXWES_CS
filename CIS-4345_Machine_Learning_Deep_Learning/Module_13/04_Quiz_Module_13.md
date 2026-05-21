# Quiz: Module 13 - Time Series Forecasting
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What is a "windowed dataset" in the context of time series forecasting with TensorFlow?
*   A) A dataset stored in a fixed-size memory buffer that flushes to disk when the buffer is full during training.
*   B) A technique that converts a raw time series into supervised learning pairs by sliding a fixed-size window across the series, using the window values as input features and the next value as the prediction target.
*   C) A validation strategy that evaluates model performance on a rolling 30-day window of the most recent data, excluding older observations from evaluation.
*   D) A data normalization method that scales each time step's value relative to the maximum value within the surrounding window of observations.
*   **Correct Answer:** B) For a series [1, 2, 3, 4, 5] with window_size=3, the windowed dataset produces: input=[1,2,3]→target=4, input=[2,3,4]→target=5. This converts the forecasting problem into a standard supervised learning task that a neural network can train on.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a data streaming buffer, not a time series preprocessing technique. Windowed datasets are about creating input/output pairs, not memory management.
    *   *Why B is correct:* In TensorFlow: `dataset.window(window_size+1, shift=1).flat_map(lambda w: w.batch(window_size+1)).map(lambda w: (w[:-1], w[-1:]))`. The `shift=1` parameter makes the window slide one step at a time.
    *   *Why C is incorrect:* This describes a walk-forward or expanding window validation strategy used to evaluate model generalization over time — it is an evaluation technique, not a dataset preparation method.
    *   *Why D is incorrect:* This describes local normalization or windowed scaling, a preprocessing technique. Windowed datasets refer to creating supervised learning pairs, not scaling values.

---

**Question 2**
Which of the following is the most accurate definition of the **naive forecast** and why it is important for time series evaluation?
*   A) A forecast produced by a fully connected Dense network with no hidden layers, used as a lightweight baseline before training deeper models.
*   B) A baseline forecast that predicts the next value to equal the most recent observed value. It establishes a minimum performance threshold — any useful model should produce lower MAE than the naive forecast.
*   C) A forecast that averages the entire historical series and predicts that average as every future value, representing the simplest possible statistical baseline.
*   D) A forecast produced by fitting a linear regression line to the training period and extrapolating it forward, representing the simplest learned model baseline.
*   **Correct Answer:** B) The naive forecast (`forecast[t] = series[t-1]`) is often surprisingly competitive on stationary or slowly-drifting series. Computing its MAE on the validation set gives a performance floor — if your neural network's MAE is not clearly below the naive MAE, the model has not learned anything useful.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A single-layer Dense network, however simple, still learns from data. The naive forecast uses no learning at all — it only looks at the immediately preceding value.
    *   *Why B is correct:* In Python: `naive_forecast = series[split_time-1:-1]` where `split_time` is the start of the validation window. MAE: `tf.keras.metrics.mean_absolute_error(y_val, naive_forecast).numpy()`.
    *   *Why C is incorrect:* Predicting the historical mean is the "mean forecast" baseline. While also a valid baseline, it is not the naive forecast. The naive forecast is value-at-lag-1, not the global mean.
    *   *Why D is incorrect:* Linear regression extrapolation is a simple learned model but it requires a fitting step. The naive forecast requires zero learning — it is purely `y_pred[t] = y_true[t-1]`.

---

**Question 3**
A developer builds an LSTM time series model. The input series has been converted to windows of 20 time steps for a univariate series. Which input shape should be specified for the model's first layer?
*   A) `input_shape=(20,)` — a flat 1D vector of 20 values.
*   B) `input_shape=(20, 1)` — a sequence of 20 time steps, each with 1 feature (univariate).
*   C) `input_shape=(1, 20)` — 1 sequence of length 20, matching the LSTM's expected batch-first format.
*   D) `input_shape=(None, 20)` — variable batch size with 20 features per step.
*   **Correct Answer:** B) LSTM layers expect 3D input of shape `(batch, timesteps, features)`. For a univariate series with window_size=20, the correct shape per sample is `(20, 1)` — 20 time steps, 1 feature each. The batch dimension is handled automatically by Keras.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `input_shape=(20,)` is a 1D flat vector — appropriate for Dense layers but not for LSTM. LSTM requires the timestep and feature dimensions to be separate. A Lambda layer expanding dims or explicit reshape is needed to convert from flat to sequence format.
    *   *Why B is correct:* Usage: `tf.keras.layers.LSTM(64, input_shape=(20, 1))`. Alternatively, use a Lambda layer as the first layer: `Lambda(lambda x: tf.expand_dims(x, axis=-1))` after accepting `input_shape=(20,)`.
    *   *Why C is incorrect:* `(1, 20)` would represent 1 time step with 20 features — this reverses the timestep and feature dimensions. The LSTM would see one step at a time with 20 simultaneous feature values, which is not the correct interpretation for a windowed univariate series.
    *   *Why D is incorrect:* `None` in `input_shape` represents a variable-length dimension. Setting `input_shape=(None, 20)` would mean variable number of time steps each with 20 features, which is wrong for a fixed window of 20 univariate values.

---

**Question 4**
Why is it important to shuffle a windowed time series dataset before training, even though the original series has a meaningful temporal order?
*   A) Shuffling is never appropriate for time series data because it destroys the temporal ordering that the model needs to learn from.
*   B) Shuffling the windowed pairs prevents the model from learning spurious correlations from the sequential order of mini-batches during gradient descent — each window pair is already a complete input/target sample, so the model learns from window content, not batch sequence.
*   C) Shuffling automatically applies data augmentation by randomly reversing some window sequences, which improves the model's ability to generalize across different sequence directions.
*   D) Shuffling must be applied before windowing because the `tf.data.Dataset.window()` function requires pre-sorted data to create correct overlapping windows.
*   **Correct Answer:** B) The temporal order within each window is preserved — the window still covers consecutive time steps in the correct order. Shuffling only randomizes which windows appear in which batch. This prevents gradient updates from being biased by the global order in which windows are presented to the optimizer.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Shuffling the windowed dataset is standard practice and appropriate. The key distinction is that shuffling occurs at the window level, not within each window — the internal order of each sample remains temporally correct.
    *   *Why B is correct:* In the `tf.data` pipeline: `.shuffle(buffer_size=1000)` after `.flat_map()` and before `.batch()`. The `buffer_size` should be at least as large as the number of windows to ensure proper randomization.
    *   *Why C is incorrect:* Shuffling in `tf.data` randomizes the order of complete windows — it does not reverse sequences internally. Sequence reversal would require a custom `.map()` transformation.
    *   *Why D is incorrect:* `tf.data.Dataset.window()` operates on the data in the order it receives it — it creates windows from whatever order the series is in. Sorting is not a requirement of `window()`.

---

**Question 5**
A time series forecasting model has training MAE of 3.2 and validation MAE of 3.5, while the naive forecast has MAE of 8.1 on the same validation period. What do these results indicate?
*   A) The model is severely overfitting — the large gap between training MAE and validation MAE means the model has memorized the training series.
*   B) The model is performing well — it generalizes close to training performance and substantially outperforms the naive baseline, suggesting it has learned useful patterns.
*   C) The model is underfitting — both MAE values are above zero, indicating the model has not yet converged to an optimal solution.
*   D) The naive forecast is performing poorly, which indicates the time series has no autocorrelation and a neural network cannot learn to forecast it.
*   **Correct Answer:** B) The gap between training MAE (3.2) and validation MAE (3.5) is small (less than 10% relative difference), indicating good generalization without significant overfitting. More importantly, the model's validation MAE of 3.5 is 57% below the naive forecast MAE of 8.1, demonstrating that the model has learned meaningful temporal patterns.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A 0.3 difference between training MAE (3.2) and validation MAE (3.5) is small and expected. Overfitting would show a much larger gap — e.g., training MAE of 0.5 vs validation MAE of 5.0.
    *   *Why B is correct:* Beating the naive forecast is the minimum requirement for a useful forecasting model. A 57% improvement over naive is a strong result. The tight train/val gap confirms the model generalizes well.
    *   *Why C is incorrect:* Any non-zero MAE does not indicate underfitting — perfect forecasting (MAE=0) is not possible on real series with noise. Underfitting would produce MAE values near or above the naive baseline, not well below it.
    *   *Why D is incorrect:* A high naive forecast MAE means the series changes significantly between consecutive time steps — it actually indicates the series has high variance that the naive predictor cannot handle. A neural network learning meaningful patterns (lower MAE) suggests the series does have learnable structure.

# Reading Guide: Module 13 - Time Series Forecasting
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 13 - Time Series Forecasting**! Time series forecasting is one of the four core task categories on the TensorFlow Developer Certificate exam. Unlike static datasets, time series data has a temporal ordering — each observation depends on the observations that came before it. This module covers how to prepare time series data for deep learning models using windowed datasets, and how to build forecasting models using Dense networks, LSTMs, and convolutional architectures.

You will learn to convert a raw time series into supervised learning format using sliding window sequences, normalize the data appropriately, and evaluate forecast quality with Mean Absolute Error (MAE).

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Windowed dataset**: A technique that converts a 1D time series into supervised learning input/output pairs by sliding a fixed-size window across the series. For a window size of W, input features are the W most recent values and the target is the next value. In TensorFlow: `tf.data.Dataset.from_tensor_slices(series).window(size+1, shift=1, drop_remainder=True).flat_map(lambda w: w.batch(size+1)).map(lambda w: (w[:-1], w[-1]))`.

*   **`tf.data.Dataset`**: The TensorFlow data pipeline API used for time series preprocessing. Key methods: `.window()` creates overlapping sub-series, `.flat_map()` converts them to tensors, `.shuffle()` randomizes order to prevent sequential overfitting, `.batch()` groups samples, and `.prefetch()` loads data ahead of training to reduce GPU idle time.

*   **Naive forecast**: A baseline forecast that predicts the next value to be equal to the most recent observed value: `forecast[t] = series[t-1]`. Used as a performance baseline — any useful model should outperform the naive forecast. Computing the naive MAE gives a lower bound for what a trivial predictor achieves.

*   **Mean Absolute Error (MAE)**: The primary evaluation metric for time series forecasting: `MAE = mean(|y_true - y_pred|)`. MAE is in the same units as the original series, making it easy to interpret. In Keras: `model.compile(loss='mae', optimizer='adam')` or computed post-hoc with `tf.keras.metrics.mean_absolute_error(y_true, y_pred)`.

*   **Learning rate finder**: A technique that runs a short training loop over a range of learning rates (e.g., log-scale from 1e-8 to 1e-1) and plots loss vs. learning rate. The optimal learning rate is the value just before loss begins to increase — typically used with `tf.keras.callbacks.LearningRateScheduler` in combination with `tf.keras.optimizers.SGD`.

*   **`Conv1D` for time series**: A 1D convolutional layer that applies learnable filters along the time axis to detect local temporal patterns (e.g., weekly periodicity). `tf.keras.layers.Conv1D(filters=32, kernel_size=5, activation='relu', input_shape=(window_size, 1))` processes the sequence locally before passing features to LSTM or Dense layers, often improving both accuracy and training speed.

---

### 2. Certification Exam Tips
*   **Input Shape for Time Series:** For a univariate series with window size W, input shape is `(W, 1)` — each timestep has 1 feature. The model receives batches of shape `(batch, W, 1)`. If using a Dense-only model, reshape or flatten first: `input_shape=(W,)`.
*   **Compile with MAE:** Time series regression models use `model.compile(loss='mae', optimizer='adam')`. Unlike classification, no `metrics=['accuracy']` — track `loss` and `val_loss` in training history.
*   **Lambda Layer for Reshaping:** The TF exam commonly uses `tf.keras.layers.Lambda(lambda x: tf.expand_dims(x, axis=-1))` as the first layer to add the channel dimension to a flat window, converting shape `(batch, W)` to `(batch, W, 1)` for LSTM or Conv1D layers.
*   **Study Resource:** The [TensorFlow time series forecasting tutorial](https://www.tensorflow.org/tutorials/structured_data/time_series) at tensorflow.org covers windowed dataset creation, LSTM forecasting, and MAE evaluation in the exact format used on the exam. The [TensorFlow Developer Certificate course on Coursera](https://www.coursera.org/professional-certificates/tensorflow-in-practice) by Laurence Moroney (free to audit) includes a dedicated time series module that is directly exam-representative.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Work through the [TensorFlow time series forecasting tutorial](https://www.tensorflow.org/tutorials/structured_data/time_series) at tensorflow.org. This free official tutorial covers `tf.data.Dataset` windowing, LSTM and Dense forecasting models, and MAE-based evaluation.
*   **Required Video:** Watch the time series forecasting lecture in the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers the windowed dataset pattern, naive baseline computation, and how to build and train LSTM forecasters with `tf.keras`.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Create a windowed dataset**: Use `tf.data.Dataset` to create `(window, label)` pairs from a synthetic sinusoidal series with `window_size=20`. Shuffle, batch (32), and prefetch (1).
*   **Build and train a forecasting model**: Define `Sequential([Lambda(expand_dims), LSTM(64, return_sequences=True), LSTM(32), Dense(1)])`, compile with `loss='mae', optimizer='adam'`, and train for 100 epochs with EarlyStopping.
*   **Compute and compare MAE**: Compute MAE for the naive forecast and your model's forecast on the validation period. Plot predicted vs. actual values with Matplotlib to visually inspect forecast quality.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and explain the windowed dataset pattern in your own words.
*   [ ] Work through the [TensorFlow time series forecasting tutorial](https://www.tensorflow.org/tutorials/structured_data/time_series).
*   [ ] Watch the time series lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 13 lab: windowed dataset, LSTM forecaster, MAE comparison.
*   [ ] Proceed to the Module 13 quiz.

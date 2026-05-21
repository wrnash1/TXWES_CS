# Quiz: Module 05 - TensorFlow and Keras Introduction
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
In the Keras build-compile-fit workflow, what does `model.compile()` configure?
*   A) The layer architecture and number of neurons in each layer
*   B) The optimizer algorithm, loss function, and evaluation metrics used during training
*   C) The train/test data split ratio and batch size
*   D) The number of epochs and learning rate schedule
*   **Correct Answer:** B) `model.compile()` sets the training configuration — which optimizer minimizes the loss, which loss function is used, and which metrics are tracked — without performing any training.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Layer architecture is defined when building the model with `tf.keras.Sequential([...])` or the Functional API, before compile is called.
    *   *Why B is correct:* The three key arguments are `optimizer=`, `loss=`, and `metrics=`. This must be called before `model.fit()`.
    *   *Why C is incorrect:* Data splitting is done externally with `train_test_split`; batch size is passed to `model.fit()`, not `model.compile()`.
    *   *Why D is incorrect:* Epochs are passed to `model.fit(epochs=)`; learning rate schedules are set on the optimizer object, not in compile directly.

---

**Question 2**
Which of the following is the most accurate definition of a **Keras EarlyStopping callback**?
*   A) A layer type that randomly sets a fraction of neuron outputs to zero during each training batch to prevent co-adaptation.
*   B) A training callback that monitors a specified metric (such as validation loss) and halts training automatically when the metric stops improving, preventing overfitting and wasted computation.
*   C) A function that loads a previously saved model from disk and resumes training from the last completed epoch.
*   D) A data preprocessing utility that splits the training dataset into mini-batches and shuffles them before each epoch.
*   **Correct Answer:** B) EarlyStopping watches a monitored metric and stops training after `patience` epochs with no improvement, then optionally restores the best weights.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a Dropout layer, which is a regularization technique, not a training callback.
    *   *Why B is correct:* Usage: `tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)`. This is a high-value exam pattern.
    *   *Why C is incorrect:* Loading a saved model uses `tf.keras.models.load_model()`; callbacks do not perform this function.
    *   *Why D is incorrect:* Mini-batch creation and shuffling are handled internally by `model.fit()`'s `batch_size` and `shuffle` parameters, not by callbacks.

---

**Question 3**
A developer needs to **save a trained Keras model to disk** for later deployment. Which code is correct?
*   A) `model.save('my_model.h5')`
*   B) `model.export('my_model.pkl')`
*   C) `np.save('weights.npy', model.layers)`
*   D) `model.compile(save_path='my_model')`
*   **Correct Answer:** A) `model.save()` serializes the full model — architecture, weights, and compile configuration — to HDF5 or SavedModel format.
*   **Distractor Analysis:**
    *   *Why A is correct:* Both `model.save('path.h5')` (HDF5) and `model.save('saved_model/')` (SavedModel directory) are valid. Reload with `tf.keras.models.load_model('path')`.
    *   *Why B is incorrect:* Keras models do not have an `.export()` method; `.pkl` is a Python pickle format used by scikit-learn, not TensorFlow.
    *   *Why C is incorrect:* `np.save()` saves NumPy arrays; it cannot serialize an entire Keras model with its architecture and compile state.
    *   *Why D is incorrect:* `model.compile()` has no `save_path` argument; it only configures the optimizer, loss, and metrics.

---

**Question 4**
When calling `model.fit(X_train, y_train, epochs=20, validation_data=(X_val, y_val))`, what does the `validation_data` argument do?
*   A) It splits `X_train` internally so part of it is used for validation instead of training.
*   B) It evaluates the model on the provided validation set at the end of each epoch and reports validation loss and metrics without using that data for weight updates.
*   C) It enables data augmentation on the validation examples to improve generalization.
*   D) It stops training when validation accuracy reaches 100%.
*   **Correct Answer:** B) `validation_data` provides a held-out dataset that is evaluated each epoch to monitor generalization, but its samples never contribute to gradient updates.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* That describes `validation_split=0.2`, which carves a fraction from `X_train`. `validation_data` accepts a separate pre-split dataset.
    *   *Why B is correct:* The validation metrics appear as `val_loss`, `val_accuracy`, etc. in training output and in `history.history`.
    *   *Why C is incorrect:* Data augmentation is a separate preprocessing step; `validation_data` does not apply augmentation.
    *   *Why D is incorrect:* Stopping on accuracy is controlled by `EarlyStopping(monitor='val_accuracy')`; `validation_data` alone does not stop training.

---

**Question 5**
Which Keras code correctly builds a model for 10-class image classification using the Sequential API?
*   A) `model = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)), tf.keras.layers.Dense(128, activation='relu'), tf.keras.layers.Dense(10, activation='softmax')])`
*   B) `model = tf.keras.Sequential([tf.keras.layers.Dense(128, activation='sigmoid'), tf.keras.layers.Dense(1, activation='sigmoid')])`
*   C) `model = tf.keras.Sequential([tf.keras.layers.Dense(10, activation='relu'), tf.keras.layers.Dense(1, activation='linear')])`
*   D) `model = tf.keras.Sequential([tf.keras.layers.LSTM(128), tf.keras.layers.Dense(10, activation='softmax')])`
*   **Correct Answer:** A) Flatten reshapes 2D image input to 1D, a hidden Dense layer with ReLU learns features, and a 10-unit softmax output produces a probability distribution over 10 classes.
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the standard MNIST-style model. Compile with `loss='sparse_categorical_crossentropy'` (integer labels) or `'categorical_crossentropy'` (one-hot labels).
    *   *Why B is incorrect:* A single sigmoid output unit produces a binary probability, not a 10-class distribution. This is suitable for binary classification only.
    *   *Why C is incorrect:* A linear output with 1 unit is for regression. Using ReLU in the output layer for classification prevents gradient flow and cannot produce valid class probabilities.
    *   *Why D is incorrect:* LSTM layers are designed for sequential/time-series data, not flat image tensors. While technically runnable, LSTM is not the correct architecture for image classification.

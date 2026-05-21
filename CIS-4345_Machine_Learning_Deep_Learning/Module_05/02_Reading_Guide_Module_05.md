# Reading Guide: Module 05 - TensorFlow and Keras Introduction
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 05 - TensorFlow and Keras Introduction**! This module marks the transition from classical ML to the TensorFlow ecosystem. TensorFlow is the open-source deep learning framework developed by Google; Keras is its high-level API that makes building and training neural networks approachable. The TensorFlow Developer Certificate exam is conducted entirely within TensorFlow 2.x and tf.keras — this module establishes the foundational patterns you will use for every remaining module.

You will learn the Sequential and Functional API model building patterns, how to compile and fit models, how to use callbacks, and how to save and reload trained models.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **tf.keras.Sequential**: The simplest Keras model type — a linear stack of layers where each layer has exactly one input tensor and one output tensor. Defined as `model = tf.keras.Sequential([layer1, layer2, ...])`. Used for the majority of TF Developer Certificate exam tasks including image classification, NLP, and time series.

*   **model.compile()**: Configures the model for training by specifying the optimizer (e.g., `'adam'`), the loss function (e.g., `'sparse_categorical_crossentropy'`), and evaluation metrics (e.g., `['accuracy']`). Must be called before `model.fit()`. The compile step does not train the model — it only sets up the training configuration.

*   **model.fit()**: Runs the training loop. Key parameters: `x` (training inputs), `y` (training labels), `epochs` (number of full passes over training data), `validation_data` (tuple of val inputs and labels for per-epoch evaluation), `callbacks` (list of Callback objects). Returns a History object.

*   **Keras Callback**: An object passed to `model.fit()` that can execute code at various training events. The most important callbacks for the exam are: `EarlyStopping(monitor='val_loss', patience=3)` to stop training when validation loss stops improving, and `ModelCheckpoint` to save the best weights during training.

*   **model.save() / tf.keras.models.load_model()**: Serializes a trained model to disk in either HDF5 format (`model.save('model.h5')`) or SavedModel format (`model.save('saved_model/')`). The SavedModel format is the TensorFlow standard and is required for TF Serving deployment. Load with `tf.keras.models.load_model('path')`.

*   **TensorFlow tensor**: The fundamental data unit in TensorFlow — an N-dimensional array with a fixed dtype. TensorFlow tensors are similar to NumPy arrays but can be placed on GPU/TPU and support automatic differentiation. `tf.constant()`, `tf.Variable()`, and layer outputs are all tensors.

---

### 2. Certification Exam Tips
*   **Exam Environment:** The TF Developer Certificate exam runs in PyCharm with TensorFlow 2.x pre-installed. You write Python scripts, not Jupyter notebooks. Practice running `.py` files, not just notebooks.
*   **Three-Step Pattern:** Every exam task follows the same pattern: (1) build with `tf.keras.Sequential([...])`, (2) compile with `model.compile(optimizer=, loss=, metrics=)`, (3) train with `model.fit(X_train, y_train, epochs=, validation_data=)`. Memorize this pattern cold.
*   **EarlyStopping:** The exam often rewards training efficiency. Use `callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)]` to avoid overfitting and wasted epochs.
*   **Study Resource:** The [official TensorFlow Keras overview](https://www.tensorflow.org/guide/keras) at tensorflow.org/guide/keras covers all Sequential and Functional API patterns tested on the exam. The [Keras getting started guide](https://keras.io/getting_started/) at keras.io provides additional interactive examples using the same API.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the [TensorFlow Keras Sequential model guide](https://www.tensorflow.org/guide/keras/sequential_model) and the [training and evaluation guide](https://www.tensorflow.org/guide/keras/training_with_built_in_methods) at tensorflow.org. These free official docs walk through the complete build-compile-fit workflow used on the certification exam.
*   **Required Video:** Watch the TensorFlow and Keras introduction segment of the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers `tf.keras.Sequential`, `model.compile()`, `model.fit()`, and callback usage with runnable examples.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Build and compile a Sequential model**: Define a multi-layer network for a classification task using `tf.keras.Sequential`, then call `model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])`.
*   **Train with EarlyStopping**: Call `model.fit()` with `validation_split=0.2` and `callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)]`. Observe which epoch training stops.
*   **Save and reload the model**: Use `model.save('my_model.h5')` and then `loaded = tf.keras.models.load_model('my_model.h5')`. Confirm predictions match by running `model.predict()` on both objects.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and write a three-step Keras code template from memory.
*   [ ] Review the [Keras Sequential model guide](https://www.tensorflow.org/guide/keras/sequential_model) and [training guide](https://www.tensorflow.org/guide/keras/training_with_built_in_methods).
*   [ ] Watch the TensorFlow/Keras lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 05 lab: Sequential model with EarlyStopping and model save/load.
*   [ ] Proceed to the Module 05 quiz.

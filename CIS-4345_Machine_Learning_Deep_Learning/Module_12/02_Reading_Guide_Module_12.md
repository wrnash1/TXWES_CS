# Reading Guide: Module 12 - Hyperparameter Tuning and Keras Tuner
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 12 - Hyperparameter Tuning and Keras Tuner**! Hyperparameters are the configuration choices that govern model architecture and training but are not learned from data — things like learning rate, number of layers, number of units per layer, dropout rate, and batch size. Choosing these values manually by intuition is inefficient; automated hyperparameter search finds better configurations faster.

Keras Tuner is the official TensorFlow library for automated hyperparameter optimization. It provides search strategies — Random Search, Hyperband, and Bayesian Optimization — that systematically explore the hyperparameter space and identify the best-performing configuration.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Hyperparameter**: A configuration value set before training that controls the learning process itself, as opposed to a model parameter (weight or bias) that is learned during training. Examples: learning rate, number of Dense units, dropout rate, number of layers, batch size, optimizer choice. Hyperparameters must be tuned to get good model performance.

*   **Keras Tuner**: An official TensorFlow library for automated hyperparameter optimization. Installed via `pip install keras-tuner`. Provides the `HyperModel` interface and search strategies: `RandomSearch`, `Hyperband`, and `BayesianOptimization`. Each search trial builds and evaluates a model with a different hyperparameter combination.

*   **`HyperParameters` object (`hp`)**: The object passed to the model-building function in Keras Tuner that defines the search space. Usage: `hp.Int('units', min_value=32, max_value=512, step=32)` searches integer values; `hp.Float('learning_rate', min_value=1e-4, max_value=1e-2, sampling='log')` searches float values on a log scale; `hp.Choice('activation', ['relu', 'tanh'])` searches categorical choices.

*   **Random Search**: A Keras Tuner search strategy that samples hyperparameter combinations randomly from the defined search space. More efficient than grid search (which exhaustively tries all combinations) and often finds good solutions quickly. Usage: `tuner = kt.RandomSearch(build_model, objective='val_accuracy', max_trials=20)`.

*   **Hyperband**: An advanced Keras Tuner search strategy based on the Hyperband algorithm that runs many configurations for a few epochs, then promotes only the best-performing ones for more epochs. Hyperband is more efficient than Random Search for expensive models because it eliminates poor configurations early.

*   **`tuner.search()`**: The method that runs the hyperparameter search. It calls the model-building function for each trial, trains the model on training data, and evaluates on validation data. Usage: `tuner.search(X_train, y_train, epochs=50, validation_split=0.2, callbacks=[tf.keras.callbacks.EarlyStopping(patience=3)])`.

---

### 2. Certification Exam Tips
*   **Model-Building Function Pattern:** The Keras Tuner model-building function always takes `hp` as its only argument and must return a compiled model. The `hp` object is used to define the hyperparameter ranges. The function is passed as the first argument to the tuner constructor.
*   **`tuner.get_best_hyperparameters()`:** After `tuner.search()` completes, retrieve the best-found hyperparameter values with `best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]`. Then build the final model: `model = tuner.hypermodel.build(best_hps)`.
*   **Manual Grid Search:** Even without Keras Tuner, you can manually search learning rates by training the same architecture with `learning_rate` in `[1e-4, 1e-3, 1e-2]` and comparing `val_loss`. The TF exam may require recognizing which hyperparameter change improves a given scenario.
*   **Study Resource:** The [Keras Tuner introduction tutorial](https://www.tensorflow.org/tutorials/keras/keras_tuner) at tensorflow.org walks through the complete Random Search workflow — defining the search space, running `tuner.search()`, and retrieving the best model — using the exact API tested on the exam. The [Keras Tuner documentation](https://keras.io/keras_tuner/) at keras.io covers all search strategies with runnable examples.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Work through the [TensorFlow Keras Tuner tutorial](https://www.tensorflow.org/tutorials/keras/keras_tuner) at tensorflow.org. This free official tutorial is the primary reference for the Keras Tuner API and covers the complete workflow from search space definition to final model training.
*   **Required Video:** Watch the hyperparameter tuning lecture in the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers the concept of hyperparameters vs. parameters, manual tuning strategies, and the Keras Tuner API.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Define a tunable model**: Write a `build_model(hp)` function that uses `hp.Int('units', 32, 256, step=32)` for Dense layer sizes and `hp.Float('learning_rate', 1e-4, 1e-2, sampling='log')` for the Adam optimizer learning rate.
*   **Run a Random Search**: Create `tuner = kt.RandomSearch(build_model, objective='val_accuracy', max_trials=15)` and call `tuner.search(X_train, y_train, epochs=30, validation_split=0.2)`.
*   **Retrieve and train the best model**: Call `best_hps = tuner.get_best_hyperparameters(1)[0]`, build the final model with `model = tuner.hypermodel.build(best_hps)`, and train it to convergence with EarlyStopping.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and explain the difference between a hyperparameter and a model parameter.
*   [ ] Work through the [TensorFlow Keras Tuner tutorial](https://www.tensorflow.org/tutorials/keras/keras_tuner).
*   [ ] Watch the hyperparameter tuning lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 12 lab: Random Search with Keras Tuner on a classification task.
*   [ ] Proceed to the Module 12 quiz.

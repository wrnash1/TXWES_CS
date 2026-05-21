# Quiz: Module 12 - Hyperparameter Tuning and Keras Tuner
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
Which of the following is a hyperparameter, as opposed to a model parameter that is learned during training?
*   A) The weight values in a Dense layer that are updated by the optimizer during backpropagation.
*   B) The bias terms added to each neuron's weighted sum that shift the activation function.
*   C) The learning rate passed to the Adam optimizer that controls the step size during gradient descent.
*   D) The output of the softmax activation function that represents predicted class probabilities.
*   **Correct Answer:** C) The learning rate is set before training begins and is not updated by backpropagation — it controls how backpropagation updates the parameters. Hyperparameters include: learning rate, number of layers, units per layer, dropout rate, batch size, and optimizer type.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Dense layer weights are model parameters — they start at random values and are updated by the optimizer via backpropagation on every training step. They are the quantities being learned.
    *   *Why B is incorrect:* Bias terms are also learned model parameters, updated during training alongside the weights.
    *   *Why C is correct:* Learning rate is configured before training in `model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001))`. It does not change during training unless a learning rate scheduler callback is used.
    *   *Why D is incorrect:* Softmax output values are computed during the forward pass from the model's learned weights — they are outputs, not configuration settings.

---

**Question 2**
Which of the following is the most accurate definition of **Keras Tuner**?
*   A) A Keras callback that monitors training metrics and automatically adjusts the model architecture by adding or removing layers when validation loss stops improving.
*   B) A TensorFlow library for automated hyperparameter optimization that systematically searches over a defined hyperparameter space, trains a model for each configuration, and identifies the best-performing hyperparameter combination.
*   C) A visualization tool that plots training and validation loss curves across epochs to help identify the optimal stopping point for early termination.
*   D) A model compression utility that reduces the number of parameters in a trained neural network by pruning low-magnitude weights for deployment on edge devices.
*   **Correct Answer:** B) Keras Tuner decouples the hyperparameter search from model training. You define the search space via an `hp` object in a model-building function, choose a search strategy (RandomSearch, Hyperband, BayesianOptimization), and call `tuner.search()` to find the best configuration.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Automatic architecture modification during training is not what Keras Tuner does. Keras Tuner runs separate trials — each trial builds a new fixed architecture from scratch and trains it independently.
    *   *Why B is correct:* Install with `pip install keras-tuner`. Usage: `import keras_tuner as kt`. The tuner calls the build function once per trial with a different hyperparameter sample.
    *   *Why C is incorrect:* Training curve visualization is done with Matplotlib using `history.history` from `model.fit()`. Keras Tuner runs the search but does not produce loss curve plots.
    *   *Why D is incorrect:* This describes model pruning (e.g., TensorFlow Model Optimization Toolkit). Keras Tuner optimizes hyperparameter selection before/during training, not post-training model compression.

---

**Question 3**
A developer writes a Keras Tuner model-building function. Which code correctly defines a tunable number of Dense units between 32 and 256 in steps of 32?
*   A) `units = hp.Int('units', min_value=32, max_value=256, step=32)`
*   B) `units = hp.search('units', range(32, 256, 32))`
*   C) `units = hp.uniform('units', 32, 256)`
*   D) `units = hp.tune(Dense, min=32, max=256)`
*   **Correct Answer:** A) `hp.Int()` defines an integer hyperparameter with explicit bounds and a step size. Keras Tuner will try values 32, 64, 96, 128, 160, 192, 224, and 256 during the search, depending on the strategy.
*   **Distractor Analysis:**
    *   *Why A is correct:* The full usage in a model-building function: `def build_model(hp): units = hp.Int('units', min_value=32, max_value=256, step=32); model = tf.keras.Sequential([tf.keras.layers.Dense(units, activation='relu'), ...]); return model`.
    *   *Why B is incorrect:* `hp.search()` is not a valid Keras Tuner method. The `hp` object provides specific typed methods: `hp.Int()`, `hp.Float()`, `hp.Choice()`, `hp.Boolean()`.
    *   *Why C is incorrect:* `hp.uniform()` is not a Keras Tuner method — it is a scipy distribution sampling function. For float hyperparameters, Keras Tuner uses `hp.Float()` with a `sampling` argument.
    *   *Why D is incorrect:* `hp.tune()` is not a valid Keras Tuner API call. Keras Tuner does not have a method that directly wraps layer constructors.

---

**Question 4**
After calling `tuner.search(X_train, y_train, epochs=30, validation_split=0.2)`, how does a developer retrieve the best hyperparameters and build the final model?
*   A) `model = tuner.best_model()` — Keras Tuner automatically stores the fully trained best model as an attribute.
*   B) `best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]; model = tuner.hypermodel.build(best_hps)` — retrieve the best hyperparameter values, then build a new model instance using those values.
*   C) `model = tuner.results[-1]` — the last element of the results list contains the model trained with the best hyperparameters.
*   D) `best_hps = tuner.search_results['best']; model = tf.keras.models.load_model(best_hps)` — load the best model directly from the search results dictionary.
*   **Correct Answer:** B) `get_best_hyperparameters()` returns a list of `HyperParameters` objects sorted by objective value. Index `[0]` gives the best. `tuner.hypermodel.build(best_hps)` creates a fresh model with those hyperparameter values, which you then train to convergence with EarlyStopping.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Keras Tuner does not expose a `best_model()` method as an attribute. The search process evaluates configurations but does not store a single "best model" object directly.
    *   *Why B is correct:* Full workflow: `best_hps = tuner.get_best_hyperparameters(1)[0]` → `model = tuner.hypermodel.build(best_hps)` → `model.fit(X_train, y_train, epochs=100, validation_split=0.2, callbacks=[EarlyStopping(patience=5)])`.
    *   *Why C is incorrect:* `tuner.results` is not a valid Keras Tuner attribute. Trial results are accessed through `tuner.oracle.get_best_trials()` or `tuner.get_best_hyperparameters()`, not a list index.
    *   *Why D is incorrect:* `tuner.search_results` is not a valid attribute. Loading a model from a hyperparameter object with `load_model` makes no sense — hyperparameters are configuration values, not saved model file paths.

---

**Question 5**
A developer manually tests three learning rate values (0.1, 0.01, 0.001) for an Adam optimizer and records validation accuracy after 20 epochs: 0.1 → 62%, 0.01 → 88%, 0.001 → 83%. What does this indicate, and what would be the best next step?
*   A) The optimal learning rate is exactly 0.01 — there is no need to search further since the highest accuracy has been found.
*   B) The learning rate of 0.1 caused divergence or oscillation; 0.01 performs best in this range. A refined search around 0.01 (e.g., 0.005, 0.01, 0.02) or using Keras Tuner's `hp.Float('lr', 1e-3, 1e-1, sampling='log')` could identify an even better value.
*   C) The results show that higher learning rates always produce worse models — the search should continue only with values smaller than 0.001.
*   D) Manual learning rate testing is never valid because it causes data leakage between trials. Only automated Keras Tuner searches produce reliable hyperparameter estimates.
*   **Correct Answer:** B) The performance curve (low at 0.1, peak at 0.01, slight drop at 0.001) is a classic learning rate sensitivity pattern. The true optimum likely lies near 0.01. A log-scale search between 0.005 and 0.05 using Keras Tuner's `hp.Float()` with `sampling='log'` would efficiently narrow the best range.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Three-point manual grid search with 5% increments cannot guarantee the optimum is at exactly 0.01. The true best learning rate may lie between tested values, and results can vary with random seed and data split.
    *   *Why B is correct:* Log-scale search is appropriate for learning rates because they span several orders of magnitude. `hp.Float('learning_rate', 1e-4, 1e-1, sampling='log')` in Keras Tuner samples densely on the log scale, concentrating more trials around common learning rates.
    *   *Why C is incorrect:* The drop from 0.01 to 0.001 (88% to 83%) does not indicate a monotonic trend toward smaller values. Very small learning rates converge too slowly in 20 epochs. The optimum is interior to the tested range, not at its boundary.
    *   *Why D is incorrect:* Manual learning rate grid search on a validation set is a standard and valid practice. Data leakage occurs when test data influences preprocessing or feature selection — evaluating hyperparameters on a held-out validation set is the correct and expected approach.

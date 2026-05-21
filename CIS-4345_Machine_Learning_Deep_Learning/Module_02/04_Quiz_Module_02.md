# Quiz: Module 02 - Python for ML
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What is the objective of feature scaling (normalization/standardization) before training a neural network?
*   A) To reduce the number of training samples
*   B) To ensure all input features contribute equally to gradient updates and prevent slow or failed convergence
*   C) To convert labels from integers to strings
*   D) To remove duplicate rows from the dataset
*   **Correct Answer:** B) Neural networks use gradient descent; features on vastly different scales cause gradients to be dominated by large-scale features, slowing learning.
*   **Distractor Analysis:**
    *   *Why correct:* Scaling centers and narrows the loss surface so gradient descent converges faster and more reliably.
    *   *Why A is incorrect:* Scaling does not change the number of samples, only the numeric range of feature values.
    *   *Why C is incorrect:* Label encoding is a separate step; scaling applies to input features, not labels.
    *   *Why D is incorrect:* Removing duplicates is a data cleaning step unrelated to feature scaling.

---

**Question 2**
Which of the following is the most accurate definition of a **Pandas DataFrame**?
*   A) A one-dimensional array of fixed-type values indexed by integers, equivalent to a single column of a spreadsheet.
*   B) A two-dimensional labeled data structure with named columns that can hold mixed data types, used to load, inspect, and preprocess tabular datasets.
*   C) A compiled computation graph that TensorFlow uses to execute tensor operations efficiently on GPU hardware.
*   D) A dictionary mapping word tokens to integer indices, used to encode text sequences for NLP models.
*   **Correct Answer:** B) A DataFrame is Pandas' primary tabular data structure — equivalent to a spreadsheet with labeled rows and columns.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes a Pandas Series, which is one-dimensional. A DataFrame is two-dimensional with multiple named columns.
    *   *Why B is correct:* DataFrames provide methods for loading CSVs, handling missing values, filtering rows, and encoding features — all critical preprocessing steps.
    *   *Why C is incorrect:* This describes a TensorFlow computation graph, not a Pandas data structure.
    *   *Why D is incorrect:* This describes a word-to-index vocabulary mapping used in NLP tokenization, not a DataFrame.

---

**Question 3**
A developer needs to **load a CSV file and inspect the first five rows**. Which commands are most appropriate?
*   A) `df = pd.read_csv('data.csv'); df.head()`
*   B) `model.fit(X_train, y_train, epochs=10)`
*   C) `np.reshape(X, (-1, 28, 28, 1))`
*   D) `accuracy_score(y_test, predictions)`
*   **Correct Answer:** A) `pd.read_csv()` loads a CSV into a DataFrame and `.head()` displays the first five rows for inspection.
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the standard Pandas pattern for loading and previewing tabular data before preprocessing.
    *   *Why B is incorrect:* `model.fit()` trains a Keras model; it cannot load or preview a CSV file.
    *   *Why C is incorrect:* `np.reshape()` changes array dimensions; it does not load files.
    *   *Why D is incorrect:* `accuracy_score` evaluates predictions; it does not load or inspect data.

---

**Question 4**
While preprocessing data for a model, a developer fits a `StandardScaler` on the full dataset (training + test) before splitting. What ML problem does this cause?
*   A) Underfitting — the model becomes too simple because the scaler removes useful variance.
*   B) Data leakage — test set statistics influence the scaler, giving an overly optimistic evaluation.
*   C) Class imbalance — scaling changes the ratio of positive to negative examples.
*   D) Gradient explosion — large scaled values cause weight updates to become unbounded.
*   **Correct Answer:** B) Fitting the scaler on combined data lets test-set mean and std influence preprocessing, making test performance appear better than it truly is.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Underfitting results from a model that is too simple, not from scaler fitting order.
    *   *Why B is correct:* The fix is `scaler.fit(X_train)` then `scaler.transform(X_test)` — the test set should never influence any fitted transform.
    *   *Why C is incorrect:* Scaling changes feature magnitude, not label counts or class proportions.
    *   *Why D is incorrect:* StandardScaler makes features smaller and more uniform — it reduces, not increases, the risk of gradient explosion.

---

**Question 5**
After calling `history = model.fit(X_train, y_train, epochs=20, validation_data=(X_val, y_val))`, which code correctly plots training and validation loss curves?
*   A) `plt.plot(history.history['loss']); plt.plot(history.history['val_loss'])`
*   B) `plt.bar(history['accuracy'], history['val_accuracy'])`
*   C) `sns.heatmap(history.history)`
*   D) `tf.keras.utils.plot_model(model, to_file='model.png')`
*   **Correct Answer:** A) The `history.history` dict contains per-epoch metric lists; plotting `'loss'` and `'val_loss'` shows the training curve and whether overfitting is occurring.
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the standard pattern for diagnosing model training — a widening gap between training and validation loss signals overfitting.
    *   *Why B is incorrect:* `history` is an object; you must access `history.history['accuracy']`, and `plt.bar` produces a bar chart, not a learning curve.
    *   *Why C is incorrect:* `sns.heatmap` requires a 2D matrix; `history.history` is a dict of lists, not a matrix suitable for heatmap visualization.
    *   *Why D is incorrect:* `plot_model` visualizes the model architecture diagram, not the training loss history.

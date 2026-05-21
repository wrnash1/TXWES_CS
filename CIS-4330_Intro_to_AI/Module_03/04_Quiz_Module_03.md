# Quiz: Module 03 - Unsupervised Learning – Clustering and Dimensionality Reduction
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which Pandas DataFrame method displays count, mean, standard deviation, and quartile ranges?
*   A) head()
*   B) info()
*   C) describe()
*   D) summary()
*   **Correct Answer:** C) The `.describe()` method generates descriptive statistics for numerical columns in a DataFrame.
*   **Distractor Analysis:**
    *   *Why correct:* The `.describe()` method generates descriptive statistics for numerical columns in a DataFrame.
    *   head() shows rows. info() shows data types. summary() is not a Pandas method.

---

**Question 2**
In the context of machine learning, which of the following is the most accurate definition of **loading CSV files**?
*   A) Reading a comma-separated values file from disk into a structured in-memory table (e.g., a Pandas DataFrame) so the data can be inspected, cleaned, and passed to a machine learning model.
*   B) A method of compressing tabular data into a binary format to reduce storage footprint before model training.
*   C) A data serialization technique that converts Python objects into JSON strings for transmission over REST APIs.
*   D) A database indexing strategy that speeds up queries by storing frequently accessed rows in a separate lookup table.
*   **Correct Answer:** A) Reading a comma-separated values file from disk into a structured in-memory table (e.g., a Pandas DataFrame) so the data can be inspected, cleaned, and passed to a machine learning model.
*   **Distractor Analysis:**
    *   *Why A is correct:* `pd.read_csv()` parses the file's rows and columns into a DataFrame, which is the standard first step in any Python-based ML pipeline.
    *   *Why B is incorrect:* CSV files are plain text, not binary compressed — this describes a different concept entirely.
    *   *Why C is incorrect:* JSON serialization converts Python objects to JSON format; it has no relation to reading CSV files.
    *   *Why D is incorrect:* Database indexing is a relational database concept unrelated to loading flat files in Python.

---

**Question 3**
A data scientist needs to **import the Pandas library and load a tabular dataset from a CSV file**. Which command is most appropriate?
*   A) import pandas as pd; df = pd.read_csv('data.csv')
*   B) predictions = model.predict(X_test)
*   C) accuracy = accuracy_score(y_test, predictions)
*   D) model.fit(X_train, y_train)
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    *   *Why A is correct:* This imports Pandas and calls `read_csv()` to load the file into a DataFrame, which is the correct first step.
    *   *Why B is incorrect:* `model.predict()` runs inference on a trained model; it does not load data.
    *   *Why C is incorrect:* `accuracy_score()` evaluates prediction quality; it requires predictions and labels already in memory.
    *   *Why D is incorrect:* `model.fit()` trains a model on features already loaded into memory; the data must be loaded first.

---

**Question 4**
A data scientist discovers that preprocessing scalers were fitted on the complete dataset before the train/test split, causing unrealistically optimistic validation scores. What is the correct term for this problem and the appropriate fix?
*   A) Data leakage — fit preprocessing steps only on training data, then apply the fitted transformer to test data separately.
*   B) Overfitting — reduce model complexity and apply L1/L2 regularization to penalize large weights.
*   C) Missing value errors — use mean/median imputation or drop rows containing null values before modeling.
*   D) Class imbalance — use oversampling (SMOTE) or adjust class weights in the model configuration.
*   **Correct Answer:** A) Data leakage — fit preprocessing steps only on training data, then apply the fitted transformer to test data separately.
*   **Distractor Analysis:**
    *   *Why A is correct:* Fitting scalers on the full dataset causes statistical information from the test set to "leak" into training, inflating validation metrics. The fix is to call `.fit_transform()` on training data only, and `.transform()` on test data.
    *   *Why B is incorrect:* Overfitting causes low validation accuracy (not high) because the model memorizes training data but fails to generalize.
    *   *Why C is incorrect:* Missing value errors cause runtime failures or biased imputations, not artificially high validation scores.
    *   *Why D is incorrect:* Class imbalance affects recall/precision on minority classes; it does not inflate overall accuracy through data leakage.

---

**Question 5**
Attackers are sending thousands of carefully crafted queries to a publicly deployed model API and using the outputs to reconstruct individual training records. Which security control best mitigates this **model inversion** attack?
*   A) Apply differential privacy to the training data and implement rate limiting on the public API.
*   B) Train the model on adversarial examples and validate all inputs before passing them to the model.
*   C) Enable full disk encryption on all client endpoints accessing the API.
*   D) Use role-based access control (RBAC) to restrict which Azure users can view model artifacts.
*   **Correct Answer:** A) Apply differential privacy to the training data and implement rate limiting on the public API.
*   **Distractor Analysis:**
    *   *Why A is correct:* Differential privacy mathematically prevents individual training records from being reconstructed; rate limiting reduces the volume of outputs an attacker can harvest.
    *   *Why B is incorrect:* Adversarial training defends against adversarial input perturbations, not against output-analysis attacks like model inversion.
    *   *Why C is incorrect:* Disk encryption protects stored data; it has no effect on inference requests made through a live API.
    *   *Why D is incorrect:* RBAC controls internal Azure user permissions; it does not prevent an external attacker from querying a public-facing endpoint.

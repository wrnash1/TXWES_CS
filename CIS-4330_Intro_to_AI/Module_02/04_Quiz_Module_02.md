# Quiz: Module 02 - Supervised vs Unsupervised Learning
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which type of machine learning uses labeled data to predict continuous numerical values?
*   A) Classification
*   B) Clustering
*   C) Regression
*   D) Dimensionality Reduction
*   **Correct Answer:** C) Regression is a supervised learning task designed to predict continuous values (e.g., home prices).
*   **Distractor Analysis:**
    *   *Why correct:* Regression is a supervised learning task designed to predict continuous values (e.g., home prices).
    *   Classification predicts discrete labels. Clustering deals with unlabeled groupings.

---

**Question 2**
In the context of AI and machine learning, which of the following is the most accurate definition of **clustering**?
*   A) An unsupervised learning technique that groups data points by similarity without using predefined labels, allowing the algorithm to discover natural patterns in the data.
*   B) A supervised method that assigns discrete category labels to input samples using a labeled training dataset.
*   C) A technique that reduces the number of input features by combining correlated variables into fewer dimensions.
*   D) A process that forecasts future values in a time series by fitting a regression model to historical data points.
*   **Correct Answer:** A) An unsupervised learning technique that groups data points by similarity without using predefined labels, allowing the algorithm to discover natural patterns in the data.
*   **Distractor Analysis:**
    *   *Why A is correct:* Clustering (e.g., K-Means) is an unsupervised method — no labels are needed — that partitions data into groups based on feature similarity.
    *   *Why B is incorrect:* This describes classification, a supervised task that requires labeled training data.
    *   *Why C is incorrect:* This describes dimensionality reduction (e.g., PCA), which compresses features rather than grouping records.
    *   *Why D is incorrect:* This describes time-series regression/forecasting, not clustering.

---

**Question 3**
A data scientist needs to **train a machine learning model on labeled training features and targets**. Which of the following commands is the most appropriate?
*   A) model.fit(X_train, y_train)
*   B) predictions = model.predict(X_test)
*   C) accuracy = accuracy_score(y_test, predictions)
*   D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    *   *Why A is correct:* `model.fit(X_train, y_train)` passes the feature matrix and target labels to the model's training algorithm.
    *   *Why B is incorrect:* `model.predict()` generates predictions from an already-trained model — it does not perform training.
    *   *Why C is incorrect:* `accuracy_score()` evaluates prediction quality after training and prediction are already complete.
    *   *Why D is incorrect:* This loads data from a CSV file — it is data preparation, not model training.

---

**Question 4**
A model's validation accuracy is significantly higher than expected because preprocessing scalers were fitted on the entire dataset before splitting into train and test sets. Which term describes this problem, and what is the correct fix?
*   A) Data leakage — fit preprocessing steps only on the training set, then apply (transform) to the test set.
*   B) Overfitting — apply L1/L2 regularization and gather more training data.
*   C) Missing value errors — use imputation techniques such as mean or median filling.
*   D) Underfitting — increase model complexity or add more features.
*   **Correct Answer:** A) Data leakage — fit preprocessing steps only on the training set, then apply (transform) to the test set.
*   **Distractor Analysis:**
    *   *Why A is correct:* Fitting the scaler on the full dataset leaks information from the test set into training, inflating performance metrics. The fix is to call `.fit_transform()` on training data only and `.transform()` on test data.
    *   *Why B is incorrect:* Overfitting results in high training accuracy but low validation accuracy, not artificially high validation accuracy.
    *   *Why C is incorrect:* Missing value errors cause model failures or biased imputations, not inflated validation scores.
    *   *Why D is incorrect:* Underfitting produces low accuracy on both training and validation sets.

---

**Question 5**
An AI model exposed via a public API is being exploited: attackers are sending thousands of crafted queries and reconstructing sensitive records from the model's outputs. Which security control best mitigates this **model inversion** attack?
*   A) Apply differential privacy methods to the training data and limit public API query rates.
*   B) Train models with adversarial inputs and implement input validation/filtering.
*   C) Enable full disk encryption on all client endpoints.
*   D) Store model weights in an encrypted key vault and rotate API keys monthly.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API query rates.
*   **Distractor Analysis:**
    *   *Why A is correct:* Differential privacy injects calibrated noise so individual training records cannot be reconstructed; rate limiting reduces the attacker's ability to harvest outputs.
    *   *Why B is incorrect:* Adversarial training defends against adversarial example attacks (perturbed inputs), not model inversion via output analysis.
    *   *Why C is incorrect:* Disk encryption protects data at rest and is irrelevant to an API-based reconstruction attack.
    *   *Why D is incorrect:* Key rotation controls API authentication but does not prevent a legitimate-looking flood of inference queries from an attacker.

# Quiz: Module 04 - Neural Networks and Deep Learning
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What is the purpose of one-hot encoding in data preprocessing?
*   A) To compress files
*   B) To convert categorical text features into binary vectors
*   C) To clean out duplicates
*   D) To normalize numeric data
*   **Correct Answer:** B) One-hot encoding converts labels or categories into binary indicators (0 or 1) that machine learning models can compute.
*   **Distractor Analysis:**
    *   *Why correct:* One-hot encoding converts labels or categories into binary indicators (0 or 1) that machine learning models can compute.
    *   Normalization scales numbers. Compression and deduplication are general data administration tasks unrelated to encoding.

---

**Question 2**
In the context of machine learning, which of the following is the most accurate definition of **feature scaling**?
*   A) A preprocessing step that transforms numeric input features to a comparable range (e.g., 0–1 or zero mean/unit variance) so that gradient-based algorithms converge faster and no single feature dominates due to its magnitude.
*   B) A two-dimensional CSS layout system that allows developers to design grid-based user interfaces with rows and columns.
*   C) A technique that removes leaf nodes from a decision tree to reduce model complexity and prevent overfitting.
*   D) A database normalization rule that eliminates redundant data by ensuring each non-key attribute depends only on the primary key.
*   **Correct Answer:** A) A preprocessing step that transforms numeric input features to a comparable range so that gradient-based algorithms converge faster and no single feature dominates due to its magnitude.
*   **Distractor Analysis:**
    *   *Why A is correct:* Feature scaling (via Min-Max normalization or standardization) is essential for neural networks and distance-based algorithms where unscaled features with large ranges distort learning.
    *   *Why B is incorrect:* This describes CSS Grid layout — a web design concept entirely unrelated to machine learning preprocessing.
    *   *Why C is incorrect:* This describes decision tree pruning, not feature scaling.
    *   *Why D is incorrect:* This describes database normalization (3NF), a relational database concept unrelated to ML feature engineering.

---

**Question 3**
A data scientist needs to **calculate the accuracy of model predictions against actual test labels**. Which command is most appropriate?
*   A) accuracy = accuracy_score(y_test, predictions)
*   B) model.fit(X_train, y_train)
*   C) predictions = model.predict(X_test)
*   D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) accuracy = accuracy_score(y_test, predictions)
*   **Distractor Analysis:**
    *   *Why A is correct:* `accuracy_score(y_test, predictions)` compares the model's predicted labels against the true test labels and returns the fraction that match.
    *   *Why B is incorrect:* `model.fit()` trains the model; it does not evaluate prediction accuracy.
    *   *Why C is incorrect:* `model.predict()` generates predictions; it does not compute an accuracy metric.
    *   *Why D is incorrect:* This loads data from a CSV; it is data loading, not evaluation.

---

**Question 4**
A model returns NaN loss values during training. Investigation reveals the dataset contains many null entries in numeric columns. Which action most directly resolves this?
*   A) Use imputation techniques (mean, median, or mode) or drop rows/columns containing missing values before training.
*   B) Apply L1/L2 regularization to the model weights to reduce overfitting.
*   C) Ensure preprocessing scalers are fitted only on training data, then applied to test data.
*   D) Reboot the training environment and restart the pipeline from scratch.
*   **Correct Answer:** A) Use imputation techniques (mean, median, or mode) or drop rows/columns containing missing values before training.
*   **Distractor Analysis:**
    *   *Why A is correct:* NaN values propagate through mathematical operations, causing NaN loss. Imputing or dropping missing values before training prevents this.
    *   *Why B is incorrect:* Regularization addresses overfitting, not NaN values caused by missing data.
    *   *Why C is incorrect:* Scaler fitting strategy prevents data leakage; it does not resolve NaN input values.
    *   *Why D is incorrect:* Restarting a pipeline does not fix missing data in the underlying dataset.

---

**Question 5**
A public-facing model API is being exploited by attackers who send imperceptibly modified input images that cause the model to misclassify them with high confidence. Which security control best mitigates this **adversarial example** attack?
*   A) Train the model with adversarial examples included in the training set and implement input validation/filtering on all incoming data.
*   B) Apply differential privacy to the training data and rate-limit public API queries.
*   C) Enable full disk encryption on all client endpoints.
*   D) Rotate the model's API key every 30 days and enforce TLS 1.3 on all connections.
*   **Correct Answer:** A) Train the model with adversarial examples included in the training set and implement input validation/filtering on all incoming data.
*   **Distractor Analysis:**
    *   *Why A is correct:* Adversarial training exposes the model to perturbed inputs during training, improving its robustness. Input validation filters suspicious inputs before they reach the model.
    *   *Why B is incorrect:* Differential privacy defends against model inversion attacks (reconstructing training data), not adversarial example attacks on inputs.
    *   *Why C is incorrect:* Disk encryption protects stored data and is irrelevant to manipulated inference inputs sent via API.
    *   *Why D is incorrect:* Key rotation and TLS protect the transport layer; they do not make the model robust against crafted adversarial inputs.

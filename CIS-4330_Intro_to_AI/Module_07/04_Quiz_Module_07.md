# Quiz: Module 07 - Azure Cognitive Services: Vision, Speech, and Language
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which metric measures the fraction of actual positive instances that were correctly identified by a classification model?
*   A) Precision
*   B) Recall (Sensitivity)
*   C) Accuracy
*   D) Specificity
*   **Correct Answer:** B) Recall (True Positives / (True Positives + False Negatives)) measures the model's ability to find all actual positive cases.
*   **Distractor Analysis:**
    *   *Why correct:* Recall answers "of all the real positives, how many did the model catch?" — it penalizes missed positives (false negatives).
    *   Precision measures how many predicted positives are actually positive (penalizes false alarms). Accuracy is the overall fraction correct. Specificity measures true negative rate.

---

**Question 2**
In the context of machine learning evaluation, which of the following is the most accurate definition of **Mean Squared Error (MSE)**?
*   A) The average of the squared differences between each predicted value and the corresponding actual value, used as the standard loss metric for regression models.
*   B) The harmonic mean of precision and recall, calculated as 2 × (Precision × Recall) / (Precision + Recall), used to balance false positives and false negatives.
*   C) A table that displays the counts of true positives, true negatives, false positives, and false negatives for each class in a classification problem.
*   D) The fraction of all predictions that are correct, calculated as (TP + TN) / (TP + TN + FP + FN), used as a high-level performance summary.
*   **Correct Answer:** A) The average of the squared differences between each predicted value and the corresponding actual value, used as the standard loss metric for regression models.
*   **Distractor Analysis:**
    *   *Why A is correct:* MSE quantifies regression error by squaring residuals (which penalizes large errors more heavily) and averaging them, giving a single number that measures how far predictions are from actual values.
    *   *Why B is incorrect:* This describes the F1-Score — a classification metric, not a regression error metric.
    *   *Why C is incorrect:* This describes the Confusion Matrix — a classification evaluation tool, not a numeric error measure for regression.
    *   *Why D is incorrect:* This describes Accuracy — a classification metric measuring the overall fraction of correct predictions.

---

**Question 3**
A developer needs to **use a trained model to generate predictions on unseen test data**. Which command is most appropriate?
*   A) predictions = model.predict(X_test)
*   B) accuracy = accuracy_score(y_test, predictions)
*   C) import pandas as pd; df = pd.read_csv('data.csv')
*   D) model.fit(X_train, y_train)
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    *   *Why A is correct:* `model.predict(X_test)` passes unseen test features through the trained model and returns predicted labels or values.
    *   *Why B is incorrect:* `accuracy_score()` computes a performance metric from existing predictions; it does not produce predictions itself.
    *   *Why C is incorrect:* This loads data from a CSV file — data loading, not prediction.
    *   *Why D is incorrect:* `model.fit()` trains the model on labeled training data; it does not generate predictions on new data.

---

**Question 4**
A classification model achieves 99% accuracy on a medical diagnosis dataset, but the confusion matrix reveals it is predicting "healthy" for almost every patient. The dataset has 990 healthy and 10 sick patients. What problem does this illustrate, and what is the best fix?
*   A) Class imbalance — use oversampling (SMOTE), undersampling, or class weights to force the model to learn the minority class.
*   B) Data leakage — fit the preprocessing scaler only on training data using `.fit_transform()`, then apply `.transform()` to the test set separately.
*   C) Missing value errors — impute null entries with mean or median before retraining the model.
*   D) Underfitting — increase model complexity by adding more layers or polynomial features to improve performance.
*   **Correct Answer:** A) Class imbalance — use oversampling (SMOTE), undersampling, or class weights to force the model to learn the minority class.
*   **Distractor Analysis:**
    *   *Why A is correct:* When one class dominates the dataset, a model can achieve high accuracy by predicting the majority class almost exclusively. Rebalancing via SMOTE, undersampling, or `class_weight='balanced'` teaches the model to treat rare classes as important.
    *   *Why B is incorrect:* Data leakage causes inflated validation scores from improper preprocessing, not the class-dominance pattern described here.
    *   *Why C is incorrect:* Missing value imputation addresses NaN errors; the dataset here has no missing values — it has an imbalanced distribution.
    *   *Why D is incorrect:* The model is not underfitting — it has learned a trivial rule (always predict healthy) that achieves high accuracy due to skewed class distribution.

---

**Question 5**
Attackers are querying a public model API with many carefully crafted inputs and analyzing the output probabilities to reconstruct the private training data (including patient records). Which defense best mitigates this **model inversion** attack?
*   A) Apply differential privacy to the training data and rate-limit the public inference API to reduce the attacker's ability to extract information.
*   B) Train the model with adversarial examples included in the training set and implement input validation before inference.
*   C) Enable full disk encryption on all client endpoints submitting queries to the API.
*   D) Require multi-factor authentication (MFA) for all developer accounts with access to the model training pipeline.
*   **Correct Answer:** A) Apply differential privacy to the training data and rate-limit the public inference API to reduce the attacker's ability to extract information.
*   **Distractor Analysis:**
    *   *Why A is correct:* Differential privacy adds calibrated noise to training data, making it statistically difficult to reconstruct individual records from model outputs. Rate-limiting reduces the number of queries an attacker can submit, slowing or blocking the reconstruction attempt.
    *   *Why B is incorrect:* Adversarial training defends against adversarial example attacks on inference inputs — it does not protect training data from model inversion via API output analysis.
    *   *Why C is incorrect:* Disk encryption protects data at rest on a device; it has no effect on information leaked through a live inference API's probability outputs.
    *   *Why D is incorrect:* MFA secures developer account access to the training pipeline but does not prevent a public API from leaking training data through its outputs.

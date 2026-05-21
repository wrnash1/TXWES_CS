# Quiz: Module 07 - Evaluating Machine Learning Models
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
    *   *Why correct:* Recall (True Positives / (True Positives + False Negatives)) measures the model's ability to find all actual positive cases.
    *   Precision measures how many predicted positives are actually positive.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Mean Squared Error (MSE).**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
D) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
C) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
B) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Mean Squared Error (MSE).**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Mean Squared Error (MSE).**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Mean Squared Error (MSE).**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Mean Squared Error (MSE).**.


---

**Question 3**
A systems administrator or developer needs to **use the trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
B) accuracy = accuracy_score(y_test, predictions)
D) model.fit(X_train, y_train)
A) predictions = model.predict(X_test)
C) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `predictions = model.predict(X_test)` command is directly designed to use the trained model to generate predictions on unseen test data.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Evaluating Machine Learning Models** in a production environment, you encounter a system alert indicating a **Low Model Generalization** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
D) Reboot the physical machine and wait for services to reload.
A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Correct Answer:** A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why B is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why D is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why A is correct:* Because The model has overfit the training data and performs poorly on unseen validation or testing datasets. The appropriate fix is to Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture..


---

**Question 5**
When designing a system for **Evaluating Machine Learning Models**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
A) Apply differential privacy methods to the training data and limit public API rate queries.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


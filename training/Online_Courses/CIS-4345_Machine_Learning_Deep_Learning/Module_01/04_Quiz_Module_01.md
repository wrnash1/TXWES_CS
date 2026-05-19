# Quiz: Module 01 - Introduction to ML Pipelines
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What is the primary reason for splitting data into Training and Testing datasets?
*   A) To save disk storage space
*   B) To evaluate how the model performs on unseen data and detect overfitting
*   C) To double compile datasets
*   D) To format files for database engines
*   **Correct Answer:** B) Testing datasets provide unbiased metrics indicating how well models generalize to new inputs.
*   **Distractor Analysis:**
    *   *Why correct:* Testing datasets provide unbiased metrics indicating how well models generalize to new inputs.
    *   It does not optimize space or compile script files.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Machine learning lifecycle**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
D) A computational model inspired by the biological brain structure, consisting of interconnected layers of nodes (neurons).
B) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
C) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Machine learning lifecycle**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Machine learning lifecycle**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Machine learning lifecycle**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Machine learning lifecycle**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
C) predictions = model.predict(X_test)
A) model.fit(X_train, y_train)
B) import pandas as pd; df = pd.read_csv('data.csv')
D) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Introduction to ML Pipelines** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **Introduction to ML Pipelines**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
C) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


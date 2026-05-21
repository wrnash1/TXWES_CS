# Quiz: Module 05 - Linear and Logistic Regression Models
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which model is appropriate for predicting binary (yes/no) output class labels?
*   A) Linear Regression
*   B) Logistic Regression
*   C) K-Means Clustering
*   D) Principal Component Analysis
*   **Correct Answer:** B) Logistic regression maps output predictions to a probability between 0 and 1, making it ideal for binary classification.
*   **Distractor Analysis:**
    *   *Why correct:* Logistic regression maps output predictions to a probability between 0 and 1, making it ideal for binary classification.
    *   Linear regression is for continuous variables. K-Means is for grouping.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **logistic sigmoid curve for classification.**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
C) A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.
D) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
B) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **logistic sigmoid curve for classification.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **logistic sigmoid curve for classification.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **logistic sigmoid curve for classification.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **logistic sigmoid curve for classification.**.


---

**Question 3**
A systems administrator or developer needs to **use the trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
A) predictions = model.predict(X_test)
D) import pandas as pd; df = pd.read_csv('data.csv')
B) model.fit(X_train, y_train)
C) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    * *Why A is correct:* The `predictions = model.predict(X_test)` command is directly designed to use the trained model to generate predictions on unseen test data.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Linear and Logistic Regression Models** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
D) Reboot the physical machine and wait for services to reload.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..


---

**Question 5**
When designing a system for **Linear and Logistic Regression Models**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
B) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.


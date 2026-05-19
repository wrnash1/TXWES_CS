# Quiz: Module 02 - Linear Regression
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What is the objective of the Gradient Descent algorithm in model training?
*   A) To select random features
*   B) To iteratively adjust model weights to minimize the cost function value
*   C) To prune decision tree leaves
*   D) To backup SQL tables
*   **Correct Answer:** B) Gradient Descent is an optimization method that computes cost gradients to update weights toward minimum cost levels.
*   **Distractor Analysis:**
    *   *Why correct:* Gradient Descent is an optimization method that computes cost gradients to update weights toward minimum cost levels.
    *   Pruning trees and database administration are independent tasks.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **weights and biases.**?
C) A machine learning error where a model learns the training data too well, capturing noise and failing to generalize to new data.
B) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
D) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **weights and biases.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **weights and biases.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **weights and biases.**.
    * *Why A is correct:* This describes the exact role and function of **weights and biases.**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
D) accuracy = accuracy_score(y_test, predictions)
A) model.fit(X_train, y_train)
B) import pandas as pd; df = pd.read_csv('data.csv')
C) predictions = model.predict(X_test)
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Linear Regression** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
D) Reboot the physical machine and wait for services to reload.
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.


---

**Question 5**
When designing a system for **Linear Regression**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
D) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


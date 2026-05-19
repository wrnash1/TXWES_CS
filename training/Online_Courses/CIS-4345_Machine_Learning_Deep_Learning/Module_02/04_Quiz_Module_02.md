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
D) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
C) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
B) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **weights and biases.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **weights and biases.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **weights and biases.**.
    * *Why A is correct:* This describes the exact role and function of **weights and biases.**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
D) accuracy = accuracy_score(y_test, predictions)
A) model.fit(X_train, y_train)
C) import pandas as pd; df = pd.read_csv('data.csv')
B) predictions = model.predict(X_test)
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Linear Regression** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..


---

**Question 5**
When designing a system for **Linear Regression**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
B) Apply differential privacy methods to the training data and limit public API rate queries.
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.


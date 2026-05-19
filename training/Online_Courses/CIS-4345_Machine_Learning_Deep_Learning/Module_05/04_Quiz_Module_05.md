# Quiz: Module 05 - Support Vector Machines
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What are support vectors in the context of Support Vector Machines?
*   A) Empty dimensions
*   B) The data points closest to the separating hyperplane that define the margin boundaries
*   C) The outputs of activation layers
*   D) Target variable index arrays
*   **Correct Answer:** B) Support vectors are the data points closest to the separating hyperplane that define the margin boundaries.
*   **Distractor Analysis:**
    *   *Why correct:* Support vectors are the data points closest to the separating hyperplane that define the margin boundaries.
    *   Support vectors are real points, not dimensions or activations.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **kernel trick**?
C) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
D) A machine learning error where a model learns the training data too well, capturing noise and failing to generalize to new data.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **kernel trick**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **kernel trick**.
    * *Why A is correct:* This describes the exact role and function of **kernel trick**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **kernel trick**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
A) model.fit(X_train, y_train)
D) import pandas as pd; df = pd.read_csv('data.csv')
B) accuracy = accuracy_score(y_test, predictions)
C) predictions = model.predict(X_test)
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Support Vector Machines** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
D) Reboot the physical machine and wait for services to reload.
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..


---

**Question 5**
When designing a system for **Support Vector Machines**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
D) Enable full disk encryption on all client endpoints.
B) Apply differential privacy methods to the training data and limit public API rate queries.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.


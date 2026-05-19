# Quiz: Module 09 - Introduction to Neural Networks
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What is the primary function of a hidden layer in an artificial neural network?
*   A) To store inputs exactly
*   B) To learn non-linear feature representations from input data patterns
*   C) To write files to disk
*   D) To communicate directly with user interfaces
*   **Correct Answer:** B) Hidden layers apply weights and activation functions to extract high-level feature mappings from preceding inputs.
*   **Distractor Analysis:**
    *   *Why correct:* Hidden layers apply weights and activation functions to extract high-level feature mappings from preceding inputs.
    *   Hidden layers are intermediate computation steps, isolated from raw files and client frontends.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **output activations.**?
D) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
C) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **output activations.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **output activations.**.
    * *Why A is correct:* This describes the exact role and function of **output activations.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **output activations.**.


---

**Question 3**
A systems administrator or developer needs to **use the trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
B) accuracy = accuracy_score(y_test, predictions)
A) predictions = model.predict(X_test)
D) model.fit(X_train, y_train)
C) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `predictions = model.predict(X_test)` command is directly designed to use the trained model to generate predictions on unseen test data.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Introduction to Neural Networks** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.


---

**Question 5**
When designing a system for **Introduction to Neural Networks**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


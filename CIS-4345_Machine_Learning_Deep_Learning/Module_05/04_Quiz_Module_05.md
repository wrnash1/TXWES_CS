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
B) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
C) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
D) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **kernel trick**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **kernel trick**.
    * *Why A is correct:* This describes the exact role and function of **kernel trick**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **kernel trick**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
D) accuracy = accuracy_score(y_test, predictions)
B) predictions = model.predict(X_test)
A) model.fit(X_train, y_train)
C) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Support Vector Machines** in a production environment, you encounter a system alert indicating a **Low Model Generalization** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
D) Reboot the physical machine and wait for services to reload.
A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Correct Answer:** A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why C is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why D is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why A is correct:* Because The model has overfit the training data and performs poorly on unseen validation or testing datasets. The appropriate fix is to Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture..


---

**Question 5**
When designing a system for **Support Vector Machines**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Apply differential privacy methods to the training data and limit public API rate queries.
D) Enable full disk encryption on all client endpoints.
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..


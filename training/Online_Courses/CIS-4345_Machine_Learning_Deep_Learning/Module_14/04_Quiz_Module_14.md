# Quiz: Module 14 - Model Optimization & Tuning
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
How does the Dropout technique prevent overfitting in deep neural networks?
*   A) It drops input rows
*   B) It randomly deactivates a fraction of neurons during each training step, forcing redundancy
*   C) It deletes model files
*   D) It turns off the CPU
*   **Correct Answer:** B) Dropout stops co-adaptation by ensuring no single neuron can dominate feature representation.
*   **Distractor Analysis:**
    *   *Why correct:* Dropout stops co-adaptation by ensuring no single neuron can dominate feature representation.
    *   It is applied during training steps, not row deletion.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Learning rate adjustments**?
D) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
B) CSS rules (like width, height, max-width, box-sizing) that dictate how the dimensions of elements are calculated and rendered.
C) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Learning rate adjustments**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Learning rate adjustments**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Learning rate adjustments**.
    * *Why A is correct:* This describes the exact role and function of **Learning rate adjustments**.


---

**Question 3**
A systems administrator or developer needs to **use the trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
C) accuracy = accuracy_score(y_test, predictions)
A) predictions = model.predict(X_test)
B) model.fit(X_train, y_train)
D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `predictions = model.predict(X_test)` command is directly designed to use the trained model to generate predictions on unseen test data.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Model Optimization & Tuning** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
D) Reboot the physical machine and wait for services to reload.
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **Model Optimization & Tuning**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
B) Apply differential privacy methods to the training data and limit public API rate queries.
D) Enable full disk encryption on all client endpoints.
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.


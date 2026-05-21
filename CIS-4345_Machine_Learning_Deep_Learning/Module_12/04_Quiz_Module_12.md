# Quiz: Module 12 - Recurrent Neural Networks (RNN/LSTM)
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What problem do Long Short-Term Memory (LSTM) cells solve compared to basic Recurrent Neural Networks (RNNs)?
*   A) Memory leak errors
*   B) The vanishing gradient problem, allowing the model to learn long-term dependencies
*   C) The lack of GPU drivers
*   D) High compilation speeds
*   **Correct Answer:** B) LSTMs use internal gating mechanisms (forget gate, input gate, output gate) to maintain state values across many sequence steps.
*   **Distractor Analysis:**
    *   *Why correct:* LSTMs use internal gating mechanisms (forget gate, input gate, output gate) to maintain state values across many sequence steps.
    *   LSTMs do not change computer hardware drivers or execution speeds.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **recurrent loops**?
B) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
D) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
C) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **recurrent loops**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **recurrent loops**.
    * *Why A is correct:* This describes the exact role and function of **recurrent loops**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **recurrent loops**.


---

**Question 3**
A systems administrator or developer needs to **calculate the accuracy metric of the model predictions against actual labels**. Which of the following commands is the most appropriate to execute?
C) predictions = model.predict(X_test)
A) accuracy = accuracy_score(y_test, predictions)
D) import pandas as pd; df = pd.read_csv('data.csv')
B) model.fit(X_train, y_train)
*   **Correct Answer:** A) accuracy = accuracy_score(y_test, predictions)
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `accuracy = accuracy_score(y_test, predictions)` command is directly designed to calculate the accuracy metric of the model predictions against actual labels.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Recurrent Neural Networks (RNN/LSTM)** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.


---

**Question 5**
When designing a system for **Recurrent Neural Networks (RNN/LSTM)**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
B) Apply differential privacy methods to the training data and limit public API rate queries.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.


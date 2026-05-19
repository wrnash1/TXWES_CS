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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Sequence databases**?
D) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
C) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Sequence databases**.
    * *Why A is correct:* This describes the exact role and function of **Sequence databases**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Sequence databases**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Sequence databases**.


---

**Question 3**
A systems administrator or developer needs to **import the pandas library to load and analyze a tabular dataset**. Which of the following commands is the most appropriate to execute?
C) predictions = model.predict(X_test)
D) model.fit(X_train, y_train)
A) import pandas as pd; df = pd.read_csv('data.csv')
B) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `import pandas as pd; df = pd.read_csv('data.csv')` command is directly designed to import the pandas library to load and analyze a tabular dataset.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Recurrent Neural Networks (RNN/LSTM)** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.


---

**Question 5**
When designing a system for **Recurrent Neural Networks (RNN/LSTM)**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..


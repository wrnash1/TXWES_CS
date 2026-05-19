# Quiz: Module 06 - Decision Trees & Random Forests
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
Which process describes the 'Bagging' ensemble technique used in Random Forests?
*   A) Sequential tree boosting
*   B) Training multiple independent decision trees on bootstrap datasets and averaging their votes
*   C) Regularizing feature weight matrices
*   D) Compressing tree layers into a single node
*   **Correct Answer:** B) Bootstrap Aggregation (Bagging) reduces variance by training multiple trees on random sub-samples and combining predictions.
*   **Distractor Analysis:**
    *   *Why correct:* Bootstrap Aggregation (Bagging) reduces variance by training multiple trees on random sub-samples and combining predictions.
    *   Sequential tree training is characteristic of Boosting.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Entropy index**?
C) The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
D) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Entropy index**.
    * *Why A is correct:* This describes the exact role and function of **Entropy index**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Entropy index**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Entropy index**.


---

**Question 3**
A systems administrator or developer needs to **import the pandas library to load and analyze a tabular dataset**. Which of the following commands is the most appropriate to execute?
A) import pandas as pd; df = pd.read_csv('data.csv')
C) accuracy = accuracy_score(y_test, predictions)
D) model.fit(X_train, y_train)
B) predictions = model.predict(X_test)
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    * *Why A is correct:* The `import pandas as pd; df = pd.read_csv('data.csv')` command is directly designed to import the pandas library to load and analyze a tabular dataset.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Decision Trees & Random Forests** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..


---

**Question 5**
When designing a system for **Decision Trees & Random Forests**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Apply differential privacy methods to the training data and limit public API rate queries.
C) Enable full disk encryption on all client endpoints.
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..


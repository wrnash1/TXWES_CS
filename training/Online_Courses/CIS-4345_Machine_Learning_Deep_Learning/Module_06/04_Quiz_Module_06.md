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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **ensemble methods**?
D) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
C) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **ensemble methods**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **ensemble methods**.
    * *Why A is correct:* This describes the exact role and function of **ensemble methods**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **ensemble methods**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
C) accuracy = accuracy_score(y_test, predictions)
A) model.fit(X_train, y_train)
B) predictions = model.predict(X_test)
D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Decision Trees & Random Forests** in a production environment, you encounter a system alert indicating a **Low Model Generalization** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
D) Reboot the physical machine and wait for services to reload.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Correct Answer:** A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why D is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why C is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why A is correct:* Because The model has overfit the training data and performs poorly on unseen validation or testing datasets. The appropriate fix is to Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture..


---

**Question 5**
When designing a system for **Decision Trees & Random Forests**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
A) Apply differential privacy methods to the training data and limit public API rate queries.
D) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


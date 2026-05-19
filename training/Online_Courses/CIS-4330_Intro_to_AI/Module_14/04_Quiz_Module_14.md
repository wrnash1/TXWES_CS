# Quiz: Module 14 - Automated Machine Learning (AutoML)
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What does Automated Machine Learning (AutoML) automate?
*   A) Data collection from websites
*   B) Feature selection, algorithm sweep, and hyperparameter tuning
*   C) Writing Python code for front-end web layouts
*   D) Database backups
*   **Correct Answer:** B) AutoML automates the iterative process of model training, sweeping across algorithms and tuning hyperparameters to find the optimal model.
*   **Distractor Analysis:**
    *   *Why correct:* AutoML automates the iterative process of model training, sweeping across algorithms and tuning hyperparameters to find the optimal model.
    *   AutoML does not collect data or write web app UI code.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **AutoML pipelines**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
C) A mathematical method of evaluating how well a machine learning algorithm models the training dataset.
B) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
D) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **AutoML pipelines**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **AutoML pipelines**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **AutoML pipelines**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **AutoML pipelines**.


---

**Question 3**
A systems administrator or developer needs to **use the trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
D) import pandas as pd; df = pd.read_csv('data.csv')
A) predictions = model.predict(X_test)
B) accuracy = accuracy_score(y_test, predictions)
C) model.fit(X_train, y_train)
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `predictions = model.predict(X_test)` command is directly designed to use the trained model to generate predictions on unseen test data.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Automated Machine Learning (AutoML)** in a production environment, you encounter a system alert indicating a **Low Model Generalization** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
D) Reboot the physical machine and wait for services to reload.
C) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Correct Answer:** A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why D is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why C is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why A is correct:* Because The model has overfit the training data and performs poorly on unseen validation or testing datasets. The appropriate fix is to Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture..


---

**Question 5**
When designing a system for **Automated Machine Learning (AutoML)**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
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


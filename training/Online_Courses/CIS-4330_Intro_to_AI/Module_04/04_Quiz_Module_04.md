# Quiz: Module 04 - Data Preprocessing
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What is the purpose of one-hot encoding in data preprocessing?
*   A) To compress files
*   B) To convert categorical text features into binary vectors
*   C) To clean out duplicates
*   D) To normalize numeric data
*   **Correct Answer:** B) One-hot encoding converts labels or categories into binary indicators (0 or 1) that machine learning models can compute.
*   **Distractor Analysis:**
    *   *Why correct:* One-hot encoding converts labels or categories into binary indicators (0 or 1) that machine learning models can compute.
    *   Normalization scales numbers. Compression and deduplication are general data administration.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Handling missing data**?
D) A mathematical method of evaluating how well a machine learning algorithm models the training dataset.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
C) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
B) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Handling missing data**.
    * *Why A is correct:* This describes the exact role and function of **Handling missing data**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Handling missing data**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Handling missing data**.


---

**Question 3**
A systems administrator or developer needs to **use the trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
C) accuracy = accuracy_score(y_test, predictions)
A) predictions = model.predict(X_test)
D) import pandas as pd; df = pd.read_csv('data.csv')
B) model.fit(X_train, y_train)
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `predictions = model.predict(X_test)` command is directly designed to use the trained model to generate predictions on unseen test data.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Preprocessing** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
D) Reboot the physical machine and wait for services to reload.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **Data Preprocessing**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
A) Apply differential privacy methods to the training data and limit public API rate queries.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


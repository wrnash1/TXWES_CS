# Quiz: Module 03 - Python Data Exploration
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which Pandas DataFrame method displays count, mean, standard deviation, and quartile ranges?
*   A) head()
*   B) info()
*   C) describe()
*   D) summary()
*   **Correct Answer:** C) The `.describe()` method generates descriptive statistics for numerical columns in a DataFrame.
*   **Distractor Analysis:**
    *   *Why correct:* The `.describe()` method generates descriptive statistics for numerical columns in a DataFrame.
    *   head() shows rows. info() shows data types. summary() is not a Pandas method.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **loading CSV files**?
D) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
B) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
C) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **loading CSV files**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **loading CSV files**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **loading CSV files**.
    * *Why A is correct:* This describes the exact role and function of **loading CSV files**.


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
While working on **Python Data Exploration** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
D) Reboot the physical machine and wait for services to reload.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **Python Data Exploration**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..


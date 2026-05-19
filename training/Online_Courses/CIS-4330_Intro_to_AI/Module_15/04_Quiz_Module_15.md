# Quiz: Module 15 - AI System Deployment
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
How is a trained machine learning model typically exposed to client applications?
*   A) As a raw Python script
*   B) As a web-accessible REST API endpoint
*   C) Direct connection to SQL server
*   D) Inside an email attachment
*   **Correct Answer:** B) Models are usually deployed inside containerized web services that expose REST API endpoints for clients to submit data and receive predictions.
*   **Distractor Analysis:**
    *   *Why correct:* Models are usually deployed inside containerized web services that expose REST API endpoints for clients to submit data and receive predictions.
    *   Direct client access to script files or SQL servers is not recommended for scalable production deployments.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **containerization (Docker)**?
B) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
C) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
D) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **containerization (Docker)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **containerization (Docker)**.
    * *Why A is correct:* This describes the exact role and function of **containerization (Docker)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **containerization (Docker)**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
C) accuracy = accuracy_score(y_test, predictions)
A) model.fit(X_train, y_train)
D) import pandas as pd; df = pd.read_csv('data.csv')
B) predictions = model.predict(X_test)
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **AI System Deployment** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..


---

**Question 5**
When designing a system for **AI System Deployment**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
D) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..


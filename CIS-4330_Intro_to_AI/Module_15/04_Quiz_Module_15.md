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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **monitoring endpoints.**?
B) CSS rules (like width, height, max-width, box-sizing) that dictate how the dimensions of elements are calculated and rendered.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
D) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
C) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **monitoring endpoints.**.
    * *Why A is correct:* This describes the exact role and function of **monitoring endpoints.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **monitoring endpoints.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **monitoring endpoints.**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
C) import pandas as pd; df = pd.read_csv('data.csv')
D) predictions = model.predict(X_test)
B) accuracy = accuracy_score(y_test, predictions)
A) model.fit(X_train, y_train)
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.


---

**Question 4**
While working on **AI System Deployment** in a production environment, you encounter a system alert indicating a **Low Model Generalization** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When designing a system for **AI System Deployment**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
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


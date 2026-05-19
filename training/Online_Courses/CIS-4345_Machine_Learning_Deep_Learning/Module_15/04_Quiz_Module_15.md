# Quiz: Module 15 - Model Deployment & Serving
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What format is typically used to exchange model prediction input payloads over HTTP APIs?
*   A) XML
*   B) JSON
*   C) CSV
*   D) SQL Data
*   **Correct Answer:** B) REST APIs typically use JSON format to structure features and return class labels or scores.
*   **Distractor Analysis:**
    *   *Why correct:* REST APIs typically use JSON format to structure features and return class labels or scores.
    *   JSON is the standard format for modern HTTP REST requests.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Model serialization (Keras H5**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) HTML tags that convey the meaning and structure of the enclosed content to both the browser and search engines (e.g., <header>, <article>, <footer>) instead of generic containers.
C) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
D) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Model serialization (Keras H5**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Model serialization (Keras H5**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Model serialization (Keras H5**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Model serialization (Keras H5**.


---

**Question 3**
A systems administrator or developer needs to **calculate the accuracy metric of the model predictions against actual labels**. Which of the following commands is the most appropriate to execute?
D) predictions = model.predict(X_test)
A) accuracy = accuracy_score(y_test, predictions)
B) model.fit(X_train, y_train)
C) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) accuracy = accuracy_score(y_test, predictions)
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `accuracy = accuracy_score(y_test, predictions)` command is directly designed to calculate the accuracy metric of the model predictions against actual labels.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Model Deployment & Serving** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
D) Reboot the physical machine and wait for services to reload.
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..


---

**Question 5**
When designing a system for **Model Deployment & Serving**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
B) Apply differential privacy methods to the training data and limit public API rate queries.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.


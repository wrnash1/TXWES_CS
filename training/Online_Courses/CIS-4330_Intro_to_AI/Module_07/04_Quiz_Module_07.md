# Quiz: Module 07 - Evaluating Machine Learning Models
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which metric measures the fraction of actual positive instances that were correctly identified by a classification model?
*   A) Precision
*   B) Recall (Sensitivity)
*   C) Accuracy
*   D) Specificity
*   **Correct Answer:** B) Recall (True Positives / (True Positives + False Negatives)) measures the model's ability to find all actual positive cases.
*   **Distractor Analysis:**
    *   *Why correct:* Recall (True Positives / (True Positives + False Negatives)) measures the model's ability to find all actual positive cases.
    *   Precision measures how many predicted positives are actually positive.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **F1-Score**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
C) HTML tags that convey the meaning and structure of the enclosed content to both the browser and search engines (e.g., <header>, <article>, <footer>) instead of generic containers.
D) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **F1-Score**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **F1-Score**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **F1-Score**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **F1-Score**.


---

**Question 3**
A systems administrator or developer needs to **calculate the accuracy metric of the model predictions against actual labels**. Which of the following commands is the most appropriate to execute?
C) predictions = model.predict(X_test)
A) accuracy = accuracy_score(y_test, predictions)
B) import pandas as pd; df = pd.read_csv('data.csv')
D) model.fit(X_train, y_train)
*   **Correct Answer:** A) accuracy = accuracy_score(y_test, predictions)
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `accuracy = accuracy_score(y_test, predictions)` command is directly designed to calculate the accuracy metric of the model predictions against actual labels.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Evaluating Machine Learning Models** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
D) Reboot the physical machine and wait for services to reload.
C) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..


---

**Question 5**
When designing a system for **Evaluating Machine Learning Models**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..


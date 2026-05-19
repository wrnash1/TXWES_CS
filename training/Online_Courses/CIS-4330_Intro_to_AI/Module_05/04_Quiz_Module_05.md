# Quiz: Module 05 - Linear and Logistic Regression Models
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which model is appropriate for predicting binary (yes/no) output class labels?
*   A) Linear Regression
*   B) Logistic Regression
*   C) K-Means Clustering
*   D) Principal Component Analysis
*   **Correct Answer:** B) Logistic regression maps output predictions to a probability between 0 and 1, making it ideal for binary classification.
*   **Distractor Analysis:**
    *   *Why correct:* Logistic regression maps output predictions to a probability between 0 and 1, making it ideal for binary classification.
    *   Linear regression is for continuous variables. K-Means is for grouping.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Linear equation ($y=mx+b$)**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
C) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
B) Electrostatic Discharge protection; tools (like wrist straps, grounding mats) used to prevent static electricity from destroying sensitive microchips when handling hardware.
D) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Linear equation ($y=mx+b$)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Linear equation ($y=mx+b$)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Linear equation ($y=mx+b$)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Linear equation ($y=mx+b$)**.


---

**Question 3**
A systems administrator or developer needs to **use the trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
A) predictions = model.predict(X_test)
D) accuracy = accuracy_score(y_test, predictions)
C) import pandas as pd; df = pd.read_csv('data.csv')
B) model.fit(X_train, y_train)
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    * *Why A is correct:* The `predictions = model.predict(X_test)` command is directly designed to use the trained model to generate predictions on unseen test data.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Linear and Logistic Regression Models** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
C) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.


---

**Question 5**
When designing a system for **Linear and Logistic Regression Models**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
B) Apply differential privacy methods to the training data and limit public API rate queries.
C) Enable full disk encryption on all client endpoints.
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.


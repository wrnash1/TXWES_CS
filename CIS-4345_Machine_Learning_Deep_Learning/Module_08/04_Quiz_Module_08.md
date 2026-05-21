# Quiz: Module 08 - Dimensionality Reduction (PCA)
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What is the main purpose of Principal Component Analysis (PCA)?
*   A) To predict label outputs
*   B) To project high-dimensional data onto lower-dimensional spaces while preserving maximum variance
*   C) To cluster similar users
*   D) To balance binary classes
*   **Correct Answer:** B) PCA simplifies data structures by identifying orthogonal principal components that capture the most information.
*   **Distractor Analysis:**
    *   *Why correct:* PCA simplifies data structures by identifying orthogonal principal components that capture the most information.
    *   PCA is a linear transformer, not a predictor or clustering engine.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **covariance matrix**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
C) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
D) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
B) The process of using domain knowledge to extract features from raw data, improving machine learning model performance.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **covariance matrix**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **covariance matrix**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **covariance matrix**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **covariance matrix**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
D) accuracy = accuracy_score(y_test, predictions)
A) model.fit(X_train, y_train)
C) predictions = model.predict(X_test)
B) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Dimensionality Reduction (PCA)** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
D) Reboot the physical machine and wait for services to reload.
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..


---

**Question 5**
When designing a system for **Dimensionality Reduction (PCA)**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.


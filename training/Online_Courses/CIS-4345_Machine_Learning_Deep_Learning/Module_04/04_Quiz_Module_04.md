# Quiz: Module 04 - Regularization Techniques
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
How does L1 regularization (Lasso) differ from L2 regularization (Ridge)?
*   A) L1 adds squared penalties, L2 adds absolute penalties
*   B) L1 can force feature weights exactly to zero, performing feature selection
*   C) L2 is only used in unsupervised learning
*   D) L1 increases model training time by 10x
*   **Correct Answer:** B) Lasso adds an absolute weight penalty to the cost, leading to sparse coefficients (forces unimportant features to 0).
*   **Distractor Analysis:**
    *   *Why correct:* Lasso adds an absolute weight penalty to the cost, leading to sparse coefficients (forces unimportant features to 0).
    *   Ridge uses squared penalties (L2) and shrinks weights close to but not exactly to 0.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Overfitting indicators**?
B) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
D) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
C) A two-dimensional CSS layout system that allows developers to design complex grid-based user interfaces with rows and columns, offering precise control over alignment.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Overfitting indicators**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Overfitting indicators**.
    * *Why A is correct:* This describes the exact role and function of **Overfitting indicators**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Overfitting indicators**.


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
While working on **Regularization Techniques** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
D) Reboot the physical machine and wait for services to reload.
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **Regularization Techniques**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
A) Apply differential privacy methods to the training data and limit public API rate queries.
C) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


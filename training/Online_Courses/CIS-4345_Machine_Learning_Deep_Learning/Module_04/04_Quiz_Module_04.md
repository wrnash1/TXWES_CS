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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **alpha penalty.**?
C) The difference in height between the left and right subtrees of a node in an AVL tree, which must be -1, 0, or 1 to remain balanced.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
D) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
B) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **alpha penalty.**.
    * *Why A is correct:* This describes the exact role and function of **alpha penalty.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **alpha penalty.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **alpha penalty.**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
C) accuracy = accuracy_score(y_test, predictions)
B) predictions = model.predict(X_test)
A) model.fit(X_train, y_train)
D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Regularization Techniques** in a production environment, you encounter a system alert indicating a **Low Model Generalization** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why C is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why A is correct:* Because The model has overfit the training data and performs poorly on unseen validation or testing datasets. The appropriate fix is to Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture..
    * *Why B is incorrect:* This action does not resolve the root cause of Low Model Generalization.


---

**Question 5**
When designing a system for **Regularization Techniques**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


# Quiz: Module 02 - Supervised vs Unsupervised Learning
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which type of machine learning uses labeled data to predict continuous numerical values?
*   A) Classification
*   B) Clustering
*   C) Regression
*   D) Dimensionality Reduction
*   **Correct Answer:** C) Regression is a supervised learning task designed to predict continuous values (e.g., home prices).
*   **Distractor Analysis:**
    *   *Why correct:* Regression is a supervised learning task designed to predict continuous values (e.g., home prices).
    *   Classification predicts discrete labels. Clustering deals with unlabeled groupings.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **clustering**?
B) The single, top-most node in a tree structure from which all other nodes descend, serving as the starting reference for search algorithms.
C) The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
D) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **clustering**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **clustering**.
    * *Why A is correct:* This describes the exact role and function of **clustering**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **clustering**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
D) predictions = model.predict(X_test)
B) import pandas as pd; df = pd.read_csv('data.csv')
A) model.fit(X_train, y_train)
C) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Supervised vs Unsupervised Learning** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
D) Reboot the physical machine and wait for services to reload.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **Supervised vs Unsupervised Learning**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
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


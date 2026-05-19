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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **regression**?
D) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
C) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) CSS properties (like block, inline, flex, grid) that determine how an element is rendered and how it behaves relative to surrounding elements.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **regression**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **regression**.
    * *Why A is correct:* This describes the exact role and function of **regression**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **regression**.


---

**Question 3**
A systems administrator or developer needs to **train the machine learning model on the training features and targets**. Which of the following commands is the most appropriate to execute?
C) import pandas as pd; df = pd.read_csv('data.csv')
D) accuracy = accuracy_score(y_test, predictions)
A) model.fit(X_train, y_train)
B) predictions = model.predict(X_test)
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `model.fit(X_train, y_train)` command is directly designed to train the machine learning model on the training features and targets.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Supervised vs Unsupervised Learning** in a production environment, you encounter a system alert indicating a **Low Model Generalization** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Correct Answer:** A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why C is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why A is correct:* Because The model has overfit the training data and performs poorly on unseen validation or testing datasets. The appropriate fix is to Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture..
    * *Why B is incorrect:* This action does not resolve the root cause of Low Model Generalization.


---

**Question 5**
When designing a system for **Supervised vs Unsupervised Learning**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
C) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


# Quiz: Module 03 - Logistic Regression
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
Which mathematical function maps real number inputs to a probability value between 0 and 1 in logistic regression?
*   A) Linear function
*   B) Sigmoid (Logistic) function
*   C) Step function
*   D) Relu function
*   **Correct Answer:** B) The sigmoid function (1 / (1 + e^-x)) outputs values bounded between 0 and 1, representing probabilities.
*   **Distractor Analysis:**
    *   *Why correct:* The sigmoid function (1 / (1 + e^-x)) outputs values bounded between 0 and 1, representing probabilities.
    *   Linear function can return infinite outputs. ReLU is max(0, x).

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **probability mapping**?
C) A computational model inspired by the biological brain structure, consisting of interconnected layers of nodes (neurons).
D) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **probability mapping**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **probability mapping**.
    * *Why A is correct:* This describes the exact role and function of **probability mapping**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **probability mapping**.


---

**Question 3**
A systems administrator or developer needs to **import the pandas library to load and analyze a tabular dataset**. Which of the following commands is the most appropriate to execute?
D) model.fit(X_train, y_train)
B) predictions = model.predict(X_test)
C) accuracy = accuracy_score(y_test, predictions)
A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `import pandas as pd; df = pd.read_csv('data.csv')` command is directly designed to import the pandas library to load and analyze a tabular dataset.


---

**Question 4**
While working on **Logistic Regression** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **Logistic Regression**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
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


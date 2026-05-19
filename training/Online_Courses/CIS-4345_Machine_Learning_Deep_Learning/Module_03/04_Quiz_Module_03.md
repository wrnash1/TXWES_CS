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
D) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
C) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
B) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **probability mapping**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **probability mapping**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **probability mapping**.
    * *Why A is correct:* This describes the exact role and function of **probability mapping**.


---

**Question 3**
A systems administrator or developer needs to **import the pandas library to load and analyze a tabular dataset**. Which of the following commands is the most appropriate to execute?
B) accuracy = accuracy_score(y_test, predictions)
A) import pandas as pd; df = pd.read_csv('data.csv')
C) predictions = model.predict(X_test)
D) model.fit(X_train, y_train)
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `import pandas as pd; df = pd.read_csv('data.csv')` command is directly designed to import the pandas library to load and analyze a tabular dataset.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Logistic Regression** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **Logistic Regression**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


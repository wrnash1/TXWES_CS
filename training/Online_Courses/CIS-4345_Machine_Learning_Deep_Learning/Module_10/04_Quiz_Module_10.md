# Quiz: Module 10 - Activation & Backpropagation
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
Which mathematical derivative rule is utilized to compute gradients of nested layers during the backpropagation step?
*   A) Product Rule
*   B) Quotient Rule
*   C) Chain Rule
*   D) Addition Rule
*   **Correct Answer:** C) Backpropagation computes error gradients starting at the output layer and propagating backward using the Chain Rule.
*   **Distractor Analysis:**
    *   *Why correct:* Backpropagation computes error gradients starting at the output layer and propagating backward using the Chain Rule.
    *   The chain rule handles derivatives of composed functions.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **loss calculations**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
C) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
B) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
D) A computational model inspired by the biological brain structure, consisting of interconnected layers of nodes (neurons).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **loss calculations**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **loss calculations**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **loss calculations**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **loss calculations**.


---

**Question 3**
A systems administrator or developer needs to **import the pandas library to load and analyze a tabular dataset**. Which of the following commands is the most appropriate to execute?
C) model.fit(X_train, y_train)
B) accuracy = accuracy_score(y_test, predictions)
A) import pandas as pd; df = pd.read_csv('data.csv')
D) predictions = model.predict(X_test)
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `import pandas as pd; df = pd.read_csv('data.csv')` command is directly designed to import the pandas library to load and analyze a tabular dataset.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Activation & Backpropagation** in a production environment, you encounter a system alert indicating a **Low Model Generalization** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
D) Reboot the physical machine and wait for services to reload.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why A is correct:* Because The model has overfit the training data and performs poorly on unseen validation or testing datasets. The appropriate fix is to Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture..
    * *Why D is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why C is incorrect:* This action does not resolve the root cause of Low Model Generalization.


---

**Question 5**
When designing a system for **Activation & Backpropagation**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
A) Apply differential privacy methods to the training data and limit public API rate queries.
D) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


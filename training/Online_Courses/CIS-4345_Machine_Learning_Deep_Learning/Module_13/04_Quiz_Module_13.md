# Quiz: Module 13 - Natural Language Processing
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What is a word embedding in Natural Language Processing (NLP)?
*   A) A dictionary lookup string
*   B) A dense vector representation where words with similar semantic meanings are mapped close together
*   C) A file compression method
*   D) A type of database primary key
*   **Correct Answer:** B) Word embeddings project words into high-dimensional geometric spaces, encoding semantic relationships.
*   **Distractor Analysis:**
    *   *Why correct:* Word embeddings project words into high-dimensional geometric spaces, encoding semantic relationships.
    *   It is not a static dictionary lookup or a database key.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **vocabulary lookup**?
C) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
D) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **vocabulary lookup**.
    * *Why A is correct:* This describes the exact role and function of **vocabulary lookup**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **vocabulary lookup**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **vocabulary lookup**.


---

**Question 3**
A systems administrator or developer needs to **use the trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
D) import pandas as pd; df = pd.read_csv('data.csv')
A) predictions = model.predict(X_test)
B) accuracy = accuracy_score(y_test, predictions)
C) model.fit(X_train, y_train)
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `predictions = model.predict(X_test)` command is directly designed to use the trained model to generate predictions on unseen test data.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Natural Language Processing** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
D) Reboot the physical machine and wait for services to reload.
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **Natural Language Processing**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


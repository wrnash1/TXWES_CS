# Quiz: Module 07 - K-Means & Hierarchical Clustering
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
How do you determine the optimal number of clusters (K) in K-Means clustering using the Elbow Method?
*   A) Look for the point where the cost curve changes from steep to shallow (inertia drops level off)
*   B) Find the highest classification score
*   C) Check the number of columns
*   D) Count the total row count
*   **Correct Answer:** A) The 'elbow' represents a point of diminishing returns where adding more clusters yields minimal reduction in inertia.
*   **Distractor Analysis:**
    *   *Why correct:* The 'elbow' represents a point of diminishing returns where adding more clusters yields minimal reduction in inertia.
    *   Classification scores are unavailable since K-Means is unsupervised.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **elbow method**?
C) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
B) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
D) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **elbow method**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **elbow method**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **elbow method**.
    * *Why A is correct:* This describes the exact role and function of **elbow method**.


---

**Question 3**
A systems administrator or developer needs to **calculate the accuracy metric of the model predictions against actual labels**. Which of the following commands is the most appropriate to execute?
D) predictions = model.predict(X_test)
C) model.fit(X_train, y_train)
B) import pandas as pd; df = pd.read_csv('data.csv')
A) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) accuracy = accuracy_score(y_test, predictions)
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `accuracy = accuracy_score(y_test, predictions)` command is directly designed to calculate the accuracy metric of the model predictions against actual labels.


---

**Question 4**
While working on **K-Means & Hierarchical Clustering** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
D) Reboot the physical machine and wait for services to reload.
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..


---

**Question 5**
When designing a system for **K-Means & Hierarchical Clustering**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
D) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..


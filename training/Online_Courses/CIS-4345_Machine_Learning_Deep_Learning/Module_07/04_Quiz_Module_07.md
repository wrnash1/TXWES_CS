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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **centroids**?
C) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
D) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
B) A machine learning error where a model learns the training data too well, capturing noise and failing to generalize to new data.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **centroids**.
    * *Why A is correct:* This describes the exact role and function of **centroids**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **centroids**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **centroids**.


---

**Question 3**
A systems administrator or developer needs to **import the pandas library to load and analyze a tabular dataset**. Which of the following commands is the most appropriate to execute?
D) accuracy = accuracy_score(y_test, predictions)
C) model.fit(X_train, y_train)
B) predictions = model.predict(X_test)
A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `import pandas as pd; df = pd.read_csv('data.csv')` command is directly designed to import the pandas library to load and analyze a tabular dataset.


---

**Question 4**
While working on **K-Means & Hierarchical Clustering** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **K-Means & Hierarchical Clustering**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..


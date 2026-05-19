# Quiz: Module 13 - Cloud AI Services
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What is the benefit of using Cloud Cognitive Services over building models from scratch?
*   A) Pre-trained models save development time and compute resources
*   B) They are always free
*   C) They do not require an internet connection
*   D) They support any custom hardware
*   **Correct Answer:** A) Cloud cognitive APIs provide pre-trained, vendor-hosted models that can be integrated via simple HTTP requests, bypassing complex local model training.
*   **Distractor Analysis:**
    *   *Why correct:* Cloud cognitive APIs provide pre-trained, vendor-hosted models that can be integrated via simple HTTP requests, bypassing complex local model training.
    *   They are billed services, require internet connections, and run on cloud hardware.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Cognitive APIs**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
C) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
B) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
D) A machine learning error where a model learns the training data too well, capturing noise and failing to generalize to new data.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Cognitive APIs**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Cognitive APIs**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Cognitive APIs**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Cognitive APIs**.


---

**Question 3**
A systems administrator or developer needs to **import the pandas library to load and analyze a tabular dataset**. Which of the following commands is the most appropriate to execute?
D) accuracy = accuracy_score(y_test, predictions)
A) import pandas as pd; df = pd.read_csv('data.csv')
B) predictions = model.predict(X_test)
C) model.fit(X_train, y_train)
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `import pandas as pd; df = pd.read_csv('data.csv')` command is directly designed to import the pandas library to load and analyze a tabular dataset.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Cloud AI Services** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
D) Reboot the physical machine and wait for services to reload.
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.


---

**Question 5**
When designing a system for **Cloud AI Services**, you must mitigate the risk of **Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs.**. Which of the following security configurations or controls represents the best practice to implement?
A) Apply differential privacy methods to the training data and limit public API rate queries.
B) Train models with adversarial inputs and implement input validation/filtering on inputs.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Apply differential privacy methods to the training data and limit public API rate queries. mitigates the risk of Attackers reconstructing sensitive training data by querying the public model API and analyzing outputs..
    * *Why B is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why D is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.
    * *Why C is incorrect:* This does not address the security vulnerability of Model Inversion Vulnerability.


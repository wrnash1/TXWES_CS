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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **pre-trained vs custom models**?
C) The difference in height between the left and right subtrees of a node in an AVL tree, which must be -1, 0, or 1 to remain balanced.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
B) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
D) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **pre-trained vs custom models**.
    * *Why A is correct:* This describes the exact role and function of **pre-trained vs custom models**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **pre-trained vs custom models**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **pre-trained vs custom models**.


---

**Question 3**
A systems administrator or developer needs to **import the pandas library to load and analyze a tabular dataset**. Which of the following commands is the most appropriate to execute?
B) predictions = model.predict(X_test)
A) import pandas as pd; df = pd.read_csv('data.csv')
D) accuracy = accuracy_score(y_test, predictions)
C) model.fit(X_train, y_train)
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `import pandas as pd; df = pd.read_csv('data.csv')` command is directly designed to import the pandas library to load and analyze a tabular dataset.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Cloud AI Services** in a production environment, you encounter a system alert indicating a **Low Model Generalization** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
C) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Correct Answer:** A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why A is correct:* Because The model has overfit the training data and performs poorly on unseen validation or testing datasets. The appropriate fix is to Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture..
    * *Why B is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why C is incorrect:* This action does not resolve the root cause of Low Model Generalization.


---

**Question 5**
When designing a system for **Cloud AI Services**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Apply differential privacy methods to the training data and limit public API rate queries.
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..


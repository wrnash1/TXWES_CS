# Quiz: Module 12 - Ethical AI and Responsible Deployment
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which Responsible AI principle states that AI systems should treat all people fairly without demographic discrimination?
*   A) Reliability and Safety
*   B) Privacy and Security
*   C) Fairness
*   D) Transparency
*   **Correct Answer:** C) Fairness ensures that algorithms do not make biased assertions based on gender, race, or demographics.
*   **Distractor Analysis:**
    *   *Why correct:* Fairness ensures that algorithms do not make biased assertions based on gender, race, or demographics.
    *   Safety focuses on system operational hazards. Privacy focuses on data protection.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Privacy/Security**?
D) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
B) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
C) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Privacy/Security**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Privacy/Security**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Privacy/Security**.
    * *Why A is correct:* This describes the exact role and function of **Privacy/Security**.


---

**Question 3**
A systems administrator or developer needs to **use the trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
B) accuracy = accuracy_score(y_test, predictions)
A) predictions = model.predict(X_test)
C) import pandas as pd; df = pd.read_csv('data.csv')
D) model.fit(X_train, y_train)
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `predictions = model.predict(X_test)` command is directly designed to use the trained model to generate predictions on unseen test data.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Ethical AI and Responsible Deployment** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..


---

**Question 5**
When designing a system for **Ethical AI and Responsible Deployment**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Apply differential privacy methods to the training data and limit public API rate queries.
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.


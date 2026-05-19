# Quiz: Module 08 - Deep Learning & Neural Networks
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What activation function is typically used in the hidden layers of modern neural networks to prevent vanishing gradients?
*   A) Sigmoid
*   B) Rectified Linear Unit (ReLU)
*   C) Tanh
*   D) Step function
*   **Correct Answer:** B) ReLU (outputting max(0, x)) is widely used in hidden layers because of its computational simplicity and prevention of vanishing gradients.
*   **Distractor Analysis:**
    *   *Why correct:* ReLU (outputting max(0, x)) is widely used in hidden layers because of its computational simplicity and prevention of vanishing gradients.
    *   Sigmoid and Tanh are prone to vanishing gradients in deep networks.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **layers (input**?
C) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
D) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
B) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **layers (input**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **layers (input**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **layers (input**.
    * *Why A is correct:* This describes the exact role and function of **layers (input**.


---

**Question 3**
A systems administrator or developer needs to **calculate the accuracy metric of the model predictions against actual labels**. Which of the following commands is the most appropriate to execute?
B) predictions = model.predict(X_test)
C) model.fit(X_train, y_train)
D) import pandas as pd; df = pd.read_csv('data.csv')
A) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) accuracy = accuracy_score(y_test, predictions)
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `accuracy = accuracy_score(y_test, predictions)` command is directly designed to calculate the accuracy metric of the model predictions against actual labels.


---

**Question 4**
While working on **Deep Learning & Neural Networks** in a production environment, you encounter a system alert indicating a **Missing Value Errors** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
C) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why C is incorrect:* This action does not resolve the root cause of Missing Value Errors.
    * *Why A is correct:* Because The dataset contains null or missing values, causing mathematical operators in the model to fail. The appropriate fix is to Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values..
    * *Why D is incorrect:* This action does not resolve the root cause of Missing Value Errors.


---

**Question 5**
When designing a system for **Deep Learning & Neural Networks**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Apply differential privacy methods to the training data and limit public API rate queries.
C) Enable full disk encryption on all client endpoints.
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..


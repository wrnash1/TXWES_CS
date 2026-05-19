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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **backpropagation.**?
C) A complete binary tree where the key of any parent node is less than or equal to the keys of its children, guaranteeing the root is always the minimum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
D) A two-dimensional CSS layout system that allows developers to design complex grid-based user interfaces with rows and columns, offering precise control over alignment.
B) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **backpropagation.**.
    * *Why A is correct:* This describes the exact role and function of **backpropagation.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **backpropagation.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **backpropagation.**.


---

**Question 3**
A systems administrator or developer needs to **use the trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
B) import pandas as pd; df = pd.read_csv('data.csv')
A) predictions = model.predict(X_test)
C) model.fit(X_train, y_train)
D) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `predictions = model.predict(X_test)` command is directly designed to use the trained model to generate predictions on unseen test data.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Deep Learning & Neural Networks** in a production environment, you encounter a system alert indicating a **Data Leakage** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
D) Reboot the physical machine and wait for services to reload.
A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
B) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   **Correct Answer:** A) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why D is incorrect:* This action does not resolve the root cause of Data Leakage.
    * *Why A is correct:* Because Information from outside the training dataset is used to train the model, resulting in overly optimistic validation scores. The appropriate fix is to Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set..
    * *Why B is incorrect:* This action does not resolve the root cause of Data Leakage.


---

**Question 5**
When designing a system for **Deep Learning & Neural Networks**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
B) Apply differential privacy methods to the training data and limit public API rate queries.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.


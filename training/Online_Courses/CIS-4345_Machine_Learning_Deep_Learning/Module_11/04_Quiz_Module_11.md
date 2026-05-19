# Quiz: Module 11 - Convolutional Neural Networks
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
Why are Convolutional layers superior to Fully Connected layers for image processing tasks?
*   A) They require larger database spaces
*   B) They preserve spatial relationships and reduce parameters through weight sharing
*   C) They do not require activation functions
*   D) They compile directly to C++ binaries
*   **Correct Answer:** B) CNN filters scan local pixel neighborhoods, capturing spatial patterns (edges, shapes) regardless of position in the image.
*   **Distractor Analysis:**
    *   *Why correct:* CNN filters scan local pixel neighborhoods, capturing spatial patterns (edges, shapes) regardless of position in the image.
    *   Fully connected layers flatten images, destroying spatial layout and causing parameters to explode.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **stride settings**?
C) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
D) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
B) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within ai operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **stride settings**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **stride settings**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **stride settings**.
    * *Why A is correct:* This describes the exact role and function of **stride settings**.


---

**Question 3**
A systems administrator or developer needs to **calculate the accuracy metric of the model predictions against actual labels**. Which of the following commands is the most appropriate to execute?
A) accuracy = accuracy_score(y_test, predictions)
B) predictions = model.predict(X_test)
D) model.fit(X_train, y_train)
C) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) accuracy = accuracy_score(y_test, predictions)
*   **Distractor Analysis:**
    * *Why A is correct:* The `accuracy = accuracy_score(y_test, predictions)` command is directly designed to calculate the accuracy metric of the model predictions against actual labels.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Convolutional Neural Networks** in a production environment, you encounter a system alert indicating a **Low Model Generalization** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why A is correct:* Because The model has overfit the training data and performs poorly on unseen validation or testing datasets. The appropriate fix is to Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture..
    * *Why B is incorrect:* This action does not resolve the root cause of Low Model Generalization.
    * *Why D is incorrect:* This action does not resolve the root cause of Low Model Generalization.


---

**Question 5**
When designing a system for **Convolutional Neural Networks**, you must mitigate the risk of **Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications.**. Which of the following security configurations or controls represents the best practice to implement?
A) Train models with adversarial inputs and implement input validation/filtering on inputs.
B) Apply differential privacy methods to the training data and limit public API rate queries.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Train models with adversarial inputs and implement input validation/filtering on inputs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Train models with adversarial inputs and implement input validation/filtering on inputs. mitigates the risk of Attackers injecting subtle, imperceptible noise into input data (e.g. images) to force the AI into making incorrect classifications..
    * *Why B is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why C is incorrect:* This does not address the security vulnerability of Adversarial Examples.
    * *Why D is incorrect:* This does not address the security vulnerability of Adversarial Examples.


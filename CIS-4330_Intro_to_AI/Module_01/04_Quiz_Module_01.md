# Quiz: Module 01 - Introduction to AI & Machine Learning
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What is the primary characteristic of Machine Learning?
*   A) Hardcoded if-else statements
*   B) Using algorithms that learn patterns directly from data
*   C) Mimicking human speech using search trees
*   D) Database indexing
*   **Correct Answer:** B) Machine Learning algorithms use input data to build mathematical models that perform tasks without explicit, hardcoded instructions.
*   **Distractor Analysis:**
    *   *Why correct:* Machine Learning algorithms use input data to build mathematical models that perform tasks without explicit, hardcoded instructions.
    *   Hardcoded statements are traditional programming. Database indexing is database structure.

---

**Question 2**
In the context of AI and machine learning, which of the following is the most accurate definition of **Artificial Intelligence**?
*   A) A branch of computer science that enables systems to simulate human cognitive tasks such as learning, reasoning, and problem-solving from data or experience.
*   B) A binary search tree that automatically adjusts its height during insertions and deletions to maintain logarithmic operations.
*   C) A method of configuring maximum execution time limits on database query threads.
*   D) A network protocol used to route packets between subnets in a data center.
*   **Correct Answer:** A) A branch of computer science that enables systems to simulate human cognitive tasks such as learning, reasoning, and problem-solving from data or experience.
*   **Distractor Analysis:**
    *   *Why A is correct:* This accurately captures the AI-900 definition of Artificial Intelligence as the simulation of human cognitive capabilities by machines.
    *   *Why B is incorrect:* This describes a self-balancing binary search tree (e.g., AVL tree) — a data structures concept unrelated to AI.
    *   *Why C is incorrect:* This describes a database timeout configuration parameter, not an AI concept.
    *   *Why D is incorrect:* This describes network routing, which is a networking concept unrelated to AI or ML.

---

**Question 3**
A developer needs to **use a trained model to generate predictions on unseen test data**. Which of the following commands is the most appropriate to execute?
*   A) predictions = model.predict(X_test)
*   B) model.fit(X_train, y_train)
*   C) accuracy = accuracy_score(y_test, predictions)
*   D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    *   *Why A is correct:* `model.predict(X_test)` applies the trained model to new test data and returns predicted output values.
    *   *Why B is incorrect:* `model.fit()` trains the model on existing data — it does not generate predictions on new data.
    *   *Why C is incorrect:* `accuracy_score()` evaluates predictions already made — it does not generate predictions itself.
    *   *Why D is incorrect:* This loads a CSV file into a DataFrame — it is data loading, not prediction.

---

**Question 4**
A data scientist observes that a model achieves 99% accuracy on training data but only 62% on the validation set. Which of the following is the most effective action to address this?
*   A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   B) Ensure data preprocessing steps (scaling, normalization) are fit only on the training set and applied to the test set.
*   C) Use imputation techniques (mean, median, mode) or drop rows/columns containing missing values.
*   D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Apply regularization techniques (L1/L2), gather more training data, or simplify the model architecture.
*   **Distractor Analysis:**
    *   *Why A is correct:* The model has overfit the training data and performs poorly on unseen data. Regularization, more data, or a simpler model reduces overfitting.
    *   *Why B is incorrect:* Fitting scalers on the full dataset causes data leakage, but is not the primary fix for overfitting.
    *   *Why C is incorrect:* Imputation addresses missing data issues, not overfitting.
    *   *Why D is incorrect:* Rebooting a machine has no effect on a model's generalization performance.

---

**Question 5**
A model is deployed publicly via an API. Attackers are querying it repeatedly and reconstructing sensitive training data from the outputs — a technique called **model inversion**. Which security control best mitigates this risk?
*   A) Apply differential privacy methods to the training data and limit public API query rates.
*   B) Train models with adversarial inputs and implement input validation/filtering.
*   C) Enable full disk encryption on all client endpoints.
*   D) Require multi-factor authentication for all developer workstations.
*   **Correct Answer:** A) Apply differential privacy methods to the training data and limit public API query rates.
*   **Distractor Analysis:**
    *   *Why A is correct:* Differential privacy adds mathematical noise to training data so individual records cannot be reconstructed, and rate limiting reduces the attacker's ability to query the model extensively.
    *   *Why B is incorrect:* Adversarial training defends against adversarial examples (perturbed inputs), not model inversion attacks.
    *   *Why C is incorrect:* Full disk encryption protects data at rest on endpoints but does not prevent model inversion via API queries.
    *   *Why D is incorrect:* MFA protects developer accounts but does not address a publicly accessible model API being queried by attackers.

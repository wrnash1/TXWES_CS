# Quiz: Module 10 - Responsible AI: Ethics, Fairness, and Transparency
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What is the process of breaking down a continuous stream of text into individual words or punctuation marks called?
*   A) Lemmatization
*   B) Tokenization
*   C) Stemming
*   D) Vectorization
*   **Correct Answer:** B) Tokenization splits a raw text string into a sequence of discrete tokens (words and punctuation), which is the required first step before any further NLP processing can occur.
*   **Distractor Analysis:**
    *   *Why correct:* Every downstream NLP operation — stop-word removal, vectorization, model training — requires text to be in token form first. Tokenization performs that initial segmentation.
    *   Lemmatization and stemming both reduce words to root forms after tokenization. Vectorization converts an already-tokenized list into numeric features.

---

**Question 2**
In the context of Microsoft's Responsible AI framework, which of the following is the most accurate definition of the **Fairness** principle?
*   A) AI systems should treat all individuals equitably and must not produce discriminatory outcomes based on protected characteristics such as race, gender, age, or disability status.
*   B) AI systems should perform consistently and reliably across all operating conditions, failing gracefully and safely rather than causing unpredictable harm.
*   C) Humans must retain oversight and responsibility for AI system decisions, with clear lines of accountability when an AI causes negative outcomes.
*   D) AI systems should be designed to be understandable, with their capabilities, limitations, and decision-making processes communicated clearly to users and operators.
*   **Correct Answer:** A) AI systems should treat all individuals equitably and must not produce discriminatory outcomes based on protected characteristics such as race, gender, age, or disability status.
*   **Distractor Analysis:**
    *   *Why A is correct:* Fairness is specifically about equitable treatment and non-discrimination — for example, ensuring a hiring algorithm does not systematically disadvantage one demographic group over another.
    *   *Why B is incorrect:* This describes the **Reliability and Safety** principle — consistent performance and graceful failure under all conditions.
    *   *Why C is incorrect:* This describes the **Accountability** principle — humans maintaining responsibility and oversight over AI systems.
    *   *Why D is incorrect:* This describes the **Transparency** principle — making AI behavior and reasoning understandable to those who use or are affected by it.

---

**Question 3**
A developer needs to **train a machine learning model on labeled training features and targets**. Which command is most appropriate?
*   A) model.fit(X_train, y_train)
*   B) predictions = model.predict(X_test)
*   C) accuracy = accuracy_score(y_test, predictions)
*   D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    *   *Why A is correct:* `model.fit(X_train, y_train)` passes the feature matrix and target vector to the model, allowing it to learn the mapping between inputs and outputs through the training algorithm.
    *   *Why B is incorrect:* `model.predict()` generates predictions from an already-trained model; it requires `fit()` to be called first.
    *   *Why C is incorrect:* `accuracy_score()` evaluates predictions against true labels — an evaluation step that comes after training and prediction.
    *   *Why D is incorrect:* This loads a CSV file into a DataFrame — data loading, which occurs before any model training.

---

**Question 4**
A bank deploys an AI loan-approval model. Auditors find the model denies applications from one demographic group at twice the rate of comparable applicants from other groups, even when financial risk factors are equal. Which Responsible AI principle is being violated, and what is the recommended action?
*   A) Fairness — audit the training data for historical bias, apply fairness-aware algorithms or re-weighting techniques, and evaluate the model's outputs across demographic groups before redeployment.
*   B) Reliability — retrain the model with more diverse data to improve its performance consistency across all operating conditions and edge cases.
*   C) Privacy and Security — anonymize the demographic data in the training set so the model cannot learn any personal attributes associated with applicants.
*   D) Transparency — add a feature importance report to the model so auditors can see which input variables contribute most to each loan decision.
*   **Correct Answer:** A) Fairness — audit the training data for historical bias, apply fairness-aware algorithms or re-weighting techniques, and evaluate the model's outputs across demographic groups before redeployment.
*   **Distractor Analysis:**
    *   *Why A is correct:* Disparate impact across protected demographic groups is the defining Fairness violation. The fix requires examining the training data for embedded historical bias and applying techniques that ensure equitable outcomes across groups.
    *   *Why B is incorrect:* Reliability addresses inconsistent or unsafe model behavior, not discriminatory outcomes that are consistently applied to a demographic group.
    *   *Why C is incorrect:* Anonymizing demographic features may not eliminate bias if correlated proxy variables remain in the data — and this action addresses Privacy, not Fairness.
    *   *Why D is incorrect:* Adding feature importance improves Transparency — it explains which features drive decisions — but does not address the discriminatory outcomes that define the Fairness violation.

---

**Question 5**
A company deploys a customer-service NLP model that classifies support tickets. Attackers submit carefully crafted ticket text with subtle word substitutions, causing the model to misclassify urgent security incidents as low-priority billing questions. Which defense best mitigates this **adversarial text** attack?
*   A) Train the model with adversarial text examples included in the training set and implement input validation to detect anomalous or manipulated text before classification.
*   B) Apply differential privacy to the training data and rate-limit the ticket submission API to reduce the attacker's query volume.
*   C) Enable full disk encryption on all servers hosting the ticket classification model.
*   D) Require multi-factor authentication for all agents who access the ticket management dashboard.
*   **Correct Answer:** A) Train the model with adversarial text examples included in the training set and implement input validation to detect anomalous or manipulated text before classification.
*   **Distractor Analysis:**
    *   *Why A is correct:* Adversarial training on perturbed text examples teaches the model to classify both clean and manipulated inputs correctly. Input validation can flag statistically unusual text patterns before they reach the classifier.
    *   *Why B is incorrect:* Differential privacy defends against training data reconstruction via model inversion — it does not protect against adversarial inputs manipulated at inference time.
    *   *Why C is incorrect:* Disk encryption protects data at rest on the server; it has no effect on crafted text payloads submitted through the live classification API.
    *   *Why D is incorrect:* MFA secures agent account access to the dashboard but does not prevent external attackers from submitting adversarial ticket text through the public submission endpoint.

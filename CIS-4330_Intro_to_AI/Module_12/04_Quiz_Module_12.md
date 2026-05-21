# Quiz: Module 12 - AI in Business: Use Cases and ROI
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which Responsible AI principle states that AI systems should treat all people fairly without demographic discrimination?
*   A) Reliability and Safety
*   B) Privacy and Security
*   C) Fairness
*   D) Transparency
*   **Correct Answer:** C) Fairness requires that AI systems produce equitable outcomes across all demographic groups and do not make decisions that discriminate based on race, gender, age, disability, or other protected characteristics.
*   **Distractor Analysis:**
    *   *Why correct:* Fairness is specifically about equitable treatment — for example, ensuring a hiring or credit model does not systematically disadvantage one demographic group.
    *   Reliability and Safety addresses consistent operation and graceful failure. Privacy and Security addresses data protection and consent. Transparency addresses explainability and openness about AI capabilities and limitations.

---

**Question 2**
In the context of Azure AI business applications, which of the following is the most accurate definition of **anomaly detection**?
*   A) A machine learning technique that identifies data points or events that deviate significantly from an expected pattern in a time-series or dataset, used to flag unusual activity such as fraud, equipment failure, or traffic spikes without requiring labeled training data.
*   B) A supervised classification approach that assigns each data point to one of several predefined categories (e.g., spam/not spam) based on patterns learned from labeled training examples.
*   C) A technique that groups similar data points together into clusters based on feature similarity, without any predefined class labels or target variable, used for customer segmentation and topic discovery.
*   D) A process that extracts structured information — such as named entities, key phrases, and relationships — from unstructured text documents to make them searchable and analyzable.
*   **Correct Answer:** A) A machine learning technique that identifies data points or events that deviate significantly from an expected pattern in a time-series or dataset, used to flag unusual activity such as fraud, equipment failure, or traffic spikes without requiring labeled training data.
*   **Distractor Analysis:**
    *   *Why A is correct:* Azure Anomaly Detector applies this technique to business metrics — it learns normal behavior automatically and surfaces deviations in real time, making it suitable for IoT sensor monitoring, financial fraud detection, and application performance management.
    *   *Why B is incorrect:* This describes supervised classification — a labeled-data approach that assigns predefined categories, not the pattern-deviation detection of anomaly detection.
    *   *Why C is incorrect:* This describes unsupervised clustering (e.g., K-Means) — grouping data by similarity, not identifying outliers from an expected time-series pattern.
    *   *Why D is incorrect:* This describes knowledge mining / information extraction — pulling structured data from unstructured text, which is the domain of Azure Cognitive Search and Azure AI Language, not anomaly detection.

---

**Question 3**
A developer needs to **load a tabular dataset from a CSV file using the Pandas library**. Which command is most appropriate?
*   A) import pandas as pd; df = pd.read_csv('data.csv')
*   B) model.fit(X_train, y_train)
*   C) predictions = model.predict(X_test)
*   D) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    *   *Why A is correct:* `pd.read_csv()` reads a CSV file from disk into a Pandas DataFrame — the standard first step in any Python ML or data analysis pipeline.
    *   *Why B is incorrect:* `model.fit()` trains a model on already-loaded data; it does not load data from a file.
    *   *Why C is incorrect:* `model.predict()` generates predictions from a trained model; data must already be loaded and the model already fitted before prediction.
    *   *Why D is incorrect:* `accuracy_score()` evaluates predictions against true labels — an evaluation step that occurs after loading, training, and predicting.

---

**Question 4**
A retail company deploys an AI recommendation engine that increases click-through rates by 18% but generates recommendations that systematically exclude products marketed to older demographics. Which Responsible AI principle is being violated, and what is the most appropriate response?
*   A) Fairness — audit the recommendation algorithm and training data for age-related bias, apply fairness constraints or re-weighting to ensure equitable representation across demographic groups, and re-evaluate before redeployment.
*   B) Reliability — retrain the model with a larger and more representative dataset to improve accuracy and consistency across all product categories and user segments.
*   C) Accountability — assign a dedicated human reviewer to manually approve every recommendation before it is shown to a user, ensuring human oversight of all AI outputs.
*   D) Transparency — publish a detailed report explaining how the recommendation algorithm works and which data signals it uses, so affected users can understand the basis for recommendations they receive.
*   **Correct Answer:** A) Fairness — audit the recommendation algorithm and training data for age-related bias, apply fairness constraints or re-weighting to ensure equitable representation across demographic groups, and re-evaluate before redeployment.
*   **Distractor Analysis:**
    *   *Why A is correct:* Systematically excluding a demographic group from recommendations is a Fairness violation. The root cause is typically biased training data (historical interaction data that underrepresents older users) or an objective function that optimizes click-through without fairness constraints.
    *   *Why B is incorrect:* Reliability addresses inconsistent or unpredictable behavior — the system here is performing consistently (just unfairly). More data alone will not fix demographic exclusion without explicit fairness constraints.
    *   *Why C is incorrect:* Manual human review of every recommendation is operationally impractical at scale and addresses Accountability (oversight), not the underlying algorithmic Fairness problem.
    *   *Why D is incorrect:* Publishing an explanation improves Transparency — it informs users of how the system works — but does not change the discriminatory outputs the Fairness principle requires fixing.

---

**Question 5**
Attackers are submitting thousands of queries to a public AI business intelligence API, analyzing the confidence scores returned with each prediction to reconstruct the private customer records used to train the model. Which defense best mitigates this **model inversion** attack?
*   A) Apply differential privacy to the training data and rate-limit the public inference API to reduce the amount of information an attacker can extract per unit time.
*   B) Train the model with adversarial examples included in the training set and implement input validation and filtering on all API requests.
*   C) Enable full disk encryption on all servers hosting the business intelligence model.
*   D) Require users to complete a CAPTCHA challenge before submitting each inference request to slow down automated querying.
*   **Correct Answer:** A) Apply differential privacy to the training data and rate-limit the public inference API to reduce the amount of information an attacker can extract per unit time.
*   **Distractor Analysis:**
    *   *Why A is correct:* Differential privacy injects calibrated statistical noise into training data, making it mathematically hard to reconstruct individual records from model outputs. Rate-limiting caps how many queries the attacker can submit, reducing the total information extracted.
    *   *Why B is incorrect:* Adversarial training defends against perturbed inputs designed to cause misclassification at inference time — it does not prevent an attacker from using normal API outputs to reverse-engineer training data.
    *   *Why C is incorrect:* Disk encryption protects data stored on servers at rest; it has no effect on information leaked through the live API's prediction confidence scores.
    *   *Why D is incorrect:* CAPTCHAs can be bypassed by motivated attackers and only slow manual querying — they do not address the information leakage from the model's output distribution itself.

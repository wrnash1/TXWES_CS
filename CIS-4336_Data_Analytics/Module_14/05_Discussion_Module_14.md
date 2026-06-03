# Discussion Forum: Module 14 — Machine Learning for Data Analysts

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Overview

This discussion asks you to apply machine learning concepts to professional decision-making scenarios. Choose one of the three scenarios below, write an original post of 175–225 words, then respond to at least two classmates who chose different scenarios. Responses must be 75–100 words and add new reasoning rather than simply agreeing.

---

### Scenario A — Supervised or Unsupervised?

A regional bank wants to use machine learning to improve two separate initiatives. The first initiative is to predict which loan applicants are likely to default within 12 months using 5 years of historical application data where each loan is labeled as paid-off or defaulted. The second initiative is to identify natural groupings among customers to inform a new product line without any predefined segments.

Write a post that explains which type of machine learning is appropriate for each initiative. Address the following:

* Why is supervised learning appropriate for the first initiative and unsupervised for the second?
* What labeled data element makes the first initiative supervised?
* What would K-means output for the second initiative, and how would the bank use that output?
* What is one risk of using the clustering output to make lending decisions?

---

### Scenario B — The Overfitting Argument

Your manager reviews your churn prediction model and notices that training accuracy is 96% while test accuracy is 67%. She is impressed by the 96% and wants to deploy the model immediately. You believe the model is seriously overfit and should not go to production.

Write a post making the case against immediate deployment. Address the following:

* What does the gap between training and test accuracy tell you about the model's behavior on new data?
* What would the real-world consequence be of deploying this model to make customer retention calls?
* What are two specific remedies you would apply before recommending deployment?
* How would you explain overfitting to a non-technical manager without using the word "overfitting"?

---

### Scenario C — Feature Engineering Judgment

You are building a model to predict whether a retail store will exceed its monthly sales target. Your raw dataset includes columns for: store_open_date (a date string), store_city (text), square_footage (float), num_employees (int), and region (North/South/East/West).

Write a post that designs the feature engineering step for this dataset. Address the following:

* How would you transform `store_open_date` into model-ready features?
* What encoding strategy would you apply to `store_city` versus `region` and why might they require different approaches?
* Why should you scale `square_footage` and `num_employees` before training certain models?
* Name one additional feature you could derive from the existing columns that might have strong predictive power.

---

### Peer Response Requirements

Respond to at least two classmates who chose different scenarios. Each response must:

* Be 75–100 words
* Identify one specific point you agree with and explain why
* Raise one question or alternative perspective the original poster did not consider
* Reference at least one ML concept or scikit-learn method by name

---

## Discussion Rubric

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 6 | Addresses all four required points with precise ML vocabulary (supervised, unsupervised, classification, clustering, overfitting, feature engineering, one-hot encoding, train/test split). Reasoning connects algorithm characteristics to specific business requirements. Within 175–225 words. |
| 4–5 | Addresses most points. One explanation relies on algorithm names without demonstrating understanding of why the approach fits the scenario. |
| 2–3 | Addresses some points. ML recommendations are made without justification tied to scenario requirements. |
| 0–1 | Post is missing, too brief, or does not engage with the scenario. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 | Responds to at least two classmates with substantive engagement — challenges an algorithm choice, identifies a missing data quality concern, or proposes a better evaluation metric with reasoning. Names at least one ML concept or scikit-learn method. Minimum 75 words per response. |
| 2–3 | Responses are primarily agreement or restatement without new reasoning. |
| 0–1 | Only one response submitted or responses are too brief. |

---

### Submission Deadline

Initial post due by Thursday 11:59 PM. Peer responses due by Sunday 11:59 PM of the same week.

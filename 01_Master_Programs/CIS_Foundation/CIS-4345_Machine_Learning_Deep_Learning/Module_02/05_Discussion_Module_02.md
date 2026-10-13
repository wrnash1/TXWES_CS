# Discussion: Module 02 - Python for ML

**Course:** CIS-4345 Machine Learning and Deep Learning

**Institution:** Texas Wesleyan University

**Instructor:** Professor Nash

**Total Points:** 10

---

## Instructions

Read all three scenarios below. Choose one scenario to address in your initial post. Your initial post is due Wednesday at 11:59 PM. Peer responses are due Sunday at 11:59 PM.

---

## Scenario A: The Data Leakage Audit

A junior data scientist at a retail company builds a customer churn model. To save time, she writes a single `StandardScaler().fit_transform(X)` call on the entire dataset before splitting into train and test partitions. The model reports 94% test accuracy. Her manager asks her to deploy it to production. The model performs at only 71% on live data. She insists the test set accuracy was 94% and cannot explain the discrepancy.

In 175-225 words, diagnose the root cause of the performance gap using the concept of data leakage. Explain precisely how the scaler's `fit_transform` call on the full dataset contaminates the test evaluation. Then describe the correct preprocessing order — which operations must occur before the split versus after the split — and explain why following that order produces an honest estimate of real-world performance. Reference at least one specific scikit-learn or Pandas function from the Module 02 reading guide.

---

## Scenario B: Choosing the Right Visualization

A student has just loaded a medical dataset with 12 numeric features and a binary target (disease present or absent). She wants to understand the data before training but is unsure which visualizations to run first. A classmate suggests she skip visualization and just train a model to "see what happens."

In 175-225 words, argue why exploratory visualization must precede model training. Identify three specific visualizations from the Module 02 reading guide that are most valuable for this binary classification dataset and explain what diagnostic information each one provides. For at least one visualization, describe a specific data problem it might reveal — such as a highly skewed feature, extreme outlier, or multicollinear pair — and explain how that finding would change your preprocessing decisions. Close by describing how the training curve differs from the other four visualizations in terms of when it is generated.

---

## Scenario C: Picking the Right Scaler

A machine learning team is preprocessing three different feature sets before training. Feature set 1 contains annual salaries ranging from $25,000 to $10,000,000 with a few extreme values above $5M. Feature set 2 contains sensor readings bounded between 0 and 100 with a roughly uniform distribution. Feature set 3 contains exam scores that follow a roughly normal distribution between 40 and 100 with no outliers.

In 175-225 words, recommend a specific scikit-learn scaler (`StandardScaler`, `MinMaxScaler`, or `RobustScaler`) for each of the three feature sets and justify each recommendation using the mathematical formula and behavior of that scaler. Explain what would go wrong if you applied `StandardScaler` to feature set 1 without any transformation. Then describe one situation where using MinMaxScaler would be preferable to StandardScaler even for a normally distributed feature, connecting your answer to a specific type of neural network architecture from this course.

---

## Discussion Rubric

| Criteria | Points | Description |
|---|---|---|
| Initial post — content accuracy | 3 | Concepts are technically correct and use appropriate ML terminology. |
| Initial post — depth of analysis | 2 | Response goes beyond surface-level description; includes specific API references or code concepts. |
| Initial post — word count and clarity | 1 | 175-225 words; clearly written with logical structure. |
| Peer response 1 | 2 | Identifies a specific point to build on or challenge; adds new information or a counterexample. |
| Peer response 2 | 2 | Same standard as peer response 1. Responses fewer than 40 words receive 0 points. |
| **Total** | **10** | |

---

## Professor Nash Note

The scenarios in this module connect directly to the most common real-world errors I see in production ML systems. Data leakage, skipped EDA, and wrong scaler choices are responsible for a surprising number of model failures that cost engineering teams weeks to diagnose. Choose the scenario that challenges you most, not the one that feels most comfortable. When responding to peers, push back constructively if their scaler choice or leakage explanation is incomplete — that kind of technical dialogue is exactly what sharpens your exam readiness.

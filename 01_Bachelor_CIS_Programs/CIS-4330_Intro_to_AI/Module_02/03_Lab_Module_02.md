# Lab Activity: Module 02 - Supervised vs Unsupervised Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe fundamental principles of machine learning on Azure
**Points:** 100
**Submission:** Canvas LMS — Module 02 Lab Assignment

---

## Objectives

By the end of this lab, you will be able to:

- Identify whether a scenario calls for supervised or unsupervised learning.
- Distinguish between regression and classification as task types within supervised learning.
- Map a business problem to the appropriate Azure Machine Learning task type.
- Interpret basic model evaluation metrics and explain what they indicate about model performance.
- Explain the purpose of the train-test split and cross-validation.

---

## Prerequisites

No Azure subscription is required. All exercises are written analysis and classification tasks. You will need:

- Module 02 video lecture (completed).
- Module 02 reading guide (completed), including the algorithm comparison tables.

---

## Part A: Paradigm Classification (30 points)

For each scenario, write:

1. The learning paradigm: supervised learning, unsupervised learning, or reinforcement learning.
2. If supervised: the task type (regression or classification).
3. A two-sentence justification that explains your reasoning using course vocabulary.

### Scenario 1

A logistics company has 200,000 historical delivery records. Each record shows the origin city, destination city, package weight, carrier, and the actual delivery time in hours. The company wants to build a model that predicts delivery time for new shipments before they are sent.

**Learning paradigm:** _______________
**Task type (if supervised):** _______________
**Justification:** _______________

### Scenario 2

An insurance company wants to understand whether its policyholders naturally cluster into distinct risk profiles. The company has no predefined risk categories and no labeled data — it wants the data itself to reveal any groupings that exist.

**Learning paradigm:** _______________
**Task type (if supervised):** N/A
**Justification:** _______________

### Scenario 3

An online retailer has transaction logs for 500,000 customers over three years. Each transaction is labeled as either "resulted in return" or "no return." The retailer wants to build a model that predicts, at the time of purchase, whether the customer is likely to return the item.

**Learning paradigm:** _______________
**Task type (if supervised):** _______________
**Justification:** _______________

### Scenario 4

A manufacturing plant monitors vibration sensor readings on industrial equipment. The company has no historical records of which readings preceded equipment failures — it only has sensor data from normal operations. The company wants to flag readings that deviate significantly from normal patterns.

**Learning paradigm:** _______________
**Task type (if supervised):** N/A
**Justification:** _______________

### Scenario 5

A credit card company wants to predict the total spending amount a new customer will make in their first 90 days, based on their credit score, income, age, employment type, and zip code.

**Learning paradigm:** _______________
**Task type (if supervised):** _______________
**Justification:** _______________

### Scenario 6

A music streaming platform wants to sort its 80 million songs into thematic groups to power a new radio feature. The company does not have predefined genre categories and wants the groupings to emerge from audio feature data — tempo, key, energy, danceability — without human labeling.

**Learning paradigm:** _______________
**Task type (if supervised):** N/A
**Justification:** _______________

---

## Part B: Algorithm Selection (25 points)

For each scenario, recommend one specific algorithm from the following list and explain your reasoning in two to three sentences. Each algorithm may be used at most twice.

**Algorithm list:** Linear Regression, Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, K-means Clustering, PCA

### Scenario 7

A hospital needs to classify patient records as high-risk or low-risk for a rare cardiac event. The dataset has 40,000 records and 12 clinical features. The clinical team must be able to explain the model's decision logic to regulators. Accuracy and interpretability are both required.

**Recommended algorithm:** _______________
**Justification:** _______________

### Scenario 8

A retail chain wants to predict the weekly sales volume for each of its 500 store locations. The company has 5 years of weekly sales data per store along with promotional calendar data, local economic indicators, and weather data. Interpretability is not critical — accuracy is the top priority.

**Recommended algorithm:** _______________
**Justification:** _______________

### Scenario 9

An e-commerce platform has customer feature data with 300 behavioral variables per user. Analysts want to visualize the customer population in two dimensions to identify natural groups before building any predictive model. The goal is exploration, not prediction.

**Recommended algorithm:** _______________
**Justification:** _______________

### Scenario 10

A telecommunications company wants to predict whether a customer will cancel their subscription in the next 30 days (churn = yes or no). The dataset has 200,000 records and 25 features including usage patterns, billing history, and customer service contacts. The company is willing to sacrifice some interpretability for the highest possible recall on the positive (churn) class.

**Recommended algorithm:** _______________
**Justification:** _______________

### Scenario 11

A healthcare analytics team has collected patient health records with 500 features per patient and wants to reduce the dataset to its most informative dimensions before running a clustering analysis. Computation time is a concern.

**Recommended algorithm:** _______________
**Justification:** _______________

---

## Part C: Model Evaluation Interpretation (25 points)

Answer each question in complete sentences.

### Question 12

A regression model predicts apartment rental prices. On the training set it achieves an R-squared of 0.96. On the test set it achieves an R-squared of 0.61. What does this pattern indicate? What is the condition called, and what are two remedies?

**Your answer:** _______________

### Question 13

A binary classification model is trained to detect defective products on a manufacturing line. Out of 1,000 test examples, 900 are non-defective and 100 are defective. The model predicts "non-defective" for every single example. What accuracy does this model achieve? Why is accuracy a misleading metric here? Which metric should the team use instead and why?

**Your answer:** _______________

### Question 14

A data scientist is comparing two models for a medical diagnosis task. Model A has precision of 0.92 and recall of 0.61. Model B has precision of 0.73 and recall of 0.89. In this context, failing to detect a true positive (a missed diagnosis) is far more costly than a false alarm. Which model should the team prefer and why?

**Your answer:** _______________

### Question 15

What is the difference between a validation set and a test set? Why is it problematic to tune hyperparameters using the test set?

**Your answer:** _______________

---

## Part D: Azure ML Scenario Matching (20 points)

For each scenario, identify the Azure ML task type and the most appropriate AutoML setting. Select from: Classification, Regression, Time Series Forecasting, or Clustering.

### Scenario 16

A telecommunications company wants to predict each customer's monthly bill amount for the next billing cycle based on usage data from the current month.

**Azure ML task type:** _______________
**Brief justification:** _______________

### Scenario 17

A marketing team wants to segment 2 million customers into groups with similar product preferences. No predefined segments exist.

**Azure ML task type:** _______________
**Brief justification:** _______________

### Scenario 18

A utility company wants to predict daily electricity demand for the next 30 days based on 3 years of historical daily demand and weather data.

**Azure ML task type:** _______________
**Brief justification:** _______________

### Scenario 19

A content moderation platform wants to automatically label user-submitted posts as one of five categories: appropriate, adult content, violence, hate speech, or misinformation.

**Azure ML task type:** _______________
**Brief justification:** _______________

---

## Answer Key and Grading Rubric

### Part A (5 points per scenario = 30 points)

**Scenario 1:** Supervised learning — Regression. Delivery time is a continuous numerical output and historical records include labeled outcomes.

**Scenario 2:** Unsupervised learning. No labels, goal is to discover natural groupings — classic clustering use case.

**Scenario 3:** Supervised learning — Classification. The label is a binary category (return / no return) and historical labels are available.

**Scenario 4:** Unsupervised learning. Only normal data available, no failure labels — anomaly detection without labeled anomalies is unsupervised.

**Scenario 5:** Supervised learning — Regression. Spending amount is a continuous output with labeled historical data.

**Scenario 6:** Unsupervised learning. No predefined categories, goal is to discover structure from audio features — clustering.

Scoring: 5 pts = correct paradigm, correct task type (if applicable), accurate two-sentence justification. 3 pts = correct paradigm, weak justification. 0 pts = incorrect paradigm.

### Part B (5 points per scenario = 25 points)

**Scenario 7:** Logistic Regression or Decision Tree. Both are interpretable binary classifiers. Decision Tree is acceptable given the regulatory interpretability requirement.

**Scenario 8:** Gradient Boosting. High accuracy on structured tabular data with many features is gradient boosting's strength. Interpretability not required.

**Scenario 9:** PCA. The goal is dimensionality reduction for visualization, not clustering or prediction.

**Scenario 10:** Gradient Boosting or Random Forest. Both maximize recall on imbalanced classes when combined with threshold tuning. High recall is the priority.

**Scenario 11:** PCA. Dimensionality reduction before clustering is a standard preprocessing pattern; PCA is the canonical algorithm.

### Part C (5-7 points per question, total 25 points allocated by instructor)

**Q12:** Overfitting. Training R2 of 0.96 vs test R2 of 0.61 indicates the model memorized training data and fails to generalize. Remedies include regularization (L1/L2), gathering more training data, or simplifying the model.

**Q13:** The model achieves 90% accuracy by predicting the majority class for every input. Accuracy is misleading because the dataset is imbalanced. The team should use recall (sensitivity) for the defective class — a model that misses all 100 defects has 0% recall despite 90% accuracy. F1-score also balances this.

**Q14:** Model B. High recall (0.89 vs 0.61) means fewer missed diagnoses. In medical diagnosis, a false negative (missed disease) is more dangerous than a false positive. Model B's lower precision means more false alarms but far fewer missed cases.

**Q15:** The validation set is used during development to tune hyperparameters and select the best model. The test set is reserved for final evaluation only. Tuning on the test set causes data leakage — the test set effectively becomes a validation set, and the final score is optimistic and does not represent true unseen performance.

### Part D (5 points per scenario = 20 points)

**Scenario 16:** Regression. Monthly bill amount is a continuous numerical output.

**Scenario 17:** Clustering. No predefined labels; goal is to discover natural customer segments.

**Scenario 18:** Time Series Forecasting. The prediction is a sequence of future values based on temporal historical data.

**Scenario 19:** Classification (multi-class). The output is one of five discrete category labels.

---

## Deliverable

Submit a single document (PDF or Word) containing your answers to all 19 items. Include your name, course section, and date at the top. Upload to the Module 02 Lab Assignment in Canvas by the posted due date.

## Part 9 — Challenge Exercise

### Challenge 1: Imbalanced Classification Experiment

1. Using Python and scikit-learn, load the `breast_cancer` dataset from `sklearn.datasets`. Note the class distribution (malignant vs. benign counts).
2. Train a `LogisticRegression` classifier using the default settings. Report accuracy, precision, recall, and F1-score for the minority class using `classification_report`.
3. Now apply `class_weight='balanced'` to the `LogisticRegression` constructor. Retrain and report the same metrics. Document which metrics improved and which changed.
4. Explain in two sentences why recall for the malignant class is the most critical metric for a cancer screening tool, and which model configuration you would deploy.

### Challenge 2: Choosing K in K-Means with the Elbow Method

1. Using Python, generate a synthetic dataset with `sklearn.datasets.make_blobs(n_samples=300, centers=5, random_state=42)`.
2. Train K-means models for K values from 1 to 10. For each K, record the inertia (within-cluster sum of squares, accessible via `kmeans.inertia_`).
3. Plot inertia vs. K using matplotlib. Identify the "elbow" point where adding more clusters yields diminishing reduction in inertia.
4. Compare your visual elbow K to the true number of blobs (5). Calculate the silhouette score for K=3, K=5, and K=7 using `sklearn.metrics.silhouette_score` and report which K scores highest.

### Reflection Questions

1. In Challenge 1, what practical harm could result from deploying the default (unbalanced) model in a real cancer screening program? Which responsible AI principle does this relate to?
2. In Challenge 2, if you did not know the true number of clusters in a real business dataset, what combination of the elbow method and silhouette score would you use to justify your choice of K to a non-technical stakeholder?

# Lab Activity: Module 13 — Data Preparation and Feature Engineering

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe machine learning concepts (20-25%)

---

## Lab Overview

In this lab you will analyze raw datasets for quality problems, select and justify missing value strategies, apply feature engineering transformations, identify data leakage, and evaluate train-test split decisions. No Azure subscription or Python environment is required. All work is scenario-based analysis using the concepts from the reading guide.

### Learning Objectives

By completing this lab you will be able to:

- Identify data quality problems in raw datasets and recommend corrections
- Select appropriate missing value strategies for different field types and contexts
- Apply one-hot encoding and label encoding correctly to categorical variables
- Identify when normalization is required vs unnecessary for a given model type
- Recognize data leakage and explain its production consequences
- Design a valid train-test split strategy for a given scenario

### Time Estimate

Approximately 90–110 minutes.

---

## Part A: Data Quality Audit (20 points)

The table below shows a sample from a raw dataset being prepared to train a customer churn prediction model. Each row is one customer. The target variable is "Churned" (Yes/No).

| CustomerID | Age | ContractType | MonthlySpend | SupportTickets | LastLoginDays | TenureMonths | Churned |
|---|---|---|---|---|---|---|---|
| 1001 | 34 | Annual | 89.50 | 2 | 5 | 18 | No |
| 1002 | null | Monthly | 45.00 | 0 | 12 | 6 | No |
| 1003 | 28 | annual | 67.25 | 1 | 3 | 11 | Yes |
| 1004 | 51 | Monthly | 112.00 | 8 | null | 42 | Yes |
| 1005 | 29 | Monthly | 45.00 | 0 | 12 | 6 | No |
| 1006 | 29 | Monthly | 45.00 | 0 | 12 | 6 | No |
| 1007 | 67 | Annual | 89.50 | 2 | 5 | 18 | No |
| 1008 | 23 | Monthly | 9999.00 | 1 | 7 | 3 | No |
| 1009 | 41 | Annual | 89.50 | 14 | 2 | 24 | Yes |
| 1010 | 38 | null | 78.00 | 3 | 9 | 15 | No |

### Question A1 (4 points)

Identify all data quality problems present in this sample. For each problem, name the specific data quality dimension it violates (completeness, accuracy, representativeness, or relevance) and identify which row(s) and column(s) are affected.

### Question A2 (4 points)

For the missing "Age" value in row 1002, evaluate all three missing value strategies (deletion, imputation, indicator encoding). Which strategy do you recommend for this column, and why? Your answer must explain what information would be lost or distorted by the alternatives.

### Question A3 (4 points)

For the missing "LastLoginDays" value in row 1004, a team member suggests using the column median (12 days) as an imputed value. Evaluate this suggestion. Is there a reason the missingness itself might be predictive in a churn model? What encoding approach would preserve that signal?

### Question A4 (4 points)

Row 1008 shows a MonthlySpend of $9,999.00. The typical range in this dataset is $35–$150. The data engineering team is unsure whether this is a genuine high-value customer or a data entry error.

Describe two different actions the team could take depending on which explanation is true, and explain how each action affects the model differently.

### Question A5 (4 points)

Identify the duplicate records in this dataset. Explain what problem duplicates create during model training and describe how to resolve them.

---

## Part B: Feature Engineering (25 points)

### Encoding Categorical Variables

The following columns appear in a dataset being prepared to train a hotel booking cancellation model. For each column, specify the correct encoding method (one-hot encoding, label encoding, or no encoding needed) and justify your choice.

### Booking Source Encoding (5 points)

Column: "BookingSource"

Values observed: Online, Travel Agent, Corporate, Walk-In, Phone

1. Which encoding method should be applied to this column?
2. Write out exactly what the encoded representation would look like for a record where BookingSource = "Travel Agent." Show the full set of columns that would result from the encoding.
3. Why would it be incorrect to use label encoding for this column?

### Lead Time Encoding (5 points)

Column: "CancellationRisk"

Values observed: Low, Medium, High

1. Which encoding method should be applied to this column?
2. Write out exactly what the encoded representation would look like for a record where CancellationRisk = "Medium."
3. Why is the alternative encoding method inappropriate here?

### Date Feature Engineering (5 points)

Column: "CheckInDate" (raw format: YYYY-MM-DD)

The raw date column cannot be directly used by most ML models. For a hotel cancellation prediction model, describe four specific features you would engineer from this single date column. For each derived feature, explain what pattern it might help the model capture.

### Scaling Decision (5 points)

A hotel dataset contains the following numeric features that will be used in both a Logistic Regression model and a Random Forest model:

- LeadTimeDays (range: 0 to 365)
- NumberOfGuests (range: 1 to 10)
- TotalRoomNights (range: 1 to 30)
- PreviousCancellations (range: 0 to 8)

1. Which scaling method would you apply before training the Logistic Regression model?
2. Is the same scaling required for the Random Forest model? Explain why or why not.
3. What problem would occur in the Logistic Regression model if no scaling were applied?

### Interaction Feature (5 points)

A data scientist proposes creating an interaction feature: "LeadTimeDays x IsWeekendCheckIn" (the product of the lead time and a binary flag for whether check-in is on a Saturday or Sunday).

1. What pattern would this interaction feature help the model capture that neither feature alone would express clearly?
2. Under what conditions would this interaction feature be more valuable than either of its component features individually?

---

## Part C: Data Leakage Identification (20 points)

For each scenario below, determine whether data leakage is present. If leakage exists, identify the type (target leakage, future data leakage, duplicate leakage, or preprocessing leakage), explain why it is leakage, and describe how to fix it.

### Leakage Scenario C1 (5 points)

A team is training a model to predict whether a health insurance claim will be denied. Their feature set includes: claim amount, diagnosis code, procedure code, patient age, provider type, and "claim_processing_notes" (a text field that claims adjusters fill in after reviewing the claim).

Is there data leakage? Justify your answer.

### Leakage Scenario C2 (5 points)

A team is training a model to predict employee attrition (whether an employee will leave within the next 6 months). They compute the z-score standardization for all numeric columns by calculating mean and standard deviation across the entire dataset (all 8,000 rows), then split the standardized data into 80 percent training and 20 percent test.

Is there data leakage? Justify your answer and describe the correct procedure.

### Leakage Scenario C3 (5 points)

A team is training a product recommendation model. Their training dataset contains 5 million user-product interaction records. Before splitting, they deduplicate by user ID to reduce dataset size, keeping only the most recent interaction per user. The resulting 800,000 records are split 80/20 into train and test sets.

Is there data leakage in this pipeline? If yes, what kind and where? If no, explain why the deduplication was safe.

### Leakage Scenario C4 (5 points)

A team trains a time-series sales forecasting model. Their dataset contains weekly sales data from 2018 through 2024. They use a random 80/20 split across all weeks.

Is there data leakage? Justify your answer. What split strategy should they use instead and why?

---

## Part D: Train-Test Split Design (20 points)

### Split Design D1 (10 points)

A data science team is building a fraud detection model. The dataset contains 1,000,000 transactions. Exactly 0.8 percent of transactions are fraudulent (8,000 fraud records; 992,000 non-fraud records).

1. If the team uses a random 80/20 split, approximately how many fraud records will be in the test set? Show your arithmetic.
2. What problem might occur with a simple random split on this dataset?
3. What split strategy should be used to ensure both train and test sets have the correct proportion of fraud records? Name the technique.
4. What additional concern does the team face during model evaluation with this class distribution, and what metric should they prioritize over raw accuracy?

### Split Design D2 (10 points)

A team is building a model to predict customer lifetime value (CLV) for a subscription service. They have customer data from January 2020 through December 2024. The model will be used in production to score new customers acquired starting in January 2025.

1. Explain why a random split is inappropriate for this dataset.
2. Describe the correct split strategy, including specifically how to define the training, validation, and test periods.
3. Identify one feature that might appear legitimate but would constitute leakage in this time-series context. Explain why.
4. The team wants to use k-fold cross-validation. Is standard k-fold appropriate for this dataset? If not, what variant is appropriate?

---

## Part E: Azure ML Data Preparation (15 points)

### Question E1 (5 points)

A data pipeline in Azure ML Designer must handle the following transformations before model training:

- Impute missing values in the "Income" column with the column median
- Remove duplicate rows
- Normalize all numeric features to 0–1 range
- Split data 70/15/15 into train, validation, and test sets

List the Azure ML Designer components you would use for each step in the order they should appear in the pipeline. For the split step, explain how you would implement a two-stage split to create three partitions using the available component.

### Question E2 (5 points)

A model is trained in Azure ML Designer with a normalization step applied to the training data. The normalization uses training set statistics (min and max values). The trained model is then deployed as a real-time endpoint.

When a new scoring request arrives at the endpoint with raw (unnormalized) feature values, what must happen to those values before they reach the model? Where in the Azure ML pipeline should this preprocessing be placed to ensure it happens automatically at inference time?

### Question E3 (5 points)

A team registers their training dataset as a versioned Data Asset in Azure ML. Three months later, a new version of the training data is available with additional records. The team trains a new model version on the new data.

1. Why is versioning the dataset (rather than overwriting it) important for the organization?
2. What specific problem does dataset versioning solve that would occur if the same dataset file were simply replaced with updated data?

---

## Answer Key and Grading Rubric

### Part A Rubric (20 points)

**A1:** Problems present: (1) Completeness — missing Age (row 1002, Age column) and missing LastLoginDays (row 1004, LastLoginDays column) and missing ContractType (row 1010, ContractType column). (2) Accuracy / format inconsistency — row 1003 ContractType = "annual" (lowercase) vs "Annual" in other rows — inconsistent format. (3) Relevance — rows 1005 and 1006 are duplicate records (CustomerID 1005 and 1006 have identical Age/ContractType/MonthlySpend/SupportTickets/LastLoginDays/TenureMonths/Churned — these are duplicate observations, not just same values). (4) Potential accuracy issue — row 1008 MonthlySpend = $9,999 is a likely outlier requiring investigation. Award 1 point per correctly identified and classified problem (up to 4 problems).

**A2:** Deletion wastes a record when the dataset may be small; imputation with mean/median is reasonable since only one record is missing and age is a useful predictor; indicator encoding is an option if missingness in age might correlate with churn. Recommended: mean or median imputation, since age is a continuous numeric field, missing rate is low, and random missingness is the most likely explanation. Full credit requires recommending imputation with justification for why deletion loses information and why indicator encoding adds unnecessary complexity for a single missing value.

**A3:** Median imputation is not recommended here. A customer who has not logged in recently is plausibly more likely to churn — the fact that LastLoginDays is missing may itself be informative (perhaps the system only logs recent activity, meaning null = never logged in recently). Indicator encoding (add IsLastLoginMissing = 1 flag, set LastLoginDays to median placeholder) preserves the missingness signal. Award full credit for identifying that missingness may be non-random in a churn context and recommending indicator encoding.

**A4:** If genuine high-value customer: keep the record as-is or verify against billing records. The model should learn from high-spend customers. If data entry error (likely meant $99.00): correct the value to the correct amount. The difference in model impact: keeping a genuine outlier allows the model to learn high-spend behavior; keeping an erroneous value teaches the model a false pattern (that a "normal" customer might have $9,999 spend). Capping (winsorizing) at a threshold (e.g., 99th percentile) is a middle option. Award 2 points per scenario (4 total).

**A5:** Rows 1005 and 1006 are duplicates (identical values across all columns except CustomerID). Duplicates in training data cause the model to effectively see those examples multiple times, weighting those patterns more heavily than warranted and potentially overfitting to them. Resolution: remove one of the duplicate rows (keep CustomerID 1005 or 1006, not both).

### Part B Rubric (25 points)

**Booking Source:** One-hot encoding (nominal, no order). Travel Agent encoding: IsOnline=0, IsTravelAgent=1, IsCorporate=0, IsWalkIn=0, IsPhone=0. Label encoding is wrong because it implies a numeric ordering (Online=1 < TravelAgent=2 < Corporate=3) that does not exist.

**CancellationRisk:** Label encoding (Low=1, Medium=2, High=3) because this is ordinal. CancellationRisk=Medium → 2. One-hot encoding is technically valid but discards the ordinal information.

**CheckInDate:** Any four of: DayOfWeek (0–6) to capture weekday vs weekend patterns; Month (1–12) for seasonal booking patterns; IsHoliday (binary) for peak demand periods; DaysUntilHoliday for proximity effects; Year for long-term trend; WeekOfYear for micro-seasonal patterns. Each must include the pattern it captures.

**Scaling:** Apply min-max normalization (or z-score standardization) to Logistic Regression. No scaling required for Random Forest — tree-based models split on thresholds and are scale-invariant. Without scaling in Logistic Regression: LeadTimeDays (0–365) would dominate gradient updates compared to NumberOfGuests (1–10), causing slow convergence and potentially poor parameter estimates.

**Interaction Feature:** The product captures the combined effect of planning far ahead for a weekend stay — a pattern potentially associated with leisure travelers who are less likely to cancel. Neither feature alone identifies this segment. Most valuable when the model cannot discover the interaction pattern from component features alone (linear models); less critical for tree models that can approximate interactions through splits.

### Part C Rubric (20 points)

**C1:** Leakage present — target leakage. Processing notes are written by adjusters after reviewing the claim — after the denial decision is made. These notes would not exist at prediction time for a new claim. Fix: remove claim_processing_notes from the feature set.

**C2:** Leakage present — preprocessing leakage. Computing z-score statistics (mean, std) across the full 8,000-row dataset before splitting means test set statistics contaminate the training normalization. Fix: compute mean and std on training set only; apply those training statistics to normalize both train and test sets.

**C3:** No leakage. Deduplication to the most recent interaction per user before splitting is safe because it does not use future information — it only keeps existing records. If records were split first and then the most recent interaction selected per user across splits, that could create leakage. The pipeline as described is clean.

**C4:** Leakage present — future data leakage. A random split allows weeks from 2023 to appear in the training set while weeks from 2019 appear in the test set. The model "knows" the future. Fix: time-based split — train on weeks through 2022, validate on 2023, test on 2024. This mimics production conditions where the model is always predicting future data it has not seen.

### Part D Rubric (20 points)

**D1:** (1) 0.8% x 200,000 = 1,600 fraud records in test set. (2) Random split may create test sets where fraud is even rarer, making evaluation unstable. (3) Stratified split — preserves class proportion in each partition. (4) With only 0.8% fraud, a model that predicts "not fraud" on every transaction achieves 99.2% accuracy. Use precision, recall, F1-score, or area under the ROC/PR curve as evaluation metrics.

**D2:** (1) Random split allows future months to train the model and past months to test it — the model learns from data after the test period, which is impossible in production. (2) Correct split: train on 2020–2022, validate on 2023, test on 2024 (or similar time-based partition). (3) A leakage feature: "TotalPaymentsToDate" as of the scoring date — if this is computed from the full record history including events after the training cutoff, it leaks future payment behavior. (4) Standard k-fold is inappropriate because folds will mix time periods. Use time-series cross-validation (rolling window or expanding window) where each fold trains on all data up to a point and tests on the immediately following period.

### Part E Rubric (15 points)

**E1:** Order of components: (1) Clean Missing Data (impute Income with median), (2) Remove Duplicate Rows, (3) Normalize Data (min-max), (4) Split Data (80/20 to separate test set), then (5) a second Split Data on the 80% output (approximately 87.5/12.5 to produce 70% train and 12.5% validation from the 80%). The two-stage approach is necessary because the Designer's Split Data component produces exactly two outputs.

**E2:** The raw feature values must be normalized using the same min and max values that were computed from the training set before the endpoint can score them. This normalization must be part of the inference pipeline — the deployed model should be an Azure ML pipeline that includes the Normalize Data component wired ahead of the model scoring step, not a standalone model that receives pre-normalized input. If preprocessing is outside the deployed pipeline, the caller must know and apply the training statistics, which is fragile and error-prone.

**E3:** (1) Dataset versioning allows the organization to reproduce any model training run exactly — if a model must be audited, retrained, or compared against a previous version, the exact dataset used for each run is traceable. (2) Without versioning, replacing the dataset file means prior training runs can no longer be reproduced — the data that produced a deployed model no longer exists in its original form. Regulatory compliance, model audits, and debugging production incidents all depend on being able to re-run training on the original data.

---

## Submission Requirements

Submit a single document to the course LMS by the posted deadline containing:

- Part A: Answers to all five data quality questions
- Part B: Encoding, scaling, and feature engineering answers for all five sections
- Part C: Leakage determination and justification for all four scenarios
- Part D: Split design answers for both scenarios
- Part E: Azure ML pipeline and versioning answers

---

## Grading Rubric Summary

| Part | Points | Criteria |
|------|--------|----------|
| A — Data Quality Audit | 20 | Problems correctly identified and classified by dimension; strategy choices justified |
| B — Feature Engineering | 25 | Correct encoding methods with justification; derived features explained; scaling rationale accurate |
| C — Data Leakage | 20 | Leakage presence correctly determined; type identified; fix described |
| D — Train-Test Split | 20 | Arithmetic shown; split strategy correct and justified; metric choice appropriate |
| E — Azure ML | 15 | Component order correct; inference pipeline placement explained; versioning rationale accurate |
| **Total** | **100** | |

---

## Part 9 — Challenge Exercise

### Challenge 1: End-to-End Data Preparation Pipeline with scikit-learn

1. Load the Titanic dataset from `seaborn.load_dataset('titanic')` or download it from Kaggle. Identify all columns, their data types, and missing value counts. Document which quality dimensions (completeness, accuracy, consistency, relevance) are affected by the problems you find.
2. Build a scikit-learn `Pipeline` that handles: (a) imputing `age` with median, (b) imputing `embarked` with the most frequent value, (c) one-hot encoding `sex` and `embarked`, (d) dropping irrelevant columns (`name`, `ticket`, `cabin`), and (e) scaling all numeric features with `StandardScaler`. Apply the pipeline to the full dataset and verify the output shape and feature names.
3. Perform a stratified 70/15/15 train/validation/test split preserving the `survived` class proportion. Verify the class proportion in each split. Train a `LogisticRegression` on the train set using the pipeline and report accuracy on the validation and test sets.
4. Add one engineered feature of your own design (e.g., `FamilySize = sibsp + parch + 1`, or `IsAlone` binary flag). Re-run the pipeline and compare validation accuracy with and without the engineered feature. Report your finding in 2–3 sentences.

### Challenge 2: Data Leakage Detection and Time-Series Split

1. Create a synthetic dataset with 1,000 rows and the following columns: `transaction_date` (daily dates spanning 2020-01-01 to 2022-09-26), `amount` (random float 10–500), `merchant_category` (random choice of 5 categories), `is_fraud` (1 for 5 percent of rows, random). Add a leaky feature: `fraud_flag_next_day` — a binary column that equals 1 if the next day's transaction by the same simulated user was fraud. This feature would not exist at prediction time for new transactions.
2. Train a `RandomForestClassifier` twice: (a) with the leaky feature included, (b) with the leaky feature excluded. Use a random 80/20 split for both. Compare the AUC-ROC scores and explain the magnitude of the difference.
3. For the non-leaky model, switch from a random split to a time-based split: train on 2020–2021, test on 2022. Compare the AUC-ROC on the time-based test set to the random-split test score. Explain in 2–3 sentences why the scores differ and which split better simulates production conditions.
4. Add stratified k-fold cross-validation (5 folds) to the non-leaky random-split model and a time-series cross-validation (`TimeSeriesSplit`, 5 splits) to the time-based model. Compare the mean and standard deviation of AUC-ROC across folds for each approach. Write a 2-sentence recommendation about which evaluation method should be used for this fraud detection use case.

### Reflection Questions

1. After completing Challenge 1, explain why fitting preprocessing transformers (such as `StandardScaler` or `OneHotEncoder`) on the full dataset before splitting into train and test sets constitutes data leakage. What specific information from the test set contaminates the training process, and how would this cause the model's test performance to be an overestimate of true production performance?

2. Based on Challenge 2, explain why the dummy variable trap (dropping one column from one-hot encoded features) matters for logistic regression but is typically irrelevant for tree-based models like Random Forest. What property of each model type causes this difference?

---

End of Lab — Module 13

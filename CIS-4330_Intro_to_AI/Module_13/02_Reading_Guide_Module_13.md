# Reading Guide: Module 13 — Data Preparation and Feature Engineering

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe machine learning concepts (20-25%)

---

## Overview

This reading guide covers data quality dimensions, data cleaning techniques, feature engineering methods, train-test splitting, data leakage, and Azure ML data preparation tools. These topics appear in AI-900 questions about machine learning pipelines and the conditions required for successful model training. Estimated reading time: 50–65 minutes.

---

## Section 1: Core Vocabulary

**Data preparation** — The process of cleaning, transforming, and structuring raw data into a form suitable for model training. Typically 60–80 percent of total ML project time.

**Feature** — A single measurable input variable used by a model to make predictions. Also called an attribute or predictor variable.

**Feature engineering** — The process of transforming raw data columns into features that express patterns more clearly for a model to learn from.

**Missing value** — A data record where a field contains no value. Strategies: deletion, imputation, or indicator encoding.

**Imputation** — Filling in missing values with a calculated substitute such as the column mean, median, mode, or a forward-filled value.

**Outlier** — A data value that falls far outside the typical range of the feature. May be a genuine rare event, a measurement error, or a data entry mistake.

**Normalization** — Scaling numeric features to a common range (commonly 0 to 1) using min-max scaling: (value minus min) divided by (max minus min).

**Standardization** — Scaling numeric features to have mean zero and standard deviation one using z-score scaling: (value minus mean) divided by standard deviation.

**One-hot encoding** — Creating a separate binary (0/1) column for each category value in a categorical variable. Appropriate for nominal categories with no natural order.

**Label encoding** — Assigning an integer to each category value (e.g., Low=1, Medium=2, High=3). Appropriate for ordinal categories with a natural order.

**Train-test split** — Dividing a labeled dataset into a training portion (used to fit the model) and a test portion (held out for final evaluation).

**Data leakage** — The inadvertent inclusion of information in training data that would not be available at prediction time in production, causing artificially high training performance that does not generalize.

**Cross-validation** — A technique that repeatedly splits the training data into different folds, trains and evaluates on each fold, and averages results to produce a more robust performance estimate.

**Data asset** — An Azure ML concept for registering and versioning a dataset so that training runs are reproducible and traceable to the exact input data used.

**Binning** — Converting a continuous numeric feature into discrete category ranges. Example: converting age values into age bands (18–25, 26–35, etc.).

---

## Section 2: Comparison Tables

### Table 1: Data Quality Dimensions

| Dimension | Definition | ML Impact if Violated | Detection Method |
|---|---|---|---|
| Completeness | All required values are present | Missing values force deletion or imputation; both reduce accuracy | Null count per column |
| Accuracy | Values correctly reflect real-world state | Model learns from incorrect signal; errors in labels corrupt all learning | Manual audit; label agreement checks |
| Representativeness | Training data reflects production distribution | Model performs poorly on segments not seen during training | Distribution comparison: train vs production |
| Relevance | Features are predictive and appropriate | Noise features reduce model clarity; leaked features corrupt evaluation | Feature importance analysis; domain review |

### Table 2: Missing Value Strategies

| Strategy | Method | Best When | Risk |
|---|---|---|---|
| Deletion | Remove records with missing values | Missing values are rare (under 5%); missingness is random | Loses data; may introduce bias if missingness is not random |
| Mean/median imputation | Replace with column mean or median | Numeric features; missingness is random | Distorts feature distribution; reduces variance |
| Mode imputation | Replace with most frequent value | Categorical features | May over-represent one category |
| Forward-fill | Carry the last known value forward | Time series data with sequential records | Inappropriate for non-time-ordered data |
| Indicator encoding | Add binary flag for "was missing"; fill original with placeholder | When missingness itself may be predictive | Adds a feature; doubles the representation of that column |

### Table 3: Feature Encoding Methods

| Method | Use Case | Example | Caution |
|---|---|---|---|
| One-hot encoding | Nominal categorical features (no order) | Color: Red, Blue, Green → IsRed, IsBlue, IsGreen | Creates many columns if cardinality is high |
| Label encoding | Ordinal categorical features (natural order) | Size: Small=1, Medium=2, Large=3 | Implies numeric relationships — inappropriate for nominal |
| Ordinal encoding | Ranked ordinal features | Survey rating: Low=1, Medium=2, High=3 | Same as label encoding for ordered categories |
| Binary encoding | High-cardinality nominal categories | ZIP codes, product IDs | Reduces columns vs one-hot but loses interpretability |

### Table 4: Scaling Methods

| Method | Formula | When to Use | Not Required For |
|---|---|---|---|
| Min-max normalization | (x - min) / (max - min) → range 0 to 1 | Neural networks; k-NN; SVM | Tree-based models (random forest, gradient boosting) |
| Z-score standardization | (x - mean) / std dev → mean 0, std 1 | Linear models; logistic regression; PCA | Tree-based models |
| No scaling | Use raw values | Tree-based models | When features are already comparable scale |

### Table 5: Train-Test Split Strategies

| Strategy | Description | Best For |
|---|---|---|
| Random split | Randomly assign records to train, validation, test | Non-time-ordered data with large sample size |
| Stratified split | Maintain class distribution proportions in each split | Imbalanced datasets where one class is rare |
| Time-based split | Train on earlier dates; test on later dates | Time series and forecasting models |
| K-fold cross-validation | Rotate through k folds; average k evaluation scores | Small datasets where every record is valuable |

### Table 6: Data Leakage Examples

| Leakage Type | Example | Why It Is Leakage |
|---|---|---|
| Target leakage | Including "loan_default_date" in a loan default prediction model | This field is only populated after the outcome occurs |
| Future data leakage | Training churn model with data that includes activity from after the churn event date | Model would not have access to that future activity at prediction time |
| Duplicate leakage | Same customer appears in both train and test splits | Model has already "seen" the test customer |
| Preprocessing leakage | Normalizing all data before splitting; using test set statistics for scaling | Test set statistics contaminate training-time calculations |

---

## Section 3: Feature Engineering Patterns

### Deriving Features from Dates and Timestamps

Raw date columns rarely express the signal a model needs directly. The following derived features are commonly useful:

- Day of week (0–6)
- Hour of day (0–23)
- Month of year (1–12)
- Is weekday / is weekend (binary)
- Is holiday (binary, requires calendar lookup)
- Days since last event (numeric)
- Days until deadline (numeric)

### Deriving Features from Text

When raw text is not the primary input but a text field exists alongside structured data:

- Text length in characters or words
- Presence of specific keywords (binary flags)
- Sentiment score (from Azure AI Language)
- Named entity count

### Interaction Features

Interaction features capture the combined effect of two features that are more predictive together than separately:

- Example: "hour_of_day" and "day_of_week" independently predict purchase likelihood weakly. "hour_of_day x day_of_week" as a combined feature captures "Friday evening" and "Monday morning" patterns more directly.

---

## Section 4: AI-900 Exam Tips

1. Data preparation consumes the majority of ML project time. This is not a sign of a failing project — it is normal. AI-900 may ask about the relative time investment across pipeline phases.

2. Missing value strategies have trade-offs. Deletion is simple but loses data. Imputation preserves records but introduces assumptions. When a scenario describes choosing between these, match the strategy to the scenario conditions (volume of missingness, whether missingness is random).

3. One-hot encoding is for nominal categories (no order); label encoding is for ordinal categories (ranked order). Applying label encoding to nominal categories implies false numerical relationships between categories.

4. Normalization and scaling are not required for tree-based models (random forest, gradient boosting, decision tree). They are required for models that use distance calculations or gradient descent (logistic regression, neural networks, k-NN, SVM). AI-900 scenarios may ask which preprocessing step is unnecessary for a given model type.

5. Data leakage produces a model that appears highly accurate during training and evaluation but performs poorly in production. If a scenario describes this gap between development performance and production performance, the answer likely involves data leakage.

6. Train-test split is mandatory for valid model evaluation. Evaluating a model on its own training data measures memorization, not generalization. AI-900 knows the purpose of the test set: to estimate real-world performance on unseen data.

7. Azure ML data assets provide versioning for datasets. Versioned assets ensure that model training is reproducible — you can re-run a training job months later using the exact same data version.

8. Preprocessing must be part of the deployed pipeline. If you normalize training data with statistics computed from training, the same normalization (using the training statistics, not fresh test statistics) must be applied to scoring data at inference time. This is a common source of preprocessing leakage if done incorrectly.

---

## Section 5: Required Reading

**Microsoft Learn — Explore and analyze data with Python:**
learn.microsoft.com/en-us/training/paths/explore-data-science-tools-in-azure/

**Microsoft Learn — Prepare data for machine learning:**
learn.microsoft.com/en-us/training/modules/introduction-to-data-for-machine-learning/

---

## Section 6: Study Checklist

- [ ] Name the four data quality dimensions and explain how each affects model performance.
- [ ] Describe three strategies for handling missing values and when to use each.
- [ ] Explain the difference between one-hot encoding and label encoding with examples.
- [ ] Explain when normalization is required and when it is not.
- [ ] Describe data leakage using a concrete example and explain how it causes production failure.
- [ ] Explain the purpose of the train-test split and why evaluation on training data is invalid.
- [ ] Describe two derived features you could engineer from a raw date column.
- [ ] Explain what a versioned data asset is in Azure ML and why it supports reproducibility.
- [ ] Complete the Module 13 quiz.
- [ ] Complete the Module 13 lab.
- [ ] Post initial discussion by Wednesday 11:59 PM and respond to two peers by Sunday 11:59 PM.

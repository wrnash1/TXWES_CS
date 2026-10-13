# Lab: Module 14 — Machine Learning for Data Analysts

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Lab Overview

In this lab you will build a complete binary classification pipeline using scikit-learn. You will load a cleaned dataset, engineer features, split data correctly to avoid leakage, train two classifiers, evaluate them on the test set, and interpret the results. Each step mirrors the workflow used by data analysts in production ML projects.

**Estimated time:** 90–105 minutes

**Tools required:** Python 3.10+, JupyterLab or VS Code with Jupyter extension, pandas, numpy, scikit-learn, matplotlib, seaborn

**Dataset:** `customer_churn_module14.csv` — download from the course LMS (3,500 rows, 12 columns, binary target: `churned`)

---

### Learning Objectives

By completing this lab you will be able to:

* Perform feature engineering including one-hot encoding, scaling, and date decomposition
* Split data correctly using stratify to preserve class balance
* Train a logistic regression classifier and a random forest classifier using scikit-learn
* Evaluate models using accuracy, precision, recall, F1 score, and confusion matrix
* Identify which model overfits by comparing training and test accuracy
* Interpret a feature importance chart from a random forest

---

### Dataset Schema

| Column | Type | Description |
|---|---|---|
| customer_id | int | Unique customer identifier |
| signup_date | str | Date customer signed up (YYYY-MM-DD) |
| region | str | Geographic region (North, South, East, West) |
| plan_type | str | Subscription plan (Basic, Standard, Premium) |
| monthly_charges | float | Monthly bill amount in USD |
| tenure_months | int | Months since signup |
| support_tickets | int | Total support tickets opened |
| avg_session_minutes | float | Average session duration in minutes |
| login_frequency | int | Logins in the last 30 days |
| has_addon | int | Binary flag: 1 = has add-on product |
| contract_type | str | Month-to-month, One year, Two year |
| churned | int | Target: 1 = churned, 0 = retained |

---

### Part 1: Setup and Exploration (15 minutes)

#### Step 1.1 — Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)

pd.set_option('display.max_columns', None)
sns.set_theme(style='whitegrid')
print("Ready.")
```

#### Step 1.2 — Load and Inspect

```python
df = pd.read_csv('customer_churn_module14.csv')
print(f"Shape: {df.shape}")
print(df.dtypes)
print(df.isnull().sum())
df.head()
```

#### Step 1.3 — Class Balance Check

```python
churn_rate = df['churned'].value_counts(normalize=True)
print(churn_rate)
sns.countplot(data=df, x='churned')
plt.title('Target Class Distribution')
plt.show()
```

**Checkpoint question 1:** What is the churn rate in this dataset? Is the dataset balanced or imbalanced?

---

### Part 2: Feature Engineering (25 minutes)

#### Step 2.1 — Date Decomposition

Convert `signup_date` to datetime and extract features:

```python
df['signup_date'] = pd.to_datetime(df['signup_date'])
df['signup_year'] = df['signup_date'].dt.year
df['signup_month'] = df['signup_date'].dt.month
df = df.drop(columns=['signup_date', 'customer_id'])
```

#### Step 2.2 — One-Hot Encode Categorical Columns

```python
categorical_cols = ['region', 'plan_type', 'contract_type']
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
print(f"Columns after encoding: {df_encoded.shape[1]}")
df_encoded.head()
```

**Checkpoint question 2:** How many columns does the dataset have after one-hot encoding? List which new columns were created.

#### Step 2.3 — Separate Features and Target

```python
X = df_encoded.drop(columns=['churned'])
y = df_encoded['churned']
print(f"Features: {X.shape}")
print(f"Target: {y.value_counts().to_dict()}")
```

---

### Part 3: Train/Test Split and Scaling (10 minutes)

#### Step 3.1 — Split the Data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")
print(f"Train churn rate: {y_train.mean():.3f}")
print(f"Test churn rate:  {y_test.mean():.3f}")
```

**Checkpoint question 3:** Why is `stratify=y` important here? What would happen to the churn rate in the test set without it?

#### Step 3.2 — Scale Numeric Features

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

**Checkpoint question 4:** Why do we call `fit_transform` on training data but only `transform` on test data?

---

### Part 4: Train and Evaluate Two Models (30 minutes)

#### Step 4.1 — Logistic Regression

```python
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train_scaled, y_train)

lr_train_acc = accuracy_score(y_train, lr.predict(X_train_scaled))
lr_test_acc  = accuracy_score(y_test,  lr.predict(X_test_scaled))

print(f"LR Train Accuracy: {lr_train_acc:.4f}")
print(f"LR Test  Accuracy: {lr_test_acc:.4f}")
print(classification_report(y_test, lr.predict(X_test_scaled)))
```

#### Step 4.2 — Random Forest

```python
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_scaled, y_train)

rf_train_acc = accuracy_score(y_train, rf.predict(X_train_scaled))
rf_test_acc  = accuracy_score(y_test,  rf.predict(X_test_scaled))

print(f"RF Train Accuracy: {rf_train_acc:.4f}")
print(f"RF Test  Accuracy: {rf_test_acc:.4f}")
print(classification_report(y_test, rf.predict(X_test_scaled)))
```

**Checkpoint question 5:** Compare training accuracy to test accuracy for both models. Which model shows signs of overfitting? How can you tell?

#### Step 4.3 — Confusion Matrices

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

for ax, model, name in zip(
    axes,
    [lr, rf],
    ['Logistic Regression', 'Random Forest']
):
    cm = confusion_matrix(y_test, model.predict(X_test_scaled))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_title(f'{name} — Confusion Matrix')
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')

plt.tight_layout()
plt.savefig('confusion_matrices.png', dpi=150)
plt.show()
```

**Checkpoint question 6:** Looking at the confusion matrices, which model produces fewer false negatives (customers who churned but were predicted as retained)? Why does this matter for a business trying to reduce churn?

---

### Part 5: Feature Importance (10 minutes)

#### Step 5.1 — Plot Top 15 Features

```python
importances = pd.Series(
    rf.feature_importances_,
    index=X.columns
).sort_values(ascending=False).head(15)

fig, ax = plt.subplots(figsize=(9, 6))
importances.plot(kind='barh', ax=ax, color='steelblue')
ax.set_title('Random Forest — Top 15 Feature Importances')
ax.set_xlabel('Importance Score')
ax.invert_yaxis()
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=150)
plt.show()
```

**Checkpoint question 7:** What are the three most important features according to the random forest? Does this make intuitive business sense for predicting churn?

---

### Part 6: Summary Reflection (5 minutes)

Add a markdown cell answering these questions in 3–5 sentences total:

* Which model would you recommend deploying and why?
* What is one additional feature you could engineer from the existing columns that might improve model performance?
* What is the biggest limitation of this analysis that you would want to address before using the model in production?

---

### Submission Instructions

Export your completed notebook as both `.ipynb` and PDF. Submit both files to the course LMS by the due date. All cells must be executed with outputs visible.

---

### Grading Rubric

| Criterion | Points |
|---|---|
| Libraries imported and data loaded with correct inspection | 10 |
| Feature engineering: encoding and date decomposition correct | 15 |
| Train/test split uses stratify with correct checkpoint explanation | 10 |
| Scaler fit on training only with correct explanation | 10 |
| Both models trained and evaluation metrics printed | 20 |
| Confusion matrix visualization rendered correctly | 15 |
| Feature importance chart rendered with correct interpretation | 10 |
| Summary reflection markdown cell with substantive answers | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: ROC Curve and Threshold Analysis

Extend the classification model evaluation from the lab by plotting a full ROC curve and analyzing the precision-recall tradeoff at multiple thresholds.

1. Using the trained logistic regression or random forest from the lab, call `model.predict_proba(X_test)[:, 1]` to get the positive class probabilities. Use `sklearn.metrics.roc_curve` to compute false positive rates, true positive rates, and thresholds across the probability range. Plot the ROC curve with FPR on the x-axis and TPR on the y-axis. Add a diagonal dashed reference line representing a random classifier. Annotate the chart with the AUC score (`roc_auc_score`). Save as `roc_curve.png`.
2. Create a precision-recall table for five threshold values (0.3, 0.4, 0.5, 0.6, 0.7) by computing precision and recall at each threshold using `precision_score` and `recall_score` with `threshold`-adjusted predictions. Print the table. Write two sentences explaining which threshold you would recommend for a churn model where retaining a churning customer is worth $200 but the outreach cost per contacted customer is $15.

```python
from sklearn.metrics import roc_curve, roc_auc_score, precision_score, recall_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

probs = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds_roc = roc_curve(y_test, probs)
auc = roc_auc_score(y_test, probs)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(fpr, tpr, color="steelblue", linewidth=2, label=f"ROC AUC = {auc:.3f}")
ax.plot([0, 1], [0, 1], color="gray", linestyle="--", linewidth=1, label="Random")
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_title("ROC Curve", fontsize=13, fontweight="bold")
ax.legend()
for sp in ["top", "right"]: ax.spines[sp].set_visible(False)
plt.tight_layout()
plt.savefig("roc_curve.png", dpi=150)
plt.show()

rows = []
for t in [0.3, 0.4, 0.5, 0.6, 0.7]:
    preds = (probs >= t).astype(int)
    rows.append({
        "threshold": t,
        "precision": round(precision_score(y_test, preds, zero_division=0), 3),
        "recall":    round(recall_score(y_test, preds, zero_division=0), 3)
    })
print(pd.DataFrame(rows).to_string(index=False))
```

### Challenge 2: Hyperparameter Tuning with GridSearchCV

Apply cross-validated grid search to optimize a decision tree or random forest and compare the tuned model to the default baseline.

1. Define a parameter grid for `DecisionTreeClassifier`: `max_depth` in [3, 5, 7, 10, None] and `min_samples_split` in [2, 5, 10]. Use `GridSearchCV` with `cv=5`, `scoring='f1'`, and `refit=True`. Fit the grid search on `X_train` / `y_train`. Print the best parameters and best cross-validated F1 score.
2. Evaluate the best estimator on `X_test` using a full classification report. Compare the tuned F1 score to the default tree's test F1 from the lab. Plot training and test F1 scores for each `max_depth` value (averaging over `min_samples_split`) as a line chart. Save as `depth_tuning.png`. Write two sentences explaining why the test F1 first increases then potentially decreases as `max_depth` grows, and what this shape tells you about the bias-variance tradeoff.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, f1_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

param_grid = {
    "max_depth":        [3, 5, 7, 10, None],
    "min_samples_split": [2, 5, 10]
}

grid = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring="f1",
    refit=True,
    n_jobs=-1
)
grid.fit(X_train, y_train)

print(f"Best params: {grid.best_params_}")
print(f"Best CV F1:  {grid.best_score_:.4f}")
print("\nTest Set Classification Report:")
print(classification_report(y_test, grid.best_estimator_.predict(X_test)))

# Plot F1 by max_depth
results = pd.DataFrame(grid.cv_results_)
depth_vals = [3, 5, 7, 10, 20]  # use 20 as proxy for None
train_f1 = results.groupby("param_max_depth")["mean_train_score"].mean() \
    if "mean_train_score" in results.columns else None
test_f1  = results.groupby("param_max_depth")["mean_test_score"].mean()

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(test_f1.index.astype(str), test_f1.values,
        marker="o", color="steelblue", linewidth=2, label="CV F1 (test fold)")
ax.set_title("Decision Tree CV F1 by max_depth", fontsize=13, fontweight="bold")
ax.set_xlabel("max_depth")
ax.set_ylabel("Mean F1 Score")
ax.legend()
for sp in ["top", "right"]: ax.spines[sp].set_visible(False)
plt.tight_layout()
plt.savefig("depth_tuning.png", dpi=150)
plt.show()
```

### Reflection Questions

1. In Challenge 1, the cost-benefit analysis for threshold selection ($200 retention value vs. $15 outreach cost) implies that a false positive (contacting a non-churner) costs $15 while a false negative (missing a churner) costs $200. Using the precision-recall table you computed, which threshold minimizes expected cost per 1,000 test customers? Show your calculation.
2. In Challenge 2, `GridSearchCV` uses 5-fold cross-validation internally. If the grid has 15 parameter combinations (5 depths × 3 min_samples values) and each fold trains a decision tree in approximately 0.02 seconds, estimate the total compute time for the grid search. Under what circumstances would you switch to `RandomizedSearchCV` instead of exhaustive `GridSearchCV`?

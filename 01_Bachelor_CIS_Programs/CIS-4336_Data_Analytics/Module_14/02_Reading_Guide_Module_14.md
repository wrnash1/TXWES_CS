# Reading Guide: Module 14 — Machine Learning for Data Analysts

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4336 &BULL; DATA ANALYTICS & BUSINESS INTELLIGENCE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Introduction

Welcome to **Module 14 — Machine Learning for Data Analysts**. This module provides the conceptual foundation in machine learning that the CompTIA Data+ exam expects and that modern analyst roles require. You will not become a machine learning engineer from one module, but you will understand what supervised and unsupervised learning are, how to prepare data for a model, what train-test split means and why it matters, and how to diagnose whether a model is overfitting or underfitting.

These concepts appear in Domain 3 of the Data+ exam and in job interviews for analyst roles at every level. The goal is fluent conceptual understanding, not code memorization.

---

### Learning Objectives

By the end of this module you will be able to:

* Distinguish supervised learning from unsupervised learning and give one example of each
* Explain the purpose and workflow of scikit-learn's fit-predict API
* Apply common feature engineering techniques: encoding, scaling, date decomposition, and log transformation
* Implement a train-test split and explain why it is required for honest model evaluation
* Compare classification and regression tasks and name one algorithm for each
* Distinguish overfitting from underfitting and describe two remedies for each

---

### Section 1: Types of Machine Learning

#### Supervised Learning

In supervised learning, every training example has a label — the correct answer the model is trying to predict. The model learns a mapping from input features to the label by minimizing prediction error across thousands of examples.

Supervised learning divides into two sub-types based on the type of label:

* **Classification** — the label is a category. Examples: spam or not spam; will churn or not; which product category does this image show?
* **Regression** — the label is a continuous number. Examples: predicted sale price; next quarter's revenue; expected customer lifetime value.

Common supervised learning algorithms:

| Algorithm | Type | Characteristics |
|---|---|---|
| Logistic regression | Classification | Fast, interpretable, works well for linearly separable data |
| Linear regression | Regression | Fast, interpretable, assumes linear relationship |
| Decision tree | Classification or regression | Interpretable, prone to overfitting |
| Random forest | Classification or regression | Reduces overfitting by averaging many trees; less interpretable |
| Gradient boosting (XGBoost) | Classification or regression | High performance, complex, requires tuning |
| K-nearest neighbors (KNN) | Classification or regression | Simple, no training phase, slow at prediction time |
| Support vector machine (SVM) | Classification | Effective in high-dimensional spaces, requires feature scaling |

#### Unsupervised Learning

In unsupervised learning, the data has no labels. The algorithm finds structure — patterns, groupings, or compressed representations — without being told what to look for.

The most common unsupervised task is **clustering**, which groups similar records together. K-means clustering assigns every record to one of k clusters by minimizing the distance from each record to its cluster center (centroid):

```python
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3, random_state=42)
model.fit(X_scaled)
labels = model.labels_
```

Other unsupervised techniques:

* **Dimensionality reduction** — compresses many features into fewer dimensions while preserving variance. Principal Component Analysis (PCA) is the most common method.
* **Anomaly detection** — identifies records significantly different from the majority; used for fraud detection and equipment failure prediction.

---

### Section 2: scikit-learn Basics

#### The Estimator API

Every scikit-learn model implements the same four methods:

* `fit(X, y)` — trains the model; for unsupervised models, `fit(X)` with no y
* `predict(X)` — returns class labels for classifiers or numeric values for regressors
* `predict_proba(X)` — returns class probabilities (classifiers only)
* `score(X, y)` — returns the default metric (accuracy for classifiers, R² for regressors)

This uniform interface means switching algorithms requires only one line change:

```python
# Compare two models by changing only this line
model = LogisticRegression()
# model = RandomForestClassifier(n_estimators=100)

model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(accuracy_score(y_test, predictions))
```

#### Evaluation Metrics

For classification:

* **Accuracy** — fraction of correct predictions. Misleading when classes are imbalanced.
* **Precision** — of all predicted positives, how many are correct? Minimizes false positives.
* **Recall** — of all actual positives, how many did the model find? Minimizes false negatives.
* **F1 score** — harmonic mean of precision and recall; useful when both matter.
* **Confusion matrix** — table showing true positives, true negatives, false positives, false negatives.

For regression:

* **MAE (Mean Absolute Error)** — average absolute difference between predicted and actual values.
* **RMSE (Root Mean Squared Error)** — square root of average squared error; penalizes large errors more.
* **R² (R-squared)** — proportion of variance in the target explained by the model; 1.0 is perfect.

---

### Section 3: Feature Engineering

#### Why Feature Engineering Matters

Raw data rarely arrives ready for a model. Dates are strings. Categories are text. Numeric columns span different scales. Feature engineering converts raw data into model-ready numeric features and is where analytical judgment creates the most leverage on model quality.

#### Encoding Categorical Variables

One-hot encoding creates a binary column for each unique category value:

```python
df_encoded = pd.get_dummies(df, columns=['Region', 'Product'], drop_first=True)
```

`drop_first=True` removes one dummy column per variable to avoid the dummy variable trap (perfect multicollinearity).

Ordinal encoding maps ordered categories to integers:

```python
from sklearn.preprocessing import OrdinalEncoder
enc = OrdinalEncoder(categories=[['Small', 'Medium', 'Large']])
df['size_encoded'] = enc.fit_transform(df[['size']])
```

#### Scaling Numeric Features

Many algorithms are sensitive to feature scale. StandardScaler (Z-score normalization):

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)   # transform only — never fit on test set
```

MinMaxScaler (0–1 range):

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

#### Date Decomposition

```python
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['day_of_week'] = df['order_date'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
```

#### Log Transformation

For right-skewed numeric variables:

```python
import numpy as np
df['log_revenue'] = np.log1p(df['revenue'])  # log1p handles zeros: log(1 + x)
```

#### Data Leakage Warning

Data leakage occurs when information from the test set influences the training process. Always split first, then fit transformers on training data only, then apply (transform only) to the test set.

---

### Section 4: Train/Test Split and Cross-Validation

#### The Train/Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y   # preserves class proportions in both sets
)
```

`stratify=y` is important for classification tasks with imbalanced classes.

#### Cross-Validation

For small datasets, a single split may give unreliable estimates. K-fold cross-validation trains and evaluates the model k times on different data partitions:

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"CV accuracy: {scores.mean():.3f} +/- {scores.std():.3f}")
```

---

### Section 5: Overfitting and Underfitting

#### The Bias-Variance Tradeoff

* **Bias** — systematic error from incorrect model assumptions. High bias produces underfitting.
* **Variance** — sensitivity to training data fluctuations. High variance produces overfitting.

#### Detecting Overfitting and Underfitting

| Symptom | Training accuracy | Test accuracy | Diagnosis |
|---|---|---|---|
| Both low | 62% | 60% | Underfitting (high bias) |
| Both high | 91% | 89% | Good fit |
| High train, low test | 98% | 63% | Overfitting (high variance) |

#### Remedies for Overfitting

* Reduce model complexity
* Get more training data
* Apply regularization (Ridge or Lasso)
* Use ensemble methods (random forest)
* Early stopping during training

#### Remedies for Underfitting

* Use a more complex algorithm
* Add more features through feature engineering
* Reduce regularization strength
* Train for more iterations

---

### Key Terms

* **supervised learning** — machine learning where training data includes labeled examples.
* **unsupervised learning** — machine learning where data has no labels; the algorithm finds structure independently.
* **classification** — a supervised task where the label is a category.
* **regression** — a supervised task where the label is a continuous number.
* **clustering** — an unsupervised task that groups similar records without predefined labels.
* **feature engineering** — transforming raw data into numeric input features suitable for a model.
* **one-hot encoding** — converting a categorical variable into binary columns, one per category.
* **scaling** — normalizing numeric features to a common range or distribution.
* **train/test split** — dividing data into training (model learns) and test (model is evaluated) sets.
* **data leakage** — when test set information contaminates the training process, producing overly optimistic results.
* **overfitting** — a model that memorizes training data including noise; performs poorly on new data.
* **underfitting** — a model too simple to capture real patterns; performs poorly on both training and new data.
* **cross-validation** — evaluating a model across multiple data partitions for a more reliable accuracy estimate.
* **bias** — systematic error from incorrect model assumptions; associated with underfitting.
* **variance** — sensitivity to training data fluctuations; associated with overfitting.
* **regularization** — a penalty on model complexity to reduce overfitting.
* **confusion matrix** — a table of true positives, true negatives, false positives, and false negatives.

---

### Review Questions

1. What is the difference between a classification task and a regression task? Give one real-world example of each.

2. A model achieves 99% accuracy on training data but only 54% on test data. What is the diagnosis, and what are two approaches to fixing it?

3. Why must you fit a StandardScaler on the training set only and never on the full dataset before splitting?

4. Explain the purpose of cross-validation. When would you use it instead of a single train-test split?

5. What is one-hot encoding and why is `drop_first=True` recommended?

---

### OER Resources

* **Google Machine Learning Crash Course** — [developers.google.com/machine-learning/crash-course](https://developers.google.com/machine-learning/crash-course)
* **scikit-learn documentation** — [scikit-learn.org/stable](https://scikit-learn.org/stable/)
* **StatQuest with Josh Starmer — ML fundamentals playlist** — [youtube.com/c/joshstarmer](https://www.youtube.com/c/joshstarmer)
* **Hands-On Machine Learning with Scikit-Learn — free preview** — Aurélien Géron, O'Reilly

---

## 9. Supplemental Resources

**1. scikit-learn — Model Evaluation and Scoring**
<https://scikit-learn.org/stable/modules/model_evaluation.html>
The official scikit-learn reference for all classification and regression metrics — precision, recall, F1, ROC AUC, confusion matrix, and cross-validation scoring. Essential for understanding when to use each metric and how to interpret the outputs that Module 14 labs produce.

**2. Google Developers ML Crash Course — Logistic Regression and Classification**
<https://developers.google.com/machine-learning/crash-course/logistic-regression/video-lecture>
A free, self-paced video module covering logistic regression, decision thresholds, precision-recall tradeoffs, and the ROC curve with interactive visualizations. Reinforces the classification concepts and evaluation framework covered in Module 14.

**3. Towards Data Science — Understanding the Bias-Variance Tradeoff**
<https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229>
A clear, visual explanation of the bias-variance tradeoff — the foundational concept behind overfitting, underfitting, and model complexity selection. Directly supports the Module 14 discussion of training vs. test accuracy gaps and when to use regularization or pruning.

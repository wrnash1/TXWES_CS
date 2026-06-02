# Lab: Module 01 - ML Fundamentals

**Course:** CIS-4345 Machine Learning and Deep Learning

**Institution:** Texas Wesleyan University

**Instructor:** Professor Nash

**Points:** 100

**Estimated Time:** 60-90 minutes

---

## Objectives

By the end of this lab you will be able to:

- Install and verify TensorFlow, scikit-learn, NumPy, pandas, and Matplotlib in a Python environment.
- Load a real dataset and inspect its shape, data types, and class distribution.
- Perform a stratified train-test split and confirm partition sizes.
- Compute basic descriptive statistics on features.
- Visualize feature distributions and a correlation matrix.
- Identify signs of class imbalance that would affect model training.

---

## Prerequisites

- A working Python 3.8+ environment (Google Colab, Anaconda, or a local venv).
- Basic Python familiarity (lists, functions, imports).
- No prior TensorFlow experience required.

---

## Setup

### Step 1: Install Required Packages

If you are using Google Colab, TensorFlow is pre-installed. Run the cell below to install any missing packages.

```python
# Run this cell once to install required packages
# In Google Colab, TensorFlow 2.x is pre-installed
# !pip install tensorflow scikit-learn pandas matplotlib seaborn

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print("TensorFlow version:", tf.__version__)
print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("scikit-learn version:", __import__('sklearn').__version__)
```

Expected output (versions may vary):

```text
TensorFlow version: 2.13.0
NumPy version: 1.24.3
Pandas version: 2.0.1
scikit-learn version: 1.3.0
```

If any import fails, install the missing package with `pip install <package-name>` and re-run.

---

## Part A: Load and Inspect a Dataset (25 points)

We will use the Wisconsin Breast Cancer dataset — a classic binary classification benchmark built into scikit-learn. It has 569 samples, 30 numerical features, and two classes (malignant = 0, benign = 1).

### Step 2: Load the Dataset

```python
# Load the Breast Cancer Wisconsin dataset
cancer = load_breast_cancer()

# Create a pandas DataFrame for easier inspection
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df['target'] = cancer.target

# Inspect the first five rows
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
```

### Step 3: Examine Class Distribution

```python
# Count samples per class
class_counts = df['target'].value_counts()
print("Class distribution:")
print(class_counts)
print("\nClass percentages:")
print(class_counts / len(df) * 100)

# Visualize class distribution
plt.figure(figsize=(6, 4))
class_counts.plot(kind='bar', color=['steelblue', 'coral'])
plt.title('Class Distribution — Breast Cancer Dataset')
plt.xlabel('Class (0=Malignant, 1=Benign)')
plt.ylabel('Sample Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```

### Step 4: Descriptive Statistics

```python
# Summary statistics for the first 10 features
print("Descriptive statistics (first 10 features):")
print(df.iloc[:, :10].describe().round(3))
```

**Lab Question A1 (5 pts):** How many samples are in each class? Is the dataset balanced?

**Lab Question A2 (5 pts):** Which feature has the largest range (max minus min)? Why does this matter for neural network training?

---

## Part B: Feature Visualization (25 points)

### Step 5: Plot Feature Distributions

```python
# Plot histograms for the first 6 features
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
axes = axes.flatten()

for i, col in enumerate(cancer.feature_names[:6]):
    axes[i].hist(df[col], bins=30, edgecolor='black', alpha=0.7, color='steelblue')
    axes[i].set_title(col, fontsize=9)
    axes[i].set_xlabel('Value')
    axes[i].set_ylabel('Count')

plt.suptitle('Feature Distributions — First 6 Features', y=1.02)
plt.tight_layout()
plt.show()
```

### Step 6: Correlation Heatmap

```python
# Compute correlation matrix for the first 10 features
corr_matrix = df.iloc[:, :10].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    vmin=-1,
    vmax=1,
    square=True
)
plt.title('Feature Correlation Matrix — First 10 Features')
plt.tight_layout()
plt.show()
```

**Lab Question B1 (5 pts):** Which two features are most strongly correlated with each other? What does high feature correlation imply for model training?

**Lab Question B2 (5 pts):** Do any features appear to follow a normal (bell-curve) distribution? Why might normality matter for some ML algorithms but not for neural networks?

---

## Part C: Train-Test Split (25 points)

### Step 7: Perform the Split

```python
# Separate features from labels
X = cancer.data      # shape (569, 30)
y = cancer.target    # shape (569,)

print("Feature matrix shape:", X.shape)
print("Label vector shape:", y.shape)
print("Label values:", np.unique(y))

# Perform a stratified 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y          # preserves class proportions in both splits
)

print("\nTraining set size:", X_train.shape)
print("Test set size:", X_test.shape)
print("\nTraining class distribution:", np.bincount(y_train))
print("Test class distribution:    ", np.bincount(y_test))
```

### Step 8: Verify Stratification

```python
# Confirm that class proportions are preserved
train_pct = np.bincount(y_train) / len(y_train) * 100
test_pct  = np.bincount(y_test)  / len(y_test)  * 100

print("Training class percentages:  Malignant={:.1f}%  Benign={:.1f}%".format(
    train_pct[0], train_pct[1]))
print("Test class percentages:      Malignant={:.1f}%  Benign={:.1f}%".format(
    test_pct[0], test_pct[1]))
```

**Lab Question C1 (5 pts):** Why is `stratify=y` important when the dataset has class imbalance? What would happen if you omitted it on a heavily imbalanced dataset?

**Lab Question C2 (5 pts):** Why must you never use the test set for any decision during model development, including choosing hyperparameters?

---

## Part D: Feature Scaling (25 points)

### Step 9: Apply StandardScaler

Neural networks are sensitive to feature scale. Features with large ranges will dominate gradient updates unless normalized.

```python
# Fit scaler on training data ONLY — then transform both sets
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)   # use training statistics — do not re-fit

# Verify scaling results
print("Before scaling — feature 0 stats:")
print("  Training mean: {:.4f}  std: {:.4f}".format(
    X_train[:, 0].mean(), X_train[:, 0].std()))

print("\nAfter scaling — feature 0 stats:")
print("  Training mean: {:.4f}  std: {:.4f}".format(
    X_train_scaled[:, 0].mean(), X_train_scaled[:, 0].std()))

# Visualize before and after for one feature
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.hist(X_train[:, 0], bins=30, color='steelblue', edgecolor='black', alpha=0.7)
ax1.set_title('Feature 0 — Before Scaling')
ax1.set_xlabel('Raw Value')
ax1.set_ylabel('Count')

ax2.hist(X_train_scaled[:, 0], bins=30, color='coral', edgecolor='black', alpha=0.7)
ax2.set_title('Feature 0 — After StandardScaler')
ax2.set_xlabel('Standardized Value (z-score)')
ax2.set_ylabel('Count')

plt.tight_layout()
plt.show()
```

### Step 10: Critical Scaler Rule

```python
# CORRECT: fit only on training data
scaler_correct = StandardScaler()
scaler_correct.fit(X_train)
X_train_scaled = scaler_correct.transform(X_train)
X_test_scaled  = scaler_correct.transform(X_test)

# WRONG — never do this:
# scaler_wrong = StandardScaler()
# X_test_scaled = scaler_wrong.fit_transform(X_test)  # data leakage!

print("Scaler training mean (feature 0): {:.4f}".format(scaler_correct.mean_[0]))
print("Scaler training std  (feature 0): {:.4f}".format(scaler_correct.scale_[0]))
print("\nApplying these SAME statistics to X_test prevents data leakage.")
```

**Lab Question D1 (5 pts):** Why is it data leakage to call `fit_transform` on the test set separately rather than using the scaler fitted on the training set?

**Lab Question D2 (5 pts):** After applying `StandardScaler`, what is the expected mean and standard deviation of each feature in the training set? Confirm this from your output.

---

## Submission Checklist

- All code cells run without errors.
- All four lab questions per section are answered in complete sentences below each question cell.
- All plots are visible in the submitted notebook.
- Submit the completed `.ipynb` file to the Canvas assignment portal.

---

## Grading Rubric

| Section | Task | Points |
|---|---|---|
| A | Dataset loaded, shape and class distribution printed correctly | 15 |
| A | Questions A1 and A2 answered correctly | 10 |
| B | Feature histograms and correlation heatmap rendered correctly | 15 |
| B | Questions B1 and B2 answered correctly | 10 |
| C | Train-test split executed with stratification, sizes verified | 15 |
| C | Questions C1 and C2 answered correctly | 10 |
| D | StandardScaler applied correctly (fit on train, transform both) | 15 |
| D | Questions D1 and D2 answered correctly | 10 |
| **Total** | | **100** |

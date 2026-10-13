# Video Script: Module 02 - Python for ML

**Course:** CIS-4345 Machine Learning and Deep Learning

**Institution:** Texas Wesleyan University

**Instructor:** Professor Nash

**Estimated Duration:** 20-24 minutes

**TensorFlow Developer Certificate Alignment:** Python and NumPy Foundations, Data Manipulation with Pandas, Visualization with Matplotlib

---

## [00:00 - 01:30] Opening and Module Overview

**[VISUAL: Title card — "Module 02: Python for ML | CIS-4345 | Professor Nash"]**

Welcome back. I'm Professor Nash, and this is Module 02 — Python for Machine Learning.

In Module 01 we established the conceptual framework: what machine learning is, how the three learning paradigms differ, and what the full ML pipeline looks like. Now we descend from theory into the practical tools every ML practitioner uses every single day.

Today we cover four interconnected topics. First, NumPy — the numerical computing library that powers every major ML framework including TensorFlow. Second, Pandas — the data manipulation library you will use to load, inspect, clean, and transform tabular data. Third, Matplotlib and Seaborn — the visualization tools that let you understand your data before you model it. Fourth, a focused tour of scikit-learn's preprocessing utilities, which you will use constantly in the early modules of this course before we transition fully to TensorFlow.

Every skill in this module is a prerequisite for everything that follows. If you are already comfortable with NumPy and Pandas, use this session to sharpen the specific patterns that appear in ML workflows. If these tools are new to you, go slowly, run every code example yourself, and do not move forward until the fundamentals are solid.

Let's get started.

---

## [01:30 - 05:30] NumPy: The Engine Under the Hood

**[VISUAL: Slide — "NumPy: N-Dimensional Array Operations"]**

NumPy is the foundational library for numerical computation in Python. TensorFlow tensors and NumPy arrays share the same underlying memory representation in many contexts, and the operations you learn in NumPy map directly to TensorFlow operations you will use throughout this course.

The central object in NumPy is the `ndarray` — an N-dimensional array of homogeneous data type. Unlike Python lists, NumPy arrays store data in contiguous memory blocks, which makes operations extremely fast through vectorization.

**[SHOW CODE]**

```python
import numpy as np

# Create a 1D array
a = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
print(a.shape)   # (5,)
print(a.dtype)   # float64

# Create a 2D array (matrix)
M = np.array([[1, 2, 3],
              [4, 5, 6]])
print(M.shape)   # (2, 3)

# Array creation utilities
zeros = np.zeros((3, 4))
ones  = np.ones((2, 2))
rand  = np.random.randn(100, 10)   # 100 samples, 10 features
```

**[VISUAL: Diagram — 1D array as a row vector, 2D array as a grid with rows=samples, cols=features]**

The shape convention is critical in ML: rows represent samples and columns represent features. A dataset with 1000 examples and 20 features is shape `(1000, 20)`. When you call `model.fit(X, y)` in Keras, Keras expects X to be shape `(n_samples, n_features)`. Understanding this convention prevents some of the most common beginner errors.

**[SHOW CODE]**

```python
# Vectorized operations — no loops needed
X = np.random.randn(1000, 10)

# Normalize: subtract mean, divide by std (z-score)
X_mean = X.mean(axis=0)       # mean of each feature (shape: 10,)
X_std  = X.std(axis=0)        # std of each feature  (shape: 10,)
X_norm = (X - X_mean) / X_std # broadcasting applies mean/std to all 1000 rows

print(X_norm.mean(axis=0).round(6))  # near zero
print(X_norm.std(axis=0).round(6))   # near one
```

Axis-0 operations run along the rows — so `mean(axis=0)` gives you the mean of each column across all rows. This is exactly the normalization step you will apply to features before training. The `axis` parameter is one of the most important NumPy concepts to understand deeply.

**[SHOW CODE]**

```python
# Reshaping — essential for neural network input formatting
flat = np.arange(784)          # single image flattened to 784 pixels
image = flat.reshape(28, 28)   # reshape to 28×28 grayscale image
batch = flat.reshape(1, 784)   # add batch dimension for model.predict()

# Broadcasting rule: dimensions align from the right
a = np.array([1, 2, 3])        # shape (3,)
b = np.array([[10], [20]])     # shape (2, 1)
print((a + b).shape)           # (2, 3) — broadcasting expands both
```

---

## [05:30 - 10:00] Pandas: Loading and Preparing Tabular Data

**[VISUAL: Slide — "Pandas: DataFrame Operations for ML"]**

Pandas provides the DataFrame — a tabular data structure with named columns, index-based rows, and a rich API for reading, filtering, grouping, and transforming data. You will use Pandas to load raw CSV files and clean them before passing arrays to a model.

**[SHOW CODE]**

```python
import pandas as pd

# Load a CSV file
df = pd.read_csv("housing.csv")

# First look at any new dataset — always run these four
print(df.shape)          # rows, columns
print(df.dtypes)         # data type of each column
print(df.isnull().sum()) # count missing values per column
print(df.describe())     # count, mean, std, min, quartiles, max
```

**[VISUAL: Table output of df.describe() with column statistics highlighted]**

The `describe()` output tells you immediately whether any feature has a wildly different scale from others, whether there are suspicious minimum or maximum values, and how many non-null entries exist. This is the first diagnostic you run before any preprocessing.

**[SHOW CODE]**

```python
# Handling missing values — two common strategies
df["age"].fillna(df["age"].median(), inplace=True)   # impute with median
df.dropna(subset=["target"], inplace=True)           # drop rows with missing target

# Encoding categorical variables
df["city"] = df["city"].astype("category").cat.codes        # integer encoding
city_dummies = pd.get_dummies(df["city"], prefix="city")    # one-hot encoding
df = pd.concat([df, city_dummies], axis=1)
df.drop(columns=["city"], inplace=True)

# Separating features and target
X = df.drop(columns=["price"]).values   # .values converts to NumPy array
y = df["price"].values
print(X.shape, y.shape)
```

**[SHOW CODE]**

```python
# Train/test split using scikit-learn
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(X_train.shape, X_test.shape)   # 80% / 20%
```

One pattern to memorize: always call `.values` after selecting DataFrame columns to convert to NumPy. TensorFlow and scikit-learn both accept NumPy arrays directly. Forgetting `.values` is a common source of type errors.

---

## [10:00 - 14:30] Matplotlib and Seaborn: Visualizing Data Before Modeling

**[VISUAL: Slide — "Exploratory Data Analysis: Why Visualization Comes Before Modeling"]**

There is a saying in data science: visualize before you model. If you skip exploratory analysis and jump straight to training, you will often build a model on corrupted, unscaled, or biased data — and you will not know it until the model fails unexpectedly.

These are the five visualizations every ML practitioner runs on every new dataset:

**[SHOW CODE]**

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Distribution of target variable
plt.figure(figsize=(8, 4))
plt.hist(y, bins=50, edgecolor="black")
plt.xlabel("House Price ($)")
plt.ylabel("Count")
plt.title("Distribution of Target Variable")
plt.tight_layout()
plt.show()

# 2. Feature correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Feature Correlation Matrix")
plt.tight_layout()
plt.show()
```

**[SHOW CODE]**

```python
# 3. Scatter plot: single feature vs target
plt.figure(figsize=(6, 4))
plt.scatter(df["sqft"], df["price"], alpha=0.3, s=10)
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Square Footage vs Price")
plt.tight_layout()
plt.show()

# 4. Pairplot for multi-feature relationships
sns.pairplot(df[["sqft", "bedrooms", "bathrooms", "price"]], diag_kind="kde")
plt.suptitle("Feature Pairplot", y=1.02)
plt.show()

# 5. Training curve (you will use this in every training run)
history_loss = [0.8, 0.5, 0.3, 0.2, 0.15]       # placeholder example
history_val  = [0.85, 0.55, 0.38, 0.32, 0.30]

plt.figure(figsize=(7, 4))
plt.plot(history_loss, label="Training Loss")
plt.plot(history_val, label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training and Validation Loss")
plt.legend()
plt.tight_layout()
plt.show()
```

**[VISUAL: Two curves diverging — train loss dropping, val loss plateauing — labeled "Overfitting"]**

Get comfortable with the training curve plot now. You will generate it after every `model.fit()` call for the rest of this course. The relationship between the training loss curve and the validation loss curve is the primary diagnostic tool for detecting overfitting and underfitting.

---

## [14:30 - 18:30] scikit-learn Preprocessing: Scalers and Pipelines

**[VISUAL: Slide — "scikit-learn Preprocessing: The Tools You Will Use Before TF"]**

scikit-learn provides preprocessing transformers that you will use in the first half of this course and occasionally alongside TensorFlow pipelines. The two most important are `StandardScaler` and `MinMaxScaler`.

**[SHOW CODE]**

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# StandardScaler: zero mean, unit variance (z-score)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit on train, transform train
X_test_scaled  = scaler.transform(X_test)       # transform test (no fit!)

# MinMaxScaler: scales each feature to [0, 1]
mm_scaler = MinMaxScaler()
X_train_mm = mm_scaler.fit_transform(X_train)
X_test_mm  = mm_scaler.transform(X_test)
```

**[VISUAL: Warning callout — "Never fit on test data: data leakage contaminates evaluation"]**

The golden rule of preprocessing: fit only on training data, then transform both train and test using the parameters learned from training data only. If you fit on the full dataset (train + test combined), you have contaminated the test set with information from the future — this is called data leakage, and it produces falsely optimistic test metrics.

**[SHOW CODE]**

```python
# scikit-learn Pipeline: chain preprocessing and model into one object
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  LinearRegression())
])

pipeline.fit(X_train, y_train)
score = pipeline.score(X_test, y_test)
print(f"R² score: {score:.4f}")
```

Pipelines prevent data leakage automatically. When you call `pipeline.fit(X_train, y_train)`, the scaler is fitted and the model is trained in sequence. When you call `pipeline.predict(X_test)`, the scaler applies the training-time parameters before prediction — no leakage possible.

---

## [18:30 - 21:30] Connecting Python Fundamentals to TensorFlow

**[VISUAL: Slide — "From NumPy to TensorFlow: The Bridge"]**

Everything we have covered today feeds directly into TensorFlow. Let me show you the explicit connection.

**[SHOW CODE]**

```python
import tensorflow as tf
import numpy as np

# A TensorFlow tensor is the TF equivalent of a NumPy array
a_np = np.array([1.0, 2.0, 3.0])
a_tf = tf.constant([1.0, 2.0, 3.0])

# Convert freely between the two
back_to_numpy = a_tf.numpy()

# TF operations mirror NumPy operations
print(tf.reduce_mean(a_tf))     # like np.mean()
print(tf.reduce_sum(a_tf))      # like np.sum()

# tf.data.Dataset: the TF way to feed data to a model
dataset = tf.data.Dataset.from_tensor_slices((X_train_scaled, y_train))
dataset = dataset.shuffle(buffer_size=1000).batch(32).prefetch(1)
```

**[VISUAL: Diagram — NumPy array → tf.data.Dataset → model.fit()]**

The `tf.data.Dataset` pipeline is how TensorFlow efficiently feeds data to models during training. The `shuffle` randomizes sample order each epoch, `batch` groups samples into mini-batches, and `prefetch` loads the next batch in the background while the current batch is being processed. You will build `tf.data` pipelines starting in Module 05.

---

## [21:30 - 23:30] Module Summary and Lab Preview

**[VISUAL: Slide — "Module 02 Key Takeaways"]**

Let's consolidate what we covered today.

NumPy provides N-dimensional arrays with vectorized operations, axis-based aggregation, and broadcasting — all patterns you will use constantly in TensorFlow. Pandas provides DataFrame operations for loading CSVs, handling missing values, encoding categoricals, and splitting features from targets. Matplotlib and Seaborn power the visualizations — especially the training curve — that you will use in every subsequent module. scikit-learn provides scalers and pipelines for preprocessing that prevent data leakage. And TensorFlow's tensor abstraction is a natural extension of NumPy that adds automatic differentiation and GPU execution.

In the Module 02 lab, you will load a real tabular dataset, run exploratory analysis, preprocess features with StandardScaler, visualize feature distributions, and build a baseline NumPy-based implementation before transitioning to TensorFlow. Complete the lab before you move to Module 03, because Module 03 assumes these preprocessing skills are already in your toolkit.

The TensorFlow Developer Certificate exam does not test NumPy and Pandas in isolation, but every problem you will solve requires fluency with these tools. You cannot work efficiently in the exam environment if you are still thinking about how to reshape an array or handle missing values.

See you in Module 03, where we apply these Python foundations to linear and logistic regression.

---

## Certification Alignment Notes

This module aligns to the TensorFlow Developer Certificate skill category: building and training neural networks using TensorFlow 2.x. Specifically, data preparation using NumPy arrays, batch handling via `tf.data.Dataset`, and input normalization are prerequisites for every problem category on the exam. Verify current exam objectives at tensorflow.org/certificate.

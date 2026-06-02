# Reading Guide: Module 02 - Python for ML

**Course:** CIS-4345 Machine Learning and Deep Learning

**Institution:** Texas Wesleyan University

**Instructor:** Professor Nash

**TensorFlow Developer Certificate Alignment:** NumPy Array Operations, Pandas Data Preparation, Matplotlib Visualization, scikit-learn Preprocessing, tf.data Pipelines

---

## Introduction

Module 02 establishes the Python toolkit that every subsequent module depends on. Machine learning in Python is built on a small set of interoperable libraries — NumPy, Pandas, Matplotlib, and scikit-learn — that share data through NumPy arrays. TensorFlow sits on top of this ecosystem and extends it with automatic differentiation and GPU acceleration. Fluency with these lower-level tools is not optional; it is the prerequisite for working efficiently under the timed TensorFlow Developer Certificate exam.

This guide walks through each library in depth, provides the API calls and patterns that appear most frequently in ML workflows, and ends with targeted exam tips and a study checklist.

---

## Section 1: NumPy

### The ndarray

The `ndarray` is NumPy's core data structure. It stores elements of a single data type in a contiguous memory block, enabling vectorized operations that are far faster than equivalent Python loops. Every TensorFlow tensor can be converted to and from a NumPy array using `.numpy()` on the tensor or `tf.constant()` on the array.

Key `ndarray` attributes:

| Attribute | Description | Example |
|---|---|---|
| `.shape` | Tuple of dimension sizes | `(1000, 20)` |
| `.dtype` | Data type of elements | `float32`, `int64` |
| `.ndim` | Number of dimensions | `2` |
| `.size` | Total number of elements | `20000` |
| `.T` | Transpose | Swaps rows and columns |

### Array Creation Functions

| Function | Description |
|---|---|
| `np.array(list)` | Create array from Python list |
| `np.zeros(shape)` | Array of zeros |
| `np.ones(shape)` | Array of ones |
| `np.arange(start, stop, step)` | Evenly spaced integers |
| `np.linspace(start, stop, n)` | Evenly spaced floats |
| `np.random.randn(n, m)` | Standard normal random values |
| `np.random.rand(n, m)` | Uniform random values in [0, 1) |
| `np.random.seed(42)` | Set random seed for reproducibility |

### Axis-Based Operations

The `axis` parameter is one of the most important concepts in NumPy. For a 2D array where rows represent samples and columns represent features:

- `axis=0` — operates along rows, produces one result per column (feature-wise statistics)
- `axis=1` — operates along columns, produces one result per row (sample-wise statistics)

| Operation | Code | Result shape for (1000, 20) input |
|---|---|---|
| Column means | `X.mean(axis=0)` | `(20,)` |
| Row sums | `X.sum(axis=1)` | `(1000,)` |
| Column max | `X.max(axis=0)` | `(20,)` |
| Global mean | `X.mean()` | scalar |

### Broadcasting

Broadcasting allows NumPy to perform arithmetic between arrays of different but compatible shapes. Dimensions align from right to left; size-1 dimensions are expanded to match.

Common broadcasting patterns in ML:

- Subtracting the feature mean from every row: `X - X.mean(axis=0)` — mean shape `(20,)` broadcasts to `(1000, 20)`
- Dividing by the feature standard deviation: `X / X.std(axis=0)` — same broadcast
- Adding a bias term: `np.dot(X, w) + b` — b shape `(1,)` broadcasts to match output

### Reshaping and Indexing

| Operation | Code | Use case |
|---|---|---|
| Reshape | `x.reshape(28, 28)` | Flatten to image |
| Add batch dim | `x.reshape(1, -1)` | Single sample for `predict()` |
| Flatten | `x.reshape(-1)` | Image to flat vector |
| Slice rows | `X[0:100]` | First 100 samples |
| Boolean mask | `X[y == 1]` | Select positive-class samples |

---

## Section 2: Pandas

### DataFrame Fundamentals

A `DataFrame` is a 2D labeled data structure where columns have names and rows have an integer or custom index. It is the standard container for tabular ML datasets before conversion to NumPy.

Essential first-look operations for any new dataset:

| Call | What it tells you |
|---|---|
| `df.shape` | (rows, columns) |
| `df.dtypes` | Column data types — spot object columns that need encoding |
| `df.isnull().sum()` | Count of missing values per column |
| `df.describe()` | Statistics: count, mean, std, min, 25%, 50%, 75%, max |
| `df.head(5)` | First 5 rows — spot structural anomalies |
| `df.value_counts("col")` | Frequency of each unique value in a column |

### Missing Value Handling

| Strategy | Code | When to use |
|---|---|---|
| Drop rows with missing target | `df.dropna(subset=["y"])` | Target is always required |
| Impute with median | `df["age"].fillna(df["age"].median())` | Numeric columns with outliers |
| Impute with mean | `df["age"].fillna(df["age"].mean())` | Numeric columns, roughly normal |
| Forward fill | `df.fillna(method="ffill")` | Time series — carry last known value |

### Encoding Categorical Variables

| Method | Code | When to use |
|---|---|---|
| Integer encoding | `df["col"].astype("category").cat.codes` | Ordinal categories |
| One-hot encoding | `pd.get_dummies(df["col"], prefix="col")` | Nominal categories |
| Drop original | `df.drop(columns=["col"])` | After replacing with encoded version |

### Separating Features from Target

```python
X = df.drop(columns=["target"]).values   # NumPy array, shape (n, p)
y = df["target"].values                  # NumPy array, shape (n,)
```

Always call `.values` to extract the underlying NumPy array. Leaving a DataFrame where a NumPy array is expected causes type errors in TensorFlow.

---

## Section 3: Matplotlib and Seaborn

### The Five Essential Plots

Every ML project requires a standard set of exploratory visualizations before model training.

| Plot | Code | What it reveals |
|---|---|---|
| Histogram | `plt.hist(y, bins=50)` | Target distribution, skewness, outliers |
| Correlation heatmap | `sns.heatmap(df.corr(), annot=True)` | Multicollinearity, strong predictors |
| Scatter: feature vs target | `plt.scatter(X[:,0], y)` | Linear vs nonlinear relationship |
| Box plot | `df.boxplot(column="feat")` | Outliers, quartile spread |
| Training curve | `plt.plot(history["loss"])` | Overfitting, convergence rate |

### Training Curve Interpretation

| Training curve shape | Diagnosis | Remedy |
|---|---|---|
| Both losses drop together | Healthy training | Continue or use early stopping |
| Train drops, val plateaus (gap forms) | Overfitting | Dropout, regularization, more data |
| Both losses high and flat | Underfitting | Larger model, more epochs, lower LR |
| Spiky / oscillating losses | Learning rate too high | Reduce learning rate |

---

## Section 4: scikit-learn Preprocessing

### Scalers

| Scaler | Formula | When to use |
|---|---|---|
| `StandardScaler` | `(x - mean) / std` | General purpose; roughly normal distribution |
| `MinMaxScaler` | `(x - min) / (max - min)` | Data in a known bounded range |
| `RobustScaler` | `(x - median) / IQR` | Data with many outliers |

The critical rule: fit only on training data. Call `fit_transform()` on `X_train` and `transform()` (without fit) on `X_test`. Fitting on the test set introduces data leakage and produces falsely optimistic evaluation metrics.

### Pipeline

`sklearn.pipeline.Pipeline` chains transformers and a final estimator. The pipeline calls `fit_transform()` on each transformer during `pipeline.fit()` and `transform()` on each transformer during `pipeline.predict()`, enforcing the no-leakage rule automatically.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("reg",    LinearRegression())
])
pipe.fit(X_train, y_train)
print(pipe.score(X_test, y_test))
```

---

## Section 5: tf.data.Dataset

### Why tf.data

`tf.data.Dataset` is TensorFlow's input pipeline API. It replaces raw NumPy arrays in large-scale training for two reasons: memory efficiency (streaming from disk rather than loading everything into RAM) and performance (prefetching and parallel loading eliminate CPU idle time during GPU computation).

### Core Pipeline Pattern

```python
import tensorflow as tf

dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
dataset = (dataset
           .shuffle(buffer_size=len(X_train))
           .batch(32)
           .prefetch(tf.data.AUTOTUNE))
```

| Method | Purpose |
|---|---|
| `.from_tensor_slices((X, y))` | Create dataset from arrays |
| `.shuffle(buffer_size)` | Randomize order each epoch |
| `.batch(n)` | Group samples into batches of size n |
| `.prefetch(tf.data.AUTOTUNE)` | Overlap data loading and model training |
| `.map(fn)` | Apply a preprocessing function to each element |
| `.repeat(n)` | Repeat dataset n times (None = indefinitely) |

Shuffle before batch. Shuffling after batching only randomizes the batch order, not the samples within each batch.

---

## Section 6: ML-Specific Python Patterns

### The Standard Preprocessing Block

This block appears at the start of nearly every ML project. Memorize it.

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data.csv")
df.dropna(inplace=True)

X = df.drop(columns=["target"]).values.astype(np.float32)
y = df["target"].values.astype(np.float32)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)
```

### Random State and Reproducibility

Always set a random state. In scikit-learn use `random_state=42`. In NumPy use `np.random.seed(42)`. In TensorFlow use `tf.random.set_seed(42)`. Without a fixed seed, results differ between runs and debugging becomes unreliable.

---

## Exam Tips

1. The TensorFlow Developer Certificate exam environment has TensorFlow, NumPy, and Pandas pre-installed. Just import the libraries directly.

2. `X.reshape(-1, 1)` converts a 1D array to a 2D column vector. Many scikit-learn estimators require 2D input even for a single feature.

3. Data leakage is a common code-completion trap. Verify that `fit_transform()` is called only on training data — never on validation or test data.

4. Build `tf.data` pipelines in the order `.shuffle()` then `.batch()` then `.prefetch()`. This is the standard exam-ready pattern.

5. `df.describe()` produces statistics only for numeric columns by default. Pass `include="all"` to include object-dtype columns.

6. `pd.get_dummies()` may produce boolean dtype in recent Pandas versions. Cast to float32 with `.astype(np.float32)` before passing to TensorFlow.

7. `np.random.randn()` samples from a standard normal distribution. `np.random.rand()` samples from a uniform distribution over [0, 1). Do not confuse these.

8. When normalizing image pixel values, divide by 255.0 after converting to float32: `X = X.astype(np.float32) / 255.0`.

---

## Study Checklist

Work through each item before the Module 02 quiz.

- [ ] Create 1D, 2D, and 3D NumPy arrays using `np.array()`, `np.zeros()`, and `np.random.randn()`
- [ ] Perform axis-0 and axis-1 aggregations (mean, std, sum, max) on a 2D array
- [ ] Manually implement z-score normalization using NumPy without sklearn
- [ ] Use `reshape()` to convert a flat array to a 2D matrix and back
- [ ] Load a CSV with `pd.read_csv()`, run `describe()`, and identify missing values
- [ ] Drop rows with missing targets and impute missing feature values with the median
- [ ] One-hot encode a categorical column using `pd.get_dummies()`
- [ ] Extract X and y as NumPy arrays from a DataFrame using `.values`
- [ ] Perform a stratified train/test split with `train_test_split(stratify=y)`
- [ ] Apply `StandardScaler` — fit on train only, transform both train and test
- [ ] Plot a histogram of the target variable and a correlation heatmap
- [ ] Reproduce the training curve plot using placeholder loss values
- [ ] Build a `tf.data.Dataset` from NumPy arrays with shuffle, batch, and prefetch
- [ ] Convert a TensorFlow tensor to NumPy using `.numpy()`

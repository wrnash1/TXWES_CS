# Lab: Module 02 - Python for ML

**Course:** CIS-4345 Machine Learning and Deep Learning

**Institution:** Texas Wesleyan University

**Instructor:** Professor Nash

**Total Points:** 100

**Estimated Time:** 90-120 minutes

**TensorFlow Developer Certificate Alignment:** NumPy array operations, Pandas data preparation, scikit-learn preprocessing, tf.data pipeline construction

---

## Lab Overview

In this lab you will build the complete Python preprocessing pipeline used in every ML project. You will load and inspect a dataset using Pandas, clean and transform it, normalize features with StandardScaler, visualize key distributions and relationships, and construct a `tf.data.Dataset` pipeline ready for model training. These are the exact workflows you will perform at the start of every coding problem on the TensorFlow Developer Certificate exam.

---

## Environment Setup

Confirm the following libraries are installed before beginning.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import tensorflow as tf

print(f"NumPy:      {np.__version__}")
print(f"Pandas:     {pd.__version__}")
print(f"TensorFlow: {tf.__version__}")
```

---

## Part 1: NumPy Fundamentals (20 points)

### Part 1 Objective

Practice the NumPy array operations that appear constantly in ML preprocessing: array creation, axis-based aggregation, broadcasting, and reshaping.

### Part 1 Tasks

#### Task 1.1 — Array Creation and Inspection

```python
np.random.seed(42)

# Create a synthetic feature matrix: 500 samples, 8 features
X = np.random.randn(500, 8).astype(np.float32)
y = (3.0 * X[:, 0] - 1.5 * X[:, 2] + 0.5 * X[:, 5]
     + np.random.randn(500).astype(np.float32) * 0.5)

print("X shape:", X.shape)
print("y shape:", y.shape)
print("X dtype:", X.dtype)
print("y dtype:", y.dtype)
print("\nFirst 3 rows of X:")
print(X[:3])
```

#### Task 1.2 — Axis-Based Statistics

```python
# Compute feature statistics without scikit-learn
col_means  = X.mean(axis=0)
col_stds   = X.std(axis=0)
col_mins   = X.min(axis=0)
col_maxes  = X.max(axis=0)

print("Feature means (should be near 0):")
print(col_means.round(3))

print("\nFeature stds (should be near 1):")
print(col_stds.round(3))
```

#### Task 1.3 — Manual Z-Score Normalization

```python
# Implement StandardScaler manually using broadcasting
X_norm = (X - col_means) / col_stds

print("After manual normalization:")
print("Means:", X_norm.mean(axis=0).round(6))   # should be near 0
print("Stds: ", X_norm.std(axis=0).round(6))    # should be near 1
```

#### Task 1.4 — Reshaping

```python
# Simulate a batch of 10 grayscale 28x28 images flattened to 784
flat_images = np.random.rand(10, 784).astype(np.float32)

# Reshape to (10, 28, 28)
image_batch = flat_images.reshape(10, 28, 28)
print("Reshaped image batch shape:", image_batch.shape)

# Add channel dimension for CNN input: (10, 28, 28, 1)
image_batch_cnn = image_batch.reshape(10, 28, 28, 1)
print("CNN input shape:", image_batch_cnn.shape)
```

#### Part 1 Deliverable

Screenshot or print output showing correct shapes and near-zero means and near-one stds after normalization.

---

## Part 2: Pandas Data Loading and Cleaning (25 points)

### Part 2 Objective

Load, inspect, and clean a tabular dataset using Pandas. Prepare it for model input by handling missing values, encoding categoricals, and converting to NumPy.

### Part 2 Tasks

#### Task 2.1 — Generate and Inspect a Synthetic Dataset

```python
np.random.seed(0)
n = 400

data = {
    "sqft":      np.random.randint(600, 4000, n).astype(float),
    "bedrooms":  np.random.randint(1, 6, n).astype(float),
    "age":       np.random.randint(1, 50, n).astype(float),
    "city":      np.random.choice(["Austin", "Dallas", "Houston", "SA"], n),
    "price":     np.random.randint(150_000, 800_000, n).astype(float)
}

df = pd.DataFrame(data)

# Introduce missing values
df.loc[np.random.choice(n, 20, replace=False), "age"]      = np.nan
df.loc[np.random.choice(n, 10, replace=False), "bedrooms"] = np.nan
df.loc[np.random.choice(n, 5,  replace=False), "price"]    = np.nan

print("Shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nSummary statistics:\n", df.describe())
```

#### Task 2.2 — Handle Missing Values

```python
# Drop rows where target (price) is missing
df.dropna(subset=["price"], inplace=True)
print("After dropping missing targets:", df.shape)

# Impute missing 'age' with median
age_median = df["age"].median()
df["age"].fillna(age_median, inplace=True)

# Impute missing 'bedrooms' with median
bed_median = df["bedrooms"].median()
df["bedrooms"].fillna(bed_median, inplace=True)

print("Missing values after imputation:\n", df.isnull().sum())
```

#### Task 2.3 — Encode Categorical Variables

```python
# One-hot encode the city column
city_dummies = pd.get_dummies(df["city"], prefix="city")
df = pd.concat([df, city_dummies], axis=1)
df.drop(columns=["city"], inplace=True)

print("Columns after encoding:", list(df.columns))
print("Shape after encoding:", df.shape)
```

#### Task 2.4 — Extract Features and Target

```python
X = df.drop(columns=["price"]).values.astype(np.float32)
y = df["price"].values.astype(np.float32)

print("Feature matrix shape:", X.shape)
print("Target vector shape:", y.shape)
print("Feature dtype:", X.dtype)
```

#### Part 2 Deliverable

Print outputs showing zero missing values after cleaning, correct column structure after encoding, and correct final shapes.

---

## Part 3: Visualization (20 points)

### Part 3 Objective

Produce the five standard exploratory visualizations that guide every ML project.

### Part 3 Tasks

#### Task 3.1 — Target Distribution

```python
plt.figure(figsize=(8, 4))
plt.hist(y, bins=40, edgecolor="black", color="steelblue")
plt.xlabel("House Price ($)")
plt.ylabel("Count")
plt.title("Distribution of House Prices")
plt.axvline(np.median(y), color="red", linestyle="--",
            label=f"Median: ${np.median(y):,.0f}")
plt.legend()
plt.tight_layout()
plt.savefig("target_distribution.png", dpi=100)
plt.show()
print("Target: mean={:.0f}, std={:.0f}".format(y.mean(), y.std()))
```

#### Task 3.2 — Correlation Heatmap

```python
numeric_cols = df.select_dtypes(include=[np.number]).columns
plt.figure(figsize=(10, 7))
sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f",
            cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Feature Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=100)
plt.show()
print("Correlation heatmap saved.")
```

#### Task 3.3 — Feature vs Target Scatter

```python
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
feature_names = ["sqft", "bedrooms", "age"]
feature_idx   = [0, 1, 2]

for ax, name, idx in zip(axes, feature_names, feature_idx):
    ax.scatter(X[:, idx], y, alpha=0.3, s=12, color="teal")
    ax.set_xlabel(name)
    ax.set_ylabel("Price")
    ax.set_title(f"{name} vs Price")

plt.tight_layout()
plt.savefig("scatter_plots.png", dpi=100)
plt.show()
```

#### Task 3.4 — Simulated Training Curve

```python
epochs     = list(range(1, 31))
train_loss = [0.9 * (0.88 ** i) + 0.02 for i in range(30)]
val_loss   = [0.95 * (0.91 ** i) + 0.10 for i in range(30)]

plt.figure(figsize=(8, 4))
plt.plot(epochs, train_loss, label="Training Loss",   color="blue")
plt.plot(epochs, val_loss,   label="Validation Loss", color="orange", linestyle="--")
plt.xlabel("Epoch")
plt.ylabel("Loss (MSE)")
plt.title("Simulated Training and Validation Loss")
plt.legend()
plt.tight_layout()
plt.savefig("training_curve.png", dpi=100)
plt.show()

gap = val_loss[-1] - train_loss[-1]
print(f"Final train loss: {train_loss[-1]:.4f}")
print(f"Final val loss:   {val_loss[-1]:.4f}")
print(f"Gap: {gap:.4f} — {'overfitting detected' if gap > 0.05 else 'healthy'}")
```

#### Part 3 Deliverable

Four saved plot files and print statements confirming plot generation.

---

## Part 4: scikit-learn Preprocessing and Baseline Model (20 points)

### Part 4 Objective

Apply train/test splitting, StandardScaler, and a baseline linear regression model using scikit-learn Pipeline.

### Part 4 Tasks

#### Task 4.1 — Train/Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Train: {X_train.shape[0]} samples | Test: {X_test.shape[0]} samples")
```

#### Task 4.2 — Scale with StandardScaler

```python
scaler  = StandardScaler()
X_tr_sc = scaler.fit_transform(X_train)   # fit on train only
X_te_sc = scaler.transform(X_test)        # transform test

print("Train feature means after scaling:", X_tr_sc.mean(axis=0).round(4))
print("Train feature stds after scaling: ", X_tr_sc.std(axis=0).round(4))
print("Test feature means (not exactly 0):", X_te_sc.mean(axis=0).round(4))
```

#### Task 4.3 — Baseline Model with Pipeline

```python
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("lr",     LinearRegression())
])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print(f"\nBaseline Linear Regression Results:")
print(f"RMSE: ${rmse:,.0f}")
print(f"R2:   {r2:.4f}")

plt.figure(figsize=(6, 5))
plt.scatter(y_test, y_pred, alpha=0.5, s=15, color="darkorange")
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()], "k--", lw=1.5)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Predicted vs Actual (Baseline Linear Regression)")
plt.tight_layout()
plt.savefig("predicted_vs_actual.png", dpi=100)
plt.show()
```

#### Part 4 Deliverable

RMSE, R² score, and predicted-vs-actual plot.

---

## Part 5: tf.data.Dataset Pipeline (15 points)

### Part 5 Objective

Construct a `tf.data.Dataset` pipeline from NumPy arrays, correctly applying shuffle, batch, and prefetch in the right order.

### Part 5 Tasks

#### Task 5.1 — Build the Training Dataset

```python
tf.random.set_seed(42)

BATCH_SIZE = 32
BUFFER     = len(X_tr_sc)

train_ds = tf.data.Dataset.from_tensor_slices((X_tr_sc, y_train))
train_ds = (train_ds
            .shuffle(buffer_size=BUFFER)
            .batch(BATCH_SIZE)
            .prefetch(tf.data.AUTOTUNE))

test_ds = tf.data.Dataset.from_tensor_slices((X_te_sc, y_test))
test_ds = test_ds.batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

print("Train dataset element spec:")
print(train_ds.element_spec)
print("\nTest dataset element spec:")
print(test_ds.element_spec)
```

#### Task 5.2 — Inspect a Batch

```python
for x_batch, y_batch in train_ds.take(1):
    print("\nFirst batch shapes:")
    print(f"  x_batch shape: {x_batch.shape}")
    print(f"  y_batch shape: {y_batch.shape}")
    print(f"\nFirst 3 feature rows:\n{x_batch[:3].numpy()}")
    print(f"\nFirst 3 targets: {y_batch[:3].numpy()}")
```

#### Task 5.3 — Train a Simple TensorFlow Model on the Dataset

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu",
                          input_shape=(X_tr_sc.shape[1],)),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer="adam", loss="mse", metrics=["mae"])
model.summary()

history = model.fit(
    train_ds,
    validation_data=test_ds,
    epochs=30,
    verbose=0
)

final_val_mae = history.history["val_mae"][-1]
print(f"\nFinal validation MAE: ${final_val_mae:,.0f}")

plt.figure(figsize=(8, 4))
plt.plot(history.history["loss"],     label="Train Loss")
plt.plot(history.history["val_loss"], label="Val Loss",  linestyle="--")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("TF Model Training Curve")
plt.legend()
plt.tight_layout()
plt.savefig("tf_training_curve.png", dpi=100)
plt.show()
```

#### Part 5 Deliverable

Dataset element spec, batch shapes, TF model summary, and training curve plot.

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part 1: NumPy operations | 20 | Correct shapes, near-zero means and near-one stds after normalization, reshape outputs correct |
| Part 2: Pandas cleaning | 25 | Zero missing values after cleaning, correct one-hot encoding, correct final array shapes |
| Part 3: Visualizations | 20 | All four plots generated, training curve shows two lines, plot files saved |
| Part 4: Preprocessing and baseline | 20 | Pipeline runs without error, RMSE and R² printed, predicted vs actual plot generated |
| Part 5: tf.data pipeline | 15 | Dataset built in correct order, batch shapes correct, TF model trains and produces training curve |
| **Total** | **100** | |

---

## Submission Instructions

Submit a single `.py` file or Jupyter `.ipynb` notebook named `Lab02_YourLastName.py` (or `.ipynb`). Include all code, print outputs, and saved plot files. Ensure all code runs end-to-end without errors from a clean Python session.

---

## Part 9 — Challenge Exercise

### Challenge 1: Comparing Scaler Behaviors on Skewed Data

Generate a right-skewed income-like feature and compare how `StandardScaler`, `RobustScaler`, and a log transform each handle the distribution.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, RobustScaler

np.random.seed(7)
# Simulate skewed income: log-normal distribution
income = np.random.lognormal(mean=10.8, sigma=1.2, size=500).reshape(-1, 1)

standard_scaled = StandardScaler().fit_transform(income)
robust_scaled   = RobustScaler().fit_transform(income)
log_transformed = np.log1p(income)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
titles = ["Raw Income", "StandardScaler", "RobustScaler", "log1p Transform"]
arrays = [income, standard_scaled, robust_scaled, log_transformed]

for ax, title, arr in zip(axes, titles, arrays):
    ax.hist(arr.flatten(), bins=40, edgecolor="black", color="steelblue", alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel("Value")
    ax.set_ylabel("Count")

plt.tight_layout()
plt.savefig("scaler_comparison.png", dpi=100)
plt.show()

for name, arr in zip(titles[1:], [standard_scaled, robust_scaled, log_transformed]):
    print(f"{name:20s} | mean={arr.mean():.4f} | std={arr.std():.4f} | "
          f"min={arr.min():.4f} | max={arr.max():.4f}")
```

1. Observe which scaler produces the least skewed output histogram for log-normal income data.
2. Note the min/max range for each scaler — which has the most extreme outlier values after scaling?
3. In one sentence, explain why `RobustScaler` outperforms `StandardScaler` when extreme outliers are present.

### Challenge 2: Building a tf.data Pipeline with a Custom Map Function

Extend the `tf.data` pipeline from Part 5 by adding a `.map()` step that applies a custom feature engineering transformation (polynomial feature for the first column) before batching.

```python
import tensorflow as tf

# Reload clean scaled arrays from Part 4
# (X_tr_sc and y_train should already be in scope)

def add_polynomial_feature(x, y):
    """Add x[:,0]^2 as an extra feature column."""
    poly = tf.expand_dims(x[:, 0] ** 2, axis=1)   # shape (1,)
    x_aug = tf.concat([x, poly], axis=1)
    return x_aug, y

# Build pipeline with map applied BEFORE batching for element-wise transform
train_ds_aug = (
    tf.data.Dataset.from_tensor_slices((X_tr_sc, y_train))
    .shuffle(buffer_size=len(X_tr_sc))
    .batch(32)
    .map(add_polynomial_feature, num_parallel_calls=tf.data.AUTOTUNE)
    .prefetch(tf.data.AUTOTUNE)
)

for xb, yb in train_ds_aug.take(1):
    print("Augmented feature shape:", xb.shape)   # should be (32, n_features+1)
    print("Extra column (x0^2) — first 5 values:", xb[:5, -1].numpy())

# Train a model on the augmented dataset
model_aug = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu", input_shape=(X_tr_sc.shape[1] + 1,)),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1)
])
model_aug.compile(optimizer="adam", loss="mse", metrics=["mae"])
hist_aug = model_aug.fit(train_ds_aug, epochs=20, verbose=0)
print(f"Final train MAE (augmented): ${hist_aug.history['mae'][-1]:,.0f}")
```

1. Compare the final training MAE of the augmented model versus the baseline model from Part 5.
2. Adjust the `map` function to apply to batches (after `.batch()`) and verify the shape remains correct.

### Reflection Questions

1. In Challenge 1, the `log1p` transform produced the most symmetric distribution for income. Under what real-world conditions might you choose `RobustScaler` over a log transform, and when would you prefer the log transform?
2. The `.map()` function in `tf.data` can run in parallel with `num_parallel_calls=tf.data.AUTOTUNE`. What are the potential risks of applying non-deterministic augmentation (e.g., random noise) inside a map function, and how would you ensure reproducibility?

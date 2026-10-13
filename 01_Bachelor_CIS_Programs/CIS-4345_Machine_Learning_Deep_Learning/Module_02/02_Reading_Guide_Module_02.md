# Reading Guide: Module 02 - Python for ML

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4345 &BULL; MACHINE LEARNING & DEEP LEARNING SYSTEMS</text>
    
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

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">TensorFlow / deeplearning.ai &bull; CIS-4345 Module 02</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=NWONeJKn6kc" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/NWONeJKn6kc" title="Deep Learning & Neural Networks Masterclass" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Deep Learning & Neural Networks Masterclass</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

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

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 02 - Python for ML** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 02 - Python for ML**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 02 - Python for ML**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Module 02 - Python for ML**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**

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

---

## 9. Supplemental Resources

**1. NumPy Official Documentation — Array Creation and Indexing**
<https://numpy.org/doc/stable/user/basics.html>
The authoritative reference for NumPy array creation, axis-based operations, broadcasting rules, and reshaping. The "Absolute Beginner's Guide" section provides concise worked examples for all the patterns used in this module's lab.

**2. Pandas User Guide — Working with Missing Data**
<https://pandas.pydata.org/docs/user_guide/missing_data.html>
Official Pandas documentation covering `dropna`, `fillna`, imputation strategies, and detection of missing values. Includes examples for all the cleaning patterns in Part 2 of the lab.

**3. TensorFlow tf.data Guide — Building Input Pipelines**
<https://www.tensorflow.org/guide/data>
Google's official guide to `tf.data.Dataset` covering `from_tensor_slices`, `shuffle`, `batch`, `prefetch`, and `map`. Includes performance benchmarks showing why shuffle-before-batch and prefetch matter for training throughput.

# Reading Guide: Module 01 - ML Fundamentals

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


**Course:** CIS-4345 Machine Learning and Deep Learning

**Institution:** Texas Wesleyan University

**Instructor:** Professor Nash

**TensorFlow Developer Certificate Alignment:** Foundation Concepts — Learning Paradigms, ML Pipeline, Bias-Variance Tradeoff

---

## Introduction

Welcome to Module 01. This reading guide builds the foundational vocabulary and conceptual framework that every subsequent module depends on. Machine learning is not a collection of independent tricks — it is a disciplined engineering practice with consistent patterns, vocabulary, and failure modes that repeat across every domain. Mastering the foundations in this module will make every future topic easier to learn and every future debugging session faster to resolve.

The TensorFlow Developer Certificate exam tests practical coding ability, but that ability rests on conceptual foundations. Examiners expect you to recognize which learning paradigm applies to a problem, know why you split data the way you do, and understand the diagnostic meaning of your training and validation curves. This guide prepares you for both the conceptual knowledge and the practical application.

---

## Section 1: Core Vocabulary

### Learning Paradigms

**Supervised learning** is a training paradigm in which the model receives labeled input-output pairs (X, y) and learns a mapping function f such that f(X) approximates y. Classification and regression are both supervised tasks. The defining characteristic is the presence of ground-truth labels for every training example.

**Unsupervised learning** is a training paradigm in which the model receives only input features X with no labels. The algorithm discovers hidden structure — clusters, latent representations, or density estimates — entirely from the data distribution. Clustering, dimensionality reduction, and generative modeling are unsupervised tasks.

**Self-supervised learning** is a variant of unsupervised learning in which the model generates its own supervision signal from the input data. Large language models and contrastive image models use self-supervision. You will encounter this concept in Module 09.

**Reinforcement learning** is a paradigm in which an agent interacts with an environment, selects actions, and receives scalar reward signals. The agent learns a policy that maximizes expected cumulative reward. No labeled dataset is required. RL is out of scope for the TensorFlow Developer Certificate exam.

**Semi-supervised learning** combines a small labeled dataset with a large unlabeled dataset. The model uses the unlabeled data to improve its representations while the labeled data provides the supervision signal. Useful when labeling is expensive.

---

## Section 2: The ML Pipeline — Stage by Stage

### Problem Definition

Every ML project begins with a precise problem statement: What is the target variable? What type of output is required (class label, continuous value, probability)? What performance threshold is acceptable? What are the consequences of false positives versus false negatives? Answering these questions before touching data prevents wasted work.

### Data Collection and Storage

Training data quality dominates model performance. Sources include: relational databases, flat CSV files, image archives, streaming logs, web APIs, and public benchmark datasets. Common public datasets used throughout this course include MNIST (handwritten digits), CIFAR-10 (color images), IMDb (movie reviews), and Fashion-MNIST (clothing images).

### Data Preprocessing

Preprocessing transforms raw data into a form the model can process. Critical steps:

- **Missing value handling:** Drop rows, impute with mean/median/mode, or use model-based imputation.
- **Outlier treatment:** Cap at percentiles, remove, or apply robust scaling.
- **Categorical encoding:** One-hot encoding for nominal variables; label encoding for ordinal variables.
- **Numerical scaling:** Standardization (zero mean, unit variance) or min-max normalization to 0-1.
- **Train/validation/test splitting:** Typically 70/15/15 or 80/10/10. The test set is never examined until final evaluation.

### Feature Engineering

Feature engineering creates new input representations that expose signal the model would otherwise struggle to find. For tabular data: polynomial features, interaction terms, binning. For images: pixel normalization, channel standardization. For text: tokenization, vocabulary indexing, TF-IDF, word embeddings. Well-engineered features regularly outperform more complex models on raw features.

### Model Training

Model training adjusts the model's parameters (weights and biases) to minimize a loss function over the training set. Gradient descent and its variants (SGD, Adam, RMSProp) are the standard optimization algorithms. Training loops in Keras are handled internally by `model.fit()`, which manages forward passes, loss computation, backpropagation, and weight updates.

### Model Evaluation

Evaluation quantifies how well the trained model generalizes to unseen data. The evaluation set must be entirely held out during training. Using the test set for any hyperparameter tuning decisions introduces data leakage and inflates reported performance. A separate validation set is used during training for hyperparameter decisions; the test set is used only once.

### Deployment

Trained models are serialized and served through APIs, mobile apps, edge devices, or embedded systems. TensorFlow's deployment ecosystem includes TF Serving (gRPC/REST server), TFLite (mobile/edge), and TF.js (browser). Module 15 covers deployment in detail.

---

## Section 3: Algorithm Comparison Table

| Algorithm | Type | Supervised | Use Case | Strengths | Weaknesses |
|---|---|---|---|---|---|
| Linear Regression | Parametric | Yes | Continuous target | Interpretable, fast | Assumes linearity |
| Logistic Regression | Parametric | Yes | Binary classification | Probabilistic output | Linear decision boundary |
| Decision Tree | Non-parametric | Yes | Classification/Regression | Interpretable, handles mixed types | Prone to overfitting |
| Random Forest | Ensemble | Yes | Classification/Regression | Robust, handles nonlinearity | Less interpretable |
| k-Nearest Neighbors | Instance-based | Yes | Classification | Simple, no training phase | Slow inference, sensitive to scale |
| k-Means | Centroid-based | No | Clustering | Simple, scalable | Requires k, assumes spherical clusters |
| PCA | Dimensionality reduction | No | Feature compression | Removes redundancy | Linear transformation only |
| Neural Network (Dense) | Deep learning | Yes | General-purpose | Universal approximator | Needs large data, opaque |
| CNN | Deep learning | Yes | Image tasks | Spatial invariance | Computationally intensive |
| RNN / LSTM | Deep learning | Yes | Sequence tasks | Handles temporal dependencies | Vanishing gradient (LSTM mitigates) |

---

## Section 4: Bias-Variance Tradeoff

The total prediction error of a supervised model can be decomposed into three components:

### Total Error = Bias^2 + Variance + Irreducible Noise

**Bias** is the systematic gap between the model's average prediction and the true value. High bias means the model's assumptions are too strong — it cannot capture the real pattern in the data. Manifestation: low training accuracy AND low validation accuracy (underfitting).

**Variance** is the model's sensitivity to fluctuations in training data. High variance means the model has memorized training noise and fails on new data. Manifestation: high training accuracy BUT low validation accuracy (overfitting).

**Irreducible noise** is inherent randomness in the data-generating process that no model can eliminate.

The bias-variance tradeoff states that strategies which reduce bias tend to increase variance, and vice versa. The optimal model minimizes total error by balancing the two. Common bias-reduction strategies: more complex model, additional features, removing regularization. Common variance-reduction strategies: regularization (L1/L2), dropout, more training data, simpler architecture, early stopping.

### Diagnostic Rules

| Training Accuracy | Validation Accuracy | Diagnosis | Action |
|---|---|---|---|
| Low | Low | Underfitting (high bias) | More capacity, more features, fewer constraints |
| High | Low | Overfitting (high variance) | Regularize, more data, simpler model |
| High | High | Good generalization | Proceed to test evaluation |
| Low | High | Data issue or split error | Audit data pipeline |

---

## Section 5: Key TensorFlow and Keras Concepts Introduced

### Tensors

A tensor is the fundamental data structure in TensorFlow. It is a multidimensional array — a generalization of scalars, vectors, and matrices. A scalar is a rank-0 tensor, a vector is rank-1, a matrix is rank-2, and a batch of images is typically a rank-4 tensor with shape (batch, height, width, channels).

### The Keras Sequential API

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(n_features,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=20, validation_data=(X_val, y_val))
```

The three-step pattern — define, compile, fit — appears on every TensorFlow Developer Certificate exam problem. Memorize it.

### Train-Test Split with scikit-learn

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

The `stratify=y` argument ensures class proportions are preserved in both splits — essential for imbalanced datasets.

---

## Section 6: Evaluation Metrics Reference

| Metric | Formula | Task | Notes |
|---|---|---|---|
| Accuracy | Correct / Total | Classification | Misleading on imbalanced data |
| Precision | TP / (TP + FP) | Classification | Penalizes false positives |
| Recall | TP / (TP + FN) | Classification | Penalizes false negatives |
| F1-Score | 2 x P x R / (P + R) | Classification | Harmonic mean of precision and recall |
| MAE | Mean abs(y - y_hat) | Regression | Robust to outliers |
| MSE | Mean (y - y_hat)^2 | Regression | Penalizes large errors more |
| RMSE | sqrt(MSE) | Regression | Same units as target variable |

---

## Section 7: TensorFlow Developer Certificate Exam Tips

**Tip 1 — Know the exam format.** The exam is five hours, open-book, and run in a local Python environment (PyCharm + TensorFlow plugin). You are evaluated on whether your model achieves a target accuracy threshold, not on code style. Read the candidate handbook at tensorflow.org/certificate before attempting any exam task.

**Tip 2 — Master the three-step Keras pattern.** Define, compile, fit. Every exam problem uses this pattern. Practice it until it is automatic. You should be able to write a complete model definition and training call in under two minutes without referring to documentation.

**Tip 3 — Know your loss functions.** Binary classification uses `binary_crossentropy`. Multi-class classification with integer labels uses `sparse_categorical_crossentropy`. Multi-class with one-hot labels uses `categorical_crossentropy`. Regression uses `mse` or `mae`. Getting the wrong loss function will cause your model to fail to train.

**Tip 4 — Normalize your inputs.** Neural networks train much faster and more reliably when input features are normalized to similar scales. For image data, divide pixel values by 255.0. For tabular data, apply `StandardScaler` or `MinMaxScaler` from scikit-learn.

**Tip 5 — Use callbacks.** `tf.keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)` prevents overfitting and saves training time. The exam rewards models that hit the accuracy threshold, not models that train for the maximum number of epochs.

**Tip 6 — Understand the data pipeline.** The exam gives you data in various forms: NumPy arrays, `tf.data.Dataset` objects, or `ImageDataGenerator` output. Know how to load and feed each format to `model.fit()`.

**Tip 7 — Validation split vs. validation data.** `model.fit(X, y, validation_split=0.1)` carves off 10% of the training data. `model.fit(X_train, y_train, validation_data=(X_val, y_val))` uses a pre-split validation set. Both monitor overfitting; prefer the latter for reproducibility.

**Tip 8 — Check your output layer.** The output layer activation and number of units must match the task. Single-neuron sigmoid for binary classification. N-neuron softmax for N-class classification. Single-neuron linear (no activation) for regression.

---

## Section 8: Study Checklist

- Read every definition in Section 1 and write your own one-sentence version of each.
- Draw the ML pipeline from memory as a 7-stage flowchart.
- Reproduce the bias-variance diagnostic table from memory.
- Confirm Python environment is working: `import tensorflow as tf; print(tf.__version__)`.
- Confirm scikit-learn is working: `from sklearn.model_selection import train_test_split`.
- Complete the Module 01 lab: environment setup, data loading, train-test split.
- Read the TensorFlow Developer Certificate candidate handbook at tensorflow.org/certificate.
- Take the Module 01 quiz.
- Post to the Module 01 discussion board by Wednesday at 11:59 PM.
- Respond to at least two classmates by Sunday at 11:59 PM.

---

## 9. Supplemental Resources

**1. Google Machine Learning Crash Course**
<https://developers.google.com/machine-learning/crash-course>
Google's free, self-paced course covering ML fundamentals including supervised learning, loss functions, gradient descent, and overfitting. Includes interactive coding exercises and visual explanations ideal for reinforcing Module 01 concepts.

**2. scikit-learn User Guide — Model Selection and Evaluation**
<https://scikit-learn.org/stable/model_selection.html>
Official scikit-learn documentation for train-test splitting, cross-validation, and evaluation metrics. Contains runnable examples for `train_test_split`, `StratifiedKFold`, and `StandardScaler` directly relevant to this module's lab.

**3. TensorFlow Developer Certificate Candidate Handbook**
<https://www.tensorflow.org/certificate>
The official exam guide describing the five problem categories, scoring criteria, and development environment requirements. Reading this before Module 01 ensures all subsequent modules are studied with the exam objectives in mind.

# Reading Guide: Module 08 — Data Mining and Predictive Techniques

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

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 2: Data Analysis

---

## Overview

This guide covers the core data mining and predictive modeling techniques tested on the CompTIA Data+ exam. Work through each section, complete the practice problems, and review the exam tips before your quiz. These concepts appear heavily in Domain 2 (Data Analysis) of the Data+ certification.

---

## Section 1: Supervised vs. Unsupervised Learning

The most important conceptual distinction for the Data+ exam:

| Characteristic | Supervised Learning | Unsupervised Learning |
|----------------|--------------------|-----------------------|
| Training data | Labeled (has known outputs) | Unlabeled (no known outputs) |
| Goal | Predict output for new inputs | Discover hidden structure |
| Examples | Decision trees, regression, SVM | K-means clustering, PCA |
| Evaluation | Accuracy, precision, recall | Silhouette score, elbow method |

---

## Section 2: K-Means Clustering

### Algorithm Steps

1. Select k (number of clusters)
2. Initialize k centroids randomly
3. Assign each point to nearest centroid: `assignment = argmin_j(distance(x_i, centroid_j))`
4. Recompute centroids: `centroid_j = mean of all points assigned to cluster j`
5. Repeat steps 3–4 until convergence (centroids do not move)

### Distance Metric

K-means uses Euclidean distance by default.

`euclidean_distance = sqrt(sum((x_i - c_i)^2))`

### Selecting K — The Elbow Method

Plot WCSS (within-cluster sum of squares) vs. k. Choose k at the "elbow" — the point where adding more clusters yields diminishing improvement.

`WCSS = sum over clusters of sum of squared distances from each point to centroid`

### K-Means Assumptions and Limitations

- Clusters are assumed to be spherical and roughly equal in size
- Sensitive to outliers (outliers distort centroid positions)
- Must specify k in advance
- Results vary with random initialization — run multiple times and choose the best result

### When to Use K-Means

Use k-means when you want to segment a population into groups with no predefined categories. Common applications: customer segmentation, document grouping, image compression.

---

## Section 3: Decision Trees

### Structure

A decision tree is a flowchart-like structure where:

- Each internal node tests a feature value
- Each branch represents one outcome of that test
- Each leaf node contains a class label (classification) or numeric value (regression)

### Split Criteria

**Gini impurity** (used in CART algorithm):

`gini = 1 - sum(p_i^2)`

A perfectly pure node has `gini = 0`. The algorithm selects the split that minimizes the weighted average Gini of the child nodes.

**Entropy and information gain** (used in ID3/C4.5 algorithms):

`entropy = -sum(p_i * log2(p_i))`

`information_gain = entropy(parent) - weighted_avg_entropy(children)`

The algorithm selects the split with the highest information gain.

### Overfitting and Pruning

Decision trees can grow until every training sample is in its own leaf — perfectly accurate on training data, useless on new data. Solutions:

- **Pre-pruning:** stop splitting when tree reaches maximum depth or minimum samples per node
- **Post-pruning:** grow the full tree then remove branches that add little predictive value

### Advantages and Disadvantages

| Advantage | Disadvantage |
|-----------|-------------|
| Highly interpretable | Prone to overfitting |
| No feature scaling needed | Unstable (small data changes cause different tree structure) |
| Handles mixed data types | Biased toward features with many values |
| Fast to train and predict | Poor extrapolation beyond training data range |

---

## Section 4: Random Forests

### Ensemble Learning via Bagging

An ensemble model combines predictions from multiple models. Random forests use **bagging** (bootstrap aggregating):

1. Draw n bootstrap samples from training data (sampling with replacement)
2. Train one decision tree on each sample
3. At each split, consider only a random subset of features (`sqrt(total_features)` for classification)
4. Aggregate: majority vote for classification, mean for regression

### Why Ensembles Outperform Single Models

Individual trees have high variance — they overfit. But their errors are uncorrelated because they are trained on different data subsets. Averaging uncorrelated errors reduces variance without increasing bias.

`ensemble_error ≈ average_tree_error × (1 - correlation_between_trees)`

### Feature Importance

Random forests compute feature importance as the average decrease in impurity across all splits on that feature, weighted by the number of samples affected.

### Hyperparameters

| Parameter | Effect |
|-----------|--------|
| `n_estimators` | Number of trees — more trees means more stable but slower |
| `max_depth` | Maximum tree depth — limits overfitting |
| `min_samples_split` | Minimum samples to split a node — higher means less overfitting |
| `max_features` | Features considered per split — lower means more diversity between trees |

---

## Section 5: Regression Analysis

### Simple Linear Regression

`y = b0 + b1 * x`

The ordinary least squares (OLS) method finds `b0` and `b1` that minimize:

`SSR = sum((y_actual - y_predicted)^2)`

The slope coefficient:

`b1 = sum((x - mean_x)(y - mean_y)) / sum((x - mean_x)^2)`

`b0 = mean_y - b1 * mean_x`

### Multiple Linear Regression

`y = b0 + b1*x1 + b2*x2 + ... + bn*xn`

Each coefficient represents the marginal effect of that variable, holding all others constant.

### Model Fit Metrics

**R-squared (coefficient of determination):**

`R_sq = 1 - (SSR / SST)` where `SST = sum((y_actual - mean_y)^2)`

R-squared ranges from 0 to 1. Higher values indicate better fit. However, R-squared always increases when you add more predictors — even irrelevant ones. Use Adjusted R-squared instead:

`adj_R_sq = 1 - ((1 - R_sq) * (n - 1) / (n - k - 1))`

where n = sample size and k = number of predictors.

**Root Mean Squared Error (RMSE):**

`RMSE = sqrt(sum((y_actual - y_predicted)^2) / n)`

RMSE is in the same units as y, making it directly interpretable. Lower RMSE is better.

### Regression Assumptions

1. Linear relationship between x and y
2. Independence of observations
3. Homoscedasticity — constant variance of residuals
4. Normally distributed residuals
5. No multicollinearity (for multiple regression)

---

## Section 6: Association Rules

### Definitions and Formulas

Given transactions, an association rule has the form `{A} → {B}`.

**Support:** frequency of an itemset across all transactions

`support(A) = count(transactions containing A) / total_transactions`

**Confidence:** how often B appears given that A appeared

`confidence(A → B) = support(A and B) / support(A)`

**Lift:** whether the association is stronger than chance

`lift(A → B) = confidence(A → B) / support(B)`

Interpretation:

- `lift > 1` — positive association (A and B co-occur more than expected)
- `lift = 1` — A and B are statistically independent
- `lift < 1` — negative association (A and B co-occur less than expected)

### Apriori Algorithm

The Apriori algorithm uses the anti-monotonicity property: if an itemset is infrequent, all supersets are also infrequent. This prunes the search space dramatically, making large-scale association analysis practical.

Steps: find frequent itemsets at minimum support → generate candidate rules → filter by minimum confidence → rank by lift.

---

## Section 7: Model Evaluation — The Confusion Matrix

For binary classification (positive/negative):

|  | Predicted Positive | Predicted Negative |
|--|-------------------|-------------------|
| Actual Positive | True Positive (TP) | False Negative (FN) |
| Actual Negative | False Positive (FP) | True Negative (TN) |

### Core Metrics

`accuracy = (TP + TN) / (TP + TN + FP + FN)`

`precision = TP / (TP + FP)`

`recall = TP / (TP + FN)`

`F1 = 2 * (precision * recall) / (precision + recall)`

### When to Use Each Metric

| Metric | Best When |
|--------|-----------|
| Accuracy | Classes are balanced |
| Precision | False positives are costly (spam filter, fraud alert) |
| Recall | False negatives are costly (cancer screening, safety systems) |
| F1 Score | Classes are imbalanced; both FP and FN matter equally |

### Worked Example

A fraud detection model processes 1,000 transactions: 50 fraudulent, 950 legitimate.

Results: TP = 40, TN = 920, FP = 30, FN = 10

`accuracy = (40 + 920) / 1000 = 96%`

`precision = 40 / (40 + 30) = 57.1%`

`recall = 40 / (40 + 10) = 80%`

`F1 = 2 * (0.571 * 0.80) / (0.571 + 0.80) = 66.7%`

The 96% accuracy looks impressive, but precision of 57% means more than 4 in 10 fraud alerts are false alarms — a significant operational burden.

---

## Section 8: Data+ Exam Tips

**Tip 1:** Supervised vs. Unsupervised — The exam frequently tests this distinction. Clustering = unsupervised. Decision trees and regression = supervised.

**Tip 2:** Memorize the four confusion matrix cells (TP, TN, FP, FN) and practice computing all four metrics from raw numbers.

**Tip 3:** Precision vs. Recall — Know which to prioritize based on error cost. False negatives costly = maximize recall. False positives costly = maximize precision.

**Tip 4:** Know all three association rule metrics — support, confidence, lift — and that lift > 1 means meaningful positive association.

**Tip 5:** Overfitting is tested. A model perfect on training data but poor on test data is overfitting. Random forests and pruning are standard solutions.

**Tip 6:** R-squared ranges from 0 to 1. Higher means more variance explained. Adjusted R-squared penalizes for adding irrelevant predictors.

---

## Practice Problems

**Problem 1:** A classification model produces: TP=80, TN=750, FP=20, FN=50. Calculate accuracy, precision, recall, and F1.

**Problem 2:** A grocery dataset shows: `support(milk) = 0.40`, `support(cereal) = 0.30`, `support(milk and cereal) = 0.18`. Calculate `confidence(milk → cereal)` and `lift(milk → cereal)`.

**Problem 3:** You are building a model to detect early-stage kidney disease. Which metric should you prioritize: precision or recall? Why?

**Problem 4:** Your k-means WCSS scores are: k=2: 820, k=3: 430, k=4: 390, k=5: 375. What value of k does the elbow method suggest?

---

## 9. Supplemental Resources

**1. scikit-learn User Guide — Supervised Learning**
<https://scikit-learn.org/stable/supervised_learning.html>
The official scikit-learn documentation covering decision trees, random forests, and classification evaluation metrics (precision, recall, F1, confusion matrix) with worked examples and API references — directly aligned with Module 08 predictive modeling topics.

**2. Google Developers Machine Learning Crash Course — Classification**
<https://developers.google.com/machine-learning/crash-course/classification/video-lecture>
A free, self-paced course unit covering threshold tuning, precision-recall tradeoffs, ROC curves, and the AUC metric with interactive exercises and visualizations. Reinforces the model evaluation concepts required for the Data+ exam.

**3. Towards Data Science — Apriori Algorithm Explained**
<https://towardsdatascience.com/apriori-association-rule-mining-explanation-and-python-implementation-290b42afdfc6>
A practical walkthrough of the Apriori algorithm with Python code using the `mlxtend` library, covering support, confidence, and lift with a real grocery basket dataset. Useful for the association rule mining portion of Module 08 and Data+ Domain 2.

---

End of Module 08 Reading Guide

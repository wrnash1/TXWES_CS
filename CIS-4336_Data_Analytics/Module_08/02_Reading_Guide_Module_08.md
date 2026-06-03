# Reading Guide: Module 08 — Data Mining and Predictive Techniques

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

End of Module 08 Reading Guide

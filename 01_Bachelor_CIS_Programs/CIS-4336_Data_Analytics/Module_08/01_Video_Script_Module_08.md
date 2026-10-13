# Video Script: Module 08 — Data Mining and Predictive Techniques

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA Data+ (DA0-001)

---

## Segment 1: Introduction (0:00–1:30)

Welcome back to CIS-4336. I'm Professor Nash. In Module 07 we described data — we summarized what it looks like right now. Today we go further: we are going to predict what happens next and find hidden patterns in large datasets.

This is the world of data mining and predictive analytics — techniques that power recommendation engines, fraud detection systems, medical diagnosis tools, and credit scoring models. These are not exotic research topics. They run in production at scale every single day.

By the end of this module you will understand clustering with k-means, classification with decision trees and random forests, regression analysis, association rules, and how to evaluate whether a model is actually any good using accuracy, precision, recall, and F1 score.

The CompTIA Data+ exam tests predictive analytics concepts in Domain 2. These are high-value questions — pay close attention.

[PAUSE — Slide: Module 08 Objectives]

---

## Segment 2: What Is Data Mining? (1:30–3:00)

Data mining is the process of discovering patterns, correlations, anomalies, and useful insights in large datasets using statistical and computational techniques. It sits at the intersection of statistics, machine learning, and database systems.

Data mining techniques fall into two broad categories.

**Unsupervised learning** — the algorithm finds structure in data without labeled examples. The data has no "right answer." Clustering is the classic example.

**Supervised learning** — the algorithm learns from labeled training data, then applies what it learned to new, unseen data. Classification and regression are supervised techniques.

[SHOW CHART — Diagram: supervised vs. unsupervised learning decision tree]

[PAUSE]

---

## Segment 3: Clustering — K-Means (3:00–6:30)

Clustering groups data points so that items within a cluster are more similar to each other than to items in other clusters. The algorithm is given no labels — it discovers structure on its own.

### K-Means Algorithm

K-means is the most widely used clustering algorithm. Here is how it works.

Step 1: Choose k — the number of clusters you want.

Step 2: Randomly place k centroids in the data space.

Step 3: Assign each data point to the nearest centroid.

Step 4: Recalculate each centroid as the mean of all points assigned to it.

Step 5: Repeat steps 3 and 4 until centroids stop moving (convergence).

[SHOW CHART — Animated diagram of k-means iteration: random centroids → assignment → recalculation → convergence]

[PAUSE]

### Choosing K

Choosing the right number of clusters is one of the most important decisions in k-means. The **elbow method** plots within-cluster sum of squares (WCSS) against values of k. As k increases, WCSS decreases — but at some point, adding more clusters yields diminishing returns. The "elbow" in the curve is the optimal k.

`WCSS = sum over all clusters of sum of squared distances from each point to its cluster centroid`

### K-Means Limitations

K-means assumes clusters are spherical and roughly equal in size. It is sensitive to initial centroid placement and to outliers. It also requires you to specify k in advance, which is not always obvious.

[PAUSE]

### Business Use Cases for Clustering

- Customer segmentation: group customers by purchasing behavior
- Network anomaly detection: isolate unusual traffic patterns
- Document categorization: group news articles by topic
- Genomics: cluster gene expression profiles

---

## Segment 4: Classification — Decision Trees (6:30–10:00)

Classification assigns new data points to predefined categories based on patterns learned from labeled training data. The output is a class label, not a number.

Examples:

- Email → spam or not spam
- Loan application → approve or deny
- Medical image → malignant or benign

### Decision Trees

A decision tree splits data based on feature values, creating a tree-like structure where each internal node is a test on a feature, each branch is an outcome of that test, and each leaf node is a class prediction.

[SHOW CHART — Decision tree diagram: root node "Age > 30?" → branches → leaf nodes with class labels]

[PAUSE]

The algorithm selects the best split at each node using a measure of impurity. Two common measures:

**Gini impurity:** `gini = 1 - sum(p_i^2)` where `p_i` is the proportion of class i in the node. A pure node (all one class) has Gini = 0.

**Information gain (entropy):** `entropy = -sum(p_i * log2(p_i))`. A split that maximally reduces entropy has the highest information gain.

### Decision Tree Advantages

- Easy to interpret — you can trace exactly why a prediction was made
- No feature scaling required
- Handles both numeric and categorical features

### Decision Tree Disadvantages

- Prone to overfitting — can memorize training data perfectly but generalize poorly
- Sensitive to small changes in training data

[PAUSE]

---

## Segment 5: Random Forests (10:00–12:30)

Random forests address decision tree overfitting by combining many trees — an **ensemble method**.

Here is the idea: instead of one deep tree that overfits, build hundreds of trees. Each tree is trained on a random sample of the data (bootstrap sampling) and considers only a random subset of features at each split. This is called **bagging** (bootstrap aggregating).

The final prediction is determined by majority vote (classification) or averaging (regression) across all trees.

[SHOW CHART — Diagram: 5 trees with different training samples → voting → final prediction]

[PAUSE]

### Why Random Forests Work

Each individual tree makes errors, but the errors are uncorrelated — different trees make different mistakes. When you average across hundreds of uncorrelated trees, the errors cancel out and the ensemble is much more accurate than any single tree.

### Feature Importance

A powerful side benefit: random forests provide **feature importance scores** — how much each input variable contributed to prediction accuracy. This is invaluable for understanding your data and for feature selection.

### Random Forest Trade-offs

- More accurate than a single decision tree
- Much less interpretable — you lose the "trace the path" advantage
- Computationally expensive with large datasets

[PAUSE]

---

## Segment 6: Regression Analysis (12:30–15:00)

Regression predicts a continuous numeric output — not a category.

### Simple Linear Regression

Simple linear regression models the relationship between one input variable (x) and one output variable (y) as a straight line.

`y = b0 + b1 * x`

Where `b0` is the intercept and `b1` is the slope. The algorithm finds the values of `b0` and `b1` that minimize the sum of squared residuals — the differences between actual and predicted y values.

`SSR = sum((y_actual - y_predicted)^2)`

This is the **ordinary least squares** (OLS) method.

[PAUSE]

### Multiple Linear Regression

Multiple linear regression extends this to multiple input variables.

`y = b0 + b1*x1 + b2*x2 + ... + bn*xn`

Each `b` coefficient tells you: "holding all other variables constant, how much does y change when this variable increases by one unit?"

### Model Fit — R-Squared

R-squared measures what proportion of the variance in y is explained by the model.

`R_squared = 1 - (SSR / SST)`

Where `SST` is the total sum of squares (variance around the mean). R-squared ranges from 0 (model explains nothing) to 1 (model explains everything). Higher is better, but beware of overfitting.

[SHOW CHART — Scatter plot with regression line and residuals illustrated]

[PAUSE]

---

## Segment 7: Association Rules (15:00–17:00)

Association rule mining discovers co-occurrence patterns in transactional data. The classic application is market basket analysis: if a customer buys bread and butter, how likely are they to also buy milk?

An association rule has the form: `{A} → {B}` — if a transaction contains A, it also tends to contain B.

### Key Metrics

**Support** measures how frequently an itemset appears in all transactions.

`support(A) = transactions_containing_A / total_transactions`

**Confidence** measures how often B appears in transactions that contain A.

`confidence(A → B) = support(A and B) / support(A)`

**Lift** measures whether A and B appear together more often than by chance.

`lift(A → B) = confidence(A → B) / support(B)`

A lift value greater than 1 means the items are positively associated. Lift = 1 means they are independent.

[PAUSE]

### The Apriori Algorithm

The Apriori algorithm efficiently finds frequent itemsets by pruning candidates that do not meet a minimum support threshold. It uses the anti-monotonicity property: any subset of a frequent itemset must also be frequent.

Business use cases: retail shelf placement, cross-sell recommendations, fraud pattern detection, medical co-diagnosis analysis.

[SHOW CHART — Example association rules table with support, confidence, lift columns]

---

## Segment 8: Model Evaluation (17:00–20:00)

Building a model is only half the job. You must evaluate whether it is actually performing well before deploying it.

### The Confusion Matrix

For classification models, the confusion matrix organizes four outcomes:

- **True Positive (TP):** model predicted positive, actual is positive
- **True Negative (TN):** model predicted negative, actual is negative
- **False Positive (FP):** model predicted positive, actual is negative (Type I error)
- **False Negative (FN):** model predicted negative, actual is positive (Type II error)

[SHOW CHART — 2x2 confusion matrix with TP, TN, FP, FN labeled]

[PAUSE]

### Accuracy

`accuracy = (TP + TN) / (TP + TN + FP + FN)`

Accuracy is intuitive but misleading when classes are imbalanced. If 95% of emails are not spam, a model that always predicts "not spam" achieves 95% accuracy while being completely useless.

### Precision

`precision = TP / (TP + FP)`

Precision answers: of all the times the model said "positive," how often was it right? Use precision when false positives are costly — for example, incorrectly flagging a legitimate transaction as fraud.

### Recall (Sensitivity)

`recall = TP / (TP + FN)`

Recall answers: of all the actual positives, how many did the model catch? Use recall when false negatives are costly — for example, missing a cancer diagnosis.

### F1 Score

F1 is the harmonic mean of precision and recall. It balances both concerns.

`F1 = 2 * (precision * recall) / (precision + recall)`

F1 is the go-to metric when you care about both precision and recall and the classes are imbalanced.

[PAUSE]

### Precision-Recall Trade-off

Improving precision often hurts recall, and vice versa. The model threshold controls this trade-off. Raising the classification threshold increases precision but decreases recall. Lowering the threshold increases recall but decreases precision.

---

## Segment 9: Module Summary (20:00–21:30)

Let me close with a summary.

[PAUSE]

Data mining techniques covered today:

- **K-means clustering** — unsupervised; groups similar data points
- **Decision trees** — supervised classification; interpretable but prone to overfitting
- **Random forests** — ensemble of trees; more accurate, less interpretable
- **Linear regression** — predicts continuous output; OLS minimizes squared residuals
- **Association rules** — finds co-occurrence patterns; measured by support, confidence, lift

Model evaluation:

- Confusion matrix: TP, TN, FP, FN
- Accuracy, precision, recall, F1 score
- Precision-recall trade-off controlled by threshold

For the Data+ exam: know the difference between supervised and unsupervised learning, know all four confusion matrix cells, and be able to calculate accuracy, precision, recall, and F1 from given numbers.

Your lab this week builds a decision tree classifier in Python using scikit-learn and evaluates it with a confusion matrix. See you in Module 09 — Big Data Technologies.

[PAUSE — End card]

---

End of Module 08 Video Script

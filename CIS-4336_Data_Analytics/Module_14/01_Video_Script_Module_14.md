# Video Script: Module 14 — Machine Learning for Data Analysts

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

**Estimated Duration:** 20–24 minutes

---

### [00:00 – 02:00] Introduction

**Visual:** Instructor on camera with title card: **Machine Learning for Data Analysts**.

**Audio:** "Welcome to Module 14. Machine learning is one of the most discussed topics in data, and it is also one of the most misunderstood. This module is not about becoming a machine learning engineer. It is about understanding enough ML to be a better data analyst — to know what questions ML can and cannot answer, how to prepare data for a model, and how to evaluate whether a model is working. The CompTIA Data+ exam tests these conceptual foundations, and they are what employers expect analysts to know. Let's start from the top."

**Study Link:** [Google Machine Learning Crash Course — free](https://developers.google.com/machine-learning/crash-course)

---

### [02:00 – 06:00] Supervised vs. Unsupervised Learning

**Visual:** Two-column diagram: left column shows supervised learning with labeled examples flowing into a model; right column shows unsupervised learning with unlabeled data flowing into a clustering algorithm.

**Alt-text:** Left side: rows of data with a label column showing "spam" and "not spam" feeding into a box labeled "classifier." Right side: rows of data with no label column feeding into a box labeled "cluster algorithm," producing three color-coded groups.

**Audio:** "The first and most important distinction in machine learning is between supervised and unsupervised learning.

**Supervised learning** means the training data has labels — a column that tells the model the correct answer. The model learns to predict that label for new examples it has never seen. Every row you use to train has an input (the features) and an output (the label). Examples: predicting whether a customer will churn — yes or no — that is a **classification** task. Predicting next month's revenue — a number — that is a **regression** task. Both are supervised.

**Unsupervised learning** means the data has no labels. The algorithm finds structure in the data on its own. The most common form is **clustering** — grouping similar records together without being told what the groups are. Customer segmentation is a classic example: you give the algorithm purchase history, and it discovers that customers naturally group into budget shoppers, premium buyers, and seasonal purchasers. You did not define those groups. The algorithm found them.

A third category is **semi-supervised learning**, which uses a small amount of labeled data and a large amount of unlabeled data. For the Data+ exam, focus on supervised and unsupervised — these are the two categories tested."

---

### [06:00 – 09:30] scikit-learn Basics

**Visual:** Jupyter notebook showing a five-step machine learning workflow: import → load data → split → train → evaluate.

**Alt-text:** Notebook with five code cells. Each cell is numbered and has a comment matching the five steps.

**Audio:** "scikit-learn is the most widely used Python library for machine learning in analytical work. It is not a deep learning library — for neural networks you would use TensorFlow or PyTorch — but for the classification, regression, and clustering tasks that data analysts actually do, scikit-learn covers almost everything.

Every scikit-learn model follows the same four-method API:

One — `fit(X_train, y_train)` — trains the model on your training data.
Two — `predict(X_test)` — generates predictions for new data.
Three — `score(X_test, y_test)` — returns the default evaluation metric (accuracy for classifiers, R² for regressors).
Four — `predict_proba(X_test)` — for classifiers, returns the probability of each class rather than just the class label.

This uniform API means switching from a decision tree to a random forest to logistic regression changes only one line of code — the class you instantiate. Everything else stays the same. That is by design."

---

### [09:30 – 13:00] Feature Engineering

**Visual:** A before-and-after table: raw data on the left, engineered feature set on the right.

**Alt-text:** Left table: columns for raw_date, zip_code, price. Right table: columns for month, day_of_week, is_weekend, region (from zip), log_price, price_bucket.

**Audio:** "Feature engineering is the process of transforming raw data columns into the numerical input format that a machine learning model requires. Most models cannot accept raw text, dates, or categorical strings — they need numbers. Feature engineering is where analytical judgment has the highest impact on model quality.

Common feature engineering techniques:

**One-hot encoding** — converts a categorical variable into binary columns. If Region has values North, South, East, West, you create four binary columns: is_North, is_South, is_East, is_West. The original column is replaced.

**Ordinal encoding** — converts ordered categories to integers. Size: Small=1, Medium=2, Large=3.

**Date decomposition** — extract year, month, day of week, and is_weekend from a timestamp column.

**Log transformation** — for heavily right-skewed numeric columns (like price or income), take the natural log to compress the range and help linear models learn from the variable.

**Scaling** — StandardScaler subtracts the mean and divides by standard deviation; MinMaxScaler rescales to a 0–1 range. Many algorithms — logistic regression, SVM, KNN — require scaled features.

A common mistake: applying scaling to the entire dataset before splitting into train and test sets. This causes **data leakage** — the test set statistics contaminate the training fit. Always split first, then fit the scaler on training data only."

---

### [13:00 – 16:30] Train/Test Split and Model Selection

**Visual:** Diagram showing a dataset being split: 80% training set, 20% test set, with an arrow from training set to model and from test set to evaluation.

**Alt-text:** A horizontal bar representing the full dataset divided by a vertical line at the 80% mark. Left segment labeled "Training set — model learns here." Right segment labeled "Test set — model never sees this during training."

**Audio:** "The train/test split is the foundation of honest model evaluation. If you train a model on all your data and evaluate it on the same data, you are measuring memorization, not generalization. The model will appear to perform extremely well but will fail on new data.

The standard approach:

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

`test_size=0.2` reserves 20% for testing. `random_state=42` fixes the random seed so the split is reproducible.

For small datasets or when you want a more reliable estimate, use **cross-validation** — the data is split into k folds, the model is trained k times each time using a different fold as the test set, and the k accuracy scores are averaged.

**Model selection** means choosing the right algorithm for the problem. Key considerations:

* Is it classification or regression?
* How many training examples do you have?
* How interpretable does the model need to be?
* How long can training take?

For the Data+ exam, know that logistic regression is for binary classification, linear regression is for numeric prediction, decision trees are interpretable but prone to overfitting, and random forests reduce overfitting by averaging many trees."

---

### [16:30 – 20:00] Overfitting vs. Underfitting

**Visual:** Three curves on one chart: perfect fit, overfit, and underfit, showing training error and test error for each.

**Alt-text:** A chart with model complexity on the x-axis and error on the y-axis. Three zones are marked. The left zone shows high training error and high test error — underfitting. The middle zone shows low training error and low test error — good fit. The right zone shows very low training error but high test error — overfitting.

**Audio:** "Overfitting and underfitting are the two failure modes of any machine learning model.

**Underfitting** happens when the model is too simple to capture the patterns in the data. A straight line trying to fit an obviously curved relationship. The model performs poorly on both training data and new data. Solutions: use a more complex algorithm, add more features, or train longer.

**Overfitting** happens when the model is too complex — it memorizes the training data including its noise and random fluctuations. The model performs nearly perfectly on training data but poorly on new data. This is the more common failure mode in practice. Solutions: reduce model complexity, use more training data, apply regularization, or use cross-validation to detect it early.

The diagnostic tool is comparing training accuracy to test accuracy. If training accuracy is 98% and test accuracy is 61%, the model is overfit. If both are 64%, the model is underfit.

For the Data+ exam, be able to define overfitting and underfitting, identify which failure mode a described scenario represents, and name at least two solutions for each."

---

### [20:00 – 24:00] Exam Connection and Wrap-Up

**Visual:** Data+ domain map with Domain 3 — Data Analysis — highlighted, with ML concepts listed.

**Audio:** "Machine learning concepts appear in Domain 3 of the Data+ exam — Data Analysis and Statistics. The exam does not ask you to write or debug ML code. It asks conceptual questions: What is the difference between supervised and unsupervised learning? What does overfitting look like in a training-versus-test-accuracy comparison? What is the purpose of a train-test split? What is feature engineering?

This week's lab has you walking through a complete scikit-learn classification pipeline in a Jupyter notebook. Even if you have never written ML code before, the lab is structured step by step and the dataset is intentionally clean. Focus on understanding each step rather than memorizing syntax. I'll see you there."

---

### Instructor Notes

* Dataset for lab: `titanic_clean.csv` or similar binary classification dataset with a mix of numeric and categorical features
* Emphasize that the Data+ exam tests ML concepts, not implementation
* The overfitting vs. underfitting chart is a high-yield visual to reproduce on the board

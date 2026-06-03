# Lab 08 — Data Mining and Predictive Techniques

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 100

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 2: Data Analysis

---

## Lab Overview

In this lab you will build and evaluate a decision tree classifier and a k-means clustering model using Python and scikit-learn. You will work with a bank marketing dataset, evaluate your classifier using a confusion matrix and key metrics, and use the elbow method to select the optimal number of clusters.

**Tools required:**

- Python 3.8 or later
- scikit-learn (`pip install scikit-learn`)
- pandas (`pip install pandas`)
- matplotlib (`pip install matplotlib`)

---

## Dataset

Create a file named `bank_customers.csv` with the following data.

```csv
customer_id,age,balance,duration,campaign,previous,subscribed
1,30,1787,971,1,0,yes
2,33,4789,185,1,0,yes
3,35,1350,79,1,0,no
4,30,1476,199,4,0,no
5,59,0,226,1,0,no
6,35,747,141,2,0,no
7,36,307,341,1,0,no
8,39,147,151,2,0,no
9,41,221,57,2,0,no
10,43,0,313,1,0,no
11,39,512,273,1,0,no
12,43,270,113,2,0,no
13,36,1,328,1,0,no
14,28,2971,899,3,0,yes
15,30,0,148,1,0,yes
16,38,2475,169,2,0,no
17,44,0,58,5,0,no
18,55,1260,143,1,0,no
19,31,925,187,1,0,yes
20,37,2132,975,2,0,yes
21,41,1764,56,1,0,no
22,43,824,456,1,0,yes
23,29,764,1042,1,0,yes
24,32,1283,345,2,0,no
25,40,891,231,1,0,yes
```

---

## Part 1: Data Preparation (15 points)

### Task 1.1 — Load and inspect the data

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import (confusion_matrix, accuracy_score,
                             precision_score, recall_score, f1_score,
                             ConfusionMatrixDisplay)
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('bank_customers.csv')
print(df.shape)
print(df.dtypes)
print(df.head())
print(df['subscribed'].value_counts())
```

**Deliverable 1.1:** How many customers subscribed (yes) vs. did not subscribe (no)? Is this dataset balanced or imbalanced?

### Task 1.2 — Encode the target variable and select features

```python
le = LabelEncoder()
df['subscribed_enc'] = le.fit_transform(df['subscribed'])  # yes=1, no=0

features = ['age', 'balance', 'duration', 'campaign', 'previous']
X = df[features]
y = df['subscribed_enc']

print(f"Feature matrix shape: {X.shape}")
print(f"Target distribution: {y.value_counts().to_dict()}")
```

### Task 1.3 — Split into training and test sets

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)
print(f"Training samples: {len(X_train)}")
print(f"Test samples:     {len(X_test)}")
```

**Deliverable 1.3:** Why do we use `stratify=y` in the train/test split?

---

## Part 2: Decision Tree Classifier (35 points)

### Task 2.1 — Train the decision tree

```python
dt_model = DecisionTreeClassifier(max_depth=4, random_state=42)
dt_model.fit(X_train, y_train)
print("Decision tree trained.")
print(f"Tree depth: {dt_model.get_depth()}")
print(f"Number of leaves: {dt_model.get_n_leaves()}")
```

### Task 2.2 — Visualize the tree

```python
fig, ax = plt.subplots(figsize=(14, 6))
plot_tree(dt_model,
          feature_names=features,
          class_names=['No', 'Yes'],
          filled=True,
          rounded=True,
          ax=ax,
          fontsize=9)
plt.title('Decision Tree: Bank Subscription Prediction', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('decision_tree.png', dpi=150)
plt.show()
```

**Deliverable 2.2:** Looking at the tree visualization, what is the first (root) split feature? What does this tell you about which variable is most important for predicting subscription?

### Task 2.3 — Generate predictions and confusion matrix

```python
y_pred = dt_model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No', 'Yes'])
fig, ax = plt.subplots(figsize=(5, 4))
disp.plot(ax=ax, colorbar=False, cmap='Blues')
ax.set_title('Confusion Matrix — Decision Tree', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=150)
plt.show()

print("Confusion matrix array:")
print(cm)
```

### Task 2.4 — Compute evaluation metrics

```python
acc  = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, zero_division=0)
rec  = recall_score(y_test, y_pred, zero_division=0)
f1   = f1_score(y_test, y_pred, zero_division=0)

print(f"Accuracy:  {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall:    {rec:.4f}")
print(f"F1 Score:  {f1:.4f}")
```

**Deliverable 2.4:** Record all four metrics. Given that this is a subscription campaign, which metric is most important to the bank — precision or recall? Justify your answer in 2–3 sentences.

### Task 2.5 — Feature importance

```python
importances = pd.Series(dt_model.feature_importances_, index=features)
importances = importances.sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(6, 4))
importances.plot(kind='barh', color='steelblue', ax=ax)
ax.set_title('Feature Importance — Decision Tree', fontsize=12, fontweight='bold')
ax.set_xlabel('Importance Score')
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=150)
plt.show()
```

**Deliverable 2.5:** Which feature has the highest importance score? Does this align with the root split you identified in Task 2.2?

---

## Part 3: K-Means Clustering (30 points)

### Task 3.1 — Apply the elbow method

```python
cluster_features = ['age', 'balance', 'duration']
X_cluster = df[cluster_features].copy()

wcss = []
k_range = range(2, 9)

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_cluster)
    wcss.append(km.inertia_)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(k_range, wcss, marker='o', linewidth=2, color='darkgreen')
ax.set_title('Elbow Method — Optimal Number of Clusters', fontsize=12, fontweight='bold')
ax.set_xlabel('Number of Clusters (k)')
ax.set_ylabel('WCSS (Within-Cluster Sum of Squares)')
ax.set_xticks(list(k_range))
plt.tight_layout()
plt.savefig('elbow_plot.png', dpi=150)
plt.show()

print("WCSS values:")
for k, w in zip(k_range, wcss):
    print(f"  k={k}: {w:.1f}")
```

**Deliverable 3.1:** Based on the elbow plot, what is the optimal k? Explain your reasoning.

### Task 3.2 — Train the final k-means model

```python
optimal_k = 3  # Update this based on your elbow analysis

km_final = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['cluster'] = km_final.fit_predict(X_cluster)

print("Cluster distribution:")
print(df['cluster'].value_counts().sort_index())

print("\nCluster centroids:")
centroids = pd.DataFrame(km_final.cluster_centers_, columns=cluster_features)
print(centroids.round(1))
```

### Task 3.3 — Visualize clusters

```python
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

fig, ax = plt.subplots(figsize=(7, 5))
for c in range(optimal_k):
    mask = df['cluster'] == c
    ax.scatter(df.loc[mask, 'age'], df.loc[mask, 'balance'],
               label=f'Cluster {c}', alpha=0.7,
               color=colors[c], edgecolors='white', s=60)

ax.set_title('K-Means Customer Segments (Age vs. Balance)', fontsize=12, fontweight='bold')
ax.set_xlabel('Age')
ax.set_ylabel('Balance ($)')
ax.legend()
plt.tight_layout()
plt.savefig('kmeans_clusters.png', dpi=150)
plt.show()
```

**Deliverable 3.3:** Describe each cluster in business terms based on the centroid values. What does each cluster represent in terms of customer profile (age, balance, call duration)?

---

## Part 4: Reflection Questions (20 points)

Answer each in 3–5 sentences.

**Question 4.1:** Your decision tree achieved a certain accuracy on the test set. What would it mean if the training accuracy was 100% but the test accuracy was much lower? What technique would you use to address this problem?

**Question 4.2:** You are presenting the k-means customer segments to a marketing team. They ask why two customers with very similar age and balance ended up in different clusters. How do you explain the cluster assignment process in plain language?

**Question 4.3:** The bank's fraud team asks you to build a model that must catch at least 90% of all fraudulent transactions. Which metric does this "90%" requirement correspond to? What trade-off will you likely make to hit this target?

**Question 4.4:** Compare the decision tree and the random forest approach. In what business situation would you choose interpretability over accuracy, and in what situation would you choose accuracy over interpretability?

---

## Submission Checklist

Submit the following in a ZIP file:

- [ ] Python script (`lab08.py` or `lab08.ipynb`)
- [ ] `decision_tree.png`
- [ ] `confusion_matrix.png`
- [ ] `feature_importance.png`
- [ ] `elbow_plot.png`
- [ ] `kmeans_clusters.png`
- [ ] Lab report (PDF or Word) containing all deliverables and reflection answers

---

## Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Part 1 — Data preparation | 15 | Correct encoding, split, stratification explanation |
| Part 2 — Decision tree | 35 | Model trained, tree visualized, all four metrics computed, feature importance chart |
| Part 3 — K-means clustering | 30 | Elbow method applied, optimal k justified, cluster profiles described |
| Part 4 — Reflection | 20 | Accurate, thoughtful answers demonstrating conceptual understanding |
| **Total** | **100** | |

---

End of Lab 08

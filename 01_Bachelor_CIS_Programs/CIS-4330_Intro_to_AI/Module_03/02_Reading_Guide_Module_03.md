# Reading Guide: Module 03 - Unsupervised Learning: Clustering and Dimensionality Reduction

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4330 &BULL; INTRODUCTION TO ARTIFICIAL INTELLIGENCE</text>
    
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


## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe fundamental principles of machine learning on Azure (20-25%)

---

## Overview

This reading guide covers the theory, algorithms, and Azure implementations of unsupervised learning, with emphasis on clustering and dimensionality reduction. These topics appear in the AI-900 exam in the context of Azure ML task types, anomaly detection workloads, and scenario-based algorithm selection questions. Complete the study checklist before the lab.

---

## Section 1: Core Vocabulary

**Unsupervised Learning**
Machine learning in which training data contains no output labels. The algorithm discovers structure — clusters, latent dimensions, anomalies — from input features alone.

**Clustering**
An unsupervised task that groups data points into clusters based on similarity. The groups are not defined in advance; the algorithm discovers them.

**K-means Clustering**
An iterative clustering algorithm that partitions data into K clusters by assigning each point to the nearest centroid and recalculating centroids until convergence.

**Centroid**
The mean position of all data points currently assigned to a cluster. In K-means, centroids are recalculated at each iteration.

**Within-Cluster Sum of Squares (WCSS)**
Also called inertia. The sum of squared distances between each data point and its cluster centroid across all clusters. Lower WCSS indicates tighter, more cohesive clusters.

**Elbow Method**
A heuristic for selecting K in K-means. WCSS is plotted as a function of K, and the value of K at which the rate of decrease sharply slows (the elbow) is selected as the optimal number of clusters.

**Silhouette Score**
A metric for evaluating clustering quality that measures how similar each point is to its own cluster compared to the nearest other cluster. Ranges from -1 to 1; higher is better.

**Hierarchical Clustering**
A clustering algorithm that builds a tree of nested clusters (dendrogram) by iteratively merging the nearest pairs of clusters. Does not require specifying K in advance.

**DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
A clustering algorithm that groups densely connected points together and marks sparse outlier points as noise. Does not require specifying K and handles non-spherical cluster shapes.

**Dimensionality Reduction**
An unsupervised technique that transforms high-dimensional data into a lower-dimensional representation while preserving as much information as possible.

**Principal Component Analysis (PCA)**
A linear dimensionality reduction algorithm that projects data onto orthogonal axes (principal components) ordered by the variance they explain.

**Principal Component**
A linear combination of original features that represents a direction of maximum variance in the data. The first principal component captures the most variance; subsequent components capture decreasing amounts of remaining variance.

**Curse of Dimensionality**
The phenomenon where data becomes increasingly sparse as the number of features grows, causing distance-based algorithms to become less effective and models to require exponentially more data.

**t-SNE (t-distributed Stochastic Neighbor Embedding)**
A non-linear dimensionality reduction technique used exclusively for 2D or 3D visualization. Preserves local neighborhood structure but is not suitable for preprocessing before model training.

**Anomaly Detection**
An unsupervised (or semi-supervised) task that identifies data points that deviate significantly from the expected distribution. Used for fraud detection, equipment fault detection, and network intrusion detection.

**Isolation Forest**
An anomaly detection algorithm that assigns anomaly scores based on how quickly a data point can be isolated through random recursive partitioning. Anomalies are isolated faster than normal points.

**Inertia**
Synonym for WCSS. The sum of squared distances between data points and their assigned cluster centroids.

**Dendrogram**
A tree diagram produced by hierarchical clustering that shows the nested structure of cluster merges. The height of each merge indicates the distance between the merged clusters.

---

## Section 2: Comparison Tables

### Table 1: Clustering Algorithms

| Algorithm | K Required | Cluster Shape | Handles Noise | Best Use Case | Azure ML Support |
|---|---|---|---|---|---|
| K-means | Yes (specify before running) | Spherical, similar sizes | No | Large datasets, well-separated groups | Yes (default clustering algorithm) |
| Hierarchical | No (cut dendrogram at desired level) | Any shape | No | Small datasets, need to explore cluster hierarchy | Limited |
| DBSCAN | No (uses density parameters) | Arbitrary shapes | Yes (noise points labeled -1) | Data with irregular cluster shapes and outliers | Via custom code |
| Gaussian Mixture Model | Yes (number of components) | Ellipsoidal | Partial | Probabilistic cluster assignments needed | Via custom code |

### Table 2: Dimensionality Reduction Techniques

| Technique | Linear | Use Case | Interpretability | Suitable for Preprocessing |
|---|---|---|---|---|
| PCA | Yes | Feature compression, visualization, noise reduction | Low (components are combinations of features) | Yes |
| t-SNE | No | Visualization only (2D/3D) | Very low | No — computationally expensive and non-deterministic |
| UMAP | No | Visualization and some preprocessing | Low | Limited |
| Feature Selection | N/A | Keep original features most predictive of target | High (original features retained) | Yes |

### Table 3: Supervised vs Unsupervised Learning — Extended Comparison

| Aspect | Supervised | Unsupervised |
|---|---|---|
| Labels required | Yes | No |
| Evaluation | Objective (compare to known correct labels) | Subjective (requires domain expertise to interpret clusters) |
| Primary goal | Predict known outcomes | Discover unknown structure |
| Common failure | Overfitting or underfitting to labels | Choosing wrong K; clusters without practical meaning |
| Azure ML task type | Classification, Regression, Forecasting | Clustering |
| Typical output | A predicted label or value | Cluster assignments, reduced-dimension representations |
| Human role during evaluation | Compute accuracy/F1/RMSE against truth | Inspect cluster centroids and assign meaningful names |

### Table 4: Anomaly Detection Methods

| Approach | Labels Needed | Method | Best When |
|---|---|---|---|
| Isolation Forest | No | Anomaly score from random partitioning | General tabular anomaly detection |
| One-Class SVM | No | Learns tight boundary around normal class | High-dimensional data |
| Autoencoder (neural network) | No | Learns to reconstruct normal data; flags high reconstruction error | Complex unstructured data |
| Statistical threshold | No | Flag points beyond N standard deviations from mean | Simple univariate time series |
| Azure Anomaly Detector | No | Ensemble of statistical methods tuned per series | Time series anomaly detection via API |

---

## Section 3: K-means Algorithm in Detail

Understanding K-means at the step level is important for the AI-900 exam and for the lab activity.

**Initialization:** Select K initial centroids. Common methods are random selection from the data points, or K-means++ initialization which spaces initial centroids more evenly.

**Assignment step:** Assign each data point to the nearest centroid using Euclidean distance.

**Update step:** Move each centroid to the mean position of all points currently assigned to it.

**Convergence:** Repeat the assignment and update steps until centroid positions change by less than a tolerance threshold, or until a maximum iteration count is reached.

**Result:** K clusters, each defined by a centroid, with every data point assigned to exactly one cluster.

**Selecting K with the elbow method:**

1. Run K-means for K = 1, 2, 3, ..., 10 (or more).
2. Record the WCSS for each K.
3. Plot WCSS vs K. The curve always decreases; look for the point where the slope flattens sharply.
4. Select the K at the elbow as the best balance between cluster quality and simplicity.

---

## Section 4: PCA Algorithm in Detail

PCA is a linear algebra procedure. Understanding the conceptual steps helps you apply it correctly.

**Step 1 — Standardize:** PCA is sensitive to feature scale. Before applying PCA, standardize each feature to have mean 0 and standard deviation 1. This ensures that features measured in different units (dollars vs. counts vs. percentages) contribute equally.

**Step 2 — Compute covariance matrix:** Calculate the covariance between every pair of features. This matrix captures how features vary together.

**Step 3 — Find eigenvectors and eigenvalues:** The eigenvectors of the covariance matrix are the principal components. The eigenvalues tell you how much variance each component explains.

**Step 4 — Sort by variance explained:** Sort the principal components by their eigenvalues in descending order. The first component explains the most variance.

**Step 5 — Project the data:** Choose how many components to keep based on the cumulative variance explained. Project the original data onto the selected components.

**Interpreting explained variance:** A scree plot shows the proportion of variance explained by each principal component. A common rule of thumb is to keep enough components to explain 80-95% of total variance.

---

## Section 5: Azure ML Clustering Experiments

Azure Machine Learning supports clustering experiments through both the Designer (visual drag-and-drop) and the Python SDK. Key facts for AI-900:

Azure ML implements K-means clustering as the primary clustering algorithm. The hyperparameter you configure is the number of clusters K.

Evaluation metrics available after running a clustering experiment include:

- **Average Distance to Cluster Center:** The mean distance of all points to their assigned centroid. Lower is better.
- **Average Distance to Other Center:** The mean distance of all points to the nearest centroid they are not assigned to. Higher is better (means clusters are well-separated).
- **Number of Points:** The count of data points assigned to each cluster. Very imbalanced counts can indicate poor K selection.
- **Maximum Distance to Cluster Center:** The farthest any point lies from its assigned centroid. Very large values indicate outliers in a cluster.

When you train a clustering model in Azure ML Designer, the trained model can be used to assign new data points to the discovered clusters — useful for real-time customer segmentation.

---

## Section 6: Unsupervised Learning in Practice

### Real-World Applications

**Customer Segmentation:** Retailers, banks, and streaming platforms cluster customers by behavioral features to tailor marketing, pricing, and product recommendations.

**Document Topic Modeling:** Unsupervised algorithms like Latent Dirichlet Allocation discover latent topics in large text corpora without predefined topic labels.

**Genomics:** Researchers cluster gene expression profiles to discover subtypes of diseases that may respond differently to treatments.

**Image Compression:** K-means can compress images by replacing each pixel color with the nearest cluster centroid color.

**Network Intrusion Detection:** Isolation Forest and one-class SVM learn normal network traffic patterns and flag deviations as potential security events.

### Limitations to Know for AI-900

Unsupervised learning results are inherently subjective. Two practitioners may interpret the same clusters differently. This subjectivity is a genuine limitation when objective performance measurement is required.

K-means requires K to be specified in advance and does not guarantee a globally optimal solution — only a locally optimal one. Different random initializations can produce different results.

PCA components are mathematical constructs with no inherent business meaning. A principal component that explains 40% of variance may represent a combination of age, income, and tenure that is difficult to interpret.

---

## Section 7: AI-900 Exam Tips

1. Clustering is the primary unsupervised ML task tested on AI-900. Know K-means, the elbow method, and silhouette score.

2. The absence of labels is the defining criterion for unsupervised learning. If a scenario says "no labeled data available" or "discover natural groupings," the answer is unsupervised/clustering.

3. PCA is for dimensionality reduction and preprocessing, not for clustering or prediction by itself.

4. t-SNE is for visualization only. Never select t-SNE when a scenario asks for a preprocessing technique to use before model training.

5. Azure ML's clustering task type is evaluated using WCSS/inertia and silhouette score. Know what each metric means.

6. Anomaly detection is an AI-900 workload category distinct from clustering. Azure Anomaly Detector is the Cognitive Service for time series anomaly detection.

7. DBSCAN does not require specifying K and handles irregular cluster shapes and noise. If a scenario describes irregularly shaped clusters or data with many outliers, DBSCAN is preferable to K-means.

8. Silhouette score ranges from -1 to 1. A score near 1 is excellent; near 0 is ambiguous; negative values indicate misassignment.

---

## Section 8: Required Reading

**Microsoft Learn — Train and evaluate clustering models**
learn.microsoft.com/en-us/training/modules/train-evaluate-cluster-models/

This module covers K-means clustering, evaluation metrics, and the Azure ML clustering experiment workflow. Complete all units and the knowledge check.

**Microsoft Learn — Detect and analyze anomalies with Azure Anomaly Detector**
learn.microsoft.com/en-us/training/modules/intro-to-anomaly-detector/

Covers the Azure Cognitive Services Anomaly Detector API and its relationship to unsupervised anomaly detection.

**Microsoft Learn — Explore and analyze data with Python (optional enrichment)**
learn.microsoft.com/en-us/training/modules/explore-analyze-data-with-python/

Provides practical context for working with the types of datasets used in clustering experiments.

---

## Section 9: Study Checklist

- [ ] Write the definition of clustering, K-means, WCSS, silhouette score, and PCA from memory.
- [ ] Walk through the K-means algorithm steps on a small example without looking at your notes.
- [ ] Complete the Microsoft Learn module: Train and evaluate clustering models.
- [ ] Study Table 1 (clustering algorithm comparison) and identify which algorithm to recommend in at least three different scenarios.
- [ ] Study Table 2 (dimensionality reduction techniques) and explain why t-SNE cannot be used for preprocessing.
- [ ] Explain the curse of dimensionality in your own words.
- [ ] Review all eight AI-900 exam tips in Section 7.
- [ ] Complete the Module 03 quiz.
- [ ] Complete the Module 03 lab activity.
- [ ] Post initial discussion by Wednesday 11:59 PM and respond to two peers by Sunday 11:59 PM.

## 10. Supplemental Resources

**1. Scikit-learn Documentation — Clustering User Guide**
<https://scikit-learn.org/stable/modules/clustering.html>
The official scikit-learn reference for all clustering algorithms including K-means, DBSCAN, and hierarchical clustering. Includes algorithm comparisons, parameter guidance, and code examples that directly support the Module 03 lab.

**2. Distill.pub — How to Use t-SNE Effectively**
<https://distill.pub/2016/misread-tsne/>
An interactive visual essay explaining how t-SNE parameters affect output and the common misinterpretations of t-SNE plots. Essential reading before using t-SNE for data exploration — helps students understand why t-SNE is for visualization only.

**3. Towards Data Science — PCA Explained Visually**
<https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c>
A comprehensive illustrated guide to Principal Component Analysis covering the math, interpretation of components, explained variance, and practical guidelines for choosing how many components to retain. Complements the Module 03 dimensionality reduction content.

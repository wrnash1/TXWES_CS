# Video Script: Module 03 - Unsupervised Learning: Clustering and Dimensionality Reduction

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AI-900 Domain:** Describe fundamental principles of machine learning on Azure (20-25%)

---

## [00:00 - 01:30] Opening

Welcome back. Professor Nash here, and this is Module 03 of CIS-4330. In the last two modules we covered the full landscape of AI and machine learning and went deep on supervised learning — regression, classification, and key algorithms. Today we focus exclusively on unsupervised learning, with a detailed look at clustering and dimensionality reduction.

These topics appear on the AI-900 exam in the context of Azure ML clustering experiments and in scenarios where you need to identify when unsupervised learning is the right approach. They also connect to anomaly detection workloads, which are a distinct AI-900 exam category. Let us get into it.

---

## [01:30 - 05:00] Why Unsupervised Learning Matters

Let me start with an honest question: why would you ever want to train a model without labels? Labels are the answer key. They tell the algorithm what is correct. Why would you intentionally remove that guidance?

The answer is practical. In many real-world situations, labels do not exist or are impossibly expensive to create.

Consider a global bank with 50 million customers. A data analyst wants to understand whether different groups of customers have meaningfully different banking needs. Should the bank segment customers by transaction frequency? By average balance? By the mix of products they hold? The analyst does not know in advance what the meaningful segments are. There are no "correct" segments to train toward. The goal is to discover whatever structure the data contains and then decide what to do with it.

That is the unsupervised learning use case: exploration and discovery. You are not training toward a known answer. You are asking the algorithm to reveal the shape of the data.

Unsupervised learning is also used as a preprocessing step for supervised learning. By reducing the dimensionality of high-dimensional data, or by identifying unusual data points before training, you can improve the performance of downstream supervised models.

The AI-900 exam tests unsupervised learning primarily in two contexts: clustering as a standalone ML task type in Azure Machine Learning, and anomaly detection as a distinct AI workload. We will return to anomaly detection later in the course. Today, we focus on clustering and dimensionality reduction.

---

## [05:00 - 10:00] Clustering — K-means in Depth

[SHOW DIAGRAM: Four-panel sequence. Panel 1: scattered unlabeled points. Panel 2: same points with 3 random centroids marked. Panel 3: points colored by nearest centroid, centroids moved to cluster means. Panel 4: final stable clusters with clean color boundaries.]

Clustering is the most important unsupervised task for AI-900. The goal is to partition data points into groups — called clusters — such that points within a cluster are more similar to each other than to points in other clusters.

K-means is the standard clustering algorithm. Let me walk through it step by step with a concrete example.

Imagine you are a marketing analyst at a subscription software company. You have data on 10,000 customers: number of logins per week, number of features used, contract value in dollars, and number of support tickets submitted. You want to understand whether distinct customer profiles exist.

Step one: choose K. You decide to try K = 3 clusters first and will refine later. Step two: the algorithm randomly places 3 centroids in the four-dimensional feature space. Step three: every customer is assigned to the nearest centroid based on Euclidean distance — the straight-line distance between the customer's feature vector and each centroid. Step four: each centroid is moved to the arithmetic mean of all customer points assigned to it. Step five: steps three and four repeat until the centroid positions change by less than a small threshold.

When the algorithm converges, you examine each cluster. Cluster one might contain customers with high logins, many features used, high contract value, and few support tickets — you name this cluster "Power Users." Cluster two has low logins, few features, low contract value, and many support tickets — "At-Risk Churners." Cluster three has moderate logins and features, medium contract value, few tickets — "Healthy Mid-Market."

Notice that the algorithm did not create these names. You did. Unsupervised learning reveals structure; humans provide interpretation.

---

## [10:00 - 13:00] Choosing K and Evaluating Clustering Quality

[SHOW DIAGRAM: Line graph with K on the x-axis from 1 to 10 and "Within-Cluster Sum of Squares (WCSS)" on the y-axis. The curve drops sharply from K=1 to K=3, then levels off. An arrow points to K=3 labeled "The Elbow."]

The weakness of K-means is that you must specify K before running the algorithm. Choosing K too small merges distinct groups. Choosing K too large splits natural groups into artificial fragments.

The elbow method is the standard heuristic for choosing K. You run K-means for several values of K — say, K = 1 through 10. For each K, you calculate the Within-Cluster Sum of Squares, or WCSS — the total sum of squared distances between each data point and its cluster centroid. As K increases, WCSS always decreases, because more clusters means each point is closer to its centroid. But the rate of improvement slows as K grows past the point of diminishing returns.

You plot WCSS against K and look for the "elbow" — the point where the curve bends sharply and the rate of decrease slows. If the elbow appears at K = 3, that suggests 3 is the optimal number of clusters for this data.

Two other limitations of K-means are worth knowing for AI-900.

First, K-means is sensitive to initial centroid placement. Different random starting positions can produce different final clusters. The solution is to run K-means multiple times with different random seeds and select the run with the lowest final WCSS.

Second, K-means assumes clusters are approximately spherical and equally sized. For elongated, irregularly shaped, or very different-sized clusters, DBSCAN or hierarchical clustering may be more appropriate.

---

## [13:00 - 16:00] Dimensionality Reduction with PCA

[SHOW DIAGRAM: Left side shows a cloud of points in 3D space with three labeled axes: Feature 1, Feature 2, Feature 3. An arrow points right. Right side shows the same cloud projected onto a 2D plane with two axes labeled PC1 and PC2. Label: "PCA reduces 3 features to 2 principal components."]

Real datasets often have dozens, hundreds, or even thousands of features. High dimensionality creates several problems.

The curse of dimensionality: as the number of dimensions increases, data becomes increasingly sparse. Points that seemed close in low dimensions become farther apart. Clustering and distance-based algorithms lose effectiveness.

Visualization: you cannot directly visualize data in more than three dimensions. To explore or communicate findings about high-dimensional data, you need to reduce it to 2 or 3 dimensions first.

Computation: models trained on high-dimensional data are slower to train and more prone to overfitting.

Principal Component Analysis — PCA — addresses all three problems. PCA transforms the original features into a new set of uncorrelated variables called principal components, ordered by how much variance in the original data they explain.

Here is the key insight: the first principal component points in the direction of greatest variance in the data. The second principal component points in the direction of greatest remaining variance, orthogonal to the first. And so on. By keeping only the first few principal components, you retain most of the information in the data using far fewer dimensions.

For example, if you have 100 features in a customer dataset, PCA might reveal that the first 5 principal components explain 85% of the variance. You can replace 100 features with 5 principal components and retain the vast majority of the information for downstream analysis.

The trade-off: principal components are linear combinations of the original features and are less interpretable than the original features. You sacrifice the ability to say "this axis represents age" for the ability to say "this axis captures the most variance in the data."

---

## [16:00 - 18:30] Other Dimensionality Reduction and Anomaly Detection

Beyond PCA, two other techniques are worth knowing for this course.

**t-SNE** — t-distributed Stochastic Neighbor Embedding — is a dimensionality reduction technique designed specifically for 2D and 3D visualization. Unlike PCA, which finds linear projections, t-SNE preserves local neighborhood relationships, making it excellent for visualizing cluster structure. It is not used for preprocessing before modeling — only for visualization.

**Isolation Forest** is an unsupervised anomaly detection algorithm. Rather than learning the normal distribution and flagging outliers, it works by randomly partitioning the data. Anomalies — points that are isolated from the rest — require fewer partitions to separate. The algorithm assigns each point an anomaly score based on how quickly it was isolated. Points with the highest anomaly scores are flagged as outliers.

Azure Machine Learning includes an anomaly detection capability that uses statistical models to identify data points that deviate significantly from the expected distribution. This capability connects to the broader Azure Cognitive Services Anomaly Detector, which we will explore in a later module.

---

## [18:30 - 21:00] Azure ML Clustering Experiment Walkthrough

In Azure Machine Learning, you can run a clustering experiment using the Designer visual interface or via code. The workflow is:

Step one: register a dataset in Azure ML. Step two: create a new experiment and select the clustering task type. Step three: add a clustering component — K-means is the default. Step four: configure the number of clusters and other hyperparameters. Step five: connect the dataset to the clustering component and run the experiment. Step six: review the cluster centroids and evaluate cluster quality using inertia (WCSS) and silhouette score.

The silhouette score measures how similar each point is to its own cluster compared to the nearest other cluster. It ranges from -1 to 1. A value near 1 means the point is well within its cluster and far from others. A value near 0 means the point is on or near the boundary between clusters. A negative value means the point may have been assigned to the wrong cluster.

For AI-900, remember that Azure ML supports clustering as a task type, and that WCSS and silhouette score are the primary evaluation metrics for clustering quality.

---

## [21:00 - 22:30] Module Summary and Lab Preview

Let us summarize Module 03.

Unsupervised learning discovers structure in data without labels. The primary task is clustering: grouping similar data points together. K-means is the standard clustering algorithm; the elbow method helps select K. K-means limitations include sensitivity to initial centroids and assumption of spherical clusters.

Dimensionality reduction compresses high-dimensional data while preserving information. PCA finds the directions of maximum variance and projects data onto them. t-SNE is used for visualization only.

Anomaly detection identifies data points that deviate significantly from the normal distribution, using unsupervised methods when labeled anomalies are unavailable.

Azure ML supports clustering as a task type, evaluated by WCSS and silhouette score.

This week's lab asks you to trace through a K-means iteration by hand on a small dataset, apply the elbow method conceptually, and evaluate clustering quality using provided metrics. Working through K-means manually builds the intuition you need to answer AI-900 scenario questions accurately.

See you in Module 04, where we move into neural networks and deep learning.

---

## References

- Microsoft Learn — Train and evaluate clustering models: learn.microsoft.com/en-us/training/modules/train-evaluate-cluster-models/
- Microsoft Learn — Detect and analyze anomalies with Azure AI: learn.microsoft.com/en-us/training/modules/intro-to-anomaly-detector/

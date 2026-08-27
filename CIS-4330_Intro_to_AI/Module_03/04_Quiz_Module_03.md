# Quiz: Module 03 - Unsupervised Learning: Clustering and Dimensionality Reduction

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe fundamental principles of machine learning on Azure
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

Which of the following best describes the K-means clustering algorithm?

- A) It trains a model on labeled data to predict which cluster a new point belongs to.
- B) It iteratively assigns points to the nearest centroid and recalculates centroids until assignments stabilize.
- C) It builds a hierarchical tree of clusters by splitting the data at the point of maximum variance.
- D) It uses a neural network to encode data points into a lower-dimensional cluster space.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* K-means alternates between the assignment step (assign each point to nearest centroid) and the update step (recalculate centroid as the mean of assigned points) until convergence. This is the precise definition of the algorithm.
- *Why A is incorrect:* K-means is unsupervised and does not use labeled data. After training, it can assign new points, but the learning itself is unsupervised.
- *Why C is incorrect:* This describes hierarchical clustering, which builds a dendrogram by merging or splitting. K-means does not produce a tree structure.
- *Why D is incorrect:* K-means is not a neural network. It uses geometric distance calculations, not learned representations.

---

## Question 2

A data scientist runs K-means for K values from 1 to 8 and records the Within-Cluster Sum of Squares (WCSS) for each. The WCSS values decrease steeply from K=1 to K=3, then only marginally from K=3 onward. What does this pattern indicate?

- A) The algorithm failed to converge because WCSS should always increase with more clusters.
- B) K=3 is the optimal number of clusters, as indicated by the elbow in the WCSS curve.
- C) K=8 should be selected because it has the lowest WCSS.
- D) The data has no meaningful cluster structure because WCSS decreases at all values of K.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The elbow method identifies the K value where the rate of WCSS decrease slows sharply. A steep drop through K=3 followed by marginal improvement indicates that K=3 captures the meaningful structure; additional clusters provide little benefit.
- *Why A is incorrect:* WCSS always decreases as K increases — this is expected behavior, not a failure. At K equal to the number of data points, WCSS is zero.
- *Why C is incorrect:* Selecting K=8 for lowest WCSS ignores parsimony. The goal is the best balance between cluster quality and simplicity, not minimum WCSS at any cost.
- *Why D is incorrect:* A steep initial drop followed by flattening actually indicates strong cluster structure in the data, not its absence.

---

## Question 3

Which metric measures how similar a data point is to its own cluster compared to the nearest other cluster, with values ranging from -1 to 1?

- A) Within-Cluster Sum of Squares (WCSS)
- B) Root Mean Squared Error (RMSE)
- C) Silhouette score
- D) R-squared

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The silhouette score evaluates cluster quality at the individual point level by comparing intra-cluster distance to nearest-cluster distance. A score near 1 means the point is well within its cluster.
- *Why A is incorrect:* WCSS measures the total squared distances from points to their centroids but does not compare cluster separation.
- *Why B is incorrect:* RMSE is a regression metric that measures prediction error. It is not used for clustering evaluation.
- *Why D is incorrect:* R-squared measures explained variance in regression models. It is not a clustering metric.

---

## Question 4

A company has customer data with 250 features and wants to reduce this to 15 features before training a classification model. The team wants to preserve as much variance as possible and needs the result to be usable as input to another algorithm. Which technique is most appropriate?

- A) t-SNE
- B) K-means clustering
- C) DBSCAN
- D) PCA

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* PCA reduces dimensionality by projecting onto variance-maximizing principal components. The result is a lower-dimensional feature matrix that can serve as input to classification algorithms.
- *Why A is incorrect:* t-SNE is for visualization only. It produces 2D or 3D output for visual exploration and is not suitable as a preprocessing step before model training.
- *Why B is incorrect:* K-means produces cluster assignments, not a reduced-dimension feature matrix.
- *Why C is incorrect:* DBSCAN produces cluster assignments and noise labels. It does not reduce the dimensionality of the feature space.

---

## Question 5

Which of the following is a key limitation of K-means that DBSCAN addresses?

- A) K-means cannot handle large datasets, while DBSCAN scales to millions of points.
- B) K-means requires spherical, similarly sized clusters, while DBSCAN can find clusters of arbitrary shape.
- C) K-means requires labeled data, while DBSCAN is unsupervised.
- D) K-means only works in two dimensions, while DBSCAN works in any number of dimensions.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* K-means assumes spherical clusters of similar size because it uses Euclidean distance to a centroid. DBSCAN defines clusters as dense regions and can identify elongated, irregular, or concave cluster shapes.
- *Why A is incorrect:* Both algorithms scale to large datasets. K-means is generally faster on large datasets than DBSCAN.
- *Why C is incorrect:* Both K-means and DBSCAN are unsupervised. Neither requires labeled data.
- *Why D is incorrect:* K-means operates in any number of dimensions. The two-dimension limitation does not exist.

---

## Question 6

A network security team wants to detect unusual connections in network traffic logs. No labeled examples of intrusions are available — only normal traffic data from the past year. Which approach is most appropriate?

- A) Train a supervised binary classification model on the normal traffic data.
- B) Apply unsupervised anomaly detection to learn the distribution of normal traffic and flag deviations.
- C) Use Azure AutoML with a classification task type and the normal traffic data as a training set.
- D) Apply hierarchical clustering and label the smallest cluster as "malicious."

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Without labeled anomaly examples, unsupervised anomaly detection is the appropriate approach. The algorithm learns what normal looks like and flags statistical deviations.
- *Why A is incorrect:* Binary classification requires labeled examples of both classes. No intrusion labels exist, so a supervised model cannot be trained.
- *Why C is incorrect:* AutoML classification requires labeled training data with both positive and negative class examples.
- *Why D is incorrect:* Assuming the smallest cluster is "malicious" is an unfounded assumption. The smallest cluster may represent a rare but legitimate behavior pattern.

---

## Question 7

After running PCA on a 100-feature dataset, a data scientist finds that the first 5 principal components explain 91% of the total variance. What is the most appropriate interpretation?

- A) 91% of the original data can be discarded because it is not statistically significant.
- B) 5 components capture most of the data's variability and are sufficient for most downstream tasks, with 9% of variance lost.
- C) The original 100 features were all identical, since most variance is captured in just 5 components.
- D) PCA failed because fewer than 100 components were needed to explain 100% of the variance.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Retaining 91% of variance in 5 components means the reduced representation preserves most information. The remaining 9% represents variance not captured — potentially noise or low-signal features.
- *Why A is incorrect:* The remaining 9% is lost information, not irrelevant data to discard. The decision to accept this loss depends on the task.
- *Why C is incorrect:* High concentration of variance in few components indicates correlated features, not identical features.
- *Why D is incorrect:* The goal of PCA is to explain most variance with far fewer components. Achieving 91% with 5 components out of 100 is a successful dimensionality reduction outcome.

---

## Question 8

A retailer has clustered its customers into four segments using K-means. The business team reviews the centroids and names the segments: "Bargain Hunters," "Loyalty Shoppers," "Seasonal Buyers," and "Lapsed Customers." What does this naming process demonstrate about unsupervised learning?

- A) It demonstrates that unsupervised learning produces incorrect results that must be corrected by humans.
- B) It demonstrates that the cluster labels produced by K-means are arbitrary and meaningless.
- C) It demonstrates that unsupervised learning discovers structure in data, but humans must interpret and name that structure.
- D) It demonstrates that supervised classification is always more useful than clustering for customer data.

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Unsupervised learning discovers the mathematical grouping; the business meaning comes from human interpretation. The algorithm identifies that these four groups exist and are distinct; humans determine what they represent.
- *Why A is incorrect:* The clusters are not incorrect — they reflect genuine patterns in the data. The naming step is interpretation, not correction.
- *Why B is incorrect:* Cluster labels (e.g., cluster 0, 1, 2, 3) are arbitrary identifiers, but the clusters themselves represent real data structure. The business names give them meaning.
- *Why D is incorrect:* The scenario does not compare methods. Clustering and classification serve different purposes and are both valuable.

---

## Question 9

In Azure Machine Learning, which task type should be selected to train a K-means clustering model using the AutoML or Designer interface?

- A) Classification
- B) Regression
- C) Clustering
- D) Time Series Forecasting

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure ML explicitly supports a "Clustering" task type for training K-means models through the Designer and SDK. This is a direct AI-900 exam fact.
- *Why A is incorrect:* Classification is a supervised task type for predicting discrete labels.
- *Why B is incorrect:* Regression is a supervised task type for predicting continuous values.
- *Why D is incorrect:* Time Series Forecasting is for predicting sequential future values, not for grouping unlabeled data.

---

## Question 10

Which of the following statements about the curse of dimensionality is correct?

- A) As the number of features increases, models always become more accurate because they have more information.
- B) As the number of features increases, data becomes increasingly sparse and distance-based algorithms lose effectiveness.
- C) The curse of dimensionality only affects deep learning models and does not impact traditional ML algorithms.
- D) The curse of dimensionality is resolved by increasing the number of training examples to match the number of features.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* In high dimensions, data points become increasingly spread out. The concept of "nearness" breaks down because all points become approximately equally distant from each other. K-means, KNN, and other distance-based methods degrade.
- *Why A is incorrect:* More features do not always improve accuracy. Irrelevant features add noise, and high dimensionality increases sparsity and overfitting risk.
- *Why C is incorrect:* The curse of dimensionality affects all machine learning approaches. Distance-based classical methods like KNN are particularly vulnerable.
- *Why D is incorrect:* The number of training examples needed grows exponentially with dimensionality. Practically, adding enough examples to fully counter high dimensionality is infeasible.

---

### Question 11 (5 points)

A data scientist runs DBSCAN on a geographic dataset of store locations and finds that some points are labeled as noise (label = -1). What does the noise label indicate in DBSCAN?

- A) The points were incorrectly loaded and should be removed from the dataset.
- B) The points do not belong to any dense region and cannot be assigned to any cluster.
- C) The points are the cluster centroids and will be used for future assignment of new data.
- D) The points belong to the largest cluster but are flagged as lower-confidence members.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In DBSCAN, a noise point (also called an outlier) is a point that does not have enough neighbors within the epsilon radius to qualify as a core point and is not within epsilon of any core point. It belongs to no cluster and is assigned label -1.
  - *Why A is incorrect:* Noise in DBSCAN is a meaningful classification result, not a data error. These points may represent genuine outliers with business significance (e.g., unusual store locations).
  - *Why C is incorrect:* DBSCAN does not use centroids. That concept belongs to K-means. DBSCAN defines clusters through density reachability.
  - *Why D is incorrect:* DBSCAN does not assign confidence levels to cluster members. Points either belong to a cluster or are labeled noise.

---

### Question 12 (5 points)

Which of the following scenarios is MOST appropriate for hierarchical clustering rather than K-means?

- A) Segmenting 2 million e-commerce customers into exactly 5 known marketing segments as quickly as possible.
- B) Exploring the natural grouping structure of 200 biological specimens where the number of groups is unknown and a tree-based visualization of relationships is needed.
- C) Partitioning sensor readings from 500,000 IoT devices into 3 operational categories.
- D) Reducing the dimensionality of 300 gene expression features before a classification task.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Hierarchical clustering does not require specifying K in advance and produces a dendrogram — a tree-based visualization of cluster relationships at multiple levels of granularity. This is ideal for exploratory biological analysis with unknown group structure.
  - *Why A is incorrect:* K-means is faster and more scalable for large datasets when the desired number of clusters is known. Hierarchical clustering on 2 million records would be computationally prohibitive.
  - *Why C is incorrect:* Large-scale partitioning into a fixed number of categories with speed as a priority favors K-means.
  - *Why D is incorrect:* Dimensionality reduction is the purpose of PCA, not clustering algorithms.

---

### Question 13 (5 points)

A machine learning team applies PCA to a 50-feature dataset and retains components explaining 95% of variance. They then train a logistic regression model on the reduced features. What is the PRIMARY benefit of this PCA preprocessing step?

- A) PCA guarantees the logistic regression model will achieve higher accuracy than without preprocessing.
- B) PCA removes correlated and low-variance features, reducing overfitting risk and computational cost while retaining most information.
- C) PCA converts the numerical features into categorical variables, making them compatible with logistic regression.
- D) PCA ensures that the logistic regression model does not require a train-test split.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* PCA reduces correlated and low-variance dimensions into a compact set of uncorrelated components. This lowers the risk of overfitting from irrelevant features and speeds up training while retaining 95% of the original information.
  - *Why A is incorrect:* PCA does not guarantee higher accuracy. In some cases the 5% dropped variance contains signal, and PCA may slightly reduce accuracy. The primary benefit is efficiency and generalization, not guaranteed accuracy improvement.
  - *Why C is incorrect:* PCA transforms numerical features into different numerical features (principal components). It does not convert numerical to categorical data.
  - *Why D is incorrect:* PCA has no effect on the requirement for a train-test split. Good evaluation practice requires a split regardless of preprocessing.

---

### Question 14 (5 points)

What does "inertia" (within-cluster sum of squares) measure in K-means, and what does a lower inertia value indicate?

- A) Inertia measures the distance between cluster centroids; lower inertia means clusters are farther apart.
- B) Inertia measures total squared distances from each point to its assigned centroid; lower inertia means points are closer to their centroids and clusters are more compact.
- C) Inertia measures the total number of iterations required for convergence; lower inertia means faster training.
- D) Inertia measures model accuracy on labeled validation data; lower inertia means better predictions.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Inertia is the sum of squared Euclidean distances from each data point to the centroid of its assigned cluster, summed across all clusters. Lower inertia indicates more compact, tightly grouped clusters.
  - *Why A is incorrect:* Inter-cluster distances are measured by metrics like the Davies-Bouldin index, not inertia. Inertia measures within-cluster distances only.
  - *Why C is incorrect:* Inertia has nothing to do with training speed or iteration count. It is a cluster quality measure, not a computational efficiency measure.
  - *Why D is incorrect:* K-means is unsupervised. There is no labeled validation data, and inertia measures geometric compactness, not prediction accuracy.

---

### Question 15 (5 points)

An analyst wants to reduce a high-dimensional genomics dataset to two dimensions specifically to create a scatter plot that reveals how data points group visually — with no intention of using the result as input to another algorithm. Which technique is MOST appropriate?

- A) PCA
- B) K-means
- C) t-SNE
- D) DBSCAN

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* t-SNE is specifically designed for high-dimensional data visualization. It preserves local neighborhood structure and produces 2D plots that reveal cluster patterns far more clearly than PCA for complex datasets. It is the correct choice when visualization — not downstream modeling — is the goal.
  - *Why A is incorrect:* PCA can reduce to 2D but preserves global variance structure, not local neighborhood relationships. For visualization of cluster patterns, t-SNE typically produces more interpretable plots.
  - *Why B is incorrect:* K-means performs clustering (group assignment), not dimensionality reduction for visualization.
  - *Why D is incorrect:* DBSCAN performs density-based clustering, not dimensionality reduction. It produces cluster labels, not a 2D visualization.

---

### Question 16 (5 points)

A data scientist is comparing the quality of three different K-means solutions (K=3, K=5, K=7) using the silhouette score. The scores are: K=3: 0.68, K=5: 0.71, K=7: 0.52. Which K should be selected and why?

- A) K=3, because fewer clusters always produce higher-quality results.
- B) K=7, because more clusters always explain more of the data's structure.
- C) K=5, because it has the highest silhouette score, indicating the best balance of cohesion and separation.
- D) K=3, because the WCSS is lowest for the smallest K value.

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* The silhouette score measures intra-cluster cohesion relative to inter-cluster separation. K=5 achieves the highest score (0.71), indicating that with 5 clusters, data points are most tightly grouped within their clusters relative to neighboring clusters.
  - *Why A is incorrect:* Fewer clusters do not always produce better silhouette scores. K=3 (0.68) scores lower than K=5 (0.71), disproving this claim.
  - *Why B is incorrect:* More clusters do not guarantee better cluster quality. K=7 (0.52) performs worse than K=5, showing that over-segmentation reduces cluster coherence.
  - *Why D is incorrect:* WCSS always decreases with more clusters, so K=3 would not have the lowest WCSS. Silhouette score — not WCSS alone — is used to compare K values here.

---

### Question 17 (5 points)

Which of the following best describes the purpose of the Azure Anomaly Detector cognitive service?

- A) It trains custom clustering models on structured datasets uploaded to Azure.
- B) It applies pre-built time series anomaly detection to identify unusual patterns in sequential data without requiring custom model training.
- C) It performs principal component analysis on tabular datasets to reduce feature dimensionality.
- D) It builds classification models to distinguish normal from anomalous data using labeled training examples.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Anomaly Detector is a prebuilt Cognitive Service that detects anomalies in time series data through a REST API. No custom model training is required. It is used for monitoring metrics, KPIs, and sequential sensor readings.
  - *Why A is incorrect:* Custom clustering model training is the domain of Azure Machine Learning, not a Cognitive Service. Azure Anomaly Detector is a prebuilt API.
  - *Why C is incorrect:* PCA is a statistical algorithm implemented in ML libraries. Azure Anomaly Detector does not perform PCA.
  - *Why D is incorrect:* Azure Anomaly Detector is unsupervised — it does not require labeled anomaly examples. It detects deviations from learned normal patterns.

---

### Question 18 (5 points)

A manufacturing plant has sensor data for 10,000 machines with 80 sensor readings per machine. The team finds that the clustering model runs slowly and many clusters appear to merge at high K values. Which preprocessing step would MOST directly address this problem?

- A) Increase K to create more clusters.
- B) Apply PCA to reduce the 80 sensor readings to the top components explaining 90% of variance before clustering.
- C) Switch from K-means to a supervised classification algorithm.
- D) Remove all data points that fall below the median sensor value.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* 80 features in a distance-based algorithm like K-means leads to the curse of dimensionality — distances become less meaningful and cluster separation degrades. PCA reduces the feature space to the most informative components, improving cluster quality and training speed.
  - *Why A is incorrect:* Increasing K makes the computational problem worse, not better. More clusters in high dimensions would further degrade quality.
  - *Why C is incorrect:* If no labeled data exists, supervised classification is not applicable. The problem is dimensionality, not task type.
  - *Why D is incorrect:* Removing data based on median value is an arbitrary data removal strategy that destroys information without addressing the dimensionality problem.

---

### Question 19 (5 points)

What is the key difference between how K-means and DBSCAN handle outlier data points?

- A) K-means ignores outliers entirely; DBSCAN includes them in the largest cluster.
- B) K-means assigns every point to the nearest centroid including outliers; DBSCAN explicitly labels outliers as noise and excludes them from clusters.
- C) Both algorithms handle outliers identically by assigning them to the nearest cluster.
- D) DBSCAN removes outliers before training; K-means requires manual outlier removal as a preprocessing step.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* K-means forces every point into the nearest cluster regardless of how isolated it is, so outliers distort centroid positions. DBSCAN identifies points that do not belong to any dense region and labels them as noise (label -1), producing more robust clusters.
  - *Why A is incorrect:* K-means does not ignore outliers — it includes them in the nearest cluster, where they can significantly distort the centroid.
  - *Why C is incorrect:* The algorithms handle outliers fundamentally differently. This is one of DBSCAN's primary advantages over K-means.
  - *Why D is incorrect:* DBSCAN does not remove points before training; it identifies and labels them as noise during the clustering process itself. Neither algorithm requires manual outlier removal as a prerequisite.

---

### Question 20 (5 points)

After performing dimensionality reduction with PCA, which of the following statements about the principal components is TRUE?

- A) Each principal component is a randomly selected subset of the original features.
- B) Principal components are ordered by the amount of variance they explain, and each component is orthogonal (uncorrelated) to all others.
- C) The first principal component always explains 100% of the variance in the original data.
- D) Principal components retain the original feature names and can be interpreted the same way as the original variables.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* PCA constructs components as linear combinations of original features along directions of maximum variance. They are ordered (PC1 explains the most variance, PC2 the second most, etc.) and are mathematically orthogonal, meaning they are uncorrelated with one another.
  - *Why A is incorrect:* Principal components are computed linear combinations of all original features, not randomly selected subsets. Each component involves contributions from all original variables.
  - *Why C is incorrect:* If the first component explained 100% of variance, all features would be perfectly correlated. In practice, variance is distributed across multiple components.
  - *Why D is incorrect:* Principal components are abstract mathematical constructs — linear combinations of original features. They do not have the same names or direct interpretations as the original variables.

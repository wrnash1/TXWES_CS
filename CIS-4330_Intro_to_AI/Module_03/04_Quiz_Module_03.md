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

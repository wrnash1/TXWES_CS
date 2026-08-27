# Quiz: Module 02 - Supervised vs Unsupervised Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe fundamental principles of machine learning on Azure
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A model is trained using a dataset where each record contains a customer's age, annual income, number of prior purchases, and a label indicating whether the customer churned (yes or no). Which type of machine learning task does this represent?

- A) Unsupervised clustering
- B) Supervised regression
- C) Supervised classification
- D) Reinforcement learning

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The dataset includes labeled outcomes (churned: yes/no) and the output is a discrete category. This is supervised learning with a binary classification task.
- *Why A is incorrect:* Clustering is unsupervised and requires no labels. Labels are present in this scenario.
- *Why B is incorrect:* Regression predicts a continuous numerical value. Churn (yes/no) is a discrete category, not a continuous number.
- *Why D is incorrect:* Reinforcement learning requires an agent-environment loop with reward signals. No such structure is described.

---

## Question 2

A data science team wants to group 500,000 retail customers into natural segments based on their purchasing behavior. No category definitions exist in advance, and no historical labels are available. Which learning approach is most appropriate?

- A) Supervised binary classification
- B) Supervised regression
- C) Unsupervised clustering
- D) Supervised multi-class classification

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The goal is to discover structure in unlabeled data. No labels exist. This is the definition of unsupervised clustering.
- *Why A is incorrect:* Binary classification requires labeled data with two possible outcomes. No labels are available.
- *Why B is incorrect:* Regression requires labeled continuous output data. Neither labels nor continuous output are described.
- *Why D is incorrect:* Multi-class classification requires predefined class labels and a labeled training set. Neither exists in this scenario.

---

## Question 3

Which of the following evaluation metrics is most appropriate for measuring the performance of a regression model that predicts apartment rental prices?

- A) Accuracy
- B) F1-score
- C) Root Mean Squared Error (RMSE)
- D) AUC-ROC

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* RMSE measures the average magnitude of error in the same units as the output (dollars). It is the standard metric for regression tasks.
- *Why A is incorrect:* Accuracy measures the proportion of correct category predictions. Rental price is not a category — you cannot define "correct vs incorrect" for a continuous value without classification.
- *Why B is incorrect:* F1-score is a classification metric that balances precision and recall. It does not apply to continuous outputs.
- *Why D is incorrect:* AUC-ROC measures the ability to separate classes across classification thresholds. It is a classification metric, not a regression metric.

---

## Question 4

A model achieves 97% accuracy on the training set but only 58% accuracy on the test set. What does this most likely indicate?

- A) The model is underfitting due to insufficient training time.
- B) The test set contains data from a different domain than the training set.
- C) The model is overfitting because it has memorized training examples and fails to generalize.
- D) The model is performing well because training accuracy exceeds test accuracy in all deployed systems.

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* A large gap between training accuracy (97%) and test accuracy (58%) is the classic signature of overfitting. The model has memorized training noise rather than learning generalizable patterns.
- *Why A is incorrect:* Underfitting produces low accuracy on both training and test sets, not high training accuracy.
- *Why B is incorrect:* While data distribution shift can cause test performance degradation, the scenario describes a standard training/test evaluation setup, not a cross-domain deployment issue.
- *Why D is incorrect:* High training accuracy with much lower test accuracy is a problem, not a normal property of deployed models.

---

## Question 5

Which of the following is the primary purpose of cross-validation?

- A) To increase the size of the training dataset by duplicating records.
- B) To obtain a more reliable estimate of model performance by training and evaluating on multiple data subsets.
- C) To clean the training data by removing outlier records before model training.
- D) To automatically select the best algorithm from a list of candidates.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Cross-validation splits the data into K folds, trains and evaluates K times, and averages the scores. This provides a more reliable estimate of generalization performance than a single train-test split, especially for small datasets.
- *Why A is incorrect:* Cross-validation does not duplicate data. It reorganizes the same data into different splits.
- *Why C is incorrect:* Cross-validation is an evaluation strategy, not a data cleaning technique.
- *Why D is incorrect:* AutoML performs algorithm selection. Cross-validation measures performance; it does not select algorithms on its own.

---

## Question 6

An Azure ML engineer wants to build a model that predicts whether a given email is spam or legitimate. The engineer has 50,000 labeled emails for training. In Azure Machine Learning AutoML, which task type should be selected?

- A) Regression
- B) Clustering
- C) Time Series Forecasting
- D) Classification

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* Spam vs. legitimate is a binary discrete category. Labeled training data is available. This is supervised classification, which maps to the AutoML Classification task type.
- *Why A is incorrect:* Regression predicts continuous numerical values. Spam/not spam is not a continuous value.
- *Why B is incorrect:* Clustering is unsupervised and does not use labels. Labeled training data is present in this scenario.
- *Why C is incorrect:* Time series forecasting is for sequential data with a temporal component, such as daily demand or stock prices. Email classification is not temporal.

---

## Question 7

Which of the following best describes the role of a validation set in the machine learning workflow?

- A) It is used to train the final model before deployment.
- B) It is used to provide an honest final evaluation of model performance on completely unseen data.
- C) It is used during development to tune hyperparameters and compare model configurations.
- D) It is used to augment the training data when the training set is too small.

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The validation set guides development decisions — which algorithm, which hyperparameter values, which features. It is separate from training data but is used repeatedly during model development.
- *Why A is incorrect:* The training set, not the validation set, is used to fit model parameters.
- *Why B is incorrect:* This describes the test set, which is held out until all development decisions are finalized.
- *Why D is incorrect:* Validation sets are not used to augment training data. Data augmentation is a separate technique.

---

## Question 8

A network engineer wants to detect unusual traffic patterns in a corporate network. The only available data is 6 months of normal network logs — no labeled examples of attacks or intrusions exist. Which machine learning approach is most appropriate?

- A) Supervised binary classification
- B) Unsupervised anomaly detection
- C) Supervised time series regression
- D) Reinforcement learning with reward shaping

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* No labeled examples of attacks are available. The appropriate approach is to learn the distribution of normal traffic unsupervised and flag statistical deviations as potential anomalies.
- *Why A is incorrect:* Binary classification requires labeled examples of both classes (normal and attack). No attack labels exist.
- *Why C is incorrect:* Time series regression predicts future values. The goal here is anomaly detection, not forecasting.
- *Why D is incorrect:* Reinforcement learning requires a reward signal from environment interaction. Network intrusion detection does not fit this framework.

---

## Question 9

A data scientist is training a random forest model and notices that the model performs significantly better on the training set than the validation set. She decides to reduce the number of trees from 500 to 100. What effect is this change most likely to have?

- A) It will increase overfitting because fewer trees means less regularization.
- B) It will reduce overfitting by simplifying the ensemble and reducing variance.
- C) It will have no effect on overfitting because the number of trees does not affect generalization.
- D) It will cause underfitting because random forests always underfit with fewer than 200 trees.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Reducing the number of trees simplifies the ensemble, which can reduce variance and help with overfitting. However, too few trees can also lead to underfitting. In a scenario where the model is currently overfitting, reducing trees is one approach to simplification.
- *Why A is incorrect:* More trees in a random forest generally increase variance, not reduce it. Fewer trees reduces the ensemble's capacity.
- *Why C is incorrect:* The number of trees directly affects the model's variance and its tendency to overfit or underfit.
- *Why D is incorrect:* There is no fixed threshold of 200 trees below which random forests universally underfit. Performance depends on data complexity.

---

## Question 10

Which of the following statements about Principal Component Analysis (PCA) is correct?

- A) PCA is a supervised classification algorithm that requires labeled training data.
- B) PCA transforms features into uncorrelated components ordered by the amount of variance they explain.
- C) PCA increases the number of dimensions in the data to improve model performance.
- D) PCA is used exclusively for time series data and does not apply to tabular data.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* PCA projects data onto orthogonal axes (principal components) that maximize variance. The first component captures the most variance, each subsequent component captures the most remaining variance. The result is a lower-dimensional representation that preserves as much information as possible.
- *Why A is incorrect:* PCA is an unsupervised technique. It does not use labels. It does not classify.
- *Why C is incorrect:* PCA reduces dimensions, not increases them. The goal is compression, not expansion.
- *Why D is incorrect:* PCA applies to any numerical tabular data. It is not limited to time series and is widely used on static feature matrices.

---

### Question 11 (5 points)

A supervised learning model for predicting house prices returns an R-squared (R²) value of 0.42 on the test set. How should this result be interpreted?

- A) The model explains 42% of the variance in house prices; the remaining 58% is unexplained.
- B) The model is correct on 42% of predictions and incorrect on 58%.
- C) The model has a mean absolute error of 42 units.
- D) The model performs 42% better than the baseline random classifier.

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* R² (coefficient of determination) represents the proportion of variance in the target variable that the model explains. An R² of 0.42 means the model accounts for 42% of the variance; 58% is due to factors not captured by the model.
  - *Why B is incorrect:* R² does not count correct vs. incorrect predictions. That interpretation applies to classification accuracy, not regression R².
  - *Why C is incorrect:* Mean Absolute Error (MAE) is a separate metric measuring average absolute prediction error in the output's units. R² is a dimensionless proportion.
  - *Why D is incorrect:* R² measures variance explained, not percentage improvement over a random classifier. A random classifier baseline concept applies to classification, not regression.

---

### Question 12 (5 points)

Which of the following remedies is MOST effective for reducing overfitting in a decision tree classifier?

- A) Increasing the maximum tree depth to allow more complex splits.
- B) Adding more features to the training dataset.
- C) Pruning the tree by limiting its maximum depth or minimum samples per leaf.
- D) Removing the validation set and evaluating only on training data.

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Pruning constrains the complexity of a decision tree, preventing it from memorizing training examples. Limiting maximum depth or requiring a minimum number of samples in each leaf are standard regularization techniques that reduce overfitting.
  - *Why A is incorrect:* Increasing tree depth increases model complexity, which worsens overfitting rather than reducing it.
  - *Why B is incorrect:* Adding irrelevant features can increase overfitting by giving the tree more noise to memorize. Feature selection, not addition, is the appropriate remedy.
  - *Why D is incorrect:* Removing the validation set eliminates the mechanism for detecting overfitting. It does not reduce overfitting and makes the problem invisible.

---

### Question 13 (5 points)

A classification model is evaluated on a test set of 1,000 samples: 900 are class A and 100 are class B. The model predicts class A for every single sample and achieves 90% accuracy. What does this reveal about using accuracy as the sole metric for this dataset?

- A) The model is genuinely high-performing and accuracy is the correct metric to report.
- B) Accuracy is misleading on imbalanced datasets; a model that ignores the minority class can appear highly accurate.
- C) The test set is too small to evaluate the model; more data would fix the accuracy paradox.
- D) 90% accuracy always indicates a strong model regardless of class distribution.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* This is the accuracy paradox on imbalanced datasets. A trivial model that predicts only the majority class achieves accuracy equal to the majority class proportion. For this dataset, recall for class B is 0% — the model has not learned anything useful about the minority class.
  - *Why A is incorrect:* The model makes no correct predictions for class B. A 0% recall for the minority class makes this model useless for most practical applications.
  - *Why C is incorrect:* The issue is not dataset size but class imbalance. More data with the same imbalance would produce the same misleading accuracy.
  - *Why D is incorrect:* 90% accuracy is meaningless without context. On a 90/10 imbalanced dataset, it signals that the model may have learned nothing.

---

### Question 14 (5 points)

In K-means clustering, what does the value of K represent?

- A) The number of features used to train the clustering model.
- B) The number of clusters the algorithm will partition the data into.
- C) The number of iterations the algorithm runs before stopping.
- D) The distance metric used to measure similarity between data points.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* K in K-means specifies the number of cluster centroids the algorithm initializes and the number of groups the data will be partitioned into. Choosing K is a key hyperparameter decision in unsupervised clustering.
  - *Why A is incorrect:* The number of features is the dimensionality of the feature space, not K. K-means can run on any number of features regardless of K.
  - *Why C is incorrect:* The number of iterations is a convergence parameter, sometimes called max_iter in implementations. It is separate from K.
  - *Why D is incorrect:* The distance metric (commonly Euclidean) is a separate parameter. K-means uses Euclidean distance by default, regardless of the value of K.

---

### Question 15 (5 points)

Which metric would be MOST appropriate to evaluate a cancer screening model where missing a positive case (false negative) is far more costly than a false alarm (false positive)?

- A) Accuracy
- B) Precision
- C) Recall (Sensitivity)
- D) R-squared

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Recall = TP / (TP + FN). When false negatives are the primary cost — as in cancer screening where a missed diagnosis can be fatal — maximizing recall minimizes the rate of missed positive cases.
  - *Why A is incorrect:* Accuracy treats all errors equally. On an imbalanced medical dataset, high accuracy can coexist with catastrophically low recall for the positive class.
  - *Why B is incorrect:* Precision = TP / (TP + FP). High precision minimizes false alarms. This matters when false positives are costly (e.g., unnecessary treatment), not when false negatives are the primary concern.
  - *Why D is incorrect:* R-squared is a regression metric measuring variance explained. It does not apply to binary classification screening tasks.

---

### Question 16 (5 points)

A data scientist splits a dataset into 70% training, 15% validation, and 15% test subsets. She uses the validation set to select between three candidate models, then reports the test set score as the final performance estimate. Which best practice does this workflow follow?

- A) Data leakage — the test set should have been used to select models.
- B) Correct separation of concerns — development decisions use the validation set and the test set provides an unbiased final estimate.
- C) Overfitting — using three subsets always causes the model to overfit.
- D) Underfitting — 70% training data is insufficient for any practical model.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The three-way split is a standard best practice. The validation set guides all development decisions (model selection, hyperparameter tuning) without contaminating the test set. The test set is used exactly once for the final unbiased performance estimate.
  - *Why A is incorrect:* Using the test set for model selection would constitute data leakage. This workflow correctly avoids that by using the validation set for selection.
  - *Why C is incorrect:* Using three subsets is a regularization and evaluation best practice, not a cause of overfitting. Overfitting results from model complexity relative to data, not from the number of splits.
  - *Why D is incorrect:* 70% training is standard. Many production models are trained on far less. The adequacy of training data depends on data complexity, not a fixed minimum percentage.

---

### Question 17 (5 points)

Which of the following best describes the silhouette score used to evaluate clustering results?

- A) It measures the accuracy of cluster label predictions compared to ground truth labels.
- B) It quantifies how similar a data point is to its own cluster compared to other clusters, ranging from -1 (poor) to +1 (ideal).
- C) It counts the total number of data points correctly assigned to their cluster centroid.
- D) It measures the percentage of variance explained by the K-means cluster centroids.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The silhouette score measures intra-cluster cohesion vs. inter-cluster separation for each point, then averages across all points. A score near +1 means points are well-matched to their cluster and poorly matched to neighboring clusters. It is the standard evaluation metric when ground truth labels are unavailable.
  - *Why A is incorrect:* Ground truth labels are not available in unsupervised learning. Comparing to ground truth would make this a supervised evaluation, not an unsupervised one.
  - *Why C is incorrect:* This describes counting correctly assigned points, which requires ground truth labels. The silhouette score requires no labels.
  - *Why D is incorrect:* Percentage of variance explained by centroids is related to inertia (within-cluster sum of squares), not the silhouette score.

---

### Question 18 (5 points)

What is the primary difference between L1 regularization (Lasso) and L2 regularization (Ridge) in linear models?

- A) L1 adds a penalty proportional to the square of the weights; L2 adds a penalty proportional to the absolute value of the weights.
- B) L1 can shrink coefficients to exactly zero (producing sparse models); L2 shrinks coefficients toward zero but rarely to exactly zero.
- C) L1 is used only for classification; L2 is used only for regression.
- D) L1 increases model complexity; L2 reduces model complexity.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* L1 (Lasso) penalizes the sum of absolute values of weights. Its penalty geometry produces sparse solutions where many coefficients become exactly zero, performing implicit feature selection. L2 (Ridge) penalizes the sum of squared weights, which shrinks all coefficients smoothly but rarely to zero.
  - *Why A is incorrect:* This reverses the definitions. L2 uses squared penalties; L1 uses absolute value penalties.
  - *Why C is incorrect:* Both L1 and L2 can be applied to regression and classification models. The choice depends on desired sparsity, not task type.
  - *Why D is incorrect:* Both L1 and L2 are regularization methods that reduce model complexity. Neither increases complexity.

---

### Question 19 (5 points)

A logistics company wants to predict the exact number of days it will take to deliver a package based on origin, destination, package weight, and carrier. Which Azure Machine Learning AutoML task type should be configured?

- A) Classification
- B) Clustering
- C) Regression
- D) Time Series Forecasting

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Number of delivery days is a continuous numerical value. The labeled historical data maps input features to a specific numeric output. This is a regression task.
  - *Why A is incorrect:* Classification predicts discrete category labels. Delivery days is a continuous number, not a category.
  - *Why B is incorrect:* Clustering is unsupervised and discovers groups. Labeled training data is present and the output is a numeric prediction.
  - *Why D is incorrect:* Time series forecasting is used when the output depends on a temporal sequence of prior observations. Predicting delivery time from package attributes is a standard regression task, not a sequential forecasting problem.

---

### Question 20 (5 points)

Which of the following best describes the purpose of feature scaling (e.g., standardization or min-max normalization) before training a machine learning model?

- A) Feature scaling converts categorical variables into numerical representations.
- B) Feature scaling ensures that features with large numeric ranges do not dominate distance-based or gradient-based algorithms.
- C) Feature scaling removes outliers from the training dataset before model fitting.
- D) Feature scaling increases the number of training examples by interpolating between data points.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Algorithms that use distances (K-nearest neighbors, K-means, SVM) or gradient descent (linear regression, neural networks) are sensitive to feature scales. A feature with values in the range 0–100,000 will dominate one with values in 0–1 unless scaled. Standardization (zero mean, unit variance) or min-max scaling corrects this.
  - *Why A is incorrect:* Converting categorical variables to numbers is called encoding (e.g., one-hot encoding, label encoding). This is a separate preprocessing step from scaling.
  - *Why C is incorrect:* Outlier removal is a separate data cleaning step. Scaling transforms the range of existing values; it does not remove any data points.
  - *Why D is incorrect:* Scaling transforms existing feature values; it does not generate new training examples. Data augmentation or oversampling techniques increase training examples.

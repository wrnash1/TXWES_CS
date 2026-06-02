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

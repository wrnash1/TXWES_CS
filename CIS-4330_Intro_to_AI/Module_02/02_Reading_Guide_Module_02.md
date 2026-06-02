# Reading Guide: Module 02 - Supervised vs Unsupervised Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe fundamental principles of machine learning on Azure (20-25%)

---

## Overview

This reading guide deepens your understanding of supervised and unsupervised learning, the two primary paradigms tested on the AI-900 exam. Work through the vocabulary, comparison tables, and algorithm summaries carefully. The AI-900 exam routinely presents business scenarios and asks you to identify the correct ML approach, task type, and Azure service. Complete the study checklist before the lab.

---

## Section 1: Core Vocabulary

**Supervised Learning**
A machine learning paradigm in which every training example includes both input features and a correct output label. The algorithm learns to predict the label for new inputs by minimizing prediction error during training.

**Unsupervised Learning**
A machine learning paradigm in which the training data contains only input features with no labels. The algorithm discovers hidden structure — clusters, latent dimensions, or anomalies — without guidance from known correct answers.

**Regression**
A supervised learning task in which the output is a continuous numerical value. The model predicts a quantity that can take any value within a range, such as price, temperature, or duration.

**Classification**
A supervised learning task in which the output is a discrete category label. Binary classification has two possible outputs; multi-class classification has three or more.

**Clustering**
An unsupervised learning task in which data points are grouped into clusters based on similarity. The groups are not defined in advance; the algorithm discovers them from the data.

**K-means Clustering**
A clustering algorithm that partitions data into K clusters by iteratively assigning points to the nearest centroid and recalculating centroids until convergence. Requires specifying K before running.

**Dimensionality Reduction**
An unsupervised technique that compresses data from a high-dimensional space into fewer dimensions while retaining as much information as possible. Used for visualization, noise reduction, and preprocessing.

**Principal Component Analysis (PCA)**
A dimensionality reduction algorithm that transforms features into a set of uncorrelated principal components ordered by the amount of variance they explain.

**Training Set**
The portion of labeled data used to fit the model's parameters during training.

**Validation Set**
A held-out subset of labeled data used during development to tune hyperparameters and select the best model configuration. Not used for final evaluation.

**Test Set**
A held-out subset of labeled data used only once, after all model development decisions are made, to obtain an honest performance estimate on unseen data.

**Overfitting**
A model condition in which training accuracy is significantly higher than validation accuracy. The model has memorized training examples, including noise, and fails to generalize.

**Underfitting**
A model condition in which both training accuracy and validation accuracy are low. The model is too simple to capture the genuine patterns in the data.

**Hyperparameter**
A configuration setting for the learning algorithm that is set before training begins and is not learned from data. Examples: tree depth in decision trees, learning rate in gradient boosting, K in K-means.

**Cross-validation**
A model evaluation technique in which the training data is split into K folds and the model is trained and validated K times, each time using a different fold as the validation set. Results are averaged.

**Regularization**
A technique for reducing overfitting by adding a penalty for model complexity to the training objective. L1 regularization encourages sparse models; L2 regularization penalizes large parameter values.

**AutoML (Automated Machine Learning)**
An Azure Machine Learning feature that automatically selects algorithms, preprocesses features, tunes hyperparameters, and ranks models for a given supervised learning task and dataset.

**Feature Engineering**
The process of selecting, transforming, or creating input features that improve model performance. Good feature engineering is often more impactful than algorithm selection.

**Label**
The correct output value associated with a training example in supervised learning. Labels are provided by human annotators, historical records, or controlled experiments.

---

## Section 2: Comparison Tables

### Table 1: Supervised vs Unsupervised Learning

| Dimension | Supervised Learning | Unsupervised Learning |
|---|---|---|
| Training data labels | Required (input + label pairs) | Not present (inputs only) |
| Goal | Learn to predict known outputs | Discover unknown structure |
| Primary tasks | Classification, regression | Clustering, dimensionality reduction, anomaly detection |
| Evaluation | Measured against known correct labels (accuracy, RMSE) | Measured by cohesion and separation; requires human interpretation |
| Data challenge | Labeling is expensive and time-consuming | Interpreting discovered patterns requires domain expertise |
| Azure ML AutoML | Supported for classification, regression, forecasting | Supported for clustering experiments |
| AI-900 keyword cues | "predict," "classify," "labeled," "train on examples" | "group," "segment," "discover patterns," "no labels" |
| Examples | Spam detection, house price prediction, churn prediction | Customer segmentation, document topic modeling, anomaly detection |

### Table 2: Regression vs Classification

| Dimension | Regression | Classification |
|---|---|---|
| Output type | Continuous numerical value | Discrete category label |
| Output examples | $342,000 / 98.6°F / 47 minutes | Spam/Not Spam / Fraud/Legitimate / Cat/Dog/Bird |
| Evaluation metrics | MAE, RMSE, R-squared | Accuracy, precision, recall, F1-score, AUC-ROC |
| Common algorithms | Linear regression, ridge regression, gradient boosting, neural network | Logistic regression, decision tree, random forest, SVM, neural network |
| Azure ML AutoML task | "Regression" | "Classification" |
| Typical business questions | "How much?" / "How long?" / "How many?" | "Which category?" / "Is this A or B?" / "What type?" |

### Table 3: Key Supervised Learning Algorithms

| Algorithm | Type | Strengths | Limitations | Interpretability |
|---|---|---|---|---|
| Linear Regression | Regression | Fast, interpretable, low compute | Assumes linear relationship; sensitive to outliers | Very high |
| Logistic Regression | Classification | Fast, interpretable, strong baseline | Struggles with non-linear boundaries | High |
| Decision Tree | Both | Interpretable, handles non-linearity | Prone to overfitting; unstable with small data changes | High |
| Random Forest | Both | Robust, handles missing values, low overfitting | Less interpretable; slower than single tree | Moderate |
| Gradient Boosting | Both | High accuracy on structured data | Slower to train; requires careful tuning | Low-moderate |
| Support Vector Machine | Both | Effective in high dimensions; handles small datasets | Slow on large datasets; hard to interpret | Low |
| Neural Network | Both | Learns complex non-linear patterns; handles unstructured data | Requires large datasets; computationally expensive; black box | Very low |

### Table 4: Unsupervised Learning Algorithms

| Algorithm | Task | How It Works | Key Parameter | Best Use Case |
|---|---|---|---|---|
| K-means | Clustering | Iteratively assigns points to nearest centroid and recalculates centroids | K (number of clusters) | Large datasets with spherical clusters |
| Hierarchical Clustering | Clustering | Builds a tree (dendrogram) of nested clusters by merging nearest groups | Linkage type, distance threshold | Smaller datasets; discovering hierarchical structure |
| DBSCAN | Clustering | Groups points in dense regions; marks sparse points as noise | Epsilon (radius), minimum points | Non-spherical clusters; noise-resistant |
| PCA | Dimensionality reduction | Projects data onto axes of maximum variance | Number of components | Visualization, preprocessing before ML |
| t-SNE | Dimensionality reduction | Preserves local structure for 2D/3D visualization | Perplexity | Visualization of high-dimensional data |
| Isolation Forest | Anomaly detection | Isolates anomalies by random partitioning; anomalies are isolated faster | Contamination rate | Anomaly detection without labeled examples |

---

## Section 3: The ML Workflow

Understanding the end-to-end machine learning workflow is tested on AI-900. The five stages are:

**Stage 1 — Data Collection and Preparation**
Gather raw data from sources such as databases, APIs, files, or sensors. Clean the data: handle missing values, remove duplicates, and correct formatting errors. The quality of the data determines the ceiling of model performance. Garbage in, garbage out is a fundamental principle.

**Stage 2 — Feature Engineering**
Select, transform, and create the input features that the model will use. This includes normalizing numerical features so they share a common scale, encoding categorical features as numbers, and creating new features from combinations of existing ones. Good feature engineering often matters more than algorithm selection.

**Stage 3 — Model Training**
Split the data into training and test sets. Select an algorithm. Fit the model to the training data by optimizing its parameters.

**Stage 4 — Model Evaluation**
Measure the model's performance on the held-out test set using appropriate metrics. For regression: RMSE, MAE, R-squared. For classification: accuracy, precision, recall, F1, AUC-ROC. Compare the model to a baseline.

**Stage 5 — Model Deployment**
Package the trained model and deploy it as an inference endpoint that accepts new inputs and returns predictions. Monitor performance over time and retrain when data distribution shifts.

---

## Section 4: Evaluation Metrics Reference

### Regression Metrics

**Mean Absolute Error (MAE):** The average absolute difference between predicted and actual values. Intuitive and robust to outliers. Lower is better.

**Root Mean Squared Error (RMSE):** The square root of the average squared difference between predicted and actual values. Penalizes large errors more than MAE. Lower is better.

**R-squared (R2):** The proportion of variance in the target that is explained by the model. Ranges from 0 to 1; higher is better. An R2 of 0.85 means the model explains 85% of the variance.

### Classification Metrics

**Accuracy:** The proportion of predictions that are correct. Misleading when classes are imbalanced.

**Precision:** Of all the positive predictions the model made, what fraction were actually positive? Precision = TP / (TP + FP).

**Recall (Sensitivity):** Of all the actual positive examples in the data, what fraction did the model correctly identify? Recall = TP / (TP + FN).

**F1-score:** The harmonic mean of precision and recall. Balances both metrics. F1 = 2 x (Precision x Recall) / (Precision + Recall).

**AUC-ROC:** The area under the receiver operating characteristic curve. Measures the model's ability to distinguish between classes across all classification thresholds. A value of 1.0 is perfect; 0.5 is random.

---

## Section 5: AI-900 Exam Tips

1. The word "labeled" in a scenario description always signals supervised learning. The absence of labels always signals unsupervised learning.

2. The word "predict" usually signals supervised learning; the word "discover" or "group" usually signals unsupervised learning.

3. Regression output is always a number. Classification output is always a category. If you can ask "how much?" it is regression. If you can ask "which category?" it is classification.

4. K-means clustering requires specifying K in advance. If a scenario says "determine the number of customer segments automatically," K-means is not the right answer — hierarchical or DBSCAN clustering would be considered.

5. Azure ML AutoML supports three supervised learning task types: classification, regression, and time series forecasting. It does not perform unsupervised learning tasks.

6. Overfitting is diagnosed by high training accuracy with much lower validation accuracy. Regularization, more data, or model simplification are the remedies.

7. Cross-validation is more reliable than a single train-test split, especially for small datasets. K-fold cross-validation with K=5 or K=10 is the standard.

8. On the AI-900 exam, "model evaluation" questions often include a confusion matrix. Know how to read a confusion matrix and calculate precision and recall from it before the exam.

---

## Section 6: Required Reading

**Microsoft Learn — Explore machine learning concepts**
learn.microsoft.com/en-us/training/modules/explore-machine-learning/

This module covers the full supervised and unsupervised learning framework from the AI-900 perspective. Complete all units and the knowledge check.

**Microsoft Learn — Train and evaluate regression models**
learn.microsoft.com/en-us/training/modules/train-evaluate-regression-models/

Covers regression metrics, algorithm comparisons, and Azure ML implementation.

**Microsoft Learn — Train and evaluate classification models**
learn.microsoft.com/en-us/training/modules/train-evaluate-classification-models/

Covers classification metrics including confusion matrices, precision, recall, and F1. High AI-900 relevance.

**Microsoft Learn — Train and evaluate clustering models**
learn.microsoft.com/en-us/training/modules/train-evaluate-cluster-models/

Covers K-means clustering, evaluation metrics for unsupervised learning, and Azure ML clustering experiments.

---

## Section 7: Study Checklist

- [ ] Write out the definitions of supervised, unsupervised, regression, and classification from memory.
- [ ] Complete the Microsoft Learn module: Explore machine learning concepts.
- [ ] Complete the Microsoft Learn module: Train and evaluate classification models.
- [ ] Study Table 1 (supervised vs unsupervised) until you can identify the correct paradigm from a brief scenario description.
- [ ] Study Table 3 (algorithm comparison) and know when to recommend each algorithm type.
- [ ] Memorize the six evaluation metrics: MAE, RMSE, R2, accuracy, F1, AUC-ROC.
- [ ] Be able to define overfitting and underfitting and describe one remedy for each.
- [ ] Review all eight AI-900 exam tips in Section 5.
- [ ] Complete the Module 02 quiz.
- [ ] Complete the Module 02 lab.
- [ ] Post initial discussion by Wednesday 11:59 PM and respond to two peers by Sunday 11:59 PM.

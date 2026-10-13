# Video Script: Module 02 - Supervised vs Unsupervised Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AI-900 Domain:** Describe fundamental principles of machine learning on Azure (20-25%)

---

## [00:00 - 01:30] Opening

Welcome back. I am Professor Nash, and this is Module 02 of CIS-4330 at Texas Wesleyan. In Module 01 we established the hierarchy — AI contains machine learning, which contains deep learning — and introduced the three learning paradigms. Today we go deep on the two most commonly tested paradigms for the AI-900 exam: supervised learning and unsupervised learning.

These concepts appear in exam scenarios constantly. You will be given a business problem and asked to pick the right approach. By the end of this lecture, you will have a clear mental model for making that call quickly and confidently. Let us get started.

---

## [01:30 - 05:30] Supervised Learning — The Core Structure

[SHOW DIAGRAM: Table with two columns labeled "Input Features (X)" and "Output Label (y)" with sample rows. Arrow points from table to box labeled "Algorithm Training." Arrow from that box points to "Trained Model." Arrow from model points to "Predictions on New X."]

Supervised learning is the most common form of machine learning in production systems today. The word supervised refers to the fact that the training data includes labels — the correct answers — so the algorithm receives guidance during learning.

Here is the fundamental structure. Every training example has two components: input features and an output label. Features describe the example. The label is what we want to predict. The algorithm adjusts its internal parameters to minimize prediction error — the difference between what it predicts and what the label says is correct.

Think of supervised learning like studying with a practice exam that has an answer key. You work through problems, check your answers, and adjust your approach based on mistakes. The answer key is the supervision.

Supervised learning divides into two task types based on the nature of the label.

Regression is when the output is a continuous numerical value. Example: predicting the sale price of a house given features like square footage, number of bedrooms, neighborhood, and year built. The model outputs a number — say, $342,000 — not a category.

Classification is when the output is a discrete category. Example: predicting whether a bank transaction is fraudulent or legitimate. The output is one of two labels, not a number. When there are only two possible classes, it is called binary classification. When there are three or more, it is multi-class classification.

Here is a good rule of thumb for the AI-900 exam: if you could put the output on a number line with meaningful values between the possible answers, it is regression. If the output is a category name, it is classification.

---

## [05:30 - 09:30] Key Supervised Learning Algorithms

You do not need to code these algorithms from scratch for AI-900, but you need to understand what each one does and when to use it. These appear in exam scenarios.

**Linear Regression** models the relationship between features and a continuous output as a straight line. It is highly interpretable — the coefficient for each feature tells you exactly how much that feature influences the prediction. Best for: simple relationships with a moderate number of features.

**Logistic Regression** — despite having "regression" in its name — is used for classification. It outputs the probability that an input belongs to a class, then applies a threshold (usually 0.5) to assign the final label. It is fast, interpretable, and excellent as a baseline. Best for: binary classification when interpretability matters.

**Decision Trees** split the data recursively using feature thresholds that maximize the separation between classes or minimize prediction error at each split. The result is a flowchart of yes/no questions that is easy to visualize and explain to non-technical stakeholders. Limitation: they tend to overfit because they can grow arbitrarily complex.

**Random Forests** solve the overfitting problem of decision trees by training many trees on random subsets of data and features, then aggregating their predictions. Individual trees may be wrong, but the ensemble is much more reliable. This is called bagging — bootstrap aggregation. Best for: structured data where accuracy matters more than interpretability.

**Gradient Boosting** takes a different ensemble approach: trees are trained sequentially, with each new tree focused on correcting the residual errors of the previous ones. Implementations like XGBoost and LightGBM are among the most effective algorithms for structured tabular data in practice.

**Support Vector Machines** find the decision boundary that maximizes the margin between classes. Effective when the number of features is large relative to the number of training examples. Used in text classification and high-dimensional biological data.

For AI-900 scenario questions: if the data is structured and tabular and accuracy is the priority, ensemble methods. If interpretability is required, logistic regression or decision trees. If the output is continuous, regression algorithms.

---

## [09:30 - 13:00] Unsupervised Learning — The Core Structure

[SHOW DIAGRAM: Scatter plot of unlabeled data points on the left. Arrow labeled "Clustering Algorithm." Same scatter plot on the right with colored circles around three groups of points. Left label: "No labels — raw data." Right label: "Discovered clusters."]

Unsupervised learning operates without labels. The training data contains only input features — no correct answers. The algorithm's job is to discover patterns, structure, or groupings that are not explicitly defined in advance.

The most important unsupervised task is clustering. A clustering algorithm groups data points that are similar to each other into clusters. The groups are not predefined — the algorithm discovers them from the data's own structure.

The canonical clustering algorithm is K-means. Here is how it works step by step.

Step one: you choose K, the number of clusters you want to find. Step two: the algorithm randomly places K centroids — points representing cluster centers — in the feature space. Step three: every data point is assigned to the nearest centroid based on distance. Step four: each centroid is recalculated as the mean of all points assigned to it. Step five: steps three and four repeat until the centroid positions stabilize — they stop moving significantly between iterations.

The weakness of K-means is that you must specify K in advance, and the result depends on the initial random centroid placement. The elbow method helps choose K: you run K-means for several values of K, plot the within-cluster sum of squares (the total distance from each point to its centroid), and look for the "elbow" — the point where adding more clusters provides diminishing returns.

The second key unsupervised task is dimensionality reduction. Real datasets often have hundreds or thousands of features. High dimensionality creates problems: data becomes sparse, computation becomes slow, and visualizing the data is impossible. Principal Component Analysis — PCA — compresses the data into fewer dimensions while preserving as much variance as possible. It is commonly used as a preprocessing step before clustering or visualization.

---

## [13:00 - 15:30] When to Choose Supervised vs Unsupervised

This decision comes down to one question: do you have labels?

If you have labeled data — historical outcomes, human annotations, known correct answers — supervised learning is usually the right choice. You can train a model to predict those outcomes.

If you do not have labels — or if labeling would be too expensive or you genuinely do not know what the categories should be — unsupervised learning is appropriate.

Here are four scenario patterns that signal unsupervised learning on the AI-900 exam:

Pattern one: "discover hidden groups." Customer segmentation, market research, user behavior analysis — any scenario where the goal is to find natural groupings in the data without predefined categories.

Pattern two: "reduce the number of features." When the input data has too many dimensions for efficient processing or visualization, dimensionality reduction is the answer.

Pattern three: "detect anomalies without labeled examples." When you want to find outliers but have no labeled examples of what an anomaly looks like, unsupervised anomaly detection learns the normal distribution and flags deviations.

Pattern four: "explore the data." Unsupervised methods are often used in exploratory data analysis before any model is built, to understand the structure of the data.

---

## [15:30 - 18:30] Model Training, Validation, and the Train-Test Split

[SHOW DIAGRAM: Full dataset bar divided into three segments: "Training Set 70%" on the left, "Validation Set 15%" in the middle, "Test Set 15%" on the right. Three arrows: Training Set → Train Model. Validation Set → Tune Hyperparameters. Test Set → Final Honest Evaluation.]

Before deploying any supervised model, you need an honest estimate of its performance on new data. You cannot evaluate the model on the same data you trained it on — that would produce an artificially inflated score, because the model has already "memorized" those examples.

The solution is to split your labeled data into separate sets before training begins.

The training set is used to fit the model's parameters — the algorithm sees this data and adjusts its weights or splits.

The validation set is used to tune hyperparameters — the settings that control the learning process, like tree depth, learning rate, or the number of clusters. You train multiple model versions with different settings and compare their validation performance to choose the best configuration.

The test set is held out completely until the end. You evaluate the final model on it exactly once to get an honest performance estimate. If you use the test set to make decisions during development, it effectively becomes a validation set and your test results are optimistic.

A common practical alternative is cross-validation. In K-fold cross-validation, you split the training data into K equal folds. You train and evaluate the model K times, each time using a different fold as the validation set. You average the K performance scores. Five-fold and ten-fold cross-validation are standard. Cross-validation is more reliable than a single train-validation split, especially when the dataset is small.

---

## [18:30 - 20:30] Overfitting and Underfitting

[SHOW DIAGRAM: Three panels side by side. Left panel: curve barely fitting data points — labeled "Underfitting (high bias)." Center panel: smooth curve closely following data — labeled "Good Fit." Right panel: jagged curve threading through every data point — labeled "Overfitting (high variance)."]

Two failure modes threaten every supervised model.

Overfitting occurs when the model learns the training data too precisely, including the noise and random fluctuations that are not genuine patterns. The model performs extremely well on training data but poorly on new data. Overfitting is caused by models that are too complex for the amount of training data available. The fix is regularization, which adds a penalty to the model's complexity during training; gathering more data; or choosing a simpler model architecture.

Underfitting occurs when the model is too simple to capture the true patterns in the data. It performs poorly on both training data and new data. The fix is to increase model complexity, add more relevant features, or train for more iterations.

You can diagnose both conditions using learning curves — plots of training and validation performance as training data size increases. In overfitting, training accuracy is high and validation accuracy is much lower. In underfitting, both are low and close together.

---

## [20:30 - 22:30] Azure Machine Learning AutoML

Azure Machine Learning includes Automated ML — AutoML — which automates the model selection and training process for supervised learning. When you provide a labeled dataset and specify a task type, AutoML:

- Applies feature preprocessing automatically.
- Tries a configurable set of algorithms.
- Performs hyperparameter search for each algorithm.
- Ranks all trained models by a performance metric you choose.
- Returns the best model ready for deployment.

For regression tasks, AutoML evaluates algorithms like linear regression, random forest, gradient boosting, and neural networks. For classification tasks, it evaluates logistic regression, decision trees, gradient boosting, and more.

On the AI-900 exam, AutoML represents the answer to scenarios that say "train a model with minimal code" or "quickly identify the best algorithm for a dataset." The service handles the complexity; the practitioner provides the data and defines the success metric.

---

## [22:30 - 24:00] Module Summary and Lab Preview

Let me summarize Module 02.

Supervised learning uses labeled data to train models that predict outputs for new inputs. Regression predicts continuous values; classification predicts discrete categories. Key algorithms range from simple logistic regression to powerful ensemble methods. Model evaluation requires an honest train-test split to avoid overfitting estimates. Azure ML AutoML automates supervised learning.

Unsupervised learning finds structure in unlabeled data. Clustering (K-means) discovers groups. Dimensionality reduction (PCA) compresses high-dimensional data. Results require human interpretation.

The AI-900 exam will show you a scenario and ask: supervised or unsupervised? Regression or classification? Read for the presence of labels — that is always the deciding factor.

This week's lab asks you to classify scenarios and identify which Azure ML task type applies. Take your time; some scenarios are deliberately ambiguous, and the justification matters as much as the answer.

See you in Module 03, where we go deeper into clustering algorithms and dimensionality reduction techniques.

---

## References

- Microsoft Learn — Explore machine learning concepts: learn.microsoft.com/en-us/training/modules/explore-machine-learning/
- Microsoft Learn — Train and evaluate regression models: learn.microsoft.com/en-us/training/modules/train-evaluate-regression-models/
- Microsoft Learn — Train and evaluate classification models: learn.microsoft.com/en-us/training/modules/train-evaluate-classification-models/
- Microsoft Learn — Use Automated Machine Learning: learn.microsoft.com/en-us/training/modules/use-automated-machine-learning/

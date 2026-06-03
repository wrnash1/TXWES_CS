# Quiz: Module 14 — Machine Learning for Data Analysts

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A data team wants to predict whether a customer will cancel their subscription in the next 30 days. The training dataset includes historical customer records, each labeled with whether the customer actually churned. Which type of machine learning task is this?

A) Unsupervised clustering — groups customers by similarity without a target label.

B) Supervised classification — uses labeled examples (churned or not) to train a model that predicts a category for new customers.

C) Supervised regression — predicts a continuous numeric value rather than a category.

D) Dimensionality reduction — compresses features into fewer dimensions; does not predict a target.

#### Q1 Correct Answer: B

#### Q1 Distractor Analysis

A is incorrect because the data has labels. C is incorrect because the output (churned or not churned) is a category, not a number. D is an unsupervised transformation technique, not a prediction task.

---

### Question 2

An analyst applies `StandardScaler.fit_transform()` to the entire dataset before calling `train_test_split()`. What problem does this introduce?

A) The scaler will fail to run if it encounters null values in the dataset.

B) StandardScaler only works on integer columns; float columns require MinMaxScaler.

C) Test set statistics influence the scaler's mean and standard deviation, causing data leakage and overly optimistic test performance.

D) The train-test split will become non-random because the scaler sorts the data by value.

#### Q2 Correct Answer: C

#### Q2 Distractor Analysis

A describes a separate null-handling issue unrelated to leakage. B is false; StandardScaler works on all numeric types. D is false; scaler does not sort data.

---

### Question 3

A random forest model achieves 97% accuracy on the training set and 64% accuracy on the test set. What is the most likely diagnosis?

A) Underfitting — the model is too simple to learn the patterns in the training data.

B) Overfitting — the model memorized the training data including noise and does not generalize to new data.

C) Data leakage — test data was used during training, producing artificially high training accuracy.

D) Class imbalance — the high training accuracy reflects the majority class baseline rather than learning.

#### Q3 Correct Answer: B

#### Q3 Distractor Analysis

A is incorrect; underfitting shows low accuracy on both training and test sets. C could produce high test accuracy, not low test accuracy. D typically appears as uniformly high accuracy with low recall on the minority class — the scenario describes a large gap between training and test accuracy, which is the signature of overfitting.

---

### Question 4

Which of the following is an example of unsupervised learning?

A) Training a model on past loan applications labeled as approved or rejected to predict future approvals.

B) Using a decision tree to predict house sale prices from square footage, location, and number of rooms.

C) Grouping retail customers into segments based on purchase frequency and average order value without predefined segment labels.

D) Using logistic regression to classify email as spam or not spam from labeled training examples.

#### Q4 Correct Answer: C

#### Q4 Distractor Analysis

A is supervised classification with labeled training examples. B is supervised regression with a numeric target. D is supervised classification with labeled spam examples. C has no labels — the algorithm discovers the groups independently.

---

### Question 5

An analyst needs to include a `contract_type` column with values Month-to-Month, One Year, and Two Year in a logistic regression model. What is the correct encoding approach?

A) Assign integers 1, 2, 3 to the three values — this is ordinal encoding and is appropriate because logistic regression requires numeric inputs.

B) Apply one-hot encoding to create binary dummy columns, using `drop_first=True` to avoid perfect multicollinearity.

C) Leave the column as a string; logistic regression in scikit-learn handles text columns automatically.

D) Drop the column entirely because categorical variables cannot be used in regression models.

#### Q5 Correct Answer: B

#### Q5 Distractor Analysis

A is inappropriate for nominal categories without a natural order — contract type has no inherent numeric order and assigning integers implies one type is "greater than" another. C is false; scikit-learn requires numeric input. D is unnecessarily discards a potentially predictive feature.

---

### Question 6

Which evaluation metric is most appropriate when minimizing false negatives is the priority? For example, a medical screening test that must not miss patients who have a disease.

A) Accuracy — measures overall correctness but treats false negatives and false positives equally.

B) Precision — measures the fraction of positive predictions that are correct; optimizes against false positives.

C) Recall — measures the fraction of actual positives that were detected; minimizing false negatives directly maximizes recall.

D) R² — a regression metric measuring explained variance; not applicable to classification.

#### Q6 Correct Answer: C

#### Q6 Distractor Analysis

A treats both error types equally and does not prioritize false negatives. B optimizes for false positives (precision) not false negatives. D is a regression metric that does not apply.

---

### Question 7

What does `stratify=y` do in `train_test_split(X, y, test_size=0.2, stratify=y)`?

A) It sorts the data by the target variable before splitting so the training set contains the earliest examples.

B) It ensures the proportion of each class in the target variable is preserved in both the training and test sets.

C) It oversamples the minority class to create a balanced training set.

D) It applies class weights so the model penalizes errors on minority class examples more heavily.

#### Q7 Correct Answer: B

#### Q7 Distractor Analysis

A describes sorting, which stratify does not do. C describes a resampling technique (SMOTE); stratify only preserves existing proportions during the split. D describes class_weight parameter, not stratify.

---

### Question 8

A K-means clustering model is run on customer transaction data with `n_clusters=4`. What does the model output?

A) Four class probability scores for each customer, summing to 1.0.

B) A single numeric prediction for each customer representing their expected spend.

C) A cluster label (0, 1, 2, or 3) for each customer indicating which group the algorithm assigned them to.

D) Four decision boundaries that separate customer segments by the most important feature.

#### Q8 Correct Answer: C

#### Q8 Distractor Analysis

A describes predict_proba output from a classifier, not clustering. B describes regression output. D describes a decision tree boundary, not K-means output.

---

### Question 9

An analyst wants to reduce overfitting in a decision tree model without switching to a different algorithm. Which approach is most appropriate?

A) Increase the maximum tree depth to allow the model to learn more complex patterns.

B) Remove the train-test split so the model trains on all available data.

C) Reduce the maximum tree depth or set a minimum number of samples required to split a node, limiting the model's complexity.

D) Apply one-hot encoding to all features, which reduces the feature space and prevents memorization.

#### Q9 Correct Answer: C

#### Q9 Distractor Analysis

A would increase overfitting by making the tree more complex. B removes the ability to detect overfitting; it does not reduce it. D changes the feature representation but does not directly constrain tree complexity or prevent leaf-level memorization.

---

### Question 10

Which combination of training and test accuracy best represents a well-fitted model with no significant overfitting or underfitting?

A) Training accuracy: 99.8%, Test accuracy: 54.2% — large gap indicates overfitting.

B) Training accuracy: 58.3%, Test accuracy: 57.1% — both low indicates underfitting.

C) Training accuracy: 87.4%, Test accuracy: 85.1% — small gap with high absolute performance indicates good generalization.

D) Training accuracy: 100.0%, Test accuracy: 100.0% — perfect scores indicate the model learned a trivial dataset or there is data leakage.

#### Q10 Correct Answer: C

#### Q10 Distractor Analysis

A shows a 45-point gap between training and test accuracy — a clear overfitting signature. B shows both metrics below 60% — underfitting. D should not be trusted; 100% accuracy on both sets almost always indicates data leakage or a trivial problem, not a genuinely well-trained model.

---

### Answer Key

| Question | Correct Answer |
|---|---|
| 1 | B |
| 2 | C |
| 3 | B |
| 4 | C |
| 5 | B |
| 6 | C |
| 7 | B |
| 8 | C |
| 9 | C |
| 10 | C |

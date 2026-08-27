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

---

### Question 11 (5 points)

A logistic regression model predicts the probability of a customer making a purchase. The default decision threshold is 0.5. An analyst lowers the threshold to 0.3. What is the effect on the model's precision and recall?

A) Precision increases and recall decreases — fewer predictions are made, and more are correct.

B) Both precision and recall decrease — lowering the threshold reduces confidence in all predictions.

C) Precision decreases and recall increases — more customers are predicted positive, catching more true positives but also more false positives.

D) Neither precision nor recall changes — only the predicted probabilities change, not the class labels.

#### Q11 Correct Answer: C

#### Q11 Distractor Analysis

Lowering the threshold means more observations are classified as positive. This catches more actual positives (raising recall) but also increases false positives (reducing precision). A reverses the direction. B is incorrect; recall improves when more positives are predicted. D is incorrect; changing the threshold directly changes which class labels are assigned, affecting both metrics.

---

### Question 12 (5 points)

Which cross-validation technique is most appropriate for a time-series dataset (e.g., monthly sales forecasting) where temporal order matters?

A) K-fold cross-validation — randomly splits data into k folds; appropriate for non-temporal datasets.

B) Stratified k-fold — preserves class proportions across folds; designed for classification imbalance, not time order.

C) Time series split (walk-forward validation) — always trains on past data and tests on future data, preserving temporal order.

D) Leave-one-out cross-validation — uses one sample as the test set; does not respect temporal ordering.

#### Q12 Correct Answer: C

#### Q12 Distractor Analysis

For time series, it is critical that the model never trains on future data. Time series split (walk-forward validation) sequentially expands the training window and always evaluates on the next future period. K-fold and leave-one-out (A, D) randomly assign samples to folds, which would allow future data to appear in training. Stratified k-fold (B) addresses class imbalance in classification, not temporal structure.

---

### Question 13 (5 points)

A feature importance chart from a trained Random Forest shows that `tenure_months` has an importance score of 0.42 and all other 19 features each have scores below 0.05. What is the most appropriate business interpretation and next analytical step?

A) Remove `tenure_months` from the model because features with high importance scores cause overfitting.

B) `tenure_months` is the most predictive feature; investigate the business relationship between customer tenure and the target, and consider whether this feature is available at prediction time.

C) The model is underfitting because a single feature dominates; add more features immediately.

D) A feature importance of 0.42 means the model is 42% accurate when using only that feature.

#### Q13 Correct Answer: B

#### Q13 Distractor Analysis

High feature importance means the model found this variable most useful for splitting. The correct response is to understand the business meaning and verify it is a legitimate predictor (not a proxy that leaks the label). A is incorrect; high importance does not cause overfitting by itself. C is incorrect; feature dominance is not an underfitting signal. D misinterprets importance scores as accuracy values.

---

### Question 14 (5 points)

What is the purpose of `MinMaxScaler` versus `StandardScaler` in feature preprocessing?

A) `MinMaxScaler` centers features at mean=0 and scales to std=1; `StandardScaler` scales features to a [0, 1] range.

B) `MinMaxScaler` scales features to a defined range (e.g., 0 to 1); `StandardScaler` centers features at mean=0 with std=1. Use `MinMaxScaler` when the algorithm requires bounded inputs; use `StandardScaler` for algorithms sensitive to outliers.

C) Both scalers produce identical output; the choice between them is purely a coding style preference.

D) `StandardScaler` should only be used with tree-based models; `MinMaxScaler` is required for distance-based models like KNN.

#### Q14 Correct Answer: B

#### Q14 Distractor Analysis

A reverses the definitions. C is incorrect; the two scalers produce different outputs and behave differently with outliers. D is incorrect in its prescriptions; tree-based models do not require scaling at all, and both scalers can be used with distance-based models, though StandardScaler is more robust to outliers.

---

### Question 15 (5 points)

A classification model is evaluated on a test set of 1,000 records: 950 "No" and 50 "Yes". The model predicts "No" for every record and achieves 95% accuracy. What critical problem does this reveal?

A) The model is well-trained because 95% accuracy is an excellent result.

B) The model is overfitting — it memorized the majority class during training.

C) The model has learned nothing useful; it exploits class imbalance and fails to detect any positive cases (0% recall on the minority class).

D) The test set is too small to evaluate model performance accurately.

#### Q15 Correct Answer: C

#### Q15 Distractor Analysis

A is incorrect — 95% accuracy on an imbalanced dataset can be achieved with a trivially useless model that always predicts the majority class. B is incorrect; this pattern is class imbalance, not overfitting. D is a distraction; the problem is the model, not the sample size.

---

### Question 16 (5 points)

What is the primary purpose of using `cross_val_score` with 5 folds instead of a single train-test split?

A) Cross-validation uses all available data for training simultaneously, producing a more accurate model.

B) Cross-validation produces five independent performance estimates, reducing the variance of the evaluation metric and providing a more reliable assessment of generalization performance.

C) Cross-validation eliminates the need for feature scaling because folds automatically normalize data.

D) Cross-validation is only appropriate when the dataset has fewer than 1,000 rows.

#### Q16 Correct Answer: B

#### Q16 Distractor Analysis

A is incorrect; each fold holds out a portion of data for testing — it does not train on all data simultaneously. C is false; each fold still requires the same preprocessing pipeline as a single split. D is incorrect; cross-validation is recommended for any dataset size where robust performance estimation is needed.

---

### Question 17 (5 points)

An analyst encodes a `city` column with 500 distinct values using one-hot encoding. What problem does this create?

A) The resulting 500 binary columns will cause a key error in scikit-learn because the column limit is 256.

B) The resulting high-dimensional feature space (500 new columns) may cause the curse of dimensionality, slow training, and overfitting — especially with small to medium datasets.

C) One-hot encoding is only appropriate for binary (2-value) columns; label encoding must be used for columns with more than 10 categories.

D) The resulting columns will sum to a value greater than 1 for each row, violating the binary constraint.

#### Q17 Correct Answer: B

#### Q17 Distractor Analysis

A is false; there is no 256-column limit in scikit-learn. C is incorrect; one-hot encoding can be used for any number of categories, though high cardinality creates the dimensionality problem described in B. D is incorrect; exactly one of the 500 columns will equal 1 per row, so they sum to exactly 1.

---

### Question 18 (5 points)

Which scikit-learn class correctly builds a pipeline that first applies `StandardScaler` and then trains a `LogisticRegression` model?

A) `Pipeline([('scaler', LogisticRegression()), ('model', StandardScaler())])` — steps are in the wrong order.

B) `Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression())])` — the transformer precedes the estimator in the correct order.

C) `Pipeline(StandardScaler(), LogisticRegression())` — missing the list of named tuples required by Pipeline.

D) `Pipeline([StandardScaler(), LogisticRegression()])` — missing the required name strings for each step.

#### Q18 Correct Answer: B

#### Q18 Distractor Analysis

A places the estimator before the transformer — incorrect order and incorrect step assignments. C uses positional arguments without names — not the correct Pipeline API syntax. D omits the name strings required by Pipeline (each step must be a `(name, estimator)` tuple).

---

### Question 19 (5 points)

A churn prediction model reports: precision = 0.71, recall = 0.55, F1 = 0.62. The business team wants to reduce customer service costs by targeting only high-confidence churn predictions. Which adjustment should the analyst make?

A) Lower the classification threshold to 0.3 to increase recall and catch more churning customers.

B) Raise the classification threshold to 0.7 to increase precision, ensuring that predicted churners are more likely to be true churners before the team invests in outreach.

C) Switch from F1 score to accuracy as the primary metric to align with business cost reduction goals.

D) Remove the recall metric entirely because the business only cares about cost, not true positive rate.

#### Q19 Correct Answer: B

#### Q19 Distractor Analysis

When the goal is to reduce cost by avoiding false positives (contacting non-churners), increasing the threshold raises precision at the expense of recall. A lowers the threshold — the opposite effect, catching more churners but with more false positives. C is incorrect; accuracy is misleading for imbalanced classes. D is incorrect; removing metrics does not change model behavior.

---

### Question 20 (5 points)

What does `model.predict_proba(X_test)` return that `model.predict(X_test)` does not?

A) A single class label (0 or 1) for each test observation using the default 0.5 threshold.

B) A two-column array where each row contains the probability of belonging to class 0 and class 1, allowing threshold adjustment and probability-ranked outputs.

C) The confusion matrix comparing predicted labels to actual labels.

D) The feature importance scores sorted in descending order.

#### Q20 Correct Answer: B

#### Q20 Distractor Analysis

`predict()` returns the predicted class label after applying the decision threshold. `predict_proba()` returns a probability distribution over all classes, enabling analysts to rank observations by confidence, adjust the decision threshold, or produce probability-calibrated outputs. C describes `confusion_matrix()`, not `predict_proba()`. D describes `feature_importances_` attribute.

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
| 11 | C |
| 12 | C |
| 13 | B |
| 14 | B |
| 15 | C |
| 16 | B |
| 17 | B |
| 18 | B |
| 19 | B |
| 20 | B |

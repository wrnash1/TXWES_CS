# Quiz: Module 13 - Data Preparation and Feature Engineering
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What is the primary benefit of using Azure Cognitive Services (pre-built models) over building a custom model from scratch?
*   A) Pre-trained models save development time and compute resources by providing ready-to-use AI capabilities via REST API, with no labeled training data or model training required.
*   B) Pre-trained Azure Cognitive Services models are always free and have no usage limits for production applications.
*   C) Pre-trained models run entirely on the developer's local hardware without requiring an internet connection.
*   D) Pre-trained models always outperform custom-trained models regardless of the domain or task.
*   **Correct Answer:** A) Pre-trained models save development time and compute resources by providing ready-to-use AI capabilities via REST API, with no labeled training data or model training required.
*   **Distractor Analysis:**
    *   *Why correct:* Cognitive Services provide vendor-trained models accessible via authenticated HTTP requests — developers integrate AI capabilities in hours rather than weeks, without needing ML expertise or training infrastructure.
    *   Cognitive Services are billed per API call (not free at scale). They require an internet connection to reach Azure endpoints. For highly specialized domains, a custom-trained model may outperform a general pre-trained model.

---

**Question 2**
In the context of machine learning data pipelines, which of the following is the most accurate definition of **feature engineering**?
*   A) The process of using domain knowledge to transform raw data into new or modified input variables that better represent the underlying problem structure, improving a model's ability to learn accurate patterns.
*   B) The process of splitting a labeled dataset into training and test subsets to provide an unbiased estimate of model performance on unseen data.
*   C) A technique that reduces the number of input variables by projecting high-dimensional data onto a lower-dimensional space while retaining the most important variance.
*   D) The process of adjusting a model's hyperparameters (such as learning rate, tree depth, or regularization strength) to optimize performance on a validation set.
*   **Correct Answer:** A) The process of using domain knowledge to transform raw data into new or modified input variables that better represent the underlying problem structure, improving a model's ability to learn accurate patterns.
*   **Distractor Analysis:**
    *   *Why A is correct:* Feature engineering bridges raw data and model input — examples include creating ratio features, one-hot encoding categories, extracting date components, or binning continuous values. It often delivers larger accuracy gains than algorithm selection alone.
    *   *Why B is incorrect:* This describes the train/test split — a model evaluation technique, not feature creation.
    *   *Why C is incorrect:* This describes dimensionality reduction (e.g., PCA) — it reduces existing features rather than creating new meaningful ones from domain knowledge.
    *   *Why D is incorrect:* This describes hyperparameter tuning — adjusting model configuration settings, not transforming input data.

---

**Question 3**
A developer needs to **calculate the accuracy of model predictions against actual test labels**. Which command is most appropriate?
*   A) accuracy = accuracy_score(y_test, predictions)
*   B) model.fit(X_train, y_train)
*   C) predictions = model.predict(X_test)
*   D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) accuracy = accuracy_score(y_test, predictions)
*   **Distractor Analysis:**
    *   *Why A is correct:* `accuracy_score(y_test, predictions)` compares the model's predicted labels to the true test labels and returns the fraction of correct predictions — the standard classification evaluation metric.
    *   *Why B is incorrect:* `model.fit()` trains the model; it does not evaluate prediction accuracy against test labels.
    *   *Why C is incorrect:* `model.predict()` generates predictions from a trained model; it does not compute a performance metric.
    *   *Why D is incorrect:* This loads a CSV file into a DataFrame — data loading, which occurs before training and evaluation.

---

**Question 4**
A data scientist finds that after one-hot encoding a categorical feature with 500 unique values, the model's training time increases dramatically and performance drops. What is the most effective approach to address this?
*   A) Use target encoding or ordinal encoding instead of one-hot encoding for high-cardinality categorical features, or apply dimensionality reduction (e.g., PCA) after encoding to reduce the expanded feature space.
*   B) Apply L2 regularization to the model weights to penalize the large number of new binary features and reduce overfitting caused by the encoding expansion.
*   C) Ensure the one-hot encoder is fitted only on training data and applied to test data separately to prevent data leakage from test category frequencies.
*   D) Increase the number of training epochs or estimators so the model has more iterations to learn the relationships across all 500 binary indicator columns.
*   **Correct Answer:** A) Use target encoding or ordinal encoding instead of one-hot encoding for high-cardinality categorical features, or apply dimensionality reduction (e.g., PCA) after encoding to reduce the expanded feature space.
*   **Distractor Analysis:**
    *   *Why A is correct:* One-hot encoding a 500-category feature creates 500 new binary columns (high cardinality), causing a "curse of dimensionality" problem. Target encoding replaces categories with their mean target value (one column), and ordinal encoding assigns integer ranks — both avoid the explosion in feature space.
    *   *Why B is incorrect:* L2 regularization can help reduce overfitting from noisy features, but it does not address the root cause of training time explosion from 500 binary columns.
    *   *Why C is incorrect:* Fitting the encoder only on training data is correct practice to prevent data leakage, but this is a separate issue from the high-cardinality dimensionality problem described.
    *   *Why D is incorrect:* More training iterations will not reduce the dimensionality problem and will further increase training time rather than solving it.

---

**Question 5**
Attackers are sending subtly modified images to an Azure Custom Vision endpoint used for quality control in manufacturing, causing defective parts to be classified as passing. Which defense best mitigates this **adversarial example** attack?
*   A) Train the model with adversarial examples included in the training set and implement input validation and filtering to detect anomalous image inputs before they reach the classifier.
*   B) Apply differential privacy to the training image dataset and rate-limit the Custom Vision prediction endpoint.
*   C) Enable full disk encryption on all edge devices that capture images and submit them to the API.
*   D) Restrict Custom Vision endpoint access using Azure Private Link so only internal factory network traffic can reach the prediction URL.
*   **Correct Answer:** A) Train the model with adversarial examples included in the training set and implement input validation and filtering to detect anomalous image inputs before they reach the classifier.
*   **Distractor Analysis:**
    *   *Why A is correct:* Adversarial training on perturbed images builds model robustness against crafted noise. Input filtering can detect images with statistical anomalies (unusual pixel distributions) before classification, blocking the attack path entirely.
    *   *Why B is incorrect:* Differential privacy defends against training data reconstruction via model inversion — it does not make the model robust to adversarial pixel perturbations submitted at inference time.
    *   *Why C is incorrect:* Disk encryption protects image data stored on edge devices at rest; it has no effect on manipulated images submitted through the live prediction API.
    *   *Why D is incorrect:* Private Link restricts which network can reach the endpoint but does not prevent an internal attacker or a compromised device on the factory network from sending adversarially crafted images.

---

**Question 6**
A machine learning team is preparing a dataset for training a customer churn prediction model. They discover that 12 percent of records are missing values in the `DaysSinceLastLogin` column. The team hypothesizes that customers who have not logged in recently are more likely to churn, meaning missingness may itself be informative. Which strategy is most appropriate?

* A) Delete all rows with missing `DaysSinceLastLogin` values to keep the training dataset clean and prevent the model from learning patterns from incomplete records.
* B) Impute the missing values with the column median to preserve all records and keep the feature contribution stable.
* C) Add a binary indicator feature `IsLastLoginMissing` and impute the missing values with a placeholder (such as median), preserving both the missingness signal and the feature value for non-missing records.
* D) Replace missing values with zero, since customers with no login record have effectively zero days since last login.
* **Correct Answer:** C) Add a binary indicator feature `IsLastLoginMissing` and impute the missing values with a placeholder (such as median), preserving both the missingness signal and the feature value for non-missing records.
* **Distractor Analysis:**
  * *Why C is correct:* When missingness is informative (correlated with the target), simply deleting or imputing destroys the signal. Indicator encoding preserves the signal in a dedicated binary feature while allowing the original column to remain usable.
  * *Why A is incorrect:* Deleting 12 percent of records loses training data and discards the missingness signal entirely.
  * *Why B is incorrect:* Median imputation keeps the records but treats missingness as random noise, ignoring the hypothesis that missingness predicts churn.
  * *Why D is incorrect:* Substituting zero is factually incorrect — a null record does not mean zero days since last login; it means the value is unknown. This creates a misleading data point.

---

**Question 7**
A model trained on normalized data achieves 94 percent test accuracy. When deployed to production, the model receives raw (un-normalized) input features. What will most likely happen, and why?

* A) The model will perform identically because normalization is only a training-time optimization that does not affect inference.
* B) The model will produce garbage predictions because the feature values at inference time are in a different numerical range than the range the model learned from during training.
* C) The model will automatically re-normalize incoming features since it stores the training normalization parameters internally.
* D) The model will flag the input as an anomaly and return a confidence score of zero for all classes.
* **Correct Answer:** B) The model will produce garbage predictions because the feature values at inference time are in a different numerical range than the range the model learned from during training.
* **Distractor Analysis:**
  * *Why B is correct:* A model trained on features normalized to [0, 1] has learned weight relationships calibrated to that scale. Raw features (e.g., income of $75,000 instead of a normalized 0.45) activate completely different parts of the learned function, producing incorrect outputs.
  * *Why A is incorrect:* Normalization affects the learned parameter weights, not just training speed — the model's parameters are calibrated to normalized input distributions.
  * *Why C is incorrect:* Standard ML models (scikit-learn, Azure ML) do not automatically apply stored preprocessing at inference time unless the normalization step is explicitly included in the deployed pipeline.
  * *Why D is incorrect:* Most models do not have a built-in anomaly detection mechanism that detects out-of-range inputs and returns a zero confidence score.

---

**Question 8**
A developer one-hot encodes a `Color` feature with values Red, Blue, and Green into three binary columns: `IsRed`, `IsBlue`, `IsGreen`. After training a linear regression model, the developer notices that `IsRed`, `IsBlue`, and `IsGreen` always sum to exactly 1 for every row. What problem does this create?

* A) Multicollinearity — one of the binary columns is perfectly predictable from the other two, creating a linearly dependent feature that can destabilize linear model coefficient estimation.
* B) Class imbalance — the three binary columns create an unbalanced target distribution that biases the model toward the most frequent color.
* C) Data leakage — the fact that the three columns sum to 1 allows the model to infer the test set target variable before training.
* D) Overfitting — using three columns instead of one causes the model to memorize training examples rather than learning generalizable patterns.
* **Correct Answer:** A) Multicollinearity — one of the binary columns is perfectly predictable from the other two, creating a linearly dependent feature that can destabilize linear model coefficient estimation.
* **Distractor Analysis:**
  * *Why A is correct:* This is the "dummy variable trap." If `IsRed` = 1 - `IsBlue` - `IsGreen`, the three columns are perfectly correlated. Linear models cannot uniquely estimate coefficients when features are linearly dependent. The fix is to drop one column (use k-1 dummies for k categories).
  * *Why B is incorrect:* Class imbalance refers to the target variable distribution, not to the sum of binary indicator columns.
  * *Why C is incorrect:* Data leakage involves future information contaminating training; the sum-to-1 constraint is a mathematical property of the encoding, not an information leak.
  * *Why D is incorrect:* While extra features can contribute to overfitting, the specific problem caused by perfectly correlated features is coefficient instability in linear models, not general memorization.

---

**Question 9**
A team is building a fraud detection model on a dataset with 99.2 percent non-fraud and 0.8 percent fraud transactions. After training, the model achieves 99.2 percent accuracy on the test set. What is the most important concern about this result?

* A) The accuracy is too high, suggesting the model is overfitting to the fraud class and will miss non-fraud transactions in production.
* B) Accuracy is a misleading metric for severely imbalanced datasets; a model that always predicts "not fraud" would achieve the same 99.2 percent accuracy while correctly detecting zero fraud cases.
* C) The test set should have contained a higher proportion of fraud transactions so that the accuracy metric reflects model performance on the minority class.
* D) The model has memorized the training data because an accuracy above 99 percent is always a sign of overfitting.
* **Correct Answer:** B) Accuracy is a misleading metric for severely imbalanced datasets; a model that always predicts "not fraud" would achieve the same 99.2 percent accuracy while correctly detecting zero fraud cases.
* **Distractor Analysis:**
  * *Why B is correct:* In a class-imbalanced problem, a trivial classifier that ignores the minority class matches or beats many real models on accuracy. Precision, recall, F1-score, and area under the precision-recall curve are appropriate metrics because they evaluate minority class performance explicitly.
  * *Why A is incorrect:* High accuracy does not indicate overfitting to the minority class; the concern is the opposite — the model likely ignores the minority class entirely.
  * *Why C is incorrect:* Stratified sampling for test split is good practice but does not make accuracy a valid metric for imbalanced data.
  * *Why D is incorrect:* 99.2 percent accuracy matching the majority class proportion is a statistical property of imbalanced data, not evidence of overfitting.

---

**Question 10**
A data scientist wants to compare a model trained with feature engineering (creating derived features from raw columns) against a baseline model trained on raw features only. Both models are evaluated on the same held-out test set. Which outcome would most strongly suggest that feature engineering added meaningful predictive value?

* A) The feature-engineered model achieves lower training accuracy than the baseline, indicating it is not overfitting to the training data.
* B) The feature-engineered model achieves higher test accuracy and a higher cross-validation F1-score than the baseline, with similar or smaller gap between training and test accuracy.
* C) The feature-engineered model contains more total features than the baseline, indicating that more information was captured from the raw dataset.
* D) The feature-engineered model trains faster than the baseline because engineered features reduce the number of raw input columns.
* **Correct Answer:** B) The feature-engineered model achieves higher test accuracy and a higher cross-validation F1-score than the baseline, with similar or smaller gap between training and test accuracy.
* **Distractor Analysis:**
  * *Why B is correct:* Improved test performance with a small training-test gap demonstrates that the engineered features helped the model learn generalizable patterns — the goal of feature engineering. Cross-validation F1 confirms the improvement is not a single lucky test split.
  * *Why A is incorrect:* Lower training accuracy does not indicate successful feature engineering; it may indicate the engineered features are less useful, or that the model is underfitting.
  * *Why C is incorrect:* More features are not inherently better — they can add noise and increase overfitting risk. The metric of success is model performance on unseen data, not feature count.
  * *Why D is incorrect:* Feature engineering often increases the number of features and can increase training time; speed improvement is not an indicator of predictive value.

---

**Question 11**
A dataset contains a `Color` feature with three unique values: Red, Blue, and Green. A data scientist wants to encode this feature for use in a logistic regression model. Which encoding strategy is most appropriate, and why?
*   A) Label encoding — assign integers 1, 2, 3 to Red, Blue, Green because logistic regression requires numeric inputs.
*   B) One-hot encoding — create three binary columns (IsRed, IsBlue, IsGreen) because nominal categories have no ordinal relationship and label encoding would imply a false ranking.
*   C) Target encoding — replace each color with the mean of the target variable for that color because it reduces dimensionality compared to one-hot encoding.
*   D) Binary encoding — convert the integer label codes to binary bits because it is always more efficient than one-hot encoding for categorical features.
*   **Correct Answer:** B) One-hot encoding — create three binary columns (IsRed, IsBlue, IsGreen) because nominal categories have no ordinal relationship and label encoding would imply a false ranking.
*   **Distractor Analysis:**
    *   *Why B is correct:* Color has no meaningful ordering — Red is not "greater than" Blue. Label encoding (1, 2, 3) imposes an artificial ordinal relationship that linear models will exploit, distorting coefficient estimation. One-hot encoding treats each category as independent, which is the correct representation for nominal features.
    *   *Why A is incorrect:* Label encoding is appropriate for ordinal features (e.g., Small=1, Medium=2, Large=3) where rank is meaningful. For unordered nominal categories, it misleads linear models into treating numeric proximity as semantic similarity.
    *   *Why C is incorrect:* Target encoding is useful for high-cardinality features where one-hot would create too many columns, but it introduces data leakage risk if not applied correctly (the target mean must be computed on training data only). For a 3-category feature, one-hot is the safer, standard approach.
    *   *Why D is incorrect:* Binary encoding is a dimensionality-saving technique for high-cardinality features (e.g., 1,000 categories). For a 3-category feature, one-hot (3 columns) is standard and binary encoding offers no meaningful advantage.

---

**Question 12**
A dataset has a `Salary` column ranging from $25,000 to $250,000. A data scientist applies Min-Max normalization and separately applies Z-score standardization. After transformation, which statement correctly describes the output of each method?
*   A) Normalization rescales values to a [0, 1] range; standardization transforms values to have a mean of 0 and a standard deviation of 1 — the choice depends on whether the algorithm assumes a bounded range or a Gaussian distribution.
*   B) Both methods produce identical output when the original data is normally distributed.
*   C) Standardization always produces values in [0, 1]; normalization produces values with mean 0 and standard deviation 1.
*   D) Normalization is used only for target variables; standardization is used only for input features.
*   **Correct Answer:** A) Normalization rescales values to a [0, 1] range; standardization transforms values to have a mean of 0 and a standard deviation of 1 — the choice depends on whether the algorithm assumes a bounded range or a Gaussian distribution.
*   **Distractor Analysis:**
    *   *Why A is correct:* Min-Max normalization: (x − min) / (max − min) → bounded [0, 1]. Z-score standardization: (x − mean) / std → unbounded, mean=0, std=1. Use normalization for algorithms sensitive to value range (k-NN, neural networks); use standardization for algorithms that assume Gaussian input (SVM, linear regression, PCA).
    *   *Why B is incorrect:* Even on normally distributed data, the two methods produce different output ranges and distributions. Their outputs are identical only in a degenerate trivial case (mean=0, std=1, min=0, max=1 simultaneously), which essentially never occurs in practice.
    *   *Why C is incorrect:* The definitions are exactly reversed. Standardization does not produce [0, 1] outputs; normalization does not produce mean=0 outputs.
    *   *Why D is incorrect:* Both techniques can be applied to input features or target variables depending on context. There is no rule restricting normalization to targets or standardization to inputs.

---

**Question 13**
A binary classification dataset contains 95% negative class (label 0) and 5% positive class (label 1). After training, the model's recall for the positive class is only 0.12. Which technique most directly addresses the class imbalance to improve minority class recall?
*   A) Increase the number of decision trees in a Random Forest model, which naturally balances class importance by averaging over more trees.
*   B) Apply SMOTE (Synthetic Minority Over-sampling Technique) to the training set to generate synthetic positive-class examples, increasing the minority class representation before training.
*   C) Remove 90% of negative class samples from the test set so that the evaluation dataset is balanced.
*   D) Apply PCA to reduce the number of features, since high dimensionality causes class imbalance in training data.
*   **Correct Answer:** B) Apply SMOTE (Synthetic Minority Over-sampling Technique) to the training set to generate synthetic positive-class examples, increasing the minority class representation before training.
*   **Distractor Analysis:**
    *   *Why B is correct:* SMOTE creates synthetic minority samples by interpolating between existing positive-class examples in feature space, giving the model more exposure to the minority class during training. This directly improves recall for the positive class. SMOTE is applied only to the training set — never the test set.
    *   *Why A is incorrect:* Adding more trees improves model stability but does not inherently resolve class imbalance. Without balancing, the majority class still dominates each tree's training, and ensemble averaging does not fix the underlying skew.
    *   *Why C is incorrect:* Modifying the test set creates a biased evaluation that does not reflect real-world data distribution. Balancing should be applied to the training set only; the test set must mirror production conditions.
    *   *Why D is incorrect:* PCA reduces dimensionality by projecting features to principal components — it has no effect on the class distribution or the ratio of positive to negative samples.

---

**Question 14**
A machine learning team splits their labeled dataset into training (70%), validation (15%), and test (15%) sets. What is the specific purpose of the validation set that distinguishes it from the test set?
*   A) The validation set is used to train the model's final weights; the test set is used to tune hyperparameters.
*   B) The validation set is used during model development to tune hyperparameters and select the best model configuration; the test set is reserved as a final unbiased estimate of generalization performance on completely unseen data.
*   C) The validation set is a random subset of the training set used to check that the model is fitting correctly; the test set is used when a validation set is not available.
*   D) The validation set is provided to stakeholders for business review; the test set is used internally by the data science team.
*   **Correct Answer:** B) The validation set is used during model development to tune hyperparameters and select the best model configuration; the test set is reserved as a final unbiased estimate of generalization performance on completely unseen data.
*   **Distractor Analysis:**
    *   *Why B is correct:* The validation set is an "in-development" feedback loop — the team tries different hyperparameters and model architectures, evaluates on the validation set, and iterates. Because the team has indirectly "seen" validation results during tuning, the test set must remain completely untouched until the final model is selected, providing a clean unbiased performance estimate.
    *   *Why A is incorrect:* This reverses the roles of the two sets. Model weights are learned on the training set; hyperparameters are tuned using the validation set; the test set is only used once at the end.
    *   *Why C is incorrect:* The validation set is not part of the training set and is not used for training. It is a separate held-out set used exclusively for evaluation during development. The test set is not a fallback for when the validation set is absent.
    *   *Why D is incorrect:* Stakeholder business review is not a data split criterion. The distinction between validation and test sets is entirely about when in the development process they are used and by whom in the model lifecycle.

---

**Question 15**
A data scientist is preparing a dataset to predict whether a loan will default. During feature engineering, they compute a feature called `CreditScoreAtLoanClose` using the applicant's credit score recorded at the time the loan outcome (default/no default) was already known. What problem does this introduce?
*   A) Overfitting — the model will memorize the training data because the feature perfectly predicts the target.
*   B) Data leakage — the feature incorporates information from after the prediction event (loan default), contaminating the training process with future knowledge that would not be available at the time of a real prediction.
*   C) Multicollinearity — credit score is likely correlated with other financial features, creating redundant information that destabilizes the model.
*   D) Class imbalance — loan defaults are rare events, so any feature derived from default outcomes will have an imbalanced distribution.
*   **Correct Answer:** B) Data leakage — the feature incorporates information from after the prediction event (loan default), contaminating the training process with future knowledge that would not be available at the time of a real prediction.
*   **Distractor Analysis:**
    *   *Why B is correct:* Data leakage occurs when training data includes information that would not exist at prediction time in production. A credit score "at loan close" is influenced by the loan's outcome history — it is post-event information. At the time of making a new loan decision, only the applicant's pre-loan credit score would be available. Models trained on leaked features appear to perform well in evaluation but fail in production.
    *   *Why A is incorrect:* Overfitting means the model learns noise from training data but this is a separate concept. Data leakage causes artificially inflated evaluation metrics rather than training set memorization per se.
    *   *Why C is incorrect:* Multicollinearity is a real concern with credit features, but it does not describe the specific problem of using future information that is unavailable at prediction time.
    *   *Why D is incorrect:* Class imbalance describes the distribution of the target variable, not a property of a specific feature derived from the outcome.

---

**Question 16**
A team evaluates three feature selection methods for a classification task: (1) Pearson correlation filter, (2) Recursive Feature Elimination (RFE), and (3) L1 (Lasso) regularization. Which description correctly classifies each method?
*   A) All three are filter methods because they all compute a statistical score to rank features before model training.
*   B) Pearson correlation is a filter method (evaluates features independently of the model); RFE is a wrapper method (uses model performance to iteratively eliminate features); L1 regularization is an embedded method (performs feature selection as part of the model training process).
*   C) Pearson correlation is an embedded method; RFE is a filter method; L1 regularization is a wrapper method.
*   D) RFE and L1 regularization are both filter methods because they both reduce the number of features without evaluating model performance during selection.
*   **Correct Answer:** B) Pearson correlation is a filter method (evaluates features independently of the model); RFE is a wrapper method (uses model performance to iteratively eliminate features); L1 regularization is an embedded method (performs feature selection as part of the model training process).
*   **Distractor Analysis:**
    *   *Why B is correct:* Filter methods rank features using statistics (correlation, mutual information) independently of any model — fast but model-agnostic. Wrapper methods (RFE, forward/backward selection) train and evaluate the model repeatedly with different feature subsets — computationally expensive but model-aware. Embedded methods (Lasso/L1, tree importance) perform selection during training by incorporating a penalty that drives some feature coefficients to zero.
    *   *Why A is incorrect:* Pearson correlation is a filter method, but RFE and L1 are not — they involve the model directly during selection.
    *   *Why C is incorrect:* These assignments are all incorrect. Pearson correlation is a filter method; RFE is a wrapper method; L1 is an embedded method.
    *   *Why D is incorrect:* RFE explicitly trains a model on different feature subsets to evaluate which features to eliminate — it is a wrapper method, not a filter method.

---

**Question 17**
A data scientist applies Principal Component Analysis (PCA) to a dataset with 50 features and reduces it to 10 principal components that capture 92% of the variance. Which statement correctly describes the resulting principal components?
*   A) The 10 principal components are the 10 original features with the highest correlation to the target variable.
*   B) The 10 principal components are linear combinations of the original 50 features, ordered by the amount of variance they explain, and are mutually uncorrelated (orthogonal).
*   C) PCA removes the 40 least important features while preserving the original 10 most important features unchanged.
*   D) The 10 principal components are a random sample of 10 rows from the original 50-feature dataset.
*   **Correct Answer:** B) The 10 principal components are linear combinations of the original 50 features, ordered by the amount of variance they explain, and are mutually uncorrelated (orthogonal).
*   **Distractor Analysis:**
    *   *Why B is correct:* PCA finds the directions of maximum variance in the feature space and projects all data onto those axes. Each principal component is a weighted combination of all original features. Components are ordered by explained variance (PC1 captures the most, PC2 the next most, etc.) and are geometrically orthogonal — meaning they are uncorrelated. Interpretability of original features is lost after PCA transformation.
    *   *Why A is incorrect:* PCA is an unsupervised technique — it uses variance in the feature matrix, not correlation with the target variable. The 10 components are not a subset of original features; they are newly constructed axes.
    *   *Why C is incorrect:* PCA does not select and preserve original features — it transforms all features into a new coordinate system. The resulting components have no direct one-to-one correspondence with any original feature.
    *   *Why D is incorrect:* PCA operates on features (columns), not on observations (rows). Sampling rows is a data splitting concept, not dimensionality reduction.

---

**Question 18**
A dataset has 8% missing values in the `AnnualIncome` column. The distribution of `AnnualIncome` is strongly right-skewed with several high-income outliers. Which imputation strategy is most appropriate?
*   A) Mean imputation — replace missing values with the column mean to preserve the overall average income level.
*   B) Median imputation — replace missing values with the column median because the median is robust to outliers and better represents the central tendency of a skewed distribution.
*   C) Mode imputation — replace missing values with the most frequent income value because income is a discrete variable.
*   D) Forward-fill imputation — fill missing values using the income value from the preceding row because income is a time-series variable.
*   **Correct Answer:** B) Median imputation — replace missing values with the column median because the median is robust to outliers and better represents the central tendency of a skewed distribution.
*   **Distractor Analysis:**
    *   *Why B is correct:* For skewed distributions, the mean is pulled toward the tail by extreme values — imputing with the mean would introduce systematically biased estimates for typical earners. The median is the middle value and is unaffected by outliers, making it the preferred imputation choice for right-skewed income data.
    *   *Why A is incorrect:* Mean imputation is appropriate for normally distributed data. For right-skewed data with high-income outliers, the mean overestimates the typical value and would introduce bias into the imputed records.
    *   *Why C is incorrect:* Mode imputation is used for categorical features, not continuous numeric features like income. Substituting the most frequent income value for all missing entries ignores the full distribution and artificially inflates the frequency of one specific value.
    *   *Why D is incorrect:* Forward-fill is a time-series imputation technique used when data is ordered chronologically and values are expected to carry forward (e.g., stock prices on non-trading days). Income in a cross-sectional dataset has no meaningful row order, making forward-fill inappropriate.

---

**Question 19**
During exploratory data analysis, a data scientist notices that the `TransactionAmount` column contains several values exceeding $500,000 in a dataset where the 99th percentile is $12,000. Which approach is most appropriate for handling these potential outliers before model training?
*   A) Delete all rows where `TransactionAmount` exceeds $12,000 because they are clearly errors and will harm model performance.
*   B) Investigate whether the extreme values are valid data points (e.g., legitimate large transactions) or data entry errors, then apply winsorization (capping at a high percentile) or log transformation if the extremes are genuine but skewing the distribution.
*   C) Replace all outlier values with the column mean to normalize the distribution without losing any rows.
*   D) Leave all values unchanged because removing or modifying any data point constitutes manipulation that will introduce bias.
*   **Correct Answer:** B) Investigate whether the extreme values are valid data points (e.g., legitimate large transactions) or data entry errors, then apply winsorization (capping at a high percentile) or log transformation if the extremes are genuine but skewing the distribution.
*   **Distractor Analysis:**
    *   *Why B is correct:* Outlier treatment should begin with domain investigation — a $500,000 transaction may be valid (a large corporate account) or an error (misplaced decimal). If valid, winsorization caps extreme values at a chosen percentile without removing data; log transformation compresses the scale of skewed distributions. Treating outliers blindly without domain context can corrupt the dataset.
    *   *Why A is incorrect:* Deleting all values above the 99th percentile without investigation removes potentially legitimate extreme cases and introduces a systematic bias against high-value transactions — which in fraud detection, for example, may be the most important records.
    *   *Why C is incorrect:* Replacing outliers with the column mean does not normalize the distribution and introduces the same biases as mean imputation for skewed data. It also destroys the information content of the outlier values.
    *   *Why D is incorrect:* Treating all data modifications as bias is incorrect. Outlier handling is an accepted and necessary part of data preparation. The goal is principled, documented treatment — not blind preservation of every raw value.

---

**Question 20**
A data scientist uses 5-fold cross-validation instead of a single train/test split to evaluate a classification model. What is the primary advantage of 5-fold cross-validation over a single holdout evaluation?
*   A) Cross-validation always produces higher accuracy scores because the model is trained on more data in total across all folds.
*   B) Cross-validation provides a more reliable and less variance-dependent estimate of model performance by training and evaluating the model five times on different data partitions, reducing the risk that a single lucky or unlucky split distorts the performance estimate.
*   C) Cross-validation eliminates the need for a separate test set because the final fold serves as the definitive test set.
*   D) Cross-validation is faster than a single holdout split because each fold uses only 20% of the data for training.
*   **Correct Answer:** B) Cross-validation provides a more reliable and less variance-dependent estimate of model performance by training and evaluating the model five times on different data partitions, reducing the risk that a single lucky or unlucky split distorts the performance estimate.
*   **Distractor Analysis:**
    *   *Why B is correct:* A single 80/20 train/test split can yield misleadingly optimistic or pessimistic results depending on which records happen to land in the test set. 5-fold CV trains 5 models, each evaluated on a different 20% fold, and averages the results — the variance of the performance estimate is reduced and every data point participates in both training and validation across the folds.
    *   *Why A is incorrect:* Cross-validation does not inflate accuracy scores. Each fold trains on 80% of the data — less than a single split that uses the full training set — and the average CV score is an unbiased estimate, not an inflated one.
    *   *Why C is incorrect:* Cross-validation is used for model selection and hyperparameter tuning during development. A separate final test set (kept entirely apart from cross-validation folds) is still required for the unbiased final evaluation. Using the last fold as a "test set" would compromise its independence.
    *   *Why D is incorrect:* Cross-validation is computationally more expensive than a single split because the model is trained five times rather than once. Speed is not an advantage of cross-validation — reliability is.

---

End of Quiz — Module 13

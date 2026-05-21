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

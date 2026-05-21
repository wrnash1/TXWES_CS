# Quiz: Module 14 - Model Evaluation and Deployment
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What does Azure Automated Machine Learning (AutoML) primarily automate?
*   A) Collecting and labeling raw training data from web sources
*   B) Feature selection, algorithm sweeping, and hyperparameter tuning to find the best-performing model
*   C) Writing Python front-end code for model visualization dashboards
*   D) Managing database backups and storage replication for training datasets
*   **Correct Answer:** B) AutoML automates the iterative process of model experimentation — testing multiple algorithms and hyperparameter combinations in parallel and ranking them by a chosen metric, eliminating manual trial-and-error.
*   **Distractor Analysis:**
    *   *Why correct:* AutoML addresses the most time-consuming part of ML development: trying many model configurations to find the best one. It handles preprocessing, algorithm selection, and tuning automatically.
    *   AutoML requires pre-labeled data provided by the user — it does not collect or label data. Writing visualization code and managing database backups are unrelated to the AutoML training process.

---

**Question 2**
In the context of model evaluation, which of the following is the most accurate definition of **cross-validation**?
*   A) A technique that divides the training dataset into k folds, trains the model k times using a different fold as the validation set each time, and averages the performance metrics to produce a more reliable estimate of real-world generalization.
*   B) A deployment strategy that routes a small percentage of live production traffic to a newly trained model while the existing model handles the remainder, allowing safe comparison before full rollout.
*   C) A regularization method that randomly deactivates a fraction of neurons during each training step to prevent co-adaptation and reduce overfitting in neural networks.
*   D) A feature engineering technique that applies mathematical transformations (log, square root, Box-Cox) to skewed numeric distributions to make them more symmetric before model training.
*   **Correct Answer:** A) A technique that divides the training dataset into k folds, trains the model k times using a different fold as the validation set each time, and averages the performance metrics to produce a more reliable estimate of real-world generalization.
*   **Distractor Analysis:**
    *   *Why A is correct:* Cross-validation is the standard method for estimating a model's true performance when the dataset is too small for a reliable single train/test split. It reduces variance in the performance estimate by using all data for both training and validation across different iterations.
    *   *Why B is incorrect:* This describes a canary deployment or A/B testing strategy — a production rollout technique, not a model evaluation method.
    *   *Why C is incorrect:* This describes Dropout regularization — a neural network training technique to reduce overfitting, not an evaluation strategy.
    *   *Why D is incorrect:* This describes feature transformation for skewed distributions — a data preprocessing step, not a model evaluation method.

---

**Question 3**
A developer needs to **use a trained model to generate predictions on unseen test data**. Which command is most appropriate?
*   A) predictions = model.predict(X_test)
*   B) model.fit(X_train, y_train)
*   C) accuracy = accuracy_score(y_test, predictions)
*   D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    *   *Why A is correct:* `model.predict(X_test)` passes unseen test features through the trained model and returns predicted labels or values — the standard inference call in scikit-learn.
    *   *Why B is incorrect:* `model.fit()` trains the model on labeled training data; it must be called before prediction, but it does not generate predictions.
    *   *Why C is incorrect:* `accuracy_score()` computes a performance metric from existing predictions; predictions must already exist before this can be called.
    *   *Why D is incorrect:* This loads a CSV file — data loading, which occurs at the start of the pipeline before training or prediction.

---

**Question 4**
A deployed Azure Machine Learning classification model that was 94% accurate at launch has declined to 71% accuracy six months later. Investigation reveals the real-world input data distribution has shifted significantly from the training data distribution. What is this problem and what is the recommended response?
*   A) Data drift — use Azure Machine Learning model monitoring to detect when input feature distributions diverge from training baselines, then retrain the model on a dataset that includes recent real-world data.
*   B) Overfitting — apply stronger L1/L2 regularization to the deployed model and reduce the number of features to improve generalization on the drifted data.
*   C) Data leakage — refit all preprocessing scalers using only the original training data split and redeploy to prevent test-set statistics from contaminating the model.
*   D) Class imbalance — apply SMOTE oversampling to the new data distribution and retrain to ensure the minority class is equally represented.
*   **Correct Answer:** A) Data drift — use Azure Machine Learning model monitoring to detect when input feature distributions diverge from training baselines, then retrain the model on a dataset that includes recent real-world data.
*   **Distractor Analysis:**
    *   *Why A is correct:* Data drift occurs when the statistical properties of production inputs change over time, causing a previously accurate model to degrade. The solution is to detect drift using monitoring (comparing live feature distributions to training baselines) and retrain on updated data.
    *   *Why B is incorrect:* Regularization adjusts training-time complexity — it cannot be applied to an already-deployed model and does not address the drift in incoming data distribution.
    *   *Why C is incorrect:* Data leakage causes inflated validation scores, not a decline in performance over time. The scenario describes progressive degradation from a distribution shift, not an evaluation artifact.
    *   *Why D is incorrect:* Class imbalance is a training data problem that affects model bias toward majority classes — it does not explain performance degradation that begins months after deployment as the input data changes.

---

**Question 5**
Attackers are sending subtly modified tabular inputs to a deployed Azure Machine Learning real-time endpoint — imperceptibly changing numeric feature values to cause a fraud detection model to approve fraudulent transactions. Which defense best mitigates this **adversarial example** attack?
*   A) Train the model with adversarial examples included in the training set and implement input validation and anomaly detection on incoming feature vectors before they reach the model.
*   B) Apply differential privacy to the training data and rate-limit the real-time endpoint to reduce the number of queries an attacker can submit.
*   C) Enable full disk encryption on all compute nodes hosting the Azure Machine Learning endpoint.
*   D) Store the model in Azure Key Vault and rotate the endpoint authentication key on a 60-day schedule.
*   **Correct Answer:** A) Train the model with adversarial examples included in the training set and implement input validation and anomaly detection on incoming feature vectors before they reach the model.
*   **Distractor Analysis:**
    *   *Why A is correct:* Adversarial training exposes the model to perturbed feature vectors during training, building robustness to crafted inputs. Input validation and anomaly detection on the feature space can flag requests with statistically unusual value combinations before they reach the model.
    *   *Why B is incorrect:* Differential privacy defends against training data reconstruction via model inversion — it does not make the model robust to adversarially crafted feature vectors at inference time.
    *   *Why C is incorrect:* Disk encryption protects data stored on compute nodes at rest; it has no effect on manipulated feature values submitted through the live prediction endpoint.
    *   *Why D is incorrect:* Securing the model artifact in Key Vault and rotating authentication keys protects access credentials, but does not prevent an authorized caller from submitting adversarially modified input data.

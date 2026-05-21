# Quiz: Module 05 - Natural Language Processing (NLP) Fundamentals
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
Which model is appropriate for predicting binary (yes/no) output class labels?
*   A) Linear Regression
*   B) Logistic Regression
*   C) K-Means Clustering
*   D) Principal Component Analysis
*   **Correct Answer:** B) Logistic regression maps output predictions to a probability between 0 and 1, making it ideal for binary classification.
*   **Distractor Analysis:**
    *   *Why correct:* Logistic regression applies the sigmoid function to produce a class probability, then thresholds it (typically at 0.5) to assign a binary label.
    *   Linear regression predicts continuous values, not class labels. K-Means is unsupervised grouping. PCA is dimensionality reduction.

---

**Question 2**
In the context of machine learning and NLP, which of the following is the most accurate definition of the **logistic sigmoid curve for classification**?
*   A) An S-shaped mathematical function that maps any real-valued input to a probability between 0 and 1, used in logistic regression to convert a linear score into a predicted class probability.
*   B) A self-balancing binary search tree that maintains logarithmic insertion and lookup times by adjusting node heights after each operation.
*   C) A rule that defines the ordering property of a binary search tree: all left-subtree keys are less than the parent, all right-subtree keys are greater.
*   D) A memory region allocated on the call stack for a single function invocation, storing its local variables, parameters, and return address.
*   **Correct Answer:** A) An S-shaped mathematical function that maps any real-valued input to a probability between 0 and 1, used in logistic regression to convert a linear score into a predicted class probability.
*   **Distractor Analysis:**
    *   *Why A is correct:* The sigmoid σ(z) = 1/(1+e^-z) is specifically designed to squash unbounded linear outputs into the [0,1] probability range required for binary classification.
    *   *Why B is incorrect:* This describes a self-balancing BST (e.g., AVL tree) — a data structures concept unrelated to NLP or classification.
    *   *Why C is incorrect:* This describes the BST ordering invariant, also a data structures concept unrelated to classification functions.
    *   *Why D is incorrect:* This describes a call stack frame — a systems programming concept entirely unrelated to ML.

---

**Question 3**
A developer needs to **use a trained model to generate predictions on unseen test data**. Which command is most appropriate?
*   A) predictions = model.predict(X_test)
*   B) import pandas as pd; df = pd.read_csv('data.csv')
*   C) model.fit(X_train, y_train)
*   D) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) predictions = model.predict(X_test)
*   **Distractor Analysis:**
    *   *Why A is correct:* `model.predict(X_test)` passes unseen test features through the trained model and returns predicted labels or values.
    *   *Why B is incorrect:* This loads data from a CSV file — data loading, not prediction.
    *   *Why C is incorrect:* `model.fit()` trains the model on known labeled data; it does not generate predictions on new data.
    *   *Why D is incorrect:* `accuracy_score()` computes a performance metric from existing predictions; it does not produce predictions itself.

---

**Question 4**
A regression model is producing suspiciously optimistic validation scores. Investigation reveals the MinMaxScaler was fitted on the combined train+test dataset. What is this problem called and how should it be fixed?
*   A) Data leakage — fit the scaler only on training data using `.fit_transform()`, then apply `.transform()` to test data separately.
*   B) Overfitting — apply L1 (Lasso) or L2 (Ridge) regularization to penalize large model coefficients.
*   C) Missing value errors — impute or drop null entries before fitting the scaler.
*   D) Underfitting — increase model complexity by adding polynomial features or more hidden layers.
*   **Correct Answer:** A) Data leakage — fit the scaler only on training data using `.fit_transform()`, then apply `.transform()` to test data separately.
*   **Distractor Analysis:**
    *   *Why A is correct:* Fitting the scaler on the full dataset lets test-set statistics influence training normalization, making the model appear better than it truly is on unseen data.
    *   *Why B is incorrect:* Regularization addresses overfitting (high train accuracy, low validation accuracy), not data leakage from improper scaler fitting.
    *   *Why C is incorrect:* Missing value imputation is a separate concern; null values cause errors or bias but do not inflate validation scores.
    *   *Why D is incorrect:* Underfitting produces uniformly low accuracy on both sets; it is the opposite of artificially high validation scores.

---

**Question 5**
Attackers are sending subtly modified input images to a deployed vision model, causing it to misclassify stop signs as speed limit signs with high confidence. Which defense best mitigates this **adversarial example** attack?
*   A) Train the model with adversarial examples included in the training set and validate/filter all inputs before inference.
*   B) Apply differential privacy techniques to the training data and rate-limit the public API.
*   C) Enable full disk encryption on all client endpoints connecting to the model API.
*   D) Use Azure Private Link to restrict model endpoint access to internal virtual networks only.
*   **Correct Answer:** A) Train the model with adversarial examples included in the training set and validate/filter all inputs before inference.
*   **Distractor Analysis:**
    *   *Why A is correct:* Adversarial training exposes the model to crafted perturbations during training, building robustness. Input validation detects anomalous inputs before they reach the model.
    *   *Why B is incorrect:* Differential privacy protects training data from reconstruction via model inversion; it does not defend against adversarial perturbations on inference inputs.
    *   *Why C is incorrect:* Disk encryption protects data at rest; it is irrelevant to manipulated inputs submitted through a live API.
    *   *Why D is incorrect:* Private Link restricts network access but does not prevent a legitimate internal user (or compromised system) from sending adversarial inputs.

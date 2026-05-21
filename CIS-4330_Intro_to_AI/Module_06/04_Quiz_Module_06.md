# Quiz: Module 06 - Computer Vision and Image Recognition
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What type of machine learning model is a Random Forest?
*   A) Linear Model
*   B) Single Decision Tree
*   C) Ensemble Model
*   D) Neural Network
*   **Correct Answer:** C) A Random Forest is an ensemble model that combines the predictions of multiple decision trees to improve overall stability.
*   **Distractor Analysis:**
    *   *Why correct:* A Random Forest is an ensemble (collection) of trees, not a single tree or linear model.
    *   Linear models fit a single equation. Neural networks use layered neurons. Random Forest is specifically defined as an ensemble.

---

**Question 2**
In the context of machine learning, which of the following is the most accurate definition of **bootstrap aggregation (bagging)**?
*   A) A technique where multiple models are each trained on a different random sample (with replacement) of the training data, and their predictions are averaged or voted on to reduce variance.
*   B) A process that adjusts node positions in a binary heap to restore the min-heap or max-heap property after an insertion or deletion.
*   C) HTML elements placed in the document head that define metadata, stylesheets, and viewport settings for the browser.
*   D) A queue operation pair where enqueue appends an element to the back and dequeue removes the front element.
*   **Correct Answer:** A) A technique where multiple models are each trained on a different random sample (with replacement) of the training data, and their predictions are averaged or voted on to reduce variance.
*   **Distractor Analysis:**
    *   *Why A is correct:* Bagging (Bootstrap AGGregating) trains each base learner on a bootstrapped subset, making the ensemble more robust than any single model.
    *   *Why B is incorrect:* This describes heap re-heapification — a data structures concept unrelated to ensemble learning.
    *   *Why C is incorrect:* This describes HTML head elements — a web development concept entirely unrelated to ML.
    *   *Why D is incorrect:* This describes queue operations — a computer science data structure unrelated to ML ensemble methods.

---

**Question 3**
A developer needs to **load a tabular dataset from a CSV file using the Pandas library**. Which command is most appropriate?
*   A) import pandas as pd; df = pd.read_csv('data.csv')
*   B) from sklearn.tree import DecisionTreeClassifier; model = DecisionTreeClassifier()
*   C) from sklearn.ensemble import RandomForestClassifier; model = RandomForestClassifier()
*   D) accuracy = accuracy_score(y_test, predictions)
*   **Correct Answer:** A) import pandas as pd; df = pd.read_csv('data.csv')
*   **Distractor Analysis:**
    *   *Why A is correct:* `pd.read_csv()` reads a CSV file into a Pandas DataFrame, which is the standard first step in any Python ML pipeline.
    *   *Why B is incorrect:* This imports and instantiates a decision tree classifier — it trains a model, not loads data.
    *   *Why C is incorrect:* This imports and instantiates a random forest classifier — also model setup, not data loading.
    *   *Why D is incorrect:* `accuracy_score()` evaluates predictions — it requires data already loaded and a trained model.

---

**Question 4**
A Random Forest model achieves 98% accuracy on training data but only 71% on the validation set. The model has too many deep trees memorizing noise. What is the most effective action?
*   A) Limit tree depth (`max_depth`), reduce the number of estimators, or apply regularization techniques to simplify the model architecture.
*   B) Ensure preprocessing scalers are fitted only on training data to prevent data leakage.
*   C) Use mean/median imputation to fill missing values before retraining.
*   D) Reboot the training environment and wait for services to reinitialize.
*   **Correct Answer:** A) Limit tree depth (`max_depth`), reduce the number of estimators, or apply regularization techniques to simplify the model architecture.
*   **Distractor Analysis:**
    *   *Why A is correct:* High training accuracy with low validation accuracy is the hallmark of overfitting. Reducing model complexity (shallower trees, fewer estimators) or adding regularization improves generalization.
    *   *Why B is incorrect:* Preventing data leakage addresses inflated validation scores from improper preprocessing, not the overfitting shown here.
    *   *Why C is incorrect:* Missing value imputation addresses NaN errors; it does not reduce model variance from overfitting.
    *   *Why D is incorrect:* Rebooting the environment has no effect on model complexity or overfitting behavior.

---

**Question 5**
Attackers are sending images with imperceptible pixel-level perturbations to an Azure Custom Vision classifier, causing it to misclassify safety equipment as absent. Which defense best mitigates this **adversarial example** attack?
*   A) Train the model with adversarial examples included in the training set and implement input validation and filtering before inference.
*   B) Apply differential privacy to the training data and rate-limit the public inference API.
*   C) Enable full disk encryption on all client endpoints submitting images to the API.
*   D) Restrict model endpoint access using Azure Private Link and virtual network service endpoints.
*   **Correct Answer:** A) Train the model with adversarial examples included in the training set and implement input validation and filtering before inference.
*   **Distractor Analysis:**
    *   *Why A is correct:* Adversarial training teaches the model to classify both clean and perturbed inputs correctly; input filtering can detect statistically anomalous inputs before they reach the model.
    *   *Why B is incorrect:* Differential privacy defends against training data reconstruction (model inversion), not adversarial input perturbations at inference time.
    *   *Why C is incorrect:* Disk encryption protects data at rest and is irrelevant to crafted image payloads submitted through a live API.
    *   *Why D is incorrect:* Network-level access restriction limits who can reach the endpoint but does not prevent adversarial inputs from authorized users or compromised systems.

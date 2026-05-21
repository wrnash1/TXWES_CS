# Quiz: Module 10 - Machine Learning Concepts for Analysts
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
A retail company wants to predict whether a customer will churn (cancel their subscription) in the next 30 days, using historical account data where each customer is labeled as "churned" or "retained." Which type of machine learning task is this?
*   A) Unsupervised learning — clustering customers into groups based on behavior similarity.
*   B) Supervised learning — classification, because the target variable is a known categorical label.
*   C) Supervised learning — regression, because churn probability is a continuous numeric prediction.
*   D) Unsupervised learning — anomaly detection, because churned customers are rare outliers.
*   **Correct Answer:** B) Supervised learning — classification, because the target variable is a known categorical label.
*   **Distractor Analysis:**
    *   *Why correct:* The dataset has labeled outcomes ("churned" or "retained"), making this a supervised problem. The target is a discrete category, making it classification rather than regression.
    *   A) Unsupervised clustering does not use labels — it discovers natural groupings. This problem has known labels. C) Regression predicts a continuous number. Churn is a binary category, not a continuous value, even though a probability score could be produced downstream. D) Anomaly detection identifies rare unexpected patterns in unlabeled data; this problem has explicit labeled examples of each class.

---

**Question 2**
In machine learning, which of the following most accurately defines **overfitting**?
*   A) A condition where the model is too simple to capture the underlying pattern in the data, resulting in poor performance on both training and test sets.
*   B) A condition where the model learns the training data so precisely — including its noise and random variation — that it performs significantly worse on new, unseen data.
*   C) A data preparation problem where information from the test set inadvertently influences the training process, producing an inflated estimate of model performance.
*   D) A training technique that randomly drops a percentage of neurons in a neural network during each iteration to prevent any single pathway from dominating the learned representation.
*   **Correct Answer:** B) A condition where the model learns the training data so precisely — including its noise and random variation — that it performs significantly worse on new, unseen data.
*   **Distractor Analysis:**
    *   *Why B is correct:* Overfitting is the failure to generalize. The model memorizes training examples rather than learning the underlying pattern, so it scores high on training data but poorly on the test set. A large gap between training accuracy and test accuracy is the telltale sign.
    *   *Why A is incorrect:* A model too simple to capture any pattern describes underfitting, which is the opposite of overfitting. Underfitting results in poor performance on both the training and test sets.
    *   *Why C is incorrect:* Information from the test set influencing training describes data leakage — a data preparation error that produces misleadingly optimistic performance estimates, distinct from overfitting.
    *   *Why D is incorrect:* Randomly dropping neurons during training describes dropout regularization — a technique used to prevent overfitting, not the definition of overfitting itself.

---

**Question 3**
A data science team builds a customer segmentation model to divide 50,000 customers into distinct behavioral groups. The customers have no pre-existing category labels — the team wants the data itself to reveal natural groupings. Which machine learning approach is most appropriate?
*   A) Supervised classification using logistic regression with "customer tier" as the target label.
*   B) Supervised regression using linear regression to predict each customer's lifetime value.
*   C) Unsupervised clustering using k-means to discover natural groupings based on purchase behavior features.
*   D) Supervised learning with a decision tree trained on a labeled training set of manually categorized customers.
*   **Correct Answer:** C) Unsupervised clustering using k-means to discover natural groupings based on purchase behavior features.
*   **Distractor Analysis:**
    *   *Why C is correct:* The problem has no labels — the goal is to discover unknown structure. Unsupervised clustering is precisely designed for this. K-means partitions customers into k groups by minimizing the distance between each point and its cluster centroid.
    *   *Why A is incorrect:* Logistic regression is a supervised classifier — it requires labeled training examples. The scenario explicitly states there are no pre-existing category labels.
    *   *Why B is incorrect:* Linear regression is supervised and predicts a continuous value such as lifetime value, not group membership. The goal here is segmentation, not numeric prediction.
    *   *Why D is incorrect:* A decision tree is a supervised model requiring a labeled training set. Without pre-existing labels, there is no target variable to train against.

---

**Question 4**
After training a fraud detection model, an analyst reports 99.2% training accuracy and 71% test accuracy. What does this gap indicate, and what is the most appropriate remediation?
*   A) The model is underfitting — the algorithm is too simple. The fix is to use a more complex model architecture.
*   B) The model is overfitting — it has memorized training data rather than learning generalizable patterns. Remediation includes reducing model complexity, adding regularization, or obtaining more training data.
*   C) The model has a data leakage problem — test data was used during training. The fix is to retrain without the test set.
*   D) The accuracy metrics are computed incorrectly. The fix is to re-run evaluation using a different performance metric such as F1 score.
*   **Correct Answer:** B) The model is overfitting — it has memorized training data rather than learning generalizable patterns. Remediation includes reducing model complexity, adding regularization, or obtaining more training data.
*   **Distractor Analysis:**
    *   *Why B is correct:* A 28-percentage-point gap between training accuracy (99.2%) and test accuracy (71%) is the defining symptom of overfitting. The model performs well on data it has seen but fails to generalize to new cases.
    *   *Why A is incorrect:* Underfitting produces poor performance on both training and test sets. A 99.2% training accuracy is excellent, not poor — the model has more than enough capacity to fit the training data.
    *   *Why C is incorrect:* Data leakage would cause the test accuracy to appear artificially high, not low. If test data contaminated training, the reported test accuracy would be inflated, not depressed.
    *   *Why D is incorrect:* While F1 score is often more informative than accuracy for imbalanced fraud datasets, re-running with a different metric would not close the performance gap between training and test sets. The root cause is overfitting, not a metric choice.

---

**Question 5**
A data analyst splits a 10,000-row labeled dataset into training, validation, and test sets before building a model. A colleague suggests skipping the validation set to give the model more training data. Why is the validation set important and why should it be kept?
*   A) The validation set is used to measure final model performance and report accuracy to stakeholders — removing it means there is no way to evaluate the deployed model.
*   B) The validation set is used to tune model hyperparameters and compare candidate models during development, without contaminating the test set that must remain unseen until final evaluation.
*   C) The validation set prevents overfitting by automatically removing noisy training examples before the model sees them.
*   D) The validation set is required by law for any model trained on personally identifiable information under data privacy regulations.
*   **Correct Answer:** B) The validation set is used to tune model hyperparameters and compare candidate models during development, without contaminating the test set that must remain unseen until final evaluation.
*   **Distractor Analysis:**
    *   *Why B is correct:* Using the test set to make iterative modeling decisions is a form of data leakage — the model indirectly learns from the test set, inflating the final performance estimate. The validation set provides an independent benchmark for each iteration while preserving the test set's integrity as a truly held-out final evaluation.
    *   *Why A is incorrect:* The test set, not the validation set, is used to report final model performance to stakeholders. The validation set is an internal development tool, not the final evaluation benchmark.
    *   *Why C is incorrect:* The validation set does not filter or clean training data. It is a separate subset used to evaluate the model after training, not a preprocessing step applied before training.
    *   *Why D is incorrect:* No data privacy regulation (GDPR, CCPA, HIPAA) mandates a train/validation/test split. This is a machine learning best practice for building reliable models, not a legal compliance requirement.

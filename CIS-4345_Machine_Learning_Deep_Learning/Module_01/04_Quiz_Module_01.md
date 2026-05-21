# Quiz: Module 01 - ML Fundamentals
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
What is the primary reason for splitting data into Training and Testing datasets?
*   A) To save disk storage space
*   B) To evaluate how the model performs on unseen data and detect overfitting
*   C) To double-compile datasets for faster inference
*   D) To format files for relational database engines
*   **Correct Answer:** B) Testing datasets provide unbiased metrics indicating how well models generalize to new inputs.
*   **Distractor Analysis:**
    *   *Why correct:* A held-out test set has not influenced weight updates during training, so its accuracy is an honest estimate of real-world performance.
    *   *Why A is incorrect:* Data splitting has no effect on disk storage; both partitions still occupy disk space.
    *   *Why C is incorrect:* There is no "double compile" step in ML pipelines; compilation refers to model graph building, not data.
    *   *Why D is incorrect:* Data partitioning is a statistical concern, not a database formatting operation.

---

**Question 2**
Which of the following is the most accurate definition of **supervised learning**?
*   A) A method where an agent explores an environment and receives reward signals to improve its policy.
*   B) A training paradigm in which labeled input-output pairs teach the model to predict target values for new inputs.
*   C) A technique that groups data points based on similarity without any labeled examples.
*   D) A process of reducing the number of input features by projecting data to a lower-dimensional space.
*   **Correct Answer:** B) In supervised learning, the model learns from explicit input-label pairs and is evaluated on prediction accuracy for unseen inputs.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes reinforcement learning, which relies on reward signals rather than labeled data.
    *   *Why B is correct:* Labeled (X, y) pairs are the defining characteristic of supervised learning; regression and classification are both supervised.
    *   *Why C is incorrect:* This describes unsupervised clustering (e.g., k-means), where no labels guide training.
    *   *Why D is incorrect:* This describes dimensionality reduction (e.g., PCA), which is typically unsupervised.

---

**Question 3**
A developer needs to **split a dataset into training and test sets** using scikit-learn. Which command is most appropriate?
*   A) `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)`
*   B) `model.fit(X, y, validation_split=0.2)`
*   C) `np.concatenate([X_train, X_test], axis=0)`
*   D) `accuracy_score(y_test, predictions)`
*   **Correct Answer:** A) `train_test_split` from `sklearn.model_selection` partitions arrays into random train and test subsets.
*   **Distractor Analysis:**
    *   *Why A is correct:* `train_test_split` is the standard scikit-learn utility for creating separate train/test partitions before any model is defined.
    *   *Why B is incorrect:* `validation_split` inside `model.fit()` creates a Keras validation set during training but does not produce separate train/test arrays for pipeline use.
    *   *Why C is incorrect:* `np.concatenate` merges arrays together — the opposite of splitting them.
    *   *Why D is incorrect:* `accuracy_score` evaluates a trained model; it does not partition data.

---

**Question 4**
A model achieves 99% accuracy on the training set but only 62% accuracy on the test set. What ML problem does this most likely indicate?
*   A) Underfitting — the model is too simple to capture the data's patterns.
*   B) Overfitting — the model has memorized training data and fails to generalize.
*   C) Data leakage — test set information was used during training preprocessing.
*   D) Class imbalance — the label distribution is skewed toward a majority class.
*   **Correct Answer:** B) A large gap between training accuracy and test accuracy is the classic symptom of overfitting.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Underfitting produces low accuracy on both training and test sets, not a large gap between the two.
    *   *Why B is correct:* The model memorized noise in the training data; common fixes include more training data, dropout, regularization, or a simpler architecture.
    *   *Why C is incorrect:* Data leakage would typically cause inflated test accuracy, not deflated test accuracy.
    *   *Why D is incorrect:* Class imbalance causes a model to favor the majority class, which would not specifically produce near-perfect training accuracy.

---

**Question 5**
In the context of ML pipelines, which of the following best describes **reinforcement learning**?
*   A) Training a model on a fixed dataset of image-label pairs to classify photos of cats and dogs.
*   B) Clustering customer purchase records into segments without any predefined categories.
*   C) An agent learns to play a game by receiving a positive reward for winning moves and a negative reward for losing moves.
*   D) Reducing a 512-feature dataset down to 10 principal components for visualization.
*   **Correct Answer:** C) Reinforcement learning uses a reward/penalty signal to guide an agent's policy through trial and error in an environment.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Image-label pairs define a supervised classification task, not reinforcement learning.
    *   *Why B is incorrect:* Grouping unlabeled records describes unsupervised clustering.
    *   *Why C is correct:* The defining elements of RL are an agent, an environment, actions, and a reward signal — no labeled dataset is required.
    *   *Why D is incorrect:* Principal component analysis is an unsupervised dimensionality reduction technique.

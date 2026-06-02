# Quiz: Module 01 - ML Fundamentals

**Course:** CIS-4345 Machine Learning and Deep Learning

**Institution:** Texas Wesleyan University

**Instructor:** Professor Nash

**Instructions:** Select the single best answer for each question. Each question is worth 10 points (100 points total). Align your study to the TensorFlow Developer Certificate objectives listed in the candidate handbook at tensorflow.org/certificate.

---

## Question 1

What is the primary reason for splitting a dataset into training and test partitions before building a machine learning model?

- A) To reduce the total file size of the dataset on disk.
- B) To evaluate how the model performs on unseen data and detect overfitting.
- C) To double-compile the dataset for faster inference at runtime.
- D) To format the data for compatibility with relational database engines.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The test set contains examples the model has never seen during training. Because these examples did not influence any weight update, the model's accuracy on them is an honest estimate of real-world generalization performance. A large gap between training accuracy and test accuracy is the diagnostic signature of overfitting.
- *Why A is incorrect:* Both partitions still exist on disk after splitting; no storage is saved. The split is a statistical decision, not a storage optimization.
- *Why C is incorrect:* There is no "double-compile" concept in machine learning pipelines. Model compilation in Keras refers to specifying the optimizer and loss function, not to data preparation.
- *Why D is incorrect:* Data partitioning is a statistical practice aimed at unbiased performance estimation. It has no relationship to database file formats or schema design.

---

## Question 2

Which of the following most accurately defines supervised learning?

- A) A method where an agent explores an environment and receives reward signals to improve its decision policy.
- B) A training paradigm in which labeled input-output pairs are used to teach the model to predict target values for new inputs.
- C) A technique that groups data points based on similarity without any labeled examples.
- D) A process that reduces the number of input features by projecting data to a lower-dimensional space.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Labeled pairs (X, y) are the defining characteristic of supervised learning. The model learns the mapping from features to labels, and its quality is measured by prediction accuracy on held-out examples. Both classification and regression are supervised tasks.
- *Why A is incorrect:* This describes reinforcement learning, which uses a reward signal rather than labeled examples and does not require a fixed dataset.
- *Why C is incorrect:* This describes unsupervised clustering such as k-means, where no labels guide training and the algorithm discovers groupings on its own.
- *Why D is incorrect:* This describes dimensionality reduction such as PCA or autoencoders, which are typically unsupervised techniques for compressing feature representations.

---

## Question 3

A developer calls the following scikit-learn function to prepare data for a supervised model. Which statement best describes what this call accomplishes?

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

- A) It merges the arrays X and y into a single matrix for model input.
- B) It randomly partitions X and y into 80% training and 20% test subsets while preserving class proportions.
- C) It creates a Keras validation split used during the model.fit() call.
- D) It computes accuracy scores between y_test and model predictions.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* `train_test_split` with `test_size=0.2` places 20% of samples in the test set and 80% in the training set. The `stratify=y` argument ensures both subsets contain the same proportion of each class label as the original dataset, which is critical for imbalanced problems.
- *Why A is incorrect:* `np.concatenate` or `np.hstack` merges arrays. `train_test_split` does the opposite — it divides them.
- *Why C is incorrect:* A Keras validation split is created by passing `validation_split=0.2` inside `model.fit()`. That is a different mechanism that operates during training, not before the model is defined.
- *Why D is incorrect:* `accuracy_score(y_test, predictions)` computes accuracy. `train_test_split` does not evaluate a model; it prepares data partitions.

---

## Question 4

A model achieves 99% accuracy on the training set but only 61% accuracy on the validation set after 30 epochs. What ML problem does this most likely indicate, and what is one appropriate remedy?

- A) Underfitting — the model is too simple. Add more layers or neurons.
- B) Overfitting — the model has memorized training noise. Apply dropout or L2 regularization.
- C) Data leakage — test set information was used during preprocessing. Re-split the data.
- D) Class imbalance — the label distribution is skewed. Apply SMOTE to oversample the minority class.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A large gap between training accuracy (99%) and validation accuracy (61%) is the textbook symptom of overfitting. The model has memorized patterns specific to the training set, including its noise, rather than learning generalizable rules. Dropout randomly zeroes activations during training, acting as an ensemble regularizer. L2 (weight decay) penalizes large weights and encourages smoother decision boundaries.
- *Why A is incorrect:* Underfitting produces low accuracy on both training and validation sets. The training accuracy of 99% rules out underfitting because an underfitting model cannot even fit the training data well.
- *Why C is incorrect:* Data leakage typically inflates validation or test accuracy beyond what the model should achieve, not deflates it. The scenario shows deflated validation accuracy, which points to overfitting rather than leakage.
- *Why D is incorrect:* Class imbalance causes models to favor the majority class, which would result in moderate but similar accuracy on both sets — not near-perfect training accuracy paired with very low validation accuracy.

---

## Question 5

In the bias-variance tradeoff, what does "high variance" mean in the context of a trained model?

- A) The model makes consistently large errors on both training and test data due to overly simple assumptions.
- B) The model's predictions are highly sensitive to the specific training set used, leading to poor generalization.
- C) The model's loss function contains many local minima that prevent convergence.
- D) The model's feature inputs have widely different numerical scales that destabilize gradient descent.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* High variance means the model has fit the training data too closely — it has memorized noise that does not exist in new examples. If you trained the same architecture on a slightly different sample of data, you would get substantially different weights and predictions. The manifestation is high training accuracy coupled with poor test accuracy.
- *Why A is incorrect:* This describes high bias, not high variance. High bias means the model is too simple to capture the real pattern and therefore makes large errors on both training and test data.
- *Why C is incorrect:* Loss landscape geometry (local minima) is an optimization concern, not a description of bias or variance. Non-convex loss surfaces are addressed through optimizer choice and learning rate schedules.
- *Why D is incorrect:* This describes a feature scaling issue that affects gradient descent stability. While important, it is not the definition of variance in the statistical bias-variance sense.

---

## Question 6

Which of the following correctly identifies the three-step Keras pattern required on every TensorFlow Developer Certificate exam problem?

- A) load_data(), preprocess(), train()
- B) Sequential(), compile(), fit()
- C) import(), build(), deploy()
- D) InputLayer(), HiddenLayer(), OutputLayer()

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Every Keras model requires (1) defining the architecture with `tf.keras.Sequential([...])` or the functional API, (2) compiling with `model.compile(optimizer=, loss=, metrics=)`, and (3) training with `model.fit(X_train, y_train, ...)`. This exact three-step sequence appears on every TensorFlow Developer Certificate exam problem.
- *Why A is incorrect:* `load_data()` and `preprocess()` are data pipeline steps that happen before model definition. They are important but are not Keras API method names, and they do not constitute the model building pattern.
- *Why C is incorrect:* `import()` is a Python language statement, not a Keras method. `deploy()` is a post-training step handled by TF Serving or TFLite, not a model-building step.
- *Why D is incorrect:* These are conceptual layer names, not Keras API calls. Keras uses `tf.keras.layers.Dense()`, `tf.keras.layers.Conv2D()`, etc. There is no `HiddenLayer()` class in the Keras API.

---

## Question 7

A StandardScaler is fit on the training set and then used to transform both the training and test sets. Why is it incorrect to fit a new StandardScaler separately on the test set?

- A) It would make the test set too large to fit in memory.
- B) It would introduce data leakage by allowing test set statistics to influence preprocessing decisions.
- C) It would cause the model to train faster than intended.
- D) The test set does not contain enough samples to compute a stable mean and variance.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Fitting a scaler on the test set means the test set's mean and standard deviation are used in preprocessing. This allows information about the test distribution to leak into the pipeline, which invalidates the test set as an independent performance estimate. The correct practice is to fit the scaler on training data only and apply those training statistics when transforming the test set.
- *Why A is incorrect:* Scaler statistics are two numbers per feature (mean and standard deviation), consuming negligible memory regardless of dataset size.
- *Why C is incorrect:* Scaler fitting speed is irrelevant to model training speed. Training speed is determined by model size, batch size, and hardware — not by how the scaler was fit.
- *Why D is incorrect:* While small test sets do produce less stable statistics, that is not the primary reason. Even with a large test set, fitting the scaler on test data constitutes data leakage and is incorrect practice.

---

## Question 8

Which of the following describes the role of the validation set in model development, as distinct from the test set?

- A) The validation set is used to compute the final reported performance metric submitted with the model.
- B) The validation set is used during training to monitor overfitting and guide hyperparameter tuning decisions.
- C) The validation set replaces the training set when the training set is too small.
- D) The validation set is a random subset of the test set held back for cross-validation.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The validation set is observed during training (via `validation_data=` in `model.fit()`) to track generalization performance epoch by epoch. It guides decisions like when to stop training, which learning rate to use, and how many layers to include. Because it influences these decisions, it cannot provide an unbiased final performance estimate — that role belongs exclusively to the test set, which is touched only once.
- *Why A is incorrect:* Final reported performance uses the test set, not the validation set. Reporting validation accuracy as the final result is a form of optimistic bias.
- *Why C is incorrect:* The validation set does not replace the training set; the model is never trained on validation data. With very small datasets, k-fold cross-validation is used instead of a fixed validation split.
- *Why D is incorrect:* The validation set is a separate third partition created from the original dataset, not a subset of the test set. Treating part of the test set as a validation set compromises the independence of the test evaluation.

---

## Question 9

A data scientist is building a model to predict hospital readmission (yes/no) from patient records. The dataset contains 9,200 negative cases and 800 positive cases. Which preprocessing concern is most critical before training?

- A) The features must be one-hot encoded before the train-test split.
- B) The dataset should be shuffled and then a stratified split applied to maintain class proportions.
- C) The numerical features must be converted to categorical bins before scaling.
- D) The dataset must be reduced to 1,000 samples total so the classes are balanced.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* With 92% negative and 8% positive cases, the dataset is highly imbalanced. A random (non-stratified) split might by chance place most positive cases in the training set or the test set. Stratified splitting guarantees that both partitions contain approximately 8% positive cases, ensuring the evaluation reflects the true class distribution. Shuffling before splitting prevents temporal ordering artifacts.
- *Why A is incorrect:* One-hot encoding is applied during feature preprocessing, and while important, it is not the most critical concern with an imbalanced dataset. It also does not need to precede the train-test split; in fact, fitting any encoder (including one-hot) should happen only after splitting to avoid leakage.
- *Why C is incorrect:* Converting numerical features to bins discards information and is generally harmful. Numerical features should be scaled (standardized or normalized), not binned, before feeding to a neural network.
- *Why D is incorrect:* Truncating to 1,000 samples throws away 90% of the data, which dramatically reduces the model's ability to learn patterns. Better strategies for class imbalance include class weighting (`class_weight` in `model.fit()`), oversampling the minority class, or using appropriate metrics like F1-score.

---

## Question 10

The TensorFlow Developer Certificate exam requires candidates to build Keras models that achieve specified accuracy thresholds. Which output layer configuration is correct for a 10-class image classification problem where labels are provided as integers (0-9)?

- A) `Dense(1, activation='sigmoid')`
- B) `Dense(10, activation='softmax')` with loss `sparse_categorical_crossentropy`
- C) `Dense(10, activation='relu')` with loss `mean_squared_error`
- D) `Dense(2, activation='softmax')` with loss `binary_crossentropy`

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A 10-class classification problem requires 10 output neurons — one per class. The softmax activation converts the 10 raw logits into a probability distribution that sums to 1.0. When labels are provided as integers (0 through 9), `sparse_categorical_crossentropy` is the correct loss function. If labels were one-hot encoded, `categorical_crossentropy` would be used instead.
- *Why A is incorrect:* A single sigmoid neuron outputs a probability between 0 and 1 for a binary (two-class) problem. It cannot represent probabilities across 10 separate classes. Using this output layer would collapse all 10 classes into a single binary decision.
- *Why C is incorrect:* ReLU is not a valid output activation for classification. It does not produce probabilities and can output any non-negative value. MSE is a regression loss and is not appropriate for multi-class classification because it does not penalize the model for incorrect class assignments correctly.
- *Why D is incorrect:* Two output neurons with binary_crossentropy is designed for binary classification, not 10-class classification. This configuration would attempt to treat the problem as two independent binary decisions rather than a single 10-way mutually exclusive choice.

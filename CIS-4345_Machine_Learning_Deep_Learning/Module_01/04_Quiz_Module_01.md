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

---

### Question 11 (5 points)

Which optimizer is most commonly recommended as a default for training deep neural networks due to its adaptive learning rate and momentum properties?

- A) Stochastic Gradient Descent (SGD) with no momentum
- B) Adam (Adaptive Moment Estimation)
- C) Newton's Method
- D) Coordinate Descent

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Adam combines the benefits of AdaGrad (adaptive per-parameter learning rates) and RMSProp (exponential moving average of squared gradients) with momentum. It generally converges faster than vanilla SGD and requires minimal hyperparameter tuning, making it the practical default for most deep learning tasks.
  - *Why A is incorrect:* Vanilla SGD without momentum converges slowly and is sensitive to the learning rate choice. While it can achieve competitive results with careful tuning and learning rate schedules, it is not the recommended default for beginners.
  - *Why C is incorrect:* Newton's Method requires computing the full Hessian matrix (second-order derivatives), which is computationally intractable for neural networks with millions of parameters.
  - *Why D is incorrect:* Coordinate Descent optimizes one parameter at a time while holding others fixed. It is impractical for high-dimensional neural network weight spaces and is not used in standard deep learning frameworks.

---

### Question 12 (5 points)

A regression model predicts house prices. After training, the Mean Absolute Error (MAE) on the training set is $8,000 and the MAE on the test set is $9,200. What does this most likely indicate?

- A) The model is severely overfitting and requires substantial regularization.
- B) The model generalizes well — the small gap between training and test error is acceptable.
- C) The model is underfitting and needs more layers.
- D) The dataset has class imbalance that must be corrected with SMOTE.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A difference of only $1,200 between training MAE ($8,000) and test MAE ($9,200) represents a small generalization gap (about 15%). Both values are in the same range, indicating the model has learned a pattern that transfers well to unseen data — a sign of good generalization, not overfitting.
  - *Why A is incorrect:* Severe overfitting would produce a very small training error paired with a dramatically higher test error (e.g., training MAE $1,000 vs. test MAE $40,000). The values here are close, ruling out severe overfitting.
  - *Why C is incorrect:* Underfitting produces high error on both training and test sets. The pattern here (similar train and test error) is not diagnostic of underfitting.
  - *Why D is incorrect:* SMOTE (Synthetic Minority Over-sampling Technique) addresses class imbalance in classification problems. This is a regression problem with a continuous target (price), so class imbalance and SMOTE are not applicable.

---

### Question 13 (5 points)

In k-fold cross-validation with k=5, how many times is the model trained and what fraction of data is used for validation in each fold?

- A) Trained 1 time; 20% validation
- B) Trained 5 times; 20% validation each fold
- C) Trained 5 times; 80% validation each fold
- D) Trained 10 times; 10% validation each fold

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In 5-fold cross-validation, the data is split into 5 equal-sized folds. The model is trained 5 times: each time, 4 folds (80%) form the training set and 1 fold (20%) forms the validation set. Each fold serves as the validation set exactly once, giving an unbiased performance estimate with full data utilization.
  - *Why A is incorrect:* If the model were trained only once, it would be a simple hold-out validation, not cross-validation. The defining feature of k-fold cross-validation is the k separate training runs.
  - *Why C is incorrect:* In 5-fold CV, each fold is 1/5 = 20% of the data, not 80%. The 80% figure is the training fraction, not the validation fraction.
  - *Why D is incorrect:* This describes 10-fold cross-validation, not 5-fold. With k=5, exactly 5 training runs occur, each using 20% for validation.

---

### Question 14 (5 points)

Which of the following is the correct Keras definition of a multi-layer perceptron for binary classification with two hidden layers of 128 and 64 neurons?

- A) `Sequential([Dense(128), Dense(64), Dense(2, activation='softmax')])`
- B) `Sequential([Dense(128, activation='relu'), Dense(64, activation='relu'), Dense(1, activation='sigmoid')])`
- C) `Sequential([Dense(128, activation='sigmoid'), Dense(64, activation='sigmoid'), Dense(1, activation='relu')])`
- D) `Sequential([Dense(128, activation='softmax'), Dense(64, activation='softmax'), Dense(1)])`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* ReLU activation is standard for hidden layers because it introduces non-linearity, is computationally efficient, and mitigates the vanishing gradient problem. For binary classification, the output layer uses a single neuron with sigmoid activation, producing a probability between 0 and 1.
  - *Why A is incorrect:* Hidden layers without activations are linear transformations — the entire network collapses to a single linear function regardless of depth. A 2-neuron softmax output is for 2-class multi-class classification and requires `sparse_categorical_crossentropy`.
  - *Why C is incorrect:* Sigmoid hidden layers suffer from the vanishing gradient problem — gradients shrink exponentially through sigmoid neurons, making deep networks very slow to train. ReLU is preferred for hidden layers.
  - *Why D is incorrect:* Softmax in hidden layers forces units to compete against each other and is only appropriate for the output layer of a multi-class classifier. A linear final neuron outputs a raw logit, not a probability.

---

### Question 15 (5 points)

What is the purpose of the `random_state` parameter in scikit-learn functions like `train_test_split` and `RandomForestClassifier`?

- A) It controls how quickly the random number generator runs, affecting training speed.
- B) It seeds the random number generator so that results are reproducible across runs.
- C) It limits the model to use only a random subset of features during each training step.
- D) It sets the initial learning rate for the optimizer used during training.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `random_state` seeds Python's (and NumPy's) pseudo-random number generator. When the same seed is used, all random operations — shuffling, splitting, initialization — produce identical results. This is essential for reproducibility: another researcher running the same code gets the same model and evaluation.
  - *Why A is incorrect:* `random_state` has no effect on computational speed. It only determines the sequence of random numbers generated, not how fast those numbers are computed.
  - *Why C is incorrect:* The `max_features` parameter of `RandomForestClassifier` controls the fraction of features considered at each split. `random_state` seeds the RNG used for that random selection but does not directly limit features.
  - *Why D is incorrect:* The learning rate is set through the `learning_rate` parameter of the optimizer (e.g., `tf.keras.optimizers.Adam(learning_rate=0.001)`). `random_state` has nothing to do with optimization.

---

### Question 16 (5 points)

A dataset has a feature "income" ranging from $20,000 to $500,000 and a feature "age" ranging from 18 to 90. Which preprocessing step should be applied before training a neural network?

- A) One-hot encode both features to create binary indicator variables.
- B) Apply feature scaling (StandardScaler or MinMaxScaler) to bring both features to similar ranges.
- C) Drop the "income" feature because its large values will cause numerical overflow.
- D) Convert both features to categorical bins before model training.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Neural networks use gradient descent. When features have vastly different scales, the loss surface becomes elongated and ill-conditioned — gradients for the small-scale feature are much smaller than for the large-scale feature, causing slow or oscillating convergence. Scaling ensures all features contribute equally to gradient updates.
  - *Why A is incorrect:* One-hot encoding is for categorical variables (e.g., color = {red, blue, green}). Income and age are continuous numerical variables that should be scaled, not one-hot encoded.
  - *Why C is incorrect:* Modern float32 representations handle values up to ~3.4×10^38. An income of $500,000 causes no overflow. The issue is gradient scale imbalance, not numerical overflow.
  - *Why D is incorrect:* Binning continuous features into categories destroys ordinal information and reduces signal available to the model. Scaling is the correct approach for continuous numerical features.

---

### Question 17 (5 points)

Which evaluation metric is most appropriate when false negatives are much more costly than false positives, such as in a cancer screening test?

- A) Accuracy
- B) Precision
- C) Recall
- D) Specificity

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Recall = TP / (TP + FN). A false negative in cancer screening means telling a sick patient they are healthy — a potentially fatal outcome. High recall minimizes false negatives by ensuring the model catches as many true positive cases as possible, even at the cost of more false positives.
  - *Why A is incorrect:* Accuracy weights all errors equally. On an imbalanced cancer dataset (e.g., 95% healthy), a model predicting "healthy" for everyone would achieve 95% accuracy while catching zero cancer cases — a dangerous outcome.
  - *Why B is incorrect:* Precision = TP / (TP + FP). Precision minimizes false positives. While precision matters in some contexts (e.g., spam filtering), in cancer screening the priority is not missing true cases, which is recall's domain.
  - *Why D is incorrect:* Specificity = TN / (TN + FP) — it measures how well the model identifies true negatives (healthy patients). While useful, specificity does not directly measure the false negative rate, which is the primary concern in life-critical screening.

---

### Question 18 (5 points)

In neural network training, what is a "training epoch"?

- A) One forward pass through a single training example.
- B) One complete pass through the entire training dataset.
- C) One update of the model's weights using a mini-batch of samples.
- D) The total number of layers in the network.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* An epoch is one complete cycle through all training examples. If the training set has 10,000 samples and the batch size is 100, then one epoch consists of 100 gradient update steps (iterations). Training typically runs for many epochs (e.g., 50–200) to allow the model to converge.
  - *Why A is incorrect:* A single forward pass through one sample is not an epoch. In stochastic gradient descent (batch size = 1), it is one gradient update step. The term "epoch" always refers to the full dataset cycle.
  - *Why C is incorrect:* This describes one training step or iteration (a mini-batch update). An epoch contains many such steps: n_samples / batch_size steps per epoch.
  - *Why D is incorrect:* The number of layers describes the network depth or architecture, not a temporal unit of training. Depth is a design choice made before training begins.

---

### Question 19 (5 points)

What does `model.evaluate(X_test, y_test)` return in Keras, and when should it be called?

- A) It returns the model's weights and should be called after every epoch.
- B) It returns the loss and metric values on the provided data and should be called once on the held-out test set after training is complete.
- C) It returns predictions (class probabilities) for X_test and should be called during training.
- D) It computes the gradient of the loss with respect to all weights and updates them.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `model.evaluate()` runs a forward pass (no weight updates) over the provided data and returns the loss value followed by any metrics specified in `model.compile(metrics=[...])`. It should be called exactly once on the test set after all training and hyperparameter decisions are finalized.
  - *Why A is incorrect:* Model weights are accessed via `model.get_weights()`. Calling `evaluate()` after every epoch on the test set violates the principle of keeping the test set unseen — use `validation_data` in `model.fit()` instead.
  - *Why C is incorrect:* Predictions are obtained with `model.predict(X_test)`, which returns per-sample class probabilities (or logits). `model.evaluate()` returns scalar metrics, not per-sample predictions.
  - *Why D is incorrect:* This describes the backpropagation step inside `model.fit()`. `model.evaluate()` is a read-only operation — it computes metrics but does not modify any weights.

---

### Question 20 (5 points)

A machine learning engineer wants to predict the selling price of a car (a continuous dollar amount) from its features. Which combination of output layer and loss function is correct for this regression task in Keras?

- A) `Dense(1, activation='sigmoid')` with `binary_crossentropy`
- B) `Dense(1)` (no activation) with `mean_squared_error`
- C) `Dense(1, activation='softmax')` with `categorical_crossentropy`
- D) `Dense(1, activation='relu')` with `sparse_categorical_crossentropy`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Regression tasks require predicting a continuous real-valued output. A single output neuron with no activation (linear) can output any real number, which is appropriate for an unbounded quantity like price. MSE penalizes the squared difference between predicted and actual price, providing a smooth gradient signal for regression.
  - *Why A is incorrect:* Sigmoid outputs values in (0, 1). Car prices can be any positive number far exceeding 1.0. Binary crossentropy is a classification loss designed for probabilities, not continuous targets.
  - *Why C is incorrect:* Softmax produces a probability distribution over discrete classes. It is designed for multi-class classification. A single softmax neuron always outputs 1.0, which is useless for regression.
  - *Why D is incorrect:* ReLU in the output layer clips all predicted prices to be non-negative. `sparse_categorical_crossentropy` is a classification loss for integer class labels and is incompatible with a continuous regression target.

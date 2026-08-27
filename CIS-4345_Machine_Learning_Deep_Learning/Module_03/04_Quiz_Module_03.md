# Quiz: Module 03 - Linear and Logistic Regression
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
Which mathematical function maps real-number inputs to a probability value between 0 and 1 in logistic regression?
*   A) ReLU: max(0, x), which outputs zero for all negative inputs
*   B) Sigmoid: σ(x) = 1 / (1 + e^−x), which outputs values strictly between 0 and 1
*   C) Linear: f(x) = wx + b, which can produce any real-number output
*   D) Softmax, which distributes probability mass across multiple output classes
*   **Correct Answer:** B) The sigmoid function outputs values bounded between 0 and 1, making it suitable for interpreting outputs as probabilities.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ReLU outputs zero for negative inputs and the raw input for positive inputs — it is unbounded above and cannot represent probabilities.
    *   *Why B is correct:* Sigmoid is the defining activation for binary classification; in Keras: `Dense(1, activation='sigmoid')`.
    *   *Why C is incorrect:* A linear activation produces unbounded outputs and is used for regression, not probability estimation.
    *   *Why D is incorrect:* Softmax distributes probability across multiple classes and is used for multi-class classification, not binary logistic regression.

---

**Question 2**
Which of the following is the most accurate definition of **probability mapping** in the context of logistic regression?
*   A) The process of converting raw model outputs (logits) into class-probability estimates using the sigmoid activation, so the output represents the likelihood that an input belongs to the positive class.
*   B) A lookup table that maps each unique word token to a fixed integer index in a text vocabulary, used to encode sentences for NLP models.
*   C) A matrix operation that projects high-dimensional feature vectors onto a lower-dimensional subspace while maximizing retained variance.
*   D) The assignment of integer labels to categorical string features, such as encoding {red, green, blue} as {0, 1, 2} for ordinal model input.
*   **Correct Answer:** A) Probability mapping transforms unbounded logit scores into calibrated probabilities using the sigmoid function.
*   **Distractor Analysis:**
    *   *Why A is correct:* The sigmoid squashes the linear combination w·x + b into (0, 1), producing an interpretable class probability.
    *   *Why B is incorrect:* This describes vocabulary indexing in NLP tokenization, not logistic regression output transformation.
    *   *Why C is incorrect:* This describes PCA or other linear dimensionality reduction, not probability mapping.
    *   *Why D is incorrect:* This describes label/ordinal encoding of categorical features, not output probability computation.

---

**Question 3**
A developer needs to **load tabular data and display basic statistics** about each numeric column. Which command is most appropriate?
*   A) `df = pd.read_csv('data.csv'); df.describe()`
*   B) `model.predict(X_test)`
*   C) `tf.keras.utils.to_categorical(y, num_classes=10)`
*   D) `model.compile(optimizer='adam', loss='mse')`
*   **Correct Answer:** A) `pd.read_csv()` loads the data and `.describe()` returns count, mean, std, min, quartiles, and max for each numeric column.
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the standard Pandas pattern for initial data exploration before any preprocessing or modeling.
    *   *Why B is incorrect:* `model.predict()` generates predictions from a trained model — it does not load or describe raw data.
    *   *Why C is incorrect:* `to_categorical` converts integer labels to one-hot vectors — it does not load or summarize data.
    *   *Why D is incorrect:* `model.compile()` configures the training process — it has no role in data exploration.

---

**Question 4**
For a binary classification task in Keras, which combination of output layer activation and loss function is correct?
*   A) Output activation: `relu`; Loss: `mean_squared_error`
*   B) Output activation: `sigmoid`; Loss: `binary_crossentropy`
*   C) Output activation: `softmax`; Loss: `binary_crossentropy`
*   D) Output activation: `linear`; Loss: `categorical_crossentropy`
*   **Correct Answer:** B) `sigmoid` produces a probability for the positive class and `binary_crossentropy` is the mathematically appropriate loss for two-class problems.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ReLU + MSE is appropriate for regression, not classification; it produces unbounded outputs with no probabilistic interpretation.
    *   *Why B is correct:* This is the canonical Keras pattern for binary classification: `Dense(1, activation='sigmoid')` compiled with `loss='binary_crossentropy'`.
    *   *Why C is incorrect:* `softmax` normalizes over multiple classes and is paired with `categorical_crossentropy` for multi-class tasks, not binary tasks.
    *   *Why D is incorrect:* `linear` activation with `categorical_crossentropy` is not a valid configuration — linear outputs are unbounded and categorical crossentropy expects probability distributions.

---

**Question 5**
In a logistic regression model, what happens to the predicted class label when the sigmoid output is exactly 0.3?
*   A) The model predicts class 1 because 0.3 is a positive probability value.
*   B) The model predicts class 0 because 0.3 is below the standard 0.5 decision threshold.
*   C) The model outputs an error because probabilities must be above 0.5 to be valid.
*   D) The model re-trains automatically because the confidence is too low to make a prediction.
*   **Correct Answer:** B) With a standard 0.5 threshold, any sigmoid output below 0.5 is assigned to class 0 (negative class).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The raw probability value being positive does not determine the predicted class — it must exceed the decision threshold.
    *   *Why B is correct:* The decision rule is: predict class 1 if sigmoid(x) >= 0.5, else predict class 0. A value of 0.3 falls below 0.5, so class 0 is predicted.
    *   *Why C is incorrect:* Probabilities below 0.5 are completely valid outputs — they simply indicate the model believes the negative class is more likely.
    *   *Why D is incorrect:* `model.predict()` is a forward pass only; it never triggers retraining regardless of confidence level.

---

### Question 6 (5 points)

A developer trains a logistic regression model on a dataset with 50,000 samples. Which gradient descent variant updates model weights using the entire training dataset per step, which uses one sample per step, and which uses small subsets per step?

* A) Batch gradient descent uses one sample; SGD uses the full dataset; mini-batch uses subsets.
* B) Batch gradient descent uses the full dataset per step; stochastic gradient descent (SGD) uses one sample per step; mini-batch gradient descent uses a fixed subset (e.g., 32 or 64 samples) per step.
* C) All three variants use the same number of samples — the difference is only in the learning rate used.
* D) Mini-batch gradient descent uses the full dataset; batch gradient descent uses subsets; SGD uses no data (it updates randomly).

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* Batch gradient descent computes the gradient over all 50,000 samples before updating weights — stable but slow per epoch. SGD updates after each individual sample — noisy but fast per update and can escape local minima. Mini-batch gradient descent (the most commonly used in practice, including Keras's default `model.fit()`) computes gradients over small batches (e.g., 32 samples) — balancing stability and speed. In Keras, `model.fit(batch_size=32)` implements mini-batch gradient descent.
  * *Why A is incorrect:* This reverses batch and SGD. Batch gradient descent uses the entire dataset, not one sample.
  * *Why C is incorrect:* The three variants differ fundamentally in how many samples are used per weight update, not just in learning rate. This distinction directly affects gradient noise, convergence speed, and memory requirements.
  * *Why D is incorrect:* Mini-batch does not use the full dataset (that is batch GD), and gradient descent always uses real data to compute gradients — it does not update randomly.

---

### Question 7 (5 points)

A linear regression model is severely overfitting the training data. A developer wants to apply regularization. Which statement correctly distinguishes L1 (Lasso), L2 (Ridge), and ElasticNet regularization?

* A) L1 adds the sum of squared weights to the loss; L2 adds the sum of absolute weights; ElasticNet applies both but with equal fixed weighting.
* B) L1 adds the sum of absolute weight values to the loss, encouraging sparse models by driving some weights to exactly zero; L2 adds the sum of squared weights, shrinking all weights toward zero but rarely eliminating them; ElasticNet combines both L1 and L2 penalties.
* C) L1 and L2 are identical — they both shrink weights toward zero and neither produces exactly zero weights.
* D) ElasticNet is the same as dropout — both randomly zero out model parameters during training.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* L1 regularization adds `λ * Σ|w|` to the loss. Its gradient is constant (the sign of the weight), which causes small weights to reach exactly zero — producing sparse models where irrelevant features are removed. L2 adds `λ * Σw²`, whose gradient scales with weight magnitude, shrinking large weights more than small ones but rarely reaching zero. ElasticNet combines both: `λ₁ * Σ|w| + λ₂ * Σw²`, providing sparsity from L1 and grouping behavior from L2. In Keras: `kernel_regularizer=tf.keras.regularizers.l1_l2(l1=0.01, l2=0.01)`.
  * *Why A is incorrect:* This swaps the definitions of L1 and L2. L1 uses absolute values; L2 uses squared values.
  * *Why C is incorrect:* L1 and L2 behave differently — L1 produces exact zeros (feature selection), L2 produces small but non-zero values. This distinction is a tested concept in the TF Developer Certificate curriculum.
  * *Why D is incorrect:* ElasticNet is a mathematical combination of L1 and L2 weight penalties added to the loss function. Dropout randomly deactivates neuron outputs during training. They are entirely different techniques.

---

### Question 8 (5 points)

A data scientist builds a linear regression model to predict house prices using two features: square footage and number of rooms. The correlation between these two features is 0.97. What problem does this create, and how should it be addressed?

* A) Class imbalance — apply SMOTE to oversample the underrepresented price range.
* B) Multicollinearity — the two features contain nearly identical information, which inflates the variance of coefficient estimates and makes the model's feature weights unstable and difficult to interpret.
* C) Underfitting — the model needs more features or polynomial terms to capture the relationship.
* D) Overfitting — the model has memorized too many features and needs dropout regularization.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* Multicollinearity occurs when two or more predictor features are highly correlated (here, r = 0.97). When features are nearly linearly dependent, the matrix inversion in the closed-form OLS solution becomes numerically unstable, and gradient-based solutions produce coefficient estimates with high variance. Symptoms include coefficients that change dramatically when one feature is removed or added. Solutions include removing one of the correlated features, combining them (e.g., PCA), or applying L2 (Ridge) regularization, which dampens coefficient instability.
  * *Why A is incorrect:* Class imbalance is a classification problem (uneven class distribution). Linear regression predicts a continuous target — "class imbalance" does not apply to regression tasks.
  * *Why C is incorrect:* Underfitting means the model is too simple to capture the underlying pattern. Multicollinearity is a data structure problem, not a model complexity problem, and adding more features would not resolve it.
  * *Why D is incorrect:* Overfitting occurs when the model has too many parameters relative to training samples. Multicollinearity is specifically a problem of feature correlation, not model complexity. Dropout is a technique for neural networks and does not apply to linear regression.

---

### Question 9 (5 points)

A developer notices that a linear regression model performs poorly on a dataset where the relationship between the input feature `x` and the output `y` follows a curve. They decide to add `x²` and `x³` as additional input features. What technique is this, and what is the primary risk of extending it too far?

* A) Feature scaling — normalizing features to the same range; risk is that scaling changes the data distribution.
* B) Polynomial regression — extending linear regression to fit non-linear relationships by adding polynomial feature terms; risk is severe overfitting when the polynomial degree is too high.
* C) Regularization — adding penalty terms to the loss function; risk is that high regularization removes all features.
* D) Dimensionality reduction — compressing high-dimensional data; risk is that important variance is lost.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* Polynomial regression adds powers of the original features (x², x³, ...) as new input features, allowing a linear model to fit non-linear curves. In scikit-learn: `PolynomialFeatures(degree=3)` followed by `LinearRegression()`. The key risk is overfitting — a very high-degree polynomial can pass exactly through every training point but generalize poorly to new data, showing extreme oscillations between training points (Runge's phenomenon).
  * *Why A is incorrect:* Feature scaling (e.g., `StandardScaler`, `MinMaxScaler`) normalizes the range of existing features — it does not add new features or change the model's functional form.
  * *Why C is incorrect:* Regularization (L1/L2) adds penalty terms to the loss function to constrain weight magnitudes. It does not add polynomial feature terms and does not change the model's capacity to fit curves.
  * *Why D is incorrect:* Dimensionality reduction (e.g., PCA) reduces the number of features by combining existing ones. Polynomial regression increases the number of features by creating new polynomial terms — it is the opposite direction.

---

### Question 10 (5 points)

In logistic regression, the sigmoid function maps linear model outputs to probabilities, and binary crossentropy serves as the loss function. Why is binary crossentropy (log-loss) the mathematically correct loss for logistic regression, rather than Mean Squared Error (MSE)?

* A) Binary crossentropy is preferred because it is always computationally faster than MSE for all dataset sizes.
* B) Binary crossentropy is derived from maximum likelihood estimation of the Bernoulli distribution. Its log terms produce large gradient signals when the model is confidently wrong, ensuring effective learning. MSE applied to sigmoid outputs creates a non-convex loss surface and produces small gradients near extreme predictions, causing vanishing gradient problems.
* C) MSE is actually preferred for logistic regression — binary crossentropy is only used in convolutional neural networks.
* D) Binary crossentropy is preferred because it clips gradient values to prevent exploding gradients, which MSE does not do.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* The derivation of logistic regression loss from maximum likelihood estimation of the Bernoulli distribution yields exactly `−[y·log(p) + (1−y)·log(1−p)]` — binary crossentropy. When the model predicts 0.99 for a true class-0 example, `−log(1 − 0.99) = −log(0.01) ≈ 4.6`, producing a large gradient that strongly corrects the weights. With MSE, the sigmoid's derivative is near zero at extreme predictions (the "saturation" zone), producing tiny gradients that cause slow or stalled learning — the vanishing gradient problem. Binary crossentropy combined with sigmoid creates a convex optimization surface; MSE + sigmoid does not.
  * *Why A is incorrect:* Computational speed depends on dataset size, batch size, and hardware — not the loss function type. There is no guarantee binary crossentropy is faster than MSE in all cases.
  * *Why C is incorrect:* Binary crossentropy is the standard loss for binary classification regardless of model type — logistic regression, fully connected networks, and CNNs all use it for binary outputs. MSE is the standard loss for regression, not binary classification.
  * *Why D is incorrect:* Gradient clipping is a separate technique applied to the optimizer (e.g., `tf.keras.optimizers.Adam(clipnorm=1.0)`). Binary crossentropy does not perform gradient clipping — it is a loss function, not an optimization technique.

---

### Question 11 (5 points)

Which loss function is mathematically designed for binary classification and why is it preferred over Mean Squared Error (MSE) for this task?

* A) MSE is preferred because it penalizes large prediction errors more heavily.
* B) Binary crossentropy is preferred because it is derived from the log-likelihood of a Bernoulli distribution and produces larger gradients when the model is confidently wrong.
* C) Binary crossentropy is preferred because it always converges faster regardless of model architecture.
* D) MSE is preferred because it directly measures the probability error between 0 and 1.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* Binary crossentropy = −[y·log(p) + (1−y)·log(1−p)] is the negative log-likelihood of the Bernoulli distribution. When the model is confidently wrong (e.g., predicts 0.99 for a class-0 example), the log term produces a very large gradient signal, pushing weights strongly in the right direction. MSE produces small gradients when the sigmoid output is near 0 or 1, causing vanishingly slow learning.
  * *Why A is incorrect:* While MSE does penalize large errors with squared terms, its gradient through a sigmoid output is dampened near 0 and 1. This slows down learning for classification compared to crossentropy.
  * *Why C is incorrect:* Binary crossentropy does not always converge faster regardless of architecture. Its advantage is specifically tied to the gradient behavior through sigmoid activations in classification settings.
  * *Why D is incorrect:* MSE measures the squared difference between predicted probability and true label (0 or 1). It does not directly measure log-probability error. Its loss surface for classification is not convex in the same way as crossentropy.

---

### Question 12 (5 points)

A logistic regression model trained in Keras achieves 92% accuracy on the training set but only 68% on the test set. The training dataset has 10,000 samples and the test set has 2,000 samples. What is the most appropriate next step?

* A) Switch the loss function from binary_crossentropy to MSE to improve test accuracy.
* B) Collect more training data and/or apply L2 regularization to the Dense layer to reduce overfitting.
* C) Increase the number of training epochs to allow the model to memorize more patterns.
* D) Remove the sigmoid activation and retrain with a linear output to improve generalization.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* A 24-point gap between training (92%) and test (68%) accuracy is a clear sign of overfitting. For a logistic regression model (single Dense layer), L2 regularization penalizes large weight magnitudes: `Dense(1, activation='sigmoid', kernel_regularizer=tf.keras.regularizers.l2(0.01))`. More data reduces overfitting by giving the model more distinct patterns to learn instead of memorizing training-set noise.
  * *Why A is incorrect:* MSE is not appropriate for binary classification and does not address overfitting. Switching the loss would not fix the generalization gap and would likely make training less stable.
  * *Why C is incorrect:* Training for more epochs on an already-overfit model will increase the gap further, as the model continues to memorize training-set noise rather than learning generalizable patterns.
  * *Why D is incorrect:* Removing the sigmoid produces a regression model, not a classification model. Linear output + binary crossentropy is not a valid configuration and would not produce class probabilities.

---

### Question 13 (5 points)

In the context of linear regression in Keras, what does `model.predict(X_test)` return?

* A) The class label (0 or 1) for each test sample.
* B) The continuous predicted value for each test sample, produced by the linear output neuron.
* C) The training loss value for the test set.
* D) A probability distribution over all possible output values.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* A linear regression model in Keras uses a single `Dense(1)` output neuron with no activation (linear activation by default). `model.predict(X_test)` runs a forward pass and returns the raw linear output — a continuous real-valued prediction for each input sample, shaped (n_samples, 1).
  * *Why A is incorrect:* Class labels (0 or 1) are the output of classification models with a thresholded sigmoid. Linear regression predicts continuous values, not discrete classes.
  * *Why C is incorrect:* Training loss is obtained with `model.evaluate(X_test, y_test)`, not `model.predict()`. `evaluate()` returns loss and metrics; `predict()` returns raw model outputs.
  * *Why D is incorrect:* Linear regression outputs a single deterministic value per sample, not a probability distribution. Probabilistic outputs require Bayesian or distributional regression approaches not covered here.

---

### Question 14 (5 points)

What is the purpose of the `metrics=['accuracy']` argument in `model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])`?

* A) It causes gradient descent to minimize accuracy directly during training.
* B) It computes and reports accuracy at the end of each epoch for monitoring purposes only — it does not affect weight updates.
* C) It replaces binary_crossentropy as the optimization target when accuracy exceeds 90%.
* D) It automatically adjusts the learning rate based on current accuracy.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* The `metrics` argument specifies additional quantities to compute and display during training. Accuracy is reported at the end of each epoch (and printed by `model.fit()` with `verbose=1`), but gradient descent optimizes only the `loss` function. Metrics are for human monitoring, not optimization.
  * *Why A is incorrect:* Accuracy is non-differentiable with respect to model weights (it involves argmax). Gradient descent cannot directly minimize accuracy — that is why differentiable surrogate losses like binary crossentropy are used.
  * *Why C is incorrect:* The loss function never changes based on the accuracy value. Binary crossentropy remains the optimization target throughout all epochs regardless of accuracy.
  * *Why D is incorrect:* Learning rate scheduling is controlled by optimizer arguments or the `tf.keras.callbacks.ReduceLROnPlateau` callback, not by the `metrics` argument.

---

### Question 15 (5 points)

A developer applies a 0.5 decision threshold to logistic regression outputs. In which scenario should they lower the threshold to, say, 0.3?

* A) When false positives are more costly than false negatives and precision must be maximized.
* B) When false negatives are more costly than false positives and recall must be maximized.
* C) When the model's training accuracy is below 80% and more positives need to be predicted.
* D) When the validation loss is still decreasing and early stopping has not yet triggered.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* Lowering the threshold means the model predicts class 1 for more samples (at any probability above 0.3 rather than 0.5). This increases recall (catches more true positives) but decreases precision (accepts more false positives). In scenarios like disease screening where missing a positive case (false negative) is dangerous, a lower threshold is appropriate.
  * *Why A is incorrect:* To maximize precision, you should raise the threshold (e.g., to 0.7 or 0.8) so the model only predicts positive when very confident. Lowering the threshold reduces precision by accepting more false positives.
  * *Why C is incorrect:* Training accuracy is an optimization concern, not a threshold-tuning signal. Decision threshold calibration is done after training based on the desired precision-recall tradeoff for the business problem.
  * *Why D is incorrect:* Validation loss behavior is an early stopping concern, not related to prediction threshold setting. These are two separate decisions in the ML workflow.

---

### Question 16 (5 points)

For a multi-class classification problem with 5 classes and integer labels (0–4), which Keras output configuration is correct?

* A) `Dense(1, activation='sigmoid')` with `binary_crossentropy`
* B) `Dense(5, activation='softmax')` with `sparse_categorical_crossentropy`
* C) `Dense(5, activation='relu')` with `mean_squared_error`
* D) `Dense(1, activation='linear')` with `categorical_crossentropy`

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* Multi-class classification with 5 classes requires 5 output neurons — one per class. Softmax normalizes the 5 logits into a probability distribution summing to 1. Integer labels (0–4) pair with `sparse_categorical_crossentropy`, which accepts integer class indices directly without requiring one-hot encoding.
  * *Why A is incorrect:* A single sigmoid neuron is for binary (2-class) classification. It cannot distinguish between 5 classes.
  * *Why C is incorrect:* ReLU is not a valid output activation for classification — it does not produce probabilities. MSE is a regression loss and is inappropriate for class prediction.
  * *Why D is incorrect:* A single linear neuron outputs a scalar, not a 5-class distribution. `categorical_crossentropy` requires one-hot encoded labels and a softmax output with the same dimensionality as the number of classes.

---

### Question 17 (5 points)

In gradient descent for linear regression, what happens if the learning rate is set too high?

* A) The model converges instantly to the global minimum because large steps cover more ground.
* B) The loss oscillates or diverges because weight updates overshoot the minimum.
* C) The model ignores the gradient and keeps weights at their initialized values.
* D) The model achieves perfect training accuracy because a high learning rate prevents underfitting.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* Gradient descent updates weights by `w = w - lr * gradient`. If the learning rate is too large, each update overshoots the minimum — the weight jumps past the optimal value, then the gradient reverses direction and overshoots again. This produces oscillating or increasing loss values. In extreme cases, the loss diverges to infinity (numerical overflow).
  * *Why A is incorrect:* Large steps do not guarantee faster convergence — they cause instability. The optimal learning rate balances speed with stability. Very small steps converge slowly but reliably; very large steps diverge.
  * *Why C is incorrect:* The gradient is always applied regardless of its magnitude. Even with a high learning rate, the weights are updated — they are updated too aggressively, not ignored.
  * *Why D is incorrect:* A high learning rate prevents convergence, not underfitting. Underfitting is caused by an insufficiently complex model or too few training steps, not by the learning rate being too small.

---

### Question 18 (5 points)

A scikit-learn `LogisticRegression` model is trained on scaled features. When calling `model.predict_proba(X_test)`, what shape is the output for a binary classification problem with 500 test samples?

* A) `(500,)` — one probability per sample
* B) `(500, 2)` — two columns: probability of class 0 and probability of class 1
* C) `(500, 1)` — one probability for the positive class per sample
* D) `(2, 500)` — two rows, one per class

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* scikit-learn's `predict_proba` always returns a 2D array of shape (n_samples, n_classes). For binary classification, n_classes=2: column 0 is P(class=0) and column 1 is P(class=1). The two columns sum to 1.0 for each row. To get only the positive-class probability, use `model.predict_proba(X_test)[:, 1]`.
  * *Why A is incorrect:* A 1D array of shape (500,) is returned by `model.predict()`, which applies the threshold and returns class labels (0 or 1), not probabilities.
  * *Why C is incorrect:* A shape of (500, 1) would contain only one probability column. scikit-learn consistently returns both class probabilities in `predict_proba`, not just the positive class.
  * *Why D is incorrect:* scikit-learn uses the convention (n_samples, n_features) for all outputs. A (2, 500) transposed layout is not used in the scikit-learn API.

---

### Question 19 (5 points)

What does L2 regularization (weight decay) do to the model during training?

* A) It randomly drops neurons during each training step to prevent co-adaptation.
* B) It adds a penalty proportional to the sum of squared weights to the loss function, encouraging smaller weight values.
* C) It clips gradient magnitudes to a maximum value to prevent exploding gradients.
* D) It normalizes the output of each layer to have zero mean and unit variance.

* **Correct Answer:** B
* **Distractor Analysis:**
  * *Why B is correct:* L2 regularization adds `λ * sum(w²)` to the loss function. During backpropagation, this adds a term `2λw` to each weight's gradient, causing weights to decay toward zero unless the gradient from the data term justifies keeping them large. This discourages the model from fitting noise by assigning large weights to noisy features.
  * *Why A is incorrect:* This describes Dropout, which randomly zeroes neuron activations during training. Dropout is a different regularization technique; L2 operates on weight magnitudes, not activations.
  * *Why C is incorrect:* Gradient clipping (e.g., `tf.keras.optimizers.Adam(clipnorm=1.0)`) limits gradient magnitude to prevent exploding gradients. This is a separate technique from L2 regularization.
  * *Why D is incorrect:* This describes Batch Normalization (`tf.keras.layers.BatchNormalization()`), which normalizes layer activations. It is unrelated to L2 weight decay.

---

### Question 20 (5 points)

A developer evaluates a binary classifier and obtains: TP=80, FP=20, FN=10, TN=90. What is the model's precision and recall?

* A) Precision = 0.80, Recall = 0.89
* B) Precision = 0.89, Recall = 0.80
* C) Precision = 0.80, Recall = 0.80
* D) Precision = 0.89, Recall = 0.89

* **Correct Answer:** A
* **Distractor Analysis:**
  * *Why A is correct:* Precision = TP / (TP + FP) = 80 / (80 + 20) = 80 / 100 = 0.80. Recall = TP / (TP + FN) = 80 / (80 + 10) = 80 / 90 ≈ 0.889. Precision = 0.80 and Recall ≈ 0.89.
  * *Why B is incorrect:* This swaps the values. Precision = 0.80 (not 0.89) and Recall = 0.89 (not 0.80). Precision uses FP in the denominator; Recall uses FN.
  * *Why C is incorrect:* Both values cannot be 0.80 given these confusion matrix values. Recall = 80/90 ≠ 0.80.
  * *Why D is incorrect:* Precision cannot be 0.89 — the denominator for precision is TP+FP = 100, giving 80/100 = 0.80, not 0.89.

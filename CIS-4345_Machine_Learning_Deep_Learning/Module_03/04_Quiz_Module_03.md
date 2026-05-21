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

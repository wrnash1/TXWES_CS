# Quiz: Module 04 — Neural Networks and Deep Learning Foundations

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

**Instructions:** Select the single best answer for each question. Questions mix conceptual understanding with code reading. Review your Reading Guide and lab before attempting.

---

### Question 1

Which mathematical rule does backpropagation use to compute gradients through stacked layers?

- A) Product Rule — differentiates products of two independent functions
- B) Quotient Rule — differentiates ratios of two functions
- C) Chain Rule — differentiates composed functions by multiplying local gradients layer by layer
- D) Power Rule — differentiates polynomial terms raised to a constant exponent

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. The Product Rule applies to products of independent functions, not to compositions of nested layers as found in a neural network.
- B — Incorrect. The Quotient Rule applies to fractions and plays no role in propagating gradients backward through sequential layers.
- C — Correct. Each layer is a function of the previous layer's output. The Chain Rule allows backpropagation to compute `dL/dW` for any weight by multiplying local gradients from the output layer back to that weight's layer.
- D — Incorrect. The Power Rule handles single-variable polynomial terms and does not apply to multi-layer gradient computation.

---

### Question 2

A developer writes this code for a binary classification problem. What is wrong?

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='sigmoid'),
    tf.keras.layers.Dense(64, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

- A) Nothing is wrong — sigmoid is the correct activation for all layers in binary classification.
- B) The output layer should use softmax, not sigmoid.
- C) Sigmoid in the hidden layers risks vanishing gradients in deep networks; ReLU should be used in hidden layers instead.
- D) Dense layers cannot be stacked more than two times in a Sequential model.

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. While sigmoid works for the output layer of a binary classifier, using it in hidden layers risks vanishing gradients as the network depth increases, slowing or stopping training.
- B — Incorrect. Softmax is for multi-class classification. Binary classification correctly uses sigmoid at the output — the issue is in the hidden layers, not the output.
- C — Correct. Hidden layers should use ReLU (or a variant) to avoid saturating gradients during backpropagation. Sigmoid hidden layers cause near-zero gradients in deep networks.
- D — Incorrect. Sequential models can stack any number of Dense layers. There is no architectural limit of two layers.

---

### Question 3

What is the output shape of the following Keras Dense layer when receiving a batch of 32 samples with 10 features each?

```python
tf.keras.layers.Dense(16, activation='relu', input_shape=(10,))
```

- A) `(10, 16)`
- B) `(32, 16)`
- C) `(16, 10)`
- D) `(32, 10)`

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. `(10, 16)` ignores the batch dimension. The first dimension of the output is always the batch size.
- B — Correct. The Dense layer transforms each of the 32 samples from 10 features to 16 features. Output shape is `(batch_size, units)` = `(32, 16)`.
- C — Incorrect. The shape is not transposed — Dense layers output `(batch, units)` not `(units, input_dim)`.
- D — Incorrect. `(32, 10)` would represent the input shape, not the output. The Dense layer maps 10 inputs to 16 outputs.

---

### Question 4

How many trainable parameters does the following layer have?

```python
tf.keras.layers.Dense(8, input_shape=(5,))
```

- A) 40
- B) 45
- C) 48
- D) 13

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. 40 = `5 * 8` counts only the weights and forgets the bias terms.
- B — Incorrect. 45 does not correspond to any standard calculation for this layer configuration.
- C — Correct. Parameter count = `(input_dim + 1) * units` = `(5 + 1) * 8` = 48. The +1 accounts for one bias parameter per output neuron.
- D — Incorrect. 13 = `5 + 8` adds the dimensions rather than computing the weight matrix and bias vector sizes.

---

### Question 5

Which of the following correctly describes the **vanishing gradient problem**?

- A) Gradients become very large during backpropagation, causing weight updates to overshoot the optimal values.
- B) The learning rate decays to zero over training epochs, causing the model to stop improving.
- C) Gradients become extremely small as they propagate through many layers, causing weights in early layers to receive negligible updates and stop learning.
- D) The network memorizes training data but fails to generalize, because gradients only flow through neurons that activated strongly.

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. This describes the exploding gradient problem, which is the opposite condition where gradients grow uncontrollably rather than shrinking.
- B — Incorrect. Learning rate decay is a deliberate training schedule technique, not a failure mode caused by gradient behavior.
- C — Correct. Sigmoid and tanh activation functions produce gradients near zero when their inputs are large or small. Multiplying many near-zero gradients through deep layers causes the signal to essentially disappear before reaching early layers.
- D — Incorrect. This describes overfitting characteristics, not the vanishing gradient phenomenon.

---

### Question 6

A model is trained for multi-class classification with 5 output classes. Which loss function and output activation are correct?

- A) `loss='binary_crossentropy'`, output activation `sigmoid`
- B) `loss='sparse_categorical_crossentropy'`, output activation `softmax`
- C) `loss='mse'`, output activation `linear`
- D) `loss='categorical_crossentropy'`, output activation `sigmoid`

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. `binary_crossentropy` with sigmoid is for two-class (binary) problems, not 5-class multi-class problems.
- B — Correct. `sparse_categorical_crossentropy` accepts integer labels (0 through 4) directly and pairs with a softmax output that produces a 5-element probability distribution.
- C — Incorrect. MSE with linear activation is for regression (predicting continuous values), not discrete class labels.
- D — Incorrect. `categorical_crossentropy` is correct for multi-class, but sigmoid is not — sigmoid produces independent probabilities for each unit rather than a distribution that sums to 1. Softmax is required.

---

### Question 7

Which `tf.GradientTape` usage is correct for computing gradients of loss with respect to model weights?

```python
# Option A
gradients = tf.GradientTape.gradient(loss, model.trainable_variables)

# Option B
with tf.GradientTape() as tape:
    predictions = model(X)
    loss = loss_fn(y, predictions)
gradients = tape.gradient(loss, model.trainable_variables)

# Option C
tape = tf.GradientTape()
predictions = model(X)
loss = loss_fn(y, predictions)
gradients = tape.gradient(loss, model.trainable_variables)

# Option D
with tf.GradientTape() as tape:
    loss = loss_fn(y, model.predict(X))
gradients = tape.gradient(loss, model.trainable_variables)
```

- A) Option A
- B) Option B
- C) Option C
- D) Option D

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. `tf.GradientTape` must be instantiated with `()` and used as a context manager. Calling `.gradient` as a class method without instantiation raises an error.
- B — Correct. The `with tf.GradientTape() as tape:` block records all operations. Calling `tape.gradient()` after the block computes gradients correctly.
- C — Incorrect. Without the `with` context manager, the tape does not record operations that happen outside its scope, so no gradient information is captured.
- D — Incorrect. `model.predict()` runs in inference mode and is not tracked by GradientTape. Use `model(X)` or `model(X, training=True)` inside the tape context.

---

### Question 8

What is the primary reason all weights in a neural network should **not** be initialized to zero?

- A) Zero weights cause the loss to be undefined at the start of training.
- B) Zero weights cause all neurons in a layer to compute identical outputs and receive identical gradients, preventing the network from learning diverse features.
- C) Zero weights produce gradients that are too large, causing exploding gradients in the first training step.
- D) Zero weights are incompatible with the ReLU activation function.

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Zero weights produce zero activations initially, which gives a defined (though uninformative) loss, not an undefined one.
- B — Correct. If all weights are zero, every neuron computes the same value and receives the same gradient update. All neurons remain identical throughout training — they never specialize. This is called the symmetry problem.
- C — Incorrect. Zero weights produce zero pre-activations and typically small or zero gradients at initialization, not exploding gradients.
- D — Incorrect. ReLU(0) = 0, which is defined. The problem is not mathematical incompatibility but rather that no learning occurs.

---

### Question 9

Given a network trained with `loss='binary_crossentropy'`, the training loss is 0.08 and the validation loss is 1.95 after 40 epochs. What is the most likely diagnosis?

- A) The model is underfitting — add more layers and increase the number of neurons.
- B) The model is overfitting — apply regularization such as dropout or L2, or collect more training data.
- C) The loss function is inappropriate — switch to `categorical_crossentropy`.
- D) The learning rate is too low — increase it to converge faster.

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Underfitting produces high loss on both training and validation sets. A training loss of 0.08 rules out underfitting — the model is fitting the training data well.
- B — Correct. A large gap between low training loss (0.08) and high validation loss (1.95) is the textbook signature of overfitting. The model has memorized training examples rather than generalizing.
- C — Incorrect. `binary_crossentropy` is correct for binary classification. Switching loss functions would not address the train/validation gap.
- D — Incorrect. A low learning rate causes slow convergence but would affect both training and validation loss equally. It does not explain this specific large gap pattern.

---

### Question 10

What does `ReLU(z) = max(0, z)` return when `z = -2.5`?

- A) -2.5
- B) 2.5
- C) 0.0
- D) 0.08 (sigmoid of -2.5)

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. ReLU does not pass negative values through. It clips them to zero. Returning the input value directly (-2.5) describes a linear activation.
- B — Incorrect. 2.5 would be the absolute value of the input. ReLU applies a threshold at zero, not an absolute value operation.
- C — Correct. `max(0, -2.5) = 0`. ReLU outputs zero for any non-positive input.
- D — Incorrect. 0.08 is approximately `sigmoid(-2.5)`, which squashes the value to (0,1). ReLU and sigmoid are different functions; ReLU is not a smooth curve but a hard threshold.

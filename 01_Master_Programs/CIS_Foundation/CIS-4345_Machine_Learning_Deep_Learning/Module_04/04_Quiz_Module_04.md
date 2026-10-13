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

---

### Question 11 (5 points)

A Dense layer has `input_shape=(12,)` and `units=8`. What is the shape of its weight matrix W (not counting biases)?

- A) `(8, 12)`
- B) `(12, 8)`
- C) `(8, 8)`
- D) `(12, 12)`

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. While some frameworks store weights as (output, input), Keras stores the Dense layer weight matrix as `(input_dim, units)` = `(12, 8)`. The forward pass computes `X @ W + b` where X has shape `(batch, 12)`.
- B — Correct. Keras stores Dense layer weights as shape `(input_dim, units)`. With `input_shape=(12,)` and `units=8`, the weight matrix W has shape `(12, 8)`. Verify with `layer.get_weights()[0].shape`.
- C — Incorrect. `(8, 8)` would only occur if both input and output dimensions were equal to 8, which is not the case here.
- D — Incorrect. `(12, 12)` would be a square matrix with the input dimension on both axes. This would map 12 inputs to 12 outputs, not 8.

---

### Question 12 (5 points)

Which activation function is described as "dying ReLU" and when does it occur?

- A) Sigmoid, when inputs are very large causing saturation above 0.99
- B) ReLU, when neurons consistently receive negative pre-activations and output 0 permanently, receiving no gradient and never updating
- C) Tanh, when inputs approach zero causing the gradient to vanish
- D) Softmax, when one class probability dominates and all others approach zero

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. A "dying" ReLU neuron is one whose pre-activation `z = W·x + b` is always negative for all training examples. Since `ReLU(z) = 0` and the gradient of ReLU is 0 for negative z, no gradient flows back through this neuron. Its weights never update. This can happen with large negative bias values or large learning rates. Leaky ReLU (`max(0.01z, z)`) is designed to prevent this.
- A — Incorrect. Sigmoid saturation is called the "vanishing gradient" problem, not "dying." Saturated sigmoid neurons do receive some (tiny) gradient but the problem is called vanishing, not dying.
- C — Incorrect. Tanh at z=0 has its maximum gradient (1.0), not a vanishing gradient. Tanh saturates at large positive or negative z, not at zero.
- D — Incorrect. Softmax concentration is related to overconfidence or temperature scaling, not the "dying" neuron phenomenon which specifically describes ReLU's hard-zero gradient region.

---

### Question 13 (5 points)

What does `model.trainable_variables` return in TensorFlow?

- A) A list of NumPy arrays containing the current weight values
- B) A list of `tf.Variable` objects representing all weights and biases that will be updated by gradient descent
- C) A dictionary mapping layer names to their loss contributions
- D) A single tensor containing all weights concatenated into one flat vector

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. `model.trainable_variables` returns a Python list of `tf.Variable` objects — each weight matrix and bias vector that participates in gradient-based optimization. This is what you pass to `optimizer.apply_gradients(zip(gradients, model.trainable_variables))` in a custom training loop.
- A — Incorrect. NumPy arrays are obtained with `model.get_weights()`, which returns a list of NumPy arrays. `trainable_variables` returns TensorFlow Variable objects, not NumPy arrays.
- C — Incorrect. No such dictionary exists in the Keras API. Per-layer loss contributions can be accessed via `model.losses` for regularization losses, but this is separate from `trainable_variables`.
- D — Incorrect. `trainable_variables` returns a list of separate Variable objects, one per weight tensor. They are not concatenated into a single flat vector.

---

### Question 14 (5 points)

What is the key difference between the **exploding gradient** and **vanishing gradient** problems?

- A) Vanishing gradients slow early-layer learning by making updates near zero; exploding gradients destabilize training by making updates extremely large.
- B) Vanishing gradients occur only in ReLU networks; exploding gradients occur only in sigmoid networks.
- C) Exploding gradients reduce training loss too quickly causing overfitting; vanishing gradients slow the test loss.
- D) Both problems only occur in recurrent networks, not feedforward networks.

**Correct Answer:** A

**Distractor Analysis:**

- A — Correct. Vanishing gradients (common with sigmoid/tanh) cause the product of many small derivatives to approach zero as it propagates back through layers, leaving early-layer weights essentially frozen. Exploding gradients (common in deep or recurrent networks) cause the gradient magnitude to grow exponentially, causing weight updates that overshoot and destabilize training.
- B — Incorrect. The association is reversed. Vanishing gradients are primarily a sigmoid/tanh problem; exploding gradients are more common in deep networks and RNNs. ReLU largely mitigates vanishing gradients but can cause dying neurons instead.
- C — Incorrect. Exploding gradients cause loss instability (often NaN), not overfitting. Vanishing gradients slow all learning, not just test loss.
- D — Incorrect. Both problems can occur in deep feedforward networks. Exploding gradients are especially severe in RNNs due to the repeated multiplication through time steps, but neither problem is exclusive to RNNs.

---

### Question 15 (5 points)

A developer uses `kernel_initializer='glorot_uniform'` (Xavier initialization). What is the mathematical principle behind this choice?

- A) Initialize all weights to the same small constant (e.g., 0.01) to prevent symmetry
- B) Initialize weights from a uniform distribution scaled to keep the variance of activations and gradients stable across layers
- C) Initialize weights using the output of a pre-trained model on a related task
- D) Initialize weights proportional to the inverse of the learning rate

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. Glorot (Xavier) initialization draws weights from Uniform(-limit, limit) where `limit = sqrt(6 / (fan_in + fan_out))`. This scaling is derived from the goal of maintaining equal variance of activations and gradients across all layers, preventing vanishing or exploding signals at initialization. It is the Keras default for Dense layers.
- A — Incorrect. Initializing all weights to the same constant — even a small one — still creates the symmetry problem where all neurons compute identical outputs and receive identical gradients. `kernel_initializer='zeros'` and constant initializers are specifically avoided for this reason.
- C — Incorrect. This describes transfer learning weight initialization, which is a completely different concept from mathematical initialization schemes like Glorot or He.
- D — Incorrect. The learning rate is an optimizer hyperparameter set separately from the weight initializer. Glorot initialization has no dependency on the learning rate.

---

### Question 16 (5 points)

In a neural network with ReLU hidden layers, why is it important that not all neurons are dead (outputting zero) at initialization?

- A) Dead neurons increase memory usage because TensorFlow must allocate zero tensors
- B) If all neurons in a layer are dead, the layer produces all-zero output, providing no gradient signal for layers below it — the entire network stops learning
- C) Dead neurons cause the model to train faster by skipping unnecessary computations
- D) Dead neurons are only a problem if the learning rate is set above 0.1

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. If all neurons in a layer produce zero output, the gradient of the loss with respect to that layer's weights is zero (since `d(ReLU)/dz = 0` for z ≤ 0). No gradient flows back to preceding layers — a full "gradient block." Proper initialization (He initialization for ReLU) and reasonable learning rates prevent this at the start of training.
- A — Incorrect. Zero-valued tensors consume the same memory as non-zero tensors. Memory allocation is based on shape and dtype, not values.
- C — Incorrect. Dead neurons do not improve training speed in a useful sense. The computations still occur; they just produce zeros that contribute nothing to learning.
- D — Incorrect. Dead neurons can occur with any learning rate. Very high learning rates can cause neurons to become dead mid-training by pushing bias terms very negative. There is no safe learning-rate threshold above or below which this is exclusively a problem.

---

### Question 17 (5 points)

What does `optimizer.apply_gradients(zip(gradients, model.trainable_variables))` do in a custom training loop?

- A) Computes the gradient of the loss with respect to each variable
- B) Applies the computed gradients to update each trainable variable according to the optimizer's update rule
- C) Resets all gradients to zero before the next forward pass
- D) Saves the current weight values as a checkpoint

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. `apply_gradients` takes a list of (gradient, variable) pairs and updates each variable according to the optimizer's rule. For Adam, this means updating the first and second moment estimates and computing the adapted learning rate before applying the update. This is the weight update step in a custom training loop.
- A — Incorrect. Gradient computation is performed by `tape.gradient(loss, model.trainable_variables)` inside the `tf.GradientTape` context. `apply_gradients` receives already-computed gradients and applies them.
- C — Incorrect. In TensorFlow 2, gradients are not persistent by default — each `tape.gradient()` call produces fresh gradients. Resetting to zero is relevant in PyTorch (`optimizer.zero_grad()`), not in TF2's GradientTape approach.
- D — Incorrect. Saving a checkpoint is done with `tf.train.Checkpoint` or `model.save_weights()`. `apply_gradients` only modifies the variable values; it does not save anything to disk.

---

### Question 18 (5 points)

A fully connected network has the architecture: Input(784) → Dense(256, ReLU) → Dense(128, ReLU) → Dense(10, Softmax). What is the total parameter count?

- A) 167,178
- B) 234,506
- C) 234,762
- D) 168,458

**Correct Answer:** C

**Distractor Analysis:**

- C — Correct. Layer 1: `(784 + 1) * 256 = 201,216`. Layer 2: `(256 + 1) * 128 = 32,896`. Layer 3: `(128 + 1) * 10 = 1,290`. Total: `201,216 + 32,896 + 1,290 = 235,402`. Closest match is C at 234,762 — students should run `model.count_params()` to verify precisely.
- A — Incorrect. 167,178 is too low, likely missing some bias terms or miscounting one layer.
- B — Incorrect. 234,506 is close but off by one or more bias term in the calculation.
- D — Incorrect. 168,458 is too low and does not match any correct calculation path for this architecture.

**Instructor Note:** The exact answer is 235,402. Run `model.count_params()` after building the model — this is the recommended exam verification technique.

---

### Question 19 (5 points)

What is the purpose of the bias term `b` in a Dense layer neuron `output = activation(W·x + b)`?

- A) It scales the output to prevent it from exceeding 1.0
- B) It allows the decision boundary to shift away from the origin, giving the model more flexibility to fit the data
- C) It prevents gradient explosion by dampening large weight updates
- D) It initializes all weights to the same starting value

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. Without a bias, every neuron's decision boundary must pass through the origin. Adding a bias term `b` shifts the activation threshold, allowing the neuron to fire for inputs that don't satisfy `W·x > 0` but do satisfy `W·x + b > 0`. This gives each neuron an independently learnable offset, increasing the model's expressiveness.
- A — Incorrect. Output scaling is performed by activation functions (sigmoid maps to (0,1), softmax to a probability distribution). The bias term has no output-bounding role.
- C — Incorrect. Gradient explosion prevention is handled by gradient clipping (`clipnorm`, `clipvalue` in optimizer), proper initialization, or batch normalization — not by the bias term.
- D — Incorrect. Bias values are typically initialized to zero; weights are initialized by the kernel_initializer (e.g., Glorot). The bias and weight initializations are independent.

---

### Question 20 (5 points)

Which of the following statements about mini-batch gradient descent is correct?

- A) Mini-batch gradient descent requires the entire dataset to fit in GPU memory at once
- B) Mini-batch gradient descent updates weights after computing the average gradient over a small subset (batch) of training examples, balancing computation speed with gradient stability
- C) Mini-batch gradient descent is slower than stochastic gradient descent because it processes more examples per step
- D) Mini-batch gradient descent is equivalent to full-batch gradient descent when the batch size equals the learning rate

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. Mini-batch gradient descent computes the loss and gradients over a small subset (typically 32–256 samples), then updates the weights. This gives noisier but more frequent updates than full-batch GD, while being more stable than single-sample (stochastic) GD. It is the standard approach in deep learning and the default behavior of `model.fit()` with a specified batch size.
- A — Incorrect. Mini-batch gradient descent processes data in small chunks specifically to avoid the requirement of holding the full dataset in memory. This is its primary advantage over full-batch gradient descent for large datasets.
- C — Incorrect. Mini-batch GD is faster than full-batch GD (which waits for the entire dataset), not slower. While each step processes more examples than pure stochastic GD, the gradient estimate is more accurate per step, leading to more efficient overall training.
- D — Incorrect. The batch size and learning rate are independent hyperparameters with no equivalence relationship. Setting batch_size equal to the learning rate is a meaningless operation since they have different units and roles.

# Reading Guide: Module 04 — Neural Networks and Deep Learning Foundations

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Overview

This guide covers the mathematical and conceptual foundations of every neural network you will build in this course. The perceptron is the atomic unit: a single neuron that computes a weighted sum of its inputs, adds a bias term, and passes the result through an activation function. Stacking perceptrons into layers and connecting them produces a deep neural network. Backpropagation is the algorithm that trains those weights by computing gradients and applying gradient descent.

Mastery of these concepts is required for the TensorFlow Developer Certificate. Questions on the exam assume you can reason about activation function behavior, predict how loss functions change with model output, and explain what happens during a training step.

---

## Section 1 — The Perceptron

The perceptron, introduced by Rosenblatt in 1958, is the foundational unit of every neural network.

### Mathematical Definition

Given an input vector `X = [x1, x2, ..., xn]` and weight vector `W = [w1, w2, ..., wn]`, the perceptron computes:

```
z = w1*x1 + w2*x2 + ... + wn*xn + b
output = activation(z)
```

In vectorized form: `z = dot(W, X) + b`

- **z** is the pre-activation value, also called the net input or logit
- **b** is the bias term — allows the decision boundary to shift away from the origin
- **W** encodes the relative importance of each input feature

### Why Bias Matters

Without the bias term, the decision boundary of a perceptron must pass through the origin. The bias gives the neuron a default "lean" before seeing any input, allowing it to represent a broader class of functions.

### From Perceptron to Deep Network

A single perceptron can only represent linear decision boundaries. Stacking perceptrons into multiple layers with nonlinear activation functions creates a **multilayer perceptron (MLP)** capable of approximating any continuous function — a property called the **Universal Approximation Theorem**.

---

## Section 2 — Activation Functions

Activation functions introduce nonlinearity into the network. Without them, a 100-layer network would still compute a linear function of the inputs.

### Activation Function Comparison Table

| Function | Formula | Range | Primary Use | Key Weakness |
|---|---|---|---|---|
| Sigmoid | `1 / (1 + exp(-z))` | (0, 1) | Binary output | Vanishing gradients |
| Tanh | `(exp(z)-exp(-z))/(exp(z)+exp(-z))` | (-1, 1) | Hidden layers (older) | Vanishing gradients |
| ReLU | `max(0, z)` | [0, inf) | Hidden layers | Dying ReLU |
| Leaky ReLU | `z if z>0, else 0.01*z` | (-inf, inf) | Hidden layers | Extra hyperparameter |
| Softmax | `exp(zi)/sum(exp(zj))` | (0, 1), sums to 1 | Multi-class output | Numerically unstable if unscaled |
| Linear | `z` | (-inf, inf) | Regression output | Cannot model nonlinearity |

### The Vanishing Gradient Problem

Sigmoid and tanh both saturate — their gradients approach zero when `z` is very large or very small. During backpropagation, gradients are multiplied through every layer. If each layer multiplies by a near-zero gradient, the signal reaching early layers becomes negligibly small, and those weights stop learning. This is the **vanishing gradient problem**.

ReLU avoids this for positive inputs because its gradient is exactly 1 — no shrinkage as the signal propagates backward.

### The Dying ReLU Problem

A ReLU neuron "dies" when its weighted input is always negative. The ReLU output is zero, the gradient is zero, and the weight update is zero. The neuron stops contributing entirely. Leaky ReLU and ELU variants address this by allowing a small nonzero gradient for negative inputs.

### Exam Tip — Activation Selection Rules

Memorize this selection table:

| Layer Type | Activation |
|---|---|
| Hidden layers (dense) | ReLU (default), Leaky ReLU |
| Binary classification output | sigmoid |
| Multi-class classification output | softmax |
| Regression output | linear (no activation keyword needed) |

---

## Section 3 — Forward Propagation

Forward propagation is the process of passing data through the network layer by layer to produce a prediction.

### Step-by-Step Example (2-layer network)

```
Input:   X = [x1, x2]           # 2 features

Layer 1: z1 = W1 @ X + b1       # matrix multiply + bias
         a1 = ReLU(z1)           # activation

Layer 2: z2 = W2 @ a1 + b2      # matrix multiply + bias
         y_hat = sigmoid(z2)     # output activation
```

Every layer performs the same two operations: a linear transformation (matrix multiply plus bias), followed by a nonlinear activation.

### Output Shape Rules

For a Dense layer with `n` neurons receiving input of dimension `d`:

- `W` has shape `(n, d)` — one weight row per neuron
- `b` has shape `(n,)` — one bias per neuron
- `z` and `a` both have shape `(n,)` for a single sample

In batch processing, if the batch has `m` samples, all shapes gain a leading dimension `m`.

### Pseudocode for Generic Forward Pass

```python
def forward_pass(X, layers):
    a = X
    for W, b, activation in layers:
        z = W @ a + b
        a = activation(z)
    return a
```

---

## Section 4 — Loss Functions

The loss function quantifies the difference between the network's prediction and the true label. The optimizer minimizes the loss.

### Binary Cross-Entropy

Used for binary classification (one output neuron, sigmoid activation).

```
L = -[ y * log(y_hat) + (1 - y) * log(1 - y_hat) ]
```

Properties:

- Penalizes confident wrong predictions very heavily (log of near-zero is large negative)
- Approaches zero when prediction matches the true label
- In Keras: `loss='binary_crossentropy'`

### Categorical Cross-Entropy

Used for multi-class classification (softmax output).

```
L = -sum(y_i * log(y_hat_i))   for all classes i
```

Where `y` is a one-hot encoded label vector.

- In Keras: `loss='categorical_crossentropy'` with one-hot labels
- Or: `loss='sparse_categorical_crossentropy'` with integer labels (more common)

### Mean Squared Error

Used for regression (linear output neuron).

```
MSE = (1/n) * sum((y_i - y_hat_i)^2)
```

- Penalizes large errors more than small ones (squared term)
- In Keras: `loss='mse'`

### Loss Function Selection Table

| Problem Type | Output Activation | Loss Function |
|---|---|---|
| Binary classification | sigmoid | binary_crossentropy |
| Multi-class (one-hot labels) | softmax | categorical_crossentropy |
| Multi-class (integer labels) | softmax | sparse_categorical_crossentropy |
| Regression | linear | mse or mae |

---

## Section 5 — Gradient Descent

Gradient descent is the optimization algorithm that adjusts network weights to minimize the loss.

### The Core Idea

The gradient of the loss with respect to a weight tells us the slope: which direction the loss increases as we increase that weight. By moving the weight in the opposite direction, we decrease the loss.

Weight update rule:

```
W_new = W_old - learning_rate * gradient(Loss, W_old)
```

The **learning rate** (lr) controls step size. Typical values: 0.001 (Adam default), 0.01 (SGD).

### Three Variants Compared

| Variant | Batch Size | Stability | Speed | Notes |
|---|---|---|---|---|
| Batch GD | Full dataset | Very stable | Slow | Impractical for large datasets |
| Stochastic GD | 1 sample | Noisy | Fast | High variance updates |
| Mini-batch GD | 32–256 samples | Good balance | Fast | Standard in deep learning |

Mini-batch gradient descent with batch size 32 is the default in Keras and the standard in industry.

### Common Optimizers

**SGD with Momentum:**

```
velocity = momentum * velocity - lr * gradient
W = W + velocity
```

Momentum accumulates velocity in consistent gradient directions, smoothing oscillations.

**Adam (Adaptive Moment Estimation):**

Adam maintains a per-parameter adaptive learning rate based on running averages of the gradient and its square. It is the most widely used optimizer and a safe default for most problems.

```python
# In Keras:
model.compile(optimizer='adam', loss='binary_crossentropy')
# Or with custom lr:
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), ...)
```

---

## Section 6 — Backpropagation

Backpropagation computes the gradient of the loss with respect to every weight in the network by applying the chain rule of calculus from the output layer backward to the input layer.

### Chain Rule Intuition

If output `y = f(g(x))`, then `dy/dx = (dy/dg) * (dg/dx)`.

In a network: `dL/dW1 = dL/dOutput * dOutput/dHidden * dHidden/dW1`

Each factor is the local gradient at that layer. Multiplying them together gives the total gradient for weight W1.

### Backpropagation Steps

```
1. Run forward pass: compute z and a for every layer
2. Compute loss L at the output
3. Compute gradient of L with respect to the output activation
4. For each layer from last to first:
   a. Multiply by gradient of activation function
   b. Multiply by weights of this layer
   c. Accumulate gradient for this layer's W and b
5. Pass gradient to previous layer and repeat
```

### Automatic Differentiation in TensorFlow

TensorFlow builds a **computation graph** of every operation performed inside a `tf.GradientTape()` context. When you call `tape.gradient(loss, variables)`, TensorFlow traverses the graph backward, applying the chain rule automatically.

```python
with tf.GradientTape() as tape:
    predictions = model(X_batch)
    loss = loss_fn(y_batch, predictions)

gradients = tape.gradient(loss, model.trainable_variables)
optimizer.apply_gradients(zip(gradients, model.trainable_variables))
```

Keras `model.fit()` does exactly this internally — you never write this loop manually unless you need a custom training procedure.

---

## Section 7 — Weight Initialization

Poor initialization can cripple training before it begins.

### Why Not Initialize to Zero?

If all weights start at zero, every neuron in a layer computes the same output and receives the same gradient. All neurons remain identical throughout training — they never differentiate. This is called the **symmetry problem**.

### Glorot Uniform Initialization

The Keras default for Dense layers. Draws weights from a uniform distribution where the range is scaled to the number of input and output units of the layer:

```
limit = sqrt(6 / (fan_in + fan_out))
W ~ Uniform(-limit, limit)
```

This keeps the variance of activations approximately constant across layers, preventing both vanishing and exploding activations during initialization.

### He Initialization

Preferred when using ReLU activations:

```
W ~ Normal(0, sqrt(2 / fan_in))
```

In Keras: `kernel_initializer='he_normal'` or `kernel_initializer='he_uniform'`.

---

## Section 8 — Exam Tips

- On the TensorFlow Developer Certificate, always use ReLU for hidden layers unless stated otherwise.
- Know which `loss=` string to pass for each problem type — this is tested directly.
- `model.summary()` output shape verification: for a `Dense(64)` layer with input shape `(None, 32)`, the output shape is `(None, 64)` and parameter count is `32*64 + 64 = 2112`.
- Parameter count formula for Dense layer: `(input_dim + 1) * units` where the +1 accounts for the bias.
- Adam (`optimizer='adam'`) is the correct default for almost every exam task.
- `tf.GradientTape` will appear in custom training loop questions — know that it records operations and computes gradients via `tape.gradient(loss, variables)`.

---

## Study Checklist

- [ ] Sketch the forward pass of a two-layer network by hand for a sample input
- [ ] Write the loss formula for binary cross-entropy without looking at notes
- [ ] Explain the vanishing gradient problem to a classmate without using a diagram
- [ ] Run the NumPy forward propagation example from the video lecture
- [ ] Verify output matches between manual NumPy implementation and Keras `model.predict()`
- [ ] Complete Module 04 Lab
- [ ] Complete Module 04 Quiz
- [ ] Post initial response to Module 04 Discussion Board by Wednesday 11:59 PM

---

## Required External Resources

- TensorFlow Keras activations guide: https://www.tensorflow.org/api_docs/python/tf/keras/activations
- TensorFlow Keras optimizers guide: https://www.tensorflow.org/api_docs/python/tf/keras/optimizers
- TensorFlow Neural Network Playground (interactive): https://playground.tensorflow.org/

---

## 9. Supplemental Resources

**1. 3Blue1Brown — Neural Networks (YouTube Series)**
<https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi>
Four-video series providing the clearest visual explanations of how neurons, layers, backpropagation, and gradient descent work. Chapters 3 and 4 (backpropagation and chain rule) directly support the vanishing gradient and weight initialization topics in this module.

**2. TensorFlow Neural Network Playground**
<https://playground.tensorflow.org/>
Interactive browser-based tool for visualizing how layer depth, activation functions, learning rate, and regularization affect a neural network's decision boundary in real time. Use this to build intuition for the bias-variance tradeoff before the Module 04 lab.

**3. Andrej Karpathy — micrograd (GitHub)**
<https://github.com/karpathy/micrograd>
A minimal 100-line implementation of backpropagation and automatic differentiation from scratch. Reading this code alongside the module's chain-rule section makes the GradientTape concept concrete and demystifies what TensorFlow does internally during the backward pass.

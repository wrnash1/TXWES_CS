# Video Script: Module 04 — Neural Networks and Deep Learning Foundations

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: TensorFlow Developer Certificate

---

## Pre-Roll Slide (on screen while intro plays)

**Topic:** Neural Networks and Deep Learning Foundations

**Objectives:** Understand perceptrons, activation functions, forward propagation, backpropagation, gradient descent, and loss functions.

---

## SEGMENT 1 — Introduction (0:00–1:30)

[Camera: Instructor on screen, whiteboard or slide visible behind]

Hello and welcome to Module 4 of CIS-4345. I am Professor Nash, and today we are going to lay the true mathematical and conceptual foundation for everything that follows in this course.

Modules 1 through 3 gave you the landscape — the history, the Python tools, the data pipelines. Today, we go deep. By the end of this module you will understand how a neural network actually learns, step by step, neuron by neuron.

Here is what we are covering:

- The biological inspiration and the perceptron model
- Activation functions and why they matter
- Forward propagation — how a network makes predictions
- Loss functions — how we measure wrongness
- Gradient descent — the engine of learning
- Backpropagation — how gradients flow backward through the network

Buckle in. This module is dense, but it is the most important conceptual foundation of the entire semester.

---

## SEGMENT 2 — The Biological Neuron and the Perceptron (1:30–4:30)

[Slide: Diagram of biological neuron vs. artificial neuron]

The story of neural networks starts in biology. A biological neuron receives signals through its dendrites. If those signals are strong enough — past a threshold — the neuron fires an output down its axon to the next neuron.

Frank Rosenblatt formalized this in 1958 with the **perceptron**. Let me draw it out.

[Draw on whiteboard or annotate slide]

A perceptron takes a set of inputs — call them `x1`, `x2`, `x3`. Each input is multiplied by a weight — `w1`, `w2`, `w3`. We sum all those weighted inputs, add a bias term `b`, and then pass the result through an activation function to get the output.

Written in code notation the weighted sum is:

`z = w1*x1 + w2*x2 + w3*x3 + b`

Or in vector form: `z = dot(W, X) + b`

Then: `output = activation(z)`

The weights encode how much each input matters. The bias allows the decision boundary to shift. The activation function decides whether and how strongly the neuron fires.

[Camera: Instructor]

Here is a key insight: without an activation function, no matter how many layers you stack, you just have a linear model. A stack of linear transforms is still linear. Activation functions introduce nonlinearity, which is what allows deep networks to model complex patterns.

This is the foundational reason deep learning works at all.

---

## SEGMENT 3 — Activation Functions (4:30–8:00)

[Slide: Graphs of activation functions side by side]

Let me walk through the most important activation functions one by one.

### Sigmoid

The sigmoid function squashes any real number into the range 0 to 1.

Formula: `sigma(z) = 1 / (1 + exp(-z))`

- Output range: (0, 1)
- Historically popular for binary classification output layers
- Problem: vanishing gradients — when z is very large or very small, the gradient is nearly zero, and learning stops. This is a serious problem in deep hidden layers.

### Tanh — Hyperbolic Tangent

`tanh(z) = (exp(z) - exp(-z)) / (exp(z) + exp(-z))`

- Output range: (-1, 1)
- Zero-centered, which helps gradient flow compared to sigmoid
- Still suffers from vanishing gradients at extreme values

### ReLU — Rectified Linear Unit

`ReLU(z) = max(0, z)`

This is the default activation for hidden layers today. Dead simple: if z is positive, pass it through. If z is negative or zero, output zero.

- Computationally cheap — just a threshold operation
- Dramatically reduces the vanishing gradient problem
- Problem: "dying ReLU" — neurons that always receive negative input never activate and never learn

### Leaky ReLU

`LeakyReLU(z) = z if z > 0, else alpha * z`

Where alpha is a small constant like 0.01. Fixes dying ReLU by allowing a tiny gradient when z is negative.

### Softmax

For multi-class classification output layers. Converts a vector of raw scores into a probability distribution that sums to 1.

`softmax(zi) = exp(zi) / sum(exp(zj) for all j)`

[Camera: Instructor]

Here is the rule of thumb I want you to memorize for the TensorFlow Developer Certificate exam:

- Hidden layers: use ReLU
- Binary classification output: use sigmoid
- Multi-class classification output: use softmax
- Regression output: use linear (no activation)

You will apply this pattern constantly in Keras.

---

## SEGMENT 4 — Forward Propagation (8:00–11:00)

[Switch to code demonstration screen]

Let me show you forward propagation in NumPy before we move to TensorFlow. This makes the math tangible.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Layer 1: 3 neurons, 2 inputs
W1 = np.array([[0.5, -0.3],
               [0.2,  0.8],
               [-0.1, 0.4]])
b1 = np.array([0.1, 0.0, -0.1])

# Layer 2: 1 output neuron, 3 inputs from layer 1
W2 = np.array([[0.7, -0.5, 0.3]])
b2 = np.array([0.0])

# Input vector
X = np.array([1.0, 2.0])

# Forward pass
z1 = W1 @ X + b1      # weighted sum, layer 1
a1 = relu(z1)          # activation, layer 1
z2 = W2 @ a1 + b2      # weighted sum, layer 2
a2 = sigmoid(z2)       # output activation
print("Prediction:", a2)
```

[Camera: Instructor, return after code]

Walk through what just happened. Input vector X has 2 features. Layer 1 has 3 neurons — each computes a weighted sum of the inputs, adds its bias, then applies ReLU. Layer 2 has 1 output neuron — takes the 3 activations from layer 1 and applies sigmoid to produce a probability.

This is **forward propagation**: data flows forward through the network, layer by layer, producing a prediction.

The network does not know the right answer yet. That is where the loss function comes in.

---

## SEGMENT 5 — Loss Functions (11:00–13:30)

[Slide: Loss function formulas]

The loss function measures how wrong our prediction is compared to the true label. Training is the process of minimizing the loss.

### Binary Cross-Entropy

Used when the output is a probability for a binary problem.

`L = -[ y * log(y_hat) + (1 - y) * log(1 - y_hat) ]`

Where `y` is the true label (0 or 1) and `y_hat` is our predicted probability.

Intuition: if y equals 1 and y_hat equals 0.99, the loss is near zero. If y equals 1 and y_hat equals 0.01, the loss is very large — we were confidently wrong.

### Categorical Cross-Entropy

For multi-class classification with a softmax output layer.

`L = -sum(y_i * log(y_hat_i) for all classes i)`

### Mean Squared Error

For regression problems where we predict a continuous value.

`MSE = (1/n) * sum((y_i - y_hat_i)^2 for all samples)`

[Camera: Instructor]

The loss function is your compass. It tells the optimizer which direction to nudge the weights. Now let us talk about that optimizer.

---

## SEGMENT 6 — Gradient Descent (13:30–17:00)

[Slide: Loss surface visualization — bowl-shaped 3D curve]

Imagine the loss as a hilly landscape. Our weights determine our position on that landscape. We want to find the lowest valley — the minimum loss.

Gradient descent is how we walk downhill. At each step, we compute the gradient of the loss with respect to each weight — essentially the slope of the hill at our current position — and we step in the direction opposite to the slope.

The weight update rule is:

`W = W - learning_rate * (gradient of loss with respect to W)`

The **learning rate** controls how big each step is.

- Too large: we overshoot the minimum, bounce around, never converge
- Too small: we take tiny steps, training takes forever
- Just right: we descend steadily to a good minimum

[Slide: Three variants of gradient descent]

There are three main variants you need to know:

**Batch Gradient Descent:** Compute gradient over the entire dataset at once. Very stable updates but slow and memory-intensive for large datasets.

**Stochastic Gradient Descent (SGD):** Compute gradient on one sample at a time. Fast updates but very noisy — the loss bounces around significantly.

**Mini-batch Gradient Descent:** Compute gradient over a small batch, typically 32 or 64 samples. This is the best of both worlds — this is what Keras uses when you call `model.fit()`.

[Camera: Instructor]

In TensorFlow, when you call `model.fit()`, the optimizer is doing mini-batch gradient descent under the hood every step. Common optimizers you will use:

- `SGD` — classic stochastic gradient descent, optionally with momentum
- `Adam` — adaptive learning rates per parameter, typically the best default
- `RMSprop` — similar to Adam, works well on recurrent networks

Adam is your safe default starting point for almost all problems on the certification exam.

---

## SEGMENT 7 — Backpropagation (17:00–21:00)

[Whiteboard or annotated diagram]

Backpropagation is the algorithm that computes those gradients efficiently. It uses the chain rule of calculus to propagate the error signal backward through the network.

Let me give you the intuition without drowning in notation.

We have a loss L. The loss depends on the output of the last layer. The output of the last layer depends on the weights and the output of the previous layer. The output of each layer depends on its own weights and the layer before it.

The chain rule says: to find how L changes with respect to a weight deep in the network, multiply all the local derivatives along the path from that weight to the output.

Symbolically: `dL/dW1 = dL/dOutput * dOutput/dHidden * dHidden/dW1`

TensorFlow's automatic differentiation engine — called `tf.GradientTape` — tracks every operation in the forward pass and automatically computes these gradients for us.

[Screen: Code demonstration]

```python
import tensorflow as tf

x = tf.constant([[1.0, 2.0]])
y_true = tf.constant([[1.0]])

W = tf.Variable([[0.5], [-0.3]])
b = tf.Variable([[0.1]])

with tf.GradientTape() as tape:
    z = tf.matmul(x, W) + b
    y_pred = tf.sigmoid(z)
    loss = -(
        y_true * tf.math.log(y_pred) +
        (1 - y_true) * tf.math.log(1 - y_pred)
    )

gradients = tape.gradient(loss, [W, b])
print("Gradient w.r.t. W:", gradients[0].numpy())
print("Gradient w.r.t. b:", gradients[1].numpy())
```

[Camera: Instructor]

Notice: we did not implement a single derivative by hand. TensorFlow tracked every operation inside the `with tf.GradientTape()` block and computed all gradients automatically. This automatic differentiation is what makes modern deep learning practical at scale.

In Keras, `model.fit()` uses GradientTape internally during training. You almost never call it directly — but understanding that it exists and what it does is essential for the certification exam and for debugging custom training loops.

---

## SEGMENT 8 — The Complete Training Loop (21:00–22:30)

[Slide: Training loop diagram with numbered steps]

Let me summarize the full training loop so you can see all the pieces together:

1. **Initialize** weights randomly — small values, never all zeros
2. **Forward pass** — compute predictions for one batch of data
3. **Compute loss** — measure how wrong the predictions are
4. **Backward pass** — run backpropagation, compute gradients via chain rule
5. **Update weights** — apply the gradient descent step using the optimizer
6. **Repeat** for every batch in every epoch

In Keras, `model.fit(X_train, y_train, epochs=50, batch_size=32)` executes steps 2 through 5 automatically for 50 full passes over the training data.

Understanding this loop conceptually is what separates someone who can use Keras from someone who can debug it, extend it, and trust it.

---

## SEGMENT 9 — Wrap-Up and Preview (22:30–24:00)

[Camera: Instructor]

Today we covered the complete theoretical foundation of neural networks: the perceptron model, activation functions, forward propagation, loss functions, gradient descent variants, and backpropagation via the chain rule.

In Module 5, we move into TensorFlow and Keras hands-on — building, compiling, and training real models using the Sequential API and the Functional API.

Your lab this week has you implement a simple two-layer neural network manually in NumPy, then replicate the exact same network in TensorFlow and verify that the outputs match. The goal is to connect the math you learned today directly to the code you will write all semester.

Complete the quiz and post to the discussion board by Sunday at midnight.

See you in Module 5.

---

## Production Notes

- B-roll: animated neuron firing graphic during Segment 2
- Screen capture: all code segments recorded at 1080p, font size 18 or larger
- Slides: dark background, high contrast text — export as PDF for accessibility
- Closed captions required for all segments
- Annotations: highlight each line of code as it is discussed

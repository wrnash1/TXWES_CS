# Reading Guide: Module 04 - Neural Networks: Perceptrons and Backpropagation
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 04 - Neural Networks: Perceptrons and Backpropagation**! This module covers the mathematical machinery inside every Keras model. The perceptron is the building block: a single neuron that computes a weighted sum of inputs, adds a bias, and passes the result through an activation function. Stacking perceptrons into layers produces a deep neural network. Backpropagation is the algorithm that trains those layers by computing gradients and updating weights via gradient descent.

Understanding how forward and backward passes work at a conceptual level is critical for the TensorFlow Developer Certificate — you need to make informed choices about activation functions, loss functions, and optimizers.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Perceptron**: The simplest neural network unit. It computes a weighted sum of its inputs (z = w·x + b), passes z through an activation function f, and outputs f(z). A single perceptron is equivalent to logistic regression when f = sigmoid. Multiple perceptrons arranged in layers form a deep neural network capable of learning non-linear decision boundaries.

*   **Activation function**: A non-linear function applied to each neuron's weighted sum to allow the network to learn complex patterns. Without activation functions, stacked layers would collapse to a single linear transformation. Common choices: ReLU (max(0, x)) for hidden layers due to fast training; sigmoid for binary outputs; softmax for multi-class outputs; linear (no activation) for regression outputs.

*   **Forward pass**: The computation that flows from input through each layer to produce a prediction. Each layer applies its weights, biases, and activation function in sequence. In Keras, `model.predict(X)` and the training forward pass during `model.fit()` both execute forward passes.

*   **Backpropagation**: The algorithm for computing the gradient of the loss with respect to every weight in the network. It works backwards from the output layer, applying the chain rule of calculus to propagate error signals layer by layer. These gradients are then used by the optimizer (e.g., Adam, SGD) to update weights to reduce the loss.

*   **Chain rule**: The calculus rule that allows gradients to be computed through composed functions: d(f∘g)/dx = (df/dg) × (dg/dx). In backpropagation, the chain rule is applied repeatedly across every layer to compute how much each weight contributed to the final loss.

*   **Weight initialization**: The starting values assigned to network weights before training. Poor initialization (e.g., all zeros) causes symmetry breaking failure — all neurons learn the same features. Keras uses Glorot uniform initialization by default for Dense layers, which scales weight variance to the number of input and output units.

---

### 2. Certification Exam Tips
*   **Activation Function Selection:** On the TF exam, remember: ReLU for hidden layers, sigmoid for binary output, softmax for multi-class output, linear for regression. Using sigmoid in hidden layers risks vanishing gradients in deep networks.
*   **model.summary():** Always call `model.summary()` to verify output shapes and parameter counts. The exam may require you to predict output shapes after Conv2D or Dense layers.
*   **Optimizer Choices:** Adam (`optimizer='adam'`) is the safe default for almost all exam tasks. SGD with momentum works but requires more tuning. Avoid using SGD without momentum on deep networks.
*   **Study Resource:** The [fast.ai Practical Deep Learning course](https://course.fast.ai/) (free) covers perceptrons and backpropagation visually in the first two lessons. The [TensorFlow Neural Network Playground](https://playground.tensorflow.org/) lets you interactively visualize how neurons and layers learn decision boundaries — highly recommended before the exam.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the [Keras activation functions guide](https://www.tensorflow.org/api_docs/python/tf/keras/activations) and the [Keras optimizers overview](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers) at tensorflow.org. These free official docs describe every activation and optimizer available in the exam environment.
*   **Required Video:** Watch the Neural Networks and Backpropagation lecture in the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This segment covers the forward pass, loss calculation, and gradient descent weight updates step by step.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Build a multi-layer dense network**: Use `tf.keras.Sequential` with two hidden `Dense` layers using ReLU activation and one output layer with the appropriate activation for the task type.
*   **Trace forward propagation manually**: For a small network with known weights, compute the output of each layer by hand (z = w·x + b, then apply activation) and verify against `model.predict()`.
*   **Inspect gradients with GradientTape**: Use `tf.GradientTape()` to compute gradients of a simple loss with respect to model weights and print them to confirm backpropagation is working.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and sketch the forward pass of a two-layer network by hand.
*   [ ] Review the [Keras activations](https://www.tensorflow.org/api_docs/python/tf/keras/activations) and [optimizers](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers) documentation.
*   [ ] Experiment with the [TensorFlow Neural Network Playground](https://playground.tensorflow.org/) to visualize how layers learn.
*   [ ] Watch the backpropagation segment of the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 04 lab: build, trace, and inspect a multi-layer network.
*   [ ] Proceed to the Module 04 quiz.

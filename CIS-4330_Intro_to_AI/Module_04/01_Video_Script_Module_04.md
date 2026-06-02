# Video Script: Module 04 - Neural Networks and Deep Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AI-900 Domain:** Describe fundamental principles of machine learning on Azure (20-25%)

---

## [00:00 - 01:30] Opening

Welcome back. Professor Nash here, and this is Module 04. We have spent the last three modules building a solid foundation in machine learning concepts. Today we take a significant step forward: neural networks and deep learning. This is one of the most exciting areas in modern AI — it is the technology behind image recognition, speech-to-text, language translation, and generative AI systems.

Deep learning appears in the AI-900 exam primarily in the context of Azure Machine Learning and computer vision workloads. You need to understand the architecture of a neural network conceptually, how learning happens through a process called backpropagation, and why deep learning is particularly well-suited for unstructured data. Let us dig in.

---

## [01:30 - 05:00] The Biological Inspiration

[SHOW DIAGRAM: Left side — a simplified neuron with labeled dendrites, cell body, and axon. Right side — an artificial neuron with labeled inputs (x1, x2, x3), weights (w1, w2, w3), summation function, activation function, and output.]

Neural networks are loosely inspired by the structure of the human brain. The brain contains roughly 86 billion neurons. Each neuron receives signals from thousands of other neurons through dendrites, processes those signals in the cell body, and fires an output signal through its axon to other neurons when the combined input exceeds a threshold.

An artificial neuron mimics this structure mathematically. It receives multiple input values. Each input is multiplied by a weight — a number that represents the strength of that connection. The neuron adds up the weighted inputs. It then passes the sum through an activation function, which introduces non-linearity and determines the neuron's output. That output is passed to neurons in the next layer.

The key insight is that the weights are learned from data. At the start of training, weights are assigned randomly. Through the training process — which we will discuss in a moment — the weights are adjusted to minimize prediction error. By the end of training, the weights encode the patterns the network discovered in the data.

---

## [05:00 - 09:30] Neural Network Architecture

[SHOW DIAGRAM: Three-layer neural network. Left column: three circles labeled "Input Layer" with labels x1, x2, x3. Middle columns: two layers of circles labeled "Hidden Layer 1" and "Hidden Layer 2." Right column: one circle labeled "Output Layer." Lines connecting all nodes between adjacent layers, labeled "weights."]

A neural network is organized into layers. Let me walk through the standard architecture.

The input layer receives the raw features of each data example. Each node in the input layer corresponds to one feature. If you have 10 features, you have 10 input nodes. No computation happens at the input layer — it simply passes the feature values forward.

The hidden layers are where the actual computation occurs. Each hidden layer contains a set of neurons. Each neuron receives the outputs of all neurons in the previous layer, multiplies them by its weights, sums the results, applies an activation function, and passes the output to the next layer. A network with many hidden layers is called a deep network — this is where the term "deep learning" comes from.

The output layer produces the final prediction. For binary classification, the output layer typically has one node that produces a probability between 0 and 1. For multi-class classification, the output layer has one node per class, and a softmax activation function converts the raw scores into probabilities that sum to 1. For regression, the output layer has one node with no activation function, producing a raw continuous value.

The depth of a network — the number of hidden layers — determines its capacity to learn complex patterns. Shallow networks (one or two hidden layers) can learn simple patterns. Deep networks (many hidden layers) can learn hierarchical, abstract representations. A convolutional neural network designed for image recognition, for example, learns low-level features like edges in early layers, mid-level features like shapes in middle layers, and high-level concepts like "dog" or "car" in the final layers.

---

## [09:30 - 13:00] Forward Pass and Backward Pass

[SHOW DIAGRAM: Same network diagram with two sets of arrows. Red arrows going left to right labeled "Forward Pass: compute predictions." Blue arrows going right to left labeled "Backward Pass: propagate error gradients."]

Training a neural network involves two passes through the network: forward and backward.

The forward pass is prediction. You take one training example, pass its feature values through the input layer, compute each neuron's output through each hidden layer in sequence, and arrive at the network's prediction at the output layer. You then compare this prediction to the true label using a loss function — a mathematical formula that measures how wrong the prediction is. Common loss functions include mean squared error for regression and cross-entropy loss for classification.

The backward pass is learning. This process is called backpropagation — short for backward propagation of error gradients. Starting from the loss at the output layer, backpropagation computes how much each weight in the network contributed to that loss. It uses the chain rule of calculus to propagate these gradient values backward through the network, layer by layer, from output to input.

Once we know the gradient for each weight — the direction and magnitude in which changing that weight would increase the loss — we update the weights in the opposite direction by a small step. The size of this step is controlled by the learning rate, a hyperparameter. This update process is called gradient descent.

The forward and backward passes repeat for many training examples across many iterations called epochs. With each iteration, the weights are adjusted slightly, and the network's predictions gradually improve.

---

## [13:00 - 16:00] Activation Functions

Activation functions are crucial because they introduce non-linearity. Without activation functions, a neural network with any number of layers would collapse mathematically to a single linear transformation — it could only learn linear patterns, making deep layers useless.

The three activation functions you need to know for this course:

**ReLU — Rectified Linear Unit:** The most widely used activation function in hidden layers. ReLU outputs the input directly if it is positive, and outputs zero if it is negative. It is fast to compute, avoids certain training problems, and enables very deep networks to train effectively.

**Sigmoid:** Outputs a value between 0 and 1. Used in binary classification output layers to produce a probability. Not used in hidden layers of modern deep networks due to training problems at extreme input values.

**Softmax:** Applied to the output layer in multi-class classification. Takes a vector of raw scores and converts them to probabilities that sum to 1. The class with the highest probability is the predicted class.

---

## [16:00 - 19:00] Types of Deep Learning Architectures

Different types of neural network architectures are designed for different types of data.

**Feedforward Neural Networks** — also called multilayer perceptrons — are the basic architecture we have been discussing. Data flows in one direction: input to output. Best for structured tabular data.

**Convolutional Neural Networks (CNNs)** are designed for image data. Convolutional layers apply learned filters that scan across the image to detect local features, preserving spatial relationships between pixels. CNNs are the architecture behind Azure Computer Vision. We cover them in detail in Module 06.

**Recurrent Neural Networks (RNNs)** and their modern variants — LSTM (Long Short-Term Memory) and GRU (Gated Recurrent Unit) — are designed for sequential data like time series, text, and audio. They maintain internal state that allows them to remember context from earlier in the sequence.

**Transformer Networks** are the architecture behind modern large language models and generative AI systems. Instead of processing sequences step by step, transformers use a mechanism called self-attention to process entire sequences in parallel and capture long-range dependencies. GPT-4 and Azure OpenAI Service are built on transformer architectures. We cover transformers in Module 11.

For the AI-900 exam, you need to know: CNNs for images, RNNs for sequences, transformers for language models.

---

## [19:00 - 21:30] Deep Learning in Azure

Azure Machine Learning supports deep learning training through its compute clusters and integration with popular frameworks. Supported frameworks include PyTorch, TensorFlow, and Keras, which can all be used within Azure ML training runs.

Azure also provides deep learning capabilities through prebuilt services that require no model training on your part. Azure Computer Vision uses convolutional neural networks trained on millions of images. Azure Speech Service uses recurrent architectures for speech recognition. Azure OpenAI Service exposes transformer-based language models including GPT-4.

For the AI-900 exam, the key distinction is: Azure Machine Learning is for training custom deep learning models, while Azure Cognitive Services provides prebuilt deep learning capabilities accessible through simple API calls.

---

## [21:30 - 23:30] Module Summary and Lab Preview

Let me recap Module 04.

Neural networks are organized into an input layer, one or more hidden layers, and an output layer. Each neuron computes a weighted sum of its inputs, passes the result through an activation function, and passes the output forward. Training involves a forward pass to compute predictions, a loss function to measure error, and backpropagation to compute gradients and update weights via gradient descent.

Deep learning uses many hidden layers to learn hierarchical representations. CNNs are optimized for images. RNNs handle sequential data. Transformers power modern language models. Azure supports deep learning through Azure ML for custom models and Cognitive Services for prebuilt capabilities.

This week's lab is the most analytical we have done so far. You will trace a complete forward pass through a small neural network — three inputs, two hidden neurons, one output — by hand, computing each neuron's activation step by step. This exercise builds the intuition you need to understand what a neural network is actually doing when it makes a prediction.

See you in Module 05, where we move into natural language processing.

---

## References

- Microsoft Learn — Explore deep learning concepts: learn.microsoft.com/en-us/training/modules/train-evaluate-deep-learn-models/
- Microsoft Learn — Introduction to Azure Machine Learning: learn.microsoft.com/en-us/training/modules/intro-to-azure-machine-learning-service/

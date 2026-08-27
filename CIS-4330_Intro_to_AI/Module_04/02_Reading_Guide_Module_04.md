# Reading Guide: Module 04 - Neural Networks and Deep Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe fundamental principles of machine learning on Azure (20-25%)

---

## Overview

This reading guide covers neural network architecture, the training process, activation functions, deep learning architectures, and Azure's deep learning services. Neural networks underpin computer vision, speech recognition, NLP, and generative AI — all major AI-900 exam domains. Complete the study checklist before the lab.

---

## Section 1: Core Vocabulary

**Artificial Neuron**
The basic computational unit of a neural network. It receives multiple inputs, multiplies each by a weight, sums the weighted inputs, applies an activation function, and produces an output.

**Weight**
A numerical parameter in a neural network that represents the strength of the connection between two neurons. Weights are randomly initialized and adjusted during training via gradient descent.

**Bias**
An additional trainable parameter added to a neuron's weighted sum before the activation function. The bias allows the activation function to shift, enabling the neuron to activate even when all input values are zero.

**Input Layer**
The first layer of a neural network. Each node corresponds to one input feature. No computation occurs; values are passed directly to the first hidden layer.

**Hidden Layer**
Any layer between the input and output layers. Hidden layers perform the bulk of the computation. Networks with many hidden layers are called deep networks.

**Output Layer**
The final layer that produces the network's prediction. Architecture depends on task type: one sigmoid node for binary classification, multiple softmax nodes for multi-class classification, one linear node for regression.

**Activation Function**
A non-linear function applied to a neuron's weighted sum. Introduces the non-linearity that allows neural networks to learn complex patterns. Without activation functions, deep networks collapse to linear transformations.

**ReLU (Rectified Linear Unit)**
The most common activation function in hidden layers. Outputs the input value if positive, zero otherwise. Fast to compute and enables effective training of very deep networks.

**Sigmoid**
An activation function that outputs a value between 0 and 1. Used in binary classification output layers to produce probability estimates.

**Softmax**
An activation function applied to the output layer in multi-class classification. Converts a vector of raw scores into probabilities that sum to 1.

**Forward Pass**
The process of computing a neural network's prediction by passing inputs through each layer in sequence, from input to output.

**Loss Function**
A mathematical function that measures the difference between the network's prediction and the true label. Common loss functions: mean squared error (regression), cross-entropy loss (classification). The goal of training is to minimize the loss.

**Backpropagation**
The algorithm for computing the gradient of the loss with respect to each weight in the network, using the chain rule of calculus. Gradients are propagated backward from the output layer to the input layer.

**Gradient Descent**
An optimization algorithm that iteratively updates weights in the direction that decreases the loss. Each update step is proportional to the negative gradient.

**Learning Rate**
A hyperparameter that controls the size of each weight update step in gradient descent. Too high: training diverges. Too low: training is very slow. Typical values: 0.001 to 0.1.

**Epoch**
One complete pass through the entire training dataset. Training typically requires multiple epochs — often tens to hundreds — to converge.

**Overfitting (neural networks)**
When a neural network memorizes training data and performs poorly on new data. More likely with very deep or wide networks trained on small datasets. Mitigated by dropout, regularization, or early stopping.

**Dropout**
A regularization technique for neural networks in which a random subset of neurons is temporarily removed during each training step. Forces the network to learn redundant representations, reducing overfitting.

**Convolutional Neural Network (CNN)**
A deep learning architecture designed for image data. Convolutional layers apply learnable filters that scan across the image, detecting local features while preserving spatial structure.

**Recurrent Neural Network (RNN)**
A deep learning architecture for sequential data. Each neuron has a recurrent connection that passes information from one time step to the next, enabling the network to model temporal dependencies.

**LSTM (Long Short-Term Memory)**
A variant of RNN with gating mechanisms that control which information is retained or forgotten over long sequences. Overcomes the vanishing gradient problem in standard RNNs.

**Transformer**
A deep learning architecture that uses self-attention mechanisms to process entire sequences in parallel, capturing long-range dependencies without recurrence. The architecture behind modern large language models (GPT-4, etc.).

**Transfer Learning**
A technique in which a model pretrained on a large dataset is fine-tuned on a smaller domain-specific dataset. Dramatically reduces the data and compute required for deep learning on specialized tasks.

---

## Section 2: Comparison Tables

### Table 1: ML vs Deep Learning

| Dimension | Traditional Machine Learning | Deep Learning |
|---|---|---|
| Feature engineering | Manual — domain expert designs features | Automatic — network learns features from raw data |
| Data requirement | Low to moderate (hundreds to thousands) | High (thousands to millions) |
| Compute requirement | Low to moderate (CPU sufficient) | High (GPU or TPU required) |
| Interpretability | Moderate to high (decision trees, logistic regression) | Low (black box without explainability tools) |
| Best data type | Structured tabular data | Unstructured data: images, audio, text |
| Training time | Minutes to hours | Hours to days |
| Azure service | Azure ML AutoML | Azure ML with deep learning frameworks |

### Table 2: Deep Learning Architectures

| Architecture | Best Input Type | Key Innovation | Azure Application |
|---|---|---|---|
| Feedforward (MLP) | Structured tabular data | Multiple non-linear layers | Azure ML custom models |
| CNN | Images and video | Convolutional filters preserve spatial structure | Azure Computer Vision, Custom Vision |
| RNN / LSTM | Sequential data: text, time series, audio | Recurrent connections model temporal context | Azure Speech Service, language modeling |
| Transformer | Text, code, images (ViT) | Self-attention captures long-range dependencies | Azure OpenAI Service (GPT-4) |
| Autoencoder | Dimensionality reduction, anomaly detection | Encoder-decoder architecture learns compact representations | Custom Azure ML models |

### Table 3: Activation Functions

| Function | Formula (conceptual) | Output Range | Typical Use |
|---|---|---|---|
| ReLU | max(0, x) | 0 to infinity | Hidden layers in deep networks |
| Sigmoid | 1 / (1 + e^(-x)) | 0 to 1 | Binary classification output |
| Softmax | e^(xi) / sum(e^(xj)) | 0 to 1 (sums to 1) | Multi-class classification output |
| Tanh | (e^x - e^(-x)) / (e^x + e^(-x)) | -1 to 1 | Hidden layers (less common than ReLU) |
| Linear (no activation) | x | Unbounded | Regression output layer |

### Table 4: Hyperparameters in Neural Networks

| Hyperparameter | What It Controls | Typical Values | Effect of Too High | Effect of Too Low |
|---|---|---|---|---|
| Learning rate | Step size in gradient descent | 0.0001 to 0.1 | Training diverges (loss increases) | Very slow convergence |
| Batch size | Number of examples per gradient update | 32, 64, 128, 256 | Less stable gradients | Slow training; very noisy updates |
| Number of layers | Network depth | 2 to 1000+ | Overfitting; vanishing gradients | Underfitting |
| Number of neurons per layer | Layer width | 32 to 4096 | Overfitting; slow training | Underfitting |
| Dropout rate | Fraction of neurons dropped each step | 0.1 to 0.5 | Underfitting | No regularization effect |
| Epochs | Training iterations over full dataset | 10 to 500+ | Overfitting | Underfitting |

---

## Section 3: The Forward Pass in Detail

Understanding the forward pass is essential for the Module 04 lab and for AI-900 conceptual questions.

Consider a network with 3 input nodes, 2 hidden neurons (ReLU activation), and 1 output neuron (sigmoid activation).

For hidden neuron H1:

1. Multiply each input by its weight: x1 times w11, x2 times w21, x3 times w31.
2. Add the products and add the bias: z1 = (x1 times w11) + (x2 times w21) + (x3 times w31) + b1.
3. Apply ReLU: H1 output = max(0, z1).

For hidden neuron H2 (same process with different weights):

1. z2 = (x1 times w12) + (x2 times w22) + (x3 times w32) + b2.
2. H2 output = max(0, z2).

For output neuron O1:

1. z_out = (H1 times w_H1) + (H2 times w_H2) + b_out.
2. Apply sigmoid: O1 output = 1 / (1 + e^(-z_out)).

The output is a probability between 0 and 1. If this is a binary classifier, output above 0.5 predicts class 1; below 0.5 predicts class 0.

---

## Section 4: Transfer Learning and Azure AI

Training a deep learning model from scratch requires vast datasets and significant GPU compute time. For most business applications, this is impractical. Transfer learning solves this problem.

A pretrained model — one trained by a large research team on millions of examples — has already learned general feature representations. For images, a pretrained CNN has learned to detect edges, textures, shapes, and objects. For text, a pretrained transformer has learned grammar, semantics, and world knowledge.

Transfer learning takes this pretrained model and fine-tunes it on a smaller domain-specific dataset. The early layers, which contain general features, are frozen. Only the later layers, which encode task-specific patterns, are updated with new training data.

Azure Custom Vision uses transfer learning to let users train image classifiers with as few as 15 images per class. The underlying CNN was pretrained by Microsoft on millions of images; the user's small dataset fine-tunes the final layers for the specific classification task.

---

## Section 5: AI-900 Exam Tips

1. Deep learning is the correct answer when the input data is unstructured at scale: images, audio, long text documents. Structured tabular data does not typically require deep learning.

2. CNNs are the architecture for computer vision. RNNs and transformers are architectures for natural language processing. Transformers have largely replaced RNNs in modern NLP.

3. The AI-900 exam does not require you to code neural networks or perform backpropagation calculations. You need to understand the concepts and match architectures to scenarios.

4. Transfer learning is relevant when the scenario describes training a model on a small dataset for a specialized task. Custom Vision and Azure OpenAI fine-tuning both use transfer learning.

5. Overfitting in neural networks is addressed by dropout, regularization, early stopping, or data augmentation — not by adding more layers or neurons.

6. The learning rate is the most critical hyperparameter for neural network training. Too high and the model diverges; too low and training is impractically slow.

7. Azure Machine Learning supports PyTorch, TensorFlow, and Keras for custom deep learning model training. You do not need to know the code syntax for AI-900 but you should know the framework names.

8. The AI-900 exam distinguishes between building a custom deep learning model (Azure ML) and using a prebuilt deep learning capability (Azure Cognitive Services). A scenario saying "no training data available" or "prebuilt API" points to Cognitive Services.

---

## Section 6: Required Reading

**Microsoft Learn — Train and evaluate deep learning models**
learn.microsoft.com/en-us/training/modules/train-evaluate-deep-learn-models/

Covers neural network architecture, the training loop, and PyTorch basics at a conceptual level appropriate for AI-900.

**Microsoft Learn — Introduction to Azure Machine Learning**
learn.microsoft.com/en-us/training/modules/intro-to-azure-machine-learning-service/

Covers the Azure ML workspace, compute, experiments, and deployment — the operational context for deep learning on Azure.

---

## Section 7: Study Checklist

- [ ] Write the definitions of neuron, weight, activation function, forward pass, backpropagation, and epoch from memory.
- [ ] Trace the forward pass in Section 3 with a small set of example numbers to verify your understanding.
- [ ] Study Table 1 (ML vs DL) and be able to articulate when NOT to use deep learning.
- [ ] Study Table 2 (architectures) and match each architecture to its input type from memory.
- [ ] Study Table 3 (activation functions) and know which function to use for binary classification, multi-class classification, and regression output layers.
- [ ] Explain transfer learning in two sentences without looking at your notes.
- [ ] Complete the Microsoft Learn module: Train and evaluate deep learning models.
- [ ] Review all eight AI-900 exam tips in Section 5.
- [ ] Complete the Module 04 quiz.
- [ ] Complete the Module 04 lab (manual forward pass trace).
- [ ] Post initial discussion by Wednesday 11:59 PM and respond to two peers by Sunday 11:59 PM.

## 9. Supplemental Resources

**1. 3Blue1Brown — Neural Networks (YouTube series)**
<https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi>
A visually stunning free YouTube series explaining neural networks, gradient descent, and backpropagation with animated intuition-building visualizations. Widely regarded as the most accessible introduction to how neural networks actually learn — strongly recommended before or alongside the Module 04 reading.

**2. PyTorch — Deep Learning with PyTorch: A 60 Minute Blitz**
<https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html>
The official PyTorch beginner tutorial covering tensors, autograd, neural network construction, and training a simple CNN. Provides hands-on experience with the dominant deep learning framework used in research and industry.

**3. Distill.pub — A Neural Network Playground (TensorFlow Playground)**
<https://playground.tensorflow.org/>
An interactive browser-based tool for experimenting with neural network architectures, activation functions, learning rates, and regularization on toy datasets in real time. Ideal for building intuition about how architectural choices affect learning without writing any code.

# Quiz: Module 04 - Neural Networks and Deep Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe fundamental principles of machine learning on Azure
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

Which component of a neural network determines the strength of the connection between two neurons and is adjusted during training?

- A) Activation function
- B) Loss function
- C) Weight
- D) Epoch

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Weights are the trainable numerical parameters that scale each input to a neuron. Backpropagation and gradient descent adjust weights to minimize the loss function during training.
- *Why A is incorrect:* Activation functions introduce non-linearity but are not parameters learned during training — they are fixed design choices.
- *Why B is incorrect:* The loss function measures prediction error but does not connect neurons. It is the objective being minimized, not a network parameter.
- *Why D is incorrect:* An epoch is one complete pass through the training dataset — a training iteration count, not a network component.

---

## Question 2

A neural network is being designed for a ten-class image classification task. Which activation function should be applied at the output layer?

- A) ReLU
- B) Sigmoid
- C) Softmax
- D) Linear

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Softmax converts a vector of raw scores into probabilities that sum to 1, with one probability per class. It is the standard output activation for multi-class classification.
- *Why A is incorrect:* ReLU is used in hidden layers. It does not produce class probabilities and outputs unbounded positive values.
- *Why B is incorrect:* Sigmoid outputs a single value between 0 and 1 and is used for binary classification (two classes), not ten-class classification.
- *Why D is incorrect:* Linear output (no activation) is used for regression tasks, not classification. It produces unbounded values with no probabilistic interpretation.

---

## Question 3

Which of the following best describes what happens during the backward pass (backpropagation) in neural network training?

- A) Input features are passed through each layer from input to output to compute predictions.
- B) The gradient of the loss with respect to each weight is computed and weights are updated to reduce the loss.
- C) The training dataset is randomly shuffled and split into mini-batches for the next epoch.
- D) The output layer's softmax probabilities are converted back to one-hot encoded labels.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Backpropagation uses the chain rule to compute how much each weight contributed to the prediction error, then gradient descent updates each weight to reduce that error.
- *Why A is incorrect:* This describes the forward pass, not backpropagation.
- *Why C is incorrect:* Data shuffling and batching are preprocessing steps in the training loop, not part of backpropagation.
- *Why D is incorrect:* Softmax is applied during the forward pass; no conversion back to labels occurs in backpropagation.

---

## Question 4

Why are activation functions necessary in neural networks?

- A) They reduce the number of trainable parameters, making training faster.
- B) They introduce non-linearity, allowing the network to learn complex patterns that linear functions cannot capture.
- C) They convert continuous outputs into discrete class labels at every layer.
- D) They normalize the weights to prevent gradient explosion during backpropagation.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Without activation functions, any composition of linear transformations remains linear. Non-linear activations allow networks to approximate arbitrarily complex functions.
- *Why A is incorrect:* Activation functions do not reduce parameter count; the number of weights is determined by layer sizes.
- *Why C is incorrect:* Activation functions like ReLU output continuous values, not discrete labels. Only the final classification step converts probabilities to labels.
- *Why D is incorrect:* Batch normalization and gradient clipping address gradient explosion. Activation functions serve a fundamentally different purpose.

---

## Question 5

A company wants to build a model that identifies defective products from conveyor belt camera images. They have only 400 labeled images — far too few to train a deep CNN from scratch. Which approach is most appropriate?

- A) Train a logistic regression model on pixel values, since it requires less data.
- B) Use transfer learning by fine-tuning a pretrained CNN on the 400 images.
- C) Use K-means clustering to group the images into defective and non-defective categories.
- D) Increase the network depth to 100 layers to improve generalization on the small dataset.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Transfer learning reuses a CNN pretrained on millions of images. The general visual features (edges, textures, shapes) are already learned; fine-tuning adjusts only the final layers using the 400 images. Azure Custom Vision uses this approach.
- *Why A is incorrect:* Logistic regression on raw pixel values ignores spatial structure and performs poorly on image tasks without feature engineering.
- *Why C is incorrect:* K-means is unsupervised and cannot produce a reliable defective/non-defective classification without labels. It also does not process images effectively without feature extraction.
- *Why D is incorrect:* Deeper networks require more data, not less. Adding more layers would dramatically increase overfitting on 400 images.

---

## Question 6

Which deep learning architecture is most appropriate for analyzing sequences of daily stock prices to predict the next day's closing price?

- A) Convolutional Neural Network (CNN)
- B) Feedforward Neural Network (MLP)
- C) Recurrent Neural Network / LSTM
- D) Autoencoder

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Time series data is sequential; each day's price depends on preceding days. RNNs and LSTMs maintain internal state that captures temporal dependencies across the sequence.
- *Why A is incorrect:* CNNs are designed for spatial data (images). While 1D CNNs can process sequences, they are less suited to long-range temporal dependencies than LSTMs.
- *Why B is incorrect:* An MLP processes each input independently without memory of previous time steps, making it ineffective for sequential prediction without manual feature engineering.
- *Why D is incorrect:* Autoencoders learn compressed representations for reconstruction or anomaly detection. They are not designed for time series forecasting.

---

## Question 7

A deep neural network achieves 98% training accuracy but only 71% test accuracy. Which regularization technique temporarily disables random neurons during each training step to force the network to learn more robust features?

- A) L2 regularization
- B) Batch normalization
- C) Early stopping
- D) Dropout

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* Dropout randomly sets a fraction of neuron outputs to zero during each training step. This prevents neurons from co-adapting and forces the network to develop redundant representations, reducing overfitting.
- *Why A is incorrect:* L2 regularization adds a penalty on large weight values to the loss function. It does not disable neurons.
- *Why B is incorrect:* Batch normalization normalizes layer activations to stabilize training. It does not disable neurons.
- *Why C is incorrect:* Early stopping halts training when validation performance stops improving. It does not modify the network structure during training.

---

## Question 8

What is the primary difference between Azure Machine Learning and Azure Cognitive Services for deep learning use cases?

- A) Azure Machine Learning only supports traditional ML; deep learning requires Azure Cognitive Services.
- B) Azure Machine Learning is for training custom models; Azure Cognitive Services provides prebuilt AI capabilities requiring no model training.
- C) Azure Cognitive Services stores training data; Azure Machine Learning deploys trained models.
- D) Azure Machine Learning is free; Azure Cognitive Services is a paid service.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* This is the core distinction on AI-900. Azure ML is the platform for building custom models from scratch or fine-tuning. Azure Cognitive Services exposes prebuilt deep learning models (computer vision, speech, language) via REST APIs with no training required.
- *Why A is incorrect:* Azure Machine Learning fully supports deep learning training with PyTorch, TensorFlow, and Keras.
- *Why C is incorrect:* Both services have storage components, but this is not the key distinction. The distinction is custom training vs. prebuilt capability.
- *Why D is incorrect:* Both services have associated costs. Pricing differences are not the relevant distinction for AI-900.

---

## Question 9

Which of the following scenarios best illustrates why the learning rate is a critical hyperparameter in neural network training?

- A) A learning rate that is too high causes the training loss to increase or oscillate rather than decrease toward a minimum.
- B) A learning rate that is too high causes the model to memorize training data and fail to generalize.
- C) A learning rate that is too low increases the number of hidden layers added during training.
- D) A learning rate that is too low prevents the softmax function from producing probabilities that sum to 1.

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* The learning rate controls the step size in gradient descent. If it is too large, weight updates overshoot the loss minimum and the loss oscillates or diverges. If too small, convergence is very slow.
- *Why B is incorrect:* Memorization (overfitting) is caused by excessive model capacity relative to data size, not by a high learning rate.
- *Why C is incorrect:* The learning rate does not affect network architecture. Hidden layers are fixed design choices, not added dynamically during training.
- *Why D is incorrect:* Softmax is a mathematical normalization function; its behavior is not affected by the learning rate.

---

## Question 10

A data scientist is designing a neural network to predict apartment rental prices. The output should be a specific dollar amount, not a probability. Which output layer configuration is correct?

- A) One output node with sigmoid activation
- B) One output node with softmax activation
- C) One output node with no activation function (linear output)
- D) Multiple output nodes with ReLU activation

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Regression outputs need to be continuous and unbounded — any real number. A linear output node (no activation function) passes the weighted sum directly as the prediction, which can represent any rental price value.
- *Why A is incorrect:* Sigmoid constrains the output to 0-1. Dollar amounts are not in this range and cannot be represented this way.
- *Why B is incorrect:* Softmax produces probabilities summing to 1 across multiple classes. It is not applicable to regression.
- *Why D is incorrect:* ReLU outputs non-negative values and is designed for hidden layers, not regression outputs. While it would constrain predictions to non-negative values (prices are non-negative), it is not the standard approach and cannot predict zero rental prices.

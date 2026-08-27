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

---

### Question 11 (5 points)

What is the primary purpose of the loss function during neural network training?

- A) It determines the architecture (number and size of layers) of the network.
- B) It measures the difference between the network's predictions and the true labels, providing a signal for weight updates.
- C) It applies non-linearity to each neuron's output to enable complex pattern learning.
- D) It controls the rate at which weights are updated during each gradient descent step.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The loss function (e.g., cross-entropy for classification, mean squared error for regression) quantifies prediction error. Backpropagation uses this signal to compute gradients and update weights to minimize the loss.
  - *Why A is incorrect:* Network architecture (layers and sizes) is a design choice made before training. The loss function does not determine architecture.
  - *Why C is incorrect:* Applying non-linearity is the role of activation functions, not the loss function.
  - *Why D is incorrect:* The learning rate controls the step size of weight updates. The loss function provides the error signal; the learning rate scales how much that signal changes the weights.

---

### Question 12 (5 points)

A neural network training run shows that training loss decreases steadily but validation loss begins increasing after epoch 15. The network continues training until epoch 50. What should the team do to improve generalization?

- A) Increase the number of hidden layers to reduce training loss further.
- B) Apply early stopping to halt training when validation loss begins to rise.
- C) Remove the validation set so the validation loss can no longer increase.
- D) Increase the learning rate to make the network converge faster.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Early stopping monitors validation loss and halts training at the point of minimum validation loss — around epoch 15 in this scenario. This prevents the network from overfitting to training data beyond the optimal point.
  - *Why A is incorrect:* More layers would increase model capacity and worsen overfitting when training loss is already decreasing while validation loss rises.
  - *Why C is incorrect:* Removing the validation set eliminates the only signal available to detect overfitting. This does not improve generalization — it makes the problem undetectable.
  - *Why D is incorrect:* A higher learning rate would change convergence speed but would not address the overfitting that begins at epoch 15. It could also cause instability.

---

### Question 13 (5 points)

Which deep learning architecture uses convolutional layers that slide a learned filter across an input image to detect spatial patterns such as edges and textures?

- A) Recurrent Neural Network (RNN)
- B) Transformer
- C) Autoencoder
- D) Convolutional Neural Network (CNN)

- **Correct Answer:** D
- **Distractor Analysis:**
  - *Why D is correct:* CNNs apply learned filters (kernels) that slide across input images, computing dot products at each position. This detects local spatial features — edges, corners, textures — while dramatically reducing parameter count compared to fully connected layers on raw pixels.
  - *Why A is incorrect:* RNNs process sequential data with recurrent connections that carry state from step to step. They are designed for time series and text, not image spatial structure.
  - *Why B is incorrect:* Transformers use self-attention mechanisms to model relationships between all positions in a sequence simultaneously. They are dominant in NLP and increasingly used in vision but do not use sliding convolutional filters.
  - *Why C is incorrect:* Autoencoders are encoder-decoder networks that learn compressed representations. They may use convolutional layers internally but are architecturally distinct from CNNs and serve different purposes.

---

### Question 14 (5 points)

Batch normalization is added after the hidden layers of a deep network. What is the primary benefit of this technique?

- A) It randomly drops neurons to prevent co-adaptation and reduce overfitting.
- B) It normalizes layer activations to have zero mean and unit variance, stabilizing training and enabling faster learning with higher learning rates.
- C) It penalizes large weight values by adding a regularization term to the loss function.
- D) It stops training when the validation loss stops improving.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Batch normalization normalizes the distribution of activations across each mini-batch, reducing internal covariate shift. This stabilizes the gradient signal, allows larger learning rates, and often speeds up convergence.
  - *Why A is incorrect:* Randomly dropping neurons is dropout, not batch normalization. They are complementary techniques that serve different purposes.
  - *Why C is incorrect:* Penalizing large weights describes L2 regularization (weight decay). Batch normalization does not add a term to the loss function.
  - *Why D is incorrect:* Stopping training based on validation loss is early stopping. Batch normalization is applied continuously throughout training, not used as a stopping criterion.

---

### Question 15 (5 points)

A researcher is fine-tuning a pretrained ResNet-50 image classification model for a medical imaging task. She freezes the early convolutional layers and only trains the final two layers. What is the rationale for freezing the early layers?

- A) Early layers contain task-specific medical features that should not be modified.
- B) Early layers detect low-level features like edges and textures that are general across image domains and do not need relearning.
- C) Freezing early layers reduces the total number of trainable parameters to zero, preventing overfitting.
- D) Early layers in ResNet-50 contain only random weights and freezing them saves time.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* In a pretrained CNN, early layers learn universal low-level features (edges, gradients, textures) that transfer well across domains. Only the later layers learn task-specific high-level features. Fine-tuning only the final layers preserves the general features while adapting the model to the new task.
  - *Why A is incorrect:* The opposite is true — early layers contain general visual features, while later layers contain task-specific features. Medical-specific features would be in the later layers.
  - *Why C is incorrect:* Freezing early layers reduces trainable parameters but not to zero — the final two layers are still trained. The reasoning is about transfer learning, not parameter count.
  - *Why D is incorrect:* ResNet-50 is pretrained on ImageNet and its weights reflect learned visual features, not random initialization.

---

### Question 16 (5 points)

Which of the following best describes the vanishing gradient problem in deep neural networks?

- A) Weights grow unboundedly large during training, causing the network to diverge.
- B) Gradients become extremely small as they are propagated backward through many layers, causing early layers to learn very slowly or not at all.
- C) The softmax function produces gradients that sum to zero, preventing the output layer from learning.
- D) The loss function returns negative values, causing weight updates to move in the wrong direction.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* During backpropagation, gradients are multiplied at each layer. With activation functions like sigmoid that compress values to (0,1), repeated multiplication shrinks gradients exponentially. Early layers receive near-zero gradient signals and fail to update effectively. ReLU and residual connections (ResNet) were developed largely to address this.
  - *Why A is incorrect:* Weights growing unboundedly describes the exploding gradient problem, which is the opposite issue. Gradient clipping addresses this.
  - *Why C is incorrect:* Softmax is applied only at the output layer and its gradient is well-defined. The vanishing gradient problem occurs in deep networks across all layers.
  - *Why D is incorrect:* Negative loss function values are possible (e.g., log-likelihood) and are handled by the optimization algorithm. Negative gradients indicate the direction to increase the loss, which is valid.

---

### Question 17 (5 points)

An LSTM (Long Short-Term Memory) network is specifically designed to address a limitation of simple RNNs. Which limitation does LSTM address?

- A) LSTMs can process image data faster than standard CNNs.
- B) Simple RNNs struggle to retain information from many time steps earlier due to vanishing gradients; LSTMs use gating mechanisms to selectively remember or forget information over long sequences.
- C) Simple RNNs require labeled data, while LSTMs are unsupervised.
- D) LSTMs eliminate the need for an output activation function in sequence prediction tasks.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Standard RNNs suffer from vanishing gradients over long sequences, making it difficult to learn long-range dependencies. LSTMs introduce input, forget, and output gates plus a cell state that allows the network to maintain relevant information across many time steps.
  - *Why A is incorrect:* LSTMs are sequential models designed for temporal data. CNNs are designed for spatial data. LSTMs do not process images faster than CNNs.
  - *Why C is incorrect:* Both RNNs and LSTMs are supervised sequence models when used for prediction tasks. The difference is architectural, not in the type of supervision.
  - *Why D is incorrect:* LSTMs still require output activations appropriate to the task (softmax for classification, linear for regression). The gating mechanism does not eliminate this requirement.

---

### Question 18 (5 points)

A neural network for handwritten digit recognition (10 classes) produces the following raw output scores: [2.1, 0.3, -0.8, 1.5, 0.2, -1.2, 0.7, 3.4, 0.1, 0.6]. After applying softmax, which class will have the highest probability?

- A) Class 0 (score 2.1)
- B) Class 3 (score 1.5)
- C) Class 7 (score 3.4)
- D) Class 6 (score 0.7)

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Softmax preserves the ordering of scores — the class with the highest raw score (logit) always receives the highest softmax probability. Class 7 has the highest score (3.4) and therefore the highest probability after softmax.
  - *Why A is incorrect:* Class 0 has a score of 2.1, which is the second highest. After softmax it would have a high probability but not the highest.
  - *Why B is incorrect:* Class 3 has a score of 1.5, which is third highest. Softmax would assign it a lower probability than classes 0 and 7.
  - *Why D is incorrect:* Class 6 has a score of 0.7, well below classes 0, 3, and 7. Its softmax probability would be noticeably lower.

---

### Question 19 (5 points)

Which of the following best describes an autoencoder neural network?

- A) A supervised network that classifies input data into predefined categories using labeled training examples.
- B) An unsupervised network that learns a compressed representation of inputs by training an encoder to compress and a decoder to reconstruct the original input.
- C) A reinforcement learning agent that uses neural networks to estimate the value of each possible action in a game environment.
- D) A recurrent network that generates new text sequences by predicting the next word given previous words.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Autoencoders consist of an encoder (compresses input to a lower-dimensional bottleneck) and a decoder (reconstructs the original input from the compressed representation). They are trained unsupervised by minimizing reconstruction error. Applications include dimensionality reduction and anomaly detection.
  - *Why A is incorrect:* This describes a supervised classification network. Autoencoders do not require labels and do not classify inputs into predefined categories.
  - *Why C is incorrect:* This describes a Deep Q-Network (DQN), a reinforcement learning architecture. Autoencoders are unsupervised and do not involve agents or reward signals.
  - *Why D is incorrect:* Text generation using next-word prediction describes a language model (RNN-based or Transformer-based). While language models use neural networks, they are not autoencoders.

---

### Question 20 (5 points)

A team wants to generate photorealistic synthetic product images for an e-commerce catalog using deep learning. No real product images exist yet. Which deep learning architecture is specifically designed for generating new realistic data samples?

- A) Convolutional Neural Network (CNN) classifier
- B) Long Short-Term Memory (LSTM) network
- C) Generative Adversarial Network (GAN)
- D) Feedforward Neural Network (MLP) regressor

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* GANs consist of a generator network that creates synthetic images and a discriminator network that attempts to distinguish real from generated images. Through adversarial training, the generator learns to produce photorealistic outputs. GANs are the standard architecture for synthetic image generation.
  - *Why A is incorrect:* A CNN classifier categorizes existing images — it does not generate new images. Classification and generation are fundamentally different tasks.
  - *Why B is incorrect:* LSTMs model sequential temporal data (time series, text). They are not designed for image generation.
  - *Why D is incorrect:* An MLP regressor predicts continuous numerical outputs from structured tabular inputs. It cannot generate high-dimensional realistic images.

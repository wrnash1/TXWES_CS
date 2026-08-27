# Lab Activity: Module 04 - Neural Networks and Deep Learning

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe fundamental principles of machine learning on Azure
**Points:** 100
**Submission:** Canvas LMS — Module 04 Lab Assignment

---

## Objectives

By the end of this lab, you will be able to:

- Trace a complete neural network forward pass by hand, computing each neuron's activation step by step.
- Identify the correct activation function for each layer type.
- Interpret the output of a neural network as a probability and make a classification decision.
- Calculate the loss for a single training example.
- Compare deep learning architectures and match each to the appropriate data type and scenario.

---

## Prerequisites

No Azure subscription is required. All exercises are mathematical computations and written analysis. You will need:

- Module 04 video lecture (completed).
- Module 04 reading guide (completed), particularly the forward pass section.
- A calculator.

---

## Part A: Manual Neural Network Forward Pass (50 points)

This is the primary exercise for Module 04. You will trace a complete forward pass through a small neural network, computing each value step by step. This is the same process a framework like PyTorch or TensorFlow performs millions of times during training, but working through it manually builds deep intuition.

### Network Architecture

The network has:

- 3 input nodes: x1, x2, x3
- 2 hidden neurons: H1 and H2 (both use ReLU activation)
- 1 output neuron: O (uses Sigmoid activation)

### Input Values

- x1 = 0.5
- x2 = 1.0
- x3 = -0.5

### Weights from Input Layer to Hidden Layer

For hidden neuron H1:

- w(x1 to H1) = 0.8
- w(x2 to H1) = -0.4
- w(x3 to H1) = 0.6
- Bias b1 = 0.1

For hidden neuron H2:

- w(x1 to H2) = -0.3
- w(x2 to H2) = 0.7
- w(x3 to H2) = 0.2
- Bias b2 = -0.2

### Weights from Hidden Layer to Output Layer

- w(H1 to O) = 0.9
- w(H2 to O) = -0.5
- Bias b_out = 0.0

---

### Step 1: Compute the Pre-Activation Value for H1 (8 points)

The pre-activation value z1 is the weighted sum of inputs plus bias:

z1 = (x1 x w(x1 to H1)) + (x2 x w(x2 to H1)) + (x3 x w(x3 to H1)) + b1

Show each multiplication, the sum, and the final result.

**Your calculation:**

(0.5 x 0.8) = ________

(1.0 x -0.4) = ________

(-0.5 x 0.6) = ________

Bias = ________

z1 = ________

### Step 2: Apply ReLU to Get H1 Output (4 points)

ReLU(z) = max(0, z)

H1 output = ReLU(z1) = ________

Show your reasoning: is z1 positive or negative?

### Step 3: Compute the Pre-Activation Value for H2 (8 points)

z2 = (x1 x w(x1 to H2)) + (x2 x w(x2 to H2)) + (x3 x w(x3 to H2)) + b2

Show each multiplication, the sum, and the final result.

**Your calculation:**

(0.5 x -0.3) = ________

(1.0 x 0.7) = ________

(-0.5 x 0.2) = ________

Bias = ________

z2 = ________

### Step 4: Apply ReLU to Get H2 Output (4 points)

H2 output = ReLU(z2) = ________

Show your reasoning.

### Step 5: Compute the Pre-Activation Value for Output Neuron O (8 points)

z_out = (H1 output x w(H1 to O)) + (H2 output x w(H2 to O)) + b_out

Show each multiplication, the sum, and the final result.

**Your calculation:**

(H1 output x 0.9) = ________

(H2 output x -0.5) = ________

Bias = ________

z_out = ________

### Step 6: Apply Sigmoid to Get the Final Prediction (6 points)

Sigmoid(z) = 1 / (1 + e^(-z))

Use a calculator. Round to four decimal places.

O output = Sigmoid(z_out) = ________

Show your calculation including the value of e^(-z_out).

### Step 7: Interpretation (12 points)

Answer each question in complete sentences.

**Question A:** The network is a binary classifier where output above 0.5 predicts class 1 (positive) and below 0.5 predicts class 0 (negative). What is the network's classification decision for this input? Does the network appear confident in its prediction?

**Your answer:** ________

**Question B:** The true label for this training example is 1 (positive). Using binary cross-entropy loss, a high-confidence wrong prediction incurs much greater loss than a low-confidence wrong prediction. Based on your output value, would this example contribute significant loss to the training process? Explain.

Binary cross-entropy loss = -[y x log(p) + (1-y) x log(1-p)], where y is the true label (0 or 1) and p is the predicted probability.

**Your answer:** ________

**Question C:** If the network made this same prediction on many training examples with the same true label, what would happen to the weights during backpropagation? Would the weights connected to neurons that contributed most to this prediction increase or decrease?

**Your answer:** ________

---

## Part B: Activation Function Identification (15 points)

For each scenario, identify the most appropriate activation function for the specified layer from these options: ReLU, Sigmoid, Softmax, Linear (no activation function).

Each function may be used more than once.

### Scenario 8

A neural network that classifies email as spam or not spam. Which activation function should be used at the output layer?

**Answer:** ________
**Justification:** ________

### Scenario 9

A neural network with six hidden layers that predicts housing prices. Which activation function should be used for all hidden layers?

**Answer:** ________
**Justification:** ________

### Scenario 10

A neural network that classifies images of handwritten digits into one of ten categories (0 through 9). Which activation function should be used at the output layer?

**Answer:** ________
**Justification:** ________

### Scenario 11

A neural network that predicts the exact temperature in Fahrenheit for the next 24 hours. Which activation function should be used at the output layer?

**Answer:** ________
**Justification:** ________

### Scenario 12

A very deep CNN (50 hidden layers) for medical image classification. Why would using Sigmoid in all hidden layers likely cause training to fail, and why is ReLU preferred?

**Answer:** ________

---

## Part C: Architecture Matching (20 points)

For each scenario, identify the most appropriate deep learning architecture from the following options: Feedforward Neural Network (MLP), Convolutional Neural Network (CNN), Recurrent Neural Network / LSTM, Transformer.

Each architecture may be used at most twice.

### Scenario 13

A streaming platform wants to generate automatic subtitles by converting spoken audio from video files into text in real time.

**Architecture:** ________
**Justification:** ________

### Scenario 14

An autonomous vehicle system needs to identify pedestrians, stop signs, and lane markings from camera images in real time.

**Architecture:** ________
**Justification:** ________

### Scenario 15

A financial institution wants to analyze 10 years of daily stock price history to predict the next day's closing price.

**Architecture:** ________
**Justification:** ________

### Scenario 16

A customer analytics team has structured tabular data with 50 features per customer — no images, no text, no time series — and wants to predict churn probability. They have 500,000 labeled records.

**Architecture:** ________
**Justification:** ________

---

## Part D: Deep Learning Concepts (15 points)

Answer each question in two to four complete sentences.

### Question 17

Why does deep learning require significantly more training data than traditional machine learning algorithms like logistic regression?

**Your answer:** ________

### Question 18

A company wants to build a custom image classifier to identify defects on a manufacturing line. They have only 200 labeled images. Explain how transfer learning makes this feasible and describe which part of the pretrained model would be fine-tuned.

**Your answer:** ________

### Question 19

A deep neural network with 30 hidden layers achieves 99% accuracy on the training set but only 67% on the test set. A colleague suggests adding 10 more layers to improve generalization. Evaluate this suggestion.

**Your answer:** ________

---

## Answer Key and Grading Rubric

### Part A Answer Key (50 points)

**Step 1 — z1 calculation:**

(0.5 x 0.8) = 0.40
(1.0 x -0.4) = -0.40
(-0.5 x 0.6) = -0.30
Bias = 0.10
z1 = 0.40 + (-0.40) + (-0.30) + 0.10 = -0.20

**Step 2 — H1 output:** ReLU(-0.20) = max(0, -0.20) = 0.00. z1 is negative, so ReLU outputs 0.

**Step 3 — z2 calculation:**

(0.5 x -0.3) = -0.15
(1.0 x 0.7) = 0.70
(-0.5 x 0.2) = -0.10
Bias = -0.20
z2 = -0.15 + 0.70 + (-0.10) + (-0.20) = 0.25

**Step 4 — H2 output:** ReLU(0.25) = 0.25. z2 is positive, so ReLU passes through the value.

**Step 5 — z_out calculation:**

(0.00 x 0.9) = 0.00
(0.25 x -0.5) = -0.125
Bias = 0.00
z_out = 0.00 + (-0.125) + 0.00 = -0.125

**Step 6 — Final output:** Sigmoid(-0.125) = 1 / (1 + e^(0.125)) = 1 / (1 + 1.1331) = 1 / 2.1331 = approximately 0.4688

Scoring Steps 1-6: 8+4+8+4+8+6 = 38 points. Accept values within rounding tolerance of plus or minus 0.005.

**Step 7 Answers:**

Q A: The network predicts class 0 (negative) since 0.4688 < 0.5. The prediction is not confident — 0.4688 is very close to the 0.5 decision boundary, indicating near-equal probability for both classes.

Q B: The true label is 1 but the prediction is approximately 0.47. Loss = -[1 x log(0.47) + 0] = -log(0.47) = approximately 0.755. This is moderate loss — not catastrophically wrong but not trivially small.

Q C: During backpropagation, gradients would flow back to update weights. Weights that contributed to the incorrect prediction would be adjusted to reduce the loss. Since H1 output was 0 (ReLU killed it), its upstream weights would have zero gradient and would not change in this example — demonstrating the ReLU "dying neuron" concept.

Step 7 scoring: Q A = 4 pts, Q B = 4 pts, Q C = 4 pts = 12 pts.

### Part B (3 points per scenario = 15 points)

Scenario 8: Sigmoid. Binary classification output requires a probability between 0 and 1.

Scenario 9: ReLU. Standard choice for hidden layers in deep networks; fast and effective.

Scenario 10: Softmax. Multi-class (10 classes) output — softmax produces probabilities summing to 1.

Scenario 11: Linear (no activation). Regression output should be unbounded to predict any temperature value.

Scenario 12: Sigmoid in deep hidden layers causes the vanishing gradient problem — gradients become exponentially small as they propagate backward, stalling learning. ReLU's non-saturating gradient solves this.

### Part C (5 points per scenario = 20 points)

Scenario 13: RNN/LSTM. Audio is a time series; sequential models capture temporal context in speech.

Scenario 14: CNN. Image data with spatial structure requires convolutional layers.

Scenario 15: RNN/LSTM. Sequential time series prediction requires a model that captures temporal dependencies.

Scenario 16: Feedforward Neural Network (MLP). Structured tabular data with no spatial or temporal structure.

### Part D (5 points per question = 15 points)

Q17: Deep networks have millions of parameters. Each parameter needs sufficient training examples to be estimated reliably. With too few examples, the network memorizes training data rather than generalizing. Traditional algorithms like logistic regression have far fewer parameters and can generalize from smaller datasets.

Q18: Transfer learning uses a CNN pretrained on millions of images (such as ImageNet). The early and middle layers already detect general visual features. Only the final classification layers are fine-tuned on the 200 defect images. This requires much less data and compute than training from scratch.

Q19: This is a poor suggestion. Adding more layers will increase overfitting, not reduce it. The model already overfits at 30 layers. Remedies include dropout regularization, data augmentation to increase the training set size, early stopping, or reducing the network depth.

---

## Deliverable

Submit a single document (PDF or Word) showing all calculations in Part A with intermediate steps, your answers to all scenarios and questions, and your name, course section, and date at the top. Upload to the Module 04 Lab Assignment in Canvas by the posted due date.

## Part 9 — Challenge Exercise

### Challenge 1: Activation Function Comparison

1. Using Python and numpy, implement the sigmoid, tanh, and ReLU activation functions from scratch (no sklearn or torch). For each, write a single function that accepts a numpy array and returns the transformed values.
2. Generate an input array from -5 to 5 in steps of 0.1 using `numpy.arange`. Apply all three functions and plot the outputs on the same graph using matplotlib, with each function in a different color and a legend.
3. Identify the input range where sigmoid and tanh produce near-zero gradients (the "saturation zone"). Explain in two sentences why this saturation zone causes the vanishing gradient problem in deep networks.
4. Explain in two sentences why ReLU became the default hidden-layer activation despite its "dying ReLU" limitation where neurons can permanently output zero.

### Challenge 2: Build and Train a Simple MLP on the Iris Dataset

1. Using scikit-learn, load the `iris` dataset and split it into 70% training / 30% test using `train_test_split` with `random_state=42`.
2. Train a `MLPClassifier` with one hidden layer of 10 neurons, `max_iter=500`, and `random_state=42`. Report test accuracy.
3. Experiment with two architectural changes: (a) add a second hidden layer of 10 neurons, and (b) increase the first hidden layer to 50 neurons. Train and report test accuracy for each variant.
4. Apply dropout regularization by setting `alpha=0.01` (L2 penalty in scikit-learn's MLP) on the best-performing architecture. Report whether regularization improved or changed test accuracy.

### Reflection Questions

1. Based on Challenge 1, explain to a student who has not taken this course why a neural network with only linear activations (no sigmoid, tanh, or ReLU) cannot learn non-linear patterns like the XOR function.
2. In Challenge 2, if your MLP achieved high training accuracy but low test accuracy, which techniques from Module 04 would you apply first, and in what order would you try them?

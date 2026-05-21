# Quiz: Module 04 - Neural Networks: Perceptrons and Backpropagation
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
Which mathematical rule does backpropagation use to compute gradients through stacked layers?
*   A) Product Rule — differentiates products of two functions
*   B) Quotient Rule — differentiates ratios of two functions
*   C) Chain Rule — differentiates composed functions by multiplying local gradients layer by layer
*   D) Power Rule — differentiates polynomial terms raised to a constant exponent
*   **Correct Answer:** C) Backpropagation computes gradients of the loss with respect to each weight by repeatedly applying the Chain Rule through composed layer functions.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The Product Rule applies to products of two independent functions, not compositions of nested layers.
    *   *Why B is incorrect:* The Quotient Rule applies to ratios and is not the mechanism for propagating gradients through sequential layers.
    *   *Why C is correct:* Each layer is a function of the previous layer's output. The Chain Rule allows backpropagation to compute d(Loss)/d(w) for any weight w by multiplying gradients from output to that layer.
    *   *Why D is incorrect:* The Power Rule handles single polynomial terms and has no direct role in multi-layer gradient computation.

---

**Question 2**
Which of the following is the most accurate definition of **backpropagation** in a neural network?
*   A) A technique that randomly deactivates neurons during training to prevent any single neuron from dominating, forcing the network to learn redundant representations.
*   B) An algorithm that computes the gradient of the loss with respect to every weight in the network by propagating error signals backwards from the output layer using the chain rule, enabling gradient descent weight updates.
*   C) A preprocessing step that normalizes input features to zero mean and unit variance before they are fed into the network's first layer.
*   D) A regularization method that adds a penalty term proportional to weight magnitudes to the loss function, discouraging large weight values.
*   **Correct Answer:** B) Backpropagation computes gradients layer by layer from output to input, enabling the optimizer to update every weight to reduce the loss.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes Dropout regularization, not backpropagation.
    *   *Why B is correct:* Backpropagation is the gradient computation algorithm — it does not update weights itself, but provides the gradients that the optimizer (Adam, SGD) uses to update weights.
    *   *Why C is incorrect:* This describes feature standardization (z-score normalization), a data preprocessing step independent of backpropagation.
    *   *Why D is incorrect:* This describes L1 or L2 regularization, which modifies the loss function — it is distinct from the backpropagation gradient computation process.

---

**Question 3**
A developer needs to **build a two-layer neural network for binary classification** in Keras. Which code is correct?
*   A) `model = tf.keras.Sequential([tf.keras.layers.Dense(64, activation='relu'), tf.keras.layers.Dense(1, activation='sigmoid')])`
*   B) `model = tf.keras.Sequential([tf.keras.layers.Dense(64, activation='softmax'), tf.keras.layers.Dense(10)])`
*   C) `model = tf.keras.Sequential([tf.keras.layers.Conv2D(32, (3,3)), tf.keras.layers.Dense(1)])`
*   D) `model = tf.keras.Sequential([tf.keras.layers.LSTM(64), tf.keras.layers.Dense(1, activation='relu')])`
*   **Correct Answer:** A) A hidden Dense layer with ReLU followed by a sigmoid output layer is the correct Keras pattern for binary classification.
*   **Distractor Analysis:**
    *   *Why A is correct:* ReLU in the hidden layer introduces non-linearity; sigmoid in the output layer produces a binary probability. Compile with `loss='binary_crossentropy'`.
    *   *Why B is incorrect:* Softmax in a hidden layer and a raw linear output of 10 units is suited for multi-class classification, not binary.
    *   *Why C is incorrect:* Conv2D is a convolutional layer designed for image input (3D tensors), not tabular binary classification.
    *   *Why D is incorrect:* LSTM is a recurrent layer designed for sequential data; using ReLU for a binary output produces unbounded outputs that cannot represent probabilities.

---

**Question 4**
Why is ReLU (Rectified Linear Unit) preferred over sigmoid activation in hidden layers of deep networks?
*   A) ReLU always outputs a probability between 0 and 1, making it easier to interpret.
*   B) ReLU has a constant gradient of 1 for positive inputs, avoiding the vanishing gradient problem that slows sigmoid-based networks.
*   C) ReLU normalizes outputs to sum to 1 across all neurons in a layer.
*   D) ReLU adds a regularization penalty to the loss function automatically.
*   **Correct Answer:** B) Sigmoid saturates near 0 and 1, producing near-zero gradients that slow backpropagation through deep networks. ReLU's constant gradient for positive inputs keeps gradients flowing.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* ReLU outputs max(0, x), which is unbounded above zero — it does not produce probabilities. Sigmoid produces probabilities.
    *   *Why B is correct:* The vanishing gradient problem causes weights in early layers to receive negligible gradient updates when sigmoid saturates. ReLU avoids this for positive activations.
    *   *Why C is incorrect:* Softmax normalizes outputs to sum to 1 across classes. ReLU makes no such normalization.
    *   *Why D is incorrect:* ReLU is purely an activation function — it applies no regularization penalty to the loss.

---

**Question 5**
A neural network trained for 50 epochs shows training loss of 0.05 but validation loss of 1.82. What is the most likely problem and best corrective action?
*   A) Underfitting — add more layers and neurons to increase model capacity.
*   B) Overfitting — apply dropout, L2 regularization, or early stopping to improve generalization.
*   C) Vanishing gradients — switch from Adam optimizer to SGD to improve gradient flow.
*   D) Data leakage — re-split the dataset using a different random seed.
*   **Correct Answer:** B) A large gap between training loss and validation loss is the canonical overfitting signature — the model memorized training data rather than learning generalizable patterns.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Underfitting produces high loss on both training and validation sets. Low training loss rules out underfitting.
    *   *Why B is correct:* Standard remedies include: `Dropout(0.5)` layers, `kernel_regularizer=tf.keras.regularizers.l2(0.01)`, `EarlyStopping(monitor='val_loss')`, or collecting more training data.
    *   *Why C is incorrect:* Vanishing gradients would cause training loss to plateau at a high value — not drop to 0.05. The optimizer choice does not explain this specific gap pattern.
    *   *Why D is incorrect:* Data leakage would inflate validation performance (make it look too good), not inflate validation loss.

# Quiz: Module 08 - Azure Machine Learning Studio
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

**Question 1**
What activation function is typically used in the hidden layers of modern neural networks to prevent vanishing gradients?
*   A) Sigmoid
*   B) Rectified Linear Unit (ReLU)
*   C) Tanh
*   D) Step function
*   **Correct Answer:** B) ReLU outputs max(0, x) — it passes positive values unchanged and zeros out negatives, which prevents vanishing gradients and speeds up training in deep networks.
*   **Distractor Analysis:**
    *   *Why correct:* ReLU avoids the saturation problem of Sigmoid and Tanh, where gradients shrink toward zero and prevent earlier layers from learning effectively.
    *   Sigmoid and Tanh both saturate (output near 0 or ±1) for large inputs, causing vanishing gradients. The step function is non-differentiable and cannot be used with backpropagation.

---

**Question 2**
In the context of neural network training, which of the following is the most accurate definition of **backpropagation**?
*   A) An algorithm that calculates the gradient of the loss function with respect to each network weight by propagating the error signal backward from the output layer, then uses gradient descent to update the weights and reduce prediction error.
*   B) A no-code Azure Machine Learning feature that automatically evaluates multiple algorithms and hyperparameter combinations to find the best-performing model for a given dataset and task.
*   C) A preprocessing technique that transforms numeric input features to a comparable scale (0–1 or zero mean/unit variance) so that distance-based and gradient-based algorithms converge correctly.
*   D) A regularization method that randomly drops a fraction of neurons during each training step to prevent co-adaptation and reduce overfitting in deep neural networks.
*   **Correct Answer:** A) An algorithm that calculates the gradient of the loss function with respect to each network weight by propagating the error signal backward from the output layer, then uses gradient descent to update the weights and reduce prediction error.
*   **Distractor Analysis:**
    *   *Why A is correct:* Backpropagation is the core training algorithm for neural networks — it computes per-weight gradients efficiently using the chain rule of calculus, enabling gradient descent to adjust every weight in the network.
    *   *Why B is incorrect:* This describes Azure AutoML — a cloud platform feature, not the neural network training algorithm.
    *   *Why C is incorrect:* This describes feature scaling (normalization/standardization) — a data preprocessing step, not the backpropagation learning algorithm.
    *   *Why D is incorrect:* This describes Dropout regularization — a technique to prevent overfitting, not the mechanism by which a network learns from errors.

---

**Question 3**
A developer needs to **train a machine learning model on labeled training data**. Which command is most appropriate?
*   A) model.fit(X_train, y_train)
*   B) predictions = model.predict(X_test)
*   C) accuracy = accuracy_score(y_test, predictions)
*   D) import pandas as pd; df = pd.read_csv('data.csv')
*   **Correct Answer:** A) model.fit(X_train, y_train)
*   **Distractor Analysis:**
    *   *Why A is correct:* `model.fit(X_train, y_train)` passes the feature matrix and target labels to the model, allowing it to learn the mapping between inputs and outputs.
    *   *Why B is incorrect:* `model.predict()` generates predictions from a trained model; the model must be fitted first before it can predict.
    *   *Why C is incorrect:* `accuracy_score()` evaluates predictions against true labels — it is an evaluation step, not a training step.
    *   *Why D is incorrect:* This loads a CSV file into a DataFrame — data loading, not model training.

---

**Question 4**
A neural network's validation loss is significantly higher than its training loss after many epochs. The model performs well on training data but poorly on unseen examples. Which action most directly resolves this?
*   A) Apply regularization (L1/L2 or Dropout), reduce the number of hidden layers or neurons, or gather more training data to improve generalization.
*   B) Ensure preprocessing scalers are fitted only on training data, then applied to test data to prevent data leakage.
*   C) Use mean or median imputation to fill missing values in the dataset before retraining.
*   D) Reboot the training environment and reinitialize the model weights from scratch.
*   **Correct Answer:** A) Apply regularization (L1/L2 or Dropout), reduce the number of hidden layers or neurons, or gather more training data to improve generalization.
*   **Distractor Analysis:**
    *   *Why A is correct:* A large gap between training loss and validation loss is the hallmark of overfitting — the model has memorized training data rather than learning generalizable patterns. Regularization, architecture simplification, and more data all reduce overfitting.
    *   *Why B is incorrect:* Preventing data leakage addresses inflated validation scores from improper preprocessing — the opposite problem (validation appears too good, not too bad).
    *   *Why C is incorrect:* Missing value imputation resolves NaN errors; it does not address high model variance from overfitting.
    *   *Why D is incorrect:* Rebooting and reinitializing weights would simply restart the same overfitting process; it does not change the model's capacity or the training data.

---

**Question 5**
Attackers are sending images with imperceptible pixel-level perturbations to a deployed Azure Custom Vision model, causing safety equipment to be misclassified as absent. Which defense best mitigates this **adversarial example** attack?
*   A) Train the model with adversarial examples included in the training set and implement input validation and filtering before inference.
*   B) Apply differential privacy to the training data and rate-limit the public inference API.
*   C) Enable full disk encryption on all client endpoints submitting images to the API.
*   D) Store model weights in an Azure Key Vault and rotate the inference API key on a 90-day schedule.
*   **Correct Answer:** A) Train the model with adversarial examples included in the training set and implement input validation and filtering before inference.
*   **Distractor Analysis:**
    *   *Why A is correct:* Adversarial training exposes the model to perturbed inputs during training, building robustness to crafted noise. Input filtering can also detect statistically anomalous images before they reach the model.
    *   *Why B is incorrect:* Differential privacy defends against model inversion attacks (training data reconstruction from outputs) — not adversarial perturbations applied at inference time.
    *   *Why C is incorrect:* Disk encryption protects data at rest; it has no effect on manipulated image payloads submitted through a live API.
    *   *Why D is incorrect:* Securing model weights and rotating API keys protect the pipeline's access controls but do not make the model robust against crafted adversarial inputs from authorized users or compromised systems.

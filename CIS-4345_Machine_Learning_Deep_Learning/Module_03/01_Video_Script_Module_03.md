# Video Script: Module 03 - Linear and Logistic Regression

**Course:** CIS-4345 Machine Learning and Deep Learning

**Institution:** Texas Wesleyan University

**Instructor:** Professor Nash

**Estimated Duration:** 20-24 minutes

**TensorFlow Developer Certificate Alignment:** Regression with Dense layers, Binary Classification, Loss Functions, Gradient Descent

---

## [00:00 - 01:30] Opening and Module Overview

**[VISUAL: Title card — "Module 03: Linear and Logistic Regression | CIS-4345 | Professor Nash"]**

Welcome back. I'm Professor Nash, and this is Module 03 — Linear and Logistic Regression.

We are building toward neural networks, and to do that effectively you need to understand the simplest members of the neural network family first. A single-neuron neural network with no activation function is literally a linear regression model. A single-neuron network with a sigmoid activation is a logistic regression model. Understanding these models mathematically — their cost functions, their optimization procedures, their decision boundaries — gives you a mental model for everything that follows.

Today we cover four topics. First, linear regression: the math of fitting a weighted sum to continuous targets, the MSE loss function, and gradient descent. Second, logistic regression: the sigmoid activation, binary cross-entropy loss, and classification thresholds. Third, regularization: L1 and L2 penalties that prevent overfitting. Fourth, implementation in both scikit-learn and TensorFlow/Keras so you can see the direct correspondence between classical ML and neural networks.

By the end of this module you will understand not just how to run these models but why they work — and why that understanding matters when you are debugging a neural network on the certification exam.

---

## [01:30 - 06:00] Linear Regression: The Math

**[VISUAL: Slide — "Linear Regression: Fitting a Weighted Sum to Continuous Targets"]**

Linear regression models the relationship between an input feature vector X and a continuous target y as a linear function:

y-hat = w_1*x_1 + w_2*x_2 + ... + w_p*x_p + b

In matrix form: y-hat = X @ w + b, where w is the weight vector and b is the bias term. The model has no activation function — the output is the raw linear combination.

**[VISUAL: Diagram — scatter plot with a line, vertical dotted residual lines from each point to the line]**

The prediction error for a single sample is the residual: y_i minus y-hat_i. The goal of training is to find w and b that minimize the sum of squared residuals across all training samples.

**[SHOW CODE]**

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data: y = 3x + 5 + noise
np.random.seed(42)
X = np.random.randn(200, 1).astype(np.float32)
y = (3.0 * X.squeeze() + 5.0
     + np.random.randn(200).astype(np.float32) * 0.5)

plt.scatter(X, y, alpha=0.4, s=15)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Synthetic Regression Data: y = 3x + 5 + noise")
plt.tight_layout()
plt.show()
```

The loss function for linear regression is Mean Squared Error:

MSE = (1/n) * sum((y_i - y-hat_i)^2)

Squaring makes all residuals positive so negative and positive errors do not cancel. Squaring also penalizes large errors more than small ones — a prediction that is off by 10 is penalized 100 times as much as one that is off by 1.

---

## [06:00 - 10:30] Gradient Descent and the Training Loop

**[VISUAL: Slide — "Gradient Descent: Walking Down the Loss Surface"]**

Gradient descent is the optimization algorithm that trains virtually every neural network. The algorithm repeats three steps for each training iteration:

Step 1 — Forward pass: compute predictions y-hat = X @ w + b.

Step 2 — Compute loss: calculate MSE between y-hat and y.

Step 3 — Backward pass: compute the gradient of the loss with respect to every weight. Update each weight by subtracting the learning rate times the gradient.

**[SHOW CODE]**

```python
# Manual gradient descent — illustrative only
np.random.seed(0)
w = np.array([0.0], dtype=np.float32)
b = np.array([0.0], dtype=np.float32)
lr = 0.1

for epoch in range(100):
    y_hat = X.squeeze() * w[0] + b[0]
    loss  = np.mean((y - y_hat) ** 2)
    dw    = -2 * np.mean((y - y_hat) * X.squeeze())
    db    = -2 * np.mean(y - y_hat)
    w[0] -= lr * dw
    b[0] -= lr * db
    if epoch % 20 == 0:
        print(f"Epoch {epoch:3d} | Loss: {loss:.4f} | w: {w[0]:.3f} | b: {b[0]:.3f}")

print(f"\nLearned: w={w[0]:.3f} (true: 3.0), b={b[0]:.3f} (true: 5.0)")
```

**[VISUAL: Parabolic loss curve, ball rolling down to minimum, labeled gradient steps]**

The learning rate controls the step size. Too large and the weights overshoot the minimum. Too small and training converges slowly. Adam adapts the learning rate per parameter automatically, which is why it is the default optimizer in Keras.

---

## [10:30 - 14:30] Logistic Regression: Classification with Sigmoid

**[VISUAL: Slide — "Logistic Regression: Linear Model Plus Sigmoid Activation"]**

Logistic regression extends the linear model with a sigmoid activation that squashes the output to the range (0, 1):

sigmoid(z) = 1 / (1 + e^(-z))     where z = w^T * x + b

**[SHOW CODE]**

```python
z = np.linspace(-6, 6, 200)
sigma = 1 / (1 + np.exp(-z))

plt.figure(figsize=(7, 4))
plt.plot(z, sigma, lw=2, color="steelblue")
plt.axhline(0.5, color="red", linestyle="--", label="Threshold = 0.5")
plt.xlabel("z")
plt.ylabel("sigmoid(z)")
plt.title("Sigmoid Activation Function")
plt.legend()
plt.tight_layout()
plt.show()
```

**[VISUAL: S-curve with red threshold line, labels "Predict class 1" above and "Predict class 0" below]**

The sigmoid output is a probability estimate. The default threshold is 0.5. If the output exceeds 0.5, predict class 1; otherwise predict class 0. The threshold can be adjusted — we revisit this in Module 11 when we cover ROC curves.

The loss function is binary cross-entropy:

`BCE = -(1/n) * sum( yi*log(yhati) + (1-yi)*log(1-yhati) )`

This function heavily penalizes confident wrong predictions. Predicting 0.01 when the true label is 1 produces loss of -log(0.01) = 4.6. Predicting 0.99 when the true label is 1 produces loss of -log(0.99) = 0.01.

---

## [14:30 - 18:00] Regularization: L1 and L2 Penalties

**[VISUAL: Slide — "Regularization: Penalizing Large Weights"]**

Regularization adds a penalty term to the loss function to discourage large weights and reduce overfitting.

L2 regularization (Ridge): Loss = MSE + lambda * sum(w_i^2). L2 shrinks weights toward zero but never exactly to zero. It is the default choice.

L1 regularization (Lasso): Loss = MSE + lambda * sum(|w_i|). L1 can shrink weights to exactly zero, effectively performing feature selection.

**[SHOW CODE]**

```python
from sklearn.linear_model import Ridge, Lasso, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler  = StandardScaler()
Xtr     = scaler.fit_transform(X_train)
Xte     = scaler.transform(X_test)

# Ridge (L2)
ridge = Ridge(alpha=1.0)
ridge.fit(Xtr, y_train)
print("Ridge R2:", ridge.score(Xte, y_test))

# Lasso (L1)
lasso = Lasso(alpha=0.01)
lasso.fit(Xtr, y_train)
print("Lasso R2:", lasso.score(Xte, y_test))
print("Nonzero Lasso coefficients:", np.sum(lasso.coef_ != 0))
```

In scikit-learn `LogisticRegression`, the parameter `C` is the inverse of regularization strength — smaller C means stronger regularization. This is the opposite sign convention from Ridge and Lasso, which trips up beginners.

---

## [18:00 - 21:30] Both Models in TensorFlow/Keras

**[VISUAL: Slide — "Single-Neuron Networks = Classical Models"]**

**[SHOW CODE]**

```python
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

# --- Regression setup ---
X_r = X; y_r = y
Xr_tr, Xr_te, yr_tr, yr_te = train_test_split(X_r, y_r, test_size=0.2)
sc_r = StandardScaler()
Xr_tr = sc_r.fit_transform(Xr_tr); Xr_te = sc_r.transform(Xr_te)

# --- Keras Linear Regression (no activation = linear) ---
lin_model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(Xr_tr.shape[1],))
])
lin_model.compile(optimizer="adam", loss="mse", metrics=["mae"])
lin_model.fit(Xr_tr, yr_tr, epochs=100, validation_split=0.2, verbose=0)
print("LinReg MAE:", lin_model.evaluate(Xr_te, yr_te, verbose=0)[1])

# --- Classification setup ---
X_c, y_c = make_classification(n_samples=1000, n_features=10, random_state=42)
Xc_tr, Xc_te, yc_tr, yc_te = train_test_split(X_c, y_c, test_size=0.2)
sc_c = StandardScaler()
Xc_tr = sc_c.fit_transform(Xc_tr).astype("float32")
Xc_te = sc_c.transform(Xc_te).astype("float32")

# --- Keras Logistic Regression (sigmoid activation) ---
log_model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, activation="sigmoid",
                          input_shape=(Xc_tr.shape[1],))
])
log_model.compile(optimizer="adam",
                  loss="binary_crossentropy",
                  metrics=["accuracy"])
log_model.fit(Xc_tr, yc_tr, epochs=50, validation_split=0.2, verbose=0)
print("LogReg Acc:", log_model.evaluate(Xc_te, yc_te, verbose=0)[1])
```

**[VISUAL: Two architecture diagrams — Dense(1) linear vs Dense(1, sigmoid)]**

These are complete Keras models. You compile them, fit them, evaluate them, and access their training history — identical to 10-layer networks later in the course. The architecture knowledge transfers directly.

---

## [21:30 - 23:30] Module Summary and Lab Preview

**[VISUAL: Slide — "Module 03 Key Takeaways"]**

To consolidate: linear regression fits a weighted sum to continuous targets using MSE loss. Logistic regression adds a sigmoid activation and uses binary cross-entropy for binary classification. Gradient descent minimizes the loss by iteratively updating weights in the direction of the negative gradient. L1 and L2 regularization penalize large weights to prevent overfitting. Both models are directly expressible as single-neuron Keras networks.

The Module 03 lab has you implement both models in scikit-learn and Keras, compare their outputs on the same dataset, experiment with regularization strength, and analyze training curves. Focus on the lab section that has you vary the learning rate — watching the training dynamics respond builds critical intuition for all future model training.

See you in Module 04, where we stack layers into multi-neuron networks and derive backpropagation.

---

## Certification Alignment Notes

Binary classification with `sigmoid` activation and `binary_crossentropy` loss is among the most frequently tested patterns on the TensorFlow Developer Certificate exam. Understanding when to use `sigmoid` vs `softmax` — and `binary_crossentropy` vs `sparse_categorical_crossentropy` — is essential. Verify current exam objectives at tensorflow.org/certificate.

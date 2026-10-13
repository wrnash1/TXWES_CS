# Lab: Module 04 — Neural Networks and Deep Learning Foundations

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Lab Overview

In this lab you will implement a two-layer neural network from scratch in NumPy, then replicate the exact same architecture in TensorFlow/Keras and verify that the predictions match. This exercise connects the mathematical foundations from the lecture directly to the framework code you will write all semester.

**Estimated Time:** 60–90 minutes

**Tools Required:** Python 3.9+, NumPy, TensorFlow 2.x, Google Colab or local Jupyter environment

---

## Learning Objectives

By the end of this lab you will be able to:

- Implement forward propagation manually using matrix operations
- Identify the role of weights, biases, and activation functions in layer computation
- Construct an equivalent Keras Sequential model and verify matching outputs
- Use `tf.GradientTape` to compute gradients manually for a simple network
- Interpret `model.summary()` output and calculate parameter counts by hand

---

## Part 1 — NumPy Forward Propagation

### Step 1.1 — Environment Setup

Open a new Colab notebook or Jupyter file. Run the following setup cell first.

```python
import numpy as np
import tensorflow as tf

print("NumPy version:", np.__version__)
print("TensorFlow version:", tf.__version__)

# Set seeds for reproducibility
np.random.seed(42)
tf.random.set_seed(42)
```

Expected output: TensorFlow version should be 2.x (2.12 or later).

### Step 1.2 — Define Fixed Weights

We will use fixed weights so both the NumPy and Keras implementations produce identical results.

```python
# Layer 1: 4 neurons, 3 inputs
W1 = np.array([
    [ 0.5, -0.3,  0.2],
    [ 0.1,  0.8, -0.4],
    [-0.2,  0.3,  0.7],
    [ 0.6, -0.1,  0.4]
], dtype=np.float32)
b1 = np.array([0.1, -0.1, 0.2, 0.0], dtype=np.float32)

# Layer 2: 1 output neuron, 4 inputs
W2 = np.array([[0.7, -0.5, 0.3, 0.1]], dtype=np.float32)
b2 = np.array([0.05], dtype=np.float32)

# Sample input: 3 features
X = np.array([[1.0, 0.5, -0.3]], dtype=np.float32)  # shape (1, 3)
y_true = np.array([[1.0]], dtype=np.float32)
```

### Step 1.3 — Implement Activation Functions

```python
def relu_np(z):
    return np.maximum(0, z)

def sigmoid_np(z):
    return 1.0 / (1.0 + np.exp(-z))
```

### Step 1.4 — Manual Forward Pass

```python
# Layer 1 forward
z1 = X @ W1.T + b1           # shape: (1, 4)
a1 = relu_np(z1)              # shape: (1, 4)

# Layer 2 forward
z2 = a1 @ W2.T + b2           # shape: (1, 1)
y_hat_numpy = sigmoid_np(z2)  # shape: (1, 1)

print("Layer 1 pre-activation (z1):", z1)
print("Layer 1 activation (a1):", a1)
print("Layer 2 pre-activation (z2):", z2)
print("Output prediction (numpy):", y_hat_numpy)
```

**Checkpoint:** Write down the value of `y_hat_numpy`. You will compare this to the Keras prediction in Part 2.

---

## Part 2 — Keras Equivalent Network

### Step 2.1 — Build the Sequential Model

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation='relu', input_shape=(3,), name='layer1'),
    tf.keras.layers.Dense(1, activation='sigmoid', name='output')
])

model.summary()
```

**Exercise:** Before running `model.summary()`, calculate the expected parameter count for each layer by hand.

- Layer 1 parameters: `(input_dim + 1) * units` = `(3 + 1) * 4` = 16
- Layer 2 parameters: `(4 + 1) * 1` = 5
- Total: 21 parameters

Verify that `model.summary()` reports these same numbers.

### Step 2.2 — Load the Fixed Weights

To get identical predictions, we set the Keras model weights to match our NumPy arrays.

```python
model.layers[0].set_weights([W1.T, b1])   # Keras Dense stores W as (input, output)
model.layers[1].set_weights([W2.T, b2])

# Verify weights were set correctly
print("Layer 1 weights shape:", model.layers[0].get_weights()[0].shape)
print("Layer 2 weights shape:", model.layers[1].get_weights()[0].shape)
```

Note: Keras Dense layers store the weight matrix transposed relative to our NumPy convention. The `set_weights` call handles this by passing `W1.T`.

### Step 2.3 — Run Prediction and Compare

```python
y_hat_keras = model.predict(X, verbose=0)
print("Output prediction (keras):", y_hat_keras)
print("NumPy prediction:  ", y_hat_numpy)
print("Difference:", np.abs(y_hat_keras - y_hat_numpy))
```

**Expected result:** The difference should be less than `1e-6` (floating point rounding only). If it is larger, check the weight transposition in Step 2.2.

---

## Part 3 — Loss Functions

### Step 3.1 — Compute Binary Cross-Entropy Manually

```python
eps = 1e-7  # prevent log(0)
y_hat_clip = np.clip(y_hat_numpy, eps, 1 - eps)
bce_manual = -(y_true * np.log(y_hat_clip) + (1 - y_true) * np.log(1 - y_hat_clip))
print("Manual BCE loss:", bce_manual[0][0])
```

### Step 3.2 — Compute with Keras

```python
bce_fn = tf.keras.losses.BinaryCrossentropy()
bce_keras = bce_fn(y_true, y_hat_keras).numpy()
print("Keras BCE loss:", bce_keras)
```

**Checkpoint:** Both loss values should match within floating point tolerance.

---

## Part 4 — GradientTape and Backpropagation

### Step 4.1 — Compute Gradients for a Single Step

```python
# Convert inputs to tensors
x_tensor = tf.constant(X)
y_tensor = tf.constant(y_true)

# Compute loss and gradients
with tf.GradientTape() as tape:
    y_pred = model(x_tensor, training=False)
    loss = tf.keras.losses.binary_crossentropy(y_tensor, y_pred)

gradients = tape.gradient(loss, model.trainable_variables)

for var, grad in zip(model.trainable_variables, gradients):
    print(f"{var.name}: gradient shape {grad.shape}, max abs value {tf.reduce_max(tf.abs(grad)).numpy():.6f}")
```

### Step 4.2 — Reflection Questions

Answer these in a comment block or markdown cell in your notebook:

1. Which layer has the largest gradient magnitudes? What does this suggest about how much that layer is adjusting during training?
2. What would happen to the gradients if you used sigmoid instead of ReLU in the hidden layer with very large or very small z values?
3. Why do we clip the y_hat values before computing log in Step 3.1?

---

## Part 5 — Compile and Train

### Step 5.1 — Generate Training Data

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_data, y_data = make_classification(
    n_samples=1000, n_features=3, n_informative=3,
    n_redundant=0, random_state=42
)
y_data = y_data.astype(np.float32).reshape(-1, 1)

X_train, X_val, y_train, y_val = train_test_split(
    X_data, y_data, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train).astype(np.float32)
X_val = scaler.transform(X_val).astype(np.float32)
```

### Step 5.2 — Build Fresh Model and Train

```python
model2 = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model2.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model2.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=30,
    batch_size=32,
    verbose=1
)
```

### Step 5.3 — Plot Training Curves

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(history.history['loss'], label='Train Loss')
axes[0].plot(history.history['val_loss'], label='Val Loss')
axes[0].set_title('Loss Curves')
axes[0].set_xlabel('Epoch')
axes[0].legend()

axes[1].plot(history.history['accuracy'], label='Train Accuracy')
axes[1].plot(history.history['val_accuracy'], label='Val Accuracy')
axes[1].set_title('Accuracy Curves')
axes[1].set_xlabel('Epoch')
axes[1].legend()

plt.tight_layout()
plt.savefig('module04_training_curves.png', dpi=150)
plt.show()
```

---

## Deliverables

Submit the following to Canvas by the module deadline:

1. Your completed Colab or Jupyter notebook (.ipynb) with all cells executed
2. Screenshot or inline display showing matching NumPy and Keras predictions (Part 2)
3. Screenshot showing matching loss values (Part 3)
4. Written answers to the three reflection questions in Part 4
5. Training curve plot saved as `module04_training_curves.png`

---

## Grading Rubric

| Criterion | Points |
|---|---|
| NumPy forward pass produces correct output and matches Keras | 25 |
| Parameter count calculation matches model.summary() | 10 |
| BCE loss computed manually and matches Keras BinaryCrossentropy | 15 |
| GradientTape cell runs without error, gradients printed | 20 |
| Three reflection questions answered thoughtfully | 15 |
| Training curve plot included and labeled | 10 |
| Notebook executes top-to-bottom without errors | 5 |
| **Total** | **100** |

---

## Common Errors and Fixes

**Shape mismatch in matrix multiply:** Verify that `W1` has shape `(4, 3)` and input `X` has shape `(1, 3)`. Use `X @ W1.T` (not `W1 @ X`) to get shape `(1, 4)`.

**set_weights dimension error:** Keras Dense stores weights as `(input_dim, output_dim)`. If your NumPy weight is `(output, input)`, pass it transposed with `.T`.

**Predictions do not match:** Confirm both models use identical activation functions. A sigmoid in the NumPy code but ReLU in Keras (or vice versa) will produce different outputs.

**sklearn not found:** Run `pip install scikit-learn` in your environment or Colab cell.

---

## Part 9 — Challenge Exercise

### Challenge 1: Visualizing the Effect of Activation Functions on Gradient Flow

Build three identical 5-layer networks differing only in hidden-layer activation (sigmoid, tanh, ReLU) and compare how gradients propagate back to the first layer during training.

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler

X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X = StandardScaler().fit_transform(X).astype(np.float32)
y = y.astype(np.float32)

def build_deep_model(activation):
    return tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation=activation, input_shape=(20,)),
        tf.keras.layers.Dense(64, activation=activation),
        tf.keras.layers.Dense(64, activation=activation),
        tf.keras.layers.Dense(64, activation=activation),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

results = {}
for act in ['sigmoid', 'tanh', 'relu']:
    model = build_deep_model(act)
    model.compile(optimizer='adam', loss='binary_crossentropy')
    X_tf = tf.constant(X)
    y_tf = tf.constant(y)
    with tf.GradientTape() as tape:
        preds = model(X_tf, training=True)
        loss  = tf.reduce_mean(tf.keras.losses.binary_crossentropy(y_tf, tf.squeeze(preds)))
    grads = tape.gradient(loss, model.trainable_variables)
    # Gradient norm for the FIRST layer's weight matrix
    first_layer_grad_norm = tf.norm(grads[0]).numpy()
    results[act] = first_layer_grad_norm
    print(f"{act:8s} | first-layer gradient norm: {first_layer_grad_norm:.6f}")

activations = list(results.keys())
norms = [results[a] for a in activations]
plt.bar(activations, norms, color=['steelblue', 'coral', 'green'])
plt.title('First-Layer Gradient Norm by Activation Function')
plt.ylabel('L2 Norm of Gradient')
plt.tight_layout()
plt.savefig('gradient_norms.png', dpi=100)
plt.show()
```

1. Compare the first-layer gradient norms across the three activations. Which activation gives the largest gradient signal in the first layer?
2. Train each model for 20 epochs and compare final validation accuracy. Does the activation with the largest gradient norm also converge fastest?

### Challenge 2: Custom Training Loop with GradientTape

Implement a full training loop from scratch using `tf.GradientTape` — no `model.fit()` — and verify that training loss decreases correctly.

```python
import tensorflow as tf
import numpy as np

tf.random.set_seed(42)
X_train = tf.constant(X[:800], dtype=tf.float32)
y_train = tf.constant(y[:800], dtype=tf.float32)
X_val   = tf.constant(X[800:], dtype=tf.float32)
y_val   = tf.constant(y[800:], dtype=tf.float32)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(20,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
optimizer  = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_fn    = tf.keras.losses.BinaryCrossentropy()
train_losses, val_losses = [], []

EPOCHS = 30
BATCH  = 32

for epoch in range(EPOCHS):
    # Shuffle
    idx = np.random.permutation(len(X_train))
    epoch_loss = []
    for i in range(0, len(idx), BATCH):
        xb = tf.gather(X_train, idx[i:i+BATCH])
        yb = tf.gather(y_train, idx[i:i+BATCH])
        with tf.GradientTape() as tape:
            preds = model(xb, training=True)
            loss  = loss_fn(yb, tf.squeeze(preds))
        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))
        epoch_loss.append(loss.numpy())
    train_losses.append(np.mean(epoch_loss))
    val_preds = model(X_val, training=False)
    val_losses.append(loss_fn(y_val, tf.squeeze(val_preds)).numpy())
    if (epoch + 1) % 5 == 0:
        print(f"Epoch {epoch+1:3d} | train_loss={train_losses[-1]:.4f} | val_loss={val_losses[-1]:.4f}")

plt.figure(figsize=(8, 4))
plt.plot(train_losses, label='Train Loss')
plt.plot(val_losses,   label='Val Loss', linestyle='--')
plt.title('Custom Training Loop — Loss Curve')
plt.xlabel('Epoch'); plt.ylabel('BCE Loss'); plt.legend()
plt.tight_layout(); plt.savefig('custom_loop_curve.png', dpi=100); plt.show()
```

1. Confirm the training loss decreases over 30 epochs by inspecting the printed output.
2. Compare the final validation loss from this custom loop to running `model.fit()` on the same model — they should be similar if the batch size and optimizer match.

### Reflection Questions

1. In Challenge 1, sigmoid and tanh both suffered from smaller first-layer gradients than ReLU in a 5-layer network. At what network depth does this difference become practically significant, and what architectural solution (besides switching to ReLU) could help?
2. The custom training loop in Challenge 2 gives complete control over every step. In a production training scenario, what are two specific reasons you might prefer the custom loop over `model.fit()`, and what are two reasons you would prefer `model.fit()`?

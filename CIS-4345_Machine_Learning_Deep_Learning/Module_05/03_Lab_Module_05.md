# Lab: Module 05 — TensorFlow and Keras Fundamentals

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Lab Overview

In this lab you will build, inspect, and compile three distinct Keras models: one using the Sequential API, one using the Functional API with a single input, and one using the Functional API with multiple inputs. You will verify output shapes, calculate parameter counts by hand, and confirm that all models compile and produce predictions correctly.

**Estimated Time:** 60–90 minutes

**Tools Required:** Python 3.9+, TensorFlow 2.x, NumPy, Google Colab or local Jupyter environment

---

## Learning Objectives

By the end of this lab you will be able to:

- Create and manipulate tensors using `tf.constant`, `tf.Variable`, and shape operations
- Build a Sequential model and verify its architecture with `model.summary()`
- Build equivalent models using the Functional API
- Construct a multi-input Functional model with a merge layer
- Apply correct `model.compile()` settings for three different problem types
- Interpret `model.summary()` output and manually verify parameter counts

---

## Part 1 — Tensor Operations Warmup

### Step 1.1 — Environment Setup

```python
import tensorflow as tf
import numpy as np

print("TensorFlow version:", tf.__version__)
tf.random.set_seed(42)
np.random.seed(42)
```

### Step 1.2 — Create and Inspect Tensors

```python
# Create tensors of different ranks
scalar = tf.constant(7.0)
vector = tf.constant([1.0, 2.0, 3.0, 4.0])
matrix = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
tensor3d = tf.zeros([4, 3, 2])

for t, name in [(scalar, 'scalar'), (vector, 'vector'),
                (matrix, 'matrix'), (tensor3d, 'tensor3d')]:
    print(f"{name}: shape={t.shape}, rank={t.ndim}, dtype={t.dtype}")
```

**Expected output format:**

```
scalar: shape=(), rank=0, dtype=float32
vector: shape=(4,), rank=1, dtype=float32
matrix: shape=(3, 2), rank=2, dtype=float32
tensor3d: shape=(4, 3, 2), rank=3, dtype=float32
```

### Step 1.3 — Shape Operations

```python
# Reshape, expand, and squeeze
a = tf.constant([[1, 2, 3], [4, 5, 6]])    # shape (2, 3)

flat = tf.reshape(a, [-1])                  # shape (6,)
col = tf.reshape(a, [6, 1])                 # shape (6, 1)
batched = tf.expand_dims(a, axis=0)         # shape (1, 2, 3)
squeezed = tf.squeeze(batched)              # shape (2, 3)

print("Original:", a.shape)
print("Flat:", flat.shape)
print("Column:", col.shape)
print("Batched:", batched.shape)
print("Squeezed:", squeezed.shape)
```

### Step 1.4 — Matrix Operations

```python
W = tf.constant([[0.5, -0.3], [0.2, 0.8], [-0.1, 0.4]])  # (3, 2)
x = tf.constant([[1.0], [2.0]])                             # (2, 1)

result = tf.matmul(W, x)   # should be (3, 1)
print("MatMul result shape:", result.shape)
print("MatMul result:\n", result.numpy())
```

**Checkpoint:** What is the expected shape of `tf.matmul(W, x)` given `W.shape=(3,2)` and `x.shape=(2,1)`? Write your answer as a comment before running the cell.

---

## Part 2 — Sequential Model

### Step 2.1 — Build the Model

Build a Sequential model for a multi-class classification problem with 50 input features and 8 output classes.

```python
model_seq = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(50,), name='hidden_1'),
    tf.keras.layers.Dense(64, activation='relu', name='hidden_2'),
    tf.keras.layers.Dense(8, activation='softmax', name='output')
])

model_seq.summary()
```

### Step 2.2 — Manual Parameter Count

Before running the cell, calculate the expected parameter count for each layer and fill in this table in a markdown cell:

| Layer | Input Dim | Units | Formula | Expected Params |
|---|---|---|---|---|
| hidden_1 | 50 | 128 | `(50+1)*128` | 6528 |
| hidden_2 | 128 | 64 | `(128+1)*64` | 8256 |
| output | 64 | 8 | `(64+1)*8` | 520 |
| **Total** | | | | **15304** |

Verify these values match `model.summary()` output. If they do not match, identify the discrepancy.

### Step 2.3 — Inspect Weights

```python
for layer in model_seq.layers:
    weights = layer.get_weights()
    if weights:
        W, b = weights
        print(f"{layer.name}: W.shape={W.shape}, b.shape={b.shape}")
```

### Step 2.4 — Compile for Multi-class Classification

```python
model_seq.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
print("Sequential model compiled successfully.")
```

### Step 2.5 — Generate a Test Prediction

```python
# Create a fake batch of 5 samples with 50 features
x_test = tf.random.normal([5, 50])
predictions = model_seq.predict(x_test, verbose=0)
print("Predictions shape:", predictions.shape)   # should be (5, 8)
print("Sample prediction (should sum to 1.0):", predictions[0])
print("Sum:", predictions[0].sum())
```

**Checkpoint:** Confirm that each row of `predictions` sums to approximately 1.0. This verifies that the softmax output is correctly normalized.

---

## Part 3 — Functional API (Single Input)

### Step 3.1 — Build the Same Architecture with Functional API

```python
inputs = tf.keras.Input(shape=(50,), name='input_layer')
x = tf.keras.layers.Dense(128, activation='relu', name='hidden_1')(inputs)
x = tf.keras.layers.Dense(64, activation='relu', name='hidden_2')(x)
outputs = tf.keras.layers.Dense(8, activation='softmax', name='output')(x)

model_func = tf.keras.Model(inputs=inputs, outputs=outputs, name='functional_model')
model_func.summary()
```

### Step 3.2 — Confirm Parameter Parity

```python
seq_params = model_seq.count_params()
func_params = model_func.count_params()
print(f"Sequential params: {seq_params}")
print(f"Functional params: {func_params}")
print(f"Match: {seq_params == func_params}")
```

**Expected output:** Both models should have the same number of parameters (15,304) since they share the same architecture. If they do not match, inspect the layer configurations.

### Step 3.3 — Compile and Verify Prediction

```python
model_func.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

pred_func = model_func.predict(x_test, verbose=0)
print("Functional predictions shape:", pred_func.shape)
```

---

## Part 4 — Functional API (Multi-Input)

### Step 4.1 — Problem Description

You are building a model that combines two types of features:

- **Demographic features:** 12 numeric features about a customer
- **Transaction features:** 25 numeric features about recent transactions

The goal is binary classification — predict whether a customer will churn.

### Step 4.2 — Build the Multi-Input Model

```python
# Define two input tensors
demo_input = tf.keras.Input(shape=(12,), name='demographic_features')
txn_input = tf.keras.Input(shape=(25,), name='transaction_features')

# Process each stream independently
demo_branch = tf.keras.layers.Dense(32, activation='relu', name='demo_dense')(demo_input)
txn_branch = tf.keras.layers.Dense(64, activation='relu', name='txn_dense')(txn_input)

# Merge the two streams
merged = tf.keras.layers.Concatenate(name='merge')([demo_branch, txn_branch])

# Shared layers after merge
x = tf.keras.layers.Dense(32, activation='relu', name='shared_dense')(merged)
output = tf.keras.layers.Dense(1, activation='sigmoid', name='output')(x)

# Build model
model_multi = tf.keras.Model(
    inputs=[demo_input, txn_input],
    outputs=output,
    name='multi_input_model'
)

model_multi.summary()
```

### Step 4.3 — Compile

```python
model_multi.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
print("Multi-input model compiled.")
```

### Step 4.4 — Generate a Prediction with Two Inputs

```python
demo_data = tf.random.normal([10, 12])    # batch of 10 demographic samples
txn_data = tf.random.normal([10, 25])     # batch of 10 transaction samples

# Pass inputs as a list in the same order as model inputs
preds = model_multi.predict([demo_data, txn_data], verbose=0)
print("Multi-input predictions shape:", preds.shape)    # should be (10, 1)
print("Sample prediction (probability):", preds[0][0])
```

---

## Part 5 — Regression Model

### Step 5.1 — Build and Compile a Regression Model

Build a Sequential model for a regression task: predicting a continuous house price value from 13 input features.

```python
model_reg = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(13,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)   # no activation for regression output
])

model_reg.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

model_reg.summary()
```

### Step 5.2 — Verify Output Shape

```python
x_reg = tf.random.normal([8, 13])
pred_reg = model_reg.predict(x_reg, verbose=0)
print("Regression output shape:", pred_reg.shape)    # should be (8, 1)
print("Sample prediction:", pred_reg[0][0])
```

**Note:** Regression outputs are unbounded real values, not probabilities. A value of -3.5 or 150.2 is completely normal depending on your data scale.

---

## Deliverables

Submit the following to Canvas by the module deadline:

1. Completed Colab or Jupyter notebook (.ipynb) with all cells executed and outputs visible
2. Markdown cell with the parameter count table from Step 2.2, filled in before running
3. Cell output showing `seq_params == func_params` evaluates to `True`
4. `model.summary()` output for all four models (sequential, functional, multi-input, regression)
5. Written answers (in a markdown cell) to the two reflection questions below

---

## Reflection Questions

Answer these in a markdown cell in your notebook:

1. The Functional API and the Sequential API produced models with identical parameter counts and identical predictions in Parts 2 and 3. If they are equivalent, why would you ever choose the Functional API? Describe a real-world scenario where Sequential would be insufficient.

2. In Part 4, the multi-input model has two branches that merge with `Concatenate`. What would happen if you used `Add()` instead of `Concatenate()`? What constraint would that impose on the two branch output shapes, and why would that be limiting in this scenario?

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Tensor operations (Part 1) execute correctly, shapes verified | 15 |
| Sequential model summary matches hand-calculated parameter counts | 20 |
| Functional model parameter count matches Sequential (verified in code) | 15 |
| Multi-input model compiles and produces shape `(10, 1)` predictions | 20 |
| Regression model compiles with correct loss and output shape `(8, 1)` | 15 |
| Two reflection questions answered thoughtfully in complete sentences | 15 |
| **Total** | **100** |

---

## Common Errors and Fixes

**ValueError: Input 0 of layer is incompatible with the layer:** The input shape passed to the first layer does not match the data shape. Check that `input_shape=(n,)` matches the number of features in your data.

**Multi-input prediction shape error:** When calling `model.predict([a, b])`, the inputs must be in the same order as defined in `tf.keras.Model(inputs=[...])`. Swap the list order if you get a shape mismatch.

**Softmax sum not equal to 1.0:** Numerical precision may cause the sum to be `0.9999999` or `1.0000001`. Values within `1e-5` of 1.0 are acceptable. Use `np.isclose(predictions[0].sum(), 1.0)` to check programmatically.

**`count_params()` returns different values:** Verify that both models use identical layer configurations. A difference of 1 or more means a layer unit count or activation was specified differently.

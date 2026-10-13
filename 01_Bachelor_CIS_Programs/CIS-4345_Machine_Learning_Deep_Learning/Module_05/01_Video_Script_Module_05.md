# Video Script: Module 05 — TensorFlow and Keras Fundamentals

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: TensorFlow Developer Certificate

---

## Pre-Roll Slide (on screen while intro plays)

**Topic:** TensorFlow and Keras Fundamentals

**Objectives:** Understand TensorFlow installation, tensors, computational graphs, the Sequential API, the Functional API, and model compilation.

---

## SEGMENT 1 — Introduction (0:00–1:30)

[Camera: Instructor on screen]

Welcome to Module 5 of CIS-4345. I am Professor Nash. Last module we built the mathematical foundation — perceptrons, activation functions, gradient descent, backpropagation. Today we pick up the tools.

TensorFlow is the framework used for the TensorFlow Developer Certificate exam, and it is one of the two dominant deep learning frameworks in industry. Keras is the high-level API built into TensorFlow — it gives us clean, readable code that hides the complexity of the underlying engine while still exposing all the power you need.

By the end of this module you will be able to:

- Install TensorFlow and verify your environment correctly
- Create and manipulate tensors — the fundamental data unit
- Understand how TensorFlow's computational graph works
- Build models using the Sequential API
- Build models using the Functional API
- Compile models with the correct optimizer, loss function, and metrics

Let us start from the ground up.

---

## SEGMENT 2 — Installation and Environment Verification (1:30–3:30)

[Screen: Terminal or Colab notebook]

The recommended environment for this course is Google Colab, which comes with TensorFlow pre-installed. If you are working locally, install TensorFlow with:

```bash
pip install tensorflow
```

For GPU support on a local machine with an NVIDIA GPU:

```bash
pip install tensorflow[and-cuda]
```

Once installed, verify your setup with:

```python
import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("GPU available:", tf.config.list_physical_devices('GPU'))
```

[Camera: Instructor]

For the certification exam, you will work in a Colab-like browser environment, so local GPU setup is optional for coursework. What matters is that your version is TensorFlow 2.x — the exam uses 2.x APIs exclusively.

A quick history note: TensorFlow 1.x required you to manually build a graph and then run a Session object to execute it. TensorFlow 2.x runs eagerly by default — operations execute immediately, just like NumPy. That shift made TensorFlow dramatically more accessible and is why Keras became the official high-level API.

---

## SEGMENT 3 — Tensors: The Fundamental Data Structure (3:30–7:00)

[Screen: Code demonstration]

A **tensor** is the fundamental data structure in TensorFlow. Think of it as an n-dimensional array — like a NumPy array, but one that can run on a GPU and participates in automatic differentiation.

```python
import tensorflow as tf
import numpy as np

# Scalar: rank-0 tensor
scalar = tf.constant(3.14)
print("Scalar:", scalar)
print("Shape:", scalar.shape)    # ()
print("Rank:", scalar.ndim)      # 0

# Vector: rank-1 tensor
vector = tf.constant([1.0, 2.0, 3.0])
print("Vector shape:", vector.shape)    # (3,)

# Matrix: rank-2 tensor
matrix = tf.constant([[1, 2], [3, 4], [5, 6]])
print("Matrix shape:", matrix.shape)    # (3, 2)

# 3D tensor — e.g., a batch of grayscale images
images = tf.zeros([32, 28, 28])
print("Image batch shape:", images.shape)   # (32, 28, 28)

# 4D tensor — batch of RGB images
rgb_images = tf.zeros([32, 28, 28, 3])
print("RGB batch shape:", rgb_images.shape)   # (32, 28, 28, 3)
```

[Camera: Instructor]

Tensor rank equals the number of dimensions. Scalars are rank 0, vectors rank 1, matrices rank 2. When you feed image data into a CNN, you will use rank-4 tensors: batch size, height, width, channels. Understanding shapes is critical — most bugs in deep learning are shape mismatches.

### Common Tensor Operations

```python
a = tf.constant([1.0, 2.0, 3.0])
b = tf.constant([4.0, 5.0, 6.0])

# Element-wise operations
print("Sum:", a + b)
print("Product:", a * b)

# Matrix multiplication
A = tf.constant([[1.0, 2.0], [3.0, 4.0]])
B = tf.constant([[5.0, 6.0], [7.0, 8.0]])
print("MatMul:", tf.matmul(A, B))

# Reshape
c = tf.constant([[1, 2, 3], [4, 5, 6]])   # shape (2, 3)
d = tf.reshape(c, [3, 2])                   # shape (3, 2)
print("Reshaped:", d)

# Interop with NumPy
arr = np.array([1.0, 2.0, 3.0])
t = tf.constant(arr)              # NumPy to TensorFlow
back = t.numpy()                  # TensorFlow to NumPy
```

### tf.Variable vs. tf.constant

`tf.constant` is immutable. Neural network weights must be updated during training, so they use `tf.Variable`:

```python
weight = tf.Variable(0.5)
weight.assign(0.8)       # replace value
weight.assign_add(0.1)   # add to current value
print(weight.numpy())    # 0.9
```

Keras Dense layers automatically create all weights as `tf.Variable` objects. You rarely create Variables manually.

---

## SEGMENT 4 — Computational Graphs and Eager Execution (7:00–9:00)

[Slide: Diagram showing computation graph nodes]

[Camera: Instructor]

TensorFlow 2.x runs in **eager mode** by default — operations execute immediately when you call them, giving you Python-style interactivity and easy debugging.

But TensorFlow also has a **graph mode** that compiles operations into an optimized computation graph. You opt into graph mode with the `@tf.function` decorator:

```python
@tf.function
def compute_output(x, W, b):
    return tf.sigmoid(tf.matmul(x, W) + b)

x = tf.constant([[1.0, 2.0]])
W = tf.constant([[0.5], [0.3]])
b = tf.constant([0.1])

result = compute_output(x, W, b)
print(result)
```

On the first call, TensorFlow traces the function and compiles it to a graph. Subsequent calls reuse the compiled graph and run significantly faster. Keras applies `@tf.function` automatically inside `model.fit()`, so training is graph-optimized even though you write eager code.

For the exam and for this course: write eager code, let Keras handle graph compilation. You need to understand the concept, but you do not need to decorate everything manually.

---

## SEGMENT 5 — The Sequential API (9:00–13:30)

[Screen: Code demonstration]

The Sequential API is the simplest and most common way to build a neural network in Keras. Use it whenever your network is a linear stack of layers — every layer feeds exactly into the next.

### Basic Sequential Model

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(20,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()
```

`model.summary()` prints the architecture, output shapes, and parameter count for every layer. Always run this immediately after building a model to confirm the architecture is what you intended.

### Building with .add()

You can also build a Sequential model incrementally:

```python
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(64, activation='relu', input_shape=(20,)))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
```

Both approaches produce identical models.

### Specifying Input Shape

The `input_shape` parameter on the first layer tells Keras the shape of one input sample (not including the batch dimension). Alternatives:

```python
# Explicit Input layer
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(20,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Or specify input_dim shorthand for 1D input
tf.keras.layers.Dense(64, activation='relu', input_dim=20)
```

[Camera: Instructor]

For simple tabular data and straightforward classification or regression, Sequential is your go-to. But when your architecture needs branches, skip connections, or multiple input streams, you need the Functional API.

---

## SEGMENT 6 — The Functional API (13:30–18:30)

[Screen: Code demonstration]

The Functional API is more flexible. Instead of declaring a list of layers, you treat each layer as a function that you call on a tensor. This lets you create any topology — including branching, merging, and residual connections.

### Equivalent Functional Model

```python
inputs = tf.keras.Input(shape=(20,))
x = tf.keras.layers.Dense(64, activation='relu')(inputs)
x = tf.keras.layers.Dense(32, activation='relu')(x)
outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)

model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.summary()
```

The architecture is identical to the Sequential example. The difference is the syntax: `tf.keras.Input` creates a symbolic tensor, then each layer call receives and returns a tensor, and `tf.keras.Model` connects the graph.

### Multi-Input Functional Model

```python
# Two input streams
text_input = tf.keras.Input(shape=(100,), name='text_features')
numeric_input = tf.keras.Input(shape=(8,), name='numeric_features')

# Process each stream independently
text_branch = tf.keras.layers.Dense(32, activation='relu')(text_input)
numeric_branch = tf.keras.layers.Dense(16, activation='relu')(numeric_input)

# Merge
merged = tf.keras.layers.Concatenate()([text_branch, numeric_branch])
output = tf.keras.layers.Dense(1, activation='sigmoid')(merged)

model = tf.keras.Model(
    inputs=[text_input, numeric_input],
    outputs=output
)
model.summary()
```

### Skip Connection (Residual-style)

```python
inputs = tf.keras.Input(shape=(32,))
x = tf.keras.layers.Dense(32, activation='relu')(inputs)
x = tf.keras.layers.Dense(32, activation='relu')(x)
# Skip connection: add original input to transformed output
x = tf.keras.layers.Add()([inputs, x])
outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

[Camera: Instructor]

Skip connections are the core innovation in ResNet, one of the most influential computer vision architectures ever built. They allow gradients to bypass layers and flow directly from output to early layers, which is what makes training 50+ layer networks feasible.

For the certification exam, you need to be comfortable reading and writing both APIs. The Functional API will appear in questions involving multiple inputs or branching architecture diagrams.

---

## SEGMENT 7 — Model Compilation (18:30–21:00)

[Screen: Code demonstration]

Before training, you call `model.compile()` to specify three things:

1. **Optimizer** — how weights are updated each step
2. **Loss function** — what objective we minimize
3. **Metrics** — what we monitor during training (not used for gradient updates)

```python
# Binary classification
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Multi-class with integer labels
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Regression
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)
```

### Optimizer Options

You can pass optimizers as a string (uses defaults) or as an object (allows custom parameters):

```python
# Default Adam
model.compile(optimizer='adam', loss='mse')

# Custom learning rate
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss='mse'
)

# SGD with momentum and weight decay
model.compile(
    optimizer=tf.keras.optimizers.SGD(
        learning_rate=0.01,
        momentum=0.9,
        weight_decay=0.0001
    ),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
```

[Camera: Instructor]

Compilation configures the training procedure but does not train the model. The actual training happens in `model.fit()`. We cover the full training workflow — including callbacks, early stopping, and learning rate scheduling — in Module 6.

---

## SEGMENT 8 — Sequential vs. Functional Side-by-Side (21:00–22:30)

[Slide: Side-by-side comparison]

Let me put the two APIs next to each other one final time.

Sequential for a simple network:

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

Functional for the same architecture:

```python
inputs = tf.keras.Input(shape=(10,))
x = tf.keras.layers.Dense(64, activation='relu')(inputs)
outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

Both are identical in what they compute. Use Sequential when simplicity is sufficient. Use Functional when you need flexibility.

---

## SEGMENT 9 — Wrap-Up and Preview (22:30–24:00)

[Camera: Instructor]

Today we covered TensorFlow and Keras fundamentals: installation and environment verification, tensors and variables, eager execution versus graph mode with `@tf.function`, the Sequential API, the Functional API including multi-input and skip connection patterns, and model compilation with optimizer, loss, and metrics.

In Module 6, we go deep into the training process itself — callbacks, learning rate schedules, batch normalization, dropout, early stopping, and model evaluation. These are the techniques that take a model from "it runs" to "it works well."

Your lab this week has you build three models — one Sequential, one Functional, and one multi-input Functional — and verify that all three compile correctly and produce the expected output shapes from `model.summary()`.

Quiz and discussion are due Sunday at midnight.

See you in Module 6.

---

## Production Notes

- Screen capture: all code demonstrations at 1080p, font size 18 or larger
- Pause on `model.summary()` output long enough for students to read each line
- Annotate the Functional API tensor flow diagram to show data path from Input to Model
- Closed captions required for all segments

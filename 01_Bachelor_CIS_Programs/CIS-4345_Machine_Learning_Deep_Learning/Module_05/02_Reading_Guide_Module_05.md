# Reading Guide: Module 05 — TensorFlow and Keras Fundamentals

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4345 &BULL; MACHINE LEARNING & DEEP LEARNING SYSTEMS</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">TensorFlow / deeplearning.ai &bull; CIS-4345 Module 05</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=NWONeJKn6kc" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/NWONeJKn6kc" title="Deep Learning & Neural Networks Masterclass" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Deep Learning & Neural Networks Masterclass</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->




## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

## Certification Alignment: TensorFlow Developer Certificate

---

## Overview

This guide covers the TensorFlow and Keras fundamentals required for the TensorFlow Developer Certificate. You will learn the tensor data structure, understand how TensorFlow executes operations, and master both primary model-building APIs. By the end of this module you should be able to build, inspect, and compile any standard deep learning model in Keras without referencing documentation.

---

## Section 1 — TensorFlow Environment Setup

### Installation

Install TensorFlow in any Python 3.9+ environment:

```bash
pip install tensorflow
```

Verify the installation:

```python
import tensorflow as tf
print(tf.__version__)          # Should be 2.x
print(tf.config.list_physical_devices('GPU'))
```

Google Colab is the recommended environment for this course. Colab notebooks have TensorFlow pre-installed and provide free GPU acceleration.

### Eager Execution vs. Graph Mode

TensorFlow 2.x runs in **eager mode** by default. Operations execute immediately when called, exactly like NumPy. This makes debugging straightforward.

**Graph mode** compiles operations into an optimized computational graph. You opt in with `@tf.function`:

```python
@tf.function
def add(a, b):
    return a + b
```

On the first call, TensorFlow traces the function and builds the graph. Subsequent calls reuse the compiled graph and run faster. Keras applies `@tf.function` automatically inside `model.fit()`.

**Key rule:** Write your code in eager mode. Let Keras handle graph compilation unless you are writing a custom training loop that needs the performance.

---

## Section 2 — Tensors

### What Is a Tensor?

A tensor is an n-dimensional array. Tensors generalize scalars (0D), vectors (1D), and matrices (2D) to arbitrary dimensions.

| Rank | Name | Example Shape | Example Use |
|---|---|---|---|
| 0 | Scalar | `()` | A single loss value |
| 1 | Vector | `(n,)` | A 1D feature array |
| 2 | Matrix | `(m, n)` | A batch of feature vectors |
| 3 | 3D tensor | `(batch, seq, features)` | Text sequences |
| 4 | 4D tensor | `(batch, h, w, channels)` | Image batches |

### Creating Tensors

```python
# Constant (immutable)
a = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# Zeros and ones
z = tf.zeros([3, 4])
o = tf.ones([3, 4])

# Random normal
r = tf.random.normal([2, 3], mean=0.0, stddev=1.0)

# From NumPy
import numpy as np
arr = np.array([1.0, 2.0, 3.0])
t = tf.constant(arr)
```

### Essential Tensor Operations

```python
a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
b = tf.constant([[5.0, 6.0], [7.0, 8.0]])

# Element-wise
print(a + b)
print(a * b)

# Matrix multiplication
print(tf.matmul(a, b))

# Reduction
print(tf.reduce_sum(a))          # sum of all elements
print(tf.reduce_mean(a, axis=0)) # column means

# Shape manipulation
c = tf.reshape(a, [4])          # flatten to 1D
d = tf.expand_dims(a, axis=0)   # add batch dim: (1, 2, 2)
e = tf.squeeze(d)               # remove size-1 dims
```

### Variables

`tf.Variable` is a mutable tensor used for trainable parameters:

```python
w = tf.Variable(tf.random.normal([3, 2]))
w.assign(tf.zeros([3, 2]))       # replace entire value
w.assign_add(tf.ones([3, 2]))    # add in place
```

Keras creates all layer weights as `tf.Variable` automatically. You use Variables directly only when implementing custom layers or custom training loops.

### Dtype Awareness

TensorFlow is strict about data types. Mixing `float32` and `float64` tensors raises errors. Always ensure consistency:

```python
x = tf.constant([1.0, 2.0])         # float32 by default
y = tf.constant([1.0, 2.0], dtype=tf.float64)

# Cast when needed
y_f32 = tf.cast(y, dtype=tf.float32)
```

Keras models expect `float32` input by default. Preprocess your data to `float32` before training.

---

## Section 3 — The Sequential API

The Sequential API is the primary model-building interface for linear layer stacks.

### Syntax

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(n_features,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(n_classes, activation='softmax')
])
```

Or equivalently using `.add()`:

```python
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, activation='relu', input_shape=(n_features,)))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(n_classes, activation='softmax'))
```

### model.summary()

Always call `model.summary()` after building a model:

```
Model: "sequential"
_________________________________________________________________
 Layer (type)            Output Shape          Param #
=================================================================
 dense (Dense)           (None, 128)           25,728
 dense_1 (Dense)         (None, 64)            8,256
 dense_2 (Dense)         (None, 10)            650
=================================================================
Total params: 34,634
```

The output shape shows `None` for the batch dimension — Keras uses `None` as a placeholder meaning "any batch size."

### Parameter Count Formula

For a Dense layer: `params = (input_dim + 1) * units`

The `+1` accounts for the bias vector (one bias per output neuron).

Example: Dense(128) receiving 200-dimensional input: `(200 + 1) * 128 = 25,728`

### When to Use Sequential

Use Sequential when:

- Each layer has exactly one input and one output
- Layers form a straight chain from input to output
- You do not need skip connections, branching, or multiple inputs/outputs

---

## Section 4 — The Functional API

The Functional API treats layers as callable functions applied to tensor objects. It enables any network topology.

### Core Syntax Pattern

```python
# 1. Create a symbolic input tensor
inputs = tf.keras.Input(shape=(n_features,))

# 2. Call layers as functions on tensors
x = tf.keras.layers.Dense(64, activation='relu')(inputs)
x = tf.keras.layers.Dense(32, activation='relu')(x)
outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)

# 3. Define the Model
model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

### Multi-Input Functional Model

```python
input_a = tf.keras.Input(shape=(50,), name='features_a')
input_b = tf.keras.Input(shape=(10,), name='features_b')

branch_a = tf.keras.layers.Dense(32, activation='relu')(input_a)
branch_b = tf.keras.layers.Dense(16, activation='relu')(input_b)

merged = tf.keras.layers.Concatenate()([branch_a, branch_b])
output = tf.keras.layers.Dense(1, activation='sigmoid')(merged)

model = tf.keras.Model(inputs=[input_a, input_b], outputs=output)
```

### Skip Connection

```python
inputs = tf.keras.Input(shape=(32,))
x = tf.keras.layers.Dense(32, activation='relu')(inputs)
x = tf.keras.layers.Dense(32, activation='relu')(x)
x = tf.keras.layers.Add()([inputs, x])   # residual connection
outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
```

### Sequential vs. Functional Comparison Table

| Feature | Sequential | Functional |
|---|---|---|
| Syntax complexity | Simple list | Explicit tensor wiring |
| Linear topology | Yes | Yes |
| Branching paths | No | Yes |
| Multiple inputs | No | Yes |
| Skip connections | No | Yes |
| Custom topologies | No | Yes |
| Exam recommendation | Simple models | Complex models |

---

## Section 5 — Model Compilation

Compilation configures three aspects of the training procedure.

### compile() Parameters

```python
model.compile(
    optimizer,       # weight update algorithm
    loss,            # objective function to minimize
    metrics          # values to monitor (not used for updates)
)
```

### Compilation Reference Table

| Problem Type | Optimizer | Loss | Metrics |
|---|---|---|---|
| Binary classification | `'adam'` | `'binary_crossentropy'` | `['accuracy']` |
| Multi-class (int labels) | `'adam'` | `'sparse_categorical_crossentropy'` | `['accuracy']` |
| Multi-class (one-hot) | `'adam'` | `'categorical_crossentropy'` | `['accuracy']` |
| Regression | `'adam'` | `'mse'` | `['mae']` |

### Optimizer Objects vs. Strings

```python
# String shorthand uses optimizer defaults
model.compile(optimizer='adam', loss='mse')

# Object allows parameter customization
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

### Common Optimizers

**Adam:** Adaptive per-parameter learning rates. Default choice for most problems. Parameters: `learning_rate=0.001` (default), `beta_1=0.9`, `beta_2=0.999`.

**SGD:** Classic stochastic gradient descent. Add `momentum=0.9` for most use cases.

**RMSprop:** Well-suited for recurrent networks. Uses a moving average of squared gradients to normalize the learning rate.

---

## Section 6 — Model Inspection and Utilities

### Checking Weights

```python
# List all layer names
for layer in model.layers:
    print(layer.name, layer.output_shape)

# Get weights from a specific layer
weights, biases = model.layers[0].get_weights()
print("Weight shape:", weights.shape)
print("Bias shape:", biases.shape)
```

### Saving and Loading Models

```python
# Save entire model (architecture + weights + optimizer state)
model.save('my_model.keras')

# Load it back
loaded = tf.keras.models.load_model('my_model.keras')

# Save only weights
model.save_weights('my_weights.h5')
model.load_weights('my_weights.h5')
```

The `.keras` format is the modern recommended format for TensorFlow 2.x. The older `.h5` format still works but is being phased out.

---

## Section 7 — Exam Tips

- Know the parameter count formula: `(input_dim + 1) * units` for Dense layers. This is tested directly.
- `input_shape=(n,)` specifies a single sample shape, not including the batch dimension. Keras prepends `None` for the batch.
- `sparse_categorical_crossentropy` accepts integer labels. `categorical_crossentropy` requires one-hot encoded labels. Using the wrong one is a common exam error.
- The Functional API requires `tf.keras.Input(shape=(...))` — not `tf.keras.layers.Input`. Both exist but `tf.keras.Input` is the canonical modern form.
- `model.compile()` does not train the model. Training begins with `model.fit()`.
- `model.summary()` — practice reading it. The exam may ask you to predict the output shape of a specific layer.

---


---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 05 — TensorFlow and Keras Fundamentals** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 05 — TensorFlow and Keras Fundamentals**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 05 — TensorFlow and Keras Fundamentals**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Module 05 — TensorFlow and Keras Fundamentals**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**


## Study Checklist

- [ ] Run the tensor operations examples and verify all output shapes match expectations
- [ ] Build a Sequential model and confirm parameter counts in `model.summary()` match hand-calculated values
- [ ] Build a Functional model with two inputs and verify it compiles without errors
- [ ] Write the correct `model.compile()` call for each of the four problem types in the reference table
- [ ] Complete the Module 05 Lab
- [ ] Complete the Module 05 Quiz
- [ ] Post to the Module 05 Discussion Board by Wednesday 11:59 PM

---

## Required External Resources

- TensorFlow Keras Sequential API: [https://www.tensorflow.org/guide/keras/sequential_model](https://www.tensorflow.org/guide/keras/sequential_model)
- TensorFlow Keras Functional API: [https://www.tensorflow.org/guide/keras/functional_api](https://www.tensorflow.org/guide/keras/functional_api)
- TensorFlow Tensor guide: [https://www.tensorflow.org/guide/tensor](https://www.tensorflow.org/guide/tensor)

---

## 9. Supplemental Resources

**1. TensorFlow Keras Sequential Model Guide**
<https://www.tensorflow.org/guide/keras/sequential_model>
Official guide covering the Sequential API end-to-end: building, inspecting with `model.summary()`, compiling, training, and saving. Includes worked examples for the exact patterns tested on the TensorFlow Developer Certificate exam.

**2. TensorFlow Keras Functional API Guide**
<https://www.tensorflow.org/guide/keras/functional_api>
Official guide demonstrating multi-input models, skip connections, and shared layers using the Functional API. Directly supports the Module 05 lab's multi-input model section and the exam's architecture flexibility questions.

**3. TensorFlow Core — tf.Tensor Guide**
<https://www.tensorflow.org/guide/tensor>
Comprehensive reference for tensor creation, shape manipulation, dtype casting, and the relationship between TensorFlow tensors and NumPy arrays. Covers `tf.reshape`, `tf.cast`, `tf.matmul`, and `tf.reduce_sum` — all operations appearing in this module's quiz and lab.

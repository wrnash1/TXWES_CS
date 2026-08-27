# Reading Guide: Module 14 — Model Deployment and Production ML Pipelines

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Overview

Module 14 bridges the gap between model training and real-world use. Even a highly accurate model is worthless if it cannot be accessed reliably by the systems and users that need it. This guide covers the four major deployment patterns you will encounter in industry: SavedModel serialization, TensorFlow Serving, TFLite for edge devices, and production pipeline orchestration via TFX. A fifth section covers lightweight REST API deployment with Flask.

**Estimated study time:** 2–2.5 hours

---

## Learning Objectives

After completing this guide you will be able to:

1. Save a Keras model in SavedModel format and explain its directory structure
2. Distinguish SavedModel from `.h5` and when to use each
3. Describe how TensorFlow Serving handles model versioning and REST inference
4. Convert a SavedModel to TFLite and apply post-training quantization
5. Explain the role of TFX components in a production ML pipeline
6. Build a basic Flask REST endpoint that loads and serves a SavedModel

---

## Section 1 — Model Serialization: SavedModel vs `.h5`

### 1.1 The Two Formats

TensorFlow/Keras supports two primary serialization formats:

**SavedModel (recommended):**

```python
model.save('my_model')          # Directory format
model.save('my_model.tf')       # Also SavedModel
```

**HDF5/Keras legacy:**

```python
model.save('my_model.h5')       # Single file, Keras-specific
```

| Property | SavedModel | HDF5 (.h5) |
|----------|------------|------------|
| Language support | Any language | Python only |
| Custom layers | Full support | Requires config |
| TF Serving compatible | Yes | No |
| Contains serving signatures | Yes | No |

### 1.2 SavedModel Directory Structure

After calling `model.save('my_model')`, inspect the output:

```text
my_model/
  saved_model.pb        <- frozen computation graph
  variables/
    variables.index
    variables.data-00000-of-00001
  assets/               <- optional (vocabularies, etc.)
  fingerprint.pb        <- integrity check
```

The `.pb` file is a Protocol Buffer — a compact binary format designed for cross-language serialization. The variables directory contains the actual weight tensors.

### 1.3 Loading and Inspecting a SavedModel

```python
import tensorflow as tf

loaded = tf.saved_model.load('my_model')
print(list(loaded.signatures.keys()))
# ['serving_default']

infer = loaded.signatures['serving_default']
print(infer.structured_input_signature)
print(infer.structured_outputs)
```

The `serving_default` signature is automatically created from the model's `call()` method. You can define custom signatures for multi-input or multi-output models.

### 1.4 Saving and Loading with Keras API

The recommended approach for Keras models:

```python
# Save
model.save('my_model')

# Load (returns a full Keras model)
restored = tf.keras.models.load_model('my_model')
restored.predict(x_test[:10])
```

`tf.keras.models.load_model` is preferred when you want to continue training or access the Keras API. `tf.saved_model.load` is preferred for pure inference use cases.

---

## Section 2 — TensorFlow Serving

### 2.1 What TF Serving Does

TensorFlow Serving is a purpose-built inference server with the following capabilities:

- Loads one or more SavedModels into memory
- Manages multiple model versions simultaneously
- Exposes a REST API on port 8501
- Exposes a gRPC API on port 8500
- Handles batching and hardware utilization automatically

### 2.2 Model Versioning Convention

TF Serving expects models organized by version number:

```text
/models/
  my_model/
    1/          <- version 1 (SavedModel directory)
    2/          <- version 2
```

It automatically serves the highest-numbered version. You can configure policies to keep older versions loaded for graceful rollback.

### 2.3 The REST API Protocol

A prediction request to TF Serving follows this pattern:

```text
POST http://{host}:8501/v1/models/{model_name}:predict
Content-Type: application/json

{
  "instances": [[0.1, 0.2, ..., 0.9], ...]
}
```

The response:

```json
{
  "predictions": [[0.01, 0.04, ..., 0.88], ...]
}
```

For named inputs (multi-input models), use `"inputs"` instead of `"instances"`:

```json
{
  "inputs": {
    "input_layer": [[...]]
  }
}
```

### 2.4 gRPC vs REST

| Factor | REST | gRPC |
|--------|------|------|
| Protocol | HTTP/JSON | HTTP/2 + Protocol Buffers |
| Latency | Higher | Lower |
| Ease of use | Easier | Requires protobuf setup |
| Best for | Prototyping, web clients | High-throughput services |

For most coursework and small production systems, REST is sufficient. Choose gRPC when latency matters at scale.

### 2.5 Docker Deployment

The standard TF Serving deployment uses the official Docker image:

```bash
docker run -p 8501:8501 \
  --mount type=bind,source=/path/to/models,target=/models/my_model \
  -e MODEL_NAME=my_model \
  tensorflow/serving
```

The `--mount` binds your local model directory into the container. The `-e MODEL_NAME` environment variable tells the server which directory under `/models/` to load.

---

## Section 3 — TFLite for Mobile and Edge Inference

### 3.1 Why TFLite Exists

Full TensorFlow has a runtime footprint measured in megabytes and depends on BLAS libraries and GPU drivers. This is incompatible with microcontrollers (KB of RAM) and mobile apps (user expects small download). TFLite solves this with:

- A compact flatbuffer model format (`.tflite`)
- A minimal inference-only runtime (< 1 MB for microcontrollers)
- Optimized kernels for ARM NEON, DSP, and GPU delegates

### 3.2 Conversion Pipeline

```python
# Step 1: Start from SavedModel
converter = tf.lite.TFLiteConverter.from_saved_model('my_model')
tflite_model = converter.convert()

# Step 2: Write to disk
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
```

Alternative: convert from a Keras model in memory:

```python
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
```

### 3.3 Post-Training Quantization

Quantization reduces model size and speeds up inference by lowering weight precision:

| Mode | Weight precision | Activation precision | Size reduction |
|------|-----------------|---------------------|----------------|
| Dynamic range | INT8 | FP32 (at runtime) | ~4x |
| Full integer | INT8 | INT8 | ~4x + faster |
| Float16 | FP16 | FP16 | ~2x |

**Dynamic range quantization** (simplest):

```python
converter.optimizations = [tf.lite.Optimize.DEFAULT]
```

**Full integer quantization** (fastest on hardware with INT8 support):

```python
def representative_dataset():
    for x in x_train[:100]:
        yield [x.reshape(1, -1).astype('float32')]

converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8
```

### 3.4 TFLite Interpreter API

Running inference requires the interpreter API:

```python
interpreter = tf.lite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

interpreter.set_tensor(input_details[0]['index'], input_array)
interpreter.invoke()
result = interpreter.get_tensor(output_details[0]['index'])
```

Note: `allocate_tensors()` must be called before any inference, and you must call it again if the input shape changes.

### 3.5 TFLite Model Benchmark Tool

TensorFlow provides a benchmark binary to measure latency on target hardware. On Android:

```bash
adb push model.tflite /data/local/tmp/
adb shell /data/local/tmp/benchmark_model \
  --graph=/data/local/tmp/model.tflite \
  --num_runs=50
```

This reports average latency, peak memory, and CPU/GPU utilization.

---

## Section 4 — TFX: Production ML Pipelines

### 4.1 The Motivation for Pipelines

A trained model is only one artifact in a production ML system. You also need:

- Repeatable data ingestion and validation
- Versioned preprocessing that exactly matches training
- Automated model evaluation against a deployed baseline
- Audit trails for compliance and debugging
- Triggered retraining when data distribution shifts

TFX provides all of these through a component-based pipeline architecture.

### 4.2 Core TFX Components

| Component | Role |
|-----------|------|
| ExampleGen | Ingest and split raw data |
| StatisticsGen | Compute feature statistics |
| SchemaGen | Infer expected data schema |
| ExampleValidator | Flag anomalies vs schema |
| Transform | Feature engineering (saved as a preprocessing graph) |
| Trainer | Train model using Keras or Estimator |
| Evaluator | Compare candidate model to baseline |
| Pusher | Deploy blessed model to serving infrastructure |

### 4.3 The ML Metadata Store

Every component reads and writes **artifacts** to an ML Metadata (MLMD) store. This creates a complete lineage graph: you can trace any deployed model back to the exact data slice, preprocessing parameters, and hyperparameters used to produce it. This is critical in regulated industries (finance, healthcare) and for debugging production issues.

### 4.4 When to Use TFX

TFX is appropriate when:

- Retraining must be automated and auditable
- Multiple teams share the pipeline (data engineers, ML engineers, platform)
- Compliance requires full data lineage

TFX is **not** appropriate for:

- Research and experimentation (too much overhead)
- Single-developer projects (simpler solutions exist)
- One-time batch predictions

---

## Section 5 — Lightweight Deployment with Flask

### 5.1 Architecture

Flask is appropriate for:

- Internal tools and dashboards
- Prototype APIs before migrating to TF Serving
- Low-to-moderate traffic (< ~100 requests/second)

A minimal serving pattern:

```python
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load model once at startup
model = tf.keras.models.load_model('my_model')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    instances = np.array(data['instances'], dtype='float32')
    predictions = model.predict(instances)
    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### 5.2 Input Validation

Always validate inputs before passing to the model:

```python
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    if 'instances' not in data:
        return jsonify({'error': 'Missing instances key'}), 400
    try:
        instances = np.array(data['instances'], dtype='float32')
    except (ValueError, TypeError) as e:
        return jsonify({'error': str(e)}), 400
    predictions = model.predict(instances)
    return jsonify({'predictions': predictions.tolist()})
```

### 5.3 Production Considerations

Flask's built-in server is single-threaded. For moderate traffic use Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

For high traffic or GPU inference, migrate to TF Serving. Flask should not handle GPU batching — TF Serving does this automatically.

---

## Section 6 — Deployment Decision Framework

When choosing a deployment strategy, evaluate these axes:

- **Who calls the model?** Web service → TF Serving. Mobile → TFLite. Internal tool → Flask.
- **What latency is acceptable?** Milliseconds → gRPC + TF Serving. Seconds acceptable → REST.
- **Does the model run on a device without internet?** Yes → TFLite. No → server-side serving.
- **Do you need automated retraining and lineage?** Yes → TFX. No → SavedModel + Serving.
- **Model size constraints?** Embedded → TFLite Micro. Mobile → TFLite. Server → full model.

---

## Key Terms

- **SavedModel:** TensorFlow's portable model format; directory containing graph and weights
- **Serving signature:** Named input/output tensor specification embedded in SavedModel
- **TF Serving:** Production inference server; REST and gRPC endpoints; model versioning
- **TFLite:** TensorFlow Lite; compact inference runtime for mobile and embedded
- **Quantization:** Reducing weight precision (FP32 → INT8) to shrink model size and speed inference
- **TFX:** TensorFlow Extended; end-to-end ML pipeline platform with lineage tracking
- **Flask:** Python microframework; suitable for lightweight model serving
- **Artifact:** Versioned data produced or consumed by a TFX pipeline component

---

## Self-Check Questions

1. What is the difference between `model.save('model.h5')` and `model.save('model')`?
2. What directory structure does TF Serving expect for model versioning?
3. What does `converter.optimizations = [tf.lite.Optimize.DEFAULT]` do?
4. Why must you call `interpreter.allocate_tensors()` before TFLite inference?
5. What is the role of the TFX Evaluator component?
6. When is gRPC preferable to REST for model serving?

---

## Recommended Resources

- TensorFlow SavedModel documentation: [tensorflow.org/guide/saved_model](https://www.tensorflow.org/guide/saved_model)
- TF Serving documentation: [tensorflow.org/tfx/guide/serving](https://www.tensorflow.org/tfx/guide/serving)
- TFLite documentation: [tensorflow.org/lite/guide](https://www.tensorflow.org/lite/guide)
- TFX documentation: [tensorflow.org/tfx](https://www.tensorflow.org/tfx)
- Hands-On ML, Chapter 19 — Training and Deploying TensorFlow Models at Scale

---

## Next Module Preview

Module 15 covers generative models and the Transformer architecture: autoencoders, variational autoencoders, GANs, attention mechanisms, and an introduction to BERT. These are among the most exciting and rapidly evolving areas of deep learning.

---

## 9. Supplemental Resources

**1. [TensorFlow Serving — Docker Quickstart](https://www.tensorflow.org/tfx/serving/docker)**
Official TF Serving Docker deployment guide covering model directory structure, container launch commands, REST and gRPC endpoint testing, and hot model reload. The primary reference for production Keras model serving and directly aligned with the deployment content in this module.

**2. [TFLite Guide — Post-Training Quantization](https://www.tensorflow.org/lite/performance/post_training_quantization)**
Comprehensive official guide comparing all four TFLite quantization strategies (dynamic range, full integer, float16, 16x8) with accuracy benchmarks, conversion code, and `representative_dataset` examples. Essential for understanding quantization tradeoffs in edge deployment.

**3. [FastAPI — Build APIs with Python](https://fastapi.tiangolo.com/)**
FastAPI is the modern alternative to Flask for ML model serving, offering automatic OpenAPI documentation, type validation with Pydantic, and async request handling. Widely used in production ML systems and increasingly preferred over Flask for new projects.

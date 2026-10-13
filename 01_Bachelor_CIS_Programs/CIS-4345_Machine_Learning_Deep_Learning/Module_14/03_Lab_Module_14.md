# Lab Activity: Module 14 — Model Deployment and Production ML Pipelines

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Lab Overview

**Title:** From Training to Serving — SavedModel, TFLite, and REST API

**Duration:** 90–120 minutes

**Platform:** Google Colab (Parts 1–4); optional local Python environment for Part 5

**Deliverable:** Completed Colab notebook (`.ipynb`) with a 1-page written deployment summary submitted to Canvas

**Points:** 100

---

## Learning Objectives

By the end of this lab you will have:

- Saved a Keras model in SavedModel format and inspected its directory structure
- Loaded a SavedModel for inference using both the Keras API and `tf.saved_model.load`
- Converted the model to TFLite and applied dynamic range quantization
- Compared file sizes and inference latency between full and quantized models
- Written a minimal Flask-style prediction function that wraps the model

---

## Prerequisites

Complete the Module 14 video lecture and reading guide. You should understand the difference between SavedModel and `.h5`, and be able to explain what quantization does to model weights.

---

## Part 1 — Train a Reference Model (15 minutes)

### Step 1.1 — Setup

```python
import tensorflow as tf
import numpy as np
import os
import time

print("TensorFlow:", tf.__version__)
tf.random.set_seed(42)
np.random.seed(42)
```

### Step 1.2 — Load and Preprocess Fashion MNIST

```python
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]
print("Train shape:", x_train.shape)
print("Test shape:", x_test.shape)
```

### Step 1.3 — Build and Train

```python
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10,
          validation_split=0.1,
          callbacks=[tf.keras.callbacks.EarlyStopping(patience=3,
                                                       restore_best_weights=True)],
          verbose=1)

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"Test accuracy: {test_acc:.4f}")
```

**Checkpoint:** Confirm test accuracy exceeds 89% before proceeding.

---

## Part 2 — SavedModel Format (20 minutes)

### Step 2.1 — Save in SavedModel Format

```python
SAVE_DIR = 'fashion_model/1'
model.save(SAVE_DIR)
print("Saved to:", SAVE_DIR)
```

### Step 2.2 — Inspect Directory Structure

```python
for root, dirs, files in os.walk('fashion_model'):
    level = root.replace('fashion_model', '').count(os.sep)
    indent = '  ' * level
    print(f"{indent}{os.path.basename(root)}/")
    for f in files:
        size_kb = os.path.getsize(os.path.join(root, f)) / 1024
        print(f"{indent}  {f}  ({size_kb:.1f} KB)")
```

Record the total size of the SavedModel directory. You will compare this to the TFLite sizes in Part 3.

### Step 2.3 — Load with Keras API

```python
model_keras = tf.keras.models.load_model(SAVE_DIR)
preds_keras = model_keras.predict(x_test[:5], verbose=0)
print("Keras predictions (first 5):", np.argmax(preds_keras, axis=1))
print("Actual labels:               ", y_test[:5])
```

### Step 2.4 — Load with `tf.saved_model.load`

```python
loaded = tf.saved_model.load(SAVE_DIR)
print("Signatures:", list(loaded.signatures.keys()))

infer = loaded.signatures['serving_default']
print("Input names:", list(infer.structured_input_signature[1].keys()))
print("Output names:", list(infer.structured_outputs.keys()))

output_key = list(infer.structured_outputs.keys())[0]
result = infer(tf.constant(x_test[:5]))
preds_saved = np.argmax(result[output_key].numpy(), axis=1)
print("SavedModel predictions:", preds_saved)
```

**Question 2.1 (written, in a Markdown cell):** What is the difference between using `tf.keras.models.load_model` and `tf.saved_model.load`? When would you prefer each?

---

## Part 3 — TFLite Conversion (25 minutes)

### Step 3.1 — Basic TFLite Conversion (No Quantization)

```python
converter_base = tf.lite.TFLiteConverter.from_saved_model(SAVE_DIR)
tflite_base = converter_base.convert()

with open('fashion_base.tflite', 'wb') as f:
    f.write(tflite_base)

base_size_kb = len(tflite_base) / 1024
print(f"Base TFLite size: {base_size_kb:.1f} KB")
```

### Step 3.2 — Dynamic Range Quantization

```python
converter_drq = tf.lite.TFLiteConverter.from_saved_model(SAVE_DIR)
converter_drq.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_drq = converter_drq.convert()

with open('fashion_drq.tflite', 'wb') as f:
    f.write(tflite_drq)

drq_size_kb = len(tflite_drq) / 1024
print(f"Dynamic range quantized size: {drq_size_kb:.1f} KB")
print(f"Reduction: {(1 - drq_size_kb / base_size_kb) * 100:.1f}%")
```

### Step 3.3 — Inference with TFLite Interpreter

```python
def tflite_predict(model_path, input_data):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    predictions = []
    for i in range(len(input_data)):
        sample = input_data[i:i+1].astype('float32')
        interpreter.set_tensor(input_details[0]['index'], sample)
        interpreter.invoke()
        out = interpreter.get_tensor(output_details[0]['index'])
        predictions.append(np.argmax(out))
    return np.array(predictions)

preds_base_tflite = tflite_predict('fashion_base.tflite', x_test[:20])
preds_drq_tflite = tflite_predict('fashion_drq.tflite', x_test[:20])
preds_full_model = np.argmax(model.predict(x_test[:20], verbose=0), axis=1)

print("Full model:       ", preds_full_model)
print("TFLite base:      ", preds_base_tflite)
print("TFLite quantized: ", preds_drq_tflite)
print("Actual:           ", y_test[:20])
```

### Step 3.4 — Latency Benchmark

```python
def benchmark_tflite(model_path, inputs, n_runs=50):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    times = []
    for _ in range(n_runs):
        start = time.time()
        interpreter.set_tensor(input_details[0]['index'],
                               inputs[0:1].astype('float32'))
        interpreter.invoke()
        times.append(time.time() - start)
    avg_ms = np.mean(times) * 1000
    return avg_ms

base_ms = benchmark_tflite('fashion_base.tflite', x_test)
drq_ms = benchmark_tflite('fashion_drq.tflite', x_test)
print(f"TFLite base latency:     {base_ms:.2f} ms per sample")
print(f"TFLite quantized latency:{drq_ms:.2f} ms per sample")
```

---

## Part 4 — Summary Table (10 minutes)

### Step 4.1 — Compile Results

```python
savedmodel_size_kb = sum(
    os.path.getsize(os.path.join(root, f))
    for root, _, files in os.walk('fashion_model')
    for f in files
) / 1024

print(f"\n{'Format':<30} {'Size (KB)':>12}")
print("-" * 44)
print(f"{'SavedModel (full)':<30} {savedmodel_size_kb:>12.1f}")
print(f"{'TFLite base':<30} {base_size_kb:>12.1f}")
print(f"{'TFLite dynamic range quant.':<30} {drq_size_kb:>12.1f}")
```

---

## Part 5 — Flask-Style Prediction Function (15 minutes)

This part simulates the logic of a Flask endpoint without requiring a running server. You will write a function that mirrors what a real endpoint would do.

### Step 5.1 — Implement the Handler

```python
import json

def predict_endpoint(json_body: str, model) -> str:
    """
    Simulates a POST /predict endpoint handler.
    Accepts JSON string with 'instances' key.
    Returns JSON string with 'predictions' key.
    """
    try:
        data = json.loads(json_body)
    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON"})

    if 'instances' not in data:
        return json.dumps({"error": "Missing 'instances' key"})

    try:
        instances = np.array(data['instances'], dtype='float32')
    except (ValueError, TypeError) as e:
        return json.dumps({"error": str(e)})

    predictions = model.predict(instances, verbose=0)
    classes = np.argmax(predictions, axis=1).tolist()
    confidences = np.max(predictions, axis=1).round(4).tolist()

    return json.dumps({
        "predictions": classes,
        "confidence": confidences
    })

# Test it
test_payload = json.dumps({
    "instances": x_test[:3].tolist()
})

response = predict_endpoint(test_payload, model_keras)
print("Response:", response)
```

### Step 5.2 — Test Error Handling

```python
# Missing key
r1 = predict_endpoint('{"data": []}', model_keras)
print("Missing key response:", r1)

# Malformed JSON
r2 = predict_endpoint('{not valid json}', model_keras)
print("Bad JSON response:", r2)
```

---

## Part 6 — Deployment Summary (written, 10 minutes)

In a Markdown cell at the end of your notebook, write a **1-page (approximately 300–400 words) deployment summary** that addresses:

1. What format would you use to deploy this Fashion MNIST model to a mobile app, and why?
2. If 10,000 users per minute need to query the model from a web application, what serving infrastructure would you recommend?
3. What accuracy tradeoff, if any, did you observe between the full model and the quantized TFLite model?
4. Name one scenario where a full TFX pipeline would be worth the overhead for a model like this.

---

## Submission Checklist

Before submitting, confirm your notebook contains:

- [ ] Model trained with test accuracy > 89%
- [ ] SavedModel directory structure printed
- [ ] Both TFLite conversions (base and quantized) completed
- [ ] Summary size table printed
- [ ] Latency benchmark results printed
- [ ] Flask handler function tested including error cases
- [ ] Written deployment summary (300–400 words) in Markdown cell
- [ ] Question 2.1 answered in a Markdown cell

---

## Grading Rubric

| Criterion | Points |
|-----------|--------|
| Model trained, accuracy > 89% | 15 |
| SavedModel saved and both load methods demonstrated | 15 |
| TFLite base conversion correct | 15 |
| TFLite quantized conversion with size comparison | 20 |
| Flask handler with error handling tested | 15 |
| Written deployment summary | 20 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: FastAPI Serving with Input Validation

Replace the Flask prediction handler with a FastAPI endpoint that includes Pydantic input validation and automatic OpenAPI documentation.

1. Install FastAPI and Uvicorn: `pip install fastapi uvicorn pydantic`. Define a Pydantic request schema and a FastAPI app that loads the model at startup:

   ```python
   from fastapi import FastAPI
   from pydantic import BaseModel
   import numpy as np
   import tensorflow as tf

   class PredictionRequest(BaseModel):
       instances: list[list[float]]

   app = FastAPI()
   model = tf.keras.models.load_model('mnist_model')

   @app.post('/predict')
   def predict(req: PredictionRequest):
       x = np.array(req.instances, dtype=np.float32)
       preds = model.predict(x)
       return {'predictions': preds.tolist()}
   ```

2. Launch with `uvicorn app:app --reload` and test with `curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"instances": [[...]]}'`.
3. Navigate to `http://localhost:8000/docs` to view the auto-generated Swagger UI. Verify that the endpoint accepts the correct schema and rejects malformed requests with a descriptive error message.
4. Add a second endpoint `GET /model_info` that returns the model's input/output shape and the model's `summary()` output as a string. Use `io.StringIO` to capture the summary.

### Challenge 2: TF Serving with Docker and Version Management

Deploy two versions of your model to TF Serving and observe automatic version switching.

1. Save two slightly different models (e.g., the base model as version 1 and a retrained model with an extra Dense layer as version 2) in the required directory structure:

   ```text
   serving_models/
   └── mnist_model/
       ├── 1/     ← SavedModel version 1
       │   ├── saved_model.pb
       │   └── variables/
       └── 2/     ← SavedModel version 2
           ├── saved_model.pb
           └── variables/
   ```

2. Launch TF Serving with Docker mounting the `serving_models` directory. Send REST predictions to version 1 by appending `/versions/1` to the URL: `http://localhost:8501/v1/models/mnist_model/versions/1:predict`. Verify the response is different from the version 2 endpoint.
3. Delete the version 1 directory from the mounted volume while the container is running. Observe that TF Serving automatically unloads version 1 and continues serving version 2 — verify this by checking the `http://localhost:8501/v1/models/mnist_model` status endpoint.
4. In a Markdown cell, describe the TF Serving "model freshness" policy and explain how automatic version detection enables zero-downtime model updates in production.

### Reflection Questions

1. Compare the developer experience of Flask vs. FastAPI for ML serving: what specific FastAPI features (automatic validation, async support, OpenAPI docs) would have the most impact in a team environment where multiple engineers consume the prediction API?
2. In your TF Serving Docker experiment, what happened to in-flight requests when you deleted version 1 while the server was running? How does TF Serving's configurable grace period (`model_server_config_file` with `version_policy`) protect against request failures during a model update in a production environment?

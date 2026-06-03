# Video Script: Module 14 — Model Deployment and Production ML Pipelines

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Production Notes

- **Runtime target:** 20–24 minutes
- **Format:** Screencast; terminal demo for TF Serving; Colab for TFLite conversion
- **Visual aids:** Architecture diagram: training → SavedModel → Serving layer; mobile inference diagram
- **Code environment:** Google Colab + Docker (conceptual demo)

---

## SEGMENT 1 — Why Deployment Matters (0:00–2:30)

Welcome to Module 14. You have now trained time series models, image classifiers, and NLP models. But training is only half the job. A model that lives only in a Colab notebook delivers zero business value. The second half is deployment — getting your model into an environment where real users or systems can call it, reliably, at scale.

The path from notebook to production involves three distinct challenges. First, **format**: your model needs to be serialized in a way that is language-agnostic and version-stable. Second, **serving**: something needs to handle incoming requests, run inference, and return predictions efficiently. Third, **portability**: sometimes inference happens on a phone or an embedded microcontroller, not a GPU server.

In this module you will learn:

- The SavedModel format and how it differs from `.h5` checkpoints
- TensorFlow Serving for REST and gRPC inference
- TFLite for mobile and edge deployment
- An introduction to TFX pipelines for production ML workflows
- Wrapping a model in a basic REST API with Flask

These topics are not directly tested on the TF Developer Certificate exam, but they are essential context for any engineer moving from academia to industry. Let's begin with the SavedModel format.

---

## SEGMENT 2 — SavedModel Format (2:30–6:00)

[SLIDE: SavedModel directory structure]

When you call `model.save('my_model')` without a `.h5` extension, TensorFlow writes a **SavedModel** — a directory containing the computation graph, weights, and serving signatures. This is the gold-standard format for production.

Let me demonstrate. Start from a simple model trained on MNIST:

```python
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=[28, 28]),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, validation_split=0.1, verbose=0)
```

Now save it:

```python
model.save('saved_model/mnist_v1')
```

[Show the terminal output listing the saved directory]

The SavedModel directory contains:

- `saved_model.pb` — the frozen computation graph in Protocol Buffer format
- `variables/` — the weight files (two files: values and index)
- `assets/` — optional supporting files (vocabularies, lookup tables)

The key advantage over `.h5` is that SavedModel is **language-agnostic**. A Python client, a Java service, or a C++ inference engine can all load the same file. It also captures the serving signature — TensorFlow knows what tensors to feed and what tensors to return.

Load it back:

```python
loaded = tf.saved_model.load('saved_model/mnist_v1')
infer = loaded.signatures['serving_default']
result = infer(tf.constant(x_test[:1]))
print(result)
```

[Pause — show output with dense_1 key]

Notice the output key is `dense_1` — the name of the last layer. In production you would query this key to extract predictions.

---

## SEGMENT 3 — TensorFlow Serving (6:00–10:30)

[SLIDE: TensorFlow Serving architecture diagram]

TensorFlow Serving is Google's production-grade inference server. It loads SavedModels, manages model versioning, and exposes both a REST API on port 8501 and a gRPC endpoint on port 8500. You communicate with it over HTTP — no Python required on the server.

The standard deployment uses Docker. Here is the command to start a TF Serving container with our MNIST model:

```bash
docker pull tensorflow/serving

docker run -t --rm \
  -p 8501:8501 \
  -v "$(pwd)/saved_model:/models/mnist" \
  -e MODEL_NAME=mnist \
  tensorflow/serving
```

[SLIDE: Show the folder mounting and environment variable]

The `-v` flag mounts your SavedModel directory into the container. The container expects the model at `/models/{MODEL_NAME}/{version_number}/`. Our directory structure is `saved_model/mnist_v1/`, so inside the container it maps to `/models/mnist/mnist_v1/` — TF Serving treats `mnist_v1` as version 1.

Once the server is running, you send inference requests via HTTP POST:

```python
import requests
import json
import numpy as np

payload = {
    "instances": x_test[:3].tolist()
}
response = requests.post(
    "http://localhost:8501/v1/models/mnist:predict",
    data=json.dumps(payload)
)
predictions = response.json()['predictions']
predicted_classes = np.argmax(predictions, axis=1)
print("Predictions:", predicted_classes)
print("Actual:     ", y_test[:3])
```

The REST endpoint path follows the pattern `/v1/models/{model_name}:predict`. The request body is `{"instances": [...]}` where instances is a list of input tensors.

TF Serving also supports **model versioning** automatically. If you save `mnist_v2` alongside `v1`, TF Serving loads the highest-numbered version and routes all new requests to it. Older versions stay loaded for a configurable grace period. This enables zero-downtime upgrades — a critical production requirement.

---

## SEGMENT 4 — TFLite for Mobile and Edge (10:30–15:00)

[SLIDE: TFLite conversion pipeline — full model → flatbuffer → quantized]

Mobile devices and embedded microcontrollers have very different constraints than GPU servers: limited RAM, no floating-point unit on some chips, and strict latency budgets. TensorFlow Lite is TensorFlow's solution — it converts a SavedModel into a compact `.tflite` flatbuffer that runs without the full TF runtime.

Here is the basic conversion:

```python
converter = tf.lite.TFLiteConverter.from_saved_model('saved_model/mnist_v1')
tflite_model = converter.convert()

with open('mnist.tflite', 'wb') as f:
    f.write(tflite_model)

print(f"TFLite model size: {len(tflite_model) / 1024:.1f} KB")
```

The resulting file is dramatically smaller than the full SavedModel. Our MNIST model goes from about 1.2 MB to roughly 400 KB.

Now let's add **quantization** to reduce further:

```python
converter = tf.lite.TFLiteConverter.from_saved_model('saved_model/mnist_v1')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_quant_model = converter.convert()

with open('mnist_quant.tflite', 'wb') as f:
    f.write(tflite_quant_model)

print(f"Quantized size: {len(tflite_quant_model) / 1024:.1f} KB")
```

`tf.lite.Optimize.DEFAULT` applies **dynamic range quantization** — weights are stored as 8-bit integers rather than 32-bit floats. This typically reduces model size by 4x with less than 1% accuracy loss.

Running inference with TFLite uses an interpreter rather than the standard Keras API:

```python
interpreter = tf.lite.Interpreter(model_path='mnist_quant.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Run inference on one example
interpreter.set_tensor(input_details[0]['index'],
                       x_test[0:1].reshape(1, 28, 28))
interpreter.invoke()
output = interpreter.get_tensor(output_details[0]['index'])
print("Prediction:", np.argmax(output))
```

Notice the different API: `set_tensor`, `invoke`, `get_tensor`. This lower-level interface reflects TFLite's embedded-system origins.

---

## SEGMENT 5 — TFX Introduction (15:00–18:30)

[SLIDE: TFX component pipeline diagram]

TFX — TensorFlow Extended — is Google's end-to-end platform for production ML pipelines. Where Keras handles model definition and training, TFX handles everything around the model: data validation, preprocessing, training, evaluation, model analysis, and deployment — all as a reproducible, automated pipeline.

A TFX pipeline consists of **components** connected by **artifacts**. Key components include:

- `ExampleGen`: Reads and splits raw data
- `StatisticsGen`: Computes dataset statistics
- `SchemaGen`: Infers data schema for validation
- `ExampleValidator`: Detects anomalies compared to the schema
- `Transform`: Applies preprocessing using `tf.Transform`
- `Trainer`: Trains the model using your Keras code
- `Evaluator`: Compares candidate model to a baseline
- `Pusher`: Deploys the blessed model to TF Serving

[SLIDE: Simplified TFX pipeline code snippet]

A minimal TFX pipeline looks like this:

```python
from tfx.components import CsvExampleGen, Trainer, Pusher
from tfx.proto import trainer_pb2, pusher_pb2
from tfx.orchestration.experimental.interactive.interactive_context import (
    InteractiveContext
)

context = InteractiveContext()
example_gen = CsvExampleGen(input_base='/data/csv')
context.run(example_gen)
```

For this course we will not implement a full TFX pipeline — that is a graduate-level topic. But you should be aware of the pattern: each component reads artifacts from a metadata store and writes new artifacts, creating a complete audit trail of your ML experiment. This is essential for compliance in regulated industries.

---

## SEGMENT 6 — REST API with Flask (18:30–21:30)

[SLIDE: Flask server diagram]

For smaller deployments, a lightweight REST API using Flask is often sufficient. Flask is a Python microframework that you can wrap around any Keras model:

```python
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)
model = tf.saved_model.load('saved_model/mnist_v1')
infer = model.signatures['serving_default']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    instances = np.array(data['instances'], dtype=np.float32)
    output = infer(tf.constant(instances))
    predictions = output['dense_1'].numpy().tolist()
    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

A client calls this endpoint exactly the same way they would call TF Serving, but you control the server code. You can add authentication, preprocessing, logging, and business logic directly in Python.

Flask is not production-grade for high-throughput scenarios — use TF Serving or a managed platform like Vertex AI for that. But for internal tools, demos, and moderate traffic, Flask is simple and effective.

---

## SEGMENT 7 — Wrap-Up and Deployment Decision Guide (21:30–23:00)

[SLIDE: Decision tree — which deployment approach to choose]

To recap: when choosing a deployment strategy, ask three questions.

First: who is calling the model? If it is a backend service over a network, use TF Serving. If it is a mobile app, use TFLite. If it is a small team tool or prototype, use Flask.

Second: how important is latency? TF Serving with gRPC is fastest for server-side inference. TFLite with integer quantization is fastest for on-device inference.

Third: do you need a full ML platform with data validation, lineage tracking, and automated retraining? That is TFX.

In the lab for this module you will save a model as SavedModel, convert it to TFLite, apply quantization, and benchmark the size and speed difference. You will also write a minimal Flask endpoint and test it with Python `requests`.

In Module 15 we explore generative models — autoencoders, VAEs, GANs, and the Transformer architecture that powers modern NLP. See you there.

---

## End of Script

**Total estimated runtime:** 22 minutes

**Key code files referenced:** `module14_deployment.ipynb`

**TF Developer Certificate alignment:** Foundational knowledge — deployment awareness

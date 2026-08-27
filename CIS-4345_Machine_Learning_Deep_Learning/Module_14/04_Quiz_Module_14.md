# Quiz: Module 14 — Model Deployment and Production ML Pipelines

## Course: CIS-4345 Machine Learning and Deep Learning

## Texas Wesleyan University | Professor Nash

---

## Instructions

This quiz contains 10 multiple-choice questions worth 10 points each. Select the single best answer. Distractors are analyzed to support exam preparation.

**Time limit:** 20 minutes

---

## Question 1

Which command saves a Keras model in the SavedModel directory format?

- A) `model.save('model.h5')`
- B) `model.save('model')`
- C) `model.save_weights('model')`
- D) `tf.saved_model.save(model, 'model.pb')`

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. The `.h5` extension forces HDF5 format, which is not compatible with TF Serving or cross-language inference.
- **B:** Correct. Without a `.h5` extension, `model.save()` writes a SavedModel directory.
- **C:** Incorrect. `save_weights` saves only the weight tensors, not the graph or serving signatures.
- **D:** Incorrect. `tf.saved_model.save` is the low-level API; the path should be a directory, not a `.pb` file. The `.pb` file is written inside the directory automatically.

---

## Question 2

A SavedModel directory contains three main items. Which set is correct?

- A) `model.json`, `weights.bin`, `config.yaml`
- B) `saved_model.pb`, `variables/`, `assets/`
- C) `model.h5`, `signatures.pb`, `checkpoints/`
- D) `graph.proto`, `weights.npy`, `metadata.json`

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. These are TensorFlow.js artifact names, not SavedModel.
- **B:** Correct. The `.pb` file holds the frozen computation graph, `variables/` holds weight tensors, and `assets/` holds optional supporting files such as vocabularies.
- **C:** Incorrect. `model.h5` is a separate format entirely. The SavedModel does not include an `.h5` file.
- **D:** Incorrect. These names do not correspond to any TensorFlow serialization format.

---

## Question 3

TensorFlow Serving loads models from a directory following the pattern `/models/{name}/{version}/`. You have saved `model/2/` and `model/3/`. Which version will TF Serving serve by default?

- A) Version 2, because it was deployed first
- B) Version 3, because TF Serving serves the highest-numbered version
- C) Both versions simultaneously, with round-robin load balancing
- D) Neither; TF Serving requires an explicit version flag

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. TF Serving does not prioritize by deployment order.
- **B:** Correct. TF Serving automatically serves the highest-numbered version. Earlier versions remain loaded for rollback during a configurable grace period.
- **C:** Incorrect. TF Serving serves the latest version by default; multi-version routing requires explicit configuration.
- **D:** Incorrect. TF Serving auto-discovers and serves the latest version without any flags.

---

## Question 4

What is the REST API request body format expected by TensorFlow Serving?

- A) `{"data": [...]}`
- B) `{"inputs": {"x": [...]}}` (always required)
- C) `{"instances": [...]}` for batched row-based inputs
- D) `{"tensor": [...], "shape": [...]}`

**Correct Answer:** C

**Distractor Analysis:**

- **A:** Incorrect. `"data"` is not a recognized key in the TF Serving REST protocol.
- **B:** Incorrect. `"inputs"` is used for named multi-input models, not the standard single-input case.
- **C:** Correct. The standard format uses `"instances"` as the key for a list of input examples.
- **D:** Incorrect. The REST API does not use a raw tensor + shape format; that is closer to the gRPC protocol buffer format.

---

## Question 5

You apply `converter.optimizations = [tf.lite.Optimize.DEFAULT]` to a TFLite converter. What does this do?

- A) Prunes neurons with near-zero weights to reduce layer count
- B) Applies dynamic range quantization, storing weights as INT8 instead of FP32
- C) Converts the model to use 16-bit floating point activations
- D) Enables GPU acceleration in the TFLite runtime

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Pruning is a separate technique (sparsity-based compression) not triggered by this flag.
- **B:** Correct. `Optimize.DEFAULT` enables dynamic range quantization — weights are quantized to INT8 at conversion time; activations are quantized dynamically at runtime.
- **C:** Incorrect. Float16 quantization requires `converter.target_spec.supported_types = [tf.float16]` in addition to the optimization flag.
- **D:** Incorrect. GPU delegate configuration is a runtime interpreter setting, not a converter optimization.

---

## Question 6

After creating a TFLite interpreter, you must call `interpreter.allocate_tensors()` before running inference. Why?

- A) It downloads the model weights from the cloud
- B) It allocates memory buffers for input and output tensors based on the model graph
- C) It connects the interpreter to a GPU or DSP accelerator
- D) It validates that the model file has not been corrupted

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. TFLite operates entirely locally; there is no network call.
- **B:** Correct. `allocate_tensors()` analyzes the model graph and allocates fixed memory for each tensor, enabling the low-overhead inference loop on resource-constrained devices.
- **C:** Incorrect. Hardware delegate configuration uses separate `add_delegate()` calls, not `allocate_tensors()`.
- **D:** Incorrect. Model integrity is not checked by this call; it is purely a memory allocation step.

---

## Question 7

Which TFX component is responsible for detecting anomalies in incoming data relative to the expected schema?

- A) `StatisticsGen`
- B) `SchemaGen`
- C) `ExampleValidator`
- D) `Transform`

**Correct Answer:** C

**Distractor Analysis:**

- **A:** Incorrect. `StatisticsGen` computes summary statistics; it does not perform anomaly detection.
- **B:** Incorrect. `SchemaGen` infers the schema (expected types, ranges, vocabularies) from training data statistics. It produces the schema that `ExampleValidator` uses.
- **C:** Correct. `ExampleValidator` compares incoming data statistics against the schema and flags deviations such as missing values, out-of-range features, or type mismatches.
- **D:** Incorrect. `Transform` applies feature engineering operations; it does not validate data.

---

## Question 8

You want to serve a Keras image classifier via a REST API that handles roughly 50 requests per minute from an internal analytics dashboard. Which approach is most appropriate?

- A) TFX Pusher → Vertex AI Prediction
- B) TFLite interpreter running on a mobile device
- C) Flask application with `model.predict()` loaded at startup
- D) gRPC TF Serving cluster with load balancing

**Correct Answer:** C

**Distractor Analysis:**

- **A:** Incorrect. Vertex AI is a managed ML platform appropriate for high-scale production, which is overkill for 50 requests/minute internal tooling.
- **B:** Incorrect. TFLite is for on-device inference; it does not serve REST requests from a server.
- **C:** Correct. Flask with a model loaded at startup is well-suited for low-to-moderate internal traffic. It is simple to develop and maintain.
- **D:** Incorrect. A gRPC cluster is appropriate for thousands of requests per second, not 50 per minute.

---

## Question 9

What is the primary advantage of TensorFlow Serving's gRPC interface over its REST interface?

- A) gRPC supports more model types than REST
- B) gRPC uses Protocol Buffers and HTTP/2, resulting in lower latency and smaller payload sizes
- C) gRPC does not require the model to have a serving signature
- D) gRPC allows the model to be updated without restarting the server

**Correct Answer:** B

**Distractor Analysis:**

- **A:** Incorrect. Both REST and gRPC interfaces support the same SavedModel types.
- **B:** Correct. gRPC serializes data using Protocol Buffers (binary, compact) over HTTP/2 (multiplexed, low overhead), reducing both serialization time and network transfer size compared to JSON over HTTP/1.1.
- **C:** Incorrect. Both interfaces require the model to have a serving signature.
- **D:** Incorrect. Both REST and gRPC benefit from TF Serving's hot model reload; this is not specific to gRPC.

---

## Question 10

The ML Metadata (MLMD) store in TFX serves which primary purpose?

- A) Caching preprocessed batches to speed up training
- B) Storing the trained model's weights in a versioned database
- C) Recording the lineage of artifacts produced and consumed by each pipeline component
- D) Monitoring model performance in production and triggering alerts

**Correct Answer:** C

**Distractor Analysis:**

- **A:** Incorrect. Batch caching is handled by `tf.data` prefetching, not MLMD.
- **B:** Incorrect. Model weights are stored as SavedModel artifacts in a file system or object store; MLMD stores metadata about those artifacts, not the weights themselves.
- **C:** Correct. MLMD records what each component produced (artifact), what it consumed, and what parameters it used, creating a complete audit trail from raw data to deployed model.
- **D:** Incorrect. Production monitoring and alerting are typically handled by separate tools (Prometheus, Cloud Monitoring), not MLMD.

---

## Answer Key

| Question | Answer |
|----------|--------|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | C |
| 5 | B |
| 6 | B |
| 7 | C |
| 8 | C |
| 9 | B |
| 10 | C |

---

### Question 11 (5 points)

A Flask endpoint receives a JSON body `{"instances": [[0.23, 1.45, -0.87, 0.56]]}` and must return a prediction. Which code correctly handles this input and returns a JSON prediction?

- A) `data = request.json; pred = model.predict(data); return jsonify(pred.tolist())`
- B) `data = request.get_json(); instances = np.array(data['instances']); pred = model.predict(instances); return jsonify({'predictions': pred.tolist()})`
- C) `data = request.form['instances']; pred = model(data); return jsonify(pred)`
- D) `pred = model.predict(request.json['instances'][0]); return jsonify(pred)`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `request.get_json()` parses the JSON body into a Python dict. `data['instances']` extracts the list of input examples. `np.array(...)` converts it to a NumPy array suitable for `model.predict()`. Wrapping the result in `{'predictions': pred.tolist()}` converts the NumPy array to a JSON-serializable Python list in the expected response format.
  - *Why A is incorrect:* `model.predict(data)` passes the entire dict to the model, not just the instances array. `model.predict()` expects a NumPy array or tensor, not a Python dict. This would raise a TypeError.
  - *Why C is incorrect:* `request.form` accesses HTML form submissions, not JSON body data. For a JSON endpoint, `request.get_json()` is the correct method. Additionally, `model(data)` calls the model directly (eager inference on a single sample) rather than using `model.predict()` for batched inference.
  - *Why D is incorrect:* `request.json['instances'][0]` extracts only the first sample as a Python list `[0.23, 1.45, -0.87, 0.56]` (shape `(4,)`). `model.predict()` requires a batch dimension — the input should be shape `(batch_size, 4)`. Passing a 1D list would raise a shape error for most model architectures.

---

### Question 12 (5 points)

When a SavedModel is loaded with `tf.saved_model.load('model_dir')`, the result is a `tf.Module` object. How do you run inference with it?

- A) Call `loaded_model.predict(x)` as you would with a Keras model.
- B) Call `loaded_model.signatures['serving_default'](tf.constant(x))` to invoke the model using its serving signature.
- C) Call `tf.lite.Interpreter(loaded_model).invoke()` to convert it to TFLite for inference.
- D) Access `loaded_model.layers[-1].output` to get predictions.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `tf.saved_model.load()` returns a generic `tf.Module`, not a Keras model. It does not have a `.predict()` method. Inference is performed via the serving signatures, which are callable functions stored in `model.signatures`. The `'serving_default'` key is the default export signature, and calling it with a `tf.constant` tensor returns a dict of output tensors.
  - *Why A is incorrect:* `.predict()` is a Keras model method. `tf.saved_model.load()` returns a `tf.Module`, which does not have `.predict()`. For Keras-style inference, use `tf.keras.models.load_model()` instead.
  - *Why C is incorrect:* `tf.saved_model.load()` returns a loaded model object, not a path string. `tf.lite.Interpreter` accepts a path to a `.tflite` file or its bytes content, not a `tf.Module` object. These are completely separate conversion and inference paths.
  - *Why D is incorrect:* `tf.Module` objects loaded via `tf.saved_model.load()` do not have a `.layers` attribute. Layer access is only available on Keras model objects loaded with `tf.keras.models.load_model()`.

---

### Question 13 (5 points)

What does the `@tf.function` decorator do when applied to a Python function that contains TensorFlow operations?

- A) It schedules the function to run asynchronously on a background thread.
- B) It compiles the function's TensorFlow operations into a static computation graph using `tf.autograph`, enabling faster repeated execution compared to eager mode.
- C) It automatically converts the function to a TFLite-compatible format for mobile deployment.
- D) It applies gradient checkpointing to the function to reduce memory usage during backpropagation.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `@tf.function` traces the function once to create a `ConcreteFunction` (a compiled computation graph). On subsequent calls with the same input signature, the pre-compiled graph is executed directly without Python overhead. This is particularly important for serving: the serving signature in a SavedModel is a `tf.function`, which is why inference is fast even without calling through the full Python Keras stack.
  - *Why A is incorrect:* `@tf.function` does not schedule asynchronous execution. The function still runs synchronously but as a compiled graph rather than eager Python. TensorFlow's async execution is a separate feature controlled by `tf.config.experimental.set_synchronous_execution(False)`.
  - *Why C is incorrect:* TFLite conversion is a separate process performed by `TFLiteConverter`. A `@tf.function` decorated function can be included in a SavedModel and then converted to TFLite, but the decorator itself does not produce TFLite output.
  - *Why D is incorrect:* Gradient checkpointing is a memory optimization technique that recomputes intermediate activations during the backward pass instead of storing them. It is configured via `tf.recompute_grad()` or similar utilities, not `@tf.function`.

---

### Question 14 (5 points)

A developer wants to add a serving signature to a SavedModel that accepts a raw string (a single review text) and returns a sentiment probability. Which approach correctly adds this signature before saving?

- A) Add a `predict` method to the model class and decorate it with `@model.predict_function`.
- B) Create a `tf.function` with `input_signature=[tf.TensorSpec(shape=[None], dtype=tf.string)]`, wrap the full preprocessing + inference pipeline, and assign it to `model.serving_signature` before saving.
- C) Pass a `signatures` argument to `tf.saved_model.save(model, path, signatures={'serving_default': serving_fn})` where `serving_fn` is a `tf.function` with a concrete input signature.
- D) Add the serving function to `model.layers` as a `Lambda` layer so it becomes part of the Keras model graph.

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* `tf.saved_model.save()` accepts a `signatures` dict that maps string keys to concrete `tf.function` instances. The canonical pattern is: define `@tf.function(input_signature=[...])` function that runs preprocessing and inference, then pass it as `signatures={'serving_default': serving_fn}`. The result is a SavedModel that accepts raw strings via its REST or gRPC serving interface.
  - *Why A is incorrect:* There is no `@model.predict_function` decorator in the Keras or TensorFlow API. This is a fictional attribute name.
  - *Why B is incorrect:* Keras models do not have a `serving_signature` attribute. Signatures are added at save time via the `signatures` argument to `tf.saved_model.save()`, not by modifying the model object beforehand.
  - *Why D is incorrect:* `Lambda` layers add Python-callable functions to the model graph, but they do not configure serving signatures or handle string inputs for TF Serving. Serving signatures require `tf.function` specifications with concrete input types.

---

### Question 15 (5 points)

A Docker container running TF Serving exposes port 8501 (REST) and 8500 (gRPC). A Python client sends a REST request to predict on a batch of 10 images. Which URL pattern is correct?

- A) `http://localhost:8501/models/my_model:predict`
- B) `http://localhost:8501/v1/models/my_model:predict`
- C) `http://localhost:8500/v1/models/my_model:predict`
- D) `http://localhost:8501/v1/models/my_model/versions/latest:predict`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* TF Serving's REST API follows the URL pattern `http://host:port/v1/models/{model_name}:predict`. Port 8501 is the REST port. The `/v1/` prefix is part of the API versioning scheme. The `:predict` suffix specifies the classify/regress/predict endpoint. This is the exact URL used in every TF Serving REST tutorial.
  - *Why A is incorrect:* This URL is missing the required `/v1/` API version prefix. TF Serving's REST API requires this prefix — requests without it return 404.
  - *Why C is incorrect:* Port 8500 is the gRPC port, not the REST port. Sending an HTTP/1.1 REST request to the gRPC port would fail because gRPC uses HTTP/2 with Protocol Buffers, not plain JSON.
  - *Why D is incorrect:* While specifying a version number is valid (`/versions/1`), the path uses `latest` which is not a valid version specifier in TF Serving. Valid version specifiers are integer numbers (e.g., `/versions/2`). To serve the latest version (the default behavior), simply omit the version path segment entirely.

---

### Question 16 (5 points)

Which command launches a TF Serving Docker container that serves a model stored at `/home/user/models/my_model` on the host machine?

- A) `docker run -p 8501:8501 --model tensorflow/serving --model_base_path=/home/user/models/my_model`
- B) `docker run -p 8501:8501 -v /home/user/models:/models/my_model -e MODEL_NAME=my_model tensorflow/serving`
- C) `docker run -p 8501:8501 tensorflow/serving --model_dir=/home/user/models/my_model`
- D) `docker run -p 8501:8501 --volume=/home/user/models tensorflow/serving:my_model`

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The correct pattern mounts the host directory into the container using `-v host_path:container_path`, sets `MODEL_NAME` via environment variable `-e MODEL_NAME=my_model`, and uses the `tensorflow/serving` image. TF Serving looks for models at `/models/{MODEL_NAME}` inside the container, so mounting `/home/user/models` to `/models/my_model` makes the model available at the expected path.
  - *Why A is incorrect:* `--model` is not a Docker flag — it would be interpreted as an image name argument. The TF Serving image name is `tensorflow/serving`; model configuration is passed through volume mounts and environment variables, not `--model`.
  - *Why C is incorrect:* `--model_dir` is not a valid Docker flag and would not be passed to TF Serving correctly. Model path configuration in a Docker deployment uses volume mounts (`-v`) so the host filesystem is accessible inside the container.
  - *Why D is incorrect:* `tensorflow/serving:my_model` attempts to use `my_model` as a Docker image tag (e.g., version tag), not as a model name. Docker image tags are for image versions, not model configuration. The correct image tag is `tensorflow/serving:latest` or a specific TF version.

---

### Question 17 (5 points)

What does `model.get_concrete_function()` return, and why is it useful for deployment?

- A) It returns the model's training configuration (optimizer, loss, metrics) as a Python dict.
- B) It traces the `tf.function` with a specific input signature and returns a `ConcreteFunction` that is fully serializable and can be included in a SavedModel's serving signatures.
- C) It compiles the model to a `.pb` protobuf file and saves it to the current directory.
- D) It returns a Python function wrapper that converts inputs to NumPy arrays before calling `model.predict()`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* `get_concrete_function()` traces a `tf.function` with specific concrete input types (specified via `tf.TensorSpec`) and returns a `ConcreteFunction` — a compiled, type-specialized version of the function. This is the form required for SavedModel serving signatures. The `ConcreteFunction` cannot accept inputs of different types or shapes than what it was traced with, making it safe and efficient for production serving.
  - *Why A is incorrect:* Training configuration is accessed via `model.get_config()`. `get_concrete_function()` is about traced computation graphs, not training metadata.
  - *Why C is incorrect:* `get_concrete_function()` returns a Python `ConcreteFunction` object — it does not write any files to disk. File writing happens when `tf.saved_model.save()` is called with the concrete function.
  - *Why D is incorrect:* `get_concrete_function()` has no connection to NumPy conversion. It traces TensorFlow computation graphs. The result is a TensorFlow-internal object, not a Python wrapper for NumPy operations.

---

### Question 18 (5 points)

A production ML system uses TFX. After a new model passes the `Evaluator` blessing check, which TFX component physically copies the model artifacts to the serving location?

- A) `Trainer` — it writes the model directly to the serving location during training.
- B) `Evaluator` — it both evaluates and deploys the model if it passes the blessing check.
- C) `Pusher` — it reads the blessed model artifact and copies it to the configured push destination.
- D) `Transform` — it finalizes the model by attaching the preprocessing graph and pushing the combined artifact.

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* In a TFX pipeline, the `Pusher` component is responsible for model deployment. It receives the `ModelBlessing` artifact from the `Evaluator` and, if the model is blessed, copies the trained model to the serving infrastructure (TF Serving directory, Google Cloud Storage, Vertex AI endpoints, etc.). This separation of concerns — evaluation separate from deployment — is a key production ML pipeline design principle.
  - *Why A is incorrect:* `Trainer` writes model artifacts to the pipeline's artifact store (a staging directory), not to the production serving location. The `Trainer` has no awareness of the deployment destination.
  - *Why B is incorrect:* `Evaluator` only produces a `ModelBlessing` artifact (a pass/fail signal). It does not physically copy any model files. Deployment is strictly `Pusher`'s responsibility.
  - *Why D is incorrect:* `Transform` applies feature engineering and produces `TransformGraph` artifacts that are used by the `Trainer` for consistent preprocessing. It has no role in the final model deployment step.

---

### Question 19 (5 points)

When implementing full integer quantization (INT8 for both weights and activations) with TFLite, what is the purpose of the `representative_dataset` generator?

- A) It provides additional training data to fine-tune the model weights during quantization.
- B) It provides a calibration dataset that the converter uses to observe the actual range of activation values throughout the network, enabling accurate INT8 quantization of activations.
- C) It replaces the test set evaluation, measuring accuracy of the quantized model during conversion.
- D) It specifies the distribution of input pixel values so the TFLite runtime can optimize memory allocation at inference time.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Dynamic range quantization can quantize weights to INT8 without data because weight ranges are known from the trained model. However, activation quantization requires knowing the typical range of activations during inference. The `representative_dataset` provides 100–500 representative inputs that the converter runs through the model to observe activation value ranges at each layer. These ranges are then used to select appropriate INT8 scale factors (quantization parameters) for each activation tensor.
  - *Why A is incorrect:* The `representative_dataset` is used for calibration only — the model weights are not updated during conversion. It is a post-training process; no backpropagation occurs during TFLite conversion.
  - *Why C is incorrect:* The `representative_dataset` is used during conversion calibration, not for accuracy evaluation. To measure quantized model accuracy, you must run the TFLite interpreter on a separate test set after conversion is complete.
  - *Why D is incorrect:* Memory allocation in TFLite is handled by `allocate_tensors()` based on the model graph structure. The `representative_dataset` is used for determining quantization scale factors, not for memory layout optimization.

---

### Question 20 (5 points)

A developer wants to serve predictions from a Keras model via a REST API that will receive requests from a browser-based JavaScript application. Which cross-origin concern must be addressed in the Flask server code?

- A) The model must be converted to TensorFlow.js format because Flask cannot serve Keras models to browser clients.
- B) CORS (Cross-Origin Resource Sharing) headers must be added to Flask responses using `flask-cors` or manual header injection to allow the browser to receive responses from a different origin.
- C) The Flask server must run on port 443 (HTTPS) to be accessible from browsers running on localhost.
- D) The Keras model must be wrapped in a TFX Pusher component before it can respond to browser HTTP requests.

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Browsers enforce the Same-Origin Policy by default: JavaScript running at `http://app.example.com` cannot receive responses from `http://api.example.com:5000` unless the server explicitly allows it via CORS headers. Flask does not add these headers by default. The `flask-cors` extension (`from flask_cors import CORS; CORS(app)`) adds the necessary `Access-Control-Allow-Origin` headers to all responses. Without this, browser fetch requests to the Flask API will be blocked by the browser's CORS enforcement.
  - *Why A is incorrect:* Flask can serve predictions from any Python-loaded model to any HTTP client, including browsers. TensorFlow.js is only needed when the model must run in the browser itself (client-side inference). Server-side inference with Flask is completely valid for browser-facing APIs.
  - *Why C is incorrect:* While HTTPS is best practice for production, Flask development servers run on port 5000 by default (not 443) and are accessible from browsers over HTTP on localhost without any special configuration. Port 443 requires SSL certificate setup and is a production concern, not a requirement for development.
  - *Why D is incorrect:* TFX Pusher is a pipeline component for automated deployment to serving infrastructure. It has no role in the day-to-day request-response cycle of a Flask application. Flask directly calls `model.predict()` without any TFX involvement.

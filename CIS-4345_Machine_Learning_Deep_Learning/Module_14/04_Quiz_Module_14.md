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

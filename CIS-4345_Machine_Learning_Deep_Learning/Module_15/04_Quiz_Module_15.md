# Quiz: Module 15 - Model Deployment: TFLite and TF Serving
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

**Question 1**
When saving a Keras model with `model.save('my_model/')` (no file extension), what format is created and what does the resulting directory contain?
*   A) An H5 file is created at `my_model/` — a single HDF5 binary containing weights and architecture in one file.
*   B) A TensorFlow SavedModel directory is created containing `saved_model.pb` (the computation graph) and a `variables/` subdirectory (the weights) — the recommended format for TF Serving and TFLite conversion.
*   C) A TFLite flatbuffer file is created at `my_model/model.tflite` — TensorFlow automatically converts to mobile format when no extension is specified.
*   D) A Keras JSON config file is created at `my_model/config.json` — architecture only, without weights, which must be saved separately with `model.save_weights()`.
*   **Correct Answer:** B) The SavedModel format is TensorFlow's standard serialization: `saved_model.pb` stores the TensorFlow graph (operations and structure), while `variables/` stores the trained weight tensors. To save in H5 format instead, the filename must end in `.h5` (e.g., `model.save('my_model.h5')`).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* H5 format creates a single file, not a directory, and requires the `.h5` extension in the filename. Without an extension, TensorFlow defaults to SavedModel directory format.
    *   *Why B is correct:* `model.save('path/')` → SavedModel directory. Verify the structure with `ls my_model/` — you will see `saved_model.pb` and `variables/`. This format is required for `TFLiteConverter.from_saved_model()` and TensorFlow Serving.
    *   *Why C is incorrect:* TFLite conversion is not automatic — it requires an explicit `TFLiteConverter` call. `model.save()` never produces a `.tflite` file.
    *   *Why D is incorrect:* `model.save()` always saves both architecture and weights. Saving architecture-only JSON requires `model.to_json()`, which is a separate method unrelated to `model.save()`.

---

**Question 2**
Which of the following is the most accurate definition of **TensorFlow Lite (TFLite)**?
*   A) A full TensorFlow runtime identical to the desktop version, packaged as a mobile SDK that allows Android and iOS apps to train new models directly on-device using GPU acceleration.
*   B) A lightweight inference framework that converts trained TensorFlow SavedModels to a compact `.tflite` flatbuffer format for deployment on mobile devices, embedded systems, and microcontrollers — supporting quantization to reduce model size and inference latency.
*   C) A cloud-based model hosting service managed by Google that automatically scales TensorFlow model serving infrastructure based on incoming request volume.
*   D) A TensorFlow debugging tool that profiles model inference performance on desktop hardware, identifying bottleneck layers and recommending architectural optimizations.
*   **Correct Answer:** B) TFLite is purpose-built for inference on resource-constrained hardware — not training, not cloud serving. The conversion pipeline: SavedModel → `TFLiteConverter` → `.tflite` file → deployed to device where the `TFLite Interpreter` runs predictions. Post-training quantization (int8/float16) further reduces model size and latency.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* TFLite is an inference-only runtime — it does not support on-device training. Training requires the full TensorFlow runtime. TFLite's entire design purpose is to minimize binary size and memory footprint for inference.
    *   *Why B is correct:* Key TFLite facts for the exam: (1) input must be SavedModel format; (2) output is a `.tflite` flatbuffer; (3) `TFLiteConverter.from_saved_model(saved_model_dir)` is the conversion entry point; (4) `tf.lite.Optimizer.DEFAULT` applies post-training quantization.
    *   *Why C is incorrect:* This describes Google Cloud AI Platform or Vertex AI — managed cloud serving infrastructure. TFLite is specifically for on-device (edge) inference, the opposite of cloud serving.
    *   *Why D is incorrect:* This describes the TensorFlow Profiler, a separate tool for performance analysis. TFLite is a deployment format and runtime, not a profiling or debugging utility.

---

**Question 3**
A developer has saved a trained image classifier as a TensorFlow SavedModel at `'./classifier/'`. Which code correctly converts it to TFLite format with default post-training quantization applied?

```python
# Option A
import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_saved_model('./classifier/')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
with open('classifier.tflite', 'wb') as f:
    f.write(tflite_model)
```

```python
# Option B
import tensorflow as tf
model = tf.keras.models.load_model('./classifier/')
tflite_model = model.to_tflite(quantize=True)
tflite_model.save('classifier.tflite')
```

```python
# Option C
import tensorflow as tf
converter = tf.lite.TFLiteConverter.from_keras_model('./classifier/')
tflite_model = converter.convert(optimize=True)
open('classifier.tflite', 'w').write(tflite_model)
```

```python
# Option D
import tensorflow as tf
tflite_model = tf.lite.convert_saved_model('./classifier/', quantize=True)
tflite_model.export('classifier.tflite')
```

*   **Correct Answer:** A) The correct TFLite conversion pipeline: (1) `TFLiteConverter.from_saved_model(saved_model_dir)` — accepts a directory path string, not a loaded model object; (2) set `converter.optimizations` as a list before converting; (3) `converter.convert()` returns raw bytes; (4) write bytes in binary mode (`'wb'`).
*   **Distractor Analysis:**
    *   *Why A is correct:* This is the exact pattern from the TensorFlow Lite documentation. The `optimizations` attribute must be set before calling `convert()`. Writing with `'wb'` is required because `.tflite` files are binary, not text.
    *   *Why B is incorrect:* `model.to_tflite()` is not a valid Keras method. TFLite conversion requires the `TFLiteConverter` class — it cannot be called as a method on a loaded Keras model object.
    *   *Why C is incorrect:* `TFLiteConverter.from_keras_model()` accepts a Keras model object, not a string path. Additionally, `convert(optimize=True)` is not valid — optimizations must be set as `converter.optimizations = [...]` before calling `convert()` with no arguments.
    *   *Why D is incorrect:* `tf.lite.convert_saved_model()` is not a valid TensorFlow function. There is no top-level `tf.lite.convert_*` function — conversion always goes through the `TFLiteConverter` class.

---

**Question 4**
After converting a model to TFLite format, a developer needs to run inference using the TFLite Interpreter. What is the correct order of operations?
*   A) Load the `.tflite` file with `tf.lite.Interpreter` → call `model.predict(input_data)` directly on the interpreter → retrieve results from the return value.
*   B) Load the `.tflite` file with `tf.lite.Interpreter` → call `allocate_tensors()` → get input/output tensor details → set input tensor with `set_tensor()` → call `invoke()` → retrieve output with `get_tensor()`.
*   C) Load the `.tflite` file with `tf.keras.models.load_model()` → compile with `model.compile()` → run `model.predict(input_data)` as normal.
*   D) Load the `.tflite` file with `tf.lite.Interpreter` → call `run(input_data)` which handles tensor allocation, inference, and output retrieval in a single call.
*   **Correct Answer:** B) The TFLite Interpreter has a lower-level API than Keras — there is no `predict()` method. The mandatory sequence: `interpreter = tf.lite.Interpreter(model_path='model.tflite')` → `interpreter.allocate_tensors()` → `input_details = interpreter.get_input_details()` → `interpreter.set_tensor(input_details[0]['index'], input_data)` → `interpreter.invoke()` → `output = interpreter.get_tensor(output_details[0]['index'])`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `tf.lite.Interpreter` does not have a `predict()` method. The `predict()` API belongs to Keras `Model` objects. The TFLite Interpreter requires explicit tensor manipulation.
    *   *Why B is correct:* `allocate_tensors()` must be called before any tensor operations — it initializes the internal memory layout. `invoke()` runs one forward pass. The input must be set fresh before each `invoke()` call.
    *   *Why C is incorrect:* `.tflite` files cannot be loaded with `tf.keras.models.load_model()`. That function loads SavedModel directories or `.h5` files. A `.tflite` flatbuffer requires the `tf.lite.Interpreter` API.
    *   *Why D is incorrect:* `interpreter.run()` is not a valid TFLite Interpreter method. There is no single-call convenience method — tensor allocation, input setting, invocation, and output retrieval are always separate steps.

---

**Question 5**
A team trains a large image classification model (45 MB) for a mobile app. After TFLite conversion with `converter.optimizations = [tf.lite.Optimize.DEFAULT]`, the `.tflite` file is 11 MB. The model's top-1 accuracy on the test set drops from 91.2% to 90.8%. What does this result indicate, and is the trade-off acceptable?
*   A) The quantization has failed — a 75% size reduction always indicates severe model corruption, and the team must retrain from scratch without quantization.
*   B) The result is expected and the trade-off is typically acceptable. `DEFAULT` optimization applies post-training quantization (float32 → int8), which reduces model size by roughly 4x. A 0.4 percentage point accuracy drop is a normal and small cost for 75% size reduction and significantly faster mobile inference.
*   C) The size reduction is too aggressive — the team should use `tf.lite.Optimize.OPTIMIZE_FOR_SIZE` instead, which achieves better accuracy preservation than `DEFAULT` by only quantizing weights, not activations.
*   D) The `.tflite` file at 11 MB is still too large for mobile deployment. The team must use knowledge distillation to train a smaller student model before applying TFLite conversion.
*   **Correct Answer:** B) Post-training quantization with `DEFAULT` is the standard first approach: it quantizes both weights and activations from float32 to int8, typically achieving 3–4x size reduction with less than 1% accuracy loss on most vision models. An 11 MB model is well within acceptable mobile app bundle sizes (Play Store and App Store both support this). The 0.4% accuracy drop is negligible in most production contexts.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A 75% size reduction is exactly what `DEFAULT` quantization is designed to produce — it is a success, not a failure. Model corruption from quantization would manifest as dramatically higher error rates (e.g., accuracy dropping from 91% to 50%), not a 0.4 point drop.
    *   *Why B is correct:* The real-world rule of thumb: if post-training quantization accuracy loss is under 1–2%, the trade-off is almost always acceptable for production mobile deployment. The size and latency benefits (faster inference, lower battery use, smaller app download) typically outweigh a fraction-of-a-percent accuracy cost.
    *   *Why C is incorrect:* `tf.lite.Optimize.OPTIMIZE_FOR_SIZE` is not a distinct optimization constant in the TFLite API — `tf.lite.Optimize.DEFAULT` is the standard flag. Additionally, quantizing only weights (not activations) is achievable via float16 quantization, but it does not consistently produce better accuracy than int8 `DEFAULT`.
    *   *Why D is incorrect:* 11 MB is a perfectly reasonable mobile model size — many production apps ship TFLite models in the 5–50 MB range. Knowledge distillation is a valid technique for further compression, but it is not required at 11 MB. The team should deploy and collect real-world metrics before pursuing further compression.

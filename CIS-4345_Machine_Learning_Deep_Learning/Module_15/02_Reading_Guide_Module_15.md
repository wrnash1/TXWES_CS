# Reading Guide: Module 15 - Model Deployment: TFLite and TF Serving
## Course: CIS-4345_Machine_Learning_Deep_Learning (TensorFlow Developer Certificate)

---

### Introduction
Welcome to **Module 15 - Model Deployment: TFLite and TF Serving**! After training a high-performing model, the final engineering challenge is getting it into production — whether that means serving predictions over a REST API, running inference on a mobile device, or deploying to an embedded system. This module covers the two primary TensorFlow deployment paths: **TensorFlow Serving** for server-side REST/gRPC deployment and **TensorFlow Lite** for mobile and edge device inference.

While model deployment is not one of the four core TensorFlow Developer Certificate exam task categories, understanding SavedModel format, TFLite conversion, and serving infrastructure is increasingly tested in the professional exam tier and is essential for real-world ML engineering.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **TensorFlow SavedModel**: The standard TensorFlow model serialization format that saves the full model — architecture, weights, and computation graph — as a directory. Saved with `model.save('my_model/')` (no extension = SavedModel format). This is the recommended format for TensorFlow Serving and TFLite conversion; it preserves custom layers and training configuration unlike H5.

*   **Keras H5 format**: An alternative model serialization format that saves the model as a single `.h5` (HDF5) file using `model.save('my_model.h5')`. H5 is simpler for storage and portability but does not support all TensorFlow features. The SavedModel format is preferred for deployment pipelines; H5 is common for quick model sharing and checkpointing.

*   **TensorFlow Lite (TFLite)**: A lightweight inference framework for deploying TensorFlow models on mobile devices (Android/iOS), embedded systems (Raspberry Pi), and microcontrollers. TFLite converts a SavedModel to a `.tflite` flatbuffer file using `TFLiteConverter.from_saved_model()`. Supports quantization (int8/float16) to reduce model size and improve inference speed on constrained hardware.

*   **TFLite Converter**: The Python API (`tf.lite.TFLiteConverter`) that converts a SavedModel or Keras model to TFLite format. Key options include `optimizations=[tf.lite.Optimize.DEFAULT]` for post-training quantization. The converted flatbuffer is written to disk and loaded by the TFLite Interpreter at runtime.

*   **TensorFlow Serving**: A production-grade model serving system that loads SavedModel directories and exposes predictions via REST (`/v1/models/MODEL_NAME:predict`) or gRPC endpoints. Deployed as a Docker container. The server handles batching, versioning, and hot-swapping of new model versions without downtime.

*   **Post-training quantization**: A TFLite optimization technique that reduces model weights from 32-bit floats to 8-bit integers (or float16) after training, shrinking model size by up to 4x and speeding up inference on mobile hardware. Applied by setting `converter.optimizations = [tf.lite.Optimize.DEFAULT]` before calling `converter.convert()`.

---

### 2. Certification Exam Tips
*   **SavedModel vs H5:** Know the difference: `model.save('path/')` (no extension) creates a SavedModel directory; `model.save('path.h5')` creates an H5 file. TFLite conversion and TF Serving both require SavedModel format. The exam may present code that calls `converter.from_saved_model(saved_model_dir)` — recognize that `saved_model_dir` must be a directory path, not an `.h5` filename.
*   **TFLite Conversion Pipeline:** The three-step pattern: (1) `converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)`, (2) optionally set `converter.optimizations`, (3) `tflite_model = converter.convert()` → write bytes to a `.tflite` file. The exam tests whether students can identify the correct converter class and method.
*   **TFLite Interpreter:** Loading and running a `.tflite` model requires the `tf.lite.Interpreter` API: `interpreter = tf.lite.Interpreter(model_path='model.tflite')` → `interpreter.allocate_tensors()` → get input/output details → `interpreter.set_tensor()` → `interpreter.invoke()` → `interpreter.get_tensor()`. This is different from `model.predict()`.
*   **Study Resource:** The [TensorFlow Lite documentation and tutorials](https://www.tensorflow.org/lite/guide) at tensorflow.org cover the full conversion pipeline, quantization options, and Android/iOS deployment. The [TensorFlow Serving with Docker guide](https://www.tensorflow.org/tfx/guide/serving) covers REST endpoint structure and model versioning.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Work through the [TensorFlow Lite guide: Convert a model](https://www.tensorflow.org/lite/models/convert/convert_models) at tensorflow.org. This free official guide covers `TFLiteConverter`, post-training quantization, and running inference with the TFLite Interpreter. Also review the [TF Serving REST API guide](https://www.tensorflow.org/tfx/serving/api_rest) for endpoint format.
*   **Required Video:** Watch the deployment section of the course playlist: [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU). This covers SavedModel format, TFLite conversion, and the TF Serving Docker workflow.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Save a trained model**: Train a simple image classifier and save it in both SavedModel format (`model.save('saved_model/')`) and H5 format (`model.save('model.h5')`). Verify the SavedModel directory structure (`saved_model.pb` + `variables/`).
*   **Convert to TFLite**: Use `TFLiteConverter.from_saved_model()` to convert the SavedModel to a `.tflite` flatbuffer. Apply `DEFAULT` optimization for quantization. Write the `.tflite` bytes to disk and compare file sizes with the original SavedModel.
*   **Run TFLite inference**: Load the `.tflite` file with `tf.lite.Interpreter`, call `allocate_tensors()`, set an input tensor, invoke the interpreter, and retrieve the output tensor. Compare the TFLite prediction to `model.predict()` to verify correctness.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and distinguish SavedModel vs H5 format and when each is used.
*   [ ] Work through the [TensorFlow Lite guide: Convert a model](https://www.tensorflow.org/lite/models/convert/convert_models) at tensorflow.org.
*   [ ] Watch the deployment lecture in the [Machine Learning with Python & TensorFlow Course](https://www.youtube.com/watch?v=cKzgMFG5HpU).
*   [ ] Complete the Module 15 lab: SavedModel save, TFLite conversion with quantization, and TFLite inference.
*   [ ] Proceed to the Module 15 quiz.

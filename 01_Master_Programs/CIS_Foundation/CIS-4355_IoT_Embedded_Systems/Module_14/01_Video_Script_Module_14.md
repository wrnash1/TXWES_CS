# Video Script: Module 14 — Machine Learning for IoT

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

**Estimated Duration:** 15–18 minutes

---

### [00:00 – 02:00] Introduction

**Visual:** Instructor on camera with title card: **Machine Learning for IoT — TinyML on Microcontrollers**

**Alt-text:** Instructor at desk. Title card reads "Module 14: Machine Learning for IoT." Background monitor shows a neural network diagram overlaid on a microcontroller schematic.

**Audio:** "Welcome to Module 14. Artificial intelligence and machine learning are transforming IoT — not just in the cloud where servers have terabytes of memory, but directly on the microcontroller. Running ML models on the device itself — without sending data to the cloud for inference — is a field called TinyML, and it is one of the most exciting developments in embedded systems in the last decade."

"Think about what this enables: a smoke detector that distinguishes between burnt toast and a real fire. A factory machine that detects an abnormal vibration pattern before it fails. A wildlife camera that identifies whether the animal in frame is a deer or a poacher. All of these use cases require inference within milliseconds, on devices with no reliable internet connection, running on batteries for months. Cloud-based ML cannot meet these requirements. TinyML can."

"By the end of this module you will be able to: explain the TinyML pipeline from training to deployment, describe TensorFlow Lite Micro and its constraints, implement a keyword spotting model on the ESP32, explain anomaly detection on constrained devices, and apply model optimization techniques including quantization and pruning."

**Study Link:** [TensorFlow Lite for Microcontrollers — tensorflow.org/lite/microcontrollers](https://www.tensorflow.org/lite/microcontrollers)

---

### [02:00 – 04:30] What Is TinyML?

**Visual:** Diagram showing the spectrum from cloud AI to TinyML, with device capabilities (memory, power, latency) labeled at each tier.

**Alt-text:** A horizontal spectrum diagram. Left end labeled "Cloud AI" shows large server icon with labels: terabytes of RAM, kilowatts of power, hundreds of milliseconds of latency. Middle labeled "Edge AI" shows a single-board computer with gigabytes of RAM, watts of power. Right end labeled "TinyML" shows a microcontroller icon with kilobytes of RAM, milliwatts of power, single-digit millisecond latency.

**Audio:** "TinyML refers to machine learning inference running on microcontrollers and low-power embedded processors. The constraints are severe: a typical ESP32 has 520 KB of SRAM and no floating-point vector unit. An Arduino Nano 33 BLE Sense has 256 KB of SRAM and a Cortex-M4 with a limited FPU. These devices cannot run a ResNet-50 image classifier — that model alone is 100 MB. TinyML models must be measured in kilobytes."

"Why run ML on the device at all? Four reasons. **Privacy:** sensitive data — audio, images, biometrics — never leaves the device. The cloud receives only a label or a score, not the raw data. **Latency:** inference completes in milliseconds, not the round-trip time to a cloud API. **Reliability:** inference works even when the device has no network connectivity. **Power:** sending raw sensor data to the cloud continuously is expensive in terms of radio power; transmitting only an event flag when the model detects something interesting uses a fraction of the energy."

"The TinyML pipeline has four stages: **data collection** — capture labeled sensor data; **model training** — train a neural network on a capable machine (not the microcontroller); **model optimization** — compress the model to fit in microcontroller memory; **deployment** — run inference on the microcontroller using an optimized runtime."

---

### [04:30 – 07:00] TensorFlow Lite Micro

**Visual:** Architecture diagram showing the layers of TensorFlow Lite Micro on a microcontroller.

**Alt-text:** A vertical stack diagram. Bottom layer labeled Hardware: microcontroller CPU and optional hardware accelerator. Second layer: TensorFlow Lite Micro Runtime — a C++ library with no OS dependencies, no dynamic memory allocation, no file system requirement. Third layer: Model data — a FlatBuffer byte array stored in flash. Top layer: Application — calls interpreter API to run inference.

**Audio:** "TensorFlow Lite Micro — TFLM — is Google's framework for running TensorFlow models on microcontrollers. It is a purpose-built C++ library designed around three constraints: no operating system required, no dynamic memory allocation after initialization, and a binary footprint as small as 16 KB for the runtime alone."

"TFLM does not use `malloc()` or `new`. Instead, you provide a fixed-size byte array as an arena — the interpreter uses this arena for all intermediate tensor storage during inference. You size this arena based on the model's requirements plus a safety margin. On an ESP32, a small keyword spotting model might use 10–50 KB of arena memory."

"The workflow in code is: include the TFLM header; declare the model as a `const unsigned char` array in a C header file (generated by `xxd -i model.tflite > model.h`); create a `MicroInterpreter` with the model, a resolver listing the operations your model uses, and the arena buffer; call `interpreter.AllocateTensors()`; fill the input tensor with your sensor data; call `interpreter.Invoke()` to run inference; read the output tensor for your result."

"TFLM supports a resolver pattern for operations because including every possible neural network layer type in the binary would consume too much flash. You declare exactly which operations your model uses — `AddDepthwiseConv2D`, `AddFullyConnected`, `AddSoftmax`, etc. — and only those operation kernels are linked into the binary."

---

### [07:00 – 10:00] Keyword Spotting

**Visual:** Signal processing pipeline diagram from microphone input to classification output.

**Alt-text:** A left-to-right pipeline diagram with six boxes connected by arrows: Microphone, ADC Samples (16 kHz), MFCC Feature Extraction, Input Tensor (float or int8), Neural Network Inference, Output Probabilities (yes / no / unknown / silence).

**Audio:** "Keyword spotting — also called wake word detection — is the TinyML use case that has reached production at the largest scale. Every time a smart speaker activates on 'Hey Siri' or 'OK Google,' a TinyML model running on the device's dedicated DSP chip made that decision. The audio never went to the cloud until the keyword was confirmed."

"The model does not process raw audio waveforms directly. Raw 16 kHz audio at 16 bits per sample is 32 KB per second — too much to process frame by frame on a microcontroller. Instead, we extract **MFCC features** — Mel-Frequency Cepstral Coefficients. MFCC compresses each 30 ms audio frame into a small feature vector (typically 40 coefficients) that captures the perceptually relevant frequency content of speech while discarding information the human ear does not use."

"A 1-second window of 16 kHz audio produces approximately 33 MFCC frames, each with 40 coefficients — a 33×40 feature matrix. This is the input to the neural network, which is typically a depthwise separable convolutional network designed for efficiency. The output is a probability vector: one probability per keyword class plus 'unknown' and 'silence' categories."

"On the ESP32, the TensorFlow Lite for Microcontrollers hello_world_speech example demonstrates a working keyword spotter for 'yes' and 'no' using the Speech Commands dataset. The model is approximately 18 KB, the MFCC computation runs in under 10 ms, and inference runs in approximately 5–15 ms depending on clock speed."

---

### [10:00 – 13:00] Anomaly Detection on Constrained Devices

**Visual:** Two-panel diagram showing normal sensor data vs. anomalous data, with a reconstruction error graph.

**Alt-text:** Left panel labeled "Normal Operation" shows a smooth sinusoidal vibration waveform. Right panel labeled "Anomaly" shows the same waveform with a sharp spike. Below both panels is a bar chart labeled "Reconstruction Error" with short bars in the normal case and a tall bar exceeding a threshold line in the anomaly case.

**Audio:** "Anomaly detection is the TinyML use case with arguably the highest impact in industrial IoT. A rotating machine — motor, pump, compressor — has a characteristic vibration signature when operating normally. When a bearing begins to fail, that signature changes in subtle ways weeks before the failure becomes catastrophic."

"Cloud-based anomaly detection requires continuously streaming multi-axis accelerometer data to a cloud service, which is expensive in bandwidth and cloud compute costs, and fails completely when connectivity is lost. On-device anomaly detection runs 24 hours a day regardless of connectivity and transmits only an anomaly alert — a few bytes — when something unusual is detected."

"The most practical approach for microcontrollers is an **autoencoder** — a neural network trained to compress its input to a low-dimensional representation and then reconstruct the original input. When trained exclusively on normal operation data, the autoencoder learns to reconstruct normal patterns well. When given anomalous data, the reconstruction is poor — the reconstruction error is high. Threshold the reconstruction error and you have an anomaly detector."

"A small autoencoder for vibration data — say a 3-axis accelerometer at 200 Hz, downsampled to a 32-sample window — has an input of 96 values and might have a bottleneck of 8 values. The entire model can be under 10 KB. Quantized to 8-bit integers, it fits comfortably in the ESP32's SRAM and runs in under 5 ms."

"The critical insight is that you train the autoencoder on a development machine with weeks of normal operation data, then export the trained weights as a TFLM model. The microcontroller only runs inference — it never trains. Training is always done offline on a capable machine."

---

### [13:00 – 15:30] Model Optimization — Quantization and Pruning

**Visual:** Side-by-side comparison showing a full-precision model (float32, larger) vs. a quantized model (int8, smaller) with accuracy numbers.

**Alt-text:** Two model boxes side by side. Left box labeled "Float32 Model" shows parameters as 32-bit floats, a model size of 500 KB, and an accuracy of 94.2%. Right box labeled "Int8 Quantized Model" shows parameters as 8-bit integers, a model size of 130 KB, and an accuracy of 93.8%. An annotation reads "4x size reduction, 0.4% accuracy loss."

**Audio:** "Even after designing a small model architecture, the model weights are typically stored as 32-bit floats. A microcontroller with 512 KB of flash cannot store a 500 KB model and also run firmware — and a model that barely fits in flash will not fit in SRAM during inference when intermediate activation tensors are added."

"**Post-training quantization** converts the 32-bit float weights to 8-bit integers — int8 or uint8. This reduces model size by approximately 4x and inference time by 2–4x, because integer arithmetic is faster than floating-point on microcontrollers without dedicated FPUs. The accuracy penalty is typically less than 1% for well-designed models, often less than 0.2%."

"TensorFlow Lite's `TFLiteConverter` performs quantization automatically. You provide a **representative dataset** — a small sample of real input data that represents the value range your model will encounter — and the converter uses it to compute the optimal quantization scale and zero-point for each layer."

"**Weight pruning** is a complementary technique that sets small weights to exactly zero, creating a sparse network. Sparse networks can be compressed with simple run-length encoding and require fewer multiply-accumulate operations, further reducing inference time. Pruning is typically applied during training using Keras's `tfmot.sparsity.keras.prune_low_magnitude()` wrapper."

"**Knowledge distillation** trains a small 'student' model to mimic the behavior of a large 'teacher' model — producing a compact model that is more accurate than a small model trained directly on the data, because it learned from the teacher's rich probability outputs rather than hard labels."

---

### [15:30 – End] Summary and Lab Preview

**Visual:** TinyML deployment pipeline summary diagram.

**Audio:** "Let's recap Module 14. TinyML brings ML inference to microcontrollers, enabling privacy-preserving, low-latency, connectivity-independent intelligence at the edge. TensorFlow Lite Micro provides the runtime with no OS dependency and fixed memory allocation. Keyword spotting uses MFCC features to classify speech from a compact convolutional model. Anomaly detection uses autoencoders to compare current sensor patterns against a learned normal baseline. Post-training quantization, pruning, and knowledge distillation compress models to fit in kilobytes of flash and SRAM."

"In this module's lab, you will: run a pre-trained keyword spotting model on the ESP32 using TFLM, observe the inference latency and memory usage, apply post-training int8 quantization to a small regression model using TFLiteConverter, and compare accuracy and model size before and after quantization."

**Key Terms for This Module:**

- TinyML
- TensorFlow Lite Micro (TFLM)
- FlatBuffer model format
- MicroInterpreter, TensorArena
- MFCC — Mel-Frequency Cepstral Coefficients
- Keyword spotting / wake word detection
- Autoencoder, reconstruction error
- Anomaly detection
- Post-training quantization — float32 to int8
- Representative dataset
- Weight pruning
- Knowledge distillation
- Depthwise separable convolution

"In Module 15 we shift from building individual devices to managing thousands of them — device provisioning at scale, fleet management, OTA updates, and monitoring."

---

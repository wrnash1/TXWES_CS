# Reading Guide: Module 14 — Machine Learning for IoT

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

## Learning Objectives

By the end of this module you should be able to:

- Explain the TinyML pipeline and the four stages from data collection to deployment
- Describe TensorFlow Lite Micro's memory model and why it avoids dynamic allocation
- Implement a keyword spotting application using MFCC features and a CNN model
- Design an autoencoder-based anomaly detection system for IoT sensor data
- Apply post-training quantization and understand the accuracy vs. size trade-off

---

## Section 1 — The Case for On-Device Inference

### Cloud ML vs. Edge ML vs. TinyML

Machine learning inference — applying a trained model to new data to produce a prediction — has traditionally been done in the cloud. A device captures data, transmits it to a cloud API, the API runs inference on a GPU-backed server, and returns the result. This architecture works well when: connectivity is reliable, latency of several hundred milliseconds is acceptable, transmitting raw data raises no privacy concerns, and the power budget allows continuous radio transmission.

IoT devices frequently violate all four of these assumptions simultaneously. Consider:

**A wildlife poaching detection camera** must identify a person vs. an animal in a remote location with no cellular coverage, within 500 ms (before the subject moves), without sending images to the cloud (privacy and bandwidth), on a battery that must last six months.

**A bearing fault detector** on an industrial compressor must detect early-stage fault signatures in vibration data continuously, 24 hours per day, in a basement facility where cellular is unreliable, while adding under 1 watt to the device's total power budget.

**A medical wearable** must detect atrial fibrillation from ECG data in real time without transmitting health data to any cloud service, using a coin cell battery for six months.

TinyML addresses all three use cases. The model runs on the device. Raw sensor data is processed locally. Only a classification result — a few bytes — is ever transmitted.

### TinyML Hardware Landscape

The hardware landscape for TinyML spans several capability tiers:

**Cortex-M4/M7 class (Arduino Nano 33, STM32):** 64–512 KB SRAM, hardware FPU, 80–216 MHz. Suitable for audio keyword spotting and small image classification with quantized models.

**Xtensa LX6/LX7 class (ESP32, ESP32-S3):** 520 KB SRAM (ESP32), vector instructions (ESP32-S3). The ESP32-S3 includes dedicated AI instructions that accelerate int8 matrix multiply — suitable for small image models and audio processing.

**Cortex-M55 with Ethos-U55 NPU (Arduino Portenta H7, STM32MP1):** Hardware neural processing unit, hundreds of GOPS (giga operations per second) at milliwatt power levels. Suitable for moderate-complexity image models and transformer-based audio models.

**Raspberry Pi RP2040:** Dual Cortex-M0+, no FPU, 264 KB SRAM. Very constrained — best suited for tiny regression models and simple anomaly detectors.

---

## Section 2 — TensorFlow Lite Micro Architecture

### Memory Model

Standard TensorFlow requires dynamic memory allocation, a file system to load models, and a full operating system. TensorFlow Lite Micro was re-architected from scratch to eliminate these dependencies.

TFLM's memory model has three components:

**Model data (flash):** The TFLite model file is converted to a C byte array and stored in flash. It is never modified at runtime — the model is read-only. The FlatBuffer format allows field access without deserialization, so TFLM can access model parameters directly from flash without copying them to RAM.

**Tensor arena (SRAM):** A fixed-size byte array you allocate and pass to the `MicroInterpreter`. TFLM uses this arena as its workspace: input and output tensors are subarrays within the arena, intermediate activation tensors during inference are allocated and freed within the arena, and the arena is reused across inference calls. You size this arena to be large enough for your model's peak memory requirement plus a safety margin of at least 10%.

**Code (flash):** The TFLM runtime and the operation kernels for your model's layer types. Total code size varies from 16 KB (minimal configuration) to 100 KB+ (all operations included).

### Operator Resolver

TFLM uses a resolver pattern to minimize flash footprint. Instead of including all possible neural network operation implementations, you declare exactly which operations your model uses:

```cpp
static tflite::MicroMutableOpResolver<5> resolver;
resolver.AddDepthwiseConv2D();
resolver.AddFullyConnected();
resolver.AddReshape();
resolver.AddSoftmax();
resolver.AddQuantize();
```

Only the implementations of these five operations are linked into the binary. An unknown operation in the model causes an error at `AllocateTensors()` time, making the resolver an explicit model-binary compatibility check.

### Inference API

The inference workflow has five steps:

1. `tflite::GetModel(model_data)` — wrap the model byte array in a Model pointer
2. `tflite::MicroInterpreter interpreter(model, resolver, arena, arena_size)` — create interpreter
3. `interpreter.AllocateTensors()` — allocate tensor views within the arena; must succeed before inference
4. Fill `interpreter.input(0)->data.f` (float32) or `->data.int8` (quantized) with input data
5. `interpreter.Invoke()` — run inference; read results from `interpreter.output(0)->data`

---

## Section 3 — Keyword Spotting

### Audio Feature Extraction — MFCC

Speech recognition does not operate on raw audio waveforms because: (a) raw waveforms contain far more data than needed, (b) the perceptually important features of speech are in the frequency domain, not the time domain, and (c) the human auditory system applies a nonlinear frequency scale (the Mel scale) that emphasizes lower frequencies where speech information is denser.

Mel-Frequency Cepstral Coefficients (MFCC) capture these properties:

1. **Framing:** Divide the audio stream into overlapping 25 ms frames with a 10 ms stride.
2. **Windowing:** Apply a Hamming window to reduce spectral leakage at frame boundaries.
3. **FFT:** Compute the Fast Fourier Transform of the frame to get the frequency spectrum.
4. **Mel filterbank:** Apply 40 triangular filters spaced on the Mel scale — a perceptual frequency scale where equal steps correspond to equal perceived pitch differences.
5. **Log compression:** Take the log of each filterbank energy — humans perceive loudness logarithmically.
6. **DCT:** Apply the Discrete Cosine Transform to decorrelate the filterbank energies. The first 13–40 coefficients are the MFCCs.

For keyword spotting on a 1-second window at 16 kHz, you produce approximately 40 frames × 40 coefficients = a 40×40 feature matrix. This is the input to the neural network.

### Model Architecture

The most effective small architecture for keyword spotting on microcontrollers is a **Depthwise Separable Convolutional Neural Network** (DS-CNN). Regular convolutions apply a filter across all input channels simultaneously. Depthwise separable convolutions factorize this into: a depthwise convolution that filters each channel independently, followed by a pointwise (1×1) convolution that combines channels. This reduces multiply-accumulate operations by a factor of 8–9x for typical kernel sizes.

A typical DS-CNN for 10-word keyword spotting:

- Input: 49×10 MFCC features (downsampled from 40×40)
- 2–3 depthwise separable conv blocks
- Global average pooling
- Fully connected layer → 12 classes (10 keywords + unknown + silence)
- Softmax activation

Quantized to int8, this model is typically 16–40 KB — fits easily in ESP32 flash.

### Speech Commands Dataset

Google's Speech Commands dataset is the standard benchmark for keyword spotting models. It contains 105,829 one-second audio clips of 35 words spoken by thousands of speakers. The dataset is used to train and evaluate models; it is available at `tensorflow.org/datasets/catalog/speech_commands`.

---

## Section 4 — Anomaly Detection

### Autoencoder Architecture

An autoencoder is an unsupervised neural network with two components:

**Encoder:** Compresses the input to a lower-dimensional latent representation. For a 96-element vibration window, the encoder might reduce it to 8 values.

**Decoder:** Reconstructs the input from the latent representation. The reconstruction is the network's best guess at the original input.

When trained on normal data only, the autoencoder learns the manifold of normal patterns — the statistical space that normal inputs occupy. Anomalous inputs lie off this manifold; the encoder cannot represent them efficiently, and the decoder's reconstruction is poor. The **reconstruction error** — typically mean squared error between input and reconstruction — is low for normal data and high for anomalies.

Threshold the reconstruction error at a value determined from the training distribution (e.g., the 99th percentile of training reconstruction errors) to produce a binary anomaly flag.

### Training Strategy

The training-to-deployment workflow:

1. Collect 2–4 weeks of sensor data from the machine in known-normal operating state.
2. Train the autoencoder on a GPU-equipped development machine using Keras/TensorFlow.
3. Evaluate reconstruction error distribution on a held-out normal validation set.
4. Set the anomaly threshold at the 99th or 99.9th percentile of validation errors.
5. Convert the trained model to TFLite format and quantize.
6. Deploy to the microcontroller.
7. Periodically upload anomaly events (timestamp + reconstruction error) to the cloud for monitoring.

### Practical Anomaly Detection Considerations

**Concept drift:** A machine's normal signature changes over time — wear, seasonal temperature changes, load variations. The model may need periodic retraining on recent normal data to avoid false positives.

**Contextual anomalies:** Some operations are normal in one context but anomalous in another — a pump running at 3,000 RPM is normal during operation but anomalous during shutdown. Context-aware models include operating mode as an input feature.

**Sensitivity vs. specificity:** A lower threshold catches more real anomalies but also generates more false alarms. A higher threshold misses subtle early-stage faults. Tune for the cost of each error type in the specific application.

---

## Section 5 — Model Optimization Techniques

### Post-Training Quantization

Float32 (32-bit floating point) is the native training format for neural networks. For microcontroller deployment, int8 (8-bit integer) offers:

- 4x reduction in model storage size
- 2–4x reduction in inference time (integer multiply-accumulate is faster than float on MCUs without FPU)
- Reduced power consumption (integer arithmetic uses less energy per operation)

The quantization formula maps float values to int8:

```text
quantized_value = round(float_value / scale) + zero_point
```

where `scale` and `zero_point` are determined per layer by analyzing the value range of activations over the representative dataset.

**Full integer quantization** (model inputs, activations, weights, and outputs all in int8) requires a representative dataset during conversion. **Dynamic range quantization** quantizes weights only — activations remain float32 during inference. Full integer is preferred for microcontrollers because it eliminates float32 arithmetic entirely.

### Pruning

Pruning zeros out weights with small magnitudes during training, producing a sparse model. The Keras TensorFlow Model Optimization Toolkit provides the `prune_low_magnitude()` wrapper. Typically, 50–80% sparsity can be achieved with less than 1% accuracy degradation for well-regularized models.

Sparse models benefit from compression: a 50% sparse model with run-length encoding may be only 30% the size of the dense model. However, sparse matrix arithmetic is only faster than dense arithmetic when sparsity exceeds approximately 80% — most hardware lacks native sparse math acceleration.

### Knowledge Distillation

Knowledge distillation trains a compact "student" model by minimizing its divergence from a large, accurate "teacher" model's output probabilities — not from the original hard labels. The soft probability distributions from the teacher contain richer information than hard labels (a misidentified "seven" is often confused with "one" or "four", not with "dog") and allow the student to learn a more nuanced decision boundary. Distilled models typically outperform equivalently sized models trained directly on hard labels.

---

## Key Terms

- **TinyML** — machine learning inference on microcontrollers and low-power processors
- **TensorFlow Lite Micro (TFLM)** — Google's MCU-targeted ML inference runtime
- **FlatBuffer** — zero-copy serialization format used for TFLite model files
- **MicroInterpreter** — TFLM's inference engine class
- **TensorArena** — fixed-size SRAM buffer used for all dynamic allocations during inference
- **MFCC** — Mel-Frequency Cepstral Coefficients; perceptual audio features for speech recognition
- **Keyword spotting** — real-time classification of short spoken words on device
- **Autoencoder** — neural network that compresses and reconstructs its input; used for anomaly detection
- **Reconstruction error** — difference between autoencoder input and output; high for anomalies
- **Post-training quantization** — converting float32 weights to int8 after training
- **Representative dataset** — small data sample used to calibrate quantization scale factors
- **Weight pruning** — zeroing small weights to create sparse, compressible models
- **Knowledge distillation** — training a small student model to mimic a large teacher model
- **Depthwise separable convolution** — factorized convolution reducing computation by 8–9x

---

## Review Questions

1. Name the four stages of the TinyML pipeline and describe what happens in each stage.
2. Why does TFLM avoid dynamic memory allocation (`malloc`), and what is the alternative mechanism for runtime memory management?
3. What is the role of the `MicroMutableOpResolver` in TFLM, and what happens at `AllocateTensors()` time if the model uses an operation not registered in the resolver?
4. Explain the five steps of MFCC feature extraction and why each step is applied.
5. What is the input shape to a keyword spotting CNN that processes 1 second of 16 kHz audio with 40-coefficient MFCC features and 33 frames?
6. Describe the autoencoder architecture: what are the encoder and decoder, and what property of the training data makes reconstruction error a useful anomaly signal?
7. What determines the anomaly detection threshold for an autoencoder model, and what are the consequences of setting the threshold too low vs. too high?
8. In post-training full integer quantization, what is the purpose of the representative dataset and why is it required?
9. What are the three quantitative benefits of int8 quantization over float32 for microcontroller deployment?
10. A keyword spotting model achieves 94.2% accuracy in float32 and 93.6% accuracy after int8 quantization. The float32 model is 480 KB and the int8 model is 122 KB. The ESP32's available flash for the model is 200 KB. Which model can be deployed, and is the accuracy trade-off acceptable? Justify your answer.

---

## 9. Supplemental Resources

**1. TensorFlow Lite Micro — Official Getting Started Guide**
[https://www.tensorflow.org/lite/microcontrollers](https://www.tensorflow.org/lite/microcontrollers)
Google's official TensorFlow Lite Micro documentation covering the TFLM architecture, the MicroInterpreter workflow, operator resolver configuration, and the `AllocateTensors()` / `Invoke()` API. Includes worked examples for keyword spotting (micro_speech) and person detection that directly correspond to the lab exercises in this module, as well as guides for post-training quantization and converting trained models to C arrays.

**2. Edge Impulse — TinyML Model Training and Deployment Platform**
[https://docs.edgeimpulse.com/docs](https://docs.edgeimpulse.com/docs)
Edge Impulse is the leading end-to-end TinyML development platform that automates the data collection, feature extraction (including MFCC for audio and spectral analysis for vibration), model training, quantization, and deployment pipeline described in this module. The documentation covers anomaly detection with autoencoders, keyword spotting with DS-CNN, and direct deployment to the ESP32 — making it a practical companion to the theory in this reading guide.

**3. Pete Warden & Daniel Situnayake — "TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers" (O'Reilly)**
[https://www.oreilly.com/library/view/tinyml/9781492052036/](https://www.oreilly.com/library/view/tinyml/9781492052036/)
The definitive textbook on TinyML by the authors of TensorFlow Lite Micro, covering the complete pipeline from data collection through model training, quantization, and microcontroller deployment. Chapters 7–10 cover keyword spotting (the "yes/no" model used in the lab), Chapters 11–13 cover person detection, and the appendices detail the MFCC feature pipeline and tensor arena sizing methodology referenced throughout this module.

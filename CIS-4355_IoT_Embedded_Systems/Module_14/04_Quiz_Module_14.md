# Quiz: Module 14 — Machine Learning for IoT

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

### Question 1

A developer wants to run an image classification model on an ESP32. The trained Keras model is 45 MB in float32 format. The ESP32 has 4 MB of flash and 520 KB of SRAM. Which statement most accurately describes the deployment feasibility?

- A) The model cannot be deployed because the float32 model exceeds both the flash capacity and the SRAM. Even after int8 quantization (approximately 4x reduction to ~11 MB), the model still exceeds the 4 MB flash limit. A different, purpose-built small architecture is required.
- B) The model can be deployed after int8 quantization reduces it to approximately 11 MB, which fits within the ESP32's 4 MB flash by using the external PSRAM expansion.
- C) The model can be deployed as-is by streaming weights from flash to SRAM in chunks during inference — TFLM supports this streaming mode for models larger than SRAM.
- D) The model can be deployed after quantization to 4-bit weights (QAT4), which reduces the 45 MB model to approximately 5.6 MB, fitting within flash after compression.
- **Correct Answer:** A) Even after quantization the model is too large; a smaller architecture is required.
- **Distractor Analysis:**
  - *Why A is correct:* 45 MB / 4 (quantization ratio) = ~11 MB. The ESP32's flash is 4 MB total — shared between firmware, filesystem, and model storage. An 11 MB model exceeds the entire flash chip. The correct solution is to select or design a model architecture specifically for microcontroller constraints — for example, MobileNetV1-0.25, which is approximately 470 KB quantized — rather than attempting to compress a large model.
  - *Why B is incorrect:* The standard ESP32 does not include PSRAM; PSRAM is an optional external component available on some ESP32 modules (e.g., ESP32-WROVER). Even with 4 MB PSRAM, an 11 MB model still does not fit. Additionally, PSRAM access is significantly slower than internal SRAM and would make inference latency impractical for most applications.
  - *Why C is incorrect:* TFLM does not support streaming weight chunks from flash during inference. The entire model's intermediate activations must fit in SRAM simultaneously during inference. TFLM requires the full model to be accessible in flash and the full activation memory to be available in the arena.
  - *Why D is incorrect:* 4-bit quantization (QAT4) is a research-stage technique not supported by the standard TFLite converter or TFLM runtime as of the current toolchain. Even if it were, 45 MB / 8 = 5.6 MB still exceeds the 4 MB flash.

---

### Question 2

In TensorFlow Lite Micro, a developer declares a `kTensorArenaSize` of 16,384 bytes (16 KB) for a keyword spotting model. When `interpreter.AllocateTensors()` is called, it returns `kTfLiteError`. What does this indicate, and what is the correct diagnostic step?

- A) The model file is corrupted — `kTfLiteError` from `AllocateTensors()` always indicates a malformed FlatBuffer model. The fix is to re-convert the model from the original Keras file.
- B) The tensor arena is too small to hold the model's input/output tensors and intermediate activation tensors simultaneously. The fix is to increase `kTensorArenaSize` until `AllocateTensors()` succeeds, then record the minimum successful size.
- C) The operator resolver is missing a required operation — `AllocateTensors()` validates the resolver and returns error if any model operation is unregistered. The fix is to add all operations to the resolver.
- D) The ESP32 does not have enough contiguous heap memory to allocate the arena array. The fix is to call `heap_caps_malloc(kTensorArenaSize, MALLOC_CAP_8BIT)` instead of declaring the arena as a static array.
- **Correct Answer:** B) The arena is too small; increase it until AllocateTensors() succeeds.
- **Distractor Analysis:**
  - *Why A is incorrect:* A corrupted FlatBuffer model typically causes `GetModel()` to return a null pointer or a model verification check to fail — not an arena allocation failure. These are distinct failure modes.
  - *Why B is correct:* `AllocateTensors()` lays out tensor memory within the arena. If the arena is insufficient for the peak memory requirement (input tensor + output tensor + largest intermediate activation layer + TFLM internal metadata), it returns `kTfLiteError`. The diagnostic process is to increase the arena size in 1–2 KB increments until the call succeeds, establishing the minimum viable arena size.
  - *Why C is incorrect:* Missing resolver operations do cause errors, but they manifest during model loading and operator registration — not as a return value from `AllocateTensors()`. TFLM will print an error message identifying the missing operation before reaching the allocation phase.
  - *Why D is incorrect:* Static array declaration on the ESP32 uses DRAM by default, which has the required 8-byte alignment. Heap allocation vs. static declaration does not affect whether `AllocateTensors()` succeeds — only the size of the arena matters for this failure mode.

---

### Question 3

A TinyML anomaly detection model is deployed on a factory floor vibration sensor. The model was trained on 3 weeks of normal vibration data from March. By October, the model is generating false positive anomaly alerts daily, even though the machine is operating within normal parameters. What is the most likely cause and the correct long-term fix?

- A) The model's int8 quantization has degraded over time as the flash memory cells lose charge. The fix is to reflash the firmware with a fresh copy of the model.
- B) The machine's normal vibration signature has drifted due to seasonal temperature changes, mechanical wear, and operating load variations — a phenomenon called concept drift. The model's normal baseline no longer matches current normal operations. The fix is to collect new normal-operation data and retrain or fine-tune the autoencoder periodically.
- C) The TFLM runtime has a memory leak in the arena allocator that accumulates over months of continuous inference calls, causing reconstruction error calculations to become inaccurate. The fix is to restart the device periodically to reset the arena.
- D) The anomaly detection threshold set during initial deployment was too low. The fix is to recalibrate the threshold once to a higher value that eliminates the false positives at the current operating conditions.
- **Correct Answer:** B) Concept drift — the machine's normal signature has changed; the model needs retraining.
- **Distractor Analysis:**
  - *Why A is incorrect:* Flash memory charge loss (bit rot) occurs over years to decades, not months, and affects stored data uniformly — it would corrupt the model entirely rather than cause a gradual increase in false positives. This is not a realistic failure mode on the described timescale.
  - *Why B is correct:* Concept drift is the primary operational challenge for deployed anomaly detection models. Industrial machines change their vibration characteristics as bearings wear, lubricants age, ambient temperatures shift seasonally, and production loads vary. A model trained on March data does not represent October normal — the distribution has shifted. Periodic model retraining on recent normal data is the standard mitigation. Some systems implement online learning or periodic retraining pipelines that update the model quarterly.
  - *Why C is incorrect:* TFLM uses a fixed-size arena with no dynamic allocation after `AllocateTensors()`. There is no heap allocation during inference calls, therefore no memory leak in the arena allocator. The arena memory layout is static for the lifetime of the interpreter instance.
  - *Why D is incorrect:* A one-time threshold recalibration treats the symptom, not the cause. If the machine's signature continues to drift, false positives will return. More critically, raising the threshold to silence current false alarms may also silence legitimate early-fault signals in the future, defeating the purpose of anomaly detection.

---

### Question 4

What is the purpose of the representative dataset in full integer (int8) post-training quantization, and what happens if the representative dataset does not adequately cover the expected input value range?

- A) The representative dataset is used to evaluate the model's accuracy on real data before quantization — it is a validation set. If it does not cover the full range, the reported pre-quantization accuracy will be optimistic.
- B) The representative dataset is used to calibrate the quantization scale and zero-point for each layer's activations. If it does not cover the full input range, the scale factors will be computed from a narrow value range, causing clipping (saturation) when inference sees inputs outside that range — degrading accuracy significantly.
- C) The representative dataset is used to select which weights to prune to zero before quantization, combining pruning and quantization in a single pass. Inadequate coverage causes under-pruning, resulting in a larger-than-expected model.
- D) The representative dataset is used to generate synthetic training data for knowledge distillation, where the quantized model is trained to mimic the float32 model's outputs. Limited coverage restricts the distillation domain.
- **Correct Answer:** B) It calibrates scale and zero-point per layer; inadequate coverage causes activation clipping.
- **Distractor Analysis:**
  - *Why A is incorrect:* The representative dataset is not a validation or test set — it is not used to measure accuracy. It is a calibration dataset used purely for computing quantization parameters. A separate validation set is used to measure post-quantization accuracy.
  - *Why B is correct:* Full integer quantization must determine, for every layer, the range of floating-point values that will be mapped to the int8 range [-128, 127]. The scale factor is `(max_value - min_value) / 255`. The representative dataset is run through the model and the min/max of each layer's activations are recorded. If the dataset does not include inputs that exercise the full activation range, the computed scale will be too narrow — inputs outside the calibrated range are clipped to the int8 minimum or maximum, causing significant accuracy loss.
  - *Why C is incorrect:* Pruning is a separate optimization applied during training using `prune_low_magnitude()`. The representative dataset in TFLiteConverter is not used for pruning decisions. Pruning and quantization are independent operations that can be composed but use separate mechanisms.
  - *Why D is incorrect:* Knowledge distillation requires training the student model with backpropagation — it is a training-time technique. The TFLiteConverter's representative dataset is used at conversion time, after training is complete, for calibration only.

---

### Question 5

A depthwise separable convolution replaces a standard convolution with two operations: a depthwise convolution followed by a pointwise (1×1) convolution. For a layer with 32 input channels, a 3×3 kernel, and 64 output channels, what is the approximate ratio of multiply-accumulate (MAC) operations between the standard convolution and the depthwise separable version?

- A) The depthwise separable convolution uses approximately the same number of MACs as the standard convolution — the factorization reduces memory but not computation.
- B) The depthwise separable convolution uses approximately 8–9x fewer MACs than the standard convolution for typical kernel sizes, which is the primary reason for its use in mobile and embedded neural network architectures.
- C) The depthwise separable convolution uses approximately 2x fewer MACs because the factorization eliminates one multiplication per output channel.
- D) The depthwise separable convolution uses approximately 32x fewer MACs because the depthwise step processes each of the 32 input channels independently, eliminating all cross-channel multiplications.
- **Correct Answer:** B) Approximately 8–9x fewer MACs — the standard result for 3×3 depthwise separable vs. standard convolution.
- **Distractor Analysis:**
  - *Why A is incorrect:* The computational reduction is the primary motivation for depthwise separable convolutions — not just memory reduction. Howard et al.'s MobileNet paper demonstrated this explicitly: standard convolution has `D_K × D_K × M × N × D_F × D_F` MACs; depthwise separable has `(D_K × D_K × M + M × N) × D_F × D_F` MACs, where D_K is kernel size, M is input channels, N is output channels, D_F is feature map size.
  - *Why B is correct:* For a 3×3 kernel (D_K=3), the reduction ratio is approximately 1/(N + 1/D_K²) ≈ 1/9 for large N. The computation savings from eliminating cross-channel multiplications in the depthwise step is the reason MobileNet, SqueezeNet, and DS-CNN for keyword spotting all achieve competitive accuracy at a fraction of the parameter count and compute of VGG or ResNet-style architectures.
  - *Why C is incorrect:* 2x reduction would make depthwise separable convolutions only marginally useful. The actual reduction for 3×3 kernels is approximately 8–9x — sufficient to enable deployment on microcontrollers.
  - *Why D is incorrect:* 32x reduction overstates the savings. The depthwise step does process each channel independently (saving the cross-channel multiplications), but the pointwise step then combines all channels — adding back cross-channel computation. The total reduction accounts for both steps.

---

### Question 6

In a TFLM keyword spotting application on the ESP32, the audio provider captures 16 kHz, 16-bit mono audio. A 1-second sliding window is processed every 100 ms. MFCC extraction produces a 49×10 feature matrix per window. The neural network input tensor shape is (1, 49, 10, 1) — batch, time, frequency, channel. Which data type should the input tensor use for a fully int8-quantized model, and what transformation must be applied to the raw MFCC float32 features before writing them to the input tensor?

- A) The input tensor should be float32. TFLM automatically converts float32 inputs to int8 internally before inference, so no transformation is needed.
- B) The input tensor should be int8. The float32 MFCC features must be quantized using the input tensor's scale and zero-point values (obtained from `input_details[0]['quantization']`) before being written to `interpreter.input(0)->data.int8`.
- C) The input tensor should be uint8. No transformation is needed because MFCC values are always non-negative, making unsigned 8-bit the natural representation.
- D) The input tensor should be int16. TensorFlow Lite Micro uses 16-bit integer arithmetic for audio models because the dynamic range of MFCC features exceeds what int8 can represent.
- **Correct Answer:** B) Input tensor is int8; float32 MFCCs must be quantized with the tensor's scale and zero-point.
- **Distractor Analysis:**
  - *Why A is incorrect:* A fully int8-quantized model has `inference_input_type = tf.int8` set during conversion. The input tensor is int8, not float32. TFLM does not automatically convert input types — the application code is responsible for providing correctly typed and quantized input data.
  - *Why B is correct:* For a fully quantized model, the application must quantize the float32 MFCC features to int8 using the formula: `int8_value = round(float32_value / input_scale) + input_zero_point`, where `input_scale` and `input_zero_point` are retrieved from the input tensor's quantization parameters. This is explicitly the application's responsibility and is part of the pre-processing pipeline on the microcontroller.
  - *Why C is incorrect:* MFCC values can be negative (the DCT transform produces both positive and negative coefficients) — unsigned int8 cannot represent negative values. Using uint8 for MFCC inputs would clip all negative values to zero, significantly corrupting the features and degrading model accuracy.
  - *Why D is incorrect:* While int16 quantization exists as an experimental TFLM option, the standard full integer quantization uses int8 for both weights and activations. Audio models for keyword spotting routinely achieve acceptable accuracy with int8 MFCC inputs. The dynamic range of MFCC features is bounded during training and is accounted for by the quantization scale factor.

---

### Question 7

An engineer trains an autoencoder on 30 days of normal vibration data from a pump. The model achieves a mean reconstruction error of 0.012 on the training set and 0.014 on the validation set. The engineer sets the anomaly threshold at 0.050. After deployment, the pump runs for 6 months without any alerts. On day 180, a bearing fails catastrophically without any prior alert. What is the most likely explanation?

- A) The TFLM runtime's int8 quantization accumulated error over 180 days of continuous inference, causing reconstruction errors to gradually decrease until they could no longer exceed the threshold.
- B) The anomaly threshold of 0.050 is too high relative to the model's reconstruction error distribution. Early-stage bearing degradation produced reconstruction errors above the training baseline (0.014) but below the 0.050 threshold, so they were not flagged as anomalies.
- C) The autoencoder overfitted to the training data so severely that it reconstructs anomalous patterns as well as normal ones, resulting in low reconstruction error for all inputs including faulty states.
- D) The pump's normal vibration changed so significantly that the reconstruction error for normal operation exceeded 0.050, causing the system to treat all normal readings as anomalies and suppressing alerts through rate limiting.
- **Correct Answer:** B) The threshold is too high — early-stage fault signals were above baseline but below the threshold.
- **Distractor Analysis:**
  - *Why A is incorrect:* TFLM inference is a deterministic calculation using fixed int8 weights. There is no accumulation of error over repeated inference calls — each call is independent. Quantization error is constant and set at conversion time; it does not grow over time.
  - *Why B is correct:* The model's normal reconstruction error baseline is approximately 0.012–0.014. A threshold of 0.050 is 3.5x the normal baseline — a very conservative threshold that requires extreme anomalies to trigger. Early-stage bearing degradation typically produces subtle changes in vibration signature — reconstruction errors might rise to 0.020–0.035 over several weeks before failure. These signals are above the normal baseline but below the 0.050 threshold, and are therefore silently ignored. The threshold should be set closer to the 99th percentile of training reconstruction errors — likely around 0.018–0.022 — to catch early-stage degradation.
  - *Why C is incorrect:* An overfit autoencoder would produce low reconstruction error on training-distribution inputs and potentially low error on similar inputs — but bearing fault vibration signatures are typically dissimilar enough from normal signatures to produce elevated reconstruction error even in an overfit model. If the model truly reconstructs anomalies perfectly, it would need to have learned fault patterns during training, which is impossible since it was trained exclusively on normal data.
  - *Why D is incorrect:* If normal operation exceeded the threshold, the system would be generating constant false positives — not silence. The scenario describes 180 days of no alerts, which is inconsistent with a threshold that normal operation regularly exceeds.

---

### Question 8

A product team is deciding between two deployment strategies for a TinyML keyword spotting feature. Option A: run MFCC extraction and inference in a FreeRTOS task at 10 Hz (one inference per 100 ms), pinned to APP_CPU. Option B: run MFCC extraction and inference in a timer interrupt service routine that fires every 100 ms. Which option is correct and why?

- A) Option B is correct because running inference in an ISR guarantees deterministic 100 ms latency. FreeRTOS task scheduling may delay the task by up to one tick (1 ms), introducing unacceptable jitter for audio classification.
- B) Option A is correct. ISRs must be kept short — MFCC extraction and neural network inference take 5–20 ms each, far too long to run inside an ISR. Running them in a FreeRTOS task allows blocking, normal stack usage, and proper interaction with the TFLM interpreter, which is not ISR-safe.
- C) Option B is correct because the TFLM `Invoke()` function is interrupt-safe and was specifically designed to run in timer ISRs on the ESP32. FreeRTOS tasks introduce memory overhead from task stacks that should be avoided for inference.
- D) Neither option is correct. MFCC extraction and inference must be performed in a dedicated hardware peripheral (the ESP32's ULP coprocessor) to meet the real-time requirements. Neither ISRs nor RTOS tasks are appropriate.
- **Correct Answer:** B) Option A — inference must run in a task, not an ISR.
- **Distractor Analysis:**
  - *Why A is incorrect:* The 1 ms tick jitter argument is technically valid but irrelevant to this decision. Human speech perception tolerates 100 ms± 20 ms windows without accuracy degradation. More importantly, this answer recommends running 5–20 ms of computation inside an ISR — which is a fundamental embedded systems violation that will cause missed lower-priority interrupts, watchdog triggers, and Wi-Fi stack failures on the ESP32.
  - *Why B is correct:* ISRs have two absolute constraints: they must be short (microseconds, not milliseconds) and they cannot block. MFCC extraction involves FFT computation (milliseconds), and TFLM `Invoke()` is not ISR-safe (it may use non-reentrant state). A FreeRTOS task with a 100 ms `vTaskDelay()` produces functionally equivalent timing with none of the ISR constraints, proper stack allocation, and correct TFLM operation.
  - *Why C is incorrect:* TFLM `Invoke()` is not documented as ISR-safe and should not be called from interrupt context. The interpreter uses a non-reentrant execution model. There is no ESP32-specific guarantee of ISR safety for TFLM.
  - *Why D is incorrect:* The ESP32's ULP (Ultra-Low Power) coprocessor is a very limited processor (8 KB instruction memory, no multiply instruction) designed for simple sensor polling during deep sleep — it cannot perform FFT or neural network inference. RTOS tasks are the correct mechanism for this workload.

---

### Question 9

Dynamic range quantization and full integer quantization are both TFLite post-training quantization modes. What is the key operational difference, and which is preferred for TensorFlow Lite Micro deployment on a microcontroller with no hardware floating-point unit?

- A) Dynamic range quantization quantizes only model weights to int8 but performs activations in float32 during inference. Full integer quantization quantizes weights and activations to int8. Full integer quantization is preferred for MCUs without FPU because it eliminates all float32 arithmetic during inference.
- B) Dynamic range quantization is faster at conversion time because it does not require a representative dataset. Full integer quantization is slower to convert but produces smaller models. Both are equally suitable for MCU deployment because TFLM handles the float32 activations in software.
- C) Dynamic range quantization quantizes both weights and activations to int8 but uses a dynamic scale factor computed at inference time. Full integer quantization uses a static scale factor computed at conversion time. Dynamic range is preferred because the dynamic scale factor is more accurate for variable-range sensor inputs.
- D) Dynamic range quantization applies to convolutional layers only. Full integer quantization applies to all layer types including fully connected, activation, and normalization layers. Full integer is required when the model contains any non-convolutional layers.
- **Correct Answer:** A) Dynamic range quantizes weights only (activations remain float32); full integer quantizes everything; full integer is required for FPU-less MCUs.
- **Distractor Analysis:**
  - *Why A is correct:* Dynamic range quantization stores weights as int8 but dequantizes them to float32 at inference time before performing arithmetic. The activations are always float32. On an MCU without an FPU (Cortex-M0, RP2040) or with a limited FPU, this means every multiply-accumulate operation involves float32 software emulation — slow and energy-intensive. Full integer quantization performs all arithmetic in int8, which is natively fast on any 32-bit processor. For microcontroller deployment, full integer quantization is the required mode.
  - *Why B is incorrect:* The claim that both are "equally suitable" because "TFLM handles float32 in software" understates the performance impact. Float32 software emulation on a Cortex-M0 is approximately 10–100x slower than int8 hardware arithmetic. For real-time inference, full integer quantization is not merely preferred — it is often required to meet latency budgets.
  - *Why C is incorrect:* This describes the difference between static and dynamic scale factors, but the terminology is inverted from the actual TFLite definitions. Dynamic range quantization does not compute scale factors dynamically at inference time — it computes static weight scale factors at conversion time. The "dynamic" in the name refers to the fact that activation ranges are determined dynamically (at inference time) rather than from a calibration dataset.
  - *Why D is incorrect:* Both dynamic range and full integer quantization apply to all supported layer types. The distinction is not which layers are covered but rather whether activations are quantized.

---

### Question 10

A developer is building a TinyML application that classifies four machine states — idle, normal load, high load, overload — from a 3-axis accelerometer. The development machine has 32 GB of RAM and a GPU. The ESP32 target has 520 KB SRAM and 4 MB flash. Which workflow correctly describes the training-to-deployment pipeline?

- A) Train the classifier on the development machine using Keras with float32 weights and labeled accelerometer data. Convert to TFLite, apply int8 quantization with a representative dataset, generate a C array with xxd, include the array in ESP32 firmware, run inference using TFLM on the ESP32.
- B) Train the classifier directly on the ESP32 using online learning — the device receives labeled examples over MQTT and updates its weights in real time. Deploy the model to flash only after convergence on the device.
- C) Train the classifier on the development machine. Deploy the float32 Keras model to the ESP32 using the ESP-IDF TensorFlow integration, which automatically handles float32 inference natively.
- D) Train the classifier on the development machine. Use TFLite quantization-aware training (QAT) instead of post-training quantization, which requires retraining the full 45-epoch training run on the ESP32 itself to inject quantization noise during backpropagation.
- **Correct Answer:** A) Train on development machine → TFLite conversion → int8 quantization → C array → TFLM inference on ESP32.
- **Distractor Analysis:**
  - *Why A is correct:* This is the canonical TinyML workflow. Training always happens on capable hardware with GPUs. The model is converted to TFLite format and quantized to int8 using TFLiteConverter with a representative dataset. `xxd -i` converts the binary TFLite file to a C byte array that is compiled into firmware. TFLM on the ESP32 loads this array and runs inference. Each stage is the correct tool for its role.
  - *Why B is incorrect:* On-device training (online learning with weight updates) is not supported by TensorFlow Lite Micro. TFLM is an inference-only runtime — it cannot perform backpropagation or weight updates. The ESP32 also lacks the memory required for training (gradient storage requires a copy of all activations plus gradients — several times the model size).
  - *Why C is incorrect:* The full Keras model runtime cannot run on an ESP32. Keras requires TensorFlow, which requires a full OS, dynamic memory allocation, and significantly more RAM than 520 KB. The conversion to TFLM format is mandatory, not optional.
  - *Why D is incorrect:* Quantization-aware training (QAT) is performed on the development machine during training — not on the ESP32. QAT inserts fake quantization nodes into the Keras training graph and runs backpropagation with quantization noise, all on the development machine with GPU acceleration. The ESP32 is never involved in QAT.

---

# Quiz: Module 13 - IoT Analytics and Machine Learning at the Edge
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

**Question 1**
What is the primary advantage of running machine learning inference at the edge rather than sending all sensor data to the cloud for processing?
*   A) Edge inference eliminates the need for sensor hardware because the ML model can synthesize realistic sensor readings without physical transducers.
*   B) Processing data locally near the source reduces round-trip latency to milliseconds, decreases upstream bandwidth consumption, and enables inference to continue during cloud connectivity outages.
*   C) Edge inference runs without electrical power because neural network computations are performed passively by the device's radio antenna.
*   D) Edge ML models compile directly into web client JavaScript, enabling browser-based dashboards to perform inference without a backend server.
*   **Correct Answer:** B) Processing data locally reduces round-trip latency, decreases bandwidth consumption, and enables inference during cloud connectivity outages.
*   **Distractor Analysis:**
    *   *Why correct:* A cloud round-trip for inference adds 50–200 ms of network latency, which is unacceptable for real-time control or safety applications. Running inference locally on a gateway or microcontroller achieves 1–50 ms inference latency, eliminates the cost and bandwidth of transmitting raw sensor streams to the cloud, and continues operating when the WAN link is unavailable.
    *   Edge nodes still require hardware and power. ML models do not synthesize sensor data and are not executed by radio antennas. Edge ML inference runs on embedded processors, not browser JavaScript engines.

---

**Question 2**
Which of the following is the most accurate definition of **model quantization** in the context of deploying machine learning to edge IoT devices?
*   A) The process of dividing a large neural network into smaller sub-networks and distributing them across multiple edge nodes to parallelize inference across a cluster of low-power devices.
*   B) A model compression technique that reduces the numerical precision of weights and activations from 32-bit floating point to lower-precision integers (INT8 or INT4), reducing model size, memory footprint, and inference latency with a small accuracy trade-off.
*   C) A data preprocessing step that normalizes raw sensor readings to a fixed numerical range before feeding them into a neural network, ensuring stable gradient descent during training.
*   D) The process of converting a trained Keras model to ONNX format for cross-platform deployment, enabling the same model to run on both ARM and x86 hardware without recompilation.
*   **Correct Answer:** B) A compression technique reducing weight precision from FP32 to INT8/INT4, cutting model size and inference latency with a small accuracy cost.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes model parallelism or distributed inference — splitting a model across multiple devices. Quantization operates on a single model's numerical representation, not its distribution across devices.
    *   *Why B is correct:* INT8 quantization replaces 32-bit floating-point weights (4 bytes each) with 8-bit integers (1 byte each), achieving a 4x model size reduction. On microcontrollers with hardware INT8 multiply-accumulate units (ARM Cortex-M4, M7), quantized inference is also 2–4x faster. This makes models that were too large for embedded flash feasible for deployment.
    *   *Why C is incorrect:* This describes feature normalization or input scaling — a data preprocessing technique, not model compression.
    *   *Why D is incorrect:* This describes model format conversion for cross-platform compatibility (ONNX export). While useful, it does not reduce model size or inference latency the way quantization does.

---

**Question 3**
A predictive maintenance engineer wants to detect bearing faults in industrial motors using vibration sensor data. Historical records show only 12 labeled examples of bearing failures across 5 years of operation, but 50,000 hours of normal-operation data are available. Which machine learning approach is most appropriate?
*   A) A supervised multi-class classifier trained on the 12 labeled fault examples, using data augmentation to expand the fault class to 1,000 synthetic examples before training.
*   B) An unsupervised anomaly detection model trained exclusively on normal-operation data, which flags vibration patterns that deviate significantly from the learned normal baseline as potential faults.
*   C) A reinforcement learning agent that receives a reward signal when it correctly identifies a fault, training in simulation until it achieves 95% accuracy before deployment.
*   D) A large language model (LLM) fine-tuned on maintenance manual text to interpret vibration frequency descriptions and classify fault types from natural language sensor summaries.
*   **Correct Answer:** B) An unsupervised anomaly detection model trained on normal-operation data.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* 12 labeled fault examples is severely insufficient for a supervised classifier — even with augmentation, the model will overfit to those specific 12 examples and fail to generalize to unseen fault signatures. Supervised classification requires hundreds to thousands of labeled examples per class.
    *   *Why B is correct:* Anomaly detection requires only normal-operation data to train — it learns "what normal looks like" and flags deviations. With 50,000 hours of normal data available, the model will robustly characterize normal bearing vibration. The 12 fault examples can be used for evaluation but are not needed for training.
    *   *Why C is incorrect:* Reinforcement learning requires a simulation environment and reward function that accurately replicates bearing fault dynamics — prohibitively complex for this application. It is not the standard approach for predictive maintenance.
    *   *Why D is incorrect:* LLMs process text, not time-series vibration data. Converting vibration signals to natural language descriptions and back is a lossy, impractical intermediate representation that discards the precise frequency and amplitude information needed for fault detection.

---

**Question 4**
A security researcher demonstrates that by presenting a 3-second audio clip to a voice-activated IoT lock's on-device speech recognition model, the attacker can consistently cause the model to transcribe "unlock" when the actual spoken word was "hello." The researcher crafted the audio by adding an imperceptible noise pattern to the benign "hello" recording. What type of attack is this?
*   A) A replay attack, where the attacker records a legitimate "unlock" command and replays it to the device.
*   B) An adversarial input attack, where a carefully crafted perturbation added to an innocent input causes an ML model to produce a targeted misclassification.
*   C) A model extraction attack, where the attacker queries the inference API thousands of times to reconstruct the model's weights and replicate it on their own hardware.
*   D) A side-channel attack, where the attacker measures the device's power consumption during inference to determine which word the model is classifying.
*   **Correct Answer:** B) An adversarial input attack causing targeted misclassification through imperceptible input perturbation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A replay attack uses a recorded authentic command — the attacker says or plays back the actual word "unlock." The scenario describes crafting a modified version of a different word ("hello") that is misclassified, which is adversarial perturbation, not replay.
    *   *Why B is correct:* Adversarial examples are inputs modified by adding small, carefully computed perturbations that are imperceptible to humans but cause an ML model to produce an attacker-chosen output. This is a known vulnerability of neural network classifiers, including on-device speech and image recognition models.
    *   *Why C is incorrect:* Model extraction involves making many queries to infer model behavior — the researcher is crafting a single adversarial input, not performing a systematic query campaign to reconstruct weights.
    *   *Why D is incorrect:* Side-channel attacks measure physical emanations (power, electromagnetic, timing) to extract secrets — the scenario describes manipulating the input to produce a wrong output, not observing physical signals to extract information.

---

**Question 5**
An engineer trains an INT8-quantized TFLite anomaly detection model and evaluates it on a test set of 1,000 samples: 950 normal and 50 known anomalies. The model correctly identifies 45 of the 50 anomalies (true positives) but also flags 190 normal samples as anomalies (false positives). What is the false positive rate, and why does it matter for a deployed industrial IoT monitoring system?
*   A) False positive rate = 45/950 = 4.7%; this is acceptable because the model detects 90% of true anomalies.
*   B) False positive rate = 190/950 = 20%; this means 1 in 5 normal readings triggers an alert, which would overwhelm maintenance teams with false alarms and cause alert fatigue — operators begin ignoring alerts, defeating the purpose of the detection system.
*   C) False positive rate = 190/1000 = 19%; this is calculated against the total test set and represents the model's overall error rate, which must be compared against the manufacturer's specified accuracy tolerance.
*   D) False positive rate = 45/50 = 90%; the false positive rate is calculated as the fraction of anomalies correctly detected, which must exceed 85% for industrial certification.
*   **Correct Answer:** B) False positive rate = 190/950 = 20%; this level of false alarms causes alert fatigue and renders the system operationally unusable.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The false positive rate is the proportion of actual normal samples incorrectly flagged, calculated as FP / (FP + TN) = 190 / (190 + 760) = 190/950 = 20%. Option A uses the wrong numerator (45 true positives, not false positives) and wrong denominator.
    *   *Why B is correct:* FPR = FP / (FP + TN) = 190 / 950 = 20%. A 20% false positive rate means every 5 normal readings generates one false alarm. In an industrial system sending thousands of readings per day, this produces hundreds of false alerts daily. Maintenance teams experiencing this volume of false alarms develop alert fatigue — a well-documented failure mode where genuine alerts are ignored because they are buried in noise.
    *   *Why C is incorrect:* Dividing by 1,000 (total samples) computes a different metric (error rate), not the false positive rate. The false positive rate specifically measures how often normal samples are incorrectly classified as anomalous.
    *   *Why D is incorrect:* 45/50 = 90% is the true positive rate (recall/sensitivity) — the fraction of actual anomalies correctly detected. This is a different metric from the false positive rate.

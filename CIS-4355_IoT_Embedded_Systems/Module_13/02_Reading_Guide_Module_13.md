# Reading Guide: Module 13 - IoT Analytics and Machine Learning at the Edge
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 13 – IoT Analytics and Machine Learning at the Edge**! This module examines how machine learning models are trained, compressed, and deployed onto resource-constrained edge devices to enable real-time inference without a cloud round-trip. Running ML inference at the edge is increasingly important for applications where latency, bandwidth, or privacy constraints make cloud-based inference impractical — from predictive maintenance on industrial equipment to anomaly detection on smart home gateways.

You will learn how TensorFlow Lite and Edge Impulse enable model compression (quantization, pruning) for deployment on microcontrollers and single-board computers, how anomaly detection models identify out-of-distribution sensor readings, and how model performance metrics (accuracy, precision, recall, inference latency) guide the trade-off between model complexity and edge compute constraints. Security considerations — including adversarial inputs to edge ML models and protecting model intellectual property on deployed hardware — are addressed throughout.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **TensorFlow Lite (TFLite)**: A lightweight version of Google's TensorFlow ML framework optimized for inference on mobile and embedded devices. TFLite converts trained models into a FlatBuffer format (.tflite) and applies quantization to reduce model size and inference latency. A floating-point model quantized to INT8 typically achieves a 4x reduction in model size and 2–4x speedup on microcontrollers with hardware INT8 arithmetic (ARM Cortex-M4, M7), at a small accuracy cost.
*   **Model Quantization**: A model compression technique that reduces the numerical precision of model weights and activations from 32-bit floating point (FP32) to lower-precision integers (INT8 or INT4). Quantization reduces model size, memory footprint, and inference latency, making models feasible on microcontrollers with 256 KB of flash and 64 KB of RAM. Post-training quantization applies to an already-trained model; quantization-aware training incorporates quantization into the training loop for higher accuracy.
*   **Anomaly Detection (Unsupervised)**: A machine learning approach that learns a statistical model of "normal" sensor behavior from historical data, then flags readings that deviate significantly from that baseline as anomalies — without requiring labeled examples of each failure mode. Common approaches include autoencoders (reconstructing normal inputs; high reconstruction error = anomaly), isolation forests, and statistical threshold methods. Anomaly detection is widely used in predictive maintenance where labeled fault data is scarce.
*   **Edge Impulse**: A cloud-based platform for building, training, and deploying machine learning models on edge devices (Arduino Nano 33, Raspberry Pi, STM32 microcontrollers). Edge Impulse handles the full pipeline: data collection from device sensors, signal processing, model training (classification, anomaly detection, object detection), and deployment as optimized C++ libraries or TFLite models. It provides latency, RAM, and flash usage estimates for the target hardware before deployment.
*   **Inference Latency vs. Model Accuracy Trade-off**: The fundamental constraint in edge ML: larger, more complex models achieve higher accuracy but require more RAM, flash, and compute time for each inference. On a Cortex-M4 microcontroller, a MobileNet V2 image classifier may take 300 ms per inference — too slow for real-time 30 fps video analysis. Designers must use architecture search, pruning, and quantization to find the smallest model that meets accuracy requirements within the inference latency budget.

---

### 2. Certification Exam Tips
*   **TFLite model pipeline:** Memorize: train full model (Keras/PyTorch) on cloud → convert to .tflite format → apply INT8 quantization → test accuracy on validation set → deploy to edge device. The exam may ask which step reduces model size or which format is used on the edge.
*   **Quantization accuracy impact:** INT8 quantization typically reduces accuracy by 0.5–2% on well-designed models. Quantization-aware training recovers most of this accuracy loss. Exam questions may ask when to choose post-training quantization vs quantization-aware training.
*   **Anomaly detection vs classification:** Classification requires labeled examples of each fault class — impractical when failure modes are rare or unknown. Anomaly detection only requires normal-operation data to train. Use anomaly detection when fault labels are unavailable; use classification when labeled fault data exists.
*   **Security risks for edge ML:** Adversarial inputs — carefully crafted sensor readings that cause an ML model to misclassify — are a real threat for security-critical edge applications (intrusion detection, access control). Model extraction attacks attempt to reconstruct model weights by querying the inference API. Protecting models with secure boot and encrypted flash limits extraction from physical devices.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers insecure data transfer relevant to ML training data pipelines, and insufficient privacy protection relevant to inference on personal sensor data collected at the edge.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on insufficient privacy protection and insecure data transfer sections, which apply to ML training data pipelines that process personal IoT sensor data and edge inference systems that handle sensitive inputs.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) includes coverage of machine learning at the edge, demonstrating TensorFlow Lite model deployment on a Raspberry Pi and comparing inference performance for different model sizes and quantization levels.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Train and convert a TFLite anomaly detection model**: Using Edge Impulse or a local Python environment, train a simple autoencoder on 500 normal temperature sensor readings, export the model as a .tflite file, apply INT8 post-training quantization, and compare the file size and inference latency between the FP32 and INT8 versions.
*   **Deploy inference on a Raspberry Pi**: Copy the INT8 .tflite model to a Raspberry Pi, run inference using the TFLite Python interpreter on a stream of sensor readings, and log the inference latency in milliseconds for each prediction.
*   **Evaluate anomaly detection threshold**: Compute the reconstruction error distribution on the validation set of normal readings, set the anomaly threshold at the 99th percentile, then inject 10 synthetic anomalous readings and measure the detection rate (true positive rate) and false alarm rate.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize the TFLite model pipeline steps.
- [ ] Read the insufficient privacy protection section at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the edge ML sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Review quantization trade-offs and anomaly detection vs classification decision criteria before the lab.
- [ ] Proceed to the weekly hands-on lab activity.

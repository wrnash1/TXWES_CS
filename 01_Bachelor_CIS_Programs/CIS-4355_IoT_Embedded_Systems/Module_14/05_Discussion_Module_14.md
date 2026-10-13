# Discussion Forum: Module 14 — Machine Learning for IoT

## Course: CIS-4355 IoT and Embedded Systems

## Texas Wesleyan University | Professor Nash

Certification Alignment: IoT Fundamentals / Embedded Systems

---

## Overview

This week's discussion connects TinyML concepts to real engineering decisions. Each scenario presents a situation where a team must choose whether and how to deploy on-device machine learning — and the trade-offs are significant. Your post should demonstrate that you can evaluate these choices technically, not just recite definitions.

---

## Scenario 1 — Privacy vs. Accuracy: The In-Home Health Monitor

A startup is building a wearable device that monitors breathing patterns during sleep to detect apnea events. The device includes a microphone (for snoring detection), an accelerometer (for movement), and a pulse oximeter (blood oxygen saturation). The initial architecture sends all raw sensor data to a cloud backend that runs the detection model on a GPU server.

A privacy advocacy group raises concerns: the device captures continuous audio in the user's bedroom and transmits it to a company's servers. The startup's investors push for switching to on-device inference using TinyML so that no raw data ever leaves the device.

Discuss the following:

- What are the specific technical constraints that make on-device sleep apnea detection harder than cloud-based detection? Address at least two constraints: memory, latency, model complexity, or data availability for training.
- The model accuracy in the cloud version is 96.8%. After designing a small TinyML model, optimizing with int8 quantization, and running on the device, the on-device model achieves 91.2% accuracy. Is this accuracy trade-off acceptable for a medical monitoring device? Justify your position with reference to the consequences of false negatives and false positives in this application.
- Beyond privacy, what is one additional operational advantage of on-device inference for this wearable? Explain it technically.

Your initial post should be 175–225 words and take a position on the accuracy trade-off with technical justification.

---

## Scenario 2 — Concept Drift in Industrial Anomaly Detection

A manufacturing plant deployed TFLM-based anomaly detection on 40 industrial pumps six months ago. The model was trained on vibration data collected in January. In July, the plant switches to a heavier-viscosity fluid for summer operations, and all 40 pumps immediately begin generating anomaly alerts — even though the pumps are mechanically healthy and operating within specification.

The plant's ML engineer proposes three options:

Option A: Increase the anomaly threshold on all 40 devices via OTA configuration update to silence the false alerts.

Option B: Collect 2 weeks of new normal-operation data (with the new fluid), retrain the autoencoder models on the development server, quantize the updated models, and deploy the new firmware to all 40 pumps via OTA.

Option C: Implement a "baseline reset" feature where an operator can put the device in "learning mode" for 24 hours, during which the device streams raw vibration data to the cloud, trains a new model in the cloud, quantizes it, and pushes it back to the device.

Discuss the following:

- What are the specific risks of Option A? Consider both the short-term operational impact and the long-term safety impact.
- Compare Options B and C on three dimensions: time to resolution, operational complexity, and appropriateness for detecting future bearing faults.
- Which option would you recommend and why? Are there conditions under which a different option is preferable?

Your initial post should be 175–225 words with a clear recommendation and specific technical justification.

---

## Scenario 3 — Model Architecture Selection for a Wildlife Camera

A conservation organization is deploying 500 camera traps in a remote rainforest to detect poachers. Each camera uses a Cortex-M7 microcontroller (1 MB SRAM, 2 MB flash) with a low-power image sensor. The camera must classify whether an image contains a person, an animal, or nothing — and trigger a LoRa alert only when a person is detected. The cameras run on four AA batteries and must last 12 months.

A team member proposes using MobileNetV2-1.0 (the full-size MobileNet) quantized to int8. The model is 3.4 MB quantized. A second team member proposes MobileNetV1-0.25 quantized to int8, which is 470 KB but achieves 68% accuracy on person detection vs. MobileNetV2-1.0's 84% accuracy.

Discuss the following:

- The full MobileNetV2-1.0 model at 3.4 MB exceeds the 2 MB flash. What are two approaches to address this constraint? Evaluate each approach's trade-offs for this application.
- The MobileNetV1-0.25 model at 68% accuracy means approximately 32 out of every 100 persons are missed (false negatives). In a poacher detection application, what is the consequence of this false negative rate and is it acceptable?
- How does the power budget constraint interact with the model selection decision? Specifically, how does inference latency affect battery life, and what is the relationship between model size and inference time on a Cortex-M7?

Your initial post should be 175–225 words. Peer responses should address the power calculation specifically.

---

## Discussion Instructions

### Initial Post

Due: Wednesday at 11:59 PM

Choose one scenario (or address all three for extra credit). Write 175–225 words per scenario addressed. Your post must:

- Reference specific TinyML concepts from the module (quantization, model size, inference latency, representative dataset, autoencoder, concept drift)
- Take a clear position where a decision is required
- Acknowledge the trade-off your position accepts

### Peer Responses

Due: Sunday at 11:59 PM

Reply to at least two classmates (minimum 60 words each). In your replies:

- Evaluate whether their accuracy threshold argument in Scenario 1 accounts for both false positive and false negative consequences
- In Scenario 2, verify that their recommended option addresses both the immediate alert problem and the long-term bearing fault detection capability
- In Scenario 3, provide or check the power calculation linking inference frequency to daily energy consumption

---

## Discussion Rubric (10 Points Total)

### Initial Post — 6 Points

- 5–6 pts: Addresses all sub-questions. Correct use of TinyML terminology. Clear position with technical justification. Explicit acknowledgment of trade-offs. Meets 175-word minimum.
- 3–4 pts: Addresses most sub-questions. Some TinyML terminology used but not always precisely. Position taken but justification is general rather than technical.
- 0–2 pts: Post missing, significantly below word count, or does not engage with the technical content of the scenario.

### Peer Responses — 4 Points

- 4 pts: Two substantive replies that add technical value — verify calculations, challenge assumptions, or propose specific alternatives. Each meets the 60-word minimum.
- 2 pts: One substantive reply, or two replies that agree without adding technical content.
- 0 pts: No peer responses submitted.

---

# Quiz: Module 15 — Emerging AI Technologies

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. The quiz is closed-book and should be completed in 20 minutes.

---

## Questions

**Question 1**

A hospital system wants to train a shared AI model that improves diagnoses using X-ray data from 40 hospitals across three countries. Privacy laws prevent any hospital from sharing patient imaging data with external parties. Which technology directly enables training across all 40 hospitals without centralizing the raw images?

A. Transfer learning from a pretrained public model

B. Federated learning with local training and aggregated model updates

C. Differential privacy applied to the test dataset

D. Model distillation using a single hospital's data as the teacher

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Transfer learning uses a pretrained model to improve performance on a new task with limited data. It does not address the multi-hospital training coordination problem or eliminate the need to centralize data.
- **B** is correct. Federated learning trains local models at each hospital using local patient data, then aggregates only the model weight updates. No raw imaging data is transmitted to any external party.
- **C** is incorrect. Differential privacy protects individual records in published statistics or models. It does not enable multi-institution training coordination.
- **D** is incorrect. Knowledge distillation trains a small student model from a large teacher model. It still requires centralized training data to produce the teacher model.

---

**Question 2**

A multimodal AI model accepts both a photograph of a product and a written description, and then generates a quality assessment report combining visual and textual analysis. What architectural component enables the model to reason jointly across the image and text inputs?

A. A recurrent neural network that processes both modalities sequentially

B. A cross-modal projection layer that maps image embeddings into the language model's token space

C. A decision tree ensemble that evaluates visual and textual features independently

D. A rule-based expert system that applies predefined criteria to both inputs

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. While RNNs can process sequences, they do not provide the joint multimodal representation that enables simultaneous reasoning. Modern multimodal models use transformers, not RNNs.
- **B** is correct. Cross-modal projection layers translate the output of vision encoders into the embedding space of the language model backbone, enabling the language model to attend to image content as if it were text tokens.
- **C** is incorrect. Decision tree ensembles evaluate features independently or in combination but do not produce the joint semantic representations needed for language-vision reasoning.
- **D** is incorrect. Rule-based systems use predefined logic, not learned representations. They do not qualify as AI models that "reason jointly."

---

**Question 3**

An AI agent is given the goal: "Research the top three competitors in our market, summarize their recent product announcements, and email a report to the marketing team." To complete this task, which combination of capabilities must the agent have?

A. Image generation and speech-to-text transcription

B. Web search, document summarization, and email API access

C. Differential privacy and model quantization

D. A federated learning coordinator and a classification model

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. Image generation creates new images; speech-to-text converts audio. Neither is needed for researching text-based competitor news and emailing a report.
- **B** is correct. The agent needs web search to find competitor information, a summarization capability (built into the language model), and email API access to send the final report. These are the three tools the task requires.
- **C** is incorrect. Differential privacy and model quantization are ML training and deployment techniques, not agent tools needed for this business task.
- **D** is incorrect. Federated learning is for distributed model training across institutions. A classification model alone does not execute a multi-step research and communication workflow.

---

**Question 4**

A factory's quality control system uses a computer vision model that must make defect decisions within 2 milliseconds on a device embedded in the production line. The production line has no reliable internet connectivity. Which deployment approach is most appropriate?

A. Cloud inference via a managed online endpoint in Azure

B. Batch endpoint with nightly aggregated defect reports

C. Edge AI deployment on a local device using a quantized ONNX model

D. A federated learning coordinator that aggregates defect data from all production lines

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Cloud inference requires internet connectivity and has latency of 100–500ms. Both the latency requirement (2ms) and the connectivity constraint rule out cloud inference.
- **B** is incorrect. Batch endpoints process data asynchronously in bulk. Real-time 2ms decisions on a production line require synchronous, local inference.
- **C** is correct. Edge AI on a local embedded device eliminates network dependency and latency. A quantized ONNX model runs efficiently on constrained hardware with sub-millisecond inference times.
- **D** is incorrect. A federated learning coordinator manages distributed model training — it is a training architecture, not an inference deployment for real-time production decisions.

---

**Question 5**

Which of the following best describes the ReAct (Reasoning + Acting) pattern used by AI agents?

A. A neural architecture where reasoning and perception layers alternate in the model structure

B. An agent loop where the model alternates between reasoning about what to do, executing a tool action, and observing the result

C. A training method that interleaves supervised and reinforcement learning for improved reasoning

D. A data augmentation technique that combines reasoning examples with action examples in the training set

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. ReAct is not a neural network architecture. It is a reasoning and action pattern at the agent inference/execution level.
- **B** is correct. ReAct is the pattern where an agent generates a thought ("I need to find X"), takes an action (call tool Y), observes the result, and then reasons again about the next step. This cycle continues until the task is complete.
- **C** is incorrect. ReAct is not a training method. It is an inference-time pattern for structuring how an agent uses tools.
- **D** is incorrect. Data augmentation is a training technique unrelated to the ReAct agent execution pattern.

---

**Question 6**

A model is reduced from 32-bit floating point precision to 8-bit integer precision before deployment to a mobile device. What is this technique called, and what is its primary benefit?

A. Pruning; removes neurons that are not needed for the target task

B. Knowledge distillation; trains a small student model to replicate a teacher model

C. Quantization; reduces model file size and memory requirements with minimal accuracy loss

D. Fine-tuning; adapts a general model to a specific domain with additional training

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. Pruning removes weights close to zero to create a sparse model — it is not the technique of reducing numerical precision.
- **B** is incorrect. Knowledge distillation trains a separate smaller model from a larger one. It does not change the precision of existing model weights.
- **C** is correct. Quantization reduces the numerical precision of model weights — from FP32 to INT8 is the most common form. This reduces model size by approximately 4x with modest accuracy loss, enabling deployment on constrained edge hardware.
- **D** is incorrect. Fine-tuning adapts a pretrained model to a specific domain or task through additional training. It does not change the numerical precision of weights.

---

**Question 7**

Which of the following is the most accurate characterization of quantum machine learning's readiness for production deployments in 2026?

A. Quantum ML has achieved demonstrated advantages over classical ML on several benchmark tasks and is being adopted by major enterprises.

B. Quantum ML is primarily a research area; practical quantum advantage over classical ML on real production problems has not been conclusively demonstrated.

C. Quantum ML has replaced deep learning for optimization problems but remains immature for classification.

D. Quantum ML is ready for production on Azure Quantum but not available on other cloud platforms.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. As of 2026, no conclusive quantum advantage over classical ML on practical production tasks has been demonstrated. Current quantum hardware remains noisy and limited in qubit count.
- **B** is correct. Quantum ML is an active research field with theoretical promise but no production-proven advantage. Current NISQ devices have significant error rates. This is an honest and accurate assessment of the field's maturity.
- **C** is incorrect. Quantum ML has not replaced deep learning for any production optimization task. The claim of replacement overstates current capabilities.
- **D** is incorrect. Quantum hardware availability is not the limiting factor — the limiting factor is that quantum algorithms have not demonstrated practical advantages for ML tasks on any platform.

---

**Question 8**

What is the primary privacy limitation of federated learning that is often addressed by combining it with differential privacy?

A. Federated learning sends raw data to the central server during the aggregation step.

B. Federated learning model updates (gradients) can potentially leak information about individual training records through gradient inversion attacks.

C. Federated learning requires data to be centralized for the initial model training step.

D. Federated learning cannot protect privacy for more than 100 participating devices.

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. The entire point of federated learning is that raw data never leaves the local device. Only model updates (weight differences) are transmitted.
- **B** is correct. Gradient inversion attacks can reconstruct training data from gradient updates. An attacker who intercepts or controls the server can potentially recover individual training samples from the gradient updates. Differential privacy adds noise to gradients before transmission, preventing this reconstruction.
- **C** is incorrect. Federated learning specifically avoids centralizing training data. The initial model (randomly initialized) is sent to clients; no data moves to the server.
- **D** is incorrect. There is no device count threshold beyond which federated learning loses privacy protection. This is not a real limitation.

---

**Question 9**

Azure AI Agent Service uses a "thread" abstraction to manage agent interactions. What does a thread represent?

A. A parallel compute process running on a separate virtual machine

B. A persistent conversation history and context for a sequence of agent interactions

C. A code execution environment for running Python tools

D. A network connection to an external API used by the agent

**Correct Answer: B**

**Distractor Analysis:**

- **A** is incorrect. A thread in the agent context is not a compute thread. It is a logical conversation container, not a parallel execution process.
- **B** is correct. In Azure AI Agent Service, a thread stores the conversation history — the sequence of messages, tool calls, and observations — that constitutes a multi-turn agent interaction. This gives the agent persistent memory within a session.
- **C** is incorrect. Code execution is handled by the code interpreter tool, not by the thread abstraction.
- **D** is incorrect. API connections are configured as tools. The thread stores conversation history, not network connections.

---

**Question 10**

For the AI-900 certification exam, which of the following emerging AI capabilities is most directly tested?

A. Implementing FedAvg gradient aggregation in Python

B. Configuring quantum circuit parameters in Azure Quantum

C. Describing the capabilities of Azure OpenAI Service including generative AI and multimodal features

D. Optimizing ONNX model quantization for specific edge hardware

**Correct Answer: C**

**Distractor Analysis:**

- **A** is incorrect. The AI-900 is a conceptual/fundamentals exam. It does not test Python implementation of federated learning algorithms.
- **B** is incorrect. The AI-900 does not cover quantum computing configuration. Azure Quantum is outside the AI-900 exam scope.
- **C** is correct. The AI-900 exam's generative AI domain (25–30% of the exam) directly tests knowledge of Azure OpenAI Service capabilities — including what tasks generative AI and multimodal AI can perform — and responsible use of these services.
- **D** is incorrect. Model quantization configuration for edge hardware is a practitioner-level skill tested in higher-level certifications like AI-102 or DP-100, not AI-900.

---

*Quiz prepared by Professor Nash | Texas Wesleyan University | CIS-4330*

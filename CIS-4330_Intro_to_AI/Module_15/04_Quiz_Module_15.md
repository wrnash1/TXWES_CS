# Quiz: Module 15 — Emerging AI Technologies

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Instructions

This quiz contains 10 multiple-choice questions. Each question is worth 10 points for a total of 100 points. Select the single best answer for each question. Review your reading guide and video notes before attempting the quiz.

---

## Questions

### Question 1

A hospital system wants to train a disease prediction model across five partner institutions without any institution transmitting patient records outside its own data center. Each institution trains the model locally and sends only parameter updates to a central aggregator. Which technology enables this architecture?

A) Edge AI with ONNX Runtime

B) Multimodal AI with cross-attention

C) Federated learning with FedAvg aggregation

D) Knowledge distillation from a teacher model

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** Edge AI addresses local inference on-device to avoid cloud round trips. It does not describe a collaborative training architecture across multiple institutions.
- **B — Incorrect.** Cross-attention in multimodal AI enables reasoning across data modalities within a single model. It is not a distributed training paradigm.
- **C — Correct.** Federated learning enables collaborative model training across distributed data sources by sharing model updates rather than raw data. FedAvg aggregates client updates by weighted averaging at the central server, and patient records never leave each institution.
- **D — Incorrect.** Knowledge distillation trains a small student model to mimic a large teacher model. It involves a single training process and does not address distributed data ownership across institutions.

---

### Question 2

OpenAI's CLIP model demonstrated an important multimodal capability: classifying images into categories that were not part of the training data, guided only by natural language descriptions of those categories. What is this capability called?

A) Transfer learning

B) Zero-shot classification

C) Few-shot prompting

D) Supervised fine-tuning

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Transfer learning refers to adapting a pre-trained model to a new task through fine-tuning on labeled examples from that task. CLIP's capability does not require any fine-tuning on the new categories.
- **B — Correct.** Zero-shot classification is the ability to classify inputs into categories the model has never explicitly seen during training, using only natural language descriptions of those categories. CLIP achieves this by aligning image and text embeddings in a shared space during contrastive pretraining.
- **C — Incorrect.** Few-shot prompting provides a small number of labeled examples to guide model behavior. CLIP's zero-shot classification requires no examples of the new categories at inference time.
- **D — Incorrect.** Supervised fine-tuning updates model weights on labeled examples from a target task. This is the opposite of zero-shot classification, which requires no task-specific training.

---

### Question 3

A manufacturing company deploys an AI defect detection model directly on factory floor cameras to inspect products at 60 frames per second. The cameras have no reliable internet connectivity and must make accept/reject decisions in under 5 milliseconds. Which deployment approach is most appropriate?

A) Cloud-hosted inference via Azure Cognitive Services REST API

B) Edge AI with an on-device quantized model using ONNX Runtime

C) Federated learning aggregation server in the factory network

D) A multimodal model combining camera feeds and ERP system text

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Cloud API inference requires reliable internet connectivity and introduces network round-trip latency of 50–500 ms, both of which violate the stated requirements.
- **B — Correct.** Edge AI runs the model locally on the camera hardware, eliminating network dependency and achieving sub-millisecond to single-digit millisecond inference latency. Quantization reduces model size to fit constrained camera hardware. ONNX Runtime is specifically optimized for this cross-platform edge deployment scenario.
- **C — Incorrect.** A federated learning aggregation server is a training infrastructure component. It does not enable real-time inference and does not address connectivity or latency requirements.
- **D — Incorrect.** A multimodal model combining camera and ERP data could add analytical value but does not solve the core requirements of offline operation and sub-5 ms latency.

---

### Question 4

In the FedAvg algorithm, how are model updates from participating clients combined to produce the next global model?

A) The server selects the single best-performing client model and discards the others.

B) The server computes a weighted average of client parameter updates, weighted by each client's dataset size.

C) The server trains a meta-model that learns to combine client predictions at inference time.

D) Clients vote on each individual parameter, and the majority value is used.

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Selecting only one client model would discard the knowledge contributed by all other participants, defeating the purpose of collaborative training.
- **B — Correct.** FedAvg (McMahan et al., 2017) computes a weighted average of client model updates. Clients contributing larger datasets receive proportionally higher weight in the aggregation, ensuring that the global model reflects the full data distribution across all clients.
- **C — Incorrect.** Training a meta-model to combine predictions is a technique called stacking or ensemble learning. It is not the FedAvg aggregation strategy and would require sharing more data than just weight updates.
- **D — Incorrect.** Per-parameter majority voting is not a standard aggregation method in federated learning. It would be computationally expensive and would not produce a well-calibrated combined model.

---

### Question 5

Microsoft's **Semantic Kernel** SDK is best described as which of the following?

A) A hardware abstraction layer for running AI models on edge NPU processors

B) An SDK that connects large language models to external tools and data sources through a plugin architecture

C) A multi-agent framework where specialized AI agents communicate through a shared message bus

D) A differential privacy library for training LLMs with formal (ε, δ) guarantees

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Hardware abstraction for edge NPU deployment is the role of ONNX Runtime and platform-specific inference engines. Semantic Kernel operates at the application orchestration layer, not the hardware layer.
- **B — Correct.** Semantic Kernel is a Microsoft SDK that allows developers to integrate LLMs into applications by defining plugins — structured descriptions of available functions — that the model can reason about and invoke. It handles memory management, planning, and function orchestration.
- **C — Incorrect.** A multi-agent framework with a shared message bus describes AutoGen, a separate Microsoft Research project. While both AutoGen and Semantic Kernel support agent architectures, the description of plugins and tool integration specifically characterizes Semantic Kernel.
- **D — Incorrect.** Differential privacy training is supported by the SmartNoise/OpenDP toolkit and TensorFlow Privacy, not Semantic Kernel.

---

### Question 6

Under the EU AI Act, which of the following AI systems falls into the **high-risk** category subject to conformity assessments, technical documentation, and mandatory human oversight requirements?

A) A recommendation algorithm suggesting products on an e-commerce website

B) A chatbot that discloses it is an AI when users ask

C) An AI system used by employers to rank job candidates and make hiring decisions

D) A spam filter that automatically routes emails to a junk folder

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** Product recommendation systems are classified as minimal risk under the EU AI Act. They do not produce legal or similarly significant effects on individuals and have no specific obligations beyond general product safety law.
- **B — Incorrect.** A chatbot that discloses its AI nature falls under the limited-risk tier, which requires transparency (disclosure that the user is interacting with AI) but not conformity assessments or mandatory human oversight.
- **C — Correct.** Employment and worker management AI — including systems used for recruitment, hiring, task allocation, and performance monitoring — is explicitly listed in Annex III of the EU AI Act as a high-risk AI application requiring conformity assessment, technical documentation, human oversight mechanisms, and registration in the EU database.
- **D — Incorrect.** Spam filtering produces a minor, reversible effect and is classified as minimal risk. It does not affect individuals' legal rights or significantly significant interests.

---

### Question 7

A data scientist applies dynamic INT8 quantization to a neural network model before deploying it to a mobile device. Which of the following best describes what quantization does to the model?

A) It trains a smaller model from scratch using the original model's predictions as soft labels.

B) It removes entire convolutional filters whose output norms fall below a threshold.

C) It replaces 32-bit floating-point weight values with 8-bit integer representations, reducing model size and memory footprint.

D) It splits the model into a server-side teacher and a device-side student that communicate at inference time.

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** Training a smaller model using a larger model's predictions as soft labels is knowledge distillation. It produces a separate student model and requires a full training run.
- **B — Incorrect.** Removing filters below a norm threshold is structured pruning. It reduces the number of parameters by eliminating entire network substructures rather than changing numerical precision.
- **C — Correct.** Quantization reduces the numerical precision of model weights from FP32 (4 bytes per value) to INT8 (1 byte per value), achieving approximately a 4x reduction in model size and memory bandwidth requirements with typically minimal accuracy loss.
- **D — Incorrect.** Splitting a model between a server and device with runtime communication is split computing, a deployment architecture distinct from quantization.

---

### Question 8

A research group working on quantum machine learning reports that their variational quantum circuit classifier achieves competitive accuracy on a small benchmark dataset using a 20-qubit NISQ device. What is the most accurate characterization of this result for enterprise AI practitioners?

A) Quantum ML has achieved practical production readiness and should replace classical ML pipelines for classification tasks.

B) The result is a promising research demonstration, but NISQ limitations mean quantum ML is not yet practically advantageous for real-world ML workloads at scale.

C) Azure Quantum already provides NISQ-based ML services that outperform classical Azure ML on standard tabular datasets.

D) The 20-qubit result proves that fault-tolerant quantum computers are now available for commercial use.

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** NISQ devices have high error rates and limited qubit counts that restrict circuit depth and problem scale. No NISQ quantum ML system has demonstrated practical advantage over classical ML on real-world datasets.
- **B — Correct.** NISQ devices represent a valuable research platform but are not yet practically superior to classical ML for enterprise workloads. Practical quantum advantage for ML likely requires fault-tolerant quantum computers with millions of logical qubits, which are a decade or more away from current hardware.
- **C — Incorrect.** Azure Quantum provides access to quantum hardware for research purposes. It does not offer quantum ML services that outperform Azure Machine Learning on standard enterprise datasets.
- **D — Incorrect.** NISQ devices are explicitly not fault-tolerant. Fault-tolerant quantum computing requires error correction codes that demand millions of physical qubits per logical qubit — far beyond current 20-qubit demonstrations.

---

### Question 9

An AI agent built with Microsoft AutoGen is performing a multi-step task: researching a topic, drafting a report, and emailing it to a distribution list. At which step should the responsible design pattern require human approval before the agent proceeds?

A) Searching the web for research sources

B) Drafting the initial report text in memory

C) Sending the email to the distribution list

D) Summarizing source documents into bullet points

**Correct Answer: C**

**Distractor Analysis:**

- **A — Incorrect.** Web search is a low-stakes, easily reversible information-gathering action. Autonomous execution without human approval is appropriate and is the efficiency advantage of agentic systems.
- **B — Incorrect.** Drafting text in memory is an internal, non-externalized action with no external effect. The agent should proceed autonomously; the human can review the draft before it is sent.
- **C — Correct.** Sending an email is an externalized, potentially irreversible action with real-world consequences (the recipients receive the message and may act on it). The responsible human-in-the-loop design pattern requires human review and approval before any high-stakes, irreversible, or externally visible action is taken.
- **D — Incorrect.** Summarizing text is an internal reasoning step with no external effect. Autonomous summarization is both appropriate and is a core value-add of agentic AI.

---

### Question 10

The NIST AI Risk Management Framework (AI RMF 1.0) organizes AI risk management around four core functions. Which set correctly names all four functions?

A) Identify, Protect, Detect, Respond

B) Govern, Map, Measure, Manage

C) Plan, Build, Evaluate, Deploy

D) Assess, Mitigate, Monitor, Report

**Correct Answer: B**

**Distractor Analysis:**

- **A — Incorrect.** Identify, Protect, Detect, Respond (plus Recover) are the five functions of the NIST Cybersecurity Framework (CSF), not the AI RMF. These are related but distinct frameworks for different risk domains.
- **B — Correct.** The NIST AI RMF 1.0 (January 2023) organizes AI risk management around four functions: Govern (establishing policies, accountability, and culture), Map (identifying and categorizing AI risks), Measure (analyzing and assessing identified risks), and Manage (prioritizing and treating risks through controls and responses).
- **C — Incorrect.** Plan, Build, Evaluate, Deploy describes a generic software development lifecycle, not the NIST AI RMF structure.
- **D — Incorrect.** Assess, Mitigate, Monitor, Report is a reasonable risk management sequence but does not correspond to the specific function names defined in the NIST AI RMF 1.0.

---

## Answer Key

| Question | Answer |
|---|---|
| 1 | C |
| 2 | B |
| 3 | B |
| 4 | B |
| 5 | B |
| 6 | C |
| 7 | C |
| 8 | B |
| 9 | C |
| 10 | B |

---

*Quiz Line Count: 175 | Module 15 — Emerging AI Technologies*

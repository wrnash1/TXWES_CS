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
| 11 | D |
| 12 | A |
| 13 | C |
| 14 | B |
| 15 | A |
| 16 | D |
| 17 | C |
| 18 | B |
| 19 | A |
| 20 | D |

---

### Question 11

A smart factory deploys a computer vision model on edge hardware mounted to a conveyor belt to detect defective products in real time. Internet connectivity is intermittent and latency requirements are under 20 milliseconds. Which combination of Azure technologies best supports this architecture?

A) Azure Cognitive Services Vision API called via REST + Azure IoT Hub for telemetry

B) Azure Machine Learning AutoML + Azure Blob Storage for model storage

C) Azure OpenAI GPT-4 Vision + Azure Event Hubs for streaming inference

D) ONNX Runtime for edge inference + Azure IoT Edge for deployment and device management

Correct Answer: D

Distractor Analysis:

- **A — Incorrect.** Calling a cloud REST API requires reliable internet connectivity and introduces round-trip latency incompatible with a 20-millisecond requirement. Intermittent connectivity makes this architecture unreliable.
- **B — Incorrect.** AutoML is a cloud-based training service; it does not address edge inference deployment or the latency constraint.
- **C — Incorrect.** GPT-4 Vision is a large cloud-hosted model; its inference latency far exceeds 20 milliseconds and it requires consistent internet access.
- **D — Correct.** ONNX Runtime runs optimized models locally on edge hardware with no cloud round trip, meeting the latency requirement and operating during connectivity outages. Azure IoT Edge provides containerized deployment, remote model updates, and device management for the edge fleet.

---

### Question 12

A research team is using a federated learning system to train a medical imaging model across 12 hospitals. After 50 rounds of FedAvg aggregation, a security researcher demonstrates that by analyzing the gradient updates submitted by one hospital, they can reconstruct approximate versions of individual patient scans. Which privacy risk does this illustrate?

A) Gradient inversion attack — model gradients can leak information about the training data used to produce them, even when raw data is never shared

B) Model extraction attack — the researcher is stealing the global model by analyzing parameter updates across rounds

C) Data poisoning attack — the hospital's gradient updates are corrupting the global model's training trajectory

D) Backdoor attack — the researcher has implanted a trigger in the gradient updates that causes targeted misclassification

Correct Answer: A

Distractor Analysis:

- **A — Correct.** Gradient inversion (also called gradient leakage) is a known attack on federated learning: sufficiently large or poorly compressed gradient updates contain information about the local training batch, allowing reconstruction of approximate training inputs. This is why defenses like gradient compression, differential privacy on updates, and secure aggregation are applied in sensitive FL deployments.
- **B — Incorrect.** Model extraction steals model functionality through prediction queries, not through internal parameter or gradient analysis.
- **C — Incorrect.** Data poisoning corrupts the model's learned behavior, not the privacy of training data.
- **D — Incorrect.** A backdoor attack embeds a trigger during training to cause targeted misclassification; the researcher here is performing data reconstruction, not implanting a trigger.

---

### Question 13

A developer wants to deploy a large language model to a mobile device that has 4 GB of RAM and no GPU. The original model has 7 billion parameters stored in FP32 format. Which model compression technique would most directly reduce the model's memory footprint to make on-device inference feasible?

A) Knowledge distillation — training a smaller student model to mimic the larger model's outputs

B) Pruning — removing low-importance weight connections from the 7B parameter model

C) Quantization — converting model weights from FP32 (4 bytes per parameter) to INT8 (1 byte per parameter), reducing memory footprint by approximately 75 percent

D) Fine-tuning — updating the model's weights on device-specific data to improve inference efficiency

Correct Answer: C

Distractor Analysis:

- **A — Incorrect.** Knowledge distillation creates a smaller model architecture and requires training infrastructure; it reduces parameter count but is a separate process from deploying the existing model.
- **B — Incorrect.** Pruning removes individual weights, reducing the effective parameter count, but the full weight matrix is typically still stored unless sparse storage formats are used — achieving less memory reduction than quantization for most implementations.
- **C — Correct.** Quantization reduces per-weight storage from 4 bytes (FP32) to 1 byte (INT8), reducing the total model size from approximately 28 GB to approximately 7 GB. Combined with INT4 quantization (now common in on-device LLM deployment), models can be compressed to under 4 GB.
- **D — Incorrect.** Fine-tuning updates model weights but does not reduce model size or memory footprint.

---

### Question 14

A developer is building an AI agent using Microsoft AutoGen that must browse the web, read documents, and write code to complete a multi-step data analysis task. The agent is configured to run fully autonomously without human checkpoints. Which responsible AI concern is most directly raised by this design?

A) Privacy violation — the agent may access personal data without user consent while browsing the web

B) Irreversible action risk — a fully autonomous agent can take externalized actions (writing files, executing code, sending data) that may be difficult or impossible to undo, without human review

C) Fairness concern — the agent may apply biased reasoning when selecting which web sources to trust

D) Transparency concern — users will not be able to distinguish AI-generated analysis from human analysis

Correct Answer: B

Distractor Analysis:

- **A — Incorrect.** Privacy is a valid concern for web-browsing agents but is not the primary concern raised specifically by full autonomy without human checkpoints. Privacy concerns exist in both human-supervised and fully autonomous configurations.
- **B — Correct.** The primary responsible AI concern with fully autonomous multi-step agents is the risk of irreversible actions: code execution can modify files or databases, network requests can transmit data externally, and emails can be sent. Without human-in-the-loop approval gates, mistakes compound across steps and may be difficult or impossible to remediate.
- **C — Incorrect.** Source selection bias is a valid concern but is not specifically raised by the absence of human checkpoints — it exists regardless of supervision level.
- **D — Incorrect.** Transparency is important but is a communication and disclosure concern, not specifically a consequence of removing human checkpoints from the agent's operation.

---

### Question 15

Under the EU AI Act, an AI system used by a social media platform to automatically remove posts that it classifies as misinformation — without human review before removal — falls into which risk tier, and why?

A) High risk, because it makes consequential automated decisions affecting individuals' freedom of expression, which the Act classifies as a fundamental right

B) Unacceptable risk, because automated content removal is explicitly prohibited under the Act regardless of the accuracy of the underlying classification

C) Limited risk, because transparency obligations (labeling the content as AI-reviewed) are sufficient to protect users

D) Minimal risk, because content moderation is a platform safety measure and is explicitly exempted from the Act's requirements

Correct Answer: A

Distractor Analysis:

- **A — Correct.** The EU AI Act places AI systems that affect fundamental rights — including freedom of expression — in the high-risk category when deployed by platforms with significant reach. High-risk AI systems require human oversight, logging, accuracy testing, and transparency documentation before deployment.
- **B — Incorrect.** The Act's unacceptable risk category is reserved for specific prohibited uses (social scoring by governments, real-time biometric surveillance in public, subliminal manipulation). Automated content moderation is not categorically prohibited.
- **C — Incorrect.** Limited risk applies to systems like chatbots where transparency labeling is the primary obligation. Content removal that affects fundamental rights requires more than labeling.
- **D — Incorrect.** Content moderation by large platforms is not exempt; the Act specifically addresses AI systems used by "providers of general-purpose AI" and platforms subject to the Digital Services Act.

---

### Question 16

Quantum computing is expected to impact machine learning in the long term. Which statement about the current state of quantum ML is most accurate as of 2024?

A) Quantum computers can already train large language models faster than classical GPUs for most NLP tasks

B) Quantum annealing hardware (such as D-Wave) can currently outperform classical computers on all optimization problems encountered in ML training

C) Fault-tolerant quantum computers capable of running Grover's or Shor's algorithm at scale are commercially available and used in production AI pipelines

D) Current NISQ devices have limited qubit counts and high error rates that constrain practical quantum ML to narrow research use cases; fault-tolerant quantum advantage for general ML remains a future research goal

Correct Answer: D

Distractor Analysis:

- **A — Incorrect.** Current NISQ quantum hardware cannot train large language models; classical GPU clusters remain far more capable for this task in 2024.
- **B — Incorrect.** Quantum annealing shows advantages on specific structured optimization problems but does not universally outperform classical computers across all optimization tasks, including the gradient-based optimization used in neural network training.
- **C — Incorrect.** Fault-tolerant quantum computers at the scale required to run Shor's or Grover's algorithms against real-world cryptographic keys or large search spaces do not yet exist in production.
- **D — Correct.** This accurately characterizes the current landscape: NISQ devices exist but are noisy and limited in qubit count; the research community is exploring Variational Quantum Eigensolvers (VQE) and quantum circuit approaches, but fault-tolerant quantum advantage for ML remains a future milestone.

---

### Question 17

A developer is using the ReAct prompting framework to build a research assistant agent. The agent is given a question and must alternate between generating reasoning traces and calling external tools (web search, calculator). What is the primary advantage of interleaving reasoning traces with tool calls compared to using only tool calls?

A) Reasoning traces allow the agent to cache tool results permanently, reducing API calls on future identical queries

B) Reasoning traces enable the model to use more tokens per step, increasing the maximum context window available for tool outputs

C) Reasoning traces help the model plan which tool to call next and interpret tool outputs in context, reducing errors from blindly chaining tool calls without intermediate reflection

D) Reasoning traces encrypt the intermediate steps to prevent prompt injection attacks from tool outputs

Correct Answer: C

Distractor Analysis:

- **A — Incorrect.** Reasoning traces in ReAct are not a caching mechanism; they are in-context thought steps that exist only within the current conversation turn.
- **B — Incorrect.** Reasoning traces consume context window tokens rather than increasing the available window. Longer chains of thought reduce the space available for tool outputs.
- **C — Correct.** The core insight of ReAct is that interleaved reasoning (Reason → Act → Observe → Reason → Act) allows the model to use each observation to inform the next tool selection and refine its interpretation, rather than executing a blind sequence of tool calls. This reduces compounding errors in multi-step tasks.
- **D — Incorrect.** Reasoning traces offer no cryptographic protection against prompt injection from tool outputs. This is a separate defense concern addressed through input sanitization, not chain-of-thought prompting.

---

### Question 18

A startup is building a personalized health coaching application using a fine-tuned GPT model that provides dietary and exercise recommendations based on user biometric data. Under the EU AI Act and GDPR, which combination of obligations is most directly applicable?

A) The AI system is minimal risk (wellness coaching is not medical AI) and data processing requires only a privacy notice

B) The AI system may be classified as high risk (AI in health and wellness affecting individual wellbeing) and must comply with GDPR requirements for processing health biometric data as a special category under Article 9

C) The AI system is unacceptable risk because it processes biometric data, which is categorically prohibited under both the AI Act and GDPR

D) Only GDPR applies; the EU AI Act does not cover AI systems operated by startups with fewer than 250 employees

Correct Answer: B

Distractor Analysis:

- **A — Incorrect.** While wellness AI may be lower risk than medical diagnosis AI, biometric health data processing triggers GDPR Article 9 special category obligations regardless of the AI Act tier. The AI Act may also classify systems affecting individual wellbeing as high risk depending on deployment context.
- **B — Correct.** Health biometric data (BMI, heart rate, dietary logs) is a special category under GDPR Article 9, requiring explicit consent or another Article 9(2) legal basis, data minimization, and a Data Protection Impact Assessment. The EU AI Act may also require human oversight and documentation if the system's recommendations meaningfully affect health outcomes.
- **C — Incorrect.** Processing biometric data is not categorically prohibited by either the AI Act or GDPR — it is subject to heightened requirements, not a ban.
- **D — Incorrect.** The EU AI Act applies based on the AI system being placed on the EU market or affecting EU residents, not based on company size. SME exemptions exist for some conformity assessment processes but not for the fundamental obligations.

---

### Question 19

A developer is preparing to take the Microsoft AI-900 Azure AI Fundamentals exam after completing this course. The exam covers five domains. Which domain has the highest weighting and what does it primarily test?

A) Describe AI workloads and considerations (15–20%) — testing ability to classify AI use cases by type and match them to appropriate Azure services

B) Describe features of computer vision workloads on Azure (15–20%) — testing knowledge of Azure Computer Vision, Custom Vision, and Face API capabilities

C) Describe features of generative AI workloads on Azure (25–30%) — testing knowledge of Azure OpenAI, prompt engineering, and responsible AI for generative systems

D) Describe Responsible AI principles and practices on Microsoft Azure (10–15%) — testing the six Microsoft Responsible AI principles and their application

Correct Answer: A

Distractor Analysis:

- **A — Correct.** According to the published AI-900 exam skills outline, "Describe AI workloads and considerations" carries the highest weighting at 15–20% and includes identifying common AI workload types, matching workloads to Azure services, and applying responsible AI considerations.
- **B — Incorrect.** Computer vision is one of the domain areas but is not the highest-weighted domain; it shares similar weighting with other Azure AI service domains.
- **C — Incorrect.** Generative AI was added to the AI-900 exam outline but does not carry the highest weighting as a standalone domain in the published skills outline.
- **D — Incorrect.** Responsible AI principles are tested throughout the exam but as a standalone domain carry a lower percentage weighting than the AI workloads domain.

---

### Question 20

A company is designing an enterprise agentic AI system using Microsoft Semantic Kernel. The system will autonomously schedule meetings, send emails, access internal databases, and draft contract amendments on behalf of executives. Which principle from responsible AI guidance most directly requires this system to have explicit human approval gates before taking any of these actions?

A) Fairness — the system must treat all executives equally when scheduling on their behalf

B) Inclusiveness — the system must be accessible to executives with disabilities who use assistive technology

C) Privacy and Security — the system must encrypt all emails and database queries to comply with data protection requirements

D) Reliability and Safety — an autonomous agent performing high-stakes irreversible actions (sending emails, amending contracts) must be designed with human-in-the-loop controls to prevent consequential errors from propagating without review

Correct Answer: D

Distractor Analysis:

- **A — Incorrect.** Fairness applies to equitable treatment across groups and is relevant to the system's scheduling prioritization decisions, but it does not specifically require human approval gates for individual actions.
- **B — Incorrect.** Inclusiveness concerns accessibility and equitable access to the AI system, not the need for human oversight of agentic actions.
- **C — Incorrect.** Privacy and Security applies to data handling and protection, not to the governance of when the agent may act autonomously versus requiring human review.
- **D — Correct.** Reliability and Safety requires that AI systems perform consistently and minimize harm — particularly when taking irreversible externalized actions. Sending emails and amending contracts are high-stakes, irreversible, and externally visible: mistakes cannot be undone after the fact. Human-in-the-loop approval gates before these actions directly implement the Reliability and Safety principle.

---

End of Quiz — Module 15

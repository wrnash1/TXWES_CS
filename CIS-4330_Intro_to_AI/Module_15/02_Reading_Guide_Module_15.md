# Reading Guide: Module 15 — Emerging AI Technologies

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Overview

This reading guide accompanies the Module 15 video lecture. The topics covered here represent the frontier of applied AI: multimodal systems, autonomous agents, edge deployment, federated learning, quantum concepts, global regulation, and professional development pathways. Understanding these areas positions you to contribute meaningfully at the current edge of the profession.

**Estimated Reading Time:** 90–120 minutes

---

## Section 1: Multimodal AI Models

### 1.1 From Unimodal to Multimodal

The dominant AI models of the 2010s were largely unimodal: convolutional neural networks for images, recurrent networks and transformers for text, and separate pipelines for audio. While each modality advanced rapidly, real-world intelligence requires integrating signals across modalities simultaneously. Human cognition is inherently multimodal — we read a document while examining the embedded charts, describe what we see, and connect spoken words to their visual referents.

Multimodal AI models formalize this cross-modal integration within a single learned system.

### 1.2 Architectural Foundations

**Modality-specific encoders** transform raw inputs from each modality into vector representations. A vision transformer (ViT) encodes image patches; a text encoder (typically a transformer) encodes token sequences; an audio encoder may use a mel-spectrogram-based convolutional network.

**Cross-attention mechanisms** then enable the model to attend to representations from different modalities simultaneously. When a model answers the question "What is the total in column 3 of this table?" while viewing a spreadsheet screenshot, cross-attention allows the language decoder to attend to the relevant pixel regions.

**Contrastive pretraining** aligns the embedding spaces of different modalities by training the model to place paired inputs (e.g., an image and its caption) close together in the shared space while pushing unpaired inputs apart. CLIP's contrastive pretraining on 400 million image-text pairs from the web is the foundational example.

### 1.3 Landmark Multimodal Systems

**CLIP (OpenAI, 2021):** Contrastive Language-Image Pretraining established that a model trained on image-text pairs could perform zero-shot image classification competitive with supervised baselines on many benchmarks. CLIP embeddings became a widely reused component in subsequent multimodal architectures.

**Flamingo (DeepMind, 2022):** Flamingo demonstrated few-shot multimodal reasoning by interleaving visual and text inputs through a large language model. Given a few example image-question-answer pairs, Flamingo could generalize to new image-question pairs without fine-tuning.

**GPT-4V (OpenAI, 2023):** GPT-4 with vision capability extended the GPT-4 language model to accept image inputs, enabling detailed visual reasoning, OCR, chart reading, and visual question answering at a level substantially exceeding prior systems.

**Gemini (Google DeepMind, 2023):** Designed natively multimodal from the ground up, Gemini was trained jointly on text, images, audio, and video, rather than extending a unimodal language model with a visual adapter.

**Azure AI Vision and Azure OpenAI Vision:** Microsoft's production offerings combine Azure AI Vision (for structured tasks: object detection, OCR, image captioning) with Azure OpenAI Service's GPT-4V endpoint for conversational multimodal reasoning.

### 1.4 Applications and Limitations

Multimodal AI is reshaping several domains:

**Healthcare:** Combining radiology images with clinical notes and lab results for integrated diagnostic support. FDA-cleared multimodal systems are already assisting radiologists in detecting diabetic retinopathy and pulmonary nodules.

**Legal and financial document processing:** Extracting structured data from contracts, invoices, and financial statements that mix text, tables, and signatures.

**Accessibility:** Real-time image description for visually impaired users; speech-to-text combined with visual context for deaf users.

**Education:** Tutoring systems that analyze student-submitted handwritten work, diagrams, and typed explanations together.

Key limitations include: high computational cost for training and inference; potential for cross-modal hallucination (confidently misidentifying elements of an image based on textual context); and limited ability to reason about spatial relationships and physical dynamics compared to human perception.

---

## Section 2: AI Agents and Autonomous Systems

### 2.1 Defining AI Agents

An AI agent is a system that perceives its environment through sensors or inputs, reasons about what to do, and takes actions to pursue goals. This definition encompasses a wide range from simple rule-based bots to sophisticated LLM-powered systems that can write and execute code, browse the web, and coordinate with other agents.

The defining characteristics of modern LLM-powered agents are:

- **Goal-directed behavior:** the agent pursues an objective over multiple steps
- **Tool use:** the agent calls external functions, APIs, or services
- **Memory:** the agent maintains context across steps (in-context, external database, or model fine-tuning)
- **Planning:** the agent decomposes complex goals into subtask sequences

### 2.2 ReAct and Chain-of-Thought Prompting

**ReAct** (Yao et al., 2022) is an influential prompting framework that interleaves reasoning traces and actions. The model alternates between thinking ("I need to find the current population of Texas") and acting (calling a web search tool), then observes the result and continues reasoning. This tight coupling of thinking and doing significantly improves agent performance on multi-step tasks.

**Chain-of-thought (CoT) prompting** enables models to reason step-by-step before producing a final answer. Extended CoT — visible in OpenAI's o1/o3 models and Anthropic's extended thinking — allows models to spend more computation on difficult problems, dramatically improving performance on mathematical and logical reasoning tasks.

### 2.3 Microsoft Agent Frameworks

**AutoGen (Microsoft Research):** An open-source multi-agent framework in which multiple AI agents with different roles — planner, executor, critic, human proxy — communicate through a shared message bus. AutoGen supports human-in-the-loop checkpoints, where a human agent reviews and approves agent actions before execution.

**Semantic Kernel:** An enterprise SDK for integrating LLMs into applications through a plugin system. Plugins describe available functions in a schema the LLM can read, enabling the model to select and invoke appropriate tools. Semantic Kernel supports OpenAI, Azure OpenAI, and Hugging Face models and provides built-in memory management through vector store integrations.

**Azure AI Agent Service (Preview):** A managed cloud service for deploying, monitoring, and scaling AI agents, providing execution sandboxes, tool registries, conversation history storage, and observability dashboards.

### 2.4 Agent Safety and Reliability

Autonomous agents introduce new failure modes that differ from conventional ML model failures:

**Goal misalignment:** The agent achieves a specified goal through unintended means (Goodhart's Law applied to AI: when a measure becomes a target, it ceases to be a good measure).

**Irreversible actions:** An agent that deletes files, sends emails, or makes API calls that cannot be undone can cause significant harm from a single misinterpretation.

**Prompt injection:** A malicious payload embedded in content the agent retrieves (a web page, a document) may hijack the agent's goals.

**Context window overflow:** Long-running agents may lose important early context as the conversation history grows beyond the model's context window.

Responsible agent design patterns include:

- Minimal permission scope (only request the tool access actually needed)
- Explicit human approval for irreversible or high-value actions
- Sandboxed execution environments for code execution
- Comprehensive logging of all tool calls and agent reasoning steps

---

## Section 3: Edge AI and On-Device Inference

### 3.1 Motivation for Edge Deployment

Edge AI moves model inference from centralized cloud infrastructure to the devices where data is generated. The motivations are technical, economic, and regulatory:

**Latency requirements:** Cloud round trips add 50–500 ms of latency. Safety-critical applications — autonomous vehicles, industrial robotics, real-time medical monitoring — require sub-10 ms inference.

**Bandwidth and cost:** Continuously streaming raw sensor data (4K video, vibration waveforms, radar) to the cloud is prohibitively expensive. Running inference at the edge transmits only results.

**Privacy and data sovereignty:** Many regulations restrict transferring certain categories of data (patient health data, financial records, biometric data) across borders or outside controlled environments.

**Offline operation:** Manufacturing floors, ships, aircraft, and rural healthcare settings require systems that operate without reliable internet connectivity.

### 3.2 Model Compression Techniques

Deploying large models on resource-constrained edge devices requires reducing model size and computational requirements without unacceptable accuracy loss.

**Quantization** replaces 32-bit floating-point weights with lower-precision representations. Post-training quantization (PTQ) converts a trained model after training; quantization-aware training (QAT) simulates quantization effects during training, typically yielding better accuracy. INT8 quantization reduces model size approximately 4x; INT4 can achieve 8x reduction with greater accuracy risk.

**Pruning** removes network connections with small weights, creating sparse models. Unstructured pruning removes individual weights; structured pruning removes entire filters or attention heads, which is more hardware-friendly. Models can typically be pruned to 50–90% sparsity with modest accuracy loss when combined with fine-tuning.

**Knowledge distillation** transfers knowledge from a large, accurate "teacher" model to a small, efficient "student" model. The student is trained not just on ground-truth labels but on the teacher's soft probability outputs, which carry richer information about the model's uncertainty and inter-class similarities.

**Neural Architecture Search (NAS)** automates the design of efficient architectures optimized for specific hardware targets. MobileNet, EfficientNet, and SqueezeNet are examples of architectures designed via NAS or manual efficient design for edge deployment.

### 3.3 Hardware and Deployment Infrastructure

**Neural Processing Units (NPUs):** Specialized processors designed specifically for matrix multiplication, the dominant operation in neural network inference. Found in modern smartphones (Apple Neural Engine, Qualcomm Hexagon), laptops (Intel NPU in Core Ultra, Microsoft Copilot+ PC requirement), and industrial edge devices.

**ONNX (Open Neural Network Exchange):** An open format for representing ML models that decouples training frameworks (PyTorch, TensorFlow) from inference runtimes. Models exported to ONNX format can be deployed with ONNX Runtime on Windows, Linux, Android, iOS, and embedded systems without framework-specific dependencies.

**ONNX Runtime:** Microsoft's cross-platform inference engine, optimized through execution providers for specific hardware (CPU, CUDA GPU, DirectML, TensorRT, OpenVINO, ARM NN). It is the inference engine underlying Windows AI, Azure AI, and many third-party applications.

**Azure IoT Edge:** Microsoft's platform for deploying containerized workloads — including AI models wrapped in Docker containers — to edge devices. IoT Edge modules are deployed, updated, and monitored through Azure IoT Hub, enabling cloud-managed edge AI at scale.

### 3.4 Responsible Edge AI

Edge deployment introduces specific responsible AI considerations. Because edge devices have limited monitoring visibility, detecting model drift or bias in edge deployments is harder than in cloud deployments. Edge AI systems should include telemetry for prediction confidence distributions, hardware health monitoring, and scheduled model update mechanisms. Physical security of edge devices carrying model weights must also be considered, as model theft from a device is possible if weights are not encrypted at rest.

---

## Section 4: Federated Learning

### 4.1 The Privacy-Centralization Tension

Machine learning's standard assumption — that all training data is accessible to a central training server — creates fundamental tensions with privacy, data sovereignty, and competitive confidentiality. Federated learning (McMahan et al., Google, 2017) resolves this tension by bringing computation to the data rather than data to the computation.

### 4.2 Federated Averaging (FedAvg)

The core federated learning algorithm, **FedAvg**, operates in rounds:

1. Server selects a random subset of clients (devices or organizations)
2. Server broadcasts the current global model weights to selected clients
3. Each client trains locally for E epochs on its local dataset, producing updated weights
4. Each client sends its weight update (delta from the initial weights) to the server
5. Server computes a weighted average of client updates, weighted by dataset size
6. Updated global model is broadcast for the next round

FedAvg converges to good solutions even when client data distributions are highly heterogeneous (non-IID), though convergence is slower than centralized training.

### 4.3 Privacy in Federated Learning

Federated learning reduces data exposure but does not eliminate privacy risk. Gradient updates can leak information about training data through gradient inversion attacks (Zhu et al., 2019), which reconstruct training samples from gradient information.

Combining federated learning with **secure aggregation** prevents the server from seeing individual client updates — the server only sees the aggregate. Combining with **differential privacy** (adding noise to local updates before transmission) provides formal privacy guarantees against gradient inversion.

**Local differential privacy** adds noise at each client before transmission, providing privacy even against a malicious server. **Central differential privacy** adds noise at the server after aggregation, providing weaker per-client guarantees but better utility.

### 4.4 Production Deployments

**Google Gboard:** The first large-scale production deployment of federated learning. Next-word prediction models for the Android keyboard are trained on hundreds of millions of devices without keystroke data ever leaving the device.

**Apple:** Uses federated learning for features including QuickType keyboard suggestions, emoji recommendations, and "Hey Siri" voice model personalization.

**Healthcare cross-silo FL:** Projects like the federated tumor segmentation (FeTS) initiative trained brain tumor segmentation models across 71 international sites without sharing patient scans.

**Azure Federated Learning (Preview):** Microsoft's managed federated learning platform enables cross-silo FL across Azure subscriptions, Azure Arc-connected on-premises servers, and partner organizations.

---

## Section 5: Quantum Machine Learning Concepts

### 5.1 Quantum Computing Fundamentals

Quantum computers exploit two quantum mechanical phenomena:

**Superposition:** A qubit can exist in a linear combination of |0⟩ and |1⟩ states simultaneously. An n-qubit register can represent 2^n basis states simultaneously, providing an exponentially large state space.

**Entanglement:** Two or more qubits can be correlated such that measuring one instantly determines the state of the other, regardless of physical separation. Entanglement enables quantum algorithms to encode complex correlations efficiently.

**Interference:** Quantum algorithms manipulate probability amplitudes so that correct answers constructively interfere (become more probable) and incorrect answers destructively interfere (become less probable).

### 5.2 Quantum Advantage for ML

Classical ML relies heavily on linear algebra: matrix-vector multiplication, eigendecomposition, and least-squares solving. Quantum algorithms — particularly the HHL algorithm for linear systems and quantum SVD — provide theoretical exponential speedups for these operations.

**Quantum kernel methods** use quantum computers to compute kernel functions in exponentially high-dimensional feature spaces that would be intractable classically. A quantum support vector machine could theoretically learn boundaries in feature spaces no classical SVM could access.

**Variational Quantum Eigensolvers (VQE) and Quantum Neural Networks** use parameterized quantum circuits as trainable models, optimized through classical gradient descent. These hybrid classical-quantum algorithms are the most experimentally accessible form of quantum ML on current hardware.

### 5.3 Current Status and Azure Quantum

Current quantum hardware — **NISQ (Noisy Intermediate-Scale Quantum)** devices — have 50–1,000+ physical qubits but significant error rates that limit circuit depth. Practical quantum advantage for machine learning likely requires **fault-tolerant quantum computing** with error-corrected logical qubits, which requires millions of physical qubits per logical qubit with current error correction overhead.

**Azure Quantum** provides cloud access to multiple quantum hardware providers (IonQ, Quantinuum, Rigetti) and the Microsoft-developed topological qubit platform, plus a quantum-inspired optimization service for near-term combinatorial optimization problems. For AI-900 purposes, understand that quantum ML is a promising research direction, not a current production technology.

---

## Section 6: AI Regulation Landscape

### 6.1 EU AI Act (2024)

The EU AI Act (Regulation EU 2024/1689), adopted June 2024, is the world's first comprehensive horizontal AI regulation. It applies to AI systems placed on the EU market or used in the EU, regardless of where the developer is located.

**Risk tiers:**

- **Unacceptable risk (banned):** Social scoring by public authorities; real-time remote biometric identification in public spaces (with narrow exceptions); subliminal manipulation; exploitation of vulnerabilities
- **High risk:** Biometric categorization; critical infrastructure management; educational and vocational assessment; employment and worker management; access to essential services (credit, insurance); law enforcement; migration and border control; administration of justice
- **Limited risk:** Chatbots and synthetic content generators (transparency obligation: disclose AI use)
- **Minimal risk:** Spam filters, AI in video games (no specific obligations)

High-risk AI systems require technical documentation, conformity assessments, registration in an EU database, human oversight mechanisms, accuracy and robustness requirements, and cybersecurity measures.

### 6.2 US AI Governance

The United States has taken a more fragmented, sector-specific approach to AI governance compared to the EU's horizontal regulation.

**NIST AI Risk Management Framework (AI RMF 1.0, 2023):** Voluntary framework organizing AI risk management around four functions: Govern, Map, Measure, and Manage. Widely adopted by federal agencies and large enterprises as a responsible AI governance reference.

**Executive Order on Safe, Secure, and Trustworthy AI (October 2023):** Directed NIST to develop AI safety standards; required developers of powerful foundation models to share safety test results with the government; established AI safety institutes at NIST and DHS.

**Sector-specific regulations:** The FDA regulates AI/ML-based Software as a Medical Device (SaMD); financial regulators (OCC, FDIC, Federal Reserve) have issued guidance on model risk management for AI in banking; FTC has issued guidance on AI in advertising and consumer protection.

### 6.3 Microsoft Responsible AI Standard

Microsoft's public **Responsible AI Standard** (v2, 2022) is a detailed engineering governance document requiring AI product teams to:

- Conduct impact assessments identifying potential harms before deployment
- Evaluate model performance across demographic groups
- Implement transparency measures including model documentation
- Establish accountability mechanisms including named responsible individuals
- Apply security and privacy reviews using the practices covered in Module 14

The standard directly maps to the Microsoft Responsible AI Principles: fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

---

## Section 7: Certification and Career Pathways

### 7.1 Azure AI Certification Ladder

Microsoft's Azure AI certification path progresses from foundational to expert levels:

**AI-900 (Fundamentals):** Concepts, workload identification, Azure AI services overview. No prerequisites; recommended starting point for non-technical and technical learners alike.

**AI-102 (Associate):** Design and implement Azure AI solutions using Cognitive Services, Azure OpenAI, and Azure Machine Learning. Requires hands-on development experience.

**DP-100 (Associate):** Data science solution design on Azure ML, including experiment tracking, pipeline authoring, and model deployment. Targets data scientists and ML engineers.

**Expert-level:** Azure certifications at the expert level (Solutions Architect Expert, DevOps Engineer Expert) incorporate AI components but are not AI-specific.

### 7.2 Complementary Certifications

**SC-900 (Security, Compliance, and Identity Fundamentals):** Complements AI security knowledge; covers Azure security center, compliance manager, and identity governance.

**PL-300 (Power BI Data Analyst Associate):** Relevant for data visualization and reporting in AI-driven analytics workflows.

**Google Professional ML Engineer:** Vendor-agnostic ML skills; valuable for practitioners working in multi-cloud environments.

**AWS Certified ML Specialty:** Amazon's equivalent to AI-102 for AWS-based ML deployments.

**IAPP CIPT (Certified Information Privacy Technologist):** Privacy engineering certification directly relevant to the differential privacy and GDPR content from Module 14.

### 7.3 Career Roles in AI

**ML Engineer:** Builds, trains, and deploys production ML pipelines. Focuses on infrastructure, MLOps, and serving reliability. Median US salary: $150,000–$180,000.

**Data Scientist:** Develops models, conducts exploratory analysis, and communicates findings to business stakeholders. Median US salary: $120,000–$145,000.

**AI Solutions Architect:** Designs enterprise AI system architecture, selecting services, defining integration patterns, and ensuring scalability and security. Median US salary: $160,000–$200,000.

**AI Product Manager:** Translates business needs into AI product requirements; manages development lifecycle and stakeholder communication. Median US salary: $140,000–$170,000.

**AI Ethics and Governance Specialist:** Conducts bias audits, develops governance frameworks, ensures regulatory compliance, and communicates AI risk to leadership. Growing role driven by regulatory requirements.

**Prompt Engineer / LLM Application Developer:** Designs prompts and agentic workflows for LLM-powered applications. Entry-level to mid-level; rapidly evolving role as models become more capable.

---

## Key Terms Glossary

**AutoGen:** Microsoft Research's multi-agent orchestration framework for collaborative AI agent applications.

**CLIP:** Contrastive Language-Image Pretraining; OpenAI model that aligns image and text embeddings through contrastive training.

**Cross-silo federated learning:** FL across a small number of large-data organizations (e.g., hospitals, banks).

**Edge AI:** Running AI model inference on the device where data is generated rather than in the cloud.

**EU AI Act:** World's first comprehensive horizontal AI regulation; risk-tiered framework effective 2024.

**FedAvg:** Federated Averaging; the core federated learning algorithm that aggregates client model updates by weighted averaging.

**Federated learning:** Distributed ML training paradigm where data never leaves client devices; only model updates are shared.

**Knowledge distillation:** Training a small student model to mimic a large teacher model's outputs.

**Multimodal AI:** AI models that process and reason across multiple data modalities (text, image, audio, video) in a shared system.

**NISQ:** Noisy Intermediate-Scale Quantum; current generation of quantum computers with limited qubit counts and high error rates.

**ONNX Runtime:** Microsoft's cross-platform, open-source inference engine for deploying ML models on diverse hardware.

**Pruning:** Removing low-importance weights from a neural network to reduce model size and inference cost.

**Quantization:** Reducing the numerical precision of model weights (e.g., from FP32 to INT8) to decrease model size and speed up inference.

**Quantum ML:** Research area exploring quantum computing acceleration of ML training and inference.

**ReAct:** Prompting framework that interleaves model reasoning traces and tool-calling actions for multi-step agent tasks.

**Semantic Kernel:** Microsoft SDK for integrating LLMs with external tools and data through a plugin architecture.

---

## Review Questions

1. What architectural mechanism allows a multimodal model to reason across image and text inputs simultaneously?

2. Describe the perceive-think-act loop and explain how ReAct instantiates it in practice.

3. What are the three primary model compression techniques used for edge AI deployment?

4. How does federated averaging work, and what privacy risks remain even after adopting it?

5. What distinguishes NISQ quantum computers from fault-tolerant quantum computers, and why does this distinction matter for quantum ML timelines?

6. Under the EU AI Act, which risk tier applies to an AI system used by a bank to automatically approve or deny loan applications?

7. What does the Microsoft Responsible AI Standard require of product teams before deployment?

8. What is the recommended next certification after AI-900 for a practitioner building production Azure AI applications?

---

## Further Reading

- Radford, A., et al. (2021). *Learning Transferable Visual Models From Natural Language Supervision (CLIP).* arXiv:2103.00020
- McMahan, H. B., et al. (2017). *Communication-Efficient Learning of Deep Networks from Decentralized Data (FedAvg).* AISTATS.
- Yao, S., et al. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models.* arXiv:2210.03629
- European Parliament. (2024). *EU Artificial Intelligence Act.* Official Journal of the EU.
- NIST. (2023). *AI Risk Management Framework (AI RMF 1.0).* nist.gov/system/files/documents/2023/01/26/NIST.AI.100-1.pdf
- Microsoft. (2022). *Responsible AI Standard v2.* microsoft.com/en-us/ai/responsible-ai
- Azure Documentation: *ONNX Runtime overview.* learn.microsoft.com/azure/machine-learning/concept-onnx

---

*Reading Guide Line Count: 265 | Module 15 — Emerging AI Technologies*

# Video Script: Module 15 — Emerging AI Technologies

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Segment 1: Introduction (Lines 1–22)

[SLIDE: Module 15 Title Card — Emerging AI Technologies]

Welcome back to CIS-4330. I'm Professor Nash, and in this final content module before our exam preparation unit, we are going to look forward — at where AI is heading, what technologies are reshaping the field right now, and what you need to know as a practitioner entering this profession.

This module is deliberately forward-looking. The AI-900 exam tests foundational knowledge, but the professionals who succeed in this field are the ones who understand not just where AI is today but where it is going in the next five to ten years.

[SLIDE: Module Roadmap]

Here is what we will cover in this module:

- Multimodal AI models
- AI agents and autonomous systems
- Edge AI and on-device inference
- Federated learning
- Quantum machine learning concepts
- The AI regulation landscape
- Certification and career pathways

Let's begin.

---

## Segment 2: Multimodal AI Models (Lines 23–55)

[SLIDE: What Is a Multimodal Model?]

For most of AI's history, models were trained to work with a single modality — images, text, or audio — but not multiple types simultaneously. A text classifier only understood text. An image recognizer only understood pixels. These models were powerful within their lanes but blind outside them.

Multimodal AI changes this fundamentally. A multimodal model can process, reason across, and generate multiple data types in a single integrated system.

[SLIDE: How Multimodal Models Work]

The architectural key to multimodal models is the **shared embedding space**. Text, images, audio, and video are each encoded by modality-specific encoders into a common high-dimensional vector space. Once in that shared space, the model can reason about relationships across modalities.

OpenAI's **CLIP** (Contrastive Language-Image Pretraining) was an early landmark: trained on 400 million image-text pairs, CLIP learned to associate images with their natural language descriptions so well that it could classify images into categories it had never seen during training — so-called zero-shot classification.

[SLIDE: GPT-4V and Azure OpenAI Vision]

More recent systems integrate vision and language even more tightly. **GPT-4V** — the vision-enabled version of GPT-4 — can analyze photographs, diagrams, charts, and handwritten notes alongside text, enabling applications like medical image explanation, document understanding, and visual reasoning.

Through Azure OpenAI Service, organizations can access GPT-4V via API, building applications that accept both image and text inputs in the same conversation turn.

[SLIDE: Multimodal Applications]

Multimodal AI is enabling a new generation of applications:

- **Radiology assistants** that correlate CT scan findings with clinical notes and lab results
- **Document intelligence** systems that extract structured data from PDFs containing mixed text, tables, and images
- **Video understanding** models that can answer natural language questions about video content
- **Accessibility tools** that describe images for visually impaired users in real time

[SLIDE: Microsoft Copilot as a Multimodal System]

Microsoft Copilot is a practical example of a production multimodal system. Users can paste images into Copilot conversations, and the system will reason about the image content in combination with textual context. This integration is powered by Azure OpenAI Service's multimodal models and is available across Microsoft 365 Copilot, Bing, and Azure AI Studio.

---

## Segment 3: AI Agents and Autonomous Systems (Lines 56–90)

[SLIDE: From Models to Agents]

A traditional AI model takes an input and produces an output. An **AI agent** does something more: it perceives its environment, takes actions, and pursues goals — potentially over many steps, across multiple tool calls, and without continuous human direction.

[SLIDE: The Agent Loop]

AI agents operate through what researchers call a **perceive-think-act** loop.

The agent **perceives**: it receives observations about the current state of its environment — which could be a conversation, a file system, a web browser, a database, or a physical sensor.

The agent **thinks**: it reasons about what action to take next, often using a large language model as the reasoning engine.

The agent **acts**: it executes a tool call, sends a message, writes code, queries a database, or calls an API.

Then the cycle repeats, incorporating the result of the action into the next perception.

[SLIDE: AutoGen and Semantic Kernel]

Microsoft has developed two major frameworks for building AI agents.

**AutoGen** is a multi-agent orchestration framework that enables multiple AI agents to collaborate — a "planner" agent breaks down a task, "executor" agents carry out subtasks, and a "critic" agent reviews results. AutoGen applications can coordinate agents playing different roles, with humans able to enter the loop at any point.

**Semantic Kernel** is an SDK that gives AI models access to tools — plugins that connect to Microsoft 365, databases, REST APIs, and custom functions. It provides memory management, planning, and a standardized way to describe tools to the model in a way it can reason about.

[SLIDE: Autonomous vs. Human-in-the-Loop Agents]

The question of how autonomous AI agents should be is one of the most active debates in the field. Fully autonomous agents that can execute consequential actions without human approval create risks: they may misinterpret intent, get stuck in loops, or take irreversible actions based on incorrect reasoning.

The responsible design pattern is **human-in-the-loop**: agents handle routine, low-stakes subtasks autonomously but pause and request human confirmation before high-stakes, irreversible, or ambiguous actions.

[SLIDE: Real-World Agent Applications]

Production AI agents are already operating in several domains: customer service agents that can look up account data, process refunds, and escalate edge cases; coding agents that can read a GitHub issue, write a fix, run tests, and submit a pull request; and research agents that browse the web, synthesize sources, and produce structured reports.

---

## Segment 4: Edge AI and On-Device Inference (Lines 91–120)

[SLIDE: The Cloud AI Model Has Limits]

The dominant pattern for AI deployment over the past decade has been cloud-hosted: a device sends data to a cloud server, the server runs the model, and the result is sent back. This works well when connectivity is reliable and latency is acceptable.

But many important use cases cannot tolerate cloud round-trip latency, cannot depend on connectivity, or cannot transmit raw data for privacy or bandwidth reasons.

[SLIDE: What Is Edge AI?]

**Edge AI** runs AI model inference directly on the device where data is generated — a smartphone, a surveillance camera, a factory sensor, a medical monitor, or an autonomous vehicle.

This approach offers three key advantages.

**Latency**: inference happens in milliseconds without a network round trip. For safety-critical applications like collision avoidance or real-time medical monitoring, this matters enormously.

**Privacy**: raw data — video, audio, biometric signals — never leaves the device. Only inference results are transmitted if needed.

**Resilience**: the device continues to function when offline.

[SLIDE: Model Compression for Edge Deployment]

Running large AI models on resource-constrained devices requires model compression. Three main techniques are used.

**Quantization** reduces the numerical precision of model weights from 32-bit floating point to 8-bit or even 4-bit integers. This typically reduces model size by 4x with minimal accuracy loss.

**Pruning** removes network weights that contribute least to model output, producing a sparse model with fewer active parameters.

**Knowledge distillation** trains a small "student" model to mimic the outputs of a large "teacher" model, transferring knowledge into a more efficient architecture.

[SLIDE: Azure and Edge AI]

Microsoft's **Azure IoT Edge** platform enables deploying containerized AI models to edge devices, managing them remotely through Azure IoT Hub. **ONNX Runtime** — the open neural network exchange runtime — is Microsoft's cross-platform inference engine optimized for edge hardware, including ARM processors, Intel Neural Compute Sticks, and NVIDIA Jetson devices.

[SLIDE: On-Device Models in Consumer Devices]

The shift to on-device AI is already visible in consumer technology. Apple's Neural Engine runs face recognition and Siri locally. Android devices run voice recognition and keyboard prediction on-device. Modern laptops with Neural Processing Units (NPUs) — including Microsoft Copilot+ PCs — run Recall and real-time translation locally.

---

## Segment 5: Federated Learning (Lines 121–148)

[SLIDE: The Central Data Problem]

Traditional machine learning requires centralizing training data. But centralization conflicts with privacy, bandwidth constraints, data sovereignty regulations, and competitive confidentiality. Federated learning is a distributed training paradigm designed to address these tensions.

[SLIDE: How Federated Learning Works]

In **federated learning**, training data never leaves the devices or organizations that own it. Instead:

1. A central server distributes the current global model to participating clients
2. Each client trains the model locally on its own data for a fixed number of steps
3. Each client sends its model update — gradients or weight deltas — back to the server
4. The server aggregates updates, typically by averaging (FedAvg), to produce the next global model
5. The cycle repeats

[SLIDE: Cross-Device vs. Cross-Silo Federated Learning]

Federated learning operates in two distinct settings.

**Cross-device** federated learning involves millions of mobile or IoT devices, each holding small amounts of data. Google uses this to train Gboard keyboard predictions on Android devices without accessing user keystrokes.

**Cross-silo** federated learning involves a small number of organizations — hospitals, banks, or research institutions — each holding large, confidential datasets. Multiple hospitals can collaboratively train a cancer detection model without sharing patient records.

[SLIDE: Challenges]

Federated learning introduces several challenges that active research is working to address.

**Statistical heterogeneity**: client datasets may have very different distributions (non-IID data), slowing convergence.

**Communication efficiency**: transmitting model updates for large models is expensive; gradient compression and quantization help.

**Privacy**: the server sees gradient updates, which can leak information. Combining federated learning with differential privacy or secure aggregation protocols strengthens privacy guarantees.

---

## Segment 6: Quantum Machine Learning Concepts (Lines 149–168)

[SLIDE: Quantum Computing Basics]

Quantum computing uses quantum mechanical phenomena — superposition and entanglement — to perform certain computations exponentially faster than classical computers.

A classical bit is either 0 or 1. A quantum bit, or **qubit**, can exist in a superposition of 0 and 1 simultaneously. A system of n qubits can represent 2^n states simultaneously, enabling certain algorithms to explore vast solution spaces in parallel.

[SLIDE: Where Quantum Intersects ML]

**Quantum machine learning** (QML) explores whether quantum computers can accelerate ML training or enable fundamentally new model architectures.

Promising areas include quantum linear algebra — operations like matrix inversion and singular value decomposition that classical ML relies on heavily — and quantum kernels for support vector machines.

[SLIDE: Realistic Timelines]

It is important to be clear about where quantum ML stands today. Current quantum computers are **NISQ devices** — Noisy Intermediate-Scale Quantum — with dozens to hundreds of qubits and significant error rates. General-purpose quantum advantage over classical ML for practical problems likely requires fault-tolerant quantum computers with millions of logical qubits, which are likely a decade or more away.

For the AI-900 exam, you need to be aware that quantum ML is an emerging research area, not a current production technology. Azure Quantum provides quantum computing services for researchers, but quantum advantage for ML workloads remains a future horizon.

---

## Segment 7: AI Regulation Landscape and Certification Pathways (Lines 169–220)

[SLIDE: The Global AI Regulatory Landscape]

The AI regulatory environment is shifting rapidly. In 2024, two landmark frameworks took effect.

The **EU AI Act** is the world's first comprehensive AI regulation. It takes a risk-tiered approach: AI systems are classified as unacceptable risk (banned), high risk (heavily regulated), limited risk (transparency obligations), and minimal risk (no specific obligations). High-risk categories include biometric identification, critical infrastructure, employment decisions, credit scoring, and law enforcement.

In the United States, the **White House Executive Order on Safe, Secure, and Trustworthy AI** (October 2023) directs federal agencies to develop AI safety standards, and the NIST AI Risk Management Framework provides voluntary guidance for organizations developing or deploying AI.

[SLIDE: What Regulation Means for Practitioners]

For AI practitioners, this regulatory landscape has practical implications. High-risk AI systems in the EU require conformity assessments, technical documentation, human oversight mechanisms, and registration in a public database. Practitioners building these systems need to understand how to operationalize these requirements — through model cards, bias audits, explainability tools, and governance processes.

[SLIDE: Microsoft Responsible AI Standard]

Microsoft's internal **Responsible AI Standard** translates these regulatory concepts into engineering requirements. It mandates fairness assessments, transparency documentation, privacy reviews, and security evaluations for AI products shipped by Microsoft. The standard is publicly available and is a useful reference for organizations building their own responsible AI governance programs.

[SLIDE: AI-900 Certification]

The **Microsoft Azure AI Fundamentals (AI-900)** exam validates foundational knowledge of AI concepts and Azure AI services. It is the appropriate starting certification for anyone entering the AI field from a technology background.

The exam covers five domains: AI workloads and considerations, fundamental machine learning principles on Azure, computer vision workloads, natural language processing workloads, and generative AI workloads on Azure. We will review all five domains in detail in Module 16.

[SLIDE: Certification Pathways Beyond AI-900]

AI-900 is the entry point to a rich Azure AI certification path.

**AI-102** (Designing and Implementing Azure AI Solutions) is the associate-level certification for practitioners building production AI applications with Azure Cognitive Services and Azure OpenAI.

**DP-100** (Designing and Implementing a Data Science Solution on Azure) targets data scientists working with Azure Machine Learning.

**SC-900** (Security, Compliance, and Identity Fundamentals) complements AI security knowledge from this module with Azure security fundamentals.

Beyond Azure, the broader industry offers the **Google Professional Machine Learning Engineer**, **AWS Certified Machine Learning Specialty**, and vendor-neutral certifications from organizations like IAPP for AI privacy professionals.

[SLIDE: Career Pathways in AI]

Graduates with AI-900 and further certifications are well positioned for roles including:

- AI Solutions Architect: designing enterprise AI systems
- ML Engineer: building and deploying production ML pipelines
- Data Scientist: developing and evaluating predictive models
- AI Product Manager: leading AI product development
- AI Ethics and Governance Specialist: ensuring responsible AI deployment
- Prompt Engineer / AI Application Developer: building LLM-powered applications

[SLIDE: Module 15 Key Takeaways]

Let's close with our key takeaways.

Multimodal models process multiple data types in a shared embedding space, enabling richer reasoning and new application categories.

AI agents combine LLM reasoning with tool-calling in perceive-think-act loops; responsible design requires human-in-the-loop control for high-stakes actions.

Edge AI runs inference on-device for low latency, privacy, and resilience; model compression techniques enable deployment on constrained hardware.

Federated learning trains models across distributed data sources without centralizing sensitive data, using FedAvg aggregation.

Quantum ML is a promising but pre-production research area; current NISQ devices do not yet provide practical quantum advantage for ML workloads.

The EU AI Act and US AI governance frameworks are creating concrete compliance obligations for AI practitioners.

AI-900 is your entry point to a career-long certification and professional development pathway.

In Module 16, we will review all AI-900 exam domains, discuss exam strategy, and work through 20 practice questions together.

See you there.

---

*Script Line Count: 220 | Estimated Runtime: 26–30 minutes*

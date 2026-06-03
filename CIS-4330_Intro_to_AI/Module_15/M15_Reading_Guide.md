# Reading Guide: Module 15 — Emerging AI Technologies

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Overview

Module 15 surveys the frontier of AI technology: multimodal models, AI agents, edge deployment, federated learning, and quantum ML. These readings give you depth beyond the lecture slides and prepare you for the careers that will emerge from these technologies. Budget approximately 90 minutes for readings and responses.

---

## Required Readings

### Reading 1 — Microsoft Research: Multimodal Foundation Models

**URL:** `https://www.microsoft.com/en-us/research/blog/` (search "multimodal foundation models")

**Alternatively:** `https://arxiv.org/abs/2309.10020` (Multimodal Foundation Models survey paper — read abstract and Section 1 only)

**Focus Areas:**

- How multiple modalities are unified in a single model
- Applications enabled by multimodal reasoning
- Limitations of current multimodal systems

**Annotation Prompts:**

1. How do projection layers enable joint reasoning across modalities?
2. What evaluation challenges are specific to multimodal models?
3. Name one application that becomes possible with multimodal AI that was impossible with single-modality AI.

---

### Reading 2 — Microsoft: AI Agents Overview

**URL:** `https://learn.microsoft.com/en-us/azure/ai-services/agents/overview`

**Focus Areas:**

- What capabilities Azure AI Agent Service provides
- How agents use tools and maintain context
- Supported tool types

**Annotation Prompts:**

1. What does Azure AI Agent Service manage that developers would otherwise have to build themselves?
2. What tool categories does Azure AI Agent Service natively support?
3. What is the role of the thread/conversation history in an agent interaction?

---

### Reading 3 — Google AI Blog: Federated Learning

**URL:** `https://blog.research.google/2017/04/federated-learning-collaborative.html`

**Focus Areas:**

- Original motivation for federated learning
- The FedAvg algorithm concept
- Real-world deployment in Gboard

**Annotation Prompts:**

1. What privacy problem motivated Google's development of federated learning?
2. How does FedAvg aggregate updates from multiple devices?
3. What types of ML tasks is federated learning most easily applied to?

---

### Reading 4 — AI Career Paths (LinkedIn Learning or Industry Source)

**URL:** `https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm`

**Alternatively:** Search for "AI career paths 2026" on LinkedIn, Indeed, or a professional technology publication.

**Focus Areas:**

- Job titles, responsibilities, and compensation in AI
- Required skills and credentials
- Growth projections

**Annotation Prompts:**

1. What does the Bureau of Labor Statistics project for job growth in computer and information research (AI-adjacent) roles?
2. Which AI job title appears most in demand in current job postings in your region?
3. What non-AI skills (domain knowledge, communication, business acumen) are cited as differentiators in AI roles?

---

## Key Concept Summaries

### Multimodal AI Architecture

Multimodal AI systems can process and reason across multiple types of input: text, images, audio, video, code, and structured data. They differ from earlier AI systems in that they share representations across modalities rather than processing each modality in isolation.

**Core components:**

**Vision Encoder:** Typically a Vision Transformer (ViT) that converts an image into a sequence of patch embeddings. Each patch of the image is treated like a token in a language model.

**Language Model Backbone:** The large language model (LLM) that processes text tokens and serves as the reasoning engine.

**Cross-modal Projection:** A learned mapping that converts image embeddings into the language model's token space. This is the bridge that allows the language model to "read" images as if they were text.

**Output generation:** The language model generates text (or other modality) conditioned on the combined visual and textual context.

**Azure multimodal capabilities:**

| Capability | Service | Use Case |
|---|---|---|
| Image + text understanding | Azure OpenAI (GPT-4V) | Document analysis, visual QA |
| Text → image generation | Azure OpenAI (DALL-E 3) | Marketing, design, visualization |
| Audio → text | Azure OpenAI (Whisper) | Transcription, meeting notes |
| Document intelligence | Azure AI Document Intelligence | Invoice, form, contract extraction |
| Image captioning + OCR | Azure AI Vision | Accessibility, content indexing |

---

### AI Agents Architecture

AI agents extend language models with planning, memory, and tool-use capabilities.

**Core agent components:**

**Planning module:** The LLM reasons about the goal and generates a plan of action. This may be explicit (write a list of steps) or emergent (implicit planning within the ReAct loop).

**Memory:**

- **In-context memory:** The conversation history within the current context window
- **External memory:** A vector database storing past interactions and retrieved documents
- **Procedural memory:** Tool definitions and schemas that define what the agent can do

**Tool use:** The agent calls external functions and APIs. Common tools include:

- Web search
- Code execution (Python interpreter)
- Database queries
- Email and calendar APIs
- Document reading and writing
- Custom business APIs

**Observation and reflection:** After each tool call, the agent observes the result and updates its internal state, deciding what to do next.

**Multi-agent coordination:**

In multi-agent systems (Microsoft AutoGen, CrewAI), specialized agents hand off work to each other. An orchestrator agent assigns tasks; specialist agents execute; a critic agent reviews. Communication between agents uses structured messages with defined schemas.

---

### Edge AI

**Definition:** Running AI inference on devices at the network edge, close to the data source, rather than sending data to a central cloud.

**Why it matters:**

| Requirement | Cloud AI | Edge AI |
|---|---|---|
| Latency | 100–500ms | <5ms |
| Connectivity required | Yes | No |
| Data privacy | Data leaves device | Data stays local |
| Bandwidth consumption | High | Low |
| Infrastructure cost | Variable (metered) | Fixed (hardware) |

**Model compression techniques** (required for edge deployment):

**Quantization:** Reduce numerical precision from 32-bit floating point to 8-bit integer (INT8) or even 4-bit. Reduces model size by 4–8x with modest accuracy loss.

**Pruning:** Remove weights that are close to zero (have little effect on outputs). Sparse models can be significantly smaller and faster.

**Knowledge distillation:** Train a small "student" model to mimic the outputs of a large "teacher" model. The student learns a compressed representation of the teacher's knowledge.

**Neural architecture search (NAS):** Automatically search for efficient architectures designed specifically for constrained edge environments.

**ONNX (Open Neural Network Exchange):** A cross-platform model format that enables models trained in PyTorch, TensorFlow, or other frameworks to run on any edge device using ONNX Runtime. Essential for Azure edge deployment.

---

### Federated Learning

**Problem statement:** Many of the most valuable ML training datasets exist in siloed environments — hospitals cannot share patient records; banks cannot share transaction details; phones cannot send personal text messages to a central server. Federated learning enables training on these datasets without centralizing them.

**FedAvg algorithm:**

1. Server sends global model weights W₀ to all participating clients
2. Each client k trains locally for t steps: Wₖ = W₀ - η * ∇L_k (local gradient)
3. Each client sends Δₖ = Wₖ - W₀ (weight update) to server
4. Server aggregates: W_new = W₀ + Σ(nₖ/N * Δₖ) where nₖ is client k's data size
5. Repeat from step 1

**Privacy enhancement with DP:** Add Gaussian noise to client updates before transmission. This prevents the server or other parties from inferring individual training samples from the gradient updates.

**FL in Azure:** Azure Machine Learning supports federated learning through the Azure Federated Learning package. Cross-silo FL (between institutions) and cross-device FL (across user devices) are both supported.

---

### Quantum Machine Learning — Conceptual Overview

**Quantum computing basics:**

- **Qubit:** Quantum bit that can be in superposition of 0 and 1 simultaneously
- **Entanglement:** Two qubits can be correlated such that measuring one instantly determines the other
- **Quantum gates:** Operations on qubits — analogous to logic gates in classical computing
- **Interference:** Amplify correct answers and cancel wrong answers

**Potential ML applications:**

- **Quantum sampling:** Sample from complex probability distributions more efficiently than classical methods
- **Quantum optimization:** Solve combinatorial optimization problems (relevant for hyperparameter search, neural architecture search)
- **Quantum linear algebra:** Certain linear algebra operations (relevant for kernel methods) may be exponentially faster on quantum hardware

**Practical status in 2026:**

- Current "NISQ" (Noisy Intermediate-Scale Quantum) hardware has 50–1000 physical qubits
- Error rates remain high; fault-tolerant quantum computing requires logical qubits from many physical qubits
- No practical quantum advantage over classical ML demonstrated on real problems
- Active research areas: variational quantum eigensolvers, quantum neural networks, quantum kernel methods

**Azure Quantum:** Microsoft's quantum computing cloud service provides access to partner hardware (IonQ, Quantinuum) and Azure Quantum Elements for materials science simulation.

---

### Certification Pathway

**Entry Level:**

- AI-900 Azure AI Fundamentals — No prerequisites; validates foundational AI/ML understanding
- SC-900 Microsoft Security, Compliance, and Identity Fundamentals — Complementary to AI-900 for security track

**Associate Level:**

- AI-102 Azure AI Engineer Associate — Design/implement Azure AI solutions; requires coding
- DP-100 Azure Data Scientist Associate — ML model development and deployment on Azure
- DP-203 Azure Data Engineer Associate — Data pipeline engineering; prerequisites for ML at scale

**Professional / Expert Level:**

- AZ-305 Azure Solutions Architect Expert — Cloud architecture including AI/ML workloads
- DP-420 Azure Cosmos DB Developer Specialty — Vector database skills for AI retrieval-augmented generation

**Vendor-Neutral:**

- CDSS (Certified Data Science Specialist)
- CAIP (Certified Artificial Intelligence Practitioner)

**Time estimates:**

- AI-900: 2–4 weeks of study for students with this course background
- AI-102: 3–6 months of study; prior Azure experience recommended
- DP-100: 3–6 months; Python and ML fundamentals required

---

## Vocabulary Builder

Define each term in your own words:

1. Multimodal AI
2. Vision transformer (ViT)
3. Cross-modal projection
4. AI agent
5. ReAct pattern
6. Tool use (agents)
7. Multi-agent system
8. Edge AI
9. Quantization (model compression)
10. Knowledge distillation
11. ONNX
12. Federated learning
13. FedAvg
14. Quantum superposition
15. NISQ (Noisy Intermediate-Scale Quantum)

---

## Reflective Questions

Answer each question in 3–5 sentences:

**Question 1:** A hospital wants to improve its radiology AI by training on data from 50 affiliated hospitals. None of the hospitals are willing to share patient data externally due to HIPAA. What technology from this module directly addresses this constraint? Describe how it would work in this specific context.

**Question 2:** An AI agent with access to email, calendar, and file management tools is tasked with scheduling a project kickoff meeting for 15 stakeholders. What could go wrong? Apply the principle of least privilege — what specific tool permissions would you restrict to reduce risk?

**Question 3:** You are advising a startup building an AI application for real-time translation on a mobile device with 6GB RAM and no reliable internet connectivity. What two model compression techniques from this module would you prioritize, and why?

**Question 4:** The lecture states that quantum machine learning is "primarily a research topic in 2026, not a production technology." In what career context would it be valuable to start learning quantum computing concepts today, even if production applications are 5–10 years away?

---

## Industry Trend Analysis

Read ONE of the following and write a 200-word analysis:

**Option A:** The 2025 AI Index Report (Stanford HAI) — `https://aiindex.stanford.edu/report/`

**Option B:** McKinsey's State of AI 2025 — `https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai`

**Option C:** A recent industry analyst report on AI trends from Gartner, Forrester, or IDC (access via TXWES Library)

Your analysis should address:

1. What trend surprised you most and why?
2. Which finding is most relevant to your career goals?
3. What concern or limitation does the report identify that the AI industry needs to address?

---

## AI-900 Exam Alignment

Module 15 content maps to the following AI-900 exam domain:

**Domain: Describe features of generative AI workloads (25–30%)**

Specifically:

- Understanding Azure OpenAI capabilities including multimodal features
- Recognizing appropriate use cases for AI services
- Understanding responsible deployment of emerging AI capabilities

**Exam Tip:** The AI-900 exam will not test detailed knowledge of federated learning, quantum ML, or edge AI compression techniques. Focus on: what multimodal AI can do, what Azure OpenAI Service provides, what AI agents are conceptually, and how generative AI fits within responsible AI principles.

---

*Reading Guide prepared by Professor Nash | Texas Wesleyan University | CIS-4330*

# Video Script: Module 15 — Emerging AI Technologies

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Production Notes

- **Runtime Target:** 28–32 minutes
- **Slide Deck:** M15_Slides.pptx
- **Graphics:** Multimodal architecture diagram; federated learning network diagram; certification pathway chart
- **Tone:** Forward-looking and energizing; help students see where the field is going

---

## SEGMENT 1 — Hook and Module Overview (Slides 1–3) [3 min]

[ON CAMERA]

When I was teaching the first version of this course in 2019, there was a clear boundary between what AI could do and what it could not. It could classify images, translate text, and recommend products — but only one thing at a time, with separate specialized models. Today, GPT-4 can look at a photograph of a math problem handwritten on a napkin and solve it. An AI agent can plan a trip, book flights, send confirmation emails, and add events to your calendar — all from a single natural language instruction.

We are living through the most rapid expansion in AI capability in history. Module 15 is your map of what is happening on the frontier — not the hype, but the real technological advances and what they mean for practitioners.

[SLIDE 1: Title — "Emerging AI Technologies"]

[SLIDE 2: Module Learning Objectives]

By the end of this module you will be able to:

- Describe multimodal AI and its architectural foundations
- Explain AI agents and agentic workflows
- Define edge AI and its deployment considerations
- Describe federated learning and its privacy advantages
- Introduce quantum machine learning concepts
- Map a certification and career pathway in AI

[SLIDE 3: Why Emerging Technologies Matter for AI-900]

The AI-900 exam was written in 2020 and updated periodically. The exam covers foundational concepts that are stable. But your career will be built on the technologies that emerge from 2024 onward. This module gives you both the exam-relevant knowledge and the forward-looking perspective that will serve you for the next decade.

---

## SEGMENT 2 — Multimodal AI (Slides 4–9) [7 min]

[SLIDE 4: What Is Multimodal AI?]

Multimodal AI refers to models that can understand and generate information across multiple data types simultaneously — text, images, audio, video, documents, and structured data. Unlike traditional models that process a single modality, multimodal models learn joint representations of different data types in a shared embedding space.

The key word is *simultaneously*. A multimodal model does not just process an image and a text prompt separately and combine results. It processes them together, allowing one modality to inform interpretation of another.

[SLIDE 5: The Architecture of Multimodal Models]

Modern multimodal architectures typically consist of:

**Modality encoders** — separate encoder networks for each input type. A vision transformer encodes images; a language transformer encodes text. These are often large pretrained models.

**Projection layers** — linear transformations that map the output of each encoder into a shared embedding space. This is the key innovation: once images and text are in the same space, the model can reason about their relationship.

**A unified transformer** — a large language model (or similar) that processes the combined multimodal embeddings and produces output in text or another modality.

This is the architecture behind GPT-4V (vision), Google Gemini, and Microsoft Copilot. All of them use variants of this pattern.

[SLIDE 6: Azure OpenAI and Multimodal Capabilities]

For the AI-900 exam, you need to know where multimodal capabilities live in Azure. The relevant service is **Azure OpenAI Service**, which provides access to GPT-4 with vision capabilities. Key features:

- **GPT-4V:** Accepts image and text inputs, produces text outputs
- **DALL-E:** Text input, image output — text-to-image generation
- **Whisper:** Audio input, text output — speech recognition
- **Embeddings API:** Any modality → vector embedding

Microsoft's **Azure AI Vision** service also supports multimodal use cases through image captioning, optical character recognition, and dense captioning of image regions.

[SLIDE 7: Real-World Multimodal Applications]

Let's look at what multimodal AI enables in practice.

**Healthcare — Multimodal Diagnosis**
A physician uploads a chest X-ray image and types: "Does this image show any signs consistent with a pleural effusion? The patient is 68 years old with a history of congestive heart failure." The model reasons over both the image and the clinical context together.

**Manufacturing — Visual QA**
An engineer photographs a mechanical component and asks: "Is this weld line acceptable per our specification document?" The model reads the spec document and analyzes the image simultaneously.

**Legal — Document and Image Analysis**
A lawyer uploads a contract PDF and an annotated diagram, asking: "Does the diagram in Exhibit B reflect the specifications described in Section 4.3?" The model cross-references both.

[SLIDE 8: Multimodal Limitations and Challenges]

Multimodal AI is powerful but has important limitations:

**Hallucination in vision:** Models can misinterpret image content, sometimes confidently asserting things that are not visible in the image. This is called visual hallucination.

**Context length:** Long documents and high-resolution images both consume large amounts of context window capacity. Combining modalities reduces effective context for each.

**Evaluation difficulty:** Evaluating multimodal model performance is harder than single-modality benchmarks. Ensuring accurate reasoning across modalities at scale is an open research problem.

**Cost:** Multimodal API calls are significantly more expensive than text-only calls. Token pricing increases substantially when images are included.

[SLIDE 9: What Comes Next in Multimodal]

The frontier of multimodal AI is moving toward:

- **Native video understanding** — processing video as a first-class modality, not just individual frames
- **Audio generation** — high-quality speech synthesis, music generation, and sound effect synthesis
- **3D and spatial AI** — models that understand three-dimensional geometry from multiple images or depth sensors
- **Real-time multimodal interaction** — voice + vision simultaneously, as demonstrated in GPT-4o's live demo capability

---

## SEGMENT 3 — AI Agents (Slides 10–14) [6 min]

[SLIDE 10: What Is an AI Agent?]

An AI agent is a system that uses a language model (or other AI model) as a reasoning engine to autonomously plan and execute multi-step tasks toward a goal, using a set of tools or actions.

The key distinction from a standard AI model is **autonomy and tool use**. A regular language model responds to a single prompt. An agent can:

- Break a complex goal into sub-tasks
- Call external tools (web search, code execution, database queries, email APIs)
- Observe the results of those tool calls
- Revise its plan based on observations
- Continue until the goal is achieved

[SLIDE 11: The ReAct Pattern — How Agents Think]

The dominant agent reasoning pattern is called **ReAct** (Reasoning + Acting). In a ReAct loop, the agent alternates between:

**Thought:** "I need to find the current weather in Dallas to answer this question."

**Action:** Call the weather API tool.

**Observation:** "The weather API returned: Dallas, TX, 78°F, partly cloudy."

**Thought:** "Now I have the data. I can compose my answer."

**Action:** Return response to user.

This loop continues until the task is complete or the agent determines it cannot proceed. The key insight is that reasoning and tool use are interleaved — the model reasons about what to do, does it, observes the result, and reasons again.

[SLIDE 12: Agentic Frameworks in Azure]

Microsoft has invested heavily in agentic AI infrastructure. Relevant tools include:

**Azure AI Agent Service** — A managed service for building and deploying AI agents with built-in tool calling, state management, and conversation history.

**Semantic Kernel** — An open-source SDK for building AI agents in .NET, Python, and Java. Semantic Kernel provides the planner-action-memory architecture and connects to Azure OpenAI as the reasoning engine.

**AutoGen** — Microsoft Research's multi-agent framework where multiple specialized AI agents collaborate to solve complex problems. One agent might code, another tests, a third reviews — like a virtual engineering team.

**Copilot Studio** — A low-code platform for building custom Copilot agents for Microsoft 365 integration.

[SLIDE 13: Multi-Agent Systems]

Single agents are powerful. Multi-agent systems are transformative. In a multi-agent system, specialized agents handle different aspects of a complex task:

- A **planner agent** receives the high-level goal and breaks it into sub-tasks
- **Specialist agents** handle each sub-task (research, coding, data analysis, writing)
- A **critic agent** reviews outputs for quality and consistency
- An **orchestrator** coordinates handoffs between agents

Microsoft's AutoGen framework has demonstrated multi-agent systems that autonomously solve software engineering problems, with coding agents writing code and testing agents running tests in a loop.

[SLIDE 14: Agent Risks and Safeguards]

AI agents introduce new risks that do not exist with static model inference:

**Prompt injection:** Malicious content in the environment (a web page, email, or document the agent reads) can hijack the agent's actions.

**Unintended side effects:** An agent with broad tool access can take consequential actions (send emails, execute code, delete files) that are hard to reverse.

**Scope creep:** Agents optimizing for a goal may take actions outside the intended scope.

Safe agentic design requires: minimal tool permissions (principle of least privilege), human-in-the-loop approval gates for high-stakes actions, action logging and auditability, and sandboxed execution environments.

---

## SEGMENT 4 — Edge AI (Slides 15–17) [4 min]

[SLIDE 15: What Is Edge AI?]

Edge AI refers to running AI models on or near the devices generating data, rather than sending data to a central cloud for processing. The "edge" is the periphery of the network: phones, IoT sensors, cameras, vehicles, industrial equipment, and wearables.

[SLIDE 16: Why Edge AI Matters]

Four drivers make edge AI compelling:

**Latency:** A self-driving car cannot wait 200ms for a round-trip to the cloud to decide whether to brake. Edge inference happens in under 5ms.

**Bandwidth:** A manufacturing plant with 1,000 cameras generating 4K video cannot send all that data to the cloud. Processing locally and sending only alerts is practical.

**Privacy:** Patient health data processed on a local hospital device never needs to leave the premises. GDPR and HIPAA compliance is much simpler.

**Reliability:** Edge AI continues operating when network connectivity fails. Critical industrial systems cannot depend on cloud availability.

[SLIDE 17: Azure Edge AI Tools]

Azure supports edge AI through:

**Azure IoT Edge** — Runtime that deploys containerized AI models to IoT devices. Models trained in Azure ML are packaged as Docker containers and deployed to edge devices.

**ONNX Runtime** — Open-source cross-platform runtime that runs models on CPUs, GPUs, and specialized neural processing units. Models converted to ONNX format run on any edge device.

**Azure Percept (retired, superseded by partner ecosystem)** — Azure's edge AI hardware reference platform.

**Windows AI (WinML)** — Runs ONNX models locally on Windows devices using hardware acceleration.

The challenge of edge AI is model compression: the models that achieve state-of-the-art accuracy are often hundreds of gigabytes in size. Edge devices have kilobytes to megabytes of memory. Techniques like quantization (reducing numerical precision), pruning (removing unnecessary weights), and knowledge distillation (training small "student" models to mimic large "teacher" models) make edge deployment practical.

---

## SEGMENT 5 — Federated Learning (Slides 18–20) [4 min]

[SLIDE 18: What Is Federated Learning?]

Federated learning (FL) is a machine learning approach where a model is trained across multiple decentralized data sources without centralizing the raw data. Each participant trains a local model on their local data, sends model updates (gradients or weights) to a central coordinator, and the coordinator aggregates them into a global model.

No raw data ever leaves the local device or institution.

[SLIDE 19: How Federated Learning Works]

The FL training loop:

1. **Global model initialization** — coordinator sends the current global model to all participants
2. **Local training** — each participant trains the model on their local data for several steps
3. **Update transmission** — participants send local model updates (weight differences) to the coordinator
4. **Aggregation** — coordinator aggregates updates using FedAvg or a similar algorithm
5. **Global model update** — aggregated update is applied to the global model
6. **Repeat** for multiple rounds

Apple's Siri uses federated learning to improve next-word prediction without sending your typed messages to Apple's servers. Google uses FL for Google Keyboard (Gboard) predictions.

[SLIDE 20: Federated Learning Limitations]

FL solves the data centralization problem but introduces new challenges:

**Communication cost:** Sending model updates repeatedly across thousands of devices requires significant bandwidth.

**Heterogeneous data:** Each participant's local dataset may have different distributions, making convergence harder.

**Partial privacy:** Model updates can still leak information about local data through gradient inversion attacks. Differential privacy is often combined with FL to address this.

**System heterogeneity:** Participants have different compute, memory, and connectivity. Stragglers slow down training rounds.

---

## SEGMENT 6 — Quantum Machine Learning (Slides 21–23) [3 min]

[SLIDE 21: Quantum Computing Fundamentals (Brief)]

Quantum computers use quantum bits (qubits) that can exist in superposition — representing 0, 1, or any combination simultaneously. Quantum entanglement and interference allow quantum algorithms to explore exponentially large solution spaces that classical computers must explore sequentially.

For context: a 300-qubit quantum computer in superposition can represent more states simultaneously than there are atoms in the observable universe.

[SLIDE 22: Quantum Machine Learning — What It Is and Is Not]

Quantum Machine Learning (QML) is the intersection of quantum computing and ML. The theoretical promise is that quantum computers could accelerate certain ML tasks — particularly optimization (finding model weights) and sampling from complex distributions.

However, I want to be very direct: **quantum ML is primarily a research topic in 2026, not a production technology.** Current quantum computers are noisy, have limited qubit counts, and error correction is not yet solved at scale. The "quantum advantage" for ML — meaning a QML algorithm demonstrably outperforming the best classical ML algorithm on a practical problem — has not been conclusively demonstrated.

Do not let anyone sell you a "quantum AI" product without asking hard questions about what the quantum component actually does.

[SLIDE 23: Azure Quantum and Near-Term Relevance]

Azure Quantum provides cloud access to quantum hardware from IonQ, Quantinuum, and Microsoft's own topological qubit research. For students interested in this space, the relevant near-term opportunities are:

- **Quantum-inspired optimization** — classical algorithms that borrow ideas from quantum annealing to solve combinatorial optimization problems faster
- **Hybrid classical-quantum algorithms** — quantum circuits for specific subroutines (sampling, linear algebra) embedded in larger classical ML pipelines
- **Learning quantum computing foundations** — Python + Qiskit or Q# programming to position for the quantum talent market 5–10 years from now

---

## SEGMENT 7 — Future Trends and Certification Roadmap (Slides 24–28) [5 min]

[SLIDE 24: Near-Term AI Trends (2026–2030)]

Five trends that will define AI development over the next five years:

**1. AI Agents in Production** — The shift from AI as a tool (you query it) to AI as a colleague (it acts autonomously) is already underway. Enterprises will deploy fleets of specialized agents by 2027.

**2. AI-Native Applications** — New software categories designed from the ground up around AI capabilities, rather than AI bolted onto legacy software.

**3. Smaller, More Efficient Models** — The scaling-equals-performance assumption is breaking down. Models like Phi-3 and Mistral demonstrate that small, well-trained models can match much larger models on many benchmarks.

**4. Multimodal Everywhere** — Text-only AI will become a legacy modality. All production AI systems will be multimodal within five years.

**5. AI Governance as a Profession** — As AI regulation expands globally, AI ethics officers, AI governance managers, and AI auditors will be mainstream corporate roles.

[SLIDE 25: AI Regulation Trends]

The regulatory landscape is rapidly evolving:

**EU AI Act:** Enacted 2024. Classifies AI systems by risk level (unacceptable, high, limited, minimal). High-risk AI systems (healthcare, financial, employment, law enforcement) require conformity assessments, transparency, and human oversight. Prohibited uses include real-time biometric surveillance in public spaces.

**US Executive Order on AI (2023):** Requires safety testing for frontier AI models, promotes standards development through NIST, and directs federal agencies to adopt AI responsibly.

**China AI Regulations:** Require AI-generated content to be labeled, prohibit AI content that undermines state authority, and mandate security assessments for generative AI products.

The common thread: governments are converging on requirements for transparency, human oversight of high-stakes AI, and prohibition of the most dangerous applications.

[SLIDE 26: The Industry Certification Roadmap]

[GRAPHICS: Certification pathway chart]

For CIS-4330 students, here is the recommended certification pathway:

**Tier 1 — Foundation (Start Here):**

- **AI-900 Microsoft Azure AI Fundamentals** — This course prepares you for this certification. 45 minutes, no prerequisites, establishes your AI credential baseline.

**Tier 2 — Associate Level (Year 1–2 post-graduation):**

- **AI-102 Microsoft Azure AI Engineer Associate** — Designing and implementing Azure AI solutions. Requires programming experience.
- **DP-100 Azure Data Scientist Associate** — Machine learning pipelines, model training, deployment on Azure.
- **Google Professional Machine Learning Engineer** — Comparable Google Cloud alternative.
- **AWS Machine Learning Specialty** — Amazon Web Services equivalent.

**Tier 3 — Advanced (Year 3+ post-graduation):**

- **SC-200 Microsoft Security Analyst** — Relevant for AI security roles
- **GitHub Copilot certification** — For AI-assisted development roles
- **Databricks Certified Machine Learning Professional** — For data engineering + ML roles

[SLIDE 27: Career Pathways in AI]

The AI career landscape in 2026 spans technical and non-technical roles:

**Technical:**

- ML Engineer — Builds and deploys models in production
- Data Scientist — Analyzes data and develops predictive models
- AI/ML Platform Engineer — Builds MLOps infrastructure
- AI Security Engineer — Secures AI systems against adversarial threats
- Prompt Engineer / AI Interaction Designer — Designs prompts and interaction patterns for LLM applications

**Non-Technical / Hybrid:**

- AI Product Manager — Manages AI products and feature roadmaps
- AI Ethics Officer / Responsible AI Manager — Governance and policy
- AI Business Analyst — Identifies AI opportunities and translates to requirements
- AI Consultant — Advises organizations on AI strategy and implementation

[SLIDE 28: Module 15 and Course Summary]

This is the last content module before Module 16, which is your exam preparation and capstone. You have now covered the full landscape: AI fundamentals, machine learning, computer vision, NLP, generative AI, MLOps, business applications, security and privacy, and the emerging frontier.

The AI-900 exam is your immediate deliverable. But the real deliverable of this course is a mental model of AI that will serve you for the next 20 years as the technology continues to evolve. See you in Module 16.

[END OF VIDEO]

---

*Script prepared by Professor Nash | Texas Wesleyan University | CIS-4330*

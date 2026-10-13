# Reading Guide: Module 10 — Generative AI and Azure OpenAI Service

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4330 &BULL; INTRODUCTION TO ARTIFICIAL INTELLIGENCE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Domain: Describe features of generative AI workloads on Azure

---

## Overview

This reading guide covers generative AI fundamentals, Azure OpenAI Service, prompt engineering techniques, major use cases, and responsible AI guardrails. Estimated reading time: 50–65 minutes.

---

## Section 1: Generative AI Fundamentals

### Discriminative vs. Generative AI

| Dimension | Discriminative AI | Generative AI |
|-----------|------------------|---------------|
| Task | Classify, detect, extract | Create new content |
| Output | Label, score, bounding box | Text, image, code, audio |
| Training objective | Learn decision boundaries | Learn data distribution |
| Examples | Image classifier, NER, sentiment | GPT-4, DALL-E, Stable Diffusion |
| Azure examples | Custom Vision, CLU, Face API | Azure OpenAI Service |

### How Large Language Models Work

A large language model is a neural network trained to predict the next token in a sequence. Training involves exposure to hundreds of billions of tokens from diverse text sources. The model learns statistical patterns at multiple levels — grammar, style, facts, reasoning, and code conventions — without any explicit programming of these features.

At inference time, you provide a **prompt** (a sequence of tokens) and the model generates a **completion** (a continuation of that sequence) by repeatedly sampling the next most likely token.

Key properties of LLMs:

**Context window**: The maximum number of tokens the model can consider at once. GPT-4 Turbo supports 128,000 tokens — roughly 100,000 words. Everything within the context window is equally accessible to the model.

**Temperature**: Controls randomness in token sampling. Temperature 0.0 is deterministic (always most likely token). Higher values (0.7–1.0) introduce variation for creative tasks.

**Max tokens**: Caps the length of the generated response.

**Stop sequences**: Tokens that terminate generation early.

### Transformer Architecture

Modern LLMs are based on the transformer architecture introduced in the 2017 paper "Attention Is All You Need." The key innovation is the **self-attention mechanism**, which allows the model to weigh the relevance of every token in the context window when predicting the next token — capturing long-range dependencies that earlier architectures (RNNs, LSTMs) struggled with.

You do not need to understand transformer internals for AI-900, but you should know the name and the general capability it enables.

---

## Section 2: Azure OpenAI Service

### What It Provides

Azure OpenAI Service makes OpenAI's models available through Azure's enterprise cloud infrastructure. You interact with the models via REST API or the Azure OpenAI SDK, using the same prompt interface as the OpenAI API but with Azure's security, compliance, and data governance controls in place.

### Model Families Available

| Model Family | Capabilities | Primary Use Cases |
|-------------|-------------|------------------|
| GPT-4 | Complex reasoning, vision input, long context | Analysis, code generation, complex writing |
| GPT-3.5 Turbo | Chat interaction, moderate complexity | Summarization, Q&A, simple tasks |
| DALL-E 3 | Text-to-image generation | Concept art, illustrations, marketing images |
| Whisper | Speech-to-text transcription | Meeting transcription, voice input |
| Ada / text-embedding | Text vectorization | Semantic search, clustering, RAG |

### Why Azure OpenAI vs. Direct OpenAI API

| Consideration | Azure OpenAI | Direct OpenAI API |
|--------------|-------------|-------------------|
| Data privacy | Processed and stored in your Azure region | Processed by OpenAI; may be used for model improvement |
| Compliance certifications | SOC 2, ISO 27001, HIPAA, FedRAMP | Fewer enterprise certifications |
| Content filtering | Built-in, always-on, configurable | Available but less integrated |
| Azure integration | Native (AI Search, Monitor, Key Vault) | Via API calls only |
| Access | Requires approved Azure subscription | Available to all paid OpenAI customers |

### Accessing Azure OpenAI

Azure OpenAI requires an approved subscription. You apply through the Azure portal. Standard Azure for Students subscriptions do not automatically include Azure OpenAI access; your instructor will provide access details for the lab.

---

## Section 3: Prompt Engineering Techniques

### The System Prompt

The system prompt is the foundational instruction set for a chat-based model. It is processed before any user message and establishes:

- The model's role and persona
- Topic scope and constraints
- Output format requirements
- Tone and style guidelines
- Safety instructions

A well-crafted system prompt dramatically reduces the need for repetitive instructions in every user turn.

### Prompting Strategies

| Strategy | Description | Best For |
|----------|-------------|----------|
| Zero-shot | Instruction only, no examples | Simple well-defined tasks |
| One-shot | One example of input-output pair | Tasks with specific format requirements |
| Few-shot | Multiple examples | Format-sensitive tasks; improving consistency |
| Chain-of-thought | Instruct the model to reason step by step | Math, logic, multi-step analysis |
| Role prompting | Assign a specific expert role in the system prompt | Specialized language, domain framing |
| Self-consistency | Generate multiple responses and select the most consistent | High-stakes reasoning tasks |

### Few-Shot Prompt Structure

A few-shot prompt follows this pattern:

```text
[Task description]

Example 1:
Input: [example input 1]
Output: [example output 1]

Example 2:
Input: [example input 2]
Output: [example output 2]

Now:
Input: [actual input]
Output:
```

The examples teach the model the format, style, and reasoning pattern you expect. Two to five examples typically provide sufficient signal for most tasks.

### Chain-of-Thought Trigger Phrases

Adding any of these phrases to a prompt activates more deliberate step-by-step reasoning:

- "Think step by step."
- "Explain your reasoning before giving the answer."
- "Let's work through this carefully."
- "Show your work."

This technique significantly improves accuracy on arithmetic, logic puzzles, and multi-step analytical questions.

### Common Prompt Engineering Mistakes

| Mistake | Effect | Fix |
|---------|--------|-----|
| Vague task description | Unpredictable outputs | Be explicit about what you want |
| No output format specified | Inconsistent structure | Specify JSON, bullet list, table, etc. |
| No scope constraint | Model goes off-topic | Add "Answer only questions about X" |
| Asking for facts without grounding | Hallucination risk | Provide source documents in the prompt |
| Too long a prompt | Diluted attention | Keep prompts focused and structured |

---

## Section 4: Retrieval-Augmented Generation (RAG)

### The Hallucination Problem

LLMs generate text by predicting probable token sequences. They do not retrieve facts from a database; they approximate facts from statistical patterns learned during training. This means they can generate confident, fluent, but factually incorrect statements — called **hallucinations**.

Hallucinations are more common when:

- The model is asked about recent events after its training cutoff
- The model is asked about highly specific or niche information
- The question is ambiguous or lacks context

### How RAG Works

Retrieval-Augmented Generation combines a retrieval system with the generative model:

```text
1. User submits a question
2. System searches a document store for relevant chunks
3. Retrieved chunks are inserted into the model's context as grounding
4. Model generates an answer based on the retrieved content
5. Model is instructed to cite sources or say "I don't know" if content is absent
```

### Azure Services for RAG

| Component | Azure Service |
|-----------|--------------|
| Document storage and indexing | Azure AI Search |
| Text chunking and embedding | Azure OpenAI — text-embedding model |
| Vector similarity search | Azure AI Search — vector search |
| Answer generation | Azure OpenAI — GPT-4 or GPT-3.5 |
| Orchestration | Azure AI Studio prompt flows, LangChain, or custom code |

RAG is the recommended architecture for any enterprise application where factual accuracy is required — legal, medical, financial, and technical support use cases all benefit from RAG over pure generation.

---

## Section 5: Use Cases Reference

### Summarization

| Use Case | Prompt Pattern |
|----------|---------------|
| Executive summary | "Summarize the following in 3 bullet points for a non-technical audience" |
| Meeting action items | "Extract all action items and owners from the following transcript" |
| Legal contract summary | "Summarize the key obligations and termination clauses in this contract" |
| Research abstract | "Write a 150-word abstract for the following paper" |

### Code Generation

| Use Case | Prompt Pattern |
|----------|---------------|
| Function implementation | "Write a Python function that [description]. Include docstring and type hints." |
| Code explanation | "Explain what this code does in plain English" |
| Debugging | "What is wrong with this code? Here is the error: [error message]" |
| Unit tests | "Write pytest tests for this function including edge cases" |
| Language conversion | "Convert this Python function to TypeScript" |
| SQL query | "Write a SQL query to [description]" |

### Content Creation

| Use Case | Prompt Pattern |
|----------|---------------|
| Product descriptions | "Write 3 product descriptions for [product]. Each should be 40–60 words highlighting [benefit]." |
| Email drafts | "Draft a professional email declining [request] while maintaining the relationship" |
| Social media | "Write 5 tweet-length variants for this announcement: [text]" |
| Quiz questions | "Write 5 multiple-choice questions about [topic] at a college introductory level" |

---

## Section 6: Responsible AI Guardrails in Azure OpenAI

### Content Filtering Categories

Azure OpenAI Service applies built-in content filters to both prompts (inputs) and completions (outputs).

| Category | Description |
|----------|-------------|
| Hate | Content that attacks people based on protected characteristics |
| Sexual | Explicit sexual content |
| Violence | Content depicting or promoting physical harm |
| Self-harm | Content promoting self-harm or suicide |

Each category has severity levels: safe, low, medium, high. You can configure the threshold at which content is blocked, within the limits Microsoft permits. Some thresholds cannot be lowered below a baseline for safety reasons.

### Jailbreak and Prompt Injection

**Jailbreak attacks** are prompt formulations that attempt to override the system prompt and make the model ignore its safety instructions. Common patterns include asking the model to "pretend" to be an unconstrained AI, using fictional framing, or embedding instructions in base64 encoding.

Azure OpenAI Service includes jailbreak detection that flags and blocks known attack patterns.

**Prompt injection** occurs when user-supplied content attempts to insert instructions that override the developer's system prompt. This is especially relevant in RAG systems where user documents may contain adversarial text.

### Data Protection

| Feature | Description |
|---------|-------------|
| No training use | Customer prompts and completions are not used to train base models |
| Regional processing | Data stays in the Azure region you select |
| Encryption at rest | Prompts and outputs stored temporarily are encrypted |
| Audit logs | Azure Monitor captures API call metadata |

### Human Oversight Requirements

For high-stakes applications, Microsoft's responsible AI guidance recommends:

- Human review before publishing or acting on generated content
- Output evaluation on representative test cases before deployment
- Monitoring of live traffic for quality regression or safety incidents
- Clear user disclosure when content was AI-generated

---

## Section 7: AI-900 Exam Tips

### High-Frequency Exam Topics

**Topic 1 — Definition of generative AI.** Know that generative AI creates new content rather than classifying or extracting from existing content. Know examples: text (GPT), images (DALL-E), code.

**Topic 2 — Hallucination.** Know what it is (plausible but factually incorrect output) and the primary mitigation (RAG / grounding with source documents).

**Topic 3 — Prompt engineering strategies.** Know the names and descriptions of zero-shot, few-shot, and chain-of-thought. Know that system prompts define model role and constraints.

**Topic 4 — Azure OpenAI models.** Know GPT-4 and GPT-3.5 for text/code, DALL-E for images, Whisper for speech, and embedding models for vectors.

**Topic 5 — Content filter categories.** Memorize the four categories: hate, sexual, violence, self-harm. Know that filters apply to both inputs and outputs.

**Topic 6 — RAG components.** Know that RAG combines a retrieval system (Azure AI Search) with generation (GPT) to ground responses in trusted documents.

### Common Exam Traps

- "DALL-E is a language model" is wrong. DALL-E is an image generation model.
- "Content filters can be completely disabled" is wrong. Some baseline safety protections are always active.
- "GPT-4 retrieves facts from the internet at inference time" is wrong by default. Standard GPT-4 uses only its training-time knowledge plus whatever is in the context window (the prompt).
- "Azure OpenAI and OpenAI's API are the same service" is wrong. Azure OpenAI runs on Azure with enterprise controls; the direct OpenAI API runs on OpenAI's infrastructure.

---

## Section 8: Key Term Glossary

| Term | Definition |
|------|-----------|
| Generative AI | AI that produces new content (text, image, code) rather than classifying existing content |
| Large language model (LLM) | Transformer-based deep learning model trained on large text corpora for text generation |
| Prompt | Input text provided to an LLM to guide its output |
| Completion | The text output generated by an LLM in response to a prompt |
| System prompt | Pre-conversation instructions defining the model's role, scope, and behavior |
| Temperature | Sampling parameter controlling randomness of output (0 = deterministic; higher = more varied) |
| Context window | Maximum tokens the model considers at once |
| Hallucination | Confident-sounding but factually incorrect output from an LLM |
| Retrieval-Augmented Generation (RAG) | Architecture that retrieves relevant documents and injects them into the prompt to ground responses |
| Zero-shot prompting | Instructing the model with no examples |
| Few-shot prompting | Providing examples of input-output pairs in the prompt |
| Chain-of-thought | Prompting technique instructing the model to reason step by step |
| DALL-E | Azure OpenAI image generation model |
| Whisper | Azure OpenAI speech-to-text model |
| Content filtering | Built-in Azure OpenAI guardrails screening for hate, sexual, violence, and self-harm content |
| Jailbreak | Prompt attack attempting to override safety instructions |
| Grounding | Providing source material in the prompt to reduce hallucination |

---

## Section 9: Study Checklist

Work through this checklist before taking the quiz.

- [ ] I can explain the difference between discriminative and generative AI with examples
- [ ] I understand how LLMs work at a conceptual level (predict next token)
- [ ] I know what temperature controls and how it affects output
- [ ] I know the Azure OpenAI model families: GPT-4, GPT-3.5, DALL-E, Whisper, embeddings
- [ ] I can describe zero-shot, few-shot, and chain-of-thought prompting
- [ ] I know what a system prompt is and what it controls
- [ ] I can explain hallucination and describe why RAG mitigates it
- [ ] I know the four content filter categories in Azure OpenAI Service
- [ ] I can describe at least two responsible AI concerns specific to generative AI
- [ ] I know why Azure OpenAI offers enterprise advantages over the direct OpenAI API
- [ ] I can select the appropriate Azure OpenAI model for a given use case

---

## 10. Supplemental Resources

**1. OpenAI Cookbook — Prompt Engineering Guide**
<https://cookbook.openai.com/articles/related_resources>
A curated collection of practical prompting techniques, RAG patterns, and code examples maintained by OpenAI. Covers zero-shot, few-shot, chain-of-thought, and system prompt design with runnable Python notebooks directly applicable to Azure OpenAI deployments.

**2. Microsoft — Responsible AI Practices for Generative AI (official guidance)**
<https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/responsible-ai-overview>
Microsoft's official responsible AI overview for Azure OpenAI Service covering content filtering, human oversight requirements, use-case restrictions, and transparency disclosures. Directly relevant to the Module 10 lab reflection and AI-900 exam content.

**3. Andrej Karpathy — Intro to Large Language Models (YouTube, 1 hour)**
<https://www.youtube.com/watch?v=zjkBMFhNj_g>
A free one-hour conceptual lecture by AI researcher Andrej Karpathy explaining how LLMs work — tokenization, pretraining, RLHF, and emergent capabilities — at an intuitive level without heavy mathematics. One of the most viewed AI education resources available and directly supports the Module 10 conceptual foundations.

---

End of Reading Guide — Module 10

# Video Script: Module 10 — Generative AI and Azure OpenAI Service

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Microsoft Azure AI Fundamentals (AI-900)

---

## INTRO SEGMENT (0:00 – 1:30)

Welcome to Module 10. I'm Professor Nash. We have spent the last several weeks building up our understanding of AI systems — vision, language understanding, conversational agents. Today we reach what is arguably the most transformative development in the history of AI: generative AI and large language models.

By the end of this module you will be able to explain what generative AI is and how large language models work, describe Azure OpenAI Service and its available models, apply prompt engineering techniques to get better outputs, identify use cases including summarization, code generation, and content creation, and explain Microsoft's responsible AI guardrails for generative AI.

Let's start with a question that will reframe everything: what does it mean for a machine to "generate" something?

---

## SECTION 1: What Is Generative AI? (1:30 – 4:00)

All the AI we have covered so far has been **discriminative** — it takes an input and produces a classification, an extraction, or a decision. Given an image, classify it. Given text, extract sentiment.

Generative AI does something different. It creates new content — text, images, code, audio, video — that did not previously exist. It is not retrieving an answer from a database or selecting from a fixed set of labels. It is generating something novel, token by token.

The dominant architecture for generative AI today is the **large language model**, or LLM. An LLM is a deep learning model trained on enormous quantities of text — books, websites, code, scientific papers — using a transformer architecture.

The core training objective is simple in concept: predict the next token given all the tokens that came before. A token is roughly a word or subword. By solving this prediction problem at massive scale, the model develops a rich internal representation of language, facts, reasoning patterns, and even coding conventions.

At inference time, you provide a prompt — an initial sequence of tokens — and the model generates a continuation, one token at a time, until it reaches a stopping condition. The sampling process can be deterministic (always choosing the most likely next token) or stochastic (introducing randomness for creative variation).

This simple mechanism, applied at sufficient scale, produces remarkably capable systems. GPT-4, Claude, Gemini, and the models available in Azure OpenAI Service are all built on this foundation.

---

## SECTION 2: Azure OpenAI Service (4:00 – 7:00)

**Azure OpenAI Service** is a managed Azure service that provides access to OpenAI's foundation models — including GPT-4, GPT-3.5, DALL-E, and Whisper — through Azure's enterprise cloud infrastructure.

Why use Azure OpenAI instead of OpenAI's API directly?

First, **enterprise security**: data stays within your Azure subscription and does not leave your Azure region. Microsoft has contractual commitments that customer data is not used to train the base models.

Second, **compliance**: Azure OpenAI meets SOC 2, ISO 27001, HIPAA, and other certifications that enterprises and regulated industries require.

Third, **integration**: Azure OpenAI integrates naturally with other Azure services — Azure AI Search for retrieval, Azure Monitor for observability, Azure Key Vault for secrets.

Fourth, **content filtering**: built-in responsible AI content filters are always active and configurable.

**[SHOW DEMO]** In the Azure portal, navigate to Create a Resource and search for "Azure OpenAI." Show the resource creation blade. Point out that Azure OpenAI requires an approved subscription — not all subscriptions have access by default. Show the Pricing tiers (Standard). After the resource is created, show the Azure AI Studio link from the resource overview page.

The primary deployment interface is **Azure AI Studio** (now part of the Azure AI Foundry portal). This is where you deploy models, configure playgrounds, and manage your generative AI applications.

---

## SECTION 3: Available Models and Their Capabilities (7:00 – 9:30)

Azure OpenAI Service provides access to several families of models.

**GPT-4 series**: Microsoft's most capable models for complex reasoning, nuanced instruction following, long-context understanding, and multimodal tasks. GPT-4o supports both text and image inputs.

**GPT-3.5 series**: Faster and lower-cost than GPT-4. Well-suited for straightforward tasks: summarization, classification, translation, simple Q&A. GPT-3.5 Turbo is optimized for chat interaction.

**DALL-E**: Image generation. You provide a text description and DALL-E generates an image matching the description. Supports inpainting (editing specific regions of an image) and outpainting (extending an image beyond its borders).

**Whisper**: Automatic speech recognition. Transcribes audio to text in multiple languages.

**Text Embedding models**: Convert text into dense vector representations. Used for semantic search, clustering, and retrieval-augmented generation.

**[SHOW DEMO]** Navigate to Azure AI Studio. Click "Deployments" and show an existing GPT-4 deployment. Click "Open in playground." Type a simple prompt: "Explain what a transformer model is in two sentences for a first-year college student." Show the response. Point out the model selector, temperature slider, and max token setting.

---

## SECTION 4: Prompt Engineering (9:30 – 13:00)

The quality of a generative AI output is highly dependent on the quality of the prompt. **Prompt engineering** is the practice of designing and refining inputs to language models to get better, more consistent, and more useful outputs.

This is a genuine technical skill, and it is directly tested on AI-900.

### System Prompts and User Prompts

Chat-based models distinguish between the **system prompt** (a set of instructions given to the model before the conversation begins) and **user messages** (the actual conversation turns).

The system prompt is where you define the model's role, tone, constraints, and format requirements. For example:

```
System: You are a helpful customer service assistant for Contoso Electronics.
You answer questions about products, orders, and warranties only.
Do not discuss competitors. Respond in a friendly, professional tone.
Always offer to connect the user with a human agent if you cannot help.
```

### Zero-Shot, Few-Shot, and Chain-of-Thought

**Zero-shot prompting** provides only the instruction with no examples. "Translate the following sentence to French."

**Few-shot prompting** provides one or more examples of the desired input-output pattern before presenting the actual request. This is highly effective for tasks with a specific output format.

```
Classify the sentiment of the following reviews as Positive, Negative, or Neutral.

Review: "The product arrived on time and works perfectly." → Positive
Review: "It stopped working after two days." → Negative
Review: "The packaging was fine but the product is average." → Neutral

Review: "I am amazed by the build quality." →
```

**Chain-of-thought prompting** asks the model to reason step by step before reaching a conclusion. Adding "Let's think step by step" or "Explain your reasoning" to complex analytical prompts significantly improves accuracy on multi-step problems.

### Grounding and Retrieval-Augmented Generation

A common challenge with LLMs is **hallucination** — generating confident-sounding but factually incorrect statements. This is a fundamental property of statistical token prediction, not a bug that will be fully fixed.

**Retrieval-Augmented Generation**, or RAG, is the primary mitigation. In a RAG architecture:

1. A user asks a question.
2. The system searches a trusted document store (Azure AI Search, for example) for relevant passages.
3. The retrieved passages are injected into the model's context as grounding information.
4. The model generates an answer based on the retrieved content rather than relying on its parametric knowledge.

**[SHOW DEMO]** In Azure AI Studio Playground, show a grounded prompt where the system message contains a product specification document and the user asks a specific technical question. Show how the model cites the provided text rather than hallucinating. Then show the same question without the grounding document and demonstrate the hallucination risk.

---

## SECTION 5: Use Cases — Summarization (13:00 – 15:00)

One of the most immediately valuable use cases for generative AI is **summarization**.

Enterprises generate enormous volumes of text: meeting transcripts, legal documents, customer support threads, research reports, news feeds. GPT models can condense these into concise summaries in seconds.

Summarization prompt patterns include:

- "Summarize the following in three bullet points for a non-technical executive."
- "Write a one-paragraph abstract of the following research paper."
- "Identify the action items and decisions from the following meeting transcript."

The key to reliable summarization is **grounding** — always providing the source text in the prompt. Never ask the model to summarize something it has to recall from training. Provide the document and ask it to summarize what you provided.

**[SHOW DEMO]** In the Azure AI Studio Playground, paste a long article or document. Prompt the model to summarize it in three key points. Show the output. Then show a follow-up prompt: "Now write a version of that summary suitable for a tweet." Demonstrate how the same source content can be reformatted for different audiences.

---

## SECTION 6: Use Cases — Code Generation (15:00 – 17:00)

GPT-4 and GPT-3.5 were trained on billions of lines of code across dozens of programming languages. This makes them highly capable at code-related tasks.

Practical code generation use cases include:

- **Code completion**: Given a function signature and docstring, generate the implementation
- **Code explanation**: "Explain what this function does in plain English"
- **Code translation**: "Convert this Python function to JavaScript"
- **Debugging**: "What is wrong with this code? Here is the error message."
- **Unit test generation**: "Write pytest unit tests for the following function"
- **SQL generation**: "Write a SQL query that returns the top 10 customers by revenue this quarter"

**[SHOW DEMO]** In the Azure AI Studio Playground, prompt: "Write a Python function that takes a list of integers and returns the second largest unique value. Include docstring and type hints." Show the generated code. Then prompt: "Now write three pytest test cases for this function, including edge cases." Show how the model generates meaningful tests for the code it just wrote.

Caution: generated code should always be reviewed by a human developer before deployment. Models can generate code that looks correct but contains subtle logic errors, security vulnerabilities, or licensing issues.

---

## SECTION 7: Use Cases — Content Creation (17:00 – 18:30)

Content creation is another major category of generative AI applications.

Examples include:

- Drafting marketing copy in a brand voice
- Generating product descriptions from specification data
- Creating personalized email templates at scale
- Producing first drafts of reports or proposals
- Generating educational content, quiz questions, and explanations

The key responsible use principle here is **human review**. Generated content should be treated as a draft that a human reviews, edits, and approves — not as finished output ready for publication.

DALL-E extends content creation to images. Organizations use it for concept visualization, blog post illustrations, and social media graphics.

**[SHOW DEMO]** In the Azure AI Studio Playground, demonstrate a content creation prompt: "Write three product descriptions for a wireless noise-canceling headphone. Use a professional but approachable tone. Each description should be 40–60 words and highlight a different benefit: battery life, noise cancellation, and comfort." Show the three distinct outputs.

---

## SECTION 8: Responsible AI Guardrails (18:30 – 21:00)

Generative AI introduces risks distinct from those in traditional machine learning: hallucination, toxic content generation, misuse for disinformation, intellectual property concerns, and misrepresentation.

Microsoft addresses these through several layers of guardrails.

**Content filtering**: Azure OpenAI Service has built-in content filters that screen both inputs (prompts) and outputs (completions) for four harm categories — hate speech, sexual content, violence, and self-harm. Each category has configurable severity thresholds. The filters are always on; they cannot be entirely disabled.

**Jailbreak detection**: Azure OpenAI Service detects prompt injection attacks — attempts to override the system prompt and make the model behave outside its intended scope. These are flagged and blocked.

**Data residency**: Prompts and completions are processed in the Azure region you select. They are not stored or used to train the base models.

**Grounding requirements**: For applications where accuracy matters, prompt designs should always include source documents. The model should be instructed to cite sources or state when it does not know.

**Human review workflows**: For high-stakes outputs — legal documents, medical information, financial advice — a human review step must be embedded in the workflow before content is delivered or published.

**Model evaluation**: Azure AI Studio provides evaluation tools to measure generated output quality — relevance, coherence, fluency, and groundedness — across large test sets.

**[SHOW DEMO]** In Azure AI Studio, navigate to the Content Filters configuration. Show the four harm categories and their severity levels. Demonstrate submitting a prompt that triggers a filter and show the blocked response with the filter category flagged.

---

## SECTION 9: AI-900 Exam Alignment and Recap (21:00 – 23:00)

Generative AI is one of the highest-growth areas of the AI-900 exam. Let's consolidate the key terms.

- **Generative AI** — AI that produces new content (text, images, code) rather than classifying or extracting from existing content
- **Large language model (LLM)** — deep learning model trained on large text corpora to predict and generate text
- **Azure OpenAI Service** — managed Azure service providing access to GPT, DALL-E, Whisper, and embedding models
- **Prompt** — input text provided to a language model to guide its output
- **System prompt** — pre-conversation instructions defining the model's role and behavior
- **Few-shot prompting** — providing examples of desired input-output patterns in the prompt
- **Chain-of-thought** — asking the model to reason step by step
- **Hallucination** — generating plausible-sounding but factually incorrect content
- **Retrieval-Augmented Generation (RAG)** — injecting retrieved documents into the prompt to ground model responses
- **DALL-E** — Azure OpenAI image generation model
- **Content filtering** — built-in Azure OpenAI Service guardrails for hate, sexual content, violence, and self-harm
- **Grounding** — providing source material in the prompt to reduce hallucination

For the exam: know the four content filter categories, know what hallucination is and why RAG mitigates it, and know the difference between zero-shot, few-shot, and chain-of-thought prompting.

---

## OUTRO (23:00 – 24:00)

Generative AI is moving faster than any technology I have taught in 15 years of higher education. What we covered today is a foundation — the concepts will remain relevant even as specific models and tools evolve.

In the lab you will explore the Azure AI Studio Playground, engineer prompts for summarization and code generation, and test the content filtering system.

Module 11 closes the course with the full Microsoft Responsible AI framework — our ethical compass for everything we have built this semester. I will see you there.

---

End of Script — Module 10. Estimated delivery: 23 minutes with demos.

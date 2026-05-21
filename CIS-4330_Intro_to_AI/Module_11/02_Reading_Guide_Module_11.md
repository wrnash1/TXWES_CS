# Reading Guide: Module 11 - Azure OpenAI Service and Generative AI
## Course: CIS-4330_Intro_to_AI (AI-900 (Microsoft Azure AI Fundamentals))

---

### Introduction
Welcome to **Module 11 - Azure OpenAI Service and Generative AI**! This module covers the principles behind large language models (LLMs) and how Microsoft Azure provides enterprise-grade access to OpenAI's models — including GPT-4, DALL-E, and Codex — through the **Azure OpenAI Service**. Generative AI is among the most rapidly tested topics on the **AI-900 (Microsoft Azure AI Fundamentals)** exam.

As a student, you will learn how the Transformer architecture and self-attention enable LLMs to understand and generate coherent text, how prompt engineering guides model outputs without retraining, how fine-tuning adapts a pre-trained model to a specific domain, and how embeddings represent meaning as numeric vectors for similarity and retrieval tasks. Complete the glossary and checklist before beginning the lab.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Transformer architecture and self-attention**: The deep learning architecture that underpins all modern LLMs. Instead of processing tokens one at a time (like an RNN), a Transformer processes all tokens in a sequence simultaneously and uses self-attention to compute how much each token should "attend to" every other token in the same sequence. This parallelism makes Transformers dramatically faster to train on large datasets and gives them the ability to capture long-range dependencies in text.
*   **Prompt engineering**: The practice of carefully designing the input text (the "prompt") sent to an LLM to guide it toward a desired output — without modifying the model's weights. Effective prompt engineering includes providing clear instructions, relevant context, few-shot examples, and explicit output format requirements. It is the primary technique for adapting a general-purpose LLM to a specific task without fine-tuning.
*   **Fine-tuning**: The process of taking a large pre-trained model and continuing to train it on a smaller, task-specific dataset to adapt its weights to a particular domain or style. Fine-tuning is more expensive than prompt engineering but produces a model that deeply specializes in the target task. In Azure OpenAI Service, fine-tuning is available for selected base models via the Azure portal.
*   **Embeddings**: Dense numeric vector representations of text (words, sentences, or documents) that encode semantic meaning — words or passages with similar meanings produce vectors that are close together in the embedding space. Embeddings power semantic search, recommendation systems, and retrieval-augmented generation (RAG) by enabling similarity comparisons between pieces of text using distance metrics like cosine similarity.

---

### 2. Certification Exam Tips
*   **AI-900 Focus Area:** The exam tests the difference between using a pre-trained LLM as-is (via Azure OpenAI Service REST API), adapting it with prompt engineering, and fine-tuning it on custom data. Know these distinctions: **prompt engineering** = no model weight changes, fastest, cheapest; **fine-tuning** = model weights updated on custom data, more targeted results, higher cost; **embeddings** = vector representation used for similarity search, not generation. Also know that Azure OpenAI Service requires an approved Azure subscription — it is not open to all Azure accounts by default.
*   **Common AI-900 Trap:** The exam distinguishes **Azure OpenAI Service** (enterprise-secured access to OpenAI models like GPT-4 inside Azure, with data residency and compliance guarantees) from **OpenAI directly** (consumer/developer API with different terms). For enterprise scenarios involving data sovereignty or compliance, the answer is always Azure OpenAI Service. Additionally, do not confuse **generative AI** (produces new content — text, images, code) with **discriminative AI** (classifies or labels existing content). Many exam distractors use the wrong category.
*   **Study Resource:** The Microsoft Learn module [Fundamentals of Generative AI](https://learn.microsoft.com/en-us/training/modules/fundamentals-generative-ai/) covers LLM concepts, prompt engineering, and Azure OpenAI Service directly aligned to AI-900 exam objectives. It is free and includes hands-on exercises in Azure AI Studio. A companion module, [Fundamentals of Azure OpenAI Service](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/), walks through the service's capabilities, deployment models, and responsible use guidelines.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters on neural language models, Transformer architectures, and generative AI in the OER Textbook: [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/). This freely available textbook by Poole and Mackworth provides the theoretical grounding in sequence modeling and attention mechanisms that underpin all modern LLMs.
*   **Required Video:** Watch the generative AI and Azure OpenAI Service segment in the official AI-900 preparation playlist: [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU). This video covers Transformer architecture, prompt engineering best practices, and how Azure OpenAI Service fits into the broader Azure AI ecosystem — including the responsible use considerations tested on the exam.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Examine prompt templates for LLM interactions**: Write three prompt variants for the same task (zero-shot, one-shot, few-shot) using the Azure OpenAI Python SDK or the OpenAI library, then compare how the model's response changes as more in-context examples are provided.
*   **Write structured prompts with context constraints**: Craft a system-role prompt that instructs the model to answer only from a provided context passage and respond with "I don't know" when the answer is not present — demonstrating a retrieval-augmented generation (RAG) pattern without a vector database.
*   **Analyze model outputs for hallucination indicators**: Submit five factual questions to an LLM and score each response for accuracy, identifying cases where the model generates confident but incorrect statements — then revise the prompts to reduce hallucination by grounding the model with explicit source text.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and memorize their definitions.
*   [ ] Read the chapters on neural language models and generative AI in [Artificial Intelligence: Foundations of Computational Agents](http://artint.info/).
*   [ ] Watch the video lecture on Azure OpenAI Service and Generative AI in [Microsoft Azure AI Fundamentals Complete Course](https://www.youtube.com/watch?v=s0H3G50vGgU).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.

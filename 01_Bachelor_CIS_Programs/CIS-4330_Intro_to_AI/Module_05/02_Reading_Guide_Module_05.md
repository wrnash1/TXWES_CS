# Reading Guide: Module 05 - Natural Language Processing (NLP) Fundamentals

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


## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe features of Natural Language Processing workloads on Azure (15-20%)

---

## Overview

This reading guide covers NLP concepts, tasks, text representation techniques, and Azure NLP services. The AI-900 exam tests your ability to identify NLP task types and match them to the correct Azure service. The comparison tables in this guide are your primary study tools for those questions. Complete the study checklist before the lab.

---

## Section 1: Core Vocabulary

**Natural Language Processing (NLP)**
The field of AI focused on enabling computers to understand, interpret, generate, and reason about human language. NLP bridges the gap between human communication and machine computation.

**Tokenization**
The process of breaking text into discrete units called tokens. Tokens can be words, subwords, punctuation marks, or other meaningful text units. Tokenization is the first step in any NLP pipeline.

**Token**
A discrete unit of text produced by the tokenizer. In word-level tokenization, each word is one token. In subword tokenization (used by BERT and GPT), words may be split into multiple tokens.

**Word Embedding**
A dense numerical vector that represents a word or token. Words with similar meanings have similar vectors in the embedding space. Embeddings encode semantic relationships geometrically.

**Contextual Embedding**
An embedding that varies based on the surrounding words. Unlike static embeddings (Word2Vec, GloVe), contextual embeddings from transformer models represent the same word differently depending on context. Enables polysemy resolution.

**Sentiment Analysis**
An NLP task that determines the emotional tone of a text: positive, negative, neutral, or mixed. Used for customer review analysis, social media monitoring, and brand sentiment tracking.

**Key Phrase Extraction**
An NLP task that identifies the most important topics or concepts in a document without full summarization. Used for document indexing and content analysis.

**Named Entity Recognition (NER)**
An NLP task that identifies and classifies entities in text into predefined categories: people, organizations, locations, dates, monetary values, and more.

**Language Detection**
An NLP task that identifies the language a piece of text is written in. Azure Language Service supports over 120 languages.

**Text Classification**
An NLP task that assigns a predefined category label to a document. Examples: spam detection, news categorization, support ticket routing.

**Question Answering**
An NLP task that locates the answer to a natural language question within a knowledge base, FAQ document, or unstructured text.

**Machine Translation**
An NLP task that converts text from one natural language to another. Azure Translator supports 100+ languages.

**Speech Recognition (ASR)**
Converting spoken audio into text. Also called automatic speech recognition or speech-to-text. Provided by Azure Speech Service.

**Text-to-Speech (TTS)**
Converting written text into synthesized spoken audio. Azure Speech Service provides this capability with many voice options.

**Intent Recognition**
Identifying the underlying goal or intention behind a natural language utterance. Used in conversational AI to route user statements to the correct action. Provided by Azure Language Understanding (LUIS) and Conversational Language Understanding.

**Entity (in conversational AI)**
A specific piece of information extracted from an utterance that is needed to fulfill the user's intent. In "Book a flight to Dallas on Friday," the entities are: destination=Dallas, date=Friday.

**Transformer**
A deep learning architecture that uses self-attention to process entire text sequences simultaneously, capturing long-range dependencies. The architecture behind BERT, GPT-4, and most modern NLP systems.

**BERT (Bidirectional Encoder Representations from Transformers)**
A pretrained transformer model that processes text bidirectionally — it reads every word in context of all other words simultaneously. Fine-tuned BERT models power many Azure Language Service capabilities.

**Self-Attention**
A mechanism in transformer networks that allows each token in a sequence to learn relationships with every other token, enabling the model to understand context and long-range dependencies.

**Azure Language Service**
An Azure Cognitive Service that provides NLP capabilities including sentiment analysis, key phrase extraction, named entity recognition, language detection, custom text classification, and custom question answering.

**Azure Translator**
An Azure Cognitive Service for text translation across 100+ languages, document translation, and transliteration.

**Azure Speech Service**
An Azure Cognitive Service that provides speech recognition (speech-to-text), speech synthesis (text-to-speech), speaker recognition, and speech translation.

**Azure Language Understanding (LUIS)**
An Azure Cognitive Service for understanding the intent and entities in natural language utterances. Used to build conversational AI that responds to user commands. Now part of Conversational Language Understanding within Language Service.

---

## Section 2: Comparison Tables

### Table 1: Core NLP Tasks and Azure Services

| NLP Task | Description | Azure Service | API Input | API Output |
|---|---|---|---|---|
| Sentiment Analysis | Determine emotional tone of text | Azure Language Service | Text string | Positive/Negative/Neutral score (0-1) |
| Key Phrase Extraction | Identify important topics in text | Azure Language Service | Text string | List of key phrases |
| Named Entity Recognition | Identify and classify entities | Azure Language Service | Text string | Entity text, category, confidence score |
| Language Detection | Identify the language of text | Azure Language Service | Text string | Language name, ISO code, confidence |
| Text Classification | Assign category labels to documents | Azure Language Service (custom) | Text string | Label(s) with confidence scores |
| Question Answering | Find answers to questions in a knowledge base | Azure Language Service (custom QA) | Question string | Answer text, confidence score |
| Translation | Convert text between languages | Azure Translator | Text + target language | Translated text |
| Speech-to-Text | Convert spoken audio to text | Azure Speech Service | Audio stream/file | Transcript text |
| Text-to-Speech | Convert text to spoken audio | Azure Speech Service | Text string | Audio stream |
| Intent Recognition | Identify the goal behind an utterance | LUIS / Conversational Language Understanding | Utterance string | Intent name, entities, confidence |

### Table 2: Azure Language Service Capabilities

| Capability | Prebuilt or Custom | Training Data Required | Primary Use Case |
|---|---|---|---|
| Sentiment Analysis | Prebuilt | No | Customer feedback analysis |
| Key Phrase Extraction | Prebuilt | No | Document summarization, indexing |
| Named Entity Recognition | Prebuilt | No | Information extraction |
| Language Detection | Prebuilt | No | Multilingual routing |
| Custom Text Classification | Custom | Yes | Domain-specific classification |
| Custom Named Entity Recognition | Custom | Yes | Domain-specific entity types |
| Custom Question Answering | Custom | Yes (FAQ documents) | FAQ and help desk bots |

### Table 3: NLP Techniques — Historical vs Modern

| Dimension | Rule-Based / Classical NLP | Modern Transformer-Based NLP |
|---|---|---|
| Approach | Hand-crafted rules, dictionaries, grammar parsers | Data-driven, learned from billions of text examples |
| Feature representation | Bag-of-words, TF-IDF (frequency counts) | Contextual embeddings (BERT, GPT) |
| Context handling | Limited — window-based methods | Full sequence — self-attention across all tokens |
| Performance | Moderate on narrow tasks | State-of-the-art across all NLP tasks |
| Data requirement | Low (rules are written, not learned) | High (pretraining requires massive corpora) |
| Interpretability | High (rules are readable) | Low (embeddings are dense vectors) |
| Polysemy resolution | Poor — one vector per word | Excellent — context-dependent embeddings |

### Table 4: Text Representation Methods

| Method | How It Works | Pros | Cons |
|---|---|---|---|
| Bag of Words | Each document represented as word frequency counts | Simple, interpretable | Ignores word order and context |
| TF-IDF | Weights words by frequency in document vs. corpus | Highlights distinctive words | Still ignores context and order |
| Word2Vec / GloVe | Static word embedding trained on large corpus | Captures semantic similarity | One fixed vector per word — no context |
| BERT embeddings | Contextual embeddings from bidirectional transformer | Context-sensitive; handles polysemy | Computationally expensive; less interpretable |
| Sentence embeddings | Single vector representing entire sentence meaning | Enables semantic search and similarity | Requires pretrained transformer |

---

## Section 3: The NLP Pipeline

Every NLP application follows a similar processing pipeline. Understanding each stage helps you match Azure services to business requirements.

**Stage 1 — Text Ingestion:** Raw text arrives from a data source: customer reviews, emails, social media posts, documents, or live speech.

**Stage 2 — Text Preprocessing:** Cleaning and normalizing the text. Steps may include lowercasing, removing punctuation, handling HTML tags, and correcting spelling.

**Stage 3 — Tokenization:** Breaking the cleaned text into tokens. For Azure Cognitive Services, this happens automatically inside the service.

**Stage 4 — Embedding / Feature Extraction:** Converting tokens to numerical representations. For Azure prebuilt services, this is handled internally by BERT or similar models. For custom models in Azure ML, you may need to generate embeddings explicitly.

**Stage 5 — NLP Task Execution:** Applying the specific NLP algorithm: classifying sentiment, extracting entities, identifying intent, translating language, or generating a response.

**Stage 6 — Output Delivery:** Returning structured results — JSON objects containing labels, confidence scores, extracted entities, translated text — to the calling application.

---

## Section 4: Conversational AI and Intent Recognition

Intent recognition is a specialized NLP task critical for building chatbots and virtual assistants. Understanding the distinction between intents and entities is important for AI-900.

An **intent** is the goal the user is trying to accomplish. Examples: BookFlight, CheckBalance, GetWeather, CancelOrder.

An **entity** is a specific piece of information extracted from the utterance that is needed to fulfill the intent. Examples: city names, dates, product names, account numbers.

Azure Language Understanding (LUIS) and Conversational Language Understanding (CLU) let developers define intents, provide example utterances for each intent, mark entities in those utterances, and train a model to recognize the same patterns in new user input.

Example:

- User says: "What is the weather in Fort Worth this weekend?"
- Recognized intent: GetWeather (confidence: 0.97)
- Entities: Location = "Fort Worth," Date = "this weekend"
- Application action: call weather API with these parameters

---

## Section 5: Responsible AI in NLP

NLP raises specific responsible AI concerns that the AI-900 exam addresses.

**Bias in language models:** Models trained on internet text absorb societal biases. They may associate certain occupations, characteristics, or behaviors with specific demographic groups. Fairness audits and debiasing techniques are active research areas.

**Harmful content generation:** Language models can generate toxic, offensive, or misleading text if not properly constrained. Azure Language Service and Azure OpenAI include content filters and safety classifiers.

**Misinformation and hallucination:** Language models sometimes generate fluent, confident-sounding text that is factually incorrect. This is called hallucination and is a specific challenge for question answering and text generation systems.

**Privacy and memorization:** Models trained on personal data may memorize and reproduce sensitive information. Differential privacy and data minimization techniques help mitigate this.

**Accessibility:** NLP services that only perform well in dominant languages create inequitable access for speakers of minority languages. The Inclusiveness principle in Microsoft's responsible AI framework addresses this.

---

## Section 6: AI-900 Exam Tips

1. Know the difference between Azure Language Service (text analysis) and Azure Speech Service (speech). These are separate services; mixing them up is a common exam mistake.

2. Azure Translator is a separate service from Language Service. When a scenario asks specifically about translation, the answer is Azure Translator, not Language Service.

3. LUIS (Language Understanding) and CLU (Conversational Language Understanding) are for intent recognition in conversational applications. Do not confuse them with text classification or sentiment analysis.

4. Prebuilt capabilities (sentiment analysis, NER, key phrase extraction) require no training data. Custom capabilities (custom text classification, custom QA) require labeled training examples.

5. Named Entity Recognition automatically identifies people, organizations, locations, and dates. If a scenario asks to extract structured information from unstructured text without custom training, NER is the answer.

6. Azure Custom Question Answering lets you create an FAQ bot by uploading existing FAQ documents. The service extracts question-answer pairs automatically. No ML expertise is required.

7. On AI-900, the phrase "understand the intent of user utterances" always maps to LUIS or CLU, not sentiment analysis or text classification.

8. The transformer architecture and BERT are foundational to modern NLP but are not required knowledge at the implementation level for AI-900. Know conceptually that Azure Language Service is built on transformer models pretrained on large text corpora.

---

## Section 7: Required Reading

**Microsoft Learn — Analyze text with Azure AI Language**
learn.microsoft.com/en-us/training/modules/analyze-text-with-text-analytics-service/

Covers sentiment analysis, key phrase extraction, NER, and language detection with Azure Language Service. Includes hands-on exercises.

**Microsoft Learn — Create a language model with Conversational Language Understanding**
learn.microsoft.com/en-us/training/modules/create-language-model-with-language-understanding/

Covers intent recognition, entities, and building a conversational language model — directly tested on AI-900.

**Microsoft Learn — Translate text and speech**
learn.microsoft.com/en-us/training/modules/translate-text-with-translation-service/

Covers Azure Translator and Azure Speech translation capabilities.

---

## Section 8: Study Checklist

- [ ] Write the definitions of tokenization, embedding, sentiment analysis, NER, intent, and entity from memory.
- [ ] Study Table 1 (NLP tasks and Azure services) until you can match any task to its service from memory.
- [ ] Study Table 2 (Language Service capabilities) and know which require custom training vs. prebuilt.
- [ ] Explain the difference between Azure Language Service, Azure Translator, and Azure Speech Service.
- [ ] Explain what LUIS / CLU does and give one example of an intent and an entity.
- [ ] Complete the Microsoft Learn module: Analyze text with Azure AI Language.
- [ ] Review all eight AI-900 exam tips in Section 6.
- [ ] Complete the Module 05 quiz.
- [ ] Complete the Module 05 lab.
- [ ] Post initial discussion by Wednesday 11:59 PM and respond to two peers by Sunday 11:59 PM.

## 9. Supplemental Resources

**1. Hugging Face — NLP Course (free)**
<https://huggingface.co/learn/nlp-course/chapter1/1>
A free, comprehensive NLP course from the team behind the most-used open-source NLP library. Covers transformers, tokenization, fine-tuning, and the key models (BERT, GPT) that underpin Azure Language Service. Accessible to students with basic Python knowledge.

**2. Google AI — Machine Learning Glossary: NLP Terms**
<https://developers.google.com/machine-learning/glossary/nlp>
A concise reference glossary of NLP-specific terms including tokenization, embeddings, attention, and sequence-to-sequence models. Useful for quickly looking up definitions that arise in Module 05 readings and labs.

**3. Microsoft Research — Responsible AI for NLP (blog)**
<https://www.microsoft.com/en-us/research/blog/responsible-ai-for-natural-language-processing/>
A Microsoft Research blog post examining fairness, bias, and responsible AI considerations specific to NLP applications. Directly connects Module 05 content to the AI-900 responsible AI domain and reinforces quiz content on NLP bias scenarios.

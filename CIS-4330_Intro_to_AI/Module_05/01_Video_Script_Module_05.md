# Video Script: Module 05 - Natural Language Processing (NLP) Fundamentals

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AI-900 Domain:** Describe features of Natural Language Processing workloads on Azure (15-20%)

---

## [00:00 - 01:30] Opening

Welcome back. Professor Nash here, and this is Module 05. Over the past four modules, we built a solid foundation in machine learning and neural networks. Today we shift to one of the most practically impactful areas of AI: Natural Language Processing, or NLP.

NLP is the field of AI concerned with enabling computers to understand, generate, and reason about human language. It powers email spam filters, virtual assistants, search engines, real-time translation, customer sentiment analysis, and — increasingly — conversational AI systems like Azure Bot Service. The AI-900 exam dedicates an entire domain to NLP workloads on Azure. This module covers the foundational concepts; Module 07 covers the specific Azure services. Let us get started.

---

## [01:30 - 04:30] Why NLP Is Hard

Human language is extraordinarily complex. Unlike structured data where a "1" always means the same thing, language is ambiguous, context-dependent, and constantly evolving. Let me give you three concrete examples of why this is hard.

Ambiguity: "I saw the man with the telescope." Does this mean I used a telescope to see the man, or I saw a man who had a telescope? Both interpretations are grammatically valid. Humans resolve this from context; computers must be taught to do the same.

Polysemy: The word "bank" means a financial institution, a riverbank, or the act of turning an aircraft. The same word has radically different meanings depending on context. NLP systems must learn to represent words in context, not in isolation.

Negation: "The food was not bad" is a positive statement. "The food was not good" is a negative statement. Handling negation correctly is non-trivial for machines.

Historical NLP systems used hand-crafted rules — dictionaries of synonyms, grammar parsers, and rule-based entity extractors. Modern NLP is entirely data-driven: models learn language representations from billions of words of text. This shift, powered by transformer architectures (which we cover in Module 11), has produced a step-change in NLP capability.

---

## [04:30 - 08:00] Key NLP Tasks

The AI-900 exam tests your ability to identify NLP workload types and match them to Azure services. Let me walk through the eight core NLP tasks you need to know.

**Sentiment Analysis** determines the emotional tone of a piece of text: positive, negative, neutral, or mixed. Used in customer review analysis, social media monitoring, and product feedback systems. Azure Text Analytics provides sentiment analysis as a prebuilt API.

**Key Phrase Extraction** identifies the most important concepts or topics in a document without summarizing the entire text. Used in document indexing, meeting transcription analysis, and content categorization.

**Named Entity Recognition (NER)** identifies and classifies entities in text: people, organizations, locations, dates, monetary values, and more. A sentence like "Microsoft acquired GitHub in 2018 for $7.5 billion" contains named entities: Microsoft (organization), GitHub (organization), 2018 (date), and $7.5 billion (monetary value).

**Language Detection** identifies the language a document is written in. Azure Language Service can detect over 120 languages from a short text sample.

**Translation** converts text from one language to another. Azure Translator supports over 100 languages and can perform both text translation and document translation.

**Text Classification** assigns a label to a document from a set of predefined categories. Examples: spam or not spam, news article category, support ticket priority.

**Question Answering** locates the answer to a question within a knowledge base or document. Azure Language Service includes custom question answering, used to build FAQ bots.

**Speech Recognition** (speech-to-text) converts spoken audio into written text. Azure Speech Service provides this capability in real time.

---

## [08:00 - 11:30] How Text Becomes Numbers — Tokenization and Embeddings

[SHOW DIAGRAM: Pipeline with boxes: "Raw Text" → "Tokenization" → "Token IDs" → "Word Embeddings" → "Neural Network." Each box shows example values.]

Machine learning models work with numbers, not words. To apply ML to text, we need a way to convert words into numerical representations. This process involves two steps: tokenization and embedding.

Tokenization breaks text into discrete units called tokens. In simple word tokenization, each word becomes one token. In subword tokenization — used by modern transformer models — words are split into smaller pieces. The word "unhappiness" might become the tokens "un," "happiness," or even smaller units. Subword tokenization allows the model to handle rare and out-of-vocabulary words by breaking them into known subword pieces.

Once text is tokenized, each token is converted to a unique integer ID from the model's vocabulary. The sentence "the cat sat" might become [342, 891, 1204].

The next step is word embedding: converting each integer token ID into a dense numerical vector. Classic word embeddings like Word2Vec and GloVe map each word to a fixed vector that captures semantic relationships. Words with similar meanings have similar vectors. The famous example: if you take the vector for "king," subtract the vector for "man," and add the vector for "woman," you get a vector close to "queen." This algebraic relationship captures semantic meaning in geometry.

Modern transformer models use contextual embeddings — each word's vector depends on the surrounding words. The word "bank" has a different embedding in "I deposited money at the bank" versus "the river bank was muddy." This context sensitivity is what makes modern NLP systems so powerful.

---

## [11:30 - 14:30] The Transformer Architecture and Why It Matters for NLP

[SHOW DIAGRAM: A simplified transformer diagram. Input tokens enter an "Encoder" block containing a "Self-Attention" layer and a "Feed-Forward" layer. Output tokens leave a "Decoder" block. Bidirectional arrows within the Self-Attention layer connecting every token to every other token.]

Module 11 covers transformers in depth in the context of Azure OpenAI and generative AI. But I want to introduce the key concept here because it is the foundation of every modern NLP system.

The transformer architecture, introduced in the 2017 paper "Attention Is All You Need," uses a mechanism called self-attention. Self-attention allows every token in a sequence to attend to — that is, learn relationships with — every other token simultaneously. This is in contrast to RNNs, which process sequences step by step and struggle with long-range dependencies.

Self-attention means the word "it" in the sentence "The animal did not cross the street because it was too tired" can directly learn that "it" refers to "animal," even though the words are separated. This long-range dependency resolution is what makes transformers dramatically better at NLP than previous architectures.

BERT — Bidirectional Encoder Representations from Transformers — is a pretrained transformer model that learns language representations by processing text in both directions simultaneously. Fine-tuned BERT models power many of Azure's Language Service capabilities including sentiment analysis, NER, and question answering.

---

## [14:30 - 17:30] Azure NLP Services Overview

[SHOW DIAGRAM: A two-column table. Left column: "AI-900 NLP Task." Right column: "Azure Service." Rows: Sentiment Analysis → Language Service / Text Analytics. Translation → Azure Translator. Speech-to-Text → Azure Speech Service. Text-to-Speech → Azure Speech Service. Question Answering → Language Service (custom QA). Key Phrase Extraction → Language Service. Named Entity Recognition → Language Service.]

Azure organizes NLP capabilities primarily under two services that you must know for AI-900.

Azure Language Service — formerly called Text Analytics and Language Understanding (LUIS) — provides prebuilt and customizable NLP capabilities: sentiment analysis, key phrase extraction, named entity recognition, language detection, custom text classification, and custom question answering. You call the REST API with a text input and receive structured JSON results.

Azure Translator is a separate Cognitive Service focused exclusively on translation. It supports real-time text translation across 100+ languages, document translation, and transliteration (converting between scripts, such as Arabic to Latin characters).

Azure Speech Service handles speech-to-text (automatic speech recognition) and text-to-speech (speech synthesis). It also provides speaker recognition and speech translation — converting spoken language in one language directly to text in another.

Azure Language Understanding — LUIS — is a Cognitive Service for understanding the intent behind natural language utterances. Given a user statement like "Set an alarm for 7 AM tomorrow," LUIS identifies the intent (SetAlarm) and the entities (Time: 7 AM, Date: tomorrow). LUIS is used to build conversational AI applications.

For AI-900 scenarios: if the task involves written text analysis, the answer is Language Service. If it involves speech, the answer is Speech Service. If it involves intent recognition in conversation, LUIS or Conversational Language Understanding is the answer.

---

## [17:30 - 20:00] Responsible AI in NLP

Language models learn from human-generated text on the internet, which contains human biases, stereotypes, and harmful content. This creates serious responsible AI considerations for NLP systems.

Bias in language models: if training data over-represents certain demographics, professions, or viewpoints, the model's outputs will reflect those biases. Research has shown that language models associate occupations like "nurse" more strongly with women and "engineer" more strongly with men, reflecting patterns in training text.

Toxicity and harmful content generation: language models trained on internet text have encountered hate speech, misinformation, and violent content. Without careful filtering and alignment training, models can generate harmful outputs.

Privacy: NLP models trained on personal communications may inadvertently memorize and reproduce sensitive personal information including names, emails, and financial details present in training data.

Microsoft addresses these concerns through content filtering built into Azure Language Service and Azure OpenAI Service, responsible AI review processes for model deployment, and the Azure Content Safety service, which can screen both inputs to and outputs from AI systems.

---

## [20:00 - 22:00] Module Summary and Lab Preview

Let me recap Module 05.

NLP enables computers to understand and generate human language. The core NLP tasks tested on AI-900 are: sentiment analysis, key phrase extraction, named entity recognition, language detection, translation, text classification, question answering, and speech recognition.

Text is converted to numbers through tokenization and word embeddings. Modern NLP uses transformer-based contextual embeddings. The transformer's self-attention mechanism enables direct modeling of long-range dependencies.

Azure NLP services: Language Service for text analysis, Translator for translation, Speech Service for speech-to-text and text-to-speech.

Responsible AI concerns in NLP include bias in training data, harmful content generation, and privacy risks from memorization.

This week's lab asks you to analyze text samples, identify NLP tasks, and match each to the appropriate Azure service. You will also interpret sentiment and NER outputs from sample API responses.

See you in Module 06, where we cover computer vision and image recognition.

---

## References

- Microsoft Learn — Analyze text with Azure AI Language: learn.microsoft.com/en-us/training/modules/analyze-text-with-text-analytics-service/
- Microsoft Learn — Create a language model with Conversational Language Understanding: learn.microsoft.com/en-us/training/modules/create-language-model-with-language-understanding/
- Microsoft Learn — Translate text and speech: learn.microsoft.com/en-us/training/modules/translate-text-with-translation-service/

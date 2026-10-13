# Video Script: Module 08 — Natural Language Processing with Azure

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Microsoft Azure AI Fundamentals (AI-900)

---

## INTRO SEGMENT (0:00 – 1:30)

Welcome back to CIS-4330. I'm Professor Nash. Last week we taught machines to see. This week we teach them to read.

Natural language processing — NLP — is the branch of AI concerned with enabling computers to understand, interpret, and generate human language. It powers spell-checkers, search engines, translation tools, virtual assistants, and countless other systems you use daily.

By the end of this module you will be able to describe the Azure Language Service and its core capabilities, explain sentiment analysis, key phrase extraction, named entity recognition, and language detection, describe the Azure Translator service, and understand Conversational Language Understanding for building intent-based applications.

Let's start with why language is hard for computers.

---

## SECTION 1: Why NLP Is Difficult (1:30 – 3:30)

Human language is ambiguous, context-dependent, and constantly evolving. Consider the sentence: "I saw the man with the telescope." Does that mean I used a telescope to see the man, or I saw a man who was holding a telescope? A human reader uses context to disambiguate. A computer has to learn to do the same thing.

Language also involves:

- **Morphology**: words change form — run, runs, ran, running. A model must connect these as related.
- **Syntax**: word order matters, and rules vary across languages.
- **Semantics**: the same word can mean different things. "Bank" can mean a financial institution or the edge of a river.
- **Pragmatics**: meaning depends on context. "Can you pass the salt?" is a request, not a question about physical ability.

Modern NLP systems handle these challenges through transformer-based deep learning models — architectures that read entire sentences at once rather than word by word, capturing long-range relationships between words.

Azure wraps these powerful models into managed services so developers can add language capabilities to applications without building or training the models themselves.

---

## SECTION 2: Azure AI Language Service Overview (3:30 – 6:00)

The Azure AI Language service is a cloud-based API that provides a broad set of pre-built NLP capabilities accessible via REST endpoints.

**[SHOW DEMO]** In the Azure portal, navigate to Create a Resource and search for "Language." Show the Language resource creation blade. Point out the Free F0 tier: 5,000 text records per month. Standard S tier charges per 1,000 text records.

The key capabilities of Azure AI Language are:

**Sentiment analysis and opinion mining** — determines the emotional tone of text, returning positive, negative, neutral, or mixed sentiment at the document and sentence level.

**Key phrase extraction** — identifies the most important phrases in a piece of text, useful for summarization and indexing.

**Named entity recognition (NER)** — identifies and categorizes entities such as people, organizations, locations, dates, quantities, and more.

**Entity linking** — disambiguates recognized entities to a known knowledge base such as Wikipedia.

**Language detection** — identifies what language a piece of text is written in.

**Text summarization** — produces extractive or abstractive summaries of long documents.

**Personally Identifiable Information (PII) detection** — identifies and can redact sensitive personal data such as names, social security numbers, and phone numbers.

**Custom text classification** — trains a model on your own labeled text data to classify documents into your own categories.

**Custom named entity recognition** — trains a model to recognize domain-specific entity types not in the pre-built model.

All capabilities are available through a single multi-purpose endpoint or through specialized endpoints, depending on the feature.

---

## SECTION 3: Sentiment Analysis (6:00 – 8:00)

Sentiment analysis — also called opinion mining when applied to specific aspects of a document — determines whether text expresses a positive, negative, or neutral attitude.

The Azure Language service returns sentiment at two levels.

**Document sentiment** gives an overall assessment of the entire text with confidence scores for positive, negative, and neutral.

**Sentence sentiment** breaks the document into sentences and gives each an independent sentiment assessment.

Opinion mining goes further. It identifies specific aspects — nouns or noun phrases — and associates a sentiment with each. For example, in a restaurant review: "The food was excellent but the service was slow" — opinion mining would identify food with positive sentiment and service with negative sentiment.

**[SHOW DEMO]** Navigate to Language Studio at language.cognitive.azure.com. Select "Analyze sentiment and mine opinions." Enter the text: "The new software update made the dashboard much faster, but I am frustrated that it removed the dark mode feature." Show the output identifying mixed document sentiment, positive sentence for speed, and negative sentence for dark mode removal. Point out the aspect-level breakdown.

The REST call is a POST to:

```http
POST https://<endpoint>/language/:analyze-text?api-version=2023-04-01
```

The request body specifies the task type as `SentimentAnalysis` and includes the input documents array.

---

## SECTION 4: Key Phrase Extraction (8:00 – 9:30)

Key phrase extraction identifies the main talking points in a piece of text. It surfaces the most important words and phrases without you having to read the entire document.

This is valuable for:

- Building search indexes from large document collections
- Generating tags for articles and blog posts automatically
- Providing a quick summary of what a customer review is about
- Routing support tickets to the right team based on content

The service returns an array of key phrases ranked by importance.

For the text: "Azure AI Language provides natural language processing capabilities including sentiment analysis, key phrase extraction, and named entity recognition." — the extracted key phrases might include "Azure AI Language," "natural language processing capabilities," "sentiment analysis," "key phrase extraction," and "named entity recognition."

Notice that the service identifies meaningful multi-word phrases, not just individual keywords. This is important for preserving semantic context.

**[SHOW DEMO]** In Language Studio, select "Extract key phrases." Paste in a paragraph of a news article. Show the extracted phrase list and discuss which phrases the service prioritized.

---

## SECTION 5: Named Entity Recognition (9:30 – 11:30)

Named Entity Recognition — NER — identifies mentions of real-world entities in text and classifies them into predefined categories.

Azure AI Language recognizes the following entity categories by default:

- **Person** — names of people
- **Organization** — companies, agencies, institutions
- **Location** — geographic places, addresses
- **DateTime** — dates, times, durations, sets
- **Quantity** — numbers, percentages, currencies, measurements
- **URL** — web addresses
- **Email** — email addresses
- **Phone number** — telephone numbers
- **IP address** — network addresses

NER is the backbone of many high-value applications. Legal contract analysis systems use NER to extract party names, dates, and clause references. Medical records systems extract diagnoses, medications, and patient identifiers. News aggregators use NER to build knowledge graphs of who, what, when, and where.

**Entity linking** extends NER by connecting recognized entities to their Wikipedia entries. "Jordan" in a sports context links to the athlete Michael Jordan. "Jordan" in a geography context links to the country. The service uses surrounding context to disambiguate.

**[SHOW DEMO]** In Language Studio, select "Extract named entities." Enter a short paragraph about a business news event. Show the color-coded entity annotations over the text and the JSON response with entity categories, text, offset, length, and confidence scores.

---

## SECTION 6: Language Detection and Translation (11:30 – 13:30)

### Language Detection

The language detection capability identifies which language a text is written in. It returns the detected language, its ISO 639-1 code, and a confidence score.

This is useful as a preprocessing step for multilingual pipelines: detect the language first, then route to the appropriate analysis pipeline or translation service.

The service can detect over 120 languages. For mixed-language documents it returns the predominant language.

### Azure AI Translator

While language detection is part of Azure AI Language, translation is handled by a separate service: **Azure AI Translator**.

Translator is a REST API that provides:

- **Text translation** — translate text from any supported language to any other supported language. Supports 135+ languages.
- **Transliteration** — convert text between scripts, for example from Arabic script to Latin script.
- **Language auto-detection** — detect the source language automatically as part of the translation call.
- **Dictionary lookups** — return alternative translations with usage examples.
- **Custom Translator** — fine-tune translations for domain-specific terminology by providing parallel sentence pairs.

**[SHOW DEMO]** In the Azure portal, show the Translator resource. Then open a browser and send a quick REST call demonstrating translation of an English sentence to Spanish and French simultaneously in a single API call. Show the response JSON with the detected source language and both translations.

---

## SECTION 7: Conversational Language Understanding (13:30 – 17:00)

So far we have discussed analyzing static text. But many applications need to understand what a user is trying to do — their intent — and extract the specific information — the entities — relevant to that intent.

This is the domain of **Conversational Language Understanding**, or CLU, which replaced the older LUIS (Language Understanding Intelligent Service) as the primary Azure intent-recognition service.

### Intents and Entities

An **intent** represents the user's goal or purpose. For a pizza ordering app, intents might include:

- OrderPizza
- CancelOrder
- CheckOrderStatus
- GetMenu

An **entity** represents a specific piece of information the model should extract from the utterance. For the pizza scenario, entities might include:

- PizzaSize (small, medium, large)
- PizzaTopping (pepperoni, mushrooms)
- Quantity (one, two, three)

When a user says "I want two medium pepperoni pizzas," CLU should identify the intent as OrderPizza and extract Quantity=2, PizzaSize=medium, PizzaTopping=pepperoni.

### Building a CLU Project

**[SHOW DEMO]** Navigate to Language Studio. Select "Conversational Language Understanding." Show an existing project. Walk through the schema: intents list, entities list, and example utterances. Click Train. Show the evaluation metrics — intent accuracy and entity F1 scores.

A CLU project has three building blocks.

First, you define intents — the categories of user goals.

Second, you define entities — the types of information to extract.

Third, you add training utterances — example sentences labeled with the correct intent and entity values. The more utterances per intent, the better the model generalizes to novel phrasings.

After training, you publish the model to a prediction endpoint. Your application sends user input to this endpoint and receives the top predicted intent and extracted entities in JSON.

### CLU vs. Pre-built Question Answering

CLU is for applications where the user is issuing commands or making requests. It answers "what does the user want to do?"

Question Answering (formerly QnA Maker) is for applications where the user asks a question and expects a direct answer from a knowledge base. It answers "what information does the user need?"

Many conversational AI systems combine both — CLU handles task intents, Question Answering handles informational queries. We will go deeper on this in Module 9.

---

## SECTION 8: Text Summarization and PII Detection (17:00 – 19:00)

### Text Summarization

Azure AI Language offers two summarization approaches.

**Extractive summarization** selects the most important existing sentences from the document and returns them as a summary. No new text is generated — the summary is literally a subset of the original.

**Abstractive summarization** generates new sentences that capture the key points, potentially combining and rephrasing content from multiple parts of the document.

Extractive summarization is more deterministic and interpretable. Abstractive summarization produces more natural-sounding summaries but can occasionally introduce inaccuracies.

Use cases include summarizing legal documents, executive briefings, customer support transcripts, and news articles.

### PII Detection and Redaction

The PII detection capability scans text for personally identifiable information and returns the entities with their category and location in the text.

Crucially, the service can also redact the detected PII — replacing it with placeholder text like `[PERSON]` or `[PHONE_NUMBER]` — before the text is stored or processed further.

This is a critical capability for compliance with GDPR, HIPAA, and similar data protection regulations. Support center transcripts, patient records, and financial documents often contain sensitive information that must be protected.

**[SHOW DEMO]** In Language Studio, demonstrate PII detection on a synthetic customer support transcript. Show how names, phone numbers, and email addresses are identified and how the redacted version replaces them.

---

## SECTION 9: AI-900 Exam Alignment and Recap (19:00 – 21:30)

Azure AI Language covers a significant portion of the AI-900 NLP domain. Let's consolidate the key points.

The exam tests your ability to identify appropriate NLP services for given scenarios, distinguish between the capabilities within Azure AI Language, explain the difference between CLU and Question Answering, and describe the purpose of entities and intents in CLU.

Key terms for the exam:

- **Azure AI Language** — unified service for NLP tasks including sentiment, NER, key phrases, summarization, PII, CLU
- **Azure AI Translator** — dedicated service for text translation across 135+ languages
- **Sentiment analysis** — determining positive, negative, neutral, or mixed emotional tone
- **Opinion mining** — aspect-level sentiment identifying which specific features are discussed positively or negatively
- **Named Entity Recognition (NER)** — identifying and categorizing real-world entities in text
- **Entity linking** — connecting recognized entities to a knowledge base for disambiguation
- **Intent** — the user's goal in a CLU model
- **Entity (CLU)** — a specific piece of information extracted from an utterance
- **Utterance** — an example of user input used to train a CLU model
- **Extractive summarization** — summary built from existing sentences in the source document
- **Abstractive summarization** — summary built from newly generated sentences
- **PII detection** — identification and optional redaction of personally identifiable information

For scenario questions: if a business needs to understand what a user wants to do with a chatbot, the answer is CLU. If a business needs to analyze customer review sentiment at scale, the answer is Azure AI Language sentiment analysis. If a business needs to translate content into 50 languages, the answer is Azure AI Translator.

---

## OUTRO (21:30 – 22:30)

In this module we covered the full breadth of Azure's NLP offerings. In the lab you will call the Language Service API for sentiment analysis and NER, and build a simple CLU project.

Module 9 takes us into conversational AI — chatbots, the Azure Bot Framework, and how CLU and Question Answering work together to build intelligent assistants.

I will see you there.

---

End of Script — Module 08. Estimated delivery: 22 minutes with demos.

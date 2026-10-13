# Reading Guide: Module 08 — Natural Language Processing with Azure

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

## AI-900 Domain: Describe features of Natural Language Processing workloads on Azure

---

## Overview

This reading guide covers the Azure AI Language service, Azure AI Translator, and Conversational Language Understanding (CLU). Work through each section after watching the video lecture. Estimated reading time: 45–60 minutes.

---

## Section 1: NLP Fundamentals

### The NLP Pipeline

Most NLP applications follow a processing pipeline that transforms raw text into structured insights.

**Tokenization** splits text into individual tokens — usually words or subwords. "Running quickly" becomes ["Running", "quickly"].

**Normalization** standardizes tokens: lowercasing, removing punctuation, expanding contractions.

**Stop word removal** filters out high-frequency words with low semantic value: "the," "is," "at."

**Part-of-speech tagging** assigns grammatical roles: noun, verb, adjective.

**Named entity recognition** identifies mentions of real-world entities.

**Dependency parsing** maps syntactic relationships between words.

Modern transformer models (like those behind Azure AI Language) perform many of these steps internally without explicit pipeline stages — they learn contextual representations that implicitly capture all of this information.

### Key NLP Task Types

| Task | Input | Output |
|------|-------|--------|
| Sentiment analysis | Text | Sentiment label + confidence score |
| Key phrase extraction | Text | List of important phrases |
| Named entity recognition | Text | Entity mentions with category + location |
| Language detection | Text | Language code + confidence score |
| Text translation | Text + target language | Translated text |
| Intent classification (CLU) | Utterance | Top intent + confidence score |
| Entity extraction (CLU) | Utterance | Entity type + value + location |
| Text summarization | Document | Summary (extractive or abstractive) |
| PII detection | Text | PII entity list; optional redacted text |

---

## Section 2: Azure AI Language Service — Capability Deep Dive

### Sentiment Analysis

Sentiment analysis returns a label and confidence scores at the document and sentence levels.

| Level | Labels | Output |
|-------|--------|--------|
| Document | positive, negative, neutral, mixed | Label + scores for all three polarities |
| Sentence | positive, negative, neutral | Label + scores per sentence |
| Aspect (opinion mining) | positive, negative, neutral | Aspect noun + associated opinion word |

The scores for positive, negative, and neutral sum to 1.0 at each level.

Opinion mining is enabled by passing `opinionMining=true` in the request. It returns target-assessment pairs: `{ "target": "service", "sentiment": "negative", "assessments": [{ "text": "slow" }] }`.

### Key Phrase Extraction

Key phrase extraction uses statistical and linguistic signals to rank phrases by importance. The service does not return scores for individual phrases — it returns a ranked list ordered by significance.

Practical applications:

- Auto-tagging articles for content management systems
- Building search indexes from unstructured document collections
- Routing customer support tickets to the right specialist queue
- Extracting talking points from meeting transcripts

### Named Entity Recognition

Azure AI Language pre-built NER recognizes the following top-level categories and subcategories.

| Category | Example Entities | Subcategories |
|----------|-----------------|---------------|
| Person | "Satya Nadella," "Dr. Smith" | — |
| PersonType | "engineer," "CEO" | — |
| Organization | "Microsoft," "the FDA" | — |
| Location | "Seattle," "the Pacific Ocean" | GPE, Natural, Structural |
| Event | "World War II," "the Super Bowl" | — |
| Product | "Surface Pro," "iPhone" | — |
| Skill | "Python," "project management" | — |
| Address | "1 Microsoft Way, Redmond WA" | — |
| PhoneNumber | "+1 (206) 555-0100" | — |
| Email | `user@example.com` | — |
| URL | `https://azure.microsoft.com` | — |
| IPAddress | "192.168.1.1" | — |
| DateTime | "next Tuesday," "January 2024" | Date, Time, Duration, Set |
| Quantity | "five kilograms," "30%" | Number, Ordinal, Dimension, Currency |

Custom NER lets you train models to recognize domain-specific entity types not in this list — for example, contract clause types, medical procedure names, or product model numbers.

### PII Detection Categories

PII detection recognizes sensitive personal data including:

- Person names
- Social security / national ID numbers
- Credit card and financial account numbers
- Phone numbers
- Email addresses
- Physical addresses
- Passport and driver's license numbers
- Medical terms (with Healthcare PII model)
- IP addresses

The redaction feature replaces PII with category placeholders in the returned text, enabling downstream processing without exposing sensitive data.

---

## Section 3: Azure AI Translator

### Key Capabilities

| Capability | Description |
|-----------|-------------|
| Text translation | Translate input text to one or more target languages in a single call |
| Language auto-detection | Automatically identify the source language |
| Transliteration | Convert text between writing scripts |
| Dictionary lookup | Get alternative translations with usage context |
| Dictionary examples | Get example sentences for a dictionary translation |
| Detect | Standalone language detection without translation |
| Custom Translator | Fine-tune with domain-specific parallel text |

### Supported Scale

Azure AI Translator supports over 135 languages and dialects. A single API call can request translations into multiple target languages simultaneously, which is efficient for multilingual content distribution.

### Custom Translator

When specialized terminology matters — medical, legal, technical, or brand-specific vocabulary — Custom Translator lets you fine-tune the base translation model by providing aligned sentence pairs in your source and target languages.

The fine-tuned model is deployed to your own private endpoint and behaves like the standard Translator API.

---

## Section 4: Conversational Language Understanding (CLU)

### Core Concepts

CLU is the Azure service for building intent-classification and entity-extraction models for conversational applications.

| Concept | Definition | Example |
|---------|-----------|---------|
| Intent | The user's goal or request | OrderPizza, CancelOrder |
| Entity | A specific piece of information in the utterance | PizzaSize, Topping, Quantity |
| Utterance | An example of user input with labeled intent and entities | "I want a large mushroom pizza" |
| Schema | The complete set of intents and entity types | The "vocabulary" of the application |
| Deployment | A trained model published to a prediction endpoint | Production vs. staging slot |

### None Intent

Every CLU project should include a **None** intent. When a user says something unrelated to any defined intent, the model should predict None rather than forcing a match to the closest real intent. Utterances for None should be diverse and cover common off-topic inputs.

### Entity Types in CLU

| Entity Type | Description | Example |
|-------------|-------------|---------|
| Learned | Extracted by the model from context | Custom product names |
| List | Exact match or fuzzy match against a defined list | City names, product codes |
| Prebuilt | Reuses Azure AI Language prebuilt types | DateTimeV2, Number, Temperature |
| Regex | Pattern-match using a regular expression | Invoice numbers, ZIP codes |

### Training and Evaluation

CLU reports the following metrics per intent and per entity.

| Metric | Meaning |
|--------|---------|
| Precision | Of all predictions of this intent/entity, what fraction were correct |
| Recall | Of all actual instances of this intent/entity, what fraction were found |
| F1 score | Harmonic mean of Precision and Recall |

A model with high precision but low recall is conservative — it predicts the intent only when highly confident, missing some genuine instances. A model with high recall but low precision is aggressive — it predicts the intent often, including false positives.

### CLU vs. Question Answering

Understanding this distinction is critical for AI-900.

| Dimension | CLU | Question Answering |
|-----------|-----|-------------------|
| Purpose | Understand what the user wants to do | Answer a specific question |
| Training data | Labeled utterances with intents and entities | Question-answer pairs from documents or manual entry |
| Output | Top intent + extracted entities | Best matching answer with confidence |
| Use case | Command-based bots, task automation | FAQ bots, knowledge-base queries |
| Formerly known as | LUIS | QnA Maker |

Both services can be combined in a single bot: CLU handles task requests, Question Answering handles informational queries.

---

## Section 5: Text Summarization

### Extractive vs. Abstractive

| Dimension | Extractive | Abstractive |
|-----------|-----------|-------------|
| Method | Selects existing sentences | Generates new sentences |
| Faithfulness | High — no hallucination risk | Moderate — may rephrase inaccurately |
| Fluency | Depends on source text quality | Typically higher |
| Use case | Legal documents, news, contracts | Meeting notes, customer feedback |
| Azure support | Yes (generally available) | Yes (generally available) |

Extractive summarization is deterministic and auditable — you can trace every sentence in the summary back to the source. This is important for regulated industries.

---

## Section 6: Service Comparison for AI-900

### Choosing the Right NLP Service

| Scenario | Service and Feature |
|----------|-------------------|
| Determine if customer reviews are positive or negative | Azure AI Language — Sentiment Analysis |
| Extract main topics from 10,000 support tickets | Azure AI Language — Key Phrase Extraction |
| Find all company names and dates in a contract | Azure AI Language — Named Entity Recognition |
| Translate a website into 20 languages | Azure AI Translator — Text Translation |
| Build a chatbot that books meeting rooms | Azure AI Language — CLU (intents: BookRoom, CancelRoom) |
| Build a chatbot that answers policy questions from an HR manual | Azure AI Language — Question Answering |
| Remove patient names from medical transcripts before storage | Azure AI Language — PII Detection with redaction |
| Condense a 50-page report to 3 key points | Azure AI Language — Text Summarization |

### Pricing Reference

| Service | Free Tier | Standard (approx.) |
|---------|-----------|-------------------|
| Azure AI Language | 5,000 records/month | $2.00 per 1,000 records |
| Azure AI Translator | 2M characters/month | $10.00 per 1M characters |
| CLU training | Included with Language | Compute charges apply |

---

## Section 7: AI-900 Exam Tips

### High-Frequency Topics

**Topic 1 — Sentiment analysis output.** Know that the service returns scores for positive, negative, and neutral that sum to 1.0. Know the difference between document-level and sentence-level sentiment. Know that opinion mining adds aspect-level analysis.

**Topic 2 — NER categories.** Memorize the main categories: Person, Organization, Location, DateTime, Quantity, URL, Email, Phone. Know that custom NER is available for domain-specific types.

**Topic 3 — CLU intents and entities.** For a given scenario, be able to identify what the intents would be and what entities would need to be extracted. This is a frequent scenario-based question format.

**Topic 4 — CLU vs. Question Answering.** This distinction appears regularly. CLU = task/command understanding. QA = answer retrieval from a knowledge base.

**Topic 5 — Translator vs. Language Service.** Translation is a separate service (Azure AI Translator). Language detection is in both services. Do not confuse them.

**Topic 6 — PII redaction.** Know that the service can both detect and redact PII — the redacted text is returned in the response so the original is not modified in place.

### Common Mistakes

- Confusing Key Phrase Extraction (what topics are discussed) with NER (what real-world entities are named)
- Using CLU when Question Answering is the better fit, or vice versa
- Thinking that Azure AI Language and Azure AI Translator are the same service
- Forgetting that CLU replaced LUIS — on the exam, CLU and LUIS may both appear

---

## Section 8: Key Term Glossary

| Term | Definition |
|------|-----------|
| Azure AI Language | Unified Azure service for NLP: sentiment, NER, key phrases, CLU, summarization, PII |
| Azure AI Translator | Separate Azure service for text and document translation across 135+ languages |
| Sentiment analysis | Determining positive, negative, neutral, or mixed tone in text |
| Opinion mining | Aspect-level sentiment — which specific features are discussed positively or negatively |
| Key phrase extraction | Identifying the most important phrases in a piece of text |
| Named entity recognition (NER) | Locating and categorizing real-world entities (Person, Org, Location, etc.) in text |
| Entity linking | Connecting recognized entities to a knowledge base such as Wikipedia |
| Intent (CLU) | The user's goal or purpose in a conversational application |
| Entity (CLU) | A specific piece of information extracted from a user utterance |
| Utterance | A training example of user input labeled with intent and entities |
| None intent | The fallback intent for inputs that do not match any defined application intent |
| F1 score | Harmonic mean of Precision and Recall; balanced quality metric |
| Extractive summarization | Summary composed of existing sentences selected from the source |
| Abstractive summarization | Summary composed of newly generated sentences |
| PII detection | Identifying personally identifiable information; optional redaction in response |
| Custom Translator | Fine-tuned translation model using domain-specific parallel text |

---

## Section 9: Study Checklist

Work through this checklist before taking the quiz.

- [ ] I can name the core capabilities of Azure AI Language (sentiment, key phrases, NER, CLU, summarization, PII)
- [ ] I understand what document-level vs. sentence-level sentiment means
- [ ] I can explain opinion mining and how it differs from basic sentiment analysis
- [ ] I know the main NER entity categories returned by the pre-built model
- [ ] I can define intent, entity, and utterance in the CLU context
- [ ] I understand the None intent and why it is important
- [ ] I can explain the difference between CLU and Question Answering with a scenario example
- [ ] I know that Azure AI Translator is separate from Azure AI Language
- [ ] I can describe the difference between extractive and abstractive summarization
- [ ] I understand what PII detection and redaction do
- [ ] I can select the correct Azure NLP service for a given scenario

---

## 10. Supplemental Resources

**1. Microsoft Learn — Analyze text with Azure AI Language (hands-on module)**
<https://learn.microsoft.com/en-us/training/modules/analyze-text-with-text-analytics-service/>
The primary Microsoft Learn module for Azure AI Language covering sentiment analysis, NER, key phrase extraction, and language detection with sandboxed Azure exercises. Essential preparation for the Module 08 lab.

**2. Hugging Face — Course Chapter on Token Classification (NER)**
<https://huggingface.co/learn/nlp-course/chapter7/2>
A free deep-dive into how token classification (the basis of NER) works in modern transformer models. Covers how models like BERT are fine-tuned for entity recognition and explains the BIO tagging scheme used under the hood by services like Azure AI Language.

**3. Stanford NLP Group — CoreNLP Online Demo**
<https://corenlp.run/>
A free web-based demo of Stanford's CoreNLP pipeline showing tokenization, POS tagging, NER, dependency parsing, and coreference resolution in real time on any text you enter. Excellent for building intuition about what each NLP pipeline stage produces before implementing with Azure AI Language.

---

End of Reading Guide — Module 08

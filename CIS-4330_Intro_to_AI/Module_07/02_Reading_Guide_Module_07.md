# Reading Guide: Module 07 - Azure Cognitive Services: Vision, Speech, and Language

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describes features across all workload domains (vision, NLP, speech, conversational AI)

---

## Overview

This reading guide provides a comprehensive service-by-service reference for all Azure Cognitive Services tested on AI-900. The master comparison tables are your primary exam study tools. Memorize the service-to-task mapping in Table 1 before taking any practice exam. Complete the study checklist before the lab.

---

## Section 1: Core Vocabulary

**Azure Cognitive Services**
Microsoft's family of prebuilt AI APIs. No model training required. Developers create a resource, obtain an endpoint and subscription key, and call the REST API with input data to receive AI-powered results.

**Subscription Key**
The authentication credential required for every Azure Cognitive Services API call. Passed in the Ocp-Apim-Subscription-Key HTTP header.

**Endpoint URL**
The HTTPS URL of a Cognitive Services resource, specific to the Azure region where the resource was provisioned. Every API call targets this URL.

**Multi-service Resource**
A single Azure Cognitive Services resource that provides access to multiple AI services under one endpoint and key, simplifying credential management for multi-capability applications.

**Pricing Tier**
The service tier selected at provisioning. Most Cognitive Services offer a Free tier (F0) with limited monthly transactions and one or more standard tiers (S0, S1) for higher volume. AI-900 labs typically use the Free tier.

**Azure Computer Vision**
Prebuilt vision analysis service. Capabilities: image tagging, object detection, image captioning, OCR (Read API), smart crop, and content moderation flags.

**Azure Custom Vision**
Vision service for training custom image classifiers and object detectors using labeled images. Uses transfer learning; minimum 15 images per class for classification.

**Azure Face API**
Vision service for face detection (locate faces, return attributes) and face verification (1:1 identity comparison). Face identification (1:N) requires gated access.

**Azure Form Recognizer / Document Intelligence**
Applied AI service for extracting structured field data from documents: receipts, invoices, business cards, and custom form types.

**Azure Speech Service**
Service providing speech-to-text (ASR), text-to-speech (TTS), speech translation, and speaker recognition under a single service endpoint.

**Neural TTS**
Deep learning-based text-to-speech synthesis producing human-like voices. Azure offers 400+ neural voices across 140+ languages.

**Custom Speech**
An Azure Speech Service capability for adapting the speech recognition model to custom vocabulary (domain terminology, product names, proper nouns).

**Custom Neural Voice**
A gated Azure Speech capability for creating a custom TTS voice from a licensed voice actor's recordings. Requires Microsoft approval due to deepfake risk.

**Azure Language Service**
The consolidated Azure text analysis service. Provides prebuilt capabilities (sentiment, NER, key phrase, language detection, PII detection) and custom capabilities (custom text classification, custom NER, custom question answering, CLU).

**Conversational Language Understanding (CLU)**
The Azure Language Service capability for intent recognition and entity extraction in conversational applications. The functional successor to LUIS.

**Azure Translator**
A separate Azure Cognitive Service for text translation (100+ languages), document translation, and transliteration.

**Azure Anomaly Detector**
A Decision Cognitive Service that detects anomalies in time series data without custom training. Returns anomaly flags, trend direction, and seasonality.

**Azure Personalizer**
A Decision Cognitive Service that uses reinforcement learning to rank content items and recommend the best action for a given user context.

**Azure Content Safety**
A Cognitive Service that detects harmful content (hate speech, violence, sexual content, self-harm) in text and images, providing severity scores for each category.

---

## Section 2: Master Service-to-Task Mapping Table

This is the highest-priority table for AI-900 exam preparation. Memorize every row.

### Table 1: Azure Cognitive Services — Complete Task Reference

| Task | Specific Capability | Azure Service | Training Required |
|---|---|---|---|
| Describe what is in an image (tags, objects, caption) | Image analysis | Azure Computer Vision | No |
| Extract printed/handwritten text from images | OCR / Read API | Azure Computer Vision | No |
| Classify images into custom categories | Custom image classification | Azure Custom Vision | Yes |
| Detect custom objects in images with bounding boxes | Custom object detection | Azure Custom Vision | Yes |
| Detect human faces in an image | Face detection | Azure Face API | No |
| Compare two faces to determine if same person | Face verification | Azure Face API | No |
| Identify a person from a database of known faces | Face identification | Azure Face API | Yes + gated access |
| Extract structured fields from invoices, receipts, forms | Document field extraction | Azure Form Recognizer | No (prebuilt) / Yes (custom) |
| Convert spoken audio to text | Speech-to-Text (ASR) | Azure Speech Service | No |
| Convert text to spoken audio | Text-to-Speech (TTS) | Azure Speech Service | No |
| Translate spoken language in real time | Speech Translation | Azure Speech Service | No |
| Identify speaker by voice | Speaker Recognition | Azure Speech Service | No |
| Determine emotional tone of text | Sentiment Analysis | Azure Language Service | No |
| Identify important topics in text | Key Phrase Extraction | Azure Language Service | No |
| Identify people, orgs, locations, dates in text | Named Entity Recognition | Azure Language Service | No |
| Identify what language text is written in | Language Detection | Azure Language Service | No |
| Detect and redact personally identifiable information | PII Detection | Azure Language Service | No |
| Classify text into custom category labels | Custom Text Classification | Azure Language Service | Yes |
| Extract custom domain entities from text | Custom NER | Azure Language Service | Yes |
| Build an FAQ bot from existing documents | Custom Question Answering | Azure Language Service | Yes (FAQ docs) |
| Recognize user intent in conversation | Conversational Language Understanding (CLU) | Azure Language Service | Yes |
| Translate text between 100+ languages | Text Translation | Azure Translator | No |
| Detect anomalies in time series data | Anomaly Detection | Azure Anomaly Detector | No |
| Rank content to personalize user experience | Content Personalization | Azure Personalizer | No (learns from rewards) |
| Filter harmful content from text and images | Content Moderation | Azure Content Safety | No |

---

## Section 3: Service Provisioning Pattern

All Azure Cognitive Services follow the same provisioning and calling pattern.

**Creating a resource:**

In the Azure portal, search for the service name (e.g., "Language," "Computer Vision," "Speech"). Select Create. Choose:

- Subscription: your Azure subscription
- Resource group: a logical container for related Azure resources
- Region: the Azure data center location (choose one near your users for lower latency)
- Name: a unique resource name
- Pricing tier: F0 (free) or S0 (standard)

**Getting credentials:**

After deployment, navigate to the resource's "Keys and Endpoint" section. Copy:

- Key 1 (or Key 2): subscription key for API authentication
- Endpoint: the base URL for API calls

**Calling the API:**

Every API call is an HTTPS POST request. The request includes:

- URL: endpoint + capability-specific path (e.g., /language/:analyze-text?api-version=2023-04-01)
- Header: Ocp-Apim-Subscription-Key with your subscription key
- Header: Content-Type: application/json
- Body: JSON payload with your input text, image URL, or audio parameters

**Parsing the response:**

The response is JSON. Structure varies by service but always includes the analysis result and confidence information.

---

## Section 4: Comparison Tables

### Table 2: Azure Vision Services Compared

| Dimension | Azure Computer Vision | Azure Custom Vision | Azure Face API | Azure Form Recognizer |
|---|---|---|---|---|
| Training required | No | Yes | No | No (prebuilt) / Yes (custom) |
| Input | Image URL or binary | Labeled images (training) | Image URL or binary | Document URL or binary |
| Output | Tags, objects, caption, OCR text | Classification labels or bounding boxes | Face bounding boxes, attributes, verification result | Extracted field key-value pairs |
| Minimum images | N/A | 15 per class (classification) | N/A | N/A |
| Responsible AI note | Content filters available | Dataset bias risk | Face ID gated | PII data handling required |

### Table 3: Azure Speech Service Capabilities

| Capability | Input | Output | Custom Model Available |
|---|---|---|---|
| Speech-to-Text | Audio stream or file | Text transcript with timestamps | Yes (Custom Speech) |
| Text-to-Speech | Text string | Audio stream | Yes (Custom Neural Voice — gated) |
| Speech Translation | Audio stream in source language | Text or audio in target language | No |
| Speaker Verification | Audio + claimed speaker identity | Match/no-match with confidence | No |
| Speaker Identification | Audio + list of known speakers | Identified speaker | No |

### Table 4: Azure Language Service — Prebuilt vs Custom

| Capability | Type | Training Data Required | Use When |
|---|---|---|---|
| Sentiment Analysis | Prebuilt | No | Standard positive/negative/neutral classification |
| Key Phrase Extraction | Prebuilt | No | Extract main topics from documents |
| Named Entity Recognition | Prebuilt | No | Extract people, orgs, locations, dates |
| Language Detection | Prebuilt | No | Identify document language |
| PII Detection | Prebuilt | No | Detect and optionally redact personal data |
| Custom Text Classification | Custom | Yes (labeled documents) | Domain-specific categories |
| Custom NER | Custom | Yes (labeled entities) | Domain-specific entity types |
| Custom Question Answering | Custom | Yes (FAQ documents) | FAQ bot from existing documents |
| CLU | Custom | Yes (labeled utterances) | Intent recognition for conversation |

---

## Section 5: AI-900 Exam Tips

1. The most frequently missed AI-900 question type involves confusing Azure Language Service with Azure Translator. Language Service analyzes text (sentiment, NER, etc.). Translator converts text between languages. These are different services at different endpoints.

2. Custom Voice (Text-to-Speech) requires gated access because custom voice cloning can be used to impersonate individuals. Know that both Face Identification and Custom Neural Voice are gated capabilities with responsible AI justification.

3. Azure Anomaly Detector does not require labeled anomaly examples. It learns the normal pattern from the time series you provide and flags deviations. This makes it unsupervised anomaly detection via API.

4. The Read API is the OCR component of Azure Computer Vision. When a scenario involves extracting text from photographs or mixed-layout images, the answer is Azure Computer Vision Read API — not Form Recognizer (which is for structured forms and documents).

5. Azure Personalizer uses reinforcement learning. It is the only Cognitive Service that uses RL. When a scenario mentions "recommend content," "personalize feed," or "learn from user clicks," Personalizer is the answer.

6. CLU (Conversational Language Understanding) and LUIS serve the same purpose: intent recognition in conversational AI. On AI-900 questions, treat them as equivalent. CLU is the newer name; LUIS is the legacy name.

7. Multi-service resources provide one endpoint and key for multiple services. This is useful for applications that use Computer Vision and Language Service together — one resource instead of two.

8. All Cognitive Services support the Free tier (F0) for development and testing. This is important for the AI-900 exam scenarios that ask how to minimize cost during proof-of-concept phases.

---

## Section 6: Required Reading

**Microsoft Learn — Azure AI Services overview**
learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services

Provides the authoritative catalog of all Azure AI services including names, capabilities, and links to documentation.

**Microsoft Learn — Analyze images with Azure AI Vision**
learn.microsoft.com/en-us/training/modules/analyze-images-computer-vision/

**Microsoft Learn — Recognize and synthesize speech**
learn.microsoft.com/en-us/training/modules/recognize-synthesize-speech/

Covers Azure Speech Service speech-to-text and text-to-speech with hands-on exercises.

**Microsoft Learn — Analyze text with Azure AI Language**
learn.microsoft.com/en-us/training/modules/analyze-text-with-text-analytics-service/

---

## Section 7: Study Checklist

- [ ] Complete Table 1 from memory: write the correct Azure service for each of the 25 listed tasks without looking.
- [ ] Explain the difference between Azure Language Service and Azure Translator in one sentence each.
- [ ] Explain why Face Identification and Custom Neural Voice require gated access.
- [ ] Describe the four steps to provision and call any Cognitive Service.
- [ ] Complete the Microsoft Learn module: Recognize and synthesize speech.
- [ ] Complete the Microsoft Learn module: Analyze images with Azure AI Vision.
- [ ] Review all eight AI-900 exam tips in Section 5.
- [ ] Complete the Module 07 quiz.
- [ ] Complete the Module 07 lab.
- [ ] Post initial discussion by Wednesday 11:59 PM and respond to two peers by Sunday 11:59 PM.

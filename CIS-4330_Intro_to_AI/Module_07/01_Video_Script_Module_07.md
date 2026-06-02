# Video Script: Module 07 - Azure Cognitive Services: Vision, Speech, and Language

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AI-900 Domain:** All five domains — Cognitive Services span vision, NLP, speech, and conversational AI

---

## [00:00 - 01:30] Opening

Welcome back. Professor Nash here, and this is Module 07. We have covered computer vision conceptually in Module 06 and NLP fundamentals in Module 05. Today we zoom in on the Azure Cognitive Services portfolio — the specific prebuilt services Microsoft provides for vision, speech, and language workloads. This module is one of the most directly exam-applicable in the course. AI-900 questions about Cognitive Services are numerous and specific, so your goal for this module is to have a precise mental map of what each service does and when to use it. Let us build that map.

---

## [01:30 - 05:00] What Are Azure Cognitive Services?

Azure Cognitive Services is Microsoft's family of prebuilt AI APIs. The defining characteristic: you do not need to train a model. You create an Azure resource, get an API key, and call the REST endpoint with your data. Azure does the AI work on Microsoft's infrastructure, returning structured results.

Cognitive Services is organized into five categories:

- Vision: analyzing images and video
- Speech: processing and generating spoken audio
- Language: understanding and generating text
- Decision: making personalized recommendations and detecting anomalies
- Azure OpenAI Service: accessing large language models including GPT-4

Each service has a distinct endpoint and pricing model. For AI-900, you need to know which service to select for a given business scenario.

Cognitive Services follows a common consumption pattern. You create a Cognitive Services resource (or a multi-service resource) in the Azure portal. Every API call requires two headers: the API endpoint URL and the subscription key. You send your input data — an image, audio bytes, or text — in the request body. The service returns JSON.

You can also create a single multi-service Cognitive Services resource that provides access to multiple services under one endpoint and key. This simplifies management when an application uses multiple AI capabilities.

---

## [05:00 - 09:30] Azure Vision Services in Depth

[SHOW DIAGRAM: Four boxes in a row: "Azure Computer Vision," "Azure Custom Vision," "Azure Face API," "Azure Form Recognizer." Under each box, two to three bullet points listing primary capabilities.]

I covered these services at a high level in Module 06. Now let me be more specific, because the AI-900 exam tests fine-grained distinctions between them.

**Azure Computer Vision** analyzes images to produce:

- Image tags: nouns describing what is present (e.g., "outdoor," "tree," "person," "car").
- Object detection results: bounding boxes with class labels and confidence scores.
- Image descriptions: natural language captions generated automatically.
- The Read API: OCR for printed and handwritten text in images and PDFs.
- Smart crop suggestions: identifies the most visually interesting region for thumbnail generation.
- Content moderation flags: adult content and violence likelihood scores.

Key API call: POST to the /analyze endpoint with the image URL or binary and a list of visual features to extract.

**Azure Custom Vision** is the training platform for custom image classifiers and object detectors. Unlike Computer Vision, you bring your own labeled images. The service handles transfer learning internally. You interact through the Custom Vision portal or SDK to upload images, add tags, train, evaluate, and publish.

**Azure Face API** — the two capabilities you must know for AI-900:

- Face detection: locate faces in an image, return bounding boxes and attributes.
- Face verification: compare two face images, return "identical" or "not identical" with a confidence score.

Face identification (1:N matching against a stored person group) is a gated capability requiring Microsoft approval.

**Azure Form Recognizer (Document Intelligence)** uses prebuilt models for receipts, invoices, business cards, and identity documents — each model is purpose-built to find standard fields in standard document layouts. The custom model lets you define fields in your own document types and train with your own examples.

---

## [09:30 - 13:00] Azure Speech Services in Depth

[SHOW DIAGRAM: Azure Speech Service with four capability boxes: "Speech-to-Text," "Text-to-Speech," "Speech Translation," "Speaker Recognition." Arrows from left show input types: audio stream, text, audio stream. Arrows on right show output types: transcript, audio, translated transcript, identity.]

Azure Speech Service consolidates all speech AI capabilities under one service. The four capabilities:

**Speech-to-Text (Automatic Speech Recognition, ASR):** Converts audio to text in real time or batch mode. Supports over 100 languages. Custom Speech lets you adapt the model to your domain's vocabulary — medical terminology, product names, or industry jargon — using custom acoustic and language models. The transcription endpoint accepts an audio stream and returns a transcript with word-level timestamps.

**Text-to-Speech (Speech Synthesis):** Converts text to natural-sounding spoken audio. Azure provides over 400 neural voices across 140+ languages. Neural voices — called Neural TTS — use deep learning to produce human-like prosody, intonation, and breathing. You can also create a Custom Neural Voice by recording a consenting voice actor and fine-tuning the model. Custom Neural Voice requires Microsoft approval due to deepfake and identity misuse concerns.

**Speech Translation:** Real-time translation of spoken audio from one language to another, outputting either translated text or synthesized translated speech. Supports 30+ source languages. Used for live meeting translation and multilingual customer service.

**Speaker Recognition:** Identifies who is speaking based on voice characteristics. Speaker verification confirms the speaker is who they claim to be (1:1). Speaker identification determines which of a set of known speakers is currently speaking (1:N).

---

## [13:00 - 17:00] Azure Language Services in Depth

[SHOW DIAGRAM: Azure Language Service with capability boxes: "Sentiment Analysis," "Key Phrase Extraction," "NER," "Language Detection," "Custom Text Classification," "Custom QA," "CLU." Additional separate boxes for "Azure Translator" and "LUIS."]

Azure Language Service provides the full portfolio of text analysis capabilities. Let me clarify the organization, because Microsoft has consolidated several previously separate services.

Azure Language Service (formerly Azure Text Analytics plus Language Understanding consolidation) includes:

- Prebuilt text analysis: sentiment analysis, key phrase extraction, named entity recognition, language detection, PII detection and redaction, linked entity recognition, and opinion mining.
- Custom capabilities: custom text classification (single-label and multi-label), custom NER with your own entity types, and custom question answering.
- Conversational Language Understanding (CLU): the successor to LUIS for building intent recognition models for conversational applications.

**Azure Translator** is a separate service from Language Service. It handles text translation (100+ languages), document translation, and transliteration. The Translator API is distinct from Language Service — you call it at a different endpoint with different input parameters.

**Language Understanding (LUIS)** was the original intent recognition service. Microsoft is transitioning LUIS to Conversational Language Understanding (CLU) within Language Service. For AI-900 purposes, LUIS and CLU represent the same capability: recognize the intent and entities in a natural language utterance.

Key AI-900 distinction: Language Service is for analyzing or classifying existing text. CLU / LUIS is for understanding what a user wants in a conversational context.

---

## [17:00 - 19:30] Azure Decision Services

The Decision category of Cognitive Services covers two services worth knowing for AI-900.

**Azure Anomaly Detector** is a prebuilt API for detecting anomalies in time series data. You send it a time series (sequences of timestamps and values) and it returns which data points are anomalies, whether the series shows an upward or downward trend, and seasonal patterns. No custom training is required — Anomaly Detector learns the normal distribution from the time series you provide. Use cases: server performance monitoring, sales anomalies, IoT sensor fault detection.

**Azure Personalizer** uses reinforcement learning to recommend the best content item (article, product, promotion) to show a specific user at a specific moment. You send a context (user attributes, time of day, device type) and a list of actions (articles, products), and Personalizer returns the ranked action. The service learns from reward signals you provide: did the user click? Did they convert? Over time it learns which actions work for which contexts.

---

## [19:30 - 21:30] Provisioning and Calling Cognitive Services

Every Azure Cognitive Service follows the same provisioning and calling pattern. Understanding this pattern is important for the AI-900 exam.

**Step 1 — Create a resource:** In the Azure portal, create a resource for the specific service (e.g., "Language" resource) or a multi-service "Cognitive Services" resource. Select a region, pricing tier (Free tier available for most services), and resource name.

**Step 2 — Get the endpoint and key:** Every resource has an endpoint URL and one or more subscription keys. These credentials authenticate every API call.

**Step 3 — Call the API:** Send an HTTP POST request to the service endpoint with the subscription key in the Ocp-Apim-Subscription-Key header and your data in the request body as JSON. Most services accept both image URLs and base64-encoded binary data.

**Step 4 — Process the response:** Parse the JSON response. Most responses include the analysis results, confidence scores, and metadata about the request.

For AI-900, the key pattern is: every Cognitive Service requires a resource endpoint and a subscription key. All calls are HTTPS REST API calls. No framework or SDK is required — a simple HTTP client works.

---

## [21:30 - 23:00] Module Summary and Lab Preview

Let me summarize Module 07.

Azure Cognitive Services are prebuilt AI APIs requiring no model training. Vision services: Computer Vision (prebuilt analysis), Custom Vision (custom classifier/detector), Face API (face detection and verification), Form Recognizer (document extraction). Speech services: Speech-to-Text, Text-to-Speech, Speech Translation, Speaker Recognition — all under Azure Speech Service. Language services: Language Service (text analysis and CLU), Azure Translator (translation).

Decision services: Anomaly Detector (time series anomaly detection) and Personalizer (reinforcement learning-based recommendations).

All services follow the same provisioning pattern: create resource, get endpoint and key, call REST API, parse JSON response.

In this week's lab, you will practice service selection — reading scenarios and identifying the exact Cognitive Service and capability to use. You will also work with sample API responses to practice interpreting structured JSON output from multiple services.

See you in Module 08, where we go into Azure Machine Learning Studio in detail.

---

## References

- Microsoft Learn — Azure AI Services overview: learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services
- Microsoft Learn — Explore Azure AI Services for Vision: learn.microsoft.com/en-us/training/modules/explore-cognitive-services-vision/
- Microsoft Learn — Explore Azure AI Services for Language: learn.microsoft.com/en-us/training/modules/explore-analyze-text-with-text-analytics-service/

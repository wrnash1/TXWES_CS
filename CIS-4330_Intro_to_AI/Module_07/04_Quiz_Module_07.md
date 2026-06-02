# Quiz: Module 07 - Azure Cognitive Services: Vision, Speech, and Language

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** All five workload domains
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A company wants to add automatic image captioning to their photo sharing platform. They need the service to describe what is happening in each photo in a natural English sentence. No custom training data is available. Which Azure service should they use?

- A) Azure Custom Vision
- B) Azure Computer Vision
- C) Azure Face API
- D) Azure Form Recognizer

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Computer Vision is a prebuilt service that generates natural language image descriptions (captions) without custom training. This is one of its core capabilities.
- *Why A is incorrect:* Azure Custom Vision requires labeled training images and produces classification labels or bounding boxes — not natural language captions.
- *Why C is incorrect:* Azure Face API is specifically for face detection and verification. It does not describe scene content.
- *Why D is incorrect:* Azure Form Recognizer (Document Intelligence) extracts structured field data from documents. It is not designed for natural language image captioning.

---

## Question 2

A podcast network wants to enable search of all episode content by keyword. To do this, they need to convert all audio episodes into searchable text transcripts. Which Azure service and capability is most appropriate?

- A) Azure Language Service — Key Phrase Extraction
- B) Azure Translator — Text Translation
- C) Azure Speech Service — Speech-to-Text
- D) Azure Language Service — Named Entity Recognition

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Speech-to-Text (ASR) converts audio to text transcripts. Azure Speech Service supports batch transcription of audio files with high accuracy across 100+ languages.
- *Why A is incorrect:* Key phrase extraction operates on text documents, not audio. It extracts topics from existing text; it cannot convert audio to text.
- *Why B is incorrect:* Azure Translator converts text between languages. It cannot process audio input.
- *Why D is incorrect:* NER extracts entities from existing text. It requires text as input, not audio.

---

## Question 3

A developer needs to use both Azure Computer Vision and Azure Language Service in the same web application. To simplify credential management, they want a single endpoint and subscription key for both services. What should they create in the Azure portal?

- A) Two separate service-specific resources, one for each service
- B) A multi-service Azure Cognitive Services resource
- C) An Azure Machine Learning workspace
- D) A virtual machine with both SDKs installed

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A multi-service Cognitive Services resource provides a single endpoint and one or two subscription keys that authenticate calls to multiple Azure AI services, simplifying application credential management.
- *Why A is incorrect:* Two separate resources require managing two sets of endpoints and keys. The scenario specifically asks for a single credential set.
- *Why C is incorrect:* Azure ML workspace is for training and deploying custom models. It does not host prebuilt Cognitive Services under a shared key.
- *Why D is incorrect:* Credential management does not require a virtual machine. Cognitive Services are cloud APIs accessed over HTTPS.

---

## Question 4

A global e-commerce platform wants to convert its English-language product listings into 30 other languages automatically. Which Azure service should they use?

- A) Azure Language Service — Custom Text Classification
- B) Azure Translator
- C) Azure Language Service — Language Detection
- D) Azure Speech Service — Speech Translation

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Translator is the dedicated Azure service for text translation across 100+ languages. It is a separate service from Azure Language Service, specifically designed for this use case.
- *Why A is incorrect:* Custom Text Classification assigns category labels to documents. It does not translate text between languages.
- *Why C is incorrect:* Language Detection identifies what language text is written in. It does not translate text.
- *Why D is incorrect:* Speech Translation converts spoken audio from one language to another. This scenario involves translating written text, not audio.

---

## Question 5

A streaming music service wants to personalize which songs appear at the top of each user's home screen. The system should learn over time which songs convert each user type from browsing to listening based on implicit feedback. Which Azure Cognitive Service is designed for this?

- A) Azure Anomaly Detector
- B) Azure Personalizer
- C) Azure Language Service — Sentiment Analysis
- D) Azure Custom Vision

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Personalizer is a Decision service that uses reinforcement learning to rank actions (songs) based on context (user profile, time of day) and learns from reward signals (did the user listen?).
- *Why A is incorrect:* Anomaly Detector identifies unusual patterns in time series data. It does not personalize content recommendations.
- *Why C is incorrect:* Sentiment analysis determines emotional tone of text. It does not rank or recommend content.
- *Why D is incorrect:* Custom Vision is for image classification and object detection. It does not handle content recommendation.

---

## Question 6

A developer calls the Azure Language Service API and receives HTTP 401 Unauthorized. What is the most likely cause?

- A) The sentiment analysis model is currently retraining.
- B) The API request was sent to the wrong HTTP method (GET instead of POST).
- C) The subscription key is missing or incorrect in the API request header.
- D) The text input contains characters that are not supported by the model.

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* HTTP 401 Unauthorized in Azure Cognitive Services means authentication failed. The most common cause is a missing, expired, or incorrectly formatted subscription key in the Ocp-Apim-Subscription-Key header.
- *Why A is incorrect:* Model retraining does not produce a 401 error. Service unavailability during retraining would produce a 503 error.
- *Why B is incorrect:* An incorrect HTTP method would return 405 Method Not Allowed, not 401.
- *Why D is incorrect:* Unsupported characters would typically result in a 400 Bad Request error or be silently handled, not a 401 authentication error.

---

## Question 7

Microsoft requires customers to apply for access before using the face identification capability of Azure Face API (1:N matching). Which responsible AI concern most directly motivated this restriction?

- A) Face identification is technically unstable and frequently returns errors.
- B) Face identification enables mass surveillance with potential for discriminatory outcomes and privacy violations.
- C) Face identification requires too much compute for the standard pricing tier.
- D) Face identification is only accurate for celebrity faces and fails on ordinary individuals.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Real-time identification of individuals from a database in public spaces enables surveillance systems that can be misused. Research also shows higher error rates for certain demographic groups (darker-skinned, female), creating discrimination risks. Microsoft explicitly cites these concerns in its responsible AI principles.
- *Why A is incorrect:* Technical instability is not the reason for gating. The capability works; the concern is its potential for misuse.
- *Why C is incorrect:* Compute cost does not require gated access — standard pricing tiers handle the compute. Gating is motivated by ethics, not infrastructure.
- *Why D is incorrect:* This is factually incorrect and is not the basis for Microsoft's access restriction.

---

## Question 8

A company needs to extract the total amount, invoice date, vendor name, and line items from thousands of scanned invoice PDF files to automate accounts payable. Which Azure service is specifically designed for this?

- A) Azure Computer Vision (Read API)
- B) Azure Language Service (Named Entity Recognition)
- C) Azure Form Recognizer (Document Intelligence) with the prebuilt invoice model
- D) Azure Custom Vision (object detection)

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Form Recognizer's prebuilt invoice model is specifically trained to extract standard invoice fields (vendor, date, total, line items) from scanned invoice documents, returning structured key-value pairs. This is exactly the described use case.
- *Why A is incorrect:* Azure Computer Vision Read API extracts raw text from images but does not understand document structure or map values to named invoice fields.
- *Why B is incorrect:* NER extracts general entity categories (organizations, dates, monetary values) but does not map them to specific invoice fields or handle tabular line items.
- *Why D is incorrect:* Custom Vision performs image classification or object detection with bounding boxes. It does not extract structured text data from documents.

---

## Question 9

An organization builds a customer service chatbot that asks "How can I help you today?" and needs to understand responses such as "I want to cancel my subscription" and "Help me upgrade my plan." The system must identify the customer's goal and any relevant details. Which Azure service capability is designed for this?

- A) Azure Language Service — Sentiment Analysis
- B) Azure Language Service — Key Phrase Extraction
- C) Azure Language Service — Conversational Language Understanding (CLU)
- D) Azure Computer Vision — Image Analysis

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* CLU (Conversational Language Understanding) is designed to recognize the intent (CancelSubscription, UpgradePlan) and entities in natural language utterances. It is the correct capability for conversational AI applications.
- *Why A is incorrect:* Sentiment analysis determines emotional tone. It cannot identify that "I want to cancel my subscription" expresses a cancellation intent vs. a service request.
- *Why B is incorrect:* Key phrase extraction identifies important topics but cannot map them to actionable intents or extract structured entities for system actions.
- *Why D is incorrect:* Image analysis processes images. Customer service chatbot requests are text utterances, not images.

---

## Question 10

Azure Anomaly Detector is used to monitor daily sales data for a retail chain. The service flags sales on December 25 as anomalous because the volume is significantly higher than typical days. Is this an appropriate use of Anomaly Detector, and what setting should the team consider adjusting?

- A) Yes, it is appropriate. Anomaly Detector cannot be adjusted for expected seasonal events.
- B) No, Anomaly Detector only works on financial data and should not be applied to retail sales.
- C) Yes, but the team should review whether the service's seasonality settings account for known recurring holiday peaks to avoid flagging expected spikes as anomalies.
- D) No, Anomaly Detector requires labeled anomaly examples and has no knowledge of holidays.

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Anomaly Detector has seasonality detection capabilities that can model recurring patterns. However, if the model has not been given sufficient historical data to learn holiday patterns, expected annual peaks may be flagged incorrectly. The team should provide multiple years of historical data and review the service's sensitivity and seasonality parameters.
- *Why A is incorrect:* Anomaly Detector does have parameters and seasonality modeling. It can be configured to reduce false positives from known seasonal patterns with sufficient historical data.
- *Why B is incorrect:* Anomaly Detector works on any numerical time series — not only financial data. It has no data type restrictions.
- *Why D is incorrect:* Anomaly Detector is unsupervised — it does not require labeled anomaly examples. It learns normal patterns from the provided time series.

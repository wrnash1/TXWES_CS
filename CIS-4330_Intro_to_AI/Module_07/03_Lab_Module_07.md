# Lab Activity: Module 07 - Azure Cognitive Services: Vision, Speech, and Language

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** All five workload domains
**Points:** 100
**Submission:** Canvas LMS — Module 07 Lab Assignment

---

## Objectives

By the end of this lab, you will be able to:

- Select the correct Azure Cognitive Service and specific capability for a given business scenario.
- Distinguish between services that require custom training and those that are prebuilt.
- Interpret structured JSON output from multiple Azure Cognitive Services.
- Explain the provisioning steps required to deploy any Cognitive Service.
- Apply responsible AI reasoning to gated service access decisions.

---

## Prerequisites

No Azure subscription is required. All exercises are service selection, interpretation, and analysis tasks. You will need:

- Module 07 video lecture (completed).
- Module 07 reading guide (completed), especially Table 1 (master service-to-task mapping).

---

## Part A: Service Selection (40 points)

For each scenario, identify the specific Azure Cognitive Service AND the specific capability within that service. Then indicate whether custom training is required.

Use the exact service names and capability names from Table 1 in the reading guide.

Format your answer as:

- Service: ________________
- Capability: ________________
- Custom training required: Yes / No

### Scenario 1

A radio station wants to automatically generate transcripts of all broadcast episodes for posting on their website. Audio files are uploaded in MP3 format after each episode.

### Scenario 2

A bank wants to detect unusual spikes or drops in its daily transaction volume over the past 18 months to identify potential fraud windows or system outages.

### Scenario 3

An accessibility nonprofit wants to add a feature to their mobile app that reads aloud the text in any photograph a user points their phone at — street signs, restaurant menus, product labels.

### Scenario 4

A legal services firm wants to automatically remove all names, addresses, phone numbers, and social security numbers from client documents before sharing them with third-party analysts.

### Scenario 5

A hardware retailer wants to build a smart mirror in their bathroom showroom. When a customer says "I want to see the blue granite countertop option," the mirror's AI recognizes the intent (view product option) and the entity (product = blue granite countertop) to display the correct product image.

### Scenario 6

A news aggregation startup wants to determine the language of each article it ingests — whether it is English, Spanish, French, Mandarin, or one of 70+ other languages — to route articles to the correct editorial team.

### Scenario 7

A food delivery platform wants to personalize which promotional banners each user sees on the app home screen based on their order history, time of day, and location, learning over time which promotions convert best for each user type.

### Scenario 8

A children's educational app needs a character with a custom voice that sounds like the company's mascot. They have recordings of a voice actor performing in that character's style.

### Scenario 9

A customs agency receives thousands of invoices per day from importers. Each invoice contains vendor name, shipment date, cargo description, and declared value. The agency needs to extract these fields automatically from scanned invoice PDFs.

### Scenario 10

An insurance company receives photos of accident scenes. They want to automatically identify and locate all vehicles, pedestrians, and road signs in each photo to assist claims adjusters.

---

## Part B: Prebuilt vs Custom Training (20 points)

For each scenario, write "Prebuilt" or "Custom Training Required" and provide a two-sentence justification explaining why.

### Scenario 11

A global corporation wants to analyze 200,000 English customer emails for sentiment to understand overall satisfaction trends. The sentiment categories are standard: positive, negative, neutral.

### Scenario 12

A pharmaceutical company wants to extract drug names, clinical trial IDs, and patient dosage levels from unstructured clinical notes. These entity types are not in the standard NER model.

### Scenario 13

A logistics company wants to extract vendor name, total amount, and delivery date from standard commercial invoices using Azure Form Recognizer.

### Scenario 14

A restaurant chain wants to build a voice assistant that responds to orders: "I'd like a large pepperoni pizza with extra cheese for pickup." The system needs to recognize the ordering intent and extract pizza type, size, toppings, and fulfillment method.

### Scenario 15

A city government wants to detect anomalous water usage readings from smart meters to identify potential pipe leaks. They have two years of daily meter readings but no labeled examples of leak events.

---

## Part C: Interpreting Multi-Service Output (25 points)

Read the following scenario and JSON output fragments, then answer the questions.

A customer service platform uses three Azure Cognitive Services in sequence:

Step 1 — Azure Speech Service transcribes the customer's audio call.
Step 2 — Azure Language Service analyzes the transcript.
Step 3 — Azure Language Understanding (CLU) identifies the customer's intent.

The following outputs were produced for one call:

Speech-to-Text output:

```json
{
  "transcript": "I've been waiting three weeks for my order and nobody has called me back. I want a full refund immediately.",
  "confidence": 0.961
}
```

Language Service — Sentiment output:

```json
{
  "sentiment": "negative",
  "confidenceScores": {"positive": 0.02, "neutral": 0.04, "negative": 0.94}
}
```

Language Service — NER output:

```json
{
  "entities": [
    {"text": "three weeks", "category": "Quantity", "subcategory": "Duration", "score": 0.99},
    {"text": "full refund", "category": "Product", "score": 0.71}
  ]
}
```

CLU output:

```json
{
  "topIntent": "RequestRefund",
  "confidence": 0.912,
  "entities": [
    {"category": "RefundType", "text": "full refund", "confidence": 0.88}
  ]
}
```

### Question 16 (7 points)

The platform automatically routes calls with negative sentiment above 0.85 and a "RequestRefund" intent above 0.80 to a senior customer service agent. Does this call meet the escalation criteria? Show your reasoning by referencing specific values from the JSON outputs.

Your answer: ________________

### Question 17 (8 points)

NER identified "full refund" with category "Product" and confidence 0.71. CLU also extracted "full refund" as a "RefundType" entity with confidence 0.88. Explain the conceptual difference between what NER and CLU are doing with the same text. Which output is more useful for routing this call to the refund processing team and why?

Your answer: ________________

### Question 18 (10 points)

Design a business rule system that uses the three services' outputs together to automate routing decisions. Propose at least three routing scenarios based on combinations of sentiment, intent, and entity values. For each scenario, describe the input combination and the automated action.

Your answer: ________________

---

## Part D: Service Provisioning Knowledge (15 points)

Answer each question in two to three complete sentences.

### Question 19 (5 points)

A developer needs to use both Azure Computer Vision and Azure Language Service in the same application. They want to manage one set of credentials rather than two separate sets. What Azure resource type should they create, and what is the benefit?

Your answer: ________________

### Question 20 (5 points)

A team is building a proof-of-concept using Azure Speech Service and wants to keep costs near zero during development. What pricing tier should they select, and what limitation should they be aware of?

Your answer: ________________

### Question 21 (5 points)

A developer calls the Azure Language Service sentiment analysis API and receives a 401 Unauthorized error. What is the most likely cause of this error, and how is it resolved?

Your answer: ________________

---

## Answer Key and Grading Rubric

### Part A (4 points per scenario = 40 points)

Scoring: 4 pts = correct service, correct capability, correct custom training indicator. 2 pts = correct service with wrong capability. 0 pts = incorrect service.

Scenario 1: Azure Speech Service / Speech-to-Text (ASR). No custom training.

Scenario 2: Azure Anomaly Detector / Anomaly Detection (time series). No custom training.

Scenario 3: Azure Computer Vision / OCR Read API. No custom training.

Scenario 4: Azure Language Service / PII Detection. No custom training.

Scenario 5: Azure Language Service / Conversational Language Understanding (CLU). Yes, custom training required.

Scenario 6: Azure Language Service / Language Detection. No custom training.

Scenario 7: Azure Personalizer / Content Personalization. No (learns from user interaction rewards).

Scenario 8: Azure Speech Service / Custom Neural Voice (Text-to-Speech). Yes, custom training required + gated access.

Scenario 9: Azure Form Recognizer / Prebuilt Invoice model (Document Intelligence). No custom training.

Scenario 10: Azure Computer Vision / Object Detection. No custom training.

### Part B (4 points per scenario = 20 points)

Scenario 11: Prebuilt. Standard English sentiment analysis is covered by the prebuilt Language Service capability.

Scenario 12: Custom Training Required. Domain-specific entities (drug names, trial IDs, dosage) are not in the standard NER model.

Scenario 13: Prebuilt. Azure Form Recognizer includes a prebuilt invoice model that handles standard commercial invoice fields.

Scenario 14: Custom Training Required. CLU intent recognition requires defining intents, labeling example utterances, and training the model on restaurant-ordering vocabulary.

Scenario 15: Prebuilt. Azure Anomaly Detector learns normal patterns from historical data without labeled anomaly examples.

### Part C (25 points)

Q16: Yes — sentiment is negative at 0.94 (exceeds 0.85 threshold) AND RequestRefund intent confidence is 0.912 (exceeds 0.80 threshold). Both criteria are met; the call should be routed to a senior agent.

Q17: NER identifies the text "full refund" as a general named entity and tries to fit it into a standard category (Product in this case, which is incorrect). CLU extracts "full refund" as the RefundType entity within the specific intent context — this is semantically correct for the business use case. CLU output is more useful because it correctly categorizes the entity within the conversation's purpose, enabling automated routing to the refund team.

Q18: Full credit requires three distinct routing scenarios with specific threshold values from the outputs. Examples: (1) Negative sentiment > 0.85 + RequestRefund > 0.80 → senior agent queue. (2) Negative sentiment > 0.70 + any "Request" intent → standard escalation queue. (3) Positive sentiment > 0.70 + any intent → automated resolution with satisfaction survey sent.

### Part D (5 points each = 15 points)

Q19: Create a multi-service Cognitive Services resource. This provides a single endpoint URL and subscription key that authenticates calls to multiple Cognitive Services, simplifying credential management in code.

Q20: Select the Free tier (F0). The free tier typically provides 5,000 transactions per month at no cost. Limitation: lower transaction limits and sometimes lower latency SLAs than standard tiers.

Q21: The most likely cause is a missing or incorrect subscription key in the Ocp-Apim-Subscription-Key header. Resolution: verify the key was copied correctly from the Azure portal "Keys and Endpoint" page, and ensure it is passed in the correct header.

---

## Deliverable

Submit a single document (PDF or Word) with all answers. Include the relevant JSON excerpts inline with Part C answers to show which values you are referencing. Include your name, course section, and date at the top. Upload to the Module 07 Lab Assignment in Canvas by the posted due date.

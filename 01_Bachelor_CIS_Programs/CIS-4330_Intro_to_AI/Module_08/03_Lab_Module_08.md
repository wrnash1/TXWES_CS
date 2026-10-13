# Lab 08 — Natural Language Processing with Azure

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Alignment: Describe features of Natural Language Processing workloads on Azure

---

## Lab Overview

In this lab you will provision an Azure AI Language resource, call the sentiment analysis and NER endpoints using Python, use Language Studio to explore opinion mining and key phrase extraction, and build a small Conversational Language Understanding (CLU) project. You will document your results and submit screenshots and written responses.

### Learning Objectives

By completing this lab you will be able to:

- Create and configure an Azure AI Language resource
- Call the Sentiment Analysis endpoint and interpret output at document, sentence, and aspect levels
- Call the Named Entity Recognition endpoint and classify entity results
- Use Key Phrase Extraction on a real document
- Build a CLU project with at least three intents and one entity, train it, and test it
- Identify one responsible AI consideration for the NLP task you completed

### Prerequisites

- Active Azure for Students subscription
- Python 3.8+ installed locally, or use Azure Cloud Shell
- Completion of Module 07 lab (Azure familiarity assumed)

### Time Estimate

Approximately 90–120 minutes.

---

## Part A: Provision Azure AI Language (15 minutes)

### Step A1: Create the Resource

1. Sign in to the Azure portal at portal.azure.com.
2. Select **Create a resource** and search for **Language service**.
3. Select **Language service** and click **Create**.
4. On the "Select additional features" page, click **Continue to create your resource**.
5. Fill in the creation form:

   - **Subscription**: Your Azure for Students subscription
   - **Resource group**: Create new — name it `cis4330-mod08-rg`
   - **Region**: East US
   - **Name**: `cis4330-language-<your-initials>` (must be globally unique)
   - **Pricing tier**: Free F0

6. Click **Review + create**, then **Create**.
7. After deployment, click **Go to resource**.
8. Navigate to **Keys and Endpoint** in the left menu. Copy **Key 1** and the **Endpoint** URL to a text file.

### Deliverable A

Screenshot of the Keys and Endpoint page (key blurred or cropped). Label it **Lab08-A-Credentials**.

---

## Part B: Sentiment Analysis and Opinion Mining (25 minutes)

### Step B1: Install the SDK

In your terminal or Cloud Shell, install the Azure AI Language SDK:

```bash
pip install azure-ai-textanalytics
```

### Step B2: Write the Sentiment Analysis Script

Create `lab08_sentiment.py` with the content below. Replace the endpoint and key placeholders.

```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

ENDPOINT = "<your-endpoint>"
KEY = "<your-key>"

client = TextAnalyticsClient(endpoint=ENDPOINT,
                              credential=AzureKeyCredential(KEY))

documents = [
    "The Azure portal is very intuitive and the documentation "
    "is excellent, but the pricing calculator is confusing.",
    "I am extremely disappointed with the response time. "
    "The support team was unhelpful and the issue is still unresolved.",
    "The training completed successfully. "
    "Performance is acceptable for our use case."
]

# Sentiment with opinion mining
result = client.analyze_sentiment(documents,
                                  show_opinion_mining=True)

for i, doc in enumerate(result):
    print(f"\n--- Document {i+1} ---")
    print(f"Document sentiment: {doc.sentiment}")
    print(f"  Positive: {doc.confidence_scores.positive:.2f}")
    print(f"  Neutral:  {doc.confidence_scores.neutral:.2f}")
    print(f"  Negative: {doc.confidence_scores.negative:.2f}")

    for sentence in doc.sentences:
        print(f"\n  Sentence: '{sentence.text}'")
        print(f"  Sentiment: {sentence.sentiment}")
        for mined_opinion in sentence.mined_opinions:
            target = mined_opinion.target
            print(f"    Aspect: '{target.text}' → {target.sentiment}")
            for assessment in mined_opinion.assessments:
                print(f"      Assessment: '{assessment.text}'"
                      f" ({assessment.sentiment})")
```

Run the script:

```bash
python lab08_sentiment.py
```

### Step B3: Interpret the Results

In your lab write-up, answer the following questions.

1. For Document 1, what is the document-level sentiment? Does it match what you would expect as a human reader?
2. For Document 1, what aspects did opinion mining identify, and what sentiment was associated with each aspect?
3. For Document 2, are there any sentences with sentiment that seems surprising? Explain why the model might have scored it that way.
4. Describe one business use case where sentence-level sentiment would be more valuable than document-level sentiment.

### Deliverable B

Terminal screenshot showing output for all three documents. Written answers to the four questions above.

---

## Part C: Named Entity Recognition (20 minutes)

### Step C1: Write the NER Script

Create `lab08_ner.py`:

```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

ENDPOINT = "<your-endpoint>"
KEY = "<your-key>"

client = TextAnalyticsClient(endpoint=ENDPOINT,
                              credential=AzureKeyCredential(KEY))

documents = [
    "Microsoft announced on January 15, 2024 that Satya Nadella "
    "would present at a conference in Seattle, Washington. "
    "The event is expected to attract over 5,000 attendees.",
    "Please contact support at help@contoso.com or call "
    "+1-800-555-0199 between 9 AM and 5 PM EST Monday through Friday.",
    "The contract between Acme Corp and Global Logistics Inc "
    "is valued at $4.2 million and expires on March 31, 2025."
]

result = client.recognize_entities(documents)

for i, doc in enumerate(result):
    print(f"\n--- Document {i+1} ---")
    for entity in doc.entities:
        print(f"  '{entity.text}' → Category: {entity.category}"
              f" | Subcategory: {entity.subcategory}"
              f" | Confidence: {entity.confidence_score:.2f}")
```

Run the script:

```bash
python lab08_ner.py
```

### Step C2: Interpret the Results

Answer the following in your lab write-up.

1. List all entities detected in Document 3. Are there any entities you expected that were not detected?
2. The model returns a confidence score for each entity. Find one entity with a confidence score below 0.90. Why might the model be less certain about this entity?
3. How would a legal or contracts team benefit from applying NER to large volumes of contracts?

### Deliverable C

Terminal screenshot showing NER output. Written answers to the three questions.

---

## Part D: Key Phrase Extraction in Language Studio (15 minutes)

### Step D1: Access Language Studio

1. Navigate to Language Studio at language.cognitive.azure.com.
2. Sign in and select your Language resource.
3. Click **Extract key phrases** under the "Classify text" or "Extract information" section.

### Step D2: Run Key Phrase Extraction

1. In the text box, paste a paragraph from a news article, a Wikipedia entry, or a professional document of your choice. The text should be at least 150 words.
2. Click **Run**.
3. Observe the highlighted key phrases in the text and the phrase list on the right.

### Step D3: Analyze the Results

Answer the following.

1. List the top five key phrases extracted from your text.
2. Do you agree with the service's selection? Are any important phrases missing?
3. How does key phrase extraction differ from a simple word frequency analysis?

### Deliverable D

Screenshot of Language Studio showing your input text and the extracted key phrases. Written answers to the three questions.

---

## Part E: Build a CLU Project (25 minutes)

### Step E1: Design Your CLU Schema

Before building in Language Studio, design your CLU schema on paper or in a text file. Choose a simple domain — a library booking system, a food ordering app, or a tech support bot.

Define at least three intents and at least one entity. For example, for a library system:

- Intents: SearchBook, ReserveBook, ReturnBook, CheckFines, None
- Entities: BookTitle (learned), AuthorName (learned), DueDate (prebuilt: DateTime)

Write your schema in your lab document before moving to Step E2.

### Step E2: Create the CLU Project

1. In Language Studio, click **Conversational Language Understanding** under "Understand questions and conversational language."
2. Click **Create new project**.
3. Name your project `lab08-clu-<your-initials>`.
4. Select **Conversation** project type.
5. Select **English** as the primary language.
6. Click **Next** and **Create project**.

### Step E3: Add Intents and Utterances

1. In the project, click **Schema definition** in the left menu.
2. Add all intents from your schema design.
3. Click **Data labeling** in the left menu.
4. For each intent, add at least five labeled utterances. Label entity spans within utterances where applicable.

Examples for the library scenario:

- SearchBook: "Do you have anything by Stephen King?"
- SearchBook: "I am looking for a book about machine learning"
- ReserveBook: "Can I reserve The Great Gatsby for next week?"
- ReturnBook: "I need to return two books by Friday"
- CheckFines: "How much do I owe in late fees?"

### Step E4: Train and Evaluate

1. Click **Training jobs** and then **Start a training job**.
2. Name the job `lab08-train-v1`, select **Standard training**, and click **Train**.
3. When training completes, click **View model details** to see the evaluation metrics.
4. Record Precision, Recall, and F1 for each intent.

### Step E5: Test the Model

1. Click **Testing deployments** and deploy your model to a slot named `production`.
2. Click **Test deployment**.
3. Enter at least three test utterances — one that should match each of your main intents.
4. Note the top predicted intent and confidence score for each.

### Deliverable E

1. Your written schema design from Step E1.
2. Screenshot of the evaluation metrics page.
3. Screenshot of at least three test predictions.
4. Written answer: Which intent had the lowest F1 score? Why do you think it performed worse than the others?

---

## Part F: Reflection (10 minutes)

You used NLP to analyze sentiment in customer feedback and extract entities from business documents. Answer the following in 150–200 words.

A company wants to use Azure AI Language's PII detection to automatically screen and redact customer support chat logs before they are stored in a database for analytics.

1. What types of information would the PII detector identify and redact from a typical support chat?
2. What is one risk of relying solely on automated PII redaction without human review?
3. Under what privacy regulation (name at least one) might this redaction step be legally required?

---

## Submission Requirements

Submit the following to the course LMS by the posted deadline.

- Lab08-A-Credentials screenshot
- Part B terminal screenshot and four written answers
- Part C terminal screenshot and three written answers
- Part D Language Studio screenshot and three written answers
- Part E schema design, evaluation screenshot, test prediction screenshots, and written analysis
- Part F reflection (150–200 words)

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Part A — Resource provisioning | 5 | Screenshot shows correct resource type |
| Part B — Sentiment analysis | 20 | Output shown; all four questions answered with specifics |
| Part C — NER | 15 | Output shown; three questions answered accurately |
| Part D — Key phrase extraction | 10 | Screenshot shown; three questions answered thoughtfully |
| Part E — CLU project | 35 | Schema designed; 3+ intents, 5+ utterances each; metrics recorded; 3 tests shown; analysis question answered |
| Part F — Reflection | 15 | Addresses PII types, automation risk, and regulation substantively |
| **Total** | **100** | |

---

## Cleanup

After submitting, delete the resource group to avoid charges.

1. In the Azure portal, go to **Resource groups**.
2. Select `cis4330-mod08-rg`.
3. Click **Delete resource group**, confirm, and click **Delete**.

---

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Language NLP Pipeline

1. Using the Azure AI Language SDK or REST API, submit the same short paragraph (3-4 sentences of your choice) in three different languages — English, Spanish, and one additional language of your choice. For each, call: (a) language detection, (b) sentiment analysis, and (c) key phrase extraction.
2. Build a summary table with columns: Language, Detected Language (name + confidence), Sentiment Label, Top 3 Key Phrases. Populate it from your API responses.
3. Translate the non-English texts to English using Azure AI Translator, then re-run sentiment analysis on the translated versions. Compare the sentiment scores to the direct-language scores from step 1.
4. Explain in 2-3 sentences why sentiment analysis scores might differ between the original language and the translated version, and which approach (direct-language vs. translate-then-analyze) is generally more reliable.

### Challenge 2: CLU Intent Coverage Gap Analysis

1. Review your CLU model from Part E of the lab. Design 10 test utterances that were NOT part of your training data — including at least 2 utterances that should map to each of your defined intents, and at least 2 that should be classified as None.
2. Submit all 10 utterances to your deployed CLU model and record the top predicted intent and confidence score for each.
3. For any utterance that was misclassified (wrong intent predicted) or correctly predicted with low confidence (below 0.70), analyze why. Is the utterance semantically ambiguous? Is the training set for that intent too small or not diverse enough?
4. Write a prioritized list of 3 improvements (additional utterances to add, intents to split, or entities to define) that would most improve your model based on the gap analysis.

### Reflection Questions

1. Based on Challenge 1, what does the difference in key phrases extracted from Spanish vs. English versions of the same content reveal about how language-specific tokenization and stopword rules affect NLP outputs?
2. Based on Challenge 2, explain to a product manager why NLP model deployment is not a one-time event — what ongoing maintenance activities are needed to keep a CLU model accurate as user language evolves?

---

End of Lab 08

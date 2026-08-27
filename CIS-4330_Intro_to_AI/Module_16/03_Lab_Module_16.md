# Lab Activity: Module 16 — AI-900 Capstone Lab and Certification Submission

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Alignment: All five exam domains (comprehensive review)

---

## Lab Overview

This is the final lab of CIS-4330. It has two components.

**Component 1 (Technical):** You will build an end-to-end Azure AI solution that integrates services from at least three different AI-900 exam domains. You will provision resources, call APIs, interpret responses, and document an architecture diagram. This demonstrates that you can compose multiple Azure AI services into a coherent application — the type of integration scenario that appears on AI-900 exam questions.

**Component 2 (Certification):** You will register for and sit the official Microsoft AI-900 exam, then submit your score report. Passing the exam earns you a Microsoft credential and satisfies the course's industry certification requirement.

### Learning Objectives

By completing this lab you will be able to:

- Integrate Azure AI Vision, Azure AI Language, and Azure OpenAI Service into a single application pipeline
- Map each service call to its AI-900 exam domain
- Articulate the Responsible AI implications of your combined system
- Pass the Microsoft AI-900 certification exam

### Estimated Time

- Component 1 (Technical Lab): 90–120 minutes
- Component 2 (Exam Prep and Scheduling): 30–60 minutes
- Component 2 (Exam Sitting): 60 minutes (scheduled separately at the testing center)

### Tools Required

- Azure free account at portal.azure.com
- Python 3.8+ or Azure Cloud Shell
- Access to language.cognitive.azure.com (Language Studio)
- Access to portal.azure.com (Azure Portal)

---

## Component 1: End-to-End Azure AI Pipeline (80 points)

You will build a document intelligence pipeline that does the following:

1. Accepts an image of a document (a scanned memo, invoice, or article)
2. Extracts the text using Azure AI Vision OCR
3. Sends the extracted text to Azure AI Language for sentiment analysis and named entity recognition
4. Generates a concise summary using Azure OpenAI Service (if access is available) or Azure AI Language summarization
5. Produces a final JSON report combining all results

This pipeline combines the Computer Vision domain (Step 2), the NLP domain (Steps 3 and 4), and the Machine Learning/AI concepts domain (Step 5 output formatting). It reflects a real-world document automation scenario.

---

## Part A: Provision Resources (15 minutes)

### Step A1: Create a Resource Group

Sign in to the Azure portal at portal.azure.com. Create a new resource group:

- Name: `cis4330-capstone-rg`
- Region: East US

```bash
az group create \
  --name cis4330-capstone-rg \
  --location eastus
```

### Step A2: Create an Azure AI Vision Resource

1. In the portal, select **Create a resource** and search for **Computer Vision**.
2. Select **Computer Vision** and click **Create**.
3. Set the following values:
   - Resource group: `cis4330-capstone-rg`
   - Region: East US
   - Name: `cis4330-vision-cap-<your-initials>`
   - Pricing tier: Free F0
4. Click **Review + create**, then **Create**.
5. After deployment, go to **Keys and Endpoint** and copy Key 1 and the Endpoint URL.

### Step A3: Create an Azure AI Language Resource

1. In the portal, select **Create a resource** and search for **Language service**.
2. Select **Language service** and click **Continue to create your resource**.
3. Set the following values:
   - Resource group: `cis4330-capstone-rg`
   - Region: East US
   - Name: `cis4330-language-cap-<your-initials>`
   - Pricing tier: Free F0
4. Click **Review + create**, then **Create**.
5. After deployment, go to **Keys and Endpoint** and copy Key 1 and the Endpoint URL.

### Deliverable A

Screenshot of each resource's Keys and Endpoint page. Label them **CapA-Vision-Credentials** and **CapA-Language-Credentials**. You may blur or crop the key values.

---

## Part B: Extract Text from a Document Image (20 minutes)

### Step B1: Select a Document Image

Find or create an image that contains a paragraph of readable text. Suitable options:

- A screenshot of a Wikipedia article paragraph
- A photo of a printed page or a magazine article
- A publicly available image of a printed document

The image must contain at least 50 words of text. Note the public URL or save the file locally.

### Step B2: Write the OCR Script

Create a file named `cap_ocr.py` with the following content. Replace the placeholder values with your Azure AI Vision endpoint and key.

```python
import requests
import json

VISION_ENDPOINT = "https://<your-vision-endpoint>/"
VISION_KEY      = "<your-vision-key>"
IMAGE_URL       = "<your-document-image-url>"  # or use local file with requests.post(files=...)

url = (
    VISION_ENDPOINT
    + "computervision/imageanalysis:analyze"
    + "?api-version=2023-02-01-preview"
    + "&features=read"
    + "&language=en"
)

headers = {
    "Ocp-Apim-Subscription-Key": VISION_KEY,
    "Content-Type": "application/json"
}

body = {"url": IMAGE_URL}

response = requests.post(url, headers=headers, json=body)
response.raise_for_status()
result = response.json()

# Extract plain text from the read result
lines = []
read_result = result.get("readResult", {})
for block in read_result.get("blocks", []):
    for line in block.get("lines", []):
        lines.append(line.get("text", ""))

extracted_text = " ".join(lines)
print("=== Extracted Text ===")
print(extracted_text)

# Save for next step
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(extracted_text)

print("\nExtracted text saved to extracted_text.txt")
```

### Step B3: Run the OCR Script

```bash
pip install requests
python cap_ocr.py
```

Verify that `extracted_text.txt` contains coherent text from your document image.

### Deliverable B

1. Screenshot of your terminal showing the extracted text output.
2. One-sentence description of the document image you used.

---

## Part C: Analyze the Extracted Text with Azure AI Language (25 minutes)

### Step C1: Write the Language Analysis Script

Create a file named `cap_language.py` with the following content. Replace the endpoint and key placeholders with your Azure AI Language credentials.

```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import json

LANGUAGE_ENDPOINT = "<your-language-endpoint>"
LANGUAGE_KEY      = "<your-language-key>"

# Load the extracted text from the previous step
with open("extracted_text.txt", "r", encoding="utf-8") as f:
    document_text = f.read()

# Truncate to 5,000 characters if necessary (free tier limit)
document_text = document_text[:5000]

client = TextAnalyticsClient(
    endpoint=LANGUAGE_ENDPOINT,
    credential=AzureKeyCredential(LANGUAGE_KEY)
)

documents = [document_text]

# --- Sentiment Analysis with Opinion Mining ---
sentiment_result = client.analyze_sentiment(
    documents, show_opinion_mining=True
)[0]

print("=== Sentiment Analysis ===")
print(f"Overall Sentiment: {sentiment_result.sentiment}")
print(f"Positive: {sentiment_result.confidence_scores.positive:.2f}")
print(f"Neutral:  {sentiment_result.confidence_scores.neutral:.2f}")
print(f"Negative: {sentiment_result.confidence_scores.negative:.2f}")

# --- Named Entity Recognition ---
ner_result = client.recognize_entities(documents)[0]

print("\n=== Named Entity Recognition ===")
entities = []
for entity in ner_result.entities:
    print(f"  '{entity.text}' — {entity.category} "
          f"(confidence: {entity.confidence_score:.2f})")
    entities.append({
        "text": entity.text,
        "category": entity.category,
        "confidence": round(entity.confidence_score, 2)
    })

# --- Key Phrase Extraction ---
kp_result = client.extract_key_phrases(documents)[0]
key_phrases = list(kp_result.key_phrases)

print("\n=== Key Phrases ===")
for phrase in key_phrases[:10]:
    print(f"  {phrase}")

# --- Compile Report ---
report = {
    "sentiment": {
        "label": sentiment_result.sentiment,
        "scores": {
            "positive": round(sentiment_result.confidence_scores.positive, 2),
            "neutral":  round(sentiment_result.confidence_scores.neutral, 2),
            "negative": round(sentiment_result.confidence_scores.negative, 2)
        }
    },
    "entities": entities,
    "key_phrases": key_phrases[:10]
}

with open("language_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2)

print("\nLanguage report saved to language_report.json")
```

### Step C2: Install SDK and Run

```bash
pip install azure-ai-textanalytics
python cap_language.py
```

### Step C3: Interpret the Results

Answer the following in your lab write-up.

1. What is the overall document sentiment? Does it match your reading of the source text?
2. List three named entities extracted. For each, name the entity category and explain whether the category assignment is correct.
3. List the top five key phrases. Do they accurately summarize the main topics of the document?
4. A company deploys this pipeline to analyze thousands of customer support emails automatically. What Responsible AI concern arises if the sentiment model misclassifies a frustrated customer's email as neutral?

### Deliverable C

1. Screenshot of the terminal showing sentiment, entities, and key phrases.
2. Contents of `language_report.json` (paste into your lab document).
3. Written answers to the four interpretation questions.

---

## Part D: Generate a Summarization Using Azure AI Language (15 minutes)

### Step D1: Write the Summarization Script

Create `cap_summary.py` with the following content.

```python
from azure.ai.textanalytics import TextAnalyticsClient, ExtractiveSummaryAction
from azure.core.credentials import AzureKeyCredential

LANGUAGE_ENDPOINT = "<your-language-endpoint>"
LANGUAGE_KEY      = "<your-language-key>"

with open("extracted_text.txt", "r", encoding="utf-8") as f:
    document_text = f.read()[:5000]

client = TextAnalyticsClient(
    endpoint=LANGUAGE_ENDPOINT,
    credential=AzureKeyCredential(LANGUAGE_KEY)
)

documents = [document_text]

# Extractive summarization — selects 3 sentences from the source
poller = client.begin_analyze_actions(
    documents,
    actions=[ExtractiveSummaryAction(max_sentence_count=3)]
)

result = list(poller.result())

print("=== Extractive Summary ===")
for action_result in result[0]:
    if not action_result.is_error:
        for sentence in action_result.sentences:
            print(f"  [{sentence.rank_score:.2f}] {sentence.text}")
```

### Step D2: Run the Summarization

```bash
python cap_summary.py
```

Note the rank scores — a higher score means the sentence was ranked more important by the model.

### Deliverable D

Screenshot of the three extracted summary sentences with their rank scores. One-sentence explanation of why extractive summarization is traceable and auditable.

---

## Part E: Architecture Diagram and Domain Mapping (10 minutes)

Draw or describe a system architecture diagram for the pipeline you built. You may use any diagramming tool (draw.io, PowerPoint, pencil and paper photographed) or a written description with a table.

Your diagram or description must include:

1. The input (document image with source URL or file path)
2. Azure AI Vision → OCR → extracted text
3. Azure AI Language → sentiment + NER + key phrase extraction + summarization
4. The output report (JSON)
5. For each service box, label the AI-900 exam domain it falls under

### Domain Reference Table

| Service Used | AI-900 Exam Domain |
|---|---|
| Azure AI Vision OCR | Computer vision workloads on Azure |
| Azure AI Language — Sentiment Analysis | Natural language processing workloads on Azure |
| Azure AI Language — NER | Natural language processing workloads on Azure |
| Azure AI Language — Key Phrase Extraction | Natural language processing workloads on Azure |
| Azure AI Language — Extractive Summarization | Natural language processing workloads on Azure |

### Deliverable E

Your architecture diagram (screenshot, photo, or table-based written description) with AI-900 domain labels.

---

## Part F: Responsible AI Reflection (15 minutes)

Write a 200–250 word reflection addressing the following prompt.

The document analysis pipeline you built can be used to automatically extract, classify, and summarize content from any text-based document — including emails, medical records, legal contracts, and financial disclosures.

Address the following:

1. **Fairness and Bias**: NLP models trained on English-language text may perform differently on documents written by non-native speakers or in regional dialects. What fairness risk does this introduce, and how would you test for it?

2. **Privacy and Data Security**: In your pipeline, the document text is sent to Azure cloud endpoints. For a healthcare organization processing patient records, what specific steps must be taken before the pipeline can be deployed, and which Microsoft Responsible AI principle governs these steps?

3. **Transparency**: The extractive summarizer selects sentences based on a rank score, but the model does not explain why it ranked each sentence higher than others. How does this lack of explainability affect a lawyer or analyst who must rely on the summary in a legal or financial context?

4. **Accountability**: If this automated pipeline misclassifies a sensitive document and causes harm, who is accountable — the developer, the organization that deployed it, or Microsoft?

---

## Part G: Cleanup (5 minutes)

After submitting your lab, delete all resources to avoid charges.

```bash
az group delete \
  --name cis4330-capstone-rg \
  --yes \
  --no-wait
```

---

## Submission Requirements

Submit all of the following to Canvas by the posted deadline.

| Item | Label |
|---|---|
| CapA-Vision-Credentials screenshot | Key blurred or cropped |
| CapA-Language-Credentials screenshot | Key blurred or cropped |
| Part B terminal screenshot | Extracted text visible |
| Part C terminal screenshot | Sentiment + entities + key phrases visible |
| Part C language_report.json contents | Pasted into document |
| Part C interpretation answers (4 questions) | Written responses |
| Part D extractive summary screenshot | Rank scores visible |
| Part D auditability explanation | One sentence |
| Part E architecture diagram | Domain labels visible |
| Part F Responsible AI reflection | 200–250 words |

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part A — Resource provisioning | 10 | Both resources created; screenshots show correct endpoints |
| Part B — OCR extraction | 15 | Text successfully extracted from a document image |
| Part C — Language analysis | 25 | Sentiment, NER, and key phrases shown; all four interpretation questions answered with specifics |
| Part D — Summarization | 10 | Three summary sentences shown with rank scores; auditability explanation provided |
| Part E — Architecture diagram | 10 | All pipeline stages shown; AI-900 domain labels present |
| Part F — Responsible AI reflection | 10 | Addresses fairness, privacy, transparency, and accountability substantively; 200–250 words |
| **Total** | **80** | Component 1 portion of Module 16 grade |

---

## Component 2: AI-900 Certification Exam (20 points)

### Instructions

1. Register for the official Microsoft AI-900 exam through the on-campus Pearson VUE testing center or an authorized online proctoring provider. Use your .edu email to access any available academic discount.
2. Complete the exam.
3. Obtain your official score report PDF. The report will show your full name, the exam name (AI-900 Microsoft Azure AI Fundamentals), your scaled score (passing = 700/1000), pass/fail status, and the exam date.
4. Upload the score report PDF to the Canvas assignment box for this module.

### Exam Registration Resources

- Microsoft Certification portal: learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/
- Exam skills outline: learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-900
- Free practice assessment (50 questions): learn.microsoft.com/en-us/certifications/exams/ai-900/practice/assessment?assessmentId=26

### Grading

| Component | Points |
|---|---|
| Official AI-900 score report submitted (any score) | 10 |
| Official AI-900 score report showing passing status (700+) | 10 additional |
| **Total** | **Up to 20** |

Students who do not pass on their first attempt will receive 10 points for attempting the exam and submitting the score report. The additional 10 points require a passing score.

---

## Part 9 — Challenge Exercise

### Challenge 1: Full-Course AI-900 Domain Diagnostic

1. Using the five AI-900 exam domains as your framework, create a personal diagnostic table with columns: Domain | Module(s) Covered | Self-Confidence (1–5) | Key Services/Concepts | Weakest Sub-topic. Complete one row for each of the five domains using your honest self-assessment based on your performance across the course quizzes and labs.
2. For the two domains where you rated your confidence lowest, revisit the corresponding module reading guides and complete at least 10 Microsoft Learn practice questions in each domain. Record your practice score (correct / total) before and after the review session.
3. For each of the five AI-900 domains, write one original scenario-based question of your own that could plausibly appear on the exam. Write the question, four answer options (A–D), the correct answer, and a one-sentence explanation of why each distractor is wrong. Use the format from the course quizzes.
4. Exchange your five questions with a classmate. Answer their five questions under timed conditions (30 seconds per question). Score each other's answers and discuss any questions where you disagreed on the correct answer. Write a 2–3 sentence reflection on what this exercise revealed about the sub-topics that are most likely to produce confusion on the real exam.

### Challenge 2: End-to-End Azure AI Solution Design

1. Select a real business problem from one of the following industries: healthcare, retail, financial services, or education. Write a 2–3 sentence problem statement describing a specific operational challenge that AI could address (for example: "A regional hospital processes 800 referral letters per day manually, which takes three hours of clinical coordinator time and introduces transcription errors").
2. Design a complete Azure AI solution architecture for the problem. Identify: (a) which Azure AI service(s) are used and why, (b) the data flow from input to output, (c) any custom training required versus pre-built service usage, (d) how the system handles errors and low-confidence outputs, and (e) where human review is required before acting on AI outputs.
3. Evaluate your proposed solution against all six Microsoft Responsible AI principles. For each principle, write one sentence explaining either how the design satisfies it or what specific risk exists and what mitigation is required.
4. Estimate the ROI framework for the solution: identify the baseline metric (current performance without AI), the expected improvement after AI deployment, the primary cost category (labor savings, cost avoidance, or revenue increase), and one ongoing risk (data drift, regulatory change, or fairness degradation) that would require monitoring after deployment.

### Reflection Questions

1. After completing Challenge 1, identify the single AI-900 exam topic that you found most difficult to master across the entire course. Explain in 3–4 sentences why this topic is conceptually challenging, what the most common mistake is when answering exam questions about it, and what specific mental model or mnemonic helped you finally understand it.

2. Based on Challenge 2, reflect on the gap between designing an AI solution on paper and deploying it in production. What aspect of responsible AI governance — transparency, human oversight, fairness monitoring, or privacy compliance — do you believe is most frequently underestimated by organizations deploying their first production AI system, and why?

---

End of Lab — Module 16

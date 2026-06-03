# Reading Guide: Module 16 — AI-900 Exam Preparation and Capstone

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Overview

This reading guide is your structured review companion for the AI-900 exam. Rather than assigning new readings, Module 16 directs you back to the official Microsoft Learn paths and provides organized study materials for each exam domain. Budget 3–4 hours for a complete study session using this guide.

---

## Official Study Resources

### Primary Resource — Microsoft Learn AI-900 Learning Path

**URL:** `https://learn.microsoft.com/en-us/certifications/exams/ai-900`

Click "Prepare for exam" → access the official Microsoft AI-900 Study Guide and the full learning path.

Complete any of the five learning path modules you have not yet visited. Each module ends with knowledge checks that closely match exam question style.

### Secondary Resource — Microsoft AI-900 Sample Questions

**URL:** `https://learn.microsoft.com/en-us/certifications/resources/study-guides/ai-900`

Microsoft publishes a sample question set and a study guide document. Download both. Review the sample questions carefully — note not just whether you got the right answer, but why the other answers are wrong.

### Community Practice Questions

**URL:** `https://www.measureup.com/ai-900.html` (paid, optional)

**URL:** `https://www.udemy.com/` — search "AI-900 practice exam" (paid, discount frequently available)

---

## Domain-by-Domain Review

### Domain 1 — Describe AI Workloads and Considerations (15–20%)

#### Core Knowledge Checklist

Place a check next to each item when you can define it, give an example, and identify which Azure service addresses it:

- [ ] Define AI workload types: prediction, computer vision, NLP, generative AI, anomaly detection
- [ ] Match workload types to business scenarios
- [ ] List all six responsible AI principles by name
- [ ] For each principle, describe a scenario where it is at risk
- [ ] Explain what "inappropriate AI use" means with an example
- [ ] Distinguish between AI and rule-based systems

#### Key Scenarios for Domain 1

**Scenario:** A bank's loan approval system approves loans for applicants of one demographic group at higher rates than another, even after controlling for creditworthiness. Which responsible AI principle is most at risk?

Answer: **Fairness.** The system produces inequitable outcomes across demographic groups.

**Scenario:** A government agency uses AI to make asylum decisions without human review, and applicants have no way to appeal or receive an explanation. Which two responsible AI principles are most at risk?

Answer: **Transparency** (no explanation) and **Accountability** (no human review or appeal mechanism).

**Scenario:** A healthcare AI vendor will not disclose the training data composition or the algorithm used in a patient risk scoring tool. Which principle is at risk?

Answer: **Transparency.**

---

### Domain 2 — Describe Fundamental Machine Learning Principles (20–25%)

#### Core Knowledge Checklist

- [ ] Define supervised, unsupervised, and reinforcement learning with one example each
- [ ] Distinguish regression from classification — can provide a business example of each
- [ ] Explain what clustering is and name one use case
- [ ] Define feature, label, training set, validation set, test set
- [ ] Explain overfitting and underfitting
- [ ] Define accuracy, precision, recall, F1 score, AUC-ROC, RMSE
- [ ] Know when to use each metric
- [ ] Describe the Azure ML workspace components: compute, data assets, environments, jobs, models, endpoints
- [ ] Explain AutoML and what it automates
- [ ] Explain the Designer and what type of user it serves
- [ ] Distinguish online endpoints from batch endpoints
- [ ] Define data drift and concept drift

#### Metric Quick-Reference

| Metric | Formula | Use When |
|---|---|---|
| Accuracy | (TP + TN) / Total | Classes are balanced |
| Precision | TP / (TP + FP) | False positives are costly (spam filter) |
| Recall | TP / (TP + FN) | False negatives are costly (cancer screening) |
| F1 Score | 2 * (P * R) / (P + R) | Both precision and recall matter |
| AUC-ROC | Area under ROC curve | Overall classifier comparison |
| RMSE | √(mean(errors²)) | Regression; penalizes large errors |
| MAE | mean(|errors|) | Regression; average error magnitude |

#### Endpoint Decision Tree

Does the application require a response within seconds? → **Online endpoint**

Does the application score large volumes of records at scheduled times? → **Batch endpoint**

Is latency irrelevant and throughput critical? → **Batch endpoint**

Is the application a user-facing web app? → **Online endpoint**

---

### Domain 3 — Describe Computer Vision Features on Azure (15–20%)

#### Core Knowledge Checklist

- [ ] Define image classification, object detection, semantic segmentation
- [ ] Explain optical character recognition (OCR)
- [ ] Define face detection vs. face recognition vs. face verification
- [ ] Name the Azure service for general image analysis: **Azure AI Vision**
- [ ] Name the Azure service for custom image models: **Azure Custom Vision**
- [ ] Name the Azure service for face analysis: **Azure Face API**
- [ ] Know responsible AI requirements for face recognition

#### Computer Vision Service Mapping

| Task | Azure Service |
|---|---|
| Classify images with pre-built labels | Azure AI Vision (Image Analysis) |
| Train a custom image classifier | Azure Custom Vision |
| Detect faces in an image | Azure Face API / Azure AI Vision |
| Recognize whose face it is | Azure Face API |
| Extract text from images/documents | Azure AI Vision (OCR) / Azure AI Document Intelligence |
| Analyze structured documents (invoices, forms) | Azure AI Document Intelligence |
| Moderate image content | Azure Content Moderator / Azure AI Vision |
| Generate image descriptions | Azure AI Vision (Image Captions) |

#### Responsible Face Recognition — Key Facts

- **Prohibited uses include:** Mass surveillance of individuals in public spaces without authorization
- **Required for deployment:** Transparency disclosure that face recognition is in use
- **Fairness requirement:** Error rates must be comparable across demographic groups
- **Access control:** Microsoft restricts access to certain face recognition capabilities and requires approval for law enforcement use

---

### Domain 4 — Describe Natural Language Processing Features (15–20%)

#### Core Knowledge Checklist

- [ ] Define key phrase extraction and its use case
- [ ] Define sentiment analysis and its use case
- [ ] Define named entity recognition (NER) and give three entity types
- [ ] Define language detection
- [ ] Define text summarization (extractive vs. abstractive)
- [ ] Define question answering
- [ ] Define intent classification and entity extraction in CLU (Conversational Language Understanding)
- [ ] Define speech-to-text and text-to-speech
- [ ] Define speech translation
- [ ] Know which service handles each: Azure AI Language vs. Azure AI Speech vs. Azure AI Translator
- [ ] Know what the Language Understanding service (CLU) does vs. regular text analytics

#### NLP Service Mapping

| Task | Azure Service |
|---|---|
| Detect sentiment in customer reviews | Azure AI Language |
| Extract key phrases from text | Azure AI Language |
| Identify people, places, dates in text | Azure AI Language (NER) |
| Detect what language text is written in | Azure AI Language |
| Transcribe spoken audio to text | Azure AI Speech |
| Convert text to natural speech | Azure AI Speech |
| Translate speech from one language to another | Azure AI Speech (speech translation) |
| Translate written text between languages | Azure AI Translator |
| Classify user intent in a chatbot utterance | Azure AI Language (CLU / LUIS) |
| Answer questions from a knowledge base | Azure AI Language (Question Answering) |

#### Common Multi-Service Scenarios

**Scenario:** "A company wants to analyze customer support chat transcripts to identify common complaint topics and sentiment."

Services needed: **Azure AI Language** (key phrase extraction + sentiment analysis)

**Scenario:** "A call center wants to automatically transcribe phone calls, then analyze each call for customer satisfaction."

Services needed: **Azure AI Speech** (transcription) + **Azure AI Language** (sentiment analysis)

**Scenario:** "A multilingual website wants to detect the language of each user review and translate it to English before sentiment analysis."

Services needed: **Azure AI Language** (language detection) + **Azure AI Translator** (translation) + **Azure AI Language** (sentiment)

---

### Domain 5 — Describe Generative AI Features on Azure (25–30%)

#### Core Knowledge Checklist

- [ ] Define large language model (LLM)
- [ ] Explain the transformer architecture at a conceptual level (self-attention)
- [ ] Define foundation model and fine-tuning
- [ ] Define prompt engineering; know system prompts and few-shot prompting
- [ ] Define temperature in LLM inference
- [ ] Know GPT-4 capabilities: text generation, summarization, code generation, reasoning
- [ ] Know GPT-4V/4o: multimodal (image + text input)
- [ ] Know DALL-E: text to image
- [ ] Know Whisper: speech to text
- [ ] Know Embeddings API: semantic vector representations
- [ ] Define Retrieval Augmented Generation (RAG) and explain its benefit
- [ ] Define Azure AI Search in the RAG pipeline context
- [ ] Know what Azure OpenAI Service is and how it differs from openai.com
- [ ] Know what content filtering does in Azure OpenAI
- [ ] Know what Microsoft Copilot is and which products embed it
- [ ] Know responsible generative AI practices: grounding, transparency, avoiding over-reliance

#### Generative AI Capability Map

| Capability | Azure OpenAI Model | Input | Output |
|---|---|---|---|
| Text generation, summarization, reasoning | GPT-4 | Text | Text |
| Text + image understanding | GPT-4V / GPT-4o | Text + Image | Text |
| Image generation from text | DALL-E 3 | Text | Image |
| Speech to text | Whisper | Audio | Text |
| Semantic embeddings | text-embedding-ada-002 | Text | Vector |
| Code generation | GPT-4 (Codex capabilities integrated) | Text/Code | Code |

#### RAG Architecture Summary

1. **Ingestion phase:** Documents are chunked → embedded via Embeddings API → stored in Azure AI Search vector index
2. **Retrieval phase:** User query is embedded → vector similarity search retrieves top-k relevant chunks
3. **Generation phase:** Retrieved chunks + user query are combined in a prompt → LLM generates a grounded response

**Why RAG?** Reduces hallucination (model is grounded in real documents). Enables use of proprietary/recent information the model was not trained on. Keeps sensitive data in Azure without sending to OpenAI training.

---

## Responsible AI Principles — Master Study Table

| Principle | Definition | Example Violation | Azure Tool/Practice |
|---|---|---|---|
| **Fairness** | Treat all people equitably | Credit AI with disparate impact by race | Fairlearn toolkit; bias testing |
| **Reliability and Safety** | Perform as expected; fail gracefully | Autonomous vehicle AI fails in rain | Rigorous testing; fallback modes |
| **Privacy and Security** | Protect personal data; resist attacks | Training data leaks via model inversion | Differential privacy; Azure Key Vault |
| **Inclusiveness** | Empower all people; accessible design | ASR model with 40% higher error for accented speech | Demographic testing; diverse training data |
| **Transparency** | Understandable to users and affected individuals | Black-box medical AI with no explanation | SHAP, LIME; model cards |
| **Accountability** | Humans are responsible for AI impacts | No human review for high-stakes automated decisions | Human-in-loop; governance policies |

---

## Common Wrong Answers — "Watch-Out" List

The following are the most frequently missed concepts on the AI-900 exam based on common question patterns:

1. **Custom Vision vs. Azure AI Vision:** Custom Vision trains a NEW model on YOUR images. Azure AI Vision uses Microsoft's pre-built models on your images.

2. **AutoML vs. Designer:** AutoML finds the best algorithm automatically. Designer is a visual drag-and-drop tool for building pipelines manually.

3. **Face detection vs. recognition:** Detection = finding a face in an image. Recognition = identifying whose face it is.

4. **Online endpoint vs. batch endpoint:** If the scenario includes "real-time," "immediate response," or "interactive" → online. If it includes "bulk," "overnight," or "scheduled" → batch.

5. **Azure AI Language vs. Azure AI Speech:** Language = text analysis. Speech = audio processing.

6. **Regression vs. classification:** Predict a number → regression. Predict a category → classification.

7. **Overfitting vs. underfitting:** Low training error, high test error → overfitting. High error on both → underfitting.

8. **RAG vs. fine-tuning:** RAG retrieves external documents at inference time — no retraining needed. Fine-tuning trains the model on new data to change its learned knowledge.

---

## Study Schedule — Final 7 Days Before Exam

| Day | Activity | Time |
|---|---|---|
| Day 1 | Domain 1 and Domain 2 review using this guide | 60 min |
| Day 2 | Domain 3 and Domain 4 review; Service Mapping tables | 60 min |
| Day 3 | Domain 5 full review; Generative AI Capability Map | 75 min |
| Day 4 | Responsible AI Principles Master Table; practice with scenarios | 45 min |
| Day 5 | 20-question practice exam (M16 Quiz document) | 45 min |
| Day 6 | Review every question you missed in Day 5 practice; revisit weak areas | 45 min |
| Day 7 (Exam Day) | Light review of Domain 5 flashcards; eat well; rest | 15 min max |

---

*Reading Guide prepared by Professor Nash | Texas Wesleyan University | CIS-4330*

# Lab: Module 16 — AI-900 Exam Preparation and Capstone

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Lab Overview

**Title:** AI-900 Capstone — Full Domain Review and Exam Simulation

**Estimated Time:** 120–150 minutes

**Skill Level:** All levels (review and reflection)

**Prerequisites:**

- Completed all 15 prior modules
- Completed Module 16 Video Script and Reading Guide
- Access to Microsoft Learn AI-900 learning path

**Learning Objectives:**

1. Complete a structured self-assessment across all five AI-900 exam domains
2. Identify and address personal knowledge gaps before the exam
3. Practice exam-style questions under timed conditions
4. Complete an Azure AI portfolio reflection
5. Finalize your certification and career plan

---

## Part 1 — Self-Assessment Diagnostic (20 minutes)

### Task 1.1 — Domain Confidence Rating

For each AI-900 exam domain and each sub-topic, rate your confidence on a scale of 1–5:

- 1 = Cannot define or explain this at all
- 2 = Vague understanding; could not answer exam questions
- 3 = Moderate understanding; might miss some exam questions
- 4 = Good understanding; confident on most questions
- 5 = Strong mastery; could teach this to a classmate

**Domain 1 — AI Workloads and Considerations**

| Topic | Confidence (1–5) |
|---|---|
| Identify AI workload types (prediction, CV, NLP, gen AI) | |
| Describe responsible AI: Fairness | |
| Describe responsible AI: Reliability and Safety | |
| Describe responsible AI: Privacy and Security | |
| Describe responsible AI: Inclusiveness | |
| Describe responsible AI: Transparency | |
| Describe responsible AI: Accountability | |
| Distinguish AI from rule-based systems | |

**Domain 2 — Fundamental ML Principles**

| Topic | Confidence (1–5) |
|---|---|
| Supervised vs. unsupervised vs. reinforcement learning | |
| Regression vs. classification | |
| Clustering and use cases | |
| Features, labels, training/test/validation split | |
| Overfitting and underfitting | |
| Accuracy, precision, recall, F1, AUC, RMSE | |
| Azure ML workspace components | |
| AutoML capabilities and limitations | |
| Designer capabilities | |
| Online vs. batch endpoints | |
| Data drift vs. concept drift | |

**Domain 3 — Computer Vision**

| Topic | Confidence (1–5) |
|---|---|
| Image classification vs. object detection vs. segmentation | |
| Optical character recognition (OCR) | |
| Face detection vs. recognition vs. verification | |
| Azure AI Vision use cases | |
| Azure Custom Vision use cases | |
| Azure Face API use cases | |
| Responsible face recognition guidelines | |

**Domain 4 — NLP**

| Topic | Confidence (1–5) |
|---|---|
| Key phrase extraction | |
| Sentiment analysis | |
| Named entity recognition | |
| Language detection | |
| Text summarization | |
| Question answering | |
| Intent classification (CLU) | |
| Speech-to-text and text-to-speech | |
| Speech translation | |
| Azure AI Language vs. Azure AI Speech vs. Azure AI Translator | |

**Domain 5 — Generative AI**

| Topic | Confidence (1–5) |
|---|---|
| Define LLM and transformer architecture (conceptual) | |
| Foundation models and fine-tuning | |
| Prompt engineering: system prompts, few-shot | |
| Temperature and output variability | |
| GPT-4 capabilities | |
| DALL-E 3 capability | |
| Whisper capability | |
| Embeddings API | |
| Retrieval Augmented Generation (RAG) | |
| Azure OpenAI Service vs. openai.com | |
| Content filtering in Azure OpenAI | |
| Microsoft Copilot | |
| Responsible generative AI practices | |

### Task 1.2 — Gap Analysis

From your confidence ratings above, identify your five lowest-rated topics. These are your priority review targets.

Record your five gap topics here:

1.
2.
3.
4.
5.

For each gap topic, write a one-paragraph summary (4–6 sentences) demonstrating your understanding after reviewing the relevant module materials. This forced recall is one of the most effective study techniques.

---

## Part 2 — Microsoft Learn Knowledge Checks (20 minutes)

### Task 2.1 — Complete Knowledge Checks

Navigate to the Microsoft Learn AI-900 learning path:

`https://learn.microsoft.com/en-us/training/paths/get-ai-ready/`

Complete the knowledge check questions at the end of each of the following modules:

- Module: "Get started with AI on Azure" — complete knowledge check
- Module: "Fundamentals of machine learning" — complete knowledge check
- Module: "Fundamentals of Azure AI Vision" — complete knowledge check
- Module: "Fundamentals of text analysis with the Language service" — complete knowledge check
- Module: "Fundamentals of Azure OpenAI Service" — complete knowledge check

For each knowledge check, record:

1. How many questions were in the check?
2. How many did you answer correctly on the first attempt?
3. Which question(s) did you miss, and what was the correct answer?

---

## Part 3 — Timed Practice Exam Simulation (30 minutes)

### Task 3.1 — Exam Instructions

This simulation mimics the actual AI-900 exam format. Rules:

- Set a 30-minute timer before starting
- Do not use notes, the internet, or any reference material
- Answer all 20 questions before reviewing any answers
- When time expires, stop and grade your answers using the answer key in the M16 Quiz document

Do not read the M16 Quiz document before completing this simulation.

### Task 3.2 — Simulation Question Set

Answer each question on a separate sheet of paper or in a document. Write only the letter of your answer.

1. A hospital wants to automatically flag urgent patient records for physician review based on clinical note text. What type of AI workload is this?

   A. Computer vision
   B. Natural language processing
   C. Anomaly detection in time series
   D. Generative content creation

2. Which responsible AI principle requires that an AI system's decision-making be understandable to the people it affects?

   A. Fairness
   B. Accountability
   C. Transparency
   D. Inclusiveness

3. A company trains an AI model to predict customer churn. The output is either "Will Churn" or "Will Not Churn." What type of ML task is this?

   A. Regression
   B. Clustering
   C. Classification
   D. Anomaly detection

4. A data scientist wants to try 200 algorithm and hyperparameter combinations to find the best performing model on a tabular dataset. Which Azure ML feature automates this?

   A. Azure Machine Learning Designer
   B. Azure AutoML
   C. Azure Custom Vision
   D. Azure AI Foundry

5. A retail company needs to deploy a model that scores every customer in their database nightly and writes predictions to a table. Which endpoint type is most appropriate?

   A. Managed online endpoint
   B. Batch endpoint
   C. Compute cluster direct deployment
   D. Real-time streaming endpoint

6. What is the primary purpose of OCR in Azure AI Vision?

   A. Detect faces in photographs
   B. Classify whether an image contains prohibited content
   C. Extract text from images and documents
   D. Translate text from one language to another

7. A company wants to train an image classifier using 200 labeled photographs of their own industrial equipment to detect malfunctions. Which Azure service should they use?

   A. Azure AI Vision (pre-built analysis)
   B. Azure Custom Vision (train custom classifier)
   C. Azure Machine Learning AutoML
   D. Azure Face API

8. A user asks a chatbot: "I want to book a flight to Dallas for next Friday." The chatbot must identify that the user intends to book a flight (intent) and extract "Dallas" and "next Friday" (entities). Which Azure service handles this?

   A. Azure AI Translator
   B. Azure AI Vision
   C. Azure AI Language — Conversational Language Understanding
   D. Azure AI Speech — speech translation

9. A contact center wants to transcribe customer service phone calls in real time. Which Azure service performs this function?

   A. Azure AI Language
   B. Azure AI Speech — speech-to-text
   C. Azure AI Translator
   D. Azure OpenAI Whisper deployment

10. Which Azure service would you use to translate a customer review written in Portuguese into English?

    A. Azure AI Language — sentiment analysis
    B. Azure AI Speech — speech translation
    C. Azure AI Translator
    D. Azure OpenAI GPT-4

11. A company deploys GPT-4 via Azure OpenAI Service. They want the model to answer questions using only information from their internal policy documents, rather than the model's general training knowledge. What pattern should they implement?

    A. Fine-tuning the model on the policy documents
    B. Retrieval Augmented Generation (RAG)
    C. Increasing the model's temperature parameter
    D. Using the DALL-E model instead of GPT-4

12. What does the temperature parameter control in an Azure OpenAI text generation request?

    A. The number of tokens in the output
    B. The randomness and creativity of the model's output
    C. The speed of inference on the compute cluster
    D. The maximum context length the model can process

13. A customer uses DALL-E 3 via Azure OpenAI Service. What type of output does DALL-E generate?

    A. Audio files from text descriptions
    B. Images generated from text descriptions
    C. Code generated from natural language specifications
    D. Summaries of uploaded documents

14. Which of the following best describes Azure OpenAI content filtering?

    A. A tokenizer that limits the length of prompts sent to the model
    B. An encryption layer that prevents unauthorized access to model weights
    C. Classifiers applied to inputs and outputs to prevent harmful or inappropriate content
    D. A pricing control that limits the number of API calls per subscription

15. An AI-powered hiring tool consistently recommends male candidates over female candidates with equal qualifications. Which responsible AI principle is most directly violated?

    A. Transparency
    B. Accountability
    C. Fairness
    D. Reliability

16. A medical imaging AI achieves 95% accuracy in testing but performs at only 78% accuracy on patients over age 75 in production. Which responsible AI principle failure does this illustrate?

    A. Privacy and Security
    B. Fairness and Inclusiveness
    C. Accountability
    D. Transparency

17. What does the Azure Machine Learning model registry provide?

    A. Real-time inference endpoints for deployed models
    B. A versioned store of trained model artifacts with lineage and metadata
    C. A visual drag-and-drop interface for building ML pipelines
    D. Automated algorithm selection and hyperparameter tuning

18. A team deploys an online endpoint for a product recommendation model. Over several months, the model's prediction quality degrades. Investigation reveals that customers' purchasing preferences have changed. What type of drift is this?

    A. Data drift — input feature distributions have changed
    B. Concept drift — the relationship between features and correct output has changed
    C. Model drift — the model weights have changed post-deployment
    D. Infrastructure drift — compute resources are insufficient

19. Which Azure service provides the embeddings API used to convert text into semantic vector representations for use in RAG pipelines?

    A. Azure AI Language
    B. Azure AI Translator
    C. Azure OpenAI Service
    D. Azure Custom Vision

20. Microsoft's responsible AI principles are best described as:

    A. Legally mandated requirements for all AI deployments in the European Union
    B. Ethical guidelines that must be embedded into AI design, development, and deployment practices
    C. Technical specifications for configuring Azure AI services securely
    D. Performance benchmarks that AI models must meet before Azure deployment

---

### Task 3.3 — Grade and Analyze

After completing the simulation, use the M16 Quiz document answer key to grade your responses.

Record your score: \_\_\_ / 20

For each question you missed, write a 2–3 sentence explanation of why the correct answer is correct and why your answer was wrong.

**Score Interpretation:**

- 18–20: Excellent — you are very well prepared for the AI-900
- 15–17: Good — review the specific domains where you missed questions
- 12–14: Fair — dedicate additional time to your gap areas before the exam
- Below 12: Return to the module materials for any topic with two or more misses

---

## Part 4 — Azure AI Portfolio Reflection (20 minutes)

### Task 4.1 — Personal AI Skills Inventory

Create an inventory of the AI skills and experiences you have gained in this course. For each module lab you completed, write one entry:

| Module | Lab Activity | Skill Demonstrated | Azure Service Used |
|---|---|---|---|
| Module 1 | | | |
| Module 2 | | | |
| (continue for all completed modules) | | | |

### Task 4.2 — Capstone Reflection Essay

Write a 400–500 word capstone reflection addressing the following questions:

1. **Growth:** What did you understand least about AI at the start of this course? How has your understanding changed?

2. **Application:** Name one real-world problem in a field you care about that could be addressed with an AI solution you now understand how to build or commission. Briefly describe what the solution would look like.

3. **Ethics:** Of the responsible AI principles covered in this course, which do you think is most frequently neglected in practice? Why? What would you do differently if you were an AI product manager?

4. **Next steps:** What is the one skill or certification you plan to pursue next? Why?

---

## Part 5 — Exam Registration and Plan (10 minutes)

### Task 5.1 — Register for AI-900

Navigate to:

`https://learn.microsoft.com/en-us/certifications/exams/ai-900`

Click "Schedule exam" and identify available testing options:

- **Online proctored:** Test from your home or office with webcam monitoring
- **In-person testing center:** Find a Pearson VUE testing center near Fort Worth, TX

**Record:**

1. Your preferred exam delivery format and reason
2. Your target exam date (within 60 days of course end recommended)
3. Total exam cost and whether you qualify for any discounts (Microsoft Student/ESI discounts available)

### Task 5.2 — Student Discount Information

Microsoft Azure certifications are significantly discounted for students. To access the discount:

1. Verify your educational status at `https://azure.microsoft.com/en-us/free/students/`
2. Check with TXWES IT or the CS department — some institutions have ESI (Enterprise Skills Initiative) agreements that provide free exam vouchers

**Record:** Whether a student discount or free voucher is available to you and the source.

---

## Lab Submission Requirements

Submit a single PDF document containing:

1. **Part 1:** Completed confidence rating tables and five gap topic paragraphs
2. **Part 2:** Microsoft Learn knowledge check results (three items per module)
3. **Part 3:** Simulation score, missed question analysis
4. **Part 4:** Portfolio inventory table and 400–500 word reflection essay
5. **Part 5:** Exam registration plan with target date and cost information

**Grading Rubric:**

| Component | Points |
|---|---|
| Self-assessment tables complete; gap paragraphs demonstrate understanding | 20 |
| Microsoft Learn knowledge checks completed and recorded | 15 |
| Practice simulation graded; missed question analysis thoughtful | 25 |
| Portfolio inventory complete; reflection essay shows genuine synthesis | 30 |
| Exam registration plan specific and committed | 10 |
| **Total** | **100** |

---

*Lab prepared by Professor Nash | Texas Wesleyan University | CIS-4330*

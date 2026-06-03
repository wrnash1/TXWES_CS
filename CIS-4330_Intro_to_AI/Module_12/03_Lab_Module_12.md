# Lab Activity: Module 12 — AI in Business: Use Cases and ROI

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe AI workloads and considerations (15-20%)

---

## Lab Overview

In this lab you will analyze AI business scenarios, categorize use cases, apply the build-versus-buy decision framework, calculate ROI, match business needs to Azure services, and evaluate an organization's AI maturity. No Azure subscription is required. All work is scenario-based analysis.

### Learning Objectives

By completing this lab you will be able to:

- Classify AI use cases into the four business value categories
- Apply the build-versus-buy decision framework to realistic scenarios
- Calculate and interpret AI ROI from cost and benefit data
- Match common business needs to the appropriate Azure AI service
- Assess organizational AI maturity and recommend next steps

### Time Estimate

Approximately 90–110 minutes.

---

## Part A: AI Use Case Categorization (20 points)

For each business scenario below, identify the AI use case category (Automation, Enhancement, Insights, or New Products) and write 2–3 sentences justifying your classification. Use the definitions from the reading guide.

### Scenario A1 (4 points)

A telecommunications company deploys an AI system that processes customer service call transcripts overnight and generates a daily report identifying the top five complaint themes, their frequency, and which customer segments are most affected. Human analysts review the report each morning to plan staffing and escalation priorities.

**Questions:**

1. What AI use case category does this represent?
2. Justify your classification in 2–3 sentences. Specifically address why this is not the same category as a system that automatically resolves complaints.

### Scenario A2 (4 points)

A regional bank replaces its paper-based loan application process with an Azure AI Document Intelligence system that extracts applicant name, income, employer, requested amount, and property address from uploaded PDF applications. The extracted data is written directly into the bank's loan origination system, eliminating manual data entry for approximately 400 applications per month.

**Questions:**

1. What AI use case category does this represent?
2. Justify your classification. What specific characteristic of this use case places it in this category rather than the Enhancement category?

### Scenario A3 (4 points)

A retail clothing company builds a mobile app feature that uses the customer's past purchases, browsing history, and real-time inventory to suggest three outfit combinations the customer has not seen before. The feature generates revenue through increased add-to-cart rates and did not exist before the AI system was built.

**Questions:**

1. What AI use case category does this represent?
2. Justify your classification. Why does this scenario not belong in the Insights category?

### Scenario A4 (4 points)

A hospital system deploys an AI model that analyzes radiology scans and highlights regions that may indicate abnormalities. Radiologists still review every scan and make all diagnostic decisions; the AI output serves as a second-check tool that reduces the chance of a missed finding.

**Questions:**

1. What AI use case category does this represent?
2. Justify your classification. What would need to change about this deployment for it to become an Automation use case instead?

### Scenario A5 (4 points)

A manufacturing company runs historical sensor data from its assembly line equipment through an Azure Machine Learning model each week. The model predicts which machines have a greater than 70 percent probability of failure in the next 14 days, allowing maintenance teams to schedule preventive repairs before failures occur.

**Questions:**

1. What AI use case category does this represent?
2. Justify your classification. Identify the specific value proposition that this use case delivers that matches the definition of its category.

---

## Part B: Build vs Buy Decision Analysis (25 points)

Read each scenario. Recommend either (a) Azure Cognitive Services / prebuilt service, (b) Azure Machine Learning custom model, or (c) Azure OpenAI with prompt engineering. Justify your recommendation using the decision framework from the reading guide. Your justification must reference at least one specific factor from the framework.

### Scenario B1 (5 points)

A logistics company wants to analyze the sentiment of customer reviews submitted after each delivery. Reviews are written in English. The company receives approximately 3,000 reviews per week. No labeled training data currently exists. The company wants to be up and running within two weeks.

**Write your recommendation and justification.**

### Scenario B2 (5 points)

An insurance company wants to classify incoming claims documents into one of 14 proprietary damage categories that are specific to their business. These categories are not standard classifications used in any commercial NLP tool. The company has 45,000 labeled historical documents that have already been manually categorized by claims adjusters.

**Write your recommendation and justification.**

### Scenario B3 (5 points)

A law firm wants to build an internal tool that allows attorneys to paste in a contract section and ask questions such as "What are the termination conditions in this clause?" and "Does this indemnification language favor the vendor or the client?" The firm does not need the tool to learn firm-specific terminology — it needs to understand standard legal language.

**Write your recommendation and justification.**

### Scenario B4 (5 points)

A grocery chain wants to forecast weekly demand for each of 8,000 SKUs across 240 store locations. The chain has five years of weekly sales history, promotional calendars, and regional holiday data. Forecast accuracy is critical — overstock costs and stockout costs are both measurable and significant.

**Write your recommendation and justification.**

### Scenario B5 (5 points)

A startup wants to add a feature to its project management app that automatically detects the language a user is typing in and translates comments into the team's preferred language. The feature must support 30 languages. The startup has no training data and a two-person engineering team.

**Write your recommendation and justification.**

---

## Part C: ROI Calculation (20 points)

Use the AI ROI formula from the reading guide: ROI = (Value Realized minus Investment Cost) divided by Investment Cost, expressed as a percentage. Show your arithmetic for full credit.

### Problem C1 (10 points)

Southland Financial deploys an Azure AI Document Intelligence system to process mortgage loan applications. Use the data below to calculate first-year ROI.

**Investment Costs (Year 1):**

- Development and integration: $42,000
- Azure compute (API calls + storage): $8,400
- Change management and staff training: $6,200

**Value Realized (Year 1):**

- Labor cost savings: 3 FTEs redirected to higher-value work. Fully loaded cost per FTE = $58,000. 3 FTEs x $58,000 = $174,000
- Error reduction: Previous error rate was 4.2 percent on 2,400 applications per year. New error rate is 0.3 percent. Error correction cost = $215 per error.
- Speed improvement: Loan approval cycle shortened from 6 days to 18 hours. Revenue value of faster approvals = $31,000 annually based on reduced fallout rate.

**Questions:**

1. Calculate total investment cost.
2. Calculate total value realized. Show the error reduction calculation.
3. Calculate first-year ROI as a percentage.
4. In one sentence, interpret what this ROI means for the business case.

### Problem C2 (10 points)

A manufacturing company deploys an Azure Machine Learning predictive maintenance model. Use the data below to answer the questions.

**Investment Costs (Year 1):**

- ML model development: $95,000
- Data collection and labeling (sensor history): $28,000
- Azure ML compute (training + inference endpoint): $14,500
- Ongoing monitoring and quarterly retraining (annualized): $18,000

**Value Realized (Year 1):**

- Unplanned downtime prevention: The model prevented an estimated 4 equipment failures that would each have caused 18 hours of downtime. Production value of one hour of downtime = $4,200.
- Maintenance labor savings: Predictive scheduling reduced emergency maintenance labor by $22,000.
- Equipment lifespan extension: Estimated value of avoided premature equipment replacement = $35,000.

**Questions:**

1. Calculate total investment cost.
2. Calculate total value realized.
3. Calculate first-year ROI as a percentage.
4. The model development cost was $95,000. A project sponsor argues this is too high. Write 2–3 sentences explaining why a high first-year investment cost does not necessarily mean a bad ROI, and what would need to be true about Year 2 costs for this investment to look even better.

---

## Part D: Azure Service Matching (20 points)

Match each business need to the correct Azure AI service. Then write one sentence explaining what specifically makes that service the right choice for this need. Use Table 5 from the reading guide.

| # | Business Need | Your Azure Service | One-Sentence Explanation |
|---|---|---|---|
| 1 | A bank needs to automatically extract account number, transaction date, and amount from scanned paper check images | | |
| 2 | A call center wants to convert recorded customer support phone calls to searchable text transcripts | | |
| 3 | A subscription service wants to predict which customers are likely to cancel in the next 30 days based on their usage patterns | | |
| 4 | A fraud operations team needs to flag unusual patterns in financial transaction streams that deviate from normal behavior | | |
| 5 | An e-commerce site wants to recommend the next best product for each individual visitor based on real-time browsing behavior | | |
| 6 | A furniture manufacturer needs to automatically detect surface scratches and dents in product photos before packaging | | |
| 7 | A support portal wants to answer common customer questions using content from the company's FAQ document library | | |
| 8 | A marketing team needs to analyze thousands of social media comments to determine whether customer sentiment about a new product launch is positive, negative, or neutral | | |
| 9 | A media company wants to generate product descriptions for 50,000 catalog items using a language model | | |
| 10 | A professional services firm wants to search across 200,000 internal documents to find relevant case precedents by meaning, not just keyword | | |

---

## Part E: AI Maturity Model Analysis (15 points)

Read the organizational profile below and answer all three questions.

### Organizational Profile

Meridian Healthcare Group is a regional hospital network with 12 facilities and approximately 8,000 employees. Their current AI situation:

- Three separate departments have independently piloted AI tools in the past 18 months: the radiology department built a custom vision proof-of-concept for scan flagging (never deployed to production), the revenue cycle team integrated a prebuilt Azure AI Document Intelligence API for insurance form processing (live for 6 months, processing 500 documents per day), and the HR department tested an Azure OpenAI chatbot for employee policy questions (decommissioned after the pilot).
- There is no centralized AI governance committee or data platform.
- AI projects are funded and managed independently by each department.
- Model performance for the Document Intelligence deployment is not monitored — no alerts are configured and the team has not reviewed error rates since go-live.
- Data scientists in the radiology department want to expand the scan flagging model to production but have no formal deployment pipeline or model versioning process.

### Question E1 (5 points)

At which maturity stage (1, 2, 3, or 4) does Meridian Healthcare Group currently operate? Justify your answer in 3–4 sentences, citing specific evidence from the organizational profile.

### Question E2 (5 points)

The radiology team wants to move the scan flagging model to production. Based on the maturity model and the current state of Meridian's AI capabilities, identify two specific gaps that must be addressed before the model is deployed to production. For each gap, name the specific MLOps practice or governance element that is missing.

### Question E3 (5 points)

Meridian's CIO wants to reach Maturity Level 3 within 18 months. Write 3–4 sentences describing two concrete organizational actions the CIO should prioritize first. Explain why these actions are prerequisites for reaching Level 3.

---

## Answer Key and Grading Rubric

### Part A Rubric (20 points — 4 points each)

**A1:** Insights. The AI extracts patterns from data at scale (complaint themes and frequencies) that humans could not efficiently process manually. The system does not replace a human action — it surfaces evidence that humans then act on. This is not Automation because no task previously done by a human is being performed by the AI; the AI is creating new analytical output that did not exist before.

**A2:** Automation. The AI performs the specific task of data extraction previously done by loan officers manually entering data from paper applications. The key characteristic distinguishing this from Enhancement is that the AI completes the task end-to-end with no human involvement — the extracted data flows directly into the origination system. Enhancement would require a human to still make the extraction decision.

**A3:** New Products. The outfit recommendation feature is an entirely new product capability that did not exist before the AI was built. Unlike Insights (which surfaces patterns to inform decisions), this feature directly generates revenue through a consumer-facing product experience. The AI enables the product itself, not just analysis to support a human decision.

**A4:** Enhancement. The AI augments the radiologist's work by highlighting regions of interest but does not replace the diagnostic decision. The human makes the final clinical call on every scan. For this to become Automation, the AI would need to make the diagnostic determination itself without requiring radiologist review — a change that would raise significant regulatory and safety concerns.

**A5:** Insights. The value is predictive — the model extracts from historical sensor data a pattern (probability of failure) that human maintenance teams could not reliably identify through manual observation. The value proposition is evidence-based decision-making (schedule preventive maintenance) that was not previously possible at this scale or accuracy.

### Part B Rubric (25 points — 5 points each)

**B1:** Azure Cognitive Services — specifically Azure AI Language sentiment analysis. Standard task (sentiment analysis) covered by prebuilt models; no training data available; deployment timeline of two weeks favors prebuilt. Award full credit for any answer that correctly identifies the prebuilt service route and cites at least one framework factor (no training data, standard task, speed).

**B2:** Azure Machine Learning custom model (text classification). Proprietary categories not available in prebuilt models; 45,000 labeled documents provide sufficient training data; performance requirements for claims processing justify custom training. Award full credit for custom model recommendation with citation of proprietary categories and available labeled data.

**B3:** Azure OpenAI with prompt engineering. General-purpose language task (contract Q&A, interpretation); no firm-specific vocabulary requiring custom training; prompt engineering with GPT-4 handles legal language without training data. Award full credit for Azure OpenAI recommendation with citation of general language task and absence of proprietary domain requirements.

**B4:** Azure Machine Learning (AutoML or custom time series). Proprietary multi-variate forecasting problem; five years of labeled history exists; performance requirements are critical and measurable; prebuilt models cannot incorporate promotional and holiday data. Award full credit for custom ML recommendation with citation of available training data and performance-critical requirements.

**B5:** Azure Cognitive Services — Azure AI Translator. Standard multi-language translation task fully covered by prebuilt service; no training data; small engineering team cannot support custom model development. Award full credit for prebuilt recommendation with citation of standard task and resource constraints.

### Part C Rubric (20 points)

**C1:**

- Total investment: $42,000 + $8,400 + $6,200 = $56,600
- Error calculation: Previous errors = 4.2% x 2,400 = 100.8 errors. New errors = 0.3% x 2,400 = 7.2 errors. Reduction = 93.6 errors x $215 = $20,124
- Total value: $174,000 + $20,124 + $31,000 = $225,124
- ROI: ($225,124 - $56,600) / $56,600 x 100 = 297.9%
- Interpretation: The investment returns approximately three times its cost in the first year, making it a financially strong business case. Award 2 points for each step; accept minor rounding.

**C2:**

- Total investment: $95,000 + $28,000 + $14,500 + $18,000 = $155,500
- Downtime savings: 4 failures x 18 hours x $4,200 = $302,400
- Total value: $302,400 + $22,000 + $35,000 = $359,400
- ROI: ($359,400 - $155,500) / $155,500 x 100 = 131.1%
- Year 2 argument: In Year 2, development and data labeling costs ($123,000 combined) are not repeated. Only recurring costs (compute ~$14,500 + monitoring ~$18,000 = ~$32,500) remain. If value held constant, Year 2 ROI would exceed 1,000%. Award 3 points for correct calculation; 3 points for Year 2 analysis with specific recurring vs one-time cost distinction.

### Part D Rubric (20 points — 2 points each)

1. Azure AI Document Intelligence — purpose-built for extracting structured fields from unstructured document images including checks and forms.
2. Azure AI Speech — provides speech-to-text transcription for audio recordings including call center calls.
3. Azure Machine Learning — binary classification model trained on customer usage features predicts churn probability.
4. Azure Anomaly Detector — designed specifically for time series anomaly detection in streaming data such as financial transactions.
5. Azure Personalizer — real-time contextual bandit model recommends next best action or item for individual users based on context.
6. Azure Custom Vision — image classification/object detection model trained on custom defect categories specific to the manufacturer's products.
7. Azure AI Language Question Answering — knowledge base built from FAQ documents answers common questions using the source content.
8. Azure AI Language — sentiment analysis API classifies text as positive, negative, or neutral at scale.
9. Azure OpenAI (GPT-4) — text generation capability produces natural language product descriptions from structured product attributes.
10. Azure AI Search with Azure OpenAI — semantic/vector search indexes document collections and retrieves by meaning rather than keyword match.

### Part E Rubric (15 points)

**E1 (5 pts):** Maturity Level 1 — Experimentation. Evidence: multiple independent pilots with no formal governance, one production deployment with no monitoring, one decommissioned pilot, one never-deployed proof-of-concept, no centralized data platform or AI platform team. The organization has not yet established the MLOps practices (versioning, monitoring, automated deployment) that define Level 2. Award full credit for Level 1 with at least two specific pieces of evidence.

**E2 (5 pts):** Any two of the following gaps with their named MLOps practice:

- No model versioning process → MLOps practice: model registry and versioning
- No deployment pipeline → MLOps practice: automated deployment / CI-CD for ML
- No performance monitoring on live model → MLOps practice: inference monitoring and alerting
- No formal governance review for clinical AI → governance element: responsible AI review board / model card requirement

**E3 (5 pts):** Priority actions for Level 3 include establishing a centralized AI governance committee (prerequisite: Level 3 requires formal responsible AI governance; without central oversight, deployments remain ungoverned and inconsistent) and building a shared data platform or MLOps infrastructure (prerequisite: Level 3 requires multiple AI systems sharing infrastructure; without shared data and deployment infrastructure, each project reinvents the same capabilities). Award full credit for any two well-justified actions tied to Level 3 requirements.

---

## Submission Requirements

Submit a single document to the course LMS by the posted deadline containing:

- Part A: Classification answers and justifications for all five scenarios
- Part B: Recommendations and justifications for all five scenarios
- Part C: Arithmetic work and answers for both problems
- Part D: Completed matching table with explanations
- Part E: Answers to all three maturity model questions

---

## Grading Rubric Summary

| Part | Points | Criteria |
|------|--------|----------|
| A — Use Case Categorization | 20 | Correct category and accurate justification citing category definition |
| B — Build vs Buy | 25 | Correct recommendation and justification citing at least one framework factor |
| C — ROI Calculation | 20 | Correct arithmetic shown; interpretation is accurate |
| D — Azure Service Matching | 20 | Correct service and valid one-sentence explanation |
| E — Maturity Analysis | 15 | Correct stage with evidence; gaps named with specific MLOps terms; actions tied to Level 3 requirements |
| **Total** | **100** | |

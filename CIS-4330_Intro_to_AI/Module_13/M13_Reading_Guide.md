# Reading Guide: Module 13 — AI Applications in Business

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Overview

Module 13 shifts focus from technical implementation to strategic application. These readings build your understanding of how AI creates measurable business value across industries, how organizations make investment decisions, and how AI projects are managed effectively. Budget approximately 90 minutes for all readings and responses.

---

## Required Readings

### Reading 1 — Microsoft: AI for Industry

**URL:** `https://www.microsoft.com/en-us/industry/ai`

**Focus Areas:**

- How Microsoft describes AI value propositions by industry
- Azure AI services mapped to industry use cases
- Customer case study examples

**Annotation Prompts:**

1. Pick one industry from the Microsoft page. What specific AI capability does Microsoft highlight as the primary value driver for that industry?
2. What Azure service is most prominently featured for your chosen industry?
3. Does Microsoft address ROI or business outcomes, or primarily focus on technical capabilities?

---

### Reading 2 — Harvard Business Review: "Why So Many High-Profile Digital Transformations Fail"

**Note:** Access through TXWES Library → HBR database

**Alternatively:** Search for the article title at `https://hbr.org`

**Focus Areas:**

- Organizational readiness for AI transformation
- Why technology alone does not drive value
- Change management and process redesign alongside AI

**Annotation Prompts:**

1. What does the article identify as the most common reason AI/digital transformation fails?
2. What role does organizational culture play according to the article?
3. How does this reading change or reinforce your view of AI ROI calculations?

---

### Reading 3 — McKinsey: Notes from the AI Frontier

**URL:** `https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai`

**Focus Areas:**

- AI adoption rates across industries
- Reported business value from AI deployments
- Talent and infrastructure challenges

**Annotation Prompts:**

1. Which industry reports the highest AI adoption rate?
2. What is the most common AI use case cited across industries?
3. What gap does McKinsey report between expected and realized AI value?

---

### Reading 4 — CRISP-DM Reference Guide

**URL:** `https://www.datascience-pm.com/crisp-dm-2/`

**Focus Areas:**

- The six phases of CRISP-DM
- Iteration between phases
- Deliverables produced in each phase

**Annotation Prompts:**

1. Which two CRISP-DM phases are most often skipped by organizations eager to start modeling, and what problems does skipping them cause?
2. In what phase would you identify that the training data is not sufficient for the required accuracy?
3. How does CRISP-DM's iterative nature differ from traditional waterfall project management?

---

## Key Concept Summaries

### AI Use Cases by Industry

Read the following summaries carefully. The AI-900 exam expects you to match Azure AI services to appropriate business scenarios.

#### Healthcare AI

| Use Case | Description | Azure Service |
|---|---|---|
| Medical imaging analysis | Detect anomalies in X-ray, MRI, CT images | Azure AI Vision, Custom Vision |
| Clinical text extraction | Extract diagnoses and medications from notes | Azure AI Language, Text Analytics for Health |
| Patient readmission prediction | Flag high-risk patients at discharge | Azure Machine Learning |
| Drug discovery acceleration | Screen molecular candidates | Azure ML + HPC |

Key regulatory note: In healthcare, AI outputs are clinical decision support, not clinical decisions. The physician retains legal responsibility.

#### Finance AI

| Use Case | Description | Azure Service |
|---|---|---|
| Real-time fraud detection | Score transactions in <100ms | Azure ML + Stream Analytics |
| Credit underwriting | Predict default probability | Azure ML |
| Customer service chatbots | Handle tier-1 banking queries | Azure AI Bot Service + Language |
| Algorithmic risk reporting | Real-time portfolio risk aggregation | Azure Synapse + ML |

Key regulatory note: Credit AI must comply with ECOA and FCRA (US). Disparate impact testing is required.

#### Retail AI

| Use Case | Description | Azure Service |
|---|---|---|
| Product recommendations | Personalized product suggestions | Azure Personalizer |
| Demand forecasting | SKU-level inventory optimization | Azure ML (time series) |
| Visual shelf inspection | Detect out-of-stock shelves | Azure Computer Vision |
| Customer sentiment analysis | Analyze reviews and service feedback | Azure AI Language |

Key insight: Amazon attributes approximately 35% of revenue to its recommendation engine — the highest ROI AI application in retail.

#### Manufacturing AI

| Use Case | Description | Azure Service |
|---|---|---|
| Predictive maintenance | Predict equipment failure from sensor data | Azure IoT Hub + ML |
| Visual quality inspection | Detect product defects at line speed | Azure Custom Vision |
| Supply chain optimization | Forecast disruptions and optimize routing | Azure ML + Supply Chain |
| Energy optimization | Reduce factory energy consumption | Azure ML + IoT |

Key insight: Unplanned downtime in automotive manufacturing costs approximately $50,000 per minute. Predictive maintenance ROI is often proven within one year.

---

### The ROI Calculation Framework

Calculating AI ROI requires separating hope from evidence. Use this five-step framework:

**Step 1 — Define the Business Metric**

Name a specific, measurable outcome: fraud loss reduction, readmission rate, inventory carrying cost, defect rate. Avoid vague metrics like "improved customer experience."

**Step 2 — Establish the Baseline**

What is the current numerical performance on that metric? Without a baseline, ROI calculation is impossible.

**Step 3 — Estimate Realistic Impact**

Use one of three sources: published benchmarks from similar deployments, pilot program results, or vendor-provided case studies (discounted for optimism bias). A common rule of thumb: halve the optimistic estimate.

**Step 4 — Calculate Total Cost of Ownership (TCO)**

Include all cost categories:

- **Data costs:** Acquisition, licensing, storage, preparation labor
- **Development costs:** Data scientist time, ML engineer time, platform licenses
- **Infrastructure costs:** Cloud compute, storage, API calls
- **Integration costs:** Connecting to existing systems — often the largest underestimated cost
- **Ongoing costs:** Monitoring, maintenance, retraining, support

**Step 5 — Compute ROI**

ROI = (Annual Value − Annual TCO) / Annual TCO × 100%

Also compute **payback period** = Total Implementation Cost / Monthly Net Value Delivered.

Positive ROI is necessary but not sufficient. Consider also: time to first value, strategic alignment, and opportunity cost of not investing.

---

### Build vs. Buy Decision Matrix

| Criterion | Build | Buy / License | Hybrid |
|---|---|---|---|
| Competitive differentiation | High | Low | Medium |
| Proprietary data advantage | Yes | No | Sometimes |
| Speed to value required | Low priority | High priority | Medium |
| Customization required | High | Low | Medium |
| Internal AI talent | Available | Scarce | Partial |
| Long-term cost | Higher upfront, lower per-unit | Lower upfront, higher ongoing licensing | Balanced |

**Common Hybrid Pattern:** Use Azure AI Services (buy) as the AI infrastructure layer. Build custom models on Azure ML (build) using your proprietary data. Integrate via custom APIs.

---

### CRISP-DM Project Framework

CRISP-DM (Cross-Industry Standard Process for Data Mining) is the dominant AI project lifecycle framework. Unlike software development's waterfall or even Agile, CRISP-DM explicitly accounts for the exploratory uncertainty of data science.

**Phase 1 — Business Understanding**

- Define business objectives and translate them into data science goals
- Identify success criteria (both technical and business)
- Produce: project charter, success criteria document

**Phase 2 — Data Understanding**

- Identify required data sources
- Assess data quality, completeness, and relevance
- Produce: data exploration report, data quality findings

**Phase 3 — Data Preparation**

- Clean, merge, and transform data
- Engineer features
- Produce: training dataset, feature documentation

**Phase 4 — Modeling**

- Select modeling techniques
- Build and train models
- Tune hyperparameters
- Produce: trained models, parameter settings, training metrics

**Phase 5 — Evaluation**

- Assess models against business success criteria
- Determine if business goals are met
- Produce: evaluation report, go/no-go decision

**Phase 6 — Deployment**

- Plan deployment architecture
- Monitor and maintain in production
- Produce: deployment plan, final report

**Key insight:** CRISP-DM loops back. Discovering poor data quality in Phase 2 may require revisiting Phase 1 to reframe the problem. Discovering unacceptable accuracy in Phase 5 may require looping back to Phase 3 for more feature engineering.

---

## Vocabulary Builder

Define each term in your own words:

1. ROI (Return on Investment)
2. TCO (Total Cost of Ownership)
3. CRISP-DM
4. Collaborative filtering
5. Content-based filtering
6. Predictive maintenance
7. Clinical decision support
8. Disparate impact
9. Build-vs-buy
10. Demand forecasting
11. Visual inspection AI
12. Algorithmic trading
13. Payback period
14. Azure Personalizer
15. Change management

---

## Reflective Questions

Answer each question in 3–5 sentences:

**Question 1:** A retail company wants to deploy a demand forecasting AI to reduce inventory. Their supply chain director says: "We already have 40 years of sales data. The model should be easy." What does this statement overlook about data quality and preparation costs?

**Question 2:** A hospital data science team achieves 94% accuracy on a readmission prediction model in testing. A clinician says: "94% sounds great, but I'm not changing my discharge decisions based on a black box." How should the team respond? What aspects of responsible AI should the model demonstrate to earn clinician trust?

**Question 3:** Which of the four industries covered in this module do you think offers the highest near-term ROI opportunity for AI, and why? Cite at least one specific use case and estimate order-of-magnitude business value.

**Question 4:** A startup CEO says she wants to "build everything in-house to maintain full control." What risks does this approach carry for a company with limited AI engineering resources? When would building in-house be clearly the right choice despite the risks?

---

## Case Study — Northwell Health Readmission AI

Read the following brief case summary and answer the questions that follow.

Northwell Health, New York's largest health system, deployed an AI model to predict patient readmissions. The model used 24 features from the EHR — lab values, vital signs, diagnosis codes, and prior utilization. After deployment with care coordinator follow-up protocols, Northwell reported a 5% reduction in 30-day readmissions for the high-risk population identified by the model.

**Case Questions:**

1. Using the ROI framework from the lecture, sketch a back-of-envelope ROI calculation. Assume 20,000 annual discharges, 15% baseline readmission rate, and $10,000 average cost per readmission.

2. The model uses 24 features from the EHR. What data preparation steps were almost certainly required before training? Name at least four.

3. Northwell noted that the model worked significantly better for some patient populations than others. What does this suggest about data representation in the training set?

---

## AI-900 Exam Alignment

Module 13 content maps to the following AI-900 exam domain:

**Domain: Describe features of AI workloads and considerations (15–20%)**

Key topics:

- Identifying appropriate AI use cases for common business scenarios
- Understanding that AI solutions must consider fairness, reliability, and accountability
- Recognizing Azure AI services relevant to industry scenarios

**Exam Tip:** The AI-900 frequently presents scenario questions like "A bank wants to automatically detect fraudulent transactions in real time. Which Azure service is most appropriate?" Know the primary use case for each Azure AI service category.

---

*Reading Guide prepared by Professor Nash | Texas Wesleyan University | CIS-4330*

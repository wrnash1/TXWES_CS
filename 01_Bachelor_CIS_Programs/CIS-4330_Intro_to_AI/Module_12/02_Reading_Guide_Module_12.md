# Reading Guide: Module 12 - AI in Business: Use Cases and ROI

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

**AI-900 Domain:** Describe AI workloads and considerations (15-20%)

---

## Overview

This reading guide covers AI business use case categories, the build-versus-buy decision framework, AI ROI measurement, common Azure AI use case patterns, and AI adoption maturity. These topics appear in AI-900 scenario questions that require matching a business need to the appropriate AI approach or Azure service. Complete the study checklist before the lab activity.

---

## Section 1: Core Vocabulary

**AI workload**
A category of business task that AI can perform or support. Common workloads: document processing, customer service, predictive analytics, image analysis, speech processing, anomaly detection.

**Automation**
An AI application category where AI performs tasks previously done by humans, reducing cost and increasing throughput. Example: extracting invoice fields with Azure Document Intelligence rather than manual data entry.

**Enhancement (AI-assisted)**
An AI application category where AI augments human work rather than replacing it. Example: a radiologist using AI-flagged scan regions to prioritize review, not to replace diagnosis.

**Insights**
An AI application category where AI extracts actionable patterns from data at a scale humans cannot match. Example: customer churn prediction from behavioral signals.

**Build vs buy (in AI)**
The decision between using a prebuilt Azure AI service versus building a custom model. Prebuilt services are faster but less flexible; custom models require training data but can address domain-specific requirements.

**ROI (Return on Investment)**
A measure of financial return relative to cost. In AI: (Value Realized minus Investment Cost) divided by Investment Cost, expressed as a percentage.

**Data drift**
The phenomenon where the statistical properties of production data change over time, degrading a model's performance. Requires ongoing monitoring and periodic retraining.

**Model drift**
A broader term for model performance degradation in production, encompassing data drift and concept drift (when the underlying relationship between features and target changes).

**Baseline metric**
A measurement of current performance before an AI system is deployed, used to calculate the improvement (and thus the value) the AI system provides.

**MLOps**
Machine Learning Operations. The set of practices for reliably deploying, monitoring, and maintaining ML models in production. Analogous to DevOps for software engineering.

**AI maturity model**
A framework describing stages of organizational AI adoption, from initial experimentation to AI-native operations.

---

## Section 2: Comparison Tables

### Table 1: AI Use Case Categories

| Category | Definition | Value Proposition | Azure Service Example |
|---|---|---|---|
| Automation | AI replaces human task execution | Lower cost, faster speed, 24/7 availability | Document Intelligence, CLU bot |
| Enhancement | AI augments human workers | Higher quality or volume per worker | Azure ML model assisting clinician |
| Insights | AI extracts patterns from data | Evidence-based decisions not previously possible | Azure ML churn prediction |
| New products | AI enables entirely new offerings | New revenue or competitive differentiation | Azure OpenAI-powered SaaS product |

### Table 2: Build vs Buy Decision Framework

| Scenario | Recommended Approach | Reason |
|---|---|---|
| Standard task (sentiment analysis, OCR, translation) | Use Azure Cognitive Services (prebuilt) | No training data needed; deployed in days |
| Domain-specific categories not in prebuilt models | Build custom model (Azure ML / Custom Vision) | Prebuilt models cannot recognize proprietary patterns |
| General language task (summarization, Q&A, drafting) | Azure OpenAI with prompt engineering | LLM handles diverse language tasks with prompting |
| Proprietary training data available; performance critical | Custom Azure ML model | Training data exists; control needed over model |
| No labeled data available; need rapid deployment | Azure Cognitive Services or Azure OpenAI | Prebuilt services require no training data |

### Table 3: AI Investment Cost Components

| Cost Type | Description | Notes |
|---|---|---|
| Development and integration | Engineering work to build, train, and connect AI to business systems | Typically highest upfront cost |
| Data collection and labeling | Acquiring, cleaning, and annotating training data | Often underestimated; critical for custom models |
| Azure compute | Training jobs, inference endpoints, storage | Ongoing; scales with usage |
| Maintenance and retraining | Monitoring performance; retraining as data drifts | Ongoing; often underbudgeted |
| Change management | Training users, updating processes, governance setup | Organizational, not technical |

### Table 4: AI ROI Value Components

| Value Type | How to Measure | Example |
|---|---|---|
| Labor cost savings | FTEs displaced or redirected x fully loaded cost | Invoice processing bot saves 8 FTE-equivalent hours per day |
| Quality improvement | Error rate reduction x cost per error | Fraud model increases detection rate from 60% to 88% |
| Speed improvement | Time reduction x value per time unit | Loan approval time from 3 days to 4 hours |
| New revenue | Incremental revenue from AI-enabled products | Personalization engine increases conversion rate by 3% |
| Cost avoidance | Cost of prevented failures or violations | Predictive maintenance prevents unplanned factory downtime |

### Table 5: Common AI Use Case Patterns and Azure Services

| Business Need | AI Pattern | Azure Service |
|---|---|---|
| Extract data from invoices, forms, contracts | Document processing | Azure AI Document Intelligence |
| Answer customer questions automatically | FAQ chatbot | Azure AI Language Question Answering |
| Route customer requests to correct department | Intent classification | Azure AI Language CLU |
| Predict customer churn | Binary classification | Azure Machine Learning |
| Predict next month's demand | Regression / time series | Azure Machine Learning AutoML |
| Detect unusual transactions | Anomaly detection | Azure Anomaly Detector |
| Quality control image inspection | Custom image classification | Azure Custom Vision |
| Transcribe customer call audio | Speech-to-text | Azure AI Speech |
| Analyze customer review sentiment | Sentiment analysis | Azure AI Language |
| Generate product descriptions | Text generation | Azure OpenAI (GPT-4) |
| Recommend products to users | Personalization | Azure Personalizer |
| Search documents by meaning | Knowledge mining | Azure AI Search + Azure OpenAI |

---

## Section 3: AI Adoption Maturity Model

Organizations adopt AI progressively across four stages:

**Stage 1 — Experimentation:** Individual projects using prebuilt services or open-source tools. No formal governance. Proof-of-concept focus. No production deployments.

**Stage 2 — Operationalization:** First production AI deployments. Beginning MLOps practices: model versioning, automated deployment, performance monitoring. Integration with business processes.

**Stage 3 — Scaling:** Multiple AI systems deployed across business units. Shared data platform. Formal responsible AI governance. Centralized AI platform team supporting multiple product teams.

**Stage 4 — AI-Native:** AI embedded in core business processes. Organization-wide data literacy. Continuous learning loops where production feedback automatically improves models.

---

## Section 4: AI-900 Exam Tips

1. AI use case categories (automation, enhancement, insights, new products) appear in scenario questions asking what type of AI value a described application creates. Know all four with examples.

2. The build-versus-buy decision is tested through scenarios. When a scenario describes a standard task (sentiment analysis, OCR), the answer is prebuilt Azure Cognitive Services. When it describes proprietary categories requiring custom training, the answer is Azure ML or Custom Vision.

3. Baseline metrics are essential to ROI measurement. If a scenario asks how an organization knows its AI system created value, the answer requires a pre-deployment baseline measurement.

4. Data drift and model drift are why AI models require ongoing monitoring and retraining. When a scenario describes a model that degraded in performance over time, the answer involves data drift.

5. Azure Document Intelligence (formerly Form Recognizer) is the service for extracting structured data from unstructured documents. When a scenario describes processing invoices, receipts, or forms at scale, this is the answer.

6. Azure Personalizer is the service for real-time personalization — recommending the next best action or content item for an individual user based on context and behavior.

7. MLOps encompasses the practices for deploying, monitoring, and maintaining ML models in production. It includes automated retraining, A/B testing model versions, and performance alerting.

8. Human-in-the-loop (HITL) is appropriate when AI systems make high-stakes decisions. The AI reduces workload; the human makes the final call. This is the appropriate design for medical diagnosis AI, credit denial AI, and criminal justice AI.

---

## Section 5: Required Reading

**Microsoft Learn — Introduction to AI technology for business leaders:**
learn.microsoft.com/en-us/training/paths/ai-technology-for-business-leaders/

**Microsoft Learn — Identify common AI workloads:**
learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/

---

## Section 6: Study Checklist

- [ ] Name and define all four AI use case categories with one example each.
- [ ] Explain the build-versus-buy decision for AI using Table 2.
- [ ] List the five cost components of an AI investment.
- [ ] Explain why baseline metrics are required to calculate AI ROI.
- [ ] Match five business needs from Table 5 to their Azure services without referring to notes.
- [ ] Explain data drift and why it requires ongoing model maintenance.
- [ ] Describe the four stages of the AI maturity model.
- [ ] Complete the Module 12 quiz.
- [ ] Complete the Module 12 lab.
- [ ] Post initial discussion by Wednesday 11:59 PM and respond to two peers by Sunday 11:59 PM.

---

## Section 7: Supplemental Resources

**1. Microsoft Learn — AI strategy for business leaders**
<https://learn.microsoft.com/en-us/training/paths/ai-technology-for-business-leaders/>
Microsoft's official learning path covering AI business value, use case selection, ROI measurement, and responsible AI considerations for leaders. Directly maps to the four AI value categories and the build-versus-buy framework covered in Module 12.

**2. McKinsey Global Institute — The Age of AI: How companies are really deploying AI**
<https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai>
Annual survey-based report tracking real enterprise AI adoption rates, value realization patterns, and common barriers. Provides real-world context for the AI maturity model and ROI concepts covered in this module; useful for the discussion board post.

**3. Azure Architecture Center — MLOps maturity model**
<https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/mlops-maturity-model>
Microsoft's official MLOps maturity model guide mapping from Level 0 (no automation) through Level 5 (full automated retraining). Provides the technical foundation behind the AI maturity stages covered in Section 3 and directly relevant to Part E of the lab.

---

End of Reading Guide — Module 12

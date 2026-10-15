# Video Script: Module 12 - AI in Business: Use Cases and ROI

## Course: CIS-4330 Introduction to AI | Texas Wesleyan University

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Harvard CS50 &bull; Artificial Intelligence with Python &bull; Module 12</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLhQjrBD2T382Nz7z1AEXmioc27axa19Kv" title="Harvard CS50 &bull; Artificial Intelligence with Python" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Harvard CS50 &bull; Artificial Intelligence with Python</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AI-900 Domain:** Describe AI workloads and considerations (15-20%)

---

## Opening

Welcome back. Professor Nash here, and this is Module 12. We have now covered the technical foundations of AI — machine learning, deep learning, computer vision, NLP, Azure Cognitive Services, Azure ML, and generative AI. This module steps back from implementation and asks: when should a business adopt AI, what does it cost, how do you measure the value, and how do you make the build-versus-buy decision? These are the business questions that data scientists, product managers, and executives wrestle with on every AI project. Understanding them will make you a more effective AI practitioner — and they appear on AI-900 in the form of scenario questions about AI use case selection. Let us get into it.

---

## AI Business Use Case Categories

AI adds value to businesses through four broad categories of application. Knowing these categories helps you quickly recognize and classify AI use cases in exam scenarios and in real project work.

**Category 1 — Automation:** AI performs tasks previously done by humans, reducing cost and increasing throughput. Examples: document processing (extracting invoice fields with Azure Form Recognizer), customer inquiry routing (CLU-based intent classification), quality control inspection (custom vision on manufacturing lines). The value proposition: same output at lower cost, faster speed, or 24/7 availability.

**Category 2 — Enhancement:** AI augments human work, making people more effective rather than replacing them entirely. Examples: AI-assisted code review, radiologist AI that pre-flags regions of interest in X-rays, writing assistants that generate drafts for human editors. The value proposition: same human labor produces higher-quality or higher-volume output.

**Category 3 — Insights:** AI extracts patterns from data at a scale humans cannot match. Examples: customer churn prediction from behavioral data, demand forecasting from sales history, fraud anomaly detection in transaction streams. The value proposition: decisions are made on evidence the business could not previously access or act on in time.

**Category 4 — New Products and Services:** AI enables entirely new product categories that did not exist without it. Examples: personalized recommendation engines, real-time language translation apps, generative AI-powered creative tools. The value proposition: new revenue streams or competitive differentiation.

For AI-900, these categories help you reason through scenario questions: "A company wants to reduce the time its accountants spend on invoice data entry" — that is automation. "A hospital wants to help radiologists prioritize scan review" — that is enhancement.

---

## The Build vs Buy Decision

When a business decides to adopt AI, one of the first decisions is whether to use a prebuilt capability or build a custom model. This is the build-versus-buy decision in AI, and it is directly tested on AI-900.

**Use prebuilt Azure Cognitive Services when:**

- The task is a standard AI task that Microsoft has already trained a model for — sentiment analysis, OCR, speech transcription, language detection.
- No labeled training data is available or practical to collect.
- Time to deployment is a priority — days or weeks, not months.
- The domain does not require specialized knowledge the prebuilt model lacks.

**Build a custom model with Azure ML or Custom Vision when:**

- The task involves proprietary categories not in any prebuilt model — custom defect detection, proprietary document layouts, domain-specific entity types.
- Sufficient labeled training data is available.
- Performance requirements exceed what prebuilt models achieve in this domain.
- The organization needs ongoing control over model versions and updates.

**Use Azure OpenAI with prompt engineering when:**

- The task is a general-purpose language task — summarization, drafting, Q&A, translation — that a powerful LLM can handle with the right prompt.
- Speed to value matters and training data is not available.
- The task evolves frequently and retraining a custom model would be impractical.

The decision is a spectrum, not binary. A single business application may use prebuilt services for some capabilities (language detection, speech-to-text) and custom models for others (proprietary entity extraction).

---

## Measuring AI ROI

Executives want to know if AI investments pay off. Measuring AI return on investment requires identifying both the costs and the value realized — and being honest about both.

**Cost components:**

Development and integration — the engineering work to build, train, and integrate the model. For custom ML models, this includes data collection, labeling, feature engineering, model development, evaluation, and deployment. For prebuilt services, this is primarily API integration.

Compute costs — Azure ML training jobs, inference endpoints, data storage. These are ongoing and scale with usage.

Data costs — acquiring, cleaning, and labeling training data. Often the most underestimated cost.

Maintenance — models degrade over time as data distributions shift (called data drift or model drift). Periodic retraining and monitoring are ongoing costs.

**Value components:**

Labor cost savings — the most direct: if AI automates a task that cost 10 FTEs, the labor savings are calculable.

Quality improvement — error rate reduction translates to downstream savings. A fraud model that increases fraud detection from 60% to 88% has a measurable dollar value per prevented fraud event.

Speed improvement — faster processing enables faster decisions, which may have revenue value.

New revenue — if AI enables a product or service that did not previously exist, the incremental revenue is part of the ROI calculation.

Cost avoidance — AI preventing errors, regulatory violations, or safety incidents has a value even though no cash is directly generated.

**ROI challenges:** Many AI benefits are indirect or qualitative. Customer satisfaction improvements, brand reputation gains, and employee productivity are real but harder to quantify. Establishing baseline metrics before deployment is essential to measuring improvement afterward.

---

## Common AI Business Use Case Patterns

Let me walk through the most common patterns you will encounter in AI-900 scenario questions, with the correct Azure service for each.

**Document processing and extraction:** Extracting structured data from unstructured documents — invoices, forms, contracts, medical records. Azure service: Azure AI Document Intelligence (formerly Form Recognizer).

**Customer service automation:** Routing, triaging, and answering customer inquiries. Azure service: Azure Bot Service with CLU and Question Answering.

**Predictive analytics:** Predicting future events or values from historical data — churn, demand, risk scores. Azure service: Azure Machine Learning (AutoML or custom models).

**Anomaly detection:** Identifying unusual patterns in time series data — fraud, equipment failure, network intrusion. Azure service: Azure Anomaly Detector.

**Image and video intelligence:** Quality control inspection, object counting, safety monitoring. Azure service: Azure Computer Vision or Custom Vision.

**Content and sentiment analysis:** Understanding customer feedback, reviews, support tickets. Azure service: Azure AI Language sentiment analysis and opinion mining.

**Personalization:** Recommending products, content, or actions to individual users based on behavior. Azure service: Azure Personalizer.

**Knowledge mining:** Extracting insights from large document collections — contracts, research papers, support logs. Azure service: Azure AI Search with Azure AI enrichment.

---

## AI Adoption Maturity

Organizations adopt AI along a maturity curve. Understanding where an organization sits on this curve informs the right AI strategy.

**Level 1 — Experimentation:** Individual projects using prebuilt services or open-source tools. No formal governance. Proof-of-concept focus.

**Level 2 — Operationalization:** First production AI deployments. Beginning to establish MLOps practices: model versioning, monitoring, automated retraining. Integration with business processes.

**Level 3 — Scaling:** Multiple AI systems deployed across business units. Shared data infrastructure. Formal responsible AI governance. Centralized AI platform team.

**Level 4 — AI-Native:** AI embedded in core business processes. Organization-wide data literacy. Continuous learning loops where AI systems improve from production feedback.

Most enterprises are currently between Levels 1 and 3. The Azure AI platform is designed to support all four levels, with Azure ML handling the operationalization infrastructure, Azure AI Services handling rapid deployment of standard capabilities, and Azure Governance tools handling responsible AI compliance.

---

## Module Summary

Let me summarize Module 12.

AI business value falls into four categories: automation, enhancement, insights, and new products. The build-versus-buy decision depends on whether prebuilt services cover the use case, whether proprietary training data is available, and whether time to value is a priority.

AI ROI is measured by comparing investment costs (development, compute, data, maintenance) to value realized (labor savings, quality improvement, new revenue). Many AI benefits are difficult to quantify, making baseline measurement before deployment essential.

Common AI use case patterns map to specific Azure services: document processing to Document Intelligence, customer service to Bot Service, predictive analytics to Azure ML, image intelligence to Computer Vision.

See you in Module 13, where we cover data preparation and feature engineering — the work that must happen before any model can be trained.

---

## References

- Microsoft Learn — Introduction to AI technology for business leaders: learn.microsoft.com/en-us/training/paths/ai-technology-for-business-leaders/
- Microsoft Learn — Identify common AI workloads: learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/

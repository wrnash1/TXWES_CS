# Video Script: Module 13 — AI Applications in Business

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Production Notes

- **Runtime Target:** 28–32 minutes
- **Slide Deck:** M13_Slides.pptx
- **Graphics:** Industry case study cards; ROI formula walkthrough; build-vs-buy matrix
- **Tone:** Strategic and managerial; accessible to non-technical students

---

## SEGMENT 1 — Hook and Module Overview (Slides 1–3) [3 min]

[ON CAMERA]

Welcome to Module 13. Let me start with a number: $15.7 trillion. That is the projected contribution of artificial intelligence to the global economy by 2030, according to PricewaterhouseCoopers. AI is not just a technology story — it is an economics story.

But here is what that number does not tell you: most organizations that invest in AI do not see returns anywhere close to what the hype suggests. The difference between the companies that succeed and the companies that do not is almost never the algorithm. It is the business strategy, the implementation approach, and the organizational readiness.

Today we are going to focus on the strategic and managerial side of AI. This is Module 13, and it is designed equally for students going into technical roles and students going into business, management, or consulting roles.

[SLIDE 1: Title — "AI Applications in Business"]

[SLIDE 2: Module Learning Objectives]

By the end of this module you will be able to:

- Identify and describe AI use cases across healthcare, finance, retail, and manufacturing
- Apply a basic ROI calculation framework to an AI initiative
- Evaluate the build-vs-buy decision for AI solutions
- Describe best practices for AI project management
- Explain how Azure AI services enable rapid deployment of business AI solutions

[SLIDE 3: Why This Module Is Different]

Every other module in this course focuses on what AI can do technically. This module focuses on what AI should do strategically. There are three questions every business leader must answer before investing in AI:

1. What problem are we actually solving?
2. What does success look like in dollars and cents?
3. Is it smarter to build, buy, or partner?

If you cannot answer those questions clearly, you will waste money. If you can, you have a competitive advantage.

---

## SEGMENT 2 — AI in Healthcare (Slides 4–8) [6 min]

[SLIDE 4: Healthcare — The Opportunity and the Stakes]

Healthcare is one of the most data-rich and impact-rich domains for AI. Clinicians, hospitals, and payers are sitting on decades of patient records, imaging data, genomic sequences, and claims data. At the same time, healthcare has the highest stakes for errors: an AI misdiagnosis can cause real harm. This tension between opportunity and risk defines every healthcare AI discussion.

[SLIDE 5: Medical Imaging and Diagnostics]

The clearest early success story for AI in healthcare is medical imaging. Companies like Microsoft (through Azure AI Health), Google DeepMind, and specialized firms have built models that detect certain cancers in radiology images with accuracy matching or exceeding specialist radiologists.

The Azure AI Health service includes pre-built models for:

- De-identifying clinical text (removing PHI for research)
- Extracting structured data from unstructured clinical notes
- Detecting conditions in medical images using Computer Vision APIs

Important caveat: none of these AI tools replace the physician. In every regulated healthcare context, AI is a clinical decision support tool — the physician remains accountable for the decision.

[SLIDE 6: Predictive Readmission and Length of Stay]

Hospital readmission — a patient being discharged and then readmitted within 30 days — is a major quality and cost problem. Medicare penalizes hospitals for high readmission rates.

Machine learning models trained on historical patient data (diagnoses, medications, lab values, social determinants) can predict which patients are at high readmission risk at the time of discharge. Care coordinators can then prioritize follow-up calls and home visits for high-risk patients.

This is a classic supervised classification problem with a clear business metric: 30-day readmission rate. The ROI is calculable: if the intervention costs $200 per high-risk patient and prevents a readmission that costs the hospital $15,000 in penalties and care costs, the math is compelling.

[SLIDE 7: Drug Discovery and Genomics]

AI is compressing the drug discovery timeline from an average of 12 years down toward 5–7 years in some research tracks. Models screen molecular libraries for drug candidates, predict protein structures (AlphaFold was transformative here), and identify patient subpopulations most likely to respond to a therapy.

This is high-barrier work — the data requirements, regulatory environment, and domain expertise needed are intense. But the financial upside of getting a successful drug to market faster is worth hundreds of millions of dollars.

[SLIDE 8: Healthcare AI Challenges]

Before we move on, let me name the three biggest challenges specific to healthcare AI:

**Data quality:** Clinical records are notoriously messy — inconsistent coding, free text, missing values, and different EHR systems across facilities.

**Regulatory approval:** The FDA has created a specific pathway for AI-based software as a medical device (SaMD). Deploying a diagnostic AI without proper clearance is illegal.

**Bias and equity:** Models trained on historically underrepresented populations can produce systematically worse results for those groups. This is not just unfair — it is dangerous.

---

## SEGMENT 3 — AI in Finance (Slides 9–12) [5 min]

[SLIDE 9: Finance — AI as Competitive Infrastructure]

Finance was among the first industries to adopt machine learning, and today AI is not a competitive advantage in finance — it is table stakes. Every major bank, insurer, and investment firm uses AI for fraud detection, credit scoring, trading, and customer service.

[SLIDE 10: Fraud Detection]

Real-time fraud detection is the canonical machine learning use case in financial services. When you swipe your credit card, a model scores that transaction in under 100 milliseconds, assigning a probability that it is fraudulent. If the score exceeds a threshold, the transaction is blocked or flagged.

The business case is straightforward: fraud losses at major banks run in the billions of dollars annually. Even a modest improvement in detection rate translates to hundreds of millions in recovered losses.

Azure services relevant here include Azure Stream Analytics for real-time event processing and Azure Machine Learning for model training and deployment.

[SLIDE 11: Credit Scoring and Underwriting]

Traditional FICO-based credit scoring uses a limited set of variables. ML models for credit scoring incorporate thousands of variables — payment timing patterns, merchant categories, even behavioral features like time of day and device type — to produce more accurate default probability estimates.

The regulatory environment matters enormously here. In the US, credit decisions are subject to the Fair Credit Reporting Act and ECOA (Equal Credit Opportunity Act). An AI credit model that produces disparate impact on protected classes — even unintentionally — creates legal and regulatory exposure. Fairness and explainability are not optional in lending AI.

[SLIDE 12: Algorithmic Trading and Risk Management]

Algorithmic trading — using AI and ML models to make buy/sell decisions faster and more systematically than humans — represents a significant fraction of all equity market trading volume. Reinforcement learning is used in some sophisticated trading systems.

For risk management, AI models aggregate exposure across massive portfolios in real time, flag concentration risks, and run stress scenarios (what happens to this portfolio if interest rates spike by 200 basis points?). The 2008 financial crisis accelerated investment in risk AI because the consequence of inadequate risk monitoring was catastrophic and visible.

---

## SEGMENT 4 — AI in Retail (Slides 13–16) [4 min]

[SLIDE 13: Retail — The Recommendation Economy]

Roughly 35% of Amazon's revenue comes from its recommendation engine. Netflix estimates its recommendation system saves approximately $1 billion per year in customer retention. Recommendation AI may be the highest-ROI application in existence.

[SLIDE 14: Personalization and Recommendations]

Recommendation systems work by modeling what a customer is likely to want next based on their purchase history, browse history, demographic data, and the behavior of similar customers. The two dominant approaches are:

**Collaborative filtering:** "Users like you also bought..." — finds patterns across users.

**Content-based filtering:** "Because you bought this, you might like..." — finds patterns in item attributes.

Azure Personalizer (part of Azure AI Services) provides a managed recommendation API that can be integrated into any web or mobile application without building the recommendation system from scratch.

[SLIDE 15: Demand Forecasting and Inventory]

Retail inventory management is an optimization problem. Too much inventory ties up capital and risks markdowns. Too little inventory means lost sales and frustrated customers.

AI demand forecasting models incorporate time series patterns, promotional calendars, weather data, and economic indicators to predict SKU-level demand at the store and distribution center level. Large retailers report 10–30% reduction in excess inventory after deploying ML-based forecasting.

[SLIDE 16: Computer Vision in Retail]

Computer vision is transforming the physical retail experience. Use cases include:

- **Automated checkout (Amazon Go style):** Cameras and CV models track what items customers pick up; customers walk out without scanning anything.
- **Shelf monitoring:** Computer vision detects out-of-stock shelves and misplaced items, triggering alerts to store staff.
- **Foot traffic analytics:** Heat maps of customer movement through stores inform store layout optimization.

Azure Computer Vision APIs and Custom Vision services are the Azure tools enabling these applications.

---

## SEGMENT 5 — AI in Manufacturing (Slides 17–19) [3 min]

[SLIDE 17: Manufacturing — The Industrial IoT + AI Convergence]

Manufacturing sits at the intersection of two massive technology trends: Industrial IoT (sensors everywhere) and AI (intelligence applied to sensor data). Modern manufacturing facilities generate terabytes of sensor data daily from equipment, production lines, and supply chains.

[SLIDE 18: Predictive Maintenance]

Predictive maintenance is the killer app for manufacturing AI. Traditional maintenance is either scheduled (replace this part every 90 days regardless of condition) or reactive (fix it when it breaks). Predictive maintenance uses sensor data — vibration, temperature, current draw, acoustic signatures — to predict when a specific piece of equipment will fail, so maintenance can be scheduled just before failure.

The ROI is dramatic in heavy manufacturing: unplanned downtime in automotive manufacturing costs approximately $50,000 per minute. A predictive maintenance model that reduces unplanned downtime by even 20% can save millions of dollars annually at a single facility.

Azure IoT Hub + Azure Machine Learning + Azure Stream Analytics is the standard Azure stack for this use case.

[SLIDE 19: Quality Control and Visual Inspection]

Computer vision models trained on images of manufacturing defects can inspect products at line speed with greater consistency than human inspectors. Semiconductor fabs, electronics assembly, and food processing have all deployed visual inspection AI with defect detection rates exceeding 99.9%.

---

## SEGMENT 6 — ROI Calculation Framework (Slides 20–23) [5 min]

[SLIDE 20: Why Most AI Projects Fail to Show ROI]

Before I give you the framework, let me name the failure modes. Most AI ROI failures happen because:

1. The team built a technically impressive model solving a problem nobody cared about
2. The business impact was never quantified upfront — so there was no way to declare success
3. Integration with existing systems took 10x longer than the model development
4. The model degraded after deployment and nobody maintained it

The framework below forces you to confront each of these before the first dollar is spent.

[SLIDE 21: The Five-Step ROI Framework]

**Step 1 — Define the Business Metric**
What specific, measurable business outcome will improve? Revenue, cost reduction, error rate, cycle time? If you cannot name a number, you do not have a business case.

**Step 2 — Establish the Baseline**
What is the current performance on that metric without AI? You need a number to compare against.

**Step 3 — Estimate AI Impact**
Based on benchmarks, pilots, or vendor claims — what improvement in the metric is realistic? Be conservative. Divide optimistic estimates by two.

**Step 4 — Calculate Total Cost of Ownership**
Include: data acquisition and preparation, model development (build cost or license cost), infrastructure, integration, maintenance, and monitoring. Most teams underestimate integration and maintenance costs by 3–5x.

**Step 5 — Compute ROI**
ROI = (Annual Value Delivered − Annual TCO) / Annual TCO × 100%

A positive ROI does not mean the project should proceed. You also need to consider time to value, risk, and opportunity cost.

[SLIDE 22: Example — Hospital Readmission Model]

Let me walk through a concrete example.

**Business metric:** 30-day readmission rate. Current baseline: 15% across 5,000 annual discharges. Each avoided readmission saves the hospital $12,000 in penalty and care costs.

**Estimated AI impact:** Literature suggests similar models reduce readmission by 2–3 percentage points. Use conservative 2% = 100 avoided readmissions per year.

**Annual value:** 100 × $12,000 = $1.2M

**Annual TCO:** $80K for data engineering, $120K for ML engineering (0.5 FTE), $40K for Azure compute and services, $60K for integration and maintenance = $300K total.

**ROI:** ($1.2M − $300K) / $300K = 300%.

That is a compelling case. But notice how sensitive the outcome is to the $12,000 per readmission savings estimate. Verify your cost assumptions before you present this to leadership.

[SLIDE 23: Build vs. Buy Decision Framework]

The build-vs-buy question comes up in every AI project. The answer depends on four factors:

**Differentiation:** Does AI capability here create competitive differentiation? If yes, build.

**Data advantage:** Do you have proprietary data that a vendor's pre-built model cannot access? If yes, build.

**Speed to value:** Can a vendor deliver a working solution in 3 months vs. your 18-month build timeline? If speed matters, buy.

**Customization requirements:** Does the problem require deep customization of model architecture or training data? If yes, build.

Most organizations land in a hybrid: buy the Azure AI platform and pre-built services as infrastructure, build proprietary models on top using their unique data.

---

## SEGMENT 7 — AI Project Management (Slides 24–27) [4 min]

[SLIDE 24: AI Projects Are Different from Software Projects]

Classic software project management assumes that with enough time and skilled engineers, you will reach the defined outcome. AI projects do not have that guarantee. A model may simply not achieve the required accuracy given the available data. This is the fundamental difference: AI has exploratory uncertainty that software does not.

[SLIDE 25: The CRISP-DM Framework]

The industry-standard AI project framework is CRISP-DM: Cross-Industry Standard Process for Data Mining. It has six phases:

1. **Business Understanding** — Define objectives and translate to data science problem
2. **Data Understanding** — Explore data quality, coverage, and relevance
3. **Data Preparation** — Clean, transform, and engineer features
4. **Modeling** — Select algorithms, train, and tune
5. **Evaluation** — Assess against business criteria, not just model metrics
6. **Deployment** — Integrate into business operations

CRISP-DM is iterative, not waterfall. You will move backward through phases as you discover data problems or unmet accuracy requirements.

[SLIDE 26: Stakeholder Communication in AI Projects]

The biggest AI project management failure mode is the communication gap between data scientists and business stakeholders. Data scientists report model metrics (AUC, precision, recall). Business stakeholders care about outcomes (fewer fraud losses, faster diagnoses). Bridge this gap by translating model metrics into business impact at every project review.

[SLIDE 27: Module Summary and AI-900 Alignment]

Today we covered AI applications across four industries, the ROI calculation framework, the build-vs-buy decision, and AI project management fundamentals.

For the AI-900 exam, the relevant domain is understanding AI workloads and considerations — including identifying appropriate AI services for business scenarios and recognizing responsible AI considerations in business contexts.

The lab this week asks you to identify an AI use case in an industry of your choice and build a formal ROI case for it. This is not a technical lab — it is a business analysis exercise. See you in Module 14.

[END OF VIDEO]

---

*Script prepared by Professor Nash | Texas Wesleyan University | CIS-4330*

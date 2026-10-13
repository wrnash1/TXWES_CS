# Discussion: Module 12 — MLOps and AI Solutions Architecture

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Instructions

Choose ONE of the three scenarios below. Write an initial post of 175–225 words responding to your chosen scenario. Then write two peer response posts of 75–100 words each, engaging substantively with classmates who chose different scenarios when possible. Reference at least one concept from the Module 12 readings in your initial post.

**Due dates:**

- Initial post: by end of Day 4 of the module week
- Peer responses: by end of Day 7

---

## Scenario A — The Degrading Fraud Model

A regional bank deployed a machine learning fraud detection model 18 months ago. At launch, the model caught 91% of fraudulent transactions with a 2% false positive rate. Today, it catches only 74% of fraud, and the false positive rate has risen to 6%. The bank's data science team has been focused on new projects and has not monitored the fraud model since deployment. The head of risk management is alarmed and wants an immediate fix.

**Prompt:** Using MLOps concepts from Module 12, diagnose what likely went wrong. What monitoring infrastructure should have been in place? What are the bank's options now — retrain, recalibrate, or rollback? What does this case teach about treating a deployed model as a "set it and forget it" artifact?

---

## Scenario B — The Pipeline Decision

A manufacturing company is building a predictive maintenance system that will score equipment sensor data to predict failures before they occur. The data science team is debating the deployment architecture. One engineer argues for a batch endpoint that scores all equipment overnight and generates a daily report. Another engineer argues for a managed online endpoint so that failure predictions are available in real time as sensors report data.

**Prompt:** Which deployment architecture is more appropriate for this use case? What factors should drive the decision (equipment failure lead time, cost, latency requirements)? Would the answer change if the equipment in question had a two-hour warning window before failure vs. a two-week warning window? Apply MLOps terminology from the module in your response.

---

## Scenario C — The Build-vs-MLOps-Platform Debate

A healthcare startup's CTO argues against adopting Azure Machine Learning. She says their small team of three data scientists can manage models using spreadsheets for tracking, manual deployments via Flask on a single VM, and monthly email check-ins to see if clinicians are still happy with the model. The lead data scientist pushes back, saying this approach is unsustainable as the number of models grows from 2 to potentially 20.

**Prompt:** Who do you agree with and why? At what scale or risk level does informal model management become irresponsible rather than simply inconvenient? What specific MLOps capabilities — from the Module 12 readings — are hardest to replicate without a proper platform? What is at stake in a healthcare context specifically?

---

## Peer Response Guidelines

Your peer responses should do at least ONE of the following:

- Add a real-world example that supports or complicates your classmate's argument
- Challenge an assumption in their post with evidence from the readings
- Connect their scenario to the one you chose, identifying shared principles
- Ask a focused follow-up question that advances the discussion

Generic responses such as "Great post!" or "I agree with everything you said" will receive zero credit.

---

## Grading Rubric — 10 Points Total

| Criterion | Excellent (Full Credit) | Partial Credit | No Credit |
|---|---|---|---|
| **Content Accuracy** (3 pts) | Uses MLOps terminology accurately; diagnoses or prescribes correctly | Minor terminology errors; mostly correct | Factual errors or no module content referenced |
| **Depth of Analysis** (3 pts) | Goes beyond surface; considers tradeoffs, scale, risk | Addresses prompt but stays at surface level | Restates prompt without analysis |
| **Reading Integration** (2 pts) | Explicitly references at least one reading concept with accuracy | Vague reference to module content | No reading content referenced |
| **Peer Engagement** (2 pts) | Both peer responses substantive; advance discussion | One strong response; one generic | Missing or purely social responses |

---

## Instructor Modeling Response — Scenario A Sample

*The following is a model response at the "Excellent" level to help calibrate your writing.*

This scenario illustrates both concept drift and the absence of production monitoring — two preventable failures that any MLOps-mature organization would have caught within weeks. Fraud patterns evolve continuously as fraudsters adapt to detection; the model was essentially frozen in the fraud landscape of 18 months ago. A properly configured Azure ML Data Drift Monitor would have flagged distributional shifts in transaction features (amounts, merchant categories, geographies) and triggered alerts long before the 74% detection rate was reached.

The bank now has three options. Retraining on recent labeled fraud data is the most thorough fix but requires a labeled dataset of current fraud patterns — which may require forensic review of recent transactions. Recalibrating the decision threshold can partially compensate for precision-recall imbalance but does not fix the underlying model degradation. Rollback makes sense only if a prior version is known to be better — unlikely here since the degradation is temporal, not versional.

The deeper lesson is that a deployed model is not software in the traditional sense. A web application does not get worse over time by itself. A machine learning model does. This distinction is why drift monitoring is a core MLOps pillar, not an optional add-on.

---

*Discussion prepared by Professor Nash | Texas Wesleyan University | CIS-4330*

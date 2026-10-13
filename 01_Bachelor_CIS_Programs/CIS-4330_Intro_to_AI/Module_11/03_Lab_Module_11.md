# Lab 11 — AI Ethics and Responsible AI Principles

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

## AI-900 Alignment: Describe responsible AI considerations and Microsoft's Responsible AI principles

---

## Lab Overview

In this lab you will conduct a structured analysis of a real or proposed AI system using Microsoft's Responsible AI framework. You will explore the Azure Machine Learning Responsible AI Dashboard, analyze a published model card, write a mini AI impact assessment, and evaluate a real-world AI controversy against the six principles.

This lab is primarily a research, analysis, and writing lab — it has less hands-on Azure portal work than previous labs and more critical thinking. It is designed to prepare you for the responsible AI questions on AI-900 and for the ethical dimensions of real AI work.

### Learning Objectives

By completing this lab you will be able to:

- Apply all six Microsoft Responsible AI principles to a real AI system
- Navigate the Azure ML Responsible AI Dashboard and interpret its outputs
- Read and analyze a published model card
- Conduct a structured AI impact assessment for a proposed system
- Identify and explain bias types in a given scenario
- Formulate concrete mitigation recommendations

### Prerequisites

- Azure for Students subscription
- Completion of Modules 07–10 labs (familiarity with Azure AI services)
- Access to the Microsoft Responsible AI website

### Time Estimate

Approximately 90–120 minutes.

---

## Part A: The Six Principles Applied (20 minutes)

### Step A1: Principle Matching

For each of the six scenarios below, identify which Responsible AI principle is primarily implicated and explain why in one to two sentences.

1. A resume screening AI consistently ranks candidates with certain university names lower, regardless of their qualifications. An audit reveals the training data came from a company that historically hired predominantly from a small set of elite universities.

2. A medical imaging AI performs with 97% accuracy on X-rays from US hospitals but drops to 74% accuracy on X-rays from hospitals in sub-Saharan Africa, which use older equipment and have different exposure settings.

3. A loan application AI sends detailed financial histories of individual applicants to a third-party analytics provider for "model improvement" without applicants' knowledge or consent.

4. A hiring platform uses an AI to score applicants and provides only a numeric score to the applicant — no explanation of which factors contributed to the score or how to improve it.

5. When the AI system that manages traffic lights in a major city fails, it provides no fallback behavior. The resulting gridlock delays emergency vehicles and contributes to two preventable deaths.

6. A company deploys an AI customer service agent that gives advice on medication dosages. When patients are harmed by incorrect advice, the company claims it cannot be held responsible because "the AI made the decision."

### Step A2: Multi-Principle Scenarios

Some situations implicate multiple principles simultaneously. For this scenario, identify ALL principles at stake and explain each.

A facial recognition system is deployed at an international airport to automatically identify individuals on a terrorism watchlist. The system has a 1% false positive rate overall, but testing reveals the false positive rate is 4% for Black women and 0.3% for white men. The system makes real-time decisions that result in travelers being pulled out of line and detained. No explanation is provided to detained travelers, and there is no human review before the decision is acted upon.

### Deliverable A

Written answers for all six scenarios in Step A1 (principle identified plus 1–2-sentence explanation each) and the multi-principle analysis for Step A2. Label each answer clearly.

---

## Part B: Bias Analysis (20 minutes)

### Step B1: Bias Type Classification

For each of the following, identify the bias type (historical, representation, measurement, aggregation, label, or feedback loop) and explain how it arose.

1. A credit scoring model was trained on 10 years of lending data. During that period, lending regulations in two states explicitly restricted loans to residents of certain zip codes. The model now systematically scores applicants from those zip codes lower.

2. A voice recognition system was trained on audio recordings collected from tech-savvy early adopters who were overwhelmingly male and between 25 and 40 years old. The system has much higher error rates for elderly speakers and for non-native English speakers.

3. A content moderation system trained by human raters to flag "toxic" comments has learned to flag comments containing African American Vernacular English (AAVE) at a higher rate than equivalent comments in standard American English, because some raters applied "toxic" labels inconsistently.

4. A predictive policing model identifies high-crime areas and directs additional police patrols to those areas. More patrols lead to more arrests in those areas. Those arrests are added to the training data for the next model version, which predicts those areas as even higher crime, leading to even more patrols.

### Step B2: Mitigation Design

For scenario 4 above (the predictive policing feedback loop), propose two specific mitigation strategies — one pre-processing and one post-processing. For each, explain concretely what would be done and what trade-off would be introduced.

### Deliverable B

Written bias type identifications and explanations for all four scenarios in Step B1. Two-paragraph mitigation proposal for Step B2.

---

## Part C: Model Card Analysis (20 minutes)

### Step C1: Locate a Published Model Card

Find and read a published model card for a real AI system. Options include:

- Microsoft Azure AI Face API model card (available on the Azure AI documentation site)
- A model card from Hugging Face Hub (browse at huggingface.co — search for models with model cards)
- Any model card from a major AI lab (Google, Meta, OpenAI publish model cards for their models)

### Step C2: Analyze the Model Card

After reading the model card, answer the following questions.

1. What model did you choose, and where did you find its model card?
2. What does the model card say about the training data? Are there any disclosed gaps or known limitations in the training data?
3. Does the model card include performance metrics broken down by demographic subgroup? If yes, what disparities are disclosed? If no, what does this omission suggest?
4. What are the documented "out of scope" or prohibited use cases?
5. If you were deploying this model in a business application, what is the single most important limitation or risk the model card flags that you would need to address in your system design?

### Deliverable C

Written answers to all five questions in Step C2, with the model card source URL or citation.

---

## Part D: Mini AI Impact Assessment (30 minutes)

### The Scenario

A community college is considering deploying an AI-powered early alert system. The system would analyze student data — attendance records, LMS login frequency, assignment submission times, grade trends, and financial aid status — to predict which students are at risk of withdrawing or failing. Students flagged by the system would receive an automatic outreach email from an AI assistant and be placed on a list that advisors review weekly.

### Step D1: Complete the Assessment

Conduct a mini AI impact assessment by answering all eight core questions from the reading guide. Your responses should be specific to this scenario — do not give generic answers.

1. What is the AI system designed to do, and what decisions will it influence?
2. Who will be directly affected (subjects of AI attention)? Who will be indirectly affected?
3. What potential harms could result — to individuals, to groups, and to the institution?
4. What is the severity and reversibility of these potential harms?
5. Which student populations should be involved in the design and testing process, and how?
6. What safeguards, human oversight mechanisms, and audit capabilities should be built in?
7. After deployment, what metrics should be monitored and how frequently?
8. If a student is harmed — for example, an advisor acts on a false positive flag and the student feels unfairly stigmatized — what is the remediation process?

### Step D2: Principle Mapping

For each Responsible AI principle, assess whether the early alert system as described has an adequate design or a gap. Use a table:

| Principle | Current Design Status | Gap or Concern |
|-----------|----------------------|----------------|
| Fairness | | |
| Reliability and Safety | | |
| Privacy and Security | | |
| Inclusiveness | | |
| Transparency | | |
| Accountability | | |

### Deliverable D

Written answers to all eight assessment questions in Step D1. Completed principle gap table from Step D2.

---

## Part E: Real-World Case Study (10 minutes)

### Step E1: Research a Real AI Controversy

Identify one real-world AI system that has been publicly criticized or investigated for a responsible AI failure. Examples include:

- Amazon's recruiting AI (2018)
- ProPublica's COMPAS recidivism study (2016)
- Gender Shades MIT study on facial analysis bias (2018)
- UK A-level grade algorithm controversy (2020)
- Any documented AI failure you have read about

Write a 175–225-word analysis that covers:

1. What the AI system was designed to do and who deployed it
2. What went wrong and what harm occurred
3. Which specific Responsible AI principles were violated and why
4. What one concrete change to the design or deployment process could have prevented or significantly reduced the harm

### Deliverable E

175–225-word written case study analysis with your source cited.

---

## Submission Requirements

Submit the following to the course LMS by the posted deadline.

- Part A: Principle matching answers for all six scenarios plus the multi-principle analysis
- Part B: Bias type analyses for all four scenarios plus the mitigation proposal
- Part C: Model card analysis with source citation
- Part D: Eight-question impact assessment plus principle gap table
- Part E: 175–225-word case study analysis with source

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Part A — Principle matching | 20 | Correct principle identified for each scenario; explanation is specific, not generic |
| Part B — Bias analysis | 20 | Correct bias type for each scenario; explanation traces how the bias arose; mitigation proposals are specific and address real trade-offs |
| Part C — Model card analysis | 15 | Model card read and cited; all five questions answered with specifics from the actual model card |
| Part D — Impact assessment | 30 | All eight questions answered with scenario-specific depth; principle gap table is substantive |
| Part E — Case study | 15 | Real case correctly described; principles accurately identified; proposed change is concrete and feasible |
| **Total** | **100** | |

---

## Additional Resources

The following resources are recommended for completing this lab.

- Microsoft Responsible AI: microsoft.com/ai/responsible-ai
- Microsoft Responsible AI Standard (full document): available from the Responsible AI site
- NIST AI Risk Management Framework: nist.gov/system/files/documents/2023/01/26/AI-RMF-1-0.pdf
- Model Cards for Model Reporting (original paper): search "Mitchell et al. 2019 model cards"
- Fairlearn documentation: fairlearn.org

---

## Part 9 — Challenge Exercise

### Challenge 1: Quantitative Fairness Audit with Fairlearn

1. Install Fairlearn: `pip install fairlearn scikit-learn pandas`. Load the Adult Income dataset from `sklearn.datasets.fetch_openml(name='adult', version=2)`. Train a `LogisticRegression` classifier to predict income (>50K vs <=50K) using numeric features only (age, hours-per-week, education-num, capital-gain, capital-loss).
2. Use Fairlearn's `MetricFrame` to compute accuracy, precision, recall, and false positive rate grouped by `sex` (the sensitive attribute). Print the `by_group` table.
3. Calculate the fairness gap for each metric (max group value minus min group value). Identify which metric shows the largest disparity and which group is disadvantaged.
4. Apply `ExponentiatedGradient` from `fairlearn.reductions` with `DemographicParity` as the constraint. Retrain the mitigated model and recompute the `MetricFrame`. Report how the disparity gap changed compared to the baseline and what overall accuracy was sacrificed.

### Challenge 2: Model Card Analysis and Gap Assessment

1. Locate a published model card for a production AI system. Recommended sources: Hugging Face Model Hub (any model with a populated Model Card tab), Google Model Cards (modelcards.withgoogle.com), or a Microsoft Azure AI model card published in documentation. Cite the model name and URL.
2. Map the model card's content to the following eight fields: (a) intended use, (b) out-of-scope uses, (c) training data description, (d) evaluation metrics and datasets, (e) performance disaggregated by demographic groups, (f) known limitations, (g) ethical considerations, (h) contact or feedback mechanism. For each field, note whether it is present, absent, or partially addressed.
3. Score the model card 1–5 on each of the six Microsoft Responsible AI principles: Fairness, Reliability and Safety, Privacy and Security, Inclusiveness, Transparency, and Accountability. Justify each score in one sentence.
4. Write a 3–4 sentence recommendation: What is the single most important gap in this model card? What specific information should be added, and which Responsible AI principle would it most strengthen?

### Reflection Questions

1. After completing Challenge 1, explain why demographic parity is not always the right fairness metric. Describe one scenario where equalizing false negative rates (equalized odds) would be more appropriate than demographic parity, and explain the harm avoided by choosing the correct metric.

2. Based on Challenge 2, explain why a model card alone is insufficient to ensure responsible AI deployment. What additional mechanisms — organizational, technical, or regulatory — are needed to close the gap between documented intentions and real-world outcomes?

---

End of Lab 11

# Lab: Module 13 — AI Applications in Business

## Course: CIS-4330 Introduction to Artificial Intelligence

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure AI Fundamentals (AI-900)

---

## Lab Overview

**Title:** AI Business Case Analysis and Azure AI Service Exploration

**Estimated Time:** 90–120 minutes

**Skill Level:** Beginner–Intermediate (no coding required)

**Prerequisites:**

- Completed Module 13 video lecture and reading guide
- Azure free account or Azure for Students subscription
- Access to Microsoft Azure AI Demos: `https://aidemos.microsoft.com`

**Learning Objectives:**

1. Apply the five-step ROI framework to a real business scenario
2. Explore Azure AI services through the AI Demo portal
3. Match business use cases to appropriate Azure AI service categories
4. Evaluate a build-vs-buy decision for a given scenario
5. Document a CRISP-DM project plan for a proposed AI initiative

---

## Part 1 — Industry Use Case Research (20 minutes)

### Task 1.1 — Select Your Industry and Use Case

From the list below, select one industry and one specific use case to develop throughout this lab. You will use your selection for all subsequent parts.

**Industries and sample use cases:**

**Healthcare:**

- Hospital readmission prediction
- Medical imaging anomaly detection
- Clinical documentation automation
- Drug-drug interaction alerts

**Finance:**

- Real-time credit card fraud detection
- Mortgage underwriting automation
- Customer service chatbot for tier-1 banking
- Investment portfolio risk monitoring

**Retail:**

- Product recommendation engine
- Demand forecasting for seasonal inventory
- Automated visual shelf inspection
- Customer churn prediction

**Manufacturing:**

- Predictive maintenance for CNC machines
- Visual defect detection on production line
- Supply chain disruption prediction
- Energy consumption optimization

**Record in your lab notebook:** Industry selected, use case selected, one-sentence description of the problem being solved.

---

### Task 1.2 — Research Published Benchmarks

Search the web for at least two published case studies or benchmarks related to your selected use case. Use sources such as:

- Microsoft customer stories: `https://customers.microsoft.com`
- McKinsey AI case studies: `https://www.mckinsey.com/capabilities/quantumblack`
- Gartner research (via TXWES library)
- Peer-reviewed journals (Google Scholar)

For each source, record:

1. Organization or study name
2. Use case description
3. Reported metric improvement (be specific: "14% reduction in fraud loss" not "improved fraud detection")
4. Source URL or citation

---

## Part 2 — ROI Calculation (25 minutes)

### Task 2.1 — Define Your ROI Inputs

Using the five-step framework from the lecture, define your ROI inputs. Use the table below as your template. Fill in realistic numbers for your scenario — use research from Task 1.2 where possible, or reasonable estimates clearly labeled as estimates.

**ROI Input Table:**

| Input | Your Value | Source or Assumption |
|---|---|---|
| Business metric name | | |
| Baseline value (current performance) | | |
| Estimated improvement from AI | | |
| Number of instances per year (transactions, patients, units) | | |
| Value per improved instance ($) | | |
| **Annual gross value** | | |
| Data preparation cost (Year 1) | | |
| Model development cost (Year 1) | | |
| Infrastructure cost (annual) | | |
| Integration cost (Year 1) | | |
| Ongoing maintenance (annual) | | |
| **Year 1 Total Cost** | | |
| **Year 2+ Annual Cost** | | |

### Task 2.2 — Calculate ROI

Using your inputs from Task 2.1, compute the following:

**Year 1 ROI:**

Year 1 ROI = (Annual Gross Value − Year 1 Total Cost) / Year 1 Total Cost × 100%

**Steady-State ROI (Year 2+):**

Steady-State ROI = (Annual Gross Value − Year 2+ Annual Cost) / Year 2+ Annual Cost × 100%

**Payback Period:**

Payback Period = Year 1 Total Cost / (Annual Gross Value − Year 2+ Annual Cost per month)

**Show your arithmetic step by step.** Do not just write the final percentage — show each multiplication and division.

### Task 2.3 — Sensitivity Analysis

Identify the TWO inputs in your model that have the most uncertainty. For each:

1. Define an optimistic value (the best you could reasonably hope for)
2. Define a pessimistic value (the worst plausible case)
3. Recalculate Year 1 ROI for the pessimistic scenario

**Lab Question 1:** Under the pessimistic scenario, is the AI initiative still financially justified? What non-financial factors (strategic value, competitive pressure, regulatory compliance) might justify proceeding even if the financial ROI is marginal?

---

## Part 3 — Build vs. Buy Analysis (15 minutes)

### Task 3.1 — Apply the Decision Matrix

Apply the build-vs-buy decision matrix from the reading guide to your selected use case.

For each of the five criteria, write 2–3 sentences explaining how your scenario scores on that dimension:

1. **Competitive differentiation:** Does AI capability here create unique competitive advantage for your hypothetical company?
2. **Proprietary data advantage:** Does your company have data a vendor would not have?
3. **Speed to value:** How urgent is the business need? Could you wait 18 months for a custom build?
4. **Customization requirements:** Is your problem standard enough for pre-built services, or does it require custom training?
5. **Internal AI talent:** Assume your hypothetical company has 2 data scientists. Is that sufficient?

**Task 3.2 — Recommendation**

Write a 1-paragraph recommendation (100–150 words) stating whether your hypothetical company should build, buy, or pursue a hybrid approach. Justify your recommendation using specific criteria from the matrix analysis. Name at least one specific Azure AI service that would be relevant if buying or going hybrid.

---

## Part 4 — Azure AI Demo Exploration (20 minutes)

### Task 4.1 — Explore the AI Demo Portal

Navigate to `https://aidemos.microsoft.com` or `https://azure.microsoft.com/en-us/products/ai-services/#overview`.

Explore the live demos for the following services:

- **Azure AI Vision** — Try the image analysis demo
- **Azure AI Language** — Try the sentiment analysis or entity recognition demo
- **Azure AI Speech** — Try the speech-to-text demo
- **Azure OpenAI / Generative AI** — Explore the available demos

For each service you explore, record:

1. Service name
2. What the demo did
3. How this could apply to your selected industry use case (even if the connection is indirect)

### Task 4.2 — Service-to-Use-Case Matching

Complete the following matching table. For each industry scenario, identify the most appropriate Azure AI service category and briefly explain why.

| Business Scenario | Best Azure AI Service | Why |
|---|---|---|
| A hospital wants to extract diagnoses from doctor's notes automatically | | |
| A retailer wants to analyze customer product reviews for sentiment | | |
| A bank wants to flag suspicious transactions in under 100ms | | |
| A manufacturer wants to detect visual defects on a production line | | |
| A call center wants to transcribe customer calls for quality review | | |
| A retailer wants to personalize product recommendations in real time | | |

---

## Part 5 — CRISP-DM Project Plan (20 minutes)

### Task 5.1 — Draft a CRISP-DM Plan

For your selected use case, draft a high-level CRISP-DM project plan covering all six phases. For each phase, provide:

- Key activities (2–3 bullet points)
- Primary deliverable
- Estimated duration (weeks)
- Key risk or challenge specific to your use case

Use this template:

**Phase 1 — Business Understanding**

- Key activities:
- Primary deliverable:
- Estimated duration:
- Key risk:

**Phase 2 — Data Understanding**

- Key activities:
- Primary deliverable:
- Estimated duration:
- Key risk:

**Phase 3 — Data Preparation**

- Key activities:
- Primary deliverable:
- Estimated duration:
- Key risk:

**Phase 4 — Modeling**

- Key activities:
- Primary deliverable:
- Estimated duration:
- Key risk:

**Phase 5 — Evaluation**

- Key activities:
- Primary deliverable:
- Estimated duration:
- Key risk:

**Phase 6 — Deployment**

- Key activities:
- Primary deliverable:
- Estimated duration:
- Key risk:

**Lab Question 2:** In your CRISP-DM plan, which phase do you think will be most challenging for your specific use case? Explain your reasoning in 3–5 sentences.

---

## Part 6 — Executive Summary (10 minutes)

### Task 6.1 — Write a One-Page Executive Summary

Write a 300–400 word executive summary addressed to a hypothetical company's leadership team. The summary should cover:

1. **Problem statement:** What business problem does this AI solution address?
2. **Proposed solution:** What AI capability will be deployed? (Azure service or custom model?)
3. **Expected ROI:** What are the financial projections? Reference your Task 2.2 calculations.
4. **Build vs. buy recommendation:** Reference your Task 3.2 analysis.
5. **Timeline and risks:** How long will implementation take? What are the two highest risks?
6. **Recommendation:** Should leadership approve this initiative? Why or why not?

---

## Lab Submission Requirements

Submit a single PDF document containing:

1. **Part 1:** Industry/use case selection and two benchmark research entries
2. **Part 2:** Completed ROI input table, arithmetic calculations, sensitivity analysis, Lab Question 1 response
3. **Part 3:** Build-vs-buy matrix analysis (5 criteria) and recommendation paragraph
4. **Part 4:** Three service exploration records and completed matching table
5. **Part 5:** Full CRISP-DM project plan and Lab Question 2 response
6. **Part 6:** Executive summary (300–400 words)

**Grading Rubric:**

| Component | Points |
|---|---|
| ROI table complete with sourced inputs | 20 |
| ROI arithmetic shown step by step, correct | 20 |
| Build-vs-buy analysis thorough and justified | 15 |
| Azure service matching table correct | 15 |
| CRISP-DM plan complete for all 6 phases | 15 |
| Executive summary clear and compelling | 15 |
| **Total** | **100** |

---

*Lab prepared by Professor Nash | Texas Wesleyan University | CIS-4330*

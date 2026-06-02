# Lab Activity: Module 08 - Feasibility Analysis and Cost-Benefit Analysis

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University
**Total Points:** 100

---

## Overview

This lab gives you hands-on practice conducting a feasibility analysis and building a cost-benefit model. You will evaluate a proposed system from all four feasibility dimensions and calculate ROI, payback period, and NPV from a provided data set. No software installation or terminal commands are required. All work is document-based.

---

## Case Study: Maplewood County Clerk's Office — Digital Permit Management System

Maplewood County currently processes building, zoning, and contractor permits through a paper-based workflow. Applicants visit the office in person, complete paper forms, submit supporting documents, pay fees by check or cash, and wait for mailed approval letters. The current process takes an average of 18 business days per permit.

The County Clerk has proposed replacing this process with a Digital Permit Management System (DPMS). The new system would allow applicants to submit permit applications online, upload supporting documents digitally, pay fees electronically, and receive automatic status updates and approvals by email. Internal staff would use a web-based portal to review, comment on, and approve applications.

The IT Director has provided the following cost and benefit data for analysis:

Development Costs (one-time):

- Software development and customization: $280,000
- Hardware and infrastructure: $45,000
- Data migration from paper records: $30,000
- Staff training: $20,000
- Project management: $25,000
- Total Development Cost: $400,000

Annual Operating Costs (ongoing, per year):

- Software maintenance and support: $35,000
- Infrastructure and hosting: $12,000
- Annual training for new staff: $3,000
- Total Annual Operating Cost: $50,000

Projected Annual Benefits (per year, beginning Year 1):

- Reduced staff labor (3 FTE positions redirected): $120,000
- Eliminated paper, postage, and storage: $18,000
- Faster permit processing (economic development fees attracted): $45,000
- Reduced error correction and rework: $22,000
- Total Annual Tangible Benefit: $205,000

Intangible Benefits (qualitative, not included in financial model):

- Improved applicant experience and satisfaction
- Reduced in-person lobby traffic and associated facility costs
- Improved regulatory compliance tracking
- Environmental benefit from eliminating paper forms

The organization uses a discount rate of 6% for NPV calculations. The system's expected useful life is 5 years.

---

## Part 1: Feasibility Assessment — 40 Points

### Part 1 Instructions

Evaluate the Maplewood County DPMS proposal from all four feasibility dimensions. For each dimension, write a 3–5 sentence analysis that identifies relevant factors from the case study, makes a clear determination (feasible, conditionally feasible, or not feasible), and explains your reasoning.

Then answer the three analysis questions at the end.

Dimension 1 — Technical Feasibility

Evaluate whether the technology exists and whether Maplewood County can build or acquire the system within reasonable constraints. Consider the standard nature of the technology, the IT Director's involvement (implying internal technical capacity), and any risks related to data migration.

Dimension 2 — Economic Feasibility

Note: Do not calculate financial metrics here — you will do that in Part 2. Instead, make a preliminary qualitative assessment: do annual benefits appear to significantly exceed annual operating costs? Does the development investment appear proportionate to the size of the organization and its budget?

Dimension 3 — Operational Feasibility

Evaluate whether staff and applicants will adopt the system and whether it fits the county's operational context. Consider that some applicants may prefer in-person service, that staff require training, and that the system requires behavior change from both internal and external users.

Dimension 4 — Legal and Ethical Feasibility

Evaluate whether any legal, regulatory, or privacy constraints apply. Consider that the system will process applicant personal information and payment data, that government systems may be subject to state public records laws, and that digital payment processing involves financial compliance requirements.

Analysis Questions (answer each in 2–3 sentences):

Question 1: Which feasibility dimension presents the greatest risk for this project? Justify your answer with specific evidence from the case study.

Question 2: The case study lists four intangible benefits but excludes them from the financial model. Explain why intangible benefits are excluded from the financial model, and describe how a BA should document them.

Question 3: The data migration cost ($30,000) is classified as a development cost. Explain why this is the correct classification rather than an operating cost.

### Grading Rubric — Part 1

| Criterion | Points |
|---|---|
| Technical feasibility analysis: relevant factors identified, clear determination, reasoning explained (5 pts each) | 5 |
| Economic feasibility analysis: qualitative assessment with supporting reasoning (5 pts) | 5 |
| Operational feasibility analysis: adoption factors identified, determination explained (5 pts) | 5 |
| Legal feasibility analysis: relevant constraints identified, determination explained (5 pts) | 5 |
| Analysis Question 1: greatest risk dimension identified with evidence (5 pts) | 5 |
| Analysis Question 2: intangible exclusion explained, documentation approach described (5 pts) | 5 |
| Analysis Question 3: classification of data migration correctly explained (5 pts) | 5 |
| Written quality: complete sentences, clear reasoning throughout all analyses (5 pts) | 5 |

Part 1 Total: 40 points

---

## Part 2: Cost-Benefit Calculations — 35 Points

### Part 2 Instructions

Using the data provided in the case study, perform the following calculations. Show all work for each calculation (formula, substituted values, result). Express each answer in the correct unit (percentage, years, or dollars).

Calculation 1 — Annual Net Benefit

Calculate the Annual Net Benefit.

Show: Total Annual Tangible Benefit minus Total Annual Operating Cost = Annual Net Benefit.

Calculation 2 — Five-Year Total Benefits and Total Costs

Calculate Total Benefits over the 5-year useful life.

Calculate Total Costs (Development Cost + 5 years of Operating Costs) over the 5-year useful life.

Calculation 3 — Return on Investment (ROI)

Using your five-year totals: ROI = (Net Benefit / Total Cost) x 100%, where Net Benefit = Total Benefits - Total Costs.

Calculation 4 — Payback Period

Using the Annual Net Benefit from Calculation 1: Payback Period = Total Development Cost / Annual Net Benefit.

Note: Use only the development cost (not operating costs) in this formula — the payback period measures recovery of the initial investment.

Calculation 5 — Net Present Value (NPV)

Calculate the NPV over the 5-year useful life using a 6% discount rate. Use the following discount factors:

- Year 0 (initial investment): 1.000
- Year 1: 0.943
- Year 2: 0.890
- Year 3: 0.840
- Year 4: 0.792
- Year 5: 0.747

For each year: Discounted Cash Flow = Net Cash Flow x Discount Factor.

Year 0 net cash flow = negative $400,000 (development investment).

Years 1 through 5 net cash flow = Annual Net Benefit (from Calculation 1) each year.

NPV = sum of all discounted cash flows.

After completing all calculations, answer this question in 3–5 sentences: Based on your ROI, payback period, and NPV results, does the DPMS project pass economic feasibility? Explain which metric you find most persuasive for this specific type of public-sector investment and why.

### Grading Rubric — Part 2

| Criterion | Points |
|---|---|
| Calculation 1 (Annual Net Benefit): correct formula, substitution, and result (4 pts) | 4 |
| Calculation 2 (5-year totals): correct benefit and cost totals shown (4 pts) | 4 |
| Calculation 3 (ROI): correct formula, substitution, result in percentage (6 pts) | 6 |
| Calculation 4 (Payback Period): correct formula, substitution, result in years (6 pts) | 6 |
| Calculation 5 (NPV): all 6 discounted cash flows shown, correct sum (10 pts) | 10 |
| Written economic feasibility assessment (3–5 sentences) (5 pts) | 5 |

Part 2 Total: 35 points

---

## Part 3: Recommendation Memo — 25 Points

### Part 3 Instructions

Write a professional recommendation memo (250–350 words) to the Maplewood County Clerk, summarizing the results of your feasibility study and making a clear recommendation to proceed or not proceed with the DPMS project.

Your memo must include all of the following:

- A brief summary of the project and the purpose of the feasibility study (1–2 sentences)
- A summary of findings for each of the four feasibility dimensions (one sentence each)
- Your calculated financial results (ROI, payback period, NPV values)
- A clear recommendation (proceed, proceed with conditions, or do not proceed) supported by specific evidence from your analysis
- At least one risk or condition you would attach to a "proceed" recommendation, or one remediation step you would recommend before proceeding if your recommendation is conditional

The memo should be written in professional business language appropriate for a government official audience.

### Grading Rubric — Part 3

| Criterion | Points |
|---|---|
| All four feasibility dimensions summarized accurately | 8 |
| Financial results (ROI, payback period, NPV) correctly stated | 6 |
| Clear recommendation with specific supporting evidence | 7 |
| At least one risk or condition attached to the recommendation | 4 |

Part 3 Total: 25 points

---

## Submission Instructions

Combine all three parts into one document with clearly labeled sections. For Part 2 calculations, show your work — do not enter only the final answer. Submit to the Canvas Module 08 Lab assignment by the due date shown in the course calendar.

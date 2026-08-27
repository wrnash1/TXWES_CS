# Lab Activity: Module 03 - ERP Selection and Vendor Landscape

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Lab Overview

This lab places you in the role of a junior business systems analyst assisting a company through the ERP vendor selection process. You will define selection criteria, build a vendor scoring matrix, calculate a simplified TCO comparison, and draft a vendor recommendation memo. All work is analytical and document-based.

**Estimated Time:** 90 minutes

**Submission:** Upload to Canvas under "Lab 03 — ERP Selection and Vendor Landscape."

---

## Learning Objectives

By completing this lab you will be able to:

- Define weighted ERP selection criteria appropriate to a given company profile
- Apply a structured vendor scoring matrix to compare ERP candidates
- Calculate a simplified 5-year TCO comparison between SaaS and on-premise deployment
- Distinguish between RFI, RFP, SOW, and SLA in a procurement scenario
- Justify a vendor recommendation in writing using selection criteria evidence

---

## Scenario Background

**Company:** Cornerstone Textile Group
**Industry:** Apparel manufacturing and wholesale distribution
**Size:** 1,200 employees; $220 million annual revenue
**Locations:** Fort Worth (HQ, manufacturing), Dallas (distribution), Austin (sales office)
**Current systems:** QuickBooks for finance, a custom Access database for inventory, a standalone HR system, and Salesforce Sales Cloud for the sales team

Cornerstone's CEO has approved a budget of $3.5 million over the first two years for ERP implementation. The company is growing at 18% annually and expects to add two distribution centers in the next 3 years. Leadership priorities are:

1. Real-time inventory visibility across all locations
2. Integration with the existing Salesforce Sales Cloud instance
3. Automated financial consolidation for the parent company's board reporting
4. Scalability for rapid geographic expansion
5. Minimize disruption to the sales team's Salesforce workflow

The IT director wants a cloud-first solution to avoid new server infrastructure. The CFO is concerned about long-term costs and wants a clear 5-year TCO comparison.

---

## Part A: Selection Criteria Definition (20 points)

### A-1: Weighted Criteria Matrix

Based on Cornerstone's profile and priorities above, define six selection criteria, assign a percentage weight to each (must total 100%), and justify each weight.

Complete this table:

| Criterion | Weight (%) | Justification for This Weight Given Cornerstone's Priorities |
|---|---|---|
| Functional fit — Inventory Management | | |
| Functional fit — Financial Accounting | | |
| Salesforce Integration Capability | | |
| Total Cost of Ownership (5-year) | | |
| Cloud/SaaS Deployment Availability | | |
| Scalability for Multi-Location Growth | | |
| **Total** | **100%** | |

Explain your weighting rationale in 75-100 words beneath the table.

### A-2: Procurement Document Sequence

List the five procurement documents from this module (RFI, RFP, SOW, MSA, SLA) in the order Cornerstone should use them. For each, write one sentence describing what Cornerstone would include in that document specific to their situation.

---

## Part B: Vendor Scoring (30 points)

### B-1: Score Three Vendors

Score the following three vendors against Cornerstone's six criteria using a 1-100 scale. You must justify each score with 1-2 sentences of reasoning based on the vendor's known market strengths and weaknesses relative to Cornerstone's needs.

The three vendors to score:

- **Vendor A:** SAP S/4HANA Cloud Public Edition (SaaS, multi-tenant)
- **Vendor B:** Microsoft Dynamics 365 Finance and Supply Chain (SaaS on Azure)
- **Vendor C:** Oracle Cloud ERP (SaaS)

Use this table. Show your weighted score calculation for each vendor.

| Criterion | Weight | Vendor A Raw Score | Vendor A Weighted | Vendor B Raw Score | Vendor B Weighted | Vendor C Raw Score | Vendor C Weighted |
|---|---|---|---|---|---|---|---|
| Inventory Management Fit | | | | | | | |
| Financial Accounting Fit | | | | | | | |
| Salesforce Integration | | | | | | | |
| 5-Year TCO | | | | | | | |
| SaaS Deployment | | | | | | | |
| Scalability | | | | | | | |
| **Weighted Total** | **100%** | | | | | | |

For each vendor score, write your reasoning in a separate section below the table (one sentence per criterion per vendor).

### B-2: Scoring Sensitivity Check

Choose the criterion where you are least confident in your scoring. Explain what information you would seek from each vendor (via RFP response or demo) to improve confidence in that score.

---

## Part C: TCO Analysis (30 points)

### C-1: Five-Year TCO Comparison

Complete a simplified 5-year TCO comparison for SAP S/4HANA Cloud Public Edition (SaaS) versus a hypothetical on-premise alternative. Use the following assumptions (you may adjust with justification):

**SaaS (S/4HANA Cloud Public Edition):**

- Year 1 subscription: $240,000 (1,200 users at $200/user/year average)
- Implementation labor (one-time): $1,800,000
- Training (one-time): $120,000
- Years 2-5 subscription: $240,000/year each
- Infrastructure: $0 (vendor-managed)
- Upgrade projects: $0 (automatic)

**On-Premise (hypothetical):**

- Perpetual license (one-time): $900,000
- Implementation labor (one-time): $2,100,000
- Hardware procurement (one-time): $350,000
- Annual maintenance (18% of license): $162,000/year
- DBA and IT staffing (annual): $180,000/year
- Major upgrade project in Year 4: $600,000
- Training (one-time): $150,000

Build a year-by-year table for both options (Year 0 through Year 5). Calculate:

- Annual cost for each option each year
- Running cumulative total for each option each year
- The year in which SaaS cumulative cost becomes lower than on-premise cumulative cost

### C-2: TCO Narrative

In 150-200 words, summarize what the TCO analysis reveals for Cornerstone's CFO. Address:

- What year does the break-even point occur?
- What factors drive the on-premise cost higher over time?
- Given Cornerstone's cloud-first preference and growth trajectory, which model do you recommend and why?

---

## Part D: Recommendation Memo (20 points)

### D-1: Vendor Recommendation

Write a 250-300 word executive memo addressed to Cornerstone's CEO recommending one of the three vendors from Part B. Your memo must:

- State the recommended vendor and the top two reasons for the recommendation
- Reference the weighted score from your matrix
- Address the CFO's TCO concern with one specific point from Part C
- Identify one risk of your recommendation and how it should be mitigated
- Use formal business writing (no informal language, no bullet points in the memo body)

---

## Grading Rubric

| Section | Points | Criteria |
|---|---|---|
| A-1: Criteria matrix completed with weights and justifications | 12 | Weights sum to 100%, each weight justified with reference to company priorities |
| A-2: Procurement document sequence | 8 | Correct order, scenario-specific sentence for each document |
| B-1: Vendor scoring table with reasoning | 20 | Scores defensible, reasoning references vendor strengths/weaknesses, weighted totals calculated correctly |
| B-2: Sensitivity check | 10 | Identifies uncertain criterion, specifies information to seek from RFP/demo |
| C-1: Year-by-year TCO table | 18 | Both models correctly built, cumulative totals accurate, break-even year identified |
| C-2: TCO narrative | 12 | 150-200 words, addresses break-even, cost drivers, and recommendation with rationale |
| D-1: Executive recommendation memo | 20 | 250-300 words, formal register, references matrix score and TCO, identifies and mitigates one risk |
| **Total** | **100** | |

---

## Submission Instructions

1. Compile all responses into a single document.
2. Name your file: `Lab03_LastName_FirstName.pdf`
3. Upload to Canvas under "Lab 03 — ERP Selection and Vendor Landscape."
4. Deadline: See course schedule in Canvas. Late submissions lose 10 points per day.

---

## Part 9 — Challenge Exercise

### Challenge 1: Build-vs-Buy-vs-Extend Decision Tree

A rapidly growing e-commerce company (250 employees, $40M revenue, projecting 3x growth in 3 years) currently uses QuickBooks Online for finance, Shopify for storefront, and a custom-built inventory spreadsheet. The CEO wants a unified system but is unsure whether to (a) implement a full ERP like NetSuite, (b) extend their current tools with integrations, or (c) build a custom system.

1. Create a structured decision framework with at least five evaluation questions that determine which path is most appropriate (e.g., "Will the company outgrow the system within 3 years?", "Does the company have in-house development capacity?"). For each question, define which answer points toward which option.
2. Apply your framework to the company described above and document your recommendation with reasoning for each decision point.
3. Identify three specific risks of the "build custom" option that an ERP implementation would avoid, with one concrete example of how each risk could manifest for this company.
4. Research one real ERP vendor (NetSuite, SAP Business One, Microsoft Dynamics 365 Business Central, or Odoo) appropriate for this company's size and summarize its pricing model, implementation timeline, and top three functional strengths.

### Challenge 2: Vendor Contract Risk Analysis

You are advising a client who has received a 150-page software license and services agreement from an ERP vendor. The client's legal team has flagged three clauses but does not understand their business implications.

1. For each of the following clause descriptions, explain the business risk in plain language and suggest one negotiation position the client should take: (a) "Vendor may modify pricing upon 90-day written notice" — (b) "Customer data may be used by vendor for product improvement purposes in anonymized form" — (c) "Service level credits shall not exceed 10% of monthly subscription fees regardless of downtime duration."
2. Write a short checklist (minimum 6 items) of contract provisions that any ERP buyer should review before signing, with a one-sentence explanation of why each matters.

### Reflection Questions

1. In the build-vs-buy-vs-extend decision, what company characteristic most strongly tips the decision toward buying a commercial ERP rather than building custom software? Would your answer change if the company operated in a highly specialized niche industry with no ERP vendor offering relevant functionality?
2. ERP vendor contracts are notoriously one-sided. What is the most important leverage point a buyer has during contract negotiation, and at what point in the procurement process should negotiation strategy be developed?

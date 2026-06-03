# Lab Activity: Module 04 — Risk Assessment and Analysis Techniques

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 2: Information Risk Management

---

## Lab Overview

This lab applies the three risk analysis techniques from Module 04 to a realistic mid-sized organization scenario. You will perform quantitative risk calculations using the ALE formula chain, conduct a qualitative risk matrix assessment, and develop a Business Impact Analysis for critical business functions. All work is document-based — no special software is required beyond a word processor and basic spreadsheet application.

**Estimated Time:** 90–120 minutes

**Submission:** Upload your completed Lab 04 Report to the Canvas assignment portal before the due date.

---

## Scenario Background

Pinnacle Payment Solutions (PPS) is a Texas-based payment processing company that handles credit and debit card transactions for 4,200 retail merchants across the southwestern United States. PPS processes approximately $1.8 billion in transactions annually and employs 340 people across two office locations in Dallas and San Antonio.

The company's information systems include a core transaction processing platform, a merchant portal (web-based), a data warehouse containing five years of transaction history, an internal HR and payroll system, and a customer support ticketing system. PPS is subject to PCI DSS compliance requirements as a Level 2 service provider.

The recently hired CISO has been asked to complete three deliverables for the board's quarterly risk review: a quantitative analysis of the top three cyber risks, a qualitative risk matrix assessment, and a BIA for the company's most critical business functions.

---

## Task 1 — Quantitative Risk Analysis: ALE Calculations (30 points)

Calculate the Annualized Loss Expectancy for each of the three risk scenarios below. Show all formula steps. After completing the calculations, answer the analysis questions that follow.

### Scenario Data

**Risk Scenario 1 — SQL Injection Attack on the Merchant Portal**

The PPS merchant portal has an asset value of $3,200,000 (representing the portal infrastructure, associated transaction data, and merchant relationship value). A successful SQL injection attack would compromise approximately 35% of the asset value (exposure factor = 0.35). PPS security analysts estimate, based on industry threat intelligence for payment processors, that a successful SQL injection attack occurs in similar organizations approximately once every three years.

**Risk Scenario 2 — Ransomware on the Transaction Processing Platform**

The core transaction processing platform has an asset value of $8,500,000. A ransomware attack would disrupt approximately 85% of the platform's operational capability (exposure factor = 0.85). Based on FBI IC3 ransomware incident data for financial services companies of PPS's size, the estimated rate of occurrence is once every four years.

**Risk Scenario 3 — Insider Data Theft**

The transaction data warehouse contains five years of payment card transaction history. The data warehouse has an asset value of $2,100,000. Insider data theft incidents affecting the full dataset would compromise 60% of the asset's value (exposure factor = 0.60). Based on industry data for financial service organizations, insider theft incidents of this type occur approximately once every eight years.

### Calculation Worksheet

Complete the following table.

| | Scenario 1 | Scenario 2 | Scenario 3 |
|---|---|---|---|
| Asset Value (AV) | $3,200,000 | $8,500,000 | $2,100,000 |
| Exposure Factor (EF) | 0.35 | 0.85 | 0.60 |
| SLE = AV × EF | | | |
| Annualized Rate of Occurrence (ARO) | | | |
| ALE = SLE × ARO | | | |

Show your ARO calculation for each scenario. For example: if an event occurs once every three years, ARO = 1/3 = 0.333.

### Control Investment Analysis

For Scenario 1 (SQL Injection), a web application firewall and quarterly penetration testing program would cost PPS $95,000 annually. This control set would reduce the exposure factor from 0.35 to 0.08.

Calculate the new SLE and ALE under this control scenario. Then determine whether the $95,000 annual investment is financially justified. Show your work.

### Analysis Questions

Answer each question in two to four sentences.

1. Which of the three risk scenarios represents the highest annual financial exposure? Is this the same scenario you would have ranked first if you had estimated intuitively, without the calculations?

2. For Scenario 3 (Insider Theft), the ARO is very low — once every eight years. Does a low ARO mean an organization can safely ignore this risk? Explain your reasoning with reference to the ALE result.

3. A colleague suggests that quantitative analysis is always superior to qualitative analysis because it produces exact numbers. Identify one weakness of quantitative analysis that this argument overlooks.

---

## Task 2 — Qualitative Risk Matrix Assessment (25 points)

Using the 5×5 risk matrix below, assess each of the ten risks listed in the risk register excerpt. Assign a Likelihood rating and an Impact rating for each risk, determine the Risk Priority, and provide a one-sentence justification for your likelihood assignment.

### Risk Matrix Reference

| | Negligible | Minor | Moderate | Major | Critical |
|---|---|---|---|---|---|
| Almost Certain | Medium | High | High | Critical | Critical |
| Likely | Low | Medium | High | High | Critical |
| Possible | Low | Low | Medium | High | High |
| Unlikely | Low | Low | Low | Medium | High |
| Rare | Low | Low | Low | Low | Medium |

### PPS Risk Register Excerpt

| Risk ID | Risk Description |
|---------|----------------|
| R-01 | PCI DSS audit finds critical non-compliance, resulting in fines and potential suspension of card processing |
| R-02 | Phishing email compromises a customer support representative's credentials |
| R-03 | Dallas data center experiences extended power outage lasting 48+ hours |
| R-04 | Key payment processing vendor declares bankruptcy and ceases operations |
| R-05 | Disgruntled employee exfiltrates merchant account data before termination |
| R-06 | DDoS attack renders the merchant portal unavailable for 6+ hours during peak business hours |
| R-07 | Unpatched vulnerability in the transaction platform is exploited by a threat actor |
| R-08 | Senior security analyst resigns and critical institutional knowledge is lost |
| R-09 | Natural disaster (tornado) causes physical damage to San Antonio office |
| R-10 | Third-party software library in the merchant portal contains a supply chain backdoor |

### Risk Assessment Worksheet

Complete the following table for each risk.

| Risk ID | Likelihood Rating | Impact Rating | Risk Priority | Likelihood Justification |
|---------|------------------|--------------|--------------|-------------------------|
| R-01 | | | | |
| R-02 | | | | |
| R-03 | | | | |
| R-04 | | | | |
| R-05 | | | | |
| R-06 | | | | |
| R-07 | | | | |
| R-08 | | | | |
| R-09 | | | | |
| R-10 | | | | |

### Qualitative Analysis Questions

Answer each question in two to four sentences.

1. Which three risks did your matrix identify as Critical priority? Do you agree with the matrix result, or does your professional judgment suggest a different prioritization? Explain.

2. Compare your qualitative results with the quantitative results from Task 1. Are the same risks in the top tier? What does this tell you about the relationship between the two methods?

3. PPS's CISO wants to present the risk matrix to the board of directors. What is one advantage and one disadvantage of presenting the heat map as the primary risk communication tool to a board audience?

---

## Task 3 — Business Impact Analysis (30 points)

Conduct a BIA for the four PPS business functions listed below. Define MTD, RTO, and RPO for each function, and justify your choices.

### PPS Business Functions for BIA

**Function 1 — Real-Time Transaction Authorization**
PPS provides real-time authorization decisions for payment card transactions. Merchants depend on this function continuously — delays or outages directly prevent customers from making purchases and immediately cost merchants revenue. PPS's contracts include a Service Level Agreement guaranteeing 99.95% monthly uptime.

**Function 2 — Merchant Settlement and Funds Transfer**
Each business day, PPS calculates net settlement amounts and initiates ACH transfers to merchant bank accounts. Merchants depend on these daily settlements for their cash flow. A delay beyond two business days would trigger contractual penalties and merchant account cancellation risk.

**Function 3 — Cardholder Data Dispute Resolution**
When cardholders dispute transactions, PPS provides documentation and response services to issuing banks within regulatory timeframes. Under PCI DSS and card network rules, response deadlines range from 10 to 45 days depending on dispute type. Failure to respond within regulatory windows results in automatic chargebacks and fines.

**Function 4 — Internal HR and Payroll Processing**
PPS processes bi-weekly payroll for 340 employees. Payroll runs on the first and third Fridays of each month. A disruption to payroll processing would affect employee compensation, but payroll obligations can typically be met through manual bank transfers for short outages.

### BIA Worksheet

Complete the following table for each function. For each metric, provide the value and a one- to two-sentence justification in the notes column.

| Function | MTD | MTD Justification | RTO | RTO Justification | RPO | RPO Justification | BIA Priority |
|----------|-----|------------------|-----|------------------|-----|------------------|-------------|
| Transaction Authorization | | | | | | | |
| Merchant Settlement | | | | | | | |
| Dispute Resolution | | | | | | | |
| HR and Payroll | | | | | | | |

### BIA Analysis Questions

Answer each question in two to four sentences.

1. For Transaction Authorization, what specific technical capability would PPS need in order to meet the RTO you defined? Be specific — name the type of infrastructure or architecture required.

2. Compare the RPO you assigned to Transaction Authorization versus HR and Payroll. Explain why the difference in RPO values reflects a meaningful business difference, not simply a difference in IT system importance.

3. The CISO wants to use the BIA results to justify a $2.4 million investment in a secondary hot site data center. Which function's BIA metrics most strongly support this investment, and how would you present that justification?

---

## Task 4 — Technique Selection Memo (15 points)

Write a 200–275 word professional memo from you (as a risk analyst) to PPS's CISO recommending which analytical technique — quantitative ALE analysis, qualitative risk matrix, or BIA — should be the primary tool for the board's quarterly risk report. Your memo must:

- State your recommendation clearly in the first paragraph
- Provide at least two specific reasons for your choice based on the characteristics of PPS's situation
- Acknowledge one limitation of your chosen technique
- Explain how the other two techniques can complement your primary choice
- Use professional memo format: To, From, Date, Subject, Body

---

## Deliverables Summary

| Deliverable | Points | Completion Check |
|------------|--------|-----------------|
| Task 1: ALE calculations worksheet and control investment analysis | 30 | |
| Task 2: Risk matrix assessment with ten risks and analysis questions | 25 | |
| Task 3: BIA worksheet and analysis questions | 30 | |
| Task 4: Technique selection memo (200–275 words) | 15 | |
| Total | 100 | |

---

## Grading Rubric

| Criterion | Full Credit | Partial Credit | No Credit |
|-----------|------------|---------------|-----------|
| ALE calculations are mathematically correct with steps shown | All calculations correct, ARO derivations shown, control analysis complete | One calculation error or missing steps | No calculations or incorrect formulas used |
| Risk matrix ratings are plausible and justified | Ratings are defensible given scenario facts; justifications are specific | Ratings assigned without justification or clearly inconsistent | Ratings missing or matrix not used correctly |
| BIA metrics are realistic and appropriately differentiated | Metrics reflect business function criticality; RTO is less than MTD for all functions | Metrics are assigned without differentiation or RTO exceeds MTD | Metrics missing or identical across all functions |
| Memo is professional and addresses all required points | All four required points addressed; professional format; 200–275 words | Missing one or two required points | No memo or fewer than 100 words |

---

## Academic Integrity Notice

All calculations, ratings, and analysis in this lab must represent your own reasoning applied to the PPS scenario. You may discuss concepts with classmates, but your submitted calculations and written responses must be your own original work. Cite any external sources consulted beyond the course reading materials.

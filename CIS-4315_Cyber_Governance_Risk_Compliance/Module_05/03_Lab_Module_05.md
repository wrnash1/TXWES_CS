# Lab Activity: Module 05 — Risk Treatment and Control Selection

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 2: Information Risk Management

---

## Lab Overview

This lab synthesizes the three-module risk management arc by requiring you to make and justify risk treatment decisions. You will select treatment options for a set of assessed risks, categorize and select specific controls, conduct cost-benefit analyses, and document residual risk — the complete workflow a risk analyst performs after assessment is complete.

**Estimated Time:** 90–120 minutes

**Submission:** Upload your completed Lab 05 Report to the Canvas assignment portal before the due date.

---

## Scenario Background

TexCore Logistics is a mid-sized freight brokerage company headquartered in Fort Worth, Texas, with 520 employees across five regional offices. TexCore operates a cloud-hosted logistics management platform that connects shippers and carriers, manages freight contracts, and processes payments. Annual revenue is $280 million.

The company's security team recently completed a comprehensive risk assessment. The risk register now contains twelve assessed risks. Your job is to serve as the risk analyst responsible for developing and documenting risk treatment recommendations for the eight risks in this lab.

TexCore's board-approved risk appetite statement reads: "TexCore will accept risks with an ALE below $50,000 per year. Risks with an ALE between $50,000 and $250,000 require documented mitigation or transfer. Risks with an ALE exceeding $250,000 require immediate treatment action and executive-level risk acceptance if residual risk remains above $50,000."

---

## Task 1 — Risk Treatment Selection (25 points)

For each of the eight risks in the TexCore risk register excerpt, recommend one of the four treatment options (Avoid, Transfer, Mitigate, Accept) and provide a written justification of two to four sentences. Your justification must reference specific characteristics of the risk and TexCore's risk appetite statement.

### Risk Register Excerpt

| Risk ID | Risk Description | ALE |
|---------|----------------|-----|
| R-01 | Ransomware attack encrypts the logistics management platform | $420,000 |
| R-02 | An employee accidentally emails confidential shipper contract to wrong recipient | $18,000 |
| R-03 | A carrier partner's compromised credentials are used to submit fraudulent freight invoices | $195,000 |
| R-04 | TexCore considers offering a cryptocurrency payment option; this would create exposure to crypto exchange rate volatility and regulatory uncertainty | $310,000 |
| R-05 | A lightning strike damages the Dallas office server room equipment | $62,000 |
| R-06 | A disgruntled former employee uses retained VPN access to access carrier rate data | $88,000 |
| R-07 | The public-facing shipper portal is taken offline by a DDoS attack for 4+ hours | $175,000 |
| R-08 | Loss of a single laptop containing locally cached contract data due to theft or loss | $9,000 |

### Treatment Recommendation Worksheet

Complete the following table and provide your justification paragraph beneath each row.

| Risk ID | Recommended Treatment | Risk Appetite Alignment |
|---------|----------------------|------------------------|
| R-01 | | |
| R-02 | | |
| R-03 | | |
| R-04 | | |
| R-05 | | |
| R-06 | | |
| R-07 | | |
| R-08 | | |

For R-04, address whether the treatment option you selected would change if TexCore's leadership decides to launch the cryptocurrency payment option despite the risk.

---

## Task 2 — Control Selection and Categorization (25 points)

For the three risks you designated as Mitigate in Task 1, identify at least two specific controls for each risk. For each control, provide the following information.

- Control name and description
- Functional type: Preventive, Detective, Corrective, or Deterrent
- Implementation method: Administrative, Technical, or Physical
- How this control addresses the specific risk

Present your analysis using the table format below for each risk.

### Control Selection Table Format

| Control Name | Description | Functional Type | Implementation Method | Risk Reduction Mechanism |
|---|---|---|---|---|
| (Control 1) | | | | |
| (Control 2) | | | | |
| (Control 3, optional) | | | | |

Create one table per risk being mitigated.

### Defense in Depth Analysis

For one of your three mitigated risks, write a paragraph (100–150 words) explaining how the controls you selected create a defense-in-depth strategy. Specifically address: how do your preventive and detective controls complement each other? What happens if the preventive control fails?

---

## Task 3 — Cost-Benefit Analysis (25 points)

Conduct a cost-benefit analysis for the control set you recommended for two of the three risks you designated as Mitigate. Use the following control cost data provided by TexCore's IT procurement team.

### Control Cost Reference Data

For Risk R-01 (Ransomware):

- Endpoint detection and response (EDR) platform: $48,000 per year. Would reduce ALE from $420,000 to $95,000.
- Immutable cloud backup solution: $22,000 per year. Would reduce ALE an additional $60,000 beyond EDR alone (total ALE with both: $35,000).
- Security awareness training program (phishing simulation): $15,000 per year. Would reduce ALE an additional $20,000 beyond EDR alone (total ALE with all three: $15,000).

For Risk R-06 (Former Employee VPN Access):

- Automated access termination workflow integrated with HR system: $12,000 per year. Would reduce ALE from $88,000 to $18,000.
- Privileged access management (PAM) solution: $35,000 per year. Would reduce ALE from $88,000 to $8,000 when used alone, or to $3,000 when combined with the automated access termination workflow.

For Risk R-07 (DDoS Attack):

- DDoS mitigation service (cloud scrubbing): $55,000 per year. Would reduce ALE from $175,000 to $28,000.
- Content delivery network (CDN) with built-in DDoS protection: $38,000 per year. Would reduce ALE from $175,000 to $42,000.

### Cost-Benefit Calculation Instructions

For each of your two selected risks, complete the following calculations.

Step 1: Calculate the net benefit for each individual control option.

Net Benefit = (Current ALE - Projected ALE with Control) - Annual Control Cost

Step 2: For risks where multiple controls are available, calculate the incremental benefit of adding each additional control beyond the first.

Step 3: Identify the optimal control combination — the set of controls that maximizes net benefit while meeting the TexCore risk appetite threshold ($50,000 ALE target for acceptable residual risk).

Step 4: Document the residual risk after your recommended control combination is implemented.

### Cost-Benefit Worksheet

Present your calculations in a structured table for each risk, showing current ALE, each control option's cost and ALE reduction, net benefit, and your recommendation.

### Analysis Questions

Answer each question in two to four sentences.

1. For at least one of your analyzed risks, is the optimal control combination (highest net benefit) the same as the combination that meets the risk appetite threshold? If they differ, which should the risk analyst recommend and why?

2. TexCore's CFO asks why the company should invest $85,000 per year in ransomware controls when the probability of a ransomware attack in any given year is less than 25%. How would you explain the ALE-based justification in terms a non-technical CFO would find compelling?

3. The cost data provided does not include implementation costs — only recurring annual costs. How would a one-time implementation cost of $120,000 affect the first-year vs. multi-year cost-benefit calculation for the EDR platform?

---

## Task 4 — Residual Risk Documentation (15 points)

Complete the residual risk register for all eight risks from Task 1. For each risk, document the treatment decision, the residual risk after treatment, and whether formal risk acceptance is required based on TexCore's risk appetite statement.

### Residual Risk Register

| Risk ID | Treatment Decision | Controls Implemented (if mitigated) | Residual ALE | Risk Appetite Met? | Formal Acceptance Required? | Acceptance Authority |
|---------|-------------------|-------------------------------------|-------------|-------------------|---------------------------|---------------------|
| R-01 | | | | | | |
| R-02 | | | | | | |
| R-03 | | | | | | |
| R-04 | | | | | | |
| R-05 | | | | | | |
| R-06 | | | | | | |
| R-07 | | | | | | |
| R-08 | | | | | | |

For risks where formal acceptance is required, identify who at TexCore should have authority to sign the acceptance — based on the ALE level and the risk appetite statement's tiered requirements.

### Residual Risk Reflection

Write a paragraph (75–100 words) explaining why documenting residual risk is a governance requirement, not just an administrative formality. Address the following: who needs this information and why, and what happens in an audit or regulatory review if residual risk is not formally documented.

---

## Deliverables Summary

| Deliverable | Points | Completion Check |
|------------|--------|-----------------|
| Task 1: Treatment selections with justifications for all 8 risks | 25 | |
| Task 2: Control selection tables and defense-in-depth paragraph | 25 | |
| Task 3: Cost-benefit calculations and analysis questions | 25 | |
| Task 4: Residual risk register and reflection paragraph | 15 | |
| Professional presentation: organized, labeled, complete | 10 | |
| Total | 100 | |

---

## Grading Rubric

| Criterion | Full Credit | Partial Credit | No Credit |
|-----------|------------|---------------|-----------|
| Treatment selections are aligned with risk appetite statement | All 8 selections explicitly reference ALE level and appetite thresholds | Most selections appropriate but not all reference the appetite statement | Selections appear random or ignore the appetite statement |
| Controls are correctly categorized by functional type and implementation method | All controls categorized correctly with accurate descriptions | Minor categorization errors (1–2 controls) | Controls missing or categorization entirely incorrect |
| Cost-benefit calculations are mathematically correct | All calculations correct; incremental analysis shown; optimal combination identified | Calculation errors in one risk or incremental analysis missing | No calculations or incorrect formula used |
| Residual risk register is complete and acceptance authority is appropriate | All 8 risks documented; acceptance authority reflects ALE tier | Incomplete entries or acceptance authority not differentiated by risk level | Register missing or all entries identical |
| Writing is professional and technically precise | Correct terminology throughout; no factual errors; clear explanations | Minor terminology errors or imprecision | Significant technical errors or absent explanations |

---

## Academic Integrity Notice

Your treatment recommendations, control selections, and cost-benefit analyses must reflect your own reasoning. For the cost-benefit calculations, there is one mathematically correct answer — show your work so partial credit can be awarded for correct methodology even if arithmetic errors occur. Cite any external sources consulted beyond course materials.

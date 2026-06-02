# Lab Activity: Module 04 - ERP Implementation Lifecycle

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Lab Overview

This lab places you in the role of a junior project analyst on an ERP implementation team. You will analyze an implementation scenario, build an implementation risk register, design a change management plan, and evaluate a go-live readiness scenario. All work is analytical and document-based.

**Estimated Time:** 90 minutes

**Submission:** Upload to Canvas under "Lab 04 — ERP Implementation Lifecycle."

---

## Learning Objectives

By completing this lab you will be able to:

- Map an ERP implementation scenario to the correct SAP Activate phase
- Identify implementation risks and classify them by probability and impact
- Design a change management approach for a specific stakeholder group
- Evaluate a go-live readiness scenario and make a defensible go/no-go recommendation
- Distinguish between unit testing, integration testing, and UAT in terms of who runs them and what they validate

---

## Scenario Background

**Company:** Meridian Hospital Network
**Industry:** Healthcare administration
**Size:** 4,200 employees across six hospital campuses
**Project:** SAP S/4HANA implementation replacing a 20-year-old on-premise financial system
**Scope:** Finance (FI, CO), Procurement (MM), and HR (SuccessFactors integration)
**Timeline:** 18-month project, currently in the Explore phase (Month 4)
**Key stakeholders:** CFO (project sponsor), VP of Finance, Directors of Procurement, HR Director, IT Director, frontline AP clerks (180 people), payroll team (12 people)

**Project context:** The current system is deeply customized and the data quality is poor — the vendor master has 8,400 records, of which the procurement team estimates 30-40% are duplicates or inactive. The CFO is under board pressure to go live on schedule. The IT director is concerned that the data quality work cannot be completed in time. Frontline AP clerks have expressed anxiety about the new system in town halls. The project team has not yet begun change management activities.

---

## Part A: Phase Mapping and Activities (20 points)

### A-1: Phase Identification

The following activities are happening at Meridian. For each activity, identify which SAP Activate phase it belongs to and explain your reasoning in one sentence.

| Activity | SAP Activate Phase | One-Sentence Justification |
|---|---|---|
| The project team holds workshops with Finance to walk through SAP's standard accounts payable process and compare it to Meridian's current process | | |
| The SAP Basis team provisions the Development, Quality Assurance, and Production system landscapes | | |
| The functional consultant configures the company code and chart of accounts in the SAP system | | |
| Finance users run end-to-end test scenarios including creating a vendor, posting an invoice, and running the payment run | | |
| The project sponsor presents the business case for SAP S/4HANA to the Board of Directors | | |
| The team executes the final data load over the go-live weekend and validates record counts | | |

### A-2: Fit-to-Standard Gap Classification

During Fit-to-Standard workshops, Meridian's procurement team identifies the following gaps between their current process and SAP's standard procurement process. For each gap, classify it as: (A) Adapt the process to match SAP standard, (B) Configure SAP to accommodate the requirement, or (C) Custom development required. Justify each classification in one sentence.

| Gap Description | Classification (A/B/C) | Justification |
|---|---|---|
| Meridian requires three approval levels for POs over $50,000; SAP standard supports two-level approval | | |
| Meridian uses a 6-digit vendor number format; SAP's standard vendor master uses alphanumeric IDs | | |
| Meridian requires that all POs over $100,000 automatically attach to a capital project code not supported in SAP's standard cost assignment | | |
| Meridian's procurement policy requires a 30-day payment term as default; SAP allows configurable default payment terms per vendor | | |

---

## Part B: Risk Register (25 points)

### B-1: Risk Identification and Scoring

Identify six implementation risks specific to the Meridian scenario. For each risk, complete the following table:

| Risk ID | Risk Description | Category (Technical/Data/People/Process/External) | Probability (1-5) | Impact (1-5) | Risk Score (P×I) | Recommended Mitigation |
|---|---|---|---|---|---|---|
| R-001 | | | | | | |
| R-002 | | | | | | |
| R-003 | | | | | | |
| R-004 | | | | | | |
| R-005 | | | | | | |
| R-006 | | | | | | |

Scoring scale: 1 = Very Low, 5 = Very High. Risk Score = Probability × Impact (max 25).

Identify the two highest-scored risks and explain in 50-75 words why they represent the most critical threats to Meridian's go-live date.

### B-2: Risk Priority Matrix

Using your six risks from B-1, place each risk on a 5x5 grid (Probability on Y-axis, Impact on X-axis). Describe verbally which quadrant each risk falls into and what that means for how much management attention it requires:

- High Probability + High Impact: Immediate action required; dedicated mitigation owner
- High Probability + Low Impact: Monitor and manage; accept if cost of mitigation exceeds impact
- Low Probability + High Impact: Contingency planning required; rollback plan essential
- Low Probability + Low Impact: Accept; document and monitor

---

## Part C: Change Management Plan (25 points)

### C-1: Stakeholder Analysis

Complete a stakeholder analysis for four key groups in the Meridian implementation:

| Stakeholder Group | Count | Current Sentiment (Support/Neutral/Resistant) | Primary Concern | Change Management Action Needed |
|---|---|---|---|---|
| CFO and VP of Finance | 2 | | | |
| Frontline AP Clerks | 180 | | | |
| Payroll Team | 12 | | | |
| Procurement Directors | 4 | | | |

Base your sentiment assessment on evidence from the scenario description.

### C-2: Super-User Network Design

Design a super-user network for Meridian's AP team (180 people across 6 campuses). Address:

- How many super-users would you recommend and how would you distribute them across campuses?
- What additional training would super-users receive beyond the standard user training?
- What would the super-user's role be during the first 4 weeks after go-live?
- How would you incentivize employees to volunteer as super-users?

Write your response in 150-200 words.

### C-3: Training Plan

Design a training approach for the AP clerks that addresses their expressed anxiety about the new system. Your plan must:

- Specify the timing of training relative to go-live (e.g., 6 weeks before, 2 weeks before)
- Describe the format: classroom, e-learning, job aids, or a combination — with justification
- Explain why training should focus on job-role workflows, not just software navigation
- Identify one metric you would track to confirm training effectiveness before go-live

Write your response in 150-200 words.

---

## Part D: Go-Live Readiness (30 points)

### D-1: Go-Live Readiness Assessment

It is 3 weeks before Meridian's scheduled go-live date. You have received the following status report from the project team. For each item, indicate: Green (ready), Yellow (at risk, action needed), or Red (not ready — do not go live).

| Readiness Item | Status (G/Y/R) | Reasoning |
|---|---|---|
| UAT: Finance scenarios tested, 3 Critical defects remain open (all are payroll-related) | | |
| UAT: Procurement scenarios fully tested, all defects resolved, sign-off obtained | | |
| Data migration: 6,200 of 8,400 vendor records cleaned; 2,200 records awaiting review | | |
| User training: 87% of AP clerks trained; 13% have not yet attended | | |
| Integration testing: SAP-to-SuccessFactors payroll integration tested and passing | | |
| Rollback plan: Documented and distributed to all team members | | |
| Helpdesk: Post-go-live support procedure is drafted but not yet approved by IT Director | | |

### D-2: Go/No-Go Recommendation

Based on your readiness assessment above, write a 175-225 word go/no-go recommendation memo addressed to the CFO. Your memo must:

- State your recommendation clearly (go live as scheduled, go live with conditions, or delay)
- Reference at least two specific items from your readiness assessment as evidence
- Address the board pressure the CFO is under and explain how the recommendation serves the organization's long-term interests
- Identify any conditions that must be met if you are recommending conditional go-live

---

## Grading Rubric

| Section | Points | Criteria |
|---|---|---|
| A-1: Phase mapping with justifications | 10 | All 6 activities mapped to correct phase, justification accurate |
| A-2: Gap classification with justification | 10 | All 4 gaps correctly classified A/B/C, justification accurate |
| B-1: Risk register with 6 risks | 15 | Risks specific to Meridian, all fields completed, scores calculated, mitigations actionable |
| B-2: Risk priority matrix | 10 | All 6 risks placed in correct quadrant with management implication described |
| C-1: Stakeholder analysis | 10 | All 4 groups with sentiment grounded in scenario evidence, actions specific |
| C-2: Super-user network design | 8 | Number/distribution justified, training described, role defined, incentive identified |
| C-3: Training plan | 7 | Timing specified, format justified, workflow-vs-navigation distinction explained, metric identified |
| D-1: Readiness assessment | 12 | All 7 items rated with accurate reasoning per module definitions |
| D-2: Go/no-go memo | 18 | 175-225 words, clear recommendation, evidence cited, board pressure addressed, conditions stated |
| **Total** | **100** | |

---

## Submission Instructions

1. Compile all responses into a single document.
2. Name your file: `Lab04_LastName_FirstName.pdf`
3. Upload to Canvas under "Lab 04 — ERP Implementation Lifecycle."
4. Deadline: See course schedule in Canvas. Late submissions lose 10 points per day.

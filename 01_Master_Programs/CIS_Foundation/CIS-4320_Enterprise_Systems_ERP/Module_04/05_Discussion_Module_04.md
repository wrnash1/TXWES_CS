# Discussion Forum: Module 04 - ERP Implementation Lifecycle

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

---

## Overview

This forum asks you to analyze implementation scenarios using the concepts from Module 04 — SAP Activate phases, change management, testing, and go-live readiness. Choose one scenario, write an analytical original post, and respond substantively to two classmates who chose different scenarios.

---

## Instructions

### Initial Post (Due Wednesday at 11:59 PM)

Choose **one** of the three scenarios below (A, B, or C). Write a response of **175-225 words** directly addressing the questions for your scenario. State your scenario choice at the start of your post.

Your post must:

- Identify which SAP Activate phase or implementation activity is most relevant to the scenario
- Apply at least one named concept from the Module 04 reading guide (change management, UAT, Fit-to-Standard, super-user, rollback plan, hypercare, etc.)
- Make a concrete recommendation supported by specific reasoning from the scenario

### Peer Responses (Due Sunday at 11:59 PM)

Reply to at least **two classmates** who chose **different scenarios** from yours. Each reply must be at least 60 words and do one of the following:

- Add a risk or consequence your classmate did not mention
- Challenge the recommendation your classmate made and explain your alternative
- Connect the scenario to a real-world ERP failure or success story you know of (general knowledge is fine — no fabricated citations)

---

## Scenarios

### Scenario A: The Compressed Timeline

A $300 million food distribution company is implementing SAP S/4HANA. The CEO announced a go-live date 14 months from now in an all-hands meeting — without consulting the project team. The SAP implementation partner estimates the project requires 20 months to properly complete the Explore and Realize phases, validate data quality, train 600 users, and test all integrations. The CEO refuses to extend the timeline because the board made a public commitment to investors. Three weeks before the announced go-live date, UAT is only 60% complete and the data migration team reports that 25% of vendor master records still have data quality issues.

**Your task:** Which SAP Activate phase(s) appear to have been compressed or skipped based on the evidence? What are the two most significant risks of proceeding with a go-live at the announced date? As the project manager, what recommendation would you make to the CEO and what evidence would you bring to the conversation?

### Scenario B: The Resistant Finance Team

A regional healthcare system has completed an SAP implementation. Go-live was 6 weeks ago. The system is technically functioning correctly — all integration tests passed, performance tests passed, and no Critical defects were found in UAT. However, the 80-person Finance team reports daily that the system is "too confusing" and is routing invoices through email rather than using the SAP workflow. AP processing time has actually increased from 4 days to 11 days since go-live. Two finance managers have submitted formal complaints to the CFO asking to return to the old system.

**Your task:** Is this a technical problem or a change management problem? What specific change management failures from the Module 04 framework can you identify in this scenario? What three specific actions would you recommend to the project sponsor to reverse the adoption problem? What metric would you use to measure whether the interventions are working?

### Scenario C: The Data Discovery

An organization is in the Realize phase of a Salesforce Sales Cloud implementation. The data migration team has completed the Extract step and is analyzing the legacy CRM data. They discover the following: 42,000 Account records (the target Salesforce environment is licensed for 50,000 Accounts); 38% of Account records have duplicate entries for the same company under different name spellings; 22% of Contact records have invalid email addresses (missing @ symbol or invalid domain); and 15% of Opportunity records reference Account IDs that no longer exist in the source system.

**Your task:** Which of these data issues is the most critical to resolve before loading into Salesforce and why? Describe the Transform step actions needed to address each of the four issues. If the team discovers on go-live weekend that the duplicate Account problem was not fully resolved and 4,000 duplicate Accounts were loaded into production, what is the immediate action and long-term consequence?

---

## Discussion Rubric

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted by Wednesday 11:59 PM | 1 | On-time submission |
| Scenario identified at start of post | 1 | Clearly states scenario letter |
| Correct SAP Activate phase or implementation activity identified | 1 | Named and applied correctly to scenario |
| Named Module 04 concept applied with specificity | 2 | Concept named and connected to scenario details, not just defined |
| Concrete recommendation with specific reasoning | 1 | Recommendation actionable, grounded in scenario evidence |
| **Initial Post Subtotal** | **6** | |
| Peer response 1: 60+ words, adds new dimension | 2 | Extends, challenges, or adds real-world context |
| Peer response 2: 60+ words, adds new dimension | 2 | Same criteria |
| **Peer Response Subtotal** | **4** | |
| **Total** | **10** | |

---

## Professor Nash's Note

Scenario A is based on a pattern that repeats constantly in real implementations: executive announcements that set unrealistic timelines before the project team has assessed scope. The certification exams test your knowledge of the phases and what happens when they are compressed. But more importantly, if you ever find yourself in this situation professionally — and you very likely will — you need to know what the evidence-based recommendation is and how to present it to a CEO. That is the skill this discussion develops.

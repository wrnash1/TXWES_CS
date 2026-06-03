# Lab: Module 15 — ERP Implementation Methodology

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Lab Overview

In this lab you will act as a junior implementation consultant assigned to plan a Salesforce CRM implementation for a fictional mid-sized company. You will produce four deliverables: a scoped project overview, a simplified fit-gap log, a role-based training plan, and a cutover weekend task list. This simulates the core planning artifacts produced across the Discover, Define, and Final Preparation phases of a real implementation.

**Estimated Time:** 80–95 minutes

**Deliverables:** One Word or PDF document containing all four parts, submitted to the course LMS.

---

## Scenario

Ridgeline Supply Co. is a regional industrial equipment distributor with 220 employees across three states (Texas, Oklahoma, and Arkansas). They currently track customers in spreadsheets, manage sales opportunities in email and sticky notes, and log service cases in a shared inbox. Customer data is siloed — sales reps do not know when a customer has an open service issue, and service reps do not know a customer's purchase history.

Leadership has approved a Salesforce Sales Cloud and Service Cloud implementation. The go-live target is 14 weeks from today. The implementation team includes: one Salesforce Administrator (you), one part-time Salesforce Developer, and a business analyst. Three business process owners are available for workshops: the VP of Sales, the Service Manager, and the IT Director.

Your job is to plan the implementation.

---

## Part A — Project Scope and Phase Plan (20 minutes)

### A1 — Scope Statement

Write a project scope statement for the Ridgeline Supply Co. implementation. Your scope statement must address all five of the following elements:

1. **In-scope modules** — List the Salesforce products and features that will be implemented (e.g., Sales Cloud, Service Cloud, specific features within each).

2. **In-scope business processes** — List at least four specific business processes that will be supported by the implementation (e.g., lead management, opportunity tracking).

3. **Out-of-scope items** — List at least three items explicitly excluded from this implementation. Explain briefly why each is out of scope (e.g., deferred to Phase 2, not feasible in timeline, requires separate procurement).

4. **Key integrations** — Identify any systems Salesforce will need to connect to. For Ridgeline, consider: their accounting system (QuickBooks), their product catalog (an internal spreadsheet), and their email platform (Microsoft 365).

5. **Data migration scope** — Describe what legacy data will be migrated into Salesforce (from spreadsheets and the shared inbox) and what will not be migrated.

Your scope statement should be 200–300 words.

### A2 — Phase Timeline

Create a phase timeline table showing all six Salesforce implementation lifecycle phases mapped to a 14-week calendar. For each phase, specify:

- Phase name
- Weeks allocated (e.g., Weeks 1–2)
- Primary activities (2–3 bullet points)
- Key deliverable

Format as a table with five columns: Phase, Weeks, Duration, Primary Activities, Deliverable.

Note: Some phases may overlap (e.g., Build and Test often run concurrently in the final sprints). Your timeline must be realistic given the 14-week constraint and the team size described.

---

## Part B — Fit-Gap Log (20 minutes)

A fit-gap log documents each business requirement, whether standard Salesforce functionality meets it (fit) or does not (gap), and how the gap will be resolved.

### Instructions

Using the Ridgeline scenario, create a fit-gap log with at least eight entries. Your entries must include at least:

- Two items that are a full fit (standard Salesforce functionality meets the requirement without any customization)
- Three items that are a partial fit (standard functionality exists but requires configuration)
- Two items that are a gap requiring custom development or a third-party app
- One item that should be resolved through a process change (Salesforce cannot do it the way the business currently does it, but the business should adapt to the standard Salesforce approach)

### Fit-Gap Log Template

| Requirement | Source | Fit/Gap | Resolution Approach | Owner | Priority |
|---|---|---|---|---|---|
| (describe the business requirement) | (Sales / Service / IT) | (Full Fit / Partial Fit / Gap / Process Change) | (describe how it will be addressed) | (VP Sales / Service Mgr / IT Dir) | (High / Medium / Low) |

Complete at least eight rows. Write requirements in plain language that a business stakeholder would recognize (e.g., "Sales reps need to see a customer's open service cases when viewing the account" — not "Implement related list on Account layout").

---

## Part C — Role-Based Training Plan (20 minutes)

Ridgeline will have four distinct user groups in Salesforce:

- **Sales Representatives** (12 users) — manage leads, contacts, accounts, opportunities
- **Service Representatives** (8 users) — manage cases, knowledge articles, service reports
- **Sales Managers** (3 users) — all sales rep capabilities plus reports, dashboards, and team management
- **System Administrator** (1 user — you) — full platform administration

### Instructions

Create a training plan table with one row per user group. For each group, specify:

- User group name and headcount
- Salesforce features they need to be trained on (list at least four specific features per group)
- Recommended training format (instructor-led, self-paced Trailhead, hands-on sandbox, or a combination)
- Estimated training hours
- Recommended timing relative to go-live (e.g., "3 weeks before go-live")
- Job aid or support material needed post-go-live

After the table, write a short paragraph (75–100 words) explaining your timing rationale — why you chose the training window you did for each group, and what risk you would face if training were compressed into the final week before go-live.

---

## Part D — Cutover Weekend Task List (20 minutes)

Ridgeline's go-live is scheduled for a Monday. Cutover activities will begin Friday at 5:00 PM and must be complete by Sunday at 6:00 PM, leaving 12 hours for final checks before Monday morning.

### Instructions

Create a detailed cutover task list with at least 12 tasks. Each task must include:

- Task number (sequential)
- Task description
- Owner (name a role: Admin, Developer, Business Analyst, VP Sales, IT Director)
- Estimated duration
- Dependency (which prior task number must be complete first; use "None" for tasks that can start immediately)
- Go/no-go checkpoint (Yes/No — mark Yes for tasks where failure means cutover stops)

Your task list must include tasks from all of the following categories:

- Legacy system freeze (halting new entries in spreadsheets and shared inbox)
- Data extraction from legacy sources
- Data migration load into Salesforce (at least two load tasks: one for accounts/contacts, one for open opportunities or cases)
- Data validation (verifying migrated record counts and spot-checking data quality)
- Integration activation (turning on the Microsoft 365 email integration)
- Smoke testing (verifying that critical business processes work in production)
- Go/no-go decision point
- User notification (communicating to all users that the system is live)

After the task list, write a brief paragraph (50–75 words) identifying the single highest-risk task in your cutover plan and explaining your contingency approach if that task fails or takes longer than estimated.

---

## Submission Checklist

Before submitting, verify your document contains:

- [ ] Part A1: Scope statement (200–300 words, all five elements addressed)
- [ ] Part A2: Phase timeline table (all six phases, 14-week calendar, primary activities and deliverables)
- [ ] Part B: Fit-gap log (at least 8 rows with correct fit/gap classifications)
- [ ] Part C: Training plan table (all four user groups) plus timing rationale paragraph
- [ ] Part D: Cutover task list (at least 12 tasks, all required categories present) plus risk paragraph

---

## Grading Criteria

| Component | Points |
|---|---|
| Part A1 — Scope statement completeness and realism | 15 |
| Part A2 — Phase timeline accuracy and feasibility | 15 |
| Part B — Fit-gap log quality and classification accuracy | 25 |
| Part C — Training plan completeness and timing rationale | 20 |
| Part D — Cutover task list completeness and risk analysis | 25 |
| **Total** | **100** |

---

*End of Lab — Module 15*

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

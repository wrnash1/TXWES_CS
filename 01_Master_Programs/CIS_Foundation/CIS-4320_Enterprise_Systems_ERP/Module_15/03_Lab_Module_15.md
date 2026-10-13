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

---

## Part 9 — Challenge Exercise

### Challenge 1: Implementation Failure Post-Mortem Analysis

A regional grocery chain (320 stores, $2.1 billion revenue) attempted to implement SAP S/4HANA with integrated warehouse management, supply chain planning, and financial accounting. After 22 months of implementation, the project was abandoned with $47 million spent and no go-live. A post-mortem identified the following facts:

- The original timeline was 14 months; it expanded to 22 months with two scope additions approved without formal change control
- UAT was compressed from the planned 8 weeks to 3 weeks due to timeline pressure
- The cutover was attempted in November — the highest-volume period of the year
- Key business stakeholders stopped attending design workshops in month 8, delegating to junior staff who lacked decision authority
- The fit-gap log identified 73 gaps; 28 were resolved with custom development that was never fully tested end-to-end
- No mock cutovers were conducted; the production cutover was the first full rehearsal
- When the live system showed critical inventory errors 6 hours after go-live, the team had no documented cutback plan and spent 14 hours attempting fixes before abandoning the go-live

1. Apply the ASAP/SAP Activate methodology framework to categorize each of the seven identified failure factors by the phase in which the failure originated (Prepare, Explore/Blueprint, Realize, Final Preparation, Deploy/Go-Live). For each factor, explain which specific phase deliverable or practice was missing or inadequate.
2. The 28 custom developments that were never fully tested end-to-end represent a testing governance failure. Design a testing governance framework for this project that would have prevented this outcome. Include: the testing types required (unit, integration, regression, UAT), who is responsible for each, what the acceptance criteria are, and what "done" looks like for each type before the project can advance to the next phase.
3. The project team had no documented cutback plan. Construct the key elements of a cutback plan for a grocery chain go-live: what triggers the cutback decision, who has authority to call the cutback, what are the technical steps to restore the legacy system, what data needs to be reconciled, and what is the communication plan for store operations if a cutback is executed on a Sunday morning.
4. Write a lessons-learned executive summary (200–250 words) addressed to the grocery chain's Board of Directors. Summarize the three highest-impact failures, quantify the estimated cost of each failure (use reasonable estimates), and recommend three specific governance changes that must be implemented before any future ERP attempt is authorized.

### Challenge 2: Phased Salesforce Implementation Design for a Professional Services Firm

A 600-person consulting firm is implementing Salesforce for the first time. Currently: sales tracks opportunities in spreadsheets, service delivery tracks project hours in a separate time-tracking tool, HR manages headcount in a third system, and finance invoices clients from a legacy billing system. The CIO wants to implement Salesforce Sales Cloud, Service Cloud, and a Salesforce-to-accounting integration in 18 months.

1. Design a phased implementation plan. Divide the 18 months into phases, specifying: what is implemented in each phase, why that sequence is correct (what dependencies exist between phases), and what the go-live definition is for each phase. Address why Sales Cloud should or should not be implemented before Service Cloud in this firm's context.
2. The ADKAR model predicts that consultants — knowledge workers who are highly self-directed — will experience a specific pattern of resistance. Predict which ADKAR element is most likely to be the gap for three different user groups: (a) senior partners who generate most of the firm's revenue, (b) junior associates who will use Salesforce daily for time entry, and (c) the finance team who will lose direct control of the invoicing system. For each group, recommend a specific change management intervention.
3. The firm's CIO wants to measure implementation success. Design a success metrics framework with two types of metrics: (a) implementation health metrics tracked weekly during the project (at least four metrics), and (b) business outcome metrics tracked monthly for 12 months post-go-live (at least four metrics). For each metric, specify the data source, the target, and the escalation threshold.
4. Six months after Salesforce Sales Cloud goes live, a senior partner reports that her team still uses their personal spreadsheets for opportunity tracking and only enters deals into Salesforce after they close. This is adoption regression. Write a three-step intervention plan that addresses the ADKAR Desire and Reinforcement gaps for this group — including specific actions, who owns each action, and the timeline.

### Reflection Questions

1. Both challenges involve situations where executive engagement declined during the implementation — the grocery chain's stakeholders stopped attending workshops, and the consulting firm's senior partners bypassed the system. In both cases, the project team had technical solutions ready but lacked organizational authority to enforce adoption. What structural governance mechanism (beyond the change management team) should be designed into an ERP implementation from the start to ensure that business stakeholders remain accountable for their participation commitments throughout the project lifecycle?
2. The grocery chain's post-mortem revealed that the project team knew about the testing gaps and the missing cutback plan but proceeded anyway under schedule pressure. This describes a failure of project escalation — the team did not stop or escalate despite knowing the go-live was unsafe. Design an escalation decision tree for an ERP implementation that defines: what conditions require escalation to the steering committee, what conditions require a mandatory go-live pause, and what conditions require the project sponsor to make a formal go/no-go decision in writing at least 30 days before go-live.

*End of Lab — Module 15*

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

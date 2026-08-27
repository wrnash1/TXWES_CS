# Reading Guide: Module 03 – Scope Management: WBS and Scope Statement

**Course:** CIS-3310 IT Project Management
**Certification Alignment:** CompTIA Project+ (PK0-005) | PMBOK 6th and 7th Editions
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Scope Management is the discipline of defining exactly what the project will and will not produce, then protecting that definition from unauthorized change. It is the root cause of the majority of IT project failures. Unclear scope leads to missed deadlines, budget overruns, team conflicts, and dissatisfied customers. This module equips you with the tools — the Scope Statement, WBS, and WBS Dictionary — to define scope precisely and defend it consistently.

---

## 1. High-Yield Glossary

### Product Scope

The features, functions, and characteristics of the product, service, or result being created. Product scope answers: "What will this thing do?" Completion is measured against the product requirements.

### Project Scope

All the work required to deliver the product scope. Project scope answers: "What must we do to build it?" Completion is measured against the Project Management Plan.

### Project Scope Statement

A formal document that defines project deliverables, acceptance criteria, exclusions, constraints, and assumptions. It is produced during Planning (Plan Scope Management process) and forms the foundation of the Scope Baseline.

### Scope Baseline

The approved version of the Scope Statement, WBS, and WBS Dictionary. The Scope Baseline is a component of the Project Management Plan. All scope change requests are measured against the Scope Baseline.

### Work Breakdown Structure (WBS)

A hierarchical decomposition of the total project scope into deliverable-oriented components. The WBS visually represents all project work. The 100% Rule requires that the WBS include 100% of the approved scope — no more, no less.

### Work Package

The lowest level of the WBS. A work package is a deliverable-oriented unit of work that can be assigned to a single owner, estimated, scheduled, and tracked. Work packages are the inputs to schedule and cost estimation.

### WBS Dictionary

A companion document to the WBS providing detailed information for each WBS element: description of work, responsible owner, activity list, acceptance criteria, estimated cost, estimated duration, and dependencies.

### Scope Creep

The uncontrolled expansion of project scope through informal requests or additions that bypass the formal change control process. Scope creep is one of the leading causes of project failure.

### Gold Plating

The practice of the project team voluntarily adding features, deliverables, or work beyond what was approved — often with good intentions but without authorization. Gold plating wastes resources and may introduce quality or integration issues.

### Validate Scope

The Executing process of formally obtaining the customer's or sponsor's acceptance of completed project deliverables. Output: accepted deliverables. Performed WITH the customer.

### Control Scope

The Monitoring and Controlling process of monitoring project scope status and managing changes to the Scope Baseline. Catches scope creep and routes unauthorized scope additions to integrated change control. Performed BY the PM.

### Requirements Documentation

A detailed record of all requirements (functional, non-functional, business, stakeholder, quality, and transition) the project's product must meet. Produced during Planning and used as the basis for the Scope Statement and WBS.

### Requirements Traceability Matrix (RTM)

A table that links each requirement to its source, the WBS element that delivers it, and the test case that validates it. Ensures no requirement is lost or delivered without validation.

---

## 2. Scope Management Process Flow

The six processes in PMI Scope Management and their Process Group placement:

| Process | Process Group | Primary Output |
|---|---|---|
| Plan Scope Management | Planning | Scope Management Plan |
| Collect Requirements | Planning | Requirements Documentation, RTM |
| Define Scope | Planning | Project Scope Statement |
| Create WBS | Planning | WBS, WBS Dictionary, Scope Baseline |
| Validate Scope | Executing | Accepted Deliverables |
| Control Scope | Monitoring and Controlling | Work Performance Information, Change Requests |

---

## 3. WBS Structure and the 100% Rule

A properly constructed WBS has the following structural properties:

- Level 1: Project name (the entire project)
- Level 2: Major deliverables or phases (e.g., Project Management, Requirements, Design, Build, Testing, Deployment)
- Level 3: Sub-deliverables within each major deliverable
- Level 4 (and below): Work packages — the lowest estimatable and assignable units

The 100% Rule states that the WBS must include 100% of the work defined in the project scope and capture all deliverables — internal, external, and interim. If a deliverable is missing from the WBS, it is effectively invisible to the project manager for scheduling and cost purposes.

### WBS Work Package Sizing Guidelines

The "8/80 Rule" is a common heuristic: a work package should represent no fewer than 8 hours and no more than 80 hours of effort. Work packages smaller than 8 hours create excessive administrative overhead; work packages larger than 80 hours are too large to estimate and control accurately.

---

## 4. Scope Statement Components Reference Table

| Component | Definition | Example for an IT Project |
|---|---|---|
| Product Scope Description | What the product will do and its key features | "Web application with SSO, mobile-responsive UI, and Salesforce API integration" |
| Project Deliverables | Specific outputs the project will produce | Requirements doc, design spec, tested application, training guide |
| Acceptance Criteria | Measurable conditions for stakeholder acceptance | "System processes 500 concurrent sessions with < 2 sec response" |
| Exclusions | What the project will NOT deliver | "Custom reporting module; data migration from legacy system" |
| Constraints | Conditions limiting the project | "Must use existing AWS infrastructure; go-live by October 1" |
| Assumptions | Believed true but unconfirmed | "Existing bandwidth supports new system load" |

---

## 5. Scope Creep vs. Gold Plating

| Attribute | Scope Creep | Gold Plating |
|---|---|---|
| Source | External — stakeholder or client request | Internal — team member's initiative |
| Authorization | Bypasses change control | Bypasses change control |
| Intent | Usually not malicious — just informal | Usually well-intentioned |
| Impact | Unplanned work, budget/schedule overrun | Unplanned work, may introduce defects |
| PM Response | Route through change control; stop unauthorized work | Educate team; reinforce scope discipline |
| Exam tip | Associated with "informal requests from stakeholders" | Associated with "team adds unrequested features" |

---

## 6. Validate Scope vs. Control Scope

| Attribute | Validate Scope | Control Scope |
|---|---|---|
| Process Group | Executing | Monitoring and Controlling |
| Who is involved | Customer/Sponsor + Project Team | Project Manager |
| Purpose | Formal acceptance of completed deliverables | Monitor scope status; manage changes |
| Output | Accepted deliverables | Work performance information; change requests |
| When does it occur | When deliverables are completed | Continuously throughout the project |
| Exam tip | "Customer formally accepts the deliverable" | "PM catches unauthorized scope addition" |

---

## 7. Certification Exam Tips

**Tip 1 — WBS is nouns, not verbs:**
The WBS is deliverable-oriented. Entries should be noun phrases representing things produced, not actions taken. "Tested application" is correct; "Test application" is a task list item.

**Tip 2 — 100% Rule means everything:**
If a deliverable is missing from the WBS, it is not in the project plan. Missing WBS elements = missing cost estimates, missing schedule activities, and missing resource assignments. The 100% Rule protects against this.

**Tip 3 — Work packages are not tasks:**
Work packages are the lowest WBS level. Activities and tasks are derived from work packages during schedule development. The exam tests this distinction in questions about WBS decomposition.

**Tip 4 — Scope Baseline = three documents:**
The Scope Baseline is always three things together: Scope Statement + WBS + WBS Dictionary. If a question asks what comprises the Scope Baseline, all three must be listed.

**Tip 5 — Validate Scope can reveal defects:**
When the customer inspects deliverables during Validate Scope and finds problems, the output is a change request (to fix the defects), not just acceptance. Students think Validate Scope always ends in acceptance — it does not.

**Tip 6 — Control Scope is about change, not work:**
Control Scope does not mean doing the work — it means managing changes to what the work is. When a stakeholder informally requests a new feature, Control Scope is the process that catches it and routes it to Integrated Change Control.

**Tip 7 — RTM connects requirements to WBS:**
The Requirements Traceability Matrix is how the PM proves that every approved requirement is covered by a WBS work package and will be tested. It is a governance and audit tool as much as a planning tool.

**Tip 8 — Exclusions are as important as inclusions:**
Exam scenario questions frequently describe a stakeholder claiming a feature was always "implied" or "assumed." Documenting exclusions in the Scope Statement is the PM's defense. Unstated exclusions become future change requests.

---

## 8. Required Reading and Study Resources

Complete the following before the lab and quiz:

- Read the scope management chapters in the course OER textbook (linked in Canvas), focusing on WBS construction and scope baseline components.
- Review the CompTIA Project+ PK0-005 exam objectives at comptia.org for the scope management domain.
- For supplemental study, visit professormesser.com for Project+ scope management coverage.

---

## 9. Study Checklist

- [ ] Distinguish product scope from project scope using an original IT example
- [ ] List all six components of a Project Scope Statement
- [ ] Explain the 100% Rule and give an example of what happens when it is violated
- [ ] Define work package and explain the 8/80 rule
- [ ] Draw or describe a 3-level WBS for a hypothetical IT project
- [ ] Explain the difference between scope creep and gold plating
- [ ] State the three documents that together form the Scope Baseline
- [ ] Compare Validate Scope and Control Scope using the table in Section 6
- [ ] Explain what a Requirements Traceability Matrix does and why it matters
- [ ] Complete the Module 03 Lab activity
- [ ] Take the Module 03 Quiz
- [ ] Post Module 03 Discussion initial response by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

The following free, openly licensed resources extend the concepts in this module. All links are publicly accessible — no account or purchase required.

1. **Project Management Open Textbook — Chapter 5: Scope Management**
   *BC Campus OpenEd* — [opentextbc.ca/projectmanagement — Chapter 5](https://opentextbc.ca/projectmanagement/chapter/chapter-5-project-scope-management/)
   Covers the full Scope Management knowledge area including WBS construction, scope verification, and scope control. Includes worked examples applicable to IT projects.

2. **PMI — Practice Standard for Work Breakdown Structures (Free Overview)**
   *Project Management Institute* — [pmi.org/pmbok-guide-standards/practice-guides/wbs](https://www.pmi.org/pmbok-guide-standards/practice-guides/wbs)
   PMI's official guidance on WBS best practices including the 100% Rule, decomposition depth, and WBS Dictionary requirements.

3. **WBS Tutorial — Lucidchart (Free)**
   [lucidchart.com/blog/work-breakdown-structure](https://www.lucidchart.com/blog/work-breakdown-structure)
   Visual guide to building a WBS with examples across multiple project types. Includes templates usable with the free tier of Lucidchart.

4. **YouTube — "Work Breakdown Structure Explained" (Mike Clayton / OnlinePMCourses)**
   [youtube.com/watch?v=_OIcFkjGBO8](https://www.youtube.com/watch?v=_OIcFkjGBO8)
   A 12-minute video walkthrough of WBS structure, the 100% Rule, and WBS Dictionary creation. Directly supports the Module 03 lab.

5. **Scope Creep vs. Gold Plating — PM Study Circle**
   [pmstudycircle.com/scope-creep-vs-gold-plating](https://pmstudycircle.com/scope-creep-vs-gold-plating/)
   Concise explanation of the difference between scope creep and gold plating with exam-focused examples. Targets one of the most commonly missed distinctions on the Project+ exam.

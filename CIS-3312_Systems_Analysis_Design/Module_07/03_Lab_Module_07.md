# Lab Activity: Module 07 — Requirements Elicitation Techniques

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Total Points:** 100
**Certification Alignment:** IIBA ECBA

---

## Scenario: Rampart County Public Library System

Rampart County Public Library System (RCPLS) serves a county population of 187,000 through a central library and four branch locations. The library currently uses a legacy integrated library system (ILS) that was installed in 2009. The system manages catalog records, patron accounts, checkouts, holds, and fines. The system is no longer supported by the vendor, and the county has approved a budget for replacement.

The library director has hired you as the BA responsible for eliciting requirements for the new ILS. You have been given access to the following stakeholders and resources:

- **Director of Library Services** — executive sponsor; focused on community access and strategic outcomes
- **Circulation Manager** — responsible for daily checkout and return operations; manages 12 circulation staff
- **Cataloging Librarian** — responsible for catalog records, metadata standards, and acquisitions
- **IT Manager** — responsible for infrastructure, integrations, and security; concerned about vendor support and cloud hosting
- **Branch Managers** — four managers, each responsible for a branch location; varying levels of technical literacy
- **Patron Advisory Committee** — six community members representing library users; varying backgrounds
- **Current system documentation** — user manual (2009), data dictionary (2009), workflow procedures (last updated 2017)

You will complete four exercises covering elicitation strategy, interview design, document analysis, and requirements documentation.

---

## Exercise 1: Elicitation Strategy (25 points)

Before conducting any elicitation, a BA develops an elicitation plan — a structured approach to deciding which techniques to use, with whom, and in what sequence.

### Task 1a: Stakeholder analysis

Complete the stakeholder analysis table below for the six stakeholder groups listed. For each group, assess their interest level (High/Medium/Low), influence level (High/Medium/Low), and assign a primary elicitation technique from the following list: individual interview, workshop, observation, survey, document analysis.

| Stakeholder Group | Interest Level | Influence Level | Primary Elicitation Technique | Justification (one sentence) |
|---|---|---|---|---|
| Director of Library Services | | | | |
| Circulation Manager | | | | |
| Cataloging Librarian | | | | |
| IT Manager | | | | |
| Branch Managers (4) | | | | |
| Patron Advisory Committee (6) | | | | |

### Task 1b: Elicitation sequence

Write a 100–150 word justification for the order in which you would conduct your elicitation activities. Address:

- Which activity should come first and why
- Whether document analysis should precede or follow stakeholder interviews, and why
- How you would use findings from one technique to inform the next

### Task 1c: JAD session rationale

The circulation manager and the IT manager have conflicting requirements: the circulation manager wants real-time fine calculation visible during patron checkout, while the IT manager wants fine calculations processed in batch at end of day to reduce system load. Write 75–100 words explaining whether you would recommend a JAD session to resolve this conflict and what you would hope to achieve from it.

---

## Exercise 2: Interview Design (25 points)

You are preparing to conduct a semi-structured interview with the Circulation Manager. The interview will last 45 minutes and focus on understanding how the current checkout, return, and hold processes work, what problems exist with the current system, and what the Circulation Manager needs from the new system.

### Task 2a: Interview question set

Write 10 interview questions for the Circulation Manager. Your questions must include:

- At least four open-ended questions that begin with "Describe," "Tell me," or "Walk me through"
- At least three probing follow-up questions (questions that probe a specific expected topic from a prior answer, formatted as: "You mentioned X — can you describe a situation where...")
- At least two questions specifically designed to surface unstated or tacit requirements (questions about exceptions, failures, workarounds, or informal practices)
- At least one question about success criteria ("How will you know the new system is working well?")

Label each question with its type (open-ended, probing, tacit-surfacing, or success criteria).

### Task 2b: Interview logistics plan

Write 75–100 words describing your preparation and logistics for this interview. Address:

- Where and when the interview will be held
- Whether you will record the session and how you will handle consent
- How you will organize your notes during the interview
- What you will send the Circulation Manager after the interview and why

---

## Exercise 3: Document Analysis (25 points)

You have reviewed the following documents from RCPLS. For each document, extract at least two requirements, constraints, or issues that a BA would identify and document.

### Document 1: Current System Data Dictionary (excerpt)

The current ILS data dictionary shows the following patron record fields: PatronID (integer), FirstName (varchar 50), LastName (varchar 50), Address (varchar 200), Phone (varchar 15), Email (varchar 100), CardExpiry (date), BalanceDue (decimal 8,2), ActiveStatus (char 1: A=Active, S=Suspended, E=Expired).

**Extract from this document (at least two findings):**

Finding 1: _______________

Finding 2: _______________

### Document 2: Workflow Procedures Manual (excerpt)

The procedure for renewing an overdue item reads: "The circulation staff member must first verify the patron has no outstanding fines over $5.00. If fines are over $5.00, the renewal is denied. If fines are $5.00 or under, the item may be renewed for one standard loan period. Exception: Items with three or more holds may not be renewed regardless of fine balance. Staff must check the holds queue manually in a separate screen."

**Extract from this document (at least two findings):**

Finding 1: _______________

Finding 2: _______________

### Document 3: Director's Strategic Plan (excerpt)

The five-year strategic plan states: "RCPLS will expand digital equity access by providing card-free service options for patrons who may not have a physical library card. All patron-facing services will be accessible via mobile devices. RCPLS will comply with all applicable accessibility standards including WCAG 2.1 Level AA."

**Extract from this document (at least two findings):**

Finding 1: _______________

Finding 2: _______________

### Task 3b: Document analysis limitations

Write 75–100 words explaining one specific risk of relying solely on the 2009 data dictionary and 2017 workflow procedures for requirements. What validation technique would you use to address this risk, and what specifically would you look for?

---

## Exercise 4: Requirements Documentation (25 points)

Based on the information gathered from Exercises 1–3 and your knowledge of the scenario, draft requirements for the new ILS in three categories.

### Task 4a: Business requirements (two required)

Business requirements describe why the organization needs the new system — the goals and outcomes it must achieve.

Write two business requirements using this format: "The new integrated library system must [enable/support/ensure] [business outcome] in order to [strategic goal]."

### Task 4b: Functional requirements (four required)

Functional requirements describe what the system must do. Write four functional requirements using this format: "The system shall [action] [object/data] [condition/constraint]."

At least one of your four functional requirements must address:

- The fine balance renewal rule from Document 2
- The card-free access requirement from Document 3

### Task 4c: Non-functional requirements (two required)

Non-functional requirements describe quality attributes — how the system must perform. Write two non-functional requirements addressing any two of the following quality attributes: performance, accessibility, security, availability, or usability.

### Task 4d: Requirements quality check

Review your six functional and non-functional requirements from Tasks 4b and 4c. For each requirement, evaluate it against these three quality criteria and mark Pass or Fail:

| Requirement | Clear (unambiguous)? | Verifiable (testable)? | Traceable (linked to a source)? |
|---|---|---|---|
| FR-1 | | | |
| FR-2 | | | |
| FR-3 | | | |
| FR-4 | | | |
| NFR-1 | | | |
| NFR-2 | | | |

For any requirement that fails one or more criteria, revise it to address the failure and explain what you changed.

---

## Submission

Submit your completed lab document to the Canvas assignment portal by the due date. All exercises must be substantively completed. Requirements must be written in full sentences using the specified formats — not described in abstract terms. Show your reasoning, not just your conclusions.

**Grading:** Each exercise is worth 25 points, distributed across tasks based on completeness, accuracy, and application of elicitation and requirements concepts.

---

## Part 9 — Challenge Exercise

This section is optional and not separately graded. It extends the lab into advanced elicitation and requirements management practice aligned with ECBA exam competencies.

### Challenge Step 1: Elicitation Risk Assessment

Using the case study from your assigned lab, identify the top three elicitation risks that could prevent you from gathering complete, accurate requirements. For each risk:

- Describe the risk in one sentence (what could go wrong)
- Identify the BABOK KA 4 task most affected by this risk
- Describe a specific mitigation strategy the BA should implement before the risk materializes

Format your assessment as a three-row risk table with columns: Risk Description | Affected KA 4 Task | Mitigation Strategy. This exercise develops the analytical habit of proactively managing elicitation quality rather than reacting to requirements gaps after they cause downstream problems.

### Challenge Step 2: Stakeholder Communication Plan

Select three stakeholders from the case study. For each stakeholder, design a tailored communication approach covering: the elicitation technique(s) most appropriate for this stakeholder and why, the format and frequency of requirements updates you will send them, the specific risk to requirements quality if this stakeholder is under-engaged, and one concrete action you will take if this stakeholder becomes unavailable during the elicitation phase. Present your plan as a structured table. This exercise integrates KA 2 stakeholder engagement planning with KA 4 elicitation technique selection.

### Challenge Step 3: Requirements Baseline Change Scenario

Assume you have completed elicitation and the requirements are baselined. Two weeks later, a stakeholder sends an email requesting a significant change — they want to add a feature that was explicitly descoped at the project kickoff. Write a formal Change Impact Assessment memo covering: what the proposed change is, which baselined requirements it would affect, the estimated impact on project scope, schedule, and budget (high/medium/low with brief rationale), and your recommendation (accept, modify, or reject) with justification. This exercise practices BABOK KA 6 requirements change control in a realistic scenario.

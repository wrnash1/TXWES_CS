# Lab Activity: Module 05 - Use Case Modeling and User Stories

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University
**Total Points:** 100

---

## Overview

This lab gives you hands-on practice with both use case modeling and user story writing — the two most common functional requirements modeling techniques in professional practice. You will draw a use case diagram, write a complete use case specification, and write well-formed user stories with acceptance criteria. No software installation or terminal commands are required.

---

## Case Study: Pinecrest Bank — Mobile Banking Application

Pinecrest Bank is building a new mobile banking application. A BA has completed requirements elicitation and identified the following information about what the application must support:

- Customers can log in using a username and password. If the password is entered incorrectly three times in a row, the account is locked.
- Customers can view their checking and savings account balances and transaction history.
- Customers can transfer funds between their own Pinecrest accounts.
- Customers can pay bills by setting up payees and scheduling one-time or recurring payments. Before a bill payment can be scheduled, the system must verify that the customer has sufficient funds.
- Customers can deposit checks by photographing both sides of the check. The system must validate the check image quality before submitting the deposit. If image quality fails, the customer is prompted to retake the photo.
- Customer service representatives can view customer account information but cannot initiate transactions.
- The mobile app must connect to the Core Banking System (an existing separate system) to retrieve account data and post transactions.

---

## Part 1: Use Case Diagram (40 points)

### Part 1 Instructions

Draw a use case diagram for the Pinecrest Mobile Banking Application based on the case study above.

Your diagram must include:

- A system boundary rectangle labeled "Pinecrest Mobile Banking App"
- All actors identified from the case study (minimum 3, including at least one non-human actor)
- At least seven use cases derived from the case study
- Associations between each actor and the use cases they participate in
- At least one include relationship with correct notation and label
- At least one extend relationship with correct notation, label, and condition note

You may draw by hand and photograph, use any diagramming tool (Lucidchart, Draw.io, PowerPoint SmartArt), or any other legible format.

### Grading Rubric — Part 1

| Criterion | Points |
|---|---|
| System boundary present and labeled | 3 |
| All actors correctly identified and labeled (3 pts each, minimum 3) | 9 |
| At least 7 use cases with descriptive verb-noun names (2 pts each) | 14 |
| Correct associations between actors and use cases | 6 |
| At least one correctly drawn include relationship with label | 4 |
| At least one correctly drawn extend relationship with label and condition note | 4 |

Part 1 Total: 40 points

---

## Part 2: Use Case Specification (35 points)

### Part 2 Instructions

Write a complete use case specification for the "Deposit Check" use case from the Pinecrest Mobile Banking Application.

Your specification must include all of the following sections:

- Use Case Name
- Use Case ID
- Primary Actor
- Secondary Actors (if any)
- Preconditions (at least 2)
- Main Success Scenario (at least 6 numbered steps, alternating actor and system actions)
- Alternate Flow (at least 1, clearly numbered and referenced to the main scenario step where it branches)
- Exception Flow (at least 1, covering the image quality failure described in the case study)
- Postconditions (at least 2)

### Grading Rubric — Part 2

| Criterion | Points |
|---|---|
| All sections present and labeled | 5 |
| Preconditions are specific and relevant | 4 |
| Main success scenario has at least 6 steps with correct actor/system alternation | 10 |
| Alternate flow is clearly branched from a specific main scenario step | 6 |
| Exception flow covers the image quality failure from the case study | 6 |
| Postconditions are specific and reflect the completed transaction | 4 |

Part 2 Total: 35 points

---

## Part 3: User Stories with Acceptance Criteria (25 points)

### Part 3 Instructions

Write three user stories for the Pinecrest Mobile Banking Application based on the case study. Each story must use the standard format: "As a [role], I want [goal] so that [value]."

For each user story, write two acceptance criteria in Given/When/Then format.

Your three stories must cover three different features from the case study (do not write three stories about the same feature).

After writing your three stories, answer this question in 3–5 sentences: One of the case study features — "Customers can pay bills by setting up payees and scheduling one-time or recurring payments" — is likely an epic rather than a single user story. Explain why, and describe how you would split it into at least two sprint-sized stories.

### Grading Rubric — Part 3

| Criterion | Points |
|---|---|
| Three stories in correct "As a / I want / so that" format (3 pts each) | 9 |
| Each story covers a different feature from the case study | 3 |
| Two acceptance criteria per story in Given/When/Then format (1 pt each x 6) | 6 |
| Epic analysis: correctly identifies why bill pay is an epic and provides 2+ valid split stories | 7 |

Part 3 Total: 25 points

---

## Submission Instructions

Combine all three parts into one document with clearly labeled sections. Submit to the Canvas Module 05 Lab assignment by the due date shown in the course calendar.

---

## Part 9 — Challenge Exercise

This section is optional and not separately graded. It extends the lab into advanced use case and user story practice aligned with ECBA exam competencies.

### Challenge Step 1: Exception Flow Documentation

Return to the use case specification you wrote in Part 2 for the Pinecrest Bank mobile banking system. Add at least two exception flows for error or failure conditions the main success scenario does not cover. For each exception flow, document: the condition that triggers it, the system's response, whether the use case ends or resumes at a specific step, and the postcondition after the exception. Examples of exception conditions to consider: authentication failure after three attempts, insufficient funds when a transfer is submitted, or network timeout during transaction processing. This exercise practices the complete Cockburn use case specification format.

### Challenge Step 2: Use Case to User Story Decomposition

Select one use case from your diagram in Part 1. Decompose it into a minimum of four sprint-sized user stories that together cover the full behavior of the use case. For each story: write the three-part user story format, assign a MoSCoW priority, write two Given/When/Then acceptance criteria, and estimate relative complexity using T-shirt sizes (S/M/L/XL). Present your decomposition as a structured backlog table. This exercise practices the KA 5 technique of breaking high-level requirements into sprint-deliverable increments.

### Challenge Step 3: Alternate Actor Analysis

Review your use case diagram from Part 1. For each use case, identify whether there could be any secondary actors (external systems, timer-triggered processes, or supporting roles) that are missing from your diagram. Add at least two secondary actors to the diagram if applicable, or justify in writing why no secondary actors are needed for each use case. Then write one paragraph explaining how identifying secondary actors in the use case diagram reduces the risk of integration requirements being missed during the design phase. This exercise connects use case modeling directly to the stakeholder identification work from Module 02.

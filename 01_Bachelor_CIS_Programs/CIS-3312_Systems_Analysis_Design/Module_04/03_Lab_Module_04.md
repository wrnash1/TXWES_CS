# Lab Activity: Module 04 - Requirements Analysis and Documentation

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University
**Total Points:** 100

---

## Overview

This lab develops your ability to classify, write, verify, and trace requirements — the core analytical skills of business analysis. You will work with a provided elicitation transcript, classify requirements by type, evaluate quality problems in poorly written requirements, rewrite them to meet quality standards, and build a partial Requirements Traceability Matrix. No software installation or terminal commands are required.

---

## Case Study: Valley Ridge Credit Union — Online Loan Application System

Valley Ridge Credit Union (VRCU) is building a new online loan application system to replace a paper-based process. A BA has conducted stakeholder interviews and produced the following raw elicitation notes from three sessions.

### Elicitation Notes

From interview with the Loan Processing Manager:

- Loan officers need to see the full application history of any member before making a decision.
- Applications should not be lost or corrupted — the system needs to be reliable.
- All loan applications exceeding $25,000 require review by the Credit Committee before approval. This has been VRCU policy for 12 years.
- The system should send the applicant an email when their application status changes.
- Currently, paper applications take 3–5 business days to reach the loan officer's desk; the new system should dramatically reduce this.

From interview with the IT Security Officer:

- All member data must be encrypted. We follow NIST standards.
- The system must log every access to a member record, including who accessed it and when.
- Passwords must be at least 12 characters and include at least one number and one special character.
- The old system had no audit trail — that was a compliance failure.

From interview with the VP of Lending:

- We want the application form to be simple and easy for members to use on their phones.
- The system needs to handle a surge of applications at month-end when rates change — sometimes 3x normal volume.
- Before the new system can go live, we need to migrate all 8,400 paper applications from the last two years into the digital system.

---

## Part 1: Requirements Classification (30 points)

### Instructions

Read all elicitation notes above. Identify 12 distinct requirements or business rules embedded in the notes. For each one, classify it as one of the following:

- Functional Requirement (FR)
- Non-Functional Requirement (NFR)
- Business Rule (BR)
- Transition Requirement (TR)

Present your work as a table with three columns: Requirement Statement (your clean restatement), Classification, and a one-sentence justification.

### Grading Rubric — Part 1

| Criterion | Points |
|---|---|
| 12 requirements/rules identified (1 pt each) | 12 |
| Correct classification for each (1 pt each) | 12 |
| Justification is accurate and uses correct terminology (0.5 pts each) | 6 |

Part 1 Total: 30 points

---

## Part 2: Requirements Quality Improvement (40 points)

### Part 2 Instructions

The following five requirements were drafted by a junior BA based on the elicitation notes. Each one has at least one quality problem. For each requirement:

- Identify the quality problem (what criterion does it violate and why?)
- Rewrite the requirement to correct the problem

Use the format: "The system shall..." for all rewritten requirements.

### Draft Requirements to Improve

Requirement A: "The system shall provide a good experience for loan applicants using mobile devices."

Requirement B: "The system shall be secure."

Requirement C: "The system shall send emails and also display the application history and process applications fast."

Requirement D: "The system shall be reliable and not lose data."

Requirement E: "The system shall handle large volumes of applications."

### Grading Rubric — Part 2

| Criterion | Points |
|---|---|
| Quality problem correctly identified with criterion named (4 pts each x 5) | 20 |
| Rewritten requirement is specific, measurable, and testable (4 pts each x 5) | 20 |

Part 2 Total: 40 points

---

## Part 3: Requirements Traceability Matrix (30 points)

### Part 3 Instructions

Build a Requirements Traceability Matrix for six of the requirements you identified in Part 1. Your RTM must include the following columns:

- Requirement ID (assign your own, e.g., FR-001, NFR-002)
- Requirement Description (clean, well-formed statement)
- Source (which stakeholder or business policy originated this requirement)
- Design Component (name a logical system component that would implement it — you are not designing the system, just identifying the logical component, such as "Application Submission Module" or "Audit Logging Service")
- Test Case Description (one sentence describing how this requirement would be verified during testing)
- Status (set all to "Not Started" — you are building the initial RTM before development)

Your RTM must include at least two functional requirements, one non-functional requirement, and one business rule.

### Grading Rubric — Part 3

| Criterion | Points |
|---|---|
| All six rows present with all six columns populated | 6 |
| Requirement IDs are unique and follow a consistent naming scheme | 2 |
| Source correctly identifies the originating stakeholder or policy | 6 |
| Design component is logical and consistent with the requirement type | 6 |
| Test case description is specific and verifiable (not "test the feature") | 10 |

Part 3 Total: 30 points

---

## Submission Instructions

Combine all three parts into one document with clearly labeled sections. Submit to the Canvas Module 04 Lab assignment by the due date shown in the course calendar.

---

## Part 9 — Challenge Exercise

This section is optional and not separately graded. It extends the lab into advanced requirements analysis practice aligned with ECBA exam competencies.

### Challenge Step 1: Full Requirements Specification Section

Using the Valley Ridge Credit Union case study, write a complete formal requirements specification section covering the Loan Application Submission function. Your section must include:

- One business requirement (the organizational goal this function supports)
- Three functional requirements (specific system behaviors, numbered FR-001 through FR-003)
- Two non-functional requirements — one performance, one security (numbered NFR-001, NFR-002)
- One business rule that constrains the loan application process
- One transition requirement if applicable

Format each requirement using: ID, Priority (MoSCoW), Statement, and Rationale. Ensure every requirement passes all eight BABOK quality criteria. This exercise produces a fragment of a real Software Requirements Specification (SRS) and mirrors the KA 5 "Specify and Model Requirements" task.

### Challenge Step 2: Requirements Impact Analysis

Choose any one of the improved requirements you wrote in Part 2 of the lab. Assume that after baseline approval, the credit union's compliance team requests a change: the loan application must now also capture the applicant's employer name and employment duration. Perform a formal requirements impact analysis covering:

- Which other requirements in the Part 2 set might be affected by this addition
- What new test cases would need to be written
- Whether any UI screen layouts or database fields described in requirements would change
- What the risk is if this change is accepted without governance review

Present your analysis as a one-page structured memo addressed to the project sponsor. This exercise practices BABOK KA 6 Requirements Life Cycle Management impact assessment.

### Challenge Step 3: Acceptance Criteria Writing Workshop

For each of the following three requirements, write two specific, measurable acceptance criteria that a QA analyst could use to write a definitive pass/fail test case:

1. "The system shall send a loan decision notification to the applicant."
2. "The system shall prevent submission of incomplete loan applications."
3. "The system shall maintain application response time under peak load."

Each acceptance criterion should follow the Given-When-Then format (e.g., "Given a submitted application where all required fields are populated, When the underwriting engine completes review, Then the system shall send an email notification to the applicant's registered email address within 60 seconds"). This exercise develops the BABOK skill of translating abstract requirements into testable acceptance criteria.

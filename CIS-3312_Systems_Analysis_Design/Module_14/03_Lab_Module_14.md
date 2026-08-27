# Lab Activity: Module 14 — Testing, Validation, and Quality Assurance

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Lab Overview

In this lab you will build the core testing artifacts a business analyst produces during the quality assurance phase. Using a provided set of requirements for a fictional system, you will construct a Requirements Traceability Matrix, write a set of test cases, plan a UAT session, and triage a set of defects. These are the hands-on skills that ECBA candidates are expected to demonstrate.

**Estimated time:** 75–90 minutes

**Deliverable:** Submit as a single PDF or Word document with all parts clearly labeled.

---

## Scenario Background

Frontier Financial Services has completed development of a new online loan application system. The system allows customers to apply for personal loans, upload supporting documents, receive an automated credit decision, and electronically sign loan agreements. The development team has completed system testing. You are the BA leading the UAT phase.

The following approved requirements are in scope for this lab.

- FR-001: The system shall allow authenticated users to initiate a new loan application.
- FR-002: The system shall require applicants to provide income, employment status, and requested loan amount.
- FR-003: The system shall validate that the requested loan amount is between $1,000 and $50,000.
- FR-004: The system shall allow applicants to upload supporting documents in PDF or JPEG format, maximum 10 MB per file.
- FR-005: The system shall generate an automated credit decision (Approved, Conditionally Approved, or Declined) within 60 seconds of application submission.
- FR-006: The system shall send an email notification to the applicant within 5 minutes of a credit decision being generated.
- FR-007: Approved applicants shall be able to electronically sign the loan agreement within the portal.
- NFR-001: The application submission page shall load within 3 seconds under a concurrent load of 200 users.
- NFR-002: The system shall be accessible per WCAG 2.1 Level AA standards.
- BR-001: Applications with a requested amount greater than $25,000 shall require manual underwriter review regardless of automated credit score.

---

## Part 1 — Requirements Traceability Matrix (25 points)

### Part 1A — Build the RTM

Construct an RTM for all ten requirements listed above. Your RTM must include the following columns:

- Requirement ID
- Requirement Type (Functional / Non-Functional / Business Rule)
- Requirement Description (brief)
- Priority (assign High, Medium, or Low based on your judgment — justify at least three of your priority assignments in a note below the table)
- Test Case ID(s) — use placeholders (TC-001, TC-002, etc.) that you will complete in Part 2
- Test Status — set all to "Not Tested" initially

### Part 1B — Traceability Justification

For requirements FR-003 and BR-001, write one paragraph each explaining why these requirements require more than one test case to achieve adequate coverage. Identify the specific test types (functional, negative, boundary) that should be applied and explain why.

---

## Part 2 — Test Case Development (35 points)

Write complete test cases for the following five requirements. Each test case must include all required components: Test Case ID, Requirement Reference, Test Objective, Test Type, Preconditions, Test Data, Test Steps (numbered), Expected Result, and space for Actual Result and Pass/Fail.

### Test Case 1 — FR-003 Positive Boundary

Write a test case verifying that the minimum valid loan amount ($1,000) is accepted by the system.

### Test Case 2 — FR-003 Negative Boundary

Write a test case verifying that an amount below the minimum ($999) is rejected with an appropriate error message.

### Test Case 3 — FR-004 Invalid File Type

Write a test case verifying that uploading a file in an unsupported format (e.g., .docx) is rejected with a clear error message.

### Test Case 4 — FR-005 Decision Timing

Write a test case verifying that the automated credit decision is generated within 60 seconds of application submission.

### Test Case 5 — BR-001 Manual Review Routing

Write a test case verifying that a loan application for $26,000 is routed for manual underwriter review regardless of the automated credit decision outcome.

### Part 2A — Coverage Assessment

After writing your five test cases, return to your RTM and fill in the Test Case ID column for the requirements your test cases cover. Identify any requirements that currently have no test case assigned. For each uncovered requirement, write one sentence describing the test case that should be written.

---

## Part 3 — UAT Planning (25 points)

### Part 3A — Entry Criteria

Define five entry criteria that must be satisfied before UAT begins for the Frontier Financial Services loan application system. For each criterion, write one sentence explaining why it matters.

### Part 3B — UAT Scenario Development

Write two UAT test scenarios. Remember: UAT scenarios are business-language end-to-end workflows, not technical test steps.

Scenario 1 must cover the complete happy path: a qualified applicant applies for a loan, receives an approval decision, and signs the loan agreement.

Scenario 2 must cover a business exception: an applicant applies for $30,000 and must wait for manual underwriter review.

For each scenario, include:

- Scenario title
- Business purpose (one sentence)
- Participant role (who performs this scenario)
- Scenario narrative (three to five sentences describing what the participant does)
- What the scenario is designed to validate (two to three bullet points)

### Part 3C — Exit Criteria

Define four exit criteria for UAT. At least one must address defect thresholds by severity. At least one must address stakeholder sign-off. Write each criterion as a specific, measurable condition.

### Part 3D — Participant Selection

From the following list of available participants, select five for the UAT session. Justify each selection and explain why the excluded participants were not chosen.

Available participants:

- Three loan processors who process applications daily
- Two underwriters who handle manual reviews
- The VP of Lending (executive sponsor)
- Two IT developers who built the system
- Three customers from a pilot group who applied for loans in beta testing
- The compliance officer
- A QA analyst from the development team

---

## Part 4 — Defect Triage (15 points)

The following defects were logged during UAT. For each defect, assign a severity (Critical, High, Medium, Low), assign a priority (High, Medium, Low), recommend a disposition (Fix Before Go-Live, Defer to Next Release, Reject — Not a Defect), and write a one-sentence justification.

### Defect DEF-001

Description: When a user uploads a valid PDF document, the system displays the error message "Unsupported file type" and rejects the upload. Reproducible 100% of the time.

Requirement reference: FR-004

### Defect DEF-002

Description: The email notification is sent within 5 minutes as required, but the subject line reads "Loan Application Update" instead of "Your Loan Application Decision — [Applicant Name]" as specified in the UI requirements document.

Requirement reference: FR-006

### Defect DEF-003

Description: The application submission page loads in 3.8 seconds under a simulated load of 200 concurrent users. The requirement specifies 3.0 seconds.

Requirement reference: NFR-001

### Defect DEF-004

Description: The loan agreement PDF does not display correctly on iOS Safari mobile browsers. The signature field is cut off. The system works correctly on all desktop browsers and Android mobile browsers.

Requirement reference: FR-007

### Defect DEF-005

Description: The system correctly routes a $26,000 application to manual underwriter review. However, the underwriter dashboard does not display the applicant's income information, which the underwriters need to make their decision.

Requirement reference: BR-001 (adjacent gap — no specific requirement covers underwriter dashboard content)

---

## Submission Checklist

Before submitting, confirm your document includes:

- Part 1: RTM table for all ten requirements, priority justifications, traceability analysis for FR-003 and BR-001
- Part 2: Five complete test cases, coverage assessment with RTM updates and gap identification
- Part 3: Five entry criteria, two UAT scenarios, four exit criteria, participant selection with justification
- Part 4: Triage decisions for all five defects with severity, priority, disposition, and justification

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — Requirements Traceability Matrix | 25 |
| Part 2 — Test Case Development | 35 |
| Part 3 — UAT Planning | 25 |
| Part 4 — Defect Triage | 15 |
| **Total** | **100** |

---

---

## Part 9 — Challenge Exercise

This section is optional and not separately graded. It extends the lab into advanced
testing and quality assurance practice aligned with ECBA exam competencies.

### Challenge Step 1: Full Test Suite Coverage Analysis

Extend your RTM from Part 1 to include all remaining requirements that currently lack
test cases. For each of the five requirements without coverage (FR-001, FR-002, FR-006,
FR-007, and NFR-002), write one complete test case using the same format as Part 2.
Then produce a coverage summary table showing: total requirements, total test cases,
average test cases per requirement, requirements with only one test case (single-point
coverage risk), and requirements with negative or boundary test cases. Write a one-
paragraph coverage assessment explaining whether the test suite is adequate for a
financial services application subject to regulatory oversight, and identify any
requirement that you believe needs additional test cases beyond what you have written.

### Challenge Step 2: Defect Root Cause Analysis

For each of the five defects in Part 4, write a root cause analysis using the 5 Whys
technique. Starting with the defect symptom, ask "Why?" five times to trace the defect
back to its root cause in the requirements, design, development, or testing process.
Then classify each root cause into one of four categories: Requirements Gap (the
requirement was missing or ambiguous), Design Defect (the requirement was present but
the design did not implement it correctly), Development Error (the design was correct
but the code was wrong), or Testing Gap (the defect existed earlier but was not caught
by prior testing phases). After completing all five analyses, write a one-paragraph
lessons-learned statement identifying the most common root cause category across the
five defects and recommending one process improvement the Frontier Financial Services
project team should implement before the next system release.

### Challenge Step 3: Regulated Environment RTM Extension

The Frontier Financial Services loan application system is subject to the Consumer
Financial Protection Bureau's (CFPB) fair lending regulations, which require that
automated credit decisions be auditable and non-discriminatory. Extend the RTM with
three new compliance requirements of your own design that address: (1) auditability of
automated credit decisions, (2) equal treatment of applicants regardless of protected
characteristics, and (3) retention of application data for regulatory examination.
For each new requirement, write a complete test case that a compliance auditor could
execute. Then write a one-paragraph explanation of how the RTM functions as a compliance
artifact in regulated industries — specifically, what an auditor would look for in the
RTM and why an incomplete or stale RTM creates organizational risk beyond the project
itself. Reference the FDA regulated software environment context from Section 2.4 of
the reading guide as a parallel example.

---

*Module 14 Lab | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

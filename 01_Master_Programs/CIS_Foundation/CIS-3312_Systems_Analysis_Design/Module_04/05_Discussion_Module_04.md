# Discussion Forum: Module 04 - Requirements Analysis and Documentation

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Instructions

Read all three scenarios below and choose ONE to respond to. Your initial post must address all three sub-questions for your chosen scenario.

Initial Post: Due Wednesday at 11:59 PM (175–225 words)

Peer Responses: Due Sunday at 11:59 PM (reply to at least two classmates who chose different scenarios; minimum 75 words each)

---

## Scenario A: The Untestable Specification

A BA at a healthcare startup has delivered a 60-page Software Requirements Specification to the development team. The development manager reviews it and flags 18 requirements as untestable, including: "The system shall protect patient data," "The portal shall be intuitive for elderly users," "Reports shall be generated quickly," and "The system shall scale to meet future needs." The BA argues that these are important requirements and should not be removed. The development manager agrees they are important — but insists they cannot be built to an unspecified standard.

Sub-questions:

1. Select any two of the four flagged requirements above and rewrite each one to be specific, measurable, and testable. Explain what information you would need from stakeholders to complete each rewrite.
2. Describe the difference between requirements verification and requirements validation, and explain which activity would have caught these untestable requirements before they reached the development team.
3. Evaluate the BA's position that these requirements are important and should not be removed. Is the BA wrong? Explain how a BA can honor the legitimate business need behind a vague requirement while also ensuring the written requirement meets quality standards.

---

## Scenario B: Classification Confusion

A government agency is building a new grants management system. The BA has produced the following list of requirements and asked you to review them:

- "The system shall allow grants administrators to review and approve grant applications."
- "All grant awards over $500,000 require certification by the agency's Inspector General office — this is a federal regulation."
- "All historical grant records from the last seven years must be imported from the legacy system before the new system goes live."
- "The system shall process grant disbursement calculations within 4 seconds."
- "The new system must enable the agency to process 25% more grant applications per year than the current system."

Sub-questions:

1. Classify each of the five items above as a Functional Requirement, Non-Functional Requirement, Business Rule, Transition Requirement, or Business Requirement. Justify each classification in one sentence.
2. Explain why correctly classifying requirements by type matters — what specific problems arise when a team treats a business rule as a functional requirement, or a transition requirement as a permanent system capability?
3. The last item ("process 25% more grant applications per year") is written as a high-level goal. What BABOK requirement category does it belong in, and what additional requirements would need to be derived from it before the development team could act on it?

---

## Scenario C: The Missing Traceability

A software company completed a major CRM system upgrade six months ago. Post-deployment, the customer success team filed 34 defects. An internal audit discovered that 22 of the 34 defects traced back to requirements that existed in the original SRS but were never implemented — the development team had skipped them, apparently because there were no test cases linking back to those requirements. The audit also found that 8 requirements from the original SRS could not be traced to any stakeholder request in the project files.

Sub-questions:

1. Describe specifically how a maintained Requirements Traceability Matrix would have prevented the 22 un-implemented requirements from reaching production without detection.
2. The 8 requirements that could not be traced to any stakeholder request represent a different problem. What BABOK requirement quality criterion do they violate, and what does this suggest about the BA's elicitation or analysis process?
3. An RTM requires ongoing maintenance throughout the project life cycle — it is not a one-time deliverable. Describe at least two specific events during a project that should trigger an RTM update, and explain what information would need to be added or changed for each event.

---

## Discussion Rubric (10 Points Total)

### Initial Post (6 Points)

| Score | Criteria |
|---|---|
| 5–6 pts | Addresses all three sub-questions with specific evidence from the scenario. Uses correct BABOK KA 5 terminology. Meets the 175–225 word count. Writing is clear and professional. |
| 3–4 pts | Addresses most sub-questions but lacks specificity or misuses terminology. Slightly outside the word count. |
| 1–2 pts | Addresses only one sub-question or provides only vague, generic responses. |
| 0 pts | No initial post submitted by the deadline. |

### Peer Responses (4 Points)

| Score | Criteria |
|---|---|
| 4 pts | Responds to at least two classmates who chose different scenarios. Each reply is at least 75 words and adds substantive analysis. |
| 2 pts | Responds to only one classmate, or both responses are fewer than 75 words or superficial. |
| 0 pts | No peer responses submitted. |

---

## A Note from Professor Nash

Requirements documentation is the most underrated skill in software development. Developers and managers often want to skip it or rush through it, and projects that do so pay for it in rework, failed tests, and stakeholder dissatisfaction. The three scenarios this week all show what happens when requirements are vague, misclassified, or untraced — and none of it is hypothetical. These are the most common failure patterns in real projects. Learning to write a testable requirement and maintain a traceability matrix is not busywork — it is the difference between a project that delivers on its promise and one that does not.

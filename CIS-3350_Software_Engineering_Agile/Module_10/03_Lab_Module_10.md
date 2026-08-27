# Lab Activity: Module 10 – Requirements Engineering and Use Cases

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Points:** 100

---

## Overview

This lab is a requirements engineering and use case writing exercise. You will classify requirements, write a complete use case, and map requirements to a Product Backlog. No programming is required.

Estimated time: 90–120 minutes

---

## Part 1 — Requirements Classification (30 points)

### Part 1 Instructions

Read the following product description and complete the tasks below.

### Product Description — CampusAlert

CampusAlert is a mobile and web application for Texas Wesleyan University that sends emergency notifications and safety alerts to students, faculty, and staff. The product description from the university's IT committee reads:

"CampusAlert must allow administrators to compose and send emergency messages (text, push notification, and email) to all registered users within 60 seconds of initiating the send action. Users must be able to register their phone numbers and email addresses, set notification preferences (which channels they receive), and opt out of non-emergency communications. The system must maintain 99.9% uptime during business hours (8 AM–6 PM weekdays). All user data must be encrypted in transit and at rest. The mobile app must meet WCAG 2.1 Level AA accessibility standards. Administrators must be able to view message delivery receipts and see which users have not yet been reached."

Task A — Classify requirements (20 points): Identify at least eight distinct requirements from the product description. For each requirement:

- Write the requirement as a clear, testable statement
- Classify it as Functional (F) or Non-Functional (NFR)
- If it is an NFR, identify its quality attribute category (Performance, Security, Availability, Usability, Compliance)

Present your classifications in a table with columns: Requirement Statement, Type (F/NFR), Category (NFR only).

Task B — Definition of Done (10 points): Review your classified requirements. Identify which requirements should be incorporated into the team's Definition of Done rather than as individual Product Backlog Items. For each DoD candidate:

- State the requirement
- Explain why it belongs in the DoD rather than a specific backlog item

---

### Part 1 Grading (30 points)

- Task A — Requirements classification (8+ requirements): 20 pts (accuracy of F/NFR classification 10, quality attribute identification for NFRs 5, clarity of statements 5)
- Task B — DoD identification with reasoning: 10 pts (correct DoD candidates 6, reasoning quality 4)

---

## Part 2 — Use Case Writing (40 points)

### Part 2 Instructions

Using the CampusAlert product description from Part 1, complete the two tasks below.

Task A — Write a complete use case (25 points): Select one functional requirement from your Part 1 classification and write a complete use case for it. Your use case must include all of the following components:

- Use case name
- Actor (who initiates the interaction)
- Preconditions (at least two)
- Main success scenario (at least six numbered steps)
- At least one alternative flow (labeled with the step it branches from)
- At least one exception flow (error or failure condition)
- Postconditions (at least two)

Task B — Use case vs. user story comparison (15 points): Convert the same behavior you documented in your use case into a user story with three acceptance criteria in Given/When/Then format. Then write a 100–150 word reflection addressing:

- What information is captured in the use case that is not in the user story?
- What does the user story capture better than the use case?
- In which contexts would each format be more appropriate for the CampusAlert team?

---

### Part 2 Grading (40 points)

- Task A — Use case completeness and quality: 25 pts (all required components present 15, step clarity and logical flow 6, alternative/exception flows realistic 4)
- Task B — User story conversion: 10 pts (correct format 4, acceptance criteria testable 6)
- Task B — Reflection: 5 pts (comparison depth 3, contextual recommendation 2)

---

## Part 3 — Product Backlog Mapping (30 points)

### Part 3 Instructions

Using your classified requirements from Part 1, complete the three tasks below.

Task A — Convert requirements to PBIs (15 points): Select five functional requirements from your Part 1 classification. For each one:

- Write it as a user story in "As a / I can / so that" format
- Write at least two acceptance criteria in Given/When/Then format
- Assign a rough size using T-shirt sizing (XS, S, M, L, XL) with a one-sentence justification

Task B — Order the backlog (10 points): Order your five user stories from highest to lowest priority. For each ordering decision, write one sentence explaining why the higher item takes precedence. Consider: user safety impact, dependency relationships, and value delivered.

Task C — Scrum vs. Traditional reflection (5 points): Write a 75–100 word paragraph responding to this prompt: A university stakeholder says, "I need all 50 requirements for CampusAlert documented and signed off before the development team writes a single line of code." Using Scrum principles, explain why this approach creates risk and describe the alternative Scrum approach to managing requirements.

---

### Part 3 Grading (30 points)

- Task A — Five user stories with acceptance criteria and sizing: 15 pts (story format 5, AC testability 6, sizing justification 4)
- Task B — Ordered backlog with reasoning: 10 pts (reasoning quality 6, logical ordering 4)
- Task C — Stakeholder reflection: 5 pts

---

## Deliverables

Submit a single document (PDF or Word) containing:

1. Part 1: Requirements classification table and Definition of Done candidates
2. Part 2: Complete use case, user story conversion, and reflection
3. Part 3: Five user stories with acceptance criteria, ordered backlog, and stakeholder reflection

Submit to the Canvas assignment portal by the module due date.

---

## Part 9 — Challenge Exercise

### Challenge 1: Use Case to Automated Test Specification

The use case you wrote in Part 2 describes behavior in structured natural language. Convert it into a test specification that a QA engineer could execute:

1. For the main success scenario: write one end-to-end test case with preconditions, test steps, and expected result for each step, and a pass/fail criterion.
2. For each alternative flow you documented: write one test case that exercises that path, including the specific condition that triggers it and the expected system response.
3. For the exception flow: write one negative test case that verifies the system handles the error condition gracefully (error message shown, no data corrupted, system remains usable).
4. Identify any acceptance criteria from your Part 3 user stories that are not covered by these test cases and write one additional test case to fill each gap.

### Challenge 2: Requirements Triage Under Uncertainty

The CampusAlert product team has just received a revised list of 30 requirements from the university IT committee. The Product Owner has 2 hours before Sprint 1 Planning and cannot refine all 30 items. Apply a structured triage approach:

1. Categorize the 8 requirements you identified in Part 1 into three tiers: Tier 1 (must be in the first 2 Sprints — user safety depends on it), Tier 2 (important within first 6 months), Tier 3 (nice-to-have, can wait). Justify each tier assignment in one sentence.
2. For Tier 1 requirements only: verify each one passes the INVEST criteria (specifically: Estimable and Testable) and flag any that need refinement before Sprint 1 Planning.
3. Write a two-paragraph recommendation to the Product Owner explaining which Tier 1 items should become Sprint 1 backlog items and why — considering dependencies, risk, and the university's primary use case (emergency notification delivery).
4. Identify one architectural decision the team will need to make in Sprint 1 that is implied by the NFRs (hint: 60-second delivery, 99.9% uptime, encryption) and describe how it affects Sprint 1 capacity planning.

### Reflection Questions

1. The Agile Manifesto values "working software over comprehensive documentation" — but in healthcare and aviation, comprehensive requirements documentation is legally required. How do high-performing Agile teams in regulated industries reconcile these two imperatives without abandoning either?
2. Requirements elicitation assumes that stakeholders know what they want. Research and describe one common cognitive bias (e.g., anchoring, availability bias, scope illusion) that causes stakeholders to provide inaccurate or incomplete requirements during elicitation interviews. Describe a specific technique a requirements analyst or Product Owner can use to counteract it.

---

## Rubric Summary

| Component | Points |
|---|---|
| Part 1 — Requirements Classification (Tasks A, B) | 30 |
| Part 2 — Use Case Writing (Tasks A, B) | 40 |
| Part 3 — Product Backlog Mapping (Tasks A, B, C) | 30 |
| Total | 100 |

---

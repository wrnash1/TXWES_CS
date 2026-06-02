# Reading Guide: Module 10 – Requirements Engineering and Use Cases

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

---

## Introduction

Requirements engineering is the process of discovering, analyzing, documenting, and managing what a software system must do and how well it must do it. This module examines the full requirements engineering discipline — from classical techniques (use cases, functional/non-functional specification) to the Scrum approach (Product Backlog as living requirements repository). Understanding both prepares you for PSM I exam questions about how Scrum handles requirements differently from traditional methods, and for professional environments where both approaches coexist.

---

## 1. Requirements Engineering Core Concepts

### What Requirements Engineering Does

Requirements engineering encompasses five activities that apply whether a team is using Waterfall or Agile:

| Activity | Description | Waterfall Application | Scrum Application |
|---|---|---|---|
| Elicitation | Discovering stakeholder needs | Workshops, interviews, observation before design | Ongoing — Sprint Reviews, refinement, user research |
| Analysis | Examining for conflicts, ambiguity, feasibility | Before specification document is written | Part of Product Backlog refinement |
| Specification | Documenting requirements in usable form | Formal SRS document | Product Backlog Items (user stories, use cases) |
| Validation | Confirming requirements match actual needs | Stakeholder sign-off on specification | Sprint Review feedback loop |
| Management | Tracking changes to requirements over time | Change control board | Product Owner maintains and reorders Product Backlog |

### Functional vs. Non-Functional Requirements

| Type | Definition | Examples | Scrum Home |
|---|---|---|---|
| Functional | What the system must do — specific behaviors triggered by inputs or conditions | User login, password reset, data export, report generation | Product Backlog Items (user stories) |
| Non-Functional (NFR) | How well the system must operate — quality attributes | Page load time < 2 seconds; 99.9% uptime; AES-256 encryption; WCAG 2.1 accessibility | Definition of Done (system-wide) or Product Backlog Items (significant development work) |

The key diagnostic question: can I describe the requirement as "the system shall do X when Y" (functional) or "the system shall operate with quality attribute Z" (non-functional)?

---

## 2. Use Cases

### Use Case Structure

A use case describes how a specific actor (human user or external system) interacts with the system to achieve a specific goal. Use cases are more formal than user stories and are common in regulated industries and enterprise environments.

| Component | Description | Example |
|---|---|---|
| Use case name | Brief goal statement | "Reset Password" |
| Actor | Who initiates the interaction | Registered User |
| Preconditions | What must be true before the use case begins | User has a registered account; user is on login page |
| Main success scenario | Numbered steps when everything goes right | 1. User clicks Forgot Password 2. System shows email form... |
| Alternative flows | Valid deviations from the main path | If email not recognized, show generic message |
| Exception flows | Error conditions the system must handle | If reset link expired, prompt user to request a new one |
| Postconditions | What is true after success | User password updated; user redirected to login |

### Use Case vs. User Story

| Dimension | Use Case | User Story |
|---|---|---|
| Format | Structured table with numbered steps | One sentence: As a / I can / so that |
| Detail level | High — all paths documented | Low — conversation starter |
| Primary purpose | Specification and testing | Dialogue and shared understanding |
| Acceptance criteria | Embedded in alternative/exception flows | Written separately (Given/When/Then) |
| Best fit | Regulated industries, detailed upfront spec needed | Agile teams, iterative discovery |
| Scrum compatibility | Both are valid PBI formats | Preferred Scrum format |

Both formats document the same underlying system behavior. Neither is prohibited in Scrum. Teams often use user stories for everyday features and use cases for complex, regulated, or safety-critical behaviors.

---

## 3. Requirements in Scrum

### The Product Backlog as Requirements Repository

The Scrum Guide does not use the phrase "requirements document." The Product Backlog is the Scrum team's complete, living, ordered list of what needs to be done on the product. It replaces the traditional requirements specification by distributing requirements discovery across the project rather than front-loading it.

Product Backlog characteristics that mirror good requirements practices:

- Emergent: new requirements are discovered and added as the team learns
- Ordered: the most valuable and best-understood items are at the top
- Transparent: visible to all stakeholders at all times
- Refined: items are analyzed and detailed before they enter a Sprint (equivalent to requirements analysis)

### Non-Functional Requirements in Scrum

| NFR Type | Where It Lives in Scrum | Rationale |
|---|---|---|
| System-wide quality standard (e.g., all pages < 2 seconds) | Definition of Done | Applies to every Increment — must be verified on every item |
| Specific infrastructure work (e.g., add TLS to legacy API) | Product Backlog Item | Requires dedicated development effort; should be planned and estimated |
| Regulatory compliance (e.g., HIPAA audit logging) | Definition of Done + possibly Product Backlog Items | Compliance applies to everything; remediation is specific work |

### Requirements Traceability in Scrum

Traditional requirements traceability links each requirement to its source and forward to its implementation and tests. Agile teams achieve traceability through:

- Acceptance criteria: each user story's Given/When/Then criteria are directly testable
- Definition of Done: quality standards verified on every story
- Backlog management tools: linking stories to test cases and sprint outcomes
- Sprint Reviews: stakeholders validate that implemented items match their needs

Formal traceability matrices are not prescribed in Scrum but are not prohibited. Teams in regulated industries (healthcare, finance, aerospace) often maintain them as required artifacts alongside their Scrum workflow.

---

## 4. Traditional vs. Agile Requirements: Key Differences

| Dimension | Traditional (Waterfall) | Scrum |
|---|---|---|
| When requirements are captured | Before development begins | Progressively throughout the project |
| Format | Formal specification document | Product Backlog Items (user stories, use cases) |
| Completeness assumption | Requirements can be fully known upfront | Requirements emerge; full specification upfront is waste |
| Change management | Change control board; changes are expensive | Product Backlog is always open; changes welcome |
| Stakeholder involvement | Heavy at the beginning, light during development | Continuous — Sprint Reviews, refinement sessions |
| Validation | Document sign-off before build | Working software demonstrated at Sprint Review |
| Non-functional requirements | Separate NFR section in specification | Definition of Done + select backlog items |

---

## 5. PSM I Exam Tips

Tip 1: The Product Backlog is Scrum's requirements document. Any question that asks where requirements "live" in Scrum points to the Product Backlog (and its commitment, the Product Goal, for strategic direction).

Tip 2: Non-functional requirements that apply system-wide belong in the Definition of Done. This is one of the most tested NFR concepts on PSM I — "where should performance standards be captured?" → Definition of Done.

Tip 3: The Product Backlog is never frozen. A common exam scenario presents a stakeholder who wants to sign off on a complete requirements list before Sprint 1. The correct Scrum response: the Product Backlog supports progressive elaboration and is always open to change.

Tip 4: The Scrum Guide does not specify the format of Product Backlog Items. User stories are common practice, not a Scrum rule. Use cases, job stories, or plain descriptions are all valid PBI formats.

Tip 5: Agile Manifesto Principle 2 — "Welcome changing requirements, even late in development. Agile processes harness change for the customer's competitive advantage." This principle directly contrasts with Waterfall requirements freezing.

Tip 6: Scrum does not define a requirements analyst role. The Product Owner is responsible for the Product Backlog, including eliciting and ordering requirements. Developers and stakeholders contribute knowledge during refinement.

Tip 7: Use cases and user stories document the same underlying behavior differently. Neither format is prohibited in Scrum. Teams choose the format that best serves their context.

Tip 8: Acceptance criteria (whether in Given/When/Then or use case format) serve as the bridge between requirements and testing — they make requirements testable and provide the basis for the Definition of Done verification.

---

## 6. Study Checklist

- [ ] Define requirements engineering and state its five core activities
- [ ] Distinguish functional from non-functional requirements and give two examples of each
- [ ] Write a complete use case with all required components for a common system behavior
- [ ] Explain how the Product Backlog replaces a traditional requirements specification in Scrum
- [ ] Describe two ways non-functional requirements are handled in Scrum
- [ ] Explain what requirements traceability is and how Agile teams achieve it without a formal matrix
- [ ] Complete this module's Lab and Quiz

---

# Video Script: Module 10 – Requirements Engineering and Use Cases

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Estimated Duration:** 20 minutes

**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Camera: Instructor on screen for introduction and transitions
- Slides: Title cards for each section heading
- [SHOW DIAGRAM] tags indicate cuts to prepared visual assets
- Use cases should be shown as structured tables alongside user story format comparisons

---

## Section 1 — Welcome and Why Requirements Matter [00:00–03:00]

"Welcome to Module 10. We are now going to shift our perspective slightly. For the past several modules we have been deep inside Scrum — Sprints, backlogs, events, artifacts. Today we are going to look at the broader discipline of requirements engineering: where software specifications come from, how they are captured in traditional and Agile contexts, and why understanding both approaches makes you a better practitioner.

Requirements engineering is one of those foundational software engineering skills that does not disappear when a team adopts Scrum. The questions are still the same: What does the system need to do? How well does it need to do it? How do we know when it is done? Scrum just answers these questions differently than Waterfall does.

By the end of this module you will be able to:

- Define requirements engineering and distinguish functional from non-functional requirements
- Write a complete use case with actor, preconditions, main success scenario, and alternative flows
- Explain how traditional requirements documentation compares to the Product Backlog in Scrum
- Describe how non-functional requirements are handled in a Scrum context
- Map stakeholder needs to Product Backlog Items and the Definition of Done"

---

## Section 2 — Requirements Engineering Fundamentals [03:00–08:00]

"Requirements engineering is the process of discovering, analyzing, documenting, and managing the needs and constraints that a software system must satisfy.

[SHOW DIAGRAM: Requirements engineering lifecycle — elicitation → analysis → specification → validation → management — shown as a continuous cycle]

It has five core activities. Elicitation is about discovering what stakeholders actually need — through interviews, workshops, observation, and prototyping. Analysis is examining the discovered needs for conflicts, ambiguities, and feasibility. Specification is writing them down in a form that developers and testers can use. Validation is confirming with stakeholders that the documented requirements match their actual needs. And management is tracking requirements as they change — because they always change.

Now, requirements come in two fundamental types. Functional requirements describe what the system must do — specific behaviors, functions, or services. 'The system must allow registered users to reset their password via email confirmation' is a functional requirement. It describes a behavior.

Non-functional requirements, or NFRs, describe how well the system must do what it does. They are constraints on quality attributes: performance, security, availability, usability, scalability. 'All pages must load within two seconds under normal load' is a non-functional requirement. 'User data must be encrypted at rest using AES-256' is a non-functional requirement.

[SHOW DIAGRAM: Two-column table — Functional Requirements (behaviors/functions, testable by input→output) vs. Non-Functional Requirements (quality attributes, testable by metrics/measurements)]

The distinction matters because functional and non-functional requirements are handled differently in both Waterfall and Agile contexts. In Waterfall, both are typically captured in a formal requirements specification document. In Scrum, functional requirements become Product Backlog Items — user stories — while non-functional requirements are often embedded in the Definition of Done.

PSM I Exam Tip: If a PSM I question asks where non-functional requirements like security or performance standards live in Scrum, the answer is often the Definition of Done — because they apply to every Increment, not just specific stories."

---

## Section 3 — Use Cases: The Traditional Requirements Tool [08:00–13:00]

"Before user stories became the dominant Agile requirements format, use cases were — and in many organizations still are — the primary way to document system behavior. Understanding use cases helps you work in environments that mix traditional and Agile practices, and it reinforces the underlying thinking about actors, goals, and flows that user stories simplify.

A use case documents how a specific actor — a user or external system — interacts with your system to achieve a specific goal. It includes:

- Actor: who or what initiates the interaction
- Preconditions: what must be true before the use case begins
- Main success scenario: the step-by-step sequence of actions when everything goes right
- Alternative flows: what happens when the main path is not followed
- Postconditions: what is true after the use case completes successfully

[SHOW DIAGRAM: Sample use case table — Use Case: User Resets Password — columns for Actor, Preconditions, Steps (numbered), Alternative Flows, Postconditions]

Let me walk through an example. Actor: registered user. Precondition: the user is on the login page and cannot remember their password. Main success scenario: Step 1 — user clicks 'Forgot Password'; Step 2 — system displays email input form; Step 3 — user enters registered email address; Step 4 — system sends password reset email; Step 5 — user clicks link in email; Step 6 — system displays password reset form; Step 7 — user enters and confirms new password; Step 8 — system validates and updates password; Step 9 — system confirms success and redirects to login. Alternative flow: at Step 3, if the email address is not registered, the system displays a generic message — 'If an account exists for this email, a reset link will be sent' — to prevent account enumeration.

[SHOW DIAGRAM: Side-by-side — the same scenario as a use case (structured table) vs. as a user story with acceptance criteria]

Now compare that to a user story: 'As a registered user who has forgotten my password, I can reset it via email so that I can regain access to my account.' The user story is lighter and conversation-starting. The use case is more formal and more complete. Neither is inherently better — the right format depends on the team, the context, and the regulatory environment.

PSM I Exam Tip: User stories are preferred in Agile because they emphasize dialogue and emergence. Use cases are preferred in regulated environments or when detailed system specification is required upfront. Scrum does not prohibit use cases — the Product Owner can use any format for Product Backlog Items."

---

## Section 4 — Requirements in Scrum: The Product Backlog Approach [13:00–17:30]

"So how does Scrum handle requirements? The answer is: through the Product Backlog.

[SHOW DIAGRAM: Traditional requirements flow (Requirements Spec → Design → Build → Test) vs. Scrum requirements flow (Product Backlog → Sprint → Increment → Feedback → Product Backlog refinement)]

In Scrum, the Product Backlog is the single source of truth for all known requirements. It is emergent — it grows and changes as the team and stakeholders learn more. It is ordered — more important items are at the top and are more detailed. And it is never complete — there is always more work to discover.

This is a fundamentally different philosophy from traditional requirements engineering. Waterfall assumes you can and should capture all requirements before building anything. Scrum assumes you cannot — that trying to do so wastes effort because requirements will change, and that the best way to discover real requirements is through building, demonstrating, and getting feedback.

The Product Goal gives the Product Backlog its strategic direction — it is the long-term objective the team is working toward. Individual Product Backlog Items are the requirements: user stories, features, bug fixes, technical improvements, and NFR work.

For non-functional requirements specifically, Scrum offers two homes. System-wide NFRs that apply to every Increment — security standards, performance baselines, accessibility requirements — belong in the Definition of Done. Every piece of work must meet them to be considered done. NFRs that require significant development work — like adding encryption to a system that currently has none — can also appear as Product Backlog Items.

PSM I Exam Tip: The Product Backlog replaces the requirements specification document in Scrum. The Scrum Guide does not describe a separate requirements document. A common exam trap presents a scenario where someone wants to freeze requirements before Sprint 1 — the correct Scrum response is that requirements are never frozen; the Product Backlog is always open to change."

---

## Section 5 — Requirements Traceability and Closing [17:30–20:00]

"One traditional requirements concept worth understanding even in Agile contexts is requirements traceability — the ability to trace each requirement from its source (a stakeholder need) forward to its implementation and test cases.

[SHOW DIAGRAM: Traceability matrix showing requirement → backlog item → sprint → test case → acceptance criteria]

In regulated industries — healthcare, finance, aerospace — traceability is often mandatory. Agile teams in these environments often maintain traceability through acceptance criteria (each user story's acceptance criteria link to test cases), Definition of Done (quality standards applied to every story), and backlog management tools that link items to test results.

Scrum does not prescribe a traceability matrix, but it does not prohibit one either. Teams that need formal traceability can build it into their workflow using well-written acceptance criteria and a test management system.

The key connection between traditional requirements engineering and Scrum is this: both are trying to answer the same question — what does the product need to do, and how will we know when it is done? Scrum just answers it incrementally and empirically rather than comprehensively and upfront.

PSM I Exam Tip: Agile Manifesto Principle 1 states that the highest priority is to satisfy the customer through early and continuous delivery of valuable software. This is the principle that drives the Product Backlog approach to requirements — deliver value early, discover more requirements through delivery, repeat.

In Module 11 we move to software design patterns — the recurring architectural solutions that experienced engineers apply to common problems. See you there."

---

## End Card

- Next module: Module 11 – Software Design Patterns
- Additional Resources (Scrum.org only):
  - Scrum Guide (free): scrum.org/resources/scrum-guide
  - PSM I exam details: scrum.org/professional-scrum-master-i-certification

---

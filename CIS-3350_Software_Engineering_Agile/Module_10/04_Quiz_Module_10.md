# Quiz: Module 10 – Requirements Engineering and Use Cases

**Course:** CIS-3350 Software Engineering and Agile

**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org

**Instructor:** Professor Nash | Texas Wesleyan University

**Total Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

In Scrum, what artifact serves as the primary repository for all known product requirements?

- A) The Requirements Specification Document maintained by a Business Analyst
- B) The Sprint Backlog, updated daily by the Developers
- C) The Product Backlog, owned and ordered by the Product Owner
- D) The Definition of Done, agreed upon by the Scrum Team before Sprint 1

Correct Answer: C — The Product Backlog is the single, emergent, ordered list of everything known to be needed in the product. It is the Scrum replacement for a traditional requirements specification document and is owned by the Product Owner.

Distractor Analysis:

- Why A is incorrect: Scrum does not define a Business Analyst role or a formal requirements specification document. These are traditional Waterfall artifacts.
- Why B is incorrect: The Sprint Backlog contains only the work selected for the current Sprint — it is a working plan for one Sprint, not a repository for all requirements.
- Why D is incorrect: The Definition of Done is a quality standard for the Increment. It may capture non-functional requirements but does not serve as a backlog of all product requirements.

---

## Question 2

Which of the following is the most accurate definition of a non-functional requirement?

- A) A requirement that describes a specific behavior the system must perform when triggered by a user action
- B) A constraint on the system's quality attributes — such as performance, security, scalability, or availability — rather than its specific behaviors
- C) A requirement that has been deprioritized in the Product Backlog and is not planned for near-term implementation
- D) A feature that the development team has decided not to build because it is too technically complex

Correct Answer: B — Non-functional requirements define how well the system must operate — response times, uptime targets, encryption standards, load capacity — as opposed to what the system does. They constrain the system's quality attributes.

Distractor Analysis:

- Why A is incorrect: This describes a functional requirement — a specific system behavior triggered by user or system input.
- Why C is incorrect: A deprioritized backlog item is simply lower in ordering — its priority position does not make it non-functional.
- Why D is incorrect: A deferred technically complex feature is a prioritization decision, not a category of requirement type.

---

## Question 3

A use case for a banking app includes a main success scenario where a user transfers funds successfully, and an alternative flow where the transfer fails because the account has insufficient funds. What does the alternative flow represent?

- A) A defect in the system that must be fixed before the use case is complete
- B) A separate use case that must be documented independently in the Product Backlog
- C) A valid deviation from the main success scenario that the system must handle gracefully
- D) An out-of-scope feature that should be removed from the specification

Correct Answer: C — Alternative flows in use cases describe valid paths a user may take that deviate from the main success scenario. The system must handle these gracefully — they are designed behaviors, not errors.

Distractor Analysis:

- Why A is incorrect: An alternative flow is a designed system behavior, not a defect. Insufficient funds handling is a required feature, not a bug.
- Why B is incorrect: While insufficient funds handling could be modeled as a separate use case, documenting it as an alternative flow within the transfer use case is a valid and common approach.
- Why D is incorrect: A real user scenario like insufficient funds is definitively in scope. Removing it would create an incomplete specification.

---

## Question 4

A stakeholder requests that all 100 system requirements be fully documented and approved before Sprint 1 begins. How should the Scrum Team respond?

- A) Agree to the request, because the Product Owner needs a complete specification to order the Product Backlog
- B) Agree, but limit upfront documentation to functional requirements only — non-functional requirements can be addressed later
- C) Explain that the Product Backlog supports progressive elaboration — requirements emerge and are refined throughout the project, not specified completely upfront
- D) Abandon the Scrum framework and return to Waterfall, since the stakeholder prefers traditional requirements management

Correct Answer: C — Scrum's empirical approach means requirements are discovered and refined iteratively. The Product Backlog starts with known items and evolves as the team and stakeholders learn. Freezing all requirements upfront is a Waterfall practice that removes Scrum's adaptability.

Distractor Analysis:

- Why A is incorrect: The Product Owner needs an ordered, sufficiently detailed set of near-term backlog items — not a frozen complete specification. Complete upfront specification is a Waterfall artifact.
- Why B is incorrect: Splitting into "functional now / NFR later" still imposes a large upfront effort that delays value delivery and locks in decisions made with incomplete information.
- Why D is incorrect: This is an overreaction. The Scrum Master should educate the stakeholder on how Scrum handles requirements progressively, not abandon the framework.

---

## Question 5

Where are non-functional requirements such as "all API responses must return within 500 milliseconds" most commonly captured in Scrum?

- A) In a separate Non-Functional Requirements Document maintained alongside the Product Backlog
- B) As tasks assigned to the Scrum Master in the Sprint Backlog
- C) In the Definition of Done, ensuring every Increment meets the performance standard as a quality baseline
- D) In the Sprint Goal, communicated by the Product Owner at each Sprint Planning

Correct Answer: C — System-wide NFRs that apply to every Increment are best captured in the Definition of Done so they are verified for every piece of delivered work, not selectively applied. This ensures consistent quality across all increments.

Distractor Analysis:

- Why A is incorrect: Creating a separate NFR document outside Scrum artifacts is a Waterfall practice. Scrum centralizes quality standards in the Definition of Done.
- Why B is incorrect: The Scrum Master does not own backlog tasks or technical standards. NFRs belong to the Developers (via DoD) and Product Owner (via backlog items for significant NFR work).
- Why D is incorrect: The Sprint Goal is a specific short-term objective — not an appropriate place for standing quality standards that apply to all Sprints.

---

## Question 6

What is requirements traceability, and how is it most commonly achieved in Agile development?

- A) Traceability is the practice of estimating requirements in story points; it is achieved through Planning Poker
- B) Traceability links each requirement to its source and forward to implementation and tests; in Agile it is achieved through testable acceptance criteria and backlog management
- C) Traceability means all requirements are approved by stakeholders before coding begins; in Agile this happens at Sprint Review
- D) Traceability is a Waterfall-only concept with no equivalent in Scrum or Agile

Correct Answer: B — Requirements traceability links a requirement from its stakeholder source forward to its implementation in code and its associated tests. Agile teams achieve this through well-written acceptance criteria (which are directly testable), the Definition of Done (applied to every story), and backlog management tools that link stories to tests and Sprint outcomes.

Distractor Analysis:

- Why A is incorrect: Story point estimation has nothing to do with traceability. Traceability is about linking requirements to their origins and implementations, not sizing work.
- Why C is incorrect: Pre-Sprint stakeholder approval is a Waterfall requirement sign-off practice. Sprint Reviews provide retrospective validation, not upfront approval.
- Why D is incorrect: Traceability is relevant in Agile, especially in regulated industries. Agile simply achieves it through different mechanisms than a formal traceability matrix.

---

## Question 7

Which of the following best describes the key difference between a user story and a use case?

- A) User stories are written by developers; use cases are written by business analysts
- B) User stories are conversation starters that emphasize dialogue and emergence; use cases are formal, structured specifications documenting all paths through a system behavior
- C) User stories document system behavior in numbered steps; use cases use the As a / I can / so that format
- D) User stories are prohibited in regulated industries; use cases are prohibited in Agile environments

Correct Answer: B — User stories are intentionally lightweight to prompt conversation and allow requirements to emerge. Use cases are more formal, documenting actors, preconditions, main success scenarios, alternative flows, and postconditions. Both formats document the same underlying behavior but serve different contexts.

Distractor Analysis:

- Why A is incorrect: There is no rule about who writes which format. Product Owners, Business Analysts, and even Developers can write either user stories or use cases depending on team practice.
- Why C is incorrect: This reverses the formats. User stories use the "As a / I can / so that" format; use cases use numbered steps for the main success scenario.
- Why D is incorrect: Both formats are used in both regulated and Agile environments. The choice depends on team context and the level of specification detail needed, not a prohibition.

---

## Question 8

Which component of a use case describes what must be true before the interaction begins?

- A) Postconditions
- B) Alternative flows
- C) Preconditions
- D) Exception flows

Correct Answer: C — Preconditions state what must already be true before a use case can begin executing. For example, "user must be logged in" or "user must have items in their cart" are preconditions for a checkout use case.

Distractor Analysis:

- Why A is incorrect: Postconditions describe what is true after the use case completes successfully — the opposite of preconditions.
- Why B is incorrect: Alternative flows describe valid deviations from the main success scenario during the interaction — not the starting conditions.
- Why D is incorrect: Exception flows describe error conditions that may occur during the interaction — not the state required before the interaction starts.

---

## Question 9

Agile Manifesto Principle 2 states that Agile processes "welcome changing requirements, even late in development." How does this principle manifest in Scrum's approach to the Product Backlog?

- A) The Product Backlog is locked after Sprint 1 to prevent scope changes from disrupting the team
- B) The Product Owner can add, modify, or reorder Product Backlog Items at any time, even after Sprints have begun
- C) Developers can add requirements to the Product Backlog during a Sprint without Product Owner approval
- D) The Sprint Backlog can accept new requirements at any time during the Sprint to reflect changing priorities

Correct Answer: B — The Product Owner maintains the Product Backlog and can update it at any time — adding new items discovered by stakeholders, modifying existing items based on Sprint Review feedback, or reordering based on changing priorities. This is Scrum's operational expression of welcoming changing requirements.

Distractor Analysis:

- Why A is incorrect: The Scrum Guide explicitly states the Product Backlog is emergent — it is never locked. Only the Sprint Backlog (for the current Sprint) has protected scope.
- Why C is incorrect: While Developers can suggest additions and do technical refinement, the Product Owner owns the Product Backlog and makes final ordering and content decisions.
- Why D is incorrect: The Sprint Backlog is protected from scope changes that would endanger the Sprint Goal. New requirements go to the Product Backlog for future Sprints, not into the current Sprint.

---

## Question 10

A software team at a hospital is building a patient medication tracking system. Government regulations require that every system requirement be traceable to a specific safety standard and linked to test cases proving it is implemented correctly. Which of the following is the most appropriate Agile response to this regulatory requirement?

- A) Refuse to use Scrum because it is incompatible with regulatory traceability requirements
- B) Abandon user stories and use only formal requirements specification documents
- C) Maintain traceability within the Scrum framework by writing acceptance criteria that reference regulatory standards and linking backlog items to test cases in the team's tooling
- D) Use traceability only for non-functional requirements; user stories for functional requirements do not require regulatory linking

Correct Answer: C — Scrum is flexible enough to accommodate regulatory traceability. Teams can write acceptance criteria that reference specific regulatory requirements, use backlog management and testing tools to link stories to test cases, and satisfy regulatory audits without abandoning Scrum's iterative approach. The Scrum Guide does not prohibit regulatory artifacts.

Distractor Analysis:

- Why A is incorrect: Scrum is used successfully in healthcare, finance, and aerospace — regulated industries with strict traceability requirements. The framework accommodates additional compliance practices.
- Why B is incorrect: Abandoning user stories removes the benefits of the Agile format (dialogue, emergence, lightweight specification) without being required. User stories with good acceptance criteria can satisfy traceability needs.
- Why D is incorrect: Regulatory traceability typically applies to all safety-relevant requirements, whether functional or non-functional. Exempting functional requirements from traceability would likely fail a regulatory audit.

---

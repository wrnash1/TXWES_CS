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

- Why A is incorrect: There is no rule about who writes which format. Product Owners, Business Analysts, and Developers can write either format depending on team practice.
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
- Why C is incorrect: While Developers can suggest additions during refinement, the Product Owner owns the Product Backlog and makes final ordering and content decisions.
- Why D is incorrect: The Sprint Backlog is protected from scope changes that would endanger the Sprint Goal. New requirements go to the Product Backlog for future Sprints, not into the current Sprint.

---

## Question 10

A software team at a hospital is building a patient medication tracking system. Government regulations require that every system requirement be traceable to a specific safety standard and linked to test cases proving it is implemented correctly. Which of the following is the most appropriate Agile response to this regulatory requirement?

- A) Refuse to use Scrum because it is incompatible with regulatory traceability requirements
- B) Abandon user stories and use only formal requirements specification documents
- C) Maintain traceability within the Scrum framework by writing acceptance criteria that reference regulatory standards and linking backlog items to test cases in the team's tooling
- D) Use traceability only for non-functional requirements; user stories for functional requirements do not require regulatory linking

Correct Answer: C — Scrum is flexible enough to accommodate regulatory traceability. Teams can write acceptance criteria that reference specific regulatory requirements, use backlog management and testing tools to link stories to test cases, and satisfy regulatory audits without abandoning Scrum's iterative approach.

Distractor Analysis:

- Why A is incorrect: Scrum is used successfully in healthcare, finance, and aerospace — regulated industries with strict traceability requirements. The framework accommodates additional compliance practices.
- Why B is incorrect: Abandoning user stories removes the benefits of Agile format without being required. User stories with good acceptance criteria can satisfy traceability needs.
- Why D is incorrect: Regulatory traceability typically applies to all safety-relevant requirements. Exempting functional requirements from traceability would likely fail a regulatory audit.

---

### Question 11 (5 points)

Which of the five requirements engineering activities is most analogous to the Sprint Review in Scrum?

- A) Elicitation — because the Sprint Review gathers new requirements from stakeholders
- B) Validation — because the Sprint Review confirms that implemented items match actual stakeholder needs
- C) Specification — because the Sprint Review produces documentation of completed features
- D) Management — because the Sprint Review tracks requirements changes over time

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — While new requirements may surface at a Sprint Review, the primary purpose is validating what was built, not eliciting new requirements.
  - C) Incorrect — The Sprint Review demonstrates working software; it is not a documentation-production activity.
  - D) Incorrect — Requirements management (tracking changes) is the Product Owner's ongoing Product Backlog activity, not the Sprint Review's primary function.

---

### Question 12 (5 points)

A use case lists the following as a postcondition: "User's password has been updated and the old password is invalidated." What does this postcondition tell the system designer?

- A) The condition the system must be in after the main success scenario completes
- B) The condition the system must be in before the use case can begin executing
- C) An alternative path the user may take if they forget their new password immediately
- D) A test case that must be executed before the use case is approved

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Incorrect — A condition that must be true before the use case begins is a precondition, not a postcondition.
  - C) Incorrect — An alternative path during the use case execution is an alternative flow, not a postcondition.
  - D) Incorrect — A postcondition is part of the use case specification, not a test case document; it describes the state after success, which test cases may verify.

---

### Question 13 (5 points)

A stakeholder says: "The app needs to work on iPhones, Androids, and older browsers." Is this a functional or non-functional requirement?

- A) Functional — because it describes what users can do with the app
- B) Non-functional — it is a compatibility/portability quality attribute constraint, not a specific behavior the system performs
- C) Functional — because platform support is a specific feature the Product Owner can order in the backlog
- D) It is neither functional nor non-functional; it is a design constraint that belongs in the technical architecture document

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Platform support is not a user-triggered behavior; it is a constraint on the system's portability quality attribute.
  - C) Incorrect — While it may appear as a backlog item requiring specific development work, the requirement itself is a quality attribute (portability), not a user action.
  - D) Incorrect — Cross-platform support is classified as a non-functional requirement (portability); it is not excluded from the requirements taxonomy.

---

### Question 14 (5 points)

In Scrum, what is the recommended approach for capturing a significant non-functional requirement like "all database queries must complete within 100ms" that requires dedicated optimization work?

- A) Add it to the Definition of Done only, since performance standards always belong there
- B) Add it both to the Definition of Done (as a quality gate) and as a Product Backlog Item requiring specific development effort if the current architecture cannot meet the standard
- C) Write it as a user story: "As a user, I can experience fast queries so that the app feels responsive"
- D) Ignore it until a Sprint Review stakeholder complains about performance

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — If meeting the performance standard requires substantial development work (optimization, indexing, caching), that work needs to be explicitly tracked as a backlog item, not just listed as a DoD quality gate.
  - C) Incorrect — While writing it as a user story captures the user value, it lacks the specific, testable quality attribute standard needed and should be supplemented with the DoD entry.
  - D) Incorrect — Reactive performance fixes are far more expensive than proactive NFR planning; deferring until complaints arrive is a classic NFR neglect pattern.

---

### Question 15 (5 points)

What is progressive elaboration in Scrum requirements management?

- A) A technique where the Product Owner writes more detailed requirements with each Sprint until a complete specification exists
- B) The practice of adding detail to Product Backlog items gradually as they move closer to the top of the backlog and nearer to Sprint-level work
- C) The process of elaborating on completed features in the Sprint Review documentation
- D) A Waterfall technique that was adapted into Scrum for large enterprise projects

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — The goal is not to build a complete specification over time; items at the bottom of the backlog intentionally remain vague because detailed specification now would likely be wasted if priorities change.
  - C) Incorrect — Sprint Review documentation is about demonstrating the Increment, not elaborating on completed features.
  - D) Incorrect — Progressive elaboration is a core Agile/Scrum principle, not a Waterfall technique.

---

### Question 16 (5 points)

A use case includes the following step: "4a. If the entered email does not match any registered account, display a generic success message." What type of use case flow is this?

- A) A postcondition
- B) A main success scenario step
- C) An alternative flow branching from step 4
- D) An exception flow for a system error

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Incorrect — A postcondition describes the state after the use case completes; this step describes behavior during execution when a condition is met.
  - B) Incorrect — The "4a." notation indicates a branch from step 4, which is the convention for alternative flows; main success scenario steps are sequentially numbered without letter suffixes.
  - D) Incorrect — An exception flow handles system errors (e.g., database failure); this step handles a valid user input condition (unrecognized email), which is an alternative flow.

---

### Question 17 (5 points)

Which of the following Product Backlog items best captures a non-functional requirement as a user story?

- A) "As a developer, I will optimize database indexes to improve query performance."
- B) "As a user, I can search for products and receive results within 2 seconds so that I can find what I need without waiting."
- C) "The system shall maintain 99.9% uptime during peak hours."
- D) "Performance: all API endpoints must respond within 500ms (P99)."

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — This is a developer-perspective technical task, not a user story with a user benefit; it also lacks the performance standard as a user-visible outcome.
  - C) Incorrect — "The system shall" is system-specification language, not a user story format; it also lacks a user perspective and benefit.
  - D) Incorrect — This is a technical specification statement, not a user story; it belongs in the Definition of Done or technical documentation, not as a standalone user story.

---

### Question 18 (5 points)

The Scrum Guide says the Product Owner is accountable for "developing and explicitly communicating the Product Goal." How does this responsibility relate to traditional requirements engineering?

- A) The Product Goal replaces all traditional requirements activities — no analysis or validation is needed
- B) The Product Goal serves as the strategic vision that gives context to requirements elicitation, helping the team understand which requirements align with the product's intended direction
- C) The Product Goal is equivalent to a requirements specification document that stakeholders sign off on before Sprint 1
- D) The Product Goal is created by the Scrum Master and communicated to the Product Owner at project kickoff

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — The Product Goal provides strategic direction but does not replace analysis, validation, or backlog refinement activities.
  - C) Incorrect — The Product Goal is a future-state vision statement, not a detailed specification; it does not require stakeholder sign-off as a Waterfall requirements freeze.
  - D) Incorrect — The Product Goal is developed and owned by the Product Owner, not the Scrum Master.

---

### Question 19 (5 points)

A traditional requirements matrix includes columns: Requirement ID, Description, Source, Priority, Status, and Test Case. Which Scrum artifact and practice combination provides equivalent traceability?

- A) The Sprint Goal, which covers all requirements for a Sprint in one statement
- B) The Definition of Done, which maps every requirement to a test case
- C) Product Backlog Items with acceptance criteria linked to test cases in the team's tooling, combined with the Definition of Done for quality standards
- D) The Daily Scrum, where Developers report requirement completion status to stakeholders

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Incorrect — The Sprint Goal is a one-sentence objective for a Sprint; it does not provide item-level traceability.
  - B) Incorrect — The Definition of Done provides quality standards but does not map individual functional requirements to specific test cases.
  - D) Incorrect — The Daily Scrum is a 15-minute Developer synchronization event; it does not produce traceability documentation.

---

### Question 20 (5 points)

A Product Owner asks a Developer to skip writing acceptance criteria for a well-understood story because "everyone knows what it should do." What risk does this create?

- A) No significant risk — well-understood stories do not need formal acceptance criteria
- B) The team loses a shared, explicit definition of Done for that item, risking disagreement at Sprint Review about whether it is complete
- C) The story violates the INVEST "Testable" criterion, making it ineligible for Sprint Planning
- D) The Scrum Master must refuse to facilitate Sprint Planning for that Sprint until acceptance criteria are added

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — "Everyone knows what it should do" is a common assumption that breaks down under pressure, ambiguity, or when different people have different mental models.
  - C) Incorrect — While a story without acceptance criteria fails the "Testable" criterion, it is not automatically "ineligible"; it signals that refinement is needed, not that Sprint Planning must be blocked.
  - D) Incorrect — The Scrum Master does not refuse to facilitate Sprint Planning; they coach the team on quality practices but do not veto events.

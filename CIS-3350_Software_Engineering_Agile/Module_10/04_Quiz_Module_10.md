# Quiz: Module 10 – Requirements Engineering and Use Cases

## Course: CIS-3350_Software_Engineering_Agile (Professional Scrum Master (PSM I))

---

### Question 1

In Scrum, what artifact serves as the primary repository for all known product requirements?

* A) The Requirements Specification Document, maintained by the Business Analyst
* B) The Sprint Backlog, updated daily by the Developers
* C) The Product Backlog, owned and ordered by the Product Owner
* D) The Definition of Done, agreed upon by the Scrum Team before Sprint 1

Correct Answer: C) The Product Backlog is the single, emergent, ordered list of everything known to be needed in the product — the Scrum replacement for a traditional requirements document.

Distractor Analysis:

* *Why C is correct:* The Scrum Guide defines the Product Backlog as the sole source of work for the Scrum Team, containing all requirements as items that are continuously refined and re-ordered.
* *Why A is incorrect:* Scrum does not define a Business Analyst role or a formal requirements specification document. These are traditional waterfall artifacts.
* *Why B is incorrect:* The Sprint Backlog contains only the work selected for the current Sprint — it is a subset of the Product Backlog, not a repository for all requirements.
* *Why D is incorrect:* The Definition of Done is a quality standard for the Increment, not a requirements document. It may capture non-functional requirements but is not a backlog of all requirements.

---

### Question 2

Which of the following is the most accurate definition of a non-functional requirement?

* A) A requirement that describes a specific behavior the system must perform when triggered by a user action.
* B) A constraint on the system's quality attributes — such as performance, security, scalability, or availability — rather than its specific behaviors.
* C) A requirement that has been deprioritized in the Product Backlog and is not planned for implementation.
* D) A feature that the development team has decided not to build because it is too technically complex.

Correct Answer: B)

Distractor Analysis:

* *Why B is correct:* Non-functional requirements (NFRs) define *how well* the system must operate — response times, uptime targets, encryption standards, load capacity — as opposed to *what* the system does.
* *Why A is incorrect:* This describes a functional requirement — a specific system behavior triggered by user or system input.
* *Why C is incorrect:* A deprioritized backlog item is simply lower in ordering; it is not defined as a "non-functional" requirement by that status.
* *Why D is incorrect:* A technically complex feature that is deferred is a prioritization decision — not a category of requirement type.

---

### Question 3

A use case specifies that a customer can log in using their email and password (main success scenario) OR reset their password if they have forgotten it (alternative flow). What does the alternative flow represent?

* A) A defect in the system that must be fixed before the use case is considered complete
* B) A separate use case that should be documented independently in the Product Backlog
* C) A deviation from the main success scenario that the system must handle gracefully
* D) An out-of-scope feature that should be removed from the use case documentation

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* Alternative flows in use cases describe valid paths a user may take that deviate from the main success scenario — situations the system must handle without failing, such as forgotten password recovery.
* *Why A is incorrect:* An alternative flow is a designed system behavior, not a defect. Password reset is a valid user path, not an error condition.
* *Why B is incorrect:* Password reset could be modeled as a separate use case, but the alternative flow format is also a valid and common approach to document it within the same use case.
* *Why D is incorrect:* An alternative flow that handles a real user need is in scope by definition. Removing it would create an incomplete system specification.

---

### Question 4

A stakeholder requests that all 200 system requirements be fully documented and signed off before Sprint 1 begins. How should the Scrum Team respond?

* A) Agree to the request, because the Product Owner needs a complete requirements specification to order the Product Backlog.
* B) Agree, but limit documentation to functional requirements only — non-functional requirements can be addressed later.
* C) Explain that the Product Backlog supports progressive elaboration — requirements emerge and are refined throughout the project rather than being fully specified upfront.
* D) Cancel the project and revert to a Waterfall model, since the stakeholder is not ready for Agile.

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* Scrum's empirical approach means requirements are discovered and refined iteratively. The Product Backlog starts with known items and evolves as the team learns — freezing all requirements upfront is a Waterfall practice that removes Scrum's adaptability.
* *Why A is incorrect:* A complete upfront requirements specification is a Waterfall artifact. The Product Owner needs an ordered, sufficiently detailed set of near-term backlog items — not a frozen complete specification.
* *Why B is incorrect:* Splitting requirements into "functional now / NFR later" still involves a large upfront specification effort that delays value delivery and locks in decisions made with incomplete information.
* *Why D is incorrect:* This is an overreaction. The Scrum Master and Product Owner should educate the stakeholder on how Scrum handles requirements, not abandon the framework.

---

### Question 5

Where are non-functional requirements (such as "all pages must load within 2 seconds") most commonly captured in Scrum?

* A) In a separate Non-Functional Requirements Document maintained outside the Scrum artifacts
* B) As tasks assigned to the Scrum Master in the Sprint Backlog
* C) In the Definition of Done, ensuring every Increment meets the performance standard as a quality baseline
* D) In the Sprint Goal, communicated by the Product Owner at each Sprint Planning

Correct Answer: C)

Distractor Analysis:

* *Why C is correct:* System-wide NFRs that apply to every Increment (like load time thresholds or security standards) are best captured in the Definition of Done so they are verified for every piece of delivered work — not just selectively.
* *Why A is incorrect:* Creating a separate NFR document outside Scrum artifacts is a Waterfall practice. Scrum centralizes requirements information in the Product Backlog and Definition of Done.
* *Why B is incorrect:* The Scrum Master does not own backlog tasks or technical standards. NFRs are owned collectively by the Developers (for DoD) and the Product Owner (for backlog items).
* *Why D is incorrect:* The Sprint Goal is a short, specific objective for the current Sprint — not an appropriate place to encode standing quality standards that apply to all Sprints.

# Quiz: Module 04 - Requirements Analysis and Documentation

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

Which of the following is an example of a non-functional requirement?

A) The system shall allow an administrator to create, edit, and deactivate user accounts.

B) The system shall generate a monthly sales report in PDF format.

C) The system shall respond to any search query within 2 seconds under normal load conditions.

D) The system shall send an email notification when an order status changes to "Shipped."

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: This is a functional requirement — it describes a specific behavior (user account management) the system must perform.
- Why B is incorrect: This is a functional requirement — it describes a specific output behavior (generating a PDF report).
- Why D is incorrect: This is a functional requirement — it describes a triggered system action (sending an email notification).
- Why C is correct: This is a non-functional requirement (performance/quality attribute) — it specifies how well the system must perform a search function, not what function it performs.

---

## Question 2

In requirements engineering, which of the following is the most accurate definition of requirements traceability?

A) The process of distributing approved requirements documents to all project stakeholders through the project communication plan

B) The ability to link each requirement forward to the design, test cases, and implementation that satisfy it, and backward to the business need that originated it

C) A technique for prioritizing requirements by assigning each requirement a numerical score based on business value and implementation effort

D) The activity of rewriting requirements that stakeholders found unclear after the initial review meeting

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Distributing documents is a communication task, not traceability.
- Why C is incorrect: This describes a requirements prioritization technique (such as MoSCoW or weighted scoring), not traceability.
- Why D is incorrect: Rewriting unclear requirements is part of verification/refinement, not traceability.
- Why B is correct: Requirements traceability provides bidirectional linkage — from business needs through requirements to design, implementation, and tests — enabling impact analysis and completeness confirmation.

---

## Question 3

A BA presents a completed requirements document to stakeholders for review. A stakeholder confirms that all the requirements are clearly written and internally consistent but says: "These requirements don't solve our actual business problem — you've documented what the old system does, not what we need the new system to do." Which activity has failed?

A) Requirements verification

B) Requirements elicitation

C) Requirements validation

D) Requirements prioritization

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Requirements verification checks that requirements are well-formed (clear, complete, consistent, testable). The stakeholder confirmed they are clearly written — verification passed.
- Why B is incorrect: While the elicitation may have been flawed, the activity that specifically failed here is the confirmation that requirements match the business need, which is validation.
- Why D is incorrect: Prioritization is the ordering of requirements by importance; it is not what failed in this scenario.
- Why C is correct: Requirements validation answers "Are we building the right thing?" — confirming requirements reflect actual business needs. The stakeholder's feedback reveals that validation failed because the requirements describe the wrong future state.

---

## Question 4

Which of the following best describes a business rule as opposed to a functional requirement?

A) A statement describing how fast the system must process transactions

B) A constraint or policy from the business domain that the system must enforce, such as "All purchase orders over $10,000 require dual approval"

C) A specific system behavior triggered by a user action, such as "clicking Save stores the record to the database"

D) A diagram showing the relationships between data entities stored in the system database

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: This describes a non-functional requirement (performance), not a business rule.
- Why C is incorrect: This describes a functional requirement — a specific system behavior in response to a user action.
- Why D is incorrect: This describes an entity-relationship diagram, a data modeling artifact, not a business rule definition.
- Why B is correct: Business rules are domain-level constraints — policies, regulations, or operational procedures — that constrain system behavior but originate in the business context, not in the technology. The dual-approval threshold is a classic example from financial policy.

---

## Question 5

A project team is preparing to hand off the requirements baseline to the development team. The BA wants to ensure that every requirement can be confirmed as implemented and tested. Which artifact should the BA create or update for this purpose?

A) A stakeholder register listing each stakeholder's role and communication preferences

B) A risk register documenting project uncertainties and their probability/impact scores

C) A requirements traceability matrix (RTM) linking each requirement to design components and test cases

D) A project schedule showing milestones and task assignments for the development team

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: A stakeholder register documents stakeholder information for engagement planning; it does not link requirements to test cases or implementation.
- Why B is incorrect: A risk register tracks project uncertainties; it does not provide the requirement-to-test linkage the BA needs.
- Why D is incorrect: A project schedule manages timing and resource assignments; it does not ensure requirements coverage.
- Why C is correct: An RTM explicitly maps each requirement to the design element and test case that address it, giving the team a tool to confirm complete implementation and test coverage as development progresses.

---

## Question 6

A BA has written the following requirement: "The system shall provide a user-friendly interface." Which quality criterion does this requirement fail, and what change would fix it?

A) It fails the Consistent criterion — it must be compared against other requirements to identify contradictions

B) It fails the Testable criterion — "user-friendly" is subjective and cannot be objectively verified; the requirement must specify a measurable standard

C) It fails the Necessary criterion — user interface requirements are optional enhancements, not business needs

D) It fails the Complete criterion — it does not specify which users the interface serves

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: The requirement does not contradict other requirements; consistency is not the issue here.
- Why C is incorrect: User interface usability is a legitimate business need; it is not optional. The Necessary criterion is not violated.
- Why D is incorrect: While specifying the user audience would improve the requirement, the primary and more fundamental failure is that "user-friendly" cannot be objectively tested.
- Why B is correct: "User-friendly" is a subjective, unmeasurable qualifier. No QA analyst can write a test case with a clear pass/fail outcome against this requirement. The fix is to specify a measurable standard, such as: "The system shall achieve a System Usability Scale score of at least 70 in post-deployment user testing with a sample of 20 representative users."

---

## Question 7

A BA needs to document a requirement that the organization's existing 47,000 customer records must be migrated from the legacy system's flat-file format into the new relational database before the system goes live. Once migration is complete, the migration tool itself will be decommissioned. How should this requirement be classified?

A) Functional requirement — because it describes a system behavior (migrating data)

B) Non-functional requirement — because it concerns system performance during the migration window

C) Transition requirement — because it is needed only during the cutover and has no value after the transition

D) Business requirement — because it supports the organization's goal of maintaining complete customer records

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: While the migration tool does perform a function, classifying it as a permanent functional requirement misses the defining characteristic: it is temporary and will be decommissioned after cutover.
- Why B is incorrect: A non-functional requirement describes a quality attribute of the ongoing system; the migration activity is not an ongoing system capability.
- Why D is incorrect: Business requirements describe organizational goals; this is a specific technical activity needed only during the transition, not an organizational objective.
- Why C is correct: BABOK defines transition requirements as capabilities needed only to support the change from current state to future state. A one-time data migration tool decommissioned after go-live is the textbook example.

---

## Question 8

Two requirements in the same specification read as follows. Requirement FR-018: "The system shall send an automated payment reminder 7 days before the due date." Requirement FR-031: "The system shall not send any automated communications to customers unless they have explicitly opted in to marketing emails." Which quality criterion do these two requirements violate together?

A) Testability — the combined rule cannot be tested with a single test case

B) Completeness — neither requirement alone describes the full payment reminder workflow

C) Consistency — the two requirements contradict each other because payment reminders may be sent to customers who have not opted in to marketing emails

D) Feasibility — the combination of these two requirements cannot be implemented in a single system

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Each requirement is individually testable; the problem is not a testing challenge but a logical contradiction between the two.
- Why B is incorrect: Completeness concerns missing information within a requirement; the issue here is that the requirements give conflicting instructions.
- Why D is incorrect: The combination is technically implementable once the contradiction is resolved; feasibility is not the issue.
- Why C is correct: FR-018 requires sending payment reminders; FR-031 prohibits automated communications to customers who have not opted in to marketing emails. A customer who opted out of marketing emails would never receive the legally required payment reminder — a direct contradiction that must be resolved before design begins.

---

## Question 9

Which BABOK requirement classification covers the higher-level goals of the organization that the project is intended to achieve — not the system features, but the business outcomes the system must enable?

A) Stakeholder requirements

B) Functional requirements

C) Business requirements

D) Transition requirements

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Stakeholder requirements describe what specific stakeholder groups need from the solution — they are more specific than business requirements and closer to user needs.
- Why B is incorrect: Functional requirements describe specific system behaviors — they are lower-level specifications derived from stakeholder and business requirements.
- Why D is incorrect: Transition requirements describe temporary capabilities needed only during the changeover; they are not the organizational goals the project is meant to achieve.
- Why C is correct: Business requirements in BABOK describe the higher-level objectives of the enterprise — the "why" behind the project. Example: "Reduce average loan processing time from 5 days to same-day." All other requirement categories flow from business requirements.

---

## Question 10

A QA analyst approaches the BA and says: "I cannot write a test case for Requirement NFR-007. It says the system must be scalable, but there is no definition of what scalability means for this system." Which is the most appropriate corrective action?

A) Accept the requirement as written and allow the development team to interpret "scalable" based on their technical experience

B) Work with stakeholders to define specific, measurable scalability thresholds, then rewrite the requirement to include those thresholds

C) Delete the requirement because non-functional requirements that cannot be tested should be removed from the specification

D) Move the requirement to a "future phase" section of the specification and proceed without it

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Allowing developers to interpret "scalable" without stakeholder input means the system may be built to a definition that does not match business needs; this is a requirements defect, not a design decision.
- Why C is incorrect: The underlying business need (scalability) is real and important; the solution is to rewrite the requirement correctly, not to remove it.
- Why D is incorrect: Deferring a known quality requirement without stakeholder agreement risks building a system that cannot meet future demands; this is not a responsible BA action.
- Why B is correct: A non-testable non-functional requirement must be rewritten with measurable thresholds. The BA should facilitate a stakeholder session to define what scalability means — for example: "The system shall support a 3x increase in concurrent users above the projected peak load of 500 users without exceeding a 10% degradation in response time." This makes the requirement specific, measurable, and testable.

# Quiz: Module 05 - Use Case Modeling and User Stories

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

In a use case diagram, what does the include relationship between two use cases indicate?

A) The included use case is optional and only executes when a specific condition is true

B) The included use case is always invoked as a mandatory part of the base use case

C) The included use case inherits all behaviors from the base use case through generalization

D) The included use case is performed by a secondary actor rather than the primary actor

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Optional, condition-based execution describes the extend relationship, not include.
- Why C is incorrect: Inheritance of behavior is represented by a generalization relationship (open arrow), not include.
- Why D is incorrect: Actor involvement is shown by association lines, not by include relationships between use cases.
- Why B is correct: Include indicates a mandatory sub-flow — every time the base use case runs, the included use case is also triggered; it is used to factor out shared behavior across multiple use cases.

---

## Question 2

In Agile development, which of the following is the most accurate definition of acceptance criteria?

A) A prioritized list of all features and tasks the development team may be asked to build during the project

B) A set of specific, verifiable conditions that a user story must satisfy for the product owner to accept it as complete

C) A formal document signed by the project sponsor that authorizes the development team to begin construction

D) A series of automated regression tests that the development team runs before each code commit

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: This describes the product backlog, not acceptance criteria.
- Why C is incorrect: This describes a project authorization document, not acceptance criteria for a user story.
- Why D is incorrect: Automated regression tests are a QA/DevOps artifact; acceptance criteria define what "done" means for a story, not the testing automation implementation.
- Why B is correct: Acceptance criteria make user stories testable and define the completion boundary; they are typically written in Given/When/Then format and reviewed by the product owner.

---

## Question 3

A team writes the following user story: "As a customer service representative, I want to manage all customer records, billing histories, refund requests, order adjustments, and account notes so that I have everything in one place." Which INVEST quality problem does this story have?

A) It is not Independent — it depends on other stories to be completed first

B) It is not Valuable — there is no clear business benefit stated

C) It is not Small — it covers too many features to be completed in a single sprint

D) It is not Negotiable — the implementation approach is already locked in

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: The story does not appear to depend on other stories; independence is not the primary issue.
- Why B is incorrect: The story states clear business value ("everything in one place"), so the Valuable criterion is met.
- Why D is incorrect: The story does not prescribe an implementation approach; negotiability is not the problem.
- Why C is correct: The story bundles five distinct features (records, billing, refunds, adjustments, notes) into a single item — a classic epic. It violates the Small criterion and should be split into individual sprint-sized user stories.

---

## Question 4

Which of the following correctly represents the standard user story format recommended by the Agile Alliance?

A) "The system shall allow a registered customer to reset their password via email verification within 30 seconds."

B) "As a registered customer, I want to reset my password via email so that I can regain access to my account without contacting support."

C) "Given a customer is locked out, when they request a password reset, then the system sends a reset email within 60 seconds."

D) "Password Reset: High Priority. Estimated effort: 3 story points. Assigned to Sprint 2."

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: This is a functional requirement written in IEEE "shall" format — not a user story.
- Why C is incorrect: This is an acceptance criterion written in Given/When/Then format — it defines done, but it is not the user story itself.
- Why D is incorrect: This is backlog item metadata (priority, points, sprint), not a user story narrative.
- Why B is correct: "As a [role], I want [goal] so that [business value]" is the standard three-part user story format capturing who benefits, what they want to do, and why it matters.

---

## Question 5

A BA is building a product backlog for a new HR onboarding system. One item reads: "As an HR coordinator, I want to generate a new-hire welcome packet so that new employees have all their Day 1 materials before they arrive." The product owner wants to ensure this story is testable. What should be added?

A) A Gantt chart showing when in the project schedule the feature will be built

B) A use case diagram showing the HR coordinator as an actor interacting with the system

C) Specific acceptance criteria defining exactly what the welcome packet must contain and what constitutes successful generation

D) A data flow diagram showing how employee data moves through the onboarding process

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: A Gantt chart is a scheduling artifact; it does not make the user story testable.
- Why B is incorrect: A use case diagram provides context and scope but does not define the acceptance conditions for a specific story.
- Why D is incorrect: A data flow diagram models data movement; it does not define what "done" means for this user story.
- Why C is correct: Acceptance criteria specify the verifiable conditions the product owner will check when accepting the story — they are what make a user story testable, satisfying the T in the INVEST criteria.

---

## Question 6

A use case diagram shows the "Withdraw Cash" use case connected to both a "Bank Customer" actor and an "ATM Network System" actor. The dashed arrow labeled extend points from a "Charge Out-of-Network Fee" use case to the "Withdraw Cash" use case, with the condition note "customer's card is from a different bank." What does this model correctly represent?

A) Charging the fee is always mandatory when a customer withdraws cash

B) Charging the fee is optional and only occurs when a specific condition is true

C) The ATM Network System must extend the Withdraw Cash use case with the fee

D) The fee use case inherits behavior from the Withdraw Cash use case

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: If the fee were always mandatory, the relationship would be include, not extend. The condition note confirms it is conditional.
- Why C is incorrect: The extend relationship is between two use cases, not between an actor and a use case; the ATM Network System is an actor, not a use case.
- Why D is incorrect: Inheritance is represented by a generalization relationship (open arrow), not by extend.
- Why B is correct: Extend indicates an optional behavior that executes only when a specific condition is met. The condition note ("customer's card is from a different bank") confirms that the fee is applied selectively — exactly what extend models.

---

## Question 7

A BA is writing a use case specification for "Submit Expense Report." The precondition states: "The employee must be logged into the system." The main success scenario describes 8 steps ending with the system sending a confirmation email. The BA is now documenting what happens when the employee's manager is on leave and cannot approve the report. Which section of the use case specification should contain this?

A) Preconditions — because the manager's availability affects whether the use case can begin

B) Main Success Scenario — because manager approval is a step in the normal workflow

C) Alternate Flow — because manager absence is a valid variation from the main path that requires a different but valid sequence

D) Postconditions — because the state of the manager's approval affects the outcome

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Preconditions define what must be true before the use case starts; manager availability mid-process is not a precondition.
- Why B is incorrect: The main success scenario describes the ideal path when all goes as expected; manager absence is a deviation, not the normal case.
- Why D is incorrect: Postconditions describe the state after the use case completes; the alternate handling process belongs in the flow sections, not postconditions.
- Why C is correct: An alternate flow documents a valid variation from the main path — a different sequence that still leads to a successful outcome. Manager absence triggering an escalation or substitute approver is a valid alternate path, not a failure.

---

## Question 8

Which of the following correctly describes the direction of the arrow in an extend relationship in a UML use case diagram?

A) The arrow points from the base use case to the extending use case

B) The arrow points from the extending use case to the base use case

C) The arrow is bidirectional, connecting both use cases with arrowheads at each end

D) There is no arrowhead; extend is represented by a solid association line

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: This describes the direction used in the include relationship (base to included), not extend.
- Why C is incorrect: Use case relationship arrows are unidirectional; there is no bidirectional extend relationship.
- Why D is incorrect: Association lines (without stereotypes) connect actors to use cases; include and extend are dashed lines with arrowheads and stereotype labels.
- Why B is correct: In the extend relationship, the dashed arrow points from the extending use case (the optional behavior) to the base use case (the one being extended). This is the opposite of include, and is a commonly tested distinction on the ECBA exam.

---

## Question 9

A product owner reviews a user story backlog and asks the BA to identify which items are epics that need to be broken down before sprint planning. Which of the following is most clearly an epic rather than a sprint-sized story?

A) "As a warehouse worker, I want to scan a barcode to mark a package as received so that inventory is updated immediately."

B) "As a store manager, I want to view today's sales dashboard so that I can monitor performance at a glance."

C) "As a customer, I want to manage my entire account including profile, payment methods, order history, subscription preferences, and communication settings so that I have full control of my account."

D) "As a delivery driver, I want to receive a push notification when a new delivery is assigned to me so that I can start routing immediately."

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Scanning a barcode to update inventory is a single, discrete, sprint-sized behavior — it satisfies the Small criterion.
- Why B is incorrect: Viewing a sales dashboard is a single discrete feature; it is not bundling multiple unrelated capabilities.
- Why D is incorrect: Receiving a push notification for a new assignment is a single, well-defined behavior suitable for a single sprint.
- Why C is correct: This story bundles at least five distinct features (profile, payment, order history, subscriptions, communication settings) into a single item. Any team would need multiple sprints to deliver all five — this is clearly an epic that must be split into individual sprint-sized user stories.

---

## Question 10

A BA is documenting preconditions for the "Transfer Funds" use case in an online banking system. Which of the following is a correctly stated precondition?

A) The customer has successfully logged in and has two or more active accounts with available balances

B) The system will validate the transfer amount before processing the transaction

C) The customer's account balance will be reduced by the transfer amount upon completion

D) The system displays a confirmation message after the transfer is submitted successfully

Correct Answer: A

Distractor Analysis:

- Why A is incorrect to reject: The other options describe actions or outcomes within the use case, not conditions that must exist before the use case begins.
- Why B is incorrect: This describes a step within the main success scenario (system validates the amount), not a precondition.
- Why C is incorrect: This describes a postcondition — a state that is true after the use case completes, not before it begins.
- Why D is incorrect: This also describes a postcondition or a step in the main scenario — the confirmation message is a result, not a prerequisite.
- Why A is correct: A precondition describes what must already be true before the use case can begin. The customer being logged in and having two accounts with available balances are conditions that must exist before the Transfer Funds use case can execute.

---

## Question 11

In a use case diagram for a university library system, the "Search Catalog" use case and the "Reserve Book" use case both require the user to be authenticated. A BA creates a separate "Authenticate User" use case and connects it to both with include relationships. What design principle does this represent?

A) Extend — authentication is optional and only triggered under certain conditions

B) Factoring out shared mandatory sub-flows into an included use case to avoid repetition

C) Generalization — the Authenticate User use case inherits from both parent use cases

D) Actor multiplicity — the same actor performs both the base and included use cases

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Include, not extend, is used when a sub-flow is always mandatory; extend is for optional, conditional behavior.
- Why C is incorrect: Generalization is an inheritance relationship between actors or between use cases with similar behavior; the scenario describes a shared sub-flow, not inheritance.
- Why D is incorrect: Actor multiplicity is not a UML use case concept; the scenario describes a structural relationship between use cases.
- Why B is correct: When multiple use cases share an identical mandatory sub-flow, BABOK and UML recommend factoring it out into a separate included use case. This reduces duplication and ensures consistent behavior across all use cases that require authentication.

---

## Question 12

A development team receives a user story: "As an admin, I want to delete user accounts." After one sprint, the team delivers the feature. During the sprint review, the product owner rejects the story saying "I needed soft-delete that archives the account, not hard-delete that permanently removes the data." Which INVEST criterion was violated?

A) Independent — the story depended on an account archival feature not yet built

B) Negotiable — the team assumed the implementation without discussing it with the product owner

C) Valuable — the delivered feature does not provide business value to the organization

D) Testable — the story had no acceptance criteria to distinguish soft-delete from hard-delete

Correct Answer: D

Distractor Analysis:

- Why A is incorrect: The story's independence is not the issue; the problem is the ambiguity about what "delete" means.
- Why B is incorrect: While Negotiable is partially relevant, the root cause here is missing acceptance criteria that would have resolved the ambiguity before development began.
- Why C is incorrect: The feature is valuable — the product owner needs account deletion; the issue is the wrong implementation, not lack of value.
- Why D is correct: The absence of acceptance criteria left "delete" undefined, allowing the team to implement hard-delete while the product owner expected soft-delete. Testable acceptance criteria — specifying exactly what the delete function must and must not do — would have caught this before the sprint started.

---

## Question 13

A BA is writing a use case specification for "Process Insurance Claim." One alternate flow reads: "If the claim amount exceeds $50,000, the system routes the claim to senior underwriting review and suspends automatic processing." Which type of scenario does this alternate flow represent?

A) Exception flow — because the system encounters an error condition

B) Alternate flow — because the system follows a different but valid path based on a business condition

C) Main success scenario — because large-claim processing is a core business function

D) Precondition — because the $50,000 threshold must be true before the use case can begin

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: An exception flow handles error or failure conditions; routing a valid high-value claim to senior review is a normal business rule, not an error.
- Why C is incorrect: The main success scenario is the most common path (standard-value claims); the large-claim route is a variation, not the default.
- Why D is incorrect: The $50,000 threshold is checked mid-process, not before the use case begins; it is not a precondition.
- Why B is correct: An alternate flow describes a different but valid sequence triggered by a specific condition. A business rule routing large claims to senior review is a valid alternate path that still achieves the goal of processing the claim.

---

## Question 14

Which of the following user stories best demonstrates the "Valuable" criterion of INVEST?

A) "As a developer, I want to refactor the database connection pool so that the code is cleaner."

B) "As a customer, I want to view my order history so that I can track past purchases and request returns without calling support."

C) "As a tester, I want to write automated test scripts so that regression testing is faster."

D) "As a database administrator, I want to index the transactions table so that query performance improves."

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Code refactoring may be technically necessary but the business value to end users or stakeholders is not articulated; the "so that" clause is an internal developer concern, not a stakeholder benefit.
- Why C is incorrect: Faster regression testing benefits the development team, not the business stakeholders or end users; it is a technical story, not a business-value story.
- Why D is incorrect: Database indexing is a technical improvement; the business value to stakeholders is indirect and unstated.
- Why B is correct: This story clearly identifies a customer benefit (tracking purchases and requesting returns without support calls) — a concrete, articulated business value that directly satisfies a user need.

---

## Question 15

In a use case diagram for an ATM system, the "Bank Customer" actor and the "Bank System" actor are both associated with the "Withdraw Cash" use case. What does the "Bank System" actor's association represent?

A) The Bank System is a human actor who must approve each withdrawal

B) The Bank System is a secondary actor — an external system that the use case interacts with to complete its goal

C) The Bank System is the system under design and should be shown inside the system boundary, not as an actor

D) The Bank System is a generalization of the Bank Customer actor

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: An external banking system is not a human approver; it is an automated external system.
- Why C is incorrect: The system under design (the ATM) is represented by the system boundary rectangle; external systems that interact with it are shown as actors outside the boundary.
- Why D is incorrect: Generalization is an inheritance relationship between actors of the same type; a bank system and a customer are entirely different types of actors.
- Why B is correct: In use case modeling, any external system that interacts with the system under design is modeled as an actor outside the system boundary. The Bank System is a secondary actor — it responds to requests from the ATM system during withdrawal processing.

---

## Question 16

A Scrum team is refining the backlog before sprint planning. One story is estimated at 40 story points. The team's average sprint velocity is 30 story points. What should the product owner do with this story?

A) Schedule it as the only story in an extended sprint to accommodate its size

B) Accept it as-is since story point estimates are relative and can be adjusted during the sprint

C) Split the story into two or more smaller stories that can fit within a sprint

D) Assign it to the senior developer who can complete it faster than the estimate suggests

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Extending sprint duration undermines sprint cadence and disrupts the team's planning rhythm; it is not standard Scrum practice.
- Why B is incorrect: Relative estimates do not change the fact that a 40-point story exceeds the team's capacity; accepting oversized stories leads to incomplete sprint goals.
- Why D is incorrect: Story point estimates are team-level capacity measures, not individual developer assignments; assigning to one person does not resolve the capacity mismatch.
- Why C is correct: When a story exceeds the team's sprint velocity, it should be split into smaller, independently deliverable stories that each fit within a sprint. This is standard backlog refinement practice and directly satisfies the Small criterion of INVEST.

---

## Question 17

A BA is modeling a library system. The use case "Renew Book" includes the use case "Verify Account Standing" because overdue fines or blocks must always be checked before a renewal is processed. What would happen to the "Verify Account Standing" use case if the include relationship is removed?

A) The Renew Book use case would still function correctly because include relationships are optional

B) The Renew Book use case would skip account verification, potentially allowing blocked patrons to renew books — a business rule violation

C) The Verify Account Standing use case would become an extend of Renew Book instead

D) The system would automatically perform verification without the relationship being modeled

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Include relationships are mandatory, not optional; removing an include means the included behavior will no longer be executed.
- Why C is incorrect: Include and extend are fundamentally different relationships; removing include does not automatically convert it to extend.
- Why D is incorrect: The model drives the implementation specification; removing the relationship from the model communicates that verification is not required, and developers would implement accordingly.
- Why B is correct: The include relationship is mandatory; it documents that account verification must always occur during renewal. Removing it would communicate to the development team that verification is not required, enabling blocked patrons to renew — a business rule violation.

---

## Question 18

Which of the following correctly illustrates a well-formed Given/When/Then acceptance criterion for a user story about bill payment?

A) "The system shall process bill payments within 3 seconds."

B) "As a customer, I want to pay my bill online so that I avoid late fees."

C) "Given the customer has a saved payment method and a balance due, When the customer confirms the payment, Then the system shall process the payment and display a confirmation number within 5 seconds."

D) "Bill payment must be implemented in Sprint 3 and tested by QA before release."

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: This is a non-functional requirement written in "shall" format, not an acceptance criterion in Given/When/Then format.
- Why B is incorrect: This is the user story itself in the "As a / I want / So that" format, not an acceptance criterion.
- Why D is incorrect: This is sprint scheduling and QA process information, not a behavioral acceptance criterion.
- Why C is correct: Given/When/Then format correctly specifies: the starting context (Given), the trigger action (When), and the expected system outcome (Then) with a measurable standard (5 seconds, confirmation number). This is a complete, testable acceptance criterion.

---

## Question 19

A BA reviews a use case diagram and notices that a "Generate Report" use case extends a "View Dashboard" use case. A developer asks: "Does the system always generate a report when the user views the dashboard?" What is the correct answer?

A) Yes — extend means the behavior always executes as part of the base use case

B) No — extend means the report generation is optional and only occurs when a specific extension point condition is met

C) It depends — the BA must check the actor association to determine whether it is mandatory

D) Yes — unless the user explicitly opts out using the suppress relationship

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: This describes the include relationship; extend is specifically used for optional, conditional behavior.
- Why C is incorrect: Actor associations do not determine whether extend is mandatory or optional; the extend relationship itself defines conditionality.
- Why D is incorrect: There is no "suppress relationship" in UML use case notation.
- Why B is correct: Extend models optional behavior that executes only when a specific condition is met at an extension point. Report generation only occurs if the user triggers that extension (e.g., clicks "Export Report") — it is not automatic on every dashboard view.

---

## Question 20

A BA is using use cases to model a subscription management system. Which artifact should the BA create first before drawing individual use case diagrams?

A) A state transition diagram showing all subscription lifecycle states

B) A context diagram or use case boundary diagram identifying all actors and the overall system scope

C) A data flow diagram showing how subscription data moves between processes

D) A class diagram showing the attributes of the Subscription entity

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: A state transition diagram models object lifecycle states; it is useful but not the first step in use case modeling.
- Why C is incorrect: A DFD models data movement and is a separate process-modeling technique; use case modeling begins with scope and actor identification, not data flows.
- Why D is incorrect: Class diagrams are object-oriented design artifacts; they are created after requirements have been modeled, not before.
- Why B is correct: Before detailing individual use cases, the BA must establish scope by identifying all actors (primary and secondary) and drawing a high-level use case boundary or context diagram. Without knowing who the actors are and what system they interact with, individual use cases cannot be defined correctly.

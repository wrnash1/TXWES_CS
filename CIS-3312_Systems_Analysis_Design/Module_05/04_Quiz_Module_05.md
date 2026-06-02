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

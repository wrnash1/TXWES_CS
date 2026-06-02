# Video Script: Module 05 - Use Case Modeling and User Stories

**Course:** CIS-3312 Systems Analysis and Design
**Estimated Duration:** 22 minutes
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.

---

## Section 1: Welcome and Module Overview [00:00 - 03:00]

Welcome to Module 05. I am Professor Nash. Today we are covering two of the most important requirements modeling techniques in business analysis: Use Case Modeling and User Stories. These are the primary ways BAs communicate system behavior to both stakeholders and developers, and they appear on the ECBA exam.

[SHOW DIAGRAM: Title slide — "Module 05: Use Case Modeling and User Stories" with BABOK KA 5 label and IIBA ECBA badge]

Use cases come from the UML tradition and are widely used in both traditional and Agile projects. User stories come from the Agile world. Both describe system behavior from the actor's perspective — what a user wants to accomplish — not how the system will implement it. Both are tools for capturing and communicating requirements. We will cover both in depth today.

---

## Section 2: Use Case Modeling [03:00 - 10:00]

[SHOW DIAGRAM: Use case diagram for a simple library system — ellipses for use cases: "Borrow Book," "Return Book," "Search Catalog," "Manage Account"; stick figures for actors: "Library Member," "Librarian"; a rectangle boundary labeled "Library Management System"; associations shown as lines between actors and use cases]

A use case diagram shows the scope of a system by identifying the actors who interact with it and the goals they pursue. Let me define the key elements.

An actor is anything outside the system boundary that interacts with the system — a person, another system, or a device. Actors initiate use cases or receive results from them. In the library system, the Library Member and the Librarian are actors.

A use case is a named, discrete goal that an actor pursues through interaction with the system. It is always described from the actor's perspective and in the actor's language. Use cases are shown as ellipses inside the system boundary rectangle.

The system boundary — the rectangle — separates what is inside the system from what is outside. Everything inside the rectangle is something the system will do. Everything outside is part of the environment.

Associations — solid lines between actors and use cases — show which actor participates in which use case.

Now let me cover the two most tested use case relationships: include and extend.

[SHOW DIAGRAM: Two mini-diagrams side by side. Left: "Process Order" use case with a dashed arrow labeled "include" pointing to "Validate Payment." Right: "Process Return" use case with a dashed arrow labeled "extend" pointing to "Apply Restocking Fee," with a condition note "if item is open-box"]

The include relationship: a solid arrowhead dashed line from the base use case to the included use case, labeled with the stereotype. Include means the included use case is always executed as a mandatory part of the base use case. "Process Order" always includes "Validate Payment" — every single time.

The extend relationship: a solid arrowhead dashed line from the extending use case to the base use case, labeled with the stereotype, often with a condition note. Extend means the extending use case is optional — it runs only when a specific condition is true. "Apply Restocking Fee" extends "Process Return" only when the returned item is open-box.

> IIBA ECBA Exam Tip: Include = always mandatory. Extend = optional, condition-based. This distinction is tested directly. A common trap answer will reverse them — always verify the direction of the arrow and the purpose of each relationship.

---

## Section 3: Use Case Specifications [10:00 - 14:30]

A use case diagram alone is not enough. Each use case also needs a written use case specification that documents the details.

[SHOW DIAGRAM: Use case specification template — rows labeled: Use Case Name, Use Case ID, Actor(s), Preconditions, Main Success Scenario (numbered steps), Alternate Flows, Exception Flows, Postconditions]

The key elements of a use case specification are:

Preconditions: what must be true before the use case can begin. For "Borrow Book," the precondition might be that the member's account is in good standing and the book is available.

Main Success Scenario: the step-by-step sequence describing how the use case executes when everything goes as expected. Number each step. Write from the actor's perspective alternating with the system's response.

Alternate Flows: valid variations from the main path. For "Borrow Book," an alternate flow might be that the member wants to place a hold on a book that is currently checked out.

Exception Flows: failure paths. For "Borrow Book," an exception might occur if the member has an outstanding fine above the threshold.

Postconditions: what is true after the use case completes. The book is checked out to the member's account; the due date is set.

---

## Section 4: User Stories and the INVEST Criteria [14:30 - 19:00]

[SHOW DIAGRAM: User story template card — large card showing three sections: "As a [role]" at top, "I want [goal]" in middle, "so that [value]" at bottom; smaller section below: "Acceptance Criteria: Given / When / Then"]

A user story is a brief, informal description of a system feature written from the perspective of the person who wants it. The standard format is: "As a [role], I want [goal] so that [value]."

Example: "As a registered customer, I want to reset my password via email so that I can regain access to my account without calling customer support."

User stories are intentionally lightweight — they capture the "who, what, and why" without prescribing implementation. The details live in the acceptance criteria, which are the verifiable conditions the product owner will check when deciding whether to accept the story as complete.

Acceptance criteria are commonly written in Given/When/Then format: "Given the customer is on the login page and has clicked Forgot Password, when they enter their registered email address and click Submit, then they receive a reset link within 60 seconds."

The INVEST criteria are the quality standards for user stories.

[SHOW DIAGRAM: INVEST acronym table — six rows: Independent, Negotiable, Valuable, Estimable, Small, Testable — each with a one-sentence definition]

Independent: the story can be developed and delivered without depending on another story.
Negotiable: the details are open to discussion — it is not a fixed contract.
Valuable: it delivers clear value to the user or business.
Estimable: the team has enough information to estimate the effort required.
Small: it can be completed within a single sprint (typically 1–2 weeks).
Testable: acceptance criteria can be written that confirm whether it is done.

> IIBA ECBA Exam Tip: The most commonly tested INVEST violation on the exam is the Small criterion. A user story that lists 5 or 6 different features is an epic — it must be broken into smaller, sprint-sized stories. Look for stories that use the word "and" multiple times to bundle features.

---

## Section 5: Lab Preview and Closing [19:00 - 22:00]

This week's lab is a hands-on use case modeling exercise. You will draw a use case diagram for a provided scenario, write a complete use case specification, and write three user stories with acceptance criteria. Make sure you understand include vs. extend before attempting the diagram.

Three exam reminders. First: include = mandatory, always executed; extend = optional, condition-based. Second: user stories follow the "As a, I want, so that" format. Third: INVEST violations — especially "not small enough" — are commonly tested.

Visit iiba.org for the ECBA exam blueprint and BABOK Guide v3 KA 5 for the formal requirements modeling techniques.

---

## End Card

## Module 05 Complete

Next: Module 06 - Data Flow Diagrams and Entity-Relationship Diagrams

### Additional Resources

- iiba.org — BABOK Guide v3 KA 5: Use Cases and User Stories techniques
- iiba.org — ECBA exam blueprint weighting information

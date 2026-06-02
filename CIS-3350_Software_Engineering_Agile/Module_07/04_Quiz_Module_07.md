# Quiz: Module 07 – User Stories and Acceptance Criteria

**Course:** CIS-3350 Software Engineering and Agile
**Certification Alignment:** PSM I (Professional Scrum Master I) – Scrum.org
**Instructor:** Professor Nash | Texas Wesleyan University
**Total Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

Which of the following is the correct format for a user story?

- A) The system shall allow users to reset their password via email
- B) As a registered user, I can reset my password so that I can regain account access when I forget my credentials
- C) Reset password feature — high priority, due Sprint 4
- D) User password reset: CRUD operations for the auth service

Correct Answer: B — The correct format is "As a [user type], I can [action] so that [benefit]." It identifies the user, the capability, and the value delivered.

Distractor Analysis:

- Why A is incorrect: This is system-specification language ("the system shall"), not a user story. It lacks a user perspective and a benefit statement.
- Why C is incorrect: This is a task title or backlog item label, not a user story. It has no format, no user, no action, and no benefit.
- Why D is incorrect: This is a technical description of implementation work, not a user story written from the user's perspective.

---

## Question 2

In Ron Jeffries' Three Cs model, what does "Confirmation" represent?

- A) The Product Owner's signature approving the story for development
- B) The acceptance criteria that define when the story is Done
- C) The Scrum Master's confirmation that the story meets INVEST criteria
- D) The stakeholder's verbal agreement that the story is needed

Correct Answer: B — "Confirmation" is the acceptance criteria — the written record of what Done means for the story, converted from the Conversation between the team and Product Owner.

Distractor Analysis:

- Why A is incorrect: The Scrum Guide does not require Product Owner sign-off on individual stories before development; stories enter Sprints through Sprint Planning.
- Why C is incorrect: INVEST criteria evaluation is a refinement quality tool, not the definition of Confirmation in the Three Cs model.
- Why D is incorrect: Verbal agreement during refinement is the "Conversation" C, not the "Confirmation" C.

---

## Question 3

Which of the following is the best example of an acceptance criterion written in Given/When/Then format?

- A) The login button must be blue with a 14px font and rounded corners
- B) Users should be able to log in easily and quickly
- C) Given a registered user is on the login page, When they enter valid credentials and click Submit, Then they are redirected to the dashboard within two seconds
- D) The authentication service must implement JWT tokens and refresh logic

Correct Answer: C — This criterion uses the correct Given/When/Then structure, describes observable behavior, and is specific and testable.

Distractor Analysis:

- Why A is incorrect: This is a UI design specification, not a behavioral acceptance criterion. It describes visual appearance, not user-observable behavior.
- Why B is incorrect: "Easily and quickly" are subjective and untestable. A good acceptance criterion must be specific enough to write a test against.
- Why D is incorrect: This is a technical implementation decision, not a user-facing acceptance criterion.

---

## Question 4

What is the key difference between acceptance criteria and the Definition of Done?

- A) Acceptance criteria are written by Developers; the Definition of Done is written by the Product Owner
- B) Acceptance criteria are specific to one Product Backlog item; the Definition of Done applies to every Increment
- C) Acceptance criteria are optional in Scrum; the Definition of Done is mandatory
- D) Acceptance criteria cover functional requirements; the Definition of Done covers non-functional requirements

Correct Answer: B — Acceptance criteria define Done for a specific user story. The Definition of Done is a quality standard that every Increment must meet regardless of which stories it contains.

Distractor Analysis:

- Why A is incorrect: Acceptance criteria are developed collaboratively by the Product Owner and Developers; the DoD is primarily owned by the Developers with Scrum Team input.
- Why C is incorrect: While the Scrum Guide does not mandate a specific format for acceptance criteria, stories without them lack the "Confirmation" needed for a clear Done state.
- Why D is incorrect: The DoD can include both functional quality criteria (e.g., all acceptance criteria met) and non-functional criteria (e.g., code reviewed, tested). The distinction is scope (item vs. all Increments), not functional vs. non-functional.

---

## Question 5

A user story reads: "As a user, I can manage my account." Why is this problematic?

- A) It uses the word "manage," which is not permitted in Scrum user stories
- B) It is too large (an epic) to complete in one Sprint and needs to be decomposed
- C) It does not specify the user type precisely enough
- D) It is missing the user's name as a required field

Correct Answer: B — "Manage my account" encompasses profile editing, password changes, payment methods, notification preferences, and more — potentially months of work. This is an epic that must be decomposed into Sprint-sized stories.

Distractor Analysis:

- Why A is incorrect: There is no vocabulary restriction on user story language.
- Why C is incorrect: While "user" is generic, the primary problem here is the story's size, not the user type specificity.
- Why D is incorrect: User stories do not include the user's personal name; they identify a user type or role.

---

## Question 6

Does the Scrum Guide require Product Backlog items to be written as user stories?

- A) Yes — the Scrum Guide mandates the "As a / I can / so that" format for all PBIs
- B) Yes — user stories are required, but the format is flexible
- C) No — the Scrum Guide does not prescribe how Product Backlog items are written; user stories are a common practice, not a Scrum rule
- D) No — the Scrum Guide prohibits user stories and requires formal use case specifications instead

Correct Answer: C — The Scrum Guide makes no prescription about the format of Product Backlog items. User stories are a widely adopted practice from the XP community, but they are not a Scrum requirement.

Distractor Analysis:

- Why A is incorrect: The Scrum Guide does not mandate any specific format for PBIs.
- Why B is incorrect: The Scrum Guide does not mandate user stories at all, flexible format or otherwise.
- Why D is incorrect: The Scrum Guide neither prohibits user stories nor requires use cases.

---

## Question 7

What is a "task" in the context of Scrum, and where does it live?

- A) A task is a user story with fewer than 3 story points; it lives in the Product Backlog
- B) A task is a specific technical activity created by Developers to implement a story; it lives in the Sprint Backlog
- C) A task is a stakeholder request added to the backlog outside of Sprint Planning
- D) A task is any item assigned to a specific Developer by the Scrum Master

Correct Answer: B — Tasks are the implementation-level activities that Developers create during Sprint Planning to plan how they will complete a user story. They belong in the Sprint Backlog and are created and owned by the Developers.

Distractor Analysis:

- Why A is incorrect: Story point size does not determine whether something is a task; tasks are implementation activities, not smaller versions of user stories.
- Why C is incorrect: Stakeholder requests enter the Product Backlog through the Product Owner, not as tasks; tasks are plan-level items within the Sprint.
- Why D is incorrect: The Scrum Master does not assign tasks to individuals; Developers self-manage and self-assign work.

---

## Question 8

Which story-splitting pattern is being used when an epic about "managing customer orders" is split into separate stories for creating an order, viewing order history, cancelling an order, and updating a shipping address?

- A) Split by user type
- B) Split by workflow step
- C) Split by CRUD operations
- D) Split by happy path vs. edge cases

Correct Answer: C — Create, Read/View, Cancel (Delete), and Update are the classic CRUD operations. Splitting an epic into Create, Read, Update, and Delete stories is the CRUD splitting pattern.

Distractor Analysis:

- Why A is incorrect: All four stories involve the same user type (the customer); no user type distinction is being made.
- Why B is incorrect: Workflow step splitting divides a sequential process (e.g., browse → select → add to cart → checkout); these stories are distinct operations on the same object, not sequential steps.
- Why D is incorrect: Happy path vs. edge case splitting separates the main success scenario from error/exception handling; these four stories are not that pattern.

---

## Question 9

A user story reads: "As a customer, I can filter search results by price range so that I can find products within my budget without scrolling through irrelevant results." A Developer proposes writing the acceptance criteria as: "The filter UI component uses a dual-handle range slider with 16px handle size and a blue color scheme." What is wrong with this acceptance criterion?

- A) It is written in Given/When/Then format, which is not compatible with this story
- B) It describes a UI implementation detail rather than a user-observable behavior, making it a design specification rather than an acceptance criterion
- C) It does not include a "so that" clause
- D) Acceptance criteria must be written by the Product Owner, not by Developers

Correct Answer: B — Acceptance criteria should describe what the user experiences and whether the feature works correctly, not how the UI is implemented. UI design specifics belong in a design specification or wireframe, not in acceptance criteria.

Distractor Analysis:

- Why A is incorrect: Given/When/Then format is compatible with any story; this criterion simply is not written in any behavioral format at all.
- Why C is incorrect: Acceptance criteria do not require a "so that" clause; that belongs in the user story itself.
- Why D is incorrect: Acceptance criteria are developed collaboratively by the Product Owner and Developers; either party can draft them.

---

## Question 10

Which of the following best illustrates the "Conversation" component of the Three Cs model?

- A) The Product Owner writes a detailed user story on a sticky note and posts it to the Sprint Backlog
- B) The Product Owner and Developers discuss a story during refinement to clarify edge cases, dependencies, and constraints
- C) The Scrum Master reads the user stories aloud at Sprint Planning for the team to estimate
- D) A stakeholder emails a list of features to the Product Owner for the next Sprint

Correct Answer: B — The "Conversation" is the collaborative discussion that fills in the details of a user story beyond what the Card captures. This discussion happens during refinement and Sprint Planning and produces the understanding that the Confirmation (acceptance criteria) records.

Distractor Analysis:

- Why A is incorrect: Writing the story is the "Card" C — the written representation of the need.
- Why C is incorrect: Reading stories aloud for estimation is part of Sprint Planning, not the rich Conversation that a story is meant to prompt during refinement.
- Why D is incorrect: A stakeholder email is an input to the Product Owner's backlog management process, not the team's Conversation about a specific story.

---

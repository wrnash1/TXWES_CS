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

### Question 11 (5 points)

A user story reads: "As a registered customer, I can view my order history so that I can track my purchases and request returns on recent orders." Which INVEST criterion does this story most clearly satisfy that makes it superior to a system-specification requirement?

- A) Independent — it has no dependencies on other stories
- B) Valuable — it expresses a clear user benefit in the "so that" clause
- C) Estimable — the team can immediately size it without further discussion
- D) Small — it can definitely be completed within a two-week Sprint

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Independence cannot be confirmed without knowing the rest of the backlog; the story may depend on an authentication story.
  - C) Incorrect — Estimability depends on the team's knowledge of the current system; a "so that" clause does not guarantee estimability.
  - D) Incorrect — The story may be too large if "order history" includes pagination, filtering, and return requests; the "so that" clause is the clearest improvement over a spec requirement.

---

### Question 12 (5 points)

Which of the following is the best Given/When/Then acceptance criterion for the story "As a user, I can log out so that my session ends securely"?

- A) "The logout button must be in the top-right corner of the navigation bar."
- B) "Given a logged-in user is on any page, When they click 'Log Out,' Then their session token is invalidated and they are redirected to the login page."
- C) "The system should implement a session timeout after 30 minutes of inactivity."
- D) "Users should not be able to access protected pages after logging out."

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Button placement is a design specification, not a behavioral acceptance criterion.
  - C) Incorrect — Session timeout is a separate functional requirement, not an acceptance criterion for the logout story; it also lacks Given/When/Then structure.
  - D) Incorrect — This describes a desired outcome vaguely but lacks the Given/When/Then structure, making it untestable as written.

---

### Question 13 (5 points)

An epic reads: "As a user, I can manage all my preferences." A developer proposes splitting it into: notification preferences, privacy settings, language/locale settings, and display theme. Which splitting pattern is being used?

- A) Split by user type
- B) Split by CRUD operations
- C) Split by data type or feature category
- D) Split by happy path vs. edge cases

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Incorrect — All stories involve the same user type; no differentiation by persona is happening.
  - B) Incorrect — CRUD splitting would produce Create/Read/Update/Delete stories for the same object; these are four different preference categories.
  - D) Incorrect — Happy path vs. edge case splitting separates success scenarios from error handling; these are different feature areas, not scenarios.

---

### Question 14 (5 points)

Why is the "so that" clause of a user story considered the most important component from a Product Owner's perspective?

- A) It satisfies the Scrum Guide's documentation requirements
- B) It enables the Product Owner to evaluate the story's value and make ordering decisions based on the benefit, not just the feature
- C) It makes the story shorter and easier to read on index cards
- D) It ensures the story passes the "Valuable" INVEST criterion automatically

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — The Scrum Guide does not mandate user story format or specific clauses; this is not a documentation compliance matter.
  - C) Incorrect — The "so that" clause adds words, not removes them; brevity is not its purpose.
  - D) Incorrect — Having a "so that" clause is necessary but not sufficient for "Valuable"; the value stated must be real and meaningful, not just present.

---

### Question 15 (5 points)

A Developer completes a user story: all acceptance criteria are met, but the code was not reviewed by another team member, which the Definition of Done requires. Is the story Done?

- A) Yes — meeting acceptance criteria means the story is Done
- B) No — a story must meet both its acceptance criteria AND the Definition of Done to be considered Done
- C) Yes — the Definition of Done is optional for high-priority stories
- D) No — but the Product Owner can waive the code review requirement for this Sprint

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Acceptance criteria are item-specific; the Definition of Done applies universally to every Increment and cannot be bypassed by meeting acceptance criteria alone.
  - C) Incorrect — The Definition of Done is never optional; its entire purpose is to create a non-negotiable quality standard.
  - D) Incorrect — The Product Owner cannot waive the Definition of Done; it is a Scrum Team commitment, and bypassing it would undermine transparency.

---

### Question 16 (5 points)

A Product Manager wants to add a Product Backlog item written as: "Implement Redis caching on the product catalog API to reduce response times below 200ms." Is this a well-formed user story?

- A) Yes — it is specific, technical, and estimable
- B) No — it is written as a system/technical specification rather than from a user's perspective with a stated benefit
- C) Yes — technical stories are valid user stories when written by the development team
- D) No — the Scrum Guide prohibits technical items in the Product Backlog

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — Being specific and technical does not make it a user story; it lacks a user perspective and a user-facing benefit.
  - C) Incorrect — Technical items may belong in the backlog, but they are better written with a user benefit (e.g., "so that page load times are fast enough for mobile users") rather than as pure technical specifications.
  - D) Incorrect — The Scrum Guide does not prohibit technical items; the issue is the story format, not the content type.

---

### Question 17 (5 points)

Which of the following acceptance criteria best covers an "edge case" for the story "As a user, I can search for products"?

- A) "Given a user enters a valid product name, When they submit the search, Then matching products appear within 500 ms."
- B) "Given a user submits a search with no text entered, When the form is submitted, Then an error message prompts them to enter at least one character."
- C) "The search bar must be displayed prominently on the home page."
- D) "The search index must be rebuilt nightly to reflect new inventory."

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — This is the happy path (valid input, expected result), not an edge case.
  - C) Incorrect — This is a UI design requirement, not an acceptance criterion in Given/When/Then format.
  - D) Incorrect — Index rebuilding is a technical implementation detail, not a user-observable acceptance criterion.

---

### Question 18 (5 points)

Where do tasks created during Sprint Planning live?

- A) In the Product Backlog, below the selected user stories
- B) In the Sprint Backlog, owned by the Developers
- C) In a separate task management system maintained by the Scrum Master
- D) In the Definition of Done as implementation requirements

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Incorrect — The Product Backlog contains user-facing items and epics; tasks are implementation-level and belong in the Sprint Backlog.
  - C) Incorrect — There is no separate task system prescribed by Scrum; all Sprint work is tracked in the Sprint Backlog.
  - D) Incorrect — The Definition of Done defines quality standards, not individual implementation tasks.

---

### Question 19 (5 points)

The story "As a user, I can do everything the old system did" fails which INVEST criteria most severely?

- A) Negotiable — because it copies the old system exactly without room for improvement
- B) Independent — because it depends on the old system's complete feature list
- C) Small and Testable — because its scope is undefined and there are no testable boundaries
- D) Valuable — because copying an old system is inherently low-value

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Incorrect — Negotiability concerns whether implementation approach is flexible; the primary failure here is scope and testability.
  - B) Incorrect — Independence concerns dependencies between backlog items; the story could theoretically stand alone even if it is too large.
  - D) Incorrect — Migrating an old system's features may be high-value; the problem is not the value, but the inability to define or test "everything the old system did."

---

### Question 20 (5 points)

A user story passes all INVEST criteria but has no acceptance criteria written. What problem does this create at Sprint Review?

- A) The story cannot be estimated at Sprint Planning
- B) The story cannot be demonstrated because there is nothing to show
- C) The team has no shared, testable definition of Done for this specific story, leading to potential disagreement about whether it is complete
- D) The Scrum Master must refuse to allow it into the Sprint Backlog

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Incorrect — Estimation depends on the Developers' understanding of the work, not on the existence of written acceptance criteria.
  - B) Incorrect — A working feature can be demonstrated even without written acceptance criteria; the problem is agreement on completeness, not demonstration ability.
  - D) Incorrect — The Scrum Master does not control Sprint Backlog entry; Developers select items during Sprint Planning. The Scrum Master may coach on quality but does not refuse items.

# Quiz: Module 08 — Use Case and User Story Development

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 1

A business analyst is modeling a banking system. The use case "Transfer Funds" always
requires the user to be authenticated before proceeding. The BA wants to factor the
authentication logic into a shared use case. Which relationship should be used, and what
is the correct direction of the arrow?

A. Extend — dashed arrow from Transfer Funds to Authenticate User

B. Include — dashed arrow from Transfer Funds to Authenticate User

C. Include — dashed arrow from Authenticate User to Transfer Funds

D. Generalization — solid inheritance arrow from Authenticate User to Transfer Funds

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because extend is conditional; authentication must always occur, making
  include the right relationship.
- C is incorrect because the include arrow points FROM the base use case TO the included
  use case, not the reverse.
- D is incorrect because generalization applies to actors or specialization of use case
  behavior, not mandatory reuse of a shared subprocess.

---

### Question 2

In a use case diagram for an online shopping system, the use case "Apply Discount Code"
only executes when a customer enters a valid promo code during checkout. "Apply Discount
Code" should be modeled using which relationship to "Complete Purchase"?

A. Include, because the behavior is triggered from within the base use case

B. Generalization, because "Apply Discount Code" is a specialized version of "Complete Purchase"

C. Association, because both use cases involve the Customer actor

D. Extend, because "Apply Discount Code" inserts optional behavior into "Complete Purchase"
   only when a condition is met

**Correct Answer: D**

**Distractor Analysis:**

- A is incorrect because include implies mandatory execution, but discount code entry is
  optional and conditional.
- B is incorrect because generalization models inheritance between actors or use case
  hierarchies, not conditional behavior.
- C is incorrect because association lines connect actors to use cases, not use cases to
  each other.

---

### Question 3

Which of the following best describes the purpose of the system boundary in a use case
diagram?

A. It separates primary actors from secondary actors

B. It defines which use cases are in scope for the system being built and which are external

C. It indicates the priority order in which use cases will be implemented

D. It groups use cases by the actor that initiates them

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because actor placement relative to the boundary indicates inside/outside
  the system, but the boundary itself does not categorize actors by type.
- C is incorrect because priority is a backlog or project management concern, not a
  function of the system boundary notation.
- D is incorrect because use cases are grouped inside the boundary by scope, not by actor
  ownership.

---

### Question 4

A user story reads: "As a customer, I want the system to be fast." A teammate says this
story fails the INVEST criteria. Which specific criterion does it fail, and why?

A. Independent — the story depends on infrastructure decisions outside the team's control

B. Valuable — system performance does not deliver direct business value to the customer

C. Testable — "fast" is not a measurable condition and cannot be verified by acceptance
   criteria without a specific threshold

D. Small — performance improvements require too many development tasks to fit in one sprint

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect because while infrastructure may be involved, the primary failure is the
  inability to write a pass/fail test without knowing what "fast" means numerically.
- B is incorrect because performance does deliver value; the story fails on testability, not
  value.
- D is incorrect because the story is arguably too vague to estimate at all; its primary
  problem is that it lacks a testable definition.

---

### Question 5

A business analyst writes: "As a librarian, I want to generate an overdue items report,
so that I can contact members who have not returned materials." This story satisfies which
component of the INVEST model that is most often omitted from poorly written stories?

A. Independent — the story can be developed without dependencies on other stories

B. Negotiable — the format of the report is open for discussion

C. Valuable — the "so that" clause explicitly states the business value driving the need

D. Estimable — the story is specific enough for the team to estimate effort

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect because independence is about story-to-story sequencing dependencies, not
  about what the story itself contains.
- B is incorrect because negotiability is a team behavior, not a textual element of the
  story.
- D is incorrect because estimability is about sizing the work; the "so that" clause does
  not primarily address estimation.

---

### Question 6

In a fully dressed use case specification, Extensions are numbered using a step-letter
convention. Which of the following correctly represents an alternate flow that branches from
Step 4 of the main success scenario as the second alternate at that step?

A. 4-b

B. Extension 4.2

C. 4b

D. Alt-4b

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect because hyphens are not used in the standard Cockburn/UML extension
  numbering convention.
- B is incorrect because the period-number format (4.2) is used for sub-steps within an
  extension, not for a second alternate at the same parent step.
- D is incorrect because "Alt-" is not a standard use case notation prefix.

---

### Question 7

A BA is reviewing a story map created by the project team. The top row lists: Register,
Search, Borrow, Return, Renew, Manage Account. The first horizontal slice below that row
is labeled "MVP." What does this top row represent?

A. The acceptance criteria for the MVP release

B. The product backlog items prioritized for the first sprint

C. The backbone — the high-level user activities that form the user journey from left to right

D. The Definition of Done applied across all user stories

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect because acceptance criteria are written at the individual story level
  below the backbone, not in the top row.
- B is incorrect because the top row represents activities, not individual sprint-ready
  stories; those appear in the rows below.
- D is incorrect because the Definition of Done is a team quality agreement, not a
  structural element of a story map.

---

### Question 8

Which of the following is the correct UML notation for an include relationship in a use
case diagram?

A. A solid line with a filled triangle arrowhead pointing from the base use case to the
   included use case

B. A dashed arrow with the stereotype label include pointing from the base use case to the
   included use case

C. A dashed arrow with the stereotype label include pointing from the included use case to
   the base use case

D. A solid line with an open arrowhead and no label between the two use cases

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because a solid filled-triangle arrow represents UML generalization
  (inheritance), not include.
- C is incorrect because the include arrow points FROM the base use case TO the included
  use case, not the reverse.
- D is incorrect because unlabeled solid association lines connect actors to use cases;
  inter-use-case relationships require dashed arrows with stereotypes.

---

### Question 9

A development team receives this acceptance criterion: "The system shall update the
loans table in the database and set the status field to RETURNED when a return is
processed." A senior BA flags this criterion as poorly written. What is the primary
problem?

A. It uses the Given-When-Then format incorrectly

B. It describes an internal implementation detail rather than an observable user outcome

C. It is too short to be a valid acceptance criterion

D. It fails the Valuable criterion of INVEST

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because the criterion does not attempt Given-When-Then at all; the problem
  is content, not format.
- C is incorrect because length is not the issue; acceptance criteria can be brief and valid
  as long as they describe observable outcomes.
- D is incorrect because INVEST applies to user stories, not to acceptance criteria
  individually.

---

### Question 10

According to use case theory, a secondary actor is best defined as which of the following?

A. An actor who has fewer permissions than the primary actor in the system

B. An actor who uses the system less frequently than the primary actor

C. An actor who is called upon by the system or primary actor to help complete a use case,
   rather than initiating the use case themselves

D. An actor who is not yet defined and will be identified in a later analysis phase

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect because secondary actor status is defined by interaction pattern, not by
  authorization level or permissions.
- B is incorrect because frequency of use is not the defining distinction; a batch job that
  runs nightly is secondary despite running repeatedly.
- D is incorrect because an undefined actor is simply a gap in the model; "secondary"
  is a defined role, not a placeholder.

---

*Quiz — Module 08 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

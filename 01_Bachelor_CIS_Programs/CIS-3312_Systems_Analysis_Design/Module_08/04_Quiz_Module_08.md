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

---

### Question 11

A BA writes the following user story: "As a library member, I want to place a hold on a checked-out book, so that I am notified when it becomes available." The product owner asks the BA to verify it passes INVEST. Which criterion is most at risk if no acceptance criteria are written for this story?

A. Independent — the story may depend on the notification system being built first

B. Negotiable — the team might implement SMS notifications when email was expected

C. Testable — without acceptance criteria specifying what "notified" means and under what conditions, the story cannot be verified

D. Small — the story bundles hold placement and notification into one story that might span two sprints

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect because dependency on the notification system is an integration concern, not a Testable criterion failure. The primary question is whether the story as written can be tested.
- B is incorrect because negotiability is about the implementation being open for discussion; the risk here is that the result cannot be verified, not that it cannot be discussed.
- D is incorrect because the story describes two closely related behaviors (place hold, receive notification) that together form a single coherent user goal — this is appropriately scoped for one story.

---

### Question 12

A use case specification for "Check Out Book" has the following postcondition in the main success scenario: "The item's status in the catalog is set to CHECKED_OUT and the member's account reflects the loan due date." A reviewer flags this postcondition as too implementation-specific. What is the better way to write it?

A. Remove the postcondition entirely — postconditions are optional elements in a use case specification

B. Rewrite it to describe the observable state from the user's perspective: "The member receives a checkout confirmation showing the item title and due date; the item is no longer available for other members to borrow."

C. Move the postcondition to the precondition section, since it describes what must be true before the use case can end

D. Replace the postcondition with an acceptance criterion in Given-When-Then format

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because postconditions are a required element of a fully dressed use case specification; they document the system state after successful execution.
- C is incorrect because a postcondition describes the state after the use case completes; moving it to preconditions reverses its logical placement.
- D is incorrect because acceptance criteria belong to user stories, not to use case specifications; the correct fix is to rewrite the postcondition in observable-outcome terms.

---

### Question 13

A story map's backbone row contains: "Browse Catalog → Search → Place Hold → Check Out → Manage Account." A team member asks whether "Manage Account" should be split into separate activities because it covers profile editing, password reset, and notification preferences. What is the correct answer?

A. No — the backbone should always be kept as brief as possible with no more than five activities

B. Yes — if "Manage Account" covers multiple distinct user goals that require different user journeys, it should be split into separate backbone activities for clarity

C. No — backbone activities are epics by definition and cannot be split

D. Yes — splitting the backbone at this stage requires restarting the sprint planning process

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because the five-activity limit is not a rule; backbone length should reflect the actual user journey, which may have more or fewer activities depending on system complexity.
- C is incorrect because backbone activities are high-level user activities, not epics; they organize the map but are not the same as INVEST epics that must be decomposed into stories.
- D is incorrect because backbone refinement is part of normal story mapping and does not restart sprint planning; it clarifies the map before sprint stories are assigned.

---

### Question 14

According to the Cockburn use case specification format, what is the correct definition of a "trigger" in a use case?

A. The technical event that causes the database to update when the use case completes

B. The condition or event that causes an actor to initiate the use case

C. The error condition that sends the use case to an exception flow

D. The system notification sent to secondary actors after the use case succeeds

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because a database update is a step within the main success scenario, not the trigger that starts the use case.
- C is incorrect because error conditions that redirect to exception flows are extension conditions, not triggers.
- D is incorrect because post-success notifications are postconditions or steps in the success scenario, not the trigger.

---

### Question 15

A BA is reviewing a product backlog before sprint planning. One item reads: "Complete the checkout module." Why is this a poorly written backlog item?

A. It uses a verb, which is not allowed in user story titles

B. It does not follow the As a / I want / so that format, does not identify who benefits, and is too broad to estimate or test

C. It is too short — backlog items must be at least two sentences

D. It should use Given-When-Then format to be valid as a backlog item

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because user stories routinely begin with verbs in the "I want to..." portion; using verbs is correct. The issue is with the structural format and scope.
- C is incorrect because length is not the criterion for a valid backlog item; clarity, specificity, and testability are.
- D is incorrect because Given-When-Then is the format for acceptance criteria, not for the user story or backlog item itself.

---

### Question 16

A BA is creating a use case diagram for a university registration system. The BA places "Academic Advisor" inside the system boundary as a use case rather than outside as an actor. What is the error and what is the correct placement?

A. No error — advisors interact with the system and can be modeled as use cases

B. Error — Academic Advisor is a role that interacts with the system and must be placed outside the system boundary as an actor

C. Error — Academic Advisor should be placed inside the boundary as a data store

D. Error — only automated system actors may be placed outside the boundary; human roles belong inside

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because actors and use cases serve different modeling purposes; actors are roles that interact with the system, not system behaviors.
- C is incorrect because data stores are a DFD concept; use case diagrams do not contain data stores.
- D is incorrect because both human and system actors are placed outside the system boundary in a use case diagram; only the system's own use cases (behaviors) are inside the boundary.

---

### Question 17

Which of the following correctly identifies the difference between a "walking skeleton" and an "MVP" in story mapping?

A. A walking skeleton includes all features from all releases; an MVP is the minimum viable version of the walking skeleton

B. A walking skeleton is the thinnest possible end-to-end implementation that demonstrates the architecture works; an MVP is the minimum feature set that delivers value to real users

C. Walking skeleton and MVP are synonyms used interchangeably in story mapping

D. An MVP is created first, then expanded into a walking skeleton during subsequent sprints

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because a walking skeleton does not include all features; it is the minimum technical implementation that proves end-to-end connectivity.
- C is incorrect because while sometimes conflated, they have distinct definitions: a walking skeleton is an architectural validation slice; an MVP is a user-value delivery slice.
- D is incorrect because a walking skeleton is often developed before or alongside the MVP to validate technical architecture; they are not sequentially dependent in the described way.

---

### Question 18

A BA adds the following extension to a use case: "3a. If the member's account has an overdue fine exceeding $25: 3a1. The system displays a payment required message. 3a2. The use case ends." What type of flow is this, and what does "the use case ends" signify?

A. Alternate flow — the use case ends because the goal is achieved through a different path

B. Exception flow — the use case ends because an error or blocking condition prevents the goal from being achieved

C. Include relationship — the use case ends because it has called the Collect Fine use case

D. Postcondition — the system records that the checkout was blocked due to fines

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because an alternate flow still achieves the goal through a different valid path; here, the goal (checkout) is blocked entirely — no book is checked out.
- C is incorrect because an include relationship is shown in the diagram as a separate structural connection; it is not written as a numbered extension in the specification.
- D is incorrect because a postcondition describes the state after the use case completes successfully; this extension describes a failure condition that prevents completion.

---

### Question 19

A team is writing user stories for a new online retail system. One story reads: "As a customer, I want to browse products, add items to cart, apply coupons, enter shipping information, choose a payment method, confirm my order, and receive a confirmation email." Which INVEST criterion does this story most clearly violate?

A. Negotiable — too many implementation decisions are locked in

B. Independent — the story has dependencies on multiple other system components

C. Small — the story bundles multiple distinct user goals that would span several sprints

D. Valuable — it is unclear which part of the story delivers direct business value

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect because negotiability is about flexibility in implementation approach, not about the number of features bundled into one story.
- B is incorrect because dependency on other components may exist but is not the primary criterion failure; the story fails Small most clearly.
- D is incorrect because the story does describe clear user value (completing a purchase); the problem is its size.

---

### Question 20

A BA is facilitating a requirements session and a developer says: "I can just look at the old system's code and reverse-engineer the requirements — we don't need to interview users." What is the most significant problem with this approach?

A. The developer does not have permission to access the legacy code without a formal code review

B. Reverse-engineering existing code can only identify what the system currently does, not what users need the new system to do — it cannot surface missing requirements, workarounds, or desired improvements

C. Requirements derived from code analysis are not traceable to business needs and therefore invalid under BABOK

D. The developer's approach is valid but should be supplemented with performance testing before being used

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because code access permissions are a governance concern, not the fundamental analytical problem with the approach.
- C is incorrect because while traceability is important, the more fundamental problem is the gap between current system behavior and desired future-state requirements.
- D is incorrect because performance testing measures non-functional characteristics of the current system; it does not help identify what users need from the new system.

---

*Quiz — Module 08 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

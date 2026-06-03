# Reading Guide: Module 08 — Use Case and User Story Development

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Life Cycle Management

---

### Overview

This reading guide supports Module 08 and covers use case modeling, user story development,
acceptance criteria, and story mapping. These techniques are foundational for both
traditional and Agile requirements practice and appear prominently on the ECBA exam.

---

### Section 1: Use Case Fundamentals

A use case represents a discrete unit of functionality that delivers observable value to an
actor. The three essential components of any use case are the actor who initiates the
interaction, the goal the actor wants to achieve, and the system response that fulfills or
denies that goal.

Use cases were formalized by Ivar Jacobson and incorporated into the Unified Modeling
Language (UML) 1.x specification. They remain one of the most widely used requirements
visualization techniques in business analysis practice.

#### Key Use Case Vocabulary

| Term | Definition |
|---|---|
| Actor | A role played by a person, system, or organization outside the SuD |
| Use Case | An ellipse representing a goal-oriented interaction |
| System Under Discussion (SuD) | The system whose requirements are being modeled |
| System Boundary | The rectangle enclosing all in-scope use cases |
| Association | A solid line connecting an actor to a use case it participates in |
| Primary Actor | The actor who initiates the use case to achieve a personal goal |
| Secondary Actor | An actor called upon to help fulfill the use case |
| Precondition | A state that must be true before the use case can begin |
| Postcondition | A state that is true after the use case completes successfully |

---

### Section 2: Use Case Diagram Notation Reference

The use case diagram is a UML structural diagram that provides a high-level view of system
scope and actor interactions. It does not show sequence, flow, or internal logic — those
details belong in the fully dressed specification.

#### Diagram Elements

```
[Stick Figure]          Actor — a role that interacts with the system
(  Ellipse  )           Use Case — a goal-oriented interaction
[  Rectangle  ]         System Boundary — encloses all in-scope use cases
 --- line ---           Association — connects actor to use case
 - - >  <<include>>     Include relationship — mandatory behavioral reuse
 - - >  <<extend>>      Extend relationship — conditional optional behavior
 -----> (triangle)      Generalization — inheritance between actors or use cases
```

#### Lakewood Library Management System (LMS) — Example Diagram Description

System Boundary Label: Library Management System

Actors (outside boundary):

- Library Patron (primary — left side)
- Librarian (primary — left side)
- System Administrator (primary — right side)
- Email Service (secondary — right side)

Use Cases (inside boundary):

- Search Catalog
- Check Out Book
- Return Book
- Reserve Book
- Manage Member Account
- Generate Overdue Report
- Authenticate Member
- Send Notification

Relationships:

- Library Patron associates with: Search Catalog, Check Out Book, Return Book, Reserve Book
- Librarian associates with: Check Out Book, Return Book, Generate Overdue Report
- System Administrator associates with: Manage Member Account
- Email Service associates with: Send Notification
- Check Out Book --include--> Authenticate Member
- Reserve Book --include--> Authenticate Member
- Apply Late Fee --extend--> Return Book (extension point: book is overdue)
- Send Notification --include--> Check Out Book

---

### Section 3: Include vs. Extend — Critical Distinction

This distinction is one of the most frequently tested topics on the ECBA exam. Master it
with both the definition and a concrete example.

#### Include Relationship

- **Direction**: Base use case --> Included use case
- **Behavior**: The included behavior ALWAYS executes as part of the base use case
- **Purpose**: Factors out common mandatory behavior shared by multiple use cases
- **Arrow label**: double-angle-brackets include double-angle-brackets on the dashed arrow
- **Example**: Check Out Book includes Authenticate Member every time, without exception

#### Extend Relationship

- **Direction**: Extending use case --> Base use case
- **Behavior**: The extending behavior executes ONLY when a specific condition is met
- **Purpose**: Documents optional or exceptional behavior without cluttering the base flow
- **Arrow label**: double-angle-brackets extend double-angle-brackets on the dashed arrow
- **Extension point**: A named location in the base use case where extension can occur
- **Example**: Apply Late Fee extends Return Book only when return date exceeds due date

#### Quick Comparison Table

| Dimension | Include | Extend |
|---|---|---|
| Frequency | Always | Conditionally |
| Arrow direction | Base → Included | Extension → Base |
| Who knows about whom | Base knows about included | Base does NOT know about extension |
| Analogy | Function call | Plugin |
| Trigger | Execution reaches step | Extension point condition is true |

> ECBA Exam Tip: The extend arrow direction is counterintuitive. The arrow points FROM the
> extending use case TO the base use case, because the extension "reaches into" the base.
> Many students get this backwards. Draw it ten times until it is automatic.

---

### Section 4: Fully Dressed Use Case — Field Reference

The fully dressed use case specification provides complete behavioral documentation. The
following table defines each field.

| Field | Description |
|---|---|
| Use Case ID | Unique identifier (e.g., UC-08) |
| Use Case Name | Short verb-noun description (e.g., Check Out Book) |
| Goal in Context | One sentence describing what the primary actor wants to achieve |
| Scope | The system being described (SuD name) |
| Level | User Goal, Summary, or Subfunction |
| Primary Actor | The actor who triggers the use case |
| Stakeholders and Interests | All parties affected and what they need from this interaction |
| Preconditions | States that must be true before execution begins |
| Minimal Guarantees | What the system ensures even if the use case fails |
| Success Guarantees | What the system ensures when the use case succeeds |
| Main Success Scenario | Numbered steps of the happy path |
| Extensions | Alternate flows and exception handling (numbered with letter suffix) |
| Technology Variations | Implementation-independent alternatives at specific steps |

#### Extension Numbering Convention

Extensions are referenced by the step number they branch from, followed by a letter. For
example, Extension 3a branches from Step 3 of the main success scenario. Extension 3b is a
second branch from the same step. Extension 3a.1 is a sub-step within Extension 3a.

---

### Section 5: User Story Format and INVEST Criteria

User stories originated in Extreme Programming (XP) and were popularized by Mike Cohn in
"User Stories Applied" (2004). They are the primary requirements format in Scrum-based
development.

#### Standard User Story Format

```
As a [type of user],
I want [to perform some action or achieve some goal],
so that [I receive some benefit or business value].
```

All three parts are required. The "so that" clause prevents feature requests from losing
their business justification as the story moves through development.

#### INVEST Criteria

| Letter | Criterion | Meaning |
|---|---|---|
| I | Independent | Stories can be developed in any order without dependency |
| N | Negotiable | Details are open for discussion between team and stakeholders |
| V | Valuable | The story delivers perceivable value to the user or business |
| E | Estimable | The team can estimate the effort required to implement it |
| S | Small | The story fits within a single sprint (1–2 weeks of work) |
| T | Testable | Acceptance criteria can verify whether the story is complete |

#### Epic vs. Story vs. Task

- **Epic**: A large user story too big for one sprint; must be split before implementation
- **Story**: A deliverable unit of work completable within a single sprint
- **Task**: A technical sub-step within a story; not directly visible to the stakeholder

> ECBA Exam Tip: The BABOK references user stories in the context of Agile Analysis. Know
> that an Epic must be decomposed before it can be estimated and placed in a sprint. Know
> that INVEST is the quality checklist applied to individual stories.

---

### Section 6: Acceptance Criteria — Given-When-Then Format

Acceptance criteria make user stories testable. Without acceptance criteria, a story cannot
be verified as done. The Given-When-Then (GWT) format provides a structured template.

```
Given [some initial context or precondition],
When  [an action is performed or an event occurs],
Then  [an observable outcome results].
```

#### LMS Acceptance Criteria Examples

For the story "As a Patron, I want to search the catalog by title":

- Given the patron is on the catalog search page, when they enter a title keyword and click
  Search, then the results list displays all matching books sorted by relevance score.
- Given the patron enters a search term with no matches, when they click Search, then the
  system displays "No results found" and suggests alternate search terms.
- Given the patron enters a blank search field, when they click Search, then the system
  displays a validation message requiring at least one character.

Best practice guidelines for acceptance criteria:

- Write 3–8 criteria per story
- Each criterion must be independently verifiable
- Use observable outcomes — not internal system states
- Avoid implementation details (do not specify how, only what)

---

### Section 7: Story Mapping

Story mapping, introduced by Jeff Patton, organizes user stories into a two-dimensional
grid that reveals the full user experience and enables release planning.

#### Story Map Structure

```
BACKBONE (top row) ──────────────────────────────────────────────────────
  [Activity 1]         [Activity 2]         [Activity 3]
─────────────────────────────────────────────────────── WALKING SKELETON
  [Story 1a]           [Story 2a]           [Story 3a]   (MVP Release)
─────────────────────────────────────────────────────── RELEASE 2
  [Story 1b]           [Story 2b]           [Story 3b]
─────────────────────────────────────────────────────── RELEASE 3
  [Story 1c]                                [Story 3c]
```

The backbone lists high-level user activities in temporal order from left to right. Each
column under an activity contains the stories that enable it. Horizontal lines represent
release boundaries — the walking skeleton contains the minimum viable feature set.

#### LMS Story Map Backbone Example

Activities in sequence: Join Library, Browse Catalog, Borrow Materials, Return Materials,
Manage Account.

MVP slice under Borrow Materials: Search catalog, Check item availability, Check out at
desk, Receive due date confirmation.

Release 2 additions: Self-checkout kiosk, Email confirmation, Renew online.

Release 3 additions: Mobile app check-out, Recommendation engine.

---

### Section 8: ECBA Exam Preparation

#### Relevant BABOK Knowledge Areas

- **Knowledge Area 4 — Requirements Analysis and Design Definition**: Use cases, user stories,
  and acceptance criteria are core elicitation and modeling outputs
- **Knowledge Area 3 — Requirements Life Cycle Management**: Tracing requirements back to use
  cases; maintaining use case specifications as requirements evolve
- **Agile Analysis and Design**: User stories, story maps, and acceptance criteria are Agile
  BA deliverables

#### Likely ECBA Question Patterns

Questions will present scenarios and ask you to identify the correct technique or element.

- A BA needs to show optional system behavior that occurs under a specific condition —
  answer: extend relationship
- A BA factors out authentication logic used by five different use cases — answer: include
  relationship
- A team needs to verify whether a story is complete — answer: acceptance criteria
- A BA needs to plan releases while showing the full user journey — answer: story mapping
- A story cannot be completed in one sprint and needs to be broken down — answer: Epic
  decomposition

---

### Study Checklist

Work through each item before attempting the quiz.

- [ ] Can you draw a use case diagram from scratch with all five notation elements?
- [ ] Can you correctly draw an include relationship with the arrow in the right direction?
- [ ] Can you correctly draw an extend relationship with the arrow in the right direction?
- [ ] Can you distinguish primary from secondary actors with an example?
- [ ] Can you write all fields of a fully dressed use case specification?
- [ ] Can you write a user story using the As a / I want / so that format?
- [ ] Can you apply INVEST to evaluate a given user story?
- [ ] Can you write three Given-When-Then acceptance criteria for a story?
- [ ] Can you describe the structure of a story map and what each dimension represents?
- [ ] Can you identify whether a given story is a Story or an Epic?

---

### Key Terms Glossary

| Term | Definition |
|---|---|
| Actor | Role interacting with the system under discussion |
| Association | Line connecting actor to use case |
| Backbone | Top-row activities in a story map showing user journey |
| ECBA | Entry Certificate in Business Analysis — IIBA entry-level credential |
| Epic | User story too large to complete in a single sprint |
| Extend | Optional conditional behavioral addition to a base use case |
| Extension Point | Named location in a base use case where extend can insert behavior |
| Fully Dressed | The most detailed use case specification format |
| Given-When-Then | Acceptance criteria format: context, action, outcome |
| Include | Mandatory behavioral reuse factored out of multiple use cases |
| INVEST | Quality criteria checklist for user stories |
| Primary Actor | Actor who triggers the use case |
| Story Map | Two-dimensional grid organizing stories by user journey and release |
| SuD | System Under Discussion — the system being modeled |
| UML | Unified Modeling Language — standard notation for software models |
| User Story | Short requirement in As a / I want / so that format |
| Walking Skeleton | Minimum viable product slice in a story map |

---

*Reading Guide — Module 08 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

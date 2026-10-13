# Discussion Forum: Module 08 — Use Case and User Story Development

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Forum Instructions

Post an original response to ONE of the three scenarios below (A, B, or C). Your initial
post must be 175–225 words written in complete sentences. After posting your initial
response, reply to at least two classmates whose posts address a different scenario than
yours. Each peer reply must be at least 60 words and must engage substantively with the
classmate's reasoning — not simply agree or restate their point.

**Due dates:** Initial post due by Thursday 11:59 PM. Peer replies due by Sunday 11:59 PM.

---

### Scenario A — The Missing Extend

A junior business analyst on your team has submitted a use case diagram for a university
course registration system. The diagram includes a use case called "Register for Course"
and a separate use case called "Apply Waitlist." The junior BA has drawn the relationship
as an include arrow from "Register for Course" to "Apply Waitlist." During review, you
notice that waitlist processing only occurs when a course section is full — it does not
happen during every registration attempt.

Respond to this scenario: Explain what is wrong with the junior BA's use of the include
relationship in this context, identify the correct relationship that should be used, describe
the correct direction and label of the arrow, and explain why getting this distinction right
matters for downstream development and testing activities.

---

### Sample Response A

The junior business analyst has misapplied the include relationship in this scenario. The
include relationship specifies that the included behavior executes every time the base use
case runs without exception, similar to a mandatory function call in programming. In this
case, however, waitlist processing does not occur on every registration attempt — it only
triggers when a course section has reached its enrollment capacity. Because the behavior is
conditional rather than universal, the correct relationship to use is extend, not include.

The arrow for the extend relationship should point from the extending use case — "Apply
Waitlist" — to the base use case — "Register for Course" — and should be labeled with the
extend stereotype. An extension point should be noted in the base use case specification at
the step where the condition is evaluated. The arrow direction is counterintuitive to many
analysts because it points toward the base, but this makes conceptual sense: the base use
case does not need to know about its extensions, and the extension reaches into the base at
the designated point.

Getting this distinction right matters because developers who read an include relationship
will implement waitlist logic as a required step in every registration transaction, causing
unnecessary processing overhead and potential errors when no waitlist condition exists.
Testers will write test cases that always expect waitlist behavior, producing false failures.
Correct modeling prevents both problems by signaling that conditional logic must be
evaluated at a specific extension point only.

---

### Peer Reply Guidance for Scenario A

When replying to a classmate's Scenario A post, address at least one of the following:
Did they correctly articulate why include was wrong, or did they confuse the definition?
Did they state the correct arrow direction for extend? Would you add anything about how this
modeling error might affect the use case specification rather than just the diagram?

---

### Scenario B — The Vague User Story

A product owner on a software development team proposes the following user story for the
sprint backlog: "As a user, I want a better dashboard, so that I can do my job more
efficiently." The team attempts to estimate the story during sprint planning but cannot
agree on a point value. The Scrum Master asks the BA to evaluate the story using the INVEST
criteria and recommend revisions.

Respond to this scenario: Identify which specific INVEST criteria this story fails and
explain why each failure occurs. Then rewrite the story — or decompose it into two or more
stories — so that the resulting stories satisfy all six INVEST criteria. For at least one
of your revised stories, write two acceptance criteria in Given-When-Then format to
demonstrate that the story is now testable.

---

### Sample Response B

The original story "As a user, I want a better dashboard, so that I can do my job more
efficiently" fails at least four of the six INVEST criteria. First, it fails Estimable
because the team has no shared understanding of what "better" means — they cannot size work
they cannot define. Second, it fails Testable for the same reason — there is no observable
condition that could confirm whether the dashboard is now "better." Third, it fails Small
because an undefined, open-ended improvement to an entire dashboard could encompass weeks of
work. Fourth, it fails Independent because an ambiguous story may secretly depend on
multiple infrastructure or design decisions that have not been made.

A revised decomposition might include: "As a project manager, I want to see my five most
overdue tasks displayed prominently on the dashboard home screen, so that I can triage
critical items without navigating to a separate report." This story passes all six INVEST
criteria. It names a specific actor, a specific feature, and a specific business outcome.

Acceptance criteria for this revised story:

Given the project manager is on the dashboard home screen, when the page loads, then the
five most overdue tasks are displayed in a highlighted panel sorted by days overdue in
descending order.

Given all tasks are on schedule, when the project manager views the dashboard, then the
overdue panel displays the message "No overdue tasks" rather than an empty container.

---

### Peer Reply Guidance for Scenario B

When replying to a classmate's Scenario B post, consider: Did they correctly apply all six
INVEST criteria or did they miss one? Are their revised stories genuinely independent of
each other, or do they create a hidden dependency? Do their Given-When-Then criteria
describe observable outcomes or internal system states?

---

### Scenario C — Story Mapping a Release

A nonprofit organization is building a volunteer scheduling application. The project team
has written forty user stories covering volunteer registration, shift browsing, shift
sign-up, schedule management, notifications, and reporting. The project sponsor wants to
launch a working version in six weeks and needs the team to identify which stories belong
in the first release versus which should be deferred.

Respond to this scenario: Explain how story mapping would help the team make this release
planning decision. Describe the structure of a story map — including the backbone, the
walking skeleton concept, and release slices — and explain what the team would place in the
MVP slice. Discuss one risk of skipping story mapping and going straight to a prioritized
flat backlog for this type of release planning decision.

---

### Sample Response C

Story mapping is ideally suited to this release planning challenge because it organizes
forty stories into a structure that reflects the end-to-end volunteer experience rather than
an arbitrary priority ranking. A flat backlog ranked by business value alone can obscure
whether the MVP slice actually covers an end-to-end workflow or simply delivers a
collection of high-priority features that do not function together as a coherent product.

The story map backbone for this application would list the major volunteer activities in
temporal sequence from left to right: Register as Volunteer, Browse Available Shifts, Sign
Up for Shift, Receive Confirmation, View My Schedule, Get Reminders, Check In. Each column
under an activity contains the stories that support it at various levels of depth and polish.

The walking skeleton — the MVP slice — draws a horizontal line below the single most
essential story in each column. For this application, that means registration must work,
shift browsing must display available slots, sign-up must record the commitment, and the
volunteer must receive some form of confirmation. Advanced features like recurring reminders
and manager reporting would fall in Release 2 and Release 3 rows.

The key risk of skipping story mapping is delivering a technically high-value feature set
that does not support a complete user journey. For example, the team might implement a
sophisticated reporting module — which scores high on stakeholder priority — while omitting
the basic shift confirmation email, leaving volunteers uncertain whether their sign-up was
recorded. Story mapping prevents this by forcing the team to evaluate completeness
horizontally before adding depth vertically.

---

### Peer Reply Guidance for Scenario C

When replying to a classmate's Scenario C post, consider: Did they correctly describe the
backbone as user activities rather than stories? Did they distinguish the walking skeleton
from a simple priority cut? Can you suggest a story for their MVP slice that they may have
overlooked or one they included that should be deferred?

---

### Discussion Rubric

| Criterion | Excellent (10) | Proficient (7) | Developing (4) | Beginning (1) |
|---|---|---|---|---|
| Accuracy of technical content | All key concepts correctly applied | Minor error in one concept | One significant conceptual error | Multiple errors or missing core concept |
| Depth of analysis | Explains why, not just what; anticipates downstream effects | Some analysis beyond surface description | Mostly descriptive, limited analysis | Restates scenario with no analysis |
| Word count and completeness | 175–225 words; all required elements addressed | 150–175 words; most elements present | Under 150 words; missing one element | Under 100 words or missing major element |
| Peer reply quality | Engages substantively with classmate's reasoning; adds new insight | Agrees with brief extension of argument | Mostly agreement without engagement | One word or off-topic reply |
| Writing quality | Professional sentences; no spelling or grammar errors | 1–2 minor errors | 3–4 errors that affect clarity | Frequent errors that impede understanding |

---

### Professor Nash Note

I read every initial post before Thursday midnight so I can address any widespread
misconceptions in the Friday office hours session. The most common issue I see in this
discussion is students who correctly identify the right relationship — extend versus include
— but then draw the arrow in the wrong direction when they describe it in words. Direction
matters as much as relationship type, because developers and testers use both pieces of
information to build and verify behavior. If you are uncertain about arrow direction, review
the Reading Guide comparison table before posting.

---

*Discussion Forum — Module 08 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

# Video Script: Module 08 — Use Case and User Story Development

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: IIBA ECBA — Business Analysis Core Concept Model

---

### SEGMENT 1: Introduction and Context (0:00–2:00)

Welcome back, everyone. This is Module 08, and today we are digging into one of the most
practical skills a business analyst will use on a daily basis: capturing what a system needs
to do from the perspective of the people who will actually use it.

[PAUSE]

We are covering two complementary techniques in this module. The first is use case modeling,
which has roots in UML and object-oriented analysis. The second is user story development,
which comes from Agile methodologies, especially Scrum and Extreme Programming.

Both techniques answer the same fundamental question: who is doing what with the system, and
why does it matter to them?

[SHOW DIAGRAM: Side-by-side comparison — Use Case Diagram on left, User Story card on right]

Before we jump into diagrams and notation, I want you to appreciate why these tools exist.
Requirements written in plain paragraphs are ambiguous. They use passive voice. They omit
actors. They leave out the business value. Use cases and user stories force us to be explicit
about who, what, and why.

[PAUSE]

By the end of this module, you will be able to draw a complete use case diagram, write fully
dressed use cases with alternate flows, write user stories in proper format with acceptance
criteria, and build a story map to sequence development priorities.

---

### SEGMENT 2: What Is a Use Case? (2:00–5:30)

Let's start with definitions. A use case is a description of how a user — which we call an
actor — interacts with a system to achieve a specific goal. The key word there is goal.

[PAUSE]

Ivar Jacobson introduced use cases in the late 1980s as part of his Objectory method. They
were later incorporated into the Unified Modeling Language — UML — and became one of the
primary tools for capturing functional requirements.

A use case has several key properties. First, it is goal-oriented — it captures a complete
unit of useful work. Second, it involves an actor — someone or something outside the system
boundary. Third, it has a success scenario and typically one or more alternate or failure
scenarios.

[SHOW DIAGRAM: Simple use case ellipse with actor stick figure connected by association line]

The vocabulary we use: the actor is drawn as a stick figure. The use case is drawn as an
ellipse containing a short verb-noun name. The system boundary is a rectangle that encloses
all use cases in scope. Actors sit outside the rectangle. Association lines connect actors to
the use cases they participate in.

[PAUSE]

Let me give you a concrete example using our course case study: the Lakewood Community
Library Management System, which we will call LMS throughout these modules.

Actors in the LMS include the Library Patron, the Librarian, the System Administrator, and
an external Email Notification Service. Notice that the Email Notification Service is not a
human — it is a system actor. Use cases support non-human actors just fine.

[SHOW DIAGRAM: LMS actors labeled with descriptions]

Some use cases in the LMS: Search Catalog, Check Out Book, Return Book, Reserve Book,
Manage Member Account, Generate Overdue Report. Each of these is a discrete goal that an
actor wants to accomplish.

---

### SEGMENT 3: Actors and System Boundary (5:30–8:00)

Let's talk about actors more carefully. An actor is a role played by a person, system, or
organization that interacts with the system under discussion — which we abbreviate as SuD.

[PAUSE]

A common mistake students make is confusing an actor with a job title. The actor is the
role, not the individual. One person can play multiple roles. A Librarian might also act as
a Library Patron when they borrow books for their own use. We draw them as separate actors
because they have different goals and different interactions.

Actors can be primary or secondary. A primary actor initiates the use case to achieve a
personal goal. A secondary actor is called upon by the system to help complete the use case.
In our LMS, the Patron is primary for Check Out Book. The Email Notification Service is
secondary — it sends the confirmation email.

[SHOW DIAGRAM: LMS use case diagram with primary and secondary actors labeled]

The system boundary defines scope. Everything inside the rectangle is built. Everything
outside is a given — an external reality the system must work with. Deciding what goes
inside versus outside the boundary is one of the most important scoping decisions a business
analyst makes.

[PAUSE]

For ECBA alignment: the IIBA Business Analysis Body of Knowledge defines elicitation as a
core technique. Use case diagrams are explicitly listed in the BABOK as a business analysis
tool for requirements visualization. When you sit for the ECBA exam, expect questions about
actor identification and system boundary definition.

---

### SEGMENT 4: Include and Extend Relationships (8:00–11:30)

Now we get into two special relationships in use case diagrams that trip up many students:
include and extend.

[PAUSE]

The include relationship means that one use case always incorporates the behavior of another.
Think of it as mandatory reuse. We draw it as a dashed arrow pointing FROM the base use case
TO the included use case, with the label double-angle-brackets include double-angle-brackets.

[SHOW DIAGRAM: Check Out Book with dashed include arrow to Authenticate Member]

In our LMS, every time a patron checks out a book, the system must authenticate them first.
That authentication logic is shared. Rather than describe it repeatedly inside every use
case, we factor it into its own use case — Authenticate Member — and include it. So Check
Out Book includes Authenticate Member. Reserve Book also includes Authenticate Member.

[PAUSE]

The extend relationship is more nuanced. Extend means that under certain conditions, one
use case optionally inserts additional behavior into a base use case. We draw it as a dashed
arrow pointing FROM the extending use case TO the base use case, labeled extend. This
direction confuses students constantly. The arrow points the opposite direction from what
you might intuit.

[SHOW DIAGRAM: Apply Late Fee with dashed extend arrow pointing to Return Book, extension point labeled]

In our LMS, Return Book has an extension point: if the book is overdue, Apply Late Fee
extends into the return process. Apply Late Fee does not happen every time — only under the
condition that the due date has passed.

[PAUSE]

Memory trick: Include is like a function call — it always happens. Extend is like a plugin —
it conditionally inserts behavior. The arrow for extend points to the base case because the
base case does not know about its extensions.

Generalization is a third relationship used when one actor or use case is a specialization of
another. We draw it with a solid triangle-tipped arrow, the same as UML inheritance. A
Librarian generalizes from Member — they can do everything a Member can do, plus more.

[SHOW DIAGRAM: Librarian generalizing from Member actor with inheritance arrow]

---

### SEGMENT 5: Fully Dressed Use Case Specification (11:30–14:30)

A use case diagram is just the overview. The real analytical work happens in the fully
dressed use case specification — a structured text document that walks through every step
of the interaction.

[PAUSE]

The fully dressed use case includes these fields: Use Case ID and Name, Goal in Context,
Scope, Level, Primary Actor, Stakeholders and Interests, Preconditions, Minimal Guarantees,
Success Guarantees, Main Success Scenario, Extensions, and Technology Variations.

[SHOW DIAGRAM: Use case specification template with all fields visible]

Let me walk through the main success scenario structure. We number each step. We alternate
between actor actions and system responses. Each step is a single observable event — not an
internal implementation detail.

For Check Out Book: Step 1 — Patron presents library card and book to Librarian. Step 2 —
Librarian scans member barcode. Step 3 — System validates member status. Step 4 — Librarian
scans book barcode. Step 5 — System checks book availability. Step 6 — System records loan,
sets due date, updates inventory. Step 7 — System prints or emails confirmation. Step 8 —
Patron receives book and receipt.

[PAUSE]

Extensions document what happens when things go sideways. Extension 3a: Member account
suspended — System displays suspension notice, use case ends. Extension 5a: Book not in
catalog — System displays error, Librarian verifies barcode, returns to Step 4.

This level of detail is what separates professional requirements documentation from casual
notes. Developers, testers, and stakeholders can all read this specification and understand
exactly what the system must do.

---

### SEGMENT 6: User Stories — Agile Requirements (14:30–17:30)

Now let's shift to user stories. User stories are short, conversational descriptions of a
feature from the perspective of the user who benefits from it.

[PAUSE]

The standard format, introduced by Mike Cohn, is: As a [type of user], I want [some goal],
so that [some reason or business value]. Every part of this template matters. The "as a"
names the actor. The "I want" names the capability. The "so that" names the value — and
teams that skip the "so that" lose the business justification that prevents gold-plating.

[SHOW DIAGRAM: User story card with all three parts labeled and color-coded]

Here are examples from our LMS. As a Library Patron, I want to search the catalog by title
or author, so that I can quickly find books I am interested in borrowing. As a Librarian,
I want to generate an overdue notice report, so that I can contact members with outstanding
items. As an Administrator, I want to add or deactivate member accounts, so that I can
maintain an accurate membership database.

[PAUSE]

Notice the difference in granularity across these stories. The catalog search story is fairly
large — it might represent several days of work. That makes it an Epic in Agile terminology.
We would break it into smaller stories: search by title, search by author, display results
with cover images, filter by genre, sort by publication date.

The INVEST criteria help us evaluate story quality. INVEST stands for Independent,
Negotiable, Valuable, Estimable, Small, and Testable. A good user story satisfies all six.

---

### SEGMENT 7: Acceptance Criteria and the Definition of Done (17:30–19:30)

User stories need acceptance criteria to be testable. Acceptance criteria define the
conditions that must be true for the story to be considered complete. They bridge the gap
between requirements and testing.

[PAUSE]

The most common format for acceptance criteria is Given-When-Then, which is also the basis
for behavior-driven development tools like Cucumber and Gherkin.

Given a patron is on the catalog search page, when they enter "Moby Dick" in the search
field and click Search, then the results list displays all books with "Moby Dick" in the
title, sorted by relevance. That is a single, testable criterion.

[SHOW DIAGRAM: Acceptance criteria card using Given-When-Then format with color-coded sections]

Best practice: write three to eight acceptance criteria per story. Fewer than three suggests
the story is too vague. More than eight suggests the story should be split.

The Definition of Done is related but different. It is a shared team agreement about quality
standards that apply to every story — things like code review completed, unit tests written,
documentation updated. Acceptance criteria are story-specific. The Definition of Done is
universal.

[PAUSE]

---

### SEGMENT 8: Story Mapping (19:30–21:30)

Story mapping is a technique created by Jeff Patton to organize user stories into a
two-dimensional grid that represents the user journey horizontally and depth of functionality
vertically.

[SHOW DIAGRAM: Story map with backbone activities across the top row, walking skeleton as first data row, enhancements stacked below]

The backbone represents the high-level activities a user performs in sequence — for LMS:
Browse, Borrow, Return, Manage Account. Under each activity, we list the user tasks that
support it. Browsing involves: search catalog, view book details, check availability, place
hold. Under Borrow: present credentials, scan items, receive receipt, get due date.

[PAUSE]

We then draw horizontal slices across the map to define releases. The first release
implements the minimum viable product — the bare minimum set of stories that delivers
end-to-end value. Subsequent releases add depth and richness.

Story mapping is particularly valuable in scope discussions because it shows what is being
deferred rather than what is being dropped. Stakeholders can see the whole picture and make
informed trade-off decisions.

---

### SEGMENT 9: Summary and ECBA Connections (21:30–23:00)

Let's bring it all together. Use cases and user stories are two different lenses on the same
requirements. Use cases are formal, comprehensive, and excellent for complex business rules
and alternate flows. User stories are lightweight, conversational, and excellent for
iterative development and stakeholder collaboration.

[PAUSE]

For the ECBA exam, remember these key associations. Use cases appear in the BABOK under
Requirements Visualization and Structured Walkthrough techniques. User stories align with
the Agile Analysis and Design knowledge area. Story mapping is a Product Backlog management
technique. The include relationship is for mandatory reuse; extend is for conditional
behavior.

[SHOW DIAGRAM: ECBA concept map connecting techniques to BABOK knowledge areas]

Your lab this week asks you to build a use case diagram for the LMS reservation subsystem,
write two fully dressed use case specifications, and develop a story map with acceptance
criteria for the first sprint. Your quiz will test your ability to distinguish include from
extend and to evaluate user stories against the INVEST criteria.

[PAUSE]

Great work today. Use cases and user stories are tools you will use in every project for the
rest of your career. The more you practice them now, the more natural they become. I will
see you in Module 09, where we move into process modeling with BPMN.

---

*[END OF VIDEO SCRIPT — Module 08]*

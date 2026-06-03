# Video Script: Module 10 — Data Flow Diagrams and System Models

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: IIBA ECBA — Business Analysis Core Concept Model

---

### SEGMENT 1: Introduction — What Is a Data Flow Diagram? (0:00–2:00)

Welcome to Module 10. Today we are stepping into a modeling technique that has been a
cornerstone of structured systems analysis since the 1970s: the Data Flow Diagram, or DFD.

[PAUSE]

While use case diagrams show who interacts with a system and BPMN shows how work flows
through an organization, a DFD shows how data moves through a system. It answers the
question: where does data come from, how is it transformed, where does it get stored, and
where does it go?

[SHOW DIAGRAM: Simple DFD with external entity, process, data store, and data flow arrows labeled]

Data Flow Diagrams use Yourdon-Coad notation, which was formalized by Edward Yourdon and
Tom DeMarco in the late 1970s as part of structured systems analysis and design methodology.
This notation is still the most widely recognized DFD notation in academic and professional
practice.

[PAUSE]

One thing I want you to understand before we dig in: DFDs are not flowcharts and they are
not process models. A DFD does not show control flow or decision logic. It shows data
transformation — inputs become outputs through processes. That distinction is fundamental.

By the end of this module you will be able to draw a context diagram, a Level 0 DFD, and a
Level 1 DFD, apply Yourdon-Coad notation correctly, and identify and correct common DFD
errors.

---

### SEGMENT 2: DFD Notation — The Four Elements (2:00–5:30)

Every DFD uses exactly four types of elements. Memorize all four: External Entity, Process,
Data Store, and Data Flow.

[SHOW DIAGRAM: Four DFD elements side by side with labels — square, circle, open rectangle, and arrow]

The External Entity is drawn as a square or rectangle. It represents a person, organization,
or system that exists outside the scope of the system we are modeling — but that sends data
to it or receives data from it. In Yourdon-Coad notation, some analysts shade external
entities to visually separate them from processes.

[PAUSE]

The Process is drawn as a circle — sometimes called a bubble. It represents a transformation:
data enters the process, something happens to it, and different data exits. Every process
must have at least one incoming data flow and at least one outgoing data flow. A process
with no inputs or no outputs is called a miracle or a black hole respectively, and both are
modeling errors.

The Data Store is drawn as an open rectangle — two horizontal parallel lines with the left
side open. It represents a repository of data at rest: a database table, a file, a ledger.
Data stores have no active behavior — they simply store and retrieve. A data store must
have at least one data flow going into it or out of it, typically both.

[SHOW DIAGRAM: Data store with one incoming and one outgoing data flow labeled]

The Data Flow is drawn as an arrow with a label. The label names the data being transferred
— it should be a noun phrase: "Book Availability Status," "Member Record," "Overdue
Notice." The direction of the arrow shows which way the data travels. A double-headed arrow
represents a bidirectional data exchange.

[PAUSE]

Yourdon-Coad notation vs. Gane-Sarson notation: Gane-Sarson uses a rounded rectangle for
processes instead of a circle. Some textbooks use one, some use the other. In this course
we use Yourdon-Coad with circles for processes and squares for external entities.

---

### SEGMENT 3: Context Diagrams — Level 0 Overview (5:30–8:30)

The starting point for DFD modeling is the Context Diagram, which is also called a Level 0
DFD. A context diagram shows the entire system as a single process — one circle in the
center — surrounded by all the external entities that interact with it.

[PAUSE]

The context diagram has three rules. First: exactly one process, representing the entire
system. Second: all external entities relevant to the system scope. Third: all data flows
between external entities and the system, but no internal detail.

[SHOW DIAGRAM: LMS Context Diagram — single "Library Management System" circle in center, four external entities around it, data flows labeled]

For our Lakewood Library Management System, the context diagram has one process circle
labeled "1.0 Library Management System." External entities include Library Patron, Librarian,
System Administrator, and Email Notification Service. Data flows from Patron to the system
include: Member Registration Request, Catalog Search Query, Book Reservation Request.
Data flows from the system to Patron include: Search Results, Reservation Confirmation,
Overdue Notice. Data flows from Librarian include: Check-Out Transaction, Return Transaction.
Data flows from Administrator include: Member Account Update, Loan Policy Configuration.

[PAUSE]

The context diagram is a scoping tool. When a stakeholder asks "does the system handle X?",
the answer is visible in the context diagram: if the data flow for X appears on the diagram,
it is in scope. If it does not appear, it is out of scope.

The context diagram is the highest level of abstraction. We expand it into the Level 1 DFD
by breaking the central process bubble into sub-processes.

---

### SEGMENT 4: Level 1 DFD — Exploding the Context Diagram (8:30–12:00)

The Level 1 DFD expands the single process circle from the context diagram into the major
functional areas of the system. Each major function becomes a numbered process bubble.
The external entities and data flows from the context diagram must all appear in the Level 1
DFD — this is called leveling consistency, and it is a key quality check.

[PAUSE]

For the LMS, the Level 1 DFD might contain these major processes: 1.0 Manage Member
Accounts, 2.0 Catalog Management, 3.0 Circulation Management, 4.0 Reservation Management,
5.0 Reporting.

Data stores appear at this level because they represent the system's persistent data. LMS
data stores include: D1 Member Records, D2 Catalog, D3 Loan Records, D4 Reservation Queue.

[SHOW DIAGRAM: LMS Level 1 DFD with 5 process bubbles, 4 data stores, external entities, and labeled data flows]

Notice that some data flows now connect processes to data stores. The Circulation Management
process reads from and writes to the Loan Records data store. The Reservation Management
process reads from the Catalog and the Member Records and writes to the Reservation Queue.

[PAUSE]

Process numbering in Level 1 uses single integers: 1.0, 2.0, 3.0, and so on. When we
expand a Level 1 process into a Level 2 DFD, the child processes are numbered with the
parent prefix: 3.1, 3.2, 3.3 for sub-processes of Circulation Management.

Each Level 1 process bubble will eventually be expanded into a Level 2 DFD showing the
internal data flows and transformations within that process. The collection of all DFD levels
forms a leveled set.

---

### SEGMENT 5: Leveling and Balancing (12:00–14:30)

Two quality concepts are critical to DFD correctness: leveling and balancing.

[PAUSE]

Leveling means that when you expand a parent process into child processes, all the data
flows that entered and exited the parent must also appear in the child diagram — either as
incoming/outgoing flows at the boundary or as flows to/from data stores added at the child
level.

[SHOW DIAGRAM: Parent process "3.0 Circulation Management" with its data flows, then child Level 2 DFD showing those same flows preserved at the boundary]

Balancing is the check that confirms leveling has been correctly applied. To balance a
Level 2 DFD against its parent Level 1 process: count all incoming and outgoing data flows
on the parent bubble. Verify that exactly those same flows appear as boundary inputs and
outputs in the child diagram. No flows may appear in the child that do not exist in the
parent. No flows from the parent may be missing in the child.

[PAUSE]

This is a mechanical check you can perform before finalizing any DFD. I encourage you to
build a balancing table as part of your lab deliverable: list every data flow in the parent,
and for each one, identify where it appears in the child.

Common balancing errors: adding a data store in the child that has no corresponding data
flow in the parent, splitting one parent data flow into two child flows with different names
without documenting the split, and omitting an external entity from a child diagram.

---

### SEGMENT 6: Data Flow Labeling Rules (14:30–16:30)

Data flow labels are one of the most important — and most neglected — aspects of DFD quality.
A DFD with unlabeled arrows is not a DFD; it is an unlabeled diagram that communicates
nothing about the system's data.

[PAUSE]

Rules for data flow labels:

First: every data flow must have a unique, descriptive noun-phrase label. "Data" is not an
acceptable label. "Book Information" is better. "Book Availability Status" is best.

Second: the label should reflect the actual content of the data being transferred, not the
action being performed. "Search Results" is correct. "Performing Search" is a process action,
not a data label.

Third: two different data flows with the same name but different directions should be
distinguished. "Member Record Request" from a process to a data store and "Member Record"
returned from the data store to a process are different flows with different content.

[SHOW DIAGRAM: DFD fragment comparing poorly labeled arrows versus well-labeled arrows side by side]

Fourth: avoid implementation-specific labels. "SQL Query" or "JSON Response" are
implementation details. "Catalog Search Query" and "Search Results" are the correct
logical labels.

[PAUSE]

For ECBA exam purposes: the BABOK lists data flow diagrams as a business analysis technique.
Questions will ask you to identify modeling errors, and unlabeled or incorrectly labeled
data flows are among the most common testable errors.

---

### SEGMENT 7: Common DFD Errors (16:30–18:30)

Let's cover the four most common DFD errors. Every one of these will appear on your quiz
and in your lab peer reviews.

[PAUSE]

Error 1: The Black Hole. A process has one or more inputs but no outputs. Data flows in
and disappears. This is always a modeling error — every process must produce output.

Error 2: The Miracle. A process has outputs but no inputs. Data is generated from nothing.
This is also always a modeling error — every process must consume input.

[SHOW DIAGRAM: Two DFD fragments — Black Hole process and Miracle process with error labels in red]

Error 3: The Data Store Connected Directly to an External Entity. Data stores represent
internal system memory. External entities should never connect directly to a data store —
they must interact with data stores through a process.

Error 4: The Unnamed Data Flow. An arrow with no label is a missing requirements statement.
Every arrow must have a name that communicates what data it carries.

[PAUSE]

A fifth error worth mentioning: adding control flow or decision logic to a DFD. DFDs do not
contain diamonds or decision symbols. Decision logic belongs in BPMN process models or
structured English specifications. If you feel the urge to draw a decision diamond in a DFD,
that is a sign you are conflating two different modeling techniques.

---

### SEGMENT 8: External Entities and System Scope (18:30–20:30)

External entities define the boundary of system responsibility. Anything that is an external
entity is outside the system — we do not design or control it; we only define the data
interface with it.

[PAUSE]

A common scoping question: should something be modeled as a process inside the system or
an external entity outside it? The test is: does the system we are building own and control
the logic of this component? If yes, it is a process inside the system. If no, it is an
external entity.

For the LMS, the Email Notification Service is an external entity — it is a third-party
system. The Circulation Management logic is a process — we are building it. The Library
Patron is an external entity — we do not control their behavior. The Member Records database
is a data store — we own it and it is inside the system.

[SHOW DIAGRAM: LMS context diagram with items labeled as internal or external, color-coded]

[PAUSE]

Some external entities appear on multiple DFD levels — this is allowed and expected. An
external entity like the Patron interacts with multiple processes at the Level 1 DFD: they
send catalog queries to the Catalog Management process and reservation requests to the
Reservation Management process. Repeating the external entity symbol across the diagram is
acceptable and often clearer than drawing long crossing data flow arrows.

---

### SEGMENT 9: Summary and ECBA Connections (20:30–22:30)

Let's bring everything together. A DFD models data transformation — not process control, not
user interfaces. The four elements are external entity (square), process (circle), data
store (open rectangle), and data flow (labeled arrow). Three levels of abstraction: context
diagram, Level 1, and Level 2.

[PAUSE]

For ECBA exam alignment: data flow diagrams are explicitly listed in the BABOK as a
business analysis technique used during requirements analysis. Know the four elements, know
how to identify the four common errors, and know the difference between a context diagram
and a Level 1 DFD.

[SHOW DIAGRAM: ECBA concept map connecting DFD levels and elements to BABOK knowledge areas]

Your lab this week has you build a context diagram and a Level 1 DFD for the LMS, then
expand one Level 1 process to a Level 2 DFD and demonstrate balancing. Your quiz tests
element identification, error detection, and leveling rules.

[PAUSE]

In Module 11 we shift from process and data flow modeling to data structure modeling with
entity-relationship diagrams. We move from asking how data flows to asking what data the
system needs to store and how it is organized. See you there.

---

*[END OF VIDEO SCRIPT — Module 10]*

# Video Script: Module 09 — Process Modeling with BPMN

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: IIBA ECBA — Business Analysis Core Concept Model

---

### SEGMENT 1: Introduction — Why Process Models Matter (0:00–2:00)

Welcome to Module 09. Today we are studying Business Process Model and Notation — BPMN —
the international standard for process modeling used by business analysts, process
engineers, and solution architects around the world.

[PAUSE]

If use case diagrams answer "what does the system do," BPMN answers "how does work actually
flow through the organization." Process models expose handoffs, decision points, delays, and
bottlenecks that requirements documents alone cannot reveal. They also serve as the bridge
between business stakeholders who describe work in words and technology teams who need to
automate it.

[SHOW DIAGRAM: Sample BPMN diagram for a simple approval workflow with pools, lanes, tasks, and a gateway visible]

BPMN is maintained by the Object Management Group and is currently at version 2.0. It is
platform-neutral, tool-neutral, and widely understood across industries. When you walk into
a process improvement engagement, BPMN is the language everyone is expected to speak.

[PAUSE]

In this module we cover the core BPMN 2.0 elements, swimlane diagrams, gateway types,
event types, subprocesses, and the critical skill of modeling current-state versus
future-state processes. All of these topics are testable on the ECBA exam.

---

### SEGMENT 2: BPMN Core Elements Overview (2:00–5:00)

BPMN has four categories of elements: Flow Objects, Connecting Objects, Swimlanes, and
Artifacts. Let's define each category.

[SHOW DIAGRAM: BPMN element taxonomy grid with all four categories and their subtypes labeled]

Flow Objects are the primary building blocks — they represent the things that happen in a
process. There are three types: Events, Activities, and Gateways.

Events are things that happen — they start, end, or interrupt a process. Activities are the
work that gets done — they can be Tasks or Subprocesses. Gateways control the flow of the
process — they decide where sequence flow splits and merges.

[PAUSE]

Connecting Objects link flow objects together. The Sequence Flow is a solid arrow that
shows the order of activities within a pool. The Message Flow is a dashed arrow with an
open circle at the source, crossing between pools to show communication between
participants. The Association is a dotted line that connects artifacts to flow objects.

Swimlanes provide organizational context. A Pool represents a participant — typically an
organization or a system. A Lane divides a pool into roles or departments. All sequence
flow stays within a single pool; communication between pools uses message flow.

Artifacts add information without changing flow. Text Annotations attach explanatory notes.
Data Objects represent data inputs and outputs. Groups visually cluster related activities
for documentation purposes.

[SHOW DIAGRAM: Annotated BPMN legend with each element type color-coded]

---

### SEGMENT 3: Events in BPMN (5:00–8:00)

Events are one of the most nuanced aspects of BPMN because there are many types. Let's
focus on the ones most commonly used and most frequently tested.

[PAUSE]

Events are categorized by position: Start Events begin a process, Intermediate Events occur
during a process, and End Events terminate a process. Events are also categorized by type,
shown by icons inside the event circle.

Start Event types we need to know: the None Start Event is an empty circle — the process
simply begins when triggered. The Message Start Event has an envelope icon — the process
begins when a message is received. The Timer Start Event has a clock icon — the process
begins on a schedule.

[SHOW DIAGRAM: Three start event circles with None, Message, and Timer icons labeled]

Intermediate Event types: the Message Intermediate Catch Event waits for a message to
arrive before continuing. The Timer Intermediate Event introduces a delay — the process
waits for a specified duration. The Error Intermediate Boundary Event attaches to the
boundary of an activity and triggers an alternate flow if an error occurs.

End Event types: the None End Event terminates the process path. The Message End Event
sends a message when the path ends. The Error End Event triggers an error that a
catching event in the parent process must handle. The Terminate End Event kills all active
paths in the entire process immediately.

[PAUSE]

The visual encoding rule: Start Events use thin single-line circles. Intermediate Events
use double-line circles. End Events use thick single-line circles. This consistent visual
grammar makes it easy to scan a diagram and identify process start and end points at a
glance.

[SHOW DIAGRAM: Start, Intermediate, and End event circles side by side with thickness comparison labeled]

---

### SEGMENT 4: Gateways — Controlling Process Flow (8:00–11:00)

Gateways are the decision points and synchronization points of a BPMN process. There are
five gateway types you must master: Exclusive, Inclusive, Parallel, Event-Based, and
Complex.

[PAUSE]

The Exclusive Gateway — also called an XOR gateway — is the most common. It is drawn as a
diamond with an X inside or sometimes an empty diamond. At an Exclusive Gateway, exactly
one outgoing path is taken based on a condition. All conditions must be mutually exclusive
and collectively exhaustive — there must be a default path for any unmatched condition.

[SHOW DIAGRAM: Exclusive gateway with three outgoing paths and conditions labeled: Order < $100, Order $100–$500, Order > $500]

The Parallel Gateway — drawn as a diamond with a plus sign — splits flow into multiple
concurrent paths, all of which execute simultaneously. It is used when activities can be
performed in parallel without dependencies. The same plus-sign gateway is used for the
joining merge that waits for all parallel paths to complete before continuing.

[PAUSE]

The Inclusive Gateway — drawn as a diamond with an O inside — is a combination of exclusive
and parallel behavior. One or more outgoing paths are taken based on conditions, and all
selected paths execute in parallel. When joining, the inclusive gateway waits for all
active paths to complete — but only the active ones, not paths that were not taken.

The Event-Based Gateway — drawn as a diamond with a double circle and pentagon or event
icon — directs flow to the first of several events that occurs, like a race condition. It
is useful for modeling wait states where the process continues based on whichever event
arrives first.

[SHOW DIAGRAM: Event-based gateway with two competing timer and message intermediate events on outgoing paths]

The Complex Gateway is the least common — a diamond with an asterisk. It handles complex
conditions that cannot be expressed with the other gateway types. Use it sparingly and
document the logic in an attached annotation.

---

### SEGMENT 5: Swimlane Diagrams — Pools and Lanes (11:00–13:30)

Swimlane diagrams extend BPMN by making participant roles and organizational boundaries
explicit in the layout of the diagram itself.

[PAUSE]

A Pool is a rectangular container representing one participant in the process. A
Collaboration diagram contains two or more pools communicating via Message Flow. For
example, a Customer pool and a Library System pool might exchange messages for the book
reservation process.

Lanes divide a pool horizontally or vertically into roles. In a library system pool, lanes
might be: Patron, Librarian, Inventory System, and Email System. Each activity is placed
in the lane of the role responsible for performing or initiating it.

[SHOW DIAGRAM: Two-pool BPMN collaboration with Customer and Library System pools; Library System pool has Patron, Librarian, and System lanes; message flows cross between pools]

The key rule for lanes: sequence flow stays inside a single pool. When a Librarian hands
work to the Inventory System, the sequence flow arrow crosses the lane boundary within the
same pool. When the Library System sends a notification to the Customer, that is a message
flow arrow that crosses the pool boundary.

[PAUSE]

Swimlane diagrams immediately reveal process problems that text descriptions hide. If you
see twenty sequence flows crossing lane boundaries, that indicates excessive handoffs —
a common source of delay and error. If you see a single lane handling most of the work,
that may indicate a capacity bottleneck. Visual process models make these patterns obvious.

---

### SEGMENT 6: Subprocesses and Collapsed Activities (13:30–15:30)

As processes grow complex, BPMN subprocesses help manage that complexity. A subprocess is
an activity that contains a complete process within it. It is drawn as a rounded rectangle
with a plus sign in the lower center.

[PAUSE]

A collapsed subprocess shows only the outer boundary on the main diagram — the internal
steps are hidden. An expanded subprocess shows the internal flow inline. Collapsed
subprocesses are useful for keeping a high-level diagram readable while signaling that
additional detail exists.

[SHOW DIAGRAM: Main process with one collapsed subprocess (plus sign visible) and one expanded subprocess showing internal tasks and events]

Call Activities are reusable subprocesses — drawn with a thick border — that invoke a
globally defined process. This is equivalent to the include relationship in use cases. The
same authentication process might be called from multiple parent processes using a Call
Activity.

[PAUSE]

The practical guidance: model processes at the right level of abstraction for your audience.
An executive sponsor needs a high-level BPMN with collapsed subprocesses. A developer
implementing a specific subprocess needs the expanded view. Having both available at
different zoom levels serves multiple stakeholder needs without creating separate documents.

---

### SEGMENT 7: Current-State vs. Future-State Modeling (15:30–18:30)

One of the most valuable applications of BPMN in business analysis is the side-by-side
comparison of current-state — called As-Is — and future-state — called To-Be — processes.

[PAUSE]

The As-Is model documents how the process works today, including all its inefficiencies.
Many analysts are tempted to skip the As-Is model and jump straight to the To-Be, but this
is a mistake. The As-Is model serves three critical purposes: it validates your understanding
with stakeholders, it identifies the specific pain points that the new system must address,
and it provides a baseline against which improvement can be measured.

[SHOW DIAGRAM: As-Is process for library book reservation with manual steps, phone calls, and paper forms highlighted in red]

The To-Be model shows the improved future state after the new system is implemented. It
should directly address each pain point identified in the As-Is model. Stakeholders can
compare the two models and see exactly what is changing — which builds confidence and
reduces resistance to change.

[PAUSE]

Common analysis patterns you will see when comparing As-Is to To-Be: elimination of
handoffs where digital automation removes manual transfer steps; consolidation of decision
points where business rules replace manual judgment calls; compression of wait states where
automated notifications replace phone tag; and role shifts where self-service features move
work from staff to the patron or customer.

[SHOW DIAGRAM: To-Be process for library book reservation with automated steps, system lanes, and removed manual steps highlighted in green]

When you present both models together, annotate the changes. Use notes or color to mark
activities that are new, modified, or removed. This delta documentation becomes the
foundation for change management planning and training material development.

---

### SEGMENT 8: Process Analysis and BPMN Quality Checks (18:30–21:00)

A BPMN diagram is only as useful as it is accurate and readable. Let me share the quality
checks every business analyst should run before presenting a process model.

[PAUSE]

First: every process must have at least one Start Event and at least one End Event. A
process with no explicit end leaves stakeholders unclear about where the process concludes.
A process with no explicit start leaves developers uncertain what triggers execution.

Second: every gateway split must have a corresponding merge. An exclusive split must have
an exclusive merge. A parallel split must have a parallel merge. Orphaned gateway paths
are one of the most common BPMN errors.

[SHOW DIAGRAM: Common BPMN errors side by side — missing end event, unmatched gateway, sequence flow crossing pool boundary]

Third: sequence flow must not cross pool boundaries. If you have drawn a sequence flow
arrow between pools, that is an error — it should be a message flow.

Fourth: every activity must be reachable and contribute to the process goal. Activities
that have no incoming sequence flow — except Start Events — or no outgoing sequence flow —
except End Events — are isolated and broken.

[PAUSE]

Fifth: lane assignments must be consistent. Every activity belongs to exactly one lane.
Activities in the wrong lane create confusion about accountability.

---

### SEGMENT 9: Summary and ECBA Exam Connections (21:00–23:00)

Let's bring everything together. BPMN is a visual language for process modeling. Its core
elements are events, activities, and gateways as flow objects; sequence flow, message flow,
and associations as connectors; and pools and lanes as swimlanes.

[PAUSE]

For the ECBA exam: BPMN appears in the BABOK as a business analysis technique under
Business Process Modeling. Know the five gateway types — exclusive, inclusive, parallel,
event-based, and complex. Know the three event positions — start, intermediate, end. Know
that sequence flow stays within a pool and message flow crosses pool boundaries.

[SHOW DIAGRAM: ECBA concept map — BPMN elements mapped to BABOK technique categories]

Your lab this week has you build both an As-Is and a To-Be process model for the LMS book
reservation workflow. Your quiz tests gateway identification, event type recognition, and
the rules distinguishing sequence flow from message flow.

[PAUSE]

In Module 10 we move to data flow diagrams — a different but complementary modeling
technique that focuses on data transformation rather than process sequence. I will see you
there.

---

*[END OF VIDEO SCRIPT — Module 09]*

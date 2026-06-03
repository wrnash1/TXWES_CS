# Reading Guide: Module 09 — Process Modeling with BPMN

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Business Process Modeling

---

### Overview

This reading guide covers BPMN 2.0 notation, swimlane diagrams, gateway types, event
types, subprocesses, and current-state versus future-state process modeling. BPMN is a
BABOK-listed technique and directly testable on the ECBA exam.

---

### Section 1: BPMN Element Categories

BPMN 2.0 organizes all diagram elements into four top-level categories.

| Category | Elements | Purpose |
|---|---|---|
| Flow Objects | Events, Activities, Gateways | Represent what happens in a process |
| Connecting Objects | Sequence Flow, Message Flow, Association | Link flow objects and artifacts |
| Swimlanes | Pools, Lanes | Show participant and role boundaries |
| Artifacts | Data Objects, Text Annotations, Groups | Add context without changing flow |

---

### Section 2: Events Reference Table

Events are circles. Their position in the process and the icon inside determine their type.

#### Event Position Visual Encoding

- Start Event: thin single-line circle
- Intermediate Event: double-line circle
- End Event: thick single-line circle

#### Event Types by Icon

| Icon | Start Meaning | Intermediate Meaning | End Meaning |
|---|---|---|---|
| (empty) | Process begins | None — used for link or compensation | Process path ends |
| Envelope | Triggered by incoming message | Wait for message / Send message | Send message |
| Clock | Triggered on schedule or timer | Delay for specified duration | N/A |
| Lightning bolt | N/A | Error boundary on activity | Throws error condition |
| Circle with ring | N/A | Catch or throw signal | Throws signal |
| Double circle | N/A | N/A | Terminates ALL active paths |

#### Key Event Rules

- A Start Event may have no incoming sequence flow.
- An End Event may have no outgoing sequence flow.
- A Terminate End Event kills the entire process instance immediately — including any
  parallel paths that are still active.
- An Error End Event throws an error that must be caught by an Error Intermediate Boundary
  Event on an enclosing subprocess or parent process.

> ECBA Exam Tip: Know the visual thickness rule. Start = thin circle. Intermediate = double
> circle. End = thick circle. Questions often show a symbol and ask you to identify whether
> it is a start, intermediate, or end event based purely on the visual encoding.

---

### Section 3: Gateway Types Reference Table

Gateways are diamonds. The icon inside identifies the gateway type.

| Symbol | Gateway Type | Behavior |
|---|---|---|
| Diamond with X | Exclusive (XOR) | Exactly one outgoing path taken; conditions mutually exclusive |
| Diamond with O | Inclusive (OR) | One or more paths taken; all selected paths run in parallel |
| Diamond with + | Parallel (AND) | ALL outgoing paths taken simultaneously |
| Diamond with double circle + pentagon | Event-Based | Flow continues on whichever event arrives first |
| Diamond with asterisk | Complex | Handles conditions too complex for other gateway types |

#### Gateway Pairing Rules

Every split gateway should have a corresponding join gateway of the same type. Mixing
gateway types at split and join creates undefined behavior and signals a modeling error.

| Split Type | Correct Join Type | Notes |
|---|---|---|
| Exclusive (XOR) split | Exclusive (XOR) join | Join continues when any one path arrives |
| Parallel (AND) split | Parallel (AND) join | Join waits for ALL paths to complete |
| Inclusive (OR) split | Inclusive (OR) join | Join waits for all ACTIVE paths to complete |

#### Exclusive Gateway Default Path

Every Exclusive Gateway split should have a default path — drawn with a small diagonal
slash on the outgoing arrow — that executes when no other condition evaluates to true.
A missing default path is a common BPMN error that leaves the process undefined for
unhandled conditions.

> ECBA Exam Tip: The inclusive gateway is the most frequently confused. It is NOT the same
> as a parallel gateway. Parallel splits always take ALL paths. Inclusive splits take ONE OR
> MORE paths based on conditions. Distinguish them by their diamond icons: + is parallel,
> O is inclusive.

---

### Section 4: Swimlane Notation — Pools and Lanes

#### Pools

A Pool is a rectangular container representing one participant. In a collaboration diagram,
two or more pools communicate via Message Flow. Common pool types:

- An organization (Customer, Vendor, Library)
- A system (CRM System, Email Service)
- A role when only one participant is modeled (Black Box Pool — collapsed with no internal lanes)

#### Lanes

Lanes subdivide a pool. Every activity in a lane is the responsibility of that lane's role.
Lane names typically match organizational roles, departments, or system components.

LMS example lanes within the Library System pool:

- Patron (self-service portal actions)
- Librarian (desk staff actions)
- Circulation System (automated system tasks)
- Email Service (automated notification tasks)

#### Sequence Flow vs. Message Flow

| Flow Type | Visual | Rule |
|---|---|---|
| Sequence Flow | Solid arrow | Stays WITHIN a single pool; shows order of activities |
| Message Flow | Dashed arrow with open circle at source | Crosses BETWEEN pools; shows communication |

This rule is absolute in BPMN 2.0. Sequence flow NEVER crosses a pool boundary. If you
see a sequence flow arrow between pools, the diagram has an error.

---

### Section 5: Activities — Tasks and Subprocesses

#### Task Types

Tasks are the basic unit of work in BPMN. Task types are indicated by icons in the upper
left corner of the rounded rectangle.

| Icon | Task Type | Meaning |
|---|---|---|
| (none) | Abstract Task | Unspecified; used in early modeling |
| Person silhouette | User Task | A person performs this step using a system interface |
| Gears | Service Task | Automated by a system or service; no human action |
| Envelope | Send Task | Sends a message to another participant |
| Envelope (catching) | Receive Task | Waits for a message from another participant |
| Script icon | Script Task | Executed by a process engine running a script |

#### Subprocesses

A Subprocess is an activity that contains a complete internal process. The visual indicator
is a plus sign at the bottom center of the rounded rectangle.

- **Collapsed Subprocess**: Shows only the outer boundary; internal flow is hidden
- **Expanded Subprocess**: Shows internal flow inline within the outer boundary
- **Call Activity**: A reusable subprocess with thick border; invokes a globally defined process

#### Subprocess Uses

Use subprocesses when:

- A group of tasks always executes together as a unit
- The detail level would make the parent diagram unreadable
- The same sequence of steps is reused across multiple processes (Call Activity)
- A set of tasks needs shared error handling or compensation logic

---

### Section 6: Current-State and Future-State Process Modeling

#### As-Is Process Model

The As-Is model documents the current business process exactly as it operates today —
including inefficiencies, workarounds, and manual steps. Its purpose is not to criticize
the current process but to:

- Confirm shared understanding with process owners and stakeholders
- Identify pain points, handoff delays, and bottleneck activities
- Establish a baseline for measuring process improvement
- Surface hidden business rules embedded in informal practices

Common As-Is indicators to look for:

- Activities with long average durations relative to their complexity
- High numbers of lane crossings indicating excessive handoffs
- Frequent loops back to earlier steps indicating rework
- Decision points where one person has no visibility into the decision criteria

#### To-Be Process Model

The To-Be model shows the improved future process after the proposed solution is
implemented. It directly addresses each pain point from the As-Is model.

Characteristics of a well-designed To-Be model:

- Fewer total steps than the As-Is model
- Reduced lane crossings through automation or role consolidation
- Explicit system tasks replacing manual steps
- Wait states shortened through automated notifications
- Decision logic moved into system gateways with explicit conditions

#### Delta Documentation

When presenting both models, annotate the changes:

- Green highlights: new activities added in To-Be
- Red highlights: activities removed from As-Is
- Yellow highlights: activities modified in To-Be
- Summary table: count of steps, handoffs, and wait states in As-Is vs. To-Be

---

### Section 7: BPMN Quality Checklist

Before finalizing any BPMN diagram, verify each item below.

| Check | Description |
|---|---|
| Start events present | Every process has at least one Start Event |
| End events present | Every process path reaches an End Event |
| No orphaned activities | Every non-start activity has at least one incoming sequence flow |
| No dead-end activities | Every non-end activity has at least one outgoing sequence flow |
| Gateways paired | Every split gateway has a corresponding merge gateway |
| Correct flow types | Sequence flow stays within pools; message flow crosses between pools |
| Lane assignments | Every activity belongs to exactly one lane |
| Default paths | Every Exclusive Gateway split has a default path |
| Labels complete | Every gateway condition and every sequence flow is labeled |
| Consistent notation | All icons follow BPMN 2.0 standard; no mixed notations |

---

### Section 8: LMS Book Reservation — As-Is vs. To-Be Narrative

#### As-Is Narrative (current manual process)

A patron telephones the library to request a book reservation. A Librarian checks physical
card catalogs and writes the reservation on a paper form. The form is placed in the patron
file cabinet. The patron calls back two days later to confirm. When the reserved book is
returned, the Librarian searches the cabinet for matching reservations, calls the patron by
phone, and waits for a callback to confirm pickup. If no callback within 3 days, the
Librarian makes a second call. If still no response, the reservation is cancelled manually.

Pain points identified: two phone-tag loops, 2-day delay between request and confirmation,
manual file search, no automated reminder, cancellation is purely manual.

#### To-Be Narrative (with LMS)

A patron logs into the online portal and searches the catalog. If the item is checked out,
the patron clicks Reserve. The LMS immediately records the reservation and sends a
confirmation email. When the reserved book is returned, the LMS automatically sends a hold
notification email with a 7-day pickup deadline. Three days before deadline expiry, the LMS
sends a reminder email. If the patron does not collect within 7 days, the reservation is
automatically cancelled and the next patron on the waitlist is notified.

Improvements: phone-tag eliminated, confirmation is instant, reminders are automated,
cancellation is rule-based and automatic.

---

### Section 9: ECBA Exam Preparation

#### BABOK Alignment

BPMN is listed in the BABOK Guide v3 as a technique under Business Process Modeling. The
ECBA exam tests recognition of BPMN elements and their correct application. Expected
question patterns:

- Identify the correct gateway type for a given scenario
- Identify whether a flow arrow should be sequence flow or message flow
- Identify which event type matches a described trigger or condition
- Determine whether a subprocess should be collapsed or expanded

#### Common Trap Questions

- An inclusive gateway is described as "one or more" — do not confuse with parallel
  ("all") or exclusive ("exactly one")
- An error boundary event attaches to an activity boundary — it is not a standalone event
  in the normal flow
- Terminate End Events kill the entire process — not just the current path — unlike None
  End Events which only end the current path

---

### Study Checklist

Work through each item before attempting the quiz.

- [ ] Can you name all four BPMN element categories?
- [ ] Can you draw and label all five gateway types from memory?
- [ ] Can you correctly identify start, intermediate, and end events by visual thickness?
- [ ] Can you explain when sequence flow crosses a lane versus when message flow crosses a pool?
- [ ] Can you describe the difference between collapsed and expanded subprocesses?
- [ ] Can you identify at least three As-Is pain points and their To-Be solutions?
- [ ] Can you explain why an inclusive gateway join behaves differently from a parallel join?
- [ ] Can you list five BPMN diagram quality checks?

---

### Key Terms Glossary

| Term | Definition |
|---|---|
| As-Is Model | Process diagram documenting the current state |
| BPMN | Business Process Model and Notation — OMG standard for process modeling |
| Call Activity | Reusable subprocess invoking a globally defined process |
| Collaboration | BPMN diagram showing two or more pools exchanging messages |
| Event-Based Gateway | Routes flow to whichever competing event occurs first |
| Exclusive Gateway | Routes flow to exactly one outgoing path |
| Inclusive Gateway | Routes flow to one or more outgoing paths based on conditions |
| Lane | Subdivision of a pool representing a role or department |
| Message Flow | Dashed arrow crossing pool boundaries to show communication |
| Parallel Gateway | Routes flow to all outgoing paths simultaneously |
| Pool | Container representing one process participant |
| Sequence Flow | Solid arrow showing order of activities within a pool |
| Subprocess | Activity containing a complete internal process |
| Terminate End | End event that kills all active process paths immediately |
| To-Be Model | Process diagram showing the improved future state |

---

*Reading Guide — Module 09 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

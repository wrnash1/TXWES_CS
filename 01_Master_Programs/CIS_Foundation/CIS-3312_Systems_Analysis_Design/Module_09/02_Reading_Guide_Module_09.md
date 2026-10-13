# Reading Guide: Module 09 — Process Modeling with BPMN

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3312 &BULL; SYSTEMS ANALYSIS & DESIGN</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


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

---

## 9. Supplemental Resources

The following open educational resources extend module content on BPMN and process modeling. All are freely accessible without login or purchase.

1. **BPMN 2.0 Specification — Object Management Group (OMG)**
   <https://www.omg.org/spec/BPMN/2.0/>
   Focus: The authoritative BPMN 2.0 specification. Review the element reference tables for gateway types, event types, and flow types to confirm notation details tested on the ECBA exam.

2. **BPMN Quick Reference Guide — BPMNQuickGuide.com**
   <https://www.bpmnquickguide.com/view-bpmn-quick-guide/>
   Focus: One-page visual reference card covering all standard BPMN 2.0 symbols with shape descriptions. Use this alongside the lab to ensure you are using correct BPMN shapes, not generic flowchart shapes.

3. **Introduction to Business Process Modeling — Coursera (free audit)**
   <https://www.coursera.org/learn/business-process-management>
   Focus: University-level course covering BPMN fundamentals, As-Is and To-Be modeling, and process improvement analysis. Supplements the process modeling content of this module.

4. **Process Improvement with BPMN — Camunda Academy (free)**
   <https://academy.camunda.com/>
   Focus: Free short courses on BPMN 2.0 notation and process modeling best practices from the makers of a leading open-source BPMN engine. Includes interactive exercises and quizzes.

5. **Draw.io BPMN Shape Library Tutorial — draw.io Blog**
   <https://www.drawio.com/blog/bpmn-2-0>
   Focus: Step-by-step guide to using draw.io's built-in BPMN shape library to create compliant BPMN diagrams. Directly supports the lab requirement to use BPMN-specific shapes rather than generic flowchart shapes.

*Reading Guide — Module 09 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

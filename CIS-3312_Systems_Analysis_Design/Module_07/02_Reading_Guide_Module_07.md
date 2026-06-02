# Reading Guide: Module 07 - Process Modeling with BPMN

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Introduction

Module 07 covers Business Process Model and Notation (BPMN), the international standard for modeling business processes. Maintained by the Object Management Group (OMG), BPMN provides a graphical language that bridges the communication gap between business stakeholders and technical teams. It is explicitly referenced in BABOK Guide v3 as a process modeling technique and is tested on the IIBA ECBA exam. BAs use BPMN to document current-state (as-is) and future-state (to-be) processes, identify inefficiencies, and communicate workflow logic with precision.

---

## 1. Core Vocabulary

### 1.1 Business Process Model and Notation (BPMN)

BPMN is an international standard (ISO/IEC 19510) for graphically modeling business processes. Every symbol in BPMN has a defined, standardized meaning — enabling consistent interpretation across organizations and industries. BPMN supports modeling at multiple levels: from high-level process overviews visible to executives to detailed flow diagrams used by developers for implementation.

### 1.2 Event

An event is something that happens during a process — a trigger or a result. Events are represented by circles. Three positional types exist: Start Events (thin circle — where the process begins), End Events (thick circle — where the process ends), and Intermediate Events (double-bordered circle — something that occurs mid-process). Event subtypes are indicated by icons inside the circle: envelope = message, clock = timer, lightning bolt = error.

### 1.3 Activity

An activity is work that is performed within a process. The two main activity types are Task (atomic, indivisible work — shown as a rounded rectangle) and Sub-process (compound activity containing its own internal flow — shown as a rounded rectangle with a plus sign at the bottom). Tasks can be typed: User Task (human action), Service Task (automated system action), Manual Task (physical action without system support).

### 1.4 Gateway

A gateway is a diamond shape that controls the routing of sequence flow — how the process branches and merges. Gateways are classified by their routing logic. The three gateways tested on the ECBA exam are Exclusive (X), Parallel (+), and Inclusive (O).

### 1.5 Exclusive Gateway (XOR)

An Exclusive Gateway (marked with X inside a diamond) routes flow along exactly one outgoing path based on a condition. The conditions on each outgoing path are mutually exclusive — only one can be true. When merging, an exclusive gateway passes through the first arriving token without waiting for others.

### 1.6 Parallel Gateway (AND)

A Parallel Gateway (marked with + inside a diamond) activates all outgoing paths simultaneously when splitting. When joining (merging), it waits until all incoming paths have completed before releasing the single outgoing flow. Use a parallel gateway when multiple activities must happen concurrently.

### 1.7 Inclusive Gateway (OR)

An Inclusive Gateway (marked with O inside a diamond) activates one or more outgoing paths based on which conditions are true. Unlike the exclusive gateway (exactly one), multiple paths may be active. The joining inclusive gateway waits for all active (triggered) paths to complete before proceeding.

### 1.8 Pool

A pool is a rectangular container representing a single participant in a process — an organization, department, or system. Each pool holds the complete internal process of that participant. Pools are used in collaboration diagrams to model interactions between two or more participants.

### 1.9 Lane

A lane is a subdivision within a pool. Lanes separate activities by role, department, or system within a single participant. All activities in a lane are performed by the role named on the lane. Lanes do not create separate participants — they organize responsibility within one participant.

### 1.10 Sequence Flow

Sequence flow is a solid arrow that represents the order of activities within a single pool. Sequence flow can only connect elements inside the same pool. Crossing a pool boundary with sequence flow is a BPMN rule violation.

### 1.11 Message Flow

Message flow is a dashed arrow with an open arrowhead that represents communication between two separate pools (participants). It crosses pool boundaries and carries a named message or data item. Message flow cannot connect elements within the same pool.

### 1.12 As-Is and To-Be Process Models

An as-is (current-state) process model documents how a process currently operates, including all its inefficiencies, redundancies, and pain points. A to-be (future-state) process model documents the improved process the organization wants to implement. BAs typically produce both — the gap between them defines the requirements for change.

---

## 2. BPMN Symbol Reference

| Symbol | Shape | Meaning |
|---|---|---|
| Start Event | Thin circle | Process begins here |
| End Event | Thick circle | Process ends here |
| Intermediate Event | Double-bordered circle | Something happens mid-process |
| Task | Rounded rectangle | Atomic unit of work |
| Sub-process | Rounded rectangle with + | Compound activity with internal flow |
| Exclusive Gateway | Diamond with X | Exactly one path; mutually exclusive |
| Parallel Gateway | Diamond with + | All paths simultaneously |
| Inclusive Gateway | Diamond with O | One or more paths |
| Sequence Flow | Solid arrow | Flow of control within a pool |
| Message Flow | Dashed arrow, open head | Communication between pools |
| Pool | Large rectangle | Single participant container |
| Lane | Subdivision of pool | Role or department within participant |

---

## 3. Gateway Comparison

| Gateway | Symbol | Splits to | Joins when | Use when |
|---|---|---|---|---|
| Exclusive (XOR) | X | Exactly one path | First token arrives | Conditions are mutually exclusive |
| Parallel (AND) | + | All paths | All paths complete | Activities must run concurrently |
| Inclusive (OR) | O | One or more paths | All active paths complete | Multiple conditions may be true |

---

## 4. BPMN Event Types

| Event Position | Shape | Meaning |
|---|---|---|
| Start Event | Thin single circle | Initiates the process |
| End Event | Thick single circle | Terminates the process |
| Intermediate Event | Double-bordered circle | Occurs during the process |
| Message Start | Thin circle with envelope icon | Process starts when a message is received |
| Timer Start | Thin circle with clock icon | Process starts at a scheduled time |
| Error End | Thick circle with lightning bolt icon | Process ends with an error condition |
| Boundary Intermediate | Double circle attached to activity edge | Interrupts or catches an event on an activity |

---

## 5. Sequence Flow vs. Message Flow

| Attribute | Sequence Flow | Message Flow |
|---|---|---|
| Appearance | Solid arrow | Dashed arrow with open arrowhead |
| Scope | Within one pool only | Between two different pools |
| Represents | Order of activities | Communication between participants |
| Rule if misused | Cannot cross pool boundary | Cannot stay within one pool |

---

## 6. BPMN vs. DFD Comparison

| Dimension | BPMN | DFD |
|---|---|---|
| Models | Process flow — sequence, decisions, events | Data flow — how data moves and transforms |
| Shows sequence | Yes — ordering of activities is explicit | No — data flows are not sequenced |
| Multi-participant | Yes — pools and message flows | Limited — external entities, no internal multi-party |
| Notation standard | OMG BPMN 2.0 (ISO 19510) | Yourdon-DeMarco or Gane-Sarson |
| Primary BABOK technique | Business Process Modeling (KA 5) | Data Flow Diagrams (KA 5) |

---

## 7. As-Is and To-Be Analysis

When BAs model processes in BPMN, they typically produce two versions. The as-is model documents the current process with all its actual steps, handoffs, decisions, and participants — including inefficiencies. Common inefficiencies visible in as-is models include unnecessary handoffs between lanes or pools, sequential activities that could run in parallel, redundant approval steps, missing exception handling, and activities with no defined owner.

The to-be model removes or improves these inefficiencies. Requirements for the new system are derived from the gap between the as-is and to-be models.

---

## 8. Certification Exam Tips

1. Gateway selection is the most frequently tested BPMN concept on the ECBA exam. Know the three gateways by symbol: X = exclusive (exactly one path), + = parallel (all paths), O = inclusive (one or more paths). When a question describes a branching scenario, identify whether the paths are mutually exclusive, all must run, or some combination may apply.

2. The sequence flow vs. message flow rule is directly tested. Sequence flow is a solid arrow that stays inside one pool. Message flow is a dashed arrow that crosses between pools. A sequence flow connecting elements in two different pools is always a modeling violation.

3. Event types are tested by icon. Know at minimum: thin circle = Start, thick circle = End, double circle = Intermediate. Know that message events use an envelope icon, timer events use a clock icon, and error events use a lightning bolt icon.

4. Pools represent participants; lanes represent roles within a participant. If a question describes separate organizations, they need separate pools. If a question describes roles within one organization, they need lanes within one pool.

5. A Parallel Gateway split must be matched with a Parallel Gateway join. If three paths are launched by a + gateway, a + gateway at the merge point waits for all three before proceeding. Mismatching gateway types at split and join is a common trap answer.

6. BPMN appears in BABOK Guide v3 KA 5 under the Business Process Modeling technique. When a scenario involves modeling activity sequence, decisions, and participant responsibilities, business process modeling (BPMN) is the correct technique.

7. As-is and to-be models are core BA deliverables. The as-is model reveals problems; the to-be model defines improvements. This distinction appears in BABOK KA 2 (Business Analysis Planning) and KA 6 (Solution Evaluation) as well as KA 5.

8. Sub-processes are collapsed compound activities. A rounded rectangle with a + symbol at the bottom contains an entire internal process. This is used when a process is too detailed to show inline without cluttering the diagram.

---

## 9. Required and Supplemental Reading

Required reading:

- BABOK Guide v3, Chapter 10 (Techniques) — Business Process Modeling
- BABOK Guide v3, KA 5: Requirements Analysis and Design Definition — Model Requirements task

Supplemental reading:

- OMG BPMN 2.0 Quick Reference Guide (free at omg.org) — gateway and event symbol summary
- Lucidchart BPMN tutorial (free) — practical notation reference with interactive examples

---

## 10. Study Checklist

- [ ] Draw a simple BPMN process from memory using all four core element types (event, activity, gateway, flow).
- [ ] Explain the difference between Exclusive, Parallel, and Inclusive Gateways with one example each.
- [ ] Draw a two-pool collaboration diagram with message flows and sequence flows correctly placed.
- [ ] Identify the three most common BPMN rule violations: sequence flow crossing pools, missing gateway join, black-hole activity.
- [ ] Draw an as-is BPMN model for a simple scenario and identify at least two inefficiencies.
- [ ] Watch the Module 07 video lecture.
- [ ] Complete the Module 07 lab activity.
- [ ] Post your initial discussion response by Wednesday at 11:59 PM.

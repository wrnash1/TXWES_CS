# Quiz: Module 09 — Process Modeling with BPMN

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Business Process Modeling

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 1

A BPMN process model shows a diamond shape with a plus sign (+) inside. At the point where
this gateway splits the flow, two outgoing paths are drawn. What will happen when execution
reaches this gateway?

A. The path with the highest-priority condition label will be taken.

B. The first outgoing path that evaluates to true will be taken, and the other will be
   skipped.

C. Both outgoing paths will execute simultaneously regardless of any conditions.

D. One or more outgoing paths will execute based on which conditions evaluate to true.

Correct Answer: C

Distractor Analysis:

- A is incorrect because priority-based routing is not a BPMN gateway behavior; BPMN
  gateways use type semantics, not priority rankings.
- B describes an Exclusive (XOR) gateway, not a Parallel gateway.
- D describes an Inclusive (OR) gateway, identified by an O inside the diamond, not a plus
  sign.

---

### Question 2

In a BPMN collaboration diagram, a Customer pool and a Vendor pool are shown. The process
analyst draws an arrow from a task in the Vendor pool to a task in the Customer pool to show
that the vendor sends an order confirmation to the customer. What type of arrow should be
used, and what is wrong if a solid arrow is used instead?

A. Message Flow (dashed arrow with open circle at source) should be used; a solid arrow
   would imply the vendor task and customer task are in the same sequence, which violates
   BPMN rules for cross-pool connections.

B. Sequence Flow (solid arrow) is correct here; pools can share sequence flow for
   communication.

C. Association (dotted line) should be used; associations connect artifacts to activities
   across pools.

D. Message Flow should be used; a solid arrow is acceptable as an informal notation
   variation when tools do not support dashed arrows.

Correct Answer: A

Distractor Analysis:

- B is incorrect because BPMN 2.0 explicitly prohibits sequence flow crossing pool
  boundaries. This is an absolute rule.
- C is incorrect because associations connect artifacts (data objects, annotations) to flow
  objects; they do not represent communication between participants.
- D is incorrect because BPMN notation is not optional or informally variable on this rule.
  Solid arrows between pools represent a modeling error regardless of tool limitations.

---

### Question 3

A business analyst is modeling a loan approval process. When an application is submitted,
three independent reviews must all be completed before a final decision can be made: a
credit check, an employment verification, and a collateral assessment. Which gateway type
should the analyst use to split the flow into the three reviews, and which type should be
used to synchronize before the final decision?

A. Exclusive Gateway split and Inclusive Gateway join

B. Parallel Gateway split and Parallel Gateway join

C. Inclusive Gateway split and Parallel Gateway join

D. Event-Based Gateway split and Exclusive Gateway join

Correct Answer: B

Distractor Analysis:

- A is incorrect because an Exclusive split would take only one of the three review paths,
  not all three. The Inclusive join would also be wrong because it waits for active paths
  only, but the semantics here require all three reviews.
- C is incorrect because an Inclusive split would allow one or more paths — not necessarily
  all three — which does not match the "must all complete" requirement.
- D is incorrect because an Event-Based gateway routes to whichever event occurs first, not
  to all concurrent paths.

---

### Question 4

A BPMN diagram shows a circle with a single thin outer ring and an envelope icon inside.
This symbol appears at the beginning of a process. What does it represent?

A. A Message End Event — the process ends by sending a message

B. A Send Intermediate Event — an outgoing message is sent during the process

C. A Message Start Event — the process is triggered when a message is received

D. A Receive Task — a task that waits for an incoming message before proceeding

Correct Answer: C

Distractor Analysis:

- A is incorrect because an End Event has a thick single-ring circle, not a thin ring. An
  End Event also appears at the end of a process path, not the beginning.
- B is incorrect because an Intermediate Event has a double-ring circle (two concentric
  lines), not a single thin ring.
- D is incorrect because a Receive Task is drawn as a rounded rectangle with an envelope
  icon, not as a circle.

---

### Question 5

An analyst is comparing an As-Is BPMN model and a To-Be BPMN model for the same process.
The As-Is model has 14 activities and 9 lane crossings. The To-Be model has 9 activities
and 3 lane crossings. What does the reduction in lane crossings most directly indicate?

A. The To-Be process has fewer decision points, which reduces branching logic complexity.

B. The To-Be process has fewer handoffs between roles or departments, which typically
   reduces delays and error opportunities.

C. The To-Be process is less expensive to implement because fewer people are involved.

D. The To-Be process uses parallel gateways to compress sequential steps.

Correct Answer: B

Distractor Analysis:

- A is incorrect because decision points are represented by gateways, not by lane
  crossings. A reduction in lane crossings does not directly indicate fewer gateways.
- C is incorrect because fewer handoffs does not necessarily mean fewer people — automation
  can reduce handoffs while keeping the same number of roles involved.
- D is incorrect because parallel gateways add concurrent paths, which would not reduce
  lane crossings; they might increase them if concurrent tasks span multiple lanes.

---

### Question 6

In BPMN 2.0, a subprocess is drawn as a rounded rectangle with a small plus sign at the
bottom center. A process analyst collapses the subprocess so only the outer boundary is
visible on the main diagram. What is the primary reason to use a collapsed subprocess
rather than showing all internal steps inline?

A. Collapsed subprocesses execute faster in process automation engines.

B. Collapsed subprocesses hide internal steps to maintain confidentiality from stakeholders
   who should not see implementation details.

C. Collapsed subprocesses keep the parent diagram readable at a high level while signaling
   that additional detail exists and is documented separately.

D. Collapsed subprocesses are required when the subprocess contains more than five tasks.

Correct Answer: C

Distractor Analysis:

- A is incorrect because diagram notation has no effect on process engine execution speed;
  this is a modeling concept, not a runtime optimization.
- B is incorrect because subprocess collapse is a diagram readability technique, not an
  access control mechanism. Stakeholder access is managed through document permissions, not
  diagram layout.
- D is incorrect because there is no BPMN rule mandating collapse based on task count;
  the choice is based on diagram readability and communication goals.

---

### Question 7

A BPMN process model for an insurance claim process has a gateway that routes the flow to
whichever of the following occurs first: the customer submits additional documentation, or
a 30-day timer expires. After either event occurs, the process continues to the next step.
Which gateway type is being described?

A. Parallel Gateway — because two paths exist

B. Exclusive Gateway — because exactly one outgoing path will be taken

C. Inclusive Gateway — because one or more of the events may occur

D. Event-Based Gateway — because the routing depends on which event occurs first

Correct Answer: D

Distractor Analysis:

- A is incorrect because a Parallel Gateway executes ALL outgoing paths simultaneously; it
  does not wait for a triggering event.
- B is incorrect because an Exclusive Gateway evaluates conditions on data, not on which
  event occurs first. The scenario describes a race between two competing events.
- C is incorrect because an Inclusive Gateway also evaluates data conditions; it does not
  route based on event arrival order.

---

### Question 8

A business analyst creates a BPMN diagram for a library book return process. One of the
end events in the diagram has a thick single-ring circle with an X inside. What does this
end event type mean, and how does it differ from a None End Event?

A. It is a Terminate End Event; it ends only the current path, leaving other parallel paths
   running.

B. It is an Error End Event; it throws an error condition that must be caught by the parent
   process.

C. It is a Terminate End Event; it immediately ends ALL active paths in the entire process
   instance.

D. It is a Cancel End Event; it cancels any pending compensation activities.

Correct Answer: C

Distractor Analysis:

- A reverses the definition of Terminate End; a None End Event ends only the current path.
  The Terminate End kills everything — that is what makes it distinct.
- B is incorrect because an Error End Event uses a lightning bolt icon, not an X, and
  throws an error condition rather than terminating all paths.
- D is incorrect because Cancel End Events are used specifically within transaction
  subprocesses and use a different icon.

---

### Question 9

A business analyst is reviewing a BPMN diagram created by a junior analyst. The diagram
shows a solid sequence flow arrow connecting a task in the Customer pool to a task in the
Order Management System pool. The senior BA immediately flags this as an error. Why?

A. Sequence flow arrows must always be horizontal; diagonal arrows are not valid in BPMN.

B. Sequence flow cannot cross pool boundaries; communication between pools must use
   message flow.

C. The task in the Customer pool cannot have an outgoing sequence flow because customers
   are always passive participants.

D. Solid arrows are reserved for data associations; process flow must use dashed arrows.

Correct Answer: B

Distractor Analysis:

- A is incorrect because arrow direction and angle have no prescribed orientation in BPMN;
  diagrams can use any layout direction.
- C is incorrect because pool participants — including customers — can initiate tasks with
  outgoing flows; the customer pool can have internal sequence flow. The problem is
  specifically that the arrow crosses the pool boundary.
- D reverses the notation rules; solid arrows are sequence flow and dashed arrows are
  message flow.

---

### Question 10

When building an As-Is process model, a business analyst should document inefficiencies,
workarounds, and manual steps even though those problems will be eliminated in the To-Be
model. Which of the following best justifies this practice?

A. Regulatory compliance requires documenting the current state before any process can
   be legally changed.

B. The As-Is model establishes a baseline for measuring improvement and surfaces embedded
   business rules that might otherwise be overlooked during To-Be design.

C. Stakeholders are more likely to approve the To-Be model if they can see how bad the
   current process is.

D. Process modeling tools require an As-Is input file before they can generate a To-Be
   diagram automatically.

Correct Answer: B

Distractor Analysis:

- A is incorrect because while some industries have regulatory documentation requirements,
  the general business analysis justification for As-Is modeling is analytical, not
  compliance-driven.
- C is incorrect because while contrast can be persuasive, the analytical purpose of the
  As-Is model is measurement and discovery, not persuasion. This answer describes a
  political tactic, not a methodology rationale.
- D is incorrect because no standard process modeling tool generates To-Be diagrams from
  As-Is inputs; the two models are independently created by the analyst.

---

*Quiz — Module 09 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

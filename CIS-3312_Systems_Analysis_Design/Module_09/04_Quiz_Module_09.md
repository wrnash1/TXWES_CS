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

---

### Question 11

A BPMN diagram for a patient intake process shows a task "Verify Insurance" followed by an Exclusive Gateway with two outgoing sequence flows: one labeled "Coverage Confirmed" and one labeled "No Coverage Found." Which element is missing that makes the gateway technically incomplete?

A. A default flow — one outgoing path should be marked as the default in case no condition evaluates to true

B. A message intermediate event on the "No Coverage Found" path to notify the billing department

C. A parallel gateway before the task to split the process for simultaneous insurance and identity verification

D. A terminate end event on the "No Coverage Found" path to stop the entire process

**Correct Answer: A**

**Distractor Analysis:**

- A is correct because BPMN best practice requires that an Exclusive Gateway include a default flow (marked with a slash on the outgoing arrow) as a fallback in case no condition evaluates to true, preventing the process from getting stuck.
- B is incorrect because a message event is a design choice for notification — it may or may not be needed depending on requirements, but it is not what makes the gateway technically incomplete.
- C is incorrect because the scenario describes sequential processing of one task followed by a decision; there is no requirement for parallel processing introduced by this scenario.
- D is incorrect because a terminate end event is a design choice for the no-coverage path — it might be appropriate depending on the process, but its absence does not make the gateway technically incomplete.

---

### Question 12

A BA is modeling a purchase approval process. Orders under $500 go directly to the warehouse. Orders $500–$5,000 require manager approval. Orders over $5,000 require VP approval. Which gateway type is most appropriate at the routing decision point?

A. Parallel Gateway — because all three approval levels may apply simultaneously

B. Event-Based Gateway — because the routing depends on which approval event occurs first

C. Inclusive Gateway — because multiple approval levels could apply to the same order

D. Exclusive Gateway — because exactly one of the three conditions will be true for any given order

**Correct Answer: D**

**Distractor Analysis:**

- A is incorrect because parallel processing would require all three approval paths to execute simultaneously, which contradicts the business rule that only one path applies.
- B is incorrect because the routing is based on data conditions (order amount), not on which external event occurs first.
- C is incorrect because only one amount range can apply to any given order — an order cannot simultaneously be under $500 and over $5,000.
- D is correct because exactly one condition is true for any given order: the amount falls in exactly one of the three defined ranges. An Exclusive Gateway routes to exactly one outgoing path.

---

### Question 13

In a BPMN Collaboration diagram, two pools represent a Customer and a Shipping Company. A dashed arrow connects a task in the Customer pool ("Submit Return Request") to a task in the Shipping Company pool ("Receive Return Request"). What does the dashed arrow represent?

A. A sequence flow showing the order of tasks within the Customer pool

B. A data association showing that a data object is passed between the two tasks

C. A message flow showing that a message is sent from one process participant to another

D. An annotation link providing a comment on the relationship between the two tasks

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect because sequence flow is a solid arrow and must stay within a single pool; it cannot cross pool boundaries.
- B is incorrect because data associations connect tasks to data objects within the same pool; cross-pool communication requires message flow.
- D is incorrect because annotation links connect text annotations to diagram elements; they use a different visual style and do not represent process flow.
- C is correct because message flow (dashed arrow with open arrowhead) represents communication between two separate process participants (pools). It models the submission of the return request as a message sent from the Customer to the Shipping Company.

---

### Question 14

A BA documents a To-Be process model for a grant application review system. The model shows that after initial screening, applications with scores above 80 proceed to full committee review while those below 80 are immediately rejected. Six months later, policy changes the threshold to 75. Which BPMN element should be updated to reflect this change?

A. The start event — the triggering condition for the process has changed

B. The sequence flow condition expression on the gateway outgoing flow — the data condition that routes applications has changed

C. The pool label — the pool represents the committee whose threshold has changed

D. The lane containing the screening task — the responsible party for screening has changed

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because the start event triggers the process initiation; the threshold change affects routing logic mid-process, not the trigger.
- C is incorrect because the pool label identifies the process participant; changing the threshold does not change who participates.
- D is incorrect because the threshold change does not alter who performs screening — it changes what happens after screening.
- B is correct because the routing condition on the Exclusive Gateway's outgoing flows encodes the business rule (score > 80). Changing the threshold to 75 requires updating the condition expression on the relevant sequence flow arrow.

---

### Question 15

A BA is reviewing a BPMN diagram and notices that a subprocess activity has a plus sign (+) marker at the bottom of its rounded rectangle shape. What does this marker indicate?

A. The subprocess is a compensation subprocess that reverses completed transactions when an error occurs

B. The subprocess contains an internal process that is collapsed — the details are defined elsewhere and not visible in the current diagram

C. The subprocess runs in parallel with the parent process

D. The subprocess is an ad-hoc subprocess where activities can be performed in any order

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because a compensation subprocess uses a rewind-arrow marker, not a plus sign.
- C is incorrect because a parallel subprocess marker is different; the plus sign specifically indicates a collapsed subprocess.
- D is incorrect because an ad-hoc subprocess uses a tilde (~) marker, not a plus sign.
- B is correct because the plus sign (+) on a subprocess shape indicates it is a collapsed subprocess — the internal process details are defined but not displayed in the current diagram view. Clicking or expanding the subprocess would reveal the internal flow.

---

### Question 16

A business analyst is modeling a customer complaint resolution process. After a complaint is filed, it can be resolved by the frontline agent OR escalated to a supervisor. If escalated, a timer boundary event on the supervisor review task will trigger after 48 hours if the supervisor has not responded. What type of BPMN element is the timer boundary event in this scenario?

A. Interrupting timer boundary event — if triggered, it cancels the supervisor review task and redirects flow

B. Non-interrupting timer boundary event — if triggered, a parallel escalation flow starts while the supervisor review task continues

C. Intermediate catching event — it pauses the entire process for 48 hours before proceeding

D. Start event — it initiates the supervisor review sub-process after the 48-hour window

**Correct Answer: A**

**Distractor Analysis:**

- B is incorrect because a non-interrupting boundary event (shown with a dashed circle) allows the task to continue running; if the requirement is to redirect flow because the supervisor has not responded, an interrupting event is appropriate.
- C is incorrect because an intermediate catching event is placed on the sequence flow, not attached to a task boundary; it does not represent a timeout on a specific task.
- D is incorrect because start events initiate processes; a timer attached to a running task is a boundary event, not a start event.
- A is correct because an interrupting timer boundary event (solid circle with clock icon) cancels the activity it is attached to when the timer fires. If the supervisor has not responded in 48 hours, the review task is cancelled and flow is redirected — the standard BPMN pattern for timeout escalation.

---

### Question 17

Which of the following best describes the purpose of a "lane" within a BPMN pool?

A. A lane separates two different process participants who cannot communicate directly

B. A lane subdivides a pool to show which role or department within the same participant is responsible for each task

C. A lane represents a time period or phase of the process, organizing tasks chronologically

D. A lane is an optional label used to group tasks by business function for documentation purposes only

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because separate participants with distinct processes are represented by separate pools, not lanes. Lanes are subdivisions within one participant's pool.
- C is incorrect because BPMN does not use lanes to represent time periods; swim lane diagrams in other notations may do this, but BPMN lanes represent responsibility assignment.
- D is incorrect because lanes are a semantic modeling element that assigns task responsibility — they are not merely documentation labels. Their placement affects who is responsible for each activity.
- B is correct because lanes partition a single participant's pool by role, department, or functional area. For example, a "Customer Service" pool might have lanes for "Agent," "Supervisor," and "System," each containing the tasks that role performs.

---

### Question 18

A BA creates an As-Is BPMN model showing that a bank loan approval process involves 14 manual handoffs, 3 data re-entry steps, and an average cycle time of 9 business days. The To-Be model eliminates re-entry through system integration and reduces handoffs to 6, targeting a 3-day cycle time. How should the BA measure whether the To-Be process has been successfully implemented?

A. Compare the number of BPMN diagram elements between the As-Is and To-Be models

B. Define measurable KPIs based on the As-Is baseline (handoff count, re-entry count, cycle time) and measure them in the deployed process

C. Ask stakeholders whether the new process feels faster and easier than the old one

D. Count the number of tasks eliminated between the As-Is and To-Be models

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because diagram element count is a model artifact metric, not a business performance metric. Fewer boxes in a diagram does not mean the process is faster.
- C is incorrect because subjective stakeholder sentiment is not a measurable performance indicator. The As-Is model established specific quantitative baselines that must be measured against specific quantitative outcomes.
- D is incorrect because task count is a process design metric, not a performance outcome metric. Eliminating tasks does not guarantee the target cycle time is achieved.
- B is correct because the As-Is model establishes a quantitative baseline (14 handoffs, 3 re-entry steps, 9-day cycle time). The To-Be model sets targets. After deployment, the same metrics must be measured in the live process to confirm improvement. This is the correct BABOK solution evaluation approach.

---

### Question 19

A BPMN diagram shows a Message Start Event at the beginning of an Order Fulfillment process. What does this start event type indicate about how the process begins?

A. The process begins automatically on a schedule defined by the message event configuration

B. The process begins when a message is received from an external participant — in this case, likely a customer order submission

C. The process begins when an internal system condition is met, such as inventory reaching a threshold

D. The process begins when a human actor manually clicks a start button in the system

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because a scheduled start is modeled by a Timer Start Event, not a Message Start Event.
- C is incorrect because a condition-based start is modeled by a Conditional Start Event; internal system thresholds do not use message start events.
- D is incorrect because a manually triggered process uses a None Start Event or a User Task; a Message Start Event is specifically triggered by receiving a message from another process or external participant.
- B is correct because a Message Start Event indicates that the process is initiated by receiving a message from an external participant — in an order fulfillment context, this is typically a customer submitting an order, which triggers the fulfillment process.

---

### Question 20

A BA is facilitating a To-Be process design session. One stakeholder proposes eliminating an approval step to speed up the process. Another stakeholder objects, saying the approval is required by the company's internal audit policy. How should the BA handle this conflict in the process design?

A. Remove the approval step from the To-Be model and document the policy as a constraint that can be waived

B. Keep the approval step in the To-Be model and note the audit policy as a business rule constraint; explore whether the approval can be automated to reduce cycle time without eliminating the control

C. Create two alternative To-Be models — one with and one without the approval — and let management choose

D. Escalate immediately to the project sponsor to make the final decision without further discussion

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because removing a step required by audit policy is a compliance risk; a BA cannot waive internal audit controls through process design.
- C is incorrect because creating two alternatives is a reasonable exploratory step, but the BA should first investigate whether the constraint can be satisfied in a less disruptive way before presenting competing designs.
- D is incorrect because immediate escalation without exploring solutions is premature; the BA has facilitation tools and analytical skills to explore solutions before escalating.
- B is correct because the BA's role is to help the team find solutions that satisfy both efficiency and compliance. Automating the approval — triggering it programmatically with system-generated data — can reduce cycle time while preserving the audit control. This is the analytical problem-solving approach expected of a BA.

---

*Quiz — Module 09 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

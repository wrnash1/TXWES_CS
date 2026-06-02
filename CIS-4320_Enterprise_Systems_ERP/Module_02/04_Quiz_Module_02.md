# Quiz: Module 02 - Business Process Management

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### Question 1

In BPMN 2.0, what element is used to categorize activities based on which department or role performs them?

- A) Task box
- B) Gateway diamond
- C) Swimlane (Pool/Lane)
- D) Event circle

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Swimlanes are horizontal or vertical bands that show which person, team, or system is responsible for each task — making handoffs between departments explicit and visible in the process diagram.
- *Why A is incorrect:* A task box represents a unit of work to be performed, not the party responsible for it.
- *Why B is incorrect:* Gateways direct logical splits in process routing (decisions), not ownership assignment.
- *Why D is incorrect:* Event circles mark start, intermediate, or end states in the process timeline, not role boundaries.

---

### Question 2

In BPMN 2.0, which of the following best describes a **gateway**?

- A) A rounded rectangle representing a single unit of work performed by one actor
- B) A diamond shape that routes process flow based on a condition or event, splitting or merging paths
- C) A circle marking the point where the process receives an external message or signal
- D) A thick border rectangle representing a high-level collapsed subprocess

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Gateways — exclusive (XOR), parallel (AND), and inclusive (OR) — are the decision and synchronization points in any BPMN diagram, represented by diamond shapes.
- *Why A is incorrect:* A rounded rectangle is the symbol for a task, not a gateway.
- *Why C is incorrect:* A circle is the symbol for an event; a message-catching event is a specific subtype, not a gateway.
- *Why D is incorrect:* A collapsed subprocess uses a rounded rectangle with a plus sign inside, not a thick border.

---

### Question 3

A business analyst discovers that a purchase order approval takes 4 days on average because the approver only checks email once a day. Which BPM concept best describes this problem?

- A) A gateway conflict caused by overlapping parallel paths
- B) A process bottleneck caused by a resource constraint at a single activity step
- C) A swimlane boundary violation where tasks cross into the wrong department
- D) An event trigger misconfiguration that fires the wrong start condition

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The approver's once-daily email check is a resource constraint creating a queue. BPM optimization would address this with automated notifications, escalation timers, or a mobile approval channel.
- *Why A is incorrect:* Gateway conflicts relate to routing logic, not to wait times caused by human behavior.
- *Why C is incorrect:* Swimlane violations are diagram-accuracy problems, not causes of real-world delays.
- *Why D is incorrect:* An event trigger controls when a process starts, not the pace of activities mid-process.

---

### Question 4

During an SAP S/4HANA implementation, the project team documents the company's current workflows before deciding how to configure the system. What BPM term describes this current-state documentation?

- A) TO-BE process mapping
- B) AS-IS process mapping
- C) Gap analysis deliverable
- D) BPMN event choreography

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* AS-IS (current state) mapping is the starting point of any BPM or ERP design engagement; it reveals inefficiencies and establishes the baseline for change.
- *Why A is incorrect:* TO-BE mapping describes the future-state process after the ERP system is configured and optimization changes are applied.
- *Why C is incorrect:* A gap analysis compares AS-IS to TO-BE to identify missing capabilities; it is a product of both maps, not the act of documenting the current state.
- *Why D is incorrect:* BPMN choreography describes interactions between multiple independent processes, not the documentation of a single internal workflow.

---

### Question 5

A process diagram shows that after a credit check passes, the system simultaneously notifies the warehouse AND sends a confirmation email to the customer. Which BPMN gateway type enables this behavior?

- A) Exclusive (XOR) gateway — routes to exactly one outgoing path
- B) Event-based gateway — waits for an external event before continuing
- C) Parallel (AND) gateway — activates all outgoing paths at the same time
- D) Inclusive (OR) gateway — activates one or more paths based on conditions

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* A parallel gateway activates all outgoing sequence flows simultaneously, enabling the warehouse notification and customer email to happen at the same time without conditions.
- *Why A is incorrect:* An exclusive gateway routes to exactly one path; only one of the two actions would fire, not both.
- *Why B is incorrect:* An event-based gateway waits for an external message or timer before choosing a path; it does not trigger concurrent paths.
- *Why D is incorrect:* An inclusive gateway activates one or more paths based on evaluated conditions; parallel is correct when all paths always fire unconditionally.

---

### Question 6

A Salesforce administrator is designing a Flow to automate the new account onboarding process. When an Account is created, the system must: (1) send a welcome email, AND (2) create a follow-up task for the account manager. The administrator wants both actions to happen immediately when the account is created. Which Flow element models this correctly?

- A) A Decision element (XOR) routing to either the email or the task depending on account type
- B) Two parallel branches after a record-triggered start, both actions firing simultaneously
- C) A Wait element that delays the task creation until the email has been delivered
- D) An Approval Process that requires an approver to authorize both actions before they fire

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Parallel branches in Salesforce Flow model the AND-gateway pattern — both actions fire simultaneously from the same trigger without conditions or sequencing between them.
- *Why A is incorrect:* A Decision element (XOR logic) routes to exactly one outcome based on conditions; it would fire either the email or the task, not both.
- *Why C is incorrect:* A Wait element introduces a time delay before an action; it does not enable simultaneous parallel execution.
- *Why D is incorrect:* An Approval Process requires human review before proceeding; automatic simultaneous actions do not need an approver.

---

### Question 7

During an SAP Activate implementation, the team holds workshops where they walk through each standard SAP process and compare it to the company's business requirements to identify gaps. Which phase does this activity belong to and what is the workshop called?

- A) Prepare phase — Fit-Gap analysis workshop
- B) Realize phase — System Integration Testing workshop
- C) Explore phase — Fit-to-Standard workshop
- D) Deploy phase — User Acceptance Testing workshop

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The Explore phase of SAP Activate is specifically dedicated to Fit-to-Standard workshops where the team documents how standard SAP processes cover business requirements and identifies gaps that require configuration decisions.
- *Why A is incorrect:* The Prepare phase handles project governance, team setup, and infrastructure; process design workshops have not yet started.
- *Why B is incorrect:* The Realize phase is where the team builds and configures the system based on design decisions already made in Explore; System Integration Testing happens late in Realize.
- *Why D is incorrect:* User Acceptance Testing occurs in the Deploy phase and involves end users validating the configured system, not business analysts identifying process gaps.

---

### Question 8

A company's Accounts Payable process currently requires the AP clerk to manually email the Finance Director every time an invoice exceeds $10,000 for secondary approval. The Finance Director is frequently out of the office, causing invoices to wait an average of 6 days. Which ERP automation feature most directly resolves this bottleneck?

- A) A database index on the invoice amount field to speed up search queries
- B) An automated escalation rule that reassigns approval authority to a designated backup approver if the primary approver does not respond within 48 hours
- C) A custom ABAP report listing all invoices over $10,000 for monthly review
- D) A new swimlane added to the process diagram assigning Finance Director tasks to the AP clerk

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Escalation rules are the BPM tool specifically designed for approval bottlenecks caused by unavailable approvers. The rule automatically routes the work item to a backup after the threshold time, eliminating the 6-day wait.
- *Why A is incorrect:* A database index improves query performance at the database layer; it has no effect on the approval routing bottleneck.
- *Why C is incorrect:* A monthly report is a reactive control that would identify the backlog after it has already grown; it does not prevent the bottleneck from occurring.
- *Why D is incorrect:* Reassigning a swimlane in a diagram changes the documentation but not the actual process; and assigning Finance Director tasks to the AP clerk would likely violate Separation of Duties controls.

---

### Question 9

A business process has a step where, based on a customer's credit rating, the order is either routed to standard fulfillment (for good credit) OR held for credit review (for poor credit) OR escalated to the VP of Sales (for borderline credit). Which BPMN gateway type correctly models this three-way routing decision?

- A) Parallel (AND) gateway — all three paths fire simultaneously
- B) Exclusive (XOR) gateway — exactly one of the three paths fires based on the credit rating evaluation
- C) Inclusive (OR) gateway — multiple paths may fire simultaneously
- D) Event-based gateway — the path depends on which external event arrives first

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* An exclusive gateway routes to exactly one outgoing path based on evaluated conditions. Since a customer cannot simultaneously have good credit and poor credit, the conditions are mutually exclusive — exactly one path fires.
- *Why A is incorrect:* A parallel gateway activates all paths simultaneously regardless of conditions; a credit-rated order cannot go to standard fulfillment and credit review at the same time.
- *Why C is incorrect:* An inclusive gateway can activate multiple paths, which is incorrect here — the routing is based on mutually exclusive credit rating outcomes.
- *Why D is incorrect:* An event-based gateway waits for an external trigger (like a message arriving); it does not evaluate data conditions like a credit rating field.

---

### Question 10

A company completes its AS-IS process mapping and TO-BE process design for a Salesforce implementation. The gap analysis reveals that one requirement — automatically generating a PDF proposal from opportunity data — cannot be met by standard Salesforce functionality. Which gap resolution approach is recommended first before considering custom code?

- A) Immediately engage a developer to write a custom Apex class to generate the PDF
- B) Evaluate whether a Salesforce AppExchange managed package or native feature (such as Salesforce CPQ or Document Generation) can meet the requirement declaratively
- C) Accept the gap and document it as a known limitation in the project risk register
- D) Remove the requirement from scope since Salesforce cannot support it natively

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The "configuration before customization" principle — central to both Salesforce and SAP implementation best practices — requires evaluating all declarative and AppExchange options before resorting to custom code. AppExchange managed packages often satisfy requirements that appear to need custom development.
- *Why A is incorrect:* Custom code is the highest-cost, highest-maintenance, and highest-risk option; it should only be chosen after declarative and packaged options have been exhausted.
- *Why C is incorrect:* Documenting a gap as a known limitation without exploring solutions is not a resolution — it is a deferral. Gaps must be actively resolved.
- *Why D is incorrect:* Removing valid business requirements from scope without evaluating alternatives fails the business; the correct response is to evaluate all available options before concluding that the requirement cannot be met.

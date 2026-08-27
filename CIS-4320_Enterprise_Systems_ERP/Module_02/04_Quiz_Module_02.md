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

---

### Question 11

(5 points)

A BPMN diagram uses a **circle with a thick border** as its final element. What does this symbol represent?

- A) An intermediate timer event that pauses the process for a set duration
- B) A terminate end event that ends the entire process instance immediately
- C) A parallel gateway that merges concurrent paths at the end of the process
- D) A collapsed subprocess that contains additional detail in a separate diagram

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A circle with a thick border is the BPMN symbol for an End Event. A filled/terminate end event variant ends the entire process instance. End events must terminate every BPMN diagram.
  - *Why A is incorrect:* A timer event uses a clock icon inside the circle and appears as an intermediate event, not a thick-bordered end event.
  - *Why C is incorrect:* A parallel gateway is a diamond shape with a plus sign; it does not use circle notation.
  - *Why D is incorrect:* A collapsed subprocess uses a rounded rectangle with a plus icon, not a thick-bordered circle.

---

### Question 12

(5 points)

Which of the following best describes the purpose of a **TO-BE process map** in an ERP implementation project?

- A) It documents how the business currently performs a process before any system changes
- B) It shows the ideal future-state process after ERP configuration and optimization changes are applied, serving as the design blueprint for system configuration
- C) It lists all gaps between the current system and the new ERP platform
- D) It records the test scripts used during User Acceptance Testing

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The TO-BE map is the future-state design — it shows how the process will work after the ERP is configured, eliminating manual steps and bottlenecks identified in the AS-IS map. It drives all configuration and training decisions.
  - *Why A is incorrect:* Documenting the current state before changes is the definition of AS-IS mapping, not TO-BE.
  - *Why C is incorrect:* The gap list is the product of comparing AS-IS to TO-BE; it is a separate deliverable, not the TO-BE map itself.
  - *Why D is incorrect:* Test scripts are created during the testing phase to validate the configured system; they are not the same as a process design document.

---

### Question 13

(5 points)

An order management process includes a step where the system checks customer credit. If credit is approved, the order proceeds to fulfillment. If credit is declined, the order is routed to the credit manager for manual review. If no credit decision is returned within 2 hours, an escalation email is sent. Which combination of BPMN elements models this scenario?

- A) One exclusive gateway for the approve/decline decision and one timer intermediate event for the 2-hour escalation
- B) One parallel gateway activating all three paths simultaneously
- C) One inclusive gateway routing all three conditions at the same time
- D) Two exclusive gateways with no timer events

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* The approve/decline routing is a mutually exclusive decision (XOR gateway). The 2-hour timeout is a timer boundary event or intermediate timer event that triggers the escalation path — a standard BPMN pattern for SLA enforcement.
  - *Why B is incorrect:* A parallel gateway fires all paths unconditionally; the order cannot simultaneously go to fulfillment and credit review.
  - *Why C is incorrect:* An inclusive gateway fires one or more paths based on conditions, but the three paths here are mutually exclusive outcomes, not overlapping conditions.
  - *Why D is incorrect:* Without a timer event, the 2-hour escalation trigger cannot be modeled; the timeout is an event-based behavior, not a data-condition gateway.

---

### Question 14

(5 points)

In Salesforce Flow Builder, which element is used to **retrieve a record** from the Salesforce database to use its field values later in the flow?

- A) Assignment element
- B) Decision element
- C) Get Records element
- D) Create Records element

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* The Get Records element queries the Salesforce database and stores the result in a flow variable, making field values available for subsequent decisions, updates, or actions in the flow.
  - *Why A is incorrect:* An Assignment element sets or modifies variable values within the flow; it does not query the database.
  - *Why B is incorrect:* A Decision element evaluates conditions to route the flow; it does not retrieve data from the database.
  - *Why D is incorrect:* Create Records inserts a new record into the database; it does not retrieve existing records.

---

### Question 15

(5 points)

A company's purchase-to-pay process includes these steps: (1) Purchase Requisition, (2) Purchase Order, (3) Goods Receipt, (4) Invoice Receipt, (5) Payment. This sequence is an example of which SAP process abbreviation?

- A) O2C (Order-to-Cash)
- B) R2R (Record-to-Report)
- C) P2P (Purchase-to-Pay / Procure-to-Pay)
- D) H2R (Hire-to-Retire)

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Purchase-to-Pay (P2P) — also called Procure-to-Pay — covers the full procurement cycle from creating a purchase requisition through final payment to the vendor. It spans SAP modules MM (procurement) and FI-AP (payment).
  - *Why A is incorrect:* O2C (Order-to-Cash) is the customer-facing sales process: order entry → delivery → invoicing → payment receipt. It is the mirror of P2P from the customer side.
  - *Why B is incorrect:* R2R (Record-to-Report) covers the financial close cycle: journal entries, reconciliations, and financial statement generation in the FI/CO modules.
  - *Why D is incorrect:* H2R (Hire-to-Retire) is the HR process spanning hiring through retirement, managed in SAP HCM/SuccessFactors.

---

### Question 16

(5 points)

During a BPM project, the team calculates that a specific approval step takes an average of 3.5 days and adds zero business value — it was created for a regulatory requirement that no longer exists. The team recommends eliminating it entirely. Which process improvement approach does this represent?

- A) Process automation — replacing a manual step with a system action
- B) Process elimination — removing a non-value-adding step from the workflow entirely
- C) Process parallelization — running the step concurrently with another step
- D) Process escalation — routing the step to a higher authority to resolve faster

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* When analysis reveals that a step adds no value and has no remaining justification, the correct BPM response is elimination — removing the step entirely from the process, not just making it faster or automated.
  - *Why A is incorrect:* Automation replaces a manual action with a system action but keeps the step in the process; the question states the step should be eliminated, not just automated.
  - *Why C is incorrect:* Parallelization runs steps simultaneously to save time, but the step still exists in the process. The correct answer removes it entirely.
  - *Why D is incorrect:* Escalation reroutes a task to a different actor for faster resolution; it does not eliminate the step from the process.

---

### Question 17

(5 points)

A business analyst creates a BPMN diagram and assigns the "Send Invoice" task to the Finance swimlane, but it is actually performed by the Sales team. Which BPMN best practice does this violate?

- A) Each swimlane must represent exactly one person, not a team
- B) Tasks must be assigned to the swimlane of the actor or system that actually performs them, not the actor that initiates the process
- C) Finance tasks must always appear in the leftmost swimlane by convention
- D) Invoicing tasks are always attributed to the customer swimlane in BPMN diagrams

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* BPMN swimlane assignment accuracy is fundamental — each task must reside in the lane of the role or system that executes it. Misassignment obscures accountability and produces incorrect handoff analysis.
  - *Why A is incorrect:* BPMN swimlanes can represent teams, departments, or systems — not just individuals. There is no requirement that a lane represent exactly one person.
  - *Why C is incorrect:* There is no BPMN standard requiring Finance to appear in any particular positional order; lane order is a design choice for readability.
  - *Why D is incorrect:* Customers may appear as an external pool in BPMN, but invoicing tasks are assigned based on who performs them — typically the billing department, not the customer.

---

### Question 18

(5 points)

What is the primary difference between a **process** and a **procedure** in business process management?

- A) A process describes the sequence of activities that produce a business outcome; a procedure is the detailed step-by-step instructions for how to perform a specific activity within a process
- B) A process is performed by automated systems only; a procedure is performed by humans only
- C) A process is documented in BPMN; a procedure is documented in plain text only
- D) A process and a procedure are synonymous terms used interchangeably in BPM

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* A process is the higher-level flow of activities (e.g., the invoice approval process with 5 steps), while a procedure provides granular instructions for performing one activity (e.g., how to enter an invoice in SAP transaction code MIRO).
  - *Why B is incorrect:* Processes include both automated and human steps; procedures can describe both system interactions and manual actions.
  - *Why C is incorrect:* Both processes and procedures can be documented in BPMN or plain text; the notation format does not define the distinction.
  - *Why D is incorrect:* Process and procedure are distinct concepts in BPM. Treating them as synonymous leads to poor documentation that conflates design-level and execution-level content.

---

### Question 19

(5 points)

A company measures its invoice approval process and finds the **cycle time** is 8 days, but the **value-added time** is only 45 minutes. What does this metric reveal about the process?

- A) The process is highly efficient because 8 days is within industry benchmark for invoice approval
- B) The process has severe waste — 7+ days are spent waiting, routing, or in non-value-adding steps, representing a major BPM improvement opportunity
- C) The 45-minute value-added time confirms the process is automated and requires no human intervention
- D) Cycle time and value-added time are the same metric expressed in different units

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* When cycle time (total elapsed time) vastly exceeds value-added time (time actually spent doing productive work), it reveals that most of the elapsed time is waste — waiting in queues, sitting in email inboxes, or flowing through unnecessary approval steps. This is a primary BPM optimization signal.
  - *Why A is incorrect:* The comparison is not to an industry benchmark; the comparison is between cycle time and value-added time within the same process. A large gap between the two is waste by definition.
  - *Why C is incorrect:* A short value-added time does not imply automation; it simply means productive work is completed quickly. The bottleneck is in the wait time, not the execution time.
  - *Why D is incorrect:* Cycle time and value-added time are entirely different metrics. Cycle time includes all elapsed time; value-added time is only the portion where productive work occurs.

---

### Question 20

(5 points)

In SAP Activate, which methodology principle discourages extensive custom ABAP development and instead promotes using standard SAP processes as delivered, modifying business practices to fit the system rather than modifying the system to fit current practices?

- A) Agile sprint delivery
- B) Fit-to-Standard (consume standard, minimize customization)
- C) User Acceptance Testing (UAT) sign-off
- D) Hypercare stabilization

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* "Fit-to-Standard" is a core SAP Activate principle that prioritizes adopting SAP's best-practice processes over customizing the system. Customization increases cost, risk, and upgrade complexity. SAP Activate workshops are specifically designed to show standard processes and gain business acceptance of them.
  - *Why A is incorrect:* Agile sprint delivery describes the iterative work packaging approach in SAP Activate; it is a delivery cadence, not a principle about customization philosophy.
  - *Why C is incorrect:* UAT sign-off is the business approval gate at the end of testing; it validates the built system but does not describe the design philosophy.
  - *Why D is incorrect:* Hypercare is the intensive post-go-live support period; it is a delivery phase activity, not a design principle about customization.

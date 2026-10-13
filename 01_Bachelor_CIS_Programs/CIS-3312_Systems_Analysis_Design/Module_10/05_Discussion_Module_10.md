# Discussion Forum: Module 10 — Data Flow Diagrams and System Models

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Forum Instructions

Post an original response to ONE of the three scenarios below (A, B, or C). Your initial
post must be 175–225 words written in complete sentences. After posting, reply to at least
two classmates who responded to a different scenario. Each peer reply must be at least 60
words and must engage with the substance of your classmate's argument — not simply agree.

**Due dates:** Initial post due by Thursday 11:59 PM. Peer replies due by Sunday 11:59 PM.

---

### Scenario A — Scoping with a Context Diagram

A project team is building a new expense reimbursement system for a mid-size company. The
project manager tells the BA that the new system needs to connect to the company's HR
system to validate employee IDs, integrate with the company's accounting system to post
approved expenses, and email employees when their reimbursements are processed.

During the scope discussion, two team members disagree: one argues the HR system should be
modeled as a process inside the expense reimbursement system. The other argues it should
be modeled as an external entity. The accounting system integration is similarly disputed.

Respond to this scenario: Explain the criterion for deciding whether a component should be
modeled as a process inside the system or as an external entity. Apply that criterion to
both the HR system and the accounting system. Describe what the context diagram for this
expense reimbursement system would show, including the process bubble, external entities,
and at least four labeled data flows.

---

### Sample Response A

The criterion for distinguishing a process from an external entity in a DFD is organizational
ownership and control. If the system being built owns and controls the internal logic of a
component, that component is modeled as a process inside the system boundary. If the logic
belongs to a separate system or organization that the project team does not build, own, or
control, that component is modeled as an external entity outside the system boundary.

Applying this criterion to both disputed components: the HR system is an independent system
managed by a separate IT department with its own data structures and business logic. The
expense reimbursement project team neither builds nor controls it. It should be modeled as
an external entity. The same reasoning applies to the accounting system — it exists
independently and the team only defines the data interface with it, not the internal
accounting logic. Both are external entities, not processes.

The context diagram for the expense reimbursement system would contain one process bubble
labeled "Expense Reimbursement System" in the center. External entities would include:
Employee, Manager, HR System, and Accounting System. Data flows would include: Employee
submits Expense Report to the system, Manager sends Approval Decision to the system, the
system sends Employee Validation Request to HR System and receives Employee Status in
return, the system sends Approved Expense Record to the Accounting System and receives
Posting Confirmation in return, and the system sends Reimbursement Notification to the
Employee. No data stores appear on the context diagram — those are introduced at Level 1.

---

### Peer Reply Guidance for Scenario A

When replying to a classmate's Scenario A post, evaluate: Did they correctly apply the
own-and-control criterion? Did their context diagram include data stores by mistake? Are
their data flow labels noun phrases or did they slip into verb phrases? Can you identify a
data flow they may have missed?

---

### Scenario B — DFD Error Diagnosis

A student submits the following DFD fragment description for peer review:

The diagram shows a data store labeled "D3 Patient Records" with an arrow going directly
from an external entity labeled "Insurance Company" to the data store. A second process
bubble labeled "Generate Claim Report" has two outgoing arrows labeled "Claim Summary"
going to two different external entities but has no incoming arrows from any source. A
third process bubble labeled "Verify Coverage" has one arrow entering from D3 Patient
Records and no arrows exiting.

Respond to this scenario: Identify the name and explanation of each DFD error present in
the fragment. For each error, state which DFD element is affected, what rule it violates,
and what specific correction is required to resolve the error.

---

### Sample Response B

The DFD fragment described contains three distinct errors, each violating a fundamental
rule of data flow diagram notation.

The first error is a Direct Entity-to-Store connection. The Insurance Company external
entity is connected directly to the D3 Patient Records data store with no process bubble
between them. The rule violated is that external entities must always interact with data
stores through a mediating process — they cannot read from or write to data stores directly.
The correction is to insert a process bubble between the Insurance Company and the data
store, such as "Validate Insurance Claim," with the incoming data flow from the Insurance
Company entering the process and a separate read-arrow from D3 Patient Records also
entering the process.

The second error is a Miracle. The "Generate Claim Report" process produces two outgoing
data flows but has no incoming arrows. Every process must consume input data to produce
output — data cannot be generated from nothing. The correction is to add the required input
data flows to the process, likely from D3 Patient Records and from the output of a
verification process upstream.

The third error is a Black Hole. The "Verify Coverage" process receives one incoming data
flow from D3 Patient Records but has no outgoing arrows. The process consumes data without
producing any result. The correction is to add at least one outgoing data flow showing
where the verified coverage result goes — likely to the Generate Claim Report process or
to an output going back to the Insurance Company or treating physician.

---

### Peer Reply Guidance for Scenario B

When replying to a classmate's Scenario B post, consider: Did they correctly name all three
errors? Did they distinguish Black Hole from Miracle accurately? Did they propose a specific
correction with a process name and data flow label, or just a vague suggestion? Can you
propose a more precise correction for any of the three?

---

### Scenario C — DFD vs. BPMN: Choosing the Right Tool

A business analyst on a healthcare IT project is tasked with documenting a patient intake
process. Her supervisor asks for a model that shows the data the system needs to capture
and how that data flows through the system. A team member suggests using a BPMN swimlane
diagram instead of a DFD because the team already used BPMN in a previous project phase.

Respond to this scenario: Explain the fundamental difference between what a DFD models
and what a BPMN diagram models, using specific features of each notation as evidence.
Recommend which tool the analyst should use for this specific request and justify the
recommendation. Then identify one situation in the same project where BPMN would be the
better choice, and explain why.

---

### Sample Response C

Data Flow Diagrams and BPMN process models answer different analytical questions, and
understanding the distinction determines which tool serves a given communication need. A
DFD models data transformation — it shows where data originates, how processes transform it,
where it is stored, and where it ultimately goes. It is explicitly designed to expose data
requirements: what data the system must capture, store, and produce. A BPMN diagram models
process control flow — it shows the sequence of activities, decision gateways, event
triggers, and participant responsibilities. BPMN can show who does what and in what order;
it does not show data stores or data transformation in any systematic way.

For the supervisor's specific request — documenting the data the system needs to capture
and how it flows — a DFD is the clearly appropriate tool. The context diagram will identify
all data flows entering and leaving the system from external parties such as the Patient,
Referring Physician, and Insurance Carrier. The Level 1 DFD will show data stores like
D1 Patient Demographics, D2 Insurance Records, and D3 Medical History, along with how each
intake process reads and writes those stores. BPMN cannot expose this data architecture
because it has no standard representation for data stores.

However, BPMN would be the better choice later in the project when the team needs to model
the step-by-step sequence of the triage process — who assesses the patient first, what
decision criteria determine priority, and which staff roles are responsible for each action.
That sequential, role-based workflow requires swimlanes, gateways, and event triggers that
DFDs cannot express. Each tool has a precise purpose; using the right one for each question
produces clearer and more useful requirements documentation.

---

### Peer Reply Guidance for Scenario C

When replying to a classmate's Scenario C post, consider: Did they clearly articulate the
data-focus of DFDs versus the control-flow-focus of BPMN? Is their recommended BPMN use
case genuinely better suited to BPMN than to a DFD? Can you think of a feature of DFDs
they did not mention that further supports the recommendation?

---

### Discussion Rubric

| Criterion | Excellent (10) | Proficient (7) | Developing (4) | Beginning (1) |
|---|---|---|---|---|
| Accuracy of DFD concepts | All elements and rules correctly stated | Minor error in one rule or element | One significant conceptual error | Multiple errors or core concept missing |
| Depth of analysis | Reasoning is specific and scenario-grounded | Some specific reasoning | Mostly general or surface-level | Restates scenario without analysis |
| Word count and completeness | 175–225 words; all required elements addressed | 150–175 words; most elements present | Under 150 words; one element missing | Under 100 words or major element absent |
| Peer reply quality | Engages with classmate's reasoning; adds new insight | Brief engagement with some extension | Agreement without substantive engagement | One sentence or off-topic |
| Writing quality | Professional sentences; no errors | 1–2 minor errors | 3–4 errors affecting clarity | Frequent errors impeding understanding |

---

### Professor Nash Note

For Scenario B — the error identification question — I am looking for the specific error
name, not just a description of what looks wrong. Use the formal names: Black Hole, Miracle,
and Direct Entity-to-Store connection. Using vague language like "the arrow is wrong" or
"the process is missing something" will not earn full credit. Practice identifying these
errors by name before posting, and use the error reference table in the Reading Guide as
your checklist.

---

*Discussion Forum — Module 10 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

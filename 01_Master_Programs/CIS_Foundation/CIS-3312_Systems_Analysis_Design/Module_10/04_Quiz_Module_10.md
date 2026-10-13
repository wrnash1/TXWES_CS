# Quiz: Module 10 — Data Flow Diagrams and System Models

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

## Certification Alignment: IIBA ECBA — Requirements Analysis and Design Definition

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 1

In Yourdon-Coad DFD notation, which shape is used to represent a process?

A. A square or rectangle with the process name inside

B. An open rectangle formed by two parallel horizontal lines with the left end open

C. A circle or bubble with the process name and number inside

D. A diamond with the process name inside and condition labels on outgoing arrows

Correct Answer: C

Distractor Analysis:

- A describes an External Entity, which represents a person, system, or organization
  outside the system boundary that sends or receives data.
- B describes a Data Store, which represents data at rest — a file, database table, or
  other persistent storage.
- D describes a gateway or decision symbol used in flowcharts or BPMN, which does not
  appear in DFDs at all.

---

### Question 2

A business analyst is drawing a context diagram for a hospital patient scheduling system.
How many process bubbles should the context diagram contain?

A. One process bubble representing the entire system

B. One process bubble per external entity interacting with the system

C. One process bubble per major functional area of the system

D. As many process bubbles as needed to show all data stores

Correct Answer: A

Distractor Analysis:

- B is incorrect because the number of process bubbles in a context diagram is always
  exactly one, regardless of how many external entities are involved.
- C describes the structure of a Level 1 DFD, not a context diagram. Level 1 DFDs explode
  the single process into functional areas.
- D is incorrect because data stores do not appear in context diagrams at all; they first
  appear at Level 1.

---

### Question 3

A DFD shows a process bubble labeled "Calculate Invoice Total." Two arrows enter the
bubble from data stores. No arrows exit the bubble. What type of DFD error is this, and
what does it indicate about the requirements?

A. A Miracle error — the process generates output without consuming input, indicating a
   missing data source requirement

B. A Black Hole error — the process consumes input without producing output, indicating
   that the destination of the calculated invoice total has not been specified

C. An unlabeled data flow error — the arrows should have noun-phrase labels, not directional
   indicators

D. A direct entity-to-store error — process bubbles should not connect to data stores
   without an intermediate step

Correct Answer: B

Distractor Analysis:

- A reverses the error definitions. A Black Hole has inputs but no outputs; a Miracle has
  outputs but no inputs. This scenario clearly shows two inputs and no outputs, making it
  a Black Hole.
- C is incorrect because the scenario says arrows exist and the issue is their direction and
  destination, not their labeling.
- D is incorrect because process bubbles connecting to data stores is normal and expected
  in DFDs. The error here is the absence of outgoing flows, not the connection type.

---

### Question 4

A business analyst creates a Level 1 DFD for a payroll system. One of the Level 1 processes
is "3.0 Calculate Payroll." This process has three incoming data flows and two outgoing data
flows in the Level 1 DFD. The analyst then creates a Level 2 DFD that expands Process 3.0.
Which of the following is a balancing error?

A. The Level 2 DFD contains an internal data store not shown in the Level 1 DFD.

B. The Level 2 DFD shows only two of the three incoming data flows from the Level 1 boundary.

C. The Level 2 DFD numbers its sub-processes as 3.1, 3.2, and 3.3.

D. The Level 2 DFD includes all five Level 1 boundary flows and adds two new internal flows
   between sub-processes.

Correct Answer: B

Distractor Analysis:

- A is not an error. New internal data stores may appear at Level 2 to show detail that was
  hidden inside the parent process. These do not introduce new boundary flows.
- C is correct numbering convention. Level 2 processes under parent 3.0 are numbered
  3.1, 3.2, 3.3, and so on.
- D is not an error. All five boundary flows are present and new internal flows between
  sub-processes are expected and acceptable at Level 2.

---

### Question 5

In a DFD for a library system, a patron wants to search the catalog. The correct way to
model the data exchange is: the Patron external entity sends a "Catalog Search Query" to
a process, and the process returns "Search Results" to the Patron. A student draws the
model differently: the Patron is connected directly to the Catalog data store with a
bidirectional arrow and no process bubble. What is wrong with the student's model?

A. External entities cannot have bidirectional arrows — all arrows must be unidirectional.

B. External entities cannot connect directly to data stores; a process must mediate all
   interactions between external entities and data stores.

C. The Catalog data store should be replaced by a process because search implies an action.

D. The student should draw two separate one-way arrows instead of a bidirectional arrow.

Correct Answer: B

Distractor Analysis:

- A is incorrect because bidirectional arrows are valid in DFDs when data flows in both
  directions between two elements; the issue here is not arrow direction but element
  connection type.
- C is incorrect because a data store correctly represents the catalog as a repository of
  book records. The search action belongs in a process bubble, but the catalog itself
  remains a data store.
- D is incorrect because arrow style is not the problem; the fundamental error is an
  external entity bypassing a process to connect directly to a data store.

---

### Question 6

A data flow arrow in a DFD is labeled "Performs Authentication." A senior analyst flags
this label as incorrect. What is wrong with the label, and what would be a correct
replacement?

A. The label is too short; it should include the actor name and the action performed.

B. The label uses a verb phrase describing an action rather than a noun phrase describing
   the data being transferred; a correct label would be "Authentication Request" or
   "Authentication Credentials."

C. The label should be in passive voice to conform to structured analysis naming standards.

D. The label should match the name of the process bubble it connects to.

Correct Answer: B

Distractor Analysis:

- A is incorrect because data flow labels should be concise noun phrases; longer labels
  including actor names would be redundant since actors are already shown as external
  entities or lanes.
- C is incorrect because passive voice is not a DFD labeling requirement. Noun phrases
  are the standard, regardless of voice.
- D is incorrect because data flow labels name the data, not the process. A flow named
  after its connected process would be circular and uninformative.

---

### Question 7

Which of the following best describes the primary difference between a context diagram
and a Level 1 DFD?

A. A context diagram uses Gane-Sarson notation while a Level 1 DFD uses Yourdon-Coad
   notation.

B. A context diagram shows the system as a single process with all external interactions;
   a Level 1 DFD explodes the system into major functional processes and introduces data
   stores.

C. A context diagram is used for current-state modeling while a Level 1 DFD is used for
   future-state modeling.

D. A context diagram includes decision gateways while a Level 1 DFD uses only data flows
   without decision logic.

Correct Answer: B

Distractor Analysis:

- A is incorrect because both context diagrams and Level 1 DFDs are drawn in the same
  notation — either Yourdon-Coad or Gane-Sarson, chosen consistently throughout a
  project.
- C is incorrect because both diagram types can model either current-state or future-state
  systems. The level of abstraction distinction is independent of the As-Is/To-Be
  distinction.
- D is incorrect because neither context diagrams nor Level 1 DFDs use decision gateways.
  DFDs do not show control flow or decision logic at any level.

---

### Question 8

A DFD process bubble labeled "1.0 Manage Reservations" has the following flows in the
Level 1 DFD: three incoming flows and four outgoing flows. A Level 2 DFD is created to
expand this process. The Level 2 diagram shows the three incoming boundary flows and three
of the four outgoing boundary flows. The fourth outgoing flow is missing. What term
describes this situation, and what must the analyst do?

A. This is a leveling error; the analyst must add the missing outgoing boundary flow to the
   Level 2 diagram to restore balance.

B. This is a miracle error; the analyst must add an input to replace the missing flow.

C. This is an acceptable simplification; Level 2 diagrams may omit minor flows from the
   parent.

D. This is a scope reduction; the analyst should remove the missing flow from the Level 1
   DFD to maintain consistency.

Correct Answer: A

Distractor Analysis:

- B is incorrect because a miracle describes a process with outputs but no inputs; the
  situation here is a missing output boundary flow in the Level 2 diagram, which is a
  balancing/leveling issue.
- C is incorrect because no DFD flows may be omitted from a lower-level diagram if they
  appeared on the parent. Balancing is a non-negotiable quality requirement.
- D is incorrect because removing the flow from Level 1 would eliminate a documented
  requirement. The correction must be made to Level 2 to match Level 1, not the reverse.

---

### Question 9

A business analyst is deciding whether to model a component as an external entity or as a
process inside the system. The component is a credit scoring service run by a third-party
financial company. The system will send applicant data to this service and receive a score
in return, but the system cannot access or control the scoring logic. How should this
component be modeled?

A. As a process inside the system, because the system sends data to it

B. As a data store, because the credit scores are stored and retrieved

C. As an external entity, because the organization running the system does not own or
   control the credit scoring logic

D. As a subprocess, because it performs a specialized calculation

Correct Answer: C

Distractor Analysis:

- A is incorrect because the test for process vs. external entity is not whether data is
  sent to it, but whether the system owns and controls its internal logic. The system
  does not control the scoring algorithm.
- B is incorrect because a data store represents persistent storage at rest. The credit
  scoring service is an active participant that processes data and returns results.
- D is incorrect because a subprocess is an internal activity within the system boundary.
  An external third-party service is by definition outside the system boundary.

---

### Question 10

Which of the following is a valid data flow label for an arrow connecting a Patron external
entity to a Catalog Management process in an LMS DFD?

A. Search

B. Patron searches the catalog for a book by title

C. Catalog Search Query

D. SQL SELECT statement with title parameter

Correct Answer: C

Distractor Analysis:

- A is incorrect because "Search" is a verb, not a noun phrase describing data content.
  Data flow labels must name what data is being transferred, not what action is occurring.
- B is incorrect because it is a sentence describing behavior, not a data label. It also
  reveals implementation intent rather than identifying the data object.
- D is incorrect because it is an implementation-specific technical detail. DFDs are
  logical models that should be technology-independent. SQL syntax has no place in a
  DFD data flow label.

---

---

### Question 11

A DFD for an insurance claims system shows the following: External Entity "Claimant" → Process 1.0 "Submit Claim" → Data Store DS-1 "Claims." A second path shows Process 1.0 → External Entity "Fraud Detection Service." Which DFD element is missing for the Fraud Detection Service path to be correctly modeled?

A. A data store between Process 1.0 and the Fraud Detection Service to buffer the claim data

B. A labeled data flow arrow showing what data is sent from Process 1.0 to the Fraud Detection Service

C. A second process bubble between Submit Claim and Fraud Detection Service

D. A pool boundary separating the internal process from the external entity

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because a buffering data store is not required for every external entity interaction; data can flow directly from a process to an external entity via a labeled data flow arrow.
- C is incorrect because adding an intermediate process where none is needed introduces unnecessary complexity. The path from Process 1.0 to the external service can be direct.
- D is incorrect because pool boundaries are a BPMN concept; DFDs use system boundary rectangles and external entity boxes, not pool notation.
- B is correct because every arrow in a DFD must be a labeled data flow identifying what data is transferred. The path from Process 1.0 to Fraud Detection Service requires a named data flow arrow describing the data being sent (e.g., "Claim Details for Review").

---

### Question 12

In a Gane-Sarson DFD, which shape is used to represent a process?

A. A rectangle with double lines on the left edge

B. A circle (bubble)

C. A rounded rectangle with straight edges

D. A rounded rectangle with a split top section containing the process number

**Correct Answer: D**

**Distractor Analysis:**

- A is incorrect because a rectangle with double lines on the left edge represents an external entity in the Gane-Sarson notation.
- B is incorrect because circles represent processes in the Yourdon-Coad notation, not Gane-Sarson.
- C is incorrect because a plain rounded rectangle is not a standard DFD process symbol in either major notation.
- D is correct because Gane-Sarson uses a rounded rectangle with a horizontal split — the top section contains the process identifier number and the bottom section contains the process name. This is the defining visual distinction between Gane-Sarson and Yourdon-Coad process notation.

---

### Question 13

A BA is reviewing a DFD and finds a data store labeled "DS-3 Audit Log" that has only outgoing data flows and no incoming data flows. Which DFD error does this represent?

A. Black hole — DS-3 receives data but produces no output

B. Miracle — DS-3 produces data without receiving any input to store

C. Level balancing violation — DS-3 should appear in the parent diagram

D. External entity violation — audit logs must be modeled as external entities

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because a black hole has inputs with no outputs — the opposite of what is described. DS-3 has outputs (outgoing flows) but no inputs.
- C is incorrect because level balancing concerns boundary flows between DFD levels, not the input/output completeness of a data store.
- D is incorrect because audit logs are internal persistent storage, which is correctly modeled as a data store. External entities are organizations or systems outside the system boundary.
- B is correct because a data store with only outgoing flows and no incoming flows implies the data materializes with no process ever writing to it — a miracle. A data store must receive data from at least one process before it can supply data to another process.

---

### Question 14

A BA is creating a Level 1 DFD for a hotel reservation system. The context diagram shows data flows: "Reservation Request" (from Guest to System) and "Confirmation Email" (from System to Guest). Which of the following Level 1 diagrams correctly balances with this context diagram?

A. Level 1 shows "Reservation Request" entering the system boundary and "Booking Confirmation" leaving — using a different name for the outgoing flow

B. Level 1 shows "Reservation Request" entering and "Confirmation Email" leaving — matching the exact flow names from the context diagram

C. Level 1 shows only "Reservation Request" entering — the confirmation email can be added later

D. Level 1 shows three new data flows not present in the context diagram

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because level balancing requires that the same data flows cross the boundary at both levels. Renaming a flow between levels breaks traceability and constitutes an unbalanced DFD.
- C is incorrect because both boundary flows from the context diagram must appear at Level 1. Omitting the confirmation email creates an unbalanced diagram.
- D is incorrect because Level 1 boundary flows must match Level 1 exactly; new flows not in the context diagram represent an unbalanced expansion of scope.
- B is correct because level balancing requires that every data flow crossing the system boundary at the context diagram also appears crossing the system boundary at Level 1, with the same names and directions.

---

### Question 15

Which of the following DFD process names follows the recommended verb-noun naming convention?

A. Customer Data

B. Order Processing System

C. Validate Member Eligibility

D. IS-3 Database Function

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect because "Customer Data" is a noun phrase with no verb — it sounds like a data store name, not a process name describing a transformation.
- B is incorrect because "Order Processing System" is a system name, not a process verb-noun label. It also implies the entire system rather than a single transformation step.
- D is incorrect because "IS-3 Database Function" is a technical implementation reference, not a descriptive verb-noun process name. Process names must describe what transformation occurs, not where it occurs technically.
- C is correct because "Validate Member Eligibility" follows the verb-noun convention: the verb "Validate" describes the action (transformation), and "Member Eligibility" identifies the data being acted upon. This is the recommended DFD process naming format.

---

### Question 16

A BA is using a DFD to model a payroll system. The process "Generate Paycheck" reads from a data store "Employee Records" and writes to a data store "Payroll Ledger." The BA also wants to show that the system sends a direct deposit notification to employees. Where should the "Employee" appear in the DFD?

A. As a data store labeled "Employee" within the system boundary

B. As an external entity outside the system boundary, receiving a "Direct Deposit Notification" data flow from the Generate Paycheck process

C. As a process labeled "Receive Notification" inside the system boundary

D. As a lane label subdividing the system boundary rectangle

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because employees are people who interact with the system from outside it; they are external entities, not data stores.
- C is incorrect because "Receive Notification" would be a process inside the system boundary; employees are outside the system and are correctly represented as external entities.
- D is incorrect because lane labels are a BPMN concept; DFDs do not use lanes.
- B is correct because employees receive notifications from the system but are not controlled by or internal to the system. They are external entities shown outside the system boundary, with a labeled data flow ("Direct Deposit Notification") from the Generate Paycheck process to the Employee entity.

---

### Question 17

A data dictionary entry for a DFD data flow reads: "Order Confirmation = Order ID + Customer Name + Item List + Total Amount + Estimated Delivery Date." What does the "+" operator represent in this data dictionary notation?

A. The "+" indicates that all elements must be concatenated into a single text string

B. The "+" means "AND" — the data flow is composed of all listed elements together

C. The "+" means "OR" — any one of the listed elements may be included

D. The "+" indicates that each element is optional and may be omitted

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because data dictionary notation describes logical data composition, not a physical string concatenation instruction for developers.
- C is incorrect because "OR" in data dictionary notation is typically represented by "|" (pipe) or "[...]" bracket notation, not "+".
- D is incorrect because optional elements in data dictionary notation are typically shown in parentheses "( )" — the "+" indicates a required component.
- B is correct because in standard Yourdon-Coad and Gane-Sarson data dictionary notation, the "+" operator means "AND" — the composition of the data flow includes all listed elements. The Order Confirmation flow contains all five named components together.

---

### Question 18

A BA is reviewing a DFD and finds that a data flow arrow connects an external entity "Supplier" directly to a data store "Inventory," bypassing any process. What DFD rule does this violate?

A. External entities cannot appear at Level 1 — they are restricted to the context diagram only

B. Data flows cannot go directly from an external entity to a data store — a process must receive and transform the data first

C. Data stores can only receive flows from internal processes, not external entities, so this is correctly modeled

D. The Supplier should be a process inside the system boundary since it writes to the inventory

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because external entities can and do appear in Level 1 DFDs; they are present at all DFD levels where they exchange data with the system.
- C is incorrect because this statement is actually the correct rule — but C frames it as justification for the diagram being correct. The diagram is not correct; the direct external entity-to-data store connection is the violation.
- D is incorrect because suppliers are outside the system boundary and cannot be remodeled as internal processes; the issue is the missing process between the entity and the store.
- B is correct because DFD rules prohibit direct connections between external entities and data stores. Any data from an external entity must pass through a process (which validates, transforms, or records the data) before being written to a data store.

---

### Question 19

Which of the following describes the correct use of data stores in a DFD?

A. A data store should be duplicated on every level of the DFD where it is referenced to avoid confusion

B. A data store represents data at rest — it stores data that persists between processes and is accessed by one or more processes

C. A data store must have the same name as the database table it represents in the physical design

D. Data stores can only be read by processes — they cannot receive incoming data flows

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because duplicating data stores at every level is not required; a data store is typically shown once at the level where the processes interacting with it are defined, with cross-reference notation if needed.
- C is incorrect because DFDs are logical models; data store names describe the business data concept (e.g., "Customer Records"), not the physical database implementation (e.g., "tbl_customers"). Physical names are assigned during design.
- D is incorrect because data stores both receive incoming flows (when processes write data) and produce outgoing flows (when processes read data). A data store with only reads and no writes is a miracle violation.
- B is correct because a data store represents persistent data — a repository that holds data between process executions. It is the DFD representation of any stored information: files, databases, ledgers, or other persistent storage.

---

### Question 20

A BA has drawn a Level 1 DFD for an order management system. A reviewer says: "Your diagram is accurate but too complex — stakeholders cannot read it." The BA's DFD has 15 processes, 8 data stores, and 6 external entities all visible simultaneously. What should the BA do?

A. Remove the external entities to simplify the diagram since they are already shown in the context diagram

B. Decompose the most complex processes into Level 2 diagrams, reducing the Level 1 to a manageable number of high-level processes

C. Replace the DFD with a use case diagram, which stakeholders find easier to read

D. Remove the data stores since they add visual complexity and can be added back during design

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect because external entities are a required part of Level 1 DFDs; removing them breaks the diagram's scope definition and violates balancing rules.
- C is incorrect because replacing one modeling artifact with another that serves a different analytical purpose does not address the complexity issue; use case diagrams and DFDs serve different analytical roles.
- D is incorrect because data stores are essential DFD elements representing persistent data; removing them eliminates critical information about where data is stored and retrieved.
- B is correct because the standard solution to an overly complex DFD level is decomposition — creating Level 2 diagrams for the most complex processes, which reduces the visible complexity at Level 1 while preserving all detail at the lower level. DFD leveling exists specifically for this purpose.

---

*Quiz — Module 10 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

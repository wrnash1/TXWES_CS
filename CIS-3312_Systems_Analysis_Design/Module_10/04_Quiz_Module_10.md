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

*Quiz — Module 10 | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

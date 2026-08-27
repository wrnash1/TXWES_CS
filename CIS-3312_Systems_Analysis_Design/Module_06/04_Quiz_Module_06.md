# Quiz: Module 06 - Data Flow Diagrams and Entity-Relationship Diagrams

**Course:** CIS-3312 Systems Analysis and Design
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

Which of the following correctly describes the purpose of a Context Diagram (Level 0 DFD)?

A) It shows the internal database tables, their columns, and the foreign key relationships between them

B) It decomposes the system into individual sub-processes and shows data stores and internal data flows

C) It presents the entire system as a single process, defines the system boundary, and shows all external entities and data flows at the highest level

D) It documents the sequence of steps an actor performs to accomplish a goal within the system

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Internal database tables and foreign keys are shown on an ERD or physical data model, not a context diagram.
- Why B is incorrect: Decomposing into sub-processes with data stores describes a Level 1 DFD, not the Level 0 context diagram.
- Why D is incorrect: Documenting a sequence of actor interactions describes a use case scenario or specification, not a context diagram.
- Why C is correct: A context diagram (Level 0 DFD) shows only one process bubble — the entire system — the external entities, and the data flows between them, establishing system scope without internal detail.

---

## Question 2

In the context of data modeling, which of the following is the most accurate definition of cardinality in an Entity-Relationship Diagram?

A) The data type and format rules (such as string, integer, or date) that constrain the values an attribute can hold

B) The numerical relationship between entity instances — specifying how many of one entity can be associated with how many of another

C) The process of removing redundant data from a table by splitting it into smaller related tables following normalization rules

D) A unique identifier attribute (primary key) that distinguishes one entity instance from all others in the same entity set

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Describing data type constraints defines a domain or attribute constraint, not cardinality.
- Why C is incorrect: Removing redundancy through splitting tables describes normalization, not cardinality.
- Why D is incorrect: A unique identifier is the definition of a primary key, not cardinality.
- Why B is correct: Cardinality in an ERD expresses the quantity relationship between related entities (1:1, 1:N, M:N), which directly drives database schema decisions about where foreign keys and junction tables belong.

---

## Question 3

A DFD shows a data flow going directly from a data store labeled "Customer Records" to another data store labeled "Invoice Archive" without passing through any process. What DFD rule does this violate?

A) External entities cannot send data flows directly to data stores

B) Data flows cannot go directly from one data store to another — a process must transform the data

C) Level 1 DFDs must be balanced with the Level 0 context diagram

D) Every external entity must have at least two data flows entering the system

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: While external-entity-to-data-store connections are also a rule violation, that is not what this scenario describes.
- Why C is incorrect: Level balancing is a rule about DFD decomposition consistency, not about data flow connections between data stores.
- Why D is incorrect: There is no DFD rule requiring external entities to have two data flows; this is not a recognized DFD constraint.
- Why B is correct: DFD rules require that data must be processed (transformed) before moving — a direct data store to data store arrow implies data moves with no transformation, which is a fundamental DFD violation.

---

## Question 4

An ERD shows that one Customer can place many Orders, but each Order belongs to exactly one Customer. What is the cardinality of the Customer-to-Order relationship?

A) One-to-one (1:1)

B) Many-to-many (M:N)

C) One-to-many (1:N)

D) Zero-to-one (0:1)

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: One-to-one means exactly one instance on each side; here, a customer can have many orders.
- Why B is incorrect: Many-to-many means multiple instances on both sides; here, each order belongs to exactly one customer.
- Why D is incorrect: Zero-to-one describes optional participation on one side; the scenario states one customer can place many orders.
- Why C is correct: One customer can have many orders; each order belongs to exactly one customer — this is 1:N. In the physical database, this is implemented by placing a CustomerID foreign key in the Order table.

---

## Question 5

A systems analyst is creating a DFD and needs to represent a company's external tax authority (which receives tax report data from the system but never sends data back into the system). Which DFD symbol should be used for the tax authority?

A) A data store (open-ended rectangle) because the tax authority stores the received data

B) A process (circle or rounded rectangle) because the tax authority processes the submitted tax reports

C) An external entity (rectangle) because the tax authority is outside the system boundary

D) A data flow (arrow) because the tax authority represents the movement of data out of the system

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Data stores represent repositories of data within the system boundary; external organizations are not data stores.
- Why B is incorrect: Processes represent transformations that occur within the system; external organizations do not appear as processes in DFDs.
- Why D is incorrect: A data flow is a named arrow that represents data movement — it is not used to represent an organization or actor.
- Why C is correct: External entities (shown as rectangles) are sources or sinks of data that exist outside the system boundary. The tax authority only receives data (a sink), making it an external entity with one outgoing data flow from the system to it.

---

## Question 6

A BA draws a Level 1 DFD for an order processing system. The Level 0 Context Diagram shows three data flows entering the system boundary: "Customer Order," "Payment Authorization," and "Inventory Update." The Level 1 diagram shows "Customer Order" and "Payment Authorization" entering the system but omits "Inventory Update." What DFD principle has been violated?

A) The process naming convention — processes must use verb-noun names

B) Level balancing — every data flow crossing the system boundary at Level 0 must appear at Level 1

C) The data store naming convention — data stores must not be numbered

D) The external entity rule — external entities may not connect directly to data stores

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Process naming conventions are a best practice but are not the issue described here.
- Why C is incorrect: Data store naming is not relevant to the missing data flow at Level 1.
- Why D is incorrect: The external entity rule is about direct entity-to-data store connections; this scenario describes a missing boundary flow.
- Why B is correct: Level balancing requires that every data flow crossing the system boundary at Level 0 must appear at Level 1. Omitting "Inventory Update" from Level 1 means the two levels are unbalanced — a fundamental DFD violation.

---

## Question 7

An ERD models a university registration system. Students can enroll in many Courses, and each Course can have many Students enrolled. What is the correct approach for implementing this relationship in a relational database?

A) Place a StudentID foreign key in the Course table to represent the enrollment link

B) Place a CourseID foreign key in the Student table to represent the enrollment link

C) Create a junction table (such as Enrollment) that holds StudentID and CourseID as foreign keys

D) Merge the Student and Course entities into a single table to eliminate the many-to-many relationship

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Placing only one foreign key on one side does not resolve M:N cardinality — it would only support 1:N.
- Why B is incorrect: Same problem — a single foreign key in one table supports 1:N, not M:N.
- Why D is incorrect: Merging two unrelated entities into one table destroys the data model and creates severe redundancy and anomalies.
- Why C is correct: A many-to-many relationship cannot be directly implemented in a relational database. A junction table (Enrollment) with StudentID and CourseID as foreign keys — typically forming a composite primary key — resolves the M:N relationship correctly.

---

## Question 8

A DFD shows a process bubble labeled "Calculate Discount" with two incoming data flows ("Order Total" and "Customer Tier") but no outgoing data flows. What type of DFD error is this?

A) A miracle — a process that produces output without receiving any input

B) A black hole — a process that receives input but never produces any output

C) A level balancing violation — the process is not represented in the parent diagram

D) An external entity violation — the process is connected directly to an external entity

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: A miracle is the opposite — output with no input. This process has input but no output.
- Why C is incorrect: Level balancing is about matching flows between DFD levels, not about individual processes lacking outputs.
- Why D is incorrect: No external entity connection is described here; the error is about the process having no outgoing data flow.
- Why B is correct: A "black hole" is a DFD process that receives data but never produces output — the data disappears into a void with no transformation result leaving the process. "Calculate Discount" receives input but produces no output, which is a black hole violation.

---

## Question 9

In Crow's Foot ERD notation, a relationship line ends with a crow's foot symbol combined with a single vertical tick mark. What does this combination indicate?

A) The entity on that end is optional — zero or one instance is allowed

B) The entity on that end must have exactly one instance — mandatory one

C) The entity on that end must have one or more instances — mandatory many

D) The entity on that end may have zero or more instances — optional many

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Zero or one (optional one) is represented by a single line combined with a circle, not a crow's foot.
- Why B is incorrect: Mandatory one (exactly one) is represented by two single vertical lines, not a crow's foot.
- Why D is incorrect: Optional many (zero or more) is represented by a crow's foot combined with a circle, not a tick mark.
- Why C is correct: In Crow's Foot notation, the crow's foot means "many" and the single vertical tick means "at least one" (mandatory). Together they mean "one or many" — the entity must have at least one instance on that side of the relationship.

---

## Question 10

A data dictionary entry reads: "CustomerEmail — Data type: String (max 100 characters). Format: standard email format (`user@domain.tld`). Used in: Process 3 (Send Confirmation), Data Store DS-2 (Customer Records). Constraints: must be unique per customer account." What is the primary purpose served by this data dictionary entry?

A) It describes how data flows between external entities in the DFD

B) It formally defines a data element, removing ambiguity about its format, constraints, and usage across the system

C) It establishes the primary key and foreign key relationships in the ERD

D) It documents the sequence of steps in the main success scenario of a use case specification

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Data dictionaries define data elements; they do not describe flow paths between external entities.
- Why C is incorrect: Primary key and foreign key relationships are defined in the ERD, not in a data dictionary entry.
- Why D is incorrect: Use case specifications document actor-system interaction sequences; data dictionaries focus on data element definitions.
- Why B is correct: A data dictionary entry formally catalogs a data element's name, type, format, acceptable values, constraints, and the processes or stores that reference it. This removes ambiguity — every analyst, developer, and stakeholder has the same understanding of what "CustomerEmail" means and how it must be formatted.

---

## Question 11

A BA is drawing a Level 1 DFD for a hotel reservation system. The process "Confirm Reservation" receives an incoming data flow from an external entity "Guest" and sends an outgoing data flow to a data store "Reservations." No data flows out of the "Confirm Reservation" process to any other element. What DFD rule violation exists?

A) Black hole — "Confirm Reservation" receives input but sends no output back to the Guest or any other element

B) Miracle — "Confirm Reservation" produces the confirmation without receiving the reservation details

C) Level balancing violation — "Confirm Reservation" does not appear at Level 0

D) No violation — data flowing only into a data store is a valid process behavior

Correct Answer: A

Distractor Analysis:

- Why B is incorrect: A miracle is a process that produces output with no input; this process has input from the Guest.
- Why C is incorrect: Level balancing concerns whether Level 1 flows match Level 0 boundary flows; the scenario describes a single process output issue, not a cross-level discrepancy.
- Why D is incorrect: A process that receives guest input but sends no confirmation back — and produces only a data store write — is a black hole. The guest receives no response, which is both a DFD rule violation and a real-world design flaw.
- Why A is correct: A black hole process consumes input without producing any output data flow. Even if the reservation is written to the data store, the guest receives no confirmation — meaning the transformation produces no meaningful output visible outside the process, which violates DFD rules.

---

## Question 12

An ERD for a hospital system includes a "Doctor" entity and a "Patient" entity. A Doctor can treat many Patients, and a Patient can be treated by many Doctors. Additionally, the hospital needs to record the date and diagnosis for each treatment. Where should the date and diagnosis attributes be stored?

A) As attributes of the Doctor entity, since doctors initiate treatments

B) As attributes of the Patient entity, since the treatment is about the patient's condition

C) As attributes of a junction table (Treatment) that resolves the many-to-many relationship between Doctor and Patient

D) As separate entities unrelated to either Doctor or Patient

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Storing date and diagnosis on the Doctor entity would duplicate them for every patient the doctor treats, causing severe data anomalies.
- Why B is incorrect: Storing on the Patient entity would duplicate them for every doctor who treats the patient.
- Why D is incorrect: Date and diagnosis are properties of the specific Doctor-Patient treatment instance, not standalone entities.
- Why C is correct: Attributes that describe the relationship instance itself (when the treatment occurred and what was diagnosed) belong in the junction table. The Treatment table holds DoctorID, PatientID, TreatmentDate, and Diagnosis — correctly capturing attributes of the M:N association.

---

## Question 13

Which of the following best explains why a Context Diagram should be created before a Level 1 DFD on a new project?

A) Context Diagrams are required by all systems development methodologies and must precede Level 1 DFDs by regulatory mandate

B) The Context Diagram establishes system scope and identifies all external entities and boundary data flows, which are prerequisites for Level 1 decomposition

C) Context Diagrams are simpler to draw, so they build team confidence before the more complex Level 1 diagram is attempted

D) Level 1 DFDs cannot be reviewed by stakeholders unless the Context Diagram is signed off first

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: There is no universal regulatory mandate for Context Diagrams; the reason is analytical, not legal.
- Why C is incorrect: Simplicity is not the analytical reason; the Context Diagram serves a specific scope-setting function.
- Why D is incorrect: Stakeholder reviews can occur on any artifact; sign-off of the Context Diagram is not a formal prerequisite for showing Level 1 diagrams to stakeholders.
- Why B is correct: The Context Diagram defines what is inside the system boundary and all external interfaces. Level 1 decomposes the single system process into sub-processes; without knowing the boundary flows from the Context Diagram, the Level 1 cannot be correctly scoped or balanced.

---

## Question 14

A BA is documenting a data element "TransactionAmount" in the data dictionary. Which of the following entries is the most complete and useful?

A) TransactionAmount — Number

B) TransactionAmount — The amount of money involved in a transaction

C) TransactionAmount — Data type: Decimal (10,2). Units: USD. Range: 0.01 to 999,999.99. Constraints: must be positive; cannot exceed the account's available balance. Used in: Process 2.3 (Authorize Payment), DS-3 (Transaction Log)

D) TransactionAmount — Required field in the payment form

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: "Number" alone provides no format, range, constraint, or usage information; it is too vague to guide implementation or testing.
- Why B is incorrect: This is a plain-language description but lacks the technical precision needed by developers and testers.
- Why D is incorrect: Noting that it is a required field is one attribute, but it omits type, format, range, and usage context.
- Why C is correct: A complete data dictionary entry specifies data type and format (Decimal 10,2), units, valid range, business constraints, and which processes and stores reference the element. This gives every team member a complete, unambiguous definition.

---

## Question 15

An ERD shows that each Employee belongs to exactly one Department, and each Department can have many Employees. A new requirement states that some Employees may be "on loan" to a second Department temporarily while still belonging to their primary Department. How should this new requirement be modeled?

A) Change the Employee-Department relationship from 1:N to M:N and add a junction table

B) Add a second "SecondaryDepartmentID" attribute to the Employee entity

C) Create a new entity "Department Assignment" with attributes for EmployeeID, DepartmentID, assignment type (primary/secondary), and effective dates to resolve the M:N relationship

D) Split the Employee entity into two separate entities: PrimaryEmployee and SecondaryEmployee

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Simply changing to M:N and adding a plain junction table would capture the linkage but would miss the assignment type and date attributes that the business needs to track.
- Why B is incorrect: Adding a fixed second attribute cannot accommodate more than two departments per employee and embeds a business rule as a hardcoded data structure.
- Why D is incorrect: Splitting the entity creates duplication and violates normal form; the same person should be one Employee record.
- Why C is correct: A "Department Assignment" junction table resolves the M:N relationship and can hold additional descriptive attributes (assignment type, start/end dates) about each assignment instance — providing a flexible, normalized design that meets the business need.

---

## Question 16

A DFD analyst labels a process "Customer Data" and a data store "Process Orders." A reviewer flags both labels as incorrect. Why?

A) Processes must use passive nouns; data stores must use active verb-noun phrases

B) Processes must use active verb-noun names (describing a transformation); data stores must use passive noun phrases (describing stored data)

C) Processes and data stores use the same naming convention — both require verb-noun phrases

D) Data stores must use names matching the external entity they receive data from

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: This reverses the correct convention.
- Why C is incorrect: Processes and data stores have different naming conventions; they do not use the same format.
- Why D is incorrect: Data store names describe the content being stored, not the entity that provides the data.
- Why B is correct: DFD naming conventions specify that processes describe a transformation (verb-noun: "Validate Order," "Process Payment") and data stores describe stored information (noun: "Orders," "Customer Records"). "Customer Data" sounds like a data store name used as a process; "Process Orders" sounds like a process name used as a data store — both are reversed.

---

## Question 17

A BA is modeling an insurance system. The ERD includes a "Policy" entity with a "PolicyType" attribute that can only hold the values "Auto," "Home," or "Life." Which ERD modeling technique best represents this constraint?

A) Add a sub-type entity for each policy type using generalization/specialization

B) Note the allowed values as a domain constraint in the data dictionary entry for PolicyType

C) Create a separate "PolicyType" lookup entity with a one-to-many relationship to Policy

D) Both B and C are valid approaches depending on whether policy types require additional unique attributes

Correct Answer: D

Distractor Analysis:

- Why A is incorrect: Generalization/specialization is appropriate when each policy type has unique attributes; if all types share the same attributes, a domain constraint or lookup table is simpler.
- Why B is incorrect alone: A data dictionary domain constraint documents the rule but does not enforce it in the data model; a lookup table enforces it at the database level.
- Why C is incorrect alone: A lookup table enforces the constraint at the data level but may not document it for the BA's requirements purposes as clearly as a data dictionary entry.
- Why D is correct: Both approaches are valid and commonly used together. The data dictionary documents the allowed values for requirements purposes; a lookup table enforces them at the database level. The choice between them depends on whether each policy type has unique data attributes that warrant separate modeling.

---

## Question 18

In a DFD, what distinguishes a "process" from an "external entity"?

A) Processes are labeled with numbers; external entities are labeled with letters

B) Processes exist inside the system boundary and transform data; external entities exist outside the boundary and are sources or sinks of data

C) Processes are shown as rectangles; external entities are shown as circles

D) Processes can only send data flows; external entities can only receive data flows

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Numbers on processes are an optional labeling convention; letters on external entities are not a DFD standard.
- Why C is incorrect: The shapes are reversed — processes are circles or rounded rectangles; external entities are rectangles.
- Why D is incorrect: External entities can both send and receive data flows; data flows are bidirectional with respect to the system boundary.
- Why B is correct: The fundamental distinction is location relative to the system boundary and function. Processes are inside the boundary and transform data; external entities are outside the boundary and originate or receive data without transforming it within the system.

---

## Question 19

A project team is building a payroll system. The ERD includes an Employee entity (EmployeeID, Name, HireDate, Salary) and a PayPeriod entity (PeriodID, StartDate, EndDate). Each pay period produces one paycheck per employee. Where should the paycheck amount be stored?

A) As an attribute of the Employee entity, since the salary determines the amount

B) As an attribute of the PayPeriod entity, since the pay period determines when it is issued

C) In a junction table (Paycheck) linking Employee and PayPeriod, with PaycheckAmount as an attribute

D) As a separate data store outside the ERD, since paycheck amounts change each period

Correct Answer: C

Distractor Analysis:

- Why A is incorrect: Storing paycheck amount on the Employee entity would require updating the record every pay period and could not retain historical paycheck amounts.
- Why B is incorrect: Storing on the PayPeriod entity would only allow one amount per period, not one per employee per period.
- Why D is incorrect: A "separate data store outside the ERD" is not a modeling concept; all persistent data is modeled in the ERD.
- Why C is correct: A paycheck is produced for each Employee-PayPeriod combination — exactly the intersection that a junction table models. The Paycheck table holds EmployeeID, PeriodID, and PaycheckAmount as a relationship instance with a descriptive attribute.

---

## Question 20

A BA presents a Level 1 DFD to stakeholders. A business user says: "I don't see where the customer gets their confirmation number after submitting the order." What type of DFD element is missing from the diagram?

A) A data store — the confirmation number needs to be saved somewhere

B) An outgoing data flow from the order confirmation process back to the Customer external entity

C) An additional process to generate the confirmation number separately

D) An additional external entity to represent the confirmation system

Correct Answer: B

Distractor Analysis:

- Why A is incorrect: Storing the confirmation number may also be needed, but the business user's complaint is specifically that the customer does not receive it — which is a missing outgoing data flow.
- Why C is incorrect: Generating the number may be a sub-step, but if the data flow returning it to the customer is missing, the customer still does not receive it regardless of what internal processes exist.
- Why D is incorrect: The customer is already an external entity; there is no need for a separate "confirmation system" entity to address the missing data flow to the customer.
- Why B is correct: The customer not receiving the confirmation number means there is no data flow labeled something like "Order Confirmation" or "Confirmation Number" going from the confirmation process back to the Customer external entity. Adding this outgoing data flow completes the interaction.

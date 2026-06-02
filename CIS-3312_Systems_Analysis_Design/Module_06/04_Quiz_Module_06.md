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

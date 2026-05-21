# Quiz: Module 06 - Data Flow Diagrams (DFDs) and Entity-Relationship Diagrams (ERDs)
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

**Question 1**
Which of the following correctly describes the purpose of a Context Diagram (Level 0 DFD)?
*   A) It shows the internal database tables, their columns, and the foreign key relationships between them
*   B) It decomposes the system into individual sub-processes and shows data stores and internal data flows
*   C) It presents the entire system as a single process, defines the system boundary, and shows all external entities and data flows at the highest level
*   D) It documents the sequence of steps an actor performs to accomplish a goal within the system
*   **Correct Answer:** C) It presents the entire system as a single process, defines the system boundary, and shows all external entities and data flows at the highest level
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Internal database tables and foreign keys are shown on an ERD or physical data model, not a context diagram.
    *   *Why B is incorrect:* Decomposing into sub-processes with data stores describes a Level 1 DFD, not the Level 0 context diagram.
    *   *Why D is incorrect:* Documenting a sequence of actor interactions describes a use case scenario, not a context diagram.
    *   *Why C is correct:* A context diagram (Level 0 DFD) shows only one process bubble (the entire system), the external entities, and the data flows between them — establishing system scope without internal detail.

---

**Question 2**
In the context of data modeling, which of the following is the most accurate definition of **cardinality** in an Entity-Relationship Diagram?
*   A) The data type and format rules (such as string, integer, or date) that constrain the values an attribute can hold
*   B) The numerical relationship between entity instances — specifying how many of one entity can be associated with how many of another
*   C) The process of removing redundant data from a table by splitting it into smaller related tables following normalization rules
*   D) A unique identifier attribute (primary key) that distinguishes one entity instance from all others in the same entity set
*   **Correct Answer:** B) The numerical relationship between entity instances — specifying how many of one entity can be associated with how many of another
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Describing data type constraints defines a domain or attribute constraint, not cardinality.
    *   *Why C is incorrect:* Removing redundancy through splitting tables describes normalization, not cardinality.
    *   *Why D is incorrect:* A unique identifier is the definition of a primary key, not cardinality.
    *   *Why B is correct:* Cardinality in an ERD expresses the quantity relationship between related entities (1:1, 1:N, M:N), which directly drives database schema decisions about where foreign keys and junction tables belong.

---

**Question 3**
A DFD shows a data flow going directly from a data store labeled "Customer Records" to another data store labeled "Invoice Archive" without passing through any process. What DFD rule does this violate?
*   A) External entities cannot send data flows directly to data stores
*   B) Data flows cannot go directly from one data store to another — a process must transform the data
*   C) Level 1 DFDs must be balanced with the Level 0 context diagram
*   D) Every external entity must have at least two data flows entering the system
*   **Correct Answer:** B) Data flows cannot go directly from one data store to another — a process must transform the data
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While external-entity-to-data-store connections are also a rule violation, that is not what this scenario describes.
    *   *Why C is incorrect:* Level balancing is a rule about DFD decomposition consistency, not about data flow connections between data stores.
    *   *Why D is incorrect:* There is no DFD rule requiring external entities to have two data flows; this is not a recognized DFD constraint.
    *   *Why B is correct:* DFD rules require that data must be processed (transformed) before moving — a direct data store to data store arrow implies data moves with no transformation, which is a fundamental DFD violation.

---

**Question 4**
An ERD shows that one Customer can place many Orders, but each Order belongs to exactly one Customer. What is the cardinality of the Customer-to-Order relationship?
*   A) One-to-one (1:1)
*   B) Many-to-many (M:N)
*   C) One-to-many (1:N)
*   D) Zero-to-one (0:1)
*   **Correct Answer:** C) One-to-many (1:N)
*   **Distractor Analysis:**
    *   *Why A is incorrect:* One-to-one means exactly one instance on each side; here, a customer can have many orders.
    *   *Why B is incorrect:* Many-to-many means multiple instances on both sides; here, each order belongs to exactly one customer.
    *   *Why D is incorrect:* Zero-to-one describes optional participation on one side; the scenario states "one Customer can place many Orders," indicating the customer side is 1, not 0 or 1.
    *   *Why C is correct:* One customer → many orders, each order → exactly one customer = 1:N cardinality. In the physical database, this is implemented by placing a CustomerID foreign key in the Order table.

---

**Question 5**
A systems analyst is creating a DFD and needs to represent the company's external tax authority (which receives tax report data from the system but never sends data back into the system). Which DFD symbol should be used for the tax authority?
*   A) A data store (open-ended rectangle) because the tax authority stores the received data
*   B) A process (circle or rounded rectangle) because the tax authority processes the submitted tax reports
*   C) An external entity (rectangle) because the tax authority is outside the system boundary
*   D) A data flow (arrow) because the tax authority represents the movement of data out of the system
*   **Correct Answer:** C) An external entity (rectangle) because the tax authority is outside the system boundary
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Data stores represent repositories of data *within* the system boundary; external organizations are not data stores.
    *   *Why B is incorrect:* Processes represent transformations that occur *within* the system; external organizations do not appear as processes in DFDs.
    *   *Why D is incorrect:* A data flow is a named arrow that represents data movement — it is not used to represent an organization or actor.
    *   *Why C is correct:* External entities (shown as rectangles) are sources or sinks of data that exist outside the system boundary. The tax authority only receives data (a sink), making it an external entity with one outgoing data flow from the system to it.

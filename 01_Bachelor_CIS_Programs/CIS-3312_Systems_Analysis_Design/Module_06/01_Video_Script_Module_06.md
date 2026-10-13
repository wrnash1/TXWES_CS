# Video Script: Module 06 - Data Flow Diagrams and Entity-Relationship Diagrams

**Course:** CIS-3312 Systems Analysis and Design
**Estimated Duration:** 22 minutes
**Certification Alignment:** IIBA ECBA (Entry Certificate in Business Analysis)
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.

---

## Section 1: Welcome and Module Overview [00:00 - 03:00]

Welcome to Module 06. I am Professor Nash. Today we are covering two foundational visual modeling techniques that every systems analyst must master: Data Flow Diagrams and Entity-Relationship Diagrams. Both appear on the IIBA ECBA exam, and both are tools you will use throughout your BA career.

[SHOW DIAGRAM: Title slide — "Module 06: Data Flow Diagrams and Entity-Relationship Diagrams" with BABOK KA 5 label and IIBA ECBA badge]

These two diagram types answer different questions. A Data Flow Diagram — DFD — asks: how does data move through the system? What processes transform it? Where is it stored? An Entity-Relationship Diagram — ERD — asks: what data does the system store? How are the pieces of data related to each other?

Think of them as complementary. The DFD shows the system in motion — data flowing and being transformed. The ERD shows the system at rest — data organized in structured relationships. A thorough systems analysis uses both.

---

## Section 2: Data Flow Diagrams [03:00 - 10:00]

[SHOW DIAGRAM: Labeled DFD symbol reference — four symbols with labels: Rectangle (External Entity), Circle/Rounded Rectangle (Process), Open-Ended Rectangle (Data Store), Arrow (Data Flow)]

A DFD uses exactly four symbols. Let me define each one carefully because the exam will test whether you can identify them.

An external entity is a rectangle. It represents any person, organization, or system that exists outside the system boundary but interacts with it by sending data in or receiving data out. External entities are also called sources and sinks — a source sends data into the system; a sink receives data from the system. An entity can be both. Examples: Customer, Tax Authority, Shipping Carrier.

A process is a circle or rounded rectangle. It represents a transformation — the system does something to the data. A process has a name that describes what it does (a verb phrase: "Validate Order," "Calculate Invoice"). Every process must receive at least one input data flow and produce at least one output data flow.

A data store is an open-ended rectangle — think of a rectangle with the right side open. It represents data held at rest within the system — a file, database table, or information repository. Data stores have descriptive names (not numbered — "Customer Records," "Order History").

A data flow is an arrow. It represents data moving from one symbol to another. Data flows are always labeled with the name of the data being moved ("Customer Order," "Validated Payment," "Shipment Confirmation").

Now let me cover the leveling structure.

[SHOW DIAGRAM: Three-level DFD hierarchy — Level 0 (one bubble labeled "Online Book Store System," external entities, and data flows), Level 1 (three process bubbles: "Process Order," "Manage Inventory," "Handle Returns," with data stores), Level 2 (expanded view of "Process Order" with sub-processes)]

A Context Diagram — also called a Level 0 DFD — shows the entire system as a single process bubble. It shows all external entities and all the data flows between the system and those external entities. The Context Diagram defines scope: what the system receives, what it produces, who is involved. Nothing inside the system is shown at Level 0.

A Level 1 DFD decomposes the single system bubble into the major sub-processes. Level 1 shows internal processes, data stores, and the data flows between them. It must be balanced with Level 0: every input and output shown at Level 0 must appear at Level 1.

A Level 2 DFD decomposes one Level 1 process into its sub-processes. The same balancing rule applies.

> IIBA ECBA Exam Tip: The exam tests DFD rule violations. There are three classic violations: data flowing directly from one data store to another (a process must transform it), data flowing directly from one external entity to another (it must pass through the system), and a process with no inputs or no outputs. These are called "black holes" (input, no output) and "miracles" (output, no input). Know all three.

---

## Section 3: ERD Concepts and Notation [10:00 - 16:00]

[SHOW DIAGRAM: ERD for a simple order system — four entities (Customer, Order, Product, OrderLine) with Crow's Foot notation showing cardinalities and key attributes listed inside each entity rectangle]

An Entity-Relationship Diagram models the data a system needs to store. It does not show process or sequence — it shows structure. Let me introduce the three core concepts: entities, attributes, and relationships.

An entity is a distinct thing about which the system stores data. Entities become tables in a relational database. They are named with singular nouns: Customer, Order, Product, Employee. A strong entity has its own primary key — it can be uniquely identified on its own. A weak entity depends on a related strong entity for its unique identification.

An attribute is a data element that describes an entity. Customer has attributes: CustomerID, FirstName, LastName, EmailAddress. Attributes become columns in a database table. The primary key attribute — the one that uniquely identifies each instance — is underlined in ERD notation.

A relationship is an association between two entities. "Customer places Order." "Order contains Product." Relationships are the connections in the ERD. Every relationship has a name (a verb phrase), and it has a cardinality.

[SHOW DIAGRAM: Crow's Foot notation reference — three relationship lines side by side: 1:1 (single lines both sides), 1:N (single line one side, crow's foot other side), M:N (crow's foot both sides), with optional/mandatory indicators (circle vs. tick mark)]

Cardinality expresses how many instances of one entity can relate to how many instances of another. There are three fundamental cardinalities.

One-to-one (1:1): One instance of Entity A relates to exactly one instance of Entity B. Example: one Employee has one Employee Badge. In the database, the foreign key can go in either table. One-to-one relationships are relatively rare.

One-to-many (1:N): One instance of Entity A relates to many instances of Entity B, but each instance of B relates to exactly one instance of A. Example: one Customer places many Orders; each Order belongs to exactly one Customer. In the database, the foreign key goes on the "many" side — CustomerID lives in the Order table.

Many-to-many (M:N): Many instances of A relate to many instances of B. Example: one Order can contain many Products; one Product can appear in many Orders. Many-to-many relationships cannot be directly implemented in a relational database. They require a junction table — also called an associative entity or bridge table — that holds the foreign keys of both sides. The OrderLine table (with OrderID and ProductID as a composite key) resolves the Order-to-Product M:N relationship.

Crow's Foot notation adds participation indicators: a circle on the line means zero (optional), a tick mark means one (mandatory). So a crow's foot with a circle means "zero or many"; a crow's foot with a tick mark means "one or many."

> IIBA ECBA Exam Tip: The exam will test cardinality identification. When a question describes a relationship, map it to 1:1, 1:N, or M:N immediately. Then ask: which side holds the foreign key? (The "many" side.) If it is M:N, what is needed? (A junction table.) These are the two downstream design decisions that cardinality drives.

---

## Section 4: DFD and ERD in the BA Context [16:00 - 19:30]

When do BAs use DFDs versus ERDs? The answer depends on what question you are trying to answer.

Use a DFD when you need to communicate how data moves through a system — what processes exist, what external parties are involved, where data is stored, and how information flows between components. DFDs are excellent for scope definition (the Context Diagram) and for communicating the logical architecture of a system to both technical and non-technical stakeholders. They are particularly useful when analyzing current-state processes and modeling future-state improvements.

Use an ERD when you need to communicate what data the system stores and how the pieces of data are related. ERDs are the bridge between requirements and database design. A BA produces a conceptual ERD based on requirements; the database architect refines it into a logical ERD (with all attributes and foreign keys identified) and eventually a physical ERD (with data types, constraints, and indexes specific to the target database platform).

Both diagram types are covered in BABOK Guide v3 under KA 5 Techniques: "Data Flow Diagrams" and "Data Modeling." Both require the same professional care about notation accuracy, level balancing, and completeness.

---

## Section 5: Lab Preview and Closing [19:30 - 22:00]

This week's lab uses a single case study — Ridgeview Community Library — to practice both techniques. You will draw a Context Diagram and Level 1 DFD showing how the library's checkout system processes patron requests, manages the catalog, and interacts with external parties. Then you will draw an ERD for the same system showing the entities and their relationships.

Two key reminders. First: in DFDs, processes transform data — data cannot flow between data stores or between external entities without passing through a process. Second: in ERDs, every M:N relationship must be resolved into a junction table with foreign keys from both sides.

Visit iiba.org for BABOK Guide v3 KA 5 reference. The draw.io diagramming tool is free and has built-in DFD and ERD shape libraries — use it for all diagram work in this course.

---

## Module 06 Complete

Next: Module 07 - Process Modeling with BPMN

### Additional Resources

- iiba.org — BABOK Guide v3 KA 5: Data Flow Diagrams and Data Modeling techniques
- iiba.org — ECBA exam blueprint weighting information

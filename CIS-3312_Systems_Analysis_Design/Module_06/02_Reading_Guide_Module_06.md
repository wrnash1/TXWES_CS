# Reading Guide: Module 06 - Data Flow Diagrams (DFDs) and Entity-Relationship Diagrams (ERDs)
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

### Introduction
Welcome to **Module 06 – Data Flow Diagrams and Entity-Relationship Diagrams**! This module covers two of the most foundational visual modeling techniques in systems analysis: DFDs, which model how data moves through a system, and ERDs, which model the structure of data the system stores.

Together, these diagrams bridge the requirements and design phases. DFDs help analysts understand and communicate current and future-state processes from a data-movement perspective. ERDs lay the conceptual groundwork for database design. Both are frequently tested on the IIBA ECBA exam and are practical tools you will use throughout your BA career.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Data Flow Diagram (DFD)**: A Data Flow Diagram is a graphical representation showing how data enters, moves through, is transformed within, and exits a system. DFDs use four symbols: external entities (rectangles — sources/sinks of data outside the system), processes (circles or rounded rectangles — transformations that act on data), data stores (open-ended rectangles — repositories where data is held at rest), and data flows (arrows — paths along which data moves). DFDs are leveled: a Context Diagram (Level 0) shows the entire system as one process; Level 1 decomposes it into major sub-processes; Level 2 further decomposes each Level 1 process.

*   **Context Diagram (Level 0 DFD)**: A context diagram is the highest-level DFD, showing the entire system as a single process bubble, all external entities that interact with it, and the data flows between them. It defines the system boundary and scope without showing any internal details. Context diagrams are excellent for stakeholder communication because they are simple and immediately show what data comes into and out of the system.

*   **Entity-Relationship Diagram (ERD)**: An Entity-Relationship Diagram is a data modeling technique that shows the entities (objects or concepts) in a system's domain, the attributes of each entity, and the relationships between entities. ERDs are the conceptual blueprint from which database schemas are derived. The Chen notation uses diamonds for relationships; the Crow's Foot notation uses line endings to indicate cardinality, and is most common in database design practice.

*   **Entity**: In an ERD, an entity is a distinct, real-world object or concept about which the system stores data. Entities become tables in a relational database. Examples include Customer, Order, Product, and Employee. A *strong entity* can be uniquely identified by its own attributes; a *weak entity* depends on a related strong entity for its unique identification.

*   **Cardinality**: Cardinality describes the numerical relationship between instances of two related entities — specifically, how many instances of one entity can be associated with how many instances of another. Common cardinalities include one-to-one (1:1), one-to-many (1:N), and many-to-many (M:N). Correctly identifying cardinality is essential because it drives the physical database design (which table holds the foreign key, and when a junction/bridge table is needed).

*   **Data Dictionary**: A data dictionary (also called a data repository) is a structured catalog that defines every data element referenced in a system, including its name, data type, format, acceptable values, and the processes or data stores that use it. A data dictionary complements DFDs by formally defining what each data flow and data store contains, removing ambiguity about data definitions.

---

### 2. Certification Exam Tips
*   **DFD Rules**: The ECBA exam tests whether you can identify violations of DFD rules. Key rules: (1) No data flow can go directly from one data store to another — a process must transform it. (2) No data flow can go directly from one external entity to another — it must pass through the system. (3) Every process must have at least one input data flow and at least one output data flow. A question may show a diagram with a rule violation and ask you to identify the error.
*   **Level Balancing**: When a DFD is decomposed from Level 0 to Level 1, the inputs and outputs to/from the Level 0 process must match exactly the inputs and outputs in the Level 1 diagram. This is called "balancing" — the ECBA exam may present a pair of diagrams and ask whether they are correctly balanced.
*   **ERD Cardinality Notation**: Know both Chen notation (1, N, M inside diamonds) and Crow's Foot notation (lines with crow's foot symbols for many, single lines for one, circle for optional/zero). The ECBA exam uses BABOK® terminology; Crow's Foot is more common in database design courses and tools like draw.io and Lucidchart.
*   **Study Resource**: draw.io (free at [https://www.drawio.com/](https://www.drawio.com/)) supports both DFD and ERD diagram types with built-in shape libraries — use it to practice drawing diagrams for the lab and to build muscle memory for the notation before the exam.

---

### Required Readings & Videos
*   **Required Reading**: BABOK® Guide v3 Techniques section — "Data Flow Diagrams" and "Data Modeling." These entries describe both techniques within the BA context. Also review the Lucidchart tutorial on ERD notation at [https://www.lucidchart.com/pages/er-diagrams](https://www.lucidchart.com/pages/er-diagrams) for a clear visual explanation of Crow's Foot notation.
*   **Supplemental Reading**: Review the draw.io DFD and ERD shape libraries documentation at [https://www.drawio.com/](https://www.drawio.com/) — understanding the tool you will use for labs makes the notation practice more efficient.

---

### Lab & Activity Integration
In this week's lab, you will:
*   Draw a Context Diagram (Level 0 DFD) for a provided scenario (online book ordering system), identifying all external entities and major data flows.
*   Decompose the context diagram into a Level 1 DFD with at least three internal processes and two data stores.
*   Draw an ERD for the same scenario using Crow's Foot notation, identifying at least four entities, their key attributes, and the cardinality of each relationship.

---

### 3. Study Checklist
- [ ] Read the glossary terms and write your own one-sentence version of each definition.
- [ ] Read BABOK® Guide v3 Techniques — "Data Flow Diagrams" and "Data Modeling."
- [ ] Review the Lucidchart ERD tutorial at [https://www.lucidchart.com/pages/er-diagrams](https://www.lucidchart.com/pages/er-diagrams).
- [ ] Watch the Module 06 video lecture.
- [ ] Open draw.io at [https://www.drawio.com/](https://www.drawio.com/) and practice creating a simple DFD and ERD before the lab submission.

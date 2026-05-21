# Reading Guide: Module 11 - Database Design and Normalization
## Course: CIS-3312 Systems Analysis & Design (IIBA ECBA)

---

### Introduction
Welcome to **Module 11 – Database Design and Normalization**! Every information system requires persistent storage of data, and in most enterprise systems that storage is a relational database. This module moves from the conceptual data model (ERD from Module 06) through logical database design and into the physical design principles that guide how relational databases are structured for integrity, efficiency, and maintainability.

Normalization is the process of organizing database tables to minimize redundancy and eliminate data anomalies. For business analysts, understanding normalization is important because poorly designed databases produce systems that are slow, inconsistent, and difficult to maintain — all of which are requirements failures, even if the functional requirements were correctly specified.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Relational Database**: A relational database organizes data into tables (relations), where each table represents an entity, each row (tuple) represents an instance, and each column (attribute) represents a property of that entity. Tables are linked through keys (primary keys and foreign keys), allowing data to be joined across tables in structured queries. The relational model, proposed by E.F. Codd in 1970, underpins nearly all enterprise data management systems.

*   **Primary Key**: A primary key is an attribute (or combination of attributes) in a database table that uniquely identifies each row. No two rows in a table can have the same primary key value, and the primary key cannot be null. Good primary key selection avoids using values that might change over time (e.g., email addresses) in favor of stable identifiers (e.g., auto-generated integer IDs or UUIDs).

*   **Foreign Key**: A foreign key is an attribute in one table that references the primary key of another table, establishing a relationship between the two tables. Foreign keys enforce *referential integrity* — the database will prevent storing a foreign key value that does not exist in the referenced table. For example, an Order table may have a CustomerID foreign key that must match an existing Customer record.

*   **First Normal Form (1NF)**: A table is in First Normal Form if every column contains atomic (indivisible) values — no repeating groups or multi-valued columns. For example, storing a comma-separated list of phone numbers in a single column violates 1NF. To reach 1NF, multi-valued attributes must be moved to a separate table. 1NF is the foundation; all higher normal forms require 1NF first.

*   **Second Normal Form (2NF)**: A table is in Second Normal Form if it is in 1NF and every non-key attribute is *fully functionally dependent* on the entire primary key. 2NF violations only occur in tables with composite (multi-column) primary keys, where some attributes depend on only part of the key. Correcting a 2NF violation requires splitting the table to isolate partial dependencies.

*   **Third Normal Form (3NF)**: A table is in Third Normal Form if it is in 2NF and no non-key attribute is transitively dependent on the primary key through another non-key attribute. In plain language: every non-key column must depend on the key, the whole key, and nothing but the key. Transitive dependencies cause update anomalies and are eliminated by splitting the dependent attributes into a separate table.

---

### 2. Certification Exam Tips
*   **Normalization Problem Recognition**: The ECBA exam may present a table structure and ask which normal form it violates. The key diagnostic questions: (1) Are there repeating groups or multi-valued columns? → 1NF violation. (2) Is there a composite key where some columns depend on only part of it? → 2NF violation. (3) Does a non-key column determine another non-key column? → 3NF violation.
*   **Referential Integrity**: Know that a foreign key constraint enforces referential integrity, meaning the database will reject any insert or update that would create an "orphan" row (a foreign key value with no matching primary key in the parent table). ECBA scenario questions about data integrity errors often point to missing or incorrectly defined foreign key constraints.
*   **Normalization Trade-offs**: In practice, some databases are intentionally *denormalized* (some redundancy accepted) for read performance. ECBA questions may ask about the trade-off: normalization reduces redundancy and update anomalies but may require more JOINs in queries; denormalization improves read speed but risks inconsistency. The BA's responsibility is to document these decisions as design constraints.
*   **Study Resource**: The Stanford Database Course on Coursera and edX includes a free audit option for the "Databases: Relational Databases and SQL" module at [https://www.edx.org/](https://www.edx.org/) — the normalization section is the most relevant for ECBA candidates who want interactive practice beyond the reading guide.

---

### Required Readings & Videos
*   **Required Reading**: Review the BABOK® Guide v3 Techniques section — "Data Modeling." This frames database design from the BA perspective. Also read the IBM Developer article "A Visual Explanation of SQL Joins" at [https://developer.ibm.com/](https://developer.ibm.com/) for an intuitive grounding in how relational tables connect through keys.
*   **Supplemental Reading**: The Wikipedia article on database normalization at [https://en.wikipedia.org/wiki/Database_normalization](https://en.wikipedia.org/wiki/Database_normalization) provides a well-structured, example-driven explanation of 1NF through 3NF (and beyond) that is freely accessible and aligned to exam-level concepts.

---

### Lab & Activity Integration
In this week's lab, you will:
*   Given an unnormalized "spreadsheet-style" table for a school enrollment system, apply 1NF, 2NF, and 3NF step by step, documenting what changed at each stage.
*   Identify the primary key and define one foreign key relationship in the normalized schema.
*   Write a brief justification (three sentences) explaining why the normalized design is preferable to the original flat table for an enterprise production system.

---

### 3. Study Checklist
- [ ] Read the glossary terms and write your own one-sentence version of each definition.
- [ ] Read BABOK® Guide v3 Techniques — "Data Modeling."
- [ ] Watch the Module 11 video lecture.
- [ ] Review the Wikipedia database normalization article at [https://en.wikipedia.org/wiki/Database_normalization](https://en.wikipedia.org/wiki/Database_normalization).
- [ ] Complete the normalization lab (1NF → 2NF → 3NF) before taking the quiz.

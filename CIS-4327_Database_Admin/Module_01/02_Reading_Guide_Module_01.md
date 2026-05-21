# Reading Guide: Module 01 - Relational Database Fundamentals and SQL Review
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 01 - Relational Database Fundamentals and SQL Review**! This week's study material focuses on the foundational concepts of relational databases and SQL that underpin every GCP database service you will administer. A strong command of relational theory, data integrity constraints, and SQL syntax is required before you can effectively design, migrate, and optimize cloud databases.

As a student, you will learn how tables, primary keys, foreign keys, indexes, and transactions work together to maintain consistent and performant databases. These concepts are tested directly on the Google Cloud Professional Cloud Database Engineer exam in the context of Cloud SQL, Cloud Spanner, and AlloyDB.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Relational Database**: A database that organizes data into structured tables (relations) consisting of rows and columns, where relationships between tables are enforced through primary and foreign key constraints. Google Cloud SQL for MySQL and PostgreSQL are fully managed relational database services built on this model.
*   **ACID Properties**: The four guarantees that define a reliable database transaction — Atomicity (all-or-nothing execution), Consistency (data remains valid before and after), Isolation (concurrent transactions do not interfere), and Durability (committed data survives failures). The GCP exam tests which services provide full ACID compliance: Cloud SQL and Cloud Spanner do; Bigtable and Firestore offer weaker consistency by default.
*   **Primary Key vs. Foreign Key**: A primary key uniquely identifies every row in a table and cannot be NULL. A foreign key in one table references a primary key in another, enforcing referential integrity. Violating this constraint causes INSERT or UPDATE failures — a common exam scenario question.
*   **Index**: A data structure (commonly a B-tree) that allows the database engine to locate rows without scanning every row in a table. Creating indexes on columns used in WHERE, JOIN, and ORDER BY clauses dramatically reduces query latency in Cloud SQL and AlloyDB.
*   **Normalization**: The process of structuring a relational schema to reduce data redundancy and improve integrity. First Normal Form (1NF) eliminates repeating groups; Second Normal Form (2NF) removes partial dependencies; Third Normal Form (3NF) removes transitive dependencies. The exam may ask you to identify a design that violates a normal form.

---

### 2. Certification Exam Tips
*   **Service Selection Scenarios**: The Google Cloud Professional Cloud Database Engineer exam frequently presents a workload description and asks you to select the most appropriate GCP database service. Cloud SQL is the right answer for regional, ACID-compliant relational workloads with lift-and-shift migrations from MySQL, PostgreSQL, or SQL Server. Cloud Spanner is the right answer when you need global distribution and >99.999% availability on a relational schema.
*   **SQL Syntax Questions**: Expect questions on the difference between `INNER JOIN`, `LEFT OUTER JOIN`, and `CROSS JOIN`. Know that `EXPLAIN` / `EXPLAIN ANALYZE` outputs query execution plans — a skill directly tested in the performance tuning and monitoring domains.
*   **Constraints and Integrity**: The exam includes scenario questions where a developer removes a foreign key constraint for performance reasons. Know that this sacrifices referential integrity and can lead to orphaned rows, and that Cloud SQL enforces constraints at the storage engine level (InnoDB for MySQL, native for PostgreSQL).
*   **Study Resource**: The freeCodeCamp full-length SQL and relational database course is an excellent free resource for reviewing SQL syntax and relational theory: [SQL and Relational Databases – freeCodeCamp Full Course](https://www.youtube.com/watch?v=HXV3zeQKqGY). Use it to reinforce concepts before reading the GCP documentation.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The open textbook *Database Design* by Adrienne Watt provides a thorough introduction to relational theory, entity-relationship modeling, and normalization. Read the chapters on the relational model and SQL basics: [Database Design by Adrienne Watt (BCcampus OpenEd)](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This free, comprehensive video lecture covers SQL fundamentals and relational database concepts that align with the GCP exam's foundational domain: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will connect to a Cloud SQL for PostgreSQL instance using the Cloud Shell, create tables with primary and foreign key constraints, run basic DML statements (INSERT, UPDATE, DELETE), and use `EXPLAIN ANALYZE` to read a query execution plan.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the chapters on the relational model and SQL in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the foundational SQL lecture in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.

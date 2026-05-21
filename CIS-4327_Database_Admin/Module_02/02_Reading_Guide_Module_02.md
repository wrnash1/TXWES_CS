# Reading Guide: Module 02 - Database Design – Normalization and ERDs
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 02 - Database Design – Normalization and ERDs**! This week focuses on how to design a sound relational schema before deploying it to any GCP database service. Poor schema design causes data anomalies, excessive storage costs, and slow queries — problems that are expensive to fix after data is in production on Cloud SQL or Cloud Spanner.

You will learn how to read and construct Entity-Relationship Diagrams (ERDs), apply normalization rules through Third Normal Form (3NF), and recognize when denormalization is a valid design trade-off for read-heavy workloads.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Entity-Relationship Diagram (ERD)**: A graphical model that maps the entities (tables), attributes (columns), and relationships (foreign key links) in a database schema. ERDs are used during design to communicate structure before any DDL is written, and the GCP exam may include a diagram to assess whether a schema is correctly normalized.
*   **First Normal Form (1NF)**: A table is in 1NF when every column contains only atomic (indivisible) values and every row is uniquely identifiable. Storing a comma-separated list of phone numbers in one column violates 1NF and prevents efficient querying in Cloud SQL.
*   **Second Normal Form (2NF)**: A table in 2NF must already be in 1NF, and every non-key attribute must depend on the entire primary key — not just part of it. Partial dependencies are only possible in tables with composite primary keys.
*   **Third Normal Form (3NF)**: A table in 3NF must be in 2NF, and no non-key attribute may depend on another non-key attribute (no transitive dependencies). Achieving 3NF reduces update anomalies and is the standard target for OLTP schema design on Cloud SQL and AlloyDB.
*   **Denormalization**: The deliberate reversal of normalization by combining tables or adding redundant columns to reduce JOIN operations at query time. This trade-off is common for read-heavy reporting tables in BigQuery, where columnar storage makes wide, flat tables far more efficient than normalized relational schemas.

---

### 2. Certification Exam Tips
*   **Normalization Scenario Questions**: The GCP Professional Cloud Database Engineer exam presents schemas and asks you to identify the normal form violation or the correct remediation. Practice identifying which normal form is violated and which SQL DDL change (splitting a table, adding a surrogate key, moving a dependent column) fixes it.
*   **ERD to DDL Translation**: Know how to translate an ERD cardinality notation (one-to-many, many-to-many) into actual SQL: a many-to-many relationship requires a junction table with two foreign keys.
*   **Spanner Schema Design**: Cloud Spanner introduces the concept of interleaved tables — a physical schema technique where child rows are stored adjacent to their parent rows on disk. This is a Spanner-specific alternative to normalized table design that eliminates remote joins. Expect at least one Spanner schema question on the exam.
*   **BigQuery vs. OLTP Schema**: Know that BigQuery favors denormalized, wide, nested-and-repeated schemas (using ARRAY and STRUCT types) over traditional 3NF schemas because the columnar engine penalizes JOINs across large tables. The exam tests your ability to choose the right schema style per service.
*   **Study Resource:** The open textbook *Database Design* by Adrienne Watt has dedicated chapters on ERDs and normalization that are freely available and directly relevant to this module: [Database Design by Adrienne Watt (BCcampus OpenEd)](https://opentextbc.ca/dbdesign01/).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The chapters on entity-relationship modeling and normalization in the open textbook provide diagrams and worked examples that match exam question types: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This comprehensive free video lecture covers relational design, normalization, and ERD concepts used across all GCP relational services: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will draw an ERD for a sample business scenario, write the corresponding DDL (CREATE TABLE statements with constraints), load the schema into a Cloud SQL for PostgreSQL instance, and verify that normalization violations are caught by the database engine.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the ERD and normalization chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the schema design and normalization segments in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.

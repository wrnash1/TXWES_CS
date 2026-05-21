# Reading Guide: Module 09 - Relational Databases with PostgreSQL
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

### Introduction
Welcome to **Module 09 - Relational Databases with PostgreSQL**! This module covers relational database design and SQL — the query language used to create, read, update, and delete structured data stored in tables with defined relationships. You will learn how to design schemas with primary and foreign keys, enforce data integrity with constraints, and write JOIN queries to combine related data across tables. PostgreSQL is one of the most widely used relational databases in full-stack development. On AWS, Amazon RDS for PostgreSQL provides a managed hosting service that is directly relevant to the DVA-C02 exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully before beginning the lab and quiz:

*   **SQL schema structure**: The formal definition of a database's tables, columns, data types, constraints, and relationships — typically created with `CREATE TABLE` statements. A well-designed schema normalizes data to eliminate redundancy, defines appropriate data types for each column (`INTEGER`, `TEXT`, `BOOLEAN`, `TIMESTAMP`), and applies constraints to enforce data integrity before records are inserted.
*   **Relational tables**: The core data storage unit in a relational database — a two-dimensional structure of rows (records) and columns (attributes). Each table represents one entity (e.g., `users`, `orders`, `products`), and relationships between entities are expressed through foreign key references rather than embedding data. The relational model, invented by E.F. Codd, ensures data consistency and enables flexible querying via SQL.
*   **PRIMARY KEY**: A column (or combination of columns) that uniquely identifies every row in a table. Primary key values must be unique and non-null. Typically implemented as an auto-incrementing integer (`SERIAL PRIMARY KEY` in PostgreSQL) or a UUID. Every table should have a primary key — it is the target of foreign key references from other tables.
*   **FOREIGN KEY constraints**: Column constraints that enforce referential integrity by requiring that a value in one table's column must match an existing value in another table's primary key column. For example, `FOREIGN KEY (user_id) REFERENCES users(id)` ensures that every `order` record references a valid, existing `user`. `ON DELETE CASCADE` automatically deletes child records when the parent is deleted.
*   **JOIN queries**: SQL clauses that combine rows from two or more tables based on a related column value. `INNER JOIN` returns only rows where the join condition matches in both tables. `LEFT JOIN` returns all rows from the left table plus matching rows from the right (nulls for non-matches). `RIGHT JOIN` and `FULL OUTER JOIN` extend this pattern. Joins are the mechanism for querying relational data that spans multiple tables.

---

### 2. Certification Exam Tips
*   **DVA-C02 Tests Amazon RDS:** The exam tests scenarios involving Amazon RDS for relational databases — including Multi-AZ deployments for high availability, Read Replicas for scaling read workloads, automated backups, and connection management. Knowing the difference between RDS PostgreSQL and Amazon Aurora PostgreSQL (compatible but distributed) is useful for DVA-C02 scenario questions.
*   **SQL Injection is the Top Web Vulnerability:** The DVA-C02 exam tests AWS WAF and security best practices for APIs backed by relational databases. SQL injection — where malicious input is injected into a SQL query string — is mitigated by using parameterized queries (prepared statements). Know that AWS WAF can provide additional protection at the API Gateway level, but parameterized queries in application code are the primary defense.
*   **Study Resource:** The PostgreSQL official documentation is the most complete reference. [PostgreSQL Tutorial — SQL JOIN Types](https://www.postgresqltutorial.com/postgresql-joins/) provides clear diagrams and examples for INNER, LEFT, RIGHT, and FULL OUTER JOINs with practice datasets.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read Part 13 covering **Relational Databases** in the OER Textbook: [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part13) — this section covers PostgreSQL integration with Node.js using the `pg` library and Sequelize ORM.
*   **Required Video:** Watch the SQL and PostgreSQL section of the [Full Stack Web Development Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=nu_pCVPKzTk) — covering schema design, CRUD queries, and JOIN operations.

---

### Lab & Command Integration
In this week's hands-on lab, you will design and query a relational database:
*   **Write raw SQL scripts to create tables**: Write `CREATE TABLE` statements for a `users` table (with `id SERIAL PRIMARY KEY`, `email TEXT UNIQUE NOT NULL`, `created_at TIMESTAMP DEFAULT NOW()`) and an `orders` table with a `user_id FOREIGN KEY` reference.
*   **Insert mock data records using INSERT queries**: Use `INSERT INTO users (email) VALUES ('alice@example.com'), ('bob@example.com')` and insert corresponding orders for each user.
*   **Perform INNER JOIN queries to return relational records**: Write a `SELECT u.email, o.total FROM users u INNER JOIN orders o ON o.user_id = u.id` query to retrieve each user's orders and verify the result against your inserted test data.

---

### 3. Study Checklist
- [ ] Read the glossary terms and understand their definitions in context.
- [ ] Read Part 13 covering **Relational Databases** in [Full Stack Open by University of Helsinki](https://fullstackopen.com/en/part13).
- [ ] Watch the SQL and PostgreSQL section of the [Full Stack Web Development Course by freeCodeCamp](https://www.youtube.com/watch?v=nu_pCVPKzTk).
- [ ] Install [PostgreSQL](https://www.postgresql.org/download/) locally or use a free cloud database (Render, Supabase) to practice SQL queries before the lab.
- [ ] Proceed to the weekly hands-on lab activity.

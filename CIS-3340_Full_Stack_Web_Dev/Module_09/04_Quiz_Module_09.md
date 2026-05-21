# Quiz: Module 09 - Relational Databases with PostgreSQL
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
Which SQL constraint uniquely identifies each record in a database table?
*   A) FOREIGN KEY
*   B) UNIQUE INDEX
*   C) PRIMARY KEY
*   D) DEFAULT
*   **Correct Answer:** C) The `PRIMARY KEY` constraint designates a column (or set of columns) whose values must be unique and non-null for every row, serving as the definitive record identifier and the target for foreign key references from other tables.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `FOREIGN KEY` creates a reference from one table to the primary key of another — it does not uniquely identify records in the table where it is defined.
    *   *Why B is incorrect:* A `UNIQUE INDEX` enforces uniqueness on a column but allows null values and does not carry the same semantic role as a primary key.
    *   *Why C is correct:* `PRIMARY KEY` combines the `UNIQUE` and `NOT NULL` constraints and semantically designates the column as the record identifier.
    *   *Why D is incorrect:* `DEFAULT` specifies a fallback value for a column when no value is supplied during insertion — it has no uniqueness constraint.

---

**Question 2**
Which of the following is the most accurate definition of **JOIN queries** in SQL?
*   A) SQL `INSERT` statements that add new rows from one table into another, merging their data in a single operation.
*   B) SQL clauses that combine rows from two or more tables based on a matching column value — such as `INNER JOIN` (both tables match), `LEFT JOIN` (all left rows plus matching right rows), and `FULL OUTER JOIN` (all rows from both tables).
*   C) SQL `ALTER TABLE` commands that restructure an existing table by adding, removing, or renaming columns to merge two schemas.
*   D) Stored procedures that automatically run whenever a specified table event (INSERT, UPDATE, DELETE) occurs, combining data from related tables into a log.
*   **Correct Answer:** B) SQL clauses that combine rows from two or more tables based on a matching column value — such as `INNER JOIN` (both tables match), `LEFT JOIN` (all left rows plus matching right rows), and `FULL OUTER JOIN` (all rows from both tables).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `INSERT INTO ... SELECT` can copy data between tables but is not a JOIN — JOINs combine data for reading, not inserting.
    *   *Why B is correct:* This accurately describes SQL JOIN operations — the mechanism for querying relational data across multiple tables.
    *   *Why C is incorrect:* `ALTER TABLE` modifies schema structure — it does not combine data from multiple tables.
    *   *Why D is incorrect:* This describes database triggers — automatic event-driven procedures that are distinct from JOIN queries.

---

**Question 3**
A developer writes this SQL query but no rows are returned, even though matching data exists in both tables. What is the most likely problem?

```sql
SELECT u.name, o.total
FROM users u
INNER JOIN orders o ON o.user_id = users.id;
```

*   A) `INNER JOIN` does not work with aliases — the developer must use `FULL OUTER JOIN` instead.
*   B) The ON clause references `users.id` using the table name instead of the alias `u.id` — the mixed reference causes the join condition to fail.
*   C) The `SELECT` clause must list all columns from both tables — selecting only `u.name` and `o.total` returns no rows.
*   D) SQL aliases (`u`, `o`) cannot be used in the same query as their full table names — all references must use the full table name.
*   **Correct Answer:** B) The ON clause references `users.id` using the table name instead of the alias `u.id` — the mixed reference causes the join condition to fail.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* `INNER JOIN` works correctly with aliases — this is standard SQL syntax.
    *   *Why B is correct:* Once an alias (`u`) is defined for a table in a query, that alias must be used consistently — mixing the alias and the original name in the same clause causes an ambiguity or reference error.
    *   *Why C is incorrect:* Selecting specific columns is perfectly valid in SQL — `SELECT *` is not required.
    *   *Why D is incorrect:* SQL allows mixing aliases and full table names in the same query, though consistency is recommended — this is not the syntax rule that applies here.

---

**Question 4**
A web application queries a PostgreSQL database by building a SQL string with user-supplied input: `"SELECT * FROM users WHERE email = '" + userInput + "'"`. A user enters `' OR '1'='1`. What vulnerability does this expose and how is it fixed?
*   A) This is a Cross-Site Scripting (XSS) attack — fix it by encoding HTML special characters in the output with `encodeURIComponent()`.
*   B) This is a SQL injection attack — fix it by using parameterized queries (prepared statements) that pass user input as a separate parameter rather than concatenating it into the query string.
*   C) This is a CSRF attack — fix it by adding a `SameSite=Strict` cookie attribute to the session cookie.
*   D) This is a denial-of-service attack — fix it by rate-limiting the `/login` endpoint with Express middleware.
*   **Correct Answer:** B) This is a SQL injection attack — fix it by using parameterized queries (prepared statements) that pass user input as a separate parameter rather than concatenating it into the query string.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* XSS attacks inject malicious scripts into HTML output — this is a SQL injection attack targeting the database layer.
    *   *Why B is correct:* The input `' OR '1'='1` breaks out of the string literal and injects a condition that returns all rows. Parameterized queries treat all user input as data, never as executable SQL.
    *   *Why C is incorrect:* CSRF (Cross-Site Request Forgery) attacks trick authenticated users into making unintended requests — unrelated to SQL injection.
    *   *Why D is incorrect:* This is not a denial-of-service pattern — rate limiting does not prevent SQL injection.

---

**Question 5**
On AWS, which service provides a managed relational database compatible with PostgreSQL that eliminates the need to patch, backup, or manage the underlying database server?
*   A) Amazon DynamoDB
*   B) Amazon ElastiCache
*   C) Amazon RDS for PostgreSQL
*   D) AWS Glue
*   **Correct Answer:** C) Amazon RDS for PostgreSQL is a fully managed relational database service that handles automated backups, software patching, Multi-AZ replication, and storage scaling — allowing developers to focus on application logic instead of database administration.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Amazon DynamoDB is a NoSQL key-value and document database — it does not support SQL or a relational data model.
    *   *Why B is incorrect:* Amazon ElastiCache provides managed Redis and Memcached in-memory caching — not a relational database.
    *   *Why C is correct:* RDS for PostgreSQL offers the full PostgreSQL feature set in a managed environment, including read replicas, automated snapshots, and VPC network isolation.
    *   *Why D is incorrect:* AWS Glue is a serverless ETL (Extract, Transform, Load) service for data pipelines and cataloging — not a relational database hosting service.

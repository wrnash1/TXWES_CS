# Reading Guide: Module 01 — Relational Database Fundamentals and SQL Review

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Introduction

Welcome to Module 01. This reading guide provides the conceptual depth you need to succeed in both the hands-on lab and the Google Cloud Professional Cloud Database Engineer certification exam. Relational database fundamentals are tested across multiple exam domains — not just in isolated theory questions. When you are asked to select a Cloud SQL configuration, troubleshoot a query performance issue, or design a migration strategy, you are drawing on the concepts in this module.

Work through each section carefully. The glossary, reference tables, SQL examples, and exam tips are all designed to build on each other. Complete this reading guide before attempting the lab or quiz.

---

### 1. High-Yield Glossary

The following terms appear frequently on the GCP Database Engineer exam. Memorize definitions and be able to apply each concept to a scenario.

**Relation**: The formal term for a table in the relational model. A relation is a set of tuples (rows) that share the same attributes (columns). No two tuples in a relation are identical — the primary key guarantee enforces this.

**Tuple**: A single row in a table. Each tuple is a set of attribute values corresponding to the table's column definitions.

**Attribute**: A column in a table. Each attribute has a defined data type, optional constraints, and a name unique within the relation.

**Primary Key (PK)**: One or more columns whose combined values uniquely identify every row in a table. A primary key column cannot contain NULL. In Cloud SQL, the primary key is typically implemented as a clustered index in MySQL (InnoDB) or a B-tree index in PostgreSQL.

**Surrogate Key**: A system-generated identifier with no business meaning, such as an auto-incrementing integer or a UUID. Surrogate keys are preferred when natural keys are unstable or composite.

**Natural Key**: A key formed from real-world attributes, such as an email address or a social security number. Natural keys can change, which complicates foreign key relationships.

**Foreign Key (FK)**: A column or group of columns in one table that references the primary key of another table. Foreign keys enforce referential integrity — a child row cannot reference a parent row that does not exist.

**Referential Integrity**: The guarantee that every foreign key value in a child table matches an existing primary key value in the parent table. Enforced at the database engine level by foreign key constraints.

**ACID Properties**: The four transactional guarantees — Atomicity, Consistency, Isolation, Durability. Covered in detail in Section 2 below.

**Normalization**: The process of organizing a relational schema to eliminate data redundancy and update anomalies. Covered in depth in Module 02.

**Index**: A data structure, commonly a B-tree, that enables efficient lookup of rows by one or more column values without scanning the entire table.

**B-Tree Index**: The default index type in both MySQL and PostgreSQL. Supports equality lookups, range queries, and ORDER BY operations efficiently.

**Hash Index**: Supports only equality lookups (=). Faster than B-tree for equality, but cannot be used for range queries or sorting. Supported in PostgreSQL for in-memory operations.

**Composite Index**: An index on two or more columns. The order of columns in a composite index matters — the index is most useful when queries filter on the leftmost columns first.

**Query Execution Plan**: The sequence of operations the database engine uses to retrieve data for a query. Produced by EXPLAIN or EXPLAIN ANALYZE. Includes information about scans, joins, sort methods, and estimated costs.

**Sequential Scan (Seq Scan)**: Reading every row in a table from beginning to end. Efficient for small tables or when most rows must be returned. A warning sign on large tables in a filtered query.

**Index Scan**: Using an index to locate specific rows. Efficient when only a small fraction of rows match the filter condition.

**Transaction**: A logical unit of work consisting of one or more SQL statements. Must exhibit ACID properties. Bounded by BEGIN and COMMIT (or ROLLBACK).

**Deadlock**: A situation where two or more transactions are each waiting for the other to release a lock, causing all to be blocked indefinitely. Database engines detect deadlocks and abort one transaction automatically.

**Connection Pooling**: Maintaining a pool of pre-established database connections that application threads reuse, rather than opening and closing a connection for each request. Reduces connection overhead significantly in high-concurrency environments.

**DDL (Data Definition Language)**: SQL commands that define database structure: CREATE, ALTER, DROP, TRUNCATE, RENAME.

**DML (Data Manipulation Language)**: SQL commands that manipulate data: SELECT, INSERT, UPDATE, DELETE, MERGE.

**DCL (Data Control Language)**: SQL commands that control access: GRANT, REVOKE.

**TCL (Transaction Control Language)**: SQL commands that manage transactions: BEGIN, COMMIT, ROLLBACK, SAVEPOINT.

---

### 2. ACID Properties — Deep Reference

ACID is the most tested concept in the relational fundamentals domain of the GCP exam. Study this table carefully.

| Property | Definition | Example | Cloud SQL Behavior |
|---|---|---|---|
| Atomicity | All operations in a transaction succeed or all are rolled back | Bank transfer: debit and credit are one atomic unit | InnoDB/PostgreSQL engines enforce atomicity via write-ahead logging |
| Consistency | A transaction brings the database from one valid state to another | A constraint violation causes the entire transaction to roll back | All defined constraints checked at COMMIT time |
| Isolation | Concurrent transactions do not see each other's intermediate states | Two simultaneous updates to the same row are serialized | Configurable isolation levels: READ UNCOMMITTED through SERIALIZABLE |
| Durability | Committed transactions survive crashes | Power loss after COMMIT does not lose data | WAL log flushed to disk before COMMIT acknowledgment |

#### Isolation Levels

PostgreSQL and MySQL support four standard SQL isolation levels. The exam tests the trade-offs between consistency and concurrency.

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
|---|---|---|---|
| READ UNCOMMITTED | Possible | Possible | Possible |
| READ COMMITTED | Prevented | Possible | Possible |
| REPEATABLE READ | Prevented | Prevented | Possible (MySQL: prevented) |
| SERIALIZABLE | Prevented | Prevented | Prevented |

READ COMMITTED is the default isolation level in PostgreSQL. REPEATABLE READ is the default in MySQL (InnoDB). SERIALIZABLE provides the strongest guarantees but has the highest performance cost due to lock contention.

---

### 3. SQL Reference Tables

#### DDL Commands

| Command | Syntax Pattern | Effect |
|---|---|---|
| CREATE TABLE | `CREATE TABLE name (col type constraint, ...)` | Defines a new table |
| ALTER TABLE ADD COLUMN | `ALTER TABLE name ADD COLUMN col type` | Adds a new column |
| ALTER TABLE DROP COLUMN | `ALTER TABLE name DROP COLUMN col` | Removes a column and its data |
| CREATE INDEX | `CREATE INDEX name ON table (col)` | Builds a B-tree index |
| DROP TABLE | `DROP TABLE IF EXISTS name` | Removes table and all data |
| TRUNCATE | `TRUNCATE TABLE name` | Removes all rows, faster than DELETE |

#### DML Commands

| Command | Syntax Pattern | Effect |
|---|---|---|
| SELECT | `SELECT cols FROM table WHERE cond` | Retrieves rows |
| INSERT | `INSERT INTO table (cols) VALUES (vals)` | Adds rows |
| UPDATE | `UPDATE table SET col=val WHERE cond` | Modifies existing rows |
| DELETE | `DELETE FROM table WHERE cond` | Removes rows |

#### JOIN Types

| JOIN Type | Returns | Use Case |
|---|---|---|
| INNER JOIN | Only rows with matches in both tables | Most common; requires a relationship to exist |
| LEFT OUTER JOIN | All rows from left table, NULLs on right | Find all left records including those with no match |
| RIGHT OUTER JOIN | All rows from right table, NULLs on left | Find all right records including those with no match |
| FULL OUTER JOIN | All rows from both tables, NULLs where no match | Complete view of both tables with or without matches |
| CROSS JOIN | Every combination of rows from both tables | Produces a Cartesian product; rarely used intentionally |

#### Aggregate Functions

| Function | Description | Example |
|---|---|---|
| COUNT() | Number of rows or non-NULL values | `COUNT(order_id)` |
| SUM() | Total of numeric column values | `SUM(order_total)` |
| AVG() | Average of numeric column values | `AVG(order_total)` |
| MAX() | Highest value | `MAX(order_date)` |
| MIN() | Lowest value | `MIN(order_date)` |

---

### 4. GCP Database Service Comparison

Understanding when to use each GCP database service is a core exam competency. Use this table as a quick reference.

| Service | Model | ACID | Scale | Best For |
|---|---|---|---|---|
| Cloud SQL | Relational | Full | Regional, vertical | Lift-and-shift MySQL/PostgreSQL/SQL Server |
| Cloud Spanner | Relational | Full | Global, horizontal | Global OLTP, financial systems |
| AlloyDB | Relational (PostgreSQL) | Full | Regional, read replicas | High-performance PostgreSQL workloads |
| Firestore | Document (NoSQL) | Single-document | Global, automatic | Mobile/web apps, flexible schema |
| Bigtable | Wide-column (NoSQL) | No multi-row | Massive scale | Time-series, IoT, analytics at petabyte scale |
| BigQuery | Columnar analytical | No row-level | Serverless, unlimited | Data warehouse, OLAP, BI reporting |
| Memorystore | Key-value (Redis/Memcached) | No | Regional | Caching, session storage, leaderboards |

---

### 5. Constraint Behavior Reference

| Constraint | ON INSERT (violation) | ON UPDATE (violation) | ON DELETE behavior options |
|---|---|---|---|
| PRIMARY KEY | Rejected — duplicate key | Rejected — duplicate key | N/A |
| FOREIGN KEY (child table) | Rejected — parent row missing | Rejected — parent row missing | RESTRICT, CASCADE, SET NULL, SET DEFAULT, NO ACTION |
| UNIQUE | Rejected — duplicate value | Rejected — duplicate value | N/A |
| NOT NULL | Rejected — NULL value | Rejected — NULL value | N/A |
| CHECK | Rejected — condition false | Rejected — condition false | N/A |

ON DELETE CASCADE is important for exam questions. If a parent row is deleted and the FK constraint uses CASCADE, all child rows are automatically deleted. If RESTRICT is used, the parent delete fails unless children are removed first.

---

### 6. EXPLAIN ANALYZE — Reading Query Plans

EXPLAIN ANALYZE is a critical skill for the performance tuning and monitoring exam domains. Learn to identify these node types in an execution plan.

| Node Type | Meaning | Action |
|---|---|---|
| Seq Scan | Full table scan — every row read | Consider adding an index if table is large |
| Index Scan | Uses index to find rows | Efficient for selective queries |
| Index Only Scan | Retrieves data from index alone — no table access | Most efficient; requires covering index |
| Nested Loop | For each row in outer table, scan inner table | Efficient when outer table is small |
| Hash Join | Builds a hash table from one input, probes with other | Efficient for large unsorted tables |
| Merge Join | Merges two pre-sorted inputs | Efficient when both sides are already sorted |
| Sort | Sort operation | Check if an index on ORDER BY columns can eliminate this |
| Aggregate | GROUP BY or aggregate function processing | Normal for aggregation queries |

The key metrics in EXPLAIN ANALYZE output:

- **cost=X..Y** — planner's estimated cost. X is startup cost, Y is total cost.
- **rows=N** — planner's estimated row count.
- **actual time=X..Y** — real execution time in milliseconds.
- **actual rows=N** — actual rows processed.
- **loops=N** — how many times this node executed.

When actual rows is far higher or lower than estimated rows, table statistics may be stale. Run `ANALYZE tablename;` to update statistics.

---

### 7. Normalization Preview

Module 02 covers normalization in full detail. Here is a preview of the three normal forms most frequently tested on the exam.

**First Normal Form (1NF)**: Every column contains atomic (indivisible) values. No repeating groups or multi-valued columns. Every row is uniquely identifiable.

**Second Normal Form (2NF)**: Must be in 1NF, and every non-key attribute must be fully functionally dependent on the entire primary key. Violations occur only in tables with composite primary keys — a non-key column depends on only part of the key.

**Third Normal Form (3NF)**: Must be in 2NF, and no non-key attribute is transitively dependent on the primary key through another non-key attribute. Example: if a table stores employee_id, department_id, and department_name, the department_name depends on department_id (not directly on employee_id), which is a transitive dependency.

---

### 8. Required Readings and Resources

Complete these resources before the lab and quiz.

**Open Textbook — Database Design by Adrienne Watt (BCcampus OpenEd)**: This zero-cost textbook covers the relational model, SQL fundamentals, normalization, and ER modeling at the appropriate depth for this course. Read the chapters on the relational model, SQL basics, and integrity constraints. Available at opentextbc.ca/dbdesign01 — no account required.

**GCP Documentation — Cloud SQL Overview**: Review the Cloud SQL product overview and the concepts section covering supported database engines, instance types, and storage. Available at cloud.google.com/learn.

**GCP Documentation — Choosing a Database**: GCP provides a database selection guide that aligns exactly with exam scenario questions. Study the decision criteria for each service.

---

### 9. Exam Tips

The following tips are based on the specific question patterns used in the Google Cloud Professional Cloud Database Engineer exam.

**Tip 1 — Service Selection**: When a scenario mentions ACID, transactional workload, and a single region, select Cloud SQL. When the scenario adds global distribution or multi-region consistency, select Cloud Spanner. These are the two most common exam traps in this domain.

**Tip 2 — JOIN Identification**: Read JOIN questions carefully. An INNER JOIN drops rows with no match. A LEFT JOIN keeps all rows from the left table. Adding `WHERE right_table.id IS NULL` to a LEFT JOIN finds records with no match — a common anti-join pattern in exam questions.

**Tip 3 — WHERE vs. HAVING**: WHERE filters individual rows before aggregation. HAVING filters groups after GROUP BY. If you see a question asking to filter on a COUNT() or SUM() result, the answer uses HAVING.

**Tip 4 — EXPLAIN vs. EXPLAIN ANALYZE**: EXPLAIN produces a plan without executing the query. EXPLAIN ANALYZE executes the query and returns actual timing. Use EXPLAIN ANALYZE when you need real performance data. EXPLAIN alone is safe to run on production queries without executing them.

**Tip 5 — Constraint Violations**: Know what happens when each constraint is violated. The exam presents scenarios where a developer removes a foreign key constraint for performance. The consequence is orphaned rows — child rows that reference non-existent parent rows. This is always the wrong answer in a data integrity context.

**Tip 6 — Index Selectivity**: An index is most effective when the column has high cardinality — many distinct values. An index on a boolean column (true/false) is rarely useful because it still accesses half the table. An index on a primary key or email column is highly selective.

**Tip 7 — ON DELETE CASCADE vs. RESTRICT**: ON DELETE CASCADE deletes child rows automatically when a parent is deleted. ON DELETE RESTRICT (the default) prevents parent deletion when children exist. Exam scenarios about preventing accidental data loss point to RESTRICT. Scenarios about automating cleanup point to CASCADE.

**Tip 8 — Isolation Levels**: READ COMMITTED is the PostgreSQL default. REPEATABLE READ is the MySQL/InnoDB default. SERIALIZABLE prevents all anomalies but has the highest contention cost. Exam questions about phantom reads specifically involve non-SERIALIZABLE isolation levels.

---

### 10. Study Checklist

Work through this checklist before proceeding to the lab.

- Read the relational model and SQL basics chapters in Database Design by Adrienne Watt at opentextbc.ca/dbdesign01
- Define all 20 glossary terms in Section 1 from memory
- Reproduce the CREATE TABLE statements from the video script without looking at them
- State the four ACID properties and provide a one-sentence example for each
- Identify the difference between INNER JOIN, LEFT JOIN, and FULL OUTER JOIN
- Write a GROUP BY query with a HAVING filter from memory
- Explain what a Seq Scan in EXPLAIN ANALYZE output means and how to address it
- State the difference between ON DELETE CASCADE and ON DELETE RESTRICT
- Complete the Module 01 lab activity in Cloud Shell
- Pass the Module 01 quiz with at least 80 percent

---

Reference: cloud.google.com/learn

---

## 9. Supplemental Resources

**1. PostgreSQL Official Documentation — The Query Planner**
https://www.postgresql.org/docs/current/planner-optimizer.html
Explains how PostgreSQL generates execution plans, interprets EXPLAIN output, and uses table statistics to choose between sequential scans and index scans.

**2. Google Cloud — Cloud SQL for PostgreSQL Concepts**
https://cloud.google.com/sql/docs/postgres/concepts
Covers instance configuration, connection options, high availability, read replicas, and maintenance windows specific to Cloud SQL for PostgreSQL.

**3. Use The Index, Luke — A Guide to Database Performance for Developers**
https://use-the-index-luke.com/
A free, vendor-neutral reference covering B-tree index internals, composite index column ordering, partial indexes, and how execution plans change with and without indexes.

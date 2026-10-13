# Quiz: Module 01 — Relational Database Fundamentals and SQL Review

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer for each question. Distractor analysis is provided to reinforce exam-level reasoning.

---

### Question 1

Your company is developing a multiplayer mobile game that requires user profiles to be stored as JSON documents. The app needs to support offline synchronization for mobile clients. Which Google Cloud database service is the most appropriate choice?

- A) Cloud SQL
- B) Cloud Spanner
- C) Cloud Bigtable
- D) Firestore

Correct Answer: D — Firestore is a serverless document database with native SDKs for Android, iOS, and web clients. It supports offline data persistence and automatic synchronization when connectivity is restored, making it the correct choice for this scenario.

Distractor analysis: A is incorrect because Cloud SQL is a relational database designed for structured tabular data and ACID transactions; it does not provide mobile offline synchronization. B is incorrect because Cloud Spanner is a globally distributed relational database for high-availability OLTP workloads, not document storage or offline sync. C is incorrect because Bigtable is a wide-column NoSQL store optimized for massive analytical and time-series workloads, not mobile app backends requiring offline capability.

---

### Question 2

You are migrating an on-premises PostgreSQL database to Google Cloud. The application serves users in a single geographic region and requires strong ACID consistency. Which service minimizes migration effort while meeting requirements?

- A) Cloud SQL for PostgreSQL
- B) Cloud Spanner
- C) BigQuery
- D) Firestore

Correct Answer: A — Cloud SQL for PostgreSQL accepts near-direct lift-and-shift migrations from on-premises PostgreSQL. It provides full ACID compliance, supports the same SQL syntax and extensions, and is the appropriate choice for a regional workload.

Distractor analysis: B is incorrect because Cloud Spanner supports a PostgreSQL-compatible dialect but requires significant schema and application changes for its distributed architecture, making it overengineered for a single-region workload. C is incorrect because BigQuery is an analytical data warehouse with no row-level ACID transaction support. D is incorrect because Firestore is a NoSQL document store that would require a complete data model redesign.

---

### Question 3

A database administrator needs to assign read-only access privileges on a table to a specific security role. Which SQL command is most appropriate?

- A) `GRANT SELECT ON orders TO analyst_role;`
- B) `CREATE INDEX idx_email ON customers(email);`
- C) `EXPLAIN ANALYZE SELECT * FROM orders;`
- D) `ALTER TABLE orders ADD COLUMN notes TEXT;`

Correct Answer: A — GRANT is the SQL Data Control Language command for assigning privileges. `GRANT SELECT` specifically grants read-only query access on the named table to the specified role.

Distractor analysis: B is incorrect because CREATE INDEX is a DDL command that creates a performance structure and has no effect on user privileges. C is incorrect because EXPLAIN ANALYZE is a diagnostic tool for query performance and does not modify permissions. D is incorrect because ALTER TABLE modifies schema structure and does not grant or revoke any access privileges.

---

### Question 4

While administering a Cloud SQL for MySQL instance, you receive an alert that a database deadlock has occurred. Which action most effectively resolves and prevents recurrence?

- A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
- B) Increase the database connection pool limit and scale the instance to more CPUs.
- C) Reboot the Cloud SQL instance from the Google Cloud Console.
- D) Add indexes on all columns referenced in WHERE and JOIN clauses.

Correct Answer: A — A deadlock occurs when two or more transactions are each waiting for the other to release a lock. The correct fix ensures transactions acquire locks in a consistent order, keeps transactions short to minimize lock hold time, and adds application-level retry logic so the application recovers gracefully when the database auto-resolves a deadlock by aborting one transaction.

Distractor analysis: B is incorrect because increasing connections or CPUs raises concurrency and can worsen lock contention. C is incorrect because rebooting clears active connections temporarily but does not fix the application logic; the deadlock recurs immediately. D is incorrect because index tuning addresses slow sequential scans, not lock ordering conflicts between concurrent transactions.

---

### Question 5

When securing a Cloud SQL instance, you must mitigate the risk of attackers injecting malicious SQL strings that bypass authentication and read database contents. Which control best addresses this vulnerability?

- A) Enforce parameterized queries and prepared statements in all application code.
- B) Enable Customer-Managed Encryption Keys (CMEK) for storage encryption at rest.
- C) Configure Cloud SQL to use Private IP only and disable public IP access.
- D) Enable Cloud SQL Auth Proxy to encrypt all in-transit connections.

Correct Answer: A — SQL injection exploits unsanitized user input concatenated directly into SQL strings. Parameterized queries pass user input as bound parameters that are never interpreted as SQL syntax, making injection structurally impossible regardless of the input content.

Distractor analysis: B is incorrect because CMEK protects data stored on disk and has no effect on how SQL strings are constructed in application code. C is incorrect because Private IP reduces network attack surface but does not prevent SQL injection from a legitimate internal application that concatenates unvalidated input. D is incorrect because Cloud SQL Auth Proxy secures the connection channel; an injected payload travels through an encrypted channel just as easily as a legitimate query.

---

### Question 6

A table named `sales` contains 50 million rows. A developer reports the query below is very slow. EXPLAIN ANALYZE shows a Seq Scan on the sales table. What is the most likely cause and the correct fix?

```sql
SELECT region, SUM(amount)
FROM   sales
WHERE  sale_date = '2025-01-15'
GROUP  BY region;
```

- A) Create an index on the `sale_date` column to allow an Index Scan.
- B) Add a PRIMARY KEY constraint to the `amount` column.
- C) Replace GROUP BY with a subquery using COUNT().
- D) Increase the Cloud SQL instance machine type to add more RAM.

Correct Answer: A — The Seq Scan on a 50-million-row table indicates the planner cannot use an index for the WHERE filter on `sale_date`. Creating an index on `sale_date` allows the planner to use an Index Scan, locating only the rows for the target date without reading the entire table.

Distractor analysis: B is incorrect because adding a PRIMARY KEY to `amount` makes no architectural sense and would not affect the scan type. C is incorrect because replacing GROUP BY with a subquery does not change the data access method; the full table still must be examined. D is incorrect because adding RAM may speed up a sequential scan marginally via caching but does not eliminate it; the root cause is the missing index.

---

### Question 7

Which SQL clause filters rows after GROUP BY aggregation, and what is the key difference between it and the WHERE clause?

- A) HAVING filters groups after aggregation; WHERE filters individual rows before aggregation.
- B) WHERE filters groups after aggregation; HAVING filters individual rows before aggregation.
- C) HAVING and WHERE are interchangeable; either can filter both rows and groups.
- D) HAVING applies only to JOIN operations; WHERE applies only to single-table queries.

Correct Answer: A — WHERE is evaluated before GROUP BY and filters individual rows. HAVING is evaluated after GROUP BY and filters the resulting groups. This distinction is necessary when filtering on an aggregate value such as `HAVING COUNT(*) > 5`.

Distractor analysis: B is incorrect because this reverses the definitions; WHERE is evaluated before aggregation occurs. C is incorrect because they are not interchangeable — using `WHERE COUNT(*) > 5` produces a syntax error since the aggregate value does not exist at WHERE evaluation time. D is incorrect because both clauses can appear in multi-table JOIN queries and single-table queries; the distinction is evaluation order relative to aggregation.

---

### Question 8

You are designing a Cloud SQL schema for an order management system. The orders table references the customers table via a foreign key. You want to prevent any customer record from being deleted while they have active orders. Which foreign key option achieves this?

- A) `ON DELETE RESTRICT`
- B) `ON DELETE CASCADE`
- C) `ON DELETE SET NULL`
- D) `ON DELETE SET DEFAULT`

Correct Answer: A — ON DELETE RESTRICT prevents deletion of a parent row when matching child rows exist. An attempt to delete a customer who has orders fails with a foreign key constraint violation until all associated orders are removed first.

Distractor analysis: B is incorrect because ON DELETE CASCADE automatically deletes all child orders when a customer is deleted, which destroys order history — the opposite of the requirement. C is incorrect because ON DELETE SET NULL sets the foreign key column in child rows to NULL, creating orders with no customer reference. D is incorrect because ON DELETE SET DEFAULT sets the foreign key column to its default value, which may not be a valid customer_id and produces logically incorrect data.

---

### Question 9

Which two GCP database services provide full ACID transaction compliance?

- A) Cloud Spanner and AlloyDB
- B) Cloud SQL and Bigtable
- C) Firestore and Bigtable
- D) BigQuery and Cloud SQL

Correct Answer: A — Cloud Spanner provides full ACID compliance globally across distributed regions. AlloyDB provides full ACID compliance for high-performance PostgreSQL workloads. Both services guarantee all four ACID properties for their supported transaction models.

Distractor analysis: B is incorrect because Bigtable does not provide multi-row ACID transactions; it is optimized for high-throughput single-row operations. C is incorrect because Firestore provides only single-document ACID semantics and Bigtable provides no multi-row transaction guarantees. D is incorrect because BigQuery is a columnar analytical warehouse with no row-level transaction support.

---

### Question 10

A developer runs EXPLAIN ANALYZE on a query and observes the following in the output: `actual rows=482000  rows=150`. What does this discrepancy indicate and what is the recommended action?

- A) Table statistics are stale; run ANALYZE on the table to update the planner's row count estimates.
- B) The query has a bug in the WHERE clause that is returning too many rows.
- C) The index on the filtered column is corrupted; drop and recreate the index.
- D) The database instance needs more memory to hold the result set in cache.

Correct Answer: A — The `rows` value is the planner's estimate while `actual rows` is the true count from execution. A large gap between estimated (150) and actual (482,000) rows means the query planner has outdated statistics. Running `ANALYZE tablename` refreshes the statistical histogram the planner uses to estimate row counts, producing more accurate execution plans.

Distractor analysis: B is incorrect because returning many rows may be correct behavior; the issue is that the planner did not predict it, which is a statistics problem rather than a query logic error. C is incorrect because index corruption typically produces execution errors, not a row count mismatch between estimated and actual values. D is incorrect because adding memory improves caching performance but does not affect the planner's statistical estimates; accurate statistics are needed for good plan selection.

---

Reference: cloud.google.com/learn

---

### Question 11 (5 points)

Which isolation level prevents dirty reads but still allows non-repeatable reads, and is the default in PostgreSQL?

- A) READ COMMITTED
- B) READ UNCOMMITTED
- C) REPEATABLE READ
- D) SERIALIZABLE

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) READ UNCOMMITTED allows dirty reads (reading uncommitted changes from other transactions), which is the least restrictive level and not the PostgreSQL default.
  - C) REPEATABLE READ prevents both dirty reads and non-repeatable reads; it is the MySQL/InnoDB default, not PostgreSQL's default.
  - D) SERIALIZABLE prevents all three anomalies (dirty reads, non-repeatable reads, and phantom reads) and carries the highest performance cost due to lock contention.

---

### Question 12 (5 points)

A DBA runs the following command on a PostgreSQL table after a large batch load of 10 million rows. What is the primary purpose of this command?

```sql
ANALYZE sales_transactions;
```

- A) It updates the statistical metadata the query planner uses to estimate row counts and choose execution plans.
- B) It rebuilds all indexes on the table to eliminate fragmentation and reclaim disk space.
- C) It scans for and repairs any data corruption in the table's heap pages.
- D) It computes and stores aggregate totals (SUM, AVG) for all numeric columns to speed up future GROUP BY queries.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Rebuilding indexes is the function of REINDEX, not ANALYZE; ANALYZE only collects statistics and does not touch index structures.
  - C) Data corruption detection and repair is performed by pg_dump validation, VACUUM FULL, or third-party tools; ANALYZE does not inspect or repair heap pages.
  - D) ANALYZE collects column-level statistical samples (histograms, most-common values), not precomputed aggregate totals; it does not speed up GROUP BY through precomputation.

---

### Question 13 (5 points)

You need to retrieve all customers along with their most recent order date. Customers who have never placed an order should still appear in the result with a NULL order date. Which SQL pattern is correct?

- A) `SELECT c.full_name, MAX(o.order_date) FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.customer_id, c.full_name;`
- B) `SELECT c.full_name, MAX(o.order_date) FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.customer_id, c.full_name;`
- C) `SELECT c.full_name, MAX(o.order_date) FROM orders o RIGHT JOIN customers c ON c.customer_id = o.customer_id WHERE o.order_id IS NOT NULL GROUP BY c.customer_id, c.full_name;`
- D) `SELECT c.full_name, MAX(o.order_date) FROM customers c CROSS JOIN orders o GROUP BY c.customer_id, c.full_name;`

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) INNER JOIN only returns customers who have at least one matching order; customers with no orders are excluded from the result set entirely.
  - C) Adding `WHERE o.order_id IS NOT NULL` after a RIGHT JOIN converts the outer join to an effective inner join, again excluding customers with no orders.
  - D) CROSS JOIN produces a Cartesian product of every customer with every order, generating nonsensical results and vastly inflating row counts.

---

### Question 14 (5 points)

A developer proposes using a UUID (universally unique identifier) as a primary key instead of a SERIAL auto-increment integer on a high-write PostgreSQL table. What is the primary performance concern with this approach?

- A) UUID primary keys cause random B-tree index page splits and increased fragmentation compared to sequentially inserted integers.
- B) UUID values are 128 bits and cannot be stored in a PostgreSQL INTEGER column type.
- C) The database engine cannot enforce UNIQUE constraints on UUID columns.
- D) UUID generation requires an external sequence generator that creates a network bottleneck.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) This is a storage type issue, not a performance concern; PostgreSQL provides a native UUID data type that stores 128-bit values efficiently; the question is about the performance trade-off, not storage impossibility.
  - C) UUID columns fully support UNIQUE constraints; the concern is performance, not correctness of constraint enforcement.
  - D) PostgreSQL generates UUIDs locally using built-in functions (gen_random_uuid()) with no external network calls; there is no network bottleneck in standard UUID generation.

---

### Question 15 (5 points)

Which SQL command permanently removes all rows from a table and resets any auto-increment sequences, but does NOT fire row-level triggers and cannot be rolled back in most RDBMS systems?

- A) TRUNCATE TABLE orders;
- B) DELETE FROM orders;
- C) DROP TABLE orders;
- D) ALTER TABLE orders DISABLE TRIGGER ALL;

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) DELETE FROM is a DML command that fires row-level triggers, can be rolled back within an open transaction, and does not reset sequences; it is slower than TRUNCATE on large tables.
  - C) DROP TABLE removes the table definition and all its data entirely, not just the rows; the schema must be recreated to use the table again.
  - D) ALTER TABLE DISABLE TRIGGER ALL disables triggers on the table but does not remove any rows; it is unrelated to data deletion.

---

### Question 16 (5 points)

A Cloud SQL for PostgreSQL instance is experiencing high CPU utilization during business hours. The DBA reviews pg_stat_activity and finds hundreds of connections in the "idle" state. What is the most appropriate corrective action?

- A) Deploy PgBouncer or configure Cloud SQL's built-in connection pooling to reuse idle connections rather than maintaining one per application thread.
- B) Increase the max_connections parameter in the Cloud SQL instance flags to allow more simultaneous connections.
- C) Scale the Cloud SQL instance to a higher machine type with more vCPUs to process idle connections faster.
- D) Terminate all idle connections using pg_terminate_backend() and restart the application.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Increasing max_connections raises the ceiling but does not eliminate idle connections; each PostgreSQL connection consumes memory regardless of state, so more connections worsen memory pressure without solving the underlying pooling problem.
  - C) Scaling vCPUs does not reduce idle connection count; idle connections consume memory, not CPU, and adding CPUs does not address memory pressure from hundreds of idle sessions.
  - D) Terminating idle connections provides only temporary relief; without connection pooling, the application immediately re-establishes the same number of connections after reconnecting.

---

### Question 17 (5 points)

What does the following PostgreSQL statement accomplish?

```sql
CREATE INDEX CONCURRENTLY idx_orders_customer_status
ON orders (customer_id, status);
```

- A) It builds a composite index on two columns without locking the table for writes during index construction.
- B) It creates a partial index that only indexes rows where customer_id and status are both non-NULL.
- C) It builds a unique composite index that enforces the combination of customer_id and status to be unique.
- D) It creates two separate single-column indexes on customer_id and status simultaneously in a single statement.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) A partial index requires an explicit WHERE clause (e.g., `WHERE status = 'active'`); this statement has no WHERE clause and indexes all rows.
  - C) A UNIQUE index requires the UNIQUE keyword; without it, duplicate combinations of (customer_id, status) are permitted.
  - D) A composite index is a single index structure on multiple columns in order; it is not the same as two separate single-column indexes and cannot be used to satisfy queries that filter only on the second column (status) without also filtering on the first.

---

### Question 18 (5 points)

A table stores customer contact records with a `phone_number` column defined as VARCHAR(20). The business now requires storing multiple phone numbers per customer. Which schema change best satisfies Third Normal Form (3NF)?

- A) Create a separate `customer_phones` table with a foreign key to `customers` and one row per phone number.
- B) Add additional columns `phone_number_2`, `phone_number_3`, and `phone_number_4` to the customers table.
- C) Change the `phone_number` column to a JSON type and store an array of phone numbers in one cell.
- D) Increase the VARCHAR length to 200 and store all phone numbers as a comma-separated string in one column.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Adding numbered columns violates First Normal Form by creating a repeating group structure; it also makes querying any phone number require searching multiple columns.
  - C) Storing an array in a JSON column violates 1NF (atomic values rule) and makes it difficult to index, query, or enforce constraints on individual phone numbers.
  - D) Storing comma-separated values in one column violates 1NF atomicity; the column no longer stores a single indivisible value, making filtering and indexing by phone number unreliable.

---

### Question 19 (5 points)

Which Cloud SQL maintenance window configuration minimizes disruption to a production application that runs 24/7?

- A) Schedule maintenance during the lowest-traffic window of the week and enable high availability to allow failover during the maintenance event.
- B) Disable all maintenance windows so the instance is never restarted automatically.
- C) Enable automatic storage increases and set the maintenance window to any time since storage events are non-disruptive.
- D) Use a read replica as the primary application endpoint to avoid any downtime during maintenance.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Disabling maintenance windows does not permanently prevent updates; Google Cloud may still apply critical security patches and the instance cannot defer updates indefinitely; it also prevents the DBA from controlling the timing.
  - C) Automatic storage increases are non-disruptive, but maintenance windows govern instance restarts for software updates, not storage events; setting the window to "any time" means restarts may occur at peak traffic.
  - D) A read replica handles read queries but cannot accept write traffic; using it as the primary endpoint for a write-capable application is not a valid HA configuration and does not prevent maintenance restarts on the primary.

---

### Question 20 (5 points)

A DBA needs to provide a development team with access to query specific columns of the `employees` table without exposing the `salary` and `ssn` columns. Which approach best accomplishes this in PostgreSQL?

- A) Create a view that selects only the non-sensitive columns and grant SELECT on the view to the developer role.
- B) Grant SELECT on the `employees` table and rely on the application to filter out sensitive columns in the SELECT list.
- C) Use row-level security (RLS) policies on the `employees` table to restrict access by row, not by column.
- D) Export the non-sensitive columns to a separate table and grant access to that table.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Granting SELECT on the full table gives developers the ability to run `SELECT * FROM employees` and see all columns including salary and ssn; relying on application-level filtering is not a security control.
  - C) Row-level security restricts which rows a role can see, not which columns; it does not prevent a developer from seeing salary or ssn in the rows they can access.
  - D) Exporting to a separate table duplicates data, creates synchronization overhead, and is not a standard access control pattern; views are the correct mechanism for column-level access restriction.

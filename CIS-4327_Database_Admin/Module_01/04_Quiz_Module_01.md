# Quiz: Module 01 - Relational Database Fundamentals and SQL Review
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
Your company is developing a multiplayer mobile game that requires user profiles to be stored as JSON documents. The app needs to support offline synchronization for mobile clients. Which Google Cloud database service is the most appropriate choice?
A) Cloud SQL
B) Cloud Spanner
C) Cloud Bigtable
D) Firestore
*   **Correct Answer:** D) Firestore
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud SQL is a relational SQL database, not designed for native JSON document storage or mobile offline sync.
    *   *Why B is incorrect:* Cloud Spanner is a global relational database, overkill and the wrong paradigm for simple mobile document syncing.
    *   *Why C is incorrect:* Bigtable is for massive analytical workloads and time-series data, not for mobile app backends with offline sync.

---

---

**Question 2**
You are migrating an on-premises PostgreSQL database to Google Cloud. The application serves users in a single geographic region and requires strong ACID consistency. Which service minimizes migration effort while meeting requirements?
A) Cloud SQL for PostgreSQL
B) Cloud Spanner
C) BigQuery
D) Firestore
*   **Correct Answer:** A) Cloud SQL for PostgreSQL
*   **Distractor Analysis:**
    *   *Why B is incorrect:* While Spanner supports a PostgreSQL-compatible dialect, migrating to it requires significant architectural changes. Cloud SQL for PostgreSQL accepts a near-direct lift-and-shift for a regional workload.
    *   *Why C is incorrect:* BigQuery is an enterprise data warehouse optimized for analytics (OLAP), not transactional (OLTP) workloads — it has no concept of row-level ACID commits.
    *   *Why D is incorrect:* Firestore is a NoSQL document database; it is structurally incompatible with a relational PostgreSQL schema and would require a full application rewrite.

---

---

**Question 3**
A database administrator needs to **assign read-only access privileges on the database to a specific security role**. Which of the following SQL commands is the most appropriate to execute?
A) GRANT SELECT ON client_db TO analyst_role;
B) CREATE INDEX idx_email ON users(email);
C) EXPLAIN ANALYZE SELECT * FROM logs;
D) ALTER TABLE users ADD COLUMN last_login TIMESTAMP;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    *   *Why A is correct:* The `GRANT SELECT` statement is the standard SQL Data Control Language (DCL) command to assign read-only query privileges on a database object to a role.
    *   *Why B is incorrect:* `CREATE INDEX` is a Data Definition Language (DDL) command that creates a performance optimization structure; it has no effect on user permissions.
    *   *Why C is incorrect:* `EXPLAIN ANALYZE` is a query-plan diagnostic tool used for performance troubleshooting, not access control.
    *   *Why D is incorrect:* `ALTER TABLE` modifies the schema structure of a table; it does not grant or revoke any privileges.

---

**Question 4**
While administering a Cloud SQL for MySQL instance, you receive an alert that a **database deadlock** has occurred. Which of the following is the most effective action to resolve and prevent this issue?
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
B) Increase the database connection pool limit and scale the instance to more CPUs.
C) Reboot the Cloud SQL instance from the Google Cloud Console.
D) Analyze the query plan and add indexes on columns used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    *   *Why A is correct:* A deadlock occurs when two or more transactions are waiting on each other to release locks. The root fix is to reduce lock contention — by accessing tables in a consistent order, keeping transactions short, and adding retry logic so the application recovers gracefully when a deadlock is automatically detected and aborted.
    *   *Why B is incorrect:* Adding connections or CPUs does not address lock ordering; it can actually increase the frequency of deadlocks under high concurrency.
    *   *Why C is incorrect:* Rebooting the instance clears active connections temporarily but does not fix the application logic that caused the deadlock and will recur immediately.
    *   *Why D is incorrect:* Index tuning addresses slow queries and full table scans, not lock ordering conflicts between concurrent transactions.

---

**Question 5**
When securing a Cloud SQL instance, you must mitigate the risk of **attackers injecting malicious SQL strings that bypass authentication and leak database contents**. Which control best addresses this vulnerability?
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
B) Enable Customer-Managed Encryption Keys (CMEK) for storage encryption at rest.
C) Configure Cloud SQL to use Private IP only and disable public IP access.
D) Enable Cloud SQL Auth Proxy to encrypt all in-transit connections.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    *   *Why A is correct:* SQL injection exploits unsanitized user input concatenated into query strings. Parameterized queries pass user data as bound parameters rather than executable SQL, making injection structurally impossible regardless of the input content.
    *   *Why B is incorrect:* CMEK protects data at rest on the physical disk; it has no effect on how query strings are constructed in application code and does not prevent injection attacks.
    *   *Why C is incorrect:* Private IP restricts network-level access, which reduces attack surface, but does not prevent SQL injection from a legitimate internal application that concatenates unvalidated input.
    *   *Why D is incorrect:* Cloud SQL Auth Proxy secures the connection channel (in-transit encryption and IAM authentication), but an injected query travels through an encrypted channel just as easily as a legitimate one.

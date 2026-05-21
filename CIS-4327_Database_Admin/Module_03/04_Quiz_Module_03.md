# Quiz: Module 03 - Cloud SQL – MySQL and PostgreSQL on GCP
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
Your organization wishes to migrate a legacy on-premises Oracle database to Google Cloud SQL for PostgreSQL to reduce licensing costs. What type of migration is this, and what mandatory step must occur before data replication begins?
A) Homogeneous migration; you must export a `.bak` file.
B) Heterogeneous migration; you must convert the database schema and stored procedures.
C) Continuous migration; you must enable High Availability on the source database.
D) Lift-and-shift migration; you must configure an IPsec VPN.
*   **Correct Answer:** B) Heterogeneous migration; you must convert the database schema and stored procedures.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Moving from Oracle to PostgreSQL involves different database engines, making it heterogeneous, not homogeneous. A `.bak` file is a SQL Server backup format, not applicable here.
    *   *Why C is incorrect:* While it will likely be a continuous migration, enabling HA on the source is not a mandatory prerequisite for starting migration.
    *   *Why D is incorrect:* "Lift-and-shift" implies moving an application without changing its underlying architecture. Changing database engines from Oracle to PostgreSQL changes the architecture, making schema conversion mandatory.

---

---

**Question 2**
You are using Google Cloud Database Migration Service (DMS) to perform a continuous migration from an on-premises MySQL database to Cloud SQL. The initial data load has finished, and Change Data Capture (CDC) is currently replicating live changes. What is the final step you must take to finalize the migration and make the Cloud SQL instance primary?
A) Delete the source database.
B) Stop the DMS job manually.
C) Promote the destination instance.
D) Change the DNS records to point to the DMS endpoint.
*   **Correct Answer:** C) Promote the destination instance.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Deleting the source database before cutover will cause total data loss for any in-flight transactions that have not yet been replicated.
    *   *Why B is incorrect:* Stopping the job manually severs the replication link and leaves the destination in a read-only state without completing the transition to primary.
    *   *Why D is incorrect:* You update your application connection string to point to the new Cloud SQL instance, not to the DMS tool's endpoint. Promoting the instance handles making it writable.

---

---

**Question 3**
A Cloud SQL administrator needs to **grant read-only query access to a database for a new reporting analyst**. Which of the following SQL commands is the most appropriate to execute?
A) GRANT SELECT ON ALL TABLES IN SCHEMA public TO reporting_analyst;
B) CREATE INDEX idx_report ON orders(created_at);
C) EXPLAIN ANALYZE SELECT * FROM transactions WHERE status = 'pending';
D) ALTER USER reporting_analyst WITH PASSWORD 'newpass';
*   **Correct Answer:** A) GRANT SELECT ON ALL TABLES IN SCHEMA public TO reporting_analyst;
*   **Distractor Analysis:**
    *   *Why A is correct:* `GRANT SELECT` is the SQL Data Control Language (DCL) command for assigning read-only access to database objects for a named user or role.
    *   *Why B is incorrect:* `CREATE INDEX` is a performance optimization command that creates a B-tree index structure; it does not affect user permissions.
    *   *Why C is incorrect:* `EXPLAIN ANALYZE` executes a query and displays its execution plan for performance diagnostics; it does not grant or manage access.
    *   *Why D is incorrect:* `ALTER USER ... WITH PASSWORD` changes a user's authentication credential, not their database object privileges.

---

**Question 4**
A Cloud SQL for PostgreSQL instance is experiencing **slow query performance**. An application developer reports that a query filtering on `customer_email` in a 50-million-row table is taking 8 seconds. Which is the most effective first action to diagnose and resolve this issue?
A) Use `EXPLAIN ANALYZE` to read the query execution plan, then create a B-tree index on `customer_email` if a sequential scan is confirmed.
B) Increase the Cloud SQL instance's machine type to add more vCPUs and RAM.
C) Reboot the Cloud SQL instance to clear the buffer pool and reset connection state.
D) Enable read replicas to distribute the query load across multiple instances.
*   **Correct Answer:** A) Use `EXPLAIN ANALYZE` to read the query execution plan, then create a B-tree index on `customer_email` if a sequential scan is confirmed.
*   **Distractor Analysis:**
    *   *Why A is correct:* The most common cause of a slow filter query on a large table is a missing index causing a full sequential scan. `EXPLAIN ANALYZE` reveals whether a Seq Scan or Index Scan is being used. If a Seq Scan is confirmed, creating an index on the filtered column resolves the root cause with minimal cost.
    *   *Why B is incorrect:* Scaling up the machine adds resources but does not fix the underlying algorithmic problem. A full table scan on 50 million rows will still be slow on a larger machine, just slightly faster.
    *   *Why C is incorrect:* Rebooting clears cached query plans and connections but does not fix the structural cause of slow queries and causes unnecessary downtime.
    *   *Why D is incorrect:* Read replicas distribute read traffic but they replicate the same schema, so the same sequential scan problem will occur on every replica.

---

**Question 5**
When securing a Cloud SQL instance, you must mitigate the risk of **attackers injecting malicious SQL strings that bypass authentication and expose database contents**. Which control best addresses this vulnerability?
A) Enforce parameterized queries and prepared statements in all application code, rejecting direct string concatenation of user inputs.
B) Enable Customer-Managed Encryption Keys (CMEK) for all Cloud SQL storage and backups.
C) Configure the Cloud SQL instance to use Private IP only and disable the public IP address.
D) Rotate the database root password on a monthly schedule using Secret Manager.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements in all application code, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    *   *Why A is correct:* SQL injection exploits application code that builds SQL queries by concatenating unvalidated user input. Parameterized queries pass user data as type-safe bound parameters that the database engine never interprets as SQL syntax, making injection structurally impossible.
    *   *Why B is incorrect:* CMEK encrypts data at rest on disk; it does not affect how the application constructs query strings and offers no protection against injection attacks.
    *   *Why C is incorrect:* Private IP removes external network exposure but does not prevent an internal or compromised application from sending an injected query through a valid connection.
    *   *Why D is incorrect:* Password rotation reduces the risk of credential compromise but does not prevent SQL injection, which exploits the query construction layer, not the authentication layer.

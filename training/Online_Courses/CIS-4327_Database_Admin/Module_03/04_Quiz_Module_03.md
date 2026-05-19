# Quiz: Module 03 - Migration
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

**Question 1**
Your organization wishes to migrate a legacy on-premises Oracle database to Google Cloud SQL for PostgreSQL to reduce licensing costs. What type of migration is this, and what mandatory step must occur before data replication begins?
A) Homogeneous migration; you must export a `.bak` file.
B) Heterogeneous migration; you must convert the database schema and stored procedures.
C) Continuous migration; you must enable High Availability on the source database.
D) Lift-and-shift migration; you must configure an IPsec VPN.
*   **Correct Answer:** B) Heterogeneous migration; you must convert the database schema and stored procedures.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Moving from Oracle to PostgreSQL involves different database engines, making it heterogeneous, not homogeneous.
    *   *Why C is incorrect:* While it will likely be a continuous migration, enabling HA on the source is not a mandatory prerequisite for migration.
    *   *Why D is incorrect:* "Lift-and-shift" implies moving an application without changing its underlying architecture (e.g., migrating an Oracle DB on a physical server to an Oracle DB on a Compute Engine VM). Changing to PostgreSQL changes the architecture.

---

**Question 2**
You are using Google Cloud Database Migration Service (DMS) to perform a continuous migration from an on-premises MySQL database to Cloud SQL. The initial data load has finished, and Change Data Capture (CDC) is currently replicating live changes. What is the final step you must take to finalize the migration and make the Cloud SQL instance primary?
A) Delete the source database.
B) Stop the DMS job manually.
C) Promote the destination instance.
D) Change the DNS records to point to the DMS endpoint.
*   **Correct Answer:** C) Promote the destination instance.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Deleting the source database before cutover will cause total data loss for any in-flight transactions.
    *   *Why B is incorrect:* Stopping the job manually will sever the replication link, leaving the destination database in a read-only or incomplete state.
    *   *Why D is incorrect:* You point your application to the new Cloud SQL instance's IP address, not the DMS tool's endpoint. Promoting the instance automatically handles severing the replication and making it writable.

---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
A) GRANT SELECT ON client_db TO analyst_role;
B) CREATE INDEX idx_email ON users(email);
D) EXPLAIN ANALYZE SELECT * FROM logs;
C) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Migration** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
D) Reboot the physical machine and wait for services to reload.
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..


---

**Question 5**
When designing a system for **Migration**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
C) Enable full disk encryption on all client endpoints.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


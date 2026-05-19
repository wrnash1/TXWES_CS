# Quiz: Module 04 - Security
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

**Question 1**
Your organization has strict compliance requirements that dictate all database backups and persistent disks must be encrypted using keys that your organization exclusively generates, manages, and rotates. Which Google Cloud feature must you implement to satisfy this requirement for Cloud SQL?
A) Google-managed encryption keys
B) Customer-Managed Encryption Keys (CMEK) using Cloud KMS
C) Transparent Data Encryption (TDE)
D) IPsec VPN tunnels
*   **Correct Answer:** B) Customer-Managed Encryption Keys (CMEK) using Cloud KMS
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Google-managed keys are the default, but they do not satisfy compliance requirements demanding that the *customer* generate and manage the key material.
    *   *Why C is incorrect:* TDE is a specific Microsoft SQL Server feature, not the Google Cloud native method for managing disk-level encryption keys across GCP services.
    *   *Why D is incorrect:* IPsec VPN encrypts data in *transit* across a network, not data at *rest* on persistent disks or backups.

---

**Question 2**
A developer complains that their application is running slowly. You suspect the database is the bottleneck, but the overall CPU utilization of the Cloud SQL instance is only at 40%. You need to identify if a specific, poorly optimized SQL `SELECT` statement is taking too long to execute. Which Google Cloud tool provides this specific visibility?
A) Cloud Audit Logs
B) Cloud SQL Proxy
C) Query Insights
D) Identity and Access Management (IAM)
*   **Correct Answer:** C) Query Insights
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Audit Logs track *who* performed an action (Data Access logs can show the query was run), but they do not provide performance metrics, execution plans, or database load analysis.
    *   *Why B is incorrect:* Cloud SQL Proxy is a tool used to establish a secure connection to the database, not a monitoring or performance tuning tool.
    *   *Why D is incorrect:* IAM manages access control and permissions, entirely unrelated to database query performance.

---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
B) EXPLAIN ANALYZE SELECT * FROM logs;
D) CREATE INDEX idx_email ON users(email);
C) GRANT SELECT ON client_db TO analyst_role;
A) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.


---

**Question 4**
While working on **Security** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.


---

**Question 5**
When designing a system for **Security**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


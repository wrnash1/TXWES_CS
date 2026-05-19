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

---

**Question 3**
A systems administrator or developer needs to **analyze the database execution plan to identify performance bottlenecks and slow scan steps**. Which of the following commands is the most appropriate to execute?
A) EXPLAIN ANALYZE SELECT * FROM logs;
B) CREATE INDEX idx_email ON users(email);
D) SELECT * FROM users WHERE active = 1;
C) GRANT SELECT ON client_db TO analyst_role;
*   **Correct Answer:** A) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Distractor Analysis:**
    * *Why A is correct:* The `EXPLAIN ANALYZE SELECT * FROM logs;` command is directly designed to analyze the database execution plan to identify performance bottlenecks and slow scan steps.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Security** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
D) Reboot the physical machine and wait for services to reload.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Security**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


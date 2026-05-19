# Quiz: Module 13 - Data Governance & Privacy
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Which of the following is classified as Personally Identifiable Information (PII)?
*   A) Server uptime stats
*   B) Aggregate store sales totals
*   C) Email address and Social Security Number
*   D) Operating system version
*   **Correct Answer:** C) PII is any information that can identify a specific individual.
*   **Distractor Analysis:**
    *   *Why correct:* PII is any information that can identify a specific individual.
    *   Uptime, sales totals, and OS versions do not identify individuals.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **data masking**?
D) The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.
B) The difference in height between the left and right subtrees of a node in an AVL tree, which must be -1, 0, or 1 to remain balanced.
C) Electrostatic Discharge protection; tools (like wrist straps, grounding mats) used to prevent static electricity from destroying sensitive microchips when handling hardware.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **data masking**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **data masking**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **data masking**.
    * *Why A is correct:* This describes the exact role and function of **data masking**.


---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
A) SELECT * FROM users WHERE active = 1;
D) EXPLAIN ANALYZE SELECT * FROM logs;
B) CREATE INDEX idx_email ON users(email);
C) GRANT SELECT ON client_db TO analyst_role;
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Governance & Privacy** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
D) Reboot the physical machine and wait for services to reload.
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.


---

**Question 5**
When designing a system for **Data Governance & Privacy**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


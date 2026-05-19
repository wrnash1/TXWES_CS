# Quiz: Module 10 - Customizing ERP Systems
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
Which programming language is proprietary to SAP and used to develop custom reports and database integrations?
*   A) Python
*   B) ABAP
*   C) Apex
*   D) SQL Server
*   **Correct Answer:** B) ABAP (Advanced Business Application Programming) is SAP's primary custom programming language.
*   **Distractor Analysis:**
    *   *Why correct:* ABAP (Advanced Business Application Programming) is SAP's primary custom programming language.
    *   Apex is used for customizing Salesforce cloud platforms.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **proprietary scripting (Salesforce Apex**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
C) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
B) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
D) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **proprietary scripting (Salesforce Apex**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **proprietary scripting (Salesforce Apex**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **proprietary scripting (Salesforce Apex**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **proprietary scripting (Salesforce Apex**.


---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
B) EXPLAIN ANALYZE SELECT * FROM logs;
D) GRANT SELECT ON client_db TO analyst_role;
A) SELECT * FROM users WHERE active = 1;
C) CREATE INDEX idx_email ON users(email);
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Customizing ERP Systems** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
D) Reboot the physical machine and wait for services to reload.
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.


---

**Question 5**
When designing a system for **Customizing ERP Systems**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
D) Enable full disk encryption on all client endpoints.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..


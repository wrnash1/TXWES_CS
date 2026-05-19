# Quiz: Module 02 - Database Structures & Schemas
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
In database design, which key uniquely identifies each row within its own table?
*   A) Foreign Key
*   B) Primary Key
*   C) Candidate Key
*   D) Composite Key
*   **Correct Answer:** B) A Primary Key enforces entity integrity by uniquely identifying table rows.
*   **Distractor Analysis:**
    *   *Why correct:* A Primary Key enforces entity integrity by uniquely identifying table rows.
    *   Foreign keys link rows in separate tables.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **primary keys**?
B) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
C) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
D) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **primary keys**.
    * *Why A is correct:* This describes the exact role and function of **primary keys**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **primary keys**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **primary keys**.


---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
A) GRANT SELECT ON client_db TO analyst_role;
B) EXPLAIN ANALYZE SELECT * FROM logs;
D) CREATE INDEX idx_email ON users(email);
C) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Database Structures & Schemas** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..


---

**Question 5**
When designing a system for **Database Structures & Schemas**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
C) Enable full disk encryption on all client endpoints.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..


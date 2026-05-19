# Quiz: Module 15 - Review
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Core Concept**?
D) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
C) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why A is correct:* This describes the exact role and function of **Core Concept**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Core Concept**?
B) The descendant node connected to the left branch of a parent node in a binary tree structure.
D) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
C) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why A is correct:* This describes the exact role and function of **Core Concept**.


---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
D) SELECT * FROM users WHERE active = 1;
B) EXPLAIN ANALYZE SELECT * FROM logs;
A) GRANT SELECT ON client_db TO analyst_role;
C) CREATE INDEX idx_email ON users(email);
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Review** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..


---

**Question 5**
When designing a system for **Review**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
D) Enable full disk encryption on all client endpoints.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


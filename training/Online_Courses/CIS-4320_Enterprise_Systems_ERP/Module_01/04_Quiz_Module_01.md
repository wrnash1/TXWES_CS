# Quiz: Module 01 - Enterprise Systems Concepts
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
What is the primary business value of implementing an Enterprise Resource Planning (ERP) system?
*   A) It lets developers write custom Python games
*   B) It integrates business data from disparate departments (finance, sales, inventory) into a single database system
*   C) It removes the need for web servers
*   D) It speeds up local CPU clock cycles
*   **Correct Answer:** B) ERP breaks down departmental silos by providing a single source of truth for business transaction data.
*   **Distractor Analysis:**
    *   *Why correct:* ERP breaks down departmental silos by providing a single source of truth for business transaction data.
    *   ERP target integration of business logistics, not programming compilers.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **integrated data**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
D) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
C) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **integrated data**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **integrated data**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **integrated data**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **integrated data**.


---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
A) SELECT * FROM users WHERE active = 1;
B) GRANT SELECT ON client_db TO analyst_role;
C) EXPLAIN ANALYZE SELECT * FROM logs;
D) CREATE INDEX idx_email ON users(email);
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Enterprise Systems Concepts** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Enterprise Systems Concepts**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


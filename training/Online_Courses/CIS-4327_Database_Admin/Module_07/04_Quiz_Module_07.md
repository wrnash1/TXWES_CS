# Quiz: Module 07 - Terraform
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **State Files**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
C) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
D) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **State Files**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **State Files**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **State Files**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **State Files**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **State Files**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) A two-dimensional CSS layout system that allows developers to design complex grid-based user interfaces with rows and columns, offering precise control over alignment.
D) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
C) A column or group of columns in one database table that refers to the primary key in another table, enforcing referential integrity.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **State Files**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **State Files**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **State Files**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **State Files**.


---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
B) CREATE INDEX idx_email ON users(email);
A) GRANT SELECT ON client_db TO analyst_role;
C) SELECT * FROM users WHERE active = 1;
D) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Terraform** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
D) Reboot the physical machine and wait for services to reload.
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Terraform**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


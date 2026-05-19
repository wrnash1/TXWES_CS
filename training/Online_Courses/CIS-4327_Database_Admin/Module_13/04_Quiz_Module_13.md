# Quiz: Module 13 - Memorystore
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Core Concept**?
D) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
C) The database design process of organizing tables to minimize data redundancy and dependency, dividing large tables into smaller ones.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) The core CSS layout block consisting of margins, borders, padding, and the actual content area, defining the sizing and spacing of every page element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why A is correct:* This describes the exact role and function of **Core Concept**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Core Concept**?
C) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
D) CSS rules (like width, height, max-width, box-sizing) that dictate how the dimensions of elements are calculated and rendered.
B) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why A is correct:* This describes the exact role and function of **Core Concept**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Core Concept**.


---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
A) GRANT SELECT ON client_db TO analyst_role;
D) CREATE INDEX idx_email ON users(email);
C) SELECT * FROM users WHERE active = 1;
B) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Memorystore** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
D) Reboot the physical machine and wait for services to reload.
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Memorystore**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
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


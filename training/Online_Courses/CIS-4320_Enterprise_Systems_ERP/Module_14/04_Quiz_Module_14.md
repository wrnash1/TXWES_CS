# Quiz: Module 14 - Cloud ERP hosting
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
What is a characteristic of a multi-tenant cloud database design?
*   A) Each customer has their own physical server
*   B) Multiple customers share the same database application instance and physical infrastructure, isolated logically
*   C) It is unencrypted
*   D) It does not support SQL
*   **Correct Answer:** B) Multi-tenancy allows cloud providers to scale resources by sharing physical infrastructure among customers while preserving strict security boundaries.
*   **Distractor Analysis:**
    *   *Why correct:* Multi-tenancy allows cloud providers to scale resources by sharing physical infrastructure among customers while preserving strict security boundaries.
    *   Dedicated servers represent single-tenant infrastructure.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **multi-tenant databases**?
B) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
D) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
C) The descendant node connected to the left branch of a parent node in a binary tree structure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **multi-tenant databases**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **multi-tenant databases**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **multi-tenant databases**.
    * *Why A is correct:* This describes the exact role and function of **multi-tenant databases**.


---

**Question 3**
A systems administrator or developer needs to **create a search index on the email column to speed up lookup queries significantly**. Which of the following commands is the most appropriate to execute?
D) SELECT * FROM users WHERE active = 1;
C) GRANT SELECT ON client_db TO analyst_role;
B) EXPLAIN ANALYZE SELECT * FROM logs;
A) CREATE INDEX idx_email ON users(email);
*   **Correct Answer:** A) CREATE INDEX idx_email ON users(email);
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `CREATE INDEX idx_email ON users(email);` command is directly designed to create a search index on the email column to speed up lookup queries significantly.


---

**Question 4**
While working on **Cloud ERP hosting** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.


---

**Question 5**
When designing a system for **Cloud ERP hosting**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


# Quiz: Module 13 - ERP Security & Roles
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
Which security concept is violated if a single ERP user is authorized to both approve purchase orders and issue vendor payments?
*   A) Least Privilege
*   B) Separation of Duties (SoD)
*   C) High Availability
*   D) Single Sign-On
*   **Correct Answer:** B) SoD prevents fraud by dividing critical transactional tasks (e.g. creating invoices vs paying them) between different users.
*   **Distractor Analysis:**
    *   *Why correct:* SoD prevents fraud by dividing critical transactional tasks (e.g. creating invoices vs paying them) between different users.
    *   Least Privilege restricts access to baseline requirements but doesn't specifically target fraud-prevention workflow splits.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Role-Based Access Control (RBAC)**?
C) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
D) A reference or memory address stored within a node that points to another node in a linked structure, forming the link between elements.
B) The difference in height between the left and right subtrees of a node in an AVL tree, which must be -1, 0, or 1 to remain balanced.
A) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
*   **Correct Answer:** A) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Role-Based Access Control (RBAC)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Role-Based Access Control (RBAC)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Role-Based Access Control (RBAC)**.
    * *Why A is correct:* This describes the exact role and function of **Role-Based Access Control (RBAC)**.


---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
A) GRANT SELECT ON client_db TO analyst_role;
C) EXPLAIN ANALYZE SELECT * FROM logs;
D) CREATE INDEX idx_email ON users(email);
B) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **ERP Security & Roles** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.


---

**Question 5**
When designing a system for **ERP Security & Roles**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
D) Enable full disk encryption on all client endpoints.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


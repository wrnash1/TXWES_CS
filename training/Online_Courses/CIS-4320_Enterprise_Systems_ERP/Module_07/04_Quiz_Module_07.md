# Quiz: Module 07 - Customer Relationship Management Modules
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
Which business entity is the primary focus of a Customer Relationship Management (CRM) module?
*   A) Raw material vendors
*   B) Warehouse locations
*   C) Customers and sales leads
*   D) Corporate employee records
*   **Correct Answer:** C) CRM systems track customer details, sales interactions, pipelines, and helpdesk tickets to improve business relationships.
*   **Distractor Analysis:**
    *   *Why correct:* CRM systems track customer details, sales interactions, pipelines, and helpdesk tickets to improve business relationships.
    *   HCM tracks employees. ERP warehouse modules track locations.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **account management**?
B) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
C) A column or group of columns in one database table that refers to the primary key in another table, enforcing referential integrity.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
D) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **account management**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **account management**.
    * *Why A is correct:* This describes the exact role and function of **account management**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **account management**.


---

**Question 3**
A systems administrator or developer needs to **analyze the database execution plan to identify performance bottlenecks and slow scan steps**. Which of the following commands is the most appropriate to execute?
B) CREATE INDEX idx_email ON users(email);
D) SELECT * FROM users WHERE active = 1;
A) EXPLAIN ANALYZE SELECT * FROM logs;
C) GRANT SELECT ON client_db TO analyst_role;
*   **Correct Answer:** A) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `EXPLAIN ANALYZE SELECT * FROM logs;` command is directly designed to analyze the database execution plan to identify performance bottlenecks and slow scan steps.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Customer Relationship Management Modules** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.


---

**Question 5**
When designing a system for **Customer Relationship Management Modules**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
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


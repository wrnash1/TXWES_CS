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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Software as a Service (SaaS)**?
D) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
C) The database design process of organizing tables to minimize data redundancy and dependency, dividing large tables into smaller ones.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Software as a Service (SaaS)**.
    * *Why A is correct:* This describes the exact role and function of **Software as a Service (SaaS)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Software as a Service (SaaS)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Software as a Service (SaaS)**.


---

**Question 3**
A systems administrator or developer needs to **analyze the database execution plan to identify performance bottlenecks and slow scan steps**. Which of the following commands is the most appropriate to execute?
A) EXPLAIN ANALYZE SELECT * FROM logs;
B) SELECT * FROM users WHERE active = 1;
D) GRANT SELECT ON client_db TO analyst_role;
C) CREATE INDEX idx_email ON users(email);
*   **Correct Answer:** A) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Distractor Analysis:**
    * *Why A is correct:* The `EXPLAIN ANALYZE SELECT * FROM logs;` command is directly designed to analyze the database execution plan to identify performance bottlenecks and slow scan steps.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Cloud ERP hosting** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Cloud ERP hosting**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..


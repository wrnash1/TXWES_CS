# Quiz: Module 15 - ERP Post-Implementation
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
Why is post-implementation auditing critical for ERP deployments?
*   A) To write code comments
*   B) To evaluate if the system met the business objectives defined in the charter and address operational bugs
*   C) To configure DNS records
*   D) To clear hard drive logs
*   **Correct Answer:** B) Audits check if the system actually realized projected ROI, resolved bottlenecks, and is being utilized correctly by staff.
*   **Distractor Analysis:**
    *   *Why correct:* Audits check if the system actually realized projected ROI, resolved bottlenecks, and is being utilized correctly by staff.
    *   It focuses on business value evaluation.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **upgrading modules.**?
D) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
C) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
B) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **upgrading modules.**.
    * *Why A is correct:* This describes the exact role and function of **upgrading modules.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **upgrading modules.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **upgrading modules.**.


---

**Question 3**
A systems administrator or developer needs to **create a search index on the email column to speed up lookup queries significantly**. Which of the following commands is the most appropriate to execute?
D) SELECT * FROM users WHERE active = 1;
A) CREATE INDEX idx_email ON users(email);
C) GRANT SELECT ON client_db TO analyst_role;
B) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Correct Answer:** A) CREATE INDEX idx_email ON users(email);
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `CREATE INDEX idx_email ON users(email);` command is directly designed to create a search index on the email column to speed up lookup queries significantly.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **ERP Post-Implementation** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **ERP Post-Implementation**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
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


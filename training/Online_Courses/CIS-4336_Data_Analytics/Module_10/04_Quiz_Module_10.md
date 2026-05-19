# Quiz: Module 10 - Creating Dashboards & Reports
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Why should dashboards have interactive filters?
*   A) To speed up database processing
*   B) To allow users to drill down and customize the data shown
*   C) To secure the server
*   D) To compile code
*   **Correct Answer:** B) Interactive filters let business users segment data (e.g. by region or date) without requiring new custom reports.
*   **Distractor Analysis:**
    *   *Why correct:* Interactive filters let business users segment data (e.g. by region or date) without requiring new custom reports.
    *   Filters do not speed up backend database configurations.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **report distribution.**?
D) The standard configuration parameters pre-loaded into a software application or system before any custom adjustments are made by an administrator.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
C) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **report distribution.**.
    * *Why A is correct:* This describes the exact role and function of **report distribution.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **report distribution.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **report distribution.**.


---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
A) GRANT SELECT ON client_db TO analyst_role;
B) SELECT * FROM users WHERE active = 1;
D) CREATE INDEX idx_email ON users(email);
C) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Creating Dashboards & Reports** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
D) Reboot the physical machine and wait for services to reload.
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..


---

**Question 5**
When designing a system for **Creating Dashboards & Reports**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


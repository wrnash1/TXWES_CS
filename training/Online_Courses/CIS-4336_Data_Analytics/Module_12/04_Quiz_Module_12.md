# Quiz: Module 12 - Data Analysis Methods
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Which analysis method groups users based on a shared characteristic or start date to track behavior over time?
*   A) Churn Analysis
*   B) Cohort Analysis
*   C) Outlier Analysis
*   D) Regression Analysis
*   **Correct Answer:** B) Cohort analysis tracks defined groups over time to identify usage or drop-off trends.
*   **Distractor Analysis:**
    *   *Why correct:* Cohort analysis tracks defined groups over time to identify usage or drop-off trends.
    *   Churn only tracks cancellations.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **trend analysis**?
D) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
C) The maximum acceptable duration of downtime before a business process or system must be restored to operation after a disaster.
B) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **trend analysis**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **trend analysis**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **trend analysis**.
    * *Why A is correct:* This describes the exact role and function of **trend analysis**.


---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
A) SELECT * FROM users WHERE active = 1;
C) EXPLAIN ANALYZE SELECT * FROM logs;
B) CREATE INDEX idx_email ON users(email);
D) GRANT SELECT ON client_db TO analyst_role;
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Analysis Methods** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.


---

**Question 5**
When designing a system for **Data Analysis Methods**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


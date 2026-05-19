# Quiz: Module 09 - ERP Database Structures
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
Why do ERP databases utilize strict indexing and normalization layouts?
*   A) To prevent users from writing queries
*   B) To ensure high transactional integrity (ACID) and prevent data duplication across large volumes
*   C) To run faster than standard HTML
*   D) To bypass operating system checks
*   **Correct Answer:** B) ERP databases handle millions of records daily; normalization prevents update anomalies, and indexes speed up searches.
*   **Distractor Analysis:**
    *   *Why correct:* ERP databases handle millions of records daily; normalization prevents update anomalies, and indexes speed up searches.
    *   HTML does not run databases, and OS checks are not related to normalization.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **high transaction volume**?
B) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
C) The method of evaluating an algorithm's efficiency by analyzing its behavior as the input size approaches infinity, focusing on growth rates rather than specific hardware speeds.
D) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **high transaction volume**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **high transaction volume**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **high transaction volume**.
    * *Why A is correct:* This describes the exact role and function of **high transaction volume**.


---

**Question 3**
A systems administrator or developer needs to **create a search index on the email column to speed up lookup queries significantly**. Which of the following commands is the most appropriate to execute?
D) GRANT SELECT ON client_db TO analyst_role;
C) SELECT * FROM users WHERE active = 1;
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
While working on **ERP Database Structures** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.


---

**Question 5**
When designing a system for **ERP Database Structures**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


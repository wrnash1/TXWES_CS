# Quiz: Module 06 - Data Profiling and Verification
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Which data quality dimension measures whether all required data fields are populated in a record?
*   A) Accuracy
*   B) Completeness
*   C) Consistency
*   D) Validity
*   **Correct Answer:** B) Completeness confirms that all expected attributes are recorded, leaving no missing entries.
*   **Distractor Analysis:**
    *   *Why correct:* Completeness confirms that all expected attributes are recorded, leaving no missing entries.
    *   Accuracy checks for correctness. Validity checks for format alignment.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **validity**?
C) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
D) The core operations of a stack: 'push' inserts an element onto the top, and 'pop' removes and returns the top element.
B) A unique identifier column or set of columns in a database table that guarantees every row can be uniquely identified.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **validity**.
    * *Why A is correct:* This describes the exact role and function of **validity**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **validity**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **validity**.


---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
C) EXPLAIN ANALYZE SELECT * FROM logs;
B) CREATE INDEX idx_email ON users(email);
D) GRANT SELECT ON client_db TO analyst_role;
A) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.


---

**Question 4**
While working on **Data Profiling and Verification** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Data Profiling and Verification**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


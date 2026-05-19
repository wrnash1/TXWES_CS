# Quiz: Module 15 - Data Quality Controls
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
What is the purpose of running data quality checks during ingestion?
*   A) To encrypt datasets
*   B) To catch and isolate corrupt records before they pollute dashboards
*   C) To compress log files
*   D) None of the above
*   **Correct Answer:** B) Checks verify that incoming data conforms to validation rules, stopping malformed inputs before they disrupt metrics.
*   **Distractor Analysis:**
    *   *Why correct:* Checks verify that incoming data conforms to validation rules, stopping malformed inputs before they disrupt metrics.
    *   It is not for compression or encryption.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Establishing data quality baselines**?
D) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
B) The difference in height between the left and right subtrees of a node in an AVL tree, which must be -1, 0, or 1 to remain balanced.
C) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Establishing data quality baselines**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Establishing data quality baselines**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Establishing data quality baselines**.
    * *Why A is correct:* This describes the exact role and function of **Establishing data quality baselines**.


---

**Question 3**
A systems administrator or developer needs to **analyze the database execution plan to identify performance bottlenecks and slow scan steps**. Which of the following commands is the most appropriate to execute?
B) SELECT * FROM users WHERE active = 1;
A) EXPLAIN ANALYZE SELECT * FROM logs;
D) GRANT SELECT ON client_db TO analyst_role;
C) CREATE INDEX idx_email ON users(email);
*   **Correct Answer:** A) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `EXPLAIN ANALYZE SELECT * FROM logs;` command is directly designed to analyze the database execution plan to identify performance bottlenecks and slow scan steps.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Quality Controls** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
D) Reboot the physical machine and wait for services to reload.
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Data Quality Controls**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..


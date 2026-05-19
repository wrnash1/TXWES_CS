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
D) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
B) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
C) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Establishing data quality baselines**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Establishing data quality baselines**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Establishing data quality baselines**.
    * *Why A is correct:* This describes the exact role and function of **Establishing data quality baselines**.


---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
B) SELECT * FROM users WHERE active = 1;
C) CREATE INDEX idx_email ON users(email);
A) GRANT SELECT ON client_db TO analyst_role;
D) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Quality Controls** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
D) Reboot the physical machine and wait for services to reload.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Data Quality Controls**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
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


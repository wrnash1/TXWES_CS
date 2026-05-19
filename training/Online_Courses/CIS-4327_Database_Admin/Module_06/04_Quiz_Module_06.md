# Quiz: Module 06 - BigQuery
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Serverless**?
D) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
B) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
C) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Serverless**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Serverless**.
    * *Why A is correct:* This describes the exact role and function of **Serverless**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Serverless**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Serverless**?
C) A unique identifier column or set of columns in a database table that guarantees every row can be uniquely identified.
D) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
B) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Serverless**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Serverless**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Serverless**.
    * *Why A is correct:* This describes the exact role and function of **Serverless**.


---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
C) GRANT SELECT ON client_db TO analyst_role;
D) CREATE INDEX idx_email ON users(email);
B) EXPLAIN ANALYZE SELECT * FROM logs;
A) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.


---

**Question 4**
While working on **BigQuery** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.


---

**Question 5**
When designing a system for **BigQuery**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


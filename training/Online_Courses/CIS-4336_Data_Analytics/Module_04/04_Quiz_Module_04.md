# Quiz: Module 04 - Data Cleaning & Normalization
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
What is the primary goal of data normalization?
*   A) Compressing files to save space
*   B) Reducing data redundancy and improving data integrity
*   C) Creating visual charts
*   D) Encrypting data
*   **Correct Answer:** B) Normalization splits data into smaller tables to reduce redundant duplicates and avoid anomaly risks.
*   **Distractor Analysis:**
    *   *Why correct:* Normalization splits data into smaller tables to reduce redundant duplicates and avoid anomaly risks.
    *   It is not for compression or encryption.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **text cleaning (regex)**?
D) A data structure that improves the speed of data retrieval operations on a database table at the cost of additional write speed and storage.
C) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **text cleaning (regex)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **text cleaning (regex)**.
    * *Why A is correct:* This describes the exact role and function of **text cleaning (regex)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **text cleaning (regex)**.


---

**Question 3**
A systems administrator or developer needs to **analyze the database execution plan to identify performance bottlenecks and slow scan steps**. Which of the following commands is the most appropriate to execute?
D) SELECT * FROM users WHERE active = 1;
B) CREATE INDEX idx_email ON users(email);
A) EXPLAIN ANALYZE SELECT * FROM logs;
C) GRANT SELECT ON client_db TO analyst_role;
*   **Correct Answer:** A) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `EXPLAIN ANALYZE SELECT * FROM logs;` command is directly designed to analyze the database execution plan to identify performance bottlenecks and slow scan steps.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Cleaning & Normalization** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
D) Reboot the physical machine and wait for services to reload.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.


---

**Question 5**
When designing a system for **Data Cleaning & Normalization**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


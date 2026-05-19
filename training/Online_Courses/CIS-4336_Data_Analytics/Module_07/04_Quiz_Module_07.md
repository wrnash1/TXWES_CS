# Quiz: Module 07 - Basic Statistical Concepts
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Which statistical metric represents the middle value of a sorted list of numbers?
*   A) Mean
*   B) Median
*   C) Mode
*   D) Variance
*   **Correct Answer:** B) The median divides the sorted dataset in half, representing the exact middle value.
*   **Distractor Analysis:**
    *   *Why correct:* The median divides the sorted dataset in half, representing the exact middle value.
    *   Mean is the average. Mode is the most frequent.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **range.**?
D) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
C) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **range.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **range.**.
    * *Why A is correct:* This describes the exact role and function of **range.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **range.**.


---

**Question 3**
A systems administrator or developer needs to **create a search index on the email column to speed up lookup queries significantly**. Which of the following commands is the most appropriate to execute?
C) GRANT SELECT ON client_db TO analyst_role;
B) SELECT * FROM users WHERE active = 1;
D) EXPLAIN ANALYZE SELECT * FROM logs;
A) CREATE INDEX idx_email ON users(email);
*   **Correct Answer:** A) CREATE INDEX idx_email ON users(email);
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `CREATE INDEX idx_email ON users(email);` command is directly designed to create a search index on the email column to speed up lookup queries significantly.


---

**Question 4**
While working on **Basic Statistical Concepts** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..


---

**Question 5**
When designing a system for **Basic Statistical Concepts**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


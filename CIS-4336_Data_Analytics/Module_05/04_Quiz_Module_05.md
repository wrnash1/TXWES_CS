# Quiz: Module 05 - Handling Missing Data and Outliers
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Which method involves replacing missing dataset values with statistical estimates like mean or median?
*   A) Deletion
*   B) Imputation
*   C) Normalization
*   D) Deduplication
*   **Correct Answer:** B) Imputation calculates replacing values rather than omitting records entirely.
*   **Distractor Analysis:**
    *   *Why correct:* Imputation calculates replacing values rather than omitting records entirely.
    *   Deletion drops rows. Deduplication removes duplicates.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **deletion methods**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
C) A column or group of columns in one database table that refers to the primary key in another table, enforcing referential integrity.
B) A unique identifier column or set of columns in a database table that guarantees every row can be uniquely identified.
D) A mathematical representation used to describe the asymptotic upper bound of an algorithm's running time or space complexity relative to the input size N. It helps developers predict how an algorithm will scale as data grows.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **deletion methods**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **deletion methods**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **deletion methods**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **deletion methods**.


---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
D) EXPLAIN ANALYZE SELECT * FROM logs;
C) CREATE INDEX idx_email ON users(email);
B) GRANT SELECT ON client_db TO analyst_role;
A) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.


---

**Question 4**
While working on **Handling Missing Data and Outliers** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.


---

**Question 5**
When designing a system for **Handling Missing Data and Outliers**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


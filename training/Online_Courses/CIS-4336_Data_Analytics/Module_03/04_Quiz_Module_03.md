# Quiz: Module 03 - Data Acquisition and SQL
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Which SQL clause is used to filter group results after aggregation has occurred?
*   A) WHERE
*   B) HAVING
*   C) GROUP BY
*   D) SELECT
*   **Correct Answer:** B) `HAVING` filters aggregated values. `WHERE` filters individual rows before aggregation.
*   **Distractor Analysis:**
    *   *Why correct:* `HAVING` filters aggregated values. `WHERE` filters individual rows before aggregation.
    *   WHERE filters rows beforehand.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **SQL SELECT**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
C) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
B) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
D) The practice of connecting an electrical circuit or chassis to the earth or a large conductor to safely dissipate static electricity or stray currents.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **SQL SELECT**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **SQL SELECT**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **SQL SELECT**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **SQL SELECT**.


---

**Question 3**
A systems administrator or developer needs to **analyze the database execution plan to identify performance bottlenecks and slow scan steps**. Which of the following commands is the most appropriate to execute?
B) CREATE INDEX idx_email ON users(email);
C) GRANT SELECT ON client_db TO analyst_role;
A) EXPLAIN ANALYZE SELECT * FROM logs;
D) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `EXPLAIN ANALYZE SELECT * FROM logs;` command is directly designed to analyze the database execution plan to identify performance bottlenecks and slow scan steps.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Acquisition and SQL** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
D) Reboot the physical machine and wait for services to reload.
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..


---

**Question 5**
When designing a system for **Data Acquisition and SQL**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
D) Enable full disk encryption on all client endpoints.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


# Quiz: Module 01 - Fundamentals of Data Analytics
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
What type of data is a database table containing names, dates, and currency values classified as?
*   A) Unstructured data
*   B) Semi-structured data
*   C) Structured data
*   D) Qualitative data only
*   **Correct Answer:** C) Structured data is highly organized into rigid columns and tables (e.g. relational databases).
*   **Distractor Analysis:**
    *   *Why correct:* Structured data is highly organized into rigid columns and tables (e.g. relational databases).
    *   Unstructured data has no predefined schema (e.g. videos).

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Data analytics lifecycle**?
C) Flexible Box Layout; a one-dimensional CSS layout model that makes it easy to align items and distribute space within a container, handling varying screen sizes dynamically.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
D) The core security model consisting of Confidentiality (preventing unauthorized access), Integrity (preventing unauthorized modification), and Availability (ensuring systems are accessible when needed).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Data analytics lifecycle**.
    * *Why A is correct:* This describes the exact role and function of **Data analytics lifecycle**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Data analytics lifecycle**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Data analytics lifecycle**.


---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
B) SELECT * FROM users WHERE active = 1;
A) GRANT SELECT ON client_db TO analyst_role;
D) CREATE INDEX idx_email ON users(email);
C) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Fundamentals of Data Analytics** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..


---

**Question 5**
When designing a system for **Fundamentals of Data Analytics**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
D) Enable full disk encryption on all client endpoints.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..


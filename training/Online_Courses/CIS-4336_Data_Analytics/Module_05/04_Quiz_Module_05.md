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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **identifying outliers using Z-score and Interquartile Range (IQR).**?
B) A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.
D) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
C) HTML tags that convey the meaning and structure of the enclosed content to both the browser and search engines (e.g., <header>, <article>, <footer>) instead of generic containers.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **identifying outliers using Z-score and Interquartile Range (IQR).**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **identifying outliers using Z-score and Interquartile Range (IQR).**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **identifying outliers using Z-score and Interquartile Range (IQR).**.
    * *Why A is correct:* This describes the exact role and function of **identifying outliers using Z-score and Interquartile Range (IQR).**.


---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
A) GRANT SELECT ON client_db TO analyst_role;
D) CREATE INDEX idx_email ON users(email);
B) EXPLAIN ANALYZE SELECT * FROM logs;
C) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Handling Missing Data and Outliers** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.


---

**Question 5**
When designing a system for **Handling Missing Data and Outliers**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


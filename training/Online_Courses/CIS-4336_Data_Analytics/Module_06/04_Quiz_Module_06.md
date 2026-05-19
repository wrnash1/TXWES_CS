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
B) A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
C) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
D) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **validity**.
    * *Why A is correct:* This describes the exact role and function of **validity**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **validity**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **validity**.


---

**Question 3**
A systems administrator or developer needs to **assign read-only access privileges on the database to a specific security role**. Which of the following commands is the most appropriate to execute?
D) CREATE INDEX idx_email ON users(email);
C) SELECT * FROM users WHERE active = 1;
B) EXPLAIN ANALYZE SELECT * FROM logs;
A) GRANT SELECT ON client_db TO analyst_role;
*   **Correct Answer:** A) GRANT SELECT ON client_db TO analyst_role;
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `GRANT SELECT ON client_db TO analyst_role;` command is directly designed to assign read-only access privileges on the database to a specific security role.


---

**Question 4**
While working on **Data Profiling and Verification** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.


---

**Question 5**
When designing a system for **Data Profiling and Verification**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
D) Enable full disk encryption on all client endpoints.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


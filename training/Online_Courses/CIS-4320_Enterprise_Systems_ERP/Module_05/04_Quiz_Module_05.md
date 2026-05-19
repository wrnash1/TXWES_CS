# Quiz: Module 05 - Financial Management Modules
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
Which ERP module records all financial transactions and serves as the primary data source for balance sheets?
*   A) Material Management
*   B) General Ledger (FI-GL)
*   C) Sales and Distribution
*   D) Human Capital Management
*   **Correct Answer:** B) The General Ledger is the central repository mapping accounts and balancing debits and credits.
*   **Distractor Analysis:**
    *   *Why correct:* The General Ledger is the central repository mapping accounts and balancing debits and credits.
    *   Material Management tracks warehouse inventory assets, not corporate accounting ledgers.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **financial reporting.**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) The total memory space required by an algorithm to execute to completion. This includes the static instruction space, variable space, and dynamic allocation space (like recursion stack frames or temporary arrays).
D) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
C) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **financial reporting.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **financial reporting.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **financial reporting.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **financial reporting.**.


---

**Question 3**
A systems administrator or developer needs to **analyze the database execution plan to identify performance bottlenecks and slow scan steps**. Which of the following commands is the most appropriate to execute?
D) CREATE INDEX idx_email ON users(email);
B) GRANT SELECT ON client_db TO analyst_role;
A) EXPLAIN ANALYZE SELECT * FROM logs;
C) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `EXPLAIN ANALYZE SELECT * FROM logs;` command is directly designed to analyze the database execution plan to identify performance bottlenecks and slow scan steps.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Financial Management Modules** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Financial Management Modules**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


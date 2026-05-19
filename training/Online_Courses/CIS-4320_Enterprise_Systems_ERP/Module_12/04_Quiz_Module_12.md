# Quiz: Module 12 - Data Migration
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
What does the Transform step in the ETL (Extract, Transform, Load) data migration process involve?
*   A) Moving files to tape drives
*   B) Cleaning, reformatting, and mapping raw data to match target database requirements
*   C) Deleting records permanently
*   D) Running compiler updates
*   **Correct Answer:** B) Transform adjusts data structures (e.g. splitting full names into first/last name columns) to match the target database schema.
*   **Distractor Analysis:**
    *   *Why correct:* Transform adjusts data structures (e.g. splitting full names into first/last name columns) to match the target database schema.
    *   Extract pulls raw data. Load writes data to the new database.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Load (ETL)**?
B) The descendant node connected to the left branch of a parent node in a binary tree structure.
D) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
C) A two-dimensional CSS layout system that allows developers to design complex grid-based user interfaces with rows and columns, offering precise control over alignment.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Load (ETL)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Load (ETL)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Load (ETL)**.
    * *Why A is correct:* This describes the exact role and function of **Load (ETL)**.


---

**Question 3**
A systems administrator or developer needs to **create a search index on the email column to speed up lookup queries significantly**. Which of the following commands is the most appropriate to execute?
B) GRANT SELECT ON client_db TO analyst_role;
D) EXPLAIN ANALYZE SELECT * FROM logs;
C) SELECT * FROM users WHERE active = 1;
A) CREATE INDEX idx_email ON users(email);
*   **Correct Answer:** A) CREATE INDEX idx_email ON users(email);
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `CREATE INDEX idx_email ON users(email);` command is directly designed to create a search index on the email column to speed up lookup queries significantly.


---

**Question 4**
While working on **Data Migration** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Data Migration**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


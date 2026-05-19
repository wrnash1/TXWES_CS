# Quiz: Module 08 - Human Capital Management Modules
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
Which data class is managed inside an ERP Human Capital Management (HCM) module?
*   A) Product pricing lists
*   B) Employee records, payroll, benefits, and timecard logs
*   C) Firewall security configurations
*   D) DNS lookup zones
*   **Correct Answer:** B) HCM modules handle personnel files, payroll allocations, tax filings, and organizational structure mappings.
*   **Distractor Analysis:**
    *   *Why correct:* HCM modules handle personnel files, payroll allocations, tax filings, and organizational structure mappings.
    *   Pricing is in sales modules. Firewall logs are system administration tasks.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **employee onboarding**?
C) A data structure that improves the speed of data retrieval operations on a database table at the cost of additional write speed and storage.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
D) The termination condition in a recursive function that stops further recursive calls and begins unwinding the call stack, preventing infinite execution.
B) Data about the HTML document (like description, keywords, author, and viewport configurations) that is processed by browsers and search engine crawlers.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **employee onboarding**.
    * *Why A is correct:* This describes the exact role and function of **employee onboarding**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **employee onboarding**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **employee onboarding**.


---

**Question 3**
A systems administrator or developer needs to **create a search index on the email column to speed up lookup queries significantly**. Which of the following commands is the most appropriate to execute?
D) GRANT SELECT ON client_db TO analyst_role;
A) CREATE INDEX idx_email ON users(email);
B) SELECT * FROM users WHERE active = 1;
C) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Correct Answer:** A) CREATE INDEX idx_email ON users(email);
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `CREATE INDEX idx_email ON users(email);` command is directly designed to create a search index on the email column to speed up lookup queries significantly.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Human Capital Management Modules** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
C) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Two or more transactions are waiting for each other to release locks on resources, causing a permanent block. The appropriate fix is to Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible..
    * *Why C is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why B is incorrect:* This action does not resolve the root cause of Database Deadlock.
    * *Why D is incorrect:* This action does not resolve the root cause of Database Deadlock.


---

**Question 5**
When designing a system for **Human Capital Management Modules**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..


# Quiz: Module 03 - ERP Selection & Vendor Landscape
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
Which ERP vendor is historically the global market leader in enterprise application software?
*   A) Salesforce
*   B) SAP
*   C) Adobe
*   D) Red Hat
*   **Correct Answer:** B) SAP is the dominant enterprise database and ERP platform provider, utilized by the majority of global corporations.
*   **Distractor Analysis:**
    *   *Why correct:* SAP is the dominant enterprise database and ERP platform provider, utilized by the majority of global corporations.
    *   Salesforce is the leader in CRM systems specifically, rather than core ERP backbones.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **total cost of ownership (TCO)**?
D) An instruction within a function that invokes the function itself, passing modified arguments to solve a smaller subproblem.
C) The core CSS layout block consisting of margins, borders, padding, and the actual content area, defining the sizing and spacing of every page element.
B) The additional execution time and CPU operations spent visiting nodes sequentially in memory, which is higher in linked structures than in contiguous arrays.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **total cost of ownership (TCO)**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **total cost of ownership (TCO)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **total cost of ownership (TCO)**.
    * *Why A is correct:* This describes the exact role and function of **total cost of ownership (TCO)**.


---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
D) GRANT SELECT ON client_db TO analyst_role;
C) CREATE INDEX idx_email ON users(email);
A) SELECT * FROM users WHERE active = 1;
B) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **ERP Selection & Vendor Landscape** in a production environment, you encounter a system alert indicating a **Slow Query Performance** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
B) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why A is correct:* Because The database is performing a full table scan on millions of rows due to a missing index or poorly written SQL syntax. The appropriate fix is to Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses..
    * *Why B is incorrect:* This action does not resolve the root cause of Slow Query Performance.
    * *Why D is incorrect:* This action does not resolve the root cause of Slow Query Performance.


---

**Question 5**
When designing a system for **ERP Selection & Vendor Landscape**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


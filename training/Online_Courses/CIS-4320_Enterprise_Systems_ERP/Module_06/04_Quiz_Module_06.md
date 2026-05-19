# Quiz: Module 06 - Supply Chain Management Integrations
## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

**Question 1**
What is the function of Material Requirements Planning (MRP) in an ERP system?
*   A) To design UI screens
*   B) To calculate what materials are needed, in what quantities, and by what dates to meet production schedules
*   C) To monitor database speeds
*   D) To compile python scripts
*   **Correct Answer:** B) MRP uses inventory data, sales orders, and bill of materials (BOM) to schedule component purchases dynamically.
*   **Distractor Analysis:**
    *   *Why correct:* MRP uses inventory data, sales orders, and bill of materials (BOM) to schedule component purchases dynamically.
    *   MRP is logistics math, not UI styling or compiler optimization.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **vendor records.**?
D) The monetary loss expected from a single occurrence of a specific risk event, calculated as Asset Value multiplied by the Exposure Factor (SLE = AV * EF).
B) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
C) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **vendor records.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **vendor records.**.
    * *Why A is correct:* This describes the exact role and function of **vendor records.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **vendor records.**.


---

**Question 3**
A systems administrator or developer needs to **create a search index on the email column to speed up lookup queries significantly**. Which of the following commands is the most appropriate to execute?
C) EXPLAIN ANALYZE SELECT * FROM logs;
A) CREATE INDEX idx_email ON users(email);
D) GRANT SELECT ON client_db TO analyst_role;
B) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) CREATE INDEX idx_email ON users(email);
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `CREATE INDEX idx_email ON users(email);` command is directly designed to create a search index on the email column to speed up lookup queries significantly.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Supply Chain Management Integrations** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.


---

**Question 5**
When designing a system for **Supply Chain Management Integrations**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
C) Enable full disk encryption on all client endpoints.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


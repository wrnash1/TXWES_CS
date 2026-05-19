# Quiz: Module 05 - TrueTime
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Interleaving Tables**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
C) Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.
B) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
D) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **Interleaving Tables**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Interleaving Tables**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Interleaving Tables**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Interleaving Tables**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Interleaving Tables**?
D) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
C) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
B) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Interleaving Tables**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Interleaving Tables**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Interleaving Tables**.
    * *Why A is correct:* This describes the exact role and function of **Interleaving Tables**.


---

**Question 3**
A systems administrator or developer needs to **create a search index on the email column to speed up lookup queries significantly**. Which of the following commands is the most appropriate to execute?
B) EXPLAIN ANALYZE SELECT * FROM logs;
C) SELECT * FROM users WHERE active = 1;
A) CREATE INDEX idx_email ON users(email);
D) GRANT SELECT ON client_db TO analyst_role;
*   **Correct Answer:** A) CREATE INDEX idx_email ON users(email);
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `CREATE INDEX idx_email ON users(email);` command is directly designed to create a search index on the email column to speed up lookup queries significantly.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **TrueTime** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
D) Reboot the physical machine and wait for services to reload.
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.


---

**Question 5**
When designing a system for **TrueTime**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
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


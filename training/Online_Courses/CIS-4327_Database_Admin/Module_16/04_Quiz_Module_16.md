# Quiz: Module 16 - Final Prep
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Documentation**?
B) Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.
D) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
C) The configuration of input data that forces an algorithm to perform the maximum number of operations, providing a guaranteed upper limit on execution time.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why A is correct:* This describes the exact role and function of **Documentation**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.


---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Documentation**?
C) The expected yearly cost of a security risk, calculated by multiplying the Single Loss Expectancy by the Annualized Rate of Occurrence (ALE = SLE * ARO).
B) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
D) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.
    * *Why A is correct:* This describes the exact role and function of **Documentation**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Documentation**.


---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
D) CREATE INDEX idx_email ON users(email);
C) EXPLAIN ANALYZE SELECT * FROM logs;
B) GRANT SELECT ON client_db TO analyst_role;
A) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.


---

**Question 4**
While working on **Final Prep** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.


---

**Question 5**
When designing a system for **Final Prep**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..


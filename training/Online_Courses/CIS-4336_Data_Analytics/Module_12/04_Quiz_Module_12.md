# Quiz: Module 12 - Data Analysis Methods
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Which analysis method groups users based on a shared characteristic or start date to track behavior over time?
*   A) Churn Analysis
*   B) Cohort Analysis
*   C) Outlier Analysis
*   D) Regression Analysis
*   **Correct Answer:** B) Cohort analysis tracks defined groups over time to identify usage or drop-off trends.
*   **Distractor Analysis:**
    *   *Why correct:* Cohort analysis tracks defined groups over time to identify usage or drop-off trends.
    *   Churn only tracks cancellations.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **trend analysis**?
C) Nodes that contain two pointers: one pointing forward to the next node and one pointing backward to the previous node, allowing bidirectional traversal.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
B) The core CSS layout block consisting of margins, borders, padding, and the actual content area, defining the sizing and spacing of every page element.
D) Elements placed inside the <head> block of an HTML document that define metadata, links to stylesheets, scripts, character sets, and page titles.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **trend analysis**.
    * *Why A is correct:* This describes the exact role and function of **trend analysis**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **trend analysis**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **trend analysis**.


---

**Question 3**
A systems administrator or developer needs to **analyze the database execution plan to identify performance bottlenecks and slow scan steps**. Which of the following commands is the most appropriate to execute?
C) CREATE INDEX idx_email ON users(email);
A) EXPLAIN ANALYZE SELECT * FROM logs;
B) SELECT * FROM users WHERE active = 1;
D) GRANT SELECT ON client_db TO analyst_role;
*   **Correct Answer:** A) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `EXPLAIN ANALYZE SELECT * FROM logs;` command is directly designed to analyze the database execution plan to identify performance bottlenecks and slow scan steps.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Analysis Methods** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
B) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..


---

**Question 5**
When designing a system for **Data Analysis Methods**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
D) Enable full disk encryption on all client endpoints.
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


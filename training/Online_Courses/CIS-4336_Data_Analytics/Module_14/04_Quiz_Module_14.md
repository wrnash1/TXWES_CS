# Quiz: Module 14 - Data Warehousing and ETL
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
What does the 'Transform' step in an ETL pipeline involve?
*   A) Extracting raw data from sources
*   B) Cleaning, formatting, and preparing the data for analysis
*   C) Loading the data into a data warehouse
*   D) Backing up the files
*   **Correct Answer:** B) Transformation converts data from source schemas to target structures, cleaning and verifying it.
*   **Distractor Analysis:**
    *   *Why correct:* Transformation converts data from source schemas to target structures, cleaning and verifying it.
    *   Extract is retrieval. Load is writing to target.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Load (ETL)**?
C) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
B) Search Engine Optimization; practices designed to improve the visibility and ranking of web pages in search engine results through clean HTML, meta tags, and alt text.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
D) The entry point or first node in a linked list, which serves as the reference for traversing the rest of the list structure.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within database operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Load (ETL)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Load (ETL)**.
    * *Why A is correct:* This describes the exact role and function of **Load (ETL)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Load (ETL)**.


---

**Question 3**
A systems administrator or developer needs to **create a search index on the email column to speed up lookup queries significantly**. Which of the following commands is the most appropriate to execute?
C) GRANT SELECT ON client_db TO analyst_role;
D) EXPLAIN ANALYZE SELECT * FROM logs;
A) CREATE INDEX idx_email ON users(email);
B) SELECT * FROM users WHERE active = 1;
*   **Correct Answer:** A) CREATE INDEX idx_email ON users(email);
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `CREATE INDEX idx_email ON users(email);` command is directly designed to create a search index on the email column to speed up lookup queries significantly.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Data Warehousing and ETL** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.


---

**Question 5**
When designing a system for **Data Warehousing and ETL**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


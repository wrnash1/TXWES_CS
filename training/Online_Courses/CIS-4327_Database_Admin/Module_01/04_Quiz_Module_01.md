# Quiz: Module 01 - Cloud SQL
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

**Question 1**
Your company is developing a multiplayer mobile game that requires user profiles to be stored as JSON documents. The app needs to support offline synchronization for mobile clients. Which Google Cloud database service is the most appropriate choice?
A) Cloud SQL
B) Cloud Spanner
C) Cloud Bigtable
D) Firestore
*   **Correct Answer:** D) Firestore
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud SQL is a relational SQL database, not designed for native JSON document storage or mobile offline sync.
    *   *Why B is incorrect:* Cloud Spanner is a global relational database, overkill and the wrong paradigm for simple mobile document syncing.
    *   *Why C is incorrect:* Bigtable is for massive analytical workloads and time-series data, not for mobile app backends with offline sync.

---

**Question 2**
You are migrating an on-premises PostgreSQL database to Google Cloud. The application serves users in a single geographic region and requires strong ACID consistency. Which service minimizes migration effort while meeting requirements?
A) Cloud SQL
B) Cloud Spanner
C) BigQuery
D) Firestore
*   **Correct Answer:** A) Cloud SQL
*   **Distractor Analysis:**
    *   *Why B is incorrect:* While Spanner supports PostgreSQL dialects, migrating to it requires architectural changes. Cloud SQL is a direct "lift and shift" for regional PostgreSQL.
    *   *Why C is incorrect:* BigQuery is an enterprise data warehouse for analytics, not an operational transactional (OLTP) database.
    *   *Why D is incorrect:* Firestore is a NoSQL document database, completely incompatible with a direct PostgreSQL migration.

---

**Question 3**
A systems administrator or developer needs to **analyze the database execution plan to identify performance bottlenecks and slow scan steps**. Which of the following commands is the most appropriate to execute?
A) EXPLAIN ANALYZE SELECT * FROM logs;
D) GRANT SELECT ON client_db TO analyst_role;
B) SELECT * FROM users WHERE active = 1;
C) CREATE INDEX idx_email ON users(email);
*   **Correct Answer:** A) EXPLAIN ANALYZE SELECT * FROM logs;
*   **Distractor Analysis:**
    * *Why A is correct:* The `EXPLAIN ANALYZE SELECT * FROM logs;` command is directly designed to analyze the database execution plan to identify performance bottlenecks and slow scan steps.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Cloud SQL** in a production environment, you encounter a system alert indicating a **Database Deadlock** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When designing a system for **Cloud SQL**, you must mitigate the risk of **Unauthorized access to database backup files or physical drives exposing all customer data.**. Which of the following security configurations or controls represents the best practice to implement?
A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
D) Enable full disk encryption on all client endpoints.
B) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest. mitigates the risk of Unauthorized access to database backup files or physical drives exposing all customer data..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Storage.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Storage.


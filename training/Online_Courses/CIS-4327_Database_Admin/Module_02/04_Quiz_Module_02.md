# Quiz: Module 02 - Spanner
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Associate Database Engineer)

---

**Question 1**
You have enabled High Availability (HA) on your Google Cloud SQL for MySQL instance. A developer accidentally executes an `UPDATE` statement without a `WHERE` clause, overwriting all customer records. How will the HA configuration protect the data?
A) The standby instance will reject the malicious UPDATE command, preventing data loss.
B) Cloud SQL will automatically fail over to the standby instance, which retains the old data.
C) HA will not protect against this scenario; the change is synchronously replicated to the standby.
D) The HA configuration will automatically trigger a Point-in-Time Recovery.
*   **Correct Answer:** C) HA will not protect against this scenario; the change is synchronously replicated to the standby.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Standby instances do not parse or judge the intent of SQL queries; they blindly replicate data blocks.
    *   *Why B is incorrect:* Because replication is synchronous, the standby instance will immediately execute the same `UPDATE` statement, meaning both instances will have corrupted data.
    *   *Why D is incorrect:* HA and PITR are separate features. HA does not automatically trigger recoveries based on user queries.

---

**Question 2**
During a regional Cloud SQL HA failover, what happens to the IP address used by the client application to connect to the database?
A) The IP address changes, and the application's connection string must be manually updated.
B) The IP address remains exactly the same, but current connections will be temporarily dropped and must be re-established.
C) The IP address changes, but Google Cloud DNS automatically updates to route traffic seamlessly.
D) The IP address remains the same, and active transactions are held in memory without connection loss.
*   **Correct Answer:** B) The IP address remains exactly the same, but current connections will be temporarily dropped and must be re-established.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* One of the primary benefits of Cloud SQL HA is that the IP address does *not* change during failover.
    *   *Why C is incorrect:* Cloud DNS is not involved in routing traffic to the primary instance during a Cloud SQL failover.
    *   *Why D is incorrect:* Active transactions are lost because the primary instance crashes or is stopped. Client applications must be coded to handle connection drops and retry transactions.

---

**Question 3**
A systems administrator or developer needs to **query and retrieve active user records matching specific conditions from the database table**. Which of the following commands is the most appropriate to execute?
D) CREATE INDEX idx_email ON users(email);
C) EXPLAIN ANALYZE SELECT * FROM logs;
A) SELECT * FROM users WHERE active = 1;
B) GRANT SELECT ON client_db TO analyst_role;
*   **Correct Answer:** A) SELECT * FROM users WHERE active = 1;
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `SELECT * FROM users WHERE active = 1;` command is directly designed to query and retrieve active user records matching specific conditions from the database table.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Spanner** in a production environment, you encounter a system alert indicating a **Connection Timeout** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
C) Optimize application query order, implement retry logic, and keep transaction blocks as brief as possible.
A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
B) Analyze the query plan and create appropriate indexes on columns frequently used in WHERE and JOIN clauses.
*   **Correct Answer:** A) Increase the database connection pool limit, adjust timeout configurations, or scale database resources.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why C is incorrect:* This action does not resolve the root cause of Connection Timeout.
    * *Why A is correct:* Because The database server has exhausted its pool of concurrent client connections or is overloaded with work. The appropriate fix is to Increase the database connection pool limit, adjust timeout configurations, or scale database resources..
    * *Why B is incorrect:* This action does not resolve the root cause of Connection Timeout.


---

**Question 5**
When designing a system for **Spanner**, you must mitigate the risk of **Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents.**. Which of the following security configurations or controls represents the best practice to implement?
B) Enable Transparent Data Encryption (TDE) or cloud database storage encryption at rest.
D) Enable full disk encryption on all client endpoints.
A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.
    * *Why A is correct:* Implementing Enforce parameterized queries and prepared statements, rejecting direct string concatenation of user inputs. mitigates the risk of Attackers injecting malicious SQL strings that bypass authentication and leak entire database contents..
    * *Why C is incorrect:* This does not address the security vulnerability of SQL Injection Exposure.


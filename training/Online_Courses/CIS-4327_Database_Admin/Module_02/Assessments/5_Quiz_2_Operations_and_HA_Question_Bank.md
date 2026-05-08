### 5. Quiz 2: Operations and HA (Question Bank)
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

# Quiz: Module 02 - Database Design – Normalization and ERDs
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

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
    *   *Why D is incorrect:* HA and PITR are separate features. HA does not automatically trigger recoveries based on user queries; you must manually initiate a PITR restore.

---

---

**Question 2**
During a regional Cloud SQL HA failover, what happens to the IP address used by the client application to connect to the database?
A) The IP address changes, and the application's connection string must be manually updated.
B) The IP address remains exactly the same, but current connections will be temporarily dropped and must be re-established.
C) The IP address changes, but Google Cloud DNS automatically updates to route traffic seamlessly.
D) The IP address remains the same, and active transactions are preserved in memory without connection loss.
*   **Correct Answer:** B) The IP address remains exactly the same, but current connections will be temporarily dropped and must be re-established.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* One of the primary benefits of Cloud SQL HA is that the instance IP address does *not* change during failover, so connection strings require no update.
    *   *Why C is incorrect:* Cloud DNS is not involved in routing traffic to the Cloud SQL primary instance; failover is handled internally by Cloud SQL's control plane.
    *   *Why D is incorrect:* Active transactions are lost because the primary instance is stopped. Client applications must implement connection retry logic to handle the brief interruption.

---

---

**Question 3**
A database designer is reviewing a table where the primary key is a composite of `(order_id, product_id)`. The column `product_name` depends only on `product_id`, not on the full composite key. Which normal form is violated?
A) First Normal Form (1NF), because the column contains repeating groups.
B) Second Normal Form (2NF), because `product_name` has a partial dependency on the primary key.
C) Third Normal Form (3NF), because `product_name` is transitively dependent on a non-key attribute.
D) Boyce-Codd Normal Form (BCNF), because there is a functional dependency from a non-superkey attribute.
*   **Correct Answer:** B) Second Normal Form (2NF), because `product_name` has a partial dependency on the primary key.
*   **Distractor Analysis:**
    *   *Why B is correct:* 2NF requires that every non-key attribute depend on the *entire* composite primary key. `product_name` depends only on `product_id`, making it a partial dependency — a 2NF violation. The fix is to move `product_name` to a separate `products` table with `product_id` as the primary key.
    *   *Why A is incorrect:* 1NF is about atomic column values and unique rows, not about key dependencies. The table likely already satisfies 1NF.
    *   *Why C is incorrect:* A transitive dependency (3NF violation) exists when a non-key column depends on another non-key column, not when it depends on part of the key.
    *   *Why D is incorrect:* BCNF is a stricter variant of 3NF. The described issue is a clear 2NF violation, which must be resolved before higher normal forms can be assessed.

---

**Question 4**
A data architect is designing a schema for a new Cloud Spanner instance that stores customer orders and their line items. To maximize performance for queries that retrieve an order and all its line items together, which Cloud Spanner-specific schema technique should be used?
A) Create a separate database for line items to allow independent scaling.
B) Define the `LineItems` table as interleaved within the `Orders` table using the `INTERLEAVE IN PARENT` clause.
C) Store line items as a JSON column inside the `Orders` table to avoid the need for JOINs.
D) Create a Cloud Spanner secondary index on the `order_id` foreign key in the `LineItems` table.
*   **Correct Answer:** B) Define the `LineItems` table as interleaved within the `Orders` table using the `INTERLEAVE IN PARENT` clause.
*   **Distractor Analysis:**
    *   *Why B is correct:* Interleaving physically co-locates child rows (line items) with their parent row (order) on the same storage split. This eliminates cross-split network hops for parent-child JOINs and is the primary Spanner schema optimization for hierarchical data.
    *   *Why A is incorrect:* Splitting tables into separate databases increases latency for cross-database operations and is the opposite of the co-location strategy Spanner's interleaving provides.
    *   *Why C is incorrect:* Storing line items as JSON inside the parent row defeats normalization, creates unbounded row growth, and prevents efficient filtering or aggregation on individual line item attributes.
    *   *Why D is incorrect:* A secondary index helps locate rows by `order_id` but does not change the physical storage layout; rows remain on potentially different splits, incurring remote read overhead.

---

**Question 5**
When securing a Cloud SQL database, you must mitigate the risk of **unauthorized access to database backup files exposing all customer data**. Which control best addresses this vulnerability?
A) Enable Google-managed or Customer-Managed Encryption Keys (CMEK) to encrypt backups at rest.
B) Enforce parameterized queries and prepared statements in all application code.
C) Configure Private IP access and disable the public IP address on the Cloud SQL instance.
D) Enable Cloud SQL Auth Proxy to secure connections from application servers.
*   **Correct Answer:** A) Enable Google-managed or Customer-Managed Encryption Keys (CMEK) to encrypt backups at rest.
*   **Distractor Analysis:**
    *   *Why A is correct:* Backup files stored on GCP infrastructure are encrypted at rest. Using CMEK via Cloud KMS gives your organization exclusive key control, ensuring that even if backup media were physically obtained, the data would be unreadable without the key.
    *   *Why B is incorrect:* Parameterized queries prevent SQL injection in application code; they have no effect on the security of stored backup files.
    *   *Why C is incorrect:* Private IP restricts network access to the live instance, not to stored backup files at rest in Google's storage layer.
    *   *Why D is incorrect:* Cloud SQL Auth Proxy secures in-transit connections between an application and the database instance; it does not protect backup files stored at rest.

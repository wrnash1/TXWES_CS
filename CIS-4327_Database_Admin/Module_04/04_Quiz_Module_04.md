# Quiz: Module 04 - Cloud Spanner – Globally Distributed Databases
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
Your organization has strict compliance requirements that dictate all database backups and persistent disks must be encrypted using keys that your organization exclusively generates, manages, and rotates. Which Google Cloud feature must you implement to satisfy this requirement for Cloud SQL?
A) Google-managed encryption keys
B) Customer-Managed Encryption Keys (CMEK) using Cloud KMS
C) Transparent Data Encryption (TDE)
D) IPsec VPN tunnels
*   **Correct Answer:** B) Customer-Managed Encryption Keys (CMEK) using Cloud KMS
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Google-managed keys are the default encryption method, but they do not satisfy compliance requirements that demand the *customer* generate and exclusively control the key material.
    *   *Why C is incorrect:* TDE is a specific Microsoft SQL Server encryption feature. GCP's equivalent mechanism for customer-controlled key management across GCP services is CMEK via Cloud KMS.
    *   *Why D is incorrect:* IPsec VPN encrypts data *in transit* across a network connection; it does not encrypt data *at rest* on persistent disks or backup storage.

---

---

**Question 2**
A developer complains that an application is running slowly. You suspect the Cloud SQL database is the bottleneck, but the overall CPU utilization of the instance is only 40%. You need to identify if a specific SQL `SELECT` statement is taking too long to execute. Which Google Cloud tool provides this specific visibility?
A) Cloud Audit Logs
B) Cloud SQL Auth Proxy
C) Query Insights
D) Identity and Access Management (IAM)
*   **Correct Answer:** C) Query Insights
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud Audit Logs record *who* performed administrative and data access actions, but do not provide per-query execution time, query plans, or load analysis.
    *   *Why B is incorrect:* Cloud SQL Auth Proxy establishes a secure, IAM-authenticated connection tunnel to Cloud SQL; it is not a monitoring or performance analysis tool.
    *   *Why D is incorrect:* IAM manages access control and permissions across Google Cloud; it is entirely unrelated to diagnosing database query performance.

---

---

**Question 3**
A Cloud Spanner schema designer is building a table for `Orders` and a child table for `OrderItems`. To ensure that `OrderItems` rows are physically co-located with their parent `Orders` row for efficient retrieval, which DDL clause must be added to the `OrderItems` table definition?
A) `INTERLEAVE IN PARENT Orders ON DELETE CASCADE`
B) `FOREIGN KEY (order_id) REFERENCES Orders(order_id)`
C) `CREATE INDEX idx_order ON OrderItems(order_id) STORING (quantity, price)`
D) `PARTITION BY order_id`
*   **Correct Answer:** A) `INTERLEAVE IN PARENT Orders ON DELETE CASCADE`
*   **Distractor Analysis:**
    *   *Why A is correct:* The `INTERLEAVE IN PARENT` clause is a Cloud Spanner-specific DDL directive that physically co-locates child rows on the same storage split as their parent row, eliminating cross-split remote reads for parent-child queries.
    *   *Why B is incorrect:* A `FOREIGN KEY` constraint enforces referential integrity but does not alter the physical storage layout; rows may still reside on different splits, incurring remote read overhead.
    *   *Why C is incorrect:* A secondary index with a `STORING` clause helps locate rows by a non-primary-key column but does not co-locate child rows with parent rows on the same split.
    *   *Why D is incorrect:* `PARTITION BY` is a BigQuery DDL concept for partitioned tables; it does not exist in Cloud Spanner DDL.

---

**Question 4**
While administering a Cloud Spanner instance, you notice that write throughput has degraded significantly even though CPU utilization on compute nodes is low. After reviewing the key distribution, you discover that all recent inserts are going to the same storage split. What is the most likely root cause?
A) The application is using bounded-staleness stale reads instead of strong reads.
B) The schema is using a monotonically increasing integer (auto-increment) as the primary key, causing a write hotspot.
C) The instance does not have enough Processing Units allocated for the current query load.
D) The interleaved child table has grown larger than the parent table, causing rebalancing overhead.
*   **Correct Answer:** B) The schema is using a monotonically increasing integer (auto-increment) as the primary key, causing a write hotspot.
*   **Distractor Analysis:**
    *   *Why B is correct:* Cloud Spanner distributes data across splits by key range. Sequential (auto-incrementing) primary keys cause all new writes to land at the top of the key range, which maps to a single split — a classic hotspot. The fix is to use UUIDs, bit-reversed integers, or a hash prefix.
    *   *Why A is incorrect:* Stale reads are a read-path optimization that reduce lock contention; they do not cause write concentration on a single split.
    *   *Why C is incorrect:* Low CPU utilization on nodes indicates the bottleneck is not a compute resource shortage; it points to a data distribution problem.
    *   *Why D is incorrect:* Spanner splits are rebalanced automatically by the service when they exceed size thresholds; this does not cause a write throughput regression related to key distribution.

---

**Question 5**
When designing a global Cloud Spanner deployment, you must mitigate the risk of **attackers injecting malicious SQL strings that bypass authentication and expose database contents**. Which control best addresses this vulnerability?
A) Enforce parameterized queries and use the Spanner client libraries' statement binding API, rejecting direct string concatenation of user inputs.
B) Enable CMEK with Cloud KMS to encrypt all Spanner data at rest.
C) Configure a VPC Service Controls perimeter around the Cloud Spanner API to restrict access by network.
D) Enable Cloud Audit Logs Data Access logs to record all SQL statements executed against the Spanner instance.
*   **Correct Answer:** A) Enforce parameterized queries and use the Spanner client libraries' statement binding API, rejecting direct string concatenation of user inputs.
*   **Distractor Analysis:**
    *   *Why A is correct:* SQL injection is a code-level vulnerability. Cloud Spanner client libraries support parameterized queries with type-safe parameter binding. Passing user input as a bound parameter prevents the database from ever interpreting user-supplied strings as SQL syntax.
    *   *Why B is incorrect:* CMEK protects data at rest on Spanner's physical storage; it does not affect how the application constructs query strings and provides no protection against injection.
    *   *Why C is incorrect:* VPC Service Controls restrict which networks and identities can call the Spanner API, reducing attack surface but not preventing injection from a legitimate, compromised application.
    *   *Why D is incorrect:* Audit logs record that an injection occurred after the fact but do not prevent the attack. Detection is not a substitute for prevention.

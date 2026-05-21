# Quiz: Module 12 - Database Migration – DMS and Migrate for Compute Engine
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
Your organization wants to migrate a production Oracle 19c database to Cloud SQL for PostgreSQL. The application cannot be down for more than 2 hours during cutover. What type of migration is required and what must be completed before data transfer can begin?
A) Homogeneous migration; configure a VPN tunnel between on-premises and GCP.
B) Heterogeneous migration; convert the Oracle schema DDL and PL/SQL stored procedures to PostgreSQL-compatible syntax.
C) Lift-and-shift migration; export the Oracle database using Data Pump and import into Cloud SQL for PostgreSQL.
D) Continuous migration; enable Oracle Streams CDC on the source database.
*   **Correct Answer:** B) Heterogeneous migration; convert the Oracle schema DDL and PL/SQL stored procedures to PostgreSQL-compatible syntax.
*   **Distractor Analysis:**
    *   *Why B is correct:* Oracle to PostgreSQL is a heterogeneous migration (different database engines with different SQL dialects, data types, and procedural language syntax). Schema conversion is mandatory before the initial data load can begin, because the Oracle DDL is not directly compatible with PostgreSQL.
    *   *Why A is incorrect:* Oracle to PostgreSQL is heterogeneous, not homogeneous. A VPN tunnel is a connectivity requirement but is not the first and primary action needed before data transfer.
    *   *Why C is incorrect:* "Lift-and-shift" refers to moving a workload without changing the underlying technology (e.g., Oracle on-premises to Oracle on a GCE VM). Changing from Oracle to PostgreSQL is a re-platforming migration requiring engine conversion. Oracle Data Pump export format is also not directly importable into PostgreSQL.
    *   *Why D is incorrect:* Oracle Streams is a legacy Oracle replication technology; DMS for heterogeneous Oracle-to-PostgreSQL migrations uses LogMiner-based CDC, not Oracle Streams. Additionally, CDC setup comes after schema conversion, not before.

---

---

**Question 2**
A DMS migration job from an on-premises MySQL 8.0 database to Cloud SQL for MySQL has completed its initial load. The job status shows "Running" and CDC is actively replicating changes. The operations team is ready to perform cutover. What is the correct sequence of final steps?
A) Delete the DMS migration job, then update the application connection string.
B) Stop all writes to the source database, wait for CDC lag to reach zero, then promote the Cloud SQL destination instance, then update the application connection string.
C) Promote the Cloud SQL destination instance immediately, then stop writes to the source database.
D) Enable Cloud SQL HA on the destination instance before promoting it to ensure high availability.
*   **Correct Answer:** B) Stop all writes to the source database, wait for CDC lag to reach zero, then promote the Cloud SQL destination instance, then update the application connection string.
*   **Distractor Analysis:**
    *   *Why B is correct:* The correct cutover sequence is: (1) Stop application writes to the source to prevent new changes from being missed, (2) Wait for the CDC replication lag to reach zero (all pending changes replicated), (3) Promote the destination to sever the replication link and make it writable, (4) Update the application connection string to point to the new Cloud SQL instance.
    *   *Why A is incorrect:* Deleting the DMS job before promoting would leave the destination in an ambiguous state. The promotion step is what severs the replication link cleanly and makes the instance fully writable.
    *   *Why C is incorrect:* Promoting before stopping writes means new changes written to the source after promotion will never be replicated to the destination, causing data loss during the window between promotion and source shutdown.
    *   *Why D is incorrect:* While enabling HA after migration is a good practice, doing it before promotion adds unnecessary delay to the cutover window and is not a required step in the promotion sequence.

---

---

**Question 3**
A database migration engineer needs to **query the current replication lag in seconds for a DMS migration job** to determine if CDC is keeping up with the source database write rate. Which approach is most appropriate?
A) Monitor the `database_migration_service/migration_job/replication_lag` metric in Cloud Monitoring.
B) Run `SHOW SLAVE STATUS` on the Cloud SQL destination to view replication lag.
C) Run `SELECT * FROM information_schema.replica_status` on the DMS migration endpoint.
D) Check the Cloud Audit Logs for the DMS service to view replication event timestamps.
*   **Correct Answer:** A) Monitor the `database_migration_service/migration_job/replication_lag` metric in Cloud Monitoring.
*   **Distractor Analysis:**
    *   *Why A is correct:* DMS exports its migration job metrics to Cloud Monitoring, including `replication_lag` measured in seconds. You can create a Cloud Monitoring dashboard or alert based on this metric to proactively detect when lag is increasing and the destination is falling behind the source.
    *   *Why B is incorrect:* `SHOW SLAVE STATUS` is a MySQL command that can show replication lag for traditional MySQL replication. During an active DMS migration, DMS manages the replication connection internally and the Cloud SQL instance is in a read-only replication state — but the recommended method is Cloud Monitoring, not direct SQL commands.
    *   *Why C is incorrect:* `information_schema.replica_status` is not a standard SQL view; this syntax does not exist in MySQL, PostgreSQL, or the DMS API.
    *   *Why D is incorrect:* Cloud Audit Logs record administrative actions (who created/modified the DMS job), not per-second replication performance metrics. Audit logs are not suitable for monitoring replication lag in real time.

---

**Question 4**
After successfully migrating a MySQL database to Cloud SQL for MySQL using DMS, the application team reports that queries that were fast on the on-premises source are running significantly slower on Cloud SQL. No indexes have been changed. What should be the first diagnostic action?
A) Run `EXPLAIN` on the slow queries and compare the execution plans between the on-premises source and the Cloud SQL destination to identify differences in index usage or table statistics.
B) Immediately upgrade the Cloud SQL instance to a larger machine type to match the on-premises server's hardware specs.
C) Restore the database from the DMS migration backup and retry the migration with a larger instance type.
D) Check Cloud Audit Logs to see if the application is connecting with insufficient IAM permissions that are degrading query execution.
*   **Correct Answer:** A) Run `EXPLAIN` on the slow queries and compare the execution plans between the on-premises source and the Cloud SQL destination to identify differences in index usage or table statistics.
*   **Distractor Analysis:**
    *   *Why A is correct:* Performance differences after migration are commonly caused by: missing statistics on Cloud SQL (run `ANALYZE TABLE`), different MySQL configuration flags (e.g., `innodb_buffer_pool_size`), or a different query optimizer version. Running `EXPLAIN` on both systems side-by-side pinpoints whether the Cloud SQL optimizer is choosing a different (worse) plan, which informs the specific fix needed.
    *   *Why B is incorrect:* Scaling up the instance may help but is an expensive first response. The root cause — statistics, configuration, or query plan differences — should be diagnosed first so the fix is targeted and cost-efficient.
    *   *Why C is incorrect:* The migration itself is complete and working; the issue is a post-migration performance problem. Restarting the migration does not fix optimizer or statistics differences.
    *   *Why D is incorrect:* IAM permissions control whether a connection is permitted, not how a permitted query is executed. An IAM permission error results in an access denied error, not slow query execution.

---

**Question 5**
When migrating a database to Cloud SQL using DMS, you must mitigate the risk of **CDC replication traffic between the on-premises source database and GCP being intercepted and read by a network adversary**. Which control best addresses this threat?
A) Configure an IPsec VPN tunnel or Cloud Interconnect between the on-premises network and the GCP VPC used by DMS, encrypting all migration traffic in transit.
B) Enable CMEK on the Cloud SQL destination instance to encrypt the replicated data at rest.
C) Enable Google-managed encryption on the DMS migration job's staging Cloud Storage bucket.
D) Use Cloud Armor to create a WAF policy that blocks unauthorized IP addresses from sending data to the DMS endpoint.
*   **Correct Answer:** A) Configure an IPsec VPN tunnel or Cloud Interconnect between the on-premises network and the GCP VPC used by DMS, encrypting all migration traffic in transit.
*   **Distractor Analysis:**
    *   *Why A is correct:* An IPsec VPN tunnel encrypts all traffic between the on-premises network and GCP using IPsec, preventing network interception of CDC replication data in transit. Cloud Dedicated Interconnect provides a private, physical connection that never traverses the public internet, offering equivalent protection against network interception.
    *   *Why B is incorrect:* CMEK encrypts data at rest on Cloud SQL's physical storage after it has been received and written. It does not encrypt the CDC replication stream as it travels across the network from on-premises to GCP.
    *   *Why C is incorrect:* Encrypting the DMS staging bucket protects data stored in Cloud Storage at rest but does not protect the in-transit replication stream between the on-premises source and GCP.
    *   *Why D is incorrect:* Cloud Armor is a WAF and DDoS protection service for HTTP/HTTPS applications and Google Cloud load balancers; it does not provide network-layer encryption for TCP database replication traffic.

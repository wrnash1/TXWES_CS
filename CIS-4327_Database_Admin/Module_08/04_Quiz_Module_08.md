# Quiz: Module 08 - AlloyDB for PostgreSQL
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
A financial services company runs a mission-critical PostgreSQL workload on Cloud SQL for PostgreSQL. The business requires a maximum of 30 seconds of downtime after any single-instance failure (RTO ≤ 30s) and zero data loss (RPO = 0). Which GCP database service best meets these requirements while maintaining full PostgreSQL compatibility?
A) Cloud SQL for PostgreSQL with HA enabled
B) Cloud Spanner with a PostgreSQL-compatible dialect
C) AlloyDB for PostgreSQL
D) Cloud SQL for PostgreSQL with a cross-region read replica
*   **Correct Answer:** C) AlloyDB for PostgreSQL
*   **Distractor Analysis:**
    *   *Why C is correct:* AlloyDB's disaggregated storage architecture provides sub-60-second failover RTO (typically under 30 seconds) and near-zero RPO because writes are synchronously committed to the distributed storage layer before acknowledgment. It is fully PostgreSQL-compatible, requiring no application changes.
    *   *Why A is incorrect:* Cloud SQL HA failover typically takes 60–120 seconds. While it provides synchronous replication to the standby zone (near-zero RPO), it does not reliably meet a 30-second RTO requirement.
    *   *Why B is incorrect:* Cloud Spanner with a PostgreSQL dialect requires significant schema and query rewrites and is not wire-compatible with standard PostgreSQL drivers; migrating to it is not maintaining "full PostgreSQL compatibility".
    *   *Why D is incorrect:* Cross-region read replicas use asynchronous replication, which means there is a replication lag and potential data loss (non-zero RPO). They also require manual promotion, not automatic failover.

---

---

**Question 2**
An AlloyDB for PostgreSQL cluster is serving a mixed OLTP and analytics workload. Business analysts run complex aggregation queries that are slowing down transactional operations on the same instance. Which AlloyDB architectural feature can help serve both workloads on the same cluster without adding a separate analytics database?
A) AlloyDB's built-in adaptive columnar cache, which automatically materializes a column-oriented copy of hot data in memory for analytical queries.
B) AlloyDB read pool nodes configured with a separate PostgreSQL `postgresql.conf` for analytics settings.
C) BigQuery Federated Queries that connect directly to the AlloyDB cluster for analytical processing.
D) AlloyDB Omni deployed on a separate VM to serve analytical queries independently.
*   **Correct Answer:** A) AlloyDB's built-in adaptive columnar cache, which automatically materializes a column-oriented copy of hot data in memory for analytical queries.
*   **Distractor Analysis:**
    *   *Why A is correct:* AlloyDB includes an adaptive, in-memory columnar engine that detects hot data accessed analytically and automatically maintains a columnar representation in memory. Analytical queries are transparently routed to this columnar cache, while OLTP queries continue using the row store — an HTAP capability that eliminates the need for a separate analytics database.
    *   *Why B is incorrect:* AlloyDB read pool nodes share the same storage and PostgreSQL engine configuration; they do not have separate `postgresql.conf` files and would still perform row-based scans for analytical queries without the columnar cache.
    *   *Why C is incorrect:* BigQuery Federated Queries connect to Cloud SQL and Spanner, not to AlloyDB. This would also add latency and data movement costs for each analytical query.
    *   *Why D is incorrect:* AlloyDB Omni is the self-managed containerized version of AlloyDB for deployment outside GCP managed infrastructure; it does not share storage with the managed AlloyDB cluster and would require separate data synchronization.

---

---

**Question 3**
A database administrator needs to **create an index on the `customer_email` column to speed up authentication lookup queries on an AlloyDB for PostgreSQL instance**. Which SQL command is most appropriate?
A) CREATE INDEX idx_customer_email ON customers(customer_email);
B) ALTER TABLE customers ADD CONSTRAINT ux_email UNIQUE (customer_email);
C) GRANT SELECT ON customers TO app_service_account;
D) EXPLAIN ANALYZE SELECT * FROM customers WHERE customer_email = 'test@example.com';
*   **Correct Answer:** A) CREATE INDEX idx_customer_email ON customers(customer_email);
*   **Correct Answer:** A) CREATE INDEX idx_customer_email ON customers(customer_email);
*   **Distractor Analysis:**
    *   *Why A is correct:* `CREATE INDEX` creates a B-tree index on the specified column, enabling index scans instead of sequential scans for lookup queries. AlloyDB is PostgreSQL-compatible and uses the same DDL syntax.
    *   *Why B is incorrect:* `ADD CONSTRAINT UNIQUE` creates a unique constraint that also creates an index as a side effect, but it additionally enforces uniqueness. If the column already has duplicate values or uniqueness is not required, this command will fail or impose an unintended restriction.
    *   *Why C is incorrect:* `GRANT SELECT` assigns read permission to an identity; it does not create any index or improve query performance.
    *   *Why D is incorrect:* `EXPLAIN ANALYZE` executes the query and displays its execution plan for diagnostic purposes; it does not create an index or change how future queries are executed.

---

**Question 4**
An AlloyDB for PostgreSQL primary instance becomes unavailable due to a zone outage. The operations team reports that the automatic failover completed, but the application is still sending write requests to the old primary's IP address. What is the correct resolution?
A) Update the application's database connection string to point to the new primary's IP address or hostname.
B) Manually promote the AlloyDB read pool node to become the new primary using the `gcloud alloydb instances promote` command.
C) Restore the AlloyDB instance from the most recent automated backup to recover the primary IP address.
D) Wait for AlloyDB to rebalance and reassign the original primary IP address to the new primary node.
*   **Correct Answer:** A) Update the application's database connection string to point to the new primary's IP address or hostname.
*   **Distractor Analysis:**
    *   *Why A is correct:* AlloyDB automatic failover promotes a new primary instance, which may have a different IP address from the failed instance. The recommended approach is to use AlloyDB's stable connection endpoint or update the connection string. Using the AlloyDB Auth Proxy or a connection via the cluster's primary instance hostname (which automatically routes to the current primary) avoids this issue.
    *   *Why B is incorrect:* AlloyDB read pool nodes are horizontally scalable read replicas; they are not promoted to primary. AlloyDB failover uses a separate primary instance managed by the cluster, not a read pool node.
    *   *Why C is incorrect:* Restoring from backup is a last-resort data recovery operation, not the correct response to a failover event. The data is not lost — the new primary already has it.
    *   *Why D is incorrect:* AlloyDB does not automatically reassign IP addresses from a failed instance. IP addresses are tied to the specific instance that has been stopped; a new primary gets a new address.

---

**Question 5**
When securing an AlloyDB for PostgreSQL instance, you must mitigate the risk of **unauthorized network access to the database from the public internet**. Which control best addresses this vulnerability?
A) Configure AlloyDB to use Private IP only within a VPC network and disable the public IP address.
B) Enable CMEK with Cloud KMS to encrypt the AlloyDB storage volumes at rest.
C) Set a strong password policy for all AlloyDB database users using `ALTER USER`.
D) Enable Cloud Audit Data Access Logs to monitor and alert on unauthorized login attempts.
*   **Correct Answer:** A) Configure AlloyDB to use Private IP only within a VPC network and disable the public IP address.
*   **Distractor Analysis:**
    *   *Why A is correct:* Disabling the public IP address ensures the AlloyDB instance is only reachable from within the VPC network (or via VPC peering/Private Service Connect). This eliminates the entire attack surface from the public internet at the network layer, preventing any unauthorized external connection attempts from reaching the database port.
    *   *Why B is incorrect:* CMEK encrypts data at rest on physical storage; it does not restrict network-level access. An attacker with network access could still attempt to connect to the database port regardless of storage encryption.
    *   *Why C is incorrect:* Strong passwords reduce the risk of credential compromise but do not prevent network-level access. An attacker can still attempt connections and brute-force passwords if the instance is publicly accessible.
    *   *Why D is incorrect:* Audit logs detect unauthorized access attempts after they have already reached the database; they do not block network connections from the public internet.

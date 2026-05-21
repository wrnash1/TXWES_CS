# Quiz: Module 11 - Database Performance Tuning and Query Optimization
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
A Cloud SQL for PostgreSQL instance is experiencing high CPU utilization and slow query response times. You need to identify which specific SQL queries are consuming the most resources without modifying application code or enabling pg_stat_statements manually. Which GCP-native tool provides this visibility directly from the Cloud Console?
A) Cloud SQL Query Insights
B) Cloud Audit Logs
C) Cloud SQL Auth Proxy metrics
D) VPC Flow Logs
*   **Correct Answer:** A) Cloud SQL Query Insights
*   **Distractor Analysis:**
    *   *Why A is correct:* Cloud SQL Query Insights is a built-in performance monitoring feature in the Cloud SQL console that automatically samples database queries, ranks them by CPU consumption and execution time, and provides per-query execution plans and latency percentiles — all without any application code changes or manual pg_stat_statements configuration.
    *   *Why B is incorrect:* Cloud Audit Logs record administrative and data access events (who executed what) but do not provide performance metrics, execution times, or resource consumption per query.
    *   *Why C is incorrect:* Cloud SQL Auth Proxy provides connection security and IAM authentication; it does not collect or report query-level performance metrics.
    *   *Why D is incorrect:* VPC Flow Logs record network packet metadata (source/destination IP, bytes, protocol) for network traffic analysis; they have no visibility into database query performance.

---

---

**Question 2**
The following `EXPLAIN ANALYZE` output is returned for a query on a Cloud SQL for PostgreSQL table with 50 million rows:

```
Seq Scan on orders (cost=0.00..8500000 rows=50000000) (actual time=0.032..45231.421 ms)
  Filter: (customer_id = 'C00123')
```

What is the most appropriate action to improve this query's performance?
A) Create a B-tree index on the `customer_id` column: `CREATE INDEX idx_orders_customer ON orders(customer_id);`
B) Increase the Cloud SQL instance's machine type to a larger CPU/RAM configuration.
C) Enable connection pooling to reduce the overhead of establishing new connections.
D) Run `VACUUM ANALYZE orders;` to update table statistics and improve the query planner's cost estimates.
*   **Correct Answer:** A) Create a B-tree index on the `customer_id` column: `CREATE INDEX idx_orders_customer ON orders(customer_id);`
*   **Distractor Analysis:**
    *   *Why A is correct:* The execution plan clearly shows a `Seq Scan` (sequential scan) over 50 million rows with a filter on `customer_id`. This means the database reads every row to find matching records. Creating a B-tree index on `customer_id` converts this to an index scan that directly locates the matching rows in O(log n) time, reducing the 45-second query to milliseconds.
    *   *Why B is incorrect:* A larger machine makes the sequential scan run faster, but a 50-million-row full table scan will still be orders of magnitude slower than an index scan. Scaling up the instance does not fix the root algorithmic problem.
    *   *Why C is incorrect:* Connection pooling reduces the overhead of connection establishment for high-concurrency workloads; it does not change how a single query is executed or reduce its scan cost.
    *   *Why D is incorrect:* `VACUUM ANALYZE` updates table statistics used by the planner for cost estimates. It is valuable when the planner is making bad row count estimates, but the execution plan already shows the correct 50 million rows. The problem is a missing index, not stale statistics.

---

---

**Question 3**
A database administrator needs to **create a composite index on the `status` and `created_at` columns of the `orders` table to support queries that filter by both columns simultaneously**. Which SQL command is most appropriate?
A) CREATE INDEX idx_orders_status_date ON orders(status, created_at);
B) GRANT SELECT ON orders TO analyst_role;
C) EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'pending' AND created_at > '2024-01-01';
D) ALTER TABLE orders ADD COLUMN status_created_composite VARCHAR(100);
*   **Correct Answer:** A) CREATE INDEX idx_orders_status_date ON orders(status, created_at);
*   **Distractor Analysis:**
    *   *Why A is correct:* A composite index on `(status, created_at)` allows the query planner to use an index scan for queries that filter on `status` alone, `status` and `created_at` together, or use `created_at` for range scans after filtering on `status`. Column order matters: put the equality filter column (`status`) first.
    *   *Why B is incorrect:* `GRANT SELECT` assigns read permission to a role; it does not create any index or improve query performance.
    *   *Why C is incorrect:* `EXPLAIN ANALYZE` executes the query and shows the execution plan for diagnostic purposes; it does not create an index or modify the schema.
    *   *Why D is incorrect:* Adding a combined column does not create a database index and would require denormalizing data, adding maintenance overhead, and rewriting queries.

---

**Question 4**
An application connecting to a Cloud SQL for PostgreSQL instance is experiencing connection timeouts during peak traffic hours. Cloud Monitoring shows that the number of active database connections is consistently hitting the maximum connection limit for the instance's machine type. Which is the most appropriate long-term solution?
A) Deploy a connection pooler such as PgBouncer (using Cloud SQL Proxy's connection pooling or a dedicated PgBouncer instance) to multiplex many application connections over a smaller number of persistent database connections.
B) Upgrade the Cloud SQL instance to the largest available machine type to maximize the connection limit.
C) Enable Cloud SQL HA to distribute connection load between the primary and standby instances.
D) Add a Cloud SQL read replica to handle half of the incoming connections.
*   **Correct Answer:** A) Deploy a connection pooler such as PgBouncer to multiplex many application connections over a smaller number of persistent database connections.
*   **Distractor Analysis:**
    *   *Why A is correct:* Connection pool exhaustion is caused by too many application threads holding open database connections, not by insufficient compute. A connection pooler like PgBouncer (or pgBouncer configured with Cloud SQL Auth Proxy) multiplexes thousands of application connections over a small pool of actual database connections, resolving the exhaustion without requiring a larger instance.
    *   *Why B is incorrect:* Larger machine types have higher connection limits, but this is a short-term workaround. As the application grows, it will hit the new limit. Connection pooling addresses the root cause (inefficient connection management) and scales to any traffic volume.
    *   *Why C is incorrect:* Cloud SQL HA standby instances do not accept connections; they only receive synchronous replication. Enabling HA does not increase the number of available connections.
    *   *Why D is incorrect:* Read replicas can offload read-only queries but cannot serve write connections. If the application is running write-heavy transactions during peak hours, a read replica does not help.

---

**Question 5**
When hardening a Cloud SQL for PostgreSQL instance for performance and security, you must prevent **unauthorized users from reading the full contents of slow query logs that may contain sensitive data values in query parameters**. Which control best addresses this vulnerability?
A) Configure Cloud SQL to use `log_min_duration_statement = -1` (disable slow query logging) and instead use Query Insights, which does not log raw parameter values.
B) Enable CMEK on the Cloud SQL instance to encrypt slow query log files at rest.
C) Grant only the `roles/cloudsql.viewer` IAM role to users who need to see query metrics but not raw log data.
D) Store slow query logs in a Cloud Storage bucket with Uniform Bucket-Level Access and restrict the bucket IAM to a dedicated logging service account.
*   **Correct Answer:** D) Store slow query logs in a Cloud Storage bucket with Uniform Bucket-Level Access and restrict the bucket IAM to a dedicated logging service account.
*   **Distractor Analysis:**
    *   *Why D is correct:* Cloud SQL logs can be exported to Cloud Storage. Applying Uniform Bucket-Level Access (disabling per-object ACLs) and restricting bucket IAM to a dedicated service account ensures that only authorized log analysis processes can read raw query log files, preventing accidental exposure of query parameter values that may contain PII or sensitive data.
    *   *Why A is incorrect:* Disabling slow query logging removes a critical diagnostic capability. Query Insights is an excellent tool but does not fully replace the information available in slow query logs for all troubleshooting scenarios.
    *   *Why B is incorrect:* CMEK protects log files at rest on physical storage, but authorized users (such as those with `roles/cloudsql.admin` or direct Cloud Logging access) can still read the decrypted log content through the Cloud Logging API.
    *   *Why C is incorrect:* `roles/cloudsql.viewer` controls access to the Cloud SQL instance's configuration and metadata; it does not control access to Cloud Logging log entries, which are governed by Logging IAM roles.

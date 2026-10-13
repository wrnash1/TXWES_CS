# Quiz: Module 11 — Database Performance Tuning and Query Optimization

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis follows each question.

---

### Question 1

A Cloud SQL for PostgreSQL instance is experiencing high CPU utilization and slow query response times. The DBA needs to identify which specific SQL queries are consuming the most CPU without modifying application code or enabling `pg_stat_statements` manually. Which GCP-native tool provides this visibility directly from the Cloud Console?

- A) Cloud SQL Query Insights — continuously samples and aggregates queries by normalized text, ranked by CPU time and latency percentiles, without application changes
- B) Cloud Audit Logs — records all query executions with CPU consumption per statement
- C) Cloud SQL Auth Proxy metrics — provides per-query CPU and latency statistics from the proxy layer
- D) VPC Flow Logs — captures query execution metadata including CPU time and row counts

Correct Answer: A — Cloud SQL Query Insights is built into the Cloud SQL service and automatically samples database queries, aggregates them by normalized query text, and ranks them by CPU time, execution count, and latency percentiles. It requires no application code changes and no manual extension configuration.

Distractor analysis: B is incorrect because Cloud Audit Logs record administrative and data access events (who ran what, when) but do not provide CPU consumption, execution time, or per-query performance metrics. C is incorrect because the Cloud SQL Auth Proxy handles IAM authentication and TLS encryption; it does not collect query-level performance statistics. D is incorrect because VPC Flow Logs capture network packet metadata (source/destination IP, bytes, protocol) and have no visibility into database query execution.

---

### Question 2

A DBA runs `EXPLAIN ANALYZE` on a query against a Cloud SQL for PostgreSQL table with 50 million rows and receives the following output:

```
Seq Scan on orders  (cost=0.00..850000.00 rows=15 width=32)
                    (actual time=0.042..52341.201 ms rows=15 loops=1)
  Filter: (customer_id = 'C009812')
  Rows Removed by Filter: 49999985
```

What is the most appropriate corrective action?

- A) `CREATE INDEX idx_orders_customer ON orders(customer_id);` to convert the sequential scan to an index scan, reducing the query from 52 seconds to milliseconds
- B) Increase the Cloud SQL instance machine type to provide more CPU for the sequential scan
- C) Enable connection pooling with PgBouncer to reduce the overhead of this query's connection
- D) Run `VACUUM ANALYZE orders;` to update table statistics and help the planner choose a better scan type

Correct Answer: A — The execution plan shows a `Seq Scan` filtering 50 million rows to find 15 results. The database is reading every row. A B-tree index on `customer_id` converts this to an `Index Scan` that directly locates the 15 matching rows in O(log n) time, reducing execution time from 52 seconds to sub-millisecond.

Distractor analysis: B is incorrect because a larger instance makes the sequential scan run faster, but a full table scan on 50 million rows will always be orders of magnitude slower than an index scan regardless of CPU. The root cause is algorithmic, not hardware. C is incorrect because connection pooling reduces connection establishment overhead, not the execution time of individual queries. D is incorrect because `ANALYZE` updates statistics that affect cardinality estimates. However, the plan already shows accurate estimated rows (15) matching actual rows (15), so statistics are not stale. The problem is a missing index, not stale statistics.

---

### Question 3

A data engineering team needs a PostgreSQL index that supports full-text search queries against a `description` column in a `products` table. Queries use the `@@` operator and `to_tsvector()` for document matching. Which index type is correct?

- A) `CREATE INDEX idx_products_fts ON products USING GIN(to_tsvector('english', description));`
- B) `CREATE INDEX idx_products_fts ON products USING BTREE(description);`
- C) `CREATE INDEX idx_products_fts ON products USING BRIN(description);`
- D) `CREATE INDEX idx_products_fts ON products USING HASH(description);`

Correct Answer: A — GIN (Generalized Inverted Index) is the correct index type for full-text search in PostgreSQL. A GIN index on a `tsvector` expression stores an inverted index of all lexemes in the document, enabling efficient `@@` operator lookups. The B-tree cannot support `@@` operator queries on text vectors.

Distractor analysis: B is incorrect because a B-tree on the raw `description` text supports only equality and prefix `LIKE` comparisons. It cannot be used with `to_tsvector()` expressions or the `@@` full-text match operator. C is incorrect because BRIN indexes store min/max values per block range and are used for large append-only tables with values that correlate with physical row order. They do not support text search. D is incorrect because Hash indexes support only equality lookups on scalar values and cannot be applied to tsvector expressions or full-text search patterns.

---

### Question 4

An application connects to Cloud SQL for PostgreSQL and begins receiving `FATAL: sorry, too many clients already` errors during peak traffic. Cloud Monitoring shows active connections reaching 800 on a `db-n1-standard-2` instance. What is the most appropriate long-term solution?

- A) Deploy PgBouncer in transaction pooling mode to multiplex thousands of application connections over a smaller number of real database connections
- B) Upgrade the Cloud SQL instance to `db-n1-standard-8` to increase the maximum connection limit
- C) Enable Cloud SQL REGIONAL High Availability to distribute connections between primary and standby instances
- D) Add a Cloud SQL read replica to handle 50% of the incoming connections

Correct Answer: A — Connection pool exhaustion is caused by too many application threads holding open database connections simultaneously. PgBouncer in transaction pooling mode returns each database connection to the pool after every COMMIT or ROLLBACK, allowing thousands of application sessions to be served by a pool of 50–100 real database connections. This addresses the root cause and scales to any traffic volume.

Distractor analysis: B is incorrect because upgrading to a larger instance increases the connection limit temporarily, but as the application grows, it will hit the new limit. This is a short-term workaround, not a solution. Connection pooling addresses the architectural root cause. C is incorrect because Cloud SQL HA standby instances do not accept application connections; they only receive synchronous replication writes. Enabling HA does not increase available connection capacity. D is incorrect because read replicas can serve read-only SELECT queries but cannot serve write transactions. If the application runs write-heavy workloads during peak hours, a read replica does not reduce write connection pressure.

---

### Question 5

A developer runs the following `EXPLAIN ANALYZE` on a Cloud SQL for PostgreSQL table and observes a large discrepancy:

```
Index Scan using idx_orders_customer on orders
  (cost=0.43..18.52 rows=3 ...)
  (actual time=0.214..4832.112 ms rows=287543 loops=1)
```

The planner estimated 3 rows but the query returned 287,543 rows. What is the most likely cause and the correct fix?

- A) Table statistics are stale — the planner's row estimate is based on outdated data. Run `ANALYZE orders;` to refresh the statistics.
- B) The index on `customer_id` is corrupt — rebuild it with `REINDEX TABLE orders;`
- C) The connection pool is full — the query waited for a connection, inflating execution time
- D) The Cloud SQL instance needs more RAM to cache the index pages for this query

Correct Answer: A — The plan shows the planner estimated 3 rows but the query returned 287,543. This large discrepancy between estimated and actual row counts is the signature of stale table statistics. The planner chose an index scan (appropriate for 3 rows) when a sequential scan might have been more efficient for 287,543 rows. Running `ANALYZE orders;` updates the column statistics and allows the planner to make an accurate decision.

Distractor analysis: B is incorrect because a corrupt index would produce incorrect results or errors, not a row count mismatch between the plan's estimate and the actual result. C is incorrect because connection wait time would inflate overall response time but would not change the row count discrepancy between the planner estimate and actual rows. D is incorrect because insufficient RAM affects cache hit rates and I/O time but does not cause row count estimation errors in the plan.

---

### Question 6

A Cloud Spanner table uses a `BIGINT` auto-increment column as the primary key. The engineering team observes that write throughput is limited to a single Spanner node while other nodes process almost no writes. What is the root cause and the correct fix?

- A) Sequential integer primary keys cause all writes to go to the same Spanner split (the highest key range). Switch to UUID primary keys to distribute writes evenly across splits.
- B) The Spanner instance has too few nodes. Add more nodes to increase the number of splits available for write processing.
- C) Write transactions are not using mutations. Rewrite all writes to use Spanner mutations instead of DML statements.
- D) The table is missing a secondary index. Creating an index on the primary key column will distribute writes across nodes.

Correct Answer: A — Spanner distributes data across splits based on key range. A monotonically increasing integer primary key means all new rows have the highest key values and go to the same split. This creates a write hotspot on one node. Using UUID primary keys (randomly distributed) spreads new rows across all splits and all nodes, eliminating the hotspot.

Distractor analysis: B is incorrect because adding more nodes does not change the root cause: all writes still go to the split containing the highest key range. The hotspot persists regardless of node count. C is incorrect because the choice between mutations and DML affects performance characteristics in other ways but is not related to the key distribution hotspot problem. D is incorrect because a secondary index on the primary key would be redundant (the primary key is already indexed) and does not redistribute primary key write operations across nodes.

---

### Question 7

A BigQuery table is partitioned by `order_date`. A query analyst reports that a query with `WHERE order_status = 'shipped'` scans all 365 partitions despite only needing 30 days of data. What change eliminates the full partition scan?

- A) Add `AND order_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) AND CURRENT_DATE()` to the WHERE clause so BigQuery can prune partitions by the partition column
- B) Create a clustering on `order_status` to prevent the partition scan
- C) Increase the partition expiration to reduce the number of active partitions
- D) Switch to integer range partitioning on `order_status` to enable partition pruning on that column

Correct Answer: A — BigQuery partition pruning only works when the WHERE clause includes a filter on the partition column (`order_date`). Filtering only on `order_status` provides no information about which date partitions to skip, so BigQuery scans all 365. Adding a date range filter on `order_date` allows BigQuery to skip all but the 30 relevant partitions.

Distractor analysis: B is incorrect because clustering improves block-level pruning within each partition but does not prevent BigQuery from opening all partitions when there is no partition column filter. C is incorrect because reducing the number of active partitions by setting expiration only removes old partitions but does not change the behavior for current data — all remaining partitions are still scanned without a partition column filter. D is incorrect because `order_status` is a string (not an integer range), and even if you could partition by status, the query is already filtering on status — the problem is the absence of a date range filter on the existing partition column.

---

### Question 8

A data engineer needs to identify the 10 most expensive BigQuery queries by bytes processed in the past 24 hours across their project. Which resource provides this information?

- A) `INFORMATION_SCHEMA.JOBS_BY_PROJECT` — a BigQuery system view that records every query job including bytes processed, elapsed time, and query text
- B) Cloud Audit Logs — the Data Access audit logs record bytes processed per BigQuery query
- C) Cloud Monitoring — the BigQuery bytes processed metric aggregates query costs in Cloud Monitoring dashboards
- D) BigQuery Query Insights — the equivalent of Cloud SQL Query Insights for BigQuery, showing per-query bytes processed

Correct Answer: A — `INFORMATION_SCHEMA.JOBS_BY_PROJECT` is a BigQuery system view that contains one row per query job. It includes `total_bytes_processed`, `elapsed_ms`, `query`, `creation_time`, `user_email`, and `error_result`. Querying this view with `ORDER BY total_bytes_processed DESC LIMIT 10` identifies the most expensive queries. It is available in the `region-us` or applicable multi-region dataset.

Distractor analysis: B is incorrect because Cloud Audit Logs for BigQuery record Data Access events (who queried what table, when) in a structured log format, but they do not expose bytes processed as a structured queryable field in the same way `INFORMATION_SCHEMA` does. While bytes_billed may appear in log payloads, `INFORMATION_SCHEMA` is the purpose-built tool for job analysis. C is incorrect because Cloud Monitoring's BigQuery metrics show aggregated bytes processed at the project or dataset level over time, not per-query breakdown with query text. D is incorrect because BigQuery does not have a feature called "BigQuery Query Insights" equivalent to Cloud SQL Query Insights; `INFORMATION_SCHEMA.JOBS_BY_PROJECT` is the correct tool for BigQuery job analysis.

---

### Question 9

An application generates the following query pattern 500 times per second. Each execution queries a separate customer record, resulting in 500 individual database round trips per second for a single page load:

```python
for customer_id in customer_list:
    result = db.execute("SELECT name, email FROM customers WHERE id = %s", customer_id)
```

Which query optimization eliminates the excessive round trips?

- A) Rewrite as a single query using `WHERE id = ANY(%s)` with the entire list, or use a JOIN to retrieve all customer records in one round trip
- B) Create a B-tree index on `customers.id` to reduce the execution time of each individual lookup
- C) Enable Cloud SQL Query Insights to identify and cache the repeated queries
- D) Deploy a read replica to distribute the 500 queries across two database instances

Correct Answer: A — This is the N+1 query problem. The application executes N separate queries for N records instead of one query returning all N records. Rewriting with `WHERE id = ANY(:ids_array)` or a JOIN consolidates all lookups into a single round trip, reducing network latency overhead by a factor of N. Each database round trip has fixed overhead (network RTT + connection handshake cost) that accumulates at 500 iterations.

Distractor analysis: B is incorrect because creating an index on `id` (which is likely already the primary key and indexed) reduces the per-query execution time but does not reduce the number of round trips. With 500 round trips, the dominant overhead is network latency, not per-query execution time. C is incorrect because Query Insights is a monitoring and diagnostic tool; it does not cache queries or modify query execution behavior. D is incorrect because distributing 500 queries across two instances still results in 500 round trips — 250 to each. The total database work is unchanged; the fundamental problem is N round trips replacing 1.

---

### Question 10

A PostgreSQL DBA notices that the `EXPLAIN ANALYZE` plan for a query shows a `Sort` node with the annotation `(Batches: 4 Memory Used: 4096kB Disk: 8192kB)`. What does this indicate and what is the appropriate response?

- A) The sort operation spilled to disk because the available `work_mem` is insufficient to hold the sort in memory. Increase `work_mem` for the session or instance to allow the sort to complete entirely in RAM.
- B) The sort is using 4 parallel worker processes. Reduce `max_parallel_workers_per_gather` to prevent excessive parallelism.
- C) The sort is reading from 4 BRIN index block ranges. Switch to a B-tree index to eliminate the disk access.
- D) The sort is batching data from 4 partitions. Re-partition the table with fewer partitions to consolidate the sort.

Correct Answer: A — When a Sort node shows `Disk: N kB`, the sort exceeded the available `work_mem` allocation and spilled the overflow data to temporary disk files. Disk sorts are orders of magnitude slower than in-memory sorts. The fix is to increase `work_mem` — either at the session level (`SET work_mem = '64MB'`) or at the instance level in the Cloud SQL flags configuration for queries that routinely sort large datasets.

Distractor analysis: B is incorrect because parallel workers are shown in the plan with `Workers Planned` and `Workers Launched` annotations, not the Batches/Memory/Disk annotation on Sort nodes. The Batches value refers to sort passes over the data, not parallel workers. C is incorrect because BRIN block ranges are shown in Index Scan nodes accessing a BRIN index, not in Sort nodes. The Sort node annotation describes memory usage during the sort operation. D is incorrect because partition count affects which partitions are accessed during scans, not how the sort node manages memory for its sorting operation.

---

Reference: cloud.google.com/learn

---

### Question 11 (5 points)

A developer proposes the following index to support a query that filters on `status = 'active'` and sorts by `last_login DESC` on a `users` table with 20 million rows:

```sql
CREATE INDEX idx_users_active_login ON users (last_login DESC) WHERE status = 'active';
```

What are the two benefits of this partial index compared to a full index on `(status, last_login)`?

A) It is smaller (only indexes active users) and the planner can skip the status filter evaluation since it is encoded in the index predicate.
B) It is faster to create and uses less CPU during query execution.
C) It prevents duplicate `last_login` values and enforces referential integrity.
D) It supports queries on all status values, not just active users.

**Correct Answer:** A

**Distractor Analysis:**

- B) Creation speed depends on data volume and server resources; a partial index may create faster only because it indexes fewer rows, which is a consequence of being smaller, not a separate benefit. CPU savings are a result of fewer rows, already captured in option A.
- C) Partial indexes do not enforce uniqueness unless the UNIQUE keyword is included; this index has no uniqueness constraint, and partial indexes are entirely unrelated to referential integrity.
- D) A partial index with `WHERE status = 'active'` only covers rows where status is active; it cannot be used for queries that need users with other status values, which is the opposite of this option's claim.

---

### Question 12 (5 points)

Cloud SQL Query Insights shows that a normalized query `SELECT * FROM orders WHERE customer_id = $1` has a P99 latency of 4.2 seconds and accounts for 38% of total CPU. The `EXPLAIN ANALYZE` shows an Index Scan on `customer_id`. What is the most likely next diagnostic step?

A) Check the average rows returned per execution in Query Insights; if the index scan returns hundreds of thousands of rows per call, the query may need a more selective filter or result caching.
B) Drop the index on `customer_id` and add a GIN index instead.
C) Increase `max_connections` to allow more parallel executions of this query.
D) Disable the Index Scan by setting `enable_indexscan = off` to force a sequential scan.

**Correct Answer:** A

**Distractor Analysis:**

- B) GIN indexes are for JSONB, array, and full-text types; `customer_id` is a scalar identifier where a B-tree index is correct. Replacing it with GIN would be unsupported or less efficient.
- C) High latency on a single query indicates the query itself is slow, not that there are insufficient connections to run it; adding connections does not make individual query executions faster.
- D) Disabling the Index Scan forces a sequential scan which would be slower for a selective query; the goal of diagnostics is to understand and fix the root cause, not to artificially worsen the plan.

---

### Question 13 (5 points)

What is the primary advantage of Cloud Spanner's `STORING` clause in a secondary index definition?

A) It stores copies of specified non-key columns in the index so queries can be satisfied from the index without accessing the base table, similar to a covering index in PostgreSQL.
B) It compresses the indexed column values to reduce storage cost.
C) It stores the index in a separate region for geographic distribution.
D) It forces the index to use strongly consistent reads instead of bounded stale reads.

**Correct Answer:** A

**Distractor Analysis:**

- B) `STORING` adds columns to the index for query coverage; it does not apply compression to column values and does not reduce individual column storage size.
- C) Spanner replicates all data (including indexes) across regions based on the instance configuration; `STORING` has no effect on geographic placement.
- D) Read consistency in Spanner is controlled by the read type (strong vs stale) at query time, not by index definition attributes like `STORING`.

---

### Question 14 (5 points)

A BigQuery analyst writes the following query and is surprised to find it scans the entire `events` table despite date partitioning:

```sql
SELECT event_type, COUNT(*)
FROM events
WHERE DATE(event_timestamp) = '2025-03-15'
GROUP BY event_type;
```

What change enables partition pruning?

A) Replace `DATE(event_timestamp) = '2025-03-15'` with `event_timestamp >= '2025-03-15' AND event_timestamp < '2025-03-16'` so BigQuery can evaluate the partition filter without a function call.
B) Add a clustering key on `event_type` to reduce the scan.
C) Add a `LIMIT 1000` clause to prevent full table scans.
D) Convert the table from date partitioning to integer range partitioning.

**Correct Answer:** A

**Distractor Analysis:**

- B) Clustering improves block-level pruning within partitions but does not help BigQuery determine which partitions to skip; partition pruning requires a filter on the partition column without a wrapping function.
- C) `LIMIT` restricts result rows but does not affect which partitions BigQuery opens and scans to find those rows; it does not enable partition pruning.
- D) Switching to integer range partitioning would require a schema redesign and is unnecessary; the existing date partitioning works correctly when the filter does not wrap the column in a function.

---

### Question 15 (5 points)

A Cloud SQL for PostgreSQL instance has `autovacuum_vacuum_scale_factor = 0.2` (default). A table with 10 million rows accumulates 2 million dead tuples. Will autovacuum trigger on this table?

A) Yes — 2 million dead tuples is 20% of 10 million rows, which equals the 0.2 threshold, triggering autovacuum.
B) No — autovacuum only triggers when dead tuples exceed 50% of the table.
C) No — autovacuum is disabled by default on Cloud SQL instances.
D) Yes — autovacuum always triggers every 5 minutes regardless of the threshold.

**Correct Answer:** A

**Distractor Analysis:**

- B) The default threshold is `autovacuum_vacuum_scale_factor = 0.2`, meaning 20% of live rows; 50% is not the threshold.
- C) Autovacuum is enabled by default on Cloud SQL for PostgreSQL; it runs as a background process and is the primary mechanism for dead tuple reclamation.
- D) Autovacuum is threshold-driven, not time-driven; it triggers when dead tuple count exceeds `autovacuum_vacuum_threshold + autovacuum_vacuum_scale_factor * reltuples`, not on a fixed interval.

---

### Question 16 (5 points)

A PostgreSQL query uses `LIKE '%invoice%'` to search a `description` column. The DBA adds a standard B-tree index on `description`. EXPLAIN ANALYZE still shows a Seq Scan. Why?

A) B-tree indexes cannot support leading-wildcard LIKE patterns (`%text`); only a GIN index with `pg_trgm` trigram tokenization can accelerate this search pattern.
B) The index was created CONCURRENTLY and is not yet available.
C) The `description` column must be cast to `tsvector` before a B-tree index applies.
D) LIKE patterns require a Hash index, not a B-tree.

**Correct Answer:** A

**Distractor Analysis:**

- B) `CREATE INDEX CONCURRENTLY` completes before returning to the prompt (it is not asynchronous in the background); once the command returns, the index is available.
- C) Casting to `tsvector` enables full-text search with GIN, not B-tree; full-text `@@` and `LIKE '%text%'` are different search mechanisms and neither uses B-tree for leading-wildcard patterns.
- D) Hash indexes support only equality (`=`) comparisons; they cannot support any form of LIKE pattern matching, including leading-wildcard patterns.

---

### Question 17 (5 points)

Which PgBouncer pooling mode should be used for an OLTP application that uses PostgreSQL features requiring session-level state, such as `SET` variables, prepared statements, and advisory locks?

A) Session pooling — one real database connection is held for the entire client session duration, preserving all session-level state.
B) Transaction pooling — the connection is returned after each transaction, making it incompatible with session-level state.
C) Statement pooling — each individual SQL statement gets a different connection, destroying all session context.
D) Connection pooling — a proprietary PgBouncer mode that caches session state across connections.

**Correct Answer:** A

**Distractor Analysis:**

- B) Transaction pooling is the highest-concurrency mode but breaks session-level features like `SET` variables, prepared statements, and advisory locks because the connection changes between transactions.
- C) Statement pooling reassigns the connection after every single statement, making it incompatible with any multi-statement operation; it is rarely used in production for this reason.
- D) "Connection pooling" is not a distinct PgBouncer mode name; the three PgBouncer modes are session, transaction, and statement.

---

### Question 18 (5 points)

A DBA runs `VACUUM VERBOSE orders;` and the output includes `index vacuumed: 0 pages removed`. What does this most likely indicate?

A) No dead index tuples were found in the index pages; the index is clean and no index page compaction was needed.
B) The index was dropped before VACUUM ran.
C) VACUUM cannot process indexes; a separate `REINDEX` is always required.
D) The `orders` table has no indexes defined.

**Correct Answer:** A

**Distractor Analysis:**

- B) If an index were dropped, the index would simply not appear in the VACUUM output at all; reporting `0 pages removed` specifically means the index was scanned and found no dead entries requiring removal.
- C) `VACUUM` does process indexes as part of its normal operation; it scans index pages to identify and remove dead index entries pointing to dead heap tuples.
- D) If the table had no indexes, the index vacuum section of the VERBOSE output would be absent entirely, not show `0 pages removed`.

---

### Question 19 (5 points)

A Cloud SQL for PostgreSQL query reads 500,000 rows, aggregates them, and returns 20 rows. `pg_stat_statements` shows `shared_blks_hit = 480000` and `shared_blks_read = 20000`. What does this cache ratio indicate?

A) A 96% buffer cache hit rate — most data is being served from `shared_buffers` in memory, which is healthy and indicates the working set fits in cache.
B) A 96% miss rate — the buffer pool is too small and most data is being read from disk.
C) The table is fragmented; 20,000 blocks were skipped during the scan.
D) The query is consuming 96% of available shared memory.

**Correct Answer:** A

**Distractor Analysis:**

- B) `shared_blks_hit` counts buffer pool hits (found in memory), and `shared_blks_read` counts physical disk reads (not in cache); 480,000 hits vs 20,000 disk reads = 96% hit rate, which is healthy, not a miss rate.
- C) `shared_blks_read` represents physical I/O operations (reads from disk), not skipped blocks; PostgreSQL does not skip heap blocks during sequential scans.
- D) `shared_blks_hit` measures hit count in blocks, not percentage of shared memory consumption; shared memory consumption is measured in bytes via `pg_buffercache` or instance memory metrics.

---

### Question 20 (5 points)

A DBA needs to find the queries with the highest ratio of total time to calls in `pg_stat_statements`, identifying candidates for optimization by mean execution time. Which query correctly identifies the top 5?

A) `SELECT query, mean_exec_time FROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT 5;`
B) `SELECT query, total_exec_time FROM pg_stat_statements ORDER BY calls ASC LIMIT 5;`
C) `SELECT query, calls FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 5;`
D) `SELECT query FROM pg_stat_statements WHERE calls > 1000 ORDER BY rows DESC LIMIT 5;`

**Correct Answer:** A

**Distractor Analysis:**

- B) Ordering by `calls ASC` finds the least-executed queries, not the slowest per execution; `total_exec_time` without dividing by calls mixes high-frequency fast queries with low-frequency slow ones.
- C) Ordering by `total_exec_time DESC` finds the queries with the highest cumulative time, which may simply be high-frequency cheap queries; it does not isolate queries that are individually slow.
- D) Filtering by `calls > 1000` and ordering by `rows` identifies high-row-returning queries, not slow queries by mean execution time; rows returned does not measure latency.

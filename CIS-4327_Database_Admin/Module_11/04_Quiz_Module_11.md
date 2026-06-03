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

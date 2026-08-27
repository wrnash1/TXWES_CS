# Quiz: Module 12 — BigQuery for Analytics

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis follows each question.

---

### Question 1

A data engineer notices that a BigQuery query scanning a 10 TB table takes the same amount of time regardless of how many rows match the WHERE clause. Which architectural feature of BigQuery best explains this behavior?

- A) BigQuery uses B-tree indexes that are not selective enough at this scale to narrow the scan
- B) Dremel distributes the scan across thousands of leaf nodes in parallel, so scan time is bounded by the parallelism level, not the result set size
- C) BigQuery caches query results for 24 hours, masking true execution time for repeated queries
- D) The table is not partitioned, so BigQuery must scan all storage blocks regardless of the filter

Correct Answer: B — Dremel's multi-level serving tree dispatches the scan to thousands of leaf nodes simultaneously. Each leaf node reads a small slice of columnar data. Because the work is parallelized across many nodes, scan time is primarily bounded by the degree of parallelism and the volume of data read — not by how many rows ultimately match the WHERE filter. Result set size has minimal effect on total scan duration.

Distractor analysis: A is incorrect because BigQuery does not use B-tree indexes; it uses columnar storage with partition and clustering pruning for selective access. B-tree index selectivity is a concept from row-based OLTP databases. C is incorrect because BigQuery does cache identical query results for approximately 24 hours, but the question states the behavior is observed across different result sizes, not identical queries. D is incorrect because while lack of partitioning does cause full table scans and is a problem for cost, it is not the architectural explanation for why scan time is independent of result size.

---

### Question 2

A 50 TB `orders` table is partitioned by `order_date`. A business analyst runs the following query daily without any date filter:

```sql
SELECT customer_id, SUM(revenue)
FROM orders
GROUP BY customer_id;
```

The query is too slow and too expensive. Which single change provides the greatest cost and performance improvement?

- A) Add `customer_id` as a cluster column to the table so BigQuery can prune blocks within partitions
- B) Require the analyst to always include a `WHERE order_date` filter so partition pruning eliminates irrelevant partitions
- C) Convert the table to an external table stored in Cloud Storage to reduce BigQuery storage costs
- D) Create a view that pre-filters orders for the current year and direct the analyst to query the view

Correct Answer: B — Without a filter on the partition column (`order_date`), BigQuery scans all 50 TB regardless of how the table is partitioned. Adding a date filter enables partition pruning, which eliminates irrelevant partitions from the scan. For a query that only needs recent data, this can reduce bytes scanned by 90% or more — the most impactful single change available.

Distractor analysis: A is incorrect because clustering improves block-level pruning within partitions, but it does not prevent BigQuery from opening all partitions when no partition column filter is present. The full partition scan still occurs; clustering reduces work within each opened partition. C is incorrect because converting to an external table removes data from BigQuery-managed storage but does not change how queries are executed or how much data is scanned. D is incorrect because a view that pre-filters for the current year is a partial workaround, but it hardcodes the time window and does not solve the fundamental issue of requiring a partition filter in the query.

---

### Question 3

A view in dataset `analytics` needs to read from a table in dataset `hr_data`. The company's security policy prohibits granting the view's users direct access to `hr_data` tables. Which BigQuery feature allows the view to access `hr_data` without exposing it to end users?

- A) A materialized view with cross-dataset refresh configured to cache `hr_data` table contents
- B) An authorized view configured in the `hr_data` dataset settings, which grants the specific view access to read from `hr_data` without passing that access to the view's users
- C) A BigQuery Data Transfer Service scheduled query that copies `hr_data` to `analytics` nightly
- D) A federated query using a Cloud SQL connection that bypasses BigQuery dataset IAM controls

Correct Answer: B — An authorized view is a view that is explicitly listed in the source dataset's access control settings. BigQuery grants the view permission to read from that dataset, but the view's users do not inherit that access — they can only see what the view exposes. This enables row-level and column-level filtering of sensitive data while making aggregate or anonymized data available to analysts.

Distractor analysis: A is incorrect because a materialized view caches query results and refreshes them on a schedule, but the access control mechanism for cross-dataset reads is still the authorized view pattern; materialized views do not add a separate access-control capability. C is incorrect because copying `hr_data` to `analytics` creates a data copy and introduces a sync delay; it is operationally costly and does not use BigQuery's native access control mechanism. D is incorrect because federated queries read from external sources (Cloud SQL, Sheets) at query time; they do not provide a mechanism for managing intra-BigQuery dataset access controls.

---

### Question 4

A developer accidentally deleted 500,000 rows from a BigQuery table at 2:00 PM. A table snapshot was created at 8:00 AM. It is now 3:00 PM. What is the most efficient recovery approach?

- A) Restore from the most recent Cloud Storage export of the table, accepting data loss since the export was created
- B) Query the table using `FOR SYSTEM_TIME AS OF` at a timestamp before 2:00 PM to retrieve the deleted rows, then re-insert them into the table
- C) Contact Google Cloud Support to restore the table from Google's internal backups
- D) Use BigQuery Data Transfer Service to reload data from the 8:00 AM snapshot

Correct Answer: B — BigQuery time travel retains table data for up to 7 days. Since the deletion occurred 1 hour ago, the data is within the time travel window. `FOR SYSTEM_TIME AS OF` queries the table at its pre-deletion state. The recovered rows can then be inserted back into the current table with a `INSERT INTO ... SELECT` from the time travel query. This is faster and more precise than restoring from a snapshot or export.

Distractor analysis: A is incorrect because restoring from a Cloud Storage export loses all data written since the export was created. Since the export predates the deletion, this is unnecessary when time travel can recover the exact rows that were deleted. C is incorrect because contacting Google support is necessary only during the fail-safe window (7–14 days after deletion) when self-service time travel has expired; it is not required or appropriate 1 hour after deletion. D is incorrect because Data Transfer Service is for scheduled data ingestion pipelines from external sources, not for point-in-time recovery within BigQuery.

---

### Question 5

A team is designing a BigQuery table for a streaming IoT sensor dataset. Each sensor emits readings every second. Queries almost always filter on `reading_date` with a date range and on `sensor_id` with an equality condition. The table will grow to trillions of rows. What is the optimal table design?

- A) Partition by `sensor_id`, cluster by `reading_date` — sensor_id is the primary filter column
- B) Partition by `reading_date`, cluster by `sensor_id` — date range filters enable partition pruning and sensor_id equality filters benefit from clustering
- C) No partitioning; use a materialized view for each sensor to pre-aggregate readings
- D) Partition by ingestion time only; `sensor_id` has too high a cardinality to cluster

Correct Answer: B — Partitioning by `reading_date` aligns with the date range filters in most queries, enabling partition pruning to skip irrelevant time ranges. Clustering by `sensor_id` co-locates rows for the same sensor within each partition, so filtering by `sensor_id = 'S001'` only reads relevant blocks within the selected date partitions. This combination is the standard BigQuery design pattern for time-series IoT data.

Distractor analysis: A is incorrect because partitioning by `sensor_id` would create millions of partitions (one per sensor), far exceeding the 4,000-partition limit and making partition management unworkable. BigQuery partitioning is designed for low-cardinality time or range keys, not high-cardinality IDs. C is incorrect because pre-aggregating in materialized views eliminates the ability to query raw readings for anomaly detection or detailed analysis; and maintaining thousands of per-sensor materialized views is operationally impractical. D is incorrect because clustering supports up to 4 columns and works effectively with high-cardinality columns like `sensor_id`; high cardinality is expected and appropriate for a cluster column.

---

### Question 6

A company runs BigQuery analytics with a consistent daily query volume of approximately 800 TB scanned. At the on-demand pricing rate of $6.25 per TB, what is the approximate monthly cost?

- A) $5,000 per month
- B) $150,000 per month
- C) $1,500,000 per month
- D) $50,000 per month

Correct Answer: B — 800 TB/day × 30 days = 24,000 TB per month. 24,000 TB × $6.25/TB = $150,000 per month. At this volume, the team should evaluate BigQuery flat-rate capacity pricing (slot reservations), which charges a fixed monthly fee for committed compute capacity rather than per-byte scanned.

Distractor analysis: A is incorrect because $5,000 would correspond to only 800 TB/month (one day's worth), not 30 days. C is incorrect because $1,500,000 would correspond to 240,000 TB scanned per month — 10× the stated volume. D is incorrect because $50,000 would correspond to 8,000 TB per month, which is approximately 10 days of the stated daily volume rather than 30.

---

### Question 7

Which BigQuery SQL statement removes all rows from a table without dropping the table's schema, and does not support a WHERE clause to filter which rows are removed?

- A) `DELETE FROM table WHERE 1=1` — removes all rows via DML with a constant-true filter
- B) `DROP TABLE table; CREATE TABLE table (...)` — drops and recreates the table
- C) `TRUNCATE TABLE table` — removes all rows, preserves schema, accepts no WHERE clause
- D) `UPDATE table SET all_columns = NULL WHERE TRUE` — nullifies all values rather than removing rows

Correct Answer: C — `TRUNCATE TABLE` in BigQuery removes all rows from a table and preserves the table schema. It does not accept a WHERE clause — it always removes all rows. It is atomic and faster than a `DELETE` with a constant-true filter because it does not go through DML row-by-row processing.

Distractor analysis: A is incorrect because `DELETE FROM table WHERE 1=1` is a valid BigQuery DML statement that does delete all rows, but it accepts a WHERE clause (just happens to use a condition that matches all rows). The question asks for a statement that does not support a WHERE clause. B is incorrect because dropping and recreating the table would lose all metadata, permissions, and potentially cause naming conflicts; it is not a standard "truncate" operation and `TRUNCATE TABLE` is preferable. D is incorrect because `UPDATE SET column = NULL` leaves the rows in the table with null values rather than removing them, which is a different operation entirely.

---

### Question 8

A materialized view is defined as:

```sql
CREATE MATERIALIZED VIEW mv_daily_sales AS
SELECT sale_date, region, SUM(amount) AS total
FROM sales
GROUP BY sale_date, region;
```

A user runs the following query directly against the base table:

```sql
SELECT region, SUM(amount) FROM sales
WHERE sale_date = '2025-06-01'
GROUP BY region;
```

What will BigQuery's optimizer do?

- A) Ignore the materialized view because the user did not explicitly reference it in their query
- B) Automatically rewrite the query to read from `mv_daily_sales` instead of `sales` if it determines the materialized view can satisfy the query more efficiently
- C) Return an error because the materialized view and the base table cannot coexist in the same dataset
- D) Require the user to explicitly reference `mv_daily_sales` in their SQL before the optimization takes effect

Correct Answer: B — BigQuery supports smart tuning: the query optimizer can automatically rewrite queries against base tables to instead read from a materialized view when the view's precomputed results can satisfy the query. The user does not need to modify their query. For this example, the query filters on `sale_date = '2025-06-01'` and groups by `region` — which matches the materialized view's `(sale_date, region)` grouping. BigQuery reads the view's cached result rather than reprocessing all rows in `sales`.

Distractor analysis: A is incorrect because BigQuery's smart tuning explicitly looks for opportunities to serve queries from materialized views even when the user's query references the base table directly. D is incorrect because automatic smart tuning does not require the user to reference the materialized view; the optimizer handles the rewrite transparently. C is incorrect because BigQuery fully supports materialized views coexisting with their base tables in the same or different datasets; the materialized view is a dependent object on the base table, not a replacement.

---

### Question 9

An organization wants to prevent runaway BigQuery costs from analysts running queries that accidentally scan an entire 500-partition table. Which table option enforces that every query must include a partition column filter at query submission time, returning an error for queries without one?

- A) `OPTIONS (max_staleness = INTERVAL '1' DAY)` — limits how stale the query results can be
- B) `OPTIONS (partition_expiration_days = 365)` — automatically expires partitions after one year
- C) `OPTIONS (require_partition_filter = true)` — causes BigQuery to reject queries that do not include a filter on the partition column
- D) `OPTIONS (clustering_fields = ['partition_date'])` — adds clustering on the partition date column

Correct Answer: C — `require_partition_filter = true` is a table-level option that causes BigQuery to return an error if a query does not include a filter on the partition column. This prevents accidental full-table scans and the associated cost on large partitioned tables. The error message explicitly tells the user to add a partition filter.

Distractor analysis: A is incorrect because `max_staleness` is used with materialized views to control how stale the cached results can be before the view reads fresh data; it does not affect whether queries against the base table require a partition filter. B is incorrect because `partition_expiration_days` controls automatic deletion of old partitions after a defined retention period; it does not enforce query-time filter requirements. D is incorrect because clustering improves block-level pruning within partitions but does not prevent full partition scans; adding clustering does not reject queries that lack a partition filter.

---

### Question 10

A team migrates from BigQuery on-demand pricing to flat-rate capacity pricing. They purchase 2,000 slots and create two reservations: 1,500 slots for production workloads and 500 slots for development. A runaway development query attempts to consume all available compute. What happens to production queries?

- A) Production queries are queued behind the development query until it completes or is cancelled
- B) BigQuery automatically cancels the development query after 60 seconds of excess resource usage
- C) Production queries continue running against their 1,500-slot reservation, isolated from the development workload
- D) All 2,000 slots are shared equally across all workloads using round-robin scheduling regardless of reservations

Correct Answer: C — BigQuery slot reservations create isolated compute pools. Assignments attach projects or folders to a specific reservation. The production reservation's 1,500 slots are fully isolated from the development reservation's 500 slots. A runaway query in development cannot consume production slots because workloads only use the slots from their assigned reservation.

Distractor analysis: A is incorrect because slot reservations prevent the development workload from affecting production — production queries are not queued behind development work. Queueing only occurs within the same reservation when its slot limit is reached. B is incorrect because BigQuery does not automatically cancel queries after 60 seconds of high resource usage; long-running queries continue unless cancelled manually or a timeout is set via query labels or scripts. D is incorrect because round-robin scheduling among all workloads would eliminate the isolation benefit of reservations; the entire point of reservations is to guarantee dedicated compute capacity per workload.

---

Reference: cloud.google.com/learn

---

### Question 11 (5 points)

A BigQuery table with 800 billion rows is clustered by `country_code` and `product_category`. A query filters on `WHERE product_category = 'Electronics'` but does NOT filter on `country_code`. Will BigQuery use the clustering to prune blocks?

A) No — clustering pruning requires a filter on the first cluster column (`country_code`) before the second cluster column can be used.
B) Yes — BigQuery can use clustering pruning on any cluster column regardless of order when using equality filters.
C) No — clustering only works when the table is also partitioned; without a partition filter, clustering is ignored.
D) Yes — BigQuery always reads only one cluster block per query regardless of filter order.

**Correct Answer:** A

**Distractor Analysis:**

- B) BigQuery clustering follows a prefix-based pruning model similar to composite B-tree indexes; skipping the first cluster column (`country_code`) means BigQuery cannot use the clustering sort order to skip blocks for `product_category` alone.
- C) Clustering can be applied to non-partitioned tables and still provides block-level pruning within the table; lack of partitioning does not disable clustering, though the combination of both is recommended for large tables.
- D) Cluster block pruning is not limited to one block; the optimizer skips blocks whose metadata indicates they cannot contain matching rows, but this is based on the sort order of cluster columns, not a fixed count.

---

### Question 12 (5 points)

A BigQuery table has `partition_expiration_days = 180`. A row was inserted on January 1, 2025. What happens to that partition on July 1, 2025 (180 days later)?

A) The partition is automatically deleted by BigQuery, removing all rows in that partition permanently.
B) The partition is moved to a cold storage tier but remains queryable at higher cost.
C) BigQuery issues an alert but takes no automatic action; a manual `DELETE` is required.
D) The partition is archived to Cloud Storage automatically.

**Correct Answer:** A

**Distractor Analysis:**

- B) BigQuery does not have a tiered "cold storage" concept for partitions; `partition_expiration_days` causes permanent deletion, not archival to a cheaper storage class.
- C) BigQuery partition expiration is fully automatic; no manual intervention or alerting is involved — the partition is deleted without warning.
- D) BigQuery does not automatically export expired partitions to Cloud Storage; if data must be retained beyond the expiration window, it must be exported manually before expiration.

---

### Question 13 (5 points)

Which BigQuery feature allows a query against a base table to transparently read pre-aggregated results from a materialized view, reducing bytes scanned without any change to the query text?

A) Authorized views
B) Smart tuning (automatic query rewriting)
C) Slot reservations
D) BI Engine acceleration

**Correct Answer:** B

**Distractor Analysis:**

- A) Authorized views control cross-dataset access permissions; they do not rewrite queries to read from materialized views or reduce bytes scanned.
- C) Slot reservations allocate dedicated compute capacity; they affect query throughput and isolation but do not rewrite query plans to use materialized views.
- D) BI Engine provides in-memory acceleration for dashboarding tools by caching data, but it is separate from the smart tuning optimizer that rewrites queries to read from materialized views.

---

### Question 14 (5 points)

A data engineer runs the following BigQuery query to check cost before executing:

```sql
SELECT * FROM dataset.events WHERE event_date = '2025-06-01'
```

Which method allows them to estimate bytes scanned without actually running the query?

A) Run the query with `SELECT COUNT(*)` instead and multiply by average row size.
B) Use the BigQuery query validator in the Cloud Console or `bq query --dry_run` to get a bytes estimate without executing.
C) Check `INFORMATION_SCHEMA.TABLES` for the total table size and divide by partition count.
D) Enable `require_partition_filter` and catch the error message which includes a cost estimate.

**Correct Answer:** B

**Distractor Analysis:**

- A) Running `COUNT(*)` still executes a query and incurs cost; it also does not directly translate to bytes scanned for the filtered query.
- C) `INFORMATION_SCHEMA.TABLES` reports total table size, not the bytes that would be scanned for a specific filtered query; dividing by partition count is an approximation, not the actual estimate.
- D) `require_partition_filter` returns an error for queries without a partition filter; the error message does not include a cost estimate and `SELECT *` with the date filter already satisfies the partition filter requirement.

---

### Question 15 (5 points)

A company ingests streaming data into BigQuery using the Storage Write API. They need to ensure that exactly-once semantics are maintained — duplicate records must not appear even if the pipeline retries failed writes. Which Storage Write API mode provides this guarantee?

A) Default stream (best-effort delivery with possible duplicates on retry)
B) Committed stream (immediate visibility, no exactly-once guarantee)
C) Buffered stream (staged writes, no exactly-once guarantee)
D) Exclusive stream with `offset`-based row deduplication (exactly-once via offset tracking)

**Correct Answer:** D

**Distractor Analysis:**

- A) The default stream uses best-effort delivery and does not deduplicate retries; it is suitable for use cases where occasional duplicates are acceptable.
- B) The committed stream makes rows immediately visible after each write but does not provide exactly-once semantics; retrying a failed write can produce duplicates.
- C) The buffered stream stages rows for batch commit but also lacks the offset-based tracking needed for exactly-once guarantees.

---

### Question 16 (5 points)

A BigQuery user runs a query that joins two very large tables. The query returns the correct results but scans 4 TB more than expected. INFORMATION_SCHEMA shows no partition pruning occurred on the second table. What is the most likely cause?

A) The join key column in the second table is not the partition column, so no partition pruning applies to the join probe side.
B) The second table is clustered but not partitioned, so all blocks are scanned.
C) BigQuery disabled partition pruning for joins as a cost control measure.
D) The second table's partition filter was applied after the join, causing a full scan.

**Correct Answer:** A

**Distractor Analysis:**

- B) A clustered-only table still benefits from clustering-based block pruning on filter columns; however, if no filter matches the cluster columns, a full scan occurs — this is a plausible but secondary cause compared to the more precise explanation that the join key is not the partition key.
- C) BigQuery does apply partition pruning to join operations when the join condition or WHERE clause includes the partition column; there is no feature that disables pruning for joins.
- D) Partition pruning in BigQuery is evaluated at query planning time based on filters visible to the optimizer; filters in WHERE clauses are pushed down before scanning, not applied after joins.

---

### Question 17 (5 points)

An analyst needs to recover a BigQuery table to its state at exactly 6:00 AM today after a batch job accidentally overwrote rows at 7:00 AM. It is currently 9:00 AM. Which SQL statement restores the table?

A) `CREATE OR REPLACE TABLE dataset.orders AS SELECT * FROM dataset.orders FOR SYSTEM_TIME AS OF TIMESTAMP('2025-06-01 06:00:00 UTC');`
B) `RESTORE TABLE dataset.orders TO TIMESTAMP '2025-06-01 06:00:00';`
C) `ROLLBACK TABLE dataset.orders;`
D) `UNDROP TABLE dataset.orders;`

**Correct Answer:** A

**Distractor Analysis:**

- B) `RESTORE TABLE` is not a valid BigQuery SQL command; point-in-time recovery is performed with `FOR SYSTEM_TIME AS OF` inside a `CREATE OR REPLACE TABLE ... AS SELECT` statement.
- C) `ROLLBACK TABLE` does not exist in BigQuery SQL; BigQuery does not support multi-statement transactions with rollback at the table level in standard DML.
- D) `UNDROP TABLE` is a Snowflake-specific command; BigQuery does not have this syntax. Recovering a dropped table in BigQuery requires time travel before the table is fully expired.

---

### Question 18 (5 points)

A data warehouse team queries a 30 TB BigQuery table daily. They want to reduce query costs by 80% without changing the table schema or losing any data. The queries always filter by a single month's data. Which approach achieves this?

A) Partition the table by `month` (or by `date` with monthly queries filtered by month range) so each query only scans the relevant month's data — approximately 1/12 of 30 TB per query.
B) Enable BI Engine on the table to cache compressed results in memory.
C) Convert the table to a view that limits rows to the past 30 days.
D) Increase slot reservations so queries run faster and cost less per second.

**Correct Answer:** A

**Distractor Analysis:**

- B) BI Engine caches data for sub-second dashboard queries but does not reduce bytes billed on-demand; cost is still charged based on bytes scanned before BI Engine caching applies.
- C) Converting to a view with a 30-day filter changes the data visible to queries and loses historical data access; the requirement explicitly states no data must be lost.
- D) Slot reservations affect compute capacity and query speed but do not change bytes scanned; on-demand pricing charges for bytes scanned regardless of how fast the query runs.

---

### Question 19 (5 points)

A BigQuery MERGE statement fails with the error: `"Merge failed because more than one source row matched the same target row."` What is the cause and the correct fix?

A) The source query in the MERGE contains duplicate keys matching the same target row; deduplicate the source with a subquery using `SELECT DISTINCT` or `ROW_NUMBER()` before the MERGE.
B) The target table requires a primary key constraint to be added before MERGE can run.
C) MERGE in BigQuery requires the source table to be a temporary table, not a subquery.
D) The MERGE condition must use an inequality operator (`<>`) instead of equality (`=`).

**Correct Answer:** A

**Distractor Analysis:**

- B) BigQuery does not enforce primary key constraints at the storage layer; MERGE does not require them and they do not resolve the duplicate source row error.
- C) BigQuery supports MERGE with inline subqueries as the source; there is no requirement for the source to be a physical temporary table.
- D) The MERGE `ON` condition must use equality to match source and target rows; changing to inequality would produce logically incorrect results and does not resolve the duplicate source row issue.

---

### Question 20 (5 points)

A company uses BigQuery for both OLAP analytics and as the backend for a real-time dashboard that refreshes every 30 seconds. Users report that the dashboard is slow and expensive. Which BigQuery feature is most appropriate for the real-time dashboard use case?

A) BI Engine — an in-memory analysis service that caches BigQuery data and answers dashboard queries in milliseconds without scanning the full table on each refresh.
B) Increase slot reservations to 10,000 slots so the dashboard queries run faster.
C) Enable `require_partition_filter` on all tables to force dashboard queries to scan less data.
D) Move the dashboard data to a Cloud Spanner table for low-latency reads.

**Correct Answer:** A

**Distractor Analysis:**

- B) More slots reduce queue time and increase parallelism but do not eliminate the per-query scan cost or reduce latency to the millisecond range needed for 30-second refresh dashboards; BI Engine provides sub-second response times that slot reservations alone cannot.
- C) `require_partition_filter` reduces bytes scanned per query but does not reduce latency to sub-second; dashboard tools often issue queries without easily controllable partition filters, making this a poor fit.
- D) Moving data to Cloud Spanner is a viable option for some low-latency use cases but requires a full data migration, schema redesign, and ongoing synchronization from BigQuery; BI Engine works natively with existing BigQuery tables and requires no migration.

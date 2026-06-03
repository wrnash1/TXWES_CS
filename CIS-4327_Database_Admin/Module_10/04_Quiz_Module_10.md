# Quiz: Module 10 — Database Performance Tuning

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

Instructions: Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A PostgreSQL EXPLAIN ANALYZE output shows `rows=50 width=120` for the planner estimate, but `actual rows=48,000`. What is the most likely cause and correct fix?

- A) The table has too many indexes; remove some indexes and rerun.
- B) The table statistics are stale; run `ANALYZE` on the table.
- C) The query has a syntax error causing the planner to use the wrong plan.
- D) `work_mem` is too small; increase it to allow a better join strategy.

**Answer: B** — A large divergence between estimated and actual row counts is the classic symptom of stale table statistics. The query planner bases its cost estimates on statistics gathered by `ANALYZE`. Running `ANALYZE` or `VACUUM ANALYZE` on the table updates the statistics and allows the planner to choose a better plan.

---

### Question 2

A table `events` has 200 million rows and a `recorded_at TIMESTAMPTZ` column. Rows are always inserted in timestamp order and queries always filter by timestamp range. Which index type minimizes storage while efficiently supporting range queries on this table?

- A) B-tree index on `recorded_at`
- B) Hash index on `recorded_at`
- C) BRIN index on `recorded_at`
- D) GIN index on `recorded_at`

**Answer: C** — BRIN (Block Range Index) is ideal for very large tables where the data is physically ordered by the indexed column (such as a time-series table where rows are always appended in timestamp order). A BRIN index is orders of magnitude smaller than a B-tree on the same column and still enables efficient range queries by eliminating blocks that cannot contain matching rows.

---

### Question 3

An application performs many queries using JSONB containment (`@>`). EXPLAIN ANALYZE shows a Seq Scan on a 10-million-row table taking 8 seconds. Which index type would best optimize these queries?

- A) B-tree index on the JSONB column
- B) BRIN index on the JSONB column
- C) GIN index on the JSONB column
- D) Hash index on the JSONB column

**Answer: C** — GIN (Generalized Inverted Index) is specifically designed for containment queries on JSONB, array, and full-text search data types. B-tree, BRIN, and Hash indexes do not support JSONB containment operators.

---

### Question 4

A MySQL EXPLAIN output shows `type=ALL` and `Extra=Using filesort; Using temporary` for a query. What should be investigated first?

- A) Increase `innodb_buffer_pool_size`.
- B) Add an index that covers the WHERE clause and ORDER BY column to eliminate the full scan, filesort, and temporary table.
- C) Increase `max_connections`.
- D) Enable the binary log.

**Answer: B** — `type=ALL` means a full table scan. `Using filesort` means MySQL cannot use an index for sorting. `Using temporary` means a temporary table is needed (common with GROUP BY or DISTINCT). The root cause is missing indexes — adding an index that covers the filter and sort columns typically resolves all three issues simultaneously.

---

### Question 5

You have a composite B-tree index on `orders (customer_id, order_date)`. Which query can use this index?

- A) `WHERE order_date > '2024-01-01'`
- B) `WHERE customer_id = 42 AND order_date > '2024-01-01'`
- C) `WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31' AND customer_id = 42`
- D) Both B and C

**Answer: D** — Both queries filter on `customer_id` (the leftmost column) and therefore can use the composite index. Option A filters only on `order_date` (the second column) and cannot use this index because the leftmost column (`customer_id`) is not present in the filter. Options B and C are equivalent in terms of index access — both specify `customer_id` which allows the B-tree lookup to narrow to the right customer's rows before applying the date range.

---

### Question 6

A query in `pg_stat_statements` shows `temp_blks_written = 250,000`. What does this indicate and what is the most appropriate fix?

- A) The query is writing too many rows to the table; add a LIMIT clause.
- B) The query's sort or hash operation exceeded `work_mem` and spilled to disk; increase `work_mem` for this query or add an index to avoid the sort.
- C) The WAL is growing too fast; increase `max_wal_size`.
- D) The table has too many dead tuples; run VACUUM.

**Answer: B** — `temp_blks_written` counts disk blocks written to temporary files. Sort operations (ORDER BY, DISTINCT) and hash operations (GROUP BY, hash joins) use `work_mem` in memory, but if the operation exceeds `work_mem`, PostgreSQL spills to temp files on disk. High `temp_blks_written` means the operation is disk-bound. Fix by increasing `work_mem` (carefully, given it multiplies per operation per connection) or adding an index that makes the sort unnecessary.

---

### Question 7

Which optimization eliminates the N+1 query pattern for fetching order details for a list of customers?

- A) Increase `shared_buffers` so queries execute from cache.
- B) Rewrite the application to use a single SQL JOIN that fetches customers and their orders in one query.
- C) Use `OFFSET` pagination to batch the customer queries.
- D) Enable `log_queries_not_using_indexes`.

**Answer: B** — The N+1 pattern runs 1 query for the list, then N queries for each item's related data. The correct fix is to rewrite the application to use a SQL JOIN (or IN clause with batching) that fetches all needed data in a single query. This reduces N+1 round-trips to a single round-trip.

---

### Question 8

A table `audit_logs` has a `user_id` column with only 500 distinct values across 50 million rows. An engineer proposes adding a B-tree index on `user_id` to improve lookup performance. What is the correct assessment?

- A) A B-tree index on `user_id` will significantly speed up lookups.
- B) A B-tree index on `user_id` is unlikely to help because the low cardinality means each lookup still returns thousands of rows, making a Seq Scan potentially cheaper for large result sets.
- C) A Hash index on `user_id` would be better than B-tree.
- D) A GIN index on `user_id` is the correct choice.

**Answer: B** — Low cardinality (500 distinct values in 50 million rows = 100,000 rows per value on average) means an index is unlikely to help for typical lookups. The planner will often choose a Seq Scan because fetching 100,000 scattered heap pages is slower than a sequential scan. A partial index for specific values, a BRIN index, or table partitioning by user_id ranges would be more effective approaches.

---

### Question 9

You want to enable Cloud SQL Performance Insights on a Cloud SQL for PostgreSQL instance. Which gcloud flag enables this?

- A) `--enable-query-plans`
- B) `--enable-performance-schema`
- C) `--insights-config-query-insights-enabled`
- D) `--enable-pg-stat-statements`

**Answer: C** — The `--insights-config-query-insights-enabled` flag enables Query Insights (Performance Insights) for Cloud SQL instances. This is the managed equivalent of pg_stat_statements with additional wait event and client attribution features available through the Cloud Console.

---

### Question 10

An application uses `SELECT * FROM orders ORDER BY created_at LIMIT 10 OFFSET 1000000` for pagination. Performance degrades severely as the page number increases. What is the correct fix?

- A) Increase `work_mem` to allow a larger in-memory sort.
- B) Add a B-tree index on `created_at`.
- C) Rewrite the query using keyset pagination: `WHERE created_at > last_seen_value ORDER BY created_at LIMIT 10`.
- D) Use `FETCH FIRST 10 ROWS ONLY` instead of `LIMIT`.

**Answer: C** — Large OFFSET values require the database to scan and discard all preceding rows before returning the target page. At OFFSET 1,000,000 this means scanning one million rows just to return ten. Keyset pagination uses an index seek on the last seen value (`WHERE created_at > last_seen`), which is an O(1) index lookup regardless of which page you are on. A B-tree index on `created_at` helps the sort but does not solve the OFFSET scan problem.

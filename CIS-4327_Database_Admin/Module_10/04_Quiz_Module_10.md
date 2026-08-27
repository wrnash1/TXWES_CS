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

---

### Question 11 (5 points)

A PostgreSQL query plan shows a `Hash Join` node with `Batches: 8`. What does this indicate and what is the recommended action?

A) The hash join required 8 passes through the table; add an index to eliminate the join.
B) The inner table's hash could not fit in `work_mem` and spilled to disk across 8 batches; increase `work_mem` for this session to reduce disk spills.
C) Eight parallel workers are being used; disable parallel query for this query.
D) The join column has 8 distinct values; add a partial index for each value.

**Correct Answer:** B

**Distractor Analysis:**

- A) `Batches` refers to disk-spill batches during the hash build phase, not table scan passes; adding an index would change the join type but does not address the root cause of the memory spill.
- C) Parallel workers appear in `Workers Planned` / `Workers Launched` nodes, not in the `Batches` field; a batch count of 8 has no relation to parallel execution degree.
- D) Distinct value count is a cardinality metric visible in statistics, not in the plan's Batches counter; partial indexes per value are a valid technique for different problems but do not address hash join memory spill.

---

### Question 12 (5 points)

Which PostgreSQL index type is most appropriate for a column storing `tsvector` full-text search data that will be queried with the `@@` match operator?

A) B-tree
B) GIN
C) BRIN
D) Hash

**Correct Answer:** B

**Distractor Analysis:**

- A) B-tree indexes support equality and range comparisons on scalar values; they cannot index the internal lexeme structure of a `tsvector` or support the `@@` full-text match operator.
- C) BRIN indexes store min/max summaries per block range; they are designed for physically ordered numeric or date columns and do not support full-text search operators.
- D) Hash indexes support only equality (`=`) comparisons; they cannot index the multi-lexeme contents of a `tsvector` column.

---

### Question 13 (5 points)

A DBA wants to create an index that allows PostgreSQL to satisfy a query using an Index Only Scan, avoiding any heap access entirely. The query is `SELECT customer_id, order_date FROM orders WHERE status = 'pending'`. Which index definition achieves this?

A) `CREATE INDEX ON orders (status) INCLUDE (customer_id, order_date);`
B) `CREATE INDEX ON orders (customer_id, order_date, status);`
C) `CREATE INDEX ON orders (status, customer_id);`
D) `CREATE INDEX ON orders (customer_id) WHERE status = 'pending';`

**Correct Answer:** A

**Distractor Analysis:**

- B) This index supports the lookup but stores `status` as the first key column, followed by the projected columns as key columns — the planner may use it but the INCLUDE clause (covering index) is the canonical way to add non-key columns for Index Only Scans without bloating the key.
- C) This composite index includes `customer_id` as a key column but does not include `order_date`, so the planner must still visit the heap to retrieve `order_date`, preventing an Index Only Scan.
- D) A partial index filtered on `status = 'pending'` reduces index size but does not include `order_date` in the index, so heap access is still required for that column.

---

### Question 14 (5 points)

The `default_statistics_target` PostgreSQL parameter is set to its default of 100. A DBA observes chronic planner misestimates on a highly skewed column `campaign_id`. What change most directly improves plan accuracy for that column?

A) `ALTER TABLE orders ALTER COLUMN campaign_id SET STATISTICS 500;`
B) `SET default_statistics_target = 500;` in `postgresql.conf`
C) `REINDEX TABLE orders;`
D) `CLUSTER orders USING idx_campaign_id;`

**Correct Answer:** A

**Distractor Analysis:**

- B) Changing `default_statistics_target` globally affects all columns in all tables, which increases `ANALYZE` time cluster-wide and wastes resources on columns that do not need higher precision; per-column statistics targeting is the correct approach.
- C) `REINDEX` rebuilds index structures and has no effect on the statistical histogram used by the planner for row count estimation.
- D) `CLUSTER` physically reorders table rows to match an index, which can improve sequential scan performance on range queries but does not change the quality of statistics collected by `ANALYZE`.

---

### Question 15 (5 points)

A developer reports that a query reading from a Cloud SQL for PostgreSQL instance runs well initially but slows dramatically after several weeks of production use. `EXPLAIN ANALYZE` shows an increasingly bloated Seq Scan. Which maintenance operation most likely resolves the long-term degradation?

A) Run `VACUUM ANALYZE` on the affected table to reclaim dead tuples and refresh statistics.
B) Increase `shared_buffers` by 25% to improve cache hit ratio.
C) Add a composite index on all columns in the SELECT list.
D) Restart the Cloud SQL instance to clear the buffer pool.

**Correct Answer:** A

**Distractor Analysis:**

- B) Increasing `shared_buffers` improves cache utilization but does not remove dead tuple bloat that inflates physical table size and forces the planner to scan more pages.
- C) Adding an index on SELECT list columns creates a covering index but does not remove existing table bloat; if the table has grown 3x due to dead tuples, even an index scan incurs extra I/O from inflated heap pages.
- D) Restarting clears the buffer cache (warms cold), which worsens performance temporarily and does not reclaim dead tuple space; this is the opposite of the correct action.

---

### Question 16 (5 points)

MySQL's `EXPLAIN` output shows `rows=8500000` for a table with 9 million total rows and `type=ALL`. An engineer adds an index on the filtered column. After adding the index, `EXPLAIN` still shows `type=ALL`. What is the most likely reason MySQL ignored the new index?

A) The index was created with an incorrect column type.
B) The optimizer estimated that fetching 8.5 million rows out of 9 million via an index would require more I/O than a sequential scan, so it chose the full table scan.
C) The MySQL version does not support the index type used.
D) The table requires `ANALYZE TABLE` before any index can be used.

**Correct Answer:** B

**Distractor Analysis:**

- A) Type mismatch typically causes a type conversion in the WHERE clause that prevents index use, but in this scenario the query selectivity (94% of rows) is the dominant factor, not a type error.
- C) Standard B-tree indexes are supported in all production MySQL versions; a version incompatibility would produce a creation error, not silent optimizer avoidance.
- D) While `ANALYZE TABLE` updates statistics, a correctly created index is immediately visible to the optimizer; the root cause here is selectivity, not missing statistics.

---

### Question 17 (5 points)

A PostgreSQL query runs an expensive subquery inside a `WHERE x IN (SELECT ...)` clause repeatedly. The DBA rewrites it as a `JOIN`. What execution plan improvement is most likely?

A) The JOIN version enables the planner to choose a hash join or merge join, which evaluates the subquery once rather than once per outer row.
B) JOINs always produce fewer rows than subqueries, reducing result set size.
C) The planner automatically converts all correlated subqueries to JOINs internally, so there is no practical difference.
D) JOINs bypass the statistics system and always use index scans.

**Correct Answer:** A

**Distractor Analysis:**

- B) JOINs do not inherently produce fewer rows; the result set size depends on join type and data — an INNER JOIN with no deduplication can produce more rows than a subquery using IN (which deduplicates).
- C) Modern PostgreSQL can decorrelate some subqueries automatically, but complex correlated subqueries are not always converted; explicit rewrites to JOINs give the planner maximum flexibility to choose the best strategy.
- D) JOINs are not exempt from the statistics system; the planner uses statistics for both JOIN and subquery plans to estimate cardinality and choose between hash join, merge join, and nested loop strategies.

---

### Question 18 (5 points)

Which `pg_stat_statements` column best identifies queries that are causing the most total I/O pressure on a PostgreSQL instance?

A) `calls`
B) `mean_exec_time`
C) `shared_blks_read + shared_blks_written`
D) `rows`

**Correct Answer:** C

**Distractor Analysis:**

- A) `calls` counts how many times a query was executed but says nothing about I/O volume per call; a query called once that reads 10 million blocks causes more I/O pressure than one called 1,000 times that reads 5 blocks each.
- B) `mean_exec_time` measures average wall-clock duration, which correlates with I/O but is also affected by CPU, lock waits, and network; it does not directly quantify block I/O volume.
- D) `rows` counts result rows returned or affected; a query returning 1 row could still read millions of blocks (e.g., a sequential scan with a highly selective filter at the very end).

---

### Question 19 (5 points)

A partial index is defined as `CREATE INDEX idx_pending ON orders (created_at) WHERE status = 'pending'`. Under which condition will the query planner use this index?

A) Only when the query contains `WHERE status = 'pending'` as a filter condition.
B) Whenever the query filters on `created_at`, regardless of the `status` filter.
C) Only when the query uses `ORDER BY created_at` without any WHERE clause.
D) Only when `created_at` is the primary key of the table.

**Correct Answer:** A

**Distractor Analysis:**

- B) The partial index only covers rows where `status = 'pending'`; a query that does not filter on `status = 'pending'` may need rows with other status values that are not in the index, so the planner will not use the partial index for such queries.
- C) A partial index with a WHERE clause cannot satisfy ORDER BY queries that touch all rows; the index only covers the pending subset, making it unusable for queries that do not also filter to that subset.
- D) The primary key has no relation to whether a partial index is used; partial index eligibility depends on whether the query's WHERE clause implies the index predicate.

---

### Question 20 (5 points)

A DBA observes that `autovacuum` is not keeping up with dead tuple accumulation on a heavily updated table, leading to table bloat. Which parameter change most directly increases autovacuum aggressiveness for that specific table?

A) `ALTER TABLE orders SET (autovacuum_vacuum_scale_factor = 0.01);`
B) `SET autovacuum_vacuum_cost_delay = 0;` in `postgresql.conf`
C) `VACUUM FULL orders;` run on a schedule.
D) Increase `max_connections` to allow more autovacuum workers.

**Correct Answer:** A

**Distractor Analysis:**

- B) Setting `autovacuum_vacuum_cost_delay = 0` removes throttling globally, which can cause autovacuum to consume excessive I/O and interfere with application queries; per-table tuning is the preferred approach.
- C) `VACUUM FULL` reclaims space by rewriting the entire table, but it holds an exclusive lock, blocking all other operations for the duration; it is a one-time fix, not an ongoing solution to autovacuum falling behind.
- D) `max_connections` controls client connection limits and has no effect on autovacuum worker count; autovacuum worker count is governed by `autovacuum_max_workers`.

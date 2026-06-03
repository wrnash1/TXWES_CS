# Video Script: Module 10 — Database Performance Tuning (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back. This is Part 2 of Module 10: Database Performance Tuning.

In Part 1 we covered execution plans, index types, and how the optimizer uses statistics. In Part 2 we get hands-on: slow query logs for finding problems, pg_stat_statements for aggregated profiling, connection pool tuning, and practical query optimization patterns.

---

## Section 1 — Slow Query Log

The first step in performance tuning is finding which queries are slow. You cannot optimize what you cannot measure.

### PostgreSQL Slow Query Log

In `postgresql.conf`:

```ini
log_min_duration_statement = 1000    # log queries taking > 1 second
log_duration = off                   # don't log all query durations
log_line_prefix = '%t [%p]: user=%u db=%d '
```

After setting these parameters, reload:

```bash
sudo systemctl reload postgresql
```

Queries taking longer than 1000 ms are now logged to the PostgreSQL log file:

```text
2024-11-15 09:31:22 UTC [12345]: user=appuser db=mydb LOG:
  duration: 4523.812 ms  statement: SELECT o.order_id, c.full_name, SUM(oi.quantity * oi.unit_price)
  FROM orders o JOIN order_items oi ON oi.order_id = o.order_id
  JOIN customers c ON c.customer_id = o.customer_id
  GROUP BY o.order_id, c.full_name;
```

### MySQL Slow Query Log

In `my.cnf`:

```ini
[mysqld]
slow_query_log = ON
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 1
log_queries_not_using_indexes = ON
min_examined_row_limit = 1000
```

`log_queries_not_using_indexes = ON` captures full table scans even if they complete quickly — catching problems before they become critical on larger datasets.

### mysqldumpslow — Analyze the Slow Log

```bash
# Top 10 slowest by total execution time
mysqldumpslow -s t -t 10 /var/log/mysql/slow.log

# Top 10 slowest by average execution time
mysqldumpslow -s at -t 10 /var/log/mysql/slow.log

# Sort by rows examined
mysqldumpslow -s r -t 10 /var/log/mysql/slow.log
```

---

## Section 2 — pg_stat_statements

`pg_stat_statements` is a PostgreSQL extension that aggregates execution statistics across all calls to each unique query pattern. It is essential for production performance analysis.

```sql
-- Enable the extension (requires shared_preload_libraries = 'pg_stat_statements')
CREATE EXTENSION pg_stat_statements;

-- Top 10 queries by total execution time
SELECT
    left(query, 100) AS query_snippet,
    calls,
    round(total_exec_time::numeric, 2) AS total_ms,
    round(mean_exec_time::numeric, 2) AS mean_ms,
    round(stddev_exec_time::numeric, 2) AS stddev_ms,
    rows,
    round(100.0 * shared_blks_hit /
          NULLIF(shared_blks_hit + shared_blks_read, 0), 2) AS cache_hit_pct
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;

-- Most frequently executed queries
SELECT left(query, 100), calls, round(mean_exec_time::numeric, 2) AS mean_ms
FROM pg_stat_statements
ORDER BY calls DESC
LIMIT 10;

-- Queries with highest cache miss rate (disk-heavy)
SELECT left(query, 100), shared_blks_read, shared_blks_hit,
       round(100.0 * shared_blks_read /
             NULLIF(shared_blks_read + shared_blks_hit, 0), 2) AS miss_pct
FROM pg_stat_statements
WHERE shared_blks_read + shared_blks_hit > 1000
ORDER BY miss_pct DESC
LIMIT 10;

-- Reset statistics (do after tuning to get a clean baseline)
SELECT pg_stat_statements_reset();
```

The `stddev_exec_time` column is particularly valuable — high standard deviation means query execution time is inconsistent, often indicating lock contention or I/O variability.

---

## Section 3 — Query Optimization Patterns

### Pattern 1 — Eliminate N+1 Queries

The N+1 query problem occurs when an application runs one query to fetch a list, then N additional queries to fetch related data for each item.

**Problem:**

```sql
-- Application code runs this once:
SELECT customer_id, full_name FROM customers LIMIT 100;
-- Then for each customer runs:
SELECT * FROM orders WHERE customer_id = ?;  -- runs 100 times
```

**Solution — JOIN:**

```sql
SELECT c.customer_id, c.full_name,
       COUNT(o.order_id) AS order_count,
       SUM(o.total_amount) AS lifetime_value
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.full_name
LIMIT 100;
```

One query instead of 101.

### Pattern 2 — Index the Right Columns

**Bad — indexing a low-cardinality column:**

```sql
-- gender column has only 2 values — B-tree index is useless
CREATE INDEX idx_users_gender ON users (gender);  -- WRONG
```

**Good — index selective columns:**

```sql
-- email is highly selective; every query filters by it
CREATE INDEX idx_users_email ON users (email);  -- RIGHT
```

**Cardinality rule:** An index is useful when it filters out at least 85–90% of rows. A column with 2 distinct values in a million-row table is never worth a B-tree index.

### Pattern 3 — Avoid Functions on Indexed Columns

Wrapping an indexed column in a function prevents index usage.

**Bad:**

```sql
-- The index on order_date cannot be used here
WHERE EXTRACT(YEAR FROM order_date) = 2024
```

**Good:**

```sql
-- Range query on order_date uses the index
WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01'
```

For PostgreSQL, you can create a **function-based index** if the function call is unavoidable:

```sql
CREATE INDEX idx_orders_year ON orders (EXTRACT(YEAR FROM order_date));
WHERE EXTRACT(YEAR FROM order_date) = 2024;  -- now uses the index
```

### Pattern 4 — Use LIMIT Wisely

`LIMIT` reduces the number of rows returned but does NOT always reduce the rows scanned. A query with `ORDER BY non_indexed_col LIMIT 10` still requires a full sort.

```sql
-- Still scans all rows and sorts — LIMIT only applies after
SELECT * FROM events ORDER BY created_at LIMIT 10;
-- Fix: ensure created_at has an index, planner uses index scan with LIMIT pushdown
```

### Pattern 5 — SELECT Only Required Columns

`SELECT *` fetches all columns, even those unused by the application. This increases:

- Data transferred from database to application
- Memory usage in the database for result sets
- Prevention of Index Only Scans (the planner needs heap access for columns not in the index)

```sql
-- Bad: fetches all columns
SELECT * FROM customers WHERE customer_id = 42;

-- Good: fetch only needed columns
SELECT full_name, email FROM customers WHERE customer_id = 42;
```

### Pattern 6 — Pagination with Keyset (Cursor) Pagination

OFFSET-based pagination is a well-known anti-pattern for large datasets.

**Bad — OFFSET pagination:**

```sql
-- Page 1000: PostgreSQL scans and discards 99,990 rows before returning 10
SELECT * FROM orders ORDER BY order_id LIMIT 10 OFFSET 99990;
```

**Good — keyset pagination:**

```sql
-- First page
SELECT order_id, order_date FROM orders ORDER BY order_id LIMIT 10;

-- Next page: use the last seen order_id as the cursor
SELECT order_id, order_date FROM orders
WHERE order_id > 99999  -- last order_id from previous page
ORDER BY order_id LIMIT 10;
```

Keyset pagination scales to any page depth because it uses an index seek, not a scan-and-skip.

---

## Section 4 — Connection Pooling Performance Metrics

In Module 06 we configured PgBouncer. Here we look at how to measure whether your pool configuration is working.

### PgBouncer Pool Metrics

```sql
-- Connect to PgBouncer admin (port 6432, database pgbouncer)
SHOW POOLS;
```

Sample output columns:

- `cl_active` — clients currently executing a query through a server connection
- `cl_waiting` — clients waiting for a server connection because the pool is full
- `sv_active` — server connections currently in use by a client
- `sv_idle` — server connections idle in the pool, ready to serve

**Red flag:** `cl_waiting > 0` means clients are queuing for a server connection — the pool is undersized for the current load. Increase `default_pool_size`.

### PostgreSQL Connection Wait Monitoring

```sql
-- Connections waiting for more than 5 seconds
SELECT pid, usename, application_name,
       now() - state_change AS wait_time,
       wait_event_type, wait_event, state
FROM pg_stat_activity
WHERE wait_event IS NOT NULL
  AND now() - state_change > interval '5 seconds'
ORDER BY wait_time DESC;
```

### Connection Pool Sizing Formula

A common sizing heuristic:

```text
optimal_pool_size ≈ (number_of_CPUs * 2) + number_of_disks
```

For a 4-core server with SSD: pool size ≈ 4*2 + 1 = 9. This follows Amdahl's law — adding more concurrent connections beyond CPU parallelism yields diminishing returns and increasing context-switch overhead.

---

## Section 5 — Cloud SQL Performance Insights

Google Cloud SQL includes **Performance Insights** — a managed version of pg_stat_statements and MySQL performance schema with a visual dashboard.

Key features:

- **Top queries** by database load (CPU, I/O, lock wait)
- **Query details** showing execution plan and wait event breakdown
- **Database load graph** over time, broken down by wait event type

Accessing Performance Insights:

```bash
# Enable on an existing instance
gcloud sql instances patch my-instance \
  --insights-config-query-insights-enabled \
  --insights-config-record-client-address \
  --project=my-project
```

In the Cloud Console: navigate to the Cloud SQL instance → Performance Insights tab.

Performance Insights shows which wait events are consuming the most time:

- `Lock` wait — queries waiting for locks; indicates lock contention
- `IO:DataFile` — queries waiting for disk reads; indicates working set larger than buffer pool
- `CPU` — queries actively using CPU; indicates computation-bound queries

---

## Section 6 — Exam Tips

**Most-tested performance tuning scenarios:**

- Reading EXPLAIN output and identifying the problem (Seq Scan on a large table = missing index)
- MySQL Extra column: `Using filesort` = sort without index; `Using temporary` = temp table needed
- BRIN index use case: time-series table with physically ordered timestamps
- GIN index use case: JSONB containment queries, array operations, full-text search
- Partial index: reduces index size by filtering rows, requires matching WHERE clause in query
- `pg_stat_statements`: best tool for aggregated query profiling
- `SELECT *` prevents Index Only Scan
- Keyset pagination vs OFFSET pagination performance difference
- `log_queries_not_using_indexes = ON` in MySQL slow query log

**Common traps:**

- The exam may describe a table with millions of rows and a query on a boolean or low-cardinality column — the answer is not to add a B-tree index. A partial index or table redesign is more appropriate.
- BRIN indexes are only effective when the table's physical row order matches the indexed column. For a table where rows are inserted in random order, BRIN provides no benefit.

---

## Closing

Module 10 complete. You now have a comprehensive performance tuning toolkit: execution plans, index selection, slow query identification, pg_stat_statements profiling, and query optimization patterns.

The Module 10 lab applies all of these tools to a real dataset. You will identify slow queries, add appropriate indexes, and measure the improvement. Complete it before the quiz.

See you in Module 11: Cloud Spanner and Distributed Databases.

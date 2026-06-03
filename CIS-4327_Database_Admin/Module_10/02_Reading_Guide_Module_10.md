# Reading Guide: Module 10 — Database Performance Tuning

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Overview

This reading guide covers database performance tuning from query analysis through index selection and systematic optimization. Performance tuning is one of the highest-frequency topic areas on the Google Cloud Professional Database Engineer exam. Work through every section and all examples before attempting the lab and quiz.

---

## Section 1 — Execution Plan Fundamentals

### 1.1 PostgreSQL EXPLAIN Options

| Option | Effect |
|---|---|
| `EXPLAIN` | Show plan estimate only, do not execute |
| `EXPLAIN ANALYZE` | Execute query and show actual vs estimated stats |
| `EXPLAIN (ANALYZE, BUFFERS)` | Include shared_buffers hit/read/written counts |
| `EXPLAIN (ANALYZE, FORMAT JSON)` | Machine-readable JSON output |
| `EXPLAIN (ANALYZE, VERBOSE)` | Include column-level output list |

Always use `EXPLAIN ANALYZE` in development and staging. Never use it on production queries you cannot afford to run to completion — use `EXPLAIN` only if you need to check a plan without executing.

### 1.2 PostgreSQL Plan Node Reference

| Node | Description | When Chosen |
|---|---|---|
| Seq Scan | Reads entire table | No usable index; small table; fetching > ~15% of rows |
| Index Scan | Uses index to find rows, fetches heap | Selective filter with index; moderate row count |
| Index Only Scan | Reads index only, no heap access | All queried columns in index; VM (visibility map) allows it |
| Bitmap Index Scan | Builds page bitmap from index | Multiple conditions on different indexes |
| Bitmap Heap Scan | Reads heap pages in order using bitmap | After Bitmap Index Scan |
| Hash Join | Builds hash table from smaller side | Equi-joins; inner side fits in work_mem |
| Nested Loop | For each outer row, scans inner | Small outer, indexed inner |
| Merge Join | Merges two pre-sorted streams | Large sorted inputs; sort cost paid elsewhere |
| Sort | Explicit sort step | ORDER BY without matching index |
| Hash Aggregate | Aggregates using hash table | GROUP BY that fits in work_mem |
| Gather | Collects results from parallel workers | Parallel query execution |

### 1.3 Detecting Plan Problems

```sql
-- Find queries where estimated rows << actual rows (bad statistics)
EXPLAIN (ANALYZE, FORMAT JSON)
SELECT * FROM orders WHERE customer_id = 42;
-- Look for: "Plan Rows" vs "Actual Rows" discrepancy > 10x
```

Large divergence between planned and actual rows is the most common cause of poor plan selection. Fix with `ANALYZE` or by adjusting `default_statistics_target`.

```sql
-- Increase statistics samples for a skewed column
ALTER TABLE orders ALTER COLUMN customer_id SET STATISTICS 500;
ANALYZE orders;
```

The default `default_statistics_target` is 100 (samples). For highly skewed distributions, increase per-column statistics.

---

## Section 2 — Index Type Selection Guide

### 2.1 Choosing the Right Index Type

| Data Type / Query Pattern | Recommended Index |
|---|---|
| Equality + range + sort on scalar values | B-tree (default) |
| Equality only on high-cardinality column | Hash |
| JSONB containment (`@>`) | GIN |
| Array containment, overlap | GIN |
| Full-text search (`@@` tsvector) | GIN |
| Geographic / spatial queries | GiST |
| Range type overlap (`&&`) | GiST or BRIN |
| Time-series, physically ordered large table | BRIN |
| Subset of rows (partial index) | B-tree with WHERE clause |

### 2.2 Index Maintenance Overhead

Every index must be updated on INSERT, UPDATE, and DELETE. Index overhead:

- INSERT: adds entry to every index on the table
- UPDATE: if the indexed column changes, removes old entry and inserts new
- DELETE: marks index entry as dead (VACUUM reclaims)

For write-heavy tables, audit your indexes regularly and remove unused ones:

```sql
-- PostgreSQL: find never-used indexes
SELECT schemaname, relname, indexrelname, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
  AND schemaname NOT IN ('pg_catalog', 'information_schema')
ORDER BY pg_relation_size(indexrelid) DESC;
```

### 2.3 Composite Index Column Ordering

For B-tree composite indexes:

- Put the most selective column first if queries filter on it alone
- Put the equality filter column before the range filter column

```sql
-- Query: WHERE customer_id = 42 AND order_date > '2024-01-01'
-- Best index: (customer_id, order_date) — equality first, range second
CREATE INDEX idx_orders_cust_date ON orders (customer_id, order_date);

-- This index would be less efficient:
CREATE INDEX idx_orders_date_cust ON orders (order_date, customer_id);
-- A query filtering only on customer_id cannot use this index
```

---

## Section 3 — MySQL EXPLAIN Reference

### 3.1 EXPLAIN Type Column Values (Ordered Best to Worst)

| type | Description |
|---|---|
| `system` | Table has exactly one row |
| `const` | At most one matching row via PRIMARY KEY or UNIQUE index |
| `eq_ref` | One row read per join via PRIMARY KEY or UNIQUE |
| `ref` | Multiple rows may match via non-unique index |
| `range` | Index range scan |
| `index` | Full index scan (better than ALL but still scans full index) |
| `ALL` | Full table scan — almost always a performance problem |

### 3.2 MySQL EXPLAIN Extra Column Warning Signs

| Extra Value | Meaning | Action |
|---|---|---|
| `Using filesort` | Sort cannot use existing index | Add index matching ORDER BY |
| `Using temporary` | Requires temporary table | Eliminate with index or query rewrite |
| `Using index` | Index-only access — excellent | No action needed |
| `Using index condition` | Index condition pushdown | Good optimization |
| `Using where` | Additional filter after index access | Normal; check if filter could be indexed |

### 3.3 Forcing Index Usage in MySQL

In rare cases when the optimizer chooses a worse plan:

```sql
-- Force specific index
SELECT * FROM orders USE INDEX (idx_orders_date)
WHERE order_date > '2024-01-01';

-- Prevent index usage (for testing)
SELECT * FROM orders IGNORE INDEX (idx_orders_date)
WHERE order_date > '2024-01-01';
```

Avoid index hints in production code — they make queries brittle to schema changes and bypass optimizer improvements.

---

## Section 4 — pg_stat_statements Query Analysis

### 4.1 Key Metrics

```sql
SELECT
    queryid,
    calls,
    total_exec_time,
    min_exec_time,
    max_exec_time,
    mean_exec_time,
    stddev_exec_time,
    rows,
    shared_blks_hit,
    shared_blks_read,
    shared_blks_written,
    temp_blks_read,
    temp_blks_written
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 20;
```

`temp_blks_written > 0` means the query spilled sort or hash operations to disk — increase `work_mem` for that query or add an appropriate index to avoid the sort entirely.

### 4.2 Identifying Lock Contention

```sql
-- Queries with high average execution time and high stddev (intermittently slow)
SELECT left(query, 80), calls,
       round(mean_exec_time::numeric, 2) AS mean_ms,
       round(stddev_exec_time::numeric, 2) AS stddev_ms,
       round(stddev_exec_time / NULLIF(mean_exec_time, 0) * 100, 1) AS cv_pct
FROM pg_stat_statements
WHERE calls > 100
ORDER BY stddev_exec_time DESC
LIMIT 10;
```

A coefficient of variation (CV) above 100% means the query occasionally takes much longer than usual — a classic signature of intermittent lock waits.

---

## Section 5 — Query Anti-Patterns Reference

### 5.1 Anti-Pattern Summary Table

| Anti-Pattern | Problem | Solution |
|---|---|---|
| `SELECT *` | Fetches unused columns; blocks Index Only Scan | Select only needed columns |
| `OFFSET N` on large N | Scans and discards N rows | Keyset (cursor) pagination |
| Function on indexed column in WHERE | Prevents index use | Rewrite as range, or use function index |
| N+1 queries | N round-trips instead of 1 | JOIN or batch fetch |
| Implicit type conversion | Prevents index use | Match column types exactly |
| OR on different columns | May not use indexes efficiently | Rewrite as UNION or use separate queries |
| Unbounded queries | Returns all rows | Always include LIMIT or pagination |

### 5.2 Implicit Type Conversion Example

```sql
-- orders.customer_id is INTEGER, but the application passes a string
WHERE customer_id = '42'  -- implicit cast; may prevent index use in some versions

-- Fix: ensure parameter type matches column type
WHERE customer_id = 42    -- integer literal
```

In PostgreSQL, the implicit cast from string to integer is usually safe and the index is still used. In MySQL, implicit conversions can cause full table scans — always match types explicitly.

---

## Section 6 — Cloud SQL Performance Insights

### 6.1 Enabling Performance Insights

```bash
gcloud sql instances patch my-instance \
  --insights-config-query-insights-enabled \
  --insights-config-query-string-length=4096 \
  --insights-config-record-application-tags \
  --insights-config-record-client-address \
  --project=my-project
```

### 6.2 Interpreting the Database Load Graph

The load graph shows database time units (DTUs or normalized CPU equivalents) broken down by wait event type:

- **CPU** — query is executing; tuning requires algorithm or index improvement
- **Lock** — query is waiting for a lock; investigate long transactions, missing indexes on join columns
- **IO/Read** — working set exceeds buffer pool; increase `shared_buffers` or `innodb_buffer_pool_size`
- **IO/Write** — checkpoint pressure; tune `checkpoint_completion_target` or `innodb_io_capacity`

---

## Section 7 — VACUUM and Statistics Integration

Performance tuning and routine maintenance are interconnected. Stale statistics cause plan regressions. Bloated tables cause Seq Scans to read many more pages than necessary.

### 7.1 Statistics Target Tuning

```sql
-- Check current statistics target per column
SELECT attname, attstattarget
FROM pg_attribute
WHERE attrelid = 'orders'::regclass AND attstattarget != -1;

-- Increase for a skewed column
ALTER TABLE orders ALTER COLUMN status SET STATISTICS 1000;
ANALYZE orders (status);
```

### 7.2 Bloat Impact on Query Performance

A table with 50% dead tuple bloat requires twice as many block reads for a Seq Scan. After VACUUM, the effective table size shrinks and Seq Scan performance improves significantly.

---

## Section 8 — Key Terms

| Term | Definition |
|---|---|
| Seq Scan | Full table scan reading every row |
| Index Scan | Uses index to find matching rows, fetches heap pages |
| Index Only Scan | Satisfies query entirely from index without heap access |
| Covering index | Index containing all columns needed by a query |
| Partial index | B-tree index with a WHERE filter limiting indexed rows |
| GIN | Generalized Inverted Index for arrays, JSONB, full-text |
| GiST | Generalized Search Tree for geometric and range types |
| BRIN | Block Range Index for physically ordered large tables |
| pg_stat_statements | Extension aggregating per-query execution statistics |
| Cardinality | Number of distinct values in a column |
| Keyset pagination | Pagination using a WHERE clause on the last seen key |
| `Using filesort` | MySQL: sort operation without index support |
| `Using temporary` | MySQL: GROUP BY or DISTINCT requires temporary table |

---

## Study Questions

1. What does a large divergence between estimated and actual rows in EXPLAIN ANALYZE indicate? How do you fix it?

2. Under what conditions would you choose a BRIN index over a B-tree index?

3. Explain why wrapping an indexed column in a function in a WHERE clause prevents index usage. How do you work around this in PostgreSQL?

4. A `pg_stat_statements` query shows `temp_blks_written = 150,000` for a specific query. What does this indicate and how would you fix it?

5. What is keyset pagination and why does it outperform OFFSET pagination for large result sets?

6. A MySQL EXPLAIN shows `Using temporary; Using filesort` in the Extra column. What does each mean and how would you address both?

---

## Certification Exam Checklist

- [ ] PostgreSQL EXPLAIN node types and when each is chosen
- [ ] B-tree: equality + range + sort; Hash: equality only
- [ ] GIN use cases: JSONB, arrays, full-text search
- [ ] GiST use cases: geometry, range types
- [ ] BRIN use cases: physically ordered large tables only
- [ ] Partial index: WHERE clause required in both index definition and query
- [ ] Covering index / INCLUDE: enables Index Only Scan
- [ ] MySQL EXPLAIN Extra: `Using filesort` and `Using temporary` are warning signs
- [ ] `pg_stat_statements`: `temp_blks_written > 0` means disk spill
- [ ] Enabling Cloud SQL Performance Insights with gcloud
- [ ] `default_statistics_target` increase for skewed columns
- [ ] Composite index column ordering: equality before range

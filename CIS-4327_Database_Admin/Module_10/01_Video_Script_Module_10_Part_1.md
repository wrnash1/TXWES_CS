# Video Script: Module 10 — Database Performance Tuning (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back to CIS-4327. I am Professor Nash, and this is Module 10: Database Performance Tuning.

Performance tuning is the art and science of understanding why a database is slow and systematically making it faster. This module covers the tools and techniques you need for both the exam and production work: query execution plans with EXPLAIN ANALYZE, index types and when to use each, slow query logs, and query optimization patterns.

Part 1 covers concepts and theory — execution plans, index types, and the query optimizer's decision-making. Part 2 covers hands-on tuning: slow query analysis, connection pooling metrics, and optimization techniques.

---

## Section 1 — Understanding Query Execution Plans

Before you can tune a query, you need to understand how the database intends to execute it. This is what query execution plans show you.

### EXPLAIN and EXPLAIN ANALYZE

`EXPLAIN` shows the plan the query optimizer has chosen without executing the query. `EXPLAIN ANALYZE` executes the query and shows both the estimated and actual costs.

In PostgreSQL:

```sql
-- Show plan without executing
EXPLAIN SELECT * FROM orders WHERE customer_id = 42;

-- Execute and show actual timing
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) SELECT * FROM orders WHERE customer_id = 42;
```

In MySQL:

```sql
-- Show execution plan
EXPLAIN SELECT * FROM orders WHERE customer_id = 42;

-- JSON format with more detail
EXPLAIN FORMAT=JSON SELECT * FROM orders WHERE customer_id = 42;

-- Execute with timing
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 42;
```

### Reading a PostgreSQL Execution Plan

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT o.order_id, c.full_name, o.total_amount
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
WHERE o.order_date > '2024-01-01'
  AND o.total_amount > 1000;
```

Sample output:

```text
Hash Join  (cost=125.50..3456.78 rows=1234 width=52) (actual time=12.3..45.6 rows=987 loops=1)
  Hash Cond: (o.customer_id = c.customer_id)
  Buffers: shared hit=245 read=89
  ->  Index Scan using idx_orders_date on orders o  (cost=0.43..2890.12 rows=5678 width=28)
          (actual time=0.05..30.2 rows=8234 loops=1)
        Index Cond: (order_date > '2024-01-01'::date)
        Filter: (total_amount > 1000.00)
        Rows Removed by Filter: 7247
        Buffers: shared hit=198 read=89
  ->  Hash  (cost=85.00..85.00 rows=4000 width=32) (actual time=8.5..8.5 rows=4000 loops=1)
        Buckets: 4096  Batches: 1  Memory Usage: 284kB
        Buffers: shared hit=47
        ->  Seq Scan on customers c  (cost=0.00..85.00 rows=4000 width=32)
```

Key elements to understand:

**Cost notation `(cost=start..total)`** — The planner's estimated cost. Lower is better. The first number is the startup cost, the second is the total cost.

**`rows=`** — Estimated vs actual row count. When these diverge significantly (for example, estimated 100, actual 50,000), the planner is making bad decisions because the statistics are stale. Run `ANALYZE` or wait for autovacuum.

**`Buffers: shared hit= read=`** — `hit` means the page was already in shared_buffers (fast). `read` means it had to be read from disk (slow). High read counts indicate the working set does not fit in the buffer pool.

**`Rows Removed by Filter:`** — Rows scanned but rejected by a WHERE condition. If this number is very high relative to rows returned, consider an index on the filter column.

**Execution node types you must know:**

- `Seq Scan` — reads every row in the table. Expected for small tables or when fetching > 10–15% of rows.
- `Index Scan` — uses an index to find matching rows, then fetches the heap pages.
- `Index Only Scan` — satisfies the query entirely from the index without touching heap pages. Only possible when all queried columns are in the index.
- `Bitmap Index Scan + Bitmap Heap Scan` — used when multiple conditions apply to different indexes. Builds a bitmap of matching pages, then fetches them in order.
- `Hash Join` — builds a hash table from the smaller relation, then probes it with the larger. Good for equi-joins on unsorted data.
- `Nested Loop Join` — for each row in the outer relation, scans the inner relation. Efficient when the inner relation has an index and the outer relation is small.
- `Merge Join` — joins two pre-sorted relations in a merge step. Requires both sides to be sorted.

---

## Section 2 — Index Types

Choosing the right index type for a query is one of the highest-impact performance decisions a DBA makes.

### B-Tree Index

The **B-tree** (balanced tree) is the default index type for both PostgreSQL and MySQL. It supports:

- Equality lookups: `WHERE col = value`
- Range queries: `WHERE col > value`, `WHERE col BETWEEN a AND b`
- Sorting: `ORDER BY col` (can use an index scan to avoid a sort step)
- `IS NULL` / `IS NOT NULL`

```sql
CREATE INDEX idx_orders_customer ON orders (customer_id);
CREATE INDEX idx_orders_date ON orders (order_date DESC);
-- Multi-column B-tree
CREATE INDEX idx_orders_cust_date ON orders (customer_id, order_date DESC);
```

The leftmost column rule: a multi-column index on `(customer_id, order_date)` can support queries filtering on `customer_id` alone, or `customer_id + order_date`, but NOT `order_date` alone.

### Hash Index

**Hash indexes** support only equality lookups. They are faster than B-trees for exact-match queries but cannot serve range queries or sorting.

```sql
CREATE INDEX idx_sessions_token ON sessions USING HASH (session_token);
```

Use case: session token lookups, UUID exact-match queries. In PostgreSQL, hash indexes were not WAL-logged before version 10 — in versions 10+, they are safe and crash-recoverable.

### GIN Index — Generalized Inverted Index

**GIN indexes** are designed for data types that contain multiple component values: arrays, JSONB, full-text search tsvector, and hstore.

```sql
-- Index a JSONB column for containment queries
CREATE INDEX idx_events_payload ON events USING GIN (payload);

-- Query uses the GIN index
SELECT * FROM events WHERE payload @> '{"event_type": "login"}';

-- Full-text search
CREATE INDEX idx_articles_fts ON articles USING GIN (to_tsvector('english', body));
SELECT * FROM articles WHERE to_tsvector('english', body) @@ to_tsquery('database & tuning');
```

GIN indexes are large and expensive to update but provide very fast searches across array and JSONB containment.

### GiST Index — Generalized Search Tree

**GiST indexes** support geometric data types, range types, and full-text search. They support nearest-neighbor search and overlap queries.

```sql
-- Index a geographic point (PostGIS)
CREATE INDEX idx_locations_point ON locations USING GIST (location);
-- Find locations within 10 km
SELECT * FROM locations WHERE ST_DWithin(location, ST_MakePoint(-97.33, 32.72)::geography, 10000);

-- Range type index
CREATE INDEX idx_bookings_period ON bookings USING GIST (booking_period);
SELECT * FROM bookings WHERE booking_period && '[2024-11-01, 2024-11-30]'::daterange;
```

### BRIN Index — Block Range Index

**BRIN indexes** are tiny indexes designed for very large tables where rows are physically ordered by the index column — for example, time-series tables where rows are inserted in timestamp order.

```sql
CREATE INDEX idx_sensor_readings_ts ON sensor_readings USING BRIN (recorded_at);
```

A BRIN index stores only the minimum and maximum value of the indexed column per block range (a contiguous group of disk pages). They are orders of magnitude smaller than B-tree indexes on the same column but only effective when data is physically sorted.

### Partial Index

A **partial index** indexes only a subset of rows matching a WHERE condition. Dramatically reduces index size and maintenance overhead for queries on selective subsets.

```sql
-- Index only active orders (not completed/cancelled)
CREATE INDEX idx_orders_active ON orders (customer_id, order_date)
WHERE status = 'active';

-- Query must include the filter condition to use the index
SELECT * FROM orders WHERE status = 'active' AND customer_id = 42;
```

### Covering Index (Index-Only Scan)

Including additional columns in the index allows the planner to satisfy a query entirely from the index without reading heap pages.

```sql
-- Covering index: customer_id is the search key, order_date and total are included
CREATE INDEX idx_orders_covering ON orders (customer_id)
INCLUDE (order_date, total_amount);

-- This query can use Index Only Scan
SELECT order_date, total_amount FROM orders WHERE customer_id = 42;
```

---

## Section 3 — MySQL EXPLAIN Output

MySQL's EXPLAIN output is different from PostgreSQL's. Key columns:

```sql
EXPLAIN
SELECT o.order_id, c.full_name
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
WHERE o.order_date > '2024-01-01';
```

```text
id | select_type | table | type  | possible_keys     | key              | key_len | ref  | rows  | Extra
1  | SIMPLE      | c     | ALL   | PRIMARY           | NULL             | NULL    | NULL | 4000  | Using temporary
1  | SIMPLE      | o     | range | idx_orders_date   | idx_orders_date  | 4       | NULL | 5678  | Using index condition
```

Key columns:

- **type** — join type. From best to worst: `system > const > eq_ref > ref > range > index > ALL`. `ALL` means full table scan — almost always bad for large tables.
- **possible_keys** — indexes the optimizer considered.
- **key** — the index actually chosen. `NULL` means no index used.
- **rows** — estimated rows examined. Multiply across all join rows to understand total work.
- **Extra** — additional operations: `Using filesort` (needs a sort), `Using temporary` (needs a temp table), `Using index` (index-only access), `Using index condition` (ICP — index condition pushdown).

`Using filesort` and `Using temporary` in the Extra column are the two biggest red flags in MySQL EXPLAIN output. They indicate expensive operations that should be eliminated through indexing or query rewriting.

---

## Section 4 — The Query Optimizer and Statistics

Both PostgreSQL and MySQL use **cost-based query optimizers**. The optimizer generates multiple possible execution plans, estimates the cost of each, and selects the cheapest.

Cost estimates depend on **statistics** about each table and index:

- Number of rows (cardinality)
- Value distribution histograms (most common values, percentile ranges)
- Null fraction
- Average column width

Statistics become stale as data changes. Stale statistics lead to bad plan choices.

In PostgreSQL, update statistics:

```sql
ANALYZE orders;
-- Or VACUUM ANALYZE to do both:
VACUUM ANALYZE orders;
```

In MySQL, update statistics:

```sql
ANALYZE TABLE orders;
```

### Statistics-Driven Plan Mistakes

A classic example: a table has 10 million rows, 99% with `status = 'completed'` and 1% with `status = 'active'`. A query for active orders:

```sql
SELECT * FROM orders WHERE status = 'active';
```

If statistics are stale and show uniform distribution, the planner estimates 50% of rows match and chooses a sequential scan. The correct choice is an index on `status` or a partial index on `status = 'active'`. Running `ANALYZE` fixes the statistics and allows the planner to make the right choice.

---

## Section 5 — Exam Summary for Part 1

Key exam topics from Part 1:

- `EXPLAIN ANALYZE` shows actual vs estimated rows — divergence indicates stale statistics
- PostgreSQL node types: Seq Scan, Index Scan, Index Only Scan, Bitmap Scan, Hash Join, Nested Loop, Merge Join
- B-tree: default, supports equality + range + sort
- Hash: equality only, faster than B-tree for exact match
- GIN: arrays, JSONB, full-text search
- GiST: geometric, range types, nearest-neighbor
- BRIN: tiny index for physically ordered large tables (time-series)
- Partial index: filters rows, reduces size and maintenance cost
- Covering index / INCLUDE: enables Index Only Scan
- MySQL Extra field: `Using filesort` and `Using temporary` = performance problems

---

## Closing

That covers Part 1 of Module 10. You understand execution plans, index types, and how the query optimizer uses statistics.

In Part 2 we shift to hands-on tuning: slow query logs, identifying problematic queries, connection pooling metrics, and systematic optimization patterns. See you in Part 2.

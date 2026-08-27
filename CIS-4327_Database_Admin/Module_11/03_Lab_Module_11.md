# Lab Activity: Module 11 — Database Performance Tuning and Query Optimization

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Total Points: 100

---

### Lab Overview

In this lab you will diagnose and resolve query performance problems on a Cloud SQL for PostgreSQL instance using `EXPLAIN ANALYZE`, index creation, and Cloud SQL Query Insights. You will also simulate and resolve connection pool exhaustion. These hands-on skills are directly tested in the performance tuning domain of the GCP Professional Cloud Database Engineer exam.

Estimated completion time: 75–90 minutes.

---

### Prerequisites

- Google Cloud student project with billing enabled
- `gcloud` CLI authenticated (`gcloud auth login`)
- PostgreSQL client (`psql`) available in Cloud Shell or locally
- Module 11 video scripts and reading guide reviewed

---

### Part 1 — Environment Setup (10 points)

#### Step 1 — Create a Cloud SQL Instance and Load Sample Data

```bash
PROJECT_ID=$(gcloud config get-value project)
SQL_INSTANCE=lab11-perf

gcloud sql instances create ${SQL_INSTANCE} \
    --database-version=POSTGRES_15 \
    --region=us-central1 \
    --tier=db-n1-standard-2 \
    --insights-config-query-insights-enabled \
    --insights-config-query-string-length=1024

gcloud sql databases create lab11_db --instance=${SQL_INSTANCE}

gcloud sql users set-password postgres \
    --host=% \
    --instance=${SQL_INSTANCE} \
    --password="PerfLab2024!"
```

#### Step 2 — Connect and Build the Schema

```bash
gcloud sql connect ${SQL_INSTANCE} --user=postgres --database=lab11_db
```

Once in psql, create the orders table and load 1 million rows:

```sql
CREATE TABLE orders (
    order_id     BIGSERIAL PRIMARY KEY,
    customer_id  VARCHAR(20) NOT NULL,
    product_sku  VARCHAR(20) NOT NULL,
    status       VARCHAR(20) NOT NULL DEFAULT 'pending',
    total_amount NUMERIC(12,2),
    created_at   TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Load 1 million sample rows (this takes 60-90 seconds)
INSERT INTO orders (customer_id, product_sku, status, total_amount, created_at)
SELECT
    'C' || LPAD((random() * 10000)::INT::TEXT, 6, '0'),
    'SKU-' || LPAD((random() * 5000)::INT::TEXT, 5, '0'),
    (ARRAY['pending','active','shipped','delivered','cancelled'])[(random()*4+1)::INT],
    ROUND((random() * 999 + 1)::NUMERIC, 2),
    NOW() - (random() * INTERVAL '365 days')
FROM generate_series(1, 1000000);

-- Verify row count
SELECT COUNT(*) FROM orders;
```

**Deliverable 1 (10 points):** Take a screenshot of the `SELECT COUNT(*)` output confirming 1,000,000 rows. Save as `lab11_screenshot_01.png`.

---

### Part 2 — Diagnosing Slow Queries with EXPLAIN ANALYZE (25 points)

#### Step 3 — Run a Slow Query and Capture the Execution Plan

```sql
-- Run EXPLAIN ANALYZE on a query with no index on customer_id
EXPLAIN ANALYZE
SELECT order_id, customer_id, total_amount
FROM orders
WHERE customer_id = 'C003456';
```

Copy the full output. Look for the following in the output:

- The scan type at the top of the plan (should be `Seq Scan`)
- The estimated and actual row counts
- The actual time in milliseconds
- The `Rows Removed by Filter` value

**Deliverable 2 (15 points):** Take a screenshot of the full `EXPLAIN ANALYZE` output showing the sequential scan. In your lab report, answer these three questions.

First: identify the scan type shown in the plan and explain what it means operationally. How many rows did the database read to return the results?

Second: what is the actual query execution time shown in the output? Why is this query slow given that you are filtering to a specific customer ID?

Third: what specific change would you make to the table to fix this performance problem?

#### Step 4 — Create an Index and Re-Measure

```sql
-- Create a B-tree index on customer_id
CREATE INDEX idx_orders_customer ON orders(customer_id);

-- Run the same EXPLAIN ANALYZE after index creation
EXPLAIN ANALYZE
SELECT order_id, customer_id, total_amount
FROM orders
WHERE customer_id = 'C003456';
```

**Deliverable 3 (10 points):** Take a screenshot of the `EXPLAIN ANALYZE` output after the index is created. In your lab report, answer these two questions.

First: what scan type does the plan show now? What is the new actual execution time?

Second: calculate the performance improvement ratio: `before_time_ms / after_time_ms`. State this in your report and explain why the improvement is so dramatic.

---

### Part 3 — Composite Index and Query Patterns (15 points)

#### Step 5 — Composite Index for Multi-Column Queries

```sql
-- Query filtering on both status and created_at
EXPLAIN ANALYZE
SELECT order_id, customer_id, total_amount
FROM orders
WHERE status = 'pending'
  AND created_at >= NOW() - INTERVAL '30 days'
ORDER BY created_at DESC;
```

Note the execution plan — likely a sequential scan or an inefficient plan.

```sql
-- Create a composite index (status first, then created_at)
CREATE INDEX idx_orders_status_date ON orders(status, created_at DESC);

-- Re-run the same query
EXPLAIN ANALYZE
SELECT order_id, customer_id, total_amount
FROM orders
WHERE status = 'pending'
  AND created_at >= NOW() - INTERVAL '30 days'
ORDER BY created_at DESC;
```

**Deliverable 4 (10 points):** Take a screenshot of both `EXPLAIN ANALYZE` outputs (before and after the composite index). In your lab report, explain why `status` was placed as the first column in the composite index rather than `created_at`. What query pattern would be unable to use this index?

#### Step 6 — Stale Statistics Exercise

```sql
-- Delete 80% of the rows to create stale statistics
DELETE FROM orders WHERE order_id % 5 != 0;

-- Run the query again WITHOUT running ANALYZE first
EXPLAIN ANALYZE
SELECT order_id, customer_id, total_amount
FROM orders
WHERE customer_id = 'C003456';
```

Observe the estimated row count versus actual row count — the planner still thinks there are 1 million rows.

```sql
-- Now run ANALYZE and re-check the plan
ANALYZE orders;

EXPLAIN ANALYZE
SELECT order_id, customer_id, total_amount
FROM orders
WHERE customer_id = 'C003456';
```

**Deliverable 5 (5 points):** In your lab report, explain what `ANALYZE` does and when it should be run manually rather than relying on autovacuum.

---

### Part 4 — Cloud SQL Query Insights (20 points)

#### Step 7 — Enable and Configure Query Insights

Query Insights was enabled during instance creation. Verify it is active:

```bash
gcloud sql instances describe ${SQL_INSTANCE} \
    --format="yaml(settings.insightsConfig)"
```

#### Step 8 — Generate Query Load

In psql, run the following queries to generate traffic that Query Insights can capture:

```sql
-- Generate varied query traffic for 2-3 minutes
DO $$
DECLARE
  i INTEGER;
BEGIN
  FOR i IN 1..200 LOOP
    PERFORM order_id, customer_id, total_amount
    FROM orders
    WHERE customer_id = 'C' || LPAD((random() * 10000)::INT::TEXT, 6, '0');

    PERFORM COUNT(*)
    FROM orders
    WHERE status = 'pending'
      AND created_at >= NOW() - INTERVAL '30 days';
  END LOOP;
END;
$$;
```

#### Step 9 — Review Query Insights in the Console

Navigate to: Cloud Console → SQL → your instance → Query Insights tab.

Observe:

- The top queries ranked by CPU time
- The execution count for each query pattern
- The latency percentiles (p50, p95, p99)
- The execution plan for one of the captured queries

**Deliverable 6 (20 points):** Take a screenshot of the Query Insights dashboard showing at least two captured query patterns ranked by CPU time. In your lab report, answer these two questions.

First: what information does Query Insights provide that you cannot get from `EXPLAIN ANALYZE` alone? Describe two specific metrics.

Second: explain why Query Insights normalizes query text by replacing literal values with placeholders like `$1`. What is the operational benefit of this normalization?

---

### Part 5 — Connection Pool Simulation (20 points)

#### Step 10 — Demonstrate Connection Limit Behavior

In Cloud Shell, open a second tab and run the following script to open many concurrent connections:

```bash
# Simulate connection exhaustion (run in Cloud Shell)
# First: check current max connections
gcloud sql connect ${SQL_INSTANCE} --user=postgres --database=lab11_db -- \
    -c "SHOW max_connections;"
```

```sql
-- View current connection count
SELECT count(*) AS active_connections
FROM pg_stat_activity;

-- View connections grouped by application
SELECT application_name, count(*) AS connections
FROM pg_stat_activity
GROUP BY application_name
ORDER BY connections DESC;
```

**Deliverable 7 (10 points):** Take a screenshot showing the current active connections query output. In your lab report, explain what would happen operationally if an application opened connections up to the `max_connections` limit and why upgrading to a larger instance is not the correct long-term solution.

#### Step 11 — PgBouncer Configuration Analysis

You do not need to install PgBouncer in this lab. Instead, write the configuration analysis described below.

**Deliverable 8 (10 points):** In your lab report, write a structured comparison of the three PgBouncer pooling modes (session, transaction, statement) covering: when the connection is returned to the pool, which application features are incompatible with each mode, and which mode you would recommend for a standard OLTP web application and why.

---

### Part 6 — Index Maintenance (10 points)

#### Step 12 — Identify Unused Indexes

```sql
-- Check index usage statistics
SELECT
    schemaname,
    tablename,
    indexname,
    idx_scan AS times_used,
    idx_tup_read AS tuples_read,
    idx_tup_fetch AS tuples_fetched,
    pg_size_pretty(pg_relation_size(indexrelid)) AS index_size
FROM pg_stat_user_indexes
ORDER BY idx_scan ASC, pg_relation_size(indexrelid) DESC;
```

```sql
-- Check table size and index sizes
SELECT
    tablename,
    pg_size_pretty(pg_total_relation_size(tablename::text)) AS total_size,
    pg_size_pretty(pg_relation_size(tablename::text)) AS table_size,
    pg_size_pretty(pg_total_relation_size(tablename::text)
                   - pg_relation_size(tablename::text)) AS index_size
FROM pg_tables
WHERE schemaname = 'public';
```

**Deliverable 9 (10 points):** Take a screenshot of the index usage query output. In your lab report, explain the trade-off of maintaining indexes on write-heavy tables. Describe one scenario where you would choose NOT to create an index on a highly queried column.

---

### Lab Cleanup

```bash
# Delete the instance when finished to avoid charges
gcloud sql instances delete ${SQL_INSTANCE} --quiet
```

---

### Lab Submission Checklist

- Deliverable 1 (10 pts) — 1M row count screenshot
- Deliverable 2 (15 pts) — Sequential scan EXPLAIN ANALYZE screenshot and analysis
- Deliverable 3 (10 pts) — Post-index EXPLAIN ANALYZE screenshot and speedup ratio
- Deliverable 4 (10 pts) — Composite index screenshots and column order explanation
- Deliverable 5 (5 pts) — ANALYZE explanation
- Deliverable 6 (20 pts) — Query Insights dashboard screenshot and analysis
- Deliverable 7 (10 pts) — Connection count screenshot and exhaustion explanation
- Deliverable 8 (10 pts) — PgBouncer pooling mode comparison
- Deliverable 9 (10 pts) — Index usage screenshot and write trade-off analysis

---

### Grading Rubric — 100 Points Total

| Deliverable | Points | Criteria |
|---|---|---|
| 1 — Row count screenshot | 10 | 1,000,000 rows confirmed |
| 2 — Sequential scan analysis | 15 | Seq Scan identified; row read count correct; index recommendation stated |
| 3 — Post-index analysis | 10 | Index Scan shown; speedup ratio calculated; mechanism explained |
| 4 — Composite index analysis | 10 | Column order rationale correct; query pattern limitation identified |
| 5 — ANALYZE explanation | 5 | Purpose of ANALYZE stated; autovacuum limitation identified |
| 6 — Query Insights analysis | 20 | Two specific metrics beyond EXPLAIN ANALYZE; normalization benefit explained |
| 7 — Connection exhaustion | 10 | Current count shown; long-term solution correct (pooler, not upgrade) |
| 8 — PgBouncer comparison | 10 | All three modes described; OLTP recommendation with rationale |
| 9 — Index maintenance | 10 | Trade-off explained; valid scenario for not indexing identified |

---

Reference: cloud.google.com/learn

---

## Part 9 — Challenge Exercise

### Challenge 1: Trigram Full-Text Search with pg_trgm

1. Enable the `pg_trgm` extension and create a GIN trigram index on a text column to support leading-wildcard LIKE searches:

   ```sql
   CREATE EXTENSION IF NOT EXISTS pg_trgm;
   CREATE INDEX idx_orders_notes_trgm ON orders USING GIN (notes gin_trgm_ops);
   ```

2. Run `EXPLAIN ANALYZE` on a leading-wildcard query before and after the index, and compare the scan type and execution time:

   ```sql
   EXPLAIN ANALYZE SELECT order_id, notes FROM orders WHERE notes LIKE '%urgent%';
   ```

3. Confirm the plan switches from `Seq Scan` to `Bitmap Index Scan` using the trigram index. Record the execution time improvement ratio.

4. Run the following to understand why trigrams work: execute `SELECT show_trgm('urgent');` and explain in your lab notes how a 3-character token index supports substring matching.

### Challenge 2: Identifying and Resolving an N+1 Query Pattern

1. In `pg_stat_statements`, identify a query that is called thousands of times per minute but returns only 1 row per call:

   ```sql
   SELECT query, calls, mean_exec_time, rows / NULLIF(calls, 0) AS avg_rows_per_call
   FROM pg_stat_statements
   WHERE rows / NULLIF(calls, 0) <= 1
     AND calls > 500
   ORDER BY calls DESC
   LIMIT 10;
   ```

2. For the top result, write an equivalent batch query that retrieves the same data for 100 IDs in a single call using `= ANY(ARRAY[...])` syntax, and capture its `EXPLAIN ANALYZE` output.

3. Compare the total execution time of 100 individual single-row queries versus one batch query returning 100 rows. Calculate the reduction in total database time.

### Reflection Questions

1. The trigram index in Challenge 1 enables `LIKE '%text%'` searches but is larger and slower to update than a B-tree index. Describe the specific scenario where you would choose a trigram GIN index over a full-text `tsvector` GIN index for a production search feature.
2. The N+1 pattern is one of the most common application-level performance problems. Describe how you would detect it in production using only `pg_stat_statements` data, and what threshold values (calls, avg_rows_per_call) would trigger an investigation.

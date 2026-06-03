# Video Script: Module 12 — BigQuery for Analytics (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Database Engineer

---

## SLIDE 1 — Recap and Part 2 Objectives

Welcome to Part 2 of Module 12. In Part 1, we covered BigQuery's architecture —
Dremel, columnar storage, dataset and table management, partitioning, and clustering.

In Part 2 we dive into:

- DML and DDL operations unique to BigQuery
- Views and materialized views
- Cost optimization: pricing model, slots, and query best practices

Let's continue.

---

## SLIDE 2 — BigQuery Pricing Model

Before writing queries, you need to understand how BigQuery charges you. BigQuery has
two pricing dimensions:

**Storage pricing**:

- Active storage: data modified in the last 90 days — approximately $0.02 per GB per month.
- Long-term storage: data not modified for 90+ days automatically drops to approximately
  $0.01 per GB per month. This happens automatically with no action required.

**Query pricing** (on-demand):

- You are charged for the number of bytes processed by each query — approximately
  $6.25 per TB (first 1 TB per month is free).
- Charges are based on bytes **scanned**, not bytes returned.

**Flat-rate pricing** (capacity-based):

- You purchase slots (units of compute). Queries run against your purchased slots.
- Useful for organizations with predictable, high-volume workloads.
- Editions: Standard, Enterprise, Enterprise Plus — each with different slot commitment options.

For the exam: know that partitioning and clustering reduce bytes scanned, which directly
reduces on-demand query cost. Also know that results cache can eliminate charges entirely
for repeated identical queries.

---

## SLIDE 3 — Query Results Cache

BigQuery caches query results for 24 hours. If you run the same query (same text, same
tables, same user) within 24 hours, BigQuery returns the cached result at no charge.

Caching requirements:

- The query must be deterministic (no `CURRENT_TIMESTAMP()`, `RAND()`, etc.).
- The underlying tables must not have changed.
- The query must not reference external tables or temporary tables.
- Caching is per-user by default; you cannot share cache across users.

You can explicitly disable caching with:

```sql
-- In the query settings or:
SELECT /*+ NO_CACHE */ SUM(revenue) FROM ...
```

Or via the API: set `useQueryCache: false` in the job configuration.

---

## SLIDE 4 — DDL in BigQuery

BigQuery supports a growing subset of DDL statements. You have already seen
`CREATE TABLE`. Here are additional important DDL operations:

**Altering a table**:

```sql
ALTER TABLE txwes-analytics.sales_data.orders
ADD COLUMN discount NUMERIC;
```

```sql
ALTER TABLE txwes-analytics.sales_data.orders
SET OPTIONS (expiration_timestamp = TIMESTAMP '2027-01-01 00:00:00 UTC');
```

**Dropping a table**:

```sql
DROP TABLE IF EXISTS txwes-analytics.sales_data.orders_old;
```

**Truncating a table** (removes all rows, keeps schema):

```sql
TRUNCATE TABLE txwes-analytics.sales_data.orders_staging;
```

Note: `TRUNCATE` in BigQuery does not support a `WHERE` clause. It removes all rows.

**Cloning a table** (zero-copy clone, billed only for changes after clone):

```sql
CREATE TABLE txwes-analytics.sales_data.orders_backup
CLONE txwes-analytics.sales_data.orders;
```

Table clones are an excellent cost-effective way to create point-in-time backups for
development and testing.

---

## SLIDE 5 — DML in BigQuery

BigQuery supports full DML: INSERT, UPDATE, DELETE, and MERGE.

**INSERT**:

```sql
INSERT INTO txwes-analytics.sales_data.orders (order_id, customer_id, order_date, revenue, region)
VALUES (10001, 42, '2025-06-01', 1250.00, 'Southwest');
```

**UPDATE**:

```sql
UPDATE txwes-analytics.sales_data.orders
SET revenue = revenue * 1.05
WHERE region = 'Southwest' AND order_date >= '2025-01-01';
```

**DELETE**:

```sql
DELETE FROM txwes-analytics.sales_data.orders
WHERE order_date < '2020-01-01';
```

**MERGE** (upsert pattern — important for the exam):

```sql
MERGE txwes-analytics.sales_data.orders AS target
USING txwes-analytics.sales_data.orders_staging AS source
ON target.order_id = source.order_id
WHEN MATCHED THEN
  UPDATE SET revenue = source.revenue, region = source.region
WHEN NOT MATCHED THEN
  INSERT (order_id, customer_id, order_date, revenue, region)
  VALUES (source.order_id, source.customer_id, source.order_date, source.revenue, source.region);
```

Important exam note: BigQuery DML mutations are billed at the byte level just like
queries. Large `UPDATE` or `DELETE` operations on petabyte tables can be expensive.
Design ETL pipelines to minimize DML by using `WRITE_TRUNCATE` load jobs instead
of row-level updates where possible.

---

## SLIDE 6 — Views in BigQuery

A view is a saved SQL query. No data is stored. Every time a view is queried, BigQuery
executes the underlying SQL.

```sql
CREATE VIEW txwes-analytics.sales_data.southwest_orders AS
SELECT order_id, customer_id, order_date, revenue
FROM txwes-analytics.sales_data.orders
WHERE region = 'Southwest';
```

Use cases for views:

- **Logical abstraction**: Hide complex joins from end users.
- **Security**: Grant users access to a view instead of the underlying table, hiding
  sensitive columns (e.g., a view that excludes a PII-containing column).
- **Standardization**: Ensure all users query data with the same filters applied.

Limitation: Views are not cached. Every query against a view re-executes the SQL.
For high-frequency, expensive views, use materialized views instead.

---

## SLIDE 7 — Authorized Views

An **authorized view** is a view that has been granted access to a dataset it doesn't
belong to, without granting the viewer access to the underlying source table.

Example scenario: The `sales_data` dataset contains a sensitive `customers` table. The
analytics team needs a view of orders joined to customer names — but should not have
direct access to `customers`.

Steps:

1. Create the view in a separate dataset (e.g., `analytics_views`).
2. In the `sales_data` dataset settings, add the view as an **authorized view**.
3. Grant the analytics team access to `analytics_views` only.

The view can now read from `sales_data.customers` even though the querying users cannot.
This is a key BigQuery security pattern tested on the exam.

---

## SLIDE 8 — Materialized Views

A materialized view stores the precomputed result of a query. BigQuery automatically
and incrementally maintains the materialized view as the base table changes.

```sql
CREATE MATERIALIZED VIEW txwes-analytics.sales_data.daily_revenue_mv AS
SELECT
  order_date,
  region,
  SUM(revenue) AS total_revenue,
  COUNT(*) AS order_count
FROM txwes-analytics.sales_data.orders
GROUP BY order_date, region;
```

Benefits:

- **Query acceleration**: BigQuery's query optimizer can rewrite queries against the
  base table to use the materialized view automatically — even if the query doesn't
  explicitly reference the view.
- **Reduced cost**: Materialized views are pre-aggregated, so queries scan far less data.
- **Automatic refresh**: BigQuery refreshes materialized views within a configurable
  max_staleness window.

Limitations:

- Supports only specific query patterns (aggregations with GROUP BY, no subqueries,
  no JOINs in the materialized view query in the standard tier).
- Max staleness setting: if data in the base table is newer than max_staleness,
  BigQuery may fall back to querying the base table directly.

---

## SLIDE 9 — Query Optimization Best Practices

Understanding query optimization is critical for both the exam and real-world BigQuery usage.

**Avoid SELECT \***:

Always specify only the columns you need. `SELECT *` forces BigQuery to scan all columns,
eliminating the columnar storage benefit.

**Filter early**:

Apply `WHERE` clauses that reference partition and cluster columns. Move filters into
subqueries when needed so pruning can occur before joins.

**Use approximate aggregation functions**:

`APPROX_COUNT_DISTINCT()` is faster and cheaper than `COUNT(DISTINCT column)` for
large datasets where exact counts are not required.

**Avoid self-joins on large tables**:

Use window functions instead:

```sql
SELECT
  order_id,
  revenue,
  AVG(revenue) OVER (PARTITION BY region ORDER BY order_date
                     ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS rolling_avg
FROM txwes-analytics.sales_data.orders;
```

**ORDER BY only at the outermost query**:

Sorting is expensive in distributed systems. Avoid ORDER BY in subqueries or CTEs.

---

## SLIDE 10 — Slot Reservations and Workload Management

For organizations on flat-rate (capacity) pricing, BigQuery uses **slots** as the unit
of compute. One slot is approximately one virtual CPU for query processing.

Slot concepts:

- **Commitments**: Purchase a fixed number of slots for 1 year or 3 years at a discount.
- **Flex slots**: Purchase slots for as little as 60 seconds — useful for burst workloads.
- **Reservations**: Allocate a pool of slots to a specific project or folder.
- **Assignment**: Attach a project to a reservation so its queries use those slots.

Example: You purchase 1,000 slots and create two reservations — 700 for production
analytics and 300 for development. Production queries are always guaranteed 700 slots
even if dev workloads are running.

For on-demand pricing, BigQuery automatically scales compute. For predictable workloads
above $20,000 per month in query costs, flat-rate pricing typically saves money.

---

## SLIDE 11 — Monitoring BigQuery with INFORMATION_SCHEMA

BigQuery provides a set of `INFORMATION_SCHEMA` views that let you query metadata and
job history directly with SQL.

Useful views:

```sql
-- Find the most expensive queries in the past 7 days
SELECT
  job_id,
  user_email,
  total_bytes_processed,
  total_slot_ms,
  query
FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
WHERE creation_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
  AND statement_type = 'SELECT'
ORDER BY total_bytes_processed DESC
LIMIT 20;
```

```sql
-- Find tables with no recent queries (candidates for archiving)
SELECT
  table_id,
  last_modified_time,
  row_count,
  size_bytes
FROM txwes-analytics.sales_data.INFORMATION_SCHEMA.TABLE_STORAGE
ORDER BY last_modified_time ASC;
```

These queries are valuable for governance, cost management, and capacity planning.

---

## SLIDE 12 — Module 12 Summary

Let's close out Module 12 with a summary of key takeaways:

**Architecture**: BigQuery separates storage (Colossus) and compute (Dremel). This
serverless, columnar design enables petabyte-scale queries in seconds.

**Data organization**: Projects → Datasets → Tables. Dataset location is immutable.

**Performance**: Partition by date or integer range for pruning. Cluster on filter
columns for block-level optimization. Both reduce bytes scanned and cost.

**DML/DDL**: BigQuery supports full DDL (CREATE, ALTER, DROP, TRUNCATE, CLONE) and
DML (INSERT, UPDATE, DELETE, MERGE). DML is billed by bytes processed.

**Views**: Regular views for abstraction and security. Materialized views for
precomputed aggregations that reduce cost and latency. Authorized views for
cross-dataset security.

**Cost**: On-demand is billed per TB scanned. Flat-rate uses slots. The query
results cache eliminates charges for repeated identical queries.

**Monitoring**: `INFORMATION_SCHEMA.JOBS_BY_PROJECT` is your go-to for auditing
expensive queries and optimizing costs.

Complete the reading guide, lab, and quiz before the next module. In Module 13
we cover database security — encryption, IAM authentication, audit logging,
and VPC Service Controls.

---

*End of Part 2 Script*

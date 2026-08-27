# Reading Guide: Module 12 — BigQuery for Analytics

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Overview

This reading guide supports the Module 12 video lectures on BigQuery for Analytics.
By the end of this module, you will understand BigQuery's architecture, how to design
efficient datasets and tables, and how to optimize queries for cost and performance —
all essential knowledge for the Google Cloud Professional Database Engineer exam.

**Estimated reading time**: 60–75 minutes

---

## Section 1 — BigQuery Architecture

### 1.1 Dremel and the Multi-Level Serving Tree

BigQuery's query engine is based on Dremel, a technology Google developed internally
and published as a research paper in 2010. The core innovation is a **multi-level
serving tree** that distributes query work across thousands of leaf nodes simultaneously.

When a query arrives at the root server, it is parsed, optimized, and then divided into
sub-tasks that are dispatched down the tree. Each leaf node reads a slice of columnar
data from Google's distributed file system (Colossus) and computes a partial result.
Results flow back up through intermediate nodes that aggregate partial results until
the final result reaches the root and is returned to you.

This architecture achieves linear scaling: doubling the data doubles the number of
leaf nodes required, but query latency stays roughly constant. For the exam, remember
that Dremel's parallelism is what makes BigQuery fast — not special hardware or indexes.

### 1.2 Capacitor Columnar Storage Format

BigQuery stores data in Google's internal **Capacitor** format, which is a columnar
format optimized for Dremel's access patterns. Data is stored column-by-column rather
than row-by-row.

Columnar benefits:

- Only queried columns are read from disk.
- Column data compresses better than row data (repetitive values, sorted order).
- SIMD (Single Instruction Multiple Data) CPU operations work efficiently on column arrays.

For exam purposes: BigQuery achieves query performance through columnar I/O reduction,
not through traditional indexing like B-tree indexes in PostgreSQL or Cloud SQL.

### 1.3 Separation of Storage and Compute

BigQuery's storage (Colossus) and compute (Dremel) are completely decoupled. You are
billed separately for each:

- **Storage**: Per GB per month (active and long-term tiers)
- **Compute**: Per TB scanned (on-demand) or per slot commitment (flat-rate)

This separation means you can run high-compute analytics without storing large amounts
of data in BigQuery — for example, by using external tables over Cloud Storage files.

---

## Section 2 — Dataset and Table Management

### 2.1 Dataset Configuration

A BigQuery dataset is the top-level organizing unit within a project. Important
configuration options at dataset creation include:

**Location**: A single region (e.g., `us-central1`) or a multi-region (`US` or `EU`).
This decision is permanent and impacts where query jobs run, data residency compliance,
and cross-region replication.

**Default table expiration**: Optional. All tables in the dataset expire after this
number of seconds unless overridden at the table level.

**Default encryption**: By default, Google-managed encryption keys are used. You can
configure Cloud KMS customer-managed encryption keys (CMEK) at the dataset level.

**Access controls**: IAM roles can be granted at the project, dataset, or table level.
Dataset-level access is configured through the dataset's sharing settings.

### 2.2 Table Types Comparison

| Feature | Native Table | External Table | View | Materialized View |
|---|---|---|---|---|
| Data stored in BigQuery | Yes | No | No | Yes (aggregated) |
| Query performance | Best | Slower | Same as query | Fast (precomputed) |
| Auto-refresh | N/A | N/A | N/A | Yes |
| Storage cost | Yes | No (source billed) | No | Yes (smaller) |
| Supports partitioning | Yes | Limited | N/A | N/A |

### 2.3 Partitioning Strategies

**Ingestion-time partitioning** uses `_PARTITIONTIME` as the partition key. BigQuery
assigns each row to a partition based on when it was loaded. This is the simplest
approach but provides less control over partition boundaries.

**Column-based partitioning** on a DATE or TIMESTAMP column is more flexible and allows
historical data to be organized by its actual event date rather than its load date.

**Integer range partitioning** divides rows into ranges of an INTEGER column. You specify
the start, end, and interval:

```sql
CREATE TABLE txwes-analytics.sales_data.customers_by_age
PARTITION BY RANGE_BUCKET(age, GENERATE_ARRAY(0, 100, 10))
AS SELECT * FROM source_table;
```

This creates 10 partitions for age ranges: 0–9, 10–19, 20–29, and so on.

**Partition limits**:

- Maximum 4,000 partitions per table.
- Each partition can hold up to approximately 1 TB (soft guideline).
- Partition expiration can be set per-partition or as a default on the table.

### 2.4 Clustering Best Practices

Clustering sorts data within each partition according to the values of the cluster
columns. BigQuery maintains metadata about the value ranges in each data block, allowing
it to skip blocks that do not match a filter predicate.

Best cluster column choices:

- Columns frequently used in `WHERE` clauses
- Columns used in `GROUP BY` aggregations
- Columns used as `JOIN` keys
- High-cardinality columns (many distinct values) benefit most from clustering

Poor cluster column choices:

- Boolean columns (only 2 values, poor selectivity)
- Columns rarely used in queries
- Columns with extreme data skew

Recommended pattern for most fact tables: Partition by date, cluster by the most common
filter dimension (e.g., region or product_category).

---

## Section 3 — DML and DDL Operations

### 3.1 MERGE Statement Patterns

The `MERGE` statement is the most complex DML operation in BigQuery and a frequent
exam topic. The general pattern is:

```sql
MERGE target
USING source
ON join_condition
WHEN MATCHED AND condition THEN action
WHEN NOT MATCHED BY TARGET AND condition THEN action
WHEN NOT MATCHED BY SOURCE AND condition THEN action
```

The `WHEN NOT MATCHED BY SOURCE` clause handles rows in the target that have no
match in the source — useful for delete operations in CDC (Change Data Capture) pipelines.

### 3.2 Table Clones and Snapshots

BigQuery offers two zero-copy table duplication features:

**Table clone**: A copy of a table that starts identical to the source. Changes to the
clone are tracked separately and you are only billed for the delta (changed data).
Clones are writable — you can INSERT, UPDATE, DELETE, and even DROP the clone without
affecting the source.

**Table snapshot**: A read-only, point-in-time copy. Cannot be modified. Useful for
audit trails or rollback points before a destructive operation.

Creating a snapshot:

```sql
CREATE SNAPSHOT TABLE txwes-analytics.sales_data.orders_snapshot_20250601
CLONE txwes-analytics.sales_data.orders
FOR SYSTEM_TIME AS OF TIMESTAMP '2025-06-01 00:00:00 UTC';
```

### 3.3 Time Travel

BigQuery retains historical data for a configurable period (default 7 days). You can
query historical data using `FOR SYSTEM_TIME AS OF`:

```sql
SELECT *
FROM txwes-analytics.sales_data.orders
FOR SYSTEM_TIME AS OF TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 2 DAY);
```

This is useful for recovering accidentally deleted rows or debugging data pipelines.

---

## Section 4 — Views and Materialized Views

### 4.1 Authorized Views and Authorized Datasets

Authorized views allow a view to access data in another dataset, even if the users
querying the view do not have direct access to that dataset.

An **authorized dataset** extends this concept: an entire dataset can be authorized to
access another dataset. This simplifies permission management when multiple views in a
dataset all need access to the same source data.

### 4.2 Materialized View Incremental Refresh

When the base table for a materialized view receives new rows via `INSERT` or load jobs
(append-only changes), BigQuery can incrementally update the materialized view by
processing only the new data. This is significantly cheaper than recomputing the full view.

If the base table receives `UPDATE` or `DELETE` operations, BigQuery must perform a full
refresh of the materialized view. Design base tables to be append-only when possible.

### 4.3 Materialized View Query Rewriting

BigQuery's query optimizer automatically rewrites queries against base tables to use
materialized views when the materialized view can satisfy the query more efficiently.
This is called **smart tuning** or query rewriting.

Example: If a materialized view precomputes `SUM(revenue) GROUP BY order_date, region`,
then a query that selects `SUM(revenue)` filtered by a specific `region` can be satisfied
by scanning the materialized view (much smaller) rather than the base table.

---

## Section 5 — Cost Optimization

### 5.1 Pricing Summary

| Resource | On-Demand Rate | Notes |
|---|---|---|
| Storage (active) | ~$0.02/GB/month | Data modified in last 90 days |
| Storage (long-term) | ~$0.01/GB/month | Automatic after 90 days |
| Queries | ~$6.25/TB scanned | First 1 TB/month free |
| Streaming inserts | ~$0.01/200 MB | Real-time ingestion |

### 5.2 Cost Control Techniques

**Query dry run**: Before executing an expensive query, use `--dry_run` with the bq CLI
or check the query validator in the console. BigQuery returns the estimated bytes to be
scanned without actually running the query.

```bash
bq query \
  --use_legacy_sql=false \
  --dry_run \
  'SELECT SUM(revenue) FROM txwes-analytics.sales_data.orders WHERE order_date >= "2025-01-01"'
```

**Dataset and project quotas**: Set custom query quotas using the BigQuery Admin console
to limit maximum bytes processed per day per user or per project.

**BI Engine**: For dashboards and BI tools (Looker, Looker Studio), enable BigQuery BI
Engine, which caches data in-memory and reduces query costs for interactive workloads.

**Committed use discounts**: Flat-rate slot commitments offer 40–70% savings over
on-demand pricing for sustained workloads.

---

## Section 6 — Key Terms

**Dremel**: BigQuery's query execution engine using a multi-level serving tree.

**Capacitor**: BigQuery's internal columnar storage format.

**Slot**: One unit of BigQuery compute (approximately 1 virtual CPU).

**Partition pruning**: Skipping partitions that do not match a query's filter predicates.

**Clustering**: Physical co-location of rows with similar cluster column values within partitions.

**Materialized view**: A view whose query result is precomputed and stored, with automatic refresh.

**Authorized view**: A view granted access to a dataset's data without exposing that dataset to the view's users.

**Time travel**: Querying historical versions of BigQuery data using `FOR SYSTEM_TIME AS OF`.

**Table clone**: A zero-storage-cost copy of a table, billed only for deltas after cloning.

---

## Section 7 — Review Questions

Answer these questions to test your comprehension before taking the module quiz.

1. What two components does BigQuery's architecture separate, and why is this separation beneficial?

2. Explain the difference between partitioning and clustering. When would you use each?

3. A table has 500 billion rows partitioned by `order_date`. A query includes `WHERE region = 'Southwest'` but no date filter. Will partition pruning occur? Explain.

4. What is the difference between a view and a materialized view in BigQuery? When should you prefer each?

5. Explain the `WHEN NOT MATCHED BY SOURCE` clause in a `MERGE` statement. Give a use case.

6. What is an authorized view? Describe a scenario where it is necessary.

7. A BigQuery table was accidentally truncated 3 days ago. How can you recover the data?

8. What query optimization technique avoids a full table scan in BigQuery? What replaces traditional indexing?

9. Describe the difference between on-demand and flat-rate BigQuery pricing. For what type of workload is each better suited?

10. What is the `require_partition_filter` table option, and what problem does it solve?

---

## Section 8 — Certification Exam Alignment

The Google Cloud Professional Database Engineer exam tests BigQuery in the following areas:

- **Section 1 (Design)**: Choosing appropriate table design (partitioning, clustering, table type) for analytical workloads
- **Section 2 (Ingest and manage)**: Loading data into BigQuery, using DML, managing schemas
- **Section 3 (Migrate)**: Moving data to/from BigQuery as part of migration scenarios
- **Section 4 (Secure)**: Authorized views, dataset-level IAM, CMEK
- **Section 5 (Monitor)**: INFORMATION_SCHEMA queries, slot utilization, cost monitoring

Expect 4–6 BigQuery-focused questions on the exam, particularly around cost optimization
and security patterns.

---

## Recommended Resources

- Official BigQuery documentation: cloud.google.com/bigquery/docs
- BigQuery best practices guide: cloud.google.com/bigquery/docs/best-practices-performance-overview
- BigQuery pricing calculator: cloud.google.com/products/calculator
- Dremel paper (2010): research.google/pubs/pub36632/
- BigQuery SQL reference: cloud.google.com/bigquery/docs/reference/standard-sql/

---

---

## 9. Supplemental Resources

The following free, open-access resources support Module 12 topics:

**1. [BigQuery Documentation — Introduction to Partitioned Tables](https://cloud.google.com/bigquery/docs/partitioned-tables)**
Covers date, timestamp, and integer range partitioning strategies, partition pruning mechanics, and the `require_partition_filter` table option.

**2. [BigQuery Documentation — Introduction to Clustered Tables](https://cloud.google.com/bigquery/docs/clustered-tables)**
Explains clustering column selection, block-level pruning behavior, the interaction between partitioning and clustering, and best practices for high-cardinality columns.

**3. [BigQuery Documentation — Materialized Views](https://cloud.google.com/bigquery/docs/materialized-views-intro)**
Documents materialized view creation, incremental refresh, smart tuning query rewriting, and the `max_staleness` option for controlling refresh frequency.

**4. [BigQuery Documentation — Introduction to BigQuery Time Travel](https://cloud.google.com/bigquery/docs/time-travel)**
Explains the `FOR SYSTEM_TIME AS OF` clause, the 7-day time travel window, fail-safe retention, and how to use time travel for point-in-time recovery of accidentally deleted rows.

---

Module 12 Reading Guide — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.

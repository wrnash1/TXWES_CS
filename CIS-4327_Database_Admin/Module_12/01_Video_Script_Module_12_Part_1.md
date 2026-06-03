# Video Script: Module 12 — BigQuery for Analytics (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Database Engineer

---

## SLIDE 1 — Welcome and Module Overview

Welcome back to CIS-4327 Database Administration. I'm Professor Nash, and today we begin
Module 12, which focuses on BigQuery — Google Cloud's fully managed, serverless data warehouse
designed for large-scale analytics.

In Part 1 we cover BigQuery's architecture, the Dremel execution engine, columnar storage, and
how to manage datasets and tables. Part 2 will cover advanced table features, DML and DDL,
views, materialized views, and cost optimization strategies.

Let's get started.

---

## SLIDE 2 — What Is BigQuery?

BigQuery is Google Cloud's serverless, highly scalable data warehouse. It is designed to run
analytical SQL queries over petabyte-scale datasets in seconds to minutes.

Key characteristics:

- **Serverless**: No infrastructure to manage. Google handles compute allocation automatically.
- **Separated storage and compute**: Storage lives in Colossus (Google's distributed file system),
  and compute is handled by the Dremel engine. You pay for each independently.
- **ANSI SQL**: BigQuery uses standard SQL (ANSI 2011 compliant) so your existing SQL skills
  transfer directly.
- **Built-in ML**: BigQueryML lets you train machine learning models with SQL alone.

This architecture differs fundamentally from Cloud SQL or Spanner, which are OLTP systems
optimized for transactions. BigQuery is OLAP — Online Analytical Processing — built for
read-heavy, aggregation-heavy workloads.

---

## SLIDE 3 — Dremel: The Execution Engine

The Dremel paper, published by Google in 2010, describes the engine that powers BigQuery's
query execution. Understanding Dremel helps you understand why BigQuery is so fast.

Dremel uses a **multi-level serving tree** architecture:

- A root server receives the query.
- The query is split and dispatched to thousands of leaf nodes simultaneously.
- Each leaf node reads a small slice of columnar data from Colossus.
- Results are aggregated back up the tree to the root.

This massively parallel architecture means that adding more data does not slow down a query
proportionally — the work simply gets distributed across more leaf nodes.

The key insight: Dremel reads only the columns your query touches. A table with 100 columns
and a query that touches 3 columns reads roughly 3 percent of the data that a row-based
database would read. This is the columnar storage advantage.

---

## SLIDE 4 — Columnar Storage Deep Dive

Traditional row-based storage (like most OLTP databases) stores all columns of a row
together on disk. This is excellent for retrieving a single record by primary key but
inefficient for aggregations across millions of rows.

Columnar storage stores each column separately. When BigQuery runs `SELECT SUM(revenue)
FROM orders`, it only reads the revenue column — not order_id, customer_id, or any other
column.

Benefits of columnar storage:

- **Reduced I/O**: Only relevant columns are scanned.
- **Better compression**: Column values are often repetitive (e.g., a country code column),
  so run-length encoding and dictionary compression achieve very high ratios.
- **Vectorized processing**: CPU operations on column arrays are cache-friendly.

BigQuery uses the **Capacitor** columnar file format internally, which is optimized for
Dremel's access patterns. You do not interact with Capacitor directly, but knowing it exists
helps explain BigQuery's performance characteristics.

---

## SLIDE 5 — BigQuery Storage Model: Projects, Datasets, Tables

BigQuery organizes data in a three-level hierarchy:

1. **Project** — The GCP project that owns the resources and incurs billing.
2. **Dataset** — A logical container for tables and views. Think of it as a database or schema.
3. **Table** — The actual data storage unit, containing rows and columns.

A fully qualified table reference in BigQuery looks like this:

```
project_id.dataset_id.table_id
```

For example: `txwes-analytics.sales_data.orders`

This matters for the exam: when you write a cross-project query in BigQuery, you must use
the fully qualified name including the project ID.

---

## SLIDE 6 — Creating Datasets

To create a dataset in the Google Cloud Console:

1. Navigate to BigQuery in the console.
2. Click your project name in the Explorer panel.
3. Click **Create Dataset**.
4. Provide a Dataset ID, choose a data location (region or multi-region), and set the
   default table expiration if desired.

Using the bq CLI:

```bash
bq mk \
  --dataset \
  --location=US \
  --default_table_expiration=2592000 \
  txwes-analytics:sales_data
```

The `--default_table_expiration` is in seconds. 2,592,000 seconds equals 30 days.

Using the BigQuery API or Terraform:

```hcl
resource "google_bigquery_dataset" "sales_data" {
  dataset_id  = "sales_data"
  location    = "US"
  project     = "txwes-analytics"
}
```

**Important exam note**: Dataset location is set at creation and cannot be changed. Data
in a dataset can only be queried by jobs running in the same region (or any region for
multi-region datasets).

---

## SLIDE 7 — Creating Tables: Native, External, and Views

BigQuery supports three primary table types:

**Native tables** — Data is stored in BigQuery-managed Colossus storage. Best performance.

**External tables** — Data lives outside BigQuery (Cloud Storage, Cloud Spanner, Cloud SQL,
Google Sheets). BigQuery reads the data at query time. Useful for data that changes
frequently outside BigQuery or when you do not want to duplicate data.

**Views** — Saved SQL queries. No data is stored; the query runs each time the view is
queried. We cover views in depth in Part 2.

Creating a native table with DDL:

```sql
CREATE TABLE txwes-analytics.sales_data.orders (
  order_id    INT64,
  customer_id INT64,
  order_date  DATE,
  revenue     NUMERIC,
  region      STRING
);
```

Creating an external table pointing to Cloud Storage:

```sql
CREATE EXTERNAL TABLE txwes-analytics.sales_data.orders_ext
OPTIONS (
  format = 'CSV',
  uris   = ['gs://txwes-bucket/orders/*.csv']
);
```

---

## SLIDE 8 — Schema Design and Data Types

BigQuery supports a rich set of data types:

- **Numeric**: INT64, FLOAT64, NUMERIC (exact 38 digits, 9 decimal places), BIGNUMERIC
- **String**: STRING (UTF-8, up to 16 MB per value)
- **Date/Time**: DATE, TIME, DATETIME, TIMESTAMP
- **Boolean**: BOOL
- **Binary**: BYTES
- **Nested/Repeated**: RECORD (STRUCT) and ARRAY — these enable denormalized nested data

The **RECORD** and **ARRAY** types deserve special attention. BigQuery supports nested
and repeated fields, which allows you to store what would traditionally be a one-to-many
relationship in a single row. This is more efficient in columnar storage than joining
across tables.

Example: An `orders` table with a nested `line_items` array means you never join to get
line item data — it is already in the row.

For the exam, know that BigQuery does not enforce primary key or foreign key constraints
for data integrity. You can declare them as informational hints, but BigQuery will not
reject rows that violate them.

---

## SLIDE 9 — Partitioned Tables

Partitioning is one of the most important performance and cost optimization features in
BigQuery. A partitioned table is divided into segments called partitions, and each query
can be restricted to scan only the relevant partitions.

Three types of partitioning:

1. **Ingestion-time partitioning**: BigQuery automatically partitions rows by the time
   they were loaded. Use `_PARTITIONTIME` pseudo-column to filter.

2. **Column partitioning**: You specify a DATE, DATETIME, TIMESTAMP, or INTEGER column
   as the partition key.

3. **Integer range partitioning**: Partition by ranges of integer values (e.g., customer
   age groups).

Creating a date-partitioned table:

```sql
CREATE TABLE txwes-analytics.sales_data.orders_partitioned
PARTITION BY order_date
OPTIONS (require_partition_filter = true)
AS SELECT * FROM txwes-analytics.sales_data.orders;
```

The `require_partition_filter = true` option forces every query to include a partition
filter, preventing accidental full-table scans and runaway costs.

---

## SLIDE 10 — Partition Pruning

Partition pruning is the mechanism by which BigQuery skips partitions not needed by your
query. This directly reduces the bytes billed.

Example:

```sql
SELECT SUM(revenue)
FROM txwes-analytics.sales_data.orders_partitioned
WHERE order_date BETWEEN '2025-01-01' AND '2025-03-31';
```

BigQuery reads only the three monthly partitions (or 90 daily partitions) covering that
date range, rather than the entire table.

Best practices for partitioning:

- Choose a partition column that matches your most common filter predicates.
- Avoid partitioning on columns with very high cardinality (e.g., order_id) — use
  clustering for that.
- BigQuery supports a maximum of 4,000 partitions per table.

---

## SLIDE 11 — Clustered Tables

Clustering is complementary to partitioning. Within each partition, BigQuery can
physically sort and co-locate rows based on cluster column values. When you filter or
aggregate on cluster columns, BigQuery reads only the relevant blocks of data.

Creating a partitioned and clustered table:

```sql
CREATE TABLE txwes-analytics.sales_data.orders_optimized
PARTITION BY order_date
CLUSTER BY region, customer_id
AS SELECT * FROM txwes-analytics.sales_data.orders;
```

Rules for clustering:

- Up to 4 cluster columns, evaluated left to right.
- Cluster columns must be top-level, non-repeated columns.
- Works best when the cluster columns appear frequently in WHERE, GROUP BY, or JOIN
  conditions.

The cost benefit: BigQuery provides a **bytes billed estimate** before query execution
(dry run). Partitioning and clustering together can reduce this estimate by 90 percent
or more on well-designed tables.

---

## SLIDE 12 — Exam Checkpoint — Part 1 Concepts

Before we move to Part 2, let's review the key concepts covered so far:

- BigQuery is a serverless OLAP data warehouse — not an OLTP system
- Dremel uses a multi-level serving tree for massively parallel query execution
- Columnar storage reads only the columns your query needs, reducing I/O dramatically
- The hierarchy is Project → Dataset → Table
- Dataset location is immutable after creation
- Partitioning (date/integer/ingestion-time) enables partition pruning to reduce scan cost
- Clustering co-locates data within partitions for filter-based optimizations
- `require_partition_filter = true` prevents accidental full-table scans

In Part 2, we cover DML and DDL operations in BigQuery, views and materialized views,
and cost optimization strategies including slot reservations, query best practices,
and the BigQuery pricing model.

See you in Part 2.

---

*End of Part 1 Script*

# Video Script: Module 12 — BigQuery and Data Analytics (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 12. I am Professor Nash. Today we cover BigQuery — Google Cloud's
serverless, fully managed data warehouse — and the broader data analytics ecosystem on
GCP.

BigQuery is one of GCP's flagship services and appears consistently on the ACE exam. You
will be expected to understand its architecture, create datasets and tables, run SQL
queries, and apply cost optimization techniques like partitioning and clustering.

By the end of this two-part video you will be able to create and query BigQuery datasets,
understand partitioned and clustered tables, use Looker Studio for visualization, and
apply the key cost and performance optimization patterns.

---

### Section 1: BigQuery Architecture

BigQuery is a fully managed, serverless data warehouse. Unlike traditional databases
where compute and storage are tightly coupled in the same server, BigQuery separates
storage and compute:

- **Storage** — data is stored in Google's Colossus distributed file system in a
  columnar format (Capacitor); you are charged per GB stored per month
- **Compute (slots)** — query execution uses BigQuery slots (units of CPU, memory, and
  networking); on-demand queries use shared slots; reserved capacity uses dedicated slots
- **Serverless** — no instances to provision, no clusters to manage; Google scales
  compute automatically for each query

This architecture means BigQuery can run petabyte-scale queries in seconds without any
infrastructure management.

#### BigQuery Resource Hierarchy

```text
GCP Project
  └── BigQuery Dataset
        ├── Table (native)
        ├── External Table (over GCS, Sheets, etc.)
        └── View (saved SQL query)
```

A **dataset** is the top-level container. Every table belongs to a dataset. Datasets
have a location (US, EU, or a specific region) that cannot be changed after creation.
Data residency and IAM permissions are set at the dataset level.

---

### Section 2: Creating Datasets and Tables

```bash
# Create a dataset in US multi-region
bq mk --dataset \
  --location=US \
  --description="Sales analytics dataset" \
  MY_PROJECT:sales_data

# List datasets
bq ls MY_PROJECT:

# Create a table with an inline schema
bq mk --table \
  MY_PROJECT:sales_data.orders \
  order_id:INTEGER,customer_id:INTEGER,order_date:DATE,amount:FLOAT,status:STRING

# Show table schema
bq show MY_PROJECT:sales_data.orders

# Load data from Cloud Storage (CSV)
bq load \
  --source_format=CSV \
  --skip_leading_rows=1 \
  MY_PROJECT:sales_data.orders \
  gs://my-bucket/orders.csv \
  order_id:INTEGER,customer_id:INTEGER,order_date:DATE,amount:FLOAT,status:STRING

# Load data from Cloud Storage (JSON)
bq load \
  --source_format=NEWLINE_DELIMITED_JSON \
  MY_PROJECT:sales_data.orders \
  gs://my-bucket/orders.json \
  order_id:INTEGER,customer_id:INTEGER,order_date:DATE,amount:FLOAT,status:STRING
```

---

### Section 3: Running SQL Queries

BigQuery supports standard SQL (ANSI 2011) with GCP extensions. You can run queries
from the Cloud Console, the bq CLI, or the BigQuery API.

```bash
# Run a query from the CLI
bq query \
  --use_legacy_sql=false \
  'SELECT
     status,
     COUNT(*) AS order_count,
     SUM(amount) AS total_revenue
   FROM `MY_PROJECT.sales_data.orders`
   WHERE order_date >= "2024-01-01"
   GROUP BY status
   ORDER BY total_revenue DESC'

# Run a query and save results to a destination table
bq query \
  --use_legacy_sql=false \
  --destination_table=MY_PROJECT:sales_data.monthly_summary \
  --replace \
  'SELECT
     FORMAT_DATE("%Y-%m", order_date) AS month,
     SUM(amount) AS revenue
   FROM `MY_PROJECT.sales_data.orders`
   GROUP BY month
   ORDER BY month'
```

Always use `--use_legacy_sql=false` — legacy SQL is an older dialect and is not tested
on the ACE exam.

---

### Section 4: Partitioned Tables

Partitioning divides a table into segments based on a column value. BigQuery only scans
the partitions relevant to your query, dramatically reducing cost and improving
performance.

#### Partition Types

- **Date/timestamp partitioning** — one partition per day, month, or year based on a
  DATE, TIMESTAMP, or DATETIME column
- **Integer range partitioning** — partition by an integer column with specified ranges
- **Ingestion-time partitioning** — automatically partitions rows by the time they were
  loaded into BigQuery

```bash
# Create a date-partitioned table
bq mk --table \
  --time_partitioning_field=order_date \
  --time_partitioning_type=DAY \
  MY_PROJECT:sales_data.orders_partitioned \
  order_id:INTEGER,customer_id:INTEGER,order_date:DATE,amount:FLOAT,status:STRING

# Query a specific partition (only scans that day's data)
bq query \
  --use_legacy_sql=false \
  'SELECT COUNT(*) FROM `MY_PROJECT.sales_data.orders_partitioned`
   WHERE order_date = "2024-01-15"'
```

The `WHERE order_date = "2024-01-15"` clause is called **partition pruning** — BigQuery
reads only the January 15, 2024 partition instead of the entire table. Without
partitioning, the same query scans every row in the table.

#### Require Partition Filter

```bash
# Create a table that requires a partition filter on every query
bq mk --table \
  --time_partitioning_field=order_date \
  --time_partitioning_type=DAY \
  --require_partition_filter=true \
  MY_PROJECT:sales_data.orders_strict_part \
  order_id:INTEGER,customer_id:INTEGER,order_date:DATE,amount:FLOAT
```

With `--require_partition_filter=true`, any query that does not include a filter on the
partition column is rejected. This prevents accidental full-table scans.

---

### Section 5: Clustered Tables

Clustering sorts table data by one or more columns within each partition. When a query
filters or aggregates on a clustered column, BigQuery skips blocks of data that do not
match — reducing the bytes scanned beyond what partitioning alone can achieve.

```bash
# Create a partitioned and clustered table
# Clustered by customer_id and status
bq mk --table \
  --time_partitioning_field=order_date \
  --time_partitioning_type=DAY \
  --clustering_fields=customer_id,status \
  MY_PROJECT:sales_data.orders_clustered \
  order_id:INTEGER,customer_id:INTEGER,order_date:DATE,amount:FLOAT,status:STRING
```

A query that filters on `customer_id` and `status` in a clustered table will scan
significantly fewer bytes than the same query on an unclustered table.

**ACE rule**: Use partitioning for time-based queries (always filter by date range).
Use clustering for high-cardinality filter columns within a partition (customer IDs,
product categories, regions).

---

### Closing — Part 1

In Part 1 we covered:

- BigQuery architecture: separated storage and compute, serverless scaling
- Dataset and table creation with the bq CLI
- Standard SQL queries and destination tables
- Partitioned tables: date partitioning, partition pruning, require\_partition\_filter
- Clustered tables: block-level skipping for filter columns

In Part 2 we cover BigQuery pricing and cost optimization, Looker Studio integration,
authorized views for data sharing, and the ACE exam patterns for BigQuery.

See you in Part 2.

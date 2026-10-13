# Video Script: Module 12 — BigQuery and Data Analytics (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction to Part 2

Welcome back. In Part 1 we covered BigQuery's architecture, creating tables, running
queries, partitioning, and clustering. In Part 2 we cover pricing models, cost
optimization, Looker Studio integration, authorized views, and the ACE exam patterns.

---

### Section 1: BigQuery Pricing Model

BigQuery charges for two main things:

- **Storage** — active storage costs approximately $0.02 per GB per month; long-term
  storage (tables not modified for 90 days) costs approximately $0.01 per GB per month
- **Query processing** — on-demand pricing charges approximately $5.00 per TB of data
  scanned; the first 1 TB per month is free

There is no charge for loading data from Cloud Storage, exporting data to Cloud Storage,
or for cached query results.

#### On-Demand vs. Reservations

- **On-demand** — you pay per TB scanned; no upfront commitment; suitable for
  intermittent or unpredictable workloads
- **Reservations (slots)** — you purchase a fixed number of BigQuery slots for a flat
  monthly rate; best for large, predictable workloads where the per-TB cost of on-demand
  would be higher

For the ACE exam, on-demand pricing with partitioned tables is the standard answer for
cost optimization questions. Slot reservations are for enterprise scenarios with
consistent heavy query workloads.

---

### Section 2: Cost Optimization Techniques

#### Estimate Query Cost Before Running

Use the Cloud Console's query validator or the `--dry_run` flag to estimate bytes
scanned before executing:

```bash
# Dry run — estimates bytes processed without executing
bq query \
  --use_legacy_sql=false \
  --dry_run \
  'SELECT order_id, amount
   FROM `MY_PROJECT.sales_data.orders`
   WHERE order_date >= "2024-01-01"'
```

The output shows `Statement would process X bytes` — multiply by $5/TB to estimate cost.

#### Select Only Needed Columns

BigQuery charges for bytes scanned per column due to its columnar storage. Always
select specific columns rather than `SELECT *`:

```sql
-- Expensive: scans all columns
SELECT * FROM `MY_PROJECT.sales_data.orders`

-- Cheaper: scans only 2 columns
SELECT order_id, amount FROM `MY_PROJECT.sales_data.orders`
```

#### Use Materialized Views

Materialized views precompute and cache query results. Subsequent queries against the
materialized view scan cached data instead of the base table:

```sql
CREATE MATERIALIZED VIEW `MY_PROJECT.sales_data.daily_revenue_mv`
AS
SELECT
  order_date,
  SUM(amount) AS daily_revenue
FROM `MY_PROJECT.sales_data.orders_partitioned`
GROUP BY order_date;
```

BigQuery automatically refreshes materialized views when the base table changes.

---

### Section 3: External Tables and Federated Queries

BigQuery can query data stored outside BigQuery without loading it first. This is called
a **federated query** via an **external table**.

Supported sources:

- Cloud Storage (CSV, JSON, Avro, Parquet, ORC)
- Google Sheets
- Cloud Bigtable
- Cloud SQL (via BigQuery Omni or direct federation)

```bash
# Create an external table over a Cloud Storage CSV
bq mk --table \
  --external_table_definition=CSV=gs://my-bucket/data/*.csv \
  MY_PROJECT:sales_data.external_orders

# Query the external table directly
bq query \
  --use_legacy_sql=false \
  'SELECT COUNT(*) FROM `MY_PROJECT.sales_data.external_orders`'
```

External tables are useful for one-time analysis of files already in Cloud Storage
without incurring the cost and time of loading them into BigQuery native storage.

---

### Section 4: Authorized Views

An authorized view allows you to share a subset of a table's data with another project
or user without granting access to the underlying table.

```bash
# Step 1: Create a view that filters sensitive columns
bq query \
  --use_legacy_sql=false \
  'CREATE VIEW `MY_PROJECT.sales_data.orders_public` AS
   SELECT order_id, order_date, status
   FROM `MY_PROJECT.sales_data.orders`'

# Step 2: Authorize the view to access the source dataset
# (done via the dataset's authorized views configuration in the Console or API)

# Step 3: Grant the consumer project/user access to the view dataset only
# They can query the view but cannot access the underlying orders table
```

Authorized views are tested on the ACE exam as the correct mechanism for data sharing
across projects without exposing raw tables.

---

### Section 5: Looker Studio Integration

Looker Studio (formerly Google Data Studio) is Google's free business intelligence and
visualization tool. It connects directly to BigQuery and renders charts, dashboards, and
reports from live BigQuery data.

```text
BigQuery Dataset → Looker Studio Data Source → Looker Studio Report (charts, tables)
```

To connect:

1. Open Looker Studio at `lookerstudio.google.com`
2. Click **Create** → **Report** → **Add data**
3. Select **BigQuery** as the connector
4. Choose your project, dataset, and table or enter a custom query
5. Build charts using drag-and-drop

Looker Studio queries BigQuery on every report refresh. To reduce BigQuery costs, use
BigQuery extract caches or schedule data extracts to Cloud Storage and connect Looker
Studio to the cached files instead.

---

### Section 6: ACE Exam BigQuery Patterns

Common ACE exam question patterns for BigQuery:

**Cost reduction** — "How do you reduce the cost of running a daily report query on a
large table?" Answer: Partition the table by date and filter on the partition column.
Also consider clustering on frequently filtered columns.

**Data sharing** — "How do you give another team access to a subset of a table without
sharing the underlying data?" Answer: Create an authorized view.

**Schema evolution** — BigQuery supports adding new columns to an existing table without
dropping and recreating it. You can also add columns via load jobs that include new
fields.

**Streaming inserts** — BigQuery supports streaming inserts for near-real-time data
ingestion via the `insertAll` API. Streaming data is immediately queryable but has a
small per-row cost. Standard batch loads from GCS are free.

```bash
# BigQuery table info and statistics
bq show --format=prettyjson MY_PROJECT:sales_data.orders

# List all tables in a dataset
bq ls MY_PROJECT:sales_data

# Copy a table to another dataset
bq cp MY_PROJECT:sales_data.orders MY_PROJECT:sales_backup.orders_backup

# Delete a table
bq rm --table MY_PROJECT:sales_data.orders_backup

# Delete a dataset and all its tables
bq rm --recursive --dataset MY_PROJECT:old_dataset
```

---

### Module 12 Summary

Module 12 covered BigQuery and Data Analytics on GCP:

- **Architecture** — separated storage and compute; serverless; columnar format
- **Datasets and tables** — bq CLI for creation, loading, and querying
- **Partitioning** — date partitioning for time-range query cost reduction
- **Clustering** — block-level skipping for high-cardinality filter columns
- **Cost optimization** — dry\_run, column selection, materialized views, reservations
- **Authorized views** — secure cross-project data sharing
- **Looker Studio** — live BigQuery-connected visualization and dashboards

For the ACE exam: partitioning + clustering = cost optimization; authorized views = data
sharing; on-demand pricing = per-TB scanned; always use standard SQL, not legacy SQL.

Complete the lab, take the quiz, and join the discussion. Module 13 covers CI/CD with
Cloud Build and Artifact Registry.

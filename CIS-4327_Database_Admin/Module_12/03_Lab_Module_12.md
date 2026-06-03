# Lab Activity: Module 12 — BigQuery for Analytics

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Lab Overview

**Title**: Designing and Optimizing BigQuery Tables for Analytical Workloads

**Estimated Time**: 90 minutes

**Difficulty**: Intermediate

In this lab you will create a BigQuery dataset, build native partitioned and clustered
tables, practice DML operations including MERGE, create a materialized view, and use
INFORMATION_SCHEMA to audit query costs. You will also validate that partition pruning
and clustering reduce bytes scanned compared to an unoptimized baseline table.

---

## Prerequisites

- Active Google Cloud project with billing enabled
- BigQuery API enabled
- Cloud Shell or local gcloud SDK authenticated
- Owner or BigQuery Admin role on the project

---

## Lab Objectives

By the end of this lab, you will be able to:

1. Create a BigQuery dataset with appropriate location and expiration settings
2. Create a partitioned and clustered table using DDL
3. Demonstrate partition pruning by comparing bytes scanned with and without filters
4. Execute INSERT, UPDATE, and MERGE DML statements
5. Create a materialized view and observe query rewriting
6. Query INFORMATION_SCHEMA to audit job-level cost metrics

---

## Part 1 — Environment Setup

### Step 1.1 — Open Cloud Shell

Navigate to console.cloud.google.com and open Cloud Shell (the terminal icon in the
top navigation bar). All commands in this lab run in Cloud Shell unless otherwise noted.

Set your project:

```bash
export PROJECT_ID=$(gcloud config get-value project)
echo "Project: $PROJECT_ID"
```

### Step 1.2 — Create the Lab Dataset

```bash
bq mk \
  --dataset \
  --location=US \
  --description="CIS-4327 Module 12 Lab Dataset" \
  ${PROJECT_ID}:cis4327_lab
```

Verify the dataset was created:

```bash
bq ls --datasets ${PROJECT_ID}
```

---

## Part 2 — Table Creation and Baseline Query

### Step 2.1 — Create an Unoptimized Baseline Table

Open the BigQuery console (console.cloud.google.com/bigquery) and run the following
DDL to create a baseline table with no partitioning or clustering, populated from
a public dataset:

```sql
CREATE OR REPLACE TABLE `cis4327_lab.orders_baseline` AS
SELECT
  CAST(FLOOR(RAND() * 10000000) AS INT64)         AS order_id,
  CAST(FLOOR(RAND() * 100000)  AS INT64)          AS customer_id,
  DATE_ADD(DATE '2022-01-01',
    INTERVAL CAST(FLOOR(RAND() * 730) AS INT64) DAY) AS order_date,
  ROUND(RAND() * 5000, 2)                         AS revenue,
  CASE CAST(FLOOR(RAND() * 5) AS INT64)
    WHEN 0 THEN 'Northeast'
    WHEN 1 THEN 'Southeast'
    WHEN 2 THEN 'Midwest'
    WHEN 3 THEN 'Southwest'
    ELSE 'West'
  END                                             AS region,
  CASE CAST(FLOOR(RAND() * 3) AS INT64)
    WHEN 0 THEN 'Electronics'
    WHEN 1 THEN 'Apparel'
    ELSE 'Home'
  END                                             AS category
FROM UNNEST(GENERATE_ARRAY(1, 5000000));
```

This creates a 5-million-row synthetic orders table. Wait for the job to complete
(approximately 30–60 seconds).

### Step 2.2 — Run a Baseline Query and Note Bytes Scanned

In the BigQuery console, run the following query and record the "Bytes processed"
shown in the Job information panel:

```sql
SELECT region, SUM(revenue) AS total_revenue, COUNT(*) AS order_count
FROM `cis4327_lab.orders_baseline`
WHERE order_date BETWEEN '2023-01-01' AND '2023-06-30'
  AND region = 'Southwest'
GROUP BY region;
```

Record the bytes processed: ____________________

---

## Part 3 — Partitioned and Clustered Table

### Step 3.1 — Create Optimized Table

```sql
CREATE OR REPLACE TABLE `cis4327_lab.orders_optimized`
PARTITION BY order_date
CLUSTER BY region, category
OPTIONS (require_partition_filter = false)
AS SELECT * FROM `cis4327_lab.orders_baseline`;
```

### Step 3.2 — Run the Same Query on the Optimized Table

```sql
SELECT region, SUM(revenue) AS total_revenue, COUNT(*) AS order_count
FROM `cis4327_lab.orders_optimized`
WHERE order_date BETWEEN '2023-01-01' AND '2023-06-30'
  AND region = 'Southwest'
GROUP BY region;
```

Record the bytes processed: ____________________

**Lab Question 1**: Calculate the percentage reduction in bytes scanned. Express
your answer as: (baseline_bytes - optimized_bytes) / baseline_bytes * 100.

### Step 3.3 — Enable Required Partition Filter

```sql
ALTER TABLE `cis4327_lab.orders_optimized`
SET OPTIONS (require_partition_filter = true);
```

Attempt to run a query without a partition filter and observe the error:

```sql
-- This should fail with a partition filter required error
SELECT COUNT(*) FROM `cis4327_lab.orders_optimized`;
```

Record the error message: ____________________

---

## Part 4 — DML Operations

### Step 4.1 — INSERT New Rows

```sql
INSERT INTO `cis4327_lab.orders_optimized`
  (order_id, customer_id, order_date, revenue, region, category)
VALUES
  (99000001, 55001, '2025-01-15', 850.00, 'Southwest', 'Electronics'),
  (99000002, 55002, '2025-01-16', 2200.00, 'Midwest', 'Apparel'),
  (99000003, 55003, '2025-01-17', 420.50, 'West', 'Home');
```

Verify the inserts:

```sql
SELECT * FROM `cis4327_lab.orders_optimized`
WHERE order_date = '2025-01-15'
  AND order_id >= 99000000;
```

### Step 4.2 — UPDATE Rows

```sql
UPDATE `cis4327_lab.orders_optimized`
SET revenue = revenue * 1.1
WHERE order_id IN (99000001, 99000002, 99000003)
  AND order_date >= '2025-01-01';
```

Verify the update:

```sql
SELECT order_id, revenue
FROM `cis4327_lab.orders_optimized`
WHERE order_id IN (99000001, 99000002, 99000003)
  AND order_date >= '2025-01-01';
```

### Step 4.3 — MERGE (Upsert) Operation

Create a staging table and execute a MERGE:

```sql
CREATE OR REPLACE TABLE `cis4327_lab.orders_staging` AS
SELECT
  99000001 AS order_id, 55001 AS customer_id,
  DATE '2025-01-15' AS order_date, 999.99 AS revenue,
  'Southwest' AS region, 'Electronics' AS category
UNION ALL
SELECT 99000099, 55099, DATE '2025-02-01', 1500.00, 'Northeast', 'Apparel';
```

```sql
MERGE `cis4327_lab.orders_optimized` AS target
USING `cis4327_lab.orders_staging` AS source
ON target.order_id = source.order_id
   AND target.order_date = source.order_date
WHEN MATCHED THEN
  UPDATE SET revenue = source.revenue, category = source.category
WHEN NOT MATCHED THEN
  INSERT (order_id, customer_id, order_date, revenue, region, category)
  VALUES (source.order_id, source.customer_id, source.order_date,
          source.revenue, source.region, source.category);
```

**Lab Question 2**: How many rows were updated versus inserted by the MERGE?
Verify by querying the target table for both order_id values.

---

## Part 5 — Materialized View

### Step 5.1 — Create a Materialized View

```sql
CREATE MATERIALIZED VIEW `cis4327_lab.daily_revenue_mv`
OPTIONS (enable_refresh = true, refresh_interval_minutes = 60)
AS
SELECT
  order_date,
  region,
  category,
  SUM(revenue)  AS total_revenue,
  COUNT(*)      AS order_count
FROM `cis4327_lab.orders_optimized`
GROUP BY order_date, region, category;
```

Wait approximately 60 seconds for the initial refresh to complete.

### Step 5.2 — Query the Materialized View Directly

```sql
SELECT region, SUM(total_revenue) AS revenue
FROM `cis4327_lab.daily_revenue_mv`
WHERE order_date BETWEEN '2023-01-01' AND '2023-03-31'
GROUP BY region
ORDER BY revenue DESC;
```

Record the bytes processed: ____________________

**Lab Question 3**: Compare bytes scanned for this query against the same query on
`orders_optimized`. What is the reduction, and why?

---

## Part 6 — INFORMATION_SCHEMA Audit

### Step 6.1 — Query Job History

Run the following query to review all jobs from your lab session:

```sql
SELECT
  job_id,
  statement_type,
  total_bytes_processed,
  total_slot_ms,
  ROUND(total_bytes_processed / POW(1024,3), 2) AS gb_processed,
  creation_time
FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
WHERE creation_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 2 HOUR)
  AND state = 'DONE'
ORDER BY total_bytes_processed DESC
LIMIT 20;
```

**Lab Question 4**: Which query in your session processed the most bytes? Which
processed the least? What is the ratio between them?

---

## Lab Deliverables

Submit a document containing:

1. The bytes scanned values from Steps 2.2, 3.2, and 5.2 with calculated reductions
2. The error message from the required partition filter test (Step 3.3)
3. Answers to Lab Questions 1 through 4
4. A screenshot of the INFORMATION_SCHEMA query result from Part 6
5. One paragraph explaining which optimization (partitioning, clustering, or
   materialized views) provided the most benefit in your lab and why

---

## Cleanup

To avoid ongoing storage charges, delete the lab dataset when finished:

```bash
bq rm -r -f ${PROJECT_ID}:cis4327_lab
```

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 2 baseline query executed and bytes recorded | 10 |
| Part 3 optimized table created correctly | 15 |
| Partition filter error demonstrated | 10 |
| Part 4 DML (INSERT, UPDATE, MERGE) all successful | 25 |
| Part 5 materialized view created and queried | 20 |
| Part 6 INFORMATION_SCHEMA query and analysis | 10 |
| Written deliverable paragraph | 10 |
| **Total** | **100** |

---

Module 12 Lab — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.

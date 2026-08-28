# Reading Guide: Module 12 — BigQuery and Data Analytics

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4329 &BULL; GOOGLE CLOUD PLATFORM (GCP) CLOUD ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This reading guide accompanies the Module 12 video lectures on BigQuery and Data
Analytics. It covers BigQuery architecture, datasets and tables, SQL queries, partitioning,
clustering, cost optimization, and Looker Studio integration.

**Estimated reading time**: 60–75 minutes

---

### Learning Objectives

After completing this module's readings you will be able to:

- Describe BigQuery's separated storage and compute architecture
- Create datasets and tables using the bq CLI
- Run standard SQL queries and save results to destination tables
- Explain date partitioning and partition pruning and how they reduce query cost
- Describe clustering and when to use it alongside partitioning
- Apply BigQuery cost optimization techniques including dry\_run and column selection
- Explain authorized views for secure cross-project data sharing
- Connect a BigQuery dataset to Looker Studio

---

### Required Reading 1: BigQuery Architecture

**Source**: Google Cloud Documentation — BigQuery Overview

**URL**: `https://cloud.google.com/bigquery/docs/introduction`

#### BigQuery Architecture Key Terms

- **Columnar storage**: BigQuery stores each column of a table separately (Capacitor
  format); queries that select only a few columns scan only those columns' bytes
- **Dremel**: The internal query execution engine that powers BigQuery; processes SQL
  queries across a massively parallel tree of workers
- **Slot**: The unit of BigQuery compute; one slot is one virtual CPU with associated
  memory; on-demand queries draw from a shared slot pool
- **Dataset**: The top-level container for BigQuery tables and views; has a geographic
  location that cannot be changed after creation
- **Table**: A structured collection of rows and columns within a dataset; supports
  native (managed), external, and materialized view types
- **View**: A saved SQL query that behaves like a table; does not store data; queries
  against a view execute the underlying SQL each time

#### BigQuery Architecture ACE Exam Focus Points

- BigQuery separates storage (Colossus) and compute (Dremel); this is why it can scale
  queries independently of storage size
- Dataset location determines data residency; US and EU are multi-region; specific
  regions (us-central1, europe-west1) are single-region
- You cannot change a dataset's location after creation; you must create a new dataset
  and copy data
- BigQuery does not require schema-on-write for JSON loads with auto-detect; schema
  can be inferred from data
- There are no indexes in BigQuery; query performance is controlled via partitioning,
  clustering, and materialized views

#### BigQuery Architecture Review Questions

1. What does it mean that BigQuery uses columnar storage, and how does this affect
   query cost?
2. What is a BigQuery slot, and how does on-demand pricing differ from slot reservations?
3. Why does dataset location matter for compliance?

---

### Required Reading 2: Partitioned Tables

**Source**: Google Cloud Documentation — Introduction to partitioned tables

**URL**: `https://cloud.google.com/bigquery/docs/partitioned-tables`

#### Partitioned Tables Key Terms

- **Partition**: A segment of a table containing rows that share the same partition
  column value; stored separately in BigQuery's internal layout
- **Partition pruning**: The query optimizer's elimination of partitions that cannot
  contain rows matching the WHERE clause; reduces bytes scanned
- **Date/time partition**: Partitions based on a DATE, TIMESTAMP, or DATETIME column;
  one partition per day, month, or year
- **Ingestion-time partition**: Automatically partitions rows by the time they are
  loaded into BigQuery; accessed via the pseudo-column `_PARTITIONTIME`
- **Partition expiration**: Automatic deletion of partitions older than a specified
  number of days; configured per table
- **Require partition filter**: A table property that rejects queries that do not
  include a filter on the partition column; prevents accidental full-table scans

#### Partitioned Tables ACE Exam Focus Points

- Partitioning is the primary cost optimization for tables queried by date range
- A query that filters on the partition column triggers partition pruning; without
  the filter, BigQuery scans all partitions
- `--require_partition_filter=true` prevents full-table scans at the cost of requiring
  every query to specify a date range
- Partition expiration automatically deletes old data to control storage costs and
  data retention policies
- You can add partitioning to a new table at creation time; you cannot add partitioning
  to an existing non-partitioned table without recreating it

#### Partitioned Tables Review Questions

1. What is partition pruning and how does it reduce BigQuery query cost?
2. What does `--require_partition_filter=true` enforce, and when would you use it?
3. What is the difference between date/time partitioning and ingestion-time partitioning?

---

### Required Reading 3: Clustered Tables

**Source**: Google Cloud Documentation — Introduction to clustered tables

**URL**: `https://cloud.google.com/bigquery/docs/clustered-tables`

#### Clustered Tables Key Terms

- **Clustering**: A table organization technique that sorts data by one to four columns
  within each partition; BigQuery skips data blocks that cannot match filter criteria
- **Cluster columns**: The columns BigQuery sorts by; order matters (first column
  benefits most from filtering)
- **Block-level skipping**: BigQuery's ability to skip entire storage blocks based on
  min/max statistics per block for clustered columns
- **Co-location**: Rows with the same cluster column values are stored physically close
  together; reduces I/O for filtered queries

#### When to Use Clustering vs. Partitioning

Partitioning and clustering are complementary, not alternatives:

- Use partitioning for time-range filters (e.g., WHERE date >= "2024-01-01")
- Use clustering for high-cardinality filter columns within a partition (e.g., WHERE
  customer\_id = 12345 or WHERE region = "west")
- A table can be both partitioned and clustered simultaneously

#### Clustered Tables ACE Exam Focus Points

- Clustering works best when queries frequently filter on the same columns
- Unlike partitions (which are exact boundaries), clustering provides block-level cost
  reduction that varies based on data distribution
- BigQuery automatically re-clusters tables over time as new data is added
- Clustering columns should be high-cardinality columns that appear frequently in WHERE
  clauses or JOIN conditions

---

### Required Reading 4: Cost Optimization

**Source**: Google Cloud Documentation — BigQuery best practices for controlling costs

**URL**: `https://cloud.google.com/bigquery/docs/best-practices-costs`

#### Cost Optimization Key Terms

- **Dry run**: A query execution mode that estimates bytes processed without running the
  query; activated with `--dry_run` in bq CLI or the Cloud Console estimate
- **Column selection**: Only selecting needed columns reduces bytes scanned; critical
  in columnar storage where each column is billed separately
- **Materialized view**: A precomputed query result stored in BigQuery; queries hitting
  the materialized view scan cached data instead of the base table
- **Long-term storage pricing**: Tables not modified for 90 consecutive days
  automatically qualify for the reduced long-term storage rate (approximately half of
  active storage price)
- **Query cache**: BigQuery caches identical query results for 24 hours; repeated
  identical queries hit the cache at no charge

#### Cost Optimization ACE Exam Focus Points

- `SELECT *` in BigQuery is expensive because it reads all columns; always select only
  the columns you need
- The dry\_run estimate is shown in the Cloud Console's query validator automatically;
  review it before executing large queries
- Streaming inserts have a per-row charge; batch loads from Cloud Storage are free
- The query cache applies to identical queries against unchanged tables; cache is
  automatically invalidated when the table changes

---

### Required Reading 5: Authorized Views and Data Sharing

**Source**: Google Cloud Documentation — Authorized views

**URL**: `https://cloud.google.com/bigquery/docs/authorized-views`

#### Authorized Views Key Terms

- **Authorized view**: A view that has been granted permission to access the underlying
  table even when the view's requester does not have direct access to that table
- **Source dataset**: The dataset containing the underlying table that the view queries
- **View dataset**: A separate dataset where the authorized view is created and shared
  with consumers
- **Row-level security**: Authorized views can filter rows based on the viewer's
  identity using `SESSION_USER()` in the view's WHERE clause

#### Authorized Views ACE Exam Focus Points

- Authorized views allow data sharing without granting direct table access; the consumer
  sees only the rows and columns defined in the view
- The view must be authorized on the source dataset (in addition to granting the consumer
  access to the view dataset)
- Authorized views are the standard ACE exam answer for "share data with another project
  without exposing the raw table"
- VPC Service Controls can further restrict BigQuery access to specific VPC networks

---

### Pre-Lab Checklist

Before starting Lab 12, confirm you can answer yes to each item:

- I can create a BigQuery dataset and table using the bq CLI
- I can write a standard SQL query with GROUP BY and WHERE clauses
- I understand what partition pruning is and how to trigger it with a WHERE clause
- I know the difference between partitioning and clustering
- I can estimate query cost using the dry\_run flag

---

### Additional Resources

- BigQuery documentation:
  `https://cloud.google.com/bigquery/docs`
- BigQuery pricing:
  `https://cloud.google.com/bigquery/pricing`
- Looker Studio:
  `https://lookerstudio.google.com`
- ACE exam guide:
  `https://cloud.google.com/certification/guides/cloud-engineer`

---

## 9. Supplemental Resources

**1. Google Cloud Documentation — BigQuery Table Partitioning**
<https://cloud.google.com/bigquery/docs/partitioned-tables>
Complete reference for BigQuery partitioned tables covering date/timestamp partitioning, integer-range partitioning, ingestion-time partitioning, partition filters, and the partition expiration setting — all high-frequency ACE exam topics.

**2. Google Cloud Skills Boost — BigQuery: Qwik Start**
<https://www.cloudskillsboost.google/focuses/1145>
Hands-on lab loading public dataset tables into BigQuery, writing SQL queries, examining query execution plans, and using the dry-run feature to estimate query costs before execution.

**3. Google Cloud Documentation — Introduction to Optimizing Query Performance**
<https://cloud.google.com/bigquery/docs/best-practices-performance-overview>
Best practices guide covering partitioning, clustering, authorized views, materialized views, and avoiding full-table scans — the optimization topics most commonly tested in ACE exam scenario questions on BigQuery cost and performance.

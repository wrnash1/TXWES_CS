# Quiz: Module 12 — BigQuery and Data Analytics

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 1

A data engineering team has a BigQuery table containing 5 years of transaction records
(approximately 2 TB). Most queries filter by transaction date within a 30-day window.
The team wants to reduce query costs. What is the most effective optimization?

- A) Add a secondary index on the transaction\_date column
- B) Create a date-partitioned table using the transaction\_date column
- C) Move the table to long-term storage
- D) Convert the table to an external table in Cloud Storage

Correct answer: B — Date partitioning divides the table into daily segments and enables
partition pruning, so queries with a date range filter scan only the relevant partitions
instead of the entire 2 TB table. BigQuery does not support traditional secondary indexes.
Moving to long-term storage reduces storage costs but not query costs. External tables
do not support partitioning as effectively as native tables.

---

### Question 2

A BigQuery query runs against a partitioned table but scans the full table instead of
the relevant partitions. What is the most likely cause?

- A) The table has too many partitions
- B) The query does not include a filter on the partition column
- C) Partitioning is not supported for this table's data type
- D) The user lacks the bigquery.tables.getData permission

Correct answer: B — Partition pruning only occurs when the WHERE clause includes a
filter on the partition column. If the query omits the partition filter, BigQuery scans
all partitions. This is the most common reason a partitioned table query costs as much
as a full-table scan.

---

### Question 3

A team needs to share a subset of a sensitive customer table with an analytics team in
a different GCP project. The analytics team should only see non-PII columns and no
records for inactive accounts. Which BigQuery feature provides this without granting
direct table access?

- A) Dataset-level IAM binding granting the analytics team bigquery.dataViewer
- B) An authorized view filtering columns and rows, shared with the analytics team
- C) Export the filtered data to Cloud Storage and share the bucket
- D) Create a copy of the table with sensitive columns removed

Correct answer: B — An authorized view lets you define exactly which rows and columns
are visible and share the view with the analytics team without granting direct table
access. Dataset-level IAM would expose the full table. Exporting or copying creates
redundancy and does not stay in sync with changes.

---

### Question 4

Which BigQuery pricing model charges approximately $5.00 per terabyte of data scanned?

- A) Flat-rate pricing (slot reservations)
- B) Streaming insert pricing
- C) On-demand pricing
- D) Storage pricing

Correct answer: C — On-demand pricing charges approximately $5.00 per TB processed by
queries. The first 1 TB per month is free. Flat-rate pricing is a fixed monthly charge
for reserved slots, independent of bytes scanned. Storage pricing is per GB stored.
Streaming insert pricing is per row inserted.

---

### Question 5

A developer runs the same BigQuery query twice within a few minutes against an unchanged
table. What happens on the second execution?

- A) BigQuery runs the query again and charges for the bytes scanned a second time
- B) BigQuery returns the cached result from the first run at no charge
- C) BigQuery denies the second query due to rate limiting
- D) BigQuery automatically converts the second run to a dry\_run

Correct answer: B — BigQuery caches query results for 24 hours. Running an identical
query against an unchanged table within the cache window returns the cached result at
no charge. The cache is automatically invalidated when the underlying table changes.

---

### Question 6

A data analyst wants to estimate how much a BigQuery query will cost before running it.
Which approach is correct?

- A) Run the query with LIMIT 1 to test on a small sample
- B) Use --dry\_run with the bq CLI or review the byte estimate in the Cloud Console
- C) Manually estimate based on table size from the BigQuery pricing page
- D) Run the query and check the bytes billed in query history

Correct answer: B — `--dry_run` (or the automatic estimate in the Cloud Console query
editor) processes the query plan and returns bytes that would be scanned without actually
executing. Adding LIMIT 1 does NOT reduce bytes scanned in BigQuery — the optimizer still
reads all matching rows before applying the limit.

---

### Question 7

A team has a large BigQuery table partitioned by `order_date`. They frequently filter on
both `order_date` and `customer_region`. What additional optimization reduces bytes
scanned for queries that filter on `customer_region`?

- A) Add a secondary index on customer\_region
- B) Create a separate table for each region
- C) Cluster the table by customer\_region
- D) Use a materialized view with customer\_region as a partition column

Correct answer: C — Clustering by `customer_region` sorts data within each partition so
BigQuery skips blocks that do not match the filter. This reduces bytes scanned beyond
what date partitioning alone achieves. BigQuery does not support secondary indexes, and
separate per-region tables are an anti-pattern.

---

### Question 8

A BigQuery dataset was created in the `us-central1` region. The team now needs the data
in `europe-west1` for a compliance requirement. What is the correct approach?

- A) Change the dataset location setting to the EU multi-region
- B) Create a new dataset in europe-west1 and copy the tables using bq cp
- C) Use BigQuery data replication to add a secondary region
- D) Create cross-region read replicas in the existing dataset

Correct answer: B — You cannot change a BigQuery dataset's location after creation.
The correct approach is to create a new dataset in the target region and copy tables
using `bq cp` or by exporting to Cloud Storage and reloading. BigQuery does not have
built-in cross-region replication within a single dataset.

---

### Question 9

What is the key difference between a BigQuery external table and a native BigQuery table?

- A) External tables support partitioning; native tables do not
- B) External tables store data inside BigQuery managed storage; native tables store data
   in Cloud Storage
- C) External tables reference data in Cloud Storage without ingesting it into BigQuery;
   native tables store data in BigQuery's managed Colossus storage
- D) External tables require a schema definition; native tables can be schemaless

Correct answer: C — External tables reference files stored outside BigQuery (Cloud
Storage, Google Sheets, etc.) without loading the data into BigQuery's internal storage.
Native tables store data in BigQuery's Colossus distributed file system. External tables
are useful for one-time analysis without ingestion cost, but are slower and less
optimizable.

---

### Question 10

A BigQuery table has not been modified for 95 days. Which pricing benefit applies
automatically?

- A) The table is automatically archived to Coldline storage
- B) The table qualifies for long-term storage pricing at approximately half the active
   storage rate
- C) Query costs for the table are reduced by 50%
- D) The table is automatically deleted after 90 days of inactivity

Correct answer: B — BigQuery automatically applies long-term storage pricing to tables
and partitions that have not been modified for 90 or more consecutive days. The storage
cost drops to approximately half the active rate, with no configuration required. This
applies to storage cost only, not query cost. Tables are not automatically deleted.

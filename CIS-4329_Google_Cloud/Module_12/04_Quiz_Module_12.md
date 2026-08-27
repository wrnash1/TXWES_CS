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

---

### Question 11 (5 points)

A team runs analytics queries against a BigQuery table 24 hours a day. At peak usage
they consume 800 slots and at off-peak only 50 slots. They want to ensure peak queries
are never throttled. Which pricing model is most appropriate?

- A) On-demand pricing, which allocates up to 2000 slots automatically
- B) Flat-rate pricing with a slot reservation sized for peak usage
- C) On-demand pricing with query priority set to INTERACTIVE
- D) Flex slots purchased for 60-second increments

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) On-demand pricing does allocate slots but does not guarantee a specific slot count; during periods of high contention, on-demand queries may be queued, which does not meet the "never throttled" requirement.
  - C) INTERACTIVE query priority is the default on-demand mode; it does not reserve slots or guarantee throughput.
  - D) Flex slots provide short-term commitment reservations (minimum 60 seconds) for burst capacity but are not suited for continuous 24-hour peak guarantees; flat-rate reservations are the appropriate long-term solution.

---

### Question 12 (5 points)

A BigQuery table stores 10 million rows. A query filters on a non-partition, non-cluster
column. What technique can reduce bytes scanned for this type of query without
restructuring the table?

- A) Create a secondary index on the filtered column
- B) Re-create the table with clustering on the filtered column
- C) Move the table to a regional dataset to enable regional query optimization
- D) Set the table's default partition expiration to 1 day

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) BigQuery does not support secondary indexes in the traditional relational database sense; this is not an available optimization technique.
  - C) Dataset region affects data residency and latency for the query job, not the amount of data scanned; changing region does not enable block skipping.
  - D) Setting a partition expiration reduces stored data over time by deleting old partitions, but it does not reduce bytes scanned for queries on existing data and does not help if the column is not a partition column.

---

### Question 13 (5 points)

A data engineering team loads new data into BigQuery every hour using batch jobs.
They also need to ingest individual transaction records within 1 second of occurring
for real-time dashboards. Which two loading methods should they use for each use case?

- A) `bq load` for both batch and real-time ingestion
- B) `bq load` for hourly batch; BigQuery Storage Write API for real-time streaming
- C) Cloud Storage transfer for hourly batch; `bq insert` (legacy streaming) for
   real-time
- D) Dataflow for both batch and streaming ingestion

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `bq load` ingests files stored in Cloud Storage or local files; it is not suitable for real-time single-record insertion with sub-second latency.
  - C) `bq insert` is the legacy streaming API that works but is being superseded by the Storage Write API; more importantly, the combination in option B is the current recommended approach per GCP documentation.
  - D) Dataflow can handle both batch and streaming but is a full pipeline service requiring more configuration; for simple hourly file loads, `bq load` is the standard approach.

---

### Question 14 (5 points)

Which BigQuery feature allows a view in one dataset to query a table in a separate
dataset that would otherwise be inaccessible to the view's users?

- A) Cross-dataset IAM binding on the source table
- B) Authorized view — the source dataset grants `bigquery.dataViewer` to the view's
   service account
- C) Authorized dataset — the source dataset adds the view's dataset as an authorized
   entity
- D) VPC Service Controls perimeter spanning both datasets

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) A cross-dataset IAM binding grants the view's users direct access to the source table, bypassing the row/column filtering the view provides; this defeats the purpose of the view.
  - B) Authorized views require granting the source dataset access to the specific view (not a service account); the correct mechanism is adding the view as an authorized view in the source dataset's configuration, not granting IAM to a service account.
  - D) VPC Service Controls restrict which networks can access BigQuery; they do not control which views can read which tables within BigQuery.

---

### Question 15 (5 points)

A BigQuery job fails with the error `quotaExceeded: Your project exceeded quota for
concurrent queries`. What is the immediate mitigation?

- A) Purchase additional BigQuery storage capacity
- B) Reduce the number of concurrent queries by queuing or batching requests, or
   request a quota increase
- C) Switch from on-demand to flat-rate pricing to remove the quota limit
- D) Move the dataset to a multi-region location to distribute the query load

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `quotaExceeded` for concurrent queries is a compute quota (number of simultaneous query jobs), not a storage quota; purchasing storage does not help.
  - C) The concurrent query quota applies regardless of pricing model; flat-rate pricing changes how compute is billed but does not eliminate the project-level concurrent query quota.
  - D) Dataset location affects data residency; distributing across regions does not increase the project-level concurrent query quota.

---

### Question 16 (5 points)

A team needs to run the same aggregation query on a large BigQuery table hundreds
of times per day with low latency. The underlying table is updated once per day.
Which BigQuery feature pre-computes and caches the query results?

- A) Query result cache (automatic 24-hour cache)
- B) Materialized view
- C) Partitioned table
- D) Clustered table

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The query result cache stores results for 24 hours and is invalidated when the underlying table changes; it re-executes the full query on the first run after the daily table update, and there is no control over cache refresh timing.
  - C) Partitioned tables reduce bytes scanned by pruning partitions, but they do not pre-compute aggregations; each query still performs the aggregation at runtime.
  - D) Clustered tables reduce bytes scanned by sorting data within partitions; they do not pre-compute or store query results.

---

### Question 17 (5 points)

A security team needs to mask the `ssn` column in a BigQuery table so that only
users with a specific IAM tag can see the plaintext values. All other users see
a masked value. Which BigQuery feature provides this?

- A) Authorized views with a CASE expression replacing SSN with `XXXX`
- B) Column-level security using policy tags and data governance with BigQuery
   Data Catalog
- C) BigQuery row-level security filters applied to the SSN column
- D) Encrypting the SSN column with CMEK at rest

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Authorized views can mask data with SQL expressions but require maintaining a separate view; column-level security with policy tags is the purpose-built, scalable solution that integrates with Data Catalog taxonomy management.
  - C) Row-level security filters control which rows a user can see, not which columns or values within a column; it does not support partial value masking.
  - D) CMEK encrypts all data at rest using a customer-managed key; it does not provide per-column access control or value masking for specific users.

---

### Question 18 (5 points)

A company stores event data in BigQuery and needs to connect Looker Studio to their
BigQuery dataset for real-time reporting. What must be configured so that Looker
Studio can access the dataset?

- A) The BigQuery dataset must be exported to Cloud Storage for Looker Studio to read
- B) Grant the Looker Studio service account `roles/bigquery.dataViewer` on the dataset,
   or use viewer credentials in the data source configuration
- C) Enable the Looker Studio API in the GCP project that contains the BigQuery dataset
- D) The BigQuery dataset must be in the same GCP project as the Looker Studio workspace

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Looker Studio connects directly to BigQuery using the BigQuery connector; no export to Cloud Storage is required.
  - C) There is no separate "Looker Studio API" to enable; the BigQuery API must be enabled, and IAM permissions on the dataset are the access control mechanism.
  - D) Looker Studio can connect to BigQuery datasets across GCP projects; they do not need to be in the same project, provided IAM permissions are correctly configured.

---

### Question 19 (5 points)

A team creates a BigQuery dataset in `US` (multi-region). A Dataflow job in
`us-central1` reads from this dataset. What egress charges apply for data
read by the Dataflow job?

- A) Standard GCP inter-region egress charges at $0.08/GB apply
- B) No egress charges apply because Dataflow in `us-central1` and BigQuery in
   the `US` multi-region are within the same geographic boundary
- C) Egress charges apply only for reads exceeding 1 TB per month
- D) BigQuery charges $5.00 per TB for Dataflow reads regardless of egress

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) BigQuery to Dataflow reads within the same GCP region or multi-region boundary do not incur inter-region egress charges; Google does not charge for data movement between services within the same location.
  - C) There is no 1 TB monthly free tier threshold for BigQuery-to-Dataflow egress within the same region; the data movement is simply not charged.
  - D) The $5.00 per TB charge is the on-demand query cost for bytes scanned by SQL queries; it is not a charge for data read by Dataflow pipelines.

---

### Question 20 (5 points)

A BigQuery table is partitioned by `event_date` with 1000 daily partitions. The
table has no partition filter requirement set. What is the risk of this configuration?

- A) Queries without a partition filter cannot execute on tables with more than
   500 partitions
- B) Without a partition filter requirement, a user can accidentally run a full
   table scan across all 1000 partitions, incurring high query cost
- C) Tables with more than 999 partitions are automatically migrated to sharded
   tables
- D) Partition expiration is automatically enabled when partition count exceeds 1000

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) BigQuery does not restrict query execution based on partition count; there is no 500-partition execution limit.
  - C) BigQuery supports up to 4000 partitions per table (7500 for ingestion-time partitions); automatic migration to sharded tables does not occur at any partition count threshold.
  - D) Partition expiration must be explicitly configured; BigQuery does not automatically enable expiration when a table reaches any specific partition count.

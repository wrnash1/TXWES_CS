# Quiz: Module 07 - BigQuery – Data Warehouse and Analytics
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
A business intelligence team runs 500 ad-hoc SQL queries per day against 10 TB of historical sales data. They need sub-minute query execution and do not want to manage database servers. Which Google Cloud service is most appropriate?
A) Cloud SQL for PostgreSQL with read replicas
B) BigQuery
C) Cloud Spanner
D) Cloud Bigtable
*   **Correct Answer:** B) BigQuery
*   **Distractor Analysis:**
    *   *Why B is correct:* BigQuery is purpose-built for this exact use case. It is serverless (no infrastructure to manage), uses columnar storage to efficiently process analytical SQL queries, and can execute queries over tens of terabytes in seconds to minutes.
    *   *Why A is incorrect:* Cloud SQL is optimized for transactional OLTP workloads. Running 500 ad-hoc analytical queries over 10 TB on a relational instance would require extensive index management and would still be much slower than BigQuery's massively parallel processing.
    *   *Why C is incorrect:* Cloud Spanner is a globally distributed OLTP relational database; it is not designed for ad-hoc analytical queries over large historical datasets and would be significantly more expensive for this use case.
    *   *Why D is incorrect:* Bigtable stores data indexed by a single row key and does not support SQL aggregation queries; it is not suitable for business intelligence reporting.

---

---

**Question 2**
A BigQuery table containing 5 TB of e-commerce orders is queried daily by analysts who always filter by `order_date` and frequently filter by `customer_region`. Which combination of optimizations will most reduce query cost and execution time?
A) Partition the table by `order_date` and cluster by `customer_region`.
B) Create a secondary index on `order_date` and a separate index on `customer_region`.
C) Replicate the table to a second BigQuery dataset for read load distribution.
D) Enable BigQuery BI Engine to cache the entire table in memory for sub-second queries.
*   **Correct Answer:** A) Partition the table by `order_date` and cluster by `customer_region`.
*   **Distractor Analysis:**
    *   *Why A is correct:* Partitioning by `order_date` means queries with a date filter scan only the relevant date partitions instead of the full 5 TB. Clustering by `customer_region` within each partition co-locates rows from the same region, so additional filtering on `customer_region` reads fewer blocks within the partition. This is the standard BigQuery optimization pattern.
    *   *Why B is incorrect:* BigQuery does not support traditional secondary indexes like Cloud SQL. While Materialized Views and search indexes exist for specific use cases, the standard optimization for filter columns in BigQuery is partitioning and clustering, not index creation.
    *   *Why C is incorrect:* BigQuery is serverless and handles read scaling automatically; replicating a table to distribute reads wastes storage and incurs unnecessary cost with no benefit.
    *   *Why D is incorrect:* BigQuery BI Engine accelerates SQL queries by caching data in memory, but it has a capacity limit (typically a few hundred GB) and cannot cache a 5 TB table. Partitioning and clustering address the root issue at the storage layer for any dataset size.

---

---

**Question 3**
A BigQuery administrator needs to **identify which SQL queries in the past 24 hours processed the most bytes and incurred the highest cost**. Which BigQuery feature provides this information?
A) Query `INFORMATION_SCHEMA.JOBS_BY_PROJECT` to view historical job statistics including bytes billed per query.
B) Run `EXPLAIN ANALYZE` on each query to view the execution plan and cost estimate.
C) Check the Cloud SQL Query Insights dashboard for slow query reports.
D) Use Cloud Monitoring to view the `bigquery.googleapis.com/storage/table_count` metric.
*   **Correct Answer:** A) Query `INFORMATION_SCHEMA.JOBS_BY_PROJECT` to view historical job statistics including bytes billed per query.
*   **Distractor Analysis:**
    *   *Why A is correct:* BigQuery's `INFORMATION_SCHEMA.JOBS_BY_PROJECT` (and `JOBS_BY_USER`) views contain detailed metadata for every query job, including `total_bytes_billed`, `total_bytes_processed`, `total_slot_ms`, creation time, and the full query text. This is the standard way to audit BigQuery query cost.
    *   *Why B is incorrect:* `EXPLAIN ANALYZE` is a PostgreSQL command for relational query plans; BigQuery uses the `EXPLAIN` statement or `INFORMATION_SCHEMA.JOBS` for query plan analysis, not `EXPLAIN ANALYZE`.
    *   *Why C is incorrect:* Cloud SQL Query Insights is a performance tool for Cloud SQL relational instances; it does not have any visibility into BigQuery jobs.
    *   *Why D is incorrect:* The `table_count` metric measures the number of tables in a BigQuery dataset; it does not provide per-query cost or bytes-processed information.

---

**Question 4**
A data engineering team migrates a 2 TB normalized relational schema from Cloud SQL into BigQuery for analytics. After migration, analysts report that their multi-table JOIN queries are much slower than expected. What is the most appropriate BigQuery-specific remediation?
A) Denormalize the schema by creating wide, flat tables that pre-join the most frequently combined tables, reducing runtime JOIN overhead.
B) Create secondary indexes on the foreign key columns in BigQuery to speed up JOIN lookups.
C) Enable BigQuery HA replication so that JOIN queries can run in parallel across two instances.
D) Increase the BigQuery slot reservation to allocate more compute capacity for JOIN operations.
*   **Correct Answer:** A) Denormalize the schema by creating wide, flat tables that pre-join the most frequently combined tables, reducing runtime JOIN overhead.
*   **Distractor Analysis:**
    *   *Why A is correct:* BigQuery's columnar storage engine is optimized for wide, flat tables. JOINs across large normalized tables require shuffle operations across distributed workers and are expensive. The standard BigQuery design pattern is to denormalize — create pre-joined tables or use nested/repeated fields (ARRAY and STRUCT) to represent hierarchical data within a single table, eliminating JOINs at query time.
    *   *Why B is incorrect:* BigQuery does not support traditional B-tree secondary indexes for JOIN acceleration. The columnar storage model makes traditional index structures unnecessary for analytical workloads; the optimization strategy is partitioning, clustering, and denormalization.
    *   *Why C is incorrect:* BigQuery is serverless and does not have HA instances or replicas in the traditional sense. Compute is automatically distributed across thousands of slots per query; there is no "second instance" to enable.
    *   *Why D is incorrect:* Adding more slots speeds up CPU-bound operations but does not reduce the inherent I/O cost of large JOIN shuffle operations. Denormalization addresses the root cause at the schema design level.

---

**Question 5**
When securing a BigQuery dataset containing sensitive customer PII, you must mitigate the risk of **analysts running queries that expose full Social Security Numbers or credit card numbers stored in the dataset**. Which control best addresses this vulnerability?
A) Apply BigQuery column-level security using policy tags and Data Catalog to mask or restrict access to sensitive columns for unauthorized roles.
B) Enable CMEK on the BigQuery dataset so that sensitive columns are stored in encrypted form.
C) Create a Firestore Security Rule that blocks queries selecting the sensitive columns.
D) Configure VPC Service Controls to block BigQuery API calls from outside the corporate network.
*   **Correct Answer:** A) Apply BigQuery column-level security using policy tags and Data Catalog to mask or restrict access to sensitive columns for unauthorized roles.
*   **Distractor Analysis:**
    *   *Why A is correct:* BigQuery's column-level security feature allows you to assign policy tags (managed in Data Catalog) to individual columns. Users without the `Fine-Grained Reader` IAM permission on the policy tag cannot see data in those columns — their query returns a null or the query is rejected entirely. This is the precise control for preventing unauthorized exposure of PII.
    *   *Why B is incorrect:* CMEK encrypts the physical storage files at rest. It does not affect which data an authorized analyst sees when running a query; all authorized users get the same decrypted results regardless of CMEK.
    *   *Why C is incorrect:* Firestore Security Rules apply to the Firestore document database service; they have no relationship to BigQuery and cannot control BigQuery queries.
    *   *Why D is incorrect:* VPC Service Controls restrict which network or identity perimeters can call the BigQuery API, but do not provide column-level data masking. An analyst inside the perimeter would still be able to query sensitive columns.

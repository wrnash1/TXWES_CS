# Video Script: Module 16 — Exam Preparation and Capstone (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Database Engineer

---

## SLIDE 1 — Welcome to Module 16

Welcome to the final module of CIS-4327. I'm Professor Nash, and this module is
dedicated to preparing you for the Google Cloud Professional Database Engineer
certification exam.

Module 16 has a different structure from previous modules. The video lectures review
and connect concepts across the entire course — serving as your comprehensive study
guide. The quiz contains 20 practice questions covering all exam domains. The lab is
a capstone architecture design exercise. The discussion is a final reflection.

Let's start with Part 1: a structured review of exam domains 1 through 3.

---

## SLIDE 2 — About the Exam

The Google Cloud Professional Database Engineer exam tests your ability to design,
build, manage, and troubleshoot database solutions on Google Cloud.

**Exam format**:

- 50–60 multiple choice and multiple select questions
- 2 hours to complete
- Available in English and Japanese
- Remote proctored or at a testing center

**Exam domains and approximate weights**:

- Section 1: Design scalable and highly available cloud database solutions — 22%
- Section 2: Manage a solution that can span multiple database systems — 20%
- Section 3: Migrate data solutions — 18%
- Section 4: Deploy cost-optimized database solutions — 18%
- Section 5: Build and maintain database solutions by using Automation — 22%

The exam is scenario-based. Most questions present a situation and ask which
configuration, tool, or approach best satisfies the stated requirements.

---

## SLIDE 3 — Section 1: Database Design Review

Section 1 tests your ability to choose the right database service and design it correctly.

**Service selection decision tree**:

- Is the workload OLTP (transactional, single-row reads/writes) or OLAP (analytical, aggregate queries)?
  - OLTP → Cloud SQL, AlloyDB, or Cloud Spanner
  - OLAP → BigQuery
- Does the workload require global scale with zero downtime during regional failure?
  - Yes → Cloud Spanner
  - No (regional HA is sufficient) → Cloud SQL or AlloyDB
- Is the data relational, or is it unstructured/semi-structured?
  - Relational → Cloud SQL, AlloyDB, Cloud Spanner
  - Wide-column NoSQL → Cloud Bigtable
  - Document NoSQL → Firestore
  - Key-value cache → Memorystore (Redis/Valkey)
- Does the application need ML inference directly in the database?
  - Yes → AlloyDB (Vertex AI integration)

**HA design**:

- Cloud SQL HA: `availability_type = REGIONAL` — synchronous standby in another zone
- Cloud Spanner: Regional = 3 zones; Multi-region = 3+ regions; no HA flag needed
- AlloyDB: HA with automated failover; read pool instances for read scale-out

**Backup and recovery**:

- Cloud SQL: Automated backups (daily) + PITR (transaction logs, up to 7 days)
- Spanner: Automatic backups with configurable retention; point-in-time restore within 7 days
- BigQuery: Time travel (7 days default); table snapshots; table clones

---

## SLIDE 4 — Section 1: Partitioning and Sharding Design

For Cloud Spanner, key design is critical. Poorly designed keys cause hotspots.

**Hotspot**: When many writes target the same key range, all those writes go to one
Spanner split (server). The split becomes a bottleneck.

Common hotspot causes:

- Auto-incrementing integer primary keys — all new rows go to the highest key split
- Timestamp as leading key — all current writes target the latest timestamp split

Hotspot prevention strategies:

- **UUID primary keys**: Random UUIDs distribute writes across all splits. Tradeoff:
  less predictable sort order; slightly larger key size.
- **Bit-reverse sequential keys**: Reverse the bits of an auto-increment value to
  distribute writes while preserving uniqueness.
- **Hash prefix**: Prepend a hash of a column value to the key. Distributes writes
  but requires scanning all prefixes for range queries.
- **Interleaved tables**: For parent-child relationships, interleave child rows
  physically with their parent in the same Spanner split. Eliminates the join cost.

For BigQuery:

- Partition by date for time-series data — prunes entire partitions from scans
- Cluster by the most-used filter columns — skips blocks within partitions
- Use integer range partitioning for non-time-series data with clear range dimensions

---

## SLIDE 5 — Section 1: AlloyDB Architecture

AlloyDB is a PostgreSQL-compatible HTAP (Hybrid Transactional/Analytical Processing)
database. Key architecture components:

**Primary instance**: Handles all writes and reads. PostgreSQL-compatible.

**Read pool instances**: Scale reads horizontally. Use columnar cache for
accelerating analytical queries while remaining fully PostgreSQL-compatible.

**Columnar cache**: AlloyDB scans column blocks stored in memory on read pool
instances. Queries using aggregate functions on large tables benefit most.

**AlloyDB Omni**: AlloyDB packaged to run on any Kubernetes cluster (on-premises
or other clouds). Same API as cloud AlloyDB. Useful for hybrid scenarios.

For the exam: choose AlloyDB when:

- PostgreSQL compatibility is required
- Both OLTP and analytical queries run against the same data
- Vertex AI ML inference is needed inside the database
- Higher throughput than Cloud SQL is needed without switching to Spanner

---

## SLIDE 6 — Section 2: Multi-Database Solution Management

Section 2 tests knowledge of managing solutions that span multiple database systems —
connecting them, migrating data between them, and ensuring consistency.

**Cross-database patterns**:

**HTAP with BigQuery**: Write OLTP data to Cloud SQL or Spanner. Stream changes
via Datastream (CDC) to BigQuery for analytics. Applications read from Cloud SQL/Spanner
for transactions and from BigQuery for reports. This is the most common multi-database
architecture in GCP.

**Federated queries from BigQuery**: BigQuery can query external data sources
including Cloud SQL, Cloud Spanner, and Cloud Storage using federated queries via
BigQuery Omni or `EXTERNAL_QUERY()`. Useful for joining BigQuery analytics with
live OLTP data without ETL.

```sql
-- BigQuery federated query to Cloud SQL
SELECT bq.order_id, sql.customer_name
FROM `my-project.analytics.orders` bq
JOIN EXTERNAL_QUERY(
  "us.my-connection",
  "SELECT customer_id, name AS customer_name FROM customers"
) sql
ON bq.customer_id = sql.customer_id;
```

**Connection management**: Cloud SQL Proxy handles authentication and SSL for
client connections. PgBouncer or Cloud SQL's built-in connection pooler handles
connection pool exhaustion for high-concurrency applications.

---

## SLIDE 7 — Section 2: Database Flags and Engine Tuning

Cloud SQL supports setting database engine flags to tune performance and behavior.

Key PostgreSQL flags:

- `max_connections`: Maximum simultaneous connections. Default varies by tier.
  Too high causes memory pressure; too low causes connection refusals.
- `shared_buffers`: Memory for caching data pages. Generally 25% of instance RAM.
  Cloud SQL manages this automatically, but it can be overridden.
- `work_mem`: Memory per sort/hash operation. Too low causes disk sorts; too high
  causes OOM errors on high-concurrency workloads.
- `effective_cache_size`: Query planner hint for available OS cache. Setting to
  75% of instance RAM improves query plan quality.
- `log_min_duration_statement`: Log queries exceeding this duration in milliseconds.
  Set to 1000 (1 second) to capture slow queries without overwhelming the log.
- `cloudsql.iam_authentication`: Must be `on` to use IAM database authentication.

Setting a flag:

```bash
gcloud sql instances patch my-pg-instance \
  --database-flags=log_min_duration_statement=1000,work_mem=16384
```

Warning: changing some flags (like `max_connections`) requires an instance restart.
Plan flag changes during a maintenance window.

---

## SLIDE 8 — Section 3: Migration Review — Key Decision Points

Section 3 tests migration planning and execution. The most common exam scenario
presents a migration requirement and asks which tool and approach to use.

**Decision chart for migration tool selection**:

- Migrating MySQL or PostgreSQL to Cloud SQL or AlloyDB → **Database Migration Service (DMS)**
- Migrating Oracle or SQL Server to Cloud SQL for PostgreSQL (heterogeneous) → **DMS with schema conversion workspace**
- Streaming CDC changes from any relational DB to BigQuery → **Datastream**
- Migrating Teradata, Redshift, or other warehouses to BigQuery → **BigQuery Data Transfer Service**
- Moving large data files from on-premises to Cloud Storage → **Storage Transfer Service**
- Complex ETL transformations during migration → **Dataflow**

**Minimal downtime migration** (always use DMS continuous migration):

1. Initial full load
2. CDC replication catches up (lag → zero)
3. Stop writes on source (seconds)
4. Verify final row count match
5. Promote target
6. Switch application connection strings
7. Monitor; rollback if critical issues within 15–30 minutes

**Schema conversion** (heterogeneous only):

- Use DMS schema conversion workspace for Oracle/SQL Server → PostgreSQL
- DMS converts data types and simple functions automatically
- Stored procedures, triggers, and complex PL/SQL require manual conversion
- Test converted procedures with pgTAP before cutover

---

## SLIDE 9 — Section 3: Datastream Overview

Datastream is a serverless, replication and CDC service. Key facts for the exam:

**Source support**: MySQL, PostgreSQL, Oracle, SQL Server

**Destination support**: BigQuery, Cloud Storage, Cloud Spanner

**Use cases**:

- Real-time analytics: Stream OLTP changes to BigQuery for sub-minute analytics
- Event-driven architecture: Stream changes to Cloud Storage as Avro/JSON files
  for downstream processing
- Multi-region replication: Replicate data to Spanner for global availability

**Configuration**: Datastream uses connection profiles (same concept as DMS) and
streams (defining source → destination with CDC rules).

**Exam distinction**: DMS is for one-time or continuous database migration with
cutover intent. Datastream is for ongoing, permanent CDC pipelines with no cutover —
the source remains the source indefinitely.

---

## SLIDE 10 — Common Exam Trap Questions

These question patterns appear frequently and are designed to catch common misconceptions:

**Trap 1 — BigQuery jobUser role**:

"A user has `roles/bigquery.dataViewer` but cannot run queries."
Answer: They also need `roles/bigquery.jobUser`. dataViewer alone allows reading
metadata but not executing query jobs.

**Trap 2 — DMS and stored procedures**:

"A DMS migration completed successfully but stored procedures are missing."
Answer: DMS does not migrate stored procedures. They must be converted and deployed separately.

**Trap 3 — Cloud SQL replica promotion**:

"After DMS cutover, replication is still running and we want to go back."
Answer: Promotion is irreversible. DMS replication cannot be resumed after promotion.
Rollback means switching the application back to the source.

**Trap 4 — Spanner and CMEK**:

"The team wants to use a customer-managed key for Spanner but the key was created
after the Spanner instance."
Answer: CMEK for Spanner is set at instance creation and cannot be added later.
You must create a new instance with CMEK configured from the start.

**Trap 5 — BigQuery partition filter**:

"A BigQuery table has `require_partition_filter=true`. A user queries it without
a date filter."
Answer: The query is REJECTED with an error — it does not just scan more data.

---

## SLIDE 11 — Part 1 Summary

We have reviewed exam Sections 1–3 covering:

- Service selection: OLTP vs. OLAP, scale requirements, consistency model
- HA design: Cloud SQL REGIONAL, Spanner multi-region, AlloyDB read pools
- Hotspot prevention in Spanner: UUID keys, bit-reverse, interleaving
- BigQuery design: partitioning and clustering for cost and performance
- Migration tool selection: DMS, Datastream, BigQuery DTS, Dataflow
- Key exam traps to avoid

In Part 2 we review Sections 4 and 5: cost optimization, security, automation,
and monitoring — then finish with exam strategy.

---

*End of Part 1 Script*

# Quiz: Module 14 — Database Migration Strategies

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis follows each question.

---

### Question 1

A company runs Oracle 19c on-premises and wants to migrate to Cloud SQL for PostgreSQL. Which term correctly classifies this migration?

- A) Homogeneous migration — both Oracle and PostgreSQL use SQL, making it the same database category
- B) Heterogeneous migration — different database engines with different SQL dialects, data types, and stored procedure syntax
- C) Lift-and-shift migration — the database is moved as-is without schema or code changes
- D) Hybrid migration — Oracle remains the primary database while PostgreSQL serves as a secondary replica

Correct Answer: B — A heterogeneous migration involves different database engines. Oracle and PostgreSQL are distinct engines with incompatible SQL dialect extensions, different data type mappings, different stored procedure languages (PL/SQL versus PL/pgSQL), and different system catalog structures. Schema conversion and code migration are required.

Distractor analysis: A is incorrect because sharing the SQL standard does not make a migration homogeneous. Oracle PL/SQL syntax, Oracle-specific functions, and data type differences (e.g., `NUMBER` vs. `NUMERIC`, `VARCHAR2` vs. `VARCHAR`) require conversion effort. Homogeneous means the same database engine — such as MySQL 5.7 to Cloud SQL for MySQL 8.0. C is incorrect because lift-and-shift means moving the workload without changes (typically a VM-level migration, not a database engine change); Oracle-to-PostgreSQL always requires schema and code conversion. D is incorrect because hybrid migration is not a standard DMS classification; Oracle-to-PostgreSQL is a one-time source-to-target heterogeneous migration.

---

### Question 2

You are configuring a MySQL 8.0 source database for a Database Migration Service continuous migration. The DMS connection test fails with `Binary logging is not enabled`. Which configuration change resolves this?

- A) Enable `general_log = ON` to capture all queries for replication
- B) Enable `slow_query_log = ON` to capture long-running queries
- C) Set `log_bin = /var/log/mysql/mysql-bin.log` with `binlog_format = ROW` to enable binary logging in row format
- D) Set `log_output = FILE` with `log_queries_not_using_indexes = ON`

Correct Answer: C — Database Migration Service requires binary logging to be enabled on the MySQL source for CDC (Change Data Capture) replication. Binary logging must use `binlog_format = ROW`, which records before/after row images for each change. STATEMENT or MIXED format is not supported by DMS because STATEMENT format can produce non-deterministic results on the target.

Distractor analysis: A is incorrect because `general_log` captures all SQL statements executed against the server for diagnostic purposes but is not the MySQL replication log. DMS uses the binary log (`binlog`), not the general query log. B is incorrect because `slow_query_log` captures queries that exceed a time threshold for performance analysis. It has no connection to replication or DMS requirements. D is incorrect because `log_output` controls where logs are written (table or file) and `log_queries_not_using_indexes` is a slow query log flag — neither enables binary logging.

---

### Question 3

A DMS migration job has been running for 6 hours. The status shows `CDC IN PROGRESS` with a replication lag of 45 minutes that has not decreased over the past 2 hours. What is the most likely cause?

- A) The Cloud SQL destination instance is too small — its write throughput cannot keep pace with the source database's change volume
- B) DMS has a 6-hour time limit on migration jobs and the job is about to expire automatically
- C) The binary log on the source database has been purged, terminating CDC replication silently
- D) The migration job is paused because the source database entered read-only mode

Correct Answer: A — Persistent, non-decreasing replication lag during CDC indicates the target cannot apply changes as fast as the source generates them. The most common cause is an undersized destination Cloud SQL instance where write throughput (IOPS, CPU for applying transactions) is the bottleneck. Upgrading the destination tier or reducing the source write rate resolves this.

Distractor analysis: B is incorrect because DMS does not impose a 6-hour time limit on migration jobs; continuous jobs run indefinitely until explicitly stopped or until cutover. C is incorrect because if the binary log is purged, DMS reports an error and the CDC job fails — it does not continue with a replication lag. D is incorrect because if the source is in read-only mode, no changes are being written, and the replication lag would remain flat but the job would still show as running without lag growth.

---

### Question 4

You are migrating a PostgreSQL 14 database from AWS RDS to Cloud SQL for PostgreSQL using DMS. Which PostgreSQL parameter must be set on the AWS RDS source instance to enable logical replication for DMS?

- A) `log_level = logical` — enables logical-level database logging
- B) `wal_level = logical` — configures the WAL to include the information needed for logical replication
- C) `replication_mode = logical` — enables logical replication mode for the instance
- D) `cdc_enabled = true` — enables change data capture on the RDS instance

Correct Answer: B — PostgreSQL logical replication requires `wal_level = logical` in `postgresql.conf` (or the RDS parameter group equivalent). This setting instructs PostgreSQL to include enough information in the WAL (Write-Ahead Log) for logical decoding — the mechanism DMS uses to read change events from the source. The default `wal_level = replica` is insufficient for logical replication.

Distractor analysis: A is incorrect because `log_level` controls the verbosity of server log messages (DEBUG, INFO, WARNING, etc.) and has no effect on WAL content or replication capability. C is incorrect because `replication_mode` is not a valid PostgreSQL configuration parameter. D is incorrect because `cdc_enabled` is not a PostgreSQL configuration parameter; it does not exist in standard PostgreSQL or AWS RDS.

---

### Question 5

A DMS migration of an Oracle database to Cloud SQL for PostgreSQL completes the full data transfer successfully. After cutover, the application throws errors when calling several stored procedures. What is the most likely explanation?

- A) DMS automatically converted the stored procedures from PL/SQL to PL/pgSQL but introduced syntax errors during conversion
- B) DMS migrates data only — stored procedures, triggers, functions, and other programmable objects must be manually converted and deployed separately
- C) Cloud SQL for PostgreSQL does not support stored procedures at all
- D) The stored procedures were migrated but require Oracle compatibility mode to be enabled in the Cloud SQL instance flags

Correct Answer: B — DMS migrates table data (rows). Stored procedures, triggers, functions, views, sequences, and other schema objects from Oracle are written in PL/SQL, which is incompatible with PostgreSQL's PL/pgSQL. These objects must be converted using the DMS schema conversion workspace, a third-party tool such as AWS Schema Conversion Tool, or manually. They are not automatically migrated or converted by DMS.

Distractor analysis: A is incorrect because DMS does not automatically convert stored procedures. The schema conversion workspace can assist with conversion, but it produces a conversion assessment and suggested changes for manual review — it does not automatically deploy converted procedures to the target. C is incorrect because Cloud SQL for PostgreSQL fully supports stored procedures written in PL/pgSQL, SQL, and other available procedural languages. The issue is that Oracle PL/SQL procedures were not converted to PL/pgSQL before cutover. D is incorrect because Cloud SQL for PostgreSQL does not have an Oracle compatibility mode; it is a standard PostgreSQL implementation and cannot execute PL/SQL natively.

---

### Question 6

A data engineering team needs to stream CDC changes from a PostgreSQL on-premises database continuously to BigQuery for near-real-time analytics. The solution must be serverless and require no custom code. Which GCP service is designed specifically for this use case?

- A) Database Migration Service — used for one-time and continuous database-to-database migrations
- B) BigQuery Data Transfer Service — scheduled batch data transfer from SaaS and other sources to BigQuery
- C) Datastream — a serverless CDC and replication service that streams changes from databases directly to BigQuery and Cloud Storage
- D) Cloud Composer with custom DAGs that query the source database on a schedule

Correct Answer: C — Datastream is Google Cloud's dedicated CDC streaming service. It connects to PostgreSQL (and other databases), reads change events via logical replication, and streams them in near real-time to BigQuery or Cloud Storage. It is serverless, requires no custom code, and is designed specifically for the use case described.

Distractor analysis: A is incorrect because DMS is designed for database migrations — moving an entire database from a source to a Cloud SQL or AlloyDB target. It is not designed to continuously stream changes to BigQuery for analytics. B is incorrect because BigQuery Data Transfer Service handles scheduled batch transfers from SaaS applications (Google Ads, Salesforce, etc.) and some database sources on a schedule — it does not provide near-real-time CDC streaming from PostgreSQL. D is incorrect because Cloud Composer with custom DAGs requires writing and maintaining custom code; the question specifies no custom code required.

---

### Question 7

After executing a DMS cutover and promoting the Cloud SQL target to primary, users report a critical issue 20 minutes later. The team wants to roll back to the original source database. Which statement correctly describes the rollback options?

- A) You can unpromote the Cloud SQL instance and DMS replication automatically resumes from where it stopped
- B) You must switch the application connection strings back to the source database; any data written to Cloud SQL during the 20 minutes after promotion will not be present on the source
- C) DMS supports bidirectional replication so all changes written to Cloud SQL after promotion are automatically synced back to the source
- D) You can use Cloud SQL PITR to restore the Cloud SQL instance to the exact state at the moment of cutover, then resume DMS replication

Correct Answer: B — After DMS promotion, replication is permanently terminated. The Cloud SQL instance becomes an independent primary. Any data written to Cloud SQL in the 20 minutes since promotion is not on the source — the source stopped receiving writes at cutover. Rolling back means pointing applications back to the source and accepting that the 20 minutes of Cloud SQL writes will need to be reconciled manually or discarded.

Distractor analysis: A is incorrect because once a DMS job is promoted, the replication link is permanently broken. DMS cannot unpromote a Cloud SQL instance and resume replication. The promotion is irreversible. C is incorrect because DMS is one-directional — source to target. There is no bidirectional replication. Changes on the Cloud SQL target do not flow back to the source. D is incorrect because PITR restores the Cloud SQL instance to a past state, but this does not reconnect DMS replication; the promotion action ended the migration, and PITR cannot undo that structural change.

---

### Question 8

A financial services firm needs to migrate 500 TB from a Teradata data warehouse to BigQuery within 30 days. The migration team does not have capacity to write custom ETL code. Which GCP service is most appropriate?

- A) Database Migration Service with a continuous migration job targeting BigQuery
- B) Dataflow with a custom Teradata JDBC source template requiring code development
- C) BigQuery Data Transfer Service with the Teradata connector, which provides a managed no-code migration path
- D) Cloud Storage transfer with manual CSV export from Teradata followed by BigQuery load jobs

Correct Answer: C — BigQuery Data Transfer Service provides managed, no-code connectors for several data warehouse sources including Teradata. It handles schema mapping, data extraction, and loading into BigQuery automatically. For a 500 TB migration without custom code development, the Teradata connector is the appropriate choice.

Distractor analysis: A is incorrect because DMS migrates data to Cloud SQL, AlloyDB, or AlloyDB for PostgreSQL targets — it does not migrate to BigQuery. B is incorrect because Dataflow with a custom JDBC template requires writing and maintaining custom code, which the question explicitly excludes. D is incorrect because manual CSV export from a 500 TB Teradata warehouse requires multiple export jobs, storage management, and BigQuery load orchestration. This approach requires significant custom scripting and operational overhead, violating the no-custom-code requirement.

---

### Question 9

Which validation level provides the strongest assurance that a migrated database will produce identical results for production application queries?

- A) Level 1 — row count comparison per table confirming the same number of rows in source and target
- B) Level 2 — column-level checksum comparison using MD5 hashes of row data to detect value-level discrepancies
- C) Level 3 — application-level query result comparison running actual production queries against both source and target and comparing results
- D) DMS built-in data validation job that automatically combines Level 1 and Level 2 comparisons

Correct Answer: C — Application-level validation (Level 3) runs the actual SQL queries used by the production application against both the source and migrated target and compares the results. This catches schema conversion errors, data type mapping issues, and query dialect differences that row counts and checksums cannot detect. It provides the highest confidence that the application will work correctly after cutover.

Distractor analysis: A is incorrect because row count validation confirms that the same number of rows were migrated but does not verify that row values are correct. A migration that truncates values or converts data types incorrectly would pass row count validation while introducing data errors. B is incorrect because checksum comparison verifies that row data is byte-for-byte identical, which is stronger than row counts but still does not verify that application queries return the expected results — especially when data types are mapped differently. D is incorrect because DMS built-in validation combines Level 1 and Level 2, which is better than either alone but does not reach the application-level validation that Level 3 provides.

---

### Question 10

A retail company requires near-zero downtime during their Cloud SQL migration. The application cannot be in read-only mode for more than 60 seconds. Which migration and cutover strategy best meets this requirement?

- A) One-time DMS migration with a scheduled 4-hour maintenance window for the full migration and cutover
- B) Continuous DMS migration running until replication lag drops below 5 seconds, then switching application connection strings to Cloud SQL within a 60-second window
- C) Dual-write application pattern where the application writes to both the source and Cloud SQL simultaneously for several months before decommissioning the source
- D) `pg_dump` or `mysqldump` with a 2-hour maintenance window for the full export and restore followed by immediate cutover

Correct Answer: B — Continuous DMS migration keeps source and target synchronized in near real-time. When replication lag drops to near zero (below 5 seconds), the application can stop writes to the source, wait for lag to reach zero, and switch connection strings to Cloud SQL — all within 60 seconds. This minimizes downtime to the duration of the final lag flush, not the total migration time.

Distractor analysis: A is incorrect because a one-time migration does not maintain ongoing synchronization. The entire dataset must be migrated during the maintenance window, which for a large database takes hours — far longer than the 60-second limit. C is incorrect because dual-write adds application complexity, requires code changes, and the 60-second requirement applies to the final cutover. Dual-write does not by itself achieve 60-second cutover — it still requires a coordinated switch. D is incorrect because `pg_dump`/`mysqldump` requires the source to be offline (or in read-only mode) for the duration of the export and restore, which for large databases takes hours, far exceeding 60 seconds.

---

Reference: cloud.google.com/learn

---

### Question 11 (5 points)

A team migrating from MySQL 5.7 to Cloud SQL for MySQL 8.0 is using DMS. The source has `binlog_format = STATEMENT`. The DMS connection test passes but the migration job fails after initial load during CDC. What is the root cause?

A) MySQL 8.0 on Cloud SQL does not support statement-based replication; the source must use `binlog_format = ROW` for DMS CDC to function correctly.
B) The MySQL 5.7 version is too old for DMS; a minimum of MySQL 5.7.34 is required.
C) `STATEMENT` format requires GTID mode to be disabled; enabling GTID caused the conflict.
D) The DMS job failed because Cloud SQL for MySQL 8.0 requires `binlog_expire_logs_seconds` instead of `expire_logs_days`.

**Correct Answer:** A

**Distractor Analysis:**

- B) MySQL 5.7 is a supported DMS source version; the version is not the cause of the CDC failure.
- C) GTID mode and binlog format are independent settings; STATEMENT format does not require GTID to be disabled, and the failure is caused by the format incompatibility, not a GTID conflict.
- D) Log retention parameter naming is a version difference but does not cause CDC to fail; DMS reads the binary log using the replication protocol, which works regardless of which parameter name controls log retention.

---

### Question 12 (5 points)

During a PostgreSQL-to-Cloud SQL DMS migration, the team needs to maintain application read traffic against the target while migration is in progress. Which Cloud SQL feature allows read queries to run against the target during migration without interfering with DMS CDC replication?

A) Promote the DMS target to primary so it can accept both reads and writes.
B) Create a read replica of the Cloud SQL migration target; applications query the replica while DMS writes to the primary target.
C) Use the Cloud SQL Auth Proxy to route read queries to the target simultaneously with DMS replication.
D) Enable Cloud SQL Query Insights on the target to route read queries through the monitoring layer.

**Correct Answer:** B

**Distractor Analysis:**

- A) Promoting the target ends the DMS migration permanently; once promoted, replication stops and the target becomes an independent primary — this is the cutover action, not a way to serve reads during migration.
- C) The Cloud SQL Auth Proxy manages connection authentication and TLS; it does not differentiate read vs write traffic or route queries to specific instances.
- D) Query Insights is a monitoring feature that samples queries for performance analysis; it does not route or manage query traffic.

---

### Question 13 (5 points)

A Datastream job streaming CDC changes from PostgreSQL to BigQuery has been running for 3 days. A data analyst reports that a row updated on the source 4 hours ago is not yet visible in BigQuery. What is the most likely cause?

A) Datastream has a 6-hour replication delay by design for consistency.
B) The Datastream stream is paused or the target BigQuery dataset is in a different region causing routing delays.
C) The PostgreSQL `wal_level` was changed from `logical` to `replica` after Datastream was configured, breaking logical decoding.
D) BigQuery only accepts INSERT operations from Datastream; UPDATE operations are not supported.

**Correct Answer:** C

**Distractor Analysis:**

- A) Datastream provides near-real-time replication with typical latency of seconds to minutes; a 4-hour delay is abnormal and indicates a problem, not designed behavior.
- B) Cross-region routing adds latency of milliseconds to seconds, not hours; a 4-hour delay would be visible as an error in the Datastream metrics, not just a delay.
- D) Datastream supports INSERT, UPDATE, and DELETE operations from PostgreSQL to BigQuery using UPSERT semantics; UPDATE operations are fully supported.

---

### Question 14 (5 points)

A company migrates from on-premises PostgreSQL 12 to Cloud SQL for PostgreSQL 15. After migration, a critical stored function using `WITH RECURSIVE` returns different results than on PostgreSQL 12. What is the most likely cause?

A) Cloud SQL disables recursive CTEs by default; they must be enabled with a database flag.
B) A behavior change between PostgreSQL versions in CTE optimization — PostgreSQL 12 added CTE inlining by default, and PostgreSQL 15 changed the optimizer behavior for certain recursive query patterns.
C) The function was not migrated correctly by DMS; it must be manually recreated.
D) `WITH RECURSIVE` is not supported in Cloud SQL for PostgreSQL 15.

**Correct Answer:** B

**Distractor Analysis:**

- A) Cloud SQL does not disable `WITH RECURSIVE`; recursive CTEs are standard PostgreSQL functionality enabled by default in all supported versions.
- C) DMS migrates data, not functions; the function needed to be manually migrated or converted — but the question states it is returning different results (not an error), implying it was successfully deployed and runs, which points to a behavioral difference between versions.
- D) `WITH RECURSIVE` is standard SQL supported in all PostgreSQL versions from 8.4 onward; Cloud SQL for PostgreSQL 15 fully supports it.

---

### Question 15 (5 points)

A DMS migration job shows `FULL DUMP IN PROGRESS` for 18 hours on a 2 TB MySQL database. The source database write rate is low. What is the most likely bottleneck?

A) The Cloud SQL destination instance's disk write IOPS are saturating during the initial load phase.
B) DMS has a 2 TB size limit and is throttling the migration.
C) The MySQL `max_allowed_packet` setting is too small, causing DMS to retry large row batches.
D) The Cloud SQL Auth Proxy is rate-limiting DMS connections.

**Correct Answer:** A

**Distractor Analysis:**

- B) DMS does not impose a 2 TB size limit on migration jobs; large database migrations are supported and may simply take longer proportional to data volume.
- C) `max_allowed_packet` affects the maximum size of a single MySQL packet; while misconfiguration can cause errors for large BLOBs, it does not cause a general 18-hour slowdown on a 2 TB dump.
- D) The Cloud SQL Auth Proxy is used for application connections, not for DMS replication connections; DMS connects via its own internal mechanism and is not rate-limited by the Auth Proxy.

---

### Question 16 (5 points)

A migration team wants to validate that no rows are missing after a MySQL-to-Cloud SQL migration. They compare `SELECT COUNT(*) FROM orders` on both source and target and get the same number. A week after cutover, a data quality issue is discovered — some order amounts were incorrectly converted from DECIMAL(10,2) to FLOAT. Which validation approach would have caught this?

A) Level 2 column checksum validation — computing an MD5 or CHECKSUM aggregate per table and comparing source vs target.
B) Level 1 row count validation — the same approach already performed, just on a larger sample.
C) Index cardinality check — comparing index statistics between source and target.
D) CDC lag monitoring — ensuring replication lag was below 1 second at cutover.

**Correct Answer:** A

**Distractor Analysis:**

- B) Row count validation was already performed and did not catch the issue; repeating it on a larger sample still only counts rows without checking column values.
- C) Index cardinality statistics reflect the distribution of column values but do not verify that numeric values are stored with correct precision; a FLOAT column has different cardinality characteristics than DECIMAL but this check would not reliably detect precision loss.
- D) CDC lag monitoring measures replication timeliness, not data correctness; near-zero lag only confirms changes arrived quickly, not that they were converted correctly.

---

### Question 17 (5 points)

Which DMS feature allows a team to assess which Oracle objects (tables, procedures, views) will require manual conversion before migrating to Cloud SQL for PostgreSQL, and provides an estimated conversion effort score?

A) DMS Schema Conversion Workspace — analyzes the Oracle schema and generates a compatibility report with conversion recommendations and effort estimates.
B) DMS connection profiles — test network connectivity and show which objects can be replicated.
C) Cloud SQL Migration Center — a separate service that scans Oracle and provides a migration readiness score.
D) BigQuery Migration Service — converts Oracle DDL to BigQuery-compatible schema definitions.

**Correct Answer:** A

**Distractor Analysis:**

- B) DMS connection profiles verify network access and authentication to the source and target databases; they do not analyze schema compatibility or estimate conversion effort.
- C) Migration Center is a Google Cloud service that assesses VM and application migration readiness; it is not specific to Oracle-to-PostgreSQL schema conversion in DMS.
- D) BigQuery Migration Service converts SQL queries and schemas for BigQuery workloads; it is not used for Oracle-to-Cloud SQL PostgreSQL schema conversion.

---

### Question 18 (5 points)

A company runs a 24/7 e-commerce application on MySQL 8.0. They need to migrate to Cloud SQL for MySQL 8.0 (homogeneous migration) with a maximum cutover window of 2 minutes. Which approach achieves this?

A) Use DMS continuous migration; when replication lag reaches under 2 seconds, stop application writes, wait for lag to reach 0, and switch connection strings to Cloud SQL.
B) Use `mysqldump` during a 2-minute maintenance window at midnight; the dump of their 3 TB database will complete in 2 minutes.
C) Use Cloud SQL import from a Cloud Storage backup; imports of large databases complete in under 2 minutes.
D) Create a manual MySQL replica on Cloud SQL and switch application writes to it during the maintenance window.

**Correct Answer:** A

**Distractor Analysis:**

- B) A `mysqldump` of a 3 TB database takes hours, not 2 minutes; this approach would require a multi-hour maintenance window.
- C) Cloud SQL imports of multi-TB databases take hours depending on instance tier and database size; 2 minutes is not achievable for a large database import.
- D) Setting up a manual MySQL replica requires configuring binary log replication outside DMS and is operationally complex; DMS continuous migration is the managed, supported approach designed for this exact scenario.

---

### Question 19 (5 points)

After completing a DMS migration promotion, the team discovers that 3 tables were excluded from the migration job due to missing primary keys on the source. How should the team migrate these 3 tables?

A) Re-run the full DMS migration job with a new configuration that includes the 3 tables after adding primary keys on the source.
B) Add primary keys to the 3 tables on the source, then export and import them separately using `mysqldump` or `pg_dump` for those specific tables.
C) The tables cannot be migrated because DMS requires primary keys and they cannot be added to existing tables.
D) Use BigQuery Data Transfer Service to load the 3 tables from the source into Cloud SQL.

**Correct Answer:** B

**Distractor Analysis:**

- A) Re-running the full DMS migration would re-migrate all tables including those already successfully migrated, risking data conflicts on the Cloud SQL target that now has live application data.
- C) Adding primary keys to existing tables is a standard DDL operation; `ALTER TABLE orders ADD PRIMARY KEY (id)` is valid in both MySQL and PostgreSQL as long as the column has no duplicate or null values.
- D) BigQuery Data Transfer Service loads data into BigQuery, not Cloud SQL; it is not a tool for migrating tables between MySQL/PostgreSQL instances.

---

### Question 20 (5 points)

A DBA is testing a DMS migration by querying `SELECT COUNT(*) FROM orders` on source (returns 1,200,000 rows) and target (returns 1,199,998 rows). The 2-row discrepancy appears during the CDC phase. What is the most likely explanation?

A) CDC is still in progress and the 2 missing rows were inserted on the source after the DMS CDC position snapshot; they will appear on the target within seconds.
B) DMS dropped 2 rows due to a primary key conflict on the target.
C) The target Cloud SQL instance ran out of storage and truncated 2 rows.
D) The COUNT queries were run at different times — the source had 2 more rows inserted between the two COUNT executions.

**Correct Answer:** D

**Distractor Analysis:**

- A) If CDC is actively running and replication lag is near zero, a 2-row discrepancy is more likely a timing artifact than a genuine data loss; however, this explanation is less precise than option D which identifies the root cause (queries run at different times).
- B) A primary key conflict causes DMS to log an error and skip the conflicting row; this would appear in DMS logs as an explicit error, not as a silent 2-row discrepancy.
- C) Cloud SQL storage exhaustion causes write errors and alerts, not silent row truncation; the DMS job would fail with a disk full error before dropping individual rows.

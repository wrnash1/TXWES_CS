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

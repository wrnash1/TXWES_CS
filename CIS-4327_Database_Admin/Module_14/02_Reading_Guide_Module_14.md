# Reading Guide: Module 14 — Database Migration Strategies

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Overview

This reading guide supports Module 14 on database migration strategies. Migration is
one of the most complex real-world database operations and a prominent exam topic.
By the end of this module, you will be able to plan, execute, and validate a database
migration to GCP using appropriate tools and strategies.

**Estimated reading time**: 65–80 minutes

---

## Section 1 — Migration Taxonomy and Planning

### 1.1 Migration Types Expanded

Beyond homogeneous and heterogeneous, migrations can also be classified by destination:

**OLTP migrations**: Moving transactional databases to Cloud SQL, AlloyDB, or Cloud
Spanner. The goal is to maintain the same transactional semantics (ACID guarantees,
low latency per query) on a managed cloud platform.

**OLAP/Analytics migrations**: Moving data warehouses to BigQuery. The schema typically
changes significantly — moving from a normalized star schema or denormalized flat files
to BigQuery's columnar partitioned model.

**Lift-and-shift vs. re-architecture**: A lift-and-shift moves the database with
minimal changes (same schema, same queries). Re-architecture takes the migration
as an opportunity to redesign the schema, optimize partitioning, or decommission
legacy features. Lift-and-shift is faster and lower risk; re-architecture delivers
more long-term benefit.

### 1.2 The Migration Phases

A well-structured migration follows six phases:

**Phase 1 — Assess**: Inventory source schema, data volumes, dependencies, compliance
requirements, and application compatibility.

**Phase 2 — Plan**: Select target service, choose migration tool, define downtime
tolerance, plan validation strategy, draft rollback plan.

**Phase 3 — Prepare**: Set up destination instance, configure networking, prepare
source database (enable binlog/WAL, create migration user), convert schema.

**Phase 4 — Migrate**: Execute the migration job, monitor replication lag, perform
ongoing validation during replication.

**Phase 5 — Cutover**: Execute the cutover plan, switch application traffic, monitor
for errors.

**Phase 6 — Decommission**: Validate post-migration performance, decommission source
after retention period, update documentation and runbooks.

### 1.3 Estimating Migration Duration

Migration duration depends on:

- **Data volume**: A 1 TB database typically takes 2–8 hours for the initial full load
  over a direct network connection (varies with network speed and I/O rate).
- **Table count**: DMS migrates tables in parallel (up to a configurable concurrency
  limit), but very large table counts increase coordination overhead.
- **Replication lag catchup**: After the full load, the target must process all CDC
  events that accumulated during the load. High-write-volume sources may take hours
  to catch up after the initial load completes.

Rule of thumb: Plan for the initial load to take 2–3x longer than a simple bandwidth
calculation would suggest, due to CPU overhead for serialization/deserialization,
network variability, and index build time on the target.

---

## Section 2 — Database Migration Service Deep Dive

### 2.1 DMS Source Requirements by Engine

**MySQL source requirements**:

- MySQL 5.6, 5.7, or 8.0
- `binlog_format = ROW` (not STATEMENT or MIXED)
- `binlog_row_image = FULL`
- Binary log retention: at least 24 hours (7 days recommended)
- Migration user requires: SELECT, RELOAD, LOCK TABLES, REPLICATION SLAVE, REPLICATION CLIENT

**PostgreSQL source requirements**:

- PostgreSQL 9.6 through 15
- `wal_level = logical`
- `max_replication_slots >= 1` (DMS creates one slot)
- `max_wal_senders >= 1`
- Migration user requires REPLICATION privilege and SELECT on all tables

**SQL Server source requirements**:

- SQL Server 2012 or later
- CDC enabled at the database level
- Agent service running (for CDC capture jobs)
- Migration user requires: db_owner or specific CDC permissions

### 2.2 DMS Limitations

Knowing DMS limitations is important for the exam and for scoping real projects:

- DMS does not migrate stored procedures, triggers, functions, or views
  automatically — these must be applied to the target separately before or after
  the data migration.
- DMS does not migrate users and grants — database users must be created on the
  target manually.
- DMS requires the source and target to be the same major engine family (MySQL → Cloud
  SQL MySQL; PostgreSQL → Cloud SQL PostgreSQL) for the data migration path. The schema
  conversion workspace handles heterogeneous DDL conversion but DMS data migration paths
  are engine-specific.
- Table size limits: Very large tables (>500 GB each) may require chunked migration
  approaches or pre-population strategies.

### 2.3 AlloyDB as a Migration Target

AlloyDB for PostgreSQL is a PostgreSQL-compatible database designed for demanding OLTP
workloads. DMS supports AlloyDB as a migration target for PostgreSQL sources.

AlloyDB advantages over Cloud SQL for PostgreSQL:

- Up to 4x faster reads for analytical queries (columnar cache)
- Up to 2x faster writes
- Automatic intelligent read-replica routing
- Native integration with Vertex AI for in-database ML inference

When to choose AlloyDB as a migration target vs. Cloud SQL:

- Choose AlloyDB for high-throughput OLTP workloads requiring both transactional
  performance and some analytical query capability.
- Choose Cloud SQL for standard OLTP workloads, smaller databases, or when cost
  efficiency is the primary concern.

---

## Section 3 — Schema Conversion

### 3.1 DMS Schema Conversion Workspace

The DMS schema conversion workspace is a browser-based IDE for converting source
schemas. It supports these source-to-target combinations:

- Oracle → Cloud SQL for PostgreSQL
- SQL Server → Cloud SQL for PostgreSQL
- MySQL → Cloud SQL for PostgreSQL
- PostgreSQL → AlloyDB

The workspace workflow:

1. Connect to the source database.
2. DMS extracts the DDL for all selected objects.
3. The AI-assisted converter analyzes each object and generates a conversion.
4. Issues are categorized as: Action Required, Suggestion, or Information.
5. You review and resolve issues interactively.
6. Export the converted DDL.

### 3.2 Handling PL/SQL to PL/pgSQL Conversion

Oracle PL/SQL stored procedures contain constructs with no direct PL/pgSQL equivalent:

**Autonomous transactions** (`PRAGMA AUTONOMOUS_TRANSACTION`): PL/pgSQL does not
support autonomous transactions natively. Workaround: use `dblink` to execute the
autonomous transaction in a separate connection, or redesign to avoid the pattern.

**FORALL bulk operations**: Oracle's `FORALL` bulk INSERT/UPDATE has no exact
PL/pgSQL equivalent. Use `UNNEST` with array parameters for similar bulk operations.

**%TYPE and %ROWTYPE**: Both are supported in PL/pgSQL with identical syntax —
this is a case where conversion is straightforward.

**REF CURSOR**: Oracle's REF CURSOR maps to PostgreSQL's `REFCURSOR` type with
minor syntax differences.

**DBMS_OUTPUT.PUT_LINE**: Maps to `RAISE NOTICE` in PL/pgSQL.

### 3.3 Schema Conversion Testing Strategy

After generating converted DDL:

1. Apply the DDL to a test Cloud SQL instance.
2. Run the pgTAP test framework (PostgreSQL unit testing) against the converted
   stored procedures and functions with known inputs and expected outputs.
3. Compare outputs against the source database running the original procedures.
4. Document all conversion issues and resolutions in a migration log.

---

## Section 4 — Validation Strategies

### 4.1 Validation by Phase

Validation is not a single step at the end — it should occur continuously:

| Phase | Validation Activity |
|---|---|
| Post-schema conversion | Apply DDL to test instance; fix errors |
| During initial load | Monitor DMS progress; spot-check row counts |
| Post-load (before CDC) | Full row count comparison; checksum samples |
| During CDC | Periodic row count spot checks; verify no replication lag |
| Pre-cutover | Full validation report; application-level query comparison |
| Post-cutover | Monitor application error rates; compare query latency |

### 4.2 Custom Validation Queries

For tables that cannot tolerate any data loss, write custom validation queries:

```sql
-- Compare aggregate values between source and target
-- Run on both source and target; outputs must match

SELECT
  DATE_TRUNC('month', order_date) AS month,
  SUM(revenue)                    AS total_revenue,
  COUNT(*)                        AS row_count,
  MIN(order_id)                   AS min_id,
  MAX(order_id)                   AS max_id
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY month
ORDER BY month;
```

If the aggregates match between source and target, you have high confidence in the
data integrity of that table.

---

## Section 5 — Rollback Planning

Every migration needs a rollback plan. The plan must be tested before cutover.

**Rollback decision point**: Define a specific time limit after cutover during which
you will monitor the application. If a critical issue occurs within this window
(typically 15–60 minutes), trigger the rollback.

**Rollback steps for a DMS migration**:

1. Switch application connection strings back to the source database.
2. Re-enable writes on the source database.
3. The source database now has all data up to the cutover point. Any writes that
   reached the Cloud SQL target during the monitoring window are lost.
4. Capture and replay any transactions that were written to Cloud SQL and not on
   the source (if feasible and necessary).

**Data divergence window**: From the moment replication is broken (target promoted)
until the rollback is complete, writes to the Cloud SQL target are not replicated
back to the source. This is the data divergence window — minimize it by detecting
and triggering rollback quickly.

**Prevention**: If data loss of any amount is unacceptable, maintain dual-write mode
for a longer period rather than cutting over fully on day one.

---

## Section 6 — Key Terms

**Homogeneous migration**: Migration between the same database engine type and version family.

**Heterogeneous migration**: Migration between different database engine types, requiring schema conversion.

**Database Migration Service (DMS)**: Google Cloud's managed service for migrating databases to Cloud SQL and AlloyDB.

**Change Data Capture (CDC)**: Technique for capturing database changes in real time by reading transaction logs.

**Replication lag**: The delay between a change on the source and its application on the target during CDC replication.

**Schema conversion workspace**: The DMS browser-based tool for converting DDL from one database dialect to another.

**Replication slot** (PostgreSQL): A durable cursor in the WAL that ensures CDC consumers do not miss changes.

**Cutover**: The moment production traffic is switched from the source to the target database.

**Blue-green deployment**: Running source and target in parallel, gradually shifting traffic from source to target.

**Datastream**: Google Cloud's native CDC service supporting streaming replication to BigQuery, Cloud Storage, and Spanner.

---

## Section 7 — Review Questions

1. What is the difference between a homogeneous and heterogeneous migration? Give an example of each.

2. What does DMS require on a MySQL source to enable CDC? Why is `binlog_format=ROW` required specifically?

3. DMS does not migrate stored procedures. What steps must you take to ensure stored procedures are available on the target before cutover?

4. Describe the three levels of migration validation. Why is Level 3 (application-level) more thorough than Level 1 (row count)?

5. What is replication lag and how does it affect cutover timing?

6. A DMS cutover has been executed and the application is running on Cloud SQL. Thirty minutes later, a critical data corruption bug is detected. Can you resume DMS replication to sync from the source? Why or why not?

7. What is the difference between DMS and Datastream? When would you choose Datastream over DMS?

8. Describe the dual-write pattern. What is its primary risk, and when is it appropriate?

9. Why is post-migration performance validation necessary even after a row-count validation passes?

10. What GCP service would you use to migrate 200 TB of historical data from a Teradata on-premises warehouse to BigQuery?

---

## Section 8 — Certification Exam Alignment

Migration is tested across multiple exam domains:

- **Section 1 (Design)**: Choosing the right migration strategy and target service
- **Section 2 (Ingest and manage)**: Using DMS, Datastream, and BigQuery DTS
- **Section 3 (Migrate)**: Full coverage — migration tools, validation, cutover planning
- **Section 5 (Monitor)**: Monitoring DMS replication lag, post-migration performance

Expect 5–7 migration questions on the exam, many in scenario format requiring you to
choose between DMS, Datastream, BigQuery DTS, and manual approaches.

---

## Recommended Resources

- DMS documentation: cloud.google.com/database-migration/docs
- Datastream documentation: cloud.google.com/datastream/docs
- BigQuery Data Transfer Service: cloud.google.com/bigquery/transfer
- DMS schema conversion: cloud.google.com/database-migration/docs/schema-conversion-workspace
- Migration best practices: cloud.google.com/solutions/database-migration-best-practices

---

---

## 9. Supplemental Resources

The following free, open-access resources support Module 14 topics:

**1. [Database Migration Service Documentation — Overview](https://cloud.google.com/database-migration/docs/overview)**
Covers supported source and target database pairs, migration job types (one-time vs continuous), prerequisites for MySQL and PostgreSQL sources, and connection profile configuration.

**2. [Database Migration Service Documentation — Schema Conversion Workspace](https://cloud.google.com/database-migration/docs/schema-conversion-workspace)**
Explains how to use the DMS schema conversion workspace to assess Oracle-to-PostgreSQL compatibility, review auto-converted objects, and manage manual conversion effort for stored procedures and triggers.

**3. [Datastream Documentation — Overview](https://cloud.google.com/datastream/docs/overview)**
Covers Datastream architecture, supported source databases (PostgreSQL, MySQL, Oracle), target destinations (BigQuery, Cloud Storage), and the CDC streaming pipeline configuration.

**4. [Google Cloud — Database Migration Best Practices](https://cloud.google.com/architecture/database-migration-best-practices)**
Architecture guidance for planning migration phases, choosing between one-time and continuous migration, performing data validation, and planning the cutover window to minimize downtime.

---

Module 14 Reading Guide — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.

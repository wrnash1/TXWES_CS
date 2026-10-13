# Video Script: Module 14 — Database Migration Strategies (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Database Engineer

---

## SLIDE 1 — Part 2 Introduction

Welcome back to Module 14. In Part 1 we covered migration types, DMS architecture,
CDC-based continuous migration, and pre-migration assessment.

In Part 2 we focus on:

- Schema conversion for heterogeneous migrations
- Migration validation techniques
- Cutover planning and minimal-downtime strategies

---

## SLIDE 2 — Schema Conversion Challenges

In heterogeneous migrations, the schema must be translated from the source dialect
to the target dialect. This is rarely a one-to-one mapping.

Common conversion challenges when migrating from Oracle or SQL Server to PostgreSQL:

**Data type differences**:

| Oracle / SQL Server | PostgreSQL Equivalent |
|---|---|
| `NUMBER(10,2)` | `NUMERIC(10,2)` |
| `VARCHAR2(100)` | `VARCHAR(100)` |
| `DATE` (includes time) | `TIMESTAMP` |
| `IDENTITY` column | `SERIAL` or `GENERATED ALWAYS AS IDENTITY` |
| `NVARCHAR` | `VARCHAR` (UTF-8 native) |

**Procedural code**: Oracle PL/SQL and SQL Server T-SQL stored procedures and
functions do not run on PostgreSQL. They must be rewritten in PL/pgSQL. This is
the most time-consuming part of a heterogeneous migration and often requires
application developers, not just DBAs.

**Sequences**: Oracle uses standalone sequences; PostgreSQL uses sequences attached
to columns. Migrating sequence values requires capturing the current value and
resetting the PostgreSQL sequence after data load.

**System functions**: Expressions like `SYSDATE`, `NVL()`, `DECODE()` (Oracle) or
`GETDATE()`, `ISNULL()` (SQL Server) must be replaced with PostgreSQL equivalents
(`NOW()`, `COALESCE()`, `CASE WHEN`).

---

## SLIDE 3 — DMS Schema Conversion Tool

DMS includes an integrated schema conversion tool with AI-assisted suggestions.
The workflow is:

1. Connect the schema conversion workspace to your source database.
2. DMS analyzes the source schema and generates a PostgreSQL-compatible DDL script.
3. Issues are flagged at three severity levels:
   - **Action required**: The conversion could not be automated; manual fix needed.
   - **Suggestion**: DMS provides a recommended translation that should be reviewed.
   - **Information**: Automatically converted; informational note only.
4. You resolve each issue interactively, applying DMS suggestions or writing custom
   translations.
5. Export the final converted DDL script and apply it to the destination database.

The schema conversion workspace is separate from the migration job. You can iterate
on the schema conversion without affecting an in-progress migration.

For the exam: DMS schema conversion handles most simple data type mappings and some
function translations automatically, but stored procedures and complex triggers almost
always require manual intervention.

---

## SLIDE 4 — Manual Schema Conversion Best Practices

When DMS flags issues requiring manual resolution:

**Stored procedures**: Create a test suite for each stored procedure before migration.
Use the test suite to validate that the PL/pgSQL version produces the same outputs
as the original. Regression testing is essential.

**Triggers**: Audit every trigger on the source. Many triggers implement business
logic that belongs in the application layer. Migration is an opportunity to refactor
triggers into application code, reducing database coupling.

**Views**: Most views translate cleanly, but views using engine-specific syntax
(e.g., Oracle's hierarchical `CONNECT BY` queries) need rewriting. PostgreSQL uses
recursive CTEs (`WITH RECURSIVE`) as the equivalent.

**Indexes**: Index types differ between engines. Oracle Bitmap indexes (useful for
low-cardinality columns in data warehouses) have no direct PostgreSQL equivalent.
GIN and GiST indexes in PostgreSQL cover use cases not served by B-tree indexes.

---

## SLIDE 5 — Migration Validation

After loading data to the target, validation confirms that the migration was successful.
Validation operates at three levels:

**Level 1 — Row count validation**:

The simplest check. Compare row counts per table between source and target.

```sql
-- Source:
SELECT table_name, table_rows
FROM information_schema.tables
WHERE table_schema = 'mydb';

-- Target (Cloud SQL for PostgreSQL):
SELECT relname, n_live_tup
FROM pg_stat_user_tables
WHERE schemaname = 'public';
```

Limitation: Row count match does not guarantee data correctness — only that the
right number of rows were transferred.

**Level 2 — Checksum / hash validation**:

Compute a checksum or aggregate hash over column values and compare between source
and target. DMS's built-in data validation performs this comparison.

For large tables, validate a sample:

```sql
-- PostgreSQL: checksum a sample of rows
SELECT MD5(CAST(order_id AS TEXT) || CAST(revenue AS TEXT) || CAST(order_date AS TEXT))
FROM orders
WHERE order_id % 1000 = 0   -- 0.1% sample
ORDER BY order_id;
```

**Level 3 — Application-level validation**:

Run a subset of the application's read queries against both source and target and
compare results. This is the most rigorous validation and catches conversion errors
in views, functions, and computed columns that simpler row-count checks miss.

---

## SLIDE 6 — Data Validation with DMS

DMS includes a built-in data validation feature that automates Level 1 and Level 2
validation. To run data validation:

1. In the DMS migration job console, click **Create data validation job**.
2. Select the tables to validate.
3. DMS compares row counts and column-level checksums and produces a report.
4. The report shows tables with matching, mismatching, or unvalidated data.

Common causes of validation failures:

- **Timezone handling**: Source stores timestamps in local time; PostgreSQL stores
  in UTC by default. `TIMESTAMP WITHOUT TIME ZONE` vs. `TIMESTAMP WITH TIME ZONE`
  differences cause apparent mismatches.
- **Character encoding**: Source uses Latin-1 or Windows-1252 encoding; Cloud SQL
  uses UTF-8. Special characters (accents, symbols) may differ.
- **Float precision**: Floating-point column values may differ slightly after
  conversion. Use `NUMERIC` instead of `FLOAT` for financial data to avoid this.

---

## SLIDE 7 — Cutover Planning

Cutover is the moment you switch production traffic from the source to the target
database. This is the highest-risk step in any migration.

**Cutover checklist**:

- Replication lag is near zero (< 30 seconds, ideally < 5 seconds)
- All data validation checks pass
- Application connection strings and environment variables are staged and ready to swap
- Rollback plan is documented and tested
- Maintenance window is communicated to all stakeholders
- Database backups of both source and target exist immediately before cutover

**Cutover sequence for a minimal-downtime migration**:

1. Stop writes to the source database (application in read-only mode or maintenance page)
2. Wait for replication lag to reach exactly zero
3. Verify final row counts match
4. Promote the Cloud SQL target to standalone (break replication)
5. Update application connection strings to point to Cloud SQL
6. Re-enable writes on the application
7. Monitor the application for errors for 15–30 minutes
8. If stable: decommission the source (after retaining it as backup for 30+ days)
9. If errors detected: roll back application to source (replication cannot be resumed
   after promotion — this is a one-way operation)

---

## SLIDE 8 — Minimal-Downtime Migration Patterns

**Blue-green deployment pattern**:

Run source (blue) and target (green) in parallel. Route a small percentage of read
traffic to the green database first. Monitor for errors. Gradually shift more traffic
until 100% of traffic is on green. Cut writes at the final step.

This pattern works well when your application supports configurable database endpoints
(e.g., via a connection pool with multiple backends).

**Dual-write pattern**:

During the transition period, the application writes to both source and target
simultaneously. Reads shift to the target gradually. Once reads are fully on the
target and validated, stop writes to the source.

Risk: Dual-write increases application complexity and can cause data divergence if
one write succeeds and the other fails. Use only with a reliable transaction
coordinator or when data loss of a small window is acceptable.

**Shadow read pattern**:

Route all writes to the source. For reads, send a copy of each read query to the
target as a shadow read. Compare results without serving shadow results to users.
This validates correctness before any production traffic is served from the target.

---

## SLIDE 9 — Alternative Migration Tools

DMS is the primary tool, but not the only one. Know these alternatives for the exam:

**Striim**: A third-party real-time data streaming platform available in the GCP
Marketplace. Supports heterogeneous migrations including Oracle-to-BigQuery with
real-time CDC. Useful when DMS does not support the source engine.

**Datastream**: Google Cloud's native CDC and replication service. Supports MySQL,
PostgreSQL, Oracle, and SQL Server as sources. Streams changes to Cloud Storage,
BigQuery, or Cloud Spanner. More flexible than DMS for non-Cloud SQL destinations.

**Dataflow + custom connectors**: For complex ETL transformations during migration,
Dataflow pipelines can read from source databases, transform data, and write to any
GCP destination. Suitable for data cleanup, deduplication, or schema reshaping
during migration.

**BigQuery Data Transfer Service**: For migrating from other data warehouses (Redshift,
Teradata, Netezza) directly into BigQuery. Handles large-scale historical data transfers.

**pg_dump / mysqldump**: For small databases where downtime is acceptable. Simple,
reliable, well-understood. Load the dump into Cloud SQL using `gcloud sql import`.

---

## SLIDE 10 — Post-Migration Tasks

Migration is not complete at cutover. Post-migration tasks include:

**Performance validation**: Run the application's performance test suite against
the Cloud SQL target. Index strategies that worked on the source may need tuning
on Cloud SQL (e.g., different query planner behavior in PostgreSQL vs. Oracle).

**Connection pool reconfiguration**: Cloud SQL has connection limits per instance
tier. Verify that your connection pool settings (max connections, connection timeout)
are appropriate for the Cloud SQL instance size.

**Monitoring setup**: Configure Cloud Monitoring dashboards and alerts for the new
Cloud SQL instance. Establish baseline metrics for CPU, memory, disk I/O, and
query latency.

**Source decommission**: After 30 days of stable production operation on Cloud SQL,
take a final backup of the source, then decommission it. Retain the backup for
any audit or rollback needs.

**Cost review**: Compare actual Cloud SQL costs against estimates. Adjust instance
tier if the instance is consistently over- or under-utilized.

---

## SLIDE 11 — Module 14 Summary

Migration strategy summary for the exam:

- **Homogeneous**: Same engine. DMS handles schema automatically. Primary effort is
  connectivity, validation, and cutover.
- **Heterogeneous**: Different engine. Requires schema conversion. DMS's schema
  conversion tool handles simple mappings; stored procedures need manual rewriting.
- **DMS**: Serverless, CDC-based, supports one-time and continuous migrations to
  Cloud SQL and AlloyDB.
- **CDC mechanisms**: MySQL uses binlog; PostgreSQL uses WAL/logical replication;
  SQL Server uses CDC tables.
- **Validation**: Level 1 (row count), Level 2 (checksums), Level 3 (application queries).
- **Cutover**: Stop writes → drain replication → promote → switch app → monitor.
  One-way operation — rollback requires app-level switch-back, not DMS resumption.
- **Alternatives**: Datastream for streaming CDC to BigQuery/Spanner; BigQuery DTS
  for warehouse migrations; Dataflow for complex ETL transformations.

Complete the lab, quiz, and discussion. Module 15 covers automation and monitoring.

---

*End of Part 2 Script*

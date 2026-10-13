# Video Script: Module 14 — Database Migration Strategies (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Database Engineer

---

## SLIDE 1 — Welcome and Module Overview

Welcome to Module 14 of CIS-4327. I'm Professor Nash, and today we focus on one of
the most practical topics in cloud database administration: migrating databases to
Google Cloud Platform.

Database migrations are complex, high-stakes operations. Done well, they move an
organization's data to a better platform with minimal disruption. Done poorly, they
cause data loss, extended downtime, and loss of stakeholder trust.

In Part 1 we cover:

- Migration taxonomy: homogeneous vs. heterogeneous migrations
- Google's Database Migration Service (DMS)
- Continuous migration and change data capture (CDC)

In Part 2 we cover:

- Schema conversion with the Database Migration Service
- Migration validation strategies
- Cutover planning and minimal-downtime techniques

Let's get started.

---

## SLIDE 2 — Migration Taxonomy

Before choosing tools, you need to classify your migration. There are two primary types:

**Homogeneous migration**: Source and target use the same database engine.

Examples:

- MySQL 5.7 on-premises → Cloud SQL for MySQL 8.0
- PostgreSQL 12 on AWS RDS → Cloud SQL for PostgreSQL 15
- SQL Server 2019 on-premises → Cloud SQL for SQL Server 2019

In homogeneous migrations, the schema and data types transfer directly. The main
challenges are version differences (features added or removed between versions) and
network/connectivity setup.

**Heterogeneous migration**: Source and target use different database engines.

Examples:

- Oracle 19c on-premises → Cloud SQL for PostgreSQL 15
- Microsoft SQL Server → Cloud Spanner
- MySQL → BigQuery (OLTP to OLAP)

Heterogeneous migrations require schema conversion — translating data types, stored
procedures, triggers, sequences, and other engine-specific constructs from one
dialect to another. This is significantly more complex than homogeneous migration.

For the exam: always identify the migration type first. DMS handles both, but
heterogeneous migrations require more preparation and validation.

---

## SLIDE 3 — Google Database Migration Service (DMS) Overview

Database Migration Service is a Google Cloud managed service that simplifies
migrating databases to Cloud SQL with minimal disruption to running workloads.

Key capabilities:

- **Serverless**: No infrastructure to provision for DMS itself
- **Continuous replication**: DMS can keep the source and target in sync in near
  real-time using change data capture (CDC), enabling minimal-downtime cutover
- **Supported sources**: MySQL, PostgreSQL, SQL Server (for Cloud SQL targets);
  MySQL and PostgreSQL (for AlloyDB targets)
- **Free to use**: DMS itself does not charge for the service; you pay for the
  Cloud SQL destination instance and network egress
- **Integrated schema conversion**: DMS includes Gemini-assisted schema conversion
  for heterogeneous migrations

DMS is the primary tool you should recommend on the exam for migrations to Cloud SQL
and AlloyDB. For BigQuery migrations, use BigQuery Data Transfer Service or Dataflow.

---

## SLIDE 4 — DMS Architecture: Connection Profiles and Migration Jobs

DMS organizes migrations around two key concepts:

**Connection Profile**: Stores the connection details for a database (hostname, port,
username, password or SSL certificates). You create one connection profile for the
source and one for the destination.

**Migration Job**: Ties a source connection profile to a destination, specifies the
migration type (one-time or continuous), and manages the migration lifecycle.

The two migration job types:

1. **One-time migration**: DMS performs a full dump and load of the source database
   to the destination. No ongoing replication. Simple and suitable for development
   migrations or when downtime is acceptable.

2. **Continuous migration**: DMS performs an initial full load followed by ongoing
   CDC replication. The target stays synchronized with the source until you perform
   cutover. This is the standard approach for production migrations with minimal
   downtime requirements.

---

## SLIDE 5 — Change Data Capture (CDC) Deep Dive

Continuous migration relies on CDC — a technique for capturing database changes
in real time and applying them to the target.

How CDC works for different engines:

**MySQL**: DMS uses the binary log (binlog). The source MySQL instance must have
`binlog_format=ROW` and binlog retention enabled (at least 3 days for safety).

```bash
# Verify binlog settings on source MySQL:
SHOW VARIABLES LIKE 'binlog_format';
SHOW VARIABLES LIKE 'expire_logs_days';
```

**PostgreSQL**: DMS uses logical replication via the write-ahead log (WAL). The source
must have `wal_level=logical` and a replication slot. DMS creates the replication slot
automatically during migration setup.

```sql
-- Verify WAL level on source PostgreSQL:
SHOW wal_level;

-- DMS creates this automatically, but you can verify:
SELECT * FROM pg_replication_slots;
```

**SQL Server**: DMS uses SQL Server's native CDC feature, which captures changes
from the transaction log into CDC tables.

Important: CDC requires the DMS service account to have replication privileges on
the source database. On managed services (AWS RDS, Azure SQL), specific parameter
group settings are required to enable replication.

---

## SLIDE 6 — DMS Connectivity Options

DMS needs network connectivity between the source database and the Cloud SQL
destination. Three connectivity modes:

**IP allowlist**: DMS adds its static IP ranges to the source database's firewall
rules. Simplest setup but exposes the source to external IP ranges.

**Reverse SSH tunnel**: A compute instance inside your VPC establishes an outbound
SSH tunnel to DMS. Useful when the source is on-premises and behind a strict firewall
that blocks inbound connections.

**VPC Peering**: If the source is in a GCP VPC (e.g., a Compute Engine VM running
MySQL), peer the source VPC with the DMS private network. Most secure option for
GCP-hosted sources.

For on-premises sources, the **reverse SSH tunnel** is the most common choice because
most corporate firewalls allow outbound SSH (port 22) but block inbound connections.

---

## SLIDE 7 — Setting Up a DMS Migration Job (Step by Step)

Here is the high-level workflow for a MySQL to Cloud SQL continuous migration:

**Step 1**: Prepare the source database.

- Enable binary logging: `binlog_format=ROW`, `expire_logs_days=7`
- Create a DMS migration user with replication privileges:

```sql
CREATE USER 'dms_user'@'%' IDENTIFIED BY 'strong-password';
GRANT SELECT, RELOAD, LOCK TABLES, REPLICATION SLAVE, REPLICATION CLIENT
  ON *.* TO 'dms_user'@'%';
FLUSH PRIVILEGES;
```

**Step 2**: Create the destination Cloud SQL instance. DMS can create it automatically
or you can pre-create it with specific configuration (CMEK, Private IP, etc.).

**Step 3**: Create connection profiles in DMS for both source and destination.

**Step 4**: Create the migration job — select source profile, destination profile,
migration type (continuous), and choose which databases to migrate.

**Step 5**: Run the migration test. DMS validates connectivity, permissions, and
binlog configuration before starting the actual migration.

**Step 6**: Start the migration. DMS performs the initial full dump, then transitions
to CDC replication.

**Step 7**: Monitor replication lag in the DMS console. When lag reaches near zero,
you are ready for cutover.

---

## SLIDE 8 — Monitoring DMS Migration Health

During a continuous migration, DMS provides several health indicators:

**Replication lag**: The amount of time the target lags behind the source. A healthy
migration shows lag decreasing to near zero after the initial load. Persistently high
lag indicates the target cannot keep up with source write volume.

**Data validation**: DMS provides a built-in row count comparison between source and
target tables. This is a coarse validation — detailed validation is covered in Part 2.

**Migration status states**:

- `STARTING`: Migration job is being initialized
- `RUNNING`: Full dump in progress or CDC actively replicating
- `CDC IN PROGRESS`: Initial load complete, CDC replicating changes
- `FAILED`: An error stopped the migration — check DMS logs
- `COMPLETED`: Migration finished (for one-time jobs)

Monitoring best practices:

- Set up Cloud Monitoring alerts on DMS replication lag metrics
- Check DMS logs in Cloud Logging for error patterns
- Monitor source database disk space — CDC requires binlog retention, which uses disk

---

## SLIDE 9 — Migration Planning: Pre-Migration Assessment

Before starting any migration, a thorough assessment prevents surprises.

**Object inventory**: Enumerate all objects in the source database — tables, views,
stored procedures, triggers, functions, sequences, indexes, users, and grants.
Many of these require manual conversion in heterogeneous migrations.

**Data volume**: Measure the size of each table. Tables with billions of rows need
special handling — parallel load, chunked migration, or pre-populating with historical
data while migrating only recent data via CDC.

**Application dependencies**: Identify which applications connect to the source database
and what SQL dialects they use. Applications using Oracle-specific SQL functions
need code changes when migrating to PostgreSQL.

**Downtime tolerance**: Understand the business's acceptable maintenance window.
This drives the decision between one-time migration (requires downtime) and continuous
migration (minimal downtime cutover).

**Compliance requirements**: Identify any data sovereignty or encryption requirements
that must be met on the destination before migration begins.

---

## SLIDE 10 — Part 1 Exam Checkpoint

Key exam concepts from Part 1:

- Homogeneous migrations (same engine) are simpler than heterogeneous (different engine)
- DMS is the primary GCP tool for migrating to Cloud SQL and AlloyDB
- DMS supports one-time and continuous (CDC-based) migration jobs
- MySQL CDC uses binary log; PostgreSQL CDC uses WAL logical replication
- DMS connectivity options: IP allowlist, reverse SSH tunnel, VPC peering
- Pre-migration assessment covers object inventory, data volume, app dependencies,
  downtime tolerance, and compliance requirements

In Part 2 we cover schema conversion, migration validation, and cutover planning.

---

*End of Part 1 Script*

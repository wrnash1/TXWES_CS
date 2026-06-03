# Discussion Forum: Module 14 — Database Migration Strategies

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Overview

Database migrations involve technical planning, stakeholder communication, risk
management, and real-time decision-making under pressure. This discussion asks you
to reason through migration scenarios from both a technical and an organizational
perspective — just as you would in a real cloud engineering role.

**Due date**: See course schedule in Canvas.

**Grading**: See rubric at the bottom of this prompt.

---

## Primary Post Prompt

Choose **one** of the following scenarios and write a primary post of at least
250 words addressing all provided questions.

---

### Scenario A — The Oracle Exit

A large telecommunications company runs 47 Oracle databases on-premises ranging
from 50 GB to 8 TB each. The CTO has issued a directive to exit Oracle licenses
entirely within 18 months to reduce costs. All databases will migrate to Cloud SQL
for PostgreSQL.

The technical lead's assessment shows:

- 23 databases are pure data storage (tables and views only) — minimal stored procedure usage
- 18 databases contain complex PL/SQL packages (50+ procedures each) developed over 15 years
- 6 databases use Oracle-specific features: Materialized Views with FAST REFRESH,
  Bitmap indexes, and autonomous transactions
- All 47 databases currently run on-premises behind a strict corporate firewall with
  no direct internet access

Address the following:

1. Propose a migration sequence and timeline for the 47 databases. Which 23 should
   be migrated first, and why? How would you structure the migration of the 18
   complex PL/SQL databases differently?

2. The 6 databases using Oracle-specific features have no direct PostgreSQL equivalents
   for some constructs (e.g., Bitmap indexes, autonomous transactions). How would you
   approach these? Are there workarounds, or do these require application code changes?

3. DMS requires network connectivity to the source Oracle databases, which are behind
   a corporate firewall. Which DMS connectivity option would you recommend, and why?
   What network access must the firewall team enable?

---

### Scenario B — The Zero-Downtime Mandate

A healthcare SaaS company runs a MySQL 5.7 database on AWS RDS. The database powers
their patient scheduling application, which operates 24 hours a day with no scheduled
maintenance windows. The business requires zero downtime during migration to Cloud SQL
for MySQL 8.0.

Additional context:

- The database is 200 GB with approximately 500 writes per second at peak hours
- Peak hours are Monday–Friday 8 AM–6 PM in three US time zones
- The application uses a connection pool (HikariCP) with database URLs configured
  as environment variables in each application server
- The company cannot risk any patient appointment data loss

Address the following:

1. Design a migration plan that achieves zero production downtime. Walk through the
   exact sequence of steps from migration job creation to final decommission of the
   AWS RDS source. What is your definition of "zero downtime" in this context?

2. The database has 500 writes per second at peak. How does this affect your migration
   strategy? At what time of day would you schedule cutover, and why?

3. "Zero data loss" is the stated requirement, but after DMS promotion, any writes
   to Cloud SQL are not backed by DMS replication. Describe the data risk window
   and the maximum acceptable data loss (RPO) for this migration. How would you
   validate that no appointment data was lost during cutover?

---

### Scenario C — The Analytics Migration

A retail company uses an on-premises Teradata data warehouse (8 TB, 200 tables)
for all business reporting. Response times for large reports average 45 minutes.
The data engineering team wants to migrate to BigQuery to reduce report times and
enable self-service analytics.

Additional context:

- The Teradata schema uses a star schema with fact tables (100M–50B rows) and
  dimension tables (1K–10M rows)
- 30 complex reports are run by the finance team using Teradata SQL, which includes
  Teradata-specific extensions (QUALIFY, SAMPLE, EXPAND ON)
- The data is refreshed nightly from an on-premises Oracle ERP system via Teradata
  FastLoad scripts
- Post-migration, the Oracle ERP refresh must continue to land in BigQuery

Address the following:

1. Design the BigQuery schema for the main fact table (`orders`, 50B rows, partitioned
   by order date in Teradata). What BigQuery table options (partitioning, clustering)
   would you apply, and why? How does this differ from the Teradata architecture?

2. Teradata SQL uses `QUALIFY` (similar to PostgreSQL `QUALIFY`/window function
   filtering) and `SAMPLE n PERCENT` (random sampling). Describe how you would
   convert these to standard BigQuery SQL.

3. After migration, the Oracle ERP nightly refresh must write to BigQuery instead
   of Teradata. Design the new data pipeline architecture. Which GCP services would
   you use to extract from Oracle, transform, and load into BigQuery, and how does
   this replace the Teradata FastLoad scripts?

---

## Response Posts

After your primary post, reply to **two classmates** who chose different scenarios.
Each reply must be at least 100 words and do one of the following:

- Identify a risk the original poster did not account for
- Propose an alternative tool or approach with specific justification
- Connect the scenario to a compliance or business continuity framework

---

## Grading Rubric

| Criteria | Points |
|---|---|
| Primary post meets 250-word minimum | 10 |
| Correct use of GCP migration tools and DMS features | 30 |
| All three sub-questions addressed with specifics | 30 |
| Risk/tradeoff reasoning demonstrated | 15 |
| Two substantive peer responses | 15 |
| **Total** | **100** |

---

## Technical Vocabulary Checklist

Strong posts naturally incorporate relevant terms:

- DMS / continuous migration / one-time migration
- Change Data Capture (CDC)
- Binlog / WAL / replication slot
- Replication lag
- Schema conversion workspace
- Homogeneous / heterogeneous
- Cutover / promotion
- Rollback / RPO (Recovery Point Objective)
- Datastream
- BigQuery Data Transfer Service
- Blue-green deployment
- Dual-write
- Validation (Level 1 / 2 / 3)

---

Module 14 Discussion — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.

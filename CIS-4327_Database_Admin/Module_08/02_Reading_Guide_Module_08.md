# Reading Guide: Module 08 — Database Backup and Recovery

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Overview

This reading guide covers database backup strategies, tools, and recovery workflows for both self-managed and Cloud SQL databases. Backup and recovery questions appear on every attempt of the Google Cloud Professional Database Engineer exam. Master this module before the midterm.

---

## Section 1 — Recovery Objectives

### 1.1 RPO — Recovery Point Objective

RPO is the maximum acceptable age of data that must be recoverable after a failure. It answers: "How much data can we afford to lose?"

Examples:

- RPO = 0: Zero data loss. Requires synchronous replication to a second copy. No data is committed until it is written to both copies.
- RPO = 1 hour: You can lose up to one hour of transactions. Requires backups or WAL shipping at least every hour.
- RPO = 24 hours: Daily backups are sufficient.

RPO drives the decision between synchronous replication (RPO = 0), WAL/binary log archiving (RPO = seconds), hourly snapshots (RPO = up to 1 hour), and daily backups (RPO = up to 24 hours).

### 1.2 RTO — Recovery Time Objective

RTO is the maximum time the system can be unavailable after a failure. It answers: "How quickly must we be back online?"

RTO drives the decision between hot standbys (RTO = seconds), warm standbys requiring some replay (RTO = minutes), and cold restores from backup (RTO = hours).

### 1.3 The Cost-RTO-RPO Triangle

Achieving very low RPO and RTO simultaneously is expensive. A system with RPO = 0 and RTO = 60 seconds requires a synchronous hot standby with automatic failover — which roughly doubles infrastructure cost. Organizations must define acceptable RPO and RTO based on business impact analysis of downtime, not engineering preference.

---

## Section 2 — Backup Type Comparison

### 2.1 Full Backup

| Attribute | Value |
|---|---|
| Contents | Complete database snapshot |
| Restore dependencies | None — self-contained |
| Storage requirement | Highest |
| Backup duration | Longest |
| Restore duration | Fastest (single file) |
| Best for | Weekly baseline, pre-migration, small databases |

### 2.2 Incremental Backup

| Attribute | Value |
|---|---|
| Contents | Changes since last backup of any type |
| Restore dependencies | Full backup + all incrementals in chain |
| Storage requirement | Lowest per backup |
| Backup duration | Fastest |
| Restore duration | Slowest (full + every incremental) |
| Best for | Daily/hourly backups of large databases |

### 2.3 Differential Backup

| Attribute | Value |
|---|---|
| Contents | Changes since last full backup |
| Restore dependencies | Full backup + most recent differential only |
| Storage requirement | Grows daily until next full |
| Backup duration | Moderate, increasing during week |
| Restore duration | Fast (two files) |
| Best for | Balance between size and restore simplicity |

### 2.4 Continuous WAL/Binary Log Archiving

| Attribute | Value |
|---|---|
| Contents | Every transaction change, continuously |
| Restore dependencies | Base backup + WAL/binlog segments to target time |
| Storage requirement | High (continuous stream) |
| Backup "duration" | Continuous background process |
| Restore duration | Moderate (replay to specific point) |
| Best for | Point-in-time recovery, RPO measured in seconds |

---

## Section 3 — pg_dump Reference

### 3.1 Format Selection Guide

| Format | Flag | Parallel Restore | Human-Readable | Recommended |
|---|---|---|---|---|
| plain SQL | `-Fp` | No | Yes | Small databases, migrations |
| custom | `-Fc` | Yes | No | Production — best choice |
| directory | `-Fd` | Yes | No | Very large databases |
| tar | `-Ft` | No | No | Legacy compatibility |

### 3.2 pg_dump Important Options

```bash
pg_dump [options] dbname

-h HOST           # database server hostname
-U USERNAME       # database user
-d DBNAME         # database name
-F FORMAT         # p=plain, c=custom, d=directory, t=tar
-Z LEVEL          # compression level 0-9 (custom/directory formats)
-j JOBS           # parallel dump jobs (directory format only)
-s               # schema only, no data
-a               # data only, no schema
-t TABLE          # dump only this table
-n SCHEMA         # dump only this schema
-T TABLE          # exclude this table
-N SCHEMA         # exclude this schema
--no-owner        # omit ownership commands
--no-privileges   # omit privilege commands
--clean           # include DROP commands before CREATE
--if-exists       # use IF EXISTS with DROP commands
```

### 3.3 pg_restore Important Options

```bash
pg_restore [options] filename

-h HOST           # target database server
-U USERNAME       # database user
-d DBNAME         # target database
-j JOBS           # parallel restore workers
-t TABLE          # restore only this table
-s               # restore schema only
-a               # restore data only
--clean           # drop objects before recreating
--if-exists       # use IF EXISTS with DROP
-v               # verbose output
-l               # list archive contents
```

### 3.4 Estimating pg_dump Duration and Size

A rough heuristic: pg_dump custom format runs at 50–150 MB/s depending on compression, disk speed, and CPU. For a 100 GB database:

- At 100 MB/s: approximately 1000 seconds (~17 minutes) to dump
- Compressed output: typically 30–60% of raw data size

Always test on a representative copy of your database to calibrate expectations.

---

## Section 4 — mysqldump Reference

### 4.1 Critical Options

```bash
mysqldump [options] database [tables]

-h HOST                    # server hostname
-u USER                    # username
-p                         # prompt for password
--single-transaction       # consistent InnoDB snapshot (REQUIRED for InnoDB)
--lock-all-tables          # lock all tables (use for MyISAM -- do not use for InnoDB)
--all-databases            # dump all databases
--routines                 # include stored procedures/functions
--triggers                 # include triggers
--events                   # include scheduled events
--hex-blob                 # encode binary columns as hex
--no-tablespaces           # omit tablespace clauses (required for Cloud SQL import)
--set-gtid-purged=OFF      # omit GTID information (required for Cloud SQL import)
--column-statistics=0      # disable column statistics (MySQL 8 compatibility)
```

### 4.2 Cloud SQL Import Requirements

When preparing a `mysqldump` file for import into Cloud SQL, you must add:

```bash
mysqldump -h source-host -u root -p \
  --single-transaction \
  --no-tablespaces \
  --set-gtid-purged=OFF \
  mydb > mydb_for_cloudsql.sql
```

Without `--no-tablespaces`, Cloud SQL import fails because Cloud SQL does not support custom tablespace definitions.

Without `--set-gtid-purged=OFF`, Cloud SQL import may fail if the source database has GTID-based replication configured.

---

## Section 5 — Cloud SQL Backup Architecture

### 5.1 Automated Backup Storage

Cloud SQL automated backups are stored in Google-managed Cloud Storage buckets — you do not see these buckets in your project, but they are billed to your project. Backup storage is charged at the Cloud Storage rate for the region.

### 5.2 Export vs Automated Backup

| Feature | Automated Backup | Manual Export |
|---|---|---|
| Destination | Google-managed bucket | Your Cloud Storage bucket |
| Format | Proprietary snapshot | SQL or CSV |
| Portable to other DB? | No (Cloud SQL only) | Yes (SQL is standard) |
| PITR support | Yes | No |
| Retention control | 1–365 days | Indefinite (manual manage) |
| Speed | Fast (disk snapshot) | Slower (logical export) |

Use automated backups for day-to-day recovery. Use manual exports for migration, compliance archiving, and cross-engine portability.

### 5.3 PITR Retention Window

For Cloud SQL PostgreSQL: transaction logs (WAL segments) are retained alongside the automated backup set. Default retention is 7 days; maximum is 35 days.

For Cloud SQL MySQL: binary logs are retained separately. Default retention is 7 days; maximum is 35 days.

PITR is only available within this window. To extend coverage, configure longer log retention.

---

## Section 6 — Self-Managed PostgreSQL WAL Archiving

### 6.1 Archive Configuration

```ini
# postgresql.conf
wal_level = replica
archive_mode = on
archive_command = 'test ! -f /archive/%f && cp %p /archive/%f'
archive_timeout = 300   # force new WAL segment every 5 minutes maximum
```

For Cloud Storage archiving:

```ini
archive_command = 'gcloud storage cp %p gs://wal-archive-bucket/wal/%f'
```

The archive command must:

- Exit 0 on success
- Exit non-zero on any failure (PostgreSQL will retry)
- Never overwrite an existing archive file (test for existence first)

### 6.2 Restore Configuration (PostgreSQL 12+)

Add to `postgresql.conf` before starting recovery:

```ini
restore_command = 'gcloud storage cp gs://wal-archive-bucket/wal/%f %p'
recovery_target_time = '2024-11-15 14:30:00 UTC'
recovery_target_inclusive = on
recovery_target_action = 'promote'
```

Create a `recovery.signal` file in PGDATA to trigger recovery mode:

```bash
touch /var/lib/postgresql/15/main/recovery.signal
sudo systemctl start postgresql
```

---

## Section 7 — Backup Security

### 7.1 Encryption

Cloud SQL automated backups use Google-managed AES-256 encryption by default. For compliance requirements, use Customer-Managed Encryption Keys (CMEK):

```bash
# Create a Cloud KMS key ring and key
gcloud kms keyrings create db-backup-ring \
  --location=us-central1 \
  --project=my-project

gcloud kms keys create db-backup-key \
  --keyring=db-backup-ring \
  --location=us-central1 \
  --purpose=encryption \
  --project=my-project

# Create Cloud SQL instance with CMEK
gcloud sql instances create my-instance \
  --disk-encryption-key=projects/my-project/locations/us-central1/keyRings/db-backup-ring/cryptoKeys/db-backup-key \
  --project=my-project
```

### 7.2 Access Control for Backup Buckets

Cloud Storage buckets containing database exports should have:

- No public access (`--no-public-access-prevention` must NOT be set)
- Retention policies to prevent premature deletion
- Object versioning for accidental delete protection

---

## Section 8 — Key Terms

| Term | Definition |
|---|---|
| RPO | Recovery Point Objective — maximum acceptable data loss in time |
| RTO | Recovery Time Objective — maximum acceptable downtime after failure |
| Full backup | Complete database snapshot, self-contained restore |
| Incremental backup | Changes since last backup of any type |
| Differential backup | Changes since last full backup |
| PITR | Point-in-time recovery — restore to a specific timestamp |
| pg_dump | PostgreSQL logical backup utility |
| pg_restore | PostgreSQL restore utility for custom/directory/tar formats |
| pg_basebackup | PostgreSQL physical base backup for streaming replication and PITR |
| mysqldump | MySQL logical backup utility |
| WAL archiving | Continuous shipping of WAL segments for PITR |
| Binary log | MySQL's change log; required for PITR and replication |
| CMEK | Customer-Managed Encryption Keys via Cloud KMS |

---

## Study Questions

1. Explain the difference between RPO and RTO. If a business states "we can tolerate losing up to 4 hours of data and can survive 2 hours of downtime," what are the RPO and RTO values?

2. Compare incremental and differential backups. Under what circumstances would you choose differential over incremental?

3. What `mysqldump` flags are required to successfully import a dump into Cloud SQL for MySQL? Explain why each is needed.

4. What is the difference between a Cloud SQL automated backup and a Cloud SQL manual export to Cloud Storage? When would you use each?

5. Walk through the steps to perform PITR on Cloud SQL for MySQL. What must be enabled before the failure occurs?

6. Why does Cloud SQL restore to a new instance rather than overwriting the existing instance?

---

## Certification Exam Checklist

- [ ] RPO definition and how it drives backup frequency
- [ ] RTO definition and how it drives standby/restore architecture
- [ ] Full vs incremental vs differential: restore dependencies
- [ ] pg_dump formats and which supports parallel restore
- [ ] `--single-transaction` requirement for InnoDB mysqldump
- [ ] `--no-tablespaces` and `--set-gtid-purged=OFF` for Cloud SQL import
- [ ] Cloud SQL PITR: enabled automatically for PostgreSQL, requires `--enable-bin-log` for MySQL
- [ ] Cloud SQL restore always creates a new instance
- [ ] Cloud SQL service account needs `storage.objectAdmin` for export/import
- [ ] WAL archiving parameters: `archive_mode`, `archive_command`, `archive_timeout`

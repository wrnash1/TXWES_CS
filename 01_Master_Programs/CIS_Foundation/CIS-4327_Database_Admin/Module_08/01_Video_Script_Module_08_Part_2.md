# Video Script: Module 08 — Database Backup and Recovery (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back. This is Part 2 of Module 08: Database Backup and Recovery.

In Part 1 we covered backup strategies, types, RPO, RTO, Cloud SQL automated backups, and the concept of point-in-time recovery. In Part 2 we get hands-on with the tools: `pg_dump` and `pg_restore` for PostgreSQL, `mysqldump` for MySQL, Cloud SQL export to Cloud Storage, and restore workflows.

---

## Section 1 — pg_dump and pg_restore

`pg_dump` is PostgreSQL's logical backup utility. It exports a database or schema objects to a file. It does not lock the database — it uses MVCC snapshots to produce a consistent dump while the database is live and accepting writes.

### pg_dump Output Formats

`pg_dump` supports four output formats:

- **plain** (`-Fp`) — plain SQL script. Human-readable. Restore with `psql`.
- **custom** (`-Fc`) — compressed binary format. Most flexible. Supports parallel restore. **Recommended for production.**
- **directory** (`-Fd`) — one file per table, parallel-capable.
- **tar** (`-Ft`) — tar archive. Portable but no parallel restore.

### pg_dump Examples

```bash
# Full database dump in custom format (recommended)
pg_dump -Fc -h localhost -U postgres -d mydb -f mydb_backup.dump

# Dump with compression level
pg_dump -Fc -Z 9 -h localhost -U postgres -d mydb -f mydb_backup.dump

# Dump only schema (no data)
pg_dump -Fc --schema-only -h localhost -U postgres -d mydb -f schema_only.dump

# Dump only data (no schema)
pg_dump -Fc --data-only -h localhost -U postgres -d mydb -f data_only.dump

# Dump a single table
pg_dump -Fc -t orders -h localhost -U postgres -d mydb -f orders_backup.dump

# Dump a specific schema
pg_dump -Fc -n analytics -h localhost -U postgres -d mydb -f analytics_schema.dump
```

### pg_restore Examples

```bash
# Restore entire database from custom format
pg_restore -h localhost -U postgres -d newdb --clean --create mydb_backup.dump

# Restore with parallel jobs (speeds up large restores)
pg_restore -h localhost -U postgres -d newdb -j 4 mydb_backup.dump

# Restore only a specific table
pg_restore -h localhost -U postgres -d newdb -t orders mydb_backup.dump

# Preview what will be restored (dry run)
pg_restore --list mydb_backup.dump
```

`-j 4` uses four parallel worker processes. This significantly reduces restore time on multi-core systems. Only the custom and directory formats support parallel restore.

### pg_dumpall

`pg_dumpall` dumps all databases in the cluster, including global objects (roles, tablespaces) that `pg_dump` does not include.

```bash
# Full cluster backup including roles and tablespaces
pg_dumpall -h localhost -U postgres -f full_cluster_backup.sql

# Dump global objects only (roles, tablespaces)
pg_dumpall -h localhost -U postgres --globals-only -f globals.sql
```

Use `pg_dumpall --globals-only` when migrating a PostgreSQL cluster to capture role definitions that `pg_dump` misses.

---

## Section 2 — mysqldump

`mysqldump` is MySQL's logical backup utility. Like `pg_dump`, it produces a consistent snapshot using transaction isolation while the database remains online.

### Key mysqldump Options

```bash
# Full database backup
mysqldump -h 127.0.0.1 -u root -p \
  --single-transaction \
  --routines \
  --triggers \
  --events \
  --hex-blob \
  mydb > mydb_backup.sql

# All databases
mysqldump -h 127.0.0.1 -u root -p \
  --all-databases \
  --single-transaction \
  --routines \
  --triggers \
  --events > all_databases.sql

# Single table
mysqldump -h 127.0.0.1 -u root -p \
  --single-transaction \
  mydb orders > orders_backup.sql
```

**Critical flags:**

- `--single-transaction` — starts a consistent read transaction before the dump. Required for InnoDB tables to get a consistent snapshot without locking. Do not use this with MyISAM tables.
- `--routines` — includes stored procedures and functions. Omitted by default.
- `--triggers` — includes triggers (default in most versions, but explicit is safer).
- `--events` — includes scheduled events.

### Restoring from mysqldump

```bash
# Create the database first
mysql -h 127.0.0.1 -u root -p -e "CREATE DATABASE mydb_restored;"

# Restore
mysql -h 127.0.0.1 -u root -p mydb_restored < mydb_backup.sql
```

For large dumps, pipe through compression:

```bash
# Compressed backup
mysqldump ... mydb | gzip > mydb_backup.sql.gz

# Compressed restore
gunzip < mydb_backup.sql.gz | mysql -h 127.0.0.1 -u root -p mydb_restored
```

### mysqldump Limitations

`mysqldump` produces SQL statements. For large databases (hundreds of GB), it can take hours and produce very large files. For faster logical backups, consider **mydumper/myloader** — a multi-threaded alternative that can dump and restore in parallel.

---

## Section 3 — Cloud SQL Export and Import

Cloud SQL provides a managed export and import workflow that exports directly to Cloud Storage. This is the recommended approach for Cloud SQL — you do not need to run `pg_dump` or `mysqldump` locally.

### Exporting from Cloud SQL

```bash
# PostgreSQL: export in SQL format to Cloud Storage
gcloud sql export sql my-postgres-instance \
  gs://my-backup-bucket/exports/mydb_$(date +%Y%m%d).sql \
  --database=mydb \
  --project=my-project

# PostgreSQL: export as CSV
gcloud sql export csv my-postgres-instance \
  gs://my-backup-bucket/exports/orders_$(date +%Y%m%d).csv \
  --database=mydb \
  --query="SELECT * FROM orders WHERE order_date > '2024-01-01'" \
  --project=my-project

# MySQL: export in SQL format
gcloud sql export sql my-mysql-instance \
  gs://my-backup-bucket/exports/mydb_mysql_$(date +%Y%m%d).sql \
  --database=mydb \
  --project=my-project
```

### Importing into Cloud SQL

```bash
# PostgreSQL: import SQL file
gcloud sql import sql my-postgres-instance \
  gs://my-backup-bucket/exports/mydb_20241115.sql \
  --database=mydb \
  --project=my-project

# MySQL: import SQL file
gcloud sql import sql my-mysql-instance \
  gs://my-backup-bucket/exports/mydb_mysql_20241115.sql \
  --database=mydb \
  --project=my-project
```

### Granting the Cloud SQL Service Account Access to Cloud Storage

Cloud SQL exports and imports using the Cloud SQL service account. You must grant this account `storage.objectAdmin` on the bucket:

```bash
# Get the service account email
gcloud sql instances describe my-instance \
  --format="value(serviceAccountEmailAddress)" \
  --project=my-project

# Grant Storage Object Admin on the bucket
gsutil iam ch serviceAccount:SERVICE_ACCOUNT_EMAIL:objectAdmin \
  gs://my-backup-bucket
```

---

## Section 4 — WAL Archiving for PostgreSQL PITR

For self-managed PostgreSQL (not Cloud SQL), configuring WAL archiving enables continuous point-in-time recovery.

In `postgresql.conf`:

```ini
wal_level = replica
archive_mode = on
archive_command = 'gcloud storage cp %p gs://my-wal-bucket/wal/%f'
archive_timeout = 60
```

`archive_command` runs for each completed WAL segment. `%p` is the full path to the WAL file, `%f` is the filename. The command must return exit code 0 to indicate success.

`archive_timeout = 60` forces a WAL segment switch every 60 seconds even if not full, limiting the maximum data loss to 60 seconds.

### Base Backup for PITR

PITR requires a base backup as the starting point:

```bash
# Take a base backup
pg_basebackup -h localhost -U replicator -D /backup/base \
  --wal-method=stream --checkpoint=fast --label="pitr_base_$(date +%Y%m%d)"
```

### Recovery Configuration

To restore to a specific time (`recovery.conf` in PostgreSQL 11 and earlier; `postgresql.conf` in 12+):

```ini
restore_command = 'gcloud storage cp gs://my-wal-bucket/wal/%f %p'
recovery_target_time = '2024-11-15 14:30:00 UTC'
recovery_target_action = 'promote'
```

---

## Section 5 — Backup Validation and Testing

Taking backups is only half the job. Validating them is equally critical.

### Automated Backup Verification

After every automated backup, run a verification job:

```bash
#!/bin/bash
# Restore to a test instance
gcloud sql instances restore-backup prod-instance \
  --restore-instance=backup-test-instance \
  --backup-id=$(gcloud sql backups list --instance=prod-instance --limit=1 --format="value(id)") \
  --project=my-project

# Wait for restore to complete
while [ "$(gcloud sql instances describe backup-test-instance --format='value(state)')" != "RUNNABLE" ]; do
  sleep 30
done

# Run validation queries
gcloud sql connect backup-test-instance --user=postgres -- \
  -c "SELECT COUNT(*) FROM orders; SELECT MAX(order_date) FROM orders;"

# Clean up test instance
gcloud sql instances delete backup-test-instance --quiet
```

---

## Section 6 — Backup Strategy Decision Matrix

| Scenario | Recommended Strategy |
|---|---|
| Cloud SQL production (simple) | Automated backups + PITR enabled |
| Cloud SQL with compliance retention | Automated backups + manual export to Cloud Storage with long retention |
| Self-managed PostgreSQL | pg_basebackup + WAL archiving to Cloud Storage |
| Large MySQL (> 100 GB) | mysqldump with --single-transaction + binary log backup |
| Pre-migration | On-demand Cloud SQL backup + manual export |
| Cross-region DR | Automated backup + cross-region Cloud Storage copy |

---

## Section 7 — Exam Tips

**Exam scenarios to recognize:**

- Question describes needing "restore to 2 hours ago" → PITR answer. For Cloud SQL MySQL: requires `--enable-bin-log`. For Cloud SQL PostgreSQL: requires automated backups enabled.
- Question asks about largest storage, simplest restore → full backup
- Question asks about fastest backup, most complex restore → incremental
- Question asks for balance between size and restore simplicity → differential
- Question involves granting Cloud SQL export permission → Cloud SQL service account needs `storage.objectAdmin` on the bucket
- Question about restoring Cloud SQL → always restores to a new instance, never overwrites existing

**Common trap:** Cloud SQL PITR restore creates a new instance. Students often assume it overwrites the existing instance. It does not.

---

## Closing

Module 08 is complete. You now have a comprehensive understanding of backup strategies, pg_dump/pg_restore, mysqldump, Cloud SQL automated backups, PITR, and backup validation.

The Module 08 lab walks you through all of these tools hands-on. Complete it before the quiz.

See you in Module 09: High Availability and Replication.

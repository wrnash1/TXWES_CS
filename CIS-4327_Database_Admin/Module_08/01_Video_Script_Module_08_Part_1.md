# Video Script: Module 08 — Database Backup and Recovery (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back to CIS-4327. I am Professor Nash, and this is Module 08: Database Backup and Recovery.

Backups are the last line of defense against data loss. Whether the cause is accidental deletion, ransomware, hardware failure, or software bugs, a reliable backup strategy determines how much data you lose and how long it takes to recover. This module covers backup strategies, types, and the concepts of RPO and RTO — all of which are heavily tested on the Google Cloud Professional Database Engineer exam.

Part 1 covers theory — backup strategies, types, and concepts. Part 2 covers the hands-on tools: `pg_dump`, `pg_restore`, `mysqldump`, Cloud SQL automated backups, and point-in-time recovery.

---

## Section 1 — Why Backups Matter: RPO and RTO

Before we discuss backup types, we need to define two critical terms that will appear in virtually every backup-related exam question.

**RPO — Recovery Point Objective** is the maximum amount of data loss an organization can tolerate, expressed as time. If your RPO is one hour, you must be able to restore to a state no older than one hour before the failure. This directly determines backup frequency — if your RPO is one hour, you cannot take backups only once per day.

**RTO — Recovery Time Objective** is the maximum amount of time the organization can tolerate the database being unavailable after a failure. If your RTO is 30 minutes, the entire restore process — including detection, restore, and verification — must complete within 30 minutes.

These two values drive every backup architecture decision. Lower RPO means more frequent backups and likely more complex recovery mechanisms like continuous WAL archiving. Lower RTO means faster restore mechanisms, possibly multiple standby copies, or pre-warmed hot standbys.

For the exam, remember: **RPO is about data loss (time), RTO is about downtime (time).**

---

## Section 2 — Backup Strategies and Types

There are four main backup types. You need to know all four for the exam.

### Full Backup

A **full backup** captures the complete state of the database at a single point in time. It contains everything needed to restore the database independently — no other backup files are needed.

Advantages:

- Simplest restore process — a single file contains everything
- Fastest recovery time from a full backup

Disadvantages:

- Largest storage requirement
- Longest backup duration — not practical to run every hour on large databases

### Incremental Backup

An **incremental backup** captures only the changes since the **most recent backup of any type** — whether that was a full or a previous incremental.

For example: Full on Sunday, incremental Monday through Saturday. Monday's incremental captures changes since Sunday's full. Tuesday's incremental captures changes since Monday's incremental.

Advantages:

- Smallest individual backup sizes
- Fastest backup duration

Disadvantages:

- Most complex restore process — requires the full backup plus every incremental in sequence
- Any corrupt or missing incremental in the chain breaks the restore

### Differential Backup

A **differential backup** captures all changes since the **last full backup**, regardless of whether incrementals have been taken in between.

For example: Full on Sunday, differential every day. Monday captures changes since Sunday. Tuesday captures changes since Sunday (including Monday's changes again). Saturday captures all changes since Sunday.

Advantages:

- Restore requires only the full backup plus the most recent differential — simpler than incremental chain
- Good balance between backup size and restore complexity

Disadvantages:

- Larger than incrementals — grows daily until the next full backup
- Slower to take than incrementals as the week progresses

### Transaction Log / WAL Backup (Continuous)

For PostgreSQL, WAL archiving; for MySQL, binary log archiving. The database continuously ships completed WAL segments or binary log files to a backup location.

This enables **point-in-time recovery (PITR)** — the ability to restore to any specific moment in time, not just a scheduled backup window.

How PITR works:

1. Restore the most recent full backup to bring the database to a consistent base state.
2. Replay WAL/binary log files from the backup forward to the target recovery timestamp.
3. Stop replay at the exact moment before the disaster occurred.

PITR is how Cloud SQL handles "restore to a specific time" requests.

---

## Section 3 — Backup Storage Considerations

Where you store backups is as important as how you take them.

**The 3-2-1 rule** is the foundational backup storage guideline:

- **3** copies of the data
- **2** different storage media types
- **1** copy offsite (or in a different cloud region)

On Google Cloud, this translates to: your primary database, a Cloud SQL automated backup in Google-managed Cloud Storage, and optionally a manually exported backup in a different region's Cloud Storage bucket.

**Encryption at rest** — All Cloud SQL backups are encrypted using AES-256. You can optionally use customer-managed encryption keys (CMEK) via Cloud KMS.

**Backup retention** — Cloud SQL retains automated backups for 7 days by default, configurable up to 365 days. Transaction logs for PITR are retained for 7 days by default (up to 35 days).

---

## Section 4 — Cloud SQL Automated Backups

Cloud SQL provides fully automated backups with minimal configuration required.

### How Cloud SQL Backups Work

For Cloud SQL MySQL: Cloud SQL takes a full logical backup using a snapshot of the underlying persistent disk. This is faster than `mysqldump` and is crash-consistent.

For Cloud SQL PostgreSQL: Cloud SQL uses a combination of base backups (using pg_basebackup internally) and WAL archiving to Google-managed Cloud Storage.

### Enabling and Configuring Backups

```bash
# Enable automated backups on an existing instance
gcloud sql instances patch my-instance \
  --backup-start-time=02:00 \
  --retained-backups-count=14 \
  --retained-transaction-log-days=7 \
  --project=my-project

# List available backups
gcloud sql backups list \
  --instance=my-instance \
  --project=my-project
```

### On-Demand Backup

```bash
# Create an immediate backup
gcloud sql backups create \
  --instance=my-instance \
  --description="Pre-migration backup" \
  --project=my-project
```

On-demand backups are not affected by the retention policy for automated backups — they persist until you delete them manually. Always take an on-demand backup before schema migrations or major data operations.

---

## Section 5 — Point-in-Time Recovery on Cloud SQL

Cloud SQL PITR allows you to restore a database to any second within the transaction log retention window.

### PostgreSQL PITR on Cloud SQL

For Cloud SQL PostgreSQL, PITR works by restoring a base backup and then replaying WAL segments up to the target time.

**PITR is enabled automatically when you enable automated backups** on Cloud SQL PostgreSQL. No separate configuration is needed.

### MySQL PITR on Cloud SQL

For Cloud SQL MySQL, PITR requires the binary log to be enabled (`--enable-bin-log`). Cloud SQL then retains binary logs for the configured retention period.

### Performing a PITR Restore

PITR on Cloud SQL restores to a **new instance** — it does not overwrite the existing instance. This is a safety feature.

```bash
# Restore to a specific point in time (PostgreSQL or MySQL)
gcloud sql instances restore-backup original-instance \
  --restore-instance=restored-instance \
  --backup-id=BACKUP_ID \
  --project=my-project

# For PITR to a specific timestamp
gcloud sql instances restore-backup original-instance \
  --restore-instance=restored-instance \
  --restore-time=2024-11-15T14:30:00Z \
  --project=my-project
```

---

## Section 6 — Backup Testing — The Most Overlooked Step

An untested backup is not a backup. It is just data you hope is recoverable.

**Backup testing best practices:**

1. **Regular restore drills** — restore the most recent backup to a non-production environment at least monthly.
2. **Data integrity verification** — after restore, run row count comparisons and application smoke tests, not just "did the restore complete without error."
3. **Timing measurement** — measure the actual restore time and compare it against your RTO. If it takes longer than your RTO, your architecture is insufficient.
4. **Document the procedure** — the restore procedure should be a documented runbook that anyone on the team can execute, not tribal knowledge held by one engineer.

For Cloud SQL, you can test restores by restoring to a separate instance and running your application's health check suite against it.

---

## Section 7 — Exam Preparation Summary

Key exam concepts from Part 1:

- **RPO** = maximum acceptable data loss (time); drives backup frequency
- **RTO** = maximum acceptable downtime; drives restore speed and redundancy
- Full backup = complete, independent; incremental = since last backup of any type; differential = since last full
- PITR requires WAL archiving (PostgreSQL) or binary log (MySQL)
- Cloud SQL restores always go to a new instance — never overwrites existing
- On-demand backups persist until manually deleted; automated backups follow retention policy
- PITR for Cloud SQL PostgreSQL is enabled automatically with automated backups
- PITR for Cloud SQL MySQL requires `--enable-bin-log`

---

## Closing

That wraps up Part 1 of Module 08. You now understand the theory behind backup strategies, the four backup types, RPO and RTO, Cloud SQL automated backups, and point-in-time recovery.

In Part 2, we get hands-on with `pg_dump`, `pg_restore`, `mysqldump`, and the Cloud SQL import/export workflow. See you there.

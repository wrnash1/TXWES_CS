# Quiz: Module 08 — Database Backup and Recovery

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

Instructions: Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A company states: "We can tolerate losing up to 4 hours of transaction data, and our database must be fully available again within 1 hour of a failure." What are the RPO and RTO respectively?

- A) RPO = 1 hour, RTO = 4 hours
- B) RPO = 4 hours, RTO = 1 hour
- C) RPO = 4 hours, RTO = 4 hours
- D) RPO = 1 hour, RTO = 1 hour

**Answer: B** — RPO is the maximum acceptable data loss (4 hours of transactions). RTO is the maximum acceptable downtime (1 hour to restore service). These values drive different architectural choices: RPO drives backup frequency, RTO drives restore speed and standby architecture.

---

### Question 2

A DBA takes a full backup on Sunday. On Monday through Saturday, incremental backups are taken. On Friday, the system fails. To restore to end-of-business Thursday, which backups are needed?

- A) Sunday full backup only
- B) Sunday full backup + Thursday incremental only
- C) Sunday full backup + Monday, Tuesday, Wednesday, and Thursday incrementals in sequence
- D) Thursday incremental only

**Answer: C** — Incremental restores require the full backup plus every incremental in the chain up to the target point. Skipping any intermediate incremental makes the restore incomplete.

---

### Question 3

Which `pg_dump` format supports parallel restore with `pg_restore -j`?

- A) plain (`-Fp`)
- B) tar (`-Ft`)
- C) custom (`-Fc`)
- D) Both custom (`-Fc`) and directory (`-Fd`)

**Answer: D** — Both custom and directory formats support parallel restore. Plain SQL format is restored with `psql`, which does not support parallel workers. Tar format does not support parallel restore.

---

### Question 4

You are preparing a `mysqldump` file to import into Cloud SQL for MySQL. Which two flags must be added that would not be needed for a self-managed MySQL restore?

- A) `--single-transaction` and `--routines`
- B) `--no-tablespaces` and `--set-gtid-purged=OFF`
- C) `--hex-blob` and `--events`
- D) `--all-databases` and `--triggers`

**Answer: B** — Cloud SQL does not support custom tablespace definitions (`--no-tablespaces` required) and may reject dumps with GTID information from source instances using GTID replication (`--set-gtid-purged=OFF` required). The other options are general best-practice flags applicable to any restore.

---

### Question 5

What must be enabled on a Cloud SQL for MySQL instance before point-in-time recovery (PITR) is available?

- A) Automated backups only
- B) Binary logging (`--enable-bin-log`)
- C) Read replicas
- D) High availability

**Answer: B** — PITR for Cloud SQL MySQL requires the binary log to be enabled. Without the binary log, Cloud SQL can only restore to the timestamp of a full automated backup, not to an arbitrary point in time.

---

### Question 6

A DBA runs `gcloud sql instances restore-backup prod-instance --restore-instance=recovered-instance --restore-time=2024-11-15T14:00:00Z`. What is the result?

- A) The `prod-instance` database is rolled back to 14:00 UTC, overwriting current data.
- B) A new instance called `recovered-instance` is created containing the database state as of 14:00 UTC.
- C) Cloud SQL rejects the command because PITR cannot target a different instance name.
- D) Both `prod-instance` and `recovered-instance` exist and share the same data after restore.

**Answer: B** — Cloud SQL PITR always restores to a new instance. The original instance is not modified. This is a safety feature that prevents accidental overwriting of a live production database during a restore operation.

---

### Question 7

You run `gcloud sql export sql` and the operation fails with a permissions error. What is the most likely cause and fix?

- A) The Cloud SQL instance is in a different region than the Cloud Storage bucket. Move the bucket to the same region.
- B) The Cloud SQL service account does not have `storage.objectAdmin` permission on the Cloud Storage bucket. Grant that role.
- C) The database is too large to export. Reduce the database size first.
- D) The `--database` flag is not specified. Add `--database=mydb` to the command.

**Answer: B** — Cloud SQL export operations run under the instance's service account. That service account must have `storage.objectAdmin` (or at minimum `storage.objectCreator`) on the target bucket. A missing permission is the most common cause of export failures.

---

### Question 8

What is the key advantage of a differential backup over an incremental backup from a recovery perspective?

- A) Differential backups are smaller than incrementals.
- B) Differential restores require only the full backup and the most recent differential — two files rather than a full plus every incremental in the chain.
- C) Differential backups run faster than incrementals.
- D) Differential backups capture data more frequently than incrementals.

**Answer: B** — The restore advantage of differential is simplicity: two files (full + latest differential) versus potentially many files (full + every incremental). Differentials are not smaller or faster — they grow daily until the next full backup.

---

### Question 9

A Cloud SQL for PostgreSQL instance needs PITR enabled with a 14-day transaction log retention window. Which gcloud command achieves this?

- A) `gcloud sql instances patch my-instance --enable-pitr --pitr-days=14`
- B) `gcloud sql instances patch my-instance --retained-transaction-log-days=14`
- C) `gcloud sql instances patch my-instance --backup-retention=14`
- D) `gcloud sql instances patch my-instance --binlog-retention=14`

**Answer: B** — The flag `--retained-transaction-log-days` controls how long transaction logs (WAL for PostgreSQL, binary logs for MySQL) are retained for PITR. PITR on Cloud SQL for PostgreSQL is enabled automatically when automated backups are enabled; no separate `--enable-pitr` flag exists.

---

### Question 10

A database engineer needs to ensure that backups are actually recoverable. Which practice is most important?

- A) Encrypt all backup files with AES-256.
- B) Store backups in a different region from the source database.
- C) Regularly restore backups to a test environment and verify data integrity against the source.
- D) Take backups every hour regardless of RPO requirements.

**Answer: C** — An untested backup is not a validated backup. Regular restore drills to a test environment, followed by data integrity checks (row counts, application smoke tests), are the only way to confirm that backups are actually recoverable. Encryption and geographic distribution are important for security and availability but do not verify recoverability.

---

### Question 11 (5 points)

A Cloud SQL for PostgreSQL instance has automated backups enabled with a 7-day retention window. PITR is also enabled with `--retained-transaction-log-days=7`. A developer accidentally drops a table at 2:37 PM on a Tuesday. What is the earliest timestamp the DBA can recover to without data loss for that table?

- A) The most recent automated backup checkpoint before 2:37 PM on Tuesday.
- B) Any timestamp within the past 7 days — including 2:36:59 PM on Tuesday — because WAL logs are retained for 7 days.
- C) The previous Sunday when the last full backup was taken.
- D) PITR is not possible once a table is dropped; only a full backup restore can recover a dropped table.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Automated backup checkpoints are the recovery points available without PITR; with WAL log retention enabled, recovery is not limited to checkpoint times but can target any second within the retention window.
  - C) Cloud SQL automated backups run daily by default, not just on Sundays; even without PITR the recovery point would be the most recent daily backup, not a weekly one.
  - D) PITR can recover a dropped table by replaying WAL logs to a point before the DROP statement executed; this is precisely the scenario PITR is designed for.

---

### Question 12 (5 points)

Which `pg_dump` flag is required to create a consistent backup of a large PostgreSQL database without locking any tables during the backup process?

- A) `--lock-wait-timeout=0`
- B) `--no-acl`
- C) `--serializable-deferrable`
- D) `--jobs=4` (parallel dump)

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) `--lock-wait-timeout=0` causes pg_dump to fail immediately if it cannot acquire a lock, rather than waiting; it does not prevent locking entirely.
  - B) `--no-acl` omits privilege (GRANT/REVOKE) statements from the dump; it has no effect on locking behavior during the backup.
  - D) `--jobs=4` parallelizes the dump for faster completion but requires the directory format; it does not itself guarantee a consistent snapshot without locks — consistency requires a transaction isolation setting, which `--serializable-deferrable` provides.

---

### Question 13 (5 points)

A DBA uses `gcloud sql instances restore-backup` and specifies `--restore-instance=recovery-test`. After the command completes, the DBA cannot find the `recovery-test` instance in the Cloud Console. What is the most likely cause?

- A) The restore is still in progress; Cloud SQL restore operations can take 10–60 minutes and the instance appears only after it reaches RUNNABLE state.
- B) The `--restore-instance` flag restores in place; the original instance name is used automatically.
- C) Cloud SQL deleted the recovery instance automatically after the restore completed to save resources.
- D) The instance was created in a different project than the one open in the Cloud Console.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) The `--restore-instance` flag creates a new instance with the specified name; it does not perform an in-place restore on the original instance.
  - C) Cloud SQL does not auto-delete restored instances; they remain until manually deleted.
  - D) While project scope is always worth verifying, the most common explanation when a restore instance is "missing" immediately after the command is that the restore is still in progress and the instance has not yet reached RUNNABLE state.

---

### Question 14 (5 points)

A `mysqldump` is taken from a source MySQL 8.0 server using `--set-gtid-purged=ON`. The import into Cloud SQL for MySQL fails with an error about GTID sets. What change to the dump command resolves the issue?

- A) Replace `--set-gtid-purged=ON` with `--set-gtid-purged=OFF` to exclude GTID information that Cloud SQL cannot accept.
- B) Add the `--all-databases` flag to include all system tables in the dump.
- C) Add the `--single-transaction` flag to ensure a consistent snapshot.
- D) Use `--gtid-mode=ON` on the Cloud SQL target instance before importing.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `--all-databases` includes system databases that Cloud SQL does not permit importing; this would worsen the import, not fix it.
  - C) `--single-transaction` ensures a consistent snapshot of InnoDB tables; it is good practice but does not resolve GTID-related import errors.
  - D) Cloud SQL manages GTID mode internally and does not expose `--gtid-mode` as a configurable flag; the correct fix is on the dump side, not the import target.

---

### Question 15 (5 points)

What is the difference between `pg_dump` and `pg_basebackup` in terms of their backup type and appropriate use case?

- A) `pg_dump` creates a logical backup of a single database using SQL statements; `pg_basebackup` creates a physical binary copy of the entire PostgreSQL cluster suitable for streaming replication setup and PITR base backup.
- B) `pg_dump` requires the database to be offline; `pg_basebackup` works on live databases.
- C) `pg_basebackup` backs up a single table; `pg_dump` backs up the entire cluster.
- D) Both tools create identical output formats; the difference is only in connection authentication method.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Both `pg_dump` and `pg_basebackup` operate on live, online databases without requiring shutdown; neither requires the database to be offline.
  - C) `pg_basebackup` backs up the entire PostgreSQL cluster (all databases); `pg_dump` can target a single database or specific objects; the scopes are reversed from what this option states.
  - D) The two tools produce fundamentally different outputs (SQL text vs. binary data files) and serve different purposes; they are not interchangeable.

---

### Question 16 (5 points)

A company has an RPO of 15 minutes for their Cloud SQL database. Which backup configuration best satisfies this requirement?

- A) Enable automated daily backups with PITR and `--retained-transaction-log-days=7`; WAL/binary logs are captured continuously and allow recovery to any 15-second window.
- B) Schedule manual `gcloud sql export` operations every 15 minutes to Cloud Storage.
- C) Configure a read replica and promote it every 15 minutes to capture a consistent snapshot.
- D) Set `--backup-retention-count=96` to retain 96 daily backups covering 15 minutes of history.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Manual exports every 15 minutes would technically satisfy an RPO of 15 minutes but is operationally fragile, expensive (each export creates a new Cloud Storage file), and unnecessary when PITR provides continuous log capture.
  - C) Promoting a replica is a destructive operation that creates a new primary; it cannot be done "every 15 minutes" as a backup strategy.
  - D) `--backup-retention-count` controls how many daily automated backups to keep; keeping 96 daily backups retains 96 days of backup history, not 15 minutes of granularity.

---

### Question 17 (5 points)

A Cloud SQL export operation to Cloud Storage fails with an "IAM permission denied" error. The DBA has confirmed that their personal user account has `storage.admin` on the bucket. What is the most likely root cause?

- A) The Cloud SQL service account (not the DBA's user account) performs the export operation and it lacks the required Cloud Storage permission.
- B) The Cloud Storage bucket is in a different region than the Cloud SQL instance.
- C) The DBA must have the `cloudsql.admin` role in addition to `storage.admin` to run exports.
- D) Cross-project exports are not supported; the Cloud Storage bucket must be in the same GCP project as the Cloud SQL instance.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud SQL can export to Cloud Storage buckets in different regions; cross-region export is supported and region mismatch is not the cause of an IAM permission denied error.
  - C) The `cloudsql.admin` role controls who can initiate the export API call; a separate storage permission is needed for the Cloud SQL service account that executes the write; having `cloudsql.admin` alone is not the issue here.
  - D) Cross-project Cloud Storage exports are supported in Cloud SQL; the bucket does not need to be in the same project as the Cloud SQL instance.

---

### Question 18 (5 points)

After restoring a PostgreSQL database from a `pg_dump` plain SQL backup, the DBA discovers that sequences on SERIAL columns are reset to 1, causing new INSERT operations to conflict with existing rows. What is the root cause?

- A) `pg_dump` by default captures the current sequence values at dump time, but if the restore was done with `--no-tablespaces` or if sequences were not included, sequences may start at their default initial value.
- B) Plain SQL `pg_dump` does not include sequence state; `pg_restore` with the custom format must be used to preserve sequence values.
- C) Sequence values are always reset to 1 after any `pg_dump` restore; the DBA must manually run `SELECT setval()` for every sequence after every restore.
- D) The conflict is caused by missing indexes on the primary key columns, not by sequence values.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Plain SQL `pg_dump` does include `SELECT pg_catalog.setval()` statements to restore sequence positions; the issue is typically that sequences were excluded from the dump or the dump was taken before some inserts occurred.
  - C) Sequence values are not always reset; `pg_dump` captures them; the problem occurs only in specific scenarios such as incomplete dumps, dumps taken before data was inserted, or restores that skip certain sections.
  - D) A primary key conflict means a new row's ID value already exists in the table, which is a sequence issue, not an index issue.

---

### Question 19 (5 points)

A DBA wants to verify that a Cloud SQL automated backup is restorable without disrupting the production instance. Which approach is correct?

- A) Use `gcloud sql instances restore-backup` to restore the backup to a new instance with a different name, then run application smoke tests and row count checks against the restored instance.
- B) Restore the backup to the same instance name, which creates a safe test environment without affecting production.
- C) Download the backup files from Cloud Storage and inspect them with a hex editor to confirm they are not empty.
- D) Run `gcloud sql backups verify BACKUP_ID` to trigger an automated integrity check in Cloud SQL.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud SQL always restores to a new instance; you cannot restore to the same instance name without deleting and recreating it; attempting to restore to the production instance name would disrupt production.
  - C) Cloud SQL automated backup files are stored in GCP-managed storage inaccessible to users; they cannot be downloaded or inspected directly; the only way to verify recoverability is an actual restore.
  - D) There is no `gcloud sql backups verify` command in the Cloud SQL CLI; backup integrity is verified only by performing an actual restore.

---

### Question 20 (5 points)

Which statement correctly describes the behavior of Cloud SQL automated backups for a PostgreSQL instance when PITR is enabled?

- A) Cloud SQL continuously archives WAL segments; the automated backup provides the base snapshot and the WAL archive fills in changes between backups, enabling recovery to any second within the retention window.
- B) Cloud SQL takes a full logical backup every hour using pg_dump when PITR is enabled.
- C) PITR replaces automated backups entirely; only WAL segments are retained, not full snapshots.
- D) Automated backups and PITR are mutually exclusive; enabling one disables the other on Cloud SQL.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud SQL automated backups are physical snapshots, not pg_dump logical backups; they are taken once daily by default, not hourly; PITR does not change the backup frequency.
  - C) PITR supplements automated backups, not replaces them; both the base snapshot (automated backup) and WAL archives are required together to restore to an arbitrary point in time.
  - D) Automated backups and PITR work together; PITR specifically requires automated backups to be enabled as a prerequisite on Cloud SQL.

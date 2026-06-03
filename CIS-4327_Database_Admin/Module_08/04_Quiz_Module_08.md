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

# Lab Activity: Module 08 — Database Backup and Recovery

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Lab Overview

In this lab you will practice the full backup and recovery workflow using both self-managed PostgreSQL tools and Cloud SQL managed backup features. You will use `pg_dump`/`pg_restore`, `mysqldump`, Cloud SQL automated backups, and perform a point-in-time recovery on a Cloud SQL PostgreSQL instance.

**Estimated Time:** 90 minutes

**Prerequisites:**

- Ubuntu 22.04 VM with PostgreSQL 15 and MySQL 8.0 installed (from Modules 06/07)
- Active Google Cloud project with Cloud SQL PostgreSQL instance from Module 06 lab (or a fresh one)
- `gcloud` CLI authenticated
- Cloud Storage bucket created (see Step 0)

---

## Part 0 — Setup: Create a Cloud Storage Bucket

```bash
export PROJECT_ID="your-project-id"
export BUCKET_NAME="db-backups-${PROJECT_ID}"
export REGION="us-central1"

gsutil mb -l $REGION gs://$BUCKET_NAME/
gsutil versioning set on gs://$BUCKET_NAME/
```

---

## Part 1 — pg_dump and pg_restore

### Step 1.1 — Prepare a PostgreSQL Database

Connect to your local PostgreSQL instance:

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE salesdb;
\c salesdb

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    region VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE sales (
    sale_id BIGSERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    amount NUMERIC(12,2),
    sale_date DATE DEFAULT CURRENT_DATE
);

-- Seed data
INSERT INTO customers (full_name, email, region)
SELECT 'Customer ' || i,
       'customer' || i || '@example.com',
       CASE WHEN i % 3 = 0 THEN 'West'
            WHEN i % 3 = 1 THEN 'East'
            ELSE 'Central' END
FROM generate_series(1,500) AS s(i);

INSERT INTO sales (customer_id, amount, sale_date)
SELECT (random() * 499 + 1)::int,
       round((random() * 1000)::numeric, 2),
       CURRENT_DATE - (random() * 365)::int
FROM generate_series(1,5000) AS s(i);

SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM sales;
\q
```

### Step 1.2 — Dump in Plain SQL Format

```bash
pg_dump -Fp -h localhost -U postgres -d salesdb \
  -f /tmp/salesdb_plain.sql

wc -l /tmp/salesdb_plain.sql
head -30 /tmp/salesdb_plain.sql
```

### Step 1.3 — Dump in Custom Format

```bash
pg_dump -Fc -Z 9 -h localhost -U postgres -d salesdb \
  -f /tmp/salesdb_backup.dump

ls -lh /tmp/salesdb_backup.dump
```

**Lab Question 1.1:** Compare the file sizes of `salesdb_plain.sql` and `salesdb_backup.dump`. What is the compression ratio? Why is the custom format smaller?

### Step 1.4 — List Archive Contents

```bash
pg_restore --list /tmp/salesdb_backup.dump | head -40
```

### Step 1.5 — Restore to a New Database

```bash
sudo -u postgres psql -c "CREATE DATABASE salesdb_restored;"

pg_restore -h localhost -U postgres \
  -d salesdb_restored \
  -j 2 \
  --clean --if-exists \
  /tmp/salesdb_backup.dump
```

### Step 1.6 — Verify Restore

```bash
sudo -u postgres psql -d salesdb_restored -c "
  SELECT 'customers' AS table_name, COUNT(*) FROM customers
  UNION ALL
  SELECT 'sales', COUNT(*) FROM sales;"
```

**Lab Question 1.2:** Do the row counts match between `salesdb` and `salesdb_restored`? What does this confirm about the consistency of pg_dump output?

### Step 1.7 — Restore a Single Table

```bash
# Drop only the sales table in the restored database
sudo -u postgres psql -d salesdb_restored -c "DROP TABLE IF EXISTS sales CASCADE;"

# Restore only the sales table from the backup
pg_restore -h localhost -U postgres \
  -d salesdb_restored \
  -t sales \
  /tmp/salesdb_backup.dump

sudo -u postgres psql -d salesdb_restored -c "SELECT COUNT(*) FROM sales;"
```

---

## Part 2 — mysqldump

### Step 2.1 — Prepare a MySQL Database

```bash
mysql -h 127.0.0.1 -u root -p
```

```sql
CREATE DATABASE inventorydb;
USE inventorydb;

CREATE TABLE items (
    item_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(200) NOT NULL,
    sku VARCHAR(50) UNIQUE,
    quantity INT DEFAULT 0,
    unit_price DECIMAL(10,2)
) ENGINE=InnoDB;

INSERT INTO items (item_name, sku, quantity, unit_price)
SELECT CONCAT('Item_', i), CONCAT('SKU-', LPAD(i, 6, '0')),
       FLOOR(RAND() * 1000), ROUND(RAND() * 100, 2)
FROM (SELECT a.N + b.N * 10 + 1 AS i
      FROM (SELECT 0 AS N UNION SELECT 1 UNION SELECT 2 UNION SELECT 3
            UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7
            UNION SELECT 8 UNION SELECT 9) a
      CROSS JOIN
           (SELECT 0 AS N UNION SELECT 1 UNION SELECT 2 UNION SELECT 3
            UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7
            UNION SELECT 8 UNION SELECT 9) b) nums;

SELECT COUNT(*) FROM items;
EXIT;
```

### Step 2.2 — Run mysqldump

```bash
mysqldump -h 127.0.0.1 -u root -p \
  --single-transaction \
  --routines \
  --triggers \
  --events \
  --hex-blob \
  inventorydb > /tmp/inventorydb_backup.sql

wc -l /tmp/inventorydb_backup.sql
```

### Step 2.3 — Inspect the Dump File

```bash
head -50 /tmp/inventorydb_backup.sql
grep "CREATE TABLE" /tmp/inventorydb_backup.sql
grep "INSERT INTO" /tmp/inventorydb_backup.sql | wc -l
```

**Lab Question 2.1:** What is the first SQL statement in the dump file after the comments? Why does mysqldump include `SET FOREIGN_KEY_CHECKS=0` in the dump?

### Step 2.4 — Restore to a New Database

```bash
mysql -h 127.0.0.1 -u root -p -e "CREATE DATABASE inventorydb_restored;"
mysql -h 127.0.0.1 -u root -p inventorydb_restored < /tmp/inventorydb_backup.sql

mysql -h 127.0.0.1 -u root -p -e "SELECT COUNT(*) FROM inventorydb_restored.items;"
```

---

## Part 3 — Cloud SQL Backup and Export

### Step 3.1 — Ensure Automated Backups Are Enabled

```bash
# Use your Cloud SQL PostgreSQL instance from Module 06
CLOUDSQL_INSTANCE="lab-postgres-instance"  # or your instance name

gcloud sql instances patch $CLOUDSQL_INSTANCE \
  --backup-start-time=03:00 \
  --retained-backups-count=7 \
  --retained-transaction-log-days=7 \
  --project=$PROJECT_ID
```

### Step 3.2 — Create an On-Demand Backup

```bash
gcloud sql backups create \
  --instance=$CLOUDSQL_INSTANCE \
  --description="Module 08 Lab - pre-export backup" \
  --project=$PROJECT_ID

# List all backups for the instance
gcloud sql backups list \
  --instance=$CLOUDSQL_INSTANCE \
  --project=$PROJECT_ID
```

Record the backup ID from the output.

### Step 3.3 — Grant Cloud SQL Service Account Access to the Bucket

```bash
# Get the Cloud SQL service account
SA_EMAIL=$(gcloud sql instances describe $CLOUDSQL_INSTANCE \
  --project=$PROJECT_ID \
  --format="value(serviceAccountEmailAddress)")

echo "Service account: $SA_EMAIL"

# Grant objectAdmin on the backup bucket
gsutil iam ch serviceAccount:${SA_EMAIL}:objectAdmin \
  gs://$BUCKET_NAME/
```

### Step 3.4 — Export the Database to Cloud Storage

```bash
gcloud sql export sql $CLOUDSQL_INSTANCE \
  gs://$BUCKET_NAME/exports/postgres_export_$(date +%Y%m%d).sql \
  --database=labdb \
  --project=$PROJECT_ID
```

Wait for the operation to complete, then verify:

```bash
gsutil ls gs://$BUCKET_NAME/exports/
```

**Lab Question 3.1:** What is the size of the exported SQL file in Cloud Storage? Compare this to the automated backup. Why might the sizes differ?

---

## Part 4 — Point-in-Time Recovery Test

### Step 4.1 — Note the Current Time

```bash
date -u +"%Y-%m-%dT%H:%M:%SZ"
```

Record this timestamp — call it T1.

### Step 4.2 — Insert Then Delete Data

```bash
gcloud sql connect $CLOUDSQL_INSTANCE --user=postgres --project=$PROJECT_ID
```

```sql
\c labdb

-- Insert marker data we will recover
INSERT INTO products (product_name, price, stock_qty)
VALUES ('PITR Test Row', 999.99, 1);

SELECT * FROM products WHERE product_name = 'PITR Test Row';
```

Record the timestamp again — call it T2.

```sql
-- Simulate accidental deletion
DELETE FROM products WHERE product_name LIKE 'PITR Test Row';
SELECT COUNT(*) FROM products WHERE product_name LIKE 'PITR Test Row';
\q
```

### Step 4.3 — Restore to a Point Before Deletion

```bash
# Get the most recent backup ID
BACKUP_ID=$(gcloud sql backups list \
  --instance=$CLOUDSQL_INSTANCE \
  --project=$PROJECT_ID \
  --limit=1 \
  --format="value(id)")

# Restore to T2 (after insert, before delete)
gcloud sql instances restore-backup $CLOUDSQL_INSTANCE \
  --restore-instance=pitr-restored-instance \
  --restore-time="$T2" \
  --project=$PROJECT_ID
```

Wait for the new instance to be `RUNNABLE`:

```bash
watch -n 10 "gcloud sql instances describe pitr-restored-instance \
  --project=$PROJECT_ID --format='value(state)'"
```

### Step 4.4 — Verify the Recovery

```bash
gcloud sql connect pitr-restored-instance --user=postgres --project=$PROJECT_ID
```

```sql
\c labdb
SELECT * FROM products WHERE product_name LIKE 'PITR Test Row';
\q
```

**Lab Question 4.1:** Was the deleted row recovered? What does this demonstrate about the value of PITR vs a simple full backup restore?

### Step 4.5 — Cleanup

```bash
gcloud sql instances delete pitr-restored-instance --project=$PROJECT_ID --quiet
```

---

## Lab Deliverables

Submit a PDF containing:

1. Screenshots of all command outputs and verification queries.
2. Written answers to all five Lab Questions.
3. A comparison table showing file sizes for: plain SQL dump, custom format dump, and Cloud Storage export.
4. A written reflection (5–8 sentences) answering: "If your organization's RPO is 1 hour and RTO is 30 minutes, is Cloud SQL's default 7-day automated backup with PITR sufficient? What would you change?"

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1: pg_dump/pg_restore with size comparison and verification | 25 |
| Part 2: mysqldump complete with restore verified | 20 |
| Part 3: Cloud SQL on-demand backup and export successful | 20 |
| Part 4: PITR restore demonstrated with recovered data | 25 |
| Written reflection on RPO/RTO analysis | 10 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Parallel pg_dump and Restore Benchmarking

Compare single-threaded vs. parallel dump and restore performance on a large dataset.

First, generate a large test table:

```sql
CREATE TABLE benchmark_data AS
SELECT
    generate_series        AS id,
    md5(random()::text)    AS payload,
    NOW() - (random() * INTERVAL '365 days') AS created_at
FROM generate_series(1, 500000);
```

Then complete the following steps:

1. Time a single-threaded custom format dump: `time pg_dump -Fc -d labdb -t benchmark_data -f /tmp/bench_single.dump` — record the elapsed time and file size with `ls -lh /tmp/bench_single.dump`.
2. Time a directory format dump with 4 parallel workers: `time pg_dump -Fd -d labdb -t benchmark_data -j 4 -f /tmp/bench_parallel/` — record elapsed time and total directory size with `du -sh /tmp/bench_parallel/`.
3. Restore both dumps to separate target databases (`bench_restore_single` and `bench_restore_parallel`) and time each restore. Record all four times in a comparison table and write a paragraph explaining under what production conditions parallel dump/restore provides the most benefit.

### Challenge 2: Backup Validation Automation Script

Write a shell script that automates backup verification on Cloud SQL.

The script should perform the following steps in order:

1. Trigger an on-demand Cloud SQL backup: `gcloud sql backups create --instance=$INSTANCE --project=$PROJECT`
2. Wait for the backup to reach SUCCESSFUL status by polling `gcloud sql backups list` every 30 seconds.
3. Restore the backup to a validation instance named `validation-$(date +%Y%m%d)`.
4. Wait for the validation instance to reach RUNNABLE state.
5. Connect to the validation instance and run a row count query to confirm data integrity: `SELECT COUNT(*) FROM labdb.products;`
6. Compare the count to the production instance count and print PASS or FAIL.
7. Delete the validation instance regardless of the result.

Write this as a complete bash script, test it in Cloud Shell, and include the script and its output in your lab report. Write a paragraph explaining how this script would be scheduled as a weekly Cloud Scheduler job triggering a Cloud Run job.

### Reflection Questions

1. In Challenge 1, why does parallel dump performance not scale linearly with worker count (e.g., 4 workers does not deliver exactly 4x speedup), and what I/O bottleneck typically limits further parallelism beyond 4–8 workers?
2. In Challenge 2, the validation script deletes the restored instance after the check. What is the trade-off between deleting immediately (saving cost) versus retaining the instance for 24 hours (enabling deeper investigation), and how would you encode this decision in the script based on the PASS/FAIL result?

# Lab Activity: Module 09 — High Availability and Replication

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Lab Overview

In this lab you will configure PostgreSQL streaming replication between a primary and a standby instance on Compute Engine, monitor replication lag, simulate failover, and observe Cloud SQL HA behavior including a controlled failover and read replica lag measurement.

**Estimated Time:** 100 minutes

**Prerequisites:**

- Two Compute Engine VMs: `pg-primary` and `pg-standby` (Ubuntu 22.04, PostgreSQL 15 installed)
- Active Cloud SQL for PostgreSQL instance with HA enabled (from Module 06 lab, or create a new one)
- `gcloud` CLI authenticated

---

## Part 1 — PostgreSQL Streaming Replication Setup

### Step 1.1 — Configure the Primary

SSH into `pg-primary`.

Edit `/etc/postgresql/15/main/postgresql.conf`:

```bash
sudo nano /etc/postgresql/15/main/postgresql.conf
```

Add or update:

```ini
wal_level = replica
max_wal_senders = 5
wal_keep_size = 512MB
hot_standby = on
```

Edit `/etc/postgresql/15/main/pg_hba.conf`:

```bash
sudo nano /etc/postgresql/15/main/pg_hba.conf
```

Add (replace `STANDBY_IP` with the internal IP of `pg-standby`):

```text
host  replication  replicator  STANDBY_IP/32  scram-sha-256
```

Reload PostgreSQL:

```bash
sudo systemctl reload postgresql
```

Create the replication user:

```bash
sudo -u postgres psql
```

```sql
CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'ReplPass2024!';
\q
```

Note the primary's internal IP address:

```bash
hostname -I
```

### Step 1.2 — Take a Base Backup on the Standby

SSH into `pg-standby`. Stop any running PostgreSQL service and clear the data directory:

```bash
sudo systemctl stop postgresql
sudo rm -rf /var/lib/postgresql/15/main/*
```

Take a base backup from the primary (replace `PRIMARY_IP`):

```bash
sudo -u postgres pg_basebackup \
  -h PRIMARY_IP \
  -U replicator \
  -D /var/lib/postgresql/15/main \
  --wal-method=stream \
  --checkpoint=fast \
  --progress \
  -v
```

### Step 1.3 — Configure the Standby

On `pg-standby`, edit `/var/lib/postgresql/15/main/postgresql.conf`:

```bash
sudo nano /var/lib/postgresql/15/main/postgresql.conf
```

Add:

```ini
primary_conninfo = 'host=PRIMARY_IP port=5432 user=replicator password=ReplPass2024! application_name=pgstandby1'
hot_standby = on
```

Create the standby signal file:

```bash
sudo touch /var/lib/postgresql/15/main/standby.signal
sudo chown postgres:postgres /var/lib/postgresql/15/main/standby.signal
```

Start PostgreSQL on the standby:

```bash
sudo systemctl start postgresql
sudo systemctl status postgresql
```

**Lab Question 1.1:** Check the PostgreSQL log on the standby for the startup message. What message confirms the standby has connected to the primary and is streaming WAL?

```bash
sudo tail -30 /var/log/postgresql/postgresql-15-main.log
```

---

## Part 2 — Monitor Replication

### Step 2.1 — Check Replication Status on the Primary

SSH into `pg-primary`:

```bash
sudo -u postgres psql
```

```sql
SELECT client_addr, application_name, state,
       sent_lsn, write_lsn, flush_lsn, replay_lsn,
       (sent_lsn - replay_lsn) AS lag_bytes
FROM pg_stat_replication;
```

### Step 2.2 — Check Lag on the Standby

SSH into `pg-standby`:

```bash
sudo -u postgres psql
```

```sql
SELECT now() - pg_last_xact_replay_timestamp() AS replication_delay;
SELECT pg_is_in_recovery() AS is_standby;
```

**Lab Question 2.1:** What value does `pg_is_in_recovery()` return on the standby? What does this confirm about the server's role?

### Step 2.3 — Generate Load and Observe Lag

On `pg-primary`, generate writes:

```bash
sudo -u postgres psql -c "
CREATE TABLE IF NOT EXISTS load_test (id SERIAL, val TEXT, ts TIMESTAMPTZ DEFAULT now());
INSERT INTO load_test (val)
SELECT md5(random()::text) FROM generate_series(1,100000);"
```

Immediately check lag on the standby:

```sql
SELECT now() - pg_last_xact_replay_timestamp() AS replication_delay;
```

Check again after 10 seconds:

```sql
SELECT now() - pg_last_xact_replay_timestamp() AS replication_delay;
```

**Lab Question 2.2:** Did the lag spike during the bulk insert and then return to near-zero? What does this pattern tell you about async replication's behavior under write bursts?

---

## Part 3 — Simulate Failover

### Step 3.1 — Verify Data on Standby Before Failover

On `pg-standby` (read-only):

```sql
SELECT COUNT(*) FROM load_test;
SELECT MAX(ts) FROM load_test;
```

Confirm the row count matches the primary.

### Step 3.2 — Stop the Primary

On `pg-primary`:

```bash
sudo systemctl stop postgresql
```

The standby should detect the primary is gone within seconds.

### Step 3.3 — Promote the Standby

On `pg-standby`:

```bash
sudo -u postgres pg_ctl promote -D /var/lib/postgresql/15/main
```

Wait a few seconds, then verify promotion:

```bash
sudo -u postgres psql -c "SELECT pg_is_in_recovery();"
```

The result should be `false` — the former standby is now the primary.

### Step 3.4 — Confirm Write Access

```bash
sudo -u postgres psql -c "
INSERT INTO load_test (val) VALUES ('post-failover-write');
SELECT val FROM load_test WHERE val = 'post-failover-write';"
```

**Lab Question 3.1:** What was the approximate time between stopping the primary and successfully completing a write to the promoted standby? Record start and end times.

---

## Part 4 — Cloud SQL HA Observation

### Step 4.1 — Check HA Instance Zones

```bash
export PROJECT_ID="your-project-id"
export HA_INSTANCE="lab-postgres-ha"   # Your Cloud SQL HA instance name

gcloud sql instances describe $HA_INSTANCE \
  --project=$PROJECT_ID \
  --format="yaml(gceZone,secondaryGceZone,settings.availabilityType)"
```

Record the primary zone and secondary zone.

### Step 4.2 — Create a Read Replica

```bash
gcloud sql instances create lab-postgres-replica \
  --master-instance-name=$HA_INSTANCE \
  --region=us-east1 \
  --tier=db-f1-micro \
  --project=$PROJECT_ID
```

Wait until the replica is `RUNNABLE`.

### Step 4.3 — Insert Data and Measure Replica Lag

Insert data on the primary:

```bash
gcloud sql connect $HA_INSTANCE --user=postgres --project=$PROJECT_ID
```

```sql
\c labdb
INSERT INTO products (product_name, price, stock_qty)
SELECT 'Replication Test ' || i, random() * 100, random() * 500
FROM generate_series(1,1000) AS s(i);
\q
```

Check the replica immediately:

```bash
gcloud sql connect lab-postgres-replica --user=postgres --project=$PROJECT_ID
```

```sql
\c labdb
SELECT COUNT(*) FROM products;
```

Wait 5 seconds and check again:

```sql
SELECT COUNT(*) FROM products;
```

**Lab Question 4.1:** Was there observable replication lag on the Cloud SQL read replica? What is the practical implication for applications that read from a replica immediately after writing to the primary?

### Step 4.4 — Cloud SQL Manual Failover

```bash
gcloud sql instances failover $HA_INSTANCE \
  --project=$PROJECT_ID
```

Monitor until complete:

```bash
watch -n 5 "gcloud sql instances describe $HA_INSTANCE \
  --project=$PROJECT_ID --format='value(state,gceZone)'"
```

**Lab Question 4.2:** After failover, which zone is the new primary in? How does this compare to the secondary zone you recorded in Step 4.1?

---

## Part 5 — Cleanup

```bash
# Delete read replica
gcloud sql instances delete lab-postgres-replica \
  --project=$PROJECT_ID --quiet
```

---

## Lab Deliverables

Submit a PDF containing:

1. Screenshots of all command outputs and query results.
2. Written answers to all five Lab Questions.
3. A diagram (hand-drawn or digital) showing your self-managed streaming replication topology from Parts 1–3, including primary IP, standby IP, and the WAL stream direction.
4. A written comparison (6–8 sentences) contrasting the self-managed failover you performed in Part 3 with the Cloud SQL HA failover in Part 4. Address: speed, steps required, operator intervention, and which is safer in production.

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1: Streaming replication configured and connected | 25 |
| Part 2: Lag monitoring with before/after data | 20 |
| Part 3: Failover completed, write verified on promoted standby | 25 |
| Part 4: Cloud SQL HA failover observed with zone data | 20 |
| Written comparison of self-managed vs Cloud SQL HA | 10 |
| **Total** | **100** |

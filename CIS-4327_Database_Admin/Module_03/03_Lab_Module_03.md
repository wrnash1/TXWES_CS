# Lab Activity: Module 03 — Cloud SQL: MySQL and PostgreSQL on GCP

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Total Points: 100

---

### Lab Overview

In this lab you will create a production-grade Cloud SQL for PostgreSQL instance with high availability enabled, create a read replica, configure automated backups with point-in-time recovery, test the Cloud SQL Auth Proxy connection method, and manage database users and access. These are the core operational tasks tested in the Cloud SQL domain of the GCP Database Engineer exam.

Estimated completion time: 75–90 minutes.

---

### Prerequisites

- Google Cloud student project with billing enabled or Cloud Skills Boost credits active
- Module 03 video scripts and reading guide reviewed
- Cloud Shell available in the Google Cloud Console

---

### Part 1 — Create a High-Availability Cloud SQL Instance (25 points)

#### Step 1 — Create the Instance with HA Enabled

Use the gcloud CLI in Cloud Shell to create the instance. This approach is tested on the exam and is faster than using the Console UI for repeated deployments.

```bash
gcloud sql instances create txwes-pg-m03 \
    --database-version=POSTGRES_15 \
    --tier=db-n1-standard-2 \
    --region=us-central1 \
    --storage-type=SSD \
    --storage-size=20GB \
    --storage-auto-increase \
    --availability-type=REGIONAL \
    --maintenance-window-day=SUN \
    --maintenance-window-hour=3 \
    --root-password=TxWes2024!Secure
```

This command creates a high-availability instance. The `--availability-type=REGIONAL` flag provisions both a primary in zone A and a standby in zone B of us-central1.

Wait approximately 5 minutes for provisioning to complete.

#### Step 2 — Verify the Instance Configuration

```bash
# View instance details
gcloud sql instances describe txwes-pg-m03 \
    --format="table(name,state,databaseVersion,settings.availabilityType,settings.tier)"
```

**Deliverable 1 (10 points)**: Take a screenshot of the gcloud describe output showing the instance name, state (RUNNABLE), database version, availabilityType (REGIONAL), and tier. Save as `lab03_screenshot_01.png`.

#### Step 3 — Create a Database and Connect

```bash
# Create the application database
gcloud sql databases create txwes_m03db \
    --instance=txwes-pg-m03

# Connect via the Auth Proxy (gcloud sql connect uses it transparently)
gcloud sql connect txwes-pg-m03 --user=postgres --quiet
```

Enter the root password when prompted.

```sql
-- Verify the database was created
\l

-- Connect to the application database
\c txwes_m03db

-- Create a sample table
CREATE TABLE app_events (
    event_id   SERIAL       PRIMARY KEY,
    event_type VARCHAR(50)  NOT NULL,
    user_id    INTEGER      NOT NULL,
    occurred_at TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO app_events (event_type, user_id) VALUES
    ('login',   101),
    ('purchase', 101),
    ('logout',  101),
    ('login',   202),
    ('support', 202);

SELECT COUNT(*) FROM app_events;
```

**Deliverable 2 (15 points)**: Take a screenshot showing the `\l` output listing databases and the COUNT(*) result from app_events. Save as `lab03_screenshot_02.png`.

---

### Part 2 — Create a Read Replica (20 points)

#### Step 4 — Create an In-Region Read Replica

```bash
gcloud sql instances create txwes-pg-m03-replica \
    --master-instance-name=txwes-pg-m03 \
    --region=us-central1 \
    --tier=db-n1-standard-1
```

Wait 3–5 minutes for the replica to be created and synchronized.

#### Step 5 — Verify Replication

```bash
# Connect to the replica
gcloud sql connect txwes-pg-m03-replica --user=postgres --quiet
```

```sql
-- Switch to the application database on the replica
\c txwes_m03db

-- Read from the replica — should show the same rows inserted into the primary
SELECT * FROM app_events ORDER BY event_id;

-- Attempt a write on the replica — this should fail
INSERT INTO app_events (event_type, user_id) VALUES ('test', 999);
```

**Deliverable 3 (10 points)**: Take a screenshot showing the SELECT result on the replica (confirming replication) and the error message when attempting the INSERT. Save as `lab03_screenshot_03.png`.

**Deliverable 4 (10 points)**: In your lab report, write two to three sentences explaining why the INSERT fails on the replica and under what circumstances you would promote a read replica to primary.

---

### Part 3 — Backup Configuration and PITR (20 points)

#### Step 6 — Configure Automated Backup with PITR

```bash
# Enable automated backup with transaction log retention for PITR
gcloud sql instances patch txwes-pg-m03 \
    --backup-start-time=03:00 \
    --enable-bin-log \
    --retained-backups-count=7 \
    --retained-transaction-log-days=3
```

#### Step 7 — Trigger an On-Demand Backup

```bash
# Create an immediate on-demand backup
gcloud sql backups create --instance=txwes-pg-m03

# List available backups
gcloud sql backups list --instance=txwes-pg-m03
```

**Deliverable 5 (10 points)**: Take a screenshot of the `gcloud sql backups list` output showing at least one backup with a SUCCESSFUL status. Save as `lab03_screenshot_04.png`.

**Deliverable 6 (10 points)**: In your lab report, answer these two questions. First: what database-level setting must be active for point-in-time recovery to work in PostgreSQL, and what is its equivalent in MySQL? Second: if a developer accidentally deletes all rows from a table at 2:47 PM today and your backup retention includes transaction logs, what GCP Console action would you take to recover the data?

---

### Part 4 — User Management and Access Control (20 points)

#### Step 8 — Create Database Users

Connect to the primary instance.

```bash
gcloud sql connect txwes-pg-m03 --user=postgres --quiet
```

```sql
\c txwes_m03db
```

```bash
# Create a read-only application user via gcloud
gcloud sql users create readonly_user \
    --instance=txwes-pg-m03 \
    --password=ReadOnly2024!
```

```sql
-- Grant read-only access
GRANT CONNECT ON DATABASE txwes_m03db TO readonly_user;
GRANT USAGE ON SCHEMA public TO readonly_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_user;

-- Verify the grants
\dp app_events
```

#### Step 9 — Create an IAM Database User

```bash
# Create an IAM database user (uses a service account email)
# Note: replace PROJECT_ID with your actual project ID
gcloud sql users create \
    "lab-test@PROJECT_ID.iam.gserviceaccount.com" \
    --instance=txwes-pg-m03 \
    --type=CLOUD_IAM_SERVICE_ACCOUNT
```

**Deliverable 7 (10 points)**: Take a screenshot of the `\dp app_events` output showing the privileges granted to readonly_user. Save as `lab03_screenshot_05.png`.

**Deliverable 8 (10 points)**: In your lab report, explain the difference between a built-in database user (readonly_user) and an IAM database user in terms of how authentication works, where credentials are stored, and which is preferred for application service accounts running on GCP and why.

---

### Part 5 — Database Flags (15 points)

#### Step 10 — Set Performance and Logging Flags

```bash
# Enable slow query logging at 500ms threshold
gcloud sql instances patch txwes-pg-m03 \
    --database-flags=log_min_duration_statement=500,log_connections=on

# Verify the flags were applied
gcloud sql instances describe txwes-pg-m03 \
    --format="value(settings.databaseFlags)"
```

**Deliverable 9 (15 points)**: Take a screenshot of the flag list output showing both flags. Save as `lab03_screenshot_06.png`. In your lab report, explain what `log_min_duration_statement=500` does and how you would use the logs it generates to improve query performance.

---

### Part 6 — Clean Up (Required)

Delete all instances after saving all deliverables.

```bash
gcloud sql instances delete txwes-pg-m03-replica --quiet
gcloud sql instances delete txwes-pg-m03 --quiet
```

Note: deleting the primary instance also deletes its automated backups. If you want to keep backups for review, export them to Cloud Storage first.

---

### Lab Submission Checklist

- Deliverable 1 (10 pts) — Instance configuration screenshot showing REGIONAL availability type
- Deliverable 2 (15 pts) — Database list and row count screenshots
- Deliverable 3 (10 pts) — Replica SELECT result and INSERT error screenshot
- Deliverable 4 (10 pts) — Written explanation of read-only replicas and promotion
- Deliverable 5 (10 pts) — Backup list screenshot showing SUCCESSFUL status
- Deliverable 6 (10 pts) — Written answers to PITR questions
- Deliverable 7 (10 pts) — Privilege display screenshot for readonly_user
- Deliverable 8 (10 pts) — Written comparison of built-in vs. IAM database users
- Deliverable 9 (15 pts) — Database flags screenshot and written explanation

---

### Grading Rubric — 100 Points Total

| Deliverable | Points | Criteria |
|---|---|---|
| 1 — Instance config screenshot | 10 | REGIONAL availability type visible; instance in RUNNABLE state |
| 2 — Database and data screenshots | 15 | Database list shown; correct row count |
| 3 — Replica verification | 10 | SELECT shows replicated rows; INSERT error shown |
| 4 — Replica written explanation | 10 | Accurate explanation of read-only behavior and promotion scenario |
| 5 — Backup list screenshot | 10 | SUCCESSFUL backup visible in list |
| 6 — PITR written answers | 10 | Correct settings identified; correct recovery procedure described |
| 7 — Privilege display screenshot | 10 | readonly_user SELECT grant visible |
| 8 — User type comparison | 10 | Accurate distinction; correct recommendation for GCP service accounts |
| 9 — Flags screenshot and explanation | 15 | Both flags visible; accurate explanation of slow query log use |
| Deductions | up to -10 | Instances not deleted after completion |

---

Reference: cloud.google.com/learn

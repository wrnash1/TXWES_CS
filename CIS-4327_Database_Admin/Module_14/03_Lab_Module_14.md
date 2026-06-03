# Lab Activity: Module 14 — Database Migration Strategies

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Lab Overview

**Title**: Migrating a MySQL Database to Cloud SQL Using Database Migration Service

**Estimated Time**: 90–120 minutes

**Difficulty**: Intermediate–Advanced

In this lab you will simulate a production database migration by provisioning a
source MySQL database on a Compute Engine VM, populating it with sample data,
configuring DMS with a continuous migration job, validating the migration, and
executing a simulated cutover.

---

## Prerequisites

- Active GCP project with billing enabled
- Cloud SQL Admin API, Compute Engine API, and Database Migration API enabled
- Owner or the following roles: Cloud SQL Admin, Compute Instance Admin,
  Database Migration Admin, Service Account User
- Cloud Shell or gcloud SDK authenticated

---

## Lab Objectives

By the end of this lab, you will be able to:

1. Prepare a MySQL source database for DMS migration (binlog configuration, migration user)
2. Create DMS connection profiles for source and destination
3. Create and monitor a continuous DMS migration job
4. Validate row counts between source and target
5. Simulate the cutover process
6. Identify the limitations of DMS for schema objects (stored procedures, triggers)

---

## Part 1 — Provision the Source MySQL Instance

### Step 1.1 — Create a Compute Engine VM with MySQL

```bash
export PROJECT_ID=$(gcloud config get-value project)
export ZONE=us-central1-a
export REGION=us-central1

gcloud compute instances create lab14-mysql-source \
  --zone=$ZONE \
  --machine-type=e2-medium \
  --image-family=debian-12 \
  --image-project=debian-cloud \
  --tags=mysql-source \
  --metadata=startup-script='#!/bin/bash
    apt-get update -y
    apt-get install -y mysql-server
    systemctl enable mysql
    systemctl start mysql'
```

Wait 2–3 minutes for the VM to start and MySQL to install.

### Step 1.2 — Configure MySQL for DMS Replication

SSH into the VM:

```bash
gcloud compute ssh lab14-mysql-source --zone=$ZONE
```

Inside the VM, configure MySQL for DMS:

```bash
sudo bash -c 'cat >> /etc/mysql/mysql.conf.d/mysqld.cnf << EOF

[mysqld]
server-id         = 1
log_bin           = /var/log/mysql/mysql-bin.log
binlog_format     = ROW
binlog_row_image  = FULL
expire_logs_days  = 7
EOF'

sudo systemctl restart mysql
```

Verify binlog is active:

```bash
sudo mysql -e "SHOW VARIABLES LIKE 'log_bin';"
sudo mysql -e "SHOW VARIABLES LIKE 'binlog_format';"
```

### Step 1.3 — Create the Source Database and Data

```bash
sudo mysql << 'SQLEOF'
CREATE DATABASE lab14_source;
USE lab14_source;

CREATE TABLE customers (
  customer_id   INT AUTO_INCREMENT PRIMARY KEY,
  name          VARCHAR(100) NOT NULL,
  email         VARCHAR(150) UNIQUE,
  region        VARCHAR(50),
  created_at    DATETIME DEFAULT NOW()
);

CREATE TABLE orders (
  order_id      INT AUTO_INCREMENT PRIMARY KEY,
  customer_id   INT,
  order_date    DATE,
  revenue       DECIMAL(10,2),
  status        VARCHAR(30) DEFAULT 'pending',
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert 10,000 sample rows
INSERT INTO customers (name, email, region)
SELECT
  CONCAT('Customer_', seq),
  CONCAT('user', seq, '@example.com'),
  ELT(1 + FLOOR(RAND() * 4), 'Northeast', 'Southeast', 'Midwest', 'West')
FROM (
  SELECT a.N + b.N * 10 + c.N * 100 + d.N * 1000 + 1 AS seq
  FROM
    (SELECT 0 AS N UNION SELECT 1 UNION SELECT 2 UNION SELECT 3
     UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7
     UNION SELECT 8 UNION SELECT 9) a,
    (SELECT 0 AS N UNION SELECT 1 UNION SELECT 2 UNION SELECT 3
     UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7
     UNION SELECT 8 UNION SELECT 9) b,
    (SELECT 0 AS N UNION SELECT 1 UNION SELECT 2 UNION SELECT 3
     UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7
     UNION SELECT 8 UNION SELECT 9) c,
    (SELECT 0 AS N UNION SELECT 1 UNION SELECT 2 UNION SELECT 3
     UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7
     UNION SELECT 8 UNION SELECT 9) d
  LIMIT 10000
) seq_table;

INSERT INTO orders (customer_id, order_date, revenue, status)
SELECT
  FLOOR(1 + RAND() * 10000),
  DATE_ADD('2024-01-01', INTERVAL FLOOR(RAND() * 365) DAY),
  ROUND(RAND() * 5000, 2),
  ELT(1 + FLOOR(RAND() * 3), 'pending', 'completed', 'cancelled')
FROM (
  SELECT a.N + b.N * 10 + c.N * 100 + 1 AS seq
  FROM
    (SELECT 0 AS N UNION SELECT 1 UNION SELECT 2 UNION SELECT 3
     UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7
     UNION SELECT 8 UNION SELECT 9) a,
    (SELECT 0 AS N UNION SELECT 1 UNION SELECT 2 UNION SELECT 3
     UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7
     UNION SELECT 8 UNION SELECT 9) b,
    (SELECT 0 AS N UNION SELECT 1 UNION SELECT 2 UNION SELECT 3
     UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7
     UNION SELECT 8 UNION SELECT 9) c
  LIMIT 5000
) seq_table;

SQLEOF
```

### Step 1.4 — Create the DMS Migration User

```bash
sudo mysql << 'SQLEOF'
CREATE USER 'dms_user'@'%' IDENTIFIED BY 'DmsStr0ng!Pass';
GRANT SELECT, RELOAD, LOCK TABLES, REPLICATION SLAVE, REPLICATION CLIENT
  ON *.* TO 'dms_user'@'%';
FLUSH PRIVILEGES;
SQLEOF
```

Record the VM's internal IP address:

```bash
hostname -I | awk '{print $1}'
```

Exit the SSH session: `exit`

---

## Part 2 — Configure Firewall and DMS Connection

### Step 2.1 — Allow MySQL Port from DMS

```bash
gcloud compute firewall-rules create allow-mysql-dms \
  --direction=INGRESS \
  --priority=1000 \
  --network=default \
  --action=ALLOW \
  --rules=tcp:3306 \
  --source-ranges=0.0.0.0/0 \
  --target-tags=mysql-source
```

### Step 2.2 — Get the VM External IP

```bash
gcloud compute instances describe lab14-mysql-source \
  --zone=$ZONE \
  --format="value(networkInterfaces[0].accessConfigs[0].natIP)"
```

Record this IP — it is the source hostname for the DMS connection profile.

---

## Part 3 — Create DMS Connection Profiles and Migration Job

### Step 3.1 — Navigate to Database Migration Service

In the GCP Console, navigate to Database Migration → Connection Profiles.
Click **Create Profile**.

**Source connection profile**:

- Profile name: `lab14-mysql-source`
- Database engine: MySQL
- Hostname or IP: (external IP from Step 2.2)
- Port: 3306
- Username: `dms_user`
- Password: `DmsStr0ng!Pass`

**Destination connection profile**:

- Profile name: `lab14-cloudsql-dest`
- Database engine: Cloud SQL for MySQL
- (Select the Cloud SQL instance to create or pre-create one with name `lab14-mysql-dest`)

### Step 3.2 — Create the Migration Job

Navigate to Database Migration → Migration Jobs → Create Migration Job.

- Migration job name: `lab14-migration`
- Source: `lab14-mysql-source`
- Destination: `lab14-cloudsql-dest`
- Migration type: **Continuous**
- Select database: `lab14_source`

Run the **Test** step to validate connectivity and permissions.

**Lab Question 1**: If the test fails, what are the two most likely causes? How
would you diagnose each?

Start the migration job and proceed to Part 4 while the initial load runs.

---

## Part 4 — Monitor and Validate

### Step 4.1 — Monitor the Migration Job

In the DMS console, observe:

- Migration status (should move from STARTING to RUNNING to CDC IN PROGRESS)
- Replication lag (should drop toward zero after initial load)
- Tables migrated count

**Lab Question 2**: How long did the initial full load take? How many tables
were migrated? What is the replication lag now that CDC is active?

### Step 4.2 — Insert New Rows on Source During CDC

SSH back into the source VM and insert new rows to verify CDC is working:

```bash
gcloud compute ssh lab14-mysql-source --zone=$ZONE

sudo mysql lab14_source << 'EOF'
INSERT INTO customers (name, email, region)
VALUES ('CDC_Test_Customer', 'cdctest@example.com', 'West');

SELECT customer_id, name FROM customers WHERE email = 'cdctest@example.com';
EOF
exit
```

### Step 4.3 — Verify the New Row Appeared on Target

Connect to the Cloud SQL target using Cloud SQL Auth Proxy or the console query
editor and verify the CDC row was replicated:

```sql
SELECT customer_id, name, email
FROM lab14_source.customers
WHERE email = 'cdctest@example.com';
```

**Lab Question 3**: How quickly did the CDC row appear on the target? What does
this tell you about replication lag for this workload?

### Step 4.4 — Row Count Validation

Run on both source and target, and compare results:

```sql
SELECT 'customers' AS tbl, COUNT(*) AS cnt FROM lab14_source.customers
UNION ALL
SELECT 'orders',          COUNT(*)          FROM lab14_source.orders;
```

**Lab Question 4**: Do the row counts match? If they differ by a small number,
what might explain the discrepancy?

---

## Part 5 — Simulated Cutover

### Step 5.1 — Verify Lag is Near Zero

In the DMS console, confirm that replication lag is less than 5 seconds.

### Step 5.2 — Stop Writes on Source

SSH into the source VM and lock the tables to simulate stopping the application:

```bash
sudo mysql -e "FLUSH TABLES WITH READ LOCK;"
```

### Step 5.3 — Wait for Lag to Reach Zero

Monitor the DMS console. Wait until lag shows 0 seconds.

### Step 5.4 — Promote the Target

In DMS, click **Promote** on the migration job. This breaks replication and
promotes the Cloud SQL instance to a standalone writable database.

### Step 5.5 — Unlock Source

```bash
sudo mysql -e "UNLOCK TABLES;"
```

**Lab Question 5**: After promoting the Cloud SQL target, can you restart DMS
replication if a problem is discovered? What is your rollback option at this point?

---

## Cleanup

```bash
gcloud compute instances delete lab14-mysql-source --zone=$ZONE --quiet
gcloud compute firewall-rules delete allow-mysql-dms --quiet
gcloud sql instances delete lab14-mysql-dest --quiet
```

---

## Grading Rubric

| Component | Points |
|---|---|
| Source MySQL configured with binlog settings verified | 20 |
| DMS migration job created and test passed | 15 |
| Initial load completed and CDC active | 15 |
| CDC row verified on target after source insert | 15 |
| Row count validation performed with results documented | 15 |
| Simulated cutover executed (promote step) | 10 |
| Lab Questions 1–5 answered | 10 |
| **Total** | **100** |

---

Module 14 Lab — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.

# Lab Activity: Module 07 — MySQL and Cloud SQL

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Lab Overview

In this lab you will create and configure a Cloud SQL for MySQL 8.0 instance with high availability, add a read replica, configure database flags, create users and roles, and connect securely using the Cloud SQL Auth Proxy.

**Estimated Time:** 90 minutes

**Prerequisites:**

- Active Google Cloud project with billing enabled
- `gcloud` CLI installed and authenticated (`gcloud auth login`)
- MySQL client installed locally (`sudo apt-get install -y mysql-client`)
- Project owner or Cloud SQL Admin IAM role

---

## Part 1 — Create a Cloud SQL MySQL Instance with HA

### Step 1.1 — Set Environment Variables

```bash
export PROJECT_ID="your-project-id"
export INSTANCE_NAME="lab-mysql-ha"
export REGION="us-central1"
export ZONE="us-central1-a"

gcloud config set project $PROJECT_ID
```

### Step 1.2 — Create the Instance

```bash
gcloud sql instances create $INSTANCE_NAME \
  --database-version=MYSQL_8_0 \
  --tier=db-n1-standard-2 \
  --region=$REGION \
  --availability-type=REGIONAL \
  --storage-type=SSD \
  --storage-size=20GB \
  --storage-auto-increase \
  --backup-start-time=03:00 \
  --enable-bin-log \
  --deletion-protection \
  --project=$PROJECT_ID
```

This command takes 3–5 minutes. Monitor progress:

```bash
gcloud sql instances describe $INSTANCE_NAME \
  --project=$PROJECT_ID \
  --format="value(state)"
```

Wait until the state shows `RUNNABLE`.

### Step 1.3 — Set the Root Password

```bash
gcloud sql users set-password root \
  --host=% \
  --instance=$INSTANCE_NAME \
  --password="RootPass2024!" \
  --project=$PROJECT_ID
```

**Lab Question 1.1:** In the Cloud Console, navigate to your instance details. In what zone is the primary instance deployed? In what zone is the standby? Record both zone names.

---

## Part 2 — Configure Database Flags

### Step 2.1 — Apply Performance Flags

```bash
gcloud sql instances patch $INSTANCE_NAME \
  --database-flags \
    slow_query_log=on,\
    long_query_time=1,\
    log_queries_not_using_indexes=on,\
    max_connections=100,\
    character_set_server=utf8mb4,\
    collation_server=utf8mb4_unicode_ci \
  --project=$PROJECT_ID
```

### Step 2.2 — Verify Flags

```bash
gcloud sql instances describe $INSTANCE_NAME \
  --project=$PROJECT_ID \
  --format="yaml(settings.databaseFlags)"
```

**Lab Question 2.1:** Which of the flags you set requires an instance restart to take effect? Check the Cloud Console — does it show a restart required indicator?

---

## Part 3 — Create a Database, Users, and Roles

### Step 3.1 — Connect via Cloud SQL CLI

```bash
gcloud sql connect $INSTANCE_NAME --user=root --project=$PROJECT_ID
```

This opens a Cloud Shell connection directly to the instance.

### Step 3.2 — Create Database and Schema

```sql
CREATE DATABASE labshop
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE labshop;

CREATE TABLE products (
    product_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(200) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL,
    stock INT UNSIGNED DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE orders (
    order_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_id INT UNSIGNED NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    order_total DECIMAL(12,2),
    order_ts DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;
```

### Step 3.3 — Create Roles

```sql
CREATE ROLE 'shop_read';
CREATE ROLE 'shop_write';

GRANT SELECT ON labshop.* TO 'shop_read';
GRANT SELECT, INSERT, UPDATE, DELETE ON labshop.* TO 'shop_write';
```

### Step 3.4 — Create Users

```sql
CREATE USER 'appuser'@'%'
  IDENTIFIED WITH mysql_native_password BY 'AppPass2024!';

CREATE USER 'reporter'@'%'
  IDENTIFIED WITH mysql_native_password BY 'ReportPass2024!';

GRANT 'shop_write' TO 'appuser'@'%';
GRANT 'shop_read' TO 'reporter'@'%';

SET DEFAULT ROLE ALL TO 'appuser'@'%';
SET DEFAULT ROLE ALL TO 'reporter'@'%';

FLUSH PRIVILEGES;
```

### Step 3.5 — Test Privileges

```sql
-- Verify appuser grants
SHOW GRANTS FOR 'appuser'@'%';

-- Verify reporter grants
SHOW GRANTS FOR 'reporter'@'%';
```

**Lab Question 3.1:** Insert a test row as appuser. Then connect as reporter and try to INSERT. Record the exact error message and MySQL error code.

```sql
-- Insert test data as root
INSERT INTO products (product_name, category, price, stock)
VALUES ('Widget Pro', 'Electronics', 49.99, 250);

SELECT * FROM products;
```

---

## Part 4 — Add a Read Replica

### Step 4.1 — Create the Replica

```bash
gcloud sql instances create lab-mysql-replica \
  --master-instance-name=$INSTANCE_NAME \
  --region=us-east1 \
  --tier=db-n1-standard-1 \
  --project=$PROJECT_ID
```

This takes 3–5 minutes.

### Step 4.2 — Monitor Replica Lag

```bash
gcloud sql instances describe lab-mysql-replica \
  --project=$PROJECT_ID \
  --format="value(replicaStatus.replicationLag)"
```

### Step 4.3 — Connect to the Replica

```bash
gcloud sql connect lab-mysql-replica --user=root --project=$PROJECT_ID
```

```sql
-- Confirm it is read-only
SHOW VARIABLES LIKE 'read_only';

-- Verify data was replicated
USE labshop;
SELECT * FROM products;

-- Attempt a write (should fail)
INSERT INTO products (product_name, category, price, stock)
VALUES ('Should Fail', 'Test', 1.00, 1);
```

**Lab Question 4.1:** What error do you receive when attempting to write to the replica? What MySQL variable confirms the replica is read-only?

---

## Part 5 — Cloud SQL Auth Proxy

### Step 5.1 — Install the Auth Proxy

```bash
# In Cloud Shell or your VM
wget https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.10.1/cloud-sql-proxy.linux.amd64 \
  -O cloud-sql-proxy
chmod +x cloud-sql-proxy
sudo mv cloud-sql-proxy /usr/local/bin/
```

### Step 5.2 — Get the Connection Name

```bash
gcloud sql instances describe $INSTANCE_NAME \
  --project=$PROJECT_ID \
  --format="value(connectionName)"
```

Copy the output — it looks like `project-id:us-central1:lab-mysql-ha`.

### Step 5.3 — Start the Auth Proxy

```bash
cloud-sql-proxy \
  --port=3306 \
  "$PROJECT_ID:$REGION:$INSTANCE_NAME" &

# Verify it started
sleep 2
netstat -tlnp | grep 3306
```

### Step 5.4 — Connect Through the Proxy

```bash
mysql -h 127.0.0.1 -P 3306 -u appuser -p labshop
```

When connected, verify the data:

```sql
SELECT * FROM products;
SHOW VARIABLES LIKE 'hostname';
```

**Lab Question 5.1:** What hostname is returned by `SHOW VARIABLES LIKE 'hostname'`? Does it show the Cloud SQL instance name or a local address? What does this tell you about the proxy's behavior?

### Step 5.5 — Stop the Proxy

```bash
pkill cloud-sql-proxy
```

---

## Part 6 — Test Failover (Optional — requires HA instance)

### Step 6.1 — Initiate Manual Failover

```bash
gcloud sql instances failover $INSTANCE_NAME \
  --project=$PROJECT_ID
```

### Step 6.2 — Monitor Failover

```bash
watch -n 5 "gcloud sql instances describe $INSTANCE_NAME \
  --project=$PROJECT_ID \
  --format='value(state,gceZone)'"
```

Observe the `gceZone` change from the original primary zone to the standby zone after failover completes.

**Lab Question 6.1:** How long did the failover take? What zone is the new primary in? Is this the former standby zone?

---

## Cleanup

```bash
# Delete replica first
gcloud sql instances delete lab-mysql-replica \
  --project=$PROJECT_ID --quiet

# Remove deletion protection, then delete primary
gcloud sql instances patch $INSTANCE_NAME \
  --no-deletion-protection \
  --project=$PROJECT_ID

gcloud sql instances delete $INSTANCE_NAME \
  --project=$PROJECT_ID --quiet
```

---

## Lab Deliverables

Submit a PDF containing:

1. Screenshots of each step's command output and Cloud Console views.
2. Written answers to all six Lab Questions.
3. The output of `SHOW GRANTS FOR 'appuser'@'%'` and `SHOW GRANTS FOR 'reporter'@'%'`.
4. A paragraph (4–6 sentences) explaining why using the Cloud SQL Auth Proxy is preferable to opening an Authorized Network rule pointing to your Cloud Shell IP.

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1: HA instance created, primary/standby zones identified | 15 |
| Part 2: Database flags applied and verified | 10 |
| Part 3: Database, roles, and users correctly configured | 25 |
| Part 4: Replica created, read-only confirmed, lag checked | 20 |
| Part 5: Auth Proxy installed and connection verified | 20 |
| Part 6 (optional): Failover completed with timing recorded | 10 bonus |
| **Total** | **100** |

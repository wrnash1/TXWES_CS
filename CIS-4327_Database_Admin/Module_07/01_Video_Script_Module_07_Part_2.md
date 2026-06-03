# Video Script: Module 07 — MySQL and Cloud SQL (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back. This is Part 2 of Module 07: MySQL and Cloud SQL.

In Part 1 we covered MySQL architecture, InnoDB, user management, and configuration. In Part 2 we shift to Google Cloud SQL — creating and configuring MySQL instances, enabling high availability, adding read replicas, and securing connections with the Cloud SQL Auth Proxy.

---

## Section 1 — Cloud SQL for MySQL Overview

Cloud SQL is Google Cloud's fully managed relational database service. For MySQL, Cloud SQL supports versions 5.7 and 8.0. Google manages patching, replication, storage scaling, and backup. You are responsible for schema design, query optimization, and application-level configuration.

**Cloud SQL MySQL instance tiers** range from shared-core for development to high-memory instances with up to 624 GB RAM for large workloads. Storage is SSD or HDD and scales automatically.

### Creating a Cloud SQL MySQL Instance

```bash
gcloud sql instances create my-mysql-instance \
  --database-version=MYSQL_8_0 \
  --tier=db-n1-standard-4 \
  --region=us-central1 \
  --storage-type=SSD \
  --storage-size=100GB \
  --storage-auto-increase \
  --backup-start-time=02:00 \
  --enable-bin-log \
  --maintenance-window-day=SUN \
  --maintenance-window-hour=3 \
  --deletion-protection \
  --project=my-gcp-project
```

Key flags to note:

- `--enable-bin-log` — enables the binary log, which is required for point-in-time recovery and replication. It is enabled automatically when you enable high availability.
- `--deletion-protection` — prevents accidental instance deletion. Always use this for production.
- `--storage-auto-increase` — Cloud SQL automatically increases storage when usage approaches the limit. Once increased, storage cannot be decreased.

### Setting Database Flags

```bash
gcloud sql instances patch my-mysql-instance \
  --database-flags \
    innodb_buffer_pool_size=4294967296,\
    slow_query_log=on,\
    long_query_time=1,\
    max_connections=200 \
  --project=my-gcp-project
```

Note that `innodb_buffer_pool_size` is set in bytes on Cloud SQL — 4294967296 bytes = 4 GB.

---

## Section 2 — Cloud SQL High Availability

Cloud SQL HA uses a **primary instance** and a **standby instance** in the same region but in a different zone. The standby is a hot standby — it is continuously synchronized with the primary using synchronous replication.

### How Cloud SQL HA Works

1. Write transactions are sent to the primary.
2. The primary writes to its data and log volumes, which are backed by persistent disk.
3. A **regional persistent disk** is used — both the primary and standby share the same disk, meaning failover is near-instantaneous because the standby does not need to replay WAL or binlog.
4. A health check agent monitors the primary. If the primary becomes unresponsive, the standby is automatically promoted.
5. The client connection string does not change — Cloud SQL updates DNS to point to the new primary automatically.

Failover typically takes 60–120 seconds.

### Enabling HA on a New Instance

```bash
gcloud sql instances create my-mysql-ha \
  --database-version=MYSQL_8_0 \
  --tier=db-n1-standard-4 \
  --region=us-central1 \
  --availability-type=REGIONAL \
  --enable-bin-log \
  --project=my-gcp-project
```

`--availability-type=REGIONAL` enables HA with a standby in a different zone. The default `ZONAL` provides no standby.

### Triggering a Manual Failover

```bash
gcloud sql instances failover my-mysql-ha \
  --project=my-gcp-project
```

Use this to test your failover procedure before production traffic depends on it.

---

## Section 3 — Read Replicas

A read replica is a separate Cloud SQL instance that receives continuous replication from the primary. Applications can direct read-heavy queries to the replica, offloading the primary.

Cloud SQL MySQL read replicas use **asynchronous replication** via the MySQL binary log. This means the replica may lag slightly behind the primary — usually milliseconds to seconds under normal load.

### Creating a Read Replica

```bash
gcloud sql instances create my-mysql-replica \
  --master-instance-name=my-mysql-ha \
  --region=us-east1 \
  --tier=db-n1-standard-2 \
  --project=my-gcp-project
```

Note: the replica can be in a **different region** than the primary — this is called a cross-region replica. It provides a geographically distributed read endpoint and can be used for disaster recovery by promoting the replica if the primary region fails.

### Promoting a Replica to Primary

```bash
gcloud sql instances promote-replica my-mysql-replica \
  --project=my-gcp-project
```

After promotion, the replica becomes a standalone instance. It is no longer connected to the original primary.

### Replica Lag Monitoring

```bash
gcloud sql instances describe my-mysql-replica \
  --format="value(replicaConfiguration.replicaLagSeconds)" \
  --project=my-gcp-project
```

Or use Cloud Monitoring with the metric `cloudsql.googleapis.com/database/replication/replica_lag`.

---

## Section 4 — Cloud SQL Auth Proxy

One of the most important security features for Cloud SQL is the **Cloud SQL Auth Proxy**. It handles authentication and authorization for database connections using IAM, without requiring you to open firewall rules or manage SSL certificates manually.

### How the Auth Proxy Works

The Auth Proxy runs as a local sidecar process on your application server or in a Kubernetes pod sidecar container. Your application connects to `127.0.0.1:3306` (or any local port) as if it were a local MySQL server. The Auth Proxy intercepts the connection, authenticates it using the application's Google Cloud service account, establishes an encrypted tunnel to the Cloud SQL instance, and forwards the connection.

```
Application → 127.0.0.1:3306 → [Auth Proxy] → encrypted tunnel → Cloud SQL
```

### Installing and Running the Auth Proxy

```bash
# Download the proxy binary
wget https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.10.1/cloud-sql-proxy.linux.amd64
chmod +x cloud-sql-proxy.linux.amd64
sudo mv cloud-sql-proxy.linux.amd64 /usr/local/bin/cloud-sql-proxy

# Run the proxy (replace with your connection name)
cloud-sql-proxy \
  --port=3306 \
  my-gcp-project:us-central1:my-mysql-ha &
```

The connection name format is `PROJECT:REGION:INSTANCE_NAME`.

### Connecting Through the Proxy

```bash
mysql -h 127.0.0.1 -P 3306 -u appuser -p mydb
```

### Required IAM Roles

The service account running the Auth Proxy needs one of:

- `roles/cloudsql.client` — allows connections to the instance
- `roles/cloudsql.instanceUser` — allows IAM database authentication

### Cloud SQL Auth Proxy in Kubernetes

In GKE, the proxy runs as a sidecar container in the same pod as the application:

```yaml
containers:
  - name: app
    image: my-app:latest
    env:
      - name: DB_HOST
        value: "127.0.0.1"
  - name: cloud-sql-proxy
    image: gcr.io/cloud-sql-connectors/cloud-sql-proxy:2.10.1
    args:
      - "--port=3306"
      - "my-gcp-project:us-central1:my-mysql-ha"
    securityContext:
      runAsNonRoot: true
```

---

## Section 5 — Connecting to Cloud SQL Without the Auth Proxy

If you must connect without the Auth Proxy, Cloud SQL supports two approaches:

**Authorized Networks** — You add specific IP addresses or CIDR ranges to the instance's authorized networks list. This opens a direct TCP connection to the Cloud SQL instance's public IP.

```bash
gcloud sql instances patch my-mysql-ha \
  --authorized-networks=203.0.113.45/32 \
  --project=my-gcp-project
```

Always enable SSL when using authorized networks:

```bash
gcloud sql instances patch my-mysql-ha \
  --require-ssl \
  --project=my-gcp-project
```

**Private IP** — Cloud SQL instances can be assigned a private IP address within your VPC via Private Service Access (VPC peering with the Google-managed service network). Applications in the same VPC connect directly without the proxy and without exposing the instance to the public internet. This is the preferred architecture for production applications in GCP.

---

## Section 6 — Exam Tips for Cloud SQL MySQL

The Google Cloud Database Engineer exam tests these Cloud SQL MySQL scenarios heavily:

**Tip 1 — HA vs Read Replica:** High availability uses a standby in the same region for automatic failover. A read replica is a separate instance for offloading reads. A read replica does not provide automatic failover without manual promotion.

**Tip 2 — Binary log:** The binary log must be enabled for both PITR and replication. `--enable-bin-log` is the gcloud flag.

**Tip 3 — Auth Proxy vs Private IP:** For GKE applications, the Auth Proxy sidecar pattern is the recommended connection method. For applications on Compute Engine within the same VPC, private IP is simpler.

**Tip 4 — Cross-region replica:** A cross-region read replica can serve as a disaster recovery target. It requires manual promotion and is not automatic failover.

**Tip 5 — Storage auto-increase:** Storage can only grow, never shrink. Size initial storage appropriately and rely on auto-increase for growth rather than over-provisioning.

**Common exam trap:** The question may describe an application that needs zero-RPO failover. Cloud SQL HA does not guarantee zero-RPO — there is a brief failover period of 60–120 seconds. For zero-RPO requirements, Cloud Spanner (Module 11) is the correct answer.

---

## Closing

That wraps up Module 07: MySQL and Cloud SQL. You now understand the full stack — from InnoDB internals and MySQL user management to Cloud SQL HA configuration, read replicas, and the Auth Proxy.

The Module 07 lab walks you through creating a Cloud SQL MySQL instance, configuring HA, adding a read replica, and connecting through the Auth Proxy. Complete the lab and reading guide before the quiz.

See you in Module 08: Database Backup and Recovery.

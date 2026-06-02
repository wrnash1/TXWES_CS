# Video Script: Module 03 — Cloud SQL: MySQL and PostgreSQL on GCP (Part 1)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 13–15 minutes

---

### Opening

**[SHOW SLIDE: Module 03 — Cloud SQL: MySQL and PostgreSQL on GCP]**

Hello, and welcome back to CIS-4327. I am Professor Nash. This is Module 03: Cloud SQL — MySQL and PostgreSQL on GCP.

Cloud SQL is Google Cloud's fully managed relational database service. It supports MySQL, PostgreSQL, and SQL Server. You do not manage the underlying virtual machines, operating system patches, or storage infrastructure — Google handles all of that. Your job as a Cloud Database Engineer is to configure, secure, tune, and operate Cloud SQL instances correctly.

In Part 1 we cover instance creation and configuration, supported database engines, storage options, connections, and users. In Part 2 we cover read replicas, automated backups, high availability, and performance considerations.

---

### Section 1 — Cloud SQL Overview and Supported Engines

**[SHOW CONSOLE: Google Cloud Console — Databases menu, SQL option]**

Cloud SQL supports three database engines.

MySQL is available in versions 5.7 and 8.0. MySQL is the most widely deployed open-source relational database and is the default choice for lift-and-shift migrations from on-premises MySQL workloads.

PostgreSQL is available in versions 12 through 16. PostgreSQL has a stronger feature set than MySQL for complex queries, custom data types, full-text search, and JSON support. Cloud SQL for PostgreSQL is binary-compatible with standard PostgreSQL — any application that runs against a self-managed PostgreSQL instance should run against Cloud SQL with minimal changes.

SQL Server is available in Express, Web, Standard, and Enterprise editions. It is the right choice when migrating from on-premises Microsoft SQL Server workloads that require Windows Authentication or SQL Server-specific features.

For the GCP exam, MySQL and PostgreSQL are the most frequently tested Cloud SQL engines. SQL Server is tested primarily in migration scenario questions.

---

### Section 2 — Instance Configuration

**[SHOW CONSOLE: Cloud SQL Create Instance form — instance ID, region, zone, machine type, storage]**

When creating a Cloud SQL instance, you configure five main dimensions.

Database version: select the engine and version appropriate for your application. Higher versions include security patches and new features, but you must verify application compatibility before upgrading.

Region and zone: Cloud SQL instances run in a single GCP region. For production workloads, choose the region closest to your application to minimize latency. Zonal availability options are single zone or multiple zones (high availability). We cover HA in Part 2.

Machine type: Cloud SQL offers shared-core, standard, and high-memory machine types. Shared-core (db-f1-micro, db-g1-small) are for development and testing only — they have burstable CPU and are not suitable for production. Standard machine types have dedicated CPU and predictable performance.

Storage: Cloud SQL uses SSD storage by default, which is strongly recommended for production. HDD storage is cheaper but has significantly lower I/O performance. Storage capacity auto-increase can be enabled so the instance grows automatically as data volume increases without manual intervention.

Maintenance window: you can specify a day of week and hour for Cloud SQL to apply minor version upgrades and maintenance operations. Align this window with your application's lowest-traffic period.

**[SHOW CODE]**

```bash
# Create a PostgreSQL 15 instance via gcloud CLI
gcloud sql instances create txwes-pg-prod \
    --database-version=POSTGRES_15 \
    --tier=db-n1-standard-2 \
    --region=us-central1 \
    --storage-type=SSD \
    --storage-size=100GB \
    --storage-auto-increase \
    --availability-type=REGIONAL \
    --maintenance-window-day=SUN \
    --maintenance-window-hour=3
```

**[END CODE]**

The `--availability-type=REGIONAL` flag creates a high-availability instance with automatic failover to a standby in a different zone. `--availability-type=ZONAL` is a single-zone instance appropriate for development.

---

### Section 3 — Connecting to Cloud SQL

**[SHOW SLIDE: Three connection methods — Cloud SQL Auth Proxy, Private IP, Cloud Shell]**

Connecting to Cloud SQL requires understanding the three available methods.

The Cloud SQL Auth Proxy is the recommended connection method for applications. It handles TLS encryption and IAM authentication automatically, without requiring you to manage SSL certificates or maintain an allowlist of IP addresses. The proxy runs as a sidecar process alongside your application and establishes an encrypted tunnel to Cloud SQL.

Private IP connectivity means your Cloud SQL instance is accessible only within a VPC network and has no public IP address exposed to the internet. This is the security best practice for production instances. It requires setting up Private Services Access between your VPC and the Cloud SQL managed network.

Public IP with authorized networks allows connections from specific IP ranges that you explicitly allowlist. This is simpler to configure than Private IP but exposes the instance to the public internet, which requires careful firewall management.

**[SHOW CODE]**

```bash
# Download and run the Cloud SQL Auth Proxy (Linux/Cloud Shell)
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 \
    -O cloud_sql_proxy
chmod +x cloud_sql_proxy

# Start the proxy for a PostgreSQL instance
./cloud_sql_proxy -instances=PROJECT:REGION:INSTANCE=tcp:5432 &

# Connect via psql through the proxy
psql -h 127.0.0.1 -p 5432 -U postgres -d mydb
```

**[END CODE]**

In Cloud Shell, you can connect directly using `gcloud sql connect` which starts the Auth Proxy transparently.

**[SHOW CODE]**

```bash
gcloud sql connect txwes-pg-prod --user=postgres --quiet
```

**[END CODE]**

---

### Section 4 — Users and Database-Level Access

**[SHOW SLIDE: Cloud SQL user management — IAM database users vs. built-in users]**

Cloud SQL supports two types of database users.

Built-in database users are standard MySQL or PostgreSQL users managed within the database itself. The default admin user is `postgres` in PostgreSQL and `root` in MySQL. You set a password for these users and connect with standard username/password authentication.

IAM database users authenticate using Google Identity (service accounts or user accounts) rather than a database password. When a user connects, Cloud SQL validates their IAM identity before granting access. This is the recommended approach for applications running on GCP services like Cloud Run, GKE, or Compute Engine, because no database passwords need to be stored or rotated.

**[SHOW CODE]**

```bash
# Create a built-in database user
gcloud sql users create app_user \
    --instance=txwes-pg-prod \
    --password=SecurePassword123

# Create an IAM database user (uses service account email as username)
gcloud sql users create my-service-account@my-project.iam.gserviceaccount.com \
    --instance=txwes-pg-prod \
    --type=CLOUD_IAM_SERVICE_ACCOUNT
```

**[END CODE]**

**[SHOW CODE]**

```sql
-- In PostgreSQL: grant database access to a user
GRANT CONNECT ON DATABASE mydb TO app_user;

-- Grant schema usage
GRANT USAGE ON SCHEMA public TO app_user;

-- Grant read-only access to all tables
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_user;

-- Grant read-write access
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
```

**[END CODE]**

---

### Section 5 — Cloud SQL Editions and Pricing Model

**[SHOW SLIDE: Cloud SQL Enterprise vs. Enterprise Plus comparison table]**

Cloud SQL offers two editions for MySQL and PostgreSQL.

Cloud SQL Enterprise is the standard edition. It provides SLA of 99.95% for high-availability instances, automated backups, read replicas in the same region, and standard I/O performance.

Cloud SQL Enterprise Plus is the premium edition introduced in 2023. It provides higher I/O throughput, faster maintenance operations with near-zero downtime, data cache for in-memory performance improvement, and a 99.99% SLA with minimal maintenance impact. It also enables cross-region read replicas for disaster recovery.

For the exam, know that Enterprise Plus provides higher performance and a stronger SLA than Enterprise, at a higher cost. Development and testing workloads should use Enterprise or shared-core instances to minimize cost.

---

### Section 6 — Storage Configuration

**[SHOW SLIDE: Storage type comparison — SSD vs. HDD, auto-increase]**

Cloud SQL storage decisions directly affect performance and cost.

SSD storage provides higher IOPS and lower latency. It is required for production workloads. SSD instances support up to 64 TB of storage per instance.

HDD storage has lower cost per GB but significantly lower throughput. It is appropriate only for archival or infrequently accessed data.

Storage auto-increase automatically expands the storage allocation when the instance approaches capacity. This prevents database outages caused by running out of disk space. Auto-increase never automatically decreases storage — once expanded, storage capacity cannot be reduced without creating a new instance.

The maximum storage increase per increment is configurable. The default behavior adds storage in increments when usage exceeds 80% of the current allocation.

---

### Closing — Part 1 Summary

**[SHOW SLIDE: Module 03 Part 1 key concepts]**

In Part 1 we covered Cloud SQL's supported engines — MySQL, PostgreSQL, and SQL Server — and the key configuration dimensions: database version, region, machine type, storage type, and maintenance window.

We covered the three connection methods — Cloud SQL Auth Proxy (recommended for applications), Private IP (security best practice), and Public IP with authorized networks.

We covered user types — built-in password users and IAM database users — and the SQL commands to grant access at the database level.

In Part 2 we cover read replicas, automated backups, high availability failover, connection pooling with PgBouncer, and the exam tips that appear in the Cloud SQL domain.

See you in Part 2.

---

Reference: cloud.google.com/learn

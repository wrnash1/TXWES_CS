# Reading Guide: Module 03 — Cloud SQL: MySQL and PostgreSQL on GCP

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Introduction

Module 03 covers Cloud SQL — Google Cloud's fully managed relational database service for MySQL, PostgreSQL, and SQL Server. Cloud SQL is one of the highest-weighted services on the GCP Database Engineer exam. You will encounter Cloud SQL questions in service selection scenarios, security design, backup and recovery, performance tuning, and migration domains. This reading guide provides the detailed reference you need for both the lab and the exam.

---

### 1. High-Yield Glossary

**Cloud SQL**: Google Cloud's fully managed relational database service. Supports MySQL 5.7 and 8.0, PostgreSQL 12–16, and SQL Server editions. Google manages patching, backups, storage, and replication infrastructure.

**Fully Managed**: Google handles operating system patching, database engine minor version upgrades, storage management, backup scheduling, and replication infrastructure. The customer manages schema design, query tuning, user access, and application configuration.

**Instance**: A single Cloud SQL database server. Each instance runs one database engine version in one GCP region.

**Cloud SQL Auth Proxy**: A local proxy process that authenticates database connections using Google Cloud IAM and encrypts all traffic with TLS. The recommended connection method for applications on GCP and on-premises.

**Private IP**: A Cloud SQL instance configured with an internal VPC IP address and no public internet endpoint. The security best practice for production instances.

**Public IP**: A Cloud SQL instance accessible from the internet, restricted by an authorized networks allowlist.

**Authorized Networks**: IP address ranges explicitly permitted to connect to a Public IP Cloud SQL instance. All other sources are blocked.

**IAM Database User**: A Cloud SQL user authenticated by Google Cloud IAM identity rather than a database password. Preferred for service accounts on GCP services.

**Built-In Database User**: A standard database user authenticated with a username and password stored in the database engine.

**Read Replica**: A copy of a primary Cloud SQL instance that serves read-only queries. Replication is asynchronous. Cannot accept write operations.

**In-Region Read Replica**: A read replica in the same region as the primary.

**Cross-Region Read Replica**: A read replica in a different region. Used for geographic read distribution and disaster recovery.

**Cascading Read Replica**: A replica of a read replica (not of the primary). Reduces replication load on the primary.

**Replica Promotion**: Promoting a read replica to a standalone primary instance. Used in disaster recovery scenarios.

**Automated Backup**: A scheduled full snapshot of the Cloud SQL instance stored in GCP-managed storage. Default retention is 7 days, configurable to 365.

**Point-in-Time Recovery (PITR)**: Recovery to any second within the transaction log retention window. Requires binary logging (MySQL) or WAL archiving (PostgreSQL) to be enabled.

**High Availability (HA)**: A configuration with a primary instance in one zone and a standby in another zone within the same region. Automatic failover on primary failure. Sets `--availability-type=REGIONAL`.

**Zonal Instance**: A single-zone Cloud SQL instance with no standby. Appropriate for development and test; not recommended for production.

**Failover**: The process of promoting the standby instance to primary when the primary fails. Takes approximately 60 seconds.

**Storage Auto-Increase**: Cloud SQL feature that automatically expands storage when usage approaches capacity. One-directional — storage can grow but not shrink.

**SSD Storage**: Default Cloud SQL storage type. Higher IOPS and lower latency than HDD. Required for production workloads.

**HDD Storage**: Lower-cost Cloud SQL storage. Significantly lower throughput than SSD. Appropriate for archival or infrequently accessed data only.

**Cloud SQL Enterprise**: Standard Cloud SQL edition. 99.95% SLA for HA instances, regional read replicas, standard I/O performance.

**Cloud SQL Enterprise Plus**: Premium Cloud SQL edition. 99.99% SLA, higher I/O, near-zero downtime maintenance, cross-region read replicas, data cache.

**Connection Pooling**: Maintaining a pool of persistent database connections shared across application threads. Reduces connection overhead for high-concurrency applications.

**PgBouncer**: A lightweight connection pooler for PostgreSQL. Supports session, transaction, and statement pool modes.

**Database Flags**: Cloud SQL mechanism for setting database engine configuration parameters (postgresql.conf or MySQL my.cnf parameters).

**Maintenance Window**: A configurable time window when Cloud SQL applies minor version upgrades and maintenance operations.

**Cloud SQL Studio**: A browser-based SQL editor in the Google Cloud Console for running queries against Cloud SQL instances.

---

### 2. Connection Methods Comparison

| Method | Authentication | Encryption | Use Case |
|---|---|---|---|
| Cloud SQL Auth Proxy | IAM | TLS (automatic) | Applications on GCP or on-premises; recommended default |
| Private IP | Database credentials or IAM | TLS optional but recommended | Production workloads; no public internet exposure |
| Public IP + Authorized Networks | Database credentials or IAM | TLS optional | Development; requires IP allowlist management |
| Cloud Shell gcloud sql connect | IAM | TLS (via proxy) | Ad-hoc administration and testing |

---

### 3. Instance Tiers and Sizing

| Tier Category | Examples | Use Case |
|---|---|---|
| Shared-core | db-f1-micro, db-g1-small | Development and testing only; burstable CPU |
| Standard | db-n1-standard-2, db-n1-standard-4 | General production workloads |
| High-memory | db-n1-highmem-4, db-n1-highmem-8 | Memory-intensive queries; large working sets |
| Enterprise Plus | db-perf-optimized-N-4 and larger | Highest performance; 99.99% SLA |

For the exam: shared-core instances are explicitly not suitable for production. Any scenario mentioning production workloads with SLA requirements eliminates shared-core as an answer.

---

### 4. Backup and Recovery Options

| Feature | Description | Key Requirement |
|---|---|---|
| Automated backup | Full snapshot, daily schedule, configurable retention | Enabled by default |
| On-demand backup | Manual full snapshot triggered at any time | None |
| PITR | Restore to any second within log retention window | Binary logging (MySQL) or WAL archiving (PostgreSQL) must be enabled |
| Export to Cloud Storage | SQL dump or CSV export to a GCS bucket | Useful for cross-project or cross-region restores |
| Clone instance | Creates a copy of the instance at a specific point in time | Fast; used for testing migrations or restores |

---

### 5. High Availability vs. Read Replicas

| Feature | High Availability Standby | Read Replica |
|---|---|---|
| Purpose | Automatic failover for availability | Offload read queries for performance |
| Accepts writes | No — standby is passive | No — replica is read-only |
| Accepts reads | No — standby is not queryable | Yes — primary purpose |
| Replication | Synchronous (shared disk) | Asynchronous |
| Failover | Automatic, ~60 seconds | Manual promotion required |
| Cost | Doubles compute cost | Additional instance cost |
| Region | Same region, different zone | Same or different region |

---

### 6. Cloud SQL for MySQL vs. PostgreSQL — Feature Comparison

| Feature | MySQL 8.0 | PostgreSQL 15 |
|---|---|---|
| JSON support | JSON column type, limited functions | Full JSONB with indexing and operators |
| Custom data types | Limited | Extensive (ENUM, ARRAY, composite, domain) |
| Full-text search | FULLTEXT index | tsvector/tsquery, GIN/GiST indexes |
| Window functions | Supported | Supported, more extensive |
| Default isolation level | REPEATABLE READ | READ COMMITTED |
| UPSERT syntax | INSERT ... ON DUPLICATE KEY UPDATE | INSERT ... ON CONFLICT DO UPDATE |
| Extensions | Limited | Over 100 extensions (pgvector, PostGIS, etc.) |
| Cloud SQL Auth | Supported | Supported |
| PITR | Binary logging | WAL archiving |

---

### 7. gcloud CLI Reference for Cloud SQL

| Task | Command |
|---|---|
| Create instance | `gcloud sql instances create NAME --database-version=VERSION --tier=TIER --region=REGION` |
| Connect via proxy | `gcloud sql connect INSTANCE --user=USER --quiet` |
| Create database | `gcloud sql databases create DBNAME --instance=INSTANCE` |
| Create user | `gcloud sql users create USER --instance=INSTANCE --password=PASS` |
| Enable HA | `gcloud sql instances patch INSTANCE --availability-type=REGIONAL` |
| Create read replica | `gcloud sql instances create REPLICA --master-instance-name=PRIMARY --region=REGION` |
| Set database flag | `gcloud sql instances patch INSTANCE --database-flags=FLAG=VALUE` |
| Create backup | `gcloud sql backups create --instance=INSTANCE` |
| Restore backup | `gcloud sql instances restore-backup INSTANCE --backup-id=ID` |
| Delete instance | `gcloud sql instances delete INSTANCE --quiet` |

---

### 8. Required Readings and Resources

**GCP Documentation — Cloud SQL Overview**: Covers the supported database engines, editions, instance configuration, and connection options. Available at cloud.google.com/learn.

**GCP Documentation — Cloud SQL Auth Proxy**: Detailed configuration guide for the Auth Proxy including installation and usage for different deployment environments. Available at cloud.google.com/learn.

**GCP Documentation — Cloud SQL High Availability**: Architecture description, failover behavior, and configuration steps for HA instances. Available at cloud.google.com/learn.

**GCP Documentation — Cloud SQL Backups and PITR**: Complete guide to automated backups, on-demand backups, and point-in-time recovery procedures. Available at cloud.google.com/learn.

---

### 9. Exam Tips

Tip 1: The Cloud SQL Auth Proxy is the correct answer whenever a question mentions secure application connectivity without managing certificates or IP allowlists. It is the recommended default connection method.

Tip 2: Private IP is the correct answer for any question involving network isolation or eliminating public internet exposure. It requires Private Services Access to be configured on the VPC.

Tip 3: Read replicas are for performance scaling of read traffic. HA standby is for availability and automatic failover. Do not confuse the two — they serve different purposes and are tested separately on the exam.

Tip 4: PITR requires binary logging or WAL archiving to be enabled before the data loss event. If the question says PITR was not configured, the best recovery option is the most recent automated backup checkpoint.

Tip 5: Cloud SQL HA failover takes approximately 60 seconds. This is an important exam fact. If a scenario requires faster failover, Cloud Spanner is the answer.

Tip 6: Storage auto-increase is one-directional. Any scenario asking about reducing storage consumption on an existing instance requires creating a new instance and migrating data.

Tip 7: Enterprise Plus provides 99.99% SLA vs. 99.95% for Enterprise. This difference matters in exam questions about contractual uptime requirements.

Tip 8: IAM database users are the preferred authentication method for service accounts running on GCP (Cloud Run, GKE, Compute Engine). They eliminate password management and integrate with Cloud Audit Logs for database access tracing.

---

### 10. Study Checklist

- State the three database engines supported by Cloud SQL and a use case for each
- Explain the difference between Cloud SQL Auth Proxy, Private IP, and Public IP connection methods
- Describe the difference between an HA standby instance and a read replica
- Explain what PITR requires to function and what its limitations are
- State the approximate Cloud SQL HA failover time
- Write gcloud CLI commands to create a PostgreSQL instance with HA and add a read replica
- Explain why storage auto-increase is one-directional
- State the SLA difference between Cloud SQL Enterprise and Enterprise Plus
- Explain when IAM database users are preferred over built-in users
- Complete the Module 03 lab activity
- Pass the Module 03 quiz with at least 80 percent

---

Reference: cloud.google.com/learn

---

## 9. Supplemental Resources

**1. Cloud SQL for PostgreSQL — Official Documentation**
https://cloud.google.com/sql/docs/postgres
The complete reference for Cloud SQL PostgreSQL instance creation, high availability configuration, read replicas, backups, PITR, database flags, and IAM authentication.

**2. Cloud SQL Auth Proxy — GitHub Repository and Setup Guide**
https://github.com/GoogleCloudPlatform/cloud-sql-proxy
Source code, release binaries, and detailed setup instructions for the Cloud SQL Auth Proxy, including Kubernetes sidecar deployment patterns and Workload Identity configuration.

**3. PostgreSQL — pg_audit Extension Documentation**
https://github.com/pgaudit/pgaudit
Documentation and configuration reference for the pgaudit extension used with Cloud SQL for PostgreSQL, covering log classes, object auditing, and session auditing modes.

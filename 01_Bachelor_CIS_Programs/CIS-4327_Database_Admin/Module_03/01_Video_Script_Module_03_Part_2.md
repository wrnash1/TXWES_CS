# Video Script: Module 03 — Cloud SQL: MySQL and PostgreSQL on GCP (Part 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 11–13 minutes

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / Oracle &bull; Database Administration & SQL Masterclass &bull; Module 03</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=HXV3zeQKqGY" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/HXV3zeQKqGY" title="freeCodeCamp / Oracle &bull; Database Administration & SQL Masterclass" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp / Oracle &bull; Database Administration & SQL Masterclass</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->


---

### Opening

**[SHOW SLIDE: Module 03 Part 2 — Read Replicas, Backups, High Availability, and Exam Tips]**

Welcome back. I am Professor Nash, and this is Part 2 of Module 03.

In Part 1 we configured a Cloud SQL instance, explored connection methods, and set up users. Now we cover the operational features that keep production databases available and recoverable: read replicas, automated backups, high availability failover, and connection pooling. These topics appear frequently on the GCP Database Engineer exam.

---

### Section 1 — Read Replicas

**[SHOW SLIDE: Primary instance with two read replicas — read traffic distributed, write traffic to primary]**

A read replica is a copy of the primary Cloud SQL instance that serves read-only queries. Read replicas replicate data asynchronously from the primary. Applications can direct read-heavy workloads — reporting queries, analytics, dashboards — to replicas, reducing load on the primary instance.

Cloud SQL supports three types of read replicas.

In-region read replicas are in the same GCP region as the primary. They are the simplest to configure and have the lowest replication lag.

Cross-region read replicas are in a different GCP region than the primary. They improve read performance for geographically distributed users and can serve as a disaster recovery target.

Cascading read replicas are replicas of another replica rather than of the primary. This reduces replication load on the primary when many replicas are needed.

**[SHOW CODE]**

```bash
# Create an in-region read replica
gcloud sql instances create txwes-pg-replica-1 \
    --master-instance-name=txwes-pg-prod \
    --region=us-central1 \
    --tier=db-n1-standard-2

# Create a cross-region read replica
gcloud sql instances create txwes-pg-replica-dr \
    --master-instance-name=txwes-pg-prod \
    --region=us-east1 \
    --tier=db-n1-standard-2
```

**[END CODE]**

A read replica can be promoted to a standalone primary. This is used in disaster recovery when the primary is unavailable. After promotion, the former replica becomes an independent instance and application connection strings must be updated.

---

### Section 2 — Automated Backups and Point-in-Time Recovery

**[SHOW CONSOLE: Cloud SQL instance Backups tab showing schedule and retention window]**

Cloud SQL provides automated backups and point-in-time recovery to protect against data loss.

Automated backups run on a configurable schedule — by default once per day during a four-hour window. Backups are stored in GCP-managed storage and retained for 7 days by default, up to 365 days.

Point-in-time recovery uses transaction log files to restore the database to any second within the retention period. PITR requires binary logging enabled for MySQL or WAL archiving for PostgreSQL. This is how you recover from an accidental mass DELETE or UPDATE without a WHERE clause — you roll back to the exact second before the destructive statement executed.

**[SHOW CODE]**

```bash
# Enable automated backup with PITR
gcloud sql instances patch txwes-pg-prod \
    --backup-start-time=03:00 \
    --enable-bin-log \
    --retained-backups-count=30 \
    --retained-transaction-log-days=7
```

**[END CODE]**

Best practice: always restore to a new instance first, verify data integrity, then cut over. Never restore directly over a production instance without verification.

---

### Section 3 — High Availability

**[SHOW SLIDE: Cloud SQL HA architecture — primary in zone A, standby in zone B, shared persistent disk]**

Cloud SQL high availability provides automatic failover when the primary instance fails. The HA configuration has a primary instance in one zone and a hot standby in a different zone in the same region. Both share the same persistent disk, so the standby always has current data.

When the primary fails, Cloud SQL promotes the standby automatically. Typical failover time is around 60 seconds. Applications must handle connection errors and reconnect — most database client libraries do this with retry logic.

**[SHOW CODE]**

```bash
# Enable HA on an existing instance
gcloud sql instances patch txwes-pg-prod \
    --availability-type=REGIONAL

# Verify the HA configuration
gcloud sql instances describe txwes-pg-prod \
    --format="value(settings.availabilityType)"
```

**[END CODE]**

HA doubles compute cost because two instances are running. Always disable HA on development and test instances to control cost. Enable it for every production workload.

---

### Section 4 — Connection Pooling with PgBouncer

**[SHOW SLIDE: Direct connections vs. connection pool — many app threads sharing fewer database connections]**

Every database connection consumes memory and CPU on the Cloud SQL instance. Applications with many short-lived connections — serverless functions, microservices — can exhaust the connection limit quickly.

Connection pooling maintains a persistent pool of database connections shared across application requests. PgBouncer is the standard PostgreSQL connection pooler for Cloud SQL deployments.

**[SHOW CODE]**

```bash
# Install PgBouncer on a Compute Engine sidecar
sudo apt-get install -y pgbouncer

# Key settings in /etc/pgbouncer/pgbouncer.ini:
# pool_mode = transaction       <- recommended for most apps
# max_client_conn = 1000        <- max app-side connections
# default_pool_size = 20        <- server-side connections to Cloud SQL
```

**[END CODE]**

PgBouncer transaction pooling mode holds a server-side connection only for the duration of a database transaction, then returns it to the pool. This allows thousands of application connections to share a much smaller number of Cloud SQL connections.

---

### Section 5 — Cloud SQL Flags

**[SHOW CONSOLE: Cloud SQL instance Edit — Database flags section]**

Cloud SQL exposes database engine parameters as instance flags. For PostgreSQL these correspond to postgresql.conf settings.

| Flag | Purpose | Recommended Value |
|---|---|---|
| shared_buffers | Data page cache size | 25% of instance RAM |
| work_mem | Per-operation sort/hash memory | 4–64 MB depending on workload |
| max_connections | Max simultaneous connections | Set by Cloud SQL based on machine type |
| log_min_duration_statement | Log slow queries above this threshold (ms) | 1000 for production monitoring |

**[SHOW CODE]**

```bash
# Set database flags
gcloud sql instances patch txwes-pg-prod \
    --database-flags=log_min_duration_statement=1000,work_mem=16384

# View current flags
gcloud sql instances describe txwes-pg-prod \
    --format="value(settings.databaseFlags)"
```

**[END CODE]**

---

### Section 6 — Exam Tips for Module 03

**[SHOW SLIDE: Cloud SQL exam tips]**

Tip one: Cloud SQL Auth Proxy is always the recommended connection method for applications. It handles TLS and IAM authentication without managing IP allowlists or SSL certificates manually.

Tip two: Private IP is the security best practice for production. Any scenario mentioning elimination of public internet exposure to the database points to Private IP.

Tip three: read replicas serve read-only queries. They cannot accept writes. When a scenario asks how to scale read throughput without resizing the primary, read replicas are the answer.

Tip four: point-in-time recovery requires binary logging (MySQL) or WAL archiving (PostgreSQL) to be enabled before a destructive event occurs. Without PITR enabled, you can only restore to a full backup checkpoint.

Tip five: Cloud SQL HA failover takes approximately 60 seconds. The application must handle reconnection. If a scenario requires sub-second failover or zero-downtime maintenance, Cloud Spanner is the correct answer.

Tip six: storage auto-increase is one-directional. Storage can grow but never shrink. Reducing storage requires creating a new instance.

Tip seven: IAM database users are preferred for applications running on GCP because they eliminate the need to store and rotate database passwords.

Tip eight: Cloud SQL Enterprise Plus provides 99.99% SLA, better I/O, near-zero downtime maintenance, and cross-region read replicas compared to Cloud SQL Enterprise.

---

### Closing — Module 03 Wrap-Up

**[SHOW SLIDE: Module 03 complete — next up Module 04 Cloud Spanner]**

That completes Module 03. You now know how to create, configure, connect to, and operate Cloud SQL for MySQL and PostgreSQL on GCP.

Your lab walks you through creating a Cloud SQL instance with HA, creating a read replica, running a backup and restore, and testing the Auth Proxy.

In Module 04 we move to Cloud Spanner — Google's globally distributed relational database. It is architecturally different from Cloud SQL in ways the exam tests directly.

See you there.

---

Reference: cloud.google.com/learn

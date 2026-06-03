# Video Script: Module 09 — High Availability and Replication (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back. This is Part 2 of Module 09: High Availability and Replication.

In Part 1 we covered the theory — synchronous vs asynchronous replication, PostgreSQL streaming replication, and MySQL Group Replication. In Part 2 we focus on Cloud SQL HA architecture, connection string management for HA, and practical monitoring.

---

## Section 1 — Cloud SQL HA Architecture Deep Dive

Cloud SQL's high availability implementation differs from a traditional primary-standby setup in an important way: instead of the standby maintaining a separate copy of the data that is continuously synchronized via WAL, Cloud SQL uses **regional persistent disk** (also called "persistent disk replication").

### How Regional Persistent Disk HA Works

```text
Zone A                              Zone B
┌─────────────────────────┐         ┌─────────────────────────┐
│  Primary Instance       │         │  Standby Instance       │
│  (compute + OS)         │         │  (compute + OS)         │
│          │              │         │          │              │
│          └──────────────┼─────────┼──────────┘              │
│                         │         │                         │
│     Regional Persistent Disk (synchronous block replication)│
└─────────────────────────┘         └─────────────────────────┘
```

The key insight: **both the primary and standby instances mount the same underlying regional persistent disk**. Writes go to the disk, and the regional disk replicates synchronously across zones at the storage layer — below the database level.

Implications:

- The standby does not need to replay WAL to catch up — it is already at the same LSN as the primary at all times
- Failover is very fast (60–120 seconds) because the new primary just mounts the existing disk; no data replay required
- RPO is near zero — no committed transactions are lost because the disk is synchronously replicated
- The standby cannot serve read queries (it is not a hot standby from a query perspective) — it is purely for failover

This architecture is fundamentally different from a PostgreSQL streaming replication standby, which does have to replay WAL and can serve reads.

### Failover Trigger Conditions

Cloud SQL HA triggers automatic failover when:

- The primary instance's health check fails for a sustained period (typically > 60 seconds)
- The primary's zone experiences an outage
- A manual failover is triggered by the operator

When failover occurs:

1. The standby instance is promoted
2. Cloud SQL updates the DNS record for the instance connection endpoint
3. Active connections to the old primary are terminated
4. Applications reconnect using the same connection string and hit the new primary

### What HA Does Not Protect Against

Cloud SQL HA with regional persistent disk protects against:

- Zone-level hardware failure
- VM failures
- OS-level crashes

It does not protect against:

- Accidental data deletion (the deletion replicates immediately to the disk)
- Corruption from a buggy application
- Region-level outages (requires cross-region replica or backups)

---

## Section 2 — Connection Strings for HA

### Cloud SQL Connection Name

Every Cloud SQL instance has a connection name in the format `PROJECT:REGION:INSTANCE`. This name resolves to the current primary's IP. After failover, DNS updates automatically and the connection name still resolves correctly.

**Always use the connection name, not a hardcoded IP.** A hardcoded IP will break after failover.

### Application-Level Connection Retry

Even with HA, connections to the old primary are terminated during failover. Applications must handle this by:

1. Using a connection pool that retries on connection failure
2. Setting appropriate retry backoff (exponential backoff with jitter)
3. Not caching the database IP address client-side

For Java applications using JDBC:

```text
jdbc:mysql://127.0.0.1:3306/mydb?useSSL=false&autoReconnect=true&connectTimeout=5000&socketTimeout=30000
```

For Python (SQLAlchemy + PyMySQL):

```python
engine = create_engine(
    "mysql+pymysql://user:pass@127.0.0.1:3306/mydb",
    pool_pre_ping=True,          # validates connections before use
    pool_recycle=3600,           # recycles connections after 1 hour
    connect_args={"connect_timeout": 10}
)
```

`pool_pre_ping=True` is critical for HA — it issues a lightweight `SELECT 1` before returning a connection from the pool, detecting dead connections before the application uses them.

### Read Replica Connection for Reporting

```python
# Primary connection (read-write)
primary_engine = create_engine("mysql+pymysql://user:pass@127.0.0.1:3306/mydb")

# Replica connection (read-only)
replica_engine = create_engine("mysql+pymysql://user:pass@127.0.0.1:3307/mydb")
# Port 3307 via second Auth Proxy sidecar for the replica
```

---

## Section 3 — Monitoring Replication on Cloud SQL

### PostgreSQL Replication Monitoring

On a Cloud SQL PostgreSQL primary, check if standbys are connected:

```sql
SELECT client_addr, application_name, state,
       sent_lsn, replay_lsn,
       (sent_lsn - replay_lsn) AS lag_bytes
FROM pg_stat_replication;
```

On a read replica, check the replica's own lag:

```sql
SELECT now() - pg_last_xact_replay_timestamp() AS replication_delay;
```

### MySQL Replication Monitoring

On a Cloud SQL MySQL replica:

```sql
SHOW REPLICA STATUS\G
```

Key fields:

- `Replica_IO_Running: Yes` — IO thread is connected and receiving binlog
- `Replica_SQL_Running: Yes` — SQL thread is applying transactions
- `Seconds_Behind_Source: 0` — lag in seconds (0 = fully caught up)
- `Last_Error` — any current error preventing replication

### Cloud Monitoring Metrics

```bash
# Check replica lag via gcloud
gcloud monitoring read-time-series \
  "metric.type=\"cloudsql.googleapis.com/database/replication/replica_lag\"" \
  --filter="resource.labels.database_id=my-project:my-replica" \
  --project=my-project
```

Set up alerting policies in Cloud Monitoring to trigger when replica lag exceeds your acceptable threshold (for example, 60 seconds for a reporting replica, or 5 seconds for a near-real-time use case).

---

## Section 4 — Patroni: Automatic Failover for Self-Managed PostgreSQL

When running PostgreSQL on Compute Engine (not Cloud SQL), you need an external tool for automatic failover. **Patroni** is the industry standard for this.

Patroni uses a distributed consensus store — etcd, Consul, or ZooKeeper — to elect a leader (primary). All Patroni agents watch the consensus store. If the primary stops updating its lease, the agents elect a new primary.

### Patroni Key Concepts

```yaml
# patroni.yml (simplified)
name: pg-node-1
scope: pg-cluster

etcd:
  host: etcd-server:2379

bootstrap:
  dcs:
    ttl: 30
    loop_wait: 10
    retry_timeout: 10
    maximum_lag_on_failover: 1048576   # 1 MB lag threshold for failover candidacy

postgresql:
  listen: 0.0.0.0:5432
  connect_address: 10.0.1.10:5432
  data_dir: /var/lib/postgresql/15/main
  pgpass: /tmp/pgpass

  parameters:
    wal_level: replica
    hot_standby: on
    max_wal_senders: 5
    max_replication_slots: 5
```

`maximum_lag_on_failover` prevents a standby that is significantly behind from being promoted — promoting an out-of-date standby would cause data loss even with the DCS protecting leadership.

### HAProxy with Patroni

Patroni exposes a REST API health endpoint:

- `GET /` — returns 200 if the node is primary, 503 otherwise
- `GET /replica` — returns 200 if the node is a healthy standby

HAProxy uses these endpoints to route connections:

```text
frontend pgsql_primary
    bind *:5000
    default_backend primary_db

backend primary_db
    option httpchk GET /
    server pg1 10.0.1.10:5432 check port 8008
    server pg2 10.0.1.11:5432 check port 8008
    server pg3 10.0.1.12:5432 check port 8008
```

Write connections go to port 5000 (primary only). Read connections can be sent to port 5001 (replicas only, using the `/replica` endpoint).

---

## Section 5 — Replication Slots (PostgreSQL)

Replication slots guarantee that the primary retains WAL segments until the standby has consumed them. Without a replication slot, if a standby falls behind and the primary cycles past WAL segments the standby needs, the standby gets disconnected and cannot catch up.

```sql
-- Create a replication slot (on primary)
SELECT pg_create_physical_replication_slot('standby1_slot');

-- List all replication slots
SELECT slot_name, slot_type, active, restart_lsn
FROM pg_replication_slots;
```

**Warning:** Replication slots that are not consumed cause WAL accumulation. If a standby goes offline and does not come back, its replication slot keeps growing indefinitely — the primary disk fills up and the primary crashes. Monitor slot lag carefully:

```sql
SELECT slot_name,
       pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) AS lag_size
FROM pg_replication_slots
WHERE active = false;
```

If an offline slot accumulates more than a few GB, drop it:

```sql
SELECT pg_drop_replication_slot('standby1_slot');
```

---

## Section 6 — Exam Tips

**Most-tested scenarios for Module 09:**

- Distinguishing synchronous from asynchronous replication by RPO (sync = 0, async > 0)
- Cloud SQL HA uses regional persistent disk, not WAL streaming to standby
- Cloud SQL HA standby cannot serve read queries
- Read replicas use async replication and can lag
- Connection string must use instance connection name, not IP, for transparent failover
- `pg_stat_replication` on primary; `pg_last_xact_replay_timestamp()` on standby
- Replication slot risk: unbounded WAL growth if standby goes offline

**Common traps:**

- The exam may describe needing a "read-only query endpoint that never lags." The technically correct answer depends on context — pure sync replication with a read-capable standby or a caching layer. Cloud SQL HA standby does not serve reads.
- PostgreSQL synchronous replication with `synchronous_standby_names` stalls the primary if all named standbys disconnect. This is intentional (to protect RPO) but students often think of it as a bug.

---

## Closing

That is Module 09 complete. You now have a comprehensive understanding of replication theory, PostgreSQL streaming replication, MySQL Group Replication, Cloud SQL HA architecture, connection management for HA, and Patroni for self-managed failover.

Complete the Module 09 lab, then tackle the quiz. See you in Module 10: Database Performance Tuning.

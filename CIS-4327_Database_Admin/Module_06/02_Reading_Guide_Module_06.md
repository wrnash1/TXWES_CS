# Reading Guide: Module 06 — PostgreSQL Administration

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Overview

This reading guide accompanies the Module 06 video lectures and lab. PostgreSQL is the foundational engine for Cloud SQL for PostgreSQL on Google Cloud Platform. Mastery of its configuration, security model, maintenance routines, and connection management is essential for both production database administration and the Google Cloud Professional Database Engineer certification exam.

Work through all sections before attempting the lab and quiz.

---

## Section 1 — PostgreSQL Architecture Review

### 1.1 Process Model

PostgreSQL uses a **process-per-connection** architecture. The `postmaster` is the supervisory process; it spawns one backend process per client connection. Contrast this with MySQL, which uses threads. The process model provides strong isolation but limits raw connection scalability — a key motivation for PgBouncer.

**Key background processes and their roles:**

| Process | Role |
|---|---|
| checkpointer | Flushes dirty shared_buffers pages to disk |
| background writer | Proactively writes dirty pages ahead of checkpoints |
| autovacuum launcher | Monitors tables and triggers autovacuum workers |
| WAL writer | Flushes WAL buffers to disk |
| stats collector | Gathers runtime statistics for pg_stat views |
| archiver | Copies completed WAL segments for point-in-time recovery |

### 1.2 Shared Memory Layout

When PostgreSQL starts, it allocates a large shared memory region. The most important component is the **shared buffer pool** (controlled by `shared_buffers`). All backend processes read from and write to these shared buffers. When a backend needs a data page not already in the buffer pool, it reads it from disk into a free buffer slot.

The **WAL buffer** (`wal_buffers`) is a smaller shared memory region used to stage WAL records before the WAL writer flushes them to disk.

### 1.3 WAL — Write-Ahead Log

Every data modification is first written to the WAL before it is applied to the data heap files. This guarantees **durability** — if a crash occurs, PostgreSQL replays the WAL during recovery.

WAL also enables replication. Standbys receive and apply WAL records continuously.

`wal_level` controls WAL verbosity:

- `minimal` — bare minimum for crash recovery. Replication not possible.
- `replica` — sufficient for streaming replication and base backups.
- `logical` — adds information needed for logical decoding, CDC, and logical replication slots.

---

## Section 2 — postgresql.conf Reference

### 2.1 Connection and Authentication

```ini
listen_addresses = 'localhost'   # Bind only to localhost for security
port = 5432
max_connections = 100            # Each connection consumes ~5-10 MB overhead
superuser_reserved_connections = 3  # Reserved for DBA emergency access
```

`superuser_reserved_connections` ensures that even when the connection pool is saturated, superusers can still connect to diagnose and resolve issues.

### 2.2 Memory

```ini
shared_buffers = 2GB             # ~25% of RAM for dedicated DB server
work_mem = 16MB                  # Per sort/hash node; multiply by concurrent operations
maintenance_work_mem = 256MB     # For VACUUM, CREATE INDEX, REINDEX
temp_buffers = 8MB               # Per-session buffer for temporary tables
effective_cache_size = 6GB       # Planner hint: ~75% of total RAM
```

### 2.3 WAL and Replication

```ini
wal_level = replica
wal_compression = on             # Compresses WAL records to reduce I/O
max_wal_senders = 10
wal_keep_size = 2GB              # Minimum WAL to retain for standbys
archive_mode = on
archive_command = 'gcloud storage cp %p gs://my-bucket/wal/%f'
```

### 2.4 Checkpoints

```ini
checkpoint_timeout = 10min
checkpoint_completion_target = 0.9
max_wal_size = 4GB
min_wal_size = 1GB
```

`checkpoint_completion_target = 0.9` spreads checkpoint writes across 90% of the interval, smoothing I/O.

### 2.5 Query Planner

```ini
random_page_cost = 1.1           # For SSD storage; default 4.0 is for spinning disk
effective_io_concurrency = 200   # For SSD; drives parallel prefetch
enable_partitionwise_join = on
enable_partitionwise_aggregate = on
```

Lowering `random_page_cost` to 1.1 for SSD is one of the most impactful planner tuning changes. It tells the planner that random reads are almost as cheap as sequential reads, making index scans more attractive.

### 2.6 Autovacuum

```ini
autovacuum = on
autovacuum_max_workers = 3
autovacuum_naptime = 1min
autovacuum_vacuum_threshold = 50
autovacuum_vacuum_scale_factor = 0.2
autovacuum_analyze_threshold = 50
autovacuum_analyze_scale_factor = 0.1
autovacuum_vacuum_cost_delay = 2ms
autovacuum_vacuum_cost_limit = 200
```

For tables with millions of rows, override autovacuum at the table level to trigger more aggressively than the defaults.

---

## Section 3 — pg_hba.conf Authentication

### 3.1 File Format

Each rule in pg_hba.conf follows this format:

```text
TYPE  DATABASE  USER  ADDRESS  METHOD  [OPTIONS]
```

Rules are evaluated top-to-bottom. The first match wins.

### 3.2 Authentication Methods Compared

| Method | Security Level | Use Case |
|---|---|---|
| trust | None (dangerous) | Local dev only |
| peer | OS-level | Local Unix socket connections |
| password | Low (plaintext) | Never use in production |
| md5 | Moderate | Legacy compatibility only |
| scram-sha-256 | Strong | All network connections |
| cert | Very strong | mTLS client certificate auth |
| gss/sspi | Enterprise | Kerberos/Active Directory |
| ldap | Enterprise | LDAP directory integration |
| reject | N/A | Explicit deny rule |

### 3.3 Recommended Production Configuration

```text
# TYPE  DATABASE        USER            ADDRESS                 METHOD

# Superuser local access via OS identity
local   all             postgres                                peer

# Application user connections (network)
host    appdb           appuser         10.0.1.0/24             scram-sha-256

# Read-only reporting user
host    appdb           reporter        10.0.2.0/24             scram-sha-256

# Streaming replication
host    replication     replicator      10.0.3.10/32            scram-sha-256

# Deny all other connections
host    all             all             0.0.0.0/0               reject
```

### 3.4 SSL Enforcement

For network connections, require SSL by changing the connection type from `host` to `hostssl`:

```text
hostssl appdb  appuser  10.0.1.0/24  scram-sha-256
```

Or use the `ssl_cert_file` and `ssl_key_file` parameters in postgresql.conf and set `ssl = on`.

---

## Section 4 — Roles and Privilege Management

### 4.1 Role Hierarchy

PostgreSQL roles form a DAG (directed acyclic graph). A role can be a member of multiple other roles, inheriting their privileges by default.

```sql
-- Create base group roles
CREATE ROLE app_read;
CREATE ROLE app_write;
CREATE ROLE app_admin;

-- Grant privileges to group roles
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_read;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_write;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_admin;

-- Create individual login users and assign groups
CREATE ROLE alice WITH LOGIN PASSWORD 'AlicePass!' IN ROLE app_write;
CREATE ROLE bob WITH LOGIN PASSWORD 'BobPass!' IN ROLE app_read;
CREATE ROLE carol WITH LOGIN PASSWORD 'CarolPass!' IN ROLE app_admin;
```

### 4.2 Row-Level Security (RLS)

PostgreSQL supports row-level security policies that filter rows based on the current role — essential for multi-tenant applications.

```sql
-- Enable RLS on the table
ALTER TABLE customer_data ENABLE ROW LEVEL SECURITY;

-- Policy: users see only their own tenant's rows
CREATE POLICY tenant_isolation ON customer_data
  USING (tenant_id = current_setting('app.tenant_id')::INTEGER);

-- Set the tenant context at application session start
SET app.tenant_id = '42';
```

### 4.3 Column-Level Privileges

```sql
-- Grant SELECT on specific columns only
GRANT SELECT (customer_id, order_date, total_amount)
  ON TABLE orders TO reporting_role;
-- Restricts access to sensitive columns like credit_card_number
```

### 4.4 Revoking Privileges

```sql
-- Revoke all privileges on a table
REVOKE ALL PRIVILEGES ON TABLE orders FROM contractor_role;

-- Revoke schema usage
REVOKE USAGE ON SCHEMA analytics FROM contractor_role;

-- Remove role membership
REVOKE app_write FROM alice;
```

---

## Section 5 — VACUUM, ANALYZE, and Bloat Management

### 5.1 MVCC and Dead Tuples

PostgreSQL's MVCC model keeps old row versions visible to concurrent transactions that started before the UPDATE or DELETE. Once all transactions that could see the old version have committed, the old tuple becomes a **dead tuple** — invisible to new queries but still occupying physical space.

VACUUM marks dead tuples as reusable. VACUUM FULL rewrites the table, compacting storage but requiring an exclusive lock.

### 5.2 Monitoring Bloat

```sql
-- Dead tuple ratio per table
SELECT schemaname, relname,
       n_live_tup, n_dead_tup,
       round(100.0 * n_dead_tup / NULLIF(n_live_tup + n_dead_tup, 0), 1) AS dead_pct,
       pg_size_pretty(pg_total_relation_size(schemaname || '.' || relname)) AS total_size
FROM pg_stat_user_tables
WHERE n_dead_tup > 10000
ORDER BY dead_pct DESC;
```

### 5.3 Transaction ID Wraparound

PostgreSQL transaction IDs are 32-bit. After 2.1 billion transactions, they wrap. PostgreSQL will refuse to process new transactions rather than allow data corruption. This is called **transaction ID wraparound**.

**Monitoring:**

```sql
SELECT datname,
       age(datfrozenxid) AS xid_age,
       2100000000 - age(datfrozenxid) AS xids_remaining
FROM pg_database
ORDER BY xid_age DESC;
```

Alert when `xid_age` exceeds 1.5 billion. Run `VACUUM FREEZE` on the oldest tables if needed.

### 5.4 Table-Level Autovacuum Override

```sql
-- Tune autovacuum for a high-churn table
ALTER TABLE order_events SET (
    autovacuum_vacuum_scale_factor = 0.01,
    autovacuum_vacuum_threshold = 100,
    autovacuum_analyze_scale_factor = 0.005
);
```

---

## Section 6 — pg_stat Views Reference

### 6.1 Frequently Used Views

| View | Purpose |
|---|---|
| pg_stat_activity | Live session state, query text, wait events |
| pg_stat_user_tables | Per-table DML counts, vacuum/analyze timestamps |
| pg_stat_user_indexes | Index scan counts — identify unused indexes |
| pg_stat_bgwriter | Checkpoint and buffer writer statistics |
| pg_stat_replication | Standby lag and replication state |
| pg_locks | Current lock holders and waiters |
| pg_stat_statements | Aggregated query performance (requires extension) |

### 6.2 Enabling pg_stat_statements

```sql
-- In postgresql.conf:
-- shared_preload_libraries = 'pg_stat_statements'

-- After restart, create the extension:
CREATE EXTENSION pg_stat_statements;

-- Query top 10 slowest queries by total execution time:
SELECT query, calls, total_exec_time, mean_exec_time, rows
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

---

## Section 7 — PgBouncer Connection Pooling

### 7.1 Architecture

```text
Application Servers (1000 connections)
         |
    [PgBouncer :6432]
         |  (20 server connections)
    [PostgreSQL :5432]
```

PgBouncer multiplexes many client connections onto a small pool of actual PostgreSQL server connections, eliminating the overhead of OS process creation per connection.

### 7.2 Pooling Mode Selection

| Mode | Server Connection | LISTEN/NOTIFY | Prepared Stmts | Typical Use |
|---|---|---|---|---|
| session | Per client session | Yes | Yes | Low concurrency apps |
| transaction | Per transaction | No | Limited | OLTP (recommended) |
| statement | Per SQL statement | No | No | Rarely appropriate |

### 7.3 pgbouncer.ini Key Parameters

```ini
[databases]
mydb = host=postgres-primary port=5432 dbname=mydb

[pgbouncer]
listen_port = 6432
pool_mode = transaction
max_client_conn = 2000
default_pool_size = 25
reserve_pool_size = 10
reserve_pool_timeout = 5
server_idle_timeout = 600
server_lifetime = 3600
client_idle_timeout = 0
auth_type = scram-sha-256
auth_file = /etc/pgbouncer/userlist.txt
stats_users = monitoring_user
```

---

## Section 8 — Key Terms

| Term | Definition |
|---|---|
| MVCC | Multi-Version Concurrency Control — readers do not block writers |
| WAL | Write-Ahead Log — durability and replication mechanism |
| Dead tuple | A row version no longer visible to any transaction |
| VACUUM | Reclaims dead tuple space; does not lock table |
| VACUUM FULL | Rewrites table; requires exclusive lock |
| Transaction ID wraparound | PostgreSQL's hard limit at 2.1 billion transactions |
| pg_hba.conf | Host-based authentication rules file |
| scram-sha-256 | Strongest standard PostgreSQL password auth method |
| PgBouncer | Lightweight connection pooler for PostgreSQL |
| Transaction pooling | PgBouncer mode: one server connection per transaction |

---

## Study Questions

1. What is the difference between VACUUM and VACUUM FULL? When should each be used?

2. Explain the transaction ID wraparound problem. How do you monitor for it?

3. What authentication method is recommended for network connections in pg_hba.conf, and why?

4. Describe the three PgBouncer pooling modes. Which features are incompatible with transaction pooling?

5. What does `effective_cache_size` actually control? Why is it common to confuse it with `shared_buffers`?

6. What is the purpose of `superuser_reserved_connections` in postgresql.conf?

7. How would you identify unused indexes in a PostgreSQL database using a system catalog view?

8. What `wal_level` is required to use logical replication or CDC tools like Debezium?

---

## Certification Exam Checklist

Before the exam, confirm you can answer these:

- [ ] Sizing recommendations for shared_buffers, work_mem, effective_cache_size
- [ ] pg_hba.conf method hierarchy from least to most secure
- [ ] What autovacuum_vacuum_scale_factor controls
- [ ] How to check transaction ID age with pg_database
- [ ] gcloud sql instances patch syntax for setting database flags
- [ ] PgBouncer pooling mode tradeoffs for LISTEN/NOTIFY compatibility
- [ ] Which background process is responsible for checkpoint writes
- [ ] How to identify a blocking session using pg_blocking_pids()

---

## 9. Supplemental Resources

**1. PostgreSQL Official Documentation — Server Configuration**
https://www.postgresql.org/docs/current/runtime-config.html
The complete reference for all postgresql.conf parameters including shared_buffers, work_mem, wal_level, autovacuum settings, and checkpoint configuration.

**2. PostgreSQL Wiki — Tuning Your PostgreSQL Server**
https://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server
Community-maintained tuning guide covering practical recommendations for shared_buffers, effective_cache_size, work_mem, and WAL settings for common workload types.

**3. PgBouncer Documentation — Configuration Reference**
https://www.pgbouncer.org/config.html
Official PgBouncer configuration reference covering all pgbouncer.ini parameters, pooling mode trade-offs, auth_type options, and pool sizing strategies.

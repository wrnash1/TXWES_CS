# Video Script: Module 06 — PostgreSQL Administration (Part 2 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back. This is Part 2 of Module 06: PostgreSQL Administration.

In Part 1 we covered architecture, postgresql.conf, pg_hba.conf, roles, and tablespaces. In Part 2 we get hands-on. We cover VACUUM and ANALYZE, the pg_stat monitoring views, and PgBouncer connection pooling — all of which appear on the Google Cloud Database Engineer exam and in the Module 06 lab.

---

## Section 1 — VACUUM and Table Bloat

PostgreSQL uses MVCC — Multi-Version Concurrency Control. When a row is updated or deleted, the old version of that row is not immediately removed. It is marked as dead. These dead tuples accumulate over time and waste disk space. They also slow down sequential scans because PostgreSQL must read and skip past them.

**VACUUM** reclaims space occupied by dead tuples and marks it as reusable.

**VACUUM FULL** reclaims space and actually returns it to the operating system, but it requires an exclusive lock on the table and rewrites the entire table. Avoid VACUUM FULL on production tables during business hours.

**ANALYZE** updates the statistics that the query planner uses to choose execution plans. Stale statistics lead to bad plan choices — for example, the planner might choose a sequential scan on a large table when an index scan would be far faster.

```sql
-- Standard VACUUM (does not lock table for reads/writes)
VACUUM orders;

-- VACUUM plus ANALYZE in one pass
VACUUM ANALYZE orders;

-- Aggressive VACUUM FULL — use off-hours only
VACUUM FULL orders;

-- ANALYZE only (faster, no dead tuple reclaim)
ANALYZE orders;
```

### Autovacuum

PostgreSQL has an autovacuum daemon that automatically runs VACUUM and ANALYZE based on table activity thresholds. The key parameters are:

```ini
autovacuum = on
autovacuum_vacuum_scale_factor = 0.2
autovacuum_analyze_scale_factor = 0.1
autovacuum_vacuum_cost_delay = 2ms
```

`autovacuum_vacuum_scale_factor = 0.2` means autovacuum triggers when 20% of a table's rows are dead. For very large tables, 20% can be millions of rows — consider lowering this for large, write-heavy tables.

You can override autovacuum parameters at the table level:

```sql
ALTER TABLE orders SET (
  autovacuum_vacuum_scale_factor = 0.05,
  autovacuum_analyze_scale_factor = 0.02
);
```

### Transaction ID Wraparound — Critical Warning

PostgreSQL transaction IDs are 32-bit unsigned integers. They wrap around after approximately 2.1 billion transactions. If a database approaches wraparound, PostgreSQL will shut down to prevent data corruption. This is the most serious operational risk of neglecting VACUUM.

Monitor transaction age with:

```sql
SELECT datname, age(datfrozenxid) AS txid_age
FROM pg_database
ORDER BY txid_age DESC;
```

If txid_age approaches 2,000,000,000, run aggressive VACUUM immediately:

```sql
VACUUM FREEZE orders;
```

---

## Section 2 — pg_stat Monitoring Views

PostgreSQL exposes a rich set of statistics views that let you monitor activity, identify slow queries, and diagnose lock contention.

### pg_stat_activity

This view shows currently running sessions.

```sql
SELECT pid, usename, application_name, state, query, now() - query_start AS duration
FROM pg_stat_activity
WHERE state != 'idle'
ORDER BY duration DESC;
```

Key columns:

- `state`: `active`, `idle`, `idle in transaction`, `waiting`
- `wait_event_type` and `wait_event`: what the backend is waiting on (lock, I/O, etc.)
- `query`: the current or most recent SQL statement

### pg_stat_user_tables

Shows cumulative statistics per table.

```sql
SELECT relname, n_live_tup, n_dead_tup,
       last_vacuum, last_autovacuum,
       last_analyze, last_autoanalyze
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;
```

High `n_dead_tup` relative to `n_live_tup` indicates a table needs VACUUM.

### pg_stat_user_indexes

Shows how often each index is used.

```sql
SELECT schemaname, relname, indexrelname,
       idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
ORDER BY idx_scan ASC;
```

An index with `idx_scan = 0` has never been used by a query plan. It is a candidate for removal — it wastes storage and slows down writes with no benefit.

### pg_locks

Shows current lock activity.

```sql
SELECT pid, locktype, relation::regclass, mode, granted
FROM pg_locks
WHERE NOT granted;
```

Rows where `granted = false` indicate blocked queries. Join with `pg_stat_activity` to see who holds the blocking lock.

### pg_stat_bgwriter

Shows checkpoint and background writer statistics.

```sql
SELECT checkpoints_timed, checkpoints_req,
       buffers_checkpoint, buffers_clean,
       maxwritten_clean, buffers_backend
FROM pg_stat_bgwriter;
```

High `buffers_backend` means backends are writing dirty pages themselves instead of the background writer keeping up — consider tuning `bgwriter_lru_maxpages` and `bgwriter_lru_multiplier`.

---

## Section 3 — Connection Pooling with PgBouncer

PostgreSQL's process-per-connection model means that every client connection spawns a separate OS process. Under high concurrency — hundreds or thousands of connections — this creates significant overhead: process creation time, memory per process, and CPU context switching.

**PgBouncer** is a lightweight connection pooler that sits between your application and PostgreSQL. Applications connect to PgBouncer, which maintains a pool of actual PostgreSQL connections and assigns them to application requests as needed.

### PgBouncer Pooling Modes

PgBouncer offers three pooling modes:

- **Session pooling**: A server connection is assigned to the client for the duration of the client session. Least efficient, but compatible with all PostgreSQL features including prepared statements and advisory locks.
- **Transaction pooling**: A server connection is assigned only for the duration of a single transaction. Most efficient and most commonly used in production. **Incompatible with session-level features** like `SET LOCAL`, `LISTEN/NOTIFY`, and some prepared statement patterns.
- **Statement pooling**: A server connection is assigned per individual SQL statement. Rarely used — incompatible with multi-statement transactions.

For most OLTP applications, **transaction pooling** is the right choice.

### PgBouncer Configuration

```ini
[databases]
appdb = host=127.0.0.1 port=5432 dbname=appdb

[pgbouncer]
listen_port = 6432
listen_addr = *
auth_type = scram-sha-256
auth_file = /etc/pgbouncer/userlist.txt
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 20
min_pool_size = 5
reserve_pool_size = 5
server_idle_timeout = 600
log_connections = 1
log_disconnections = 1
```

Key parameters:

- `max_client_conn`: Maximum number of client connections PgBouncer will accept (1,000 in this example).
- `default_pool_size`: Number of actual PostgreSQL server connections per database/user pair (20 here).
- `reserve_pool_size`: Extra connections available when all pool slots are busy.

So in this configuration, 1,000 application clients share 20 actual Postgres connections — a 50:1 multiplexing ratio.

### Starting PgBouncer

```bash
sudo apt-get install -y pgbouncer
sudo systemctl enable pgbouncer
sudo systemctl start pgbouncer

# Check status
sudo systemctl status pgbouncer

# Connect to PgBouncer admin console
psql -h 127.0.0.1 -p 6432 -U pgbouncer pgbouncer
```

### PgBouncer Admin Commands

```sql
-- Show pool status
SHOW POOLS;

-- Show active client connections
SHOW CLIENTS;

-- Show server connections to PostgreSQL
SHOW SERVERS;

-- Pause new connections (for maintenance)
PAUSE;

-- Resume connections
RESUME;

-- Reload configuration without restart
RELOAD;
```

---

## Section 4 — Hands-On: Putting It Together

Let me walk through a realistic administration scenario.

**Scenario:** You are the DBA for a production PostgreSQL 15 database. Queries are slowing down and you need to diagnose what is happening.

**Step 1 — Find long-running queries:**

```sql
SELECT pid, usename, now() - query_start AS runtime, state, query
FROM pg_stat_activity
WHERE state = 'active'
  AND now() - query_start > interval '5 seconds'
ORDER BY runtime DESC;
```

**Step 2 — Check for blocking locks:**

```sql
SELECT blocked.pid AS blocked_pid,
       blocked.query AS blocked_query,
       blocking.pid AS blocking_pid,
       blocking.query AS blocking_query
FROM pg_stat_activity AS blocked
JOIN pg_stat_activity AS blocking
  ON blocking.pid = ANY(pg_blocking_pids(blocked.pid))
WHERE cardinality(pg_blocking_pids(blocked.pid)) > 0;
```

**Step 3 — Check table bloat:**

```sql
SELECT relname,
       n_dead_tup,
       n_live_tup,
       round(100.0 * n_dead_tup / NULLIF(n_live_tup + n_dead_tup, 0), 2) AS dead_pct
FROM pg_stat_user_tables
WHERE n_dead_tup > 1000
ORDER BY dead_pct DESC;
```

**Step 4 — Terminate a stuck query if needed:**

```sql
-- Graceful cancel (sends interrupt signal)
SELECT pg_cancel_backend(12345);

-- Hard terminate (closes connection)
SELECT pg_terminate_backend(12345);
```

---

## Section 5 — Cloud SQL PostgreSQL Configuration

On Cloud SQL, you manage postgresql.conf parameters through the Cloud SQL console or gcloud. You cannot edit the file directly.

```bash
# Update a database flag on a Cloud SQL instance
gcloud sql instances patch my-postgres-instance \
  --database-flags max_connections=200,shared_buffers=512MB \
  --project my-gcp-project

# View current flags
gcloud sql instances describe my-postgres-instance \
  --project my-gcp-project \
  --format="value(settings.databaseFlags)"
```

Some flags require an instance restart (like `max_connections`). Others apply immediately. The Cloud SQL console indicates which flags require restart.

For pg_hba.conf equivalents on Cloud SQL, use **Authorized Networks** in the console combined with SSL/TLS enforcement — you cannot directly edit pg_hba.conf on a managed Cloud SQL instance.

---

## Section 6 — Exam Tips

**Most-tested PostgreSQL topics on the Google Cloud Database Engineer exam:**

- Autovacuum tuning for large tables
- Transaction ID wraparound monitoring and prevention
- pg_stat_activity for query diagnosis
- PgBouncer transaction vs session pooling tradeoffs
- gcloud sql instances patch for setting database flags
- WAL level settings for replication vs logical decoding

**Exam traps to avoid:**

- VACUUM FULL is not the standard VACUUM — it requires an exclusive lock and should not be used on live production tables without a maintenance window.
- PgBouncer transaction pooling breaks `LISTEN/NOTIFY` and some prepared statement patterns — this is a real exam scenario about choosing the right pooling mode.
- `max_connections` changes on Cloud SQL require an instance restart.

---

## Closing

That wraps up Module 06: PostgreSQL Administration. You now have a complete picture from installation and configuration through monitoring, maintenance, and connection pooling.

The Module 06 lab walks you through configuring a PostgreSQL instance, creating roles, running VACUUM, querying pg_stat views, and setting up PgBouncer. Complete it before the quiz.

See you in Module 07, where we cover MySQL and Cloud SQL.

# Quiz: Module 06 — PostgreSQL Administration

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

Instructions: Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A PostgreSQL server has 16 GB of RAM. Which value for `shared_buffers` follows the standard sizing recommendation for a dedicated database server?

- A) 512 MB
- B) 1 GB
- C) 4 GB
- D) 8 GB

**Answer: C** — The standard starting recommendation is 25% of total RAM for `shared_buffers` on a dedicated database server. 25% of 16 GB = 4 GB. Option D (8 GB = 50%) is too aggressive for most workloads.

---

### Question 2

A developer needs PostgreSQL to support a logical replication tool that streams row-level changes to a downstream CDC consumer. Which `wal_level` setting is required?

- A) minimal
- B) replica
- C) logical
- D) archive

**Answer: C** — `wal_level = logical` is required for logical replication and CDC tools such as Debezium or pglogical. The `replica` level supports streaming replication but does not write the additional information needed for logical decoding.

---

### Question 3

Which pg_hba.conf authentication method is recommended for network connections in a production PostgreSQL environment?

- A) trust
- B) md5
- C) peer
- D) scram-sha-256

**Answer: D** — `scram-sha-256` is the strongest standard password-based authentication method available. `trust` has no authentication. `md5` uses a weak hash. `peer` only works for local Unix socket connections.

---

### Question 4

You query `pg_stat_user_tables` and find the `orders` table has `n_live_tup = 500,000` and `n_dead_tup = 450,000`. What is the most appropriate immediate action?

- A) Run `REINDEX TABLE orders;`
- B) Run `VACUUM ANALYZE orders;`
- C) Run `CLUSTER orders;`
- D) Drop and recreate the table

**Answer: B** — A dead tuple ratio approaching 50% indicates severe bloat. `VACUUM ANALYZE` reclaims dead tuple space and updates planner statistics without locking the table. REINDEX does not address dead tuples. CLUSTER rewrites for physical ordering but does not directly reclaim bloat without a VACUUM first.

---

### Question 5

A database shows `age(datfrozenxid) = 1,950,000,000` in `pg_database`. What is the risk and the correct response?

- A) The database is near transaction ID wraparound; run `VACUUM FREEZE` on the oldest tables immediately.
- B) The database has too many connections; reduce `max_connections`.
- C) The WAL has grown too large; run `pg_resetwal`.
- D) This value is normal and requires no action.

**Answer: A** — PostgreSQL's 32-bit transaction IDs wrap at approximately 2.1 billion. At 1.95 billion, the database is critically close. PostgreSQL will refuse new transactions before allowing wraparound. `VACUUM FREEZE` advances `datfrozenxid` and resolves the risk.

---

### Question 6

You are configuring PgBouncer for a high-traffic OLTP application that does not use `LISTEN/NOTIFY` or session-level `SET` commands. Which pooling mode gives the best multiplexing efficiency?

- A) session
- B) transaction
- C) statement
- D) connection

**Answer: B** — Transaction pooling releases the server connection back to the pool after each transaction commit or rollback, enabling a high client-to-server multiplexing ratio. Because the application has no session-level features incompatible with transaction pooling, this is the optimal choice.

---

### Question 7

Which PostgreSQL background process automatically triggers VACUUM and ANALYZE based on per-table activity thresholds?

- A) checkpointer
- B) background writer
- C) autovacuum launcher
- D) WAL writer

**Answer: C** — The autovacuum launcher monitors per-table dead tuple and modification counters and spawns worker processes to run VACUUM and ANALYZE when scale factor and threshold values are exceeded.

---

### Question 8

A Cloud SQL for PostgreSQL instance needs `max_connections` changed from 100 to 200. What is the correct method?

- A) Edit `/etc/postgresql/15/main/postgresql.conf` directly on the instance.
- B) Use `gcloud sql instances patch` with the `--database-flags` option.
- C) Connect via psql and run `ALTER SYSTEM SET max_connections = 200;`
- D) Rebuild the instance from a snapshot with a new configuration.

**Answer: B** — Cloud SQL is a managed service; direct filesystem access is not available. Database flags are managed via `gcloud sql instances patch --database-flags`. Note that `max_connections` requires an instance restart on Cloud SQL.

---

### Question 9

You suspect a query is blocked by a lock held by another session. Which query correctly identifies both the blocked and blocking sessions?

- A) `SELECT * FROM pg_locks WHERE NOT granted;`
- B) `SELECT pid, query FROM pg_stat_activity WHERE state = 'waiting';`
- C) Join `pg_stat_activity` to itself using `pg_blocking_pids()` to find sessions where `cardinality(pg_blocking_pids(blocked.pid)) > 0`.
- D) `SELECT * FROM pg_stat_bgwriter;`

**Answer: C** — `pg_blocking_pids()` returns the PIDs of all sessions blocking a given session. Joining `pg_stat_activity` on that result surfaces both sides of the lock conflict including query text. Option A shows ungranted locks but not the blocker's query. The `'waiting'` state string in option B does not exist in modern PostgreSQL.

---

### Question 10

What does `effective_cache_size` in postgresql.conf actually control?

- A) Allocates a shared memory cache of the specified size.
- B) Sets the maximum size of the operating system page cache.
- C) Provides a hint to the query planner about total expected caching memory, including OS cache.
- D) Limits working memory used by sort and hash operations.

**Answer: C** — `effective_cache_size` is a planner hint only — it allocates no memory. It informs the planner how much memory is likely available for caching (shared_buffers + OS page cache) so it can weigh index scans more favorably on well-cached systems. `shared_buffers` allocates actual PostgreSQL buffer cache. `work_mem` controls sort and hash operation memory.

---

### Question 11 (5 points)

A PostgreSQL DBA notices that `pg_stat_user_indexes` shows `idx_scans = 0` for an index that has existed for six months on a high-traffic table. What does this indicate and what action should be considered?

- A) The index has never been used by the query planner; it should be evaluated for removal to reduce write overhead and storage cost.
- B) The index scan counter resets to zero each week; 0 scans is normal and requires no action.
- C) The index is corrupted and must be rebuilt immediately with REINDEX.
- D) An index with 0 scans is more selective than an index with many scans; it should be kept.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `pg_stat_user_indexes` counters reset only on server restart or when `pg_stat_reset()` is called; they are cumulative over time and do not reset weekly.
  - C) A zero scan count indicates the index is not being used, not that it is corrupted; a corrupted index would generate errors, not simply go unselected by the planner.
  - D) A high scan count means the planner uses the index frequently, indicating it is valuable; zero scans means the index provides no query benefit while imposing write overhead.

---

### Question 12 (5 points)

Which PostgreSQL configuration parameter controls the maximum amount of memory a single sort or hash operation can use before spilling to disk?

- A) `work_mem`
- B) `shared_buffers`
- C) `effective_cache_size`
- D) `maintenance_work_mem`

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `shared_buffers` is the size of the PostgreSQL shared buffer pool used for caching table and index data; it does not control per-operation sort or hash memory.
  - C) `effective_cache_size` is a planner hint that allocates no actual memory; it does not control memory for any operation.
  - D) `maintenance_work_mem` controls memory for maintenance operations such as VACUUM, CREATE INDEX, and CLUSTER; it does not apply to regular query sort or hash operations.

---

### Question 13 (5 points)

A PostgreSQL DBA wants to terminate a specific idle connection with PID 4821 that has been holding an idle-in-transaction state for two hours. Which command accomplishes this without restarting the server?

- A) `SELECT pg_terminate_backend(4821);`
- B) `SELECT pg_cancel_backend(4821);`
- C) `KILL 4821;` at the operating system level.
- D) `ALTER SYSTEM SET idle_in_transaction_session_timeout = '0';`

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `pg_cancel_backend()` sends a SIGINT to cancel the current query of the target backend, but it does not terminate the connection; an idle-in-transaction session has no active query to cancel.
  - C) OS-level `kill` will terminate the process but bypasses PostgreSQL's clean connection shutdown, which may leave locks unreleased momentarily; `pg_terminate_backend()` is the correct in-database method.
  - D) `idle_in_transaction_session_timeout` prevents future idle-in-transaction sessions from accumulating but does not terminate the currently offending session.

---

### Question 14 (5 points)

A PostgreSQL instance running on a Cloud SQL for PostgreSQL instance has `log_min_duration_statement = 500` set. Which queries will appear in the database log?

- A) All queries that take longer than 500 milliseconds to execute.
- B) All queries that return more than 500 rows.
- C) All queries that acquire more than 500 locks simultaneously.
- D) All queries that modify more than 500 rows.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Row count thresholds are not a built-in PostgreSQL logging parameter; `log_min_duration_statement` is purely time-based.
  - C) Lock count thresholds are not controlled by `log_min_duration_statement`; lock monitoring uses `pg_locks` and `deadlock_timeout` parameters.
  - D) Row modification counts are not the criterion for this parameter; it measures wall-clock execution time in milliseconds.

---

### Question 15 (5 points)

A Cloud SQL for PostgreSQL database engineer wants to enable logical replication for a downstream data pipeline. Which two conditions must be true simultaneously?

- A) `wal_level` must be set to `logical` AND the replication role must have the REPLICATION attribute.
- B) `wal_level` must be set to `replica` AND `max_wal_senders` must be greater than 0.
- C) `wal_level` must be set to `logical` AND `ssl` must be enabled on the instance.
- D) `wal_level` must be set to `minimal` AND a publication must be created on the source table.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `wal_level = replica` enables streaming replication but does not write the additional logical decoding information needed for row-level CDC; logical replication requires `wal_level = logical`.
  - C) SSL is a security configuration that operates independently of WAL level; enabling SSL is not a prerequisite for logical replication.
  - D) `wal_level = minimal` writes the absolute minimum WAL and does not support replication of any kind; a publication cannot function without `wal_level = logical`.

---

### Question 16 (5 points)

Which `pg_stat_bgwriter` metric most directly indicates that the `checkpoint_completion_target` should be increased?

- A) `buffers_checkpoint` is high relative to `buffers_clean`, indicating most dirty buffers are flushed during checkpoint spikes rather than being spread out by the background writer.
- B) `checkpoints_req` is greater than `checkpoints_timed`, indicating WAL-forced checkpoints are occurring more often than scheduled ones.
- C) `buffers_alloc` is very high, indicating the shared buffer pool is too small.
- D) `maxwritten_clean` is greater than zero, indicating the background writer is being throttled.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `buffers_checkpoint` vs `buffers_clean` indicates whether dirty buffer flushing is dominated by checkpoints or background writing, but the specific indicator for `checkpoint_completion_target` adjustment is the checkpoint frequency pattern.
  - C) A high `buffers_alloc` indicates that new buffer frames are frequently needed, suggesting shared_buffers may be undersized; this is not directly related to `checkpoint_completion_target`.
  - D) `maxwritten_clean > 0` means the background writer hit its `bgwriter_lru_maxpages` limit and stopped; this points to tuning `bgwriter_lru_maxpages`, not `checkpoint_completion_target`.

---

### Question 17 (5 points)

A DBA runs `VACUUM FREEZE ANALYZE orders;` on a heavily updated table. What does the FREEZE option add beyond what a standard VACUUM provides?

- A) It advances the `relfrozenxid` of the table by marking all visible tuples as frozen, preventing transaction ID wraparound for those tuples.
- B) It locks the table exclusively to prevent concurrent reads while reclaiming dead tuples.
- C) It rebuilds all indexes on the table to eliminate fragmentation caused by deleted rows.
- D) It writes all dirty buffers for the table to disk, ensuring durability before VACUUM completes.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Standard VACUUM (including VACUUM FREEZE) does not acquire an exclusive lock; it operates concurrently with reads and most writes; VACUUM FULL is the variant that requires an exclusive lock.
  - C) Index rebuilding is performed by REINDEX, not VACUUM; VACUUM can remove index entries for dead tuples but does not rebuild index structures.
  - D) WAL ensures durability independently of VACUUM; VACUUM does not have a special disk-flush step at completion.

---

### Question 18 (5 points)

A PostgreSQL role `reporting_user` needs to SELECT from all existing and future tables in the `analytics` schema. Which grant correctly covers future tables as well as existing ones?

- A) `GRANT SELECT ON ALL TABLES IN SCHEMA analytics TO reporting_user;` followed by `ALTER DEFAULT PRIVILEGES IN SCHEMA analytics GRANT SELECT ON TABLES TO reporting_user;`
- B) `GRANT SELECT ON SCHEMA analytics TO reporting_user;`
- C) `GRANT ALL ON SCHEMA analytics TO reporting_user;`
- D) `GRANT SELECT ON analytics.* TO reporting_user;`

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `GRANT SELECT ON SCHEMA` grants USAGE on the schema (the ability to access objects within it by name), not SELECT on the tables themselves; a separate table-level grant is still required.
  - C) `GRANT ALL ON SCHEMA` grants CREATE and USAGE on the schema, not SELECT on existing or future tables within it.
  - D) `GRANT SELECT ON analytics.*` is not valid PostgreSQL syntax; PostgreSQL does not support wildcard table references in GRANT statements.

---

### Question 19 (5 points)

A `pg_hba.conf` entry reads: `host all all 0.0.0.0/0 trust`. What security risk does this create?

- A) Any client from any IP address can connect to any database as any user without providing a password or any credentials.
- B) All connections are encrypted with TLS but bypassed for localhost connections.
- C) The `trust` method forces all connections to use the default `postgres` superuser account.
- D) The `trust` method is equivalent to `md5` but is deprecated; the only risk is using an outdated hash algorithm.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) The `trust` method has nothing to do with encryption; `hostssl` entries control TLS; `trust` disables authentication entirely for matched connections.
  - C) `trust` does not force use of the `postgres` user; it allows any user name the client claims without verification, including regular users and superusers alike.
  - D) `trust` is fundamentally different from `md5`; `md5` requires a password hash; `trust` requires no credentials at all — it is not a deprecated hash method.

---

### Question 20 (5 points)

After installing `pg_stat_statements`, a DBA queries the view and finds a query with `mean_exec_time = 4200ms` and `calls = 15000`. What is the most appropriate next diagnostic step?

- A) Run `EXPLAIN ANALYZE` on the query to identify the execution plan node causing the high mean execution time.
- B) Increase `work_mem` for the database to reduce sort spills for all queries.
- C) Run `VACUUM ANALYZE` on all tables to refresh planner statistics.
- D) Restart PostgreSQL to clear the `pg_stat_statements` cache and confirm the high execution time persists.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Increasing `work_mem` globally may help queries with sort spills, but without first running EXPLAIN ANALYZE it is unknown whether sort spills are the cause; changing a global parameter without diagnosis is premature.
  - C) Running VACUUM ANALYZE may help if stale statistics are the issue, but the correct diagnostic first step is to examine the execution plan of the specific slow query before taking any action.
  - D) Restarting PostgreSQL to clear statistics is destructive to monitoring data and provides no diagnostic value; the high execution time will be confirmed by running the query, not by clearing historical data.

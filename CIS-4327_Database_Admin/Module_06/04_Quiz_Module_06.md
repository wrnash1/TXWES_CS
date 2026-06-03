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

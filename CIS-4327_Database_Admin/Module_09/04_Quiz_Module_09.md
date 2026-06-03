# Quiz: Module 09 — High Availability and Replication

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

Instructions: Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

An organization requires RPO = 0 for its transaction database. Which replication configuration achieves this?

- A) Asynchronous streaming replication to one standby
- B) Synchronous streaming replication with `synchronous_standby_names` set to the standby name
- C) Daily full backups with PITR enabled
- D) Asynchronous replication with a 1-second commit timeout

**Answer: B** — Synchronous replication (`synchronous_standby_names` configured) requires the standby to confirm receipt and write of WAL before the primary acknowledges the commit. This guarantees RPO = 0 — no committed transactions can be lost on failover. Asynchronous replication always has a potential lag period with RPO > 0.

---

### Question 2

What is the fundamental difference between Cloud SQL HA and traditional PostgreSQL streaming replication to a hot standby?

- A) Cloud SQL HA uses asynchronous WAL streaming; streaming replication is synchronous.
- B) Cloud SQL HA uses regional persistent disk replication at the storage layer; the standby does not independently maintain a WAL stream.
- C) Cloud SQL HA supports reads from the standby; streaming replication standbys are read-only.
- D) Cloud SQL HA has an RTO of 0 seconds; streaming replication has an RTO of several minutes.

**Answer: B** — Cloud SQL HA replicates at the storage layer using regional persistent disk. Both the primary and standby mount the same underlying disk. There is no WAL streaming between the primary and standby VMs. In contrast, PostgreSQL streaming replication ships WAL from primary to standby which applies it independently.

---

### Question 3

You are monitoring a PostgreSQL streaming replication setup and observe a standby with `pg_is_in_recovery() = true`. What does this indicate?

- A) The standby is recovering from a crash and is unavailable.
- B) The standby is operating normally as a read-only replica, continuously applying WAL from the primary.
- C) The standby has been promoted to primary.
- D) The standby has lost its connection to the primary and is in error state.

**Answer: B** — `pg_is_in_recovery() = true` is the normal state for a PostgreSQL standby that is actively receiving and replaying WAL. It is not an error condition. When a standby is promoted to primary, `pg_is_in_recovery()` returns `false`.

---

### Question 4

A PostgreSQL replication slot called `standby_slot` has `active = false` and its retained WAL has grown to 80 GB. The standby that used this slot was decommissioned. What is the correct action?

- A) Wait for autovacuum to clean the slot.
- B) Run `VACUUM FREEZE` to reclaim the WAL space.
- C) Drop the slot with `SELECT pg_drop_replication_slot('standby_slot');`
- D) Restart PostgreSQL to force slot cleanup.

**Answer: C** — An inactive replication slot retains WAL indefinitely, which can fill the disk and crash the primary. Since the standby is decommissioned, the slot serves no purpose and must be dropped explicitly. There is no automatic cleanup; PostgreSQL deliberately retains WAL to protect the slot's consumer.

---

### Question 5

After a Cloud SQL HA failover, your application reports that some connections are failing but new connections work. What is the most likely cause and fix?

- A) The database was corrupted during failover. Restore from backup.
- B) Existing connections from before the failover were terminated and need to be re-established. The application connection pool must retry and reconnect.
- C) The Cloud SQL instance is in a different zone and requires a new connection string.
- D) The database flags were reset during failover. Reapply the database flags.

**Answer: B** — During Cloud SQL failover, active connections to the old primary are terminated. The connection string (using the instance connection name) is still valid and DNS resolves to the new primary. Applications must handle connection drops gracefully with retry logic and connection pool health checks (e.g., `pool_pre_ping=True` in SQLAlchemy).

---

### Question 6

MySQL Group Replication is configured in single-primary mode with three members. The primary fails. What happens?

- A) All three members become read-only until an operator manually promotes one.
- B) The group detects the failure via Paxos consensus, elects a new primary automatically, and resumes accepting writes.
- C) The group waits 60 seconds then promotes the member with the highest server_id.
- D) All write operations are lost because there is no standby.

**Answer: B** — Group Replication uses the Paxos consensus protocol to detect primary failure and automatically elect a new primary from the remaining members. This requires no operator intervention and happens within seconds.

---

### Question 7

Which PostgreSQL configuration parameter enables a standby to serve read-only queries to clients while continuously applying WAL from the primary?

- A) `wal_level = logical`
- B) `max_wal_senders = 5`
- C) `hot_standby = on`
- D) `synchronous_commit = remote_apply`

**Answer: C** — `hot_standby = on` enables a PostgreSQL standby in recovery mode to accept read-only connections from clients while continuously replaying WAL. Without this setting, the standby refuses all client connections.

---

### Question 8

An application uses SQLAlchemy to connect to a Cloud SQL HA instance. After a failover, some queries fail immediately. Which connection pool setting would detect stale connections before the application attempts to use them?

- A) `pool_size=10`
- B) `pool_pre_ping=True`
- C) `pool_recycle=3600`
- D) `max_overflow=20`

**Answer: B** — `pool_pre_ping=True` instructs SQLAlchemy to issue a `SELECT 1` (or equivalent) before returning a connection from the pool to the application. If the connection is dead (as it would be after a failover), the pool discards it and opens a new connection, preventing the application from receiving a stale connection.

---

### Question 9

What does `synchronous_standby_names = 'FIRST 1 (standby1, standby2)'` mean in a PostgreSQL primary configuration?

- A) Both standby1 and standby2 must confirm before each commit.
- B) The primary waits for acknowledgment from the first of standby1 or standby2 to respond before completing each commit.
- C) All commits are sent asynchronously; standby1 and standby2 are only for failover.
- D) standby1 is the primary standby; standby2 is used only when standby1 is unavailable.

**Answer: B** — `FIRST 1 (standby1, standby2)` means the primary requires acknowledgment from exactly one of the listed standbys before committing. The first one to respond satisfies the requirement. This allows the second to act as a failover for the synchronous role if the first disconnects.

---

### Question 10

A Cloud SQL for PostgreSQL read replica consistently shows `replication_lag = 15 seconds` during business hours. What is the most likely cause?

- A) The replica is in a different region and geographic latency causes lag.
- B) The replica is receiving more write traffic than the primary.
- C) The replica's compute tier is undersized and cannot apply WAL fast enough to keep up with the primary's write rate.
- D) Cloud SQL replication has a built-in 15-second delay for consistency.

**Answer: C** — Sustained replica lag is most commonly caused by the replica's CPU or I/O being insufficient to apply WAL as fast as the primary generates it. The fix is to scale up the replica's tier. Geographic latency (option A) adds latency but does not cause sustained accumulating lag unless the bandwidth is saturated.

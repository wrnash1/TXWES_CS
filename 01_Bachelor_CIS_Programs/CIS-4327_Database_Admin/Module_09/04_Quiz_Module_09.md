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

---

### Question 11 (5 points)

A PostgreSQL standby has `recovery_min_apply_delay = 60min` configured. What is the primary operational purpose of this delayed standby?

A) To reduce network bandwidth by batching WAL before applying it.
B) To provide a rolling recovery window, allowing a DBA to promote the standby and recover from accidental data changes before they are applied.
C) To increase write throughput on the primary by reducing synchronous acknowledgment overhead.
D) To enable the standby to serve read queries with a one-hour snapshot consistency window.

**Correct Answer:** B

**Distractor Analysis:**

- A) WAL is still received in real time; the delay is in application, not transmission, so bandwidth is not reduced.
- C) A delayed standby does not affect the primary's commit path or synchronous overhead; those are governed by `synchronous_commit`.
- D) The standby with a delayed apply does not expose a snapshot view to clients; it is still in recovery mode and applies changes at a fixed offset behind real time, not on a per-query basis.

---

### Question 12 (5 points)

Which view should a DBA query on the PostgreSQL primary to determine how many bytes of WAL each connected standby is lagging behind the primary?

A) `pg_stat_activity`
B) `pg_stat_replication`
C) `pg_replication_slots`
D) `pg_stat_bgwriter`

**Correct Answer:** B

**Distractor Analysis:**

- A) `pg_stat_activity` shows active backend sessions and their SQL statements; it does not contain replication state or WAL position information.
- C) `pg_replication_slots` shows slot metadata and retained WAL per slot but does not show connected standby WAL apply lag in real time.
- D) `pg_stat_bgwriter` shows checkpoint and buffer write statistics; it has no replication lag data.

---

### Question 13 (5 points)

In a MySQL Group Replication cluster, all tables must satisfy which requirement for Group Replication to accept them?

A) All tables must use the InnoDB storage engine and have a defined primary key.
B) All tables must have at least one index in addition to the primary key.
C) All tables must use the MyISAM engine for Group Replication's write-set tracking.
D) All tables must be partitioned by hash for distributed write coordination.

**Correct Answer:** A

**Distractor Analysis:**

- B) Additional indexes are not required by Group Replication; only a primary key is mandatory for write-set conflict detection.
- C) Group Replication requires InnoDB, not MyISAM; MyISAM does not support transactions and is incompatible with Group Replication's write-set protocol.
- D) Hash partitioning is not required; Group Replication uses write-set certification based on primary keys, not table partitioning.

---

### Question 14 (5 points)

What is the split-brain problem in a high-availability database cluster, and which mechanism does Cloud SQL HA use to prevent it?

A) Two nodes both accept writes simultaneously after losing contact; Cloud SQL HA uses regional persistent disk (shared storage) so only one node can be active at a time.
B) Two nodes disagree on the current schema version; Cloud SQL HA uses DDL locking to serialize schema changes.
C) Two nodes both enter read-only mode after a network partition; Cloud SQL HA promotes a new primary automatically via Paxos.
D) Two replicas diverge because they are in different regions; Cloud SQL HA uses GTID to reconcile log positions.

**Correct Answer:** A

**Distractor Analysis:**

- B) Schema version conflict is not split-brain; DDL locking is unrelated to HA architecture.
- C) Read-only mode is the opposite of split-brain (which involves both nodes accepting writes); and Cloud SQL HA uses storage-layer fencing, not Paxos.
- D) Regional divergence could be a replication lag issue; GTIDs are a MySQL mechanism not used by Cloud SQL HA's storage-layer architecture.

---

### Question 15 (5 points)

A DBA is configuring Patroni for PostgreSQL HA. Which distributed configuration store (DCS) does Patroni use for leader election?

A) etcd, Consul, or ZooKeeper
B) Redis
C) Cloud Spanner
D) PostgreSQL itself via a shared database lock

**Correct Answer:** A

**Distractor Analysis:**

- B) Redis is not a supported DCS for Patroni leader election; Redis does not provide the distributed consensus guarantees required for safe leader election.
- C) Cloud Spanner is not a supported Patroni DCS back end; it is a database service, not a coordination service.
- D) PostgreSQL cannot be used as its own DCS for leader election — a database that is down cannot participate in its own failover decision.

---

### Question 16 (5 points)

After configuring MySQL semi-synchronous replication with `rpl_semi_sync_source_timeout = 1000`, the primary loses contact with all replicas during a network partition. What happens to write transactions on the primary?

A) The primary falls back to asynchronous replication after the 1-second timeout and continues accepting writes.
B) The primary refuses all writes until at least one replica reconnects.
C) The primary crashes and requires a manual restart.
D) The primary promotes the replica automatically via Paxos and demotes itself.

**Correct Answer:** A

**Distractor Analysis:**

- B) Refusing writes indefinitely is not semi-synchronous behavior; that would require a fully synchronous configuration with no timeout fallback.
- C) MySQL does not crash on semi-sync timeout; the timeout exists specifically to allow graceful fallback to async, not to fail the instance.
- D) Semi-synchronous replication has no automatic failover or promotion mechanism; automatic failover requires Group Replication or an external HA tool.

---

### Question 17 (5 points)

A DBA wants to implement logical replication in PostgreSQL to stream changes from one database to a downstream analytics system. What is the minimum `wal_level` setting required on the source?

A) `logical`
B) `replica`
C) `minimal`
D) `archive`

**Correct Answer:** A

**Distractor Analysis:**

- B) `wal_level = replica` is sufficient for physical streaming replication but does not include the additional column-level change data required for logical decoding.
- C) `wal_level = minimal` only logs the minimum needed for crash recovery; it does not support streaming replication or logical decoding.
- D) `archive` is not a valid PostgreSQL `wal_level` value; valid options are `minimal`, `replica`, and `logical`.

---

### Question 18 (5 points)

An organization needs its Cloud SQL for PostgreSQL instance to serve read traffic from a replica in the same region while ensuring automatic failover of the primary in case of zone failure. Which combination of Cloud SQL features best satisfies both requirements?

A) Enable HA on the primary instance and create a separate read replica in the same region.
B) Create two HA instances in two zones and configure application-level load balancing between them.
C) Enable HA with a cross-region replica as the standby and a local read replica.
D) Create only a read replica — Cloud SQL automatically promotes it during primary zone failures.

**Correct Answer:** A

**Distractor Analysis:**

- B) Cloud SQL HA manages standby as a storage-layer replica, not as a second independently configured HA instance; this architecture is not supported and would not provide correct automatic failover.
- C) Cloud SQL HA uses a regional standby in the same region; cross-region replicas are read replicas, not HA standbys.
- D) A read replica is not automatically promoted during a zone failure; automatic promotion is the function of the HA standby, not a read replica.

---

### Question 19 (5 points)

Which PostgreSQL command drops a replication slot named `cdc_slot` that is no longer in use?

A) `SELECT pg_drop_replication_slot('cdc_slot');`
B) `DROP REPLICATION SLOT cdc_slot;`
C) `ALTER SYSTEM REMOVE SLOT cdc_slot;`
D) `DELETE FROM pg_replication_slots WHERE slot_name = 'cdc_slot';`

**Correct Answer:** A

**Distractor Analysis:**

- B) There is no `DROP REPLICATION SLOT` DDL syntax in standard PostgreSQL; slot management is performed via system functions, not DDL statements.
- C) `ALTER SYSTEM` is used to modify `postgresql.conf` parameters; it has no syntax for removing replication slots.
- D) `pg_replication_slots` is a system catalog view, not a writable table; direct DELETE is not permitted and would raise an error.

---

### Question 20 (5 points)

A DBA observes the following output from `pg_stat_replication` on the primary:

```
state       | streaming
sent_lsn    | 0/5A000000
replay_lsn  | 0/58000000
```

What does this LSN difference indicate?

A) The standby has not yet applied approximately 32 MB of WAL that the primary has already sent.
B) The standby is 2 transactions behind the primary.
C) The primary has a corrupted WAL segment between LSN 0/58 and 0/5A.
D) The standby is fully synchronized; the difference is due to WAL segment header padding.

**Correct Answer:** A

**Distractor Analysis:**

- B) LSN differences represent byte positions in the WAL stream, not transaction counts; you cannot determine transaction count from LSN difference alone.
- C) A non-zero LSN difference is a normal condition during replication lag; it does not indicate corruption, which would produce error messages rather than valid LSN positions.
- D) WAL segment header padding is a fixed small overhead (typically kilobytes), not a 32 MB difference; a 32 MB gap indicates genuine lag.

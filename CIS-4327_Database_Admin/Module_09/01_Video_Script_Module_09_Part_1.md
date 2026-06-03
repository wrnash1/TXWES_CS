# Video Script: Module 09 — High Availability and Replication (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back to CIS-4327. I am Professor Nash, and this is Module 09: High Availability and Replication.

In Module 08 we covered backup and recovery — what to do after a failure. In Module 09 we cover how to minimize or eliminate unplanned downtime in the first place through replication and high availability architectures.

Part 1 covers the conceptual foundation: synchronous versus asynchronous replication, PostgreSQL streaming replication architecture, and MySQL Group Replication. Part 2 covers Cloud SQL HA internals, connection strings for HA, and practical configuration commands.

---

## Section 1 — Why Replication?

A single database instance is a single point of failure. Any hardware failure, OS crash, or even a routine maintenance operation causes downtime. Replication solves this by maintaining one or more copies of the database on separate hardware.

Replication serves two purposes:

1. **High availability** — automatic failover when the primary fails, reducing unplanned downtime
2. **Read scalability** — distributing read queries across multiple replica instances, increasing total query throughput

These two goals sometimes require different configurations. A high-availability standby typically runs synchronous replication (no data loss on failover) but may not accept queries. A read replica typically runs asynchronous replication (accepts queries but may lag slightly behind the primary).

---

## Section 2 — Synchronous vs Asynchronous Replication

This distinction is one of the most tested concepts on the Google Cloud Database Engineer exam.

### Synchronous Replication

In synchronous replication, a transaction on the primary is not committed to the client until **at least one replica has confirmed receipt and write of the data**.

The flow:

1. Client sends `COMMIT`
2. Primary writes to its local WAL or binary log
3. Primary sends the WAL record to the standby
4. **Standby writes and acknowledges**
5. Primary sends commit acknowledgment to the client

Characteristics:

- **RPO = 0** — no data loss on failover; the standby has every committed transaction
- **Higher write latency** — commit waits for network round trip to standby
- **Appropriate for:** financial systems, payment databases, any system where data loss is unacceptable

### Asynchronous Replication

In asynchronous replication, the primary commits to the client as soon as it writes locally. It then ships the changes to replicas in the background.

The flow:

1. Client sends `COMMIT`
2. Primary writes to local WAL
3. **Primary immediately sends commit acknowledgment to client**
4. Primary ships WAL to replica(s) in the background

Characteristics:

- **RPO > 0** — replica may lag; if primary fails before the replica catches up, some committed transactions are lost
- **Lower write latency** — no waiting for replica acknowledgment
- **Appropriate for:** read replicas, reporting replicas, geographically distributed replicas where latency makes synchronous impractical

### Semi-Synchronous Replication

MySQL also offers semi-synchronous replication. The primary waits for at least one replica to acknowledge receipt of the WAL/binlog, but does not wait for the replica to apply it. This provides a middle ground — nearly zero data loss with lower latency than full synchronous.

---

## Section 3 — PostgreSQL Streaming Replication

PostgreSQL's built-in replication is called **streaming replication**. The primary streams WAL records directly to one or more standbys in near-real-time. Standbys apply WAL records continuously, maintaining a state close to the primary.

### Replication Roles

- **Primary** — accepts reads and writes; streams WAL
- **Hot standby** — continuously replays WAL; can accept read-only queries; promotes automatically or manually if primary fails
- **Warm standby** — continuously replays WAL; does not accept queries; less common

### Configuring Streaming Replication on the Primary

In `postgresql.conf` on the primary:

```ini
wal_level = replica
max_wal_senders = 5
wal_keep_size = 1GB
hot_standby = on
synchronous_standby_names = ''    # empty = async; set to 'standby1' for sync
```

In `pg_hba.conf` on the primary:

```text
host  replication  replicator  10.0.2.0/24  scram-sha-256
```

Create the replication user:

```sql
CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'ReplPass!';
```

### Configuring the Standby

Take a base backup from the primary:

```bash
pg_basebackup -h 10.0.1.10 -U replicator -D /var/lib/postgresql/15/main \
  --wal-method=stream --checkpoint=fast --progress
```

Create the `standby.signal` file to indicate this instance is a standby:

```bash
touch /var/lib/postgresql/15/main/standby.signal
```

Add to `postgresql.conf` on the standby:

```ini
primary_conninfo = 'host=10.0.1.10 port=5432 user=replicator password=ReplPass! application_name=standby1'
hot_standby = on
```

Start the standby:

```bash
sudo systemctl start postgresql
```

### Monitoring Replication

On the primary:

```sql
SELECT client_addr, application_name, state,
       sent_lsn, write_lsn, flush_lsn, replay_lsn,
       (sent_lsn - replay_lsn) AS replication_lag_bytes
FROM pg_stat_replication;
```

`replication_lag_bytes` shows how far behind each standby is in terms of WAL bytes. You can convert to time using:

```sql
SELECT now() - pg_last_xact_replay_timestamp() AS replication_delay;
```

Run this on the standby.

### Synchronous Replication in PostgreSQL

To require synchronous acknowledgment from a specific standby, set on the primary:

```ini
synchronous_standby_names = 'FIRST 1 (standby1, standby2)'
```

This requires at least one of `standby1` or `standby2` to acknowledge before commits complete. If neither standby is connected, the primary **hangs waiting** for acknowledgment. This is the safety-liveness tradeoff of synchronous replication.

---

## Section 4 — MySQL Group Replication

**MySQL Group Replication** (MGR) is MySQL's built-in high-availability solution introduced in MySQL 5.7. It enables a group of MySQL servers to automatically coordinate writes, handle member failures, and elect a new primary without external tooling.

### How Group Replication Works

Group Replication uses the **Paxos consensus protocol** to agree on the order of transactions before applying them. Every server in the group must reach consensus on a transaction before it is committed.

There are two modes:

- **Single-primary mode** (default) — one primary accepts writes; all others are read-only standbys. On primary failure, the group automatically elects a new primary.
- **Multi-primary mode** — all members accept writes; conflict detection handles concurrent writes to the same row.

For most OLTP applications, single-primary mode is the right choice.

### Group Replication vs Standard MySQL Replication

| Feature | Standard Replication | Group Replication |
|---|---|---|
| Failover | Manual or external tool | Automatic |
| Consensus | None | Paxos |
| Write scaling | No (single primary) | Yes (multi-primary) |
| Conflict detection | No | Yes (multi-primary) |
| Data loss on failover | Possible (async) | Minimal (Paxos-certified) |
| Complexity | Simple | Moderate |

### Configuring Group Replication

In `my.cnf` for each group member:

```ini
[mysqld]
server_id = 1                                    # unique per member
gtid_mode = ON
enforce_gtid_consistency = ON
plugin_load_add = group_replication.so
group_replication_group_name = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
group_replication_local_address = "10.0.1.10:33061"
group_replication_group_seeds = "10.0.1.10:33061,10.0.1.11:33061,10.0.1.12:33061"
group_replication_bootstrap_group = OFF          # ON only for initial bootstrap
group_replication_single_primary_mode = ON
group_replication_enforce_update_everywhere_checks = OFF
```

Bootstrap the first node only:

```sql
SET GLOBAL group_replication_bootstrap_group = ON;
START GROUP_REPLICATION;
SET GLOBAL group_replication_bootstrap_group = OFF;
```

Add subsequent nodes:

```sql
START GROUP_REPLICATION;
```

Monitor group membership:

```sql
SELECT * FROM performance_schema.replication_group_members;
```

---

## Section 5 — Failover Concepts

### Automatic Failover Requirements

For automatic failover to work, a system needs three components:

1. **Health monitoring** — detects when the primary is unavailable
2. **Promotion logic** — selects and promotes the best standby to primary
3. **DNS or connection update** — redirects client traffic to the new primary

For self-managed PostgreSQL, tools like **Patroni** (uses etcd or ZooKeeper for leader election) or **repmgr** provide automatic failover. For MySQL, **MySQL Router** with Group Replication provides automatic routing.

On Cloud SQL, Google manages all three automatically.

### Split-Brain Risk

When a primary appears to fail but is actually still running (due to a network partition), two servers may each believe they are the primary and accept writes simultaneously. This is called **split-brain** and can cause data divergence.

Solutions:

- **STONITH (Shoot The Other Node In The Head)** — forcibly powers down the suspected failed primary before promoting the standby
- **Quorum-based fencing** — require a majority vote (Paxos/Raft) before any node can become primary
- Cloud SQL's regional persistent disk architecture avoids split-brain by using a shared underlying disk

---

## Section 6 — Exam Summary

Key concepts for Part 1:

- Synchronous replication: RPO = 0, higher latency, waits for standby ack before commit
- Asynchronous replication: RPO > 0, lower latency, ships WAL after commit
- PostgreSQL streaming replication requires `wal_level = replica`, `max_wal_senders`, and replication user in pg_hba.conf
- `synchronous_standby_names` converts async to sync but risks primary stall if standby disconnects
- Group Replication uses Paxos for consensus; single-primary mode is standard
- `pg_stat_replication` on the primary shows standby lag
- Split-brain risk requires fencing or shared-disk architecture

---

## Closing

That wraps up Part 1 of Module 09. You understand the theory — synchronous vs asynchronous, PostgreSQL streaming replication, and MySQL Group Replication.

In Part 2 we focus on Cloud SQL HA architecture, connection strings for HA scenarios, and practical monitoring queries. See you there.

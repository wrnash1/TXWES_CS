# Reading Guide: Module 09 — High Availability and Replication

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4327 &BULL; DATABASE ADMINISTRATION & SQL OPTIMIZATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Overview

This reading guide covers the replication and high availability concepts tested on the Google Cloud Professional Database Engineer exam. Replication and HA appear in many exam questions, often embedded in larger architecture scenarios. A solid understanding of how Cloud SQL HA differs from self-managed streaming replication is essential.

---

## Section 1 — Replication Fundamentals

### 1.1 Replication Vocabulary

| Term | Definition |
|---|---|
| Primary / Source | The authoritative read-write database instance |
| Standby / Replica | A copy that receives and applies changes from the primary |
| WAL / Binary log | The change log used to ship changes from primary to replica |
| LSN | Log Sequence Number — PostgreSQL's position marker in the WAL |
| GTID | Global Transaction Identifier — MySQL's transaction ordering mechanism |
| Replication lag | How far behind (in bytes or time) a replica is relative to the primary |
| Failover | Promoting a standby to become the new primary |
| Switchover | Planned primary change with graceful handoff |

### 1.2 Replication Consistency Levels

Beyond synchronous/asynchronous, PostgreSQL offers fine-grained control via `synchronous_commit`:

| Setting | Behavior | Durability | Performance |
|---|---|---|---|
| `off` | Primary commits without writing WAL to disk | Lowest | Fastest |
| `local` | Primary commits after WAL written to local disk | Good for primary | Fast |
| `remote_write` | Standby acknowledges WAL written to OS buffer | Very good | Moderate |
| `remote_apply` | Standby acknowledges WAL applied to its data | Near sync | Slower |
| `on` (default) | Primary commits after WAL written to local disk | Local only | Normal |

Setting `synchronous_commit = remote_apply` on the primary means the standby has already applied the change before the client receives commit confirmation. This enables truly consistent reads from the standby.

---

## Section 2 — PostgreSQL Streaming Replication Reference

### 2.1 Required Configuration

Primary (`postgresql.conf`):

```ini
wal_level = replica                 # minimum for streaming replication
max_wal_senders = 5                 # one per standby + extras
wal_keep_size = 1GB                 # retain WAL for lagging standbys
hot_standby = on                    # allow read queries on standbys
```

Primary (`pg_hba.conf`):

```text
host  replication  replicator  standby-ip/32  scram-sha-256
```

Standby (`postgresql.conf`):

```ini
primary_conninfo = 'host=primary-ip user=replicator password=xxx application_name=standby1'
hot_standby = on
recovery_min_apply_delay = 0        # set to e.g. 10min for delayed standby
```

Standby trigger file:

```bash
touch $PGDATA/standby.signal
```

### 2.2 Promotion

To promote a standby to primary manually:

```bash
# PostgreSQL 12+
pg_ctl promote -D /var/lib/postgresql/15/main
# or
touch /var/lib/postgresql/15/main/promote.signal
```

After promotion, the standby.signal file is removed and the server transitions to primary mode.

### 2.3 Cascading Replication

A standby can itself stream WAL to another standby (cascade):

```ini
# On the second-level standby:
primary_conninfo = 'host=first-standby-ip user=replicator ...'
```

This offloads WAL streaming work from the primary for large-scale replica deployments.

### 2.4 Delayed Standby

A delayed standby applies WAL with a configured delay — for example, 1 hour. This provides a rolling window to catch accidental deletes before they propagate:

```ini
recovery_min_apply_delay = 60min
```

A delayed standby is not a substitute for PITR but provides a fast-recovery option for recent accidents.

---

## Section 3 — MySQL Replication Reference

### 3.1 Standard Replication Setup

Source (`my.cnf`):

```ini
[mysqld]
server_id = 1
log_bin = /var/log/mysql/mysql-bin
binlog_format = ROW
expire_logs_days = 7
gtid_mode = ON
enforce_gtid_consistency = ON
```

Replica (`my.cnf`):

```ini
[mysqld]
server_id = 2
read_only = ON
super_read_only = ON
gtid_mode = ON
enforce_gtid_consistency = ON
```

Start replication on the replica:

```sql
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='10.0.1.10',
  SOURCE_USER='replicator',
  SOURCE_PASSWORD='ReplPass!',
  SOURCE_AUTO_POSITION=1;

START REPLICA;
SHOW REPLICA STATUS\G
```

`SOURCE_AUTO_POSITION=1` uses GTIDs for positioning, eliminating the need to specify a binlog file and position manually.

### 3.2 Group Replication Single-Primary Mode

Group Replication is suitable when automatic failover without external tooling is required and the workload fits single-primary constraints.

Prerequisites for all members:

- `gtid_mode = ON`
- `enforce_gtid_consistency = ON`
- `log_bin = ON`
- `binlog_format = ROW`
- Unique `server_id` per member
- Group Replication plugin loaded

Limitations in single-primary mode:

- Only the primary accepts writes
- DDL on large tables can block the group
- Tables must have a primary key (Group Replication rejects tables without a PK)
- Maximum recommended group size is 9 members

### 3.3 MySQL Semi-Synchronous Replication

Semi-synchronous is available as a plugin and provides a middle ground for RPO:

```sql
-- On source
INSTALL PLUGIN rpl_semi_sync_source SONAME 'semisync_source.so';
SET GLOBAL rpl_semi_sync_source_enabled = 1;
SET GLOBAL rpl_semi_sync_source_timeout = 1000;   -- 1 second timeout before fallback to async

-- On replica
INSTALL PLUGIN rpl_semi_sync_replica SONAME 'semisync_replica.so';
SET GLOBAL rpl_semi_sync_replica_enabled = 1;
```

If no replica acknowledges within the timeout, MySQL falls back to asynchronous replication automatically.

---

## Section 4 — Cloud SQL HA vs Self-Managed Replication

### 4.1 Architecture Comparison

| Feature | Cloud SQL HA | Self-Managed PostgreSQL Streaming |
|---|---|---|
| Replication mechanism | Regional persistent disk (storage-layer) | WAL streaming (database-layer) |
| Standby serves reads | No | Yes (hot standby) |
| Failover trigger | Automatic (health check) | Manual or via Patroni/repmgr |
| Failover time | 60–120 seconds | Depends on tool; 10–60 seconds typical |
| RPO | Near zero (shared disk) | Zero (sync) or >0 (async) |
| Setup complexity | None (managed) | Significant |
| Split-brain protection | Built-in (shared disk) | Requires fencing (STONITH, DCS) |

### 4.2 When to Use Each

Use Cloud SQL HA when:

- Fully managed infrastructure is required
- The team does not have capacity to operate Patroni + etcd
- Standard failover SLA (60–120 seconds) is acceptable

Use self-managed streaming replication when:

- Read replicas need to serve queries (Cloud SQL HA standby cannot)
- Delayed standby is needed
- Cascading replication is required
- The workload runs on Compute Engine for other reasons

---

## Section 5 — PostgreSQL Replication Slots

### 5.1 Physical vs Logical Slots

| Type | Use | Retains WAL |
|---|---|---|
| Physical | Streaming replication standbys | Until standby consumes |
| Logical | Logical replication, CDC (Debezium) | Until consumer confirms |

### 5.2 Monitoring Slot Lag

```sql
SELECT slot_name, active, restart_lsn,
       pg_size_pretty(
         pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)
       ) AS retained_wal
FROM pg_replication_slots;
```

### 5.3 Slot Risk Alert

If `retained_wal` for an inactive slot exceeds your disk's free space, the primary will run out of WAL storage and crash. Set a Cloud Monitoring alert or cron job to check this daily.

---

## Section 6 — Patroni High Availability Architecture

### 6.1 Component Overview

```text
┌──────────┐    ┌──────────┐    ┌──────────┐
│ pg-node1 │    │ pg-node2 │    │ pg-node3 │
│ Primary  │    │ Standby  │    │ Standby  │
│ Patroni  │    │ Patroni  │    │ Patroni  │
└────┬─────┘    └────┬─────┘    └────┬─────┘
     └───────────────┼───────────────┘
                     │
              ┌──────┴──────┐
              │  etcd Cluster │
              │ (3 or 5 nodes)│
              └─────────────┘
```

### 6.2 Key Patroni Operations

```bash
# View cluster state
patronictl -c /etc/patroni.yml list

# Trigger manual switchover (graceful)
patronictl -c /etc/patroni.yml switchover --master pg-node1 --candidate pg-node2

# Pause automatic failover (for maintenance)
patronictl -c /etc/patroni.yml pause

# Resume automatic failover
patronictl -c /etc/patroni.yml resume

# Edit cluster configuration live
patronictl -c /etc/patroni.yml edit-config
```

---

## Section 7 — Key Terms

| Term | Definition |
|---|---|
| Streaming replication | PostgreSQL's WAL-based replication protocol |
| Group Replication | MySQL's Paxos-based multi-master HA solution |
| Patroni | Self-managed PostgreSQL HA tool using etcd/Consul |
| Replication slot | PostgreSQL mechanism to retain WAL for a specific consumer |
| Regional persistent disk | Google's storage-layer synchronous replication used by Cloud SQL HA |
| Split-brain | Two nodes both believing they are primary; causes data divergence |
| STONITH | Fencing technique to forcibly terminate the suspected failed node |
| `pg_stat_replication` | Primary-side view showing all connected replication clients |
| `hot_standby` | PostgreSQL parameter enabling read queries on standbys |

---

## Study Questions

1. What is the fundamental architectural difference between Cloud SQL HA and PostgreSQL streaming replication to a hot standby?

2. Why can the Cloud SQL HA standby not serve read queries, while a PostgreSQL hot standby can?

3. Explain the split-brain problem and describe two mechanisms that prevent it.

4. What is the risk of leaving an inactive PostgreSQL replication slot in place indefinitely?

5. A MySQL Group Replication group has three members. The primary fails. Describe what happens next automatically.

6. What does `synchronous_commit = remote_apply` guarantee that `synchronous_commit = on` does not?

---

## Certification Exam Checklist

- [ ] Synchronous replication RPO = 0; asynchronous RPO > 0
- [ ] Cloud SQL HA uses regional persistent disk; standby does not serve reads
- [ ] Cloud SQL HA failover: 60–120 seconds, DNS auto-updates
- [ ] pg_stat_replication query for monitoring streaming replication
- [ ] Replication slot risk: WAL accumulation if consumer goes offline
- [ ] Group Replication: Paxos, single-primary default, requires primary key on all tables
- [ ] Patroni: DCS-based leader election, HAProxy for connection routing
- [ ] Connection string must use instance name not IP for transparent HA failover
- [ ] `synchronous_standby_names` controls which standbys must ack before commit

---

## 9. Supplemental Resources

The following free, open-access resources support Module 09 topics:

**1. [PostgreSQL Documentation — High Availability, Load Balancing, and Replication](https://www.postgresql.org/docs/current/high-availability.html)**
Covers streaming replication configuration, replication slots, hot standby, synchronous commit levels, and Patroni integration patterns.

**2. [PostgreSQL Documentation — Monitoring Replication (pg_stat_replication)](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-VIEW)**
Reference for all columns in `pg_stat_replication` including LSN fields, lag bytes, and standby state values used in monitoring.

**3. [MySQL 8.0 Reference Manual — Group Replication](https://dev.mysql.com/doc/refman/8.0/en/group-replication.html)**
Complete reference for MySQL Group Replication, including single-primary mode, Paxos consensus, table requirements, and member management commands.

**4. [Google Cloud — Cloud SQL High Availability Overview](https://cloud.google.com/sql/docs/postgres/high-availability)**
Official documentation for Cloud SQL HA architecture, failover behavior, regional persistent disk replication, and RTO/RPO characteristics.

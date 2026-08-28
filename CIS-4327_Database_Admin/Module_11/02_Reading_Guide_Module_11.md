# Reading Guide: Module 11 — Cloud Spanner and Distributed Databases

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

This reading guide covers Cloud Spanner — Google's globally distributed, strongly consistent relational database. Cloud Spanner is among the most unique and heavily tested services on the Google Cloud Professional Database Engineer exam. Understanding both its architecture and when to choose it over Cloud SQL is essential.

---

## Section 1 — Distributed Database Theory

### 1.1 CAP Theorem

Eric Brewer's CAP theorem states that a distributed system can guarantee at most two of:

- **Consistency (C)** — every read receives the most recent write
- **Availability (A)** — every request receives a response
- **Partition Tolerance (P)** — the system continues operating despite network partitions

Because network partitions are unavoidable in real distributed systems, the practical choice is between CA (no partition tolerance — impossible for truly distributed systems), CP (sacrifice availability during partitions), and AP (sacrifice consistency during partitions).

Cloud Spanner is designed to be CP with very high practical availability by using TrueTime to minimize the window during which it must sacrifice availability to maintain consistency.

### 1.2 Consistency Models

| Model | Description | Example |
|---|---|---|
| Eventual consistency | Reads may return stale data; converges eventually | DynamoDB, Cassandra (default) |
| Read-your-writes | A client always reads its own writes | Many session-based systems |
| Monotonic reads | No client ever reads data older than what it already read | Read-only replicas with routing |
| Linearizability | Operations appear instantaneous; respects real-time order | Single-node databases |
| Serializability | Transactions appear to execute serially | Traditional ACID databases |
| External consistency | Serializability that also respects real-world time ordering | Cloud Spanner |

External consistency is stronger than serializability. It is the strongest consistency model available and is what Spanner guarantees.

### 1.3 PACELC Model

An extension of CAP, the PACELC model also considers the latency-consistency tradeoff even when there is no partition. Cloud Spanner accepts higher write latency (commit wait) to maintain external consistency even under normal (no-partition) operation.

---

## Section 2 — TrueTime Architecture

### 2.1 Hardware Infrastructure

Each Google datacenter has:

- GPS receivers synchronized to GPS satellite time
- Atomic clocks as a fallback when GPS signal is unavailable
- A TimeServer daemon that distributes time to all machines
- Uncertainty interval `ε` (epsilon) — typically 1–7 ms

### 2.2 TrueTime API

The TrueTime API provides:

- `TT.now()` — returns `{earliest, latest}` time interval
- `TT.after(t)` — returns `true` if `t` is definitely in the past
- `TT.before(t)` — returns `true` if `t` is definitely in the future

### 2.3 Commit Wait Mechanics

When a Spanner transaction commits:

1. The commit coordinator assigns a commit timestamp `s` such that `s > TT.now().latest`
2. The coordinator waits until `TT.now().earliest > s` — meaning `s` is now definitely in the past
3. Only then does the coordinator release the commit acknowledgment to the client

This brief wait (equal to the TrueTime uncertainty bound, typically 1–7 ms) guarantees that if transaction T1 commits before T2 starts in real-world time, every node in the system will see T1's timestamp as less than T2's. There is no ambiguity.

### 2.4 Why This Matters for Correctness

Without TrueTime (using NTP with 100 ms uncertainty), a transaction could be assigned a timestamp that is 100 ms in the future relative to another node's clock. That node might then process a subsequent transaction with an earlier timestamp, creating a causality inversion — T2 appears to have happened before T1 even though T1 completed first in real-world time.

---

## Section 3 — Paxos and Spanner Replication

### 3.1 Spanner Topology

A Spanner instance contains one or more **databases**. Each database's data is divided into **splits** (key ranges). Each split is managed by a **Paxos group** of replicas.

```text
Spanner Instance
└── Database: mydb
    └── Table: customers (split by customer_id ranges)
        ├── Split [a000... - m999...]: Paxos Group
        │   ├── Replica: us-central1-a (leader)
        │   ├── Replica: us-central1-b
        │   └── Replica: us-central1-c
        └── Split [n000... - z999...]: Paxos Group
            ├── Replica: us-central1-a
            ├── Replica: us-central1-b (leader)
            └── Replica: us-central1-c
```

### 3.2 Paxos Leader Election

Each Paxos group has one leader at a time. The leader:

- Coordinates all write operations for its splits
- Holds a lease that it must periodically renew
- Can be in any zone; Spanner places leaders near the geographic source of writes to reduce latency

If the leader fails to renew its lease, the remaining replicas elect a new leader via the Paxos protocol. This does not require a quorum vote of the whole database — only the affected group's replicas.

### 3.3 Quorum and Durability

For a 5-replica group (standard), writes must be acknowledged by 3 replicas (majority quorum) before commit. This means:

- The database tolerates 2 simultaneous replica failures
- A region-level failure in a multi-region config loses at most 2 replicas (assuming 3-region spread), so the remaining 3 replicas maintain quorum

---

## Section 4 — Schema Design for Spanner

### 4.1 Primary Key Design Rules

Do not use:

- Auto-incrementing integers (`AUTO_INCREMENT`, `SERIAL`) — creates hotspot
- Sequential timestamps as sole primary key — same hotspot risk
- Short sequential string prefixes — same problem

Use:

- UUIDs (`GENERATE_UUID()`) — uniform distribution
- Composite keys where the first component is high-cardinality and not sequential
- Hash prefix on a natural key

### 4.2 Parent-Child Table Pattern

```sql
-- Parent
CREATE TABLE albums (
    singer_id STRING(36) NOT NULL,
    album_id STRING(36) NOT NULL,
    title STRING(500),
    release_date DATE
) PRIMARY KEY (singer_id, album_id);

-- Child — must share parent primary key prefix
CREATE TABLE songs (
    singer_id STRING(36) NOT NULL,
    album_id STRING(36) NOT NULL,
    track_number INT64 NOT NULL,
    song_title STRING(500),
    duration_seconds INT64
) PRIMARY KEY (singer_id, album_id, track_number),
  INTERLEAVE IN PARENT albums ON DELETE CASCADE;
```

`ON DELETE CASCADE` deletes child rows when the parent is deleted. Without this, deleting a parent with existing children returns an error.

Depth limit: Spanner allows up to 7 levels of interleaving.

### 4.3 Index Design in Spanner

```sql
-- Basic secondary index
CREATE INDEX idx_albums_title ON albums (title);

-- Index with stored columns (avoids back-join to base table)
CREATE INDEX idx_songs_duration ON songs (singer_id, duration_seconds DESC)
STORING (song_title);

-- Null-filtered index (excludes NULL values from index)
CREATE NULL_FILTERED INDEX idx_orders_active
ON orders (customer_id, order_date DESC)
WHERE status IS NOT NULL;
```

`NULL_FILTERED` indexes exclude rows where the indexed column is NULL. This is useful when most rows have NULL in the column and only the non-NULL values are ever queried — significantly reducing index size.

---

## Section 5 — Transaction Types Reference

### 5.1 Read-Write Transactions

- Full ACID guarantees
- All reads within the transaction are consistent at the transaction's read timestamp
- Pessimistic locking on read-write transactions: Spanner acquires shared locks on reads and exclusive locks on writes
- Aborts and retries: Spanner may abort a transaction due to conflicts; applications must handle `ABORTED` errors with retry logic

### 5.2 Read-Only Transactions

No locking. Two modes:

**Strong reads:**

- Returns data at `TT.now()` — the most recent committed data
- Must route to (or coordinate with) the Paxos leader
- Higher latency than stale reads
- Use when absolute freshness is required

**Bounded stale reads:**

- Returns data as of a specific timestamp or within a staleness bound (for example, up to 15 seconds old)
- Can be served from any replica (no leader coordination needed)
- Lower latency, higher availability
- Use for dashboards, analytics, or any read where a few seconds of staleness is acceptable

```python
# Python Spanner client — bounded stale read
import datetime
from google.cloud import spanner
from google.cloud.spanner_v1 import param_types

client = spanner.Client(project='my-project')
instance = client.instance('my-instance')
database = instance.database('mydb')

staleness = datetime.timedelta(seconds=15)
with database.snapshot(max_staleness=staleness) as snapshot:
    results = snapshot.execute_sql(
        "SELECT order_id, total_amount FROM orders WHERE status = 'active' LIMIT 100"
    )
    for row in results:
        print(row)
```

### 5.3 Partitioned DML

For bulk operations that would exceed the mutation limit of a standard read-write transaction (80,000 mutations per transaction):

```python
# Execute partitioned DML
database.execute_partitioned_dml(
    "UPDATE orders SET archived = true WHERE order_date < '2020-01-01'"
)
```

Restrictions:

- Cannot be used alongside reads in the same operation
- Not serializable — executes in parallel across splits
- Eventual consistency within the partition DML execution

---

## Section 6 — Cloud Spanner vs Cloud SQL Decision Matrix

### 6.1 Choosing Spanner

Choose Spanner when the requirements include any of:

- Global distribution with strongly consistent reads/writes
- Availability SLA > 99.99%
- Horizontal write scaling beyond what Cloud SQL's largest tier can provide
- Schema design naturally avoids auto-increment keys (greenfield applications)
- Zero planned maintenance downtime

### 6.2 Choosing Cloud SQL

Choose Cloud SQL when:

- Single-region deployment is acceptable
- Existing PostgreSQL or MySQL codebase needs minimal migration effort
- Budget is a primary constraint (Cloud SQL starts at ~$10/month; Spanner at ~$65/month)
- Application requires features Spanner lacks: stored procedures, full-text search, extensions
- Development team has deep PostgreSQL or MySQL expertise

### 6.3 Neither — When AlloyDB

AlloyDB for PostgreSQL (Module 12) targets the gap between Cloud SQL and Spanner:

- PostgreSQL-compatible
- Faster than Cloud SQL for both OLTP and analytics
- Single-region only (like Cloud SQL)
- Columnar engine for analytical queries

---

## Section 7 — Key Terms

| Term | Definition |
|---|---|
| TrueTime | Google's GPS + atomic clock-based distributed time infrastructure |
| Commit wait | Brief pause after commit to ensure timestamp ordering across nodes |
| External consistency | Serializable transactions that also respect real-world time ordering |
| Paxos | Consensus protocol used by Spanner for replication and leader election |
| Split | Spanner's unit of Paxos replication; a key range of a table |
| Hotspot | A split receiving disproportionate write traffic due to sequential keys |
| Interleaved table | Child table co-located with parent on the same server |
| Strong read | Read at most recent committed timestamp; requires leader coordination |
| Bounded stale read | Read within a staleness window; served from any replica |
| Partitioned DML | Bulk DML executed in parallel across splits; not serializable |
| Processing units (PUs) | Spanner compute units; 1000 PUs = 1 Spanner node |
| STORING | Spanner DDL keyword to include extra columns in a secondary index |

---

## Study Questions

1. Explain TrueTime in your own words. What problem does it solve, and how does commit wait use it?

2. Why do monotonically increasing integer primary keys cause hotspots in Spanner? Name two alternative key designs.

3. When would you use a bounded stale read instead of a strong read? What is the tradeoff?

4. What is Partitioned DML, and what restrictions apply to it?

5. A company has a 500 GB PostgreSQL database running on Cloud SQL and wants to expand to serve users in Europe and Asia-Pacific with strongly consistent reads. Should they migrate to Cloud Spanner or add Cloud SQL read replicas? Justify your answer.

6. What does `INTERLEAVE IN PARENT` accomplish in a Spanner DDL statement?

---

## Certification Exam Checklist

- [ ] TrueTime: GPS + atomic clocks, uncertainty interval, commit wait
- [ ] External consistency definition and how it differs from serializability
- [ ] Paxos: quorum = majority, leader per group, 5-replica group tolerates 2 failures
- [ ] Hotspot prevention: UUID, bit-reversed sequence, no AUTO_INCREMENT
- [ ] Interleaved tables: syntax, co-location benefit, max 7 levels
- [ ] Strong read: most recent data, leader coordination required
- [ ] Bounded stale read: any replica, lower latency, acceptable staleness
- [ ] Partitioned DML: bulk operations, no reads, not serializable
- [ ] Spanner processing units: 1000 PUs = 1 node
- [ ] Spanner vs Cloud SQL decision matrix: 5-nines, global, horizontal → Spanner
- [ ] `STORING` in Spanner index = `INCLUDE` in PostgreSQL
- [ ] `NULL_FILTERED` index: excludes NULL values

---

## 9. Supplemental Resources

The following free, open-access resources support Module 11 topics:

**1. [PostgreSQL Documentation — Row Estimation Examples](https://www.postgresql.org/docs/current/row-estimation-examples.html)**
Explains how the PostgreSQL planner uses column statistics to estimate row counts, including the impact of `default_statistics_target` and per-column `SET STATISTICS` on plan quality.

**2. [Google Cloud — Cloud SQL Query Insights Overview](https://cloud.google.com/sql/docs/postgres/query-insights-overview)**
Documents how Query Insights samples and aggregates queries, explains the normalized query view, latency percentiles, and how to identify top CPU consumers without modifying application code.

**3. [Google Cloud Spanner — Secondary Indexes](https://cloud.google.com/spanner/docs/secondary-indexes)**
Covers Spanner secondary index syntax including `STORING`, `NULL_FILTERED`, and interleaved indexes, with guidance on hotspot avoidance and index selection for read performance.

**4. [BigQuery Documentation — Introduction to Partitioned Tables](https://cloud.google.com/bigquery/docs/partitioned-tables)**
Explains BigQuery date, timestamp, and integer range partitioning, partition pruning mechanics, and how to write WHERE clauses that enable partition elimination.

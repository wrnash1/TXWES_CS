# Video Script: Module 11 — Cloud Spanner and Distributed Databases (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back to CIS-4327. I am Professor Nash, and this is Module 11: Cloud Spanner and Distributed Databases.

Cloud Spanner is one of the most unique and heavily tested services on the Google Cloud Professional Database Engineer exam. It is the only database in the world that simultaneously provides global distribution, strong consistency (ACID transactions), and horizontal scalability. To understand why this is remarkable, we first need to understand the fundamental challenge it solves.

Part 1 covers theory: the CAP theorem, TrueTime, Spanner's Paxos-based consensus, and schema design principles. Part 2 covers hands-on content: DDL, interleaved tables, read/write transactions, the Spanner query interface, and the Cloud SQL vs Spanner decision matrix.

---

## Section 1 — The Distributed Database Problem

### CAP Theorem

In 2000, Eric Brewer proposed the CAP theorem: a distributed data store can provide at most two of three properties simultaneously.

- **Consistency** — every read receives the most recent write or an error (strong consistency)
- **Availability** — every request receives a response (not necessarily the most recent data)
- **Partition Tolerance** — the system continues operating even when network partitions occur

Since network partitions are an unavoidable reality in distributed systems, every distributed database must choose between Consistency and Availability during a partition.

Traditional distributed databases pick one of two camps:

- **CP (Consistent + Partition Tolerant)**: Strong consistency, but may be unavailable during partitions. Traditional banking systems, ZooKeeper.
- **AP (Available + Partition Tolerant)**: Always available, but may return stale data during partitions. Cassandra, DynamoDB in some configurations.

**Cloud Spanner's claim** is that it provides external consistency (stronger than linearizability) across a globally distributed system with five nines of availability (99.999%). It achieves this using TrueTime.

### Linearizability and External Consistency

**Linearizability** means that operations appear to take effect instantaneously at a single point in time, and once an operation completes, all subsequent reads see its effect.

**External consistency** (Spanner's guarantee) is stronger: it respects real-world time. If transaction T1 commits before transaction T2 starts in real-world time, then T2 is guaranteed to observe T1's writes. This is achieved using TrueTime.

---

## Section 2 — TrueTime

TrueTime is Google's globally synchronized clock infrastructure. It is the foundation of Spanner's external consistency guarantee.

### The Problem with Distributed Clocks

In a distributed system, different servers have different hardware clocks. Clock drift — the difference between what a server's clock reports and actual time — can be milliseconds to seconds. If you use server timestamps to order transactions across multiple datacenters, two clocks that disagree by even 10 milliseconds can produce incorrect orderings.

### TrueTime's Solution

TrueTime uses GPS receivers and atomic clocks in every Google datacenter. It does not report a single time value — it reports a time interval `[TT.now().earliest, TT.now().latest]`. This interval represents the bounds within which the true current time lies.

The key insight: if one transaction's `TT.now().latest` is less than another transaction's `TT.now().earliest`, then the first transaction definitely committed before the second in real time. There is no ambiguity.

Spanner uses this uncertainty bound (typically 1–7 milliseconds) to implement **commit wait**: after a transaction is prepared to commit, Spanner waits until the commit timestamp is safely in the past (outside all uncertainty windows across all nodes) before returning the commit acknowledgment to the client. This brief pause — usually a few milliseconds — is what makes external consistency possible.

### TrueTime vs NTP

| Property | NTP (Network Time Protocol) | TrueTime |
|---|---|---|
| Clock source | Internet time servers | GPS + atomic clocks in-datacenter |
| Uncertainty bound | Tens to hundreds of ms | 1–7 ms typical |
| Distributed transaction use | Unsafe | Safe (Spanner uses as ordering mechanism) |
| Availability | Public protocol | Google proprietary infrastructure |

---

## Section 3 — Paxos Consensus

Cloud Spanner uses the **Paxos** consensus protocol to replicate data within and across regions.

### How Paxos Works in Spanner

Each Spanner table has its data distributed across a set of Paxos groups. A Paxos group consists of replicas — typically 5 replicas spread across 3 or more zones (for regional) or multiple regions (for multi-region configurations).

A write transaction must be acknowledged by a majority of replicas (a quorum) in the Paxos group before it is considered committed. For 5 replicas, that means at least 3 replicas must acknowledge.

One replica in each Paxos group is elected the **leader**. The leader coordinates all writes. Reads can be served from any replica (for stale reads) or from the leader (for strong reads).

The leader periodically re-elects itself via lease renewals. If the leader fails, the remaining replicas hold an election and a new leader is established.

### Geographic Distribution

Spanner instances come in three configurations:

- **Regional** — data in 3 zones within a single region. Provides zone-level fault tolerance.
- **Multi-region** — data across multiple regions. Provides region-level fault tolerance. Higher latency for writes (cross-region consensus round trip).
- **Dual-region** — specific two-region pairing with an intermediate "witness" zone.

For the exam: multi-region Spanner provides the highest availability (can survive an entire region failure) but also the highest write latency (waiting for quorum acknowledgment across regions).

---

## Section 4 — Spanner Schema Design

### Key Concepts

Spanner is not a relational database in the traditional sense. While it supports SQL and ACID transactions, its schema design must account for how data is physically stored across splits (shards).

**Splits** — Spanner automatically divides data into splits based on key ranges. A split is the unit of Paxos replication. Rows with adjacent primary keys stay in the same split. As data grows, Spanner splits ranges and distributes them across nodes.

**Hotspots** — A hotspot occurs when too many writes go to the same split. The most common cause is a monotonically increasing primary key (like `AUTO_INCREMENT` or `SERIAL`). Every new row has the highest key value, so all writes go to the same split — the "hot" end of the key space. This limits write throughput.

**Solutions for hotspot prevention:**

1. **UUID v4 primary key** — random keys distribute writes evenly across splits.
2. **Bit-reversed sequence** — a technique where you reverse the bits of a sequential integer, spreading sequential values across the key space.
3. **Hash prefix** — prepend a hash of a high-cardinality value to the key.

```sql
-- Bad: monotonically increasing, creates hotspot
CREATE TABLE orders (
    order_id INT64 NOT NULL,  -- auto-incrementing
    ...
) PRIMARY KEY (order_id);

-- Good: UUID distributes writes
CREATE TABLE orders (
    order_id STRING(36) NOT NULL,  -- UUID v4
    ...
) PRIMARY KEY (order_id);

-- Alternative: use Spanner's built-in UUID function
INSERT INTO orders (order_id, ...) VALUES (GENERATE_UUID(), ...);
```

### Data Types in Spanner DDL

Spanner uses its own type system. Key differences from PostgreSQL/MySQL:

| Spanner Type | Equivalent |
|---|---|
| `INT64` | BIGINT |
| `FLOAT64` | DOUBLE PRECISION |
| `STRING(n)` | VARCHAR(n) |
| `BYTES(n)` | BYTEA / BLOB |
| `BOOL` | BOOLEAN |
| `DATE` | DATE |
| `TIMESTAMP` | TIMESTAMPTZ |
| `ARRAY<T>` | PostgreSQL ARRAY |
| `JSON` | JSONB (Spanner JSON type) |

There is no `AUTO_INCREMENT` or `SERIAL` in Spanner. Use UUID or sequence-managed keys.

---

## Section 5 — Interleaved Tables

**Interleaved tables** are Spanner's mechanism for co-locating parent and child rows physically on the same server. This is critical for performance: without interleaving, joining a parent and child requires a cross-split or even cross-region network call.

```sql
-- Parent table
CREATE TABLE customers (
    customer_id STRING(36) NOT NULL,
    full_name STRING(200),
    email STRING(150),
    created_at TIMESTAMP
) PRIMARY KEY (customer_id);

-- Child table interleaved in parent
CREATE TABLE orders (
    customer_id STRING(36) NOT NULL,
    order_id STRING(36) NOT NULL,
    total_amount FLOAT64,
    order_date DATE,
    status STRING(20)
) PRIMARY KEY (customer_id, order_id),
  INTERLEAVE IN PARENT customers ON DELETE CASCADE;
```

The child table's primary key must begin with the parent's primary key columns. Spanner physically stores all orders for a given customer_id adjacent to the customer row on the same server.

Queries that join customers to their orders no longer require cross-node communication:

```sql
-- This join is served locally because orders are co-located with customers
SELECT c.full_name, o.order_id, o.total_amount
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
WHERE c.customer_id = '550e8400-e29b-41d4-a716-446655440000';
```

---

## Section 6 — Exam Summary for Part 1

Key exam concepts from Part 1:

- CAP theorem: Spanner is CP (Consistency + Partition Tolerance) with unusually high availability achieved via TrueTime
- TrueTime: GPS + atomic clocks; reports time interval not a point; enables external consistency
- Commit wait: brief delay at transaction commit to guarantee timestamp ordering
- Paxos: quorum-based consensus; leader per group; majority of replicas must ack before commit
- Hotspot problem: monotonically increasing keys concentrate writes on one split
- Solutions: UUID v4, bit-reversed sequence, hash prefix
- Interleaved tables: co-locate parent and child rows for local joins
- No AUTO_INCREMENT in Spanner; use `GENERATE_UUID()`

---

## Closing

That wraps up Part 1 of Module 11. You now understand the theoretical foundations that make Cloud Spanner unique: TrueTime, Paxos consensus, hotspot prevention, and interleaved table co-location.

In Part 2, we look at the practical side: read/write transactions, the Spanner API, when to choose Spanner vs Cloud SQL, and specific exam patterns. See you there.

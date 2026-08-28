# Reading Guide: Module 04 — Cloud Spanner: Globally Distributed Databases

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

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Introduction

Cloud Spanner is Google's globally distributed relational database and one of the highest-weighted services on the GCP Database Engineer exam. It occupies a unique position in the database landscape: the only commercially available database that provides both full ACID transactions and horizontal scalability at global scale. Understanding its architecture, schema design rules, and the scenarios where it is the correct choice is essential for the exam and for professional cloud database work.

---

### 1. High-Yield Glossary

**Cloud Spanner**: Google's fully managed, globally distributed relational database service. Provides full ACID transactions and horizontal scaling across regions.

**TrueTime**: Google's globally synchronized clock infrastructure using atomic clocks and GPS receivers. Provides timestamps accurate to within a few milliseconds. Enables Spanner to order transactions globally without a central coordinator.

**External Consistency**: Spanner's consistency guarantee — stronger than serializable isolation. Transactions behave as if they execute sequentially on a single global machine, regardless of physical distribution.

**Paxos Consensus**: The replication protocol Spanner uses to ensure writes are acknowledged only after a majority of replicas confirm receipt. Guarantees durability and consistency across distributed nodes.

**Processing Unit (PU)**: The compute capacity unit for Cloud Spanner. 1000 PUs = 1 node. Minimum for production is typically 1 node.

**Instance**: A Cloud Spanner compute and storage resource allocation. Contains one or more databases.

**Database**: A collection of tables within a Spanner instance. Each database has its own DDL schema.

**Tablet**: A Spanner storage shard. Data is split into tablets by primary key range and distributed across Spanner servers. Tablets are automatically balanced as data grows.

**Hotspot**: A performance bottleneck caused by many writes concentrating on the same tablet due to sequential primary key values. All new rows go to the highest-key tablet, preventing horizontal scaling.

**Interleaved Table**: A Spanner-specific physical storage design where child table rows are stored co-located with their parent row. Defined with `INTERLEAVE IN PARENT`. Eliminates cross-server lookups for parent-child joins.

**Secondary Index**: An alternate key structure in Spanner for fast lookups on non-primary-key columns. Created with `CREATE INDEX`.

**Covering Index**: A Spanner secondary index that includes additional stored columns with the STORING clause. Eliminates back-joins to the base table for queries that need those columns.

**Strong Read**: A Spanner read that returns the most recent committed data. Goes through the Paxos leader. Provides the strongest consistency guarantee.

**Stale Read**: A Spanner read that returns data as of a timestamp in the past. Can be served by any replica, including non-leaders. Lower latency than strong reads.

**Bounded Staleness**: A stale read mode where the client specifies a maximum allowable staleness duration (e.g., 15 seconds). Spanner serves the most recent data within that bound.

**Read-Write Transaction**: A Spanner transaction that reads and writes data. Uses two-phase commit internally. Subject to abort if lock conflicts occur; client must implement retry.

**Read-Only Transaction**: A Spanner transaction that reads data only. No locking, no abort risk. Uses either strong or stale reads.

**Mutation**: An alternative to DML in Spanner. A set of buffered writes applied atomically at commit time. Higher throughput than DML for bulk writes but no conditional read logic.

**Regional Configuration**: A Spanner instance that replicates across three zones within one GCP region. 99.999% SLA.

**Multi-Region Configuration**: A Spanner instance that replicates across two or more GCP regions. 99.999% SLA with geographic redundancy.

**Spanner SQL**: ANSI SQL-compatible query language used by Cloud Spanner. Differs from standard SQL in data types, no AUTO_INCREMENT, and Spanner-specific functions.

**Version Retention Period**: The duration Spanner retains old versions of data for PITR. Configurable from 1 hour to 7 days.

---

### 2. Spanner Data Types Reference

| Spanner Type | Description | Standard SQL Equivalent |
|---|---|---|
| INT64 | 64-bit signed integer | INTEGER / BIGINT |
| STRING(N) | Variable-length string up to N bytes | VARCHAR(N) |
| FLOAT64 | 64-bit double-precision float | DOUBLE PRECISION |
| BOOL | Boolean true/false | BOOLEAN |
| DATE | Calendar date (no time) | DATE |
| TIMESTAMP | Microsecond-precision timestamp with timezone | TIMESTAMP WITH TIME ZONE |
| BYTES(N) | Binary data up to N bytes | BYTEA / VARBINARY |
| JSON | JSON document | JSON / JSONB |
| ARRAY | Ordered list of a single type | ARRAY (PostgreSQL) |
| STRUCT | Named-field compound type | ROW (PostgreSQL) |

Key exam fact: Spanner has no AUTO_INCREMENT, SERIAL, or SEQUENCE. Primary key values must be generated by the application.

---

### 3. Primary Key Design Strategies

| Strategy | Description | Hotspot Risk |
|---|---|---|
| UUID (random) | Generates a random 128-bit identifier | Very low — keys are uniformly distributed |
| Bit-reversed sequential | Reverses binary bits of a monotonically increasing integer | Very low — reversal spreads writes across key space |
| Hash prefix | Prepends a hash of natural key fields to primary key | Very low — hash distributes writes |
| Composite with high-cardinality leading column | Uses (region, timestamp) or (shard_id, entity_id) | Low — writes distributed across leading column values |
| Auto-increment integer | Sequential integers concentrated at the high end | Very high — all writes go to one tablet |

The exam will present a scenario with write hotspots and ask for the fix. The answer is always to move away from sequential keys.

---

### 4. Interleaved Tables — When and How

Interleaving is beneficial when:

- Child records are almost always accessed through the parent (parent-child joins are the dominant access pattern).
- Child rows have a foreign key relationship to the parent.
- Data locality reduces the most expensive operations in the query.

Interleaving is not beneficial when:

- Child rows are frequently accessed independently without the parent.
- The parent table is very wide (large rows), making co-location storage-inefficient.
- Child rows are joined to multiple parents (many-to-many relationships).

Syntax rule: to define an interleaved table, the child table's primary key must start with the same columns as the parent's primary key.

```sql
-- Parent primary key: (StudentId)
-- Child must start with StudentId
CREATE TABLE Enrollments (
    StudentId  INT64 NOT NULL,
    CourseId   INT64 NOT NULL,
    Grade      STRING(2)
) PRIMARY KEY (StudentId, CourseId),
  INTERLEAVE IN PARENT Students ON DELETE CASCADE;
```

---

### 5. Cloud Spanner vs. Cloud SQL — Detailed Comparison

| Dimension | Cloud SQL | Cloud Spanner |
|---|---|---|
| ACID transactions | Full ACID | Full ACID (external consistency) |
| Geographic scope | Single region | Single region or global multi-region |
| Horizontal scaling | No — vertical only | Yes — add nodes/PUs |
| Maximum data size | 64 TB | Unlimited |
| Availability SLA (HA) | 99.95% (Enterprise), 99.99% (Enterprise Plus) | 99.999% (multi-region) |
| Failover time | ~60 seconds | Near-zero (continuous replication) |
| SQL compatibility | Standard MySQL or PostgreSQL | Spanner SQL (ANSI with extensions) |
| Auto-increment keys | Supported | Not recommended (hotspot risk) |
| Connection model | Client libraries, Auth Proxy | Client libraries (no proxy needed) |
| Cost | Lower | Significantly higher per node |
| Best use cases | Regional OLTP, lift-and-shift | Global OLTP, financial systems |

---

### 6. Read Mode Comparison

| Mode | Latency | Consistency | Use Case |
|---|---|---|---|
| Strong read | Higher | Most recent data guaranteed | Financial transactions, inventory checks |
| Bounded staleness | Lower | Data may be up to N seconds old | Dashboards, reporting, feeds |
| Exact staleness | Lowest | Data exactly as of specified timestamp | Historical point-in-time queries |

---

### 7. Backup and Recovery Reference

| Feature | Description |
|---|---|
| Managed backup | Full backup stored in Spanner-managed storage; configurable expiration date |
| Backup retention | Configurable from 1 hour to 1 year |
| PITR | Built-in; retain versions from 1 hour to 7 days; no extra configuration needed |
| Restore | Creates a new database from backup; source database is not affected |

---

### 8. gcloud CLI Reference for Cloud Spanner

| Task | Command |
|---|---|
| Create instance | `gcloud spanner instances create NAME --config=CONFIG --processing-units=PU` |
| Create database | `gcloud spanner databases create DB --instance=INSTANCE` |
| Execute DDL | `gcloud spanner databases ddl update DB --instance=INSTANCE --ddl="DDL_STATEMENT"` |
| Execute DML | `gcloud spanner databases execute-sql DB --instance=INSTANCE --sql="SQL"` |
| Create backup | `gcloud spanner backups create NAME --instance=INSTANCE --database=DB --expiration-date=DATE` |
| List backups | `gcloud spanner backups list --instance=INSTANCE` |
| Restore database | `gcloud spanner databases restore --destination-instance=I --destination-database=DB --source-backup=BK` |
| Delete instance | `gcloud spanner instances delete INSTANCE` |

---

### 9. Required Readings and Resources

**GCP Documentation — Cloud Spanner Overview**: Architecture, use cases, and conceptual introduction. Available at cloud.google.com/learn.

**GCP Documentation — Cloud Spanner Schema Design Best Practices**: Covers primary key selection, hotspot avoidance, interleaved tables, and secondary index design. Available at cloud.google.com/learn.

**GCP Documentation — Cloud Spanner Reads and Transactions**: Covers strong reads, stale reads, read-write transactions, and mutations. Available at cloud.google.com/learn.

---

### 10. Exam Tips

Tip 1: global consistency plus horizontal scaling is the Cloud Spanner signature. No other GCP database provides both simultaneously.

Tip 2: five-nines (99.999%) SLA is a Spanner indicator. Any scenario with a contractual five-nines requirement points to Spanner multi-region.

Tip 3: sequential auto-increment keys create hotspots. The exam tests this by describing degrading write performance on a Spanner table. Answer: switch to UUID or bit-reversed keys.

Tip 4: INTERLEAVE IN PARENT is a physical optimization, not a logical constraint. It co-locates data to reduce cross-server reads. Know when to use it: parent-child access patterns where both parent and children are typically read together.

Tip 5: bounded staleness reads reduce latency by serving from any replica. Strong reads require the Paxos leader. Dashboard or reporting scenarios that mention latency reduction point to stale reads.

Tip 6: 1000 PUs = 1 Spanner node. The exam may ask about scaling Spanner capacity. Adding nodes/PUs scales both read and write throughput proportionally.

Tip 7: Spanner PITR requires no special configuration — version retention is built in. This differs from Cloud SQL, where binary logging or WAL archiving must be explicitly enabled.

Tip 8: Cloud Spanner is substantially more expensive than Cloud SQL. Cost-sensitive scenarios with only regional requirements should use Cloud SQL.

---

### 11. Study Checklist

- Explain TrueTime and its role in Spanner's external consistency
- State the SLA for Cloud Spanner multi-region configurations
- Explain what a hotspot is and identify three primary key strategies that prevent hotspots
- Write a CREATE TABLE statement with INTERLEAVE IN PARENT
- Explain the difference between strong reads and bounded staleness reads
- Explain when STORING in a secondary index eliminates a back-join
- State the difference between DML and Mutations in Spanner
- Write gcloud CLI commands to create a Spanner instance and database
- Identify the two criteria that distinguish a Cloud Spanner workload from a Cloud SQL workload
- Complete the Module 04 lab activity
- Pass the Module 04 quiz with at least 80 percent

---

Reference: cloud.google.com/learn

---

## 9. Supplemental Resources

**1. Cloud Spanner — Official Documentation: Schema and Data Model**
https://cloud.google.com/spanner/docs/schema-and-data-model
Covers table interleaving, primary key design, secondary indexes with STORING, and DDL syntax specific to Cloud Spanner.

**2. Google Cloud Blog — Spanner Internals: TrueTime and External Consistency**
https://cloud.google.com/blog/products/databases/inside-cloud-spanner-and-the-cap-theorem
Explains TrueTime's role in achieving external consistency, discusses how Spanner relates to the CAP theorem, and describes the Paxos consensus mechanism.

**3. Cloud Spanner — Best Practices for Schema Design**
https://cloud.google.com/spanner/docs/best-practice-large-scale
Google's official guide for avoiding hotspots, choosing primary key strategies (UUIDs, hash prefixes, bit-reversal), and designing interleaved tables for production workloads.

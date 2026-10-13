# Reading Guide: Module 09 — AWS Databases

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4334 &BULL; AMAZON WEB SERVICES (AWS) CLOUD ARCHITECTURE</text>
    
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


## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

## Certification Alignment: AWS Solutions Architect — Associate (SAA-C03)

---

## Introduction

AWS provides purpose-built database services for relational, key-value, document, in-memory, graph, and analytics workloads. Selecting the right database is one of the most frequently tested skills on the SAA-C03 exam. This guide provides reference tables, architectural decision trees, and exam tips for all six database services covered in Module 09.

---

## Section 1: Amazon RDS

### 1.1 Supported Engines

| Engine | Notable Characteristics |
|--------|------------------------|
| MySQL | Open source; wide compatibility; up to 5 read replicas |
| PostgreSQL | Advanced SQL features; JSONB support; up to 5 read replicas |
| MariaDB | MySQL fork; open source; community-driven |
| Oracle | Enterprise licensing; Bring Your Own License (BYOL) or License Included |
| Microsoft SQL Server | Windows-native; Express/Web/Standard/Enterprise editions |
| Amazon Aurora | AWS cloud-native; MySQL or PostgreSQL compatible; covered in Section 2 |

### 1.2 Multi-AZ vs. Read Replicas

| Feature | Multi-AZ | Read Replicas |
|---------|----------|---------------|
| Primary purpose | High availability and failover | Read scaling and load reduction |
| Replication type | Synchronous | Asynchronous |
| Standby/replica accessible for reads | No (standby is passive) | Yes (separate endpoint) |
| Failover | Automatic (60–120 seconds) | Manual promotion |
| Cross-region | No (single region only) | Yes (cross-region supported) |
| Number of standbys/replicas | 1 standby | Up to 5 (MySQL, PostgreSQL); 15 (Aurora) |
| Increases read capacity | No | Yes |
| Increases write capacity | No | No (writes always go to primary) |

**Critical exam distinction:** Multi-AZ is for availability (not performance). Read Replicas are for read performance (not availability by default — must be manually promoted).

### 1.3 RDS Automated Backups and Snapshots

| Feature | Automated Backups | Manual Snapshots |
|---------|------------------|------------------|
| Retention period | 1–35 days | Retained indefinitely until deleted |
| Scope | Full + incremental (transaction logs) | Full snapshot |
| Point-in-time restore | Yes (to any second within retention period) | No (restore to snapshot point only) |
| Deleted with instance | Yes | No |
| Storage location | S3 (managed by AWS) | S3 (managed by AWS) |

### 1.4 RDS Encryption

Encryption at rest uses AWS KMS. Encryption must be enabled at creation time — you cannot add encryption to an existing unencrypted RDS instance directly. To encrypt an unencrypted instance: create a snapshot, copy the snapshot with encryption enabled, restore from the encrypted snapshot.

Read Replicas of an encrypted master are always encrypted. The Multi-AZ standby inherits the encryption of the primary.

---

## Section 2: Amazon Aurora

### 2.1 Aurora Architecture Differentiators

| Feature | RDS (MySQL/PostgreSQL) | Aurora |
|---------|----------------------|--------|
| Storage | EBS volumes per instance | Distributed shared storage (3 AZs, 6 copies) |
| Max read replicas | 5 | 15 |
| Failover time | 60–120 seconds | ~30 seconds (replica promotion) |
| Storage auto-growth | No (manual resize) | Yes (10 GB to 128 TB automatic) |
| Multi-master | No | Yes (Aurora Multi-Master for active-active writes) |
| Serverless option | No | Aurora Serverless v2 (auto-scales ACUs) |
| Performance vs. community engine | Baseline | 5x MySQL, 3x PostgreSQL |

### 2.2 Aurora Endpoints

| Endpoint Type | Behavior | Use Case |
|---------------|----------|----------|
| Cluster Writer Endpoint | Always points to current primary | Application writes |
| Cluster Reader Endpoint | Load-balances across all read replicas | Application reads |
| Instance Endpoint | Points to specific instance | Direct access for maintenance |
| Custom Endpoint | Points to a subset of instances | Route specific query types to specific replicas |

### 2.3 Aurora Global Database

Aurora Global Database spans multiple AWS Regions with a single primary region for writes. Up to 5 secondary read-only regions with sub-second replication lag. In a disaster recovery scenario, a secondary region can be promoted to primary in under 1 minute — this is Aurora's RPO/RTO-minimizing DR architecture.

---

## Section 3: Amazon DynamoDB

### 3.1 Primary Key Types

| Key Type | Components | Query Operation | Example |
|----------|------------|-----------------|---------|
| Simple (Partition key only) | Partition key (hash) | GetItem only | UserId → User profile |
| Composite (Partition + Sort) | Partition key + Sort key | GetItem or Query | CustomerId + OrderDate → Order history |

### 3.2 Index Comparison

| Feature | Local Secondary Index (LSI) | Global Secondary Index (GSI) |
|---------|---------------------------|------------------------------|
| Partition key | Same as base table | Any attribute |
| Sort key | Different from base table | Any attribute |
| Created when | Table creation only | Any time |
| Capacity | Shares base table | Independent (separate RCUs/WCUs) |
| Strong consistency | Yes | Eventually consistent only |
| Max per table | 5 | 20 |

### 3.3 Capacity Modes

| Mode | Billing | Best For |
|------|---------|----------|
| Provisioned | Per RCU/WCU provisioned | Predictable, steady traffic — more cost-efficient at scale |
| On-Demand | Per request | Unpredictable, bursty, new applications |

Capacity unit reference:

- 1 RCU = 1 strongly consistent read/sec for items up to 4 KB (or 2 eventually consistent reads)
- 1 WCU = 1 write/sec for items up to 1 KB

### 3.4 DynamoDB Feature Reference

| Feature | Description | Use Case |
|---------|-------------|----------|
| DynamoDB Streams | Change log of item modifications (24-hour retention) | Trigger Lambda on item change |
| DAX | In-memory read cache (microsecond reads) | Read-heavy, repeated item access |
| Global Tables | Multi-region active-active replication | Global user base, active-active DR |
| TTL | Auto-delete items after timestamp attribute expires | Session data, temporary records |
| Transactions | ACID transactions across multiple items/tables | Financial workflows requiring all-or-nothing writes |

### 3.5 Partition Key Design Best Practices

Hot partition keys cause throttling even when total provisioned capacity appears sufficient. A hot key occurs when most requests target the same partition key value.

Good partition key design:

- Use high cardinality attributes (UserId, OrderId, SessionId)
- Avoid low cardinality (Status: active/inactive concentrates 50% of traffic on each of two partitions)
- For time-series data: combine a high-cardinality ID with a timestamp as a composite key

---

## Section 4: Amazon ElastiCache

### 4.1 Redis vs. Memcached Comparison

| Feature | Redis | Memcached |
|---------|-------|-----------|
| Data structures | Strings, hashes, lists, sets, sorted sets | Strings only |
| Persistence | Yes (RDB snapshots, AOF logging) | No |
| Replication | Yes | No |
| Multi-AZ failover | Yes (automatic) | No |
| Cluster sharding | Yes (Redis Cluster mode) | Yes (client-side) |
| Pub/Sub messaging | Yes | No |
| Geospatial indexing | Yes | No |
| Multi-threading | No (single-threaded) | Yes |
| Backup and restore | Yes | No |

### 4.2 ElastiCache Use Case Patterns

| Use Case | Engine | Pattern |
|----------|--------|---------|
| Database read cache | Redis or Memcached | Cache query results; reduce DB load |
| Session store | Redis | TTL-based expiration; replication for HA |
| Leaderboard | Redis | Sorted sets for ranked lists |
| Rate limiting | Redis | Atomic increment on request counters |
| Pub/Sub messaging | Redis | Publisher/subscriber channels |
| Simple high-throughput cache | Memcached | Pure key-value; multi-threaded |

### 4.3 Caching Strategies

| Strategy | Description | Pros | Cons |
|----------|-------------|------|------|
| Lazy Loading | Load to cache only on miss | Cache only holds requested data | Miss penalty on first request |
| Write-Through | Update cache on every write | Cache always current | Write overhead; unused data may be cached |
| TTL | Expire cached items after a fixed duration | Controls staleness | May serve stale data near TTL expiry |

---

## Section 5: Amazon Redshift

### 5.1 Redshift vs. RDS

| Feature | Redshift | RDS |
|---------|----------|-----|
| Optimized for | OLAP (analytical queries) | OLTP (transactional operations) |
| Storage format | Columnar | Row-based |
| Query pattern | Aggregate, scan, join large tables | Frequent small reads/writes |
| Scale | Petabyte | Terabyte |
| Typical query time | Seconds to minutes | Milliseconds |
| SQL compatibility | Yes (PostgreSQL-compatible) | Yes (engine-specific) |

### 5.2 Key Redshift Features

| Feature | Description |
|---------|-------------|
| Redshift Spectrum | Query data in S3 without loading into Redshift |
| Redshift Serverless | Auto-provisions capacity; pay per query |
| RA3 nodes | Separate compute from managed storage (S3) |
| Materialized Views | Pre-computed query results for dashboard acceleration |
| Data Sharing | Share live data across Redshift clusters without copying |
| AQUA | Advanced Query Accelerator — hardware-based query acceleration |

---

## Section 6: Amazon Neptune

### 6.1 Neptune Overview

| Feature | Description |
|---------|-------------|
| Graph models supported | Property Graph (Gremlin traversal), RDF (SPARQL queries) |
| Availability | Multi-AZ with up to 15 read replicas |
| Storage | Shared distributed storage (same as Aurora) |
| Use cases | Social networks, fraud detection, knowledge graphs, recommendations |

### 6.2 Graph vs. Relational Decision

| Scenario | Best Database |
|----------|--------------|
| Traversing relationships between entities (who knows whom) | Neptune |
| Detecting fraud via transactional relationship patterns | Neptune |
| Building a recommendation engine based on user/product relationships | Neptune |
| Complex SQL queries with known schema | RDS or Aurora |
| Key-value lookups at high scale | DynamoDB |

---

## Section 7: Database Selection Decision Framework

### 7.1 Primary Decision Matrix

| Requirement | Database |
|-------------|----------|
| Relational SQL; Oracle or SQL Server | RDS |
| MySQL/PostgreSQL; need > 5 replicas or serverless scaling | Aurora |
| Single-digit millisecond NoSQL at any scale | DynamoDB |
| Reduce database read load; cache hot data | ElastiCache |
| Petabyte analytics; business intelligence; OLAP | Redshift |
| Graph traversal; relationships between entities | Neptune |

### 7.2 Exam Decision Triggers

| Keyword or Phrase | Answer |
|-------------------|--------|
| "High availability, automatic failover, same region" | RDS Multi-AZ |
| "Read scaling, reduce primary load" | RDS Read Replicas or Aurora read replicas |
| "MySQL compatible, faster failover, automatic storage scaling" | Aurora |
| "Serverless database, variable workload" | Aurora Serverless v2 |
| "Millions of requests/sec, single-digit ms, NoSQL" | DynamoDB |
| "Query non-key attribute in existing DynamoDB table" | GSI |
| "Microsecond DynamoDB read latency" | DAX |
| "DynamoDB multi-region active-active" | DynamoDB Global Tables |
| "Reduce RDS/Aurora read latency, cache hot rows" | ElastiCache |
| "Session store with high availability" | ElastiCache Redis |
| "Simple cache, no HA needed" | ElastiCache Memcached |
| "Data warehouse, business intelligence, OLAP" | Redshift |
| "Social network, fraud detection, graph" | Neptune |

---

## Section 8: SAA-C03 Exam Tips for Module 09

**Exam Tip 1 — Multi-AZ is NOT for read scaling:**
Multi-AZ provides high availability. The standby does not serve reads. If a scenario asks how to improve read performance, Multi-AZ is never the answer. Read Replicas or ElastiCache are the answers.

**Exam Tip 2 — Read Replicas are NOT automatically promoted:**
If the primary RDS instance fails, Read Replicas are not automatically promoted to primary. Multi-AZ is. Read Replicas require a manual promotion step. Cross-region Read Replicas can be manually promoted for regional DR.

**Exam Tip 3 — Aurora's shared storage means faster failover:**
Aurora failover is faster than RDS Multi-AZ because the promoted replica already has access to all committed data in the shared storage layer. It does not need to replay transaction logs.

**Exam Tip 4 — GSI can be added after table creation; LSI cannot:**
If the scenario says an existing DynamoDB table needs a new query pattern, the answer must be GSI. LSIs are only creatable at table creation time.

**Exam Tip 5 — DAX is read-only acceleration:**
DAX accelerates DynamoDB reads. It does not help with write-heavy workloads. DAX returns eventually consistent results only. Strongly consistent reads bypass DAX.

**Exam Tip 6 — Redis for HA cache; Memcached for simple cache:**
Redis supports replication, Multi-AZ failover, persistence, and complex data structures. If a scenario mentions session storage, leaderboards, pub/sub, or "highly available cache," the answer is Redis. If it says "simple distributed cache with no persistence needed," Memcached may be the answer.

**Exam Tip 7 — Redshift for OLAP only:**
Redshift is not an OLTP database. If a scenario mentions "frequent transactional reads and writes" or "operational database," Redshift is not the answer. Redshift is for historical data analysis, reporting, and BI queries.

**Exam Tip 8 — Neptune for relationships:**
Neptune appears less frequently on the exam than other databases, but the trigger words are unmistakable: "graph database," "social network," "fraud detection via relationships," "knowledge graph," or "recommendation engine based on user relationships."

---

## Section 9: Key CLI Commands

Describe an RDS instance:

```bash
aws rds describe-db-instances \
  --db-instance-identifier mydb \
  --query "DBInstances[0].{Engine:Engine,Class:DBInstanceClass,MultiAZ:MultiAZ,Status:DBInstanceStatus}"
```

Create an RDS Read Replica:

```bash
aws rds create-db-instance-read-replica \
  --db-instance-identifier mydb-replica \
  --source-db-instance-identifier mydb \
  --db-instance-class db.t3.medium \
  --availability-zone us-east-1b
```

Describe DynamoDB table:

```bash
aws dynamodb describe-table \
  --table-name MyTable \
  --query "Table.{Name:TableName,Status:TableStatus,Keys:KeySchema,GSIs:GlobalSecondaryIndexes}"
```

Create an ElastiCache Redis cluster:

```bash
aws elasticache create-cache-cluster \
  --cache-cluster-id my-redis \
  --engine redis \
  --cache-node-type cache.t3.micro \
  --num-cache-nodes 1
```

---

## Section 10: Study Checklist

- [ ] Explain the difference between RDS Multi-AZ and Read Replicas — purpose, replication type, and failover behavior
- [ ] Describe Aurora's shared storage architecture and how it differs from standard RDS
- [ ] Explain the Aurora failover process and why it is faster than RDS Multi-AZ failover
- [ ] Compare DynamoDB GSIs and LSIs on creation timing, partition key flexibility, and consistency
- [ ] Explain DAX: what it accelerates, what it cannot accelerate, and when not to use it
- [ ] Compare ElastiCache Redis and Memcached on persistence, replication, data structures, and use cases
- [ ] Describe when to use Redshift versus RDS for a given analytical workload
- [ ] Identify the three Neptune use case patterns from the exam trigger word list
- [ ] Complete the database selection decision matrix from memory, covering all six services
- [ ] Run the CLI commands in Section 9 and record the output
- [ ] Complete the Module 09 quiz with a score of at least 80 percent

---

## References

All AWS certification study materials and exam registration: aws.amazon.com/certification

---

## 11. Supplemental Resources

**1. AWS Documentation — Amazon DynamoDB Developer Guide: Best Practices**
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html
AWS best practices for DynamoDB table design covering partition key selection, GSI strategy, capacity planning, and access pattern optimization — directly aligned to the DynamoDB design questions in this module.

**2. AWS Skill Builder — Amazon DynamoDB: Building NoSQL Database-Driven Applications**
https://skillbuilder.aws/learn/course/external/view/elearning/1304/amazon-dynamodb-building-nosql-database-driven-applications
Free course covering DynamoDB data modeling, capacity modes, GSIs, DAX, streams, and global tables — supporting Module 09 DynamoDB exam topics and lab exercises.

**3. AWS Documentation — Choosing the Right Database Service**
https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html
AWS overview of all managed database services (RDS, Aurora, DynamoDB, ElastiCache, Redshift, Neptune, DocumentDB, Keyspaces) with use case guidance — the comprehensive reference for database service selection questions on SAA-C03.

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*

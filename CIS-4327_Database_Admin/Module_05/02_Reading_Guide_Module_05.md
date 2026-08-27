# Reading Guide: Module 05 — Bigtable: Wide-Column NoSQL at Scale

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Introduction

Cloud Bigtable is the GCP service you choose when your workload involves massive volumes of data, high-throughput writes, and fast key-based reads — and when you do not need SQL JOINs or multi-row ACID transactions. Bigtable's data model is radically different from the relational databases covered in previous modules. Understanding that difference — and knowing exactly when to apply it — is a core exam competency.

---

### 1. High-Yield Glossary

**Cloud Bigtable**: Google Cloud's fully managed wide-column NoSQL database. Designed for petabyte-scale, high-throughput, low-latency workloads. Based on the internal Bigtable system that powers Google Search, Maps, and Gmail.

**Wide-Column Store**: A NoSQL database model that stores data in rows with many dynamic columns, organized into column families. Bigtable, Apache Cassandra, and Apache HBase are wide-column stores.

**Row Key**: The unique identifier for a row in a Bigtable table. A byte string up to 4 KB. Rows are sorted lexicographically by row key. The only efficient filter in Bigtable — all queries are key-based or range scans.

**Column Family**: A group of related columns defined at table creation. Column families have their own garbage collection policies. Bigtable tables should have a small number of column families (one to three).

**Column Qualifier**: The name of a specific column within a column family. Column qualifiers are dynamic — they do not need to be declared at table creation. New qualifiers can be added when writing data.

**Cell**: The intersection of a row key, column family, and column qualifier. Stores a single byte string value with a timestamp.

**Timestamp**: The version dimension of a cell. Each write to a cell creates a new version. Bigtable can store and retrieve multiple timestamped versions of each cell value.

**Garbage Collection (GC) Policy**: A per-column-family rule that specifies when to delete old cell versions. Two types: maxversions (keep latest N versions) and maxage (delete versions older than N duration).

**Tablet**: A contiguous range of rows in a Bigtable table. Tablets are automatically split as they grow and balanced across cluster nodes.

**Hotspot**: A performance bottleneck where many reads or writes concentrate on a narrow row key range, causing one or a few tablets to receive disproportionate load.

**Bigtable Instance**: The top-level resource containing one or more clusters and databases (tables). Instances are classified as PRODUCTION or DEVELOPMENT.

**Bigtable Cluster**: A group of nodes in a single GCP zone that serve requests for a Bigtable instance. Each instance can have up to eight clusters in different zones or regions.

**Node**: A compute resource in a Bigtable cluster. Throughput scales linearly with node count — approximately 10,000 rows/second per node for typical workloads.

**Colossus**: Google's distributed file system. Bigtable stores data on Colossus separately from compute nodes. Allows instant node scaling without data migration.

**App Profile**: A Bigtable configuration that controls which cluster handles requests and with what routing policy. Used to implement multi-cluster routing for high availability.

**Multi-Cluster Routing**: An App Profile setting that allows Bigtable to route requests to any available cluster. Used for automatic failover and geographic load distribution.

**Single-Cluster Routing**: An App Profile setting that pins requests to a specific cluster. Used when consistent single-cluster behavior is needed (e.g., strong-consistency dependent workflows).

**cbt CLI**: The command-line tool for interacting with Cloud Bigtable. Used for creating tables, reading/writing rows, and managing column families and GC policies.

**Key Visualizer**: A Bigtable diagnostic tool that shows read/write activity as a heatmap across the row key space. Used to identify hotspots and uneven access patterns.

**HBase API**: The open-source API that Cloud Bigtable is compatible with. Applications written for Apache HBase can run against Cloud Bigtable with minimal changes.

**Replication**: A Cloud Bigtable feature that asynchronously copies data between clusters. Provides high availability and geographic read distribution.

---

### 2. Bigtable Data Model vs. Relational Model

| Concept | Relational (Cloud SQL) | Bigtable |
|---|---|---|
| Primary lookup | Primary key or index | Row key only |
| Schema flexibility | Fixed columns per table | Dynamic column qualifiers per row |
| JOIN support | Full SQL JOINs | None |
| Multi-row transactions | Full ACID | None |
| Query language | SQL | Key-based API; limited filtering |
| Data size sweet spot | MB to tens of TB | TB to PB |
| Latency | Milliseconds to tens of ms | Single-digit milliseconds at scale |
| Throughput | Thousands of QPS | Millions of rows/second |

---

### 3. Row Key Design Patterns Reference

| Pattern | Description | Use Case |
|---|---|---|
| Sequential timestamp (anti-pattern) | Raw timestamp as leading key component | Never — creates hotspot |
| Sequential integer (anti-pattern) | Auto-increment integer as row key | Never — creates hotspot |
| Reversed timestamp | Large_constant - timestamp | Time-series newest-first range scans |
| Reversed domain name | `com.google.www` instead of `www.google.com` | Web indexing, DNS lookup data |
| Composite key | `entityId#reversedTimestamp` | Entity-time-series (sensor, user, instrument) |
| Salted prefix | Hash prefix + natural key | Distributes uniform writes across tablets |
| UUID | Random 128-bit identifier | Maximum distribution; no range scan by time |

---

### 4. Workload Selection: Bigtable vs. Other GCP Services

| Workload Characteristic | Best Service |
|---|---|
| High-throughput time-series at petabyte scale | Cloud Bigtable |
| IoT telemetry from millions of devices | Cloud Bigtable |
| OLTP with SQL JOINs, single region | Cloud SQL |
| OLTP with SQL JOINs, global | Cloud Spanner |
| Document storage, mobile/web app backend | Firestore |
| Data warehouse, SQL analytics | BigQuery |
| Caching, session storage | Memorystore |
| Less than 300 GB of data | Cloud SQL (Bigtable not cost-justified) |

---

### 5. Column Family Design Guidelines

| Rule | Explanation |
|---|---|
| Keep families to 1–3 per table | Bigtable is optimized for few families with many dynamic qualifiers |
| Group by access pattern | Columns read together should be in the same family; rarely-read columns in a separate family |
| Set GC policies | Always configure garbage collection; unbounded version growth consumes storage |
| Do not use one family per attribute | This is a relational modeling anti-pattern for Bigtable |

---

### 6. Bigtable Performance Characteristics

| Metric | Value |
|---|---|
| Read/write latency (p50) | Single-digit milliseconds |
| Write throughput per node | ~10,000 rows/second (1 KB rows) |
| Read throughput per node | ~10,000 rows/second (1 KB rows) |
| Scan throughput per node | ~220 MB/second |
| Maximum row size | 256 MB (but smaller rows are more efficient) |
| Maximum row key size | 4 KB |
| Maximum table size | Unlimited (petabyte-scale) |
| Maximum number of column families | 100 (practical limit: 1–3) |

---

### 7. gcloud and cbt CLI Reference

| Task | Command |
|---|---|
| Create instance | `gcloud bigtable instances create NAME --cluster=C --cluster-zone=Z --cluster-num-nodes=N` |
| Create table | `cbt createtable TABLE` |
| Create column family | `cbt createfamily TABLE FAMILY` |
| Set GC policy (versions) | `cbt setgcpolicy TABLE FAMILY maxversions=N` |
| Set GC policy (age) | `cbt setgcpolicy TABLE FAMILY maxage=Nd` |
| Write a row | `cbt set TABLE ROWKEY FAMILY:QUALIFIER=VALUE` |
| Read a row | `cbt read TABLE prefix="ROWKEY"` |
| Range scan | `cbt read TABLE prefix="PREFIX"` |
| List tables | `cbt ls` |
| Delete instance | `gcloud bigtable instances delete INSTANCE` |

---

### 8. Required Readings and Resources

**GCP Documentation — Cloud Bigtable Overview**: Architecture, use cases, and conceptual introduction. Available at cloud.google.com/learn.

**GCP Documentation — Cloud Bigtable Schema Design**: Row key design best practices, column family guidelines, and anti-patterns. Available at cloud.google.com/learn.

**GCP Documentation — Cloud Bigtable Performance**: Node sizing guidelines, throughput expectations, and Key Visualizer usage. Available at cloud.google.com/learn.

---

### 9. Exam Tips

Tip 1: when a scenario describes petabyte-scale, high-throughput time-series or IoT data with key-based access, Bigtable is the answer. When it describes SQL JOINs or multi-row ACID transactions, Bigtable is wrong.

Tip 2: Bigtable has no secondary indexes. All efficient queries are row key scans. This is the most frequently tested Bigtable design constraint.

Tip 3: sequential timestamps or incrementing integers as leading row key components create hotspots. The exam presents hotspot symptoms (slow writes despite sufficient nodes) and the answer is always row key redesign.

Tip 4: column qualifiers are dynamic; column families are defined at table creation. There should be one to three column families, not one per data attribute.

Tip 5: garbage collection is per column family. Configure maxversions or maxage. Without GC, all cell versions are retained forever.

Tip 6: Bigtable replication is asynchronous — eventually consistent. Not appropriate for applications that require reading a write immediately after it is committed.

Tip 7: Bigtable vs. BigQuery: Bigtable is for operational high-throughput key-based reads and writes. BigQuery is for analytical queries over large historical datasets. Both scale to petabytes but serve entirely different access patterns.

Tip 8: the minimum effective data size for Bigtable is approximately 1 TB. For smaller datasets, the cost does not justify Bigtable's capabilities — Cloud SQL or Firestore would be more appropriate.

---

### 10. Study Checklist

- Describe the five components of the Bigtable data model: row key, column family, column qualifier, cell, timestamp
- Explain why a leading timestamp in a Bigtable row key creates a hotspot
- Design a row key for an IoT sensor table that allows efficient per-sensor time-range scans
- Explain the difference between column families and column qualifiers
- State why Bigtable has no secondary indexes and what that means for query design
- Explain what a Bigtable garbage collection policy does and when to use maxversions vs. maxage
- Describe how Bigtable replication works and what consistency model it provides
- Write gcloud and cbt commands to create an instance, table, column families, and insert a row
- Identify three workload types where Bigtable is appropriate and three where it is not
- Complete the Module 05 lab activity
- Pass the Module 05 quiz with at least 80 percent

---

Reference: cloud.google.com/learn

---

## 9. Supplemental Resources

**1. Cloud Bigtable — Official Documentation: Schema Design Best Practices**
https://cloud.google.com/bigtable/docs/schema-design
Google's canonical guide for row key design, column family design, avoiding hotspots, and GC policy configuration in Cloud Bigtable.

**2. Cloud Bigtable Key Visualizer — Documentation**
https://cloud.google.com/bigtable/docs/keyvis-overview
Explains how to read Key Visualizer heatmaps, interpret hotspot signatures, and use the tool to diagnose uneven read/write distribution in production Bigtable tables.

**3. Bigtable Whitepaper — Chang et al., Google (2006)**
https://research.google/pubs/pub27898/
The original academic paper describing the Bigtable wide-column storage model, tablet architecture, and compaction design — foundational reading for understanding Bigtable's internals at the exam level.

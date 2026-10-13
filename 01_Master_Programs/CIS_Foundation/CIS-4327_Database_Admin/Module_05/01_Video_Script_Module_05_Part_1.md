# Video Script: Module 05 — Bigtable: Wide-Column NoSQL at Scale (Part 1)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 13–15 minutes

---

### Opening

**[SHOW SLIDE: Module 05 — Cloud Bigtable: Wide-Column NoSQL at Scale]**

Hello, and welcome back to CIS-4327. I am Professor Nash. This is Module 05: Cloud Bigtable.

Bigtable is not a relational database. It does not have tables with foreign keys, JOINs, or transactions that span multiple rows. What it does have is massive horizontal scalability, single-digit millisecond read and write latency at petabyte scale, and a storage model designed for exactly one class of workloads: high-throughput, low-latency access to huge volumes of data organized by a single key.

Understanding Bigtable is essential for the GCP exam because its data model is fundamentally different from everything we have covered so far, and the exam tests your ability to identify workloads where Bigtable is appropriate versus where Cloud SQL or Spanner would be used instead.

In Part 1 we cover Bigtable's architecture, data model, row key design, and the types of workloads it is built for. In Part 2 we cover schema design patterns, cluster scaling, replication, and exam scenarios.

---

### Section 1 — What Is Bigtable?

**[SHOW SLIDE: Bigtable origin — Google's internal infrastructure for Search indexing, Maps, Gmail]**

Cloud Bigtable is the managed version of the Bigtable system Google built internally starting in 2004 to power Google Search's web index, Google Maps, and Gmail. The original Bigtable paper, published in 2006, described a distributed storage system for structured data designed to handle petabytes of data across thousands of commodity servers.

Cloud Bigtable made this infrastructure available as a managed GCP service. You get the same storage system without managing the cluster hardware, replication, or compaction processes yourself.

Bigtable is a key-value store with a sorted structure. Every row has a unique row key, and rows are sorted lexicographically by that key. Within a row, values are organized into column families and column qualifiers.

---

### Section 2 — Bigtable Data Model

**[SHOW SLIDE: Bigtable data model diagram — row key, column family, column qualifier, cell, timestamp]**

The Bigtable data model has five components.

The row key is a byte string of up to 4 KB. It is the only thing you can efficiently filter on — Bigtable has no secondary indexes and cannot efficiently search by any column. Every query either reads a single row by exact key or scans a contiguous range of rows sorted by key.

Column families group related columns together. They are defined at table creation time and are part of the schema. Examples: cf_metrics, cf_metadata.

Column qualifiers are the names of individual columns within a family. Unlike in a relational database, column qualifiers do not need to be declared in advance. You can add new qualifiers dynamically when writing data.

Cells are the intersection of a row and a column (family:qualifier). Each cell stores a value, which is an arbitrary byte string.

Timestamps add a versioning dimension to each cell. By default, Bigtable retains multiple versions of a cell value over time. You can read the most recent version, a specific timestamp version, or a range of versions.

**[SHOW SLIDE: Sparse table — most cells are empty in wide rows]**

An important characteristic: Bigtable tables are sparse. A row does not need to have values in every column qualifier. Empty cells consume no storage. This makes Bigtable efficient for workloads where different rows have different sets of columns.

---

### Section 3 — Bigtable Architecture

**[SHOW SLIDE: Bigtable architecture — cluster nodes, tablets, persistent disk, Colossus storage]**

A Bigtable instance consists of one or more clusters. Each cluster runs in a single GCP zone. A cluster has nodes that serve read and write requests. Data is stored on Colossus — Google's distributed file system — separately from the compute nodes.

This separation of compute and storage means adding nodes to a Bigtable cluster does not require moving data. Adding a node immediately increases throughput capacity. It also means that if a node fails, another node takes over serving the data from Colossus with no data loss.

Data within a table is divided into tablets. A tablet is a contiguous range of rows. Tablets are automatically split as they grow and balanced across the cluster nodes. This automatic load balancing is why row key design matters: if all your writes go to a narrow range of row keys, all those tablets end up on the same node — creating a hotspot identical to what we saw with sequential keys in Spanner.

---

### Section 4 — Row Key Design

**[SHOW SLIDE: Row key design — the most important Bigtable design decision]**

Row key design is the most critical decision in Bigtable schema design. Because all reads and range scans are based exclusively on the row key, your key structure determines everything about query efficiency and write distribution.

The primary goal of row key design is to avoid hotspots while enabling the range scan patterns your application needs.

Anti-pattern: using a timestamp as the leading key component. If your row key is just a timestamp, all new writes have the highest timestamp value and accumulate on the last tablet. Every node except one is idle for writes — a classic hotspot.

Anti-pattern: using a monotonically increasing integer as the row key. Same problem as timestamp.

Good pattern — field reversal: if you need to query by domain name, reverse the components. Instead of `www.google.com`, use `com.google.www`. All subdomains of `com.google` sort together, enabling efficient range scans.

Good pattern — salting: prepend a random or hash-based prefix to distribute writes across nodes while still allowing grouped range scans.

Good pattern — composite keys for multi-dimensional access: for IoT sensor data, a key like `sensorId#reversedTimestamp` groups all readings for one sensor together in descending time order. You can range-scan the most recent N readings for a sensor efficiently.

**[SHOW SLIDE: Bigtable row key examples — IoT, user events, web index, time series]**

| Workload | Recommended Row Key Pattern |
|---|---|
| IoT sensor readings | `sensorId#reversedTimestamp` |
| User activity events | `userId#reversedTimestamp` |
| Web index | Reversed domain name prefix |
| Financial time series | `instrumentId#reversedTimestamp` |
| Ad click tracking | `advertiserId#reversedTimestamp#randomSuffix` |

---

### Section 5 — Bigtable Workloads

**[SHOW SLIDE: Workloads suited for Bigtable — time series, IoT, recommendation data, operational data]**

Bigtable is the right choice for these workload patterns:

Time series data: billions of sensor readings, financial tick data, or log events where you need fast writes and range scans by key.

IoT data: high-volume telemetry from connected devices with millions of sensors writing concurrently.

Recommendation systems: large-scale feature stores or user-item matrices where the data is too large for an in-memory system.

Marketing and analytics data: storing user profiles, behavioral signals, or advertising data that is read and updated at very high throughput.

Bigtable is not the right choice for:

Workloads that require SQL JOINs or multi-row transactions with strong ACID semantics.

Workloads with less than 1 TB of data or fewer than 300 GB of reads/writes per day — below this threshold, the cost and operational overhead of Bigtable is not justified.

Ad-hoc analytical queries — BigQuery is the correct choice for that pattern.

---

### Closing — Part 1 Summary

**[SHOW SLIDE: Module 05 Part 1 key concepts]**

In Part 1 we covered Bigtable's architecture: clusters, nodes, tablets, and Colossus storage. We covered the data model: row key, column family, column qualifier, cell, and timestamp versioning.

We covered row key design — the most important Bigtable design decision — including the hotspot anti-patterns (leading timestamp or sequential integer) and the recommended patterns (reversed field, salted prefix, composite key with reversed timestamp).

We identified the workload types where Bigtable is the correct choice: time series, IoT, recommendation, and high-throughput operational data.

In Part 2 we cover Bigtable schema design patterns in more depth, cluster replication, performance optimization, and exam scenarios.

See you in Part 2.

---

Reference: cloud.google.com/learn

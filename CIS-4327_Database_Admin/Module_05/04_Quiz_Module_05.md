# Quiz: Module 05 — Bigtable: Wide-Column NoSQL at Scale

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis follows each question.

---

### Question 1

An energy company collects power consumption readings from 5 million smart meters every 60 seconds. The data totals 3 TB per day and must be retained for 5 years. The application requires individual meter lookups and time-range scans per meter with single-digit millisecond latency. Which GCP database service is most appropriate?

- A) Cloud Bigtable
- B) Cloud SQL for PostgreSQL
- C) Cloud Spanner
- D) BigQuery

Correct Answer: A — Cloud Bigtable is purpose-built for high-throughput time-series data from many devices with key-based range scan access patterns. The scale (3 TB/day over 5 years) and access pattern (per-meter time-range scans) match Bigtable's design exactly.

Distractor analysis: B is incorrect because Cloud SQL cannot efficiently handle petabyte-scale time-series data at millions of rows per minute; it is sized for regional OLTP workloads measured in tens of TB. C is incorrect because Cloud Spanner is appropriate for globally consistent relational OLTP; this workload needs high-throughput key-based writes without SQL JOINs, making Spanner an expensive over-engineering. D is incorrect because BigQuery is an analytical data warehouse for batch queries over historical data; it does not provide single-digit millisecond latency for individual row lookups.

---

### Question 2

A data engineer designs a Bigtable table for user event tracking. The row key is defined as `userId#eventTimestamp` where eventTimestamp is in ascending chronological order. After six months in production, write throughput has degraded and Key Visualizer shows a bright band at the end of the row key space. What is the most likely cause?

- A) New events always have the highest timestamp, concentrating all writes on the tablet holding the highest key range and creating a hotspot.
- B) The userId prefix is too short, causing row key collisions on the first character.
- C) Bigtable has reached its maximum table size and needs additional storage nodes.
- D) The column family GC policy is retaining too many versions, slowing down compaction.

Correct Answer: A — Using an ascending timestamp as the trailing (or leading) component of a row key concentrates new writes at the lexicographic end of the key space. All current events have the highest timestamp values, so they are written to the same tablet. A bright band at the end of the key space in Key Visualizer is the classic hotspot signature.

Distractor analysis: B is incorrect because row key collisions would prevent data from being written correctly; the symptom would be data corruption or overwrite errors, not degraded throughput. C is incorrect because Bigtable storage scales independently of nodes; adding nodes increases throughput, not storage capacity, and there is no practical storage limit. D is incorrect because GC policy affects storage and read efficiency but does not concentrate writes; the Key Visualizer hotspot pattern specifically indicates a write distribution problem.

---

### Question 3

A Bigtable table schema includes a column family `cf_raw` for sensor readings and a column family `cf_summary` for daily aggregated values. The team wants to keep the most recent 1,000 versions of raw readings but delete summary values older than 365 days. How should the garbage collection policies be configured?

- A) Set `cf_raw` to `maxversions=1000` and set `cf_summary` to `maxage=365d`.
- B) Set both families to `maxversions=1000` and use a cron job to delete old summaries.
- C) Set `cf_raw` to `maxage=1000d` and set `cf_summary` to `maxversions=365`.
- D) Garbage collection policies apply to the entire table; you cannot set different policies per column family.

Correct Answer: A — Cloud Bigtable garbage collection policies are configured per column family, which is exactly what allows different retention rules for different data types. `maxversions=1000` retains the 1,000 most recent versions for raw data, and `maxage=365d` deletes summary values that are more than one year old.

Distractor analysis: B is incorrect because using a cron job for deletion adds operational complexity unnecessarily; Bigtable's built-in GC handles this automatically, and setting maxversions=1000 on both families does not address the age-based retention requirement for summaries. C is incorrect because the values are swapped — raw data should be controlled by version count (how many readings to keep), not age, and summary data should be controlled by age, not version count. D is incorrect because GC policies are per column family by design; this is one of Bigtable's key schema design features.

---

### Question 4

A developer proposes the following Bigtable schema for storing product catalog data: one column family for every product attribute (cf_name, cf_price, cf_category, cf_description, cf_weight, cf_dimensions). What is the primary design problem?

- A) Bigtable is optimized for a small number of column families (one to three); creating one family per attribute creates unnecessary overhead.
- B) Column families cannot store string values; all values must be binary-encoded.
- C) A separate table is required for each column family in Cloud Bigtable.
- D) This design violates First Normal Form because product attributes are not atomic.

Correct Answer: A — Cloud Bigtable is optimized for one to three column families with many dynamic column qualifiers within each family. Creating one family per attribute imposes overhead on every read (each family is a separate storage unit) and violates the design principle of grouping related data. The correct design uses one or two families with the attributes as column qualifiers.

Distractor analysis: B is incorrect because Bigtable stores values as byte strings, which can represent any data including strings; there is no restriction to binary-only values. C is incorrect because a Bigtable table can have multiple column families; each family is a partition within a table, not a separate table resource. D is incorrect because First Normal Form applies to relational schema design; Bigtable's wide-column model is a different data model entirely, and normalization rules do not apply.

---

### Question 5

Which of the following is not supported by Cloud Bigtable?

- A) SQL JOIN operations across two Bigtable tables
- B) Storing multiple timestamped versions of a cell value
- C) Dynamic column qualifiers that vary per row
- D) Petabyte-scale storage with single-digit millisecond read latency

Correct Answer: A — Cloud Bigtable does not support SQL JOINs or any cross-table relational operations. All queries in Bigtable are based on single-table key lookups or range scans. JOINs require a relational database (Cloud SQL, Cloud Spanner, BigQuery).

Distractor analysis: B is incorrect because multi-version cell storage with timestamps is a core feature of Bigtable; each write creates a new versioned cell. C is incorrect because dynamic column qualifiers are one of Bigtable's design advantages — qualifiers do not need to be declared at schema creation time. D is incorrect because petabyte-scale storage with low latency is precisely what Bigtable is designed for.

---

### Question 6

A Bigtable cluster with 3 nodes is handling 25,000 rows per second and CPU utilization is at 70%. The team expects traffic to double next month. What is the correct scaling action?

- A) Increase the cluster to 6 nodes; Bigtable throughput scales linearly with node count.
- B) Create a read replica cluster and distribute traffic across both clusters.
- C) Upgrade to Cloud SQL Enterprise Plus for higher throughput capacity.
- D) Partition the table into two tables and route 50% of requests to each.

Correct Answer: A — Bigtable throughput scales linearly with the number of nodes in a cluster. The cluster currently handles 25,000 rows/second at 3 nodes (~8,300 rows/second per node at 70% utilization). Doubling the node count to 6 proportionally doubles throughput, providing headroom for the expected 2x traffic increase.

Distractor analysis: B is incorrect because adding a replication cluster provides high availability and geographic distribution but does not double the throughput of a single cluster linearly the same way adding nodes does; write throughput still flows through the primary cluster. C is incorrect because Cloud SQL is a relational database for different workloads; there is no migration path that preserves Bigtable semantics. D is incorrect because manually partitioning a Bigtable table adds significant application complexity; Bigtable handles tablet splitting and node-based scaling automatically.

---

### Question 7

An application reads a Bigtable row and receives a value of 72.4 for `cf_metrics:temperature`. The application writes a new value of 73.1 to the same cell. The column family GC policy is `maxversions=1`. What happens to the original value 72.4?

- A) The value 72.4 is retained until the next Bigtable compaction operation runs, then it is deleted by the GC policy.
- B) The value 72.4 is immediately overwritten and permanently deleted.
- C) Both values 72.4 and 73.1 are stored as separate versions indefinitely.
- D) Writing to a cell that already has data requires a DELETE statement first.

Correct Answer: A — Bigtable writes always create a new cell version; the write does not immediately overwrite the old value. With maxversions=1, the GC policy marks the older version (72.4) for deletion. The actual deletion occurs during the next compaction operation that processes that tablet. Until compaction, both versions may exist in storage, but reads return only the most recent version.

Distractor analysis: B is incorrect because Bigtable does not immediately delete old versions on write; deletion is deferred to compaction. However, reads do return only the latest version — the old value is not visible even though it may still be in storage briefly. C is incorrect because the maxversions=1 GC policy specifically limits retention to 1 version; both versions are not stored indefinitely. D is incorrect because Bigtable cells do not require a prior DELETE before writing a new value; the write API simply creates a new versioned entry.

---

### Question 8

What is the purpose of the Key Visualizer tool in Cloud Bigtable?

- A) It displays a heatmap of read and write activity across the row key space over time, helping identify hotspots and uneven access patterns.
- B) It validates that row keys conform to the naming conventions defined in the table schema.
- C) It automatically reformats row keys to eliminate hotspots without requiring table migration.
- D) It generates a histogram of column qualifier usage to identify unused columns.

Correct Answer: A — Key Visualizer displays a two-dimensional heatmap where the X-axis is time and the Y-axis is the row key space. Color intensity indicates read or write activity. A hotspot appears as a bright band concentrated in one area of the Y-axis. This is the primary tool for diagnosing row key design problems in Bigtable.

Distractor analysis: B is incorrect because Bigtable does not enforce row key naming conventions; row keys are arbitrary byte strings and Key Visualizer does not validate them. C is incorrect because Key Visualizer is a read-only diagnostic tool; it does not modify row keys or table data. D is incorrect because Key Visualizer shows row key activity distribution, not column qualifier usage statistics.

---

### Question 9

A Bigtable instance has two clusters: one in us-central1-b and one in us-east1-c. An App Profile is configured with multi-cluster routing. What consistency model does reading from this instance provide?

- A) Eventual consistency — a write to one cluster may not be immediately visible when reading from the other cluster.
- B) Strong consistency — all reads reflect the most recent writes regardless of which cluster is queried.
- C) Read-your-writes consistency — a client always reads its own most recent writes from any cluster.
- D) Serializable consistency — all operations are globally ordered as if executed on a single machine.

Correct Answer: A — Bigtable replication between clusters is asynchronous. A write acknowledged by one cluster may take a brief period to replicate to the other cluster. Reads from the second cluster may return slightly stale data. This eventual consistency model is acceptable for time-series analytics but not for applications requiring immediate consistency after writes.

Distractor analysis: B is incorrect because strong consistency across clusters would require synchronous replication, which Bigtable does not provide; that is a characteristic of Cloud Spanner. C is incorrect because Bigtable's multi-cluster routing does not guarantee read-your-writes consistency when requests are routed across different clusters. D is incorrect because serializable consistency is a characteristic of relational databases like Cloud Spanner; Bigtable's NoSQL model does not provide global transaction ordering.

---

### Question 10

When should you use Cloud Bigtable instead of BigQuery for large-scale data storage?

- A) When the application requires operational, low-latency key-based reads and writes at high throughput rather than analytical batch queries.
- B) When the data requires complex GROUP BY aggregations and window functions that BigQuery does not support.
- C) When the data volume exceeds 1 TB, because BigQuery cannot store more than 1 TB per table.
- D) When the data has a relational schema that requires JOIN operations between multiple tables.

Correct Answer: A — Bigtable is an operational database for real-time, high-throughput, low-latency key-based reads and writes. BigQuery is an analytical data warehouse for complex SQL queries over large historical datasets. The key distinction is operational (real-time, low-latency) vs. analytical (batch, high-latency queries, complex aggregations).

Distractor analysis: B is incorrect because BigQuery fully supports GROUP BY, window functions, and virtually all SQL aggregations; it has more analytical query capability than Bigtable, not less. C is incorrect because BigQuery handles petabyte-scale tables routinely; the 1 TB claim is fabricated. D is incorrect because Bigtable does not support SQL JOINs at all; if relational joins are required, BigQuery (for analytics) or Cloud SQL/Spanner (for OLTP) would be used, not Bigtable.

---

Reference: cloud.google.com/learn

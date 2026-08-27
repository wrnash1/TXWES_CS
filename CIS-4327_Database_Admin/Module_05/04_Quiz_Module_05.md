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

---

### Question 11 (5 points)

A Bigtable row key is designed as `reverseTimestamp#sensorId` where reverseTimestamp = `MAX_LONG - currentTimestampMs`. What problem does this design solve?

- A) It prevents write hotspots by distributing new rows across the key space rather than appending to the lexicographic end.
- B) It ensures rows are sorted by sensor ID, making per-sensor scans more efficient.
- C) It enables JOINs between Bigtable tables by creating a shared key namespace.
- D) It reduces storage size because reversed timestamps are shorter than forward timestamps.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Placing reverseTimestamp as the first key component means rows are sorted by timestamp (reversed), not by sensor ID; per-sensor scans require a full table scan unless the prefix is the sensor ID.
  - C) Bigtable does not support JOINs between tables regardless of key design; the key format has no effect on cross-table operations.
  - D) A reversed timestamp is the same byte length as a forward timestamp; no storage reduction occurs.

---

### Question 12 (5 points)

A Bigtable table stores financial transaction records. A compliance audit requires retrieving all transactions for a specific account (account_id = `ACC001`) between 2025-01-01 and 2025-03-31. The row key is `account_id#YYYYMMDD#transaction_id`. Which Bigtable read operation most efficiently retrieves these rows?

- A) A range scan with start key `ACC001#20250101` and end key `ACC001#20250331~` to retrieve only the matching key prefix range.
- B) A full table scan with a row filter matching `account_id = ACC001` and date between 2025-01-01 and 2025-03-31.
- C) A SQL SELECT query: `SELECT * FROM transactions WHERE account_id = 'ACC001' AND date BETWEEN '2025-01-01' AND '2025-03-31'`.
- D) A batch of individual row lookups, one per day in the date range (90 individual reads).

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) A full table scan reads every row and applies a filter; with the correct row key design, a range scan reads only the relevant subset without scanning the entire table, making it far more efficient.
  - C) Bigtable does not support SQL SELECT syntax; all reads use the Bigtable client API with row key lookups and range scans.
  - D) Individual row lookups for each day would require knowing exact row keys for each day and does not efficiently retrieve transactions within a continuous date range using the natural key ordering.

---

### Question 13 (5 points)

A Bigtable cluster's CPU utilization is at 85%. The team wants to add replication to a second cluster in a different region for disaster recovery. After adding the second cluster, what effect does this have on write throughput capacity?

- A) Write throughput is unchanged; each cluster still processes its own writes, and replication is asynchronous; adding a replication cluster does not increase write throughput for the primary cluster.
- B) Write throughput doubles because writes are distributed between the two clusters automatically.
- C) Write throughput decreases slightly because each write must be synchronously replicated to the second cluster before acknowledging.
- D) Write throughput scales linearly with each new cluster added, identical to adding nodes within a single cluster.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Writes are not automatically load-balanced between clusters; each cluster processes writes directed to it; a replication cluster for DR is a hot standby, not a write-sharing partner.
  - C) Bigtable replication is asynchronous; writes are acknowledged before replication completes; there is no synchronous replication overhead.
  - D) Adding nodes within a cluster scales write throughput linearly; adding a new cluster for replication is a DR measure, not a throughput scaling action for the primary cluster.

---

### Question 14 (5 points)

Which Bigtable feature is used to automatically route read requests to the cluster with the lowest latency for a given client application?

- A) App Profile with multi-cluster routing enabled.
- B) Cloud Load Balancing configured in front of the Bigtable instance.
- C) A Bigtable secondary index on the row key field.
- D) Cloud CDN caching for frequently accessed rows.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud Load Balancing operates at the HTTP/TCP network layer and is not integrated with the Bigtable API routing; Bigtable routing is controlled through App Profiles.
  - C) Secondary indexes in Bigtable only exist as application-managed patterns (such as a lookup table); there is no built-in secondary index mechanism, and no index type controls cluster routing.
  - D) Cloud CDN caches HTTP responses from web applications; it has no integration with the Bigtable RPC API.

---

### Question 15 (5 points)

A Bigtable table uses column qualifier names as dynamic data (for example, storing a user's followed artist IDs as column qualifiers like `cf_follows:artist_12345`). What is the advantage of this pattern over storing the artist IDs as values in separate rows?

- A) It allows retrieving all followed artists for a user in a single row read without scanning multiple rows.
- B) It enables SQL GROUP BY queries on the qualifier names for analytics.
- C) It reduces the number of column families required to one per user.
- D) It allows the GC policy to apply a different maxversions per column qualifier.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Bigtable does not support SQL GROUP BY; analytical queries on qualifier names require exporting to BigQuery or processing in application code.
  - C) The number of column families is determined by the schema design, not by how many users exist; all users share the same column families in the same table.
  - D) GC policies in Bigtable are set at the column family level, not per individual column qualifier; you cannot set different maxversions per qualifier.

---

### Question 16 (5 points)

A Bigtable schema stores web clickstream events with row key `userId#reverseTimestamp`. A new requirement asks for efficient retrieval of all events of a specific event_type (e.g., `purchase`) across all users within the last 24 hours. How should this query be handled?

- A) This access pattern cannot be served efficiently by Bigtable alone with this key design; consider maintaining a secondary lookup table keyed on `event_type#reverseTimestamp#userId` for this query pattern.
- B) Add a `WHERE event_type = 'purchase'` filter clause to the Bigtable range scan API.
- C) Create a new column family `cf_purchase` and store only purchase events there; scan the column family.
- D) Use Bigtable's built-in full-text index on cell values to search for event_type = purchase.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) A value filter on `event_type` requires scanning all rows in the time range across all users; the row key is sorted by userId, not event_type, so Bigtable cannot use the key to skip non-matching rows efficiently.
  - C) Column families group related columns; they are not queryable in isolation for cross-user scans; a column family scan still reads all rows.
  - D) Bigtable has no built-in full-text index; all row retrieval is based on the row key or column filters that still require a range scan.

---

### Question 17 (5 points)

What happens to Bigtable storage when a cell value is deleted using the Bigtable `DeleteFromColumn` mutation?

- A) The delete is recorded as a tombstone marker; the actual storage is reclaimed during the next compaction operation.
- B) The storage is immediately freed and the cell is removed from the tablet.
- C) The cell value is set to NULL and the storage space is retained for the next write.
- D) The entire row containing that column qualifier is deleted automatically.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Bigtable uses a log-structured merge (LSM) storage model; deletes write tombstone markers rather than immediately removing data; physical reclamation happens during compaction.
  - C) Bigtable does not use NULL as a sentinel value; there is no NULL state for cell values; a deleted cell simply does not exist in subsequent reads.
  - D) A `DeleteFromColumn` mutation only removes the specified column qualifier from a row; it does not delete the entire row or other column qualifiers.

---

### Question 18 (5 points)

A team is choosing between Cloud Bigtable and Cloud Firestore for a gaming leaderboard application that stores player scores globally with millions of concurrent players. Which statement most accurately guides the selection?

- A) Bigtable is preferred for very high write throughput (millions of writes per second) at petabyte scale; Firestore is preferred for mobile/web client SDKs with real-time sync and offline support.
- B) Firestore is preferred because it supports SQL JOINs across player and score entities.
- C) Bigtable is preferred for mobile apps because it includes native iOS and Android client SDKs.
- D) Both services provide identical capabilities; the choice depends only on cost.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Firestore does not support SQL JOINs; it is a document database; the statement is factually incorrect.
  - C) Bigtable does not have native mobile SDKs; it is accessed through server-side client libraries; Firestore is the GCP service with native mobile SDK support.
  - D) Bigtable and Firestore have meaningfully different capabilities, consistency models, access patterns, and pricing structures; they are not interchangeable.

---

### Question 19 (5 points)

A Bigtable administrator notices that the average read latency has increased from 3ms to 45ms after a recent data load. Key Visualizer shows even distribution across the key space. What is the most likely cause?

- A) The cluster nodes are overloaded; the data-to-node ratio has grown and the cluster needs additional nodes.
- B) The row key design has a hotspot that Key Visualizer is not detecting.
- C) Bigtable compaction is running and temporarily blocking all reads.
- D) The GC policy is set to maxversions=1, causing excessive compaction overhead.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) The question explicitly states Key Visualizer shows even distribution; if distribution were uneven, Key Visualizer would show a bright band; even distribution rules out a hotspot.
  - C) Bigtable compaction runs in the background and does not block reads; it is a characteristic of the LSM storage model that reads and compaction operate concurrently.
  - D) maxversions=1 reduces the number of versions to compact, which would decrease compaction work; it would not increase read latency.

---

### Question 20 (5 points)

Which of the following correctly describes the relationship between a Bigtable instance, cluster, and table?

- A) An instance contains one or more clusters; each cluster is a set of nodes in a zone; tables are resources of the instance and their data is distributed across all clusters in the instance.
- B) An instance contains one table; additional tables require additional instances.
- C) A cluster contains multiple instances; each instance holds one table partition.
- D) Tables are defined per cluster; different clusters within the same instance can have different table schemas.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) A single Bigtable instance can contain many tables; instances are not limited to one table.
  - C) The hierarchy is instance → cluster → nodes; instances are the top-level resource containing clusters, not the other way around.
  - D) Tables are defined at the instance level and their data is automatically distributed and replicated across all clusters within the instance; clusters do not have independent table schemas.

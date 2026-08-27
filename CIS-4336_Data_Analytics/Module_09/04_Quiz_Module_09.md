# Quiz: Module 09 — Big Data Technologies

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 20 (2 points each)

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 1: Data Concepts and Environments

---

## Instructions

Select the single best answer for each question. Each question is worth 2 points. No partial credit.

---

## Question 1

Which of the 5 V's of big data refers to the speed at which data is generated and must be processed?

A. Volume

B. Veracity

C. Velocity

D. Variety

**Correct Answer:** C — Velocity describes the rate of data generation and the speed required for processing (e.g., millions of sensor events per second). Volume refers to data scale (A). Veracity refers to data trustworthiness (B). Variety refers to the diversity of data formats (D).

---

## Question 2

In HDFS, which node is responsible for tracking where each data block is stored across the cluster?

A. DataNode

B. NameNode

C. Secondary NameNode

D. JobTracker

**Correct Answer:** B — The NameNode is the HDFS master node that maintains all filesystem metadata, including which blocks make up each file and which DataNodes hold each block. DataNodes store the actual data blocks (A). The Secondary NameNode merges edit logs but is not a failover master (C). JobTracker is a MapReduce component, not an HDFS component (D).

---

## Question 3

What is the default block size in HDFS and the default replication factor?

A. 64 MB block size, 2 replicas

B. 128 MB block size, 3 replicas

C. 256 MB block size, 3 replicas

D. 128 MB block size, 5 replicas

**Correct Answer:** B — HDFS uses 128 MB as the default block size and replicates each block 3 times across different DataNodes. These specific values are frequently tested on the Data+ exam.

---

## Question 4

In MapReduce, what does the Map phase produce?

A. Final aggregated results written to HDFS

B. Key-value pairs emitted from processing local data blocks

C. Sorted and grouped data ready for output

D. A list of available DataNodes for task assignment

**Correct Answer:** B — The Map function processes data on local nodes and emits intermediate key-value pairs (e.g., `(word, 1)` in word count). The Reduce phase produces final aggregated results (A). The Shuffle/Sort phase groups key-value pairs (C). DataNode assignment is handled by YARN/the resource manager (D).

---

## Question 5

What is the primary reason Apache Spark is significantly faster than MapReduce for iterative workloads?

A. Spark uses more powerful hardware nodes than MapReduce

B. Spark processes data in memory rather than writing intermediate results to disk between stages

C. Spark uses a smaller block size than HDFS, reducing data transfer overhead

D. Spark automatically increases the replication factor for frequently accessed data

**Correct Answer:** B — Spark keeps intermediate computation results in RAM across stages, avoiding the disk I/O that MapReduce requires between every Map and Reduce phase. This in-memory processing is the fundamental architectural advantage. The other options describe hardware choices or HDFS behaviors unrelated to Spark's processing model.

---

## Question 6

Which Spark abstraction is an immutable, partitioned collection of data distributed across a cluster that can be reconstructed from its transformation lineage if a partition is lost?

A. DataFrame

B. Dataset

C. Resilient Distributed Dataset (RDD)

D. Spark SQL table

**Correct Answer:** C — The RDD is the foundational Spark abstraction with the lineage-based fault tolerance mechanism. DataFrames and Datasets are higher-level structured abstractions built on top of RDDs (A, B). Spark SQL tables are a query interface, not the underlying distributed data structure (D).

---

## Question 7

An organization needs to store structured, cleaned, and modeled data optimized for SQL-based BI reporting with strong data governance. Which storage architecture is most appropriate?

A. Data lake

B. Data warehouse

C. HDFS raw storage

D. Apache Kafka topic

**Correct Answer:** B — A data warehouse stores structured, governed, schema-on-write data optimized for SQL analytics and BI reporting. A data lake stores raw unstructured data with schema-on-read (A). HDFS is raw distributed storage without query optimization or governance (C). Kafka is a streaming message platform, not a storage architecture for BI queries (D).

---

## Question 8

Which term describes the risk that a data lake becomes difficult to use because data is stored without catalogs, quality controls, or governance — making it impossible to find or trust data?

A. Data latency

B. Schema drift

C. Data swamp

D. Data skew

**Correct Answer:** C — A data swamp is a data lake that has become unusable due to lack of governance, metadata management, and data quality controls. Data latency refers to processing delay (A). Schema drift refers to source schema changes over time (B). Data skew describes uneven data distribution across partitions (D).

---

## Question 9

A credit card company needs to detect and block fraudulent transactions within 200 milliseconds of a transaction occurring. Which processing approach is required?

A. Batch processing with nightly reconciliation

B. Weekly scheduled aggregation jobs

C. Real-time streaming processing

D. Monthly MapReduce reporting jobs

**Correct Answer:** C — Detecting fraud within 200 milliseconds requires event-driven streaming processing (e.g., Apache Kafka plus Spark Streaming or Apache Flink). Batch and scheduled jobs (A, B, D) all have latency measured in minutes to hours — far too slow to block a transaction in real time.

---

## Question 10

Which architecture combines a batch layer for historical accuracy with a speed layer for real-time low-latency processing, merging both in a serving layer?

A. Kappa architecture

B. Lambda architecture

C. Medallion architecture

D. Star schema architecture

**Correct Answer:** B — The lambda architecture uses three layers: a batch layer (high accuracy, high latency), a speed layer (low latency, approximate), and a serving layer that merges both for queries. The kappa architecture eliminates the batch layer and uses only a streaming layer (A). Medallion is a data organization pattern for data lakes (C). Star schema is a dimensional modeling pattern for data warehouses (D).

---

## Question 11 (5 points)

A retail company processes 10 TB of daily transaction logs. They need to run nightly sales reports and historical trend analysis. Which big data processing model is most appropriate?

A. Real-time streaming with Apache Kafka

B. Batch processing with MapReduce or Spark scheduled jobs

C. In-memory caching with Redis

D. Lambda speed layer only

**Correct Answer:** B — Nightly reports and historical trend analysis are batch workloads — data accumulates and is processed on a schedule. Batch processing (MapReduce or Spark) is the correct model. Real-time streaming (A) is for sub-second latency requirements, not overnight reports. Redis caching (C) is not a processing framework for large-scale analytics. Using only the speed layer (D) sacrifices the historical accuracy that batch provides.

---

## Question 12 (5 points)

In the context of the Kappa architecture, what is the key design difference from Lambda architecture?

A. Kappa uses a data warehouse instead of a data lake

B. Kappa eliminates the batch layer and uses a single streaming pipeline for both real-time and historical processing

C. Kappa adds a dedicated machine learning layer on top of Lambda

D. Kappa uses HDFS exclusively, while Lambda supports any storage system

**Correct Answer:** B — Kappa architecture simplifies Lambda by eliminating the separate batch layer. All data — historical and current — flows through a single streaming pipeline, reducing system complexity. It does not involve data warehouse architecture (A), add ML layers (C), or restrict storage to HDFS (D).

---

## Question 13 (5 points)

Which component of Apache Spark is specifically designed for processing continuous data streams, enabling windowed aggregations and event-time processing?

A. Spark SQL

B. Spark MLlib

C. Spark GraphX

D. Spark Structured Streaming

**Correct Answer:** D — Spark Structured Streaming is the Spark component for processing real-time data streams with support for windowed aggregations and event-time semantics. Spark SQL handles batch query processing (A). MLlib is the machine learning library (B). GraphX is for graph computation (C).

---

## Question 14 (5 points)

A DataNode fails in an HDFS cluster with a replication factor of 3. What happens to the data blocks that were stored on the failed node?

A. The data is permanently lost because the failed node held the only copy

B. The NameNode detects the missing replicas and instructs surviving DataNodes to create additional copies to restore the replication factor

C. The Secondary NameNode automatically takes over all block responsibilities from the failed DataNode

D. MapReduce jobs pause until the failed DataNode is manually replaced

**Correct Answer:** B — HDFS fault tolerance works through replication. When a DataNode fails, the NameNode detects under-replicated blocks via heartbeat timeout and triggers re-replication to other DataNodes to restore the configured replication factor. Data is not lost if at least one replica survives (A). The Secondary NameNode manages edit logs, not data blocks (C). MapReduce/YARN re-schedules tasks on surviving nodes without requiring manual intervention (D).

---

## Question 15 (5 points)

An analyst runs a HiveQL query on a 500 GB dataset stored in HDFS. The query takes 45 minutes to complete. A colleague suggests converting the data to Apache Parquet format. Why would this likely reduce query time?

A. Parquet compresses data using ZIP compression, which reduces network bandwidth

B. Parquet is a columnar storage format that allows queries to read only the columns needed, skipping irrelevant data

C. Parquet automatically distributes data more evenly across DataNodes

D. Parquet converts HDFS to a row-oriented storage format optimized for full table scans

**Correct Answer:** B — Parquet stores data by column rather than by row. Analytical queries that read only a few columns out of many can skip entire column chunks on disk, dramatically reducing I/O. This is the core performance advantage of columnar formats for analytics. Parquet uses its own compression codecs (Snappy, GZIP), not ZIP (A). Parquet does not change data distribution (C). Parquet is columnar, not row-oriented (D).

---

## Question 16 (5 points)

Which of the following best describes schema-on-read as used in data lakes?

A. The data schema must be defined and enforced before any data is written to storage

B. Data is stored in its raw format and the schema is applied at query time based on the analytical need

C. All data in the lake must conform to a single master schema approved by the governance team

D. Schema-on-read means there is no schema at all — data lakes are completely unstructured

**Correct Answer:** B — Schema-on-read defers schema enforcement to query time, allowing raw data to be stored and interpreted differently for different analytical use cases. This contrasts with schema-on-write (used in data warehouses) where the schema is enforced at load time (A). Schema-on-read does not require a single master schema (C), and data can still have an implied structure — it is not completely schema-free (D).

---

## Question 17 (5 points)

What does the "Variety" dimension of the 5 V's of big data describe?

A. The total storage size of the dataset measured in petabytes

B. The degree to which data can be trusted and is free from errors

C. The diversity of data formats including structured, semi-structured, and unstructured data from multiple sources

D. The speed at which new data records are generated per second

**Correct Answer:** C — Variety refers to the wide range of data formats and types that big data systems must handle: relational tables (structured), JSON/XML (semi-structured), and text, images, audio (unstructured). Volume describes total data size (A). Veracity describes data trustworthiness (B). Velocity describes data generation speed (D).

---

## Question 18 (5 points)

A company wants to ingest social media posts, IoT sensor readings, and structured CRM records into a single platform, then run both SQL analytics and machine learning workloads on the data. Which architecture is the best fit?

A. A traditional relational data warehouse with star schema

B. A data lakehouse combining data lake storage with warehouse-style governance and query capabilities

C. An HDFS cluster with only MapReduce processing

D. A dedicated relational database for each data source type

**Correct Answer:** B — A data lakehouse combines the flexibility and low cost of data lake storage (handles structured, semi-structured, and unstructured data) with warehouse-style ACID transactions, schema enforcement, and SQL query performance. A traditional data warehouse is too rigid for unstructured social media and IoT data (A). HDFS with only MapReduce lacks ML library integration and SQL convenience (C). Separate databases per source create data silos (D).

---

## Question 19 (5 points)

In MapReduce, what is the purpose of the Shuffle and Sort phase that occurs between the Map and Reduce phases?

A. To write all intermediate Map output to HDFS for long-term archival

B. To group all values for the same key together and transfer them to the appropriate Reducer node

C. To apply a secondary Map function to filter low-frequency key-value pairs

D. To rank the Map output by value in descending order for the Reducer

**Correct Answer:** B — The Shuffle and Sort phase takes the intermediate key-value pairs emitted by all Mappers, groups all values with the same key together, and routes them to the Reducer responsible for that key. This is what makes MapReduce's parallel aggregation possible. The output is not archived to HDFS (A). There is no secondary Map function in standard MapReduce (C). Sorting is by key for grouping, not by value for ranking (D).

---

## Question 20 (5 points)

An engineer is designing a pipeline where Apache Kafka receives real-time clickstream events and Apache Spark Streaming processes them within seconds. What role does Kafka play in this architecture?

A. Kafka is the compute engine that applies transformations to each clickstream event

B. Kafka is a distributed message broker that buffers and durably stores event streams, decoupling producers from consumers

C. Kafka replaces HDFS as the long-term storage layer for processed results

D. Kafka is a query interface that allows SQL queries to be run against streaming data

**Correct Answer:** B — Apache Kafka is a distributed message broker (publish-subscribe system) that durably buffers event streams, allowing producers (website servers generating clicks) to be decoupled from consumers (Spark Streaming jobs). Kafka does not perform data transformations — Spark does (A). Kafka is not a long-term storage system like HDFS or a data lake (C). SQL on streams is handled by tools like Spark SQL or Apache Flink (D).

---

End of Module 09 Quiz

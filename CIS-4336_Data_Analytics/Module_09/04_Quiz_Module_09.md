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

End of Module 09 Quiz

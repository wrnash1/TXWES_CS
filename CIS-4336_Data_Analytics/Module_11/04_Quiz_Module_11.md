# Quiz: Module 11 - Big Data Concepts – Hadoop and Spark
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
A social media platform generates 500 million user events per day — likes, shares, comments, and views — arriving continuously in real time. The data includes structured fields (user ID, timestamp) as well as unstructured text (post content). Which of the "3 Vs of big data" are most clearly illustrated by this scenario?
*   A) Volume and validity — the dataset is large and the values must be verified before use.
*   B) Volume, velocity, and variety — the data is massive in scale, generated continuously at high speed, and combines structured and unstructured types.
*   C) Velocity and uniqueness — events arrive in real time and each event must have a unique identifier.
*   D) Variety and veracity — the data includes multiple types and its accuracy must be confirmed before analysis.
*   **Correct Answer:** B) Volume, velocity, and variety — the data is massive in scale, generated continuously at high speed, and combines structured and unstructured types.
*   **Distractor Analysis:**
    *   *Why correct:* 500 million daily events = volume. Continuous real-time arrival = velocity. Structured fields plus unstructured text = variety. All three of the defining big data Vs are present.
    *   A) "Validity" is a data quality dimension, not one of the 3 Vs. C) "Uniqueness" is also a data quality dimension, not a big data characteristic. D) "Veracity" is sometimes listed as a 4th V but is not one of the core 3 Vs; uniqueness is not a V at all. The scenario most directly illustrates all three classic Vs together.

---

**Question 2**
In big data architecture, which of the following most accurately defines **Apache Spark**?
*   A) A distributed file system that splits large files into blocks and replicates them across multiple nodes in a cluster to provide fault-tolerant storage at commodity hardware scale.
*   B) A batch-processing framework that executes a map phase — applying a function to each data chunk in parallel — followed by a reduce phase that aggregates the intermediate results to disk.
*   C) A fast, general-purpose distributed processing engine that performs computations primarily in memory rather than writing intermediate results to disk, making it significantly faster than disk-based MapReduce for iterative and interactive workloads.
*   D) A cloud-hosted relational database service that scales compute and storage independently and stores data in columnar format for fast analytical query performance.
*   **Correct Answer:** C) A fast, general-purpose distributed processing engine that performs computations primarily in memory rather than writing intermediate results to disk, making it significantly faster than disk-based MapReduce for iterative and interactive workloads.
*   **Distractor Analysis:**
    *   *Why C is correct:* Spark's defining characteristic is in-memory processing. By caching intermediate results in RAM instead of writing them to HDFS between each step, Spark achieves 10–100x speedups over MapReduce for iterative algorithms and interactive queries.
    *   *Why A is incorrect:* Splitting files into blocks replicated across nodes describes HDFS (Hadoop Distributed File System) — the storage layer of Hadoop, not Spark.
    *   *Why B is incorrect:* Map and reduce phases writing intermediate results to disk describes Hadoop MapReduce — the original Hadoop batch processing model that Spark improves upon.
    *   *Why D is incorrect:* A cloud-hosted columnar relational database describes a service like Amazon Redshift or Google BigQuery — a data warehouse product, not a distributed processing engine.

---

**Question 3**
A company receives three types of data daily: structured order records from a SQL database, semi-structured JSON clickstream events from its website, and raw unstructured server log files. A data engineer wants to store all three in a centralized repository in their original formats before any transformation. Which storage architecture is most appropriate?
*   A) A relational data warehouse with a predefined star schema, where each data type is mapped to a fact or dimension table before loading.
*   B) A data lake that accepts all data in its native format, applying schema only when data is read for analysis.
*   C) A NoSQL key-value store optimized for high-speed lookups of individual records by primary key.
*   D) A transactional OLTP database designed for insert-heavy workloads with row-level locking.
*   **Correct Answer:** B) A data lake that accepts all data in its native format, applying schema only when data is read for analysis.
*   **Distractor Analysis:**
    *   *Why B is correct:* A data lake is purpose-built for storing raw, heterogeneous data — structured, semi-structured, and unstructured — without requiring schema enforcement at ingestion ("schema on read"). This matches the requirement to preserve original formats before transformation.
    *   *Why A is incorrect:* A data warehouse enforces a predefined schema at load time ("schema on write") and is designed for cleaned, structured data. It cannot natively store raw unstructured logs or semi-structured JSON without transformation.
    *   *Why C is incorrect:* A key-value store is optimized for fast single-record lookups, not for centralized multi-format storage of large heterogeneous datasets.
    *   *Why D is incorrect:* An OLTP database handles high-frequency transactional writes for operational systems. It is not a centralized analytics repository and does not support unstructured log storage.

---

**Question 4**
A data team uses a cloud data platform (such as Google BigQuery or Amazon Redshift) to run analytics. Raw data from three source systems is loaded into cloud storage first, then transformed using SQL queries inside the warehouse. Which data pipeline pattern does this describe?
*   A) ETL (Extract, Transform, Load) — data is cleaned and transformed before it is loaded into the target system.
*   B) ELT (Extract, Load, Transform) — raw data is loaded into the target first, then transformed using the platform's compute resources.
*   C) CDC (Change Data Capture) — only rows that changed since the last pipeline run are extracted and incrementally loaded.
*   D) MPP (Massively Parallel Processing) — the transformation is parallelized across hundreds of compute nodes simultaneously.
*   **Correct Answer:** B) ELT (Extract, Load, Transform) — raw data is loaded into the target first, then transformed using the platform's compute resources.
*   **Distractor Analysis:**
    *   *Why B is correct:* The pipeline loads raw data into cloud storage first, then applies transformations using the warehouse's SQL engine. This is the defining ELT pattern — load first, transform after. Cloud platforms favor ELT because their compute is elastic and cheap, and preserving raw data provides flexibility for future reprocessing.
    *   *Why A is incorrect:* ETL transforms data before loading it. In this scenario, raw data arrives in cloud storage before any transformation occurs, which is the opposite sequence.
    *   *Why C is incorrect:* CDC is an incremental extraction technique — it captures only rows that changed since the last run. The scenario describes a full-load pipeline pattern, not an incremental capture strategy.
    *   *Why D is incorrect:* MPP describes the hardware architecture of some data warehouses — how they parallelize query execution. It is a platform characteristic, not a pipeline pattern name.

---

**Question 5**
A data scientist runs a machine learning algorithm on a Hadoop cluster using MapReduce. The algorithm requires 100 iterations over the same dataset to converge. After each iteration, results are written to HDFS before the next iteration reads them. The job takes 6 hours. A colleague suggests migrating the job to Apache Spark. What is the primary reason Spark would improve performance for this workload?
*   A) Spark uses a more accurate algorithm that converges in fewer iterations, reducing the total computation required.
*   B) Spark caches intermediate results in memory across iterations, eliminating the repeated disk reads and writes that make MapReduce slow for iterative workloads.
*   C) Spark runs on faster hardware than Hadoop and automatically provisions larger CPU cores for machine learning tasks.
*   D) Spark converts the iterative algorithm to a single SQL query that the cluster optimizer can execute in one pass.
*   **Correct Answer:** B) Spark caches intermediate results in memory across iterations, eliminating the repeated disk reads and writes that make MapReduce slow for iterative workloads.
*   **Distractor Analysis:**
    *   *Why B is correct:* MapReduce writes intermediate results to HDFS after every map and reduce phase. In a 100-iteration algorithm, this means 200+ disk I/O operations on the full dataset. Spark keeps the working dataset in RAM between iterations — 100 iterations become 100 in-memory passes with no disk overhead, which is orders of magnitude faster.
    *   *Why A is incorrect:* Spark does not change the mathematical algorithm or its convergence behavior. The same number of iterations is required. The improvement is purely in how intermediate results are stored between iterations.
    *   *Why C is incorrect:* Spark can run on the same hardware as Hadoop. The performance advantage is architectural — in-memory processing — not a hardware specification difference.
    *   *Why D is incorrect:* Spark does not convert iterative ML algorithms into SQL queries. Spark MLlib runs distributed iterative algorithms natively; the advantage is in-memory caching, not query compilation.

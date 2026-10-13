# Video Script: Module 09 — Big Data Technologies

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA Data+ (DA0-001)

---

## Segment 1: Introduction (0:00–1:30)

Welcome back to CIS-4336. I'm Professor Nash. Today we are stepping back from individual algorithms and looking at the infrastructure that makes large-scale data analytics possible — big data technologies.

When people talk about "big data," they mean datasets so large, so fast-moving, or so varied that traditional relational databases and desktop tools simply cannot handle them. We are talking about petabytes of log files, billions of sensor readings per day, and real-time transaction streams from millions of simultaneous users.

To handle data at this scale, engineers and analysts rely on distributed computing frameworks — most notably the Apache Hadoop ecosystem and Apache Spark. We will also cover the architectural distinction between data lakes and data warehouses, and we will close with the critical decision every analytics team faces: batch processing vs. real-time streaming.

The CompTIA Data+ exam covers big data concepts in Domain 1. These topics account for roughly 20% of the exam. Let's go.

[PAUSE — Slide: Module 09 Objectives]

---

## Segment 2: What Is Big Data? (1:30–3:30)

Big data is defined by the **5 V's** — five dimensions that characterize datasets exceeding the capacity of conventional systems.

**Volume** — the sheer size of data. We are talking terabytes to petabytes. A single day of server logs from a major web platform can easily exceed 100 TB.

**Velocity** — the speed at which data is generated and must be processed. Stock market tick data, social media feeds, and IoT sensor streams generate millions of events per second.

**Variety** — the diversity of data formats. Structured tables, semi-structured JSON and XML, unstructured text, images, audio, and video — all arriving through the same pipeline.

**Veracity** — the trustworthiness of the data. Is it accurate? Is it complete? Big data systems must handle missing values, noise, and conflicting records at scale.

**Value** — the ultimate goal. The purpose of processing all this data is to extract actionable insight. More data does not automatically mean more value.

[SHOW CHART — The 5 V's diagram with icons for each dimension]

[PAUSE]

When any one of these dimensions exceeds what your existing tools can handle, you have a big data problem — and you need a big data solution.

---

## Segment 3: The Hadoop Ecosystem (3:30–9:00)

Apache Hadoop is an open-source framework for distributed storage and processing of large datasets across clusters of commodity hardware. It was inspired by Google's MapReduce and Google File System papers published in 2003–2004.

The core insight of Hadoop: instead of moving data to a powerful central computer, move the computation to where the data lives.

[SHOW CHART — Hadoop architecture diagram: HDFS nodes, MapReduce, YARN, Hive, Pig]

### HDFS — Hadoop Distributed File System

HDFS is the storage layer of Hadoop. It splits large files into blocks — typically 128 MB each — and distributes those blocks across multiple nodes in a cluster. Each block is replicated, usually three times, on different nodes.

[PAUSE]

Key concepts:

- **NameNode** — the master node that tracks where every block is stored. There is typically one active NameNode and one standby for high availability.
- **DataNode** — worker nodes that store the actual data blocks and respond to client read/write requests.
- **Replication factor** — typically 3 (one original plus two copies). If a DataNode fails, HDFS automatically re-replicates the lost blocks from surviving copies.

HDFS is optimized for large sequential reads — perfect for batch analytics. It is not designed for frequent small random writes.

[PAUSE]

### MapReduce

MapReduce is Hadoop's original processing framework. It breaks a computation into two phases executed in parallel across the cluster.

**Map phase:** Each node processes its local data blocks and emits key-value pairs. In a word count job, the Map function reads text and emits `(word, 1)` for every word encountered.

**Reduce phase:** The framework groups all values by key and sends them to Reducer nodes. The Reduce function aggregates the grouped values. In word count, it sums all the 1s for each word, producing `(word, total_count)`.

[SHOW CHART — MapReduce diagram: Input → Split → Map → Shuffle/Sort → Reduce → Output]

[PAUSE]

MapReduce is reliable and fault-tolerant — if a node fails mid-job, the framework re-runs that task on another node. But it is slow: it writes intermediate results to disk between the Map and Reduce phases, adding significant I/O latency.

### Apache Hive

Hive is a data warehouse layer built on top of Hadoop. It provides a SQL-like query language called HiveQL that translates SQL statements into MapReduce or Tez jobs running on HDFS data.

Hive makes Hadoop accessible to analysts who know SQL but not Java. You write a SELECT statement and Hive handles the rest.

```sql
-- HiveQL: count orders by region
SELECT region, COUNT(*) AS order_count
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY region
ORDER BY order_count DESC;
```

[PAUSE]

Hive is optimized for batch analytics — large aggregation queries over historical data. It is not suitable for real-time queries or frequent updates.

### Apache Pig

Pig is a high-level scripting language (Pig Latin) for building MapReduce data pipelines. Where Hive is SQL-like, Pig is more procedural — you describe a sequence of data transformations step by step.

Pig is commonly used for ETL workflows: cleaning and reshaping raw data before loading it into Hive tables for analysis.

[PAUSE]

---

## Segment 4: Apache Spark (9:00–13:00)

Apache Spark is the successor to MapReduce for distributed data processing. Released in 2014, Spark addressed MapReduce's biggest weakness: speed.

Where MapReduce writes intermediate results to disk between stages, Spark processes data **in memory** — keeping intermediate results in RAM across all computation stages. This makes Spark 10 to 100 times faster than MapReduce for iterative algorithms such as machine learning and for interactive analytical queries.

[SHOW CHART — Comparison: MapReduce disk I/O chain vs. Spark in-memory pipeline]

[PAUSE]

### Resilient Distributed Datasets

The core data structure in Spark is the **Resilient Distributed Dataset** (RDD) — an immutable, partitioned collection of data distributed across the cluster. RDDs are fault-tolerant: if a partition is lost, Spark reconstructs it from its lineage — the record of transformations applied to create it.

Spark operations on RDDs fall into two categories:

- **Transformations** — lazy operations that define a new RDD (filter, map, join, groupBy). They are not executed immediately.
- **Actions** — operations that trigger actual computation (collect, count, save). When an action is called, Spark builds and executes the full computation plan.

[PAUSE]

### Spark Ecosystem Components

Spark is not just a processing engine — it is an entire analytics platform.

- **Spark SQL** — SQL queries and DataFrames for structured data
- **Structured Streaming** — real-time processing of continuous data streams
- **MLlib** — distributed machine learning library
- **GraphX** — graph analytics

```python
# PySpark example: count orders by region
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("OrderAnalysis").getOrCreate()
df = spark.read.csv("hdfs:///data/orders.csv", header=True, inferSchema=True)

result = df.groupBy("region").count().orderBy("count", ascending=False)
result.show()
```

[PAUSE]

### Spark vs. MapReduce

| Dimension | MapReduce | Apache Spark |
|-----------|-----------|-------------|
| Speed | Slow — disk I/O between stages | Fast — in-memory processing |
| API ease | Complex Java API | Python, Scala, SQL APIs |
| Iterative algorithms | Very slow | Very fast |
| Streaming support | Not native | Native (Structured Streaming) |
| Fault tolerance | Task re-execution | RDD lineage reconstruction |

Spark has largely replaced MapReduce for new workloads. MapReduce is still found in legacy Hadoop clusters.

---

## Segment 5: Data Lakes vs. Data Warehouses (13:00–16:00)

Two architectural patterns dominate large-scale data storage. The Data+ exam tests this distinction directly.

### Data Warehouse

A data warehouse stores **structured, processed data** that has been cleaned, transformed, and organized for analytical queries. Data is modeled in advance — typically using a star schema or snowflake schema.

Characteristics:

- Schema-on-write: structure is defined before data is loaded
- High performance for structured SQL analytical queries
- Strong data governance and quality controls
- Expensive to store large volumes of unstructured data
- Examples: Snowflake, Amazon Redshift, Google BigQuery, Azure Synapse Analytics

[PAUSE]

### Data Lake

A data lake stores **raw data in its native format** — structured, semi-structured, and unstructured — at massive scale. Structure is applied when the data is read, not when it is stored.

Characteristics:

- Schema-on-read: structure applied at query time
- Stores everything cheaply using object storage (Amazon S3, Azure Data Lake Storage)
- Flexible — supports any data type
- Risk of becoming a "data swamp" without governance
- Examples: Amazon S3 plus Athena, HDFS plus Hive, Azure Data Lake Storage plus Synapse

[PAUSE]

### Data Lakehouse

A newer hybrid architecture — the **data lakehouse** — combines the storage economics of a data lake with the structure and governance of a data warehouse. Technologies implementing this pattern include Delta Lake, Apache Iceberg, and Databricks.

[SHOW CHART — Side-by-side comparison: data warehouse vs. data lake vs. data lakehouse attributes]

---

## Segment 6: Batch vs. Real-Time Processing (16:00–18:30)

Not all data needs to be processed immediately. Choosing between batch and streaming is one of the most consequential architectural decisions in data engineering.

### Batch Processing

Batch processing collects data over a period of time and processes it all at once, on a schedule — hourly, nightly, or weekly.

Best for:

- Overnight payroll calculations
- Monthly financial reports
- End-of-day inventory reconciliation
- Training machine learning models on historical data

Advantages: efficient, simple to implement, optimized for throughput.
Disadvantages: latency — results are only as fresh as the last batch run.

[PAUSE]

### Streaming Processing

Streaming processes data continuously as it arrives — within milliseconds to seconds.

Technologies: Apache Kafka, Apache Spark Structured Streaming, Apache Flink, AWS Kinesis.

Best for:

- Fraud detection on credit card transactions (act before the purchase completes)
- Real-time monitoring dashboards (server health, network traffic)
- Recommendation engines responding to the current user session
- Real-time pricing in ridesharing or e-commerce applications

[SHOW CHART — Timeline diagram: batch (bulk daily processing) vs. streaming (continuous micro-processing)]

[PAUSE]

### Lambda and Kappa Architectures

The **lambda architecture** combines batch and streaming: a batch layer processes historical data with high accuracy; a speed layer processes real-time streams; a serving layer merges both views.

The **kappa architecture** simplifies this by using only a streaming layer — treating the stream as the source of truth for both historical and real-time queries.

---

## Segment 7: Module Summary (18:30–20:30)

Let me pull everything together.

[PAUSE]

The 5 V's of big data: Volume, Velocity, Variety, Veracity, Value.

Hadoop ecosystem:

- HDFS — distributed file storage with 128 MB blocks and 3x replication
- MapReduce — batch processing with Map and Reduce phases; writes to disk between stages
- Hive — SQL interface (HiveQL) to Hadoop for analytical queries
- Pig — scripting language for ETL data pipelines

Apache Spark:

- In-memory processing — 10 to 100x faster than MapReduce
- Core abstraction: RDD (Resilient Distributed Dataset)
- Ecosystem: Spark SQL, Structured Streaming, MLlib

Storage architectures:

- Data warehouse: structured, schema-on-write, governed, SQL-optimized
- Data lake: raw, schema-on-read, flexible, data-swamp risk
- Data lakehouse: hybrid of both

Processing paradigms:

- Batch: efficient, scheduled, latency acceptable
- Streaming: real-time, low latency, event-driven

For the Data+ exam: know HDFS block replication, the two MapReduce phases, the data warehouse vs. data lake distinction, and the batch vs. streaming trade-off.

See you in Module 10 — Data Quality and Governance.

[PAUSE — End card]

---

End of Module 09 Video Script

# Reading Guide: Module 09 — Big Data Technologies

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 1: Data Concepts and Environments

---

## Overview

This guide covers the distributed computing frameworks, storage architectures, and processing paradigms that underpin large-scale data analytics. These concepts are tested in Domain 1 of the CompTIA Data+ exam. Study the comparison tables closely — the exam presents scenarios requiring you to select the right technology for each situation.

---

## Section 1: The 5 V's of Big Data

| V | Definition | Example |
|---|-----------|---------|
| Volume | Scale — terabytes to petabytes | 200 TB/day of server logs |
| Velocity | Speed of generation and required processing | 1 million sensor readings per second |
| Variety | Diversity of data types and formats | SQL tables, JSON, images, audio |
| Veracity | Trustworthiness and accuracy | Noisy readings, duplicate records |
| Value | Business utility extracted from the data | Fraud savings, churn reduction |

When any of these dimensions exceeds your current system's capacity, a big data solution is warranted.

---

## Section 2: HDFS — Hadoop Distributed File System

### Architecture

HDFS splits files into fixed-size blocks (default: 128 MB) and distributes them across DataNodes in a cluster. Each block is replicated (default replication factor: 3) on different DataNodes for fault tolerance.

| Component | Role |
|-----------|------|
| NameNode | Master — tracks file metadata, block locations, and cluster health |
| DataNode | Worker — stores actual data blocks; sends heartbeats to NameNode |
| Secondary NameNode | Merges NameNode edit logs periodically; NOT a failover node |
| Standby NameNode | High-availability failover for the active NameNode |

### Key Properties

- Write-once, read-many: optimized for large sequential reads, not random writes
- Fault tolerance through block replication
- Data locality: compute moves to the data, not vice versa

### Block Replication and Fault Tolerance

When a DataNode fails, the NameNode detects the missing heartbeat, identifies under-replicated blocks, and instructs surviving DataNodes to create replacement copies — automatically restoring the configured replication factor.

---

## Section 3: MapReduce

### Processing Model

| Phase | Function | Word Count Example |
|-------|----------|-------------------|
| Map | Process local data blocks; emit key-value pairs | Emit `(word, 1)` for each word |
| Shuffle/Sort | Framework groups all values by key automatically | Groups all `(word, 1)` by word |
| Reduce | Aggregate grouped values per key | Sum 1s per word → `(word, total)` |

### Fault Tolerance

Failed tasks are automatically re-scheduled on another available node without stopping the rest of the job.

### MapReduce Limitations

- Writes intermediate results to disk between phases — high I/O latency
- Poor performance for iterative algorithms (each iteration is a full new job)
- No native streaming support
- Complex raw Java programming model

---

## Section 4: Apache Hive and Apache Pig

### Apache Hive

Hive provides a SQL interface (HiveQL) to HDFS data. It translates SQL queries into MapReduce, Tez, or Spark jobs automatically.

Key concepts:

- **Metastore:** Stores table schemas and partition metadata in a relational database
- **External tables:** Schema defined over existing HDFS data without moving files
- **Partitioning:** Data subdivided by key (e.g., year/month) to enable partition pruning and faster queries
- **ORC/Parquet:** Columnar storage formats that improve analytical query performance dramatically

```sql
-- HiveQL: create a partitioned external table
CREATE EXTERNAL TABLE sales (
    order_id   STRING,
    customer   STRING,
    amount     DOUBLE
)
PARTITIONED BY (sale_year INT, sale_month INT)
STORED AS ORC
LOCATION '/data/sales/';
```

### Apache Pig

Pig provides a procedural scripting language (Pig Latin) for multi-step ETL data transformations.

```pig
orders  = LOAD '/data/orders' USING PigStorage(',')
          AS (order_id:chararray, region:chararray, amount:float);
big     = FILTER orders BY amount > 1000;
grouped = GROUP big BY region;
totals  = FOREACH grouped GENERATE group AS region, SUM(big.amount) AS total;
STORE totals INTO '/output/regional_totals';
```

When to use each:

- **Hive:** SQL-familiar analysts; batch aggregation queries; structured reporting
- **Pig:** Data engineers; complex multi-step ETL pipelines; logic too complex for a single SQL statement

---

## Section 5: Apache Spark

### Performance Advantage

Spark keeps intermediate results in RAM across computation stages, avoiding the disk I/O that makes MapReduce slow.

| Feature | MapReduce | Apache Spark |
|---------|-----------|-------------|
| Intermediate storage | Disk (HDFS) | RAM (spills to disk only if needed) |
| Relative speed | Baseline | 10–100x faster |
| Programming API | Java | Python, Scala, Java, SQL |
| Streaming | No | Yes — Structured Streaming |
| Machine learning | Limited | MLlib — full distributed ML library |
| Interactive queries | No | Yes — notebooks and Spark Shell |

### Resilient Distributed Datasets

An RDD is immutable, partitioned, and distributed across the cluster.

RDD operation types:

- **Transformations (lazy):** `map()`, `filter()`, `flatMap()`, `groupByKey()`, `reduceByKey()`, `join()`
- **Actions (trigger execution):** `collect()`, `count()`, `first()`, `take(n)`, `saveAsTextFile()`

Fault tolerance via lineage: Spark recomputes lost partitions from recorded transformation history rather than replicating data proactively.

### DataFrames and Spark SQL

DataFrames are the modern higher-level Spark abstraction — structured tables with named columns optimized by the Catalyst query engine.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

df = spark.read.parquet("hdfs:///data/sales/")

result = (df
    .filter(col("sale_year") == 2024)
    .groupBy("region")
    .agg(spark_sum("amount").alias("total_sales"))
    .orderBy("total_sales", ascending=False))

result.show(10)
```

---

## Section 6: Data Lake vs. Data Warehouse vs. Data Lakehouse

### Core Comparison

| Attribute | Data Warehouse | Data Lake | Data Lakehouse |
|-----------|---------------|-----------|----------------|
| Data type | Structured only | Any type | Any type |
| Schema strategy | Schema-on-write | Schema-on-read | Schema-on-write with flexible zones |
| Storage cost | High | Low (object storage) | Low |
| Query performance | High | Moderate | High |
| Data quality | High — enforced at load | Variable | High — enforced by table format |
| Governance | Strong | Weak (data swamp risk) | Strong |
| Best for | SQL analytics, BI reporting | Exploration, ML, raw archive | Unified analytics platform |
| Examples | Snowflake, Redshift, BigQuery | S3+Athena, HDFS+Hive | Databricks, Delta Lake, Apache Iceberg |

### Schema-on-Write vs. Schema-on-Read

**Schema-on-write:** Data must conform to a defined schema before loading. Quality is enforced at ingestion. Queries are fast.

**Schema-on-read:** Raw data is stored as-is. Schema is applied at query time. Flexible but adds query overhead.

### The Data Swamp Problem

A data lake without governance becomes a data swamp — untracked files with no catalog, no lineage, no quality controls, no ownership. Prevention requires: a data catalog, defined stewardship, automated quality checks, and access controls.

---

## Section 7: Batch vs. Real-Time Processing

### Comparison Table

| Attribute | Batch Processing | Streaming (Real-Time) |
|-----------|-----------------|----------------------|
| Trigger | Scheduled (time-based) | Event-driven (data arrival) |
| Latency | Minutes to hours | Milliseconds to seconds |
| Throughput | Very high | Moderate |
| Complexity | Lower | Higher |
| Use cases | Reports, model training, reconciliation | Fraud detection, monitoring, recommendations |
| Technologies | Spark, Hive, MapReduce | Kafka, Spark Streaming, Flink, Kinesis |

### Lambda Architecture

- **Batch layer:** processes full historical dataset; high accuracy, high latency
- **Speed layer:** processes real-time stream; low latency, approximate accuracy
- **Serving layer:** merges both outputs for query responses

The kappa architecture eliminates the batch layer and replays the stream for historical queries, reducing operational complexity.

---

## Section 8: Data+ Exam Tips

**Tip 1:** HDFS default block size = 128 MB. Default replication factor = 3. These numbers are tested directly.

**Tip 2:** MapReduce has two developer-facing phases: Map and Reduce. Shuffle/Sort is automatic. Know all three phases.

**Tip 3:** Spark is faster than MapReduce because it processes data in memory rather than writing to disk between stages.

**Tip 4:** Data warehouse = schema-on-write, structured, governed. Data lake = schema-on-read, raw, flexible. Know which to recommend per scenario.

**Tip 5:** Batch = scheduled, high latency. Streaming = real-time, low latency. Exam presents scenarios requiring selection of the right paradigm.

**Tip 6:** Apache Kafka is a streaming message platform — not a processing engine. Spark Streaming, Flink, or Kinesis process the streams that Kafka routes.

---

## Key Terms Reference

| Term | Definition |
|------|-----------|
| HDFS | Hadoop's distributed file system; 128 MB blocks, 3x replication |
| NameNode | HDFS master; tracks all block locations and file metadata |
| DataNode | HDFS worker; stores actual data blocks |
| MapReduce | Batch framework; Map emits key-value pairs; Reduce aggregates |
| HiveQL | SQL-like language for querying HDFS via Hive |
| RDD | Resilient Distributed Dataset; core Spark data abstraction |
| Schema-on-write | Schema defined before data is stored (data warehouse) |
| Schema-on-read | Schema applied at query time (data lake) |
| Lambda architecture | Combines batch and speed layers for unified historical/real-time queries |
| Data swamp | An ungoverned data lake where data is difficult to find and trust |

---

## 9. Supplemental Resources

**1. Apache Spark Official Documentation — Getting Started**
<https://spark.apache.org/docs/latest/quick-start.html>
The official Apache Spark quickstart guide covering RDDs, DataFrames, and Spark SQL with hands-on Python (PySpark) examples. Essential reading for understanding in-memory distributed processing and the Spark ecosystem components covered in Module 09.

**2. Databricks Glossary — Data Lakehouse Architecture**
<https://www.databricks.com/glossary/data-lakehouse>
A concise explanation of the data lakehouse pattern — combining data lake flexibility with warehouse-style ACID transactions and governance. Clarifies how lakehouse relates to Lambda/Kappa architectures and why organizations are moving beyond pure data lakes.

**3. Confluent — What is Apache Kafka?**
<https://www.confluent.io/what-is-apache-kafka>
A comprehensive introduction to Apache Kafka covering topics, partitions, consumer groups, and the publish-subscribe model. Directly supports understanding real-time streaming pipelines and the speed layer in Lambda architecture discussed in Module 09.

---

End of Module 09 Reading Guide

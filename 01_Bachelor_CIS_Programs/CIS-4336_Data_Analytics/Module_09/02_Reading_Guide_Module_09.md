# Reading Guide: Module 09 — Big Data Technologies

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4336 &BULL; DATA ANALYTICS & BUSINESS INTELLIGENCE</text>
    
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

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / IBM &bull; CIS-4336 Module 09</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=r-uOLxNrNk8" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/r-uOLxNrNk8" title="Data Analytics with Python, Pandas & SQL Masterclass" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Data Analytics with Python, Pandas & SQL Masterclass</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

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

---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 09 — Big Data Technologies** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 09 — Big Data Technologies**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 09 — Big Data Technologies**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Module 09 — Big Data Technologies**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**

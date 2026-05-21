# Reading Guide: Module 12 - Data Processing – Time-Series Databases and Stream Processing
## Course: CIS-4355_IoT_Embedded_Systems (IoT & Embedded Security (General Principles))

---

### Introduction
Welcome to **Module 12 – Data Processing: Time-Series Databases and Stream Processing**! This module examines how IoT systems store, query, and process the high-volume, time-stamped data streams that sensors continuously generate. Choosing the wrong storage and processing architecture for IoT data is one of the most common causes of system performance failure at scale — a relational database designed for transactional workloads cannot efficiently handle millions of time-stamped sensor readings per day.

You will learn how time-series databases (InfluxDB, TimescaleDB, AWS Timestream) are optimized for write-heavy, time-ordered workloads through techniques like time-partitioning, data retention policies, and downsampling. You will also learn how stream processing frameworks (Apache Kafka, AWS Kinesis, Apache Flink) enable real-time analytics on data in motion — detecting anomalies and triggering alerts within milliseconds of data arrival rather than hours later through batch jobs. Security considerations — including access control to telemetry databases and securing stream processing pipelines — run throughout.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Time-Series Database (TSDB)**: A database management system optimized for storing and querying data points indexed by timestamp. Unlike relational databases that optimize for arbitrary query patterns, TSDBs exploit time-ordering to achieve higher write throughput, efficient range queries ("give me all temperature readings between 09:00 and 10:00"), and automatic data lifecycle management through retention policies that delete or downsample old data. Examples include InfluxDB (open source), TimescaleDB (PostgreSQL extension), and AWS Timestream.
*   **Data Retention Policy**: A TSDB configuration rule that automatically deletes or compresses data older than a specified age. For example, a policy might retain raw 1-second readings for 7 days, 1-minute averages for 90 days, and hourly averages indefinitely. Retention policies prevent unbounded storage growth and reduce query latency on recent data by keeping hot data compact. From a security standpoint, retention policies enforce data minimization — a privacy principle relevant to personal IoT data under GDPR.
*   **Stream Processing**: The real-time processing of data records as they arrive, rather than accumulating records into a batch and processing them periodically. Stream processing frameworks (Apache Kafka Streams, Apache Flink, AWS Kinesis Data Analytics) apply user-defined logic — filtering, aggregation, anomaly detection, joins — to each event within milliseconds of ingestion. This enables sub-second alerting on sensor threshold breaches, which batch-only architectures cannot achieve.
*   **Apache Kafka**: A distributed, fault-tolerant event streaming platform that decouples data producers (IoT sensors, gateways) from consumers (analytics engines, databases, alert systems). Producers publish records to named topics; consumers read from topics at their own pace. Kafka retains published records for a configurable retention period, allowing consumers to replay historical data or recover from processing failures. Kafka is widely used as the ingestion backbone for large-scale IoT data pipelines.
*   **Downsampling**: The process of reducing the temporal resolution of stored data by replacing a set of high-frequency raw readings with a computed summary (mean, max, min) over a time window. For example, replacing 60 one-second readings with a single 1-minute average reduces storage by 60x. Downsampling is typically applied as data ages — recent data is kept at full resolution for debugging and anomaly detection; older data is downsampled for trend analysis and long-term storage cost management.

---

### 2. Certification Exam Tips
*   **TSDB vs RDBMS trade-offs:** Memorize: TSDB = optimized for time-ordered writes and range queries, supports retention policies and downsampling, not suitable for complex multi-table joins. RDBMS = flexible query patterns, ACID transactions, not optimized for high-frequency time-series inserts. Exam scenarios describe a workload and test whether you choose TSDB or RDBMS.
*   **Kafka producer/consumer model:** Kafka topics are append-only logs; consumers maintain their own offset (read position). Multiple consumer groups can read the same topic independently. This decoupling is the key architectural advantage — adding a new analytics consumer does not require changes to the producer.
*   **Stream vs batch processing selection:** Use stream processing when latency requirement is under 1–5 seconds (real-time alerting, anomaly detection). Use batch processing when latency requirement is hours or days (daily reports, model training). Exam scenarios state a latency requirement and test whether you choose stream or batch.
*   **Security for telemetry databases:** Time-series databases storing IoT sensor data must apply least-privilege access — read-only credentials for dashboards, write credentials for ingest agents, and admin credentials only for DBA operations. Exposed InfluxDB instances without authentication have been publicly exploited to exfiltrate or delete sensor data.
*   **Study Resource:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) covers insufficient data protection and insecure cloud interfaces — both applicable to unprotected time-series databases and unauthenticated Kafka topics that expose IoT telemetry to unauthorized consumers.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** The [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/) — focus on the insufficient data protection and insecure cloud interface sections, which cover risks from unprotected telemetry databases and unauthenticated stream processing endpoints that are directly relevant to this module.
*   **Required Video:** The [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0) includes coverage of IoT data pipeline architecture, comparing time-series database options and stream processing frameworks for different IoT workload types and scale requirements.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write sensor data to InfluxDB and query with Flux**: Install InfluxDB OSS on a Raspberry Pi or virtual machine, write a Python script using the `influxdb-client` library to publish simulated temperature readings at 1 Hz, then write a Flux query to compute the 5-minute mean and identify the maximum reading over the past hour.
*   **Configure a data retention policy**: Using the InfluxDB CLI, create a retention policy that retains raw data for 7 days and define a continuous query that downsamples to 1-minute averages stored in a separate measurement for 90-day retention.
*   **Simulate a stream processing filter**: Using Python with the `kafka-python` library (or a local queue), consume a stream of simulated sensor readings and apply a threshold filter that forwards only readings above 80°C to an "alerts" topic, logging the latency from publication to alert generation.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize the TSDB vs RDBMS trade-off distinctions.
- [ ] Read the insufficient data protection section at [OWASP IoT Security Project Guides & Embedded Systems Wiki](https://owasp.org/www-project-internet-of-things/).
- [ ] Watch the data pipeline sections of [IoT Course & Embedded Systems Tutorials by freeCodeCamp](https://www.youtube.com/watch?v=h0J8f60LdB0).
- [ ] Calculate storage reduction from downsampling 1 Hz data to 1-minute averages over 90 days before the lab.
- [ ] Proceed to the weekly hands-on lab activity.

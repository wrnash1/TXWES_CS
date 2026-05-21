# Reading Guide: Module 11 - Big Data Concepts – Hadoop and Spark
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

### Introduction
Welcome to **Module 11 - Big Data Concepts: Hadoop and Spark**! Traditional databases and single-machine analytics tools hit their limits when datasets grow to terabytes or petabytes. Big data technologies like Hadoop and Spark distribute storage and computation across clusters of commodity machines, enabling analytics at a scale that would be impossible on a single server. This module covers the big data concepts tested on the **CompTIA Data+** exam: the defining characteristics of big data, the Hadoop ecosystem, how Spark improves on Hadoop for in-memory processing, and how these technologies fit into modern data pipelines.

Understanding big data architecture helps analysts recognize when a problem requires distributed infrastructure, interpret data pipelines built by data engineers, and communicate intelligently with platform teams about the systems that generate and store the data they analyze.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **The 3 Vs of big data (volume, velocity, variety)**: Volume refers to the sheer scale of data — datasets too large to store or process on a single machine. Velocity refers to the speed at which data is generated and must be processed — streaming sensor data, real-time transactions, and social media feeds require near-instant ingestion. Variety refers to the diversity of data types — structured tables, unstructured text, images, logs, and JSON all arriving from different sources.
*   **Hadoop and HDFS**: Apache Hadoop is an open-source framework for distributed storage and batch processing of large datasets. The Hadoop Distributed File System (HDFS) splits files into blocks and distributes them across multiple nodes in a cluster, with replication for fault tolerance. MapReduce, Hadoop's original processing model, breaks a computation into a map phase (applying a function to each data chunk in parallel) and a reduce phase (aggregating the results).
*   **Apache Spark**: A fast, general-purpose distributed processing engine that improves on MapReduce by performing computations in memory (RAM) rather than writing intermediate results to disk. Spark is 10–100x faster than Hadoop MapReduce for iterative algorithms and interactive queries. Spark supports batch processing, streaming, SQL queries (Spark SQL), machine learning (MLlib), and graph processing — all within the same engine.
*   **Data lake vs. data warehouse**: A data lake is a centralized repository that stores raw data in its native format — structured, semi-structured, and unstructured — without schema enforcement at ingestion ("schema on read"). A data warehouse stores cleaned, structured, schema-enforced data optimized for analytical queries ("schema on write"). Data lakes are flexible and cheap for raw storage; warehouses are optimized for fast, reliable business reporting.
*   **ETL and ELT pipelines**: ETL (Extract, Transform, Load) extracts data from source systems, transforms it (cleans, joins, aggregates), and loads it into a target warehouse. ELT (Extract, Load, Transform) loads raw data into the target first, then transforms it using the warehouse's processing power. Cloud-scale data platforms increasingly favor ELT because compute is cheap and preserving raw data provides flexibility.

---

### 2. Certification Exam Tips
*   **Domain weight:** Big data and pipeline concepts appear in Domain 2 (Data Collection and Management, ~25%) and Domain 3 (Data Mining, ~23%) of the Data+ DA0-001 exam. Questions about data storage architectures and processing frameworks are common.
*   **Exam trap — Hadoop vs. Spark:** Hadoop MapReduce is a disk-based batch processing system; it is reliable but slow for iterative or interactive workloads. Spark is in-memory and much faster, especially for machine learning and real-time analytics. If an exam scenario asks which technology is better for iterative ML training or real-time stream processing, the answer is Spark.
*   **Exam trap — data lake vs. data warehouse:** A data lake stores raw, unstructured or semi-structured data with schema applied at read time. A data warehouse stores clean, structured data with a predefined schema applied at write time. If the scenario describes storing diverse raw data sources cheaply before any transformation, the answer is data lake. If it describes fast, reliable BI reporting on cleaned data, the answer is data warehouse.
*   **Exam trap — ETL vs. ELT:** ETL transforms data before loading — traditional, used when the target warehouse has limited compute. ELT loads first then transforms — modern, used with cloud platforms (BigQuery, Redshift, Snowflake) where compute is elastic. The exam may present a scenario and ask which pipeline pattern applies.
*   **Study Resource:** The data engineering and big data chapters of [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/) cover distributed data concepts and pipeline architecture. The [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) demonstrates data pipeline thinking in Python that translates directly to understanding what Spark and Hadoop automate at scale.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the data engineering and distributed systems chapters in the OER Textbook: [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/). Focus on the sections covering large-scale data storage architectures, pipeline design, and the distinction between batch and streaming processing.
*   **Required Video:** Watch the data pipeline and engineering sections of the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238), which demonstrates data ingestion, transformation, and loading workflows in Python that parallel the logic of distributed big data systems.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Design an ETL pipeline for a multi-source dataset**: Identify the extract source (database + CSV), the transformation steps (join, filter, type cast), and the load target (data warehouse table), then document each step with its input and output schema.
*   **Compare data lake and data warehouse storage approaches**: Given a scenario with three data sources (structured orders, semi-structured JSON events, unstructured log files), determine which sources should land in a data lake first and which should be loaded directly to a warehouse.
*   **Explain the Spark in-memory advantage**: Describe a scenario where a MapReduce job running 50 iterations of a machine learning algorithm would be impractical, and explain why Spark's in-memory caching of intermediate results solves the performance problem.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the data engineering chapters in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/).
- [ ] Watch the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238).
- [ ] Review the lab instructions and understand what each task requires.
- [ ] Proceed to the weekly hands-on lab activity.

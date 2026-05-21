# Reading Guide: Module 07 - BigQuery – Data Warehouse and Analytics
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 07 - BigQuery – Data Warehouse and Analytics**! This week you will study Google BigQuery, GCP's fully managed, serverless enterprise data warehouse. BigQuery is one of the most frequently tested services on the GCP Professional Cloud Database Engineer exam because database engineers are frequently asked to select it (or rule it out) as the appropriate GCP service for a given analytics workload.

BigQuery is not an OLTP database — it cannot replace Cloud SQL or Spanner for transactional workloads. However, for analytics, reporting, and large-scale data querying, it is unmatched in capability and simplicity of operation.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **BigQuery**: A fully managed, serverless data warehouse that enables SQL analytics over petabyte-scale datasets. BigQuery uses a columnar storage format called Capacitor, separates storage from compute, and charges by bytes processed (on-demand pricing) or by reserved slot capacity. It is not designed for transactional (OLTP) workloads.
*   **Columnar Storage**: BigQuery stores each column of a table separately on disk rather than storing complete rows together. When a query selects only 3 of 100 columns, BigQuery reads only 3% of the data, dramatically reducing I/O and query cost. This is why `SELECT *` in BigQuery is expensive — always specify the columns you need.
*   **Serverless Architecture**: BigQuery allocates compute resources (slots) automatically when you submit a query. You never provision, patch, or scale servers. Thousands of workers are assigned to execute a query in parallel and then released, making petabyte-scale queries feasible in seconds. This is a key exam differentiator — unlike Cloud SQL, there are no instances to manage.
*   **Partitioned Tables**: BigQuery tables can be partitioned by ingestion time, a DATE/TIMESTAMP column, or an integer range. Queries that filter on the partition column scan only the relevant partitions, dramatically reducing bytes processed and cost. The exam tests knowledge of partition types and partition pruning.
*   **Clustered Tables**: After partitioning, BigQuery can cluster a table by up to four columns. Clustering sorts and co-locates rows with the same cluster column values within each partition, making queries that filter on cluster columns even more efficient. Clustering and partitioning are complementary techniques.

---

### 2. Certification Exam Tips
*   **BigQuery vs. OLTP Services**: The exam consistently presents analytics scenarios and asks you to distinguish BigQuery from Cloud SQL/Spanner. Key signals that BigQuery is the answer: "analyze historical data", "run ad-hoc SQL queries on terabytes", "BI dashboards", "data warehouse", "no connection management needed". Key signals BigQuery is wrong: "transactional", "row-level updates", "sub-millisecond latency", "online application".
*   **Partitioning and Clustering**: Expect at least one question on which combination of partitioning and clustering reduces cost and improves performance for a described query pattern. Partition on the date column used in `WHERE` clauses; cluster on the high-cardinality columns used in `WHERE` and `JOIN` clauses within each partition.
*   **Slot Reservations vs. On-Demand**: On-demand pricing charges per TB processed. Flat-rate (slot reservations) pricing is better for predictable, high-volume workloads. The exam may ask you to recommend a pricing model for a given usage pattern.
*   **BigQuery ML and Federated Queries**: Know that BigQuery ML lets you train and run ML models using SQL, and that Federated Queries let BigQuery directly query data in Cloud Spanner, Cloud SQL, Cloud Storage, and Bigtable without copying data into BigQuery.
*   **Study Resource:** The official BigQuery documentation is the exam-authoritative reference: [BigQuery Documentation – Google Cloud](https://cloud.google.com/bigquery/docs). The freeCodeCamp SQL course reinforces SQL syntax for BigQuery queries: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Use *Database Design* by Adrienne Watt to understand the relational model and SQL that BigQuery's standard SQL dialect is built on: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This comprehensive free video lecture covers SQL fundamentals, data warehouse concepts, and query optimization techniques that apply directly to BigQuery: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will create a BigQuery dataset and table, load data from Cloud Storage, run `SELECT` queries with and without partition filters to observe cost differences, create a clustered and partitioned table, and run EXPLAIN on a query to view its execution plan.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the SQL and data modeling chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the SQL and data warehouse segments in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the BigQuery partitioning and clustering steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.

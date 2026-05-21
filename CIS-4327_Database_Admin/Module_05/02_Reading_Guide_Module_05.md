# Reading Guide: Module 05 - Bigtable – Wide-Column NoSQL at Scale
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 05 - Bigtable – Wide-Column NoSQL at Scale**! This week you will study Google Cloud Bigtable, the NoSQL wide-column store that powers many of Google's own internal products including Search, Maps, and Analytics. Bigtable is the right choice when you need single-digit millisecond latency at petabyte scale for workloads that access data by a single row key — such as IoT telemetry, time-series data, financial tick data, and personalization features.

Understanding Bigtable's data model, row key design, and schema patterns is essential because the GCP exam tests your ability to distinguish Bigtable from BigQuery, Firestore, and Cloud Spanner for specific workload characteristics.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cloud Bigtable**: A fully managed, petabyte-scale, wide-column NoSQL database service built on Google's internal Bigtable infrastructure. It stores data indexed by a single row key and is optimized for high-throughput, low-latency reads and writes. Bigtable does not support SQL, joins, secondary indexes, or multi-row transactions — knowing these limitations is critical for the exam.
*   **Row Key**: The single index by which Bigtable locates data. All reads and scans are performed using the row key or a row key range. Because Bigtable stores rows in sorted lexicographic order by key, row key design determines both performance and data locality. A poorly designed row key (such as a monotonically increasing timestamp prefix) causes hotspot tablets; a well-designed key distributes reads and writes evenly.
*   **Column Family**: A named group of related columns stored together on disk. In Bigtable, column families must be defined at table creation time, but individual column qualifiers within a family can be added dynamically. Grouping columns with similar access patterns into the same family reduces I/O.
*   **Interleaving Tables (Bigtable context)**: Unlike Cloud SQL or Spanner, Bigtable does not use SQL-style JOIN relationships between tables. Instead, related data is typically denormalized into wide rows within the same table, or modeled with a composite row key that encodes the parent-child relationship. This is a key schema design difference that the exam tests.
*   **Tablet**: The basic unit of data distribution in Bigtable. Each table is split into contiguous row key ranges called tablets, and each tablet is served by exactly one tablet server. When a tablet grows too large, Bigtable automatically splits it. Hotspots occur when many requests target the same tablet.

---

### 2. Certification Exam Tips
*   **Bigtable vs. BigQuery**: This is a high-frequency exam topic. Use Bigtable for: low-latency, high-throughput reads/writes, time-series, IoT, and ML feature stores. Use BigQuery for: SQL analytics, ad-hoc queries over historical data, and BI dashboards. Bigtable does not support SQL or complex aggregations efficiently; BigQuery is not designed for sub-second individual row lookups.
*   **Row Key Design**: Expect scenario questions where you must identify a good or bad row key design. Avoid monotonically increasing row keys that create write hotspots. Good patterns include: reverse timestamp (`<event_timestamp_reversed>#<device_id>`), salted prefixes, or concatenated composite keys.
*   **No Joins or Transactions**: Bigtable does not support multi-row atomic transactions (only single-row read-modify-write is atomic), secondary indexes, or SQL JOIN operations. Any exam answer suggesting a JOIN in Bigtable is wrong.
*   **Nodes and Performance**: Bigtable performance scales linearly with node count. Adding nodes does not redistribute existing data immediately; it takes time for the cluster to rebalance tablets after a scale-up event.
*   **Study Resource:** The official Google Cloud Bigtable documentation is the primary reference for this module: [Cloud Bigtable Documentation – Google Cloud](https://cloud.google.com/bigtable/docs). The freeCodeCamp database course provides context on NoSQL data models: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Use *Database Design* by Adrienne Watt to reinforce the contrast between relational and NoSQL data modeling, which will help you appreciate why Bigtable's single-key, wide-column model is a deliberate design trade-off: [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This comprehensive free lecture covers database fundamentals and NoSQL concepts that apply to Bigtable's data model: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will create a Bigtable instance, design a table schema with appropriate column families and a composite row key, write and read data using the `cbt` command-line tool, and observe the performance impact of different row key designs.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the relevant chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the NoSQL and database design segments in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the Bigtable schema design steps in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.

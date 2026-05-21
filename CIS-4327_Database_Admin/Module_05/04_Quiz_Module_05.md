# Quiz: Module 05 - Bigtable – Wide-Column NoSQL at Scale
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
An IoT platform collects temperature sensor readings from 100,000 devices, each sending one reading per second. The application needs to retrieve the most recent 1,000 readings for a specific device with sub-10-millisecond latency. Which Google Cloud database service is most appropriate?
A) BigQuery
B) Cloud SQL for PostgreSQL
C) Cloud Bigtable
D) Firestore
*   **Correct Answer:** C) Cloud Bigtable
*   **Distractor Analysis:**
    *   *Why C is correct:* Bigtable is purpose-built for high-throughput, low-latency time-series and IoT workloads. A composite row key of `<device_id>#<reverse_timestamp>` enables single-key range scans that return the most recent readings in milliseconds at petabyte scale.
    *   *Why A is incorrect:* BigQuery is a serverless analytics data warehouse optimized for large-scale SQL queries; it is not designed for sub-10-millisecond individual row lookups or high-frequency writes.
    *   *Why B is incorrect:* Cloud SQL for PostgreSQL can handle relational queries but would require a B-tree index scan and would struggle with the ingest rate of 100,000 writes per second at consistent sub-10ms latency.
    *   *Why D is incorrect:* Firestore is a document database optimized for mobile and web app backends with moderate throughput requirements; it does not match the ingest scale or the time-series access pattern of this IoT workload.

---

---

**Question 2**
A Bigtable table stores financial transaction records keyed by `<account_id>#<transaction_timestamp>`. Engineers report that write throughput is much lower than expected and one tablet server is significantly more loaded than others. What is the most likely cause, and how should it be fixed?
A) The row key places high-cardinality `account_id` first, which distributes writes well; the issue is too few nodes. Add more nodes.
B) The timestamp portion of the row key causes writes to cluster at the latest key range, creating a hotspot on one tablet. Reverse the timestamp or use a salted prefix.
C) Bigtable does not support composite row keys; the table must be redesigned with a single-field key.
D) The column family definition is missing; Bigtable requires all columns to be pre-declared for efficient storage.
*   **Correct Answer:** B) The timestamp portion of the row key causes writes to cluster at the latest key range, creating a hotspot on one tablet. Reverse the timestamp or use a salted prefix.
*   **Distractor Analysis:**
    *   *Why B is correct:* When timestamp is part of the row key and rows are sorted lexicographically, new writes always go to the largest (most recent) key prefix — concentrating all writes on the same tablet server. Reversing the timestamp distributes new rows across the key space.
    *   *Why A is incorrect:* Adding nodes helps throughput but does not fix a hotspot; the imbalanced distribution will persist until the key design is changed, because the same tablet will still receive all new writes.
    *   *Why C is incorrect:* Bigtable fully supports composite (concatenated) row keys; this is the recommended schema pattern for time-series data.
    *   *Why D is incorrect:* Column qualifiers (individual columns) within a column family can be added dynamically in Bigtable; only the column family itself needs to be predefined.

---

---

**Question 3**
A Bigtable administrator needs to **understand why a specific row key range scan is returning results slower than expected**. Which action best diagnoses the issue?
A) Use Cloud Bigtable's Key Visualizer tool to inspect read and write access patterns and identify hotspot tablets.
B) Run `EXPLAIN ANALYZE` on the Bigtable scan query to view the execution plan.
C) Check Cloud SQL Query Insights for the slow query in the Bigtable instance.
D) Enable binary logging on the Bigtable instance and replay the transaction log.
*   **Correct Answer:** A) Use Cloud Bigtable's Key Visualizer tool to inspect read and write access patterns and identify hotspot tablets.
*   **Distractor Analysis:**
    *   *Why A is correct:* Key Visualizer is Bigtable's native diagnostic tool. It generates a visual heatmap of read and write activity across the key space over time, making it straightforward to identify hotspot tablets, uneven distribution, and slow scan ranges.
    *   *Why B is incorrect:* `EXPLAIN ANALYZE` is a PostgreSQL/MySQL SQL command for relational query plans; Bigtable does not use SQL and has no equivalent command.
    *   *Why C is incorrect:* Query Insights is a Cloud SQL feature for relational query performance; it does not apply to Bigtable, which is a NoSQL service.
    *   *Why D is incorrect:* Bigtable does not expose binary logs for replay; it uses an internal Colossus-based replication mechanism that is not accessible to administrators.

---

**Question 4**
While administering a Bigtable instance serving a real-time personalization workload, engineers observe that **some read requests are experiencing high tail latency (p99 latency is 10x higher than p50)**. Which Bigtable-specific configuration change is most likely to reduce tail latency?
A) Enable replication by adding a second Bigtable cluster in a different zone and use application-side routing to send reads to the least-loaded cluster.
B) Increase the number of column families from one to ten to distribute columns across more storage files.
C) Switch the application from row key range scans to full table scans to avoid tablet boundary lookups.
D) Reduce the instance storage capacity to force Bigtable to compact tablets more aggressively.
*   **Correct Answer:** A) Enable replication by adding a second Bigtable cluster in a different zone and use application-side routing to send reads to the least-loaded cluster.
*   **Distractor Analysis:**
    *   *Why A is correct:* High tail latency in Bigtable is often caused by a single hot tablet server or transient network issues on one node. Adding a second cluster in the same instance allows the client to retry or route around a slow node, reducing p99 latency. Bigtable's built-in App Profiles support read routing policies between clusters.
    *   *Why B is incorrect:* Column families affect storage grouping on disk; increasing their count does not reduce tail latency caused by tablet server load imbalance.
    *   *Why C is incorrect:* Full table scans are significantly more expensive and slower than targeted row key scans; this would increase latency, not reduce it.
    *   *Why D is incorrect:* Reducing storage capacity does not trigger compaction or improve read latency; it may cause storage quota errors.

---

**Question 5**
When securing a Cloud Bigtable instance, you must mitigate the risk of **unauthorized access to Bigtable backup exports stored in Cloud Storage exposing all customer data**. Which control best addresses this vulnerability?
A) Enable Cloud Storage bucket-level encryption using Customer-Managed Encryption Keys (CMEK) for the export destination bucket.
B) Enforce parameterized queries and prepared statements in all application code interacting with Bigtable.
C) Configure the Bigtable instance to use Private IP only and disable public access.
D) Enable Bigtable Change Data Capture (CDC) to detect unauthorized reads on backup files.
*   **Correct Answer:** A) Enable Cloud Storage bucket-level encryption using Customer-Managed Encryption Keys (CMEK) for the export destination bucket.
*   **Distractor Analysis:**
    *   *Why A is correct:* Bigtable backups exported to Cloud Storage are files at rest. Applying CMEK to the destination Cloud Storage bucket ensures that the exported data files are encrypted with a key that only your organization controls, making them unreadable to unauthorized parties even if accessed directly.
    *   *Why B is incorrect:* Bigtable uses an API-based data model, not SQL strings; parameterized queries apply to SQL injection in relational databases and are not relevant to Bigtable access patterns.
    *   *Why C is incorrect:* Private IP restricts network-level access to the live Bigtable service endpoint but does not affect the security of exported backup files stored in Cloud Storage.
    *   *Why D is incorrect:* Bigtable Change Data Capture streams data change events for replication purposes; it does not monitor or restrict access to static backup export files.

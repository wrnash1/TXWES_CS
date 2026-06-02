# Video Script: Module 05 — Bigtable: Wide-Column NoSQL at Scale (Part 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 11–13 minutes

---

### Opening

**[SHOW SLIDE: Module 05 Part 2 — Schema Patterns, Scaling, Replication, and Exam Tips]**

Welcome back. I am Professor Nash, and this is Part 2 of Module 05.

In Part 1 we covered Bigtable's architecture, data model, and row key design principles. Now we go deeper into column family design, cluster scaling, replication, the cbt CLI tool, and the exam scenarios where Bigtable appears.

---

### Section 1 — Column Family Design

**[SHOW SLIDE: Column family design guidelines]**

Column families in Bigtable are analogous to column groups in traditional wide-column stores. Each column family has its own garbage collection policy and is stored contiguously on disk — rows within the same column family are read together from storage.

Design guidelines for column families:

Keep the number of column families small — ideally one to three per table. Bigtable is optimized for a small number of column families with many dynamic column qualifiers within each family, not many distinct families.

Group columns by access pattern. If a query almost always reads columns A, B, and C together but rarely reads columns D and E, put A, B, C in one family and D, E in another. Reads load entire column families, so separating rarely-accessed columns avoids loading unnecessary data.

Set garbage collection policies per family. You can configure a family to keep only the N most recent versions of each cell, or to delete versions older than a specified duration.

**[SHOW CODE]**

```bash
# Create a Bigtable table with two column families via cbt
cbt createtable sensor_readings
cbt createfamily sensor_readings cf_metrics
cbt createfamily sensor_readings cf_metadata

# Set garbage collection: keep only 1 version per cell in cf_metrics
cbt setgcpolicy sensor_readings cf_metrics maxversions=1

# Set GC by age: delete cells older than 30 days in cf_metadata
cbt setgcpolicy sensor_readings cf_metadata maxage=30d
```

**[END CODE]**

---

### Section 2 — Reading and Writing Data with cbt

**[SHOW CODE]**

```bash
# Install cbt tool (Cloud Shell has it pre-installed)
# Set up .cbtrc configuration
echo project = YOUR_PROJECT_ID > ~/.cbtrc
echo instance = txwes-bigtable >> ~/.cbtrc

# Write a row
cbt set sensor_readings \
    "sensor001#20250115T120000" \
    cf_metrics:temperature=72.4 \
    cf_metrics:humidity=45.2

# Read a single row by exact key
cbt read sensor_readings prefix="sensor001#20250115T120000"

# Range scan: all readings for sensor001 (prefix scan)
cbt read sensor_readings prefix="sensor001#"

# Read with a row limit
cbt read sensor_readings prefix="sensor001#" count=10
```

**[END CODE]**

The row key `sensor001#20250115T120000` encodes both the sensor identifier and the timestamp. A range scan with prefix `sensor001#` returns all readings for that sensor in lexicographic order. If you use a reversed timestamp (subtract from a large constant), the most recent readings appear first in the scan.

---

### Section 3 — Cluster Scaling and Performance

**[SHOW CONSOLE: Bigtable instance — Edit cluster — number of nodes]**

Bigtable throughput scales linearly with the number of nodes. Adding one node to a cluster proportionally increases both read and write throughput. This is the key scaling mechanism for Bigtable — you add nodes when you need more throughput, not to add storage (storage scales independently on Colossus).

Each Bigtable node provides approximately:

- 10,000 rows per second for reads of 1 KB rows
- 10,000 rows per second for writes of 1 KB rows
- 220 MB/s of throughput for sequential scans

For production workloads requiring high throughput, start with at least 3 nodes per cluster. For development and testing, 1 node is sufficient.

**[SHOW CODE]**

```bash
# Create a Bigtable instance with 3 nodes
gcloud bigtable instances create txwes-bigtable \
    --display-name="TXWES Lab Instance" \
    --cluster=txwes-bigtable-cluster \
    --cluster-zone=us-central1-b \
    --cluster-num-nodes=3 \
    --instance-type=PRODUCTION

# Scale the cluster to 5 nodes
gcloud bigtable clusters update txwes-bigtable-cluster \
    --instance=txwes-bigtable \
    --num-nodes=5
```

**[END CODE]**

---

### Section 4 — Replication

**[SHOW SLIDE: Bigtable replication — two clusters in different zones or regions]**

Cloud Bigtable supports replication by adding a second cluster to an instance. The two clusters replicate data asynchronously. Replication serves two purposes.

High availability: if one cluster becomes unavailable, the application can automatically failover to the second cluster. This requires an App Profile configured with multi-cluster routing.

Read performance: distribute read requests across two clusters in different regions to reduce latency for geographically distributed users.

**[SHOW CODE]**

```bash
# Add a replication cluster in a second zone
gcloud bigtable clusters create txwes-bigtable-cluster-2 \
    --instance=txwes-bigtable \
    --zone=us-central1-c \
    --num-nodes=3

# Create an App Profile with multi-cluster routing for HA
gcloud bigtable app-profiles create multi-cluster-profile \
    --instance=txwes-bigtable \
    --route-any \
    --description="Multi-cluster routing for HA"
```

**[END CODE]**

Important: Bigtable replication is asynchronous. A write to cluster 1 may not be immediately visible when reading from cluster 2. This is eventual consistency — acceptable for time-series analytics but not for applications requiring immediate consistency after writes.

---

### Section 5 — Key Visualizer

**[SHOW CONSOLE: Bigtable Key Visualizer — heatmap showing read/write density by row key range]**

Key Visualizer is a Bigtable diagnostic tool that shows a heatmap of read and write activity across your row key space over time. A healthy heatmap shows even distribution of activity across the key space. A hotspot appears as a bright vertical band in one area of the heatmap — indicating that one narrow row key range is receiving most of the traffic.

When you see a hotspot in Key Visualizer, the diagnosis is almost always a poor row key design. The fix is to redesign the key to distribute the workload — which typically requires a table migration because row keys are immutable in Bigtable.

---

### Section 6 — Exam Tips for Module 05

**[SHOW SLIDE: Bigtable exam tips]**

Tip one: workload identification. Bigtable is the answer when a scenario describes time-series data, IoT telemetry, high-throughput single-row reads and writes at petabyte scale, or financial tick data. Bigtable is not the answer when the scenario requires JOINs, multi-row ACID transactions, or complex SQL queries.

Tip two: no secondary indexes. Bigtable has no secondary indexes. All efficient queries are based on the row key. If a scenario describes needing to look up data by multiple different fields efficiently, and proposes Bigtable, that is a design problem — the row key must be designed to support the required access patterns.

Tip three: hotspot prevention. Sequential timestamps or incrementing integers as leading row key components are hotspot anti-patterns. The exam tests this — a scenario describing degrading write performance on a Bigtable table points to a bad row key design.

Tip four: column families. Column qualifiers are dynamic — they do not need to be pre-defined. Column families must be defined at table creation. There should be a small number of column families (one to three), not one family per attribute.

Tip five: garbage collection is per column family. You configure maxversions (keep latest N versions) or maxage (delete versions older than N days). There is no row-level DELETE in the traditional sense; data is deleted through garbage collection policies.

Tip six: Bigtable vs. BigQuery. Bigtable is for operational, high-throughput, low-latency reads and writes at large scale. BigQuery is for analytical queries over large historical datasets. Both handle petabyte-scale data but serve completely different access patterns.

Tip seven: the minimum production cluster size is 1 node, but meaningful production workloads need at least 3 nodes for throughput. Scaling is linear — double the nodes, double the throughput.

Tip eight: replication between Bigtable clusters is eventually consistent. If a scenario requires strong consistency after writes across clusters, Bigtable replication alone does not provide it.

---

### Closing — Module 05 Wrap-Up

**[SHOW SLIDE: Module 05 complete]**

That completes Module 05. You now understand Bigtable's wide-column data model, row key design principles, column family design, cluster scaling, and replication.

Your lab walks you through creating a Bigtable instance, designing a schema for sensor data, writing and reading rows using the cbt CLI, and analyzing a hotspot scenario.

In Module 06 we move to Firestore and Datastore — Google Cloud's document database services. The data model is completely different again: document-oriented, hierarchical, and designed for mobile and web application backends.

See you in Module 06.

---

Reference: cloud.google.com/learn

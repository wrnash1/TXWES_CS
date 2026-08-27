# Lab Activity: Module 05 — Bigtable: Wide-Column NoSQL at Scale

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Total Points: 100

---

### Lab Overview

In this lab you will create a Cloud Bigtable instance, design a table schema for IoT sensor data, insert and query rows using the cbt CLI, configure garbage collection policies, and analyze a hotspot row key design problem. These skills are directly tested in the Bigtable domain of the GCP Database Engineer exam.

Estimated completion time: 60–75 minutes.

---

### Prerequisites

- Google Cloud student project with billing enabled
- Module 05 video scripts and reading guide reviewed
- Cloud Shell available in the Google Cloud Console

Cost note: Cloud Bigtable production instances are billed per node per hour. A 1-node development instance costs approximately $0.065/hour. Delete the instance immediately after completing all deliverables.

---

### Part 1 — Create a Bigtable Instance (10 points)

#### Step 1 — Provision the Instance

```bash
gcloud bigtable instances create txwes-bigtable-lab \
    --display-name="TXWES CIS-4327 Lab 05" \
    --cluster=txwes-bt-cluster \
    --cluster-zone=us-central1-b \
    --cluster-num-nodes=1 \
    --instance-type=PRODUCTION
```

Wait approximately 1–2 minutes for the instance to become ready.

#### Step 2 — Configure cbt

```bash
# Configure the cbt tool to use your project and instance
echo "project = $(gcloud config get-value project)" > ~/.cbtrc
echo "instance = txwes-bigtable-lab" >> ~/.cbtrc

# Verify the configuration
cat ~/.cbtrc

# List instances to confirm
cbt listinstances
```

**Deliverable 1 (10 points)**: Take a screenshot showing the `cbt listinstances` output with txwes-bigtable-lab listed. Save as `lab05_screenshot_01.png`.

---

### Part 2 — Design and Create the Schema (20 points)

You are designing a Bigtable schema for an industrial IoT platform that collects temperature, humidity, and pressure readings from 10,000 factory floor sensors every 5 seconds.

#### Step 3 — Create the Table and Column Families

```bash
# Create the sensor readings table
cbt createtable sensor_readings

# Create two column families
cbt createfamily sensor_readings cf_metrics
cbt createfamily sensor_readings cf_metadata

# Set GC policy: keep only the latest 1 version for metrics (saves storage)
cbt setgcpolicy sensor_readings cf_metrics maxversions=1

# Set GC policy: delete metadata older than 90 days
cbt setgcpolicy sensor_readings cf_metadata maxage=90d

# Verify the table structure
cbt ls
```

**Deliverable 2 (10 points)**: In your lab report, answer these three questions about your schema design.

First: explain why cf_metrics uses maxversions=1 while cf_metadata uses maxage=90d. What is the data lifecycle difference between sensor metrics and sensor metadata?

Second: the row key format you will use is `sensorId#reversedTimestamp`. Explain what "reversed timestamp" means in this context — specifically what value you would compute to make timestamp `20250115T120000` sort after `20250115T110000` when reversed.

Third: why is using the plain timestamp `20250115T120000` as the leading row key component a hotspot anti-pattern for this workload?

**Deliverable 3 (10 points)**: Take a screenshot of the `cbt ls` output showing both column families listed for sensor_readings. Save as `lab05_screenshot_02.png`.

---

### Part 3 — Insert and Query Data (35 points)

#### Step 4 — Write Rows

For this lab we use simplified keys with a timestamp suffix that simulates the reversed pattern.

```bash
# Write readings for sensor S-001
cbt set sensor_readings "S-001#99999999999-20250115120000" \
    cf_metrics:temperature=72.4 \
    cf_metrics:humidity=45.2 \
    cf_metrics:pressure=1013.2 \
    cf_metadata:location="Assembly Line A" \
    cf_metadata:unit="Celsius/Percent/hPa"

cbt set sensor_readings "S-001#99999999999-20250115120500" \
    cf_metrics:temperature=72.6 \
    cf_metrics:humidity=45.0 \
    cf_metrics:pressure=1013.1

cbt set sensor_readings "S-001#99999999999-20250115121000" \
    cf_metrics:temperature=73.1 \
    cf_metrics:humidity=44.8 \
    cf_metrics:pressure=1012.9

# Write readings for sensor S-002
cbt set sensor_readings "S-002#99999999999-20250115120000" \
    cf_metrics:temperature=68.1 \
    cf_metrics:humidity=52.3 \
    cf_metrics:pressure=1014.0 \
    cf_metadata:location="Assembly Line B" \
    cf_metadata:unit="Celsius/Percent/hPa"

cbt set sensor_readings "S-002#99999999999-20250115120500" \
    cf_metrics:temperature=68.4 \
    cf_metrics:humidity=52.1 \
    cf_metrics:pressure=1013.8

# Write a reading for sensor S-003
cbt set sensor_readings "S-003#99999999999-20250115120000" \
    cf_metrics:temperature=70.0 \
    cf_metrics:humidity=49.9 \
    cf_metrics:pressure=1013.5 \
    cf_metadata:location="Storage Room C"
```

#### Step 5 — Read Data

Run each of the following read commands.

```bash
# Read a single row by exact key
cbt read sensor_readings \
    prefix="S-001#99999999999-20250115120000"
```

```bash
# Range scan: all readings for S-001 (prefix scan)
cbt read sensor_readings \
    prefix="S-001#"
```

```bash
# Range scan with row limit: latest 2 readings for S-001
cbt read sensor_readings \
    prefix="S-001#" \
    count=2
```

```bash
# Read all rows in the table
cbt read sensor_readings
```

**Deliverable 4 (20 points)**: Take a screenshot of the output from each of the four read commands above. Label each screenshot with the query number. For the prefix scan result, write one sentence explaining why the rows appear in the order they do. Save screenshots as `lab05_screenshot_03.png` through `lab05_screenshot_06.png`.

**Deliverable 5 (15 points)**: In your lab report, write a short analysis (100–150 words) explaining the following. If this table had 10 billion rows for 10,000 sensors, why is the prefix scan for a single sensor still fast? What property of Bigtable's storage model makes this efficient? What would happen to performance if you needed to find all sensors with temperature above 75 degrees across all sensors?

---

### Part 4 — Hotspot Analysis (20 points)

#### Step 6 — Write a Hotspot Analysis

**Deliverable 6 (20 points)**: A teammate proposes the following row key design for the sensor readings table:

```text
Row key: timestamp#sensorId
Example: 20250115120000#S-001
```

In your lab report, write a structured analysis of this design addressing the following four points.

First: describe what happens to Bigtable tablet distribution when timestamps are used as the leading component and new readings arrive every 5 seconds from 10,000 sensors simultaneously.

Second: identify which node(s) in a 3-node Bigtable cluster would receive the write traffic for new sensor readings with this key design, and which nodes would be idle.

Third: explain what output you would expect to see in the Key Visualizer tool if this key design were deployed to production — specifically what the heatmap would look like.

Fourth: propose the corrected row key design (using the reversed timestamp composite pattern from this lab) and explain how it distributes writes across all three cluster nodes.

---

### Part 5 — Clean Up (Required)

```bash
gcloud bigtable instances delete txwes-bigtable-lab --quiet
```

---

### Lab Submission Checklist

- Deliverable 1 (10 pts) — Instance list screenshot
- Deliverable 2 (10 pts) — Three written schema design questions answered
- Deliverable 3 (10 pts) — Column family list screenshot
- Deliverable 4 (20 pts) — Four query result screenshots with sort order explanation
- Deliverable 5 (15 pts) — Written analysis of scan efficiency and cross-sensor query limitation
- Deliverable 6 (20 pts) — Hotspot analysis of proposed bad row key design

---

### Grading Rubric — 100 Points Total

| Deliverable | Points | Criteria |
|---|---|---|
| 1 — Instance list screenshot | 10 | Instance listed with READY state |
| 2 — Schema design questions | 10 | All three questions answered accurately |
| 3 — Column family screenshot | 10 | Both families shown with GC policies visible |
| 4 — Four query screenshots | 20 | All four results shown; sort order explanation accurate |
| 5 — Scan efficiency analysis | 15 | Explains tablet range scan; identifies limitation of cross-sensor queries |
| 6 — Hotspot analysis | 20 | All four analysis points addressed accurately; correct corrected design proposed |
| Deductions | up to -10 | Instance not deleted after completion |

---

Reference: cloud.google.com/learn

---

## Part 9 — Challenge Exercise

### Challenge 1: Designing and Testing a Secondary Lookup Table

Bigtable has no native secondary indexes. Implement an application-managed secondary index using a second table to support cross-key queries.

Create a second table called `sensor_by_type` with the row key `sensorType#reverseTimestamp#sensorId`:

```bash
cbt createtable sensor_by_type
cbt createfamily sensor_by_type cf_ref
```

Then complete the following steps:

1. Insert 10 rows into `sensor_by_type` that mirror the sensor readings in your primary table, using the new key format. The cell value in `cf_ref:primary_key` should store the corresponding primary table row key.
2. Perform a range scan on `sensor_by_type` for `sensorType = temperature` using prefix `temperature#` and record the result. Verify that the returned `cf_ref:primary_key` values map back to valid rows in the primary table.
3. Write a two-paragraph analysis: the first paragraph explains the consistency risk of maintaining two tables (what happens if a write to the primary table succeeds but the secondary lookup write fails); the second paragraph describes how a compensating transaction or application retry strategy mitigates this risk.

### Challenge 2: GC Policy Impact on Storage and Read Latency

Modify the GC policy on a column family and observe the effect on storage.

Start by writing 20 versions of a cell value to a single row:

```bash
for i in $(seq 1 20); do
  cbt set sensors sensor_001 "cf_raw:temperature=reading_v${i}"
  sleep 0.1
done
```

Then complete the following steps:

1. Read the row with `cbt read sensors sensor_001` and count how many versions are returned. Record the output.
2. Change the GC policy to `maxversions=3`:

```bash
cbt setgcpolicy sensors cf_raw maxversions=3
```

3. Wait 2–3 minutes for compaction to run (or trigger it by reading the row repeatedly), then re-read the row and record how many versions remain. Note whether the change took effect immediately or after a delay, and explain why.

### Reflection Questions

1. In Challenge 1, if the application crashes after writing to the primary table but before writing to the secondary lookup table, how would a subsequent read from the secondary index return incorrect or missing results, and what operational procedure would you use to detect and repair this inconsistency?
2. In Challenge 2, why does a GC policy change not take effect immediately upon setting it, and what does this reveal about the underlying LSM (log-structured merge tree) storage architecture that Bigtable uses?

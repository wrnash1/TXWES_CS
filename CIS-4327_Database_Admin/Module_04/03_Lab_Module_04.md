# Lab Activity: Module 04 — Cloud Spanner: Globally Distributed Databases

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Total Points: 100

---

### Lab Overview

In this lab you will create a Cloud Spanner instance and database, design and implement a schema using Spanner DDL with interleaved tables and secondary indexes, insert and query data, and create a managed backup. You will also evaluate primary key design choices and explain their impact on write performance.

Estimated completion time: 60–75 minutes.

---

### Prerequisites

- Google Cloud student project with billing enabled
- Module 04 video scripts and reading guide reviewed
- Cloud Shell available in the Google Cloud Console

Cost note: Cloud Spanner is billed per processing unit per hour. Using 100 processing units for one lab session costs approximately $0.09. Delete the instance promptly after completing all deliverables.

---

### Part 1 — Create a Cloud Spanner Instance (15 points)

#### Step 1 — Provision the Instance

```bash
# Create a regional Spanner instance with 100 processing units (minimum)
gcloud spanner instances create txwes-spanner-lab \
    --config=regional-us-central1 \
    --description="TXWES CIS-4327 Lab 04" \
    --processing-units=100
```

#### Step 2 — Create the Application Database

```bash
gcloud spanner databases create inventory_db \
    --instance=txwes-spanner-lab
```

#### Step 3 — Verify the Instance

```bash
gcloud spanner instances describe txwes-spanner-lab \
    --format="table(name,config,processingUnits,state)"
```

**Deliverable 1 (10 points)**: Take a screenshot showing the instance name, config (regional-us-central1), processingUnits (100), and state (READY). Save as `lab04_screenshot_01.png`.

**Deliverable 2 (5 points)**: In your lab report, explain in two sentences what the processing-units value of 100 represents in terms of query capacity, and what value you would use for a production instance handling 1,000 writes per second.

---

### Part 2 — Schema Design with DDL (25 points)

#### Step 4 — Create the Schema

Apply the DDL for a product inventory system. Warehouses are the parent entity. Products are interleaved in Warehouses.

```bash
gcloud spanner databases ddl update inventory_db \
    --instance=txwes-spanner-lab \
    --ddl='CREATE TABLE Warehouses (
    WarehouseId  STRING(36)   NOT NULL,
    WarehouseName STRING(100) NOT NULL,
    City          STRING(100) NOT NULL,
    Region        STRING(50)  NOT NULL
) PRIMARY KEY (WarehouseId)'
```

```bash
gcloud spanner databases ddl update inventory_db \
    --instance=txwes-spanner-lab \
    --ddl='CREATE TABLE Products (
    WarehouseId   STRING(36)   NOT NULL,
    ProductId     STRING(36)   NOT NULL,
    ProductName   STRING(200)  NOT NULL,
    Category      STRING(100)  NOT NULL,
    StockQuantity INT64        NOT NULL,
    UnitPrice     FLOAT64      NOT NULL
) PRIMARY KEY (WarehouseId, ProductId),
  INTERLEAVE IN PARENT Warehouses ON DELETE CASCADE'
```

```bash
gcloud spanner databases ddl update inventory_db \
    --instance=txwes-spanner-lab \
    --ddl='CREATE INDEX IdxProductsByCategory
    ON Products (Category)
    STORING (ProductName, StockQuantity)'
```

**Deliverable 3 (15 points)**: In your lab report, answer the following three questions.

First: why is WarehouseId a STRING(36) rather than an INT64 auto-increment? Explain in terms of Spanner's hotspot behavior.

Second: what does INTERLEAVE IN PARENT Warehouses mean physically? Describe where the Products rows for WarehouseId 'W-001' are stored relative to the Warehouse row for 'W-001'.

Third: the IdxProductsByCategory index uses STORING (ProductName, StockQuantity). Explain what STORING does and why it eliminates a back-join for a query that filters by Category and returns ProductName and StockQuantity.

**Deliverable 4 (10 points)**: Write and run a second CREATE INDEX statement (not provided above) that creates a useful index for a query pattern of your choice on the Products table. Include the DDL statement and a one-sentence explanation of what query it optimizes. Include both in your lab report.

---

### Part 3 — Insert and Query Data (30 points)

#### Step 5 — Insert Sample Data

```bash
gcloud spanner databases execute-sql inventory_db \
    --instance=txwes-spanner-lab \
    --sql="INSERT INTO Warehouses (WarehouseId, WarehouseName, City, Region)
          VALUES ('a1b2c3d4-0001', 'Fort Worth Central', 'Fort Worth', 'South'),
                 ('a1b2c3d4-0002', 'Dallas North',       'Dallas',     'South'),
                 ('a1b2c3d4-0003', 'Austin East',        'Austin',     'Central')"
```

```bash
gcloud spanner databases execute-sql inventory_db \
    --instance=txwes-spanner-lab \
    --sql="INSERT INTO Products (WarehouseId, ProductId, ProductName, Category, StockQuantity, UnitPrice)
          VALUES
          ('a1b2c3d4-0001', 'p-aa11', 'Wireless Keyboard', 'Electronics', 150, 49.99),
          ('a1b2c3d4-0001', 'p-bb22', 'USB-C Hub',         'Electronics',  80, 34.99),
          ('a1b2c3d4-0001', 'p-cc33', 'Desk Lamp',         'Office',       60, 24.99),
          ('a1b2c3d4-0002', 'p-dd44', 'Laptop Stand',      'Electronics',  45, 39.99),
          ('a1b2c3d4-0002', 'p-ee55', 'Notebook Set',      'Office',      500,  8.99),
          ('a1b2c3d4-0003', 'p-ff66', 'Sticky Notes',      'Office',     1000,  4.99)"
```

#### Step 6 — Run Queries

Run the following queries and record results.

```bash
# Query 1: All products in Fort Worth Central
gcloud spanner databases execute-sql inventory_db \
    --instance=txwes-spanner-lab \
    --sql="SELECT ProductName, Category, StockQuantity, UnitPrice
          FROM   Products
          WHERE  WarehouseId = 'a1b2c3d4-0001'
          ORDER  BY ProductName"
```

```bash
# Query 2: All Electronics products across all warehouses (uses secondary index)
gcloud spanner databases execute-sql inventory_db \
    --instance=txwes-spanner-lab \
    --sql="SELECT WarehouseId, ProductName, StockQuantity
          FROM   Products@{FORCE_INDEX=IdxProductsByCategory}
          WHERE  Category = 'Electronics'
          ORDER  BY ProductName"
```

```bash
# Query 3: Join warehouses and products with aggregation
gcloud spanner databases execute-sql inventory_db \
    --instance=txwes-spanner-lab \
    --sql="SELECT w.WarehouseName,
                  COUNT(p.ProductId)       AS product_count,
                  SUM(p.StockQuantity)     AS total_stock
          FROM   Warehouses w
          JOIN   Products   p ON w.WarehouseId = p.WarehouseId
          GROUP  BY w.WarehouseName
          ORDER  BY total_stock DESC"
```

**Deliverable 5 (20 points)**: Take a screenshot of the result set for each of the three queries. Below each screenshot, write one sentence explaining the business question the query answers. Save as `lab04_screenshot_02.png`, `lab04_screenshot_03.png`, and `lab04_screenshot_04.png`.

**Deliverable 6 (10 points)**: In Query 2 you used `@{FORCE_INDEX=IdxProductsByCategory}`. In your lab report, explain what this hint does and why you might need to force index use in Spanner when a secondary index is available.

---

### Part 4 — Backup and Recovery (15 points)

#### Step 7 — Create a Managed Backup

```bash
# Calculate an expiration date 7 days from today
EXPIRY=$(date -u -d "+7 days" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || \
         date -u -v+7d +%Y-%m-%dT%H:%M:%SZ)

gcloud spanner backups create lab04-backup \
    --instance=txwes-spanner-lab \
    --database=inventory_db \
    --expiration-date="$EXPIRY"

# List backups to confirm
gcloud spanner backups list \
    --instance=txwes-spanner-lab
```

**Deliverable 7 (10 points)**: Take a screenshot of the backup list output showing lab04-backup with a READY state. Save as `lab04_screenshot_05.png`.

**Deliverable 8 (5 points)**: In your lab report, explain the difference between Cloud Spanner backup/restore and Cloud Spanner point-in-time recovery. Which requires additional configuration, and which is built in automatically?

---

### Part 5 — Primary Key Design Analysis (15 points)

#### Step 8 — Written Analysis

**Deliverable 9 (15 points)**: In your lab report, write a structured analysis of the following scenario.

A team is designing a Cloud Spanner table called `SensorReadings` to store IoT sensor data. One engineer proposes: `SensorReadingId INT64 NOT NULL` using a sequential counter as the primary key, claiming it simplifies inserts from the IoT pipeline.

In your analysis, explain: (1) why this key choice creates a hotspot on the Cloud Spanner tablet responsible for the highest sequential key values, (2) what specific write performance symptom the team would observe as data volume grows, and (3) propose two alternative primary key designs that would distribute writes across tablets while still allowing efficient retrieval by sensor and time range.

---

### Part 6 — Clean Up (Required)

Delete the Spanner instance to avoid continued billing. Deleting the instance also deletes all databases and backups within it.

```bash
gcloud spanner instances delete txwes-spanner-lab --quiet
```

---

### Lab Submission Checklist

- Deliverable 1 (10 pts) — Instance configuration screenshot
- Deliverable 2 (5 pts) — Written explanation of processing units
- Deliverable 3 (15 pts) — Written answers to three schema design questions
- Deliverable 4 (10 pts) — Custom CREATE INDEX with explanation
- Deliverable 5 (20 pts) — Three query result screenshots with business question explanations
- Deliverable 6 (10 pts) — Written explanation of FORCE_INDEX hint
- Deliverable 7 (10 pts) — Backup list screenshot showing READY state
- Deliverable 8 (5 pts) — Written comparison of backup vs. PITR
- Deliverable 9 (15 pts) — Primary key hotspot analysis

---

### Grading Rubric — 100 Points Total

| Deliverable | Points | Criteria |
|---|---|---|
| 1 — Instance config screenshot | 10 | READY state, regional-us-central1 config, 100 PUs visible |
| 2 — Processing units explanation | 5 | Correct PU-to-node conversion; reasonable production recommendation |
| 3 — Schema design questions | 15 | All three questions answered accurately using correct Spanner terminology |
| 4 — Custom CREATE INDEX | 10 | Valid Spanner DDL; reasonable optimization use case explained |
| 5 — Three query screenshots | 20 | All three results shown; one-sentence business explanation each |
| 6 — FORCE_INDEX explanation | 10 | Accurate explanation of query hint and when manual index selection is needed |
| 7 — Backup screenshot | 10 | READY backup visible in list |
| 8 — Backup vs. PITR comparison | 5 | Accurate distinction; correct statement about configuration requirements |
| 9 — Hotspot analysis | 15 | Hotspot mechanism explained; symptom identified; two valid alternative designs proposed |
| Deductions | up to -10 | Instance not deleted after completion |

---

Reference: cloud.google.com/learn

---

## Part 9 — Challenge Exercise

### Challenge 1: Demonstrating Hotspot vs. Distributed Insert Performance

Create two tables — one with a sequential INT64 primary key and one with a UUID STRING(36) key — and compare insert throughput.

```sql
CREATE TABLE HotspotOrders (
    OrderId     INT64  NOT NULL,
    CustomerId  STRING(36) NOT NULL,
    OrderDate   DATE   NOT NULL,
    Amount      FLOAT64 NOT NULL
) PRIMARY KEY (OrderId);

CREATE TABLE DistributedOrders (
    OrderId     STRING(36) NOT NULL DEFAULT (GENERATE_UUID()),
    CustomerId  STRING(36) NOT NULL,
    OrderDate   DATE       NOT NULL,
    Amount      FLOAT64    NOT NULL
) PRIMARY KEY (OrderId);
```

Then complete the following steps:

1. Use the Cloud Spanner Workload Generator (or insert 1000 rows via the gcloud `spanner rows insert` command in a loop) into both tables. Record the wall-clock time for each batch.
2. In the Google Cloud Console, navigate to your Spanner instance's **Monitoring** tab and capture a screenshot of the CPU utilization per split chart during each insert batch. Identify which table shows CPU concentration on a single split vs. distribution across splits.
3. Write a two-paragraph analysis: the first paragraph explains the tablet-split mechanism that causes the hotspot; the second paragraph describes two alternative primary key designs (bit-reversal prefix, hash prefix) and when each is appropriate.

### Challenge 2: Covering Index Optimization for a Reporting Query

In your lab Spanner database, create a secondary index without STORING and observe a back-join, then add STORING and confirm it is eliminated.

```sql
-- Create index without STORING
CREATE INDEX IdxOrderByCustomer ON Orders (CustomerId);

-- Run a query that requires a back-join (projects OrderDate not in index)
SELECT CustomerId, OrderDate, TotalAmount
FROM   Orders@{FORCE_INDEX=IdxOrderByCustomer}
WHERE  CustomerId = 'C001';
```

Then complete the following steps:

1. Run `EXPLAIN` on the query above and record whether a back-join to the base table appears in the execution plan.
2. Drop the index and recreate it with STORING, then re-run the same query with `FORCE_INDEX=IdxOrderByCustomer` and capture the new EXPLAIN output:

```sql
DROP INDEX IdxOrderByCustomer;

CREATE INDEX IdxOrderByCustomer ON Orders (CustomerId)
    STORING (OrderDate, TotalAmount);
```

3. Confirm the back-join is eliminated in the new plan and write one paragraph explaining the performance difference.

### Reflection Questions

1. In Challenge 1, what specific metric in the Cloud Spanner Monitoring tab most clearly showed that write load was unevenly distributed across splits for the sequential-key table, and what would an ideal distribution look like?
2. In Challenge 2, under what conditions would adding a STORING clause to a secondary index be counterproductive — that is, when does the extra storage cost of STORING outweigh its read performance benefit?

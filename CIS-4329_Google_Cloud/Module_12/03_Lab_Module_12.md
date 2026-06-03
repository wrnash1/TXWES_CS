# Lab: Module 12 — BigQuery and Data Analytics

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Lab Overview

In this lab you will create a BigQuery dataset, load sample data, run SQL queries,
create partitioned and clustered tables, practice cost estimation with dry\_run, and
connect your dataset to Looker Studio for visualization.

**Estimated time**: 60–75 minutes

**Cost estimate**: Under $1.00 USD (free tier covers 1 TB queries/month and 10 GB storage)

---

### Prerequisites

- A GCP project with billing enabled
- BigQuery API enabled (enabled by default in most projects)
- Cloud Shell or gcloud CLI authenticated

```bash
gcloud services enable bigquery.googleapis.com
```

---

### Part 1: Create Dataset and Load Data

#### Task 1.1: Create a Dataset

```bash
gcloud config set project YOUR_PROJECT_ID

# Create a dataset in the US multi-region
bq mk \
  --dataset \
  --location=US \
  --description="Lab 12 e-commerce analytics" \
  YOUR_PROJECT_ID:ecommerce

# Verify the dataset was created
bq ls YOUR_PROJECT_ID:
```

#### Task 1.2: Create a Table and Load Sample Data

Create a local sample CSV file and load it:

```bash
# Create a sample orders CSV
cat > /tmp/orders.csv << 'EOF'
order_id,customer_id,order_date,amount,status,region
1001,201,2024-01-05,149.99,completed,west
1002,202,2024-01-06,89.00,completed,east
1003,203,2024-01-07,299.50,pending,west
1004,201,2024-01-08,55.00,completed,central
1005,204,2024-01-09,410.75,completed,east
1006,205,2024-01-10,75.00,cancelled,west
1007,202,2024-02-01,199.00,completed,east
1008,206,2024-02-02,320.00,completed,central
1009,201,2024-02-03,88.50,pending,west
1010,207,2024-02-04,175.00,completed,east
EOF

# Upload to Cloud Storage (needed for BQ load)
gsutil mb -l US gs://YOUR_PROJECT_ID-lab12-data/
gsutil cp /tmp/orders.csv gs://YOUR_PROJECT_ID-lab12-data/

# Create the table
bq mk --table \
  YOUR_PROJECT_ID:ecommerce.orders \
  order_id:INTEGER,customer_id:INTEGER,order_date:DATE,amount:FLOAT,status:STRING,region:STRING

# Load the data
bq load \
  --source_format=CSV \
  --skip_leading_rows=1 \
  YOUR_PROJECT_ID:ecommerce.orders \
  gs://YOUR_PROJECT_ID-lab12-data/orders.csv

# Verify the load
bq show YOUR_PROJECT_ID:ecommerce.orders
```

---

### Part 2: Run SQL Queries

#### Task 2.1: Basic Aggregation Query

```bash
bq query \
  --use_legacy_sql=false \
  'SELECT
     status,
     COUNT(*) AS order_count,
     ROUND(SUM(amount), 2) AS total_revenue
   FROM `YOUR_PROJECT_ID.ecommerce.orders`
   GROUP BY status
   ORDER BY total_revenue DESC'
```

Record the output in your submission document.

#### Task 2.2: Query with WHERE Clause and Save to Table

```bash
bq query \
  --use_legacy_sql=false \
  --destination_table=YOUR_PROJECT_ID:ecommerce.completed_orders \
  --replace \
  'SELECT order_id, customer_id, order_date, amount, region
   FROM `YOUR_PROJECT_ID.ecommerce.orders`
   WHERE status = "completed"
   ORDER BY order_date'

# Verify the destination table was created
bq show YOUR_PROJECT_ID:ecommerce.completed_orders
```

#### Task 2.3: Dry Run — Estimate Query Cost

```bash
bq query \
  --use_legacy_sql=false \
  --dry_run \
  'SELECT * FROM `YOUR_PROJECT_ID.ecommerce.orders`'
```

Note the bytes processed estimate. Then compare with a column-selective query:

```bash
bq query \
  --use_legacy_sql=false \
  --dry_run \
  'SELECT order_id, amount FROM `YOUR_PROJECT_ID.ecommerce.orders`'
```

Record both byte estimates and calculate the cost difference in your submission.

---

### Part 3: Partitioned and Clustered Tables

#### Task 3.1: Create a Partitioned Table

```bash
# Create a date-partitioned table
bq mk --table \
  --time_partitioning_field=order_date \
  --time_partitioning_type=DAY \
  --require_partition_filter=false \
  YOUR_PROJECT_ID:ecommerce.orders_partitioned \
  order_id:INTEGER,customer_id:INTEGER,order_date:DATE,amount:FLOAT,status:STRING,region:STRING

# Load the same data into the partitioned table
bq load \
  --source_format=CSV \
  --skip_leading_rows=1 \
  YOUR_PROJECT_ID:ecommerce.orders_partitioned \
  gs://YOUR_PROJECT_ID-lab12-data/orders.csv
```

#### Task 3.2: Compare Partition Pruning

```bash
# Full scan (no partition filter) — dry run
bq query \
  --use_legacy_sql=false \
  --dry_run \
  'SELECT COUNT(*) FROM `YOUR_PROJECT_ID.ecommerce.orders_partitioned`'

# With partition filter (partition pruning) — dry run
bq query \
  --use_legacy_sql=false \
  --dry_run \
  'SELECT COUNT(*) FROM `YOUR_PROJECT_ID.ecommerce.orders_partitioned`
   WHERE order_date BETWEEN "2024-01-01" AND "2024-01-31"'
```

Record both byte estimates. The second query should scan fewer bytes.

#### Task 3.3: Create a Partitioned and Clustered Table

```bash
bq mk --table \
  --time_partitioning_field=order_date \
  --time_partitioning_type=DAY \
  --clustering_fields=region,status \
  YOUR_PROJECT_ID:ecommerce.orders_clustered \
  order_id:INTEGER,customer_id:INTEGER,order_date:DATE,amount:FLOAT,status:STRING,region:STRING

bq load \
  --source_format=CSV \
  --skip_leading_rows=1 \
  YOUR_PROJECT_ID:ecommerce.orders_clustered \
  gs://YOUR_PROJECT_ID-lab12-data/orders.csv
```

---

### Part 4: Connect to Looker Studio

1. Open `https://lookerstudio.google.com` in a browser.
2. Click **Create** then **Report**.
3. Click **Add data** and select the **BigQuery** connector.
4. Authenticate and select your project, the `ecommerce` dataset, and the `orders` table.
5. Click **Add** then **Add to report**.
6. Add a **Scorecard** chart showing the total count of rows (order count).
7. Add a **Bar chart** with dimension = `status` and metric = `Record Count`.
8. Save the report.

Record the Looker Studio report URL in your submission.

---

### Part 5: Reflection Questions

1. You ran two dry\_run queries — one with `SELECT *` and one selecting only two columns.
   How many bytes did each scan, and what explains the difference?
2. The partitioned table dry\_run showed fewer bytes when you added a date filter. What
   is the technical term for this optimization, and how does BigQuery achieve it?
3. You created a table clustered on `region` and `status`. If a query filters only on
   `status` (not `region`), will clustering still help? Why or why not?
4. What is the difference between a native BigQuery table and an external table?
   When would you prefer an external table?
5. Describe one scenario where using `--require_partition_filter=true` would be
   appropriate and one scenario where it would be too restrictive.

---

### Part 6: Cleanup

```bash
# Delete the dataset and all its tables
bq rm --recursive --dataset --force YOUR_PROJECT_ID:ecommerce

# Delete the Cloud Storage bucket
gsutil rm -r gs://YOUR_PROJECT_ID-lab12-data/
```

---

### Submission Checklist

- Dataset created in US multi-region
- Orders table created and loaded with sample data
- Three SQL queries run with results documented
- Both dry\_run estimates recorded and compared
- Partitioned table created and partition pruning tested
- Clustered table created
- Looker Studio report created and URL recorded
- All 5 reflection questions answered
- All resources cleaned up

---

### Grading Rubric

| Task | Points |
|---|---|
| Dataset and table created with data loaded | 15 |
| SQL queries run with results documented | 20 |
| Dry\_run estimates compared | 15 |
| Partitioned and clustered tables created | 20 |
| Looker Studio report created | 15 |
| Reflection questions answered | 10 |
| Resources cleaned up | 5 |
| **Total** | **100** |

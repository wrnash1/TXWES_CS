# Lab 09 — Big Data Technologies: PySpark Analysis

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 100

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 1: Data Concepts and Environments

---

## Lab Overview

In this lab you will use PySpark to perform distributed data analysis on a simulated e-commerce dataset. You will practice the core Spark operations covered in Module 09: loading data, applying transformations, aggregating with Spark SQL, and working with DataFrames. You will also complete a written architecture design exercise comparing data lake vs. data warehouse solutions.

**Tools required:**

- Python 3.8 or later
- PySpark (`pip install pyspark`)
- pandas (`pip install pandas`)

If PySpark is unavailable in your environment, all tasks marked with a pandas alternative can be completed using pandas. Note in your submission which tool you used.

---

## Dataset

Create a file named `ecommerce_orders.csv` in your working directory.

```csv
order_id,customer_id,region,category,amount,order_date,is_returned
1001,C001,North,Electronics,299.99,2024-01-05,0
1002,C002,South,Clothing,45.00,2024-01-06,0
1003,C003,East,Electronics,799.99,2024-01-07,1
1004,C004,North,Home,125.50,2024-01-08,0
1005,C005,West,Clothing,89.99,2024-01-09,0
1006,C006,South,Electronics,549.00,2024-01-10,0
1007,C007,East,Home,210.00,2024-01-11,1
1008,C008,North,Food,32.50,2024-01-12,0
1009,C009,West,Electronics,1199.99,2024-01-13,0
1010,C010,South,Clothing,75.00,2024-01-14,0
1011,C001,North,Electronics,450.00,2024-02-01,0
1012,C002,South,Home,315.00,2024-02-02,0
1013,C003,East,Food,28.75,2024-02-03,0
1014,C004,North,Clothing,110.00,2024-02-04,0
1015,C005,West,Electronics,650.00,2024-02-05,1
1016,C006,South,Home,95.00,2024-02-06,0
1017,C007,East,Electronics,375.00,2024-02-07,0
1018,C008,North,Food,42.00,2024-02-08,0
1019,C009,West,Clothing,199.99,2024-02-09,0
1020,C010,South,Electronics,889.00,2024-02-10,0
```

---

## Part 1: Spark Session and Data Loading (15 points)

### Task 1.1 — Initialize Spark and load data

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, avg, count, round as spark_round

spark = SparkSession.builder \
    .appName("EcommerceAnalysis") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.read.csv("ecommerce_orders.csv", header=True, inferSchema=True)

print(f"Total records: {df.count()}")
print(f"Partitions:    {df.rdd.getNumPartitions()}")
df.printSchema()
df.show(5)
```

**Deliverable 1.1:** Record the number of partitions Spark created. Why does Spark partition data rather than loading it as a single block?

### Task 1.2 — Basic inspection

```python
# Null check
from pyspark.sql.functions import isnan, when

null_counts = df.select(
    [count(when(col(c).isNull(), c)).alias(c) for c in df.columns]
)
null_counts.show()

# Unique regions
print("Regions:", df.select("region").distinct().rdd.flatMap(lambda r: r).collect())

# Summary statistics
df.describe(["amount"]).show()
```

**Deliverable 1.2:** Are there any null values? How many distinct regions exist? What is the mean and max order amount?

---

## Part 2: DataFrame Transformations (25 points)

### Task 2.1 — Filter and select

```python
# High-value orders only
high_value = df.filter(col("amount") > 300) \
               .select("order_id", "region", "category", "amount")

print(f"High-value orders (>$300): {high_value.count()}")
high_value.show()
```

**Deliverable 2.1:** How many orders exceed $300? List their order IDs.

### Task 2.2 — Add a derived column

```python
# Add a revenue tier column
from pyspark.sql.functions import when

df_tiered = df.withColumn(
    "revenue_tier",
    when(col("amount") >= 500, "Premium")
    .when(col("amount") >= 100, "Standard")
    .otherwise("Basic")
)

df_tiered.groupBy("revenue_tier").count().orderBy("revenue_tier").show()
```

### Task 2.3 — Filter out returned orders

```python
df_clean = df_tiered.filter(col("is_returned") == 0)
print(f"Orders after removing returns: {df_clean.count()}")
print(f"Returns removed: {df.count() - df_clean.count()}")
```

**Deliverable 2.3:** How many returned orders were removed? What percentage of total orders were returns?

---

## Part 3: Aggregations and Spark SQL (30 points)

### Task 3.1 — Regional sales summary

```python
regional = df_clean.groupBy("region").agg(
    count("order_id").alias("order_count"),
    spark_round(spark_sum("amount"), 2).alias("total_revenue"),
    spark_round(avg("amount"), 2).alias("avg_order_value")
).orderBy("total_revenue", ascending=False)

regional.show()
```

**Deliverable 3.1:** Which region has the highest total revenue? Which has the highest average order value?

### Task 3.2 — Category breakdown

```python
category_stats = df_clean.groupBy("category").agg(
    count("order_id").alias("order_count"),
    spark_round(spark_sum("amount"), 2).alias("total_revenue"),
    spark_round(avg("amount"), 2).alias("avg_amount")
).orderBy("total_revenue", ascending=False)

category_stats.show()
```

### Task 3.3 — Spark SQL queries

```python
# Register the DataFrame as a temporary SQL view
df_clean.createOrReplaceTempView("orders")

# Monthly revenue by region
monthly = spark.sql("""
    SELECT
        SUBSTRING(order_date, 1, 7) AS month,
        region,
        ROUND(SUM(amount), 2)       AS monthly_revenue,
        COUNT(*)                    AS order_count
    FROM orders
    GROUP BY SUBSTRING(order_date, 1, 7), region
    ORDER BY month, monthly_revenue DESC
""")
monthly.show(20)
```

**Deliverable 3.3:** Compare January vs. February revenue for each region. Which region showed the largest month-over-month change?

### Task 3.4 — Top customers by spend

```python
top_customers = spark.sql("""
    SELECT
        customer_id,
        COUNT(*)             AS order_count,
        ROUND(SUM(amount), 2) AS total_spend,
        ROUND(AVG(amount), 2) AS avg_spend
    FROM orders
    GROUP BY customer_id
    ORDER BY total_spend DESC
    LIMIT 5
""")
top_customers.show()
```

---

## Part 4: Architecture Design Exercise (20 points)

Answer the following questions in your lab report. Each question requires 3–5 sentences.

### Question 4.1 — Technology Selection

A logistics company generates 500 GB of tracking data per day from GPS devices, delivery apps, and warehouse sensors. The data arrives in a mix of JSON (GPS), CSV (warehouse), and binary protocol buffers (mobile app). The analytics team needs to:

- Store all raw data indefinitely for regulatory compliance
- Run nightly batch reports on delivery performance
- Power real-time dashboards showing current delivery status

Should this company use a data lake, a data warehouse, or a data lakehouse? Justify your answer by referencing specific characteristics of each architecture. Explain which component handles each of the three requirements listed.

### Question 4.2 — Batch vs. Streaming Decision

The same logistics company wants to detect when a delivery driver has been stationary for more than 20 minutes — potentially indicating a vehicle breakdown — and automatically alert a dispatcher within 60 seconds of detection.

Should this use batch processing or streaming processing? Identify the specific streaming technology from Module 09 that would be most appropriate, and explain why batch processing would be unsuitable for this requirement.

### Question 4.3 — MapReduce vs. Spark

The company's data engineers have an existing Hadoop cluster running MapReduce jobs that refresh the nightly delivery performance reports. The jobs currently take 4 hours to run. A senior engineer proposes migrating to Apache Spark.

Explain in plain, non-technical language (as if speaking to a non-technical IT director) why Spark would be faster. What is the fundamental architectural difference that drives this performance improvement?

### Question 4.4 — HDFS Fault Tolerance

A DataNode in the HDFS cluster fails overnight. Explain step-by-step what happens to the data that was stored on that node. No data is lost — describe the mechanism that prevents data loss and how HDFS automatically recovers.

---

## Submission Checklist

Submit in a single ZIP file:

- [ ] Python script (`lab09.py` or `lab09.ipynb`)
- [ ] Lab report (PDF or Word) containing all deliverables and Question 4 answers

---

## Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Part 1 — Session and loading | 15 | Spark session created, schema printed, partition question answered |
| Part 2 — Transformations | 25 | Filter, derived column, and return removal all correct |
| Part 3 — Aggregations and SQL | 30 | All four aggregation tasks complete and correct; SQL queries run |
| Part 4 — Architecture design | 20 | Accurate, well-reasoned answers demonstrating conceptual understanding |
| **Total** | **100** | |

---

End of Lab 09

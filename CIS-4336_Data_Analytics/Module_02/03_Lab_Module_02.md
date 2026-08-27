# Lab 02 — Data Collection and Data Sources

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 1 and Domain 2

---

## Objectives

By completing this lab, you will be able to:

- Identify primary and secondary data sources in realistic scenarios
- Classify data collection methods and assess their quality risks
- Interpret a relational database schema including primary keys, foreign keys, and table relationships
- Distinguish OLTP from OLAP system design
- Trace data through an ETL pipeline and identify which stage applies to a given activity

---

## Prerequisites

- Module 02 Reading Guide completed
- Python 3.8 or later (or access to Google Colab)
- The `sqlite3` module (standard library — no installation required)
- The `pandas` library (`pip install pandas`)

---

## Part A — Data Source Identification (20 points)

### Part A Instructions

For each of the eight data sources described below, provide:

1. Primary or Secondary
2. Structure type: Structured, Semi-Structured, or Unstructured
3. One data quality risk specific to this source
4. One preprocessing step likely needed before analysis

### Data Sources

**Source A1:** A marketing team distributes a 12-question Qualtrics survey to 500 randomly selected customers asking about their satisfaction with recent purchases. The survey includes Likert-scale questions and one open-text comment field.

**Source A2:** A logistics company pulls daily shipment records from its ERP system using a scheduled SQL query. The output contains shipment ID, origin, destination, weight, carrier, and delivery timestamp for every shipment completed that day.

**Source A3:** A factory floor has 200 temperature sensors reporting readings every 30 seconds to a central server. Readings are stored as JSON objects with sensor ID, timestamp, and temperature value.

**Source A4:** A data analyst downloads the U.S. Census Bureau's 2020 American Community Survey public-use microdata files from the government's open data portal.

**Source A5:** A company purchases a third-party dataset of B2B firmographic data containing company name, industry, employee count, and revenue estimates for 500,000 U.S. businesses.

**Source A6:** A developer writes a Python script that calls the Twitter API and retrieves the text of 10,000 tweets mentioning the company's product name.

**Source A7:** An operations team extracts a CSV export from their customer support ticketing system containing ticket ID, category, priority, creation date, resolution date, and resolution notes.

**Source A8:** A security team captures and stores raw network packet data using a network monitoring tool. The files are stored in PCAP format.

### Part A Deliverable

Complete this table in your submission document.

| Source | Primary/Secondary | Structure Type | Quality Risk | Preprocessing Step |
|---|---|---|---|---|
| A1 | | | | |
| A2 | | | | |
| A3 | | | | |
| A4 | | | | |
| A5 | | | | |
| A6 | | | | |
| A7 | | | | |
| A8 | | | | |

**Grading:** 2.5 points per source. 20 points total.

---

## Part B — Schema Interpretation (25 points)

### Part B Instructions

Examine the relational database schema described below, then answer the five questions that follow.

### Schema Description

A retail company uses a database with the following four tables.

Table: CUSTOMERS

- CUSTOMER_ID (integer, primary key)
- FIRST_NAME (varchar)
- LAST_NAME (varchar)
- EMAIL (varchar, unique)
- REGION (varchar)
- LOYALTY_TIER (varchar)

Table: PRODUCTS

- PRODUCT_ID (integer, primary key)
- PRODUCT_NAME (varchar)
- CATEGORY (varchar)
- UNIT_PRICE (decimal)
- REORDER_LEVEL (integer)

Table: STORES

- STORE_ID (integer, primary key)
- STORE_NAME (varchar)
- CITY (varchar)
- STATE (varchar)

Table: ORDERS

- ORDER_ID (integer, primary key)
- CUSTOMER_ID (integer, foreign key referencing CUSTOMERS.CUSTOMER_ID)
- PRODUCT_ID (integer, foreign key referencing PRODUCTS.PRODUCT_ID)
- STORE_ID (integer, foreign key referencing STORES.STORE_ID)
- ORDER_DATE (date)
- QUANTITY (integer)
- TOTAL_AMOUNT (decimal)

### Part B Questions

**Question B1 (5 points):** Draw or describe a diagram of the relationships between these four tables. Identify which table is the fact table and which three tables are dimension tables. What schema pattern does this represent — star or snowflake? Justify your answer.

**Question B2 (5 points):** A developer tries to insert a new ORDERS record with CUSTOMER_ID = 9999, but CUSTOMER_ID 9999 does not exist in the CUSTOMERS table. What constraint is violated? What is this type of constraint called, and why does the database enforce it?

**Question B3 (5 points):** An analyst wants to find the total revenue per region for all orders placed in 2024. List the tables that need to be joined to answer this question, state which columns to join on, and explain why the ORDER_DATE filter needs to be applied after the join.

**Question B4 (5 points):** Is this database schema better suited for an OLTP system or an OLAP system? Justify your answer by describing two specific characteristics of the schema that support your classification.

**Question B5 (5 points):** The PRODUCTS table has a REORDER_LEVEL column that stores how many units must be in inventory before a restock order is triggered. Should REORDER_LEVEL be stored in this same table or separated into its own table? Explain your answer using the concept of normalization.

### Part B Deliverable

Write your answers to B1 through B5 in your submission document. Each answer should be three to five sentences with clear reasoning.

---

## Part C — ETL Pipeline Exercise (25 points)

### Part C Instructions

The following scenario describes fifteen data activities performed during a quarterly analytics project. For each activity, identify which ETL stage it belongs to: Extract, Transform, or Load. Then answer the two analysis questions at the end.

### Activities

1. A Python script queries the company's SQL Server OLTP database and retrieves all order records from the past 90 days.
2. A data engineer writes logic to replace all NULL values in the REGION column with "Unknown."
3. The cleaned dataset is written to the company's Snowflake data warehouse using a bulk COPY command.
4. An analyst pulls a JSON export from the company's CRM system via its REST API.
5. A script parses the JSON response and converts each record to a flat row with consistent column names.
6. A deduplication step removes 340 order records that appear twice due to a reprocessing error.
7. The deduplicated records are appended to the ORDERS_FACT table in the data warehouse.
8. A developer downloads a CSV of product catalog updates from an external supplier's SFTP server.
9. The product catalog CSV is parsed, and the UNIT_PRICE column is converted from string to decimal type.
10. A new column called REVENUE_CATEGORY is computed by applying a business rule: orders over $500 are "High Value," orders $100–$500 are "Standard," orders under $100 are "Low Value."
11. The enriched product records are merged into the PRODUCTS_DIM dimension table in the warehouse.
12. A data engineer queries the company's web analytics platform API to retrieve weekly session counts.
13. Session counts are joined to the order data using the DATE column to create a combined marketing dataset.
14. The combined marketing dataset is written to a separate data mart used by the marketing team.
15. A freshness timestamp is updated in a metadata tracking table to record when the pipeline last completed successfully.

### Part C Analysis Questions

**Question C1 (5 points):** Three of the fifteen activities above involve applying business logic or computing derived values. Identify those three activities by number and explain why applying business logic is considered part of the Transform stage rather than the Load stage.

**Question C2 (5 points):** A colleague proposes skipping the Transform stage entirely and loading raw data from all sources directly into the data warehouse. What are two specific risks of this approach? How does ELT (Extract, Load, Transform) address these risks differently than simply skipping transformation?

### Part C Deliverable

Complete the activity classification table and write your answers to C1 and C2 in your submission document.

| Activity | ETL Stage |
|---|---|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |
| 10 | |
| 11 | |
| 12 | |
| 13 | |
| 14 | |
| 15 | |

**Grading:** 1 point per activity classification (15 points), 5 points each for C1 and C2.

---

## Part D — Python Database Simulation (30 points)

### Part D Instructions

Run the following Python code block, which creates an in-memory SQLite database, populates it with sample data, and runs several queries. Answer the four questions based on your output.

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.executescript("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    region      TEXT,
    loyalty_tier TEXT
);

CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    order_date  TEXT,
    total_amount REAL
);

INSERT INTO customers VALUES (1, 'Alice',   'North', 'Gold');
INSERT INTO customers VALUES (2, 'Bob',     'South', 'Silver');
INSERT INTO customers VALUES (3, 'Carol',   'North', 'Bronze');
INSERT INTO customers VALUES (4, 'David',   'East',  'Gold');
INSERT INTO customers VALUES (5, 'Eva',     'West',  'Silver');

INSERT INTO orders VALUES (101, 1, '2024-01-15', 450.00);
INSERT INTO orders VALUES (102, 2, '2024-01-20', 125.50);
INSERT INTO orders VALUES (103, 1, '2024-02-01', 310.75);
INSERT INTO orders VALUES (104, 3, '2024-02-14', 88.00);
INSERT INTO orders VALUES (105, 4, '2024-03-05', 670.20);
INSERT INTO orders VALUES (106, 5, '2024-03-18', 200.00);
INSERT INTO orders VALUES (107, 2, '2024-04-02', 95.00);
INSERT INTO orders VALUES (108, 1, '2024-04-10', 520.00);
""")

print("--- Query 1: Total revenue per region ---")
q1 = pd.read_sql_query("""
    SELECT c.region, SUM(o.total_amount) AS total_revenue
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.region
    ORDER BY total_revenue DESC
""", conn)
print(q1)

print("\n--- Query 2: Customers with no orders ---")
q2 = pd.read_sql_query("""
    SELECT c.customer_id, c.first_name
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id
    WHERE o.order_id IS NULL
""", conn)
print(q2)

print("\n--- Query 3: Average order value per loyalty tier ---")
q3 = pd.read_sql_query("""
    SELECT c.loyalty_tier,
           COUNT(o.order_id) AS order_count,
           ROUND(AVG(o.total_amount), 2) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.loyalty_tier
    ORDER BY avg_order_value DESC
""", conn)
print(q3)

conn.close()
```

### Part D Questions

**Question D1 (8 points):** In Query 1, the JOIN connects ORDERS to CUSTOMERS using the CUSTOMER_ID column. Explain what type of join this is, why it is necessary, and what the GROUP BY clause is doing. In your explanation, identify whether this query would be appropriate to run against an OLTP production database or an OLAP warehouse, and why.

**Question D2 (7 points):** Query 2 uses a LEFT JOIN and filters for `o.order_id IS NULL`. Explain in plain language what this query returns and why the LEFT JOIN is necessary rather than an INNER JOIN. Which customer(s) does your output show, and what does that tell you about the data?

**Question D3 (8 points):** Modify Query 3 to add a HAVING clause that returns only loyalty tiers where the average order value exceeds $300. Write out the modified SQL, run it, and report your output. Explain the difference between WHERE and HAVING in the context of this query.

**Question D4 (7 points):** The ORDERS table has a foreign key on CUSTOMER_ID referencing CUSTOMERS. If you tried to insert an order with CUSTOMER_ID = 99 (which does not exist in CUSTOMERS), SQLite may or may not enforce this constraint by default. Explain why foreign key enforcement matters for data quality, and describe one scenario where an unenforced foreign key could cause an incorrect analytical result.

### Part D Deliverable

Submit a document containing:

1. A screenshot or copy-paste of your Python output for all three queries
2. The modified SQL for D3 and its output
3. Written answers to D1 through D4

**Grading:** Points per question as listed. 30 points total.

---

## Submission Instructions

Compile all deliverables into a single PDF or Word document. Name your file: `Lab02_LastName_FirstName.pdf`.

Submit to the Canvas assignment portal before the stated deadline.

---

## Grading Rubric Summary

| Part | Description | Points |
|---|---|---|
| A | Data Source Identification | 20 |
| B | Schema Interpretation | 25 |
| C | ETL Pipeline Exercise | 25 |
| D | Python Database Simulation | 30 |
| **Total** | | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Schema Extension and Integrity Testing

Extend the SQLite database from Part D to test referential integrity and schema design decisions.

1. Add a `PRODUCTS` table with columns `product_id` (INTEGER PRIMARY KEY), `product_name` (TEXT), `category` (TEXT), and `unit_price` (REAL). Add a `product_id` foreign key column to the `orders` table (you may rebuild the table or add the column). Enable foreign key enforcement in SQLite with `PRAGMA foreign_keys = ON;`.
2. Insert five product rows and update the existing order rows to reference valid product IDs. Then attempt to insert one order row with a non-existent `product_id` and observe whether SQLite raises an error. Document the result and explain what it means for data quality.
3. Write a SQL query that returns total revenue, average order value, and order count grouped by both `region` and `product category`. Load the result into a pandas DataFrame and print it.

```python
import sqlite3, pandas as pd

conn = sqlite3.connect(":memory:")
conn.execute("PRAGMA foreign_keys = ON")
cur = conn.cursor()

cur.executescript("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT, region TEXT, loyalty_tier TEXT
);
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT, category TEXT, unit_price REAL
);
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    product_id  INTEGER REFERENCES products(product_id),
    order_date TEXT, total_amount REAL
);
INSERT INTO customers VALUES (1,'Alice','North','Gold'),(2,'Bob','South','Silver'),
    (3,'Carol','North','Bronze'),(4,'David','East','Gold'),(5,'Eva','West','Silver');
INSERT INTO products VALUES (10,'Laptop','Electronics',999.99),(11,'Headphones','Electronics',79.99),
    (12,'Desk Chair','Furniture',349.00),(13,'Notebook','Office',4.99),(14,'Monitor','Electronics',399.00);
INSERT INTO orders VALUES (101,1,10,'2024-01-15',999.99),(102,2,11,'2024-01-20',79.99),
    (103,1,12,'2024-02-01',349.00),(104,3,13,'2024-02-14',4.99),
    (105,4,14,'2024-03-05',399.00),(106,5,10,'2024-03-18',999.99);
""")

df = pd.read_sql_query("""
    SELECT c.region, p.category,
           COUNT(o.order_id) AS order_count,
           ROUND(SUM(o.total_amount),2) AS total_revenue,
           ROUND(AVG(o.total_amount),2) AS avg_order_value
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN products p ON o.product_id = p.product_id
    GROUP BY c.region, p.category
    ORDER BY total_revenue DESC
""", conn)
print(df)
```

### Challenge 2: Mini ETL Pipeline in Python

Simulate a three-stage ETL pipeline that reads raw data, applies transformations, and loads results into a clean analytical table.

1. Create a raw "source" DataFrame with at least 10 rows simulating a CSV export from an OLTP system. Include intentional quality issues: two duplicate rows, one row with a NULL `region`, and one row with a negative `total_amount`. Print the raw DataFrame and document each issue found.
2. Write an explicit Transform stage as a Python function `transform(df)` that: removes duplicate rows, fills NULL `region` values with `"Unknown"`, filters out rows where `total_amount` is negative, and adds a `revenue_category` column using `pd.cut()` with bins for Low (<$100), Standard ($100–$500), and High (>$500). Return the cleaned DataFrame.
3. Write a Load stage function `load(df, conn)` that inserts each cleaned row into a SQLite `orders_clean` table using `df.to_sql()`. Verify the load by querying the table row count and printing the final analytical summary grouped by `revenue_category`.

### Reflection Questions

1. In Challenge 1, when you enabled `PRAGMA foreign_keys = ON` and attempted to insert an order with a non-existent `product_id`, what happened? What would the consequence have been for analytical accuracy if the insert had silently succeeded?
2. In Challenge 2, your `transform()` function applied four data quality rules. For each rule, name the data quality dimension it addresses (completeness, accuracy, uniqueness, or validity) and explain your reasoning.

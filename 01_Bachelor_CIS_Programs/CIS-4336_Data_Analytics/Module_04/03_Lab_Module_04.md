# Lab 04 — Relational Databases and SQL for Analytics

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 2 and Domain 3

---

## Objectives

By completing this lab, you will be able to:

- Write GROUP BY queries to aggregate sales data by region, product category, and time period
- Apply HAVING to filter aggregated results
- Write INNER JOIN and LEFT JOIN queries across multiple tables
- Use window functions to compute running totals, ranks, and moving averages
- Interpret and validate query results against business requirements

---

## Prerequisites

- Module 04 Reading Guide completed
- Python 3.8 or later (or Google Colab)
- `sqlite3` (standard library) and `pandas` installed

---

## Dataset Setup

Run this code block first. It creates the in-memory database used throughout the lab.

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.executescript("""
CREATE TABLE regions (
    region_id   INTEGER PRIMARY KEY,
    region_name TEXT NOT NULL
);

CREATE TABLE customers (
    customer_id  INTEGER PRIMARY KEY,
    first_name   TEXT,
    last_name    TEXT,
    email        TEXT UNIQUE,
    region_id    INTEGER REFERENCES regions(region_id),
    loyalty_tier TEXT
);

CREATE TABLE products (
    product_id   INTEGER PRIMARY KEY,
    product_name TEXT,
    category     TEXT,
    unit_price   REAL
);

CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    product_id  INTEGER REFERENCES products(product_id),
    order_date  TEXT,
    quantity    INTEGER,
    total_amount REAL
);

INSERT INTO regions VALUES (1,'North'),(2,'South'),(3,'East'),(4,'West');

INSERT INTO customers VALUES
 (1,'Alice','Adams','alice@ex.com',1,'Gold'),
 (2,'Bob','Baker','bob@ex.com',2,'Silver'),
 (3,'Carol','Clark','carol@ex.com',1,'Bronze'),
 (4,'David','Davis','david@ex.com',3,'Gold'),
 (5,'Eva','Evans','eva@ex.com',4,'Silver'),
 (6,'Frank','Ford','frank@ex.com',2,'Bronze'),
 (7,'Grace','Green','grace@ex.com',3,'Gold'),
 (8,'Hank','Hill','hank@ex.com',1,'Bronze'),
 (9,'Irene','Ingram','irene@ex.com',4,'Silver'),
 (10,'Jack','Jones','jack@ex.com',2,'Gold');

INSERT INTO products VALUES
 (1,'Laptop','Electronics',999.99),
 (2,'Desk Chair','Furniture',249.99),
 (3,'Notebook','Stationery',4.99),
 (4,'Monitor','Electronics',399.99),
 (5,'Standing Desk','Furniture',549.99),
 (6,'Pen Set','Stationery',12.99),
 (7,'Webcam','Electronics',79.99),
 (8,'Bookcase','Furniture',179.99);

INSERT INTO orders VALUES
 (1001,1,1,'2024-01-10',1,999.99),
 (1002,2,3,'2024-01-15',5,24.95),
 (1003,3,2,'2024-01-22',1,249.99),
 (1004,4,4,'2024-02-05',2,799.98),
 (1005,5,5,'2024-02-14',1,549.99),
 (1006,1,7,'2024-02-20',2,159.98),
 (1007,6,6,'2024-03-01',3,38.97),
 (1008,7,1,'2024-03-10',1,999.99),
 (1009,8,3,'2024-03-18',10,49.90),
 (1010,2,4,'2024-04-02',1,399.99),
 (1011,9,8,'2024-04-15',1,179.99),
 (1012,10,2,'2024-05-01',2,499.98),
 (1013,3,5,'2024-05-12',1,549.99),
 (1014,4,6,'2024-06-03',5,64.95),
 (1015,7,7,'2024-06-18',1,79.99);
""")

print("Database ready.")
```

---

## Part A — GROUP BY Sales Aggregation (25 points)

### Part A Instructions

Write and run four SQL queries using GROUP BY. For each query, show the output using `pd.read_sql_query()`.

**Query A1 (6 points):** Write a query that returns the total revenue, order count, and average order value for each region. Join the ORDERS table to the REGIONS table so the region name appears (not the region ID). Order by total revenue descending.

Expected columns: region_name, order_count, total_revenue, avg_order_value

**Query A2 (6 points):** Write a query that returns the total revenue and order count per product category. Join ORDERS to PRODUCTS. Order by total_revenue descending.

Expected columns: category, order_count, total_revenue

**Query A3 (6 points):** Write a query that returns monthly revenue totals. Extract the year and month from order_date. Order chronologically.

Expected columns: order_year, order_month, order_count, monthly_revenue

**Query A4 (7 points):** Write a query that shows total revenue and order count per customer loyalty tier. Join ORDERS to CUSTOMERS. Also compute the average order value per tier. Order by total_revenue descending.

Expected columns: loyalty_tier, customer_count (distinct customers), order_count, total_revenue, avg_order_value

### Part A Deliverable

Four SQL queries with output. For A4, also write two to three sentences explaining what the results reveal about the relative value of different loyalty tiers.

---

## Part B — HAVING Filter Queries (20 points)

### Part B Instructions

Write three SQL queries that use HAVING to filter aggregate results.

**Query B1 (7 points):** Write a query that returns only the product categories where total revenue exceeds $1,000. Show category name, total revenue, and order count.

**Query B2 (7 points):** Write a query that identifies customers who have placed more than one order. Show customer ID, first name, order count, and total amount spent. Order by total amount descending.

**Query B3 (6 points):** Modify Query A3 (monthly revenue) to return only months where monthly revenue exceeded $800. Explain in one sentence why you must use HAVING rather than WHERE for this filter.

### Part B Deliverable

Three SQL queries with output. Written explanation for B3.

---

## Part C — JOIN Queries (25 points)

### Part C Instructions

Write four JOIN queries to answer the following analytical questions.

**Query C1 — INNER JOIN (6 points):** List all orders with the customer's full name, the product name, the product category, and the total amount. Order by total amount descending.

Expected columns: order_id, customer_full_name, product_name, category, total_amount

**Query C2 — LEFT JOIN (7 points):** List all customers, including those who have never placed an order. Show customer ID, full name, loyalty tier, region name, and order count (0 for customers with no orders).

Expected columns: customer_id, full_name, loyalty_tier, region_name, order_count

**Query C3 — Multi-table JOIN (6 points):** Write a query joining all four tables (CUSTOMERS, ORDERS, PRODUCTS, REGIONS) to produce a complete order detail report. Include region name, customer full name, product name, category, order date, quantity, unit price, and total amount.

**Query C4 — Anti-join (6 points):** Using a LEFT JOIN and a WHERE IS NULL filter, find all products that have never been ordered. Show product ID, product name, and category.

### Part C Deliverable

Four SQL queries with output. For C2, explain in two sentences what LEFT JOIN accomplishes that INNER JOIN would not.

---

## Part D — Window Functions (30 points)

### Part D Instructions

Write four window function queries.

**Query D1 — Running Total (8 points):** Write a query that shows each order with a running total of revenue ordered by date. Include order_id, order_date, total_amount, and a cumulative_revenue column that accumulates all revenue up to and including the current row's date.

```sql
-- Template structure:
SELECT order_id,
       order_date,
       total_amount,
       SUM(total_amount) OVER (
           ORDER BY order_date
       ) AS cumulative_revenue
FROM orders
ORDER BY order_date;
```

Run this query and report the output. Then answer: what does the cumulative_revenue value for the last row represent?

**Query D2 — Rank by Spend (7 points):** Write a query that ranks customers by their total spending. First aggregate each customer's total spend using a CTE, then apply RANK() OVER to rank them highest to lowest. Show customer_id, first_name, total_spent, and spend_rank.

**Query D3 — Regional Rank (8 points):** Write a query that ranks each order within its region by total_amount, highest first. Use PARTITION BY region_id (or region_name via join) and ROW_NUMBER. Show region_name, order_id, customer_id, total_amount, and rank_within_region. Filter the result to show only the top 2 orders per region.

**Query D4 — Month-over-Month Change (7 points):** Using the monthly revenue CTE from Query A3, add a LAG window function to compute the prior month's revenue. Then compute the month-over-month change as an additional column. Show order_year, order_month, monthly_revenue, prior_month_revenue, and revenue_change.

```sql
-- Template:
WITH monthly AS (
    SELECT strftime('%Y', order_date) AS order_year,
           strftime('%m', order_date) AS order_month,
           SUM(total_amount) AS monthly_revenue
    FROM orders
    GROUP BY order_year, order_month
)
SELECT order_year,
       order_month,
       monthly_revenue,
       LAG(monthly_revenue, 1) OVER (ORDER BY order_year, order_month) AS prior_month_revenue,
       monthly_revenue - LAG(monthly_revenue, 1) OVER (
           ORDER BY order_year, order_month
       ) AS revenue_change
FROM monthly;
```

Run this query and answer: in which month was the largest month-over-month increase?

### Part D Deliverable

Four SQL queries with output. Written answers for D1 and D4 analysis questions.

---

## Submission Instructions

Compile all queries, outputs, and written answers into a single PDF or Word document. Name your file: `Lab04_LastName_FirstName.pdf`. Submit to Canvas before the stated deadline.

---

## Grading Rubric Summary

| Part | Description | Points |
|---|---|---|
| A | GROUP BY Aggregation | 25 |
| B | HAVING Filter Queries | 20 |
| C | JOIN Queries | 25 |
| D | Window Functions | 30 |
| **Total** | | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Customer Cohort Analysis with Window Functions

Build a month-over-month customer cohort analysis using the lab database.

1. Write a CTE called `customer_monthly` that aggregates each customer's total spend and order count per calendar month (year + month extracted from `order_date`). Include `customer_id` and join to `customers` to include `first_name` and `loyalty_tier`.
2. Using a second CTE on top of `customer_monthly`, add three window function columns: `cumulative_spend` (running total of spend per customer ordered by month), `monthly_rank` (rank of spend within each month across all customers, highest first), and `spend_vs_prev_month` (difference from the prior month's spend for the same customer using `LAG`).
3. In the outer query, filter to return only rows where `monthly_rank <= 3` (top 3 spenders each month). Print the results and write two sentences identifying which customer appears most frequently in the top 3 and what this suggests about their purchasing behavior.

```python
query = """
WITH customer_monthly AS (
    SELECT c.customer_id, c.first_name, c.loyalty_tier,
           strftime('%Y', o.order_date) AS yr,
           strftime('%m', o.order_date) AS mo,
           SUM(o.total_amount) AS monthly_spend,
           COUNT(o.order_id) AS order_count
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, yr, mo
),
ranked AS (
    SELECT *,
           SUM(monthly_spend) OVER (
               PARTITION BY customer_id ORDER BY yr, mo
           ) AS cumulative_spend,
           RANK() OVER (
               PARTITION BY yr, mo ORDER BY monthly_spend DESC
           ) AS monthly_rank,
           monthly_spend - LAG(monthly_spend, 1) OVER (
               PARTITION BY customer_id ORDER BY yr, mo
           ) AS spend_vs_prev_month
    FROM customer_monthly
)
SELECT * FROM ranked WHERE monthly_rank <= 3 ORDER BY yr, mo, monthly_rank;
"""
df_cohort = pd.read_sql_query(query, conn)
print(df_cohort)
```

### Challenge 2: Product Performance Dashboard Query

Write a single analytical SQL query that produces a complete product performance summary suitable for an executive dashboard.

1. Using a CTE, compute for each product: total units sold, total revenue, average order value, number of distinct customers who purchased it, and its revenue rank among all products.
2. In the outer query, add a `performance_tier` classification using a CASE statement: products with revenue rank 1–3 are `'Top'`, ranks 4–6 are `'Mid'`, all others are `'Tail'`. Include the product name and category.
3. Load the result into a pandas DataFrame, then use `groupby("performance_tier")["total_revenue"].sum()` to show how much total revenue each performance tier contributes. Print the tier summary and write one sentence interpreting the revenue concentration.

```python
query_perf = """
WITH product_stats AS (
    SELECT p.product_id, p.product_name, p.category,
           SUM(o.quantity) AS units_sold,
           SUM(o.total_amount) AS total_revenue,
           AVG(o.total_amount) AS avg_order_value,
           COUNT(DISTINCT o.customer_id) AS distinct_customers,
           RANK() OVER (ORDER BY SUM(o.total_amount) DESC) AS revenue_rank
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.product_id, p.product_name, p.category
)
SELECT *,
       CASE
           WHEN revenue_rank <= 3 THEN 'Top'
           WHEN revenue_rank <= 6 THEN 'Mid'
           ELSE 'Tail'
       END AS performance_tier
FROM product_stats
ORDER BY revenue_rank;
"""
df_perf = pd.read_sql_query(query_perf, conn)
print(df_perf)
print(df_perf.groupby("performance_tier")["total_revenue"].sum())
```

### Reflection Questions

1. In Challenge 1, the `spend_vs_prev_month` column returns NULL for a customer's first month. How would you handle this NULL in a dashboard context — replace it with zero, leave it as NULL, or use a different approach? Justify your choice.
2. In Challenge 2, you used a CASE statement to classify products into performance tiers. What advantage does this derived classification provide over simply sorting by `revenue_rank` in downstream reporting?

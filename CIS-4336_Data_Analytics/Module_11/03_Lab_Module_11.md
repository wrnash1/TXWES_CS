# Lab 11 — SQL for Data Analytics

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 100

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 3: Data Analysis

---

## Lab Overview

In this lab you will write analytical SQL queries using SQLite — aggregations, GROUP BY, HAVING, window functions (ROW_NUMBER, RANK, LAG), CTEs, and subqueries. All queries run against a retail orders database you will build in the first task.

**Tools required:**

- Python 3.8 or later with the built-in `sqlite3` module (no installation needed)
- Optional: DB Browser for SQLite (free GUI at sqlitebrowser.org) for visual query testing

---

## Part 1: Database Setup (10 points)

### Task 1.1 — Create the database and load data

Save and run the following Python script to create your SQLite database.

```python
import sqlite3

conn = sqlite3.connect('retail_analytics.db')
cur  = conn.cursor()

# Create tables
cur.executescript("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;

CREATE TABLE customers (
    customer_id   TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    city          TEXT,
    state         TEXT,
    tier          TEXT  -- Bronze, Silver, Gold
);

CREATE TABLE products (
    product_id   TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category     TEXT,
    unit_price   REAL
);

CREATE TABLE orders (
    order_id    INTEGER PRIMARY KEY,
    customer_id TEXT,
    product_id  TEXT,
    order_date  TEXT,
    region      TEXT,
    sales_rep   TEXT,
    quantity    INTEGER,
    amount      REAL
);
""")

# Insert customers
customers = [
    ('C001','Acme Corp','Dallas','TX','Gold'),
    ('C002','BrightTech','Austin','TX','Silver'),
    ('C003','CloudBase','Houston','TX','Gold'),
    ('C004','DataFlow Inc','Denver','CO','Bronze'),
    ('C005','EdgeSystems','Phoenix','AZ','Silver'),
    ('C006','FastTrack LLC','Seattle','WA','Gold'),
    ('C007','GlobalMart','Chicago','IL','Bronze'),
    ('C008','HorizonCo','Miami','FL','Silver'),
]
cur.executemany("INSERT INTO customers VALUES (?,?,?,?,?)", customers)

# Insert products
products = [
    ('P001','Laptop Pro','Electronics',1299.99),
    ('P002','Wireless Mouse','Electronics',39.99),
    ('P003','Office Chair','Furniture',449.99),
    ('P004','Standing Desk','Furniture',799.99),
    ('P005','Notebook Pack','Supplies',12.99),
    ('P006','Monitor 27in','Electronics',549.99),
]
cur.executemany("INSERT INTO products VALUES (?,?,?,?)", products)

# Insert orders (30 rows across 2024)
orders = [
    (1,'C001','P001','2024-01-05','South','Alice',1,1299.99),
    (2,'C002','P002','2024-01-08','South','Bob',3,119.97),
    (3,'C003','P003','2024-01-12','South','Alice',2,899.98),
    (4,'C004','P004','2024-01-15','West','Carol',1,799.99),
    (5,'C005','P006','2024-01-20','West','Carol',1,549.99),
    (6,'C006','P001','2024-01-22','North','Dave',2,2599.98),
    (7,'C007','P005','2024-01-28','North','Dave',10,129.90),
    (8,'C008','P003','2024-02-03','East','Eve',1,449.99),
    (9,'C001','P006','2024-02-07','South','Alice',1,549.99),
    (10,'C002','P004','2024-02-10','South','Bob',1,799.99),
    (11,'C003','P001','2024-02-14','South','Alice',1,1299.99),
    (12,'C004','P002','2024-02-18','West','Carol',5,199.95),
    (13,'C005','P003','2024-02-22','West','Carol',1,449.99),
    (14,'C006','P005','2024-02-25','North','Dave',20,259.80),
    (15,'C007','P006','2024-03-01','North','Dave',1,549.99),
    (16,'C008','P001','2024-03-05','East','Eve',1,1299.99),
    (17,'C001','P004','2024-03-10','South','Alice',1,799.99),
    (18,'C002','P006','2024-03-15','South','Bob',2,1099.98),
    (19,'C003','P002','2024-03-18','South','Alice',4,159.96),
    (20,'C004','P001','2024-03-22','West','Carol',1,1299.99),
    (21,'C005','P004','2024-04-01','West','Carol',1,799.99),
    (22,'C006','P003','2024-04-05','North','Dave',2,899.98),
    (23,'C007','P001','2024-04-10','North','Dave',1,1299.99),
    (24,'C008','P006','2024-04-12','East','Eve',1,549.99),
    (25,'C001','P002','2024-04-18','South','Alice',6,239.94),
    (26,'C002','P003','2024-04-22','South','Bob',1,449.99),
    (27,'C003','P005','2024-04-25','South','Alice',15,194.85),
    (28,'C004','P006','2024-05-02','West','Carol',1,549.99),
    (29,'C005','P001','2024-05-08','West','Carol',1,1299.99),
    (30,'C006','P004','2024-05-12','North','Dave',1,799.99),
]
cur.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?,?,?)", orders)

conn.commit()
conn.close()
print("Database created: retail_analytics.db")
print("Tables: customers, products, orders")
```

**Deliverable 1.1:** Run the script and confirm no errors. Query and paste the output of: `SELECT COUNT(*) FROM orders;`

---

## Part 2: Aggregations and GROUP BY (20 points)

Connect to the database and run each query. Paste results in your lab report.

```python
import sqlite3
conn = sqlite3.connect('retail_analytics.db')
cur  = conn.cursor()

def run(label, sql):
    print(f"\n--- {label} ---")
    cur.execute(sql)
    cols = [d[0] for d in cur.description]
    print(" | ".join(cols))
    for row in cur.fetchall():
        print(" | ".join(str(v) for v in row))
```

### Task 2.1 — Revenue by region

```python
run("Revenue by Region", """
    SELECT
        region,
        COUNT(*)              AS order_count,
        ROUND(SUM(amount),2)  AS total_revenue,
        ROUND(AVG(amount),2)  AS avg_order
    FROM orders
    GROUP BY region
    ORDER BY total_revenue DESC
""")
```

### Task 2.2 — Monthly revenue (all months)

```python
run("Monthly Revenue", """
    SELECT
        SUBSTR(order_date, 1, 7)  AS month,
        COUNT(*)                  AS order_count,
        ROUND(SUM(amount), 2)     AS monthly_revenue
    FROM orders
    GROUP BY SUBSTR(order_date, 1, 7)
    ORDER BY month
""")
```

### Task 2.3 — Sales reps with revenue over $2,000 (HAVING)

```python
run("High-Revenue Sales Reps (HAVING)", """
    SELECT
        sales_rep,
        COUNT(*)              AS order_count,
        ROUND(SUM(amount),2)  AS total_revenue
    FROM orders
    GROUP BY sales_rep
    HAVING SUM(amount) > 2000
    ORDER BY total_revenue DESC
""")
```

**Deliverable 2:** Paste the output of all three queries. Explain in one sentence why HAVING is required in Task 2.3 instead of WHERE.

---

## Part 3: Window Functions (30 points)

### Task 3.1 — ROW_NUMBER: top 2 orders per region

```python
run("Top 2 Orders per Region (ROW_NUMBER)", """
    SELECT order_id, region, sales_rep, amount, rn
    FROM (
        SELECT
            order_id,
            region,
            sales_rep,
            amount,
            ROW_NUMBER() OVER (
                PARTITION BY region
                ORDER BY amount DESC
            ) AS rn
        FROM orders
    ) ranked
    WHERE rn <= 2
    ORDER BY region, amount DESC
""")
```

### Task 3.2 — RANK vs DENSE_RANK on tied amounts

```python
# Insert a tie row temporarily
cur.execute("""
    INSERT INTO orders VALUES
    (31,'C008','P001','2024-05-15','East','Eve',1,1299.99)
""")
conn.commit()

run("RANK vs DENSE_RANK (with tie)", """
    SELECT
        order_id,
        region,
        amount,
        RANK()       OVER (ORDER BY amount DESC) AS rnk,
        DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rnk
    FROM orders
    ORDER BY amount DESC
    LIMIT 8
""")
```

**Deliverable 3.2:** Find the rows where amount = 1299.99. What rank does each function assign to the row immediately following the tied rows? Explain the difference.

### Task 3.3 — LAG: month-over-month revenue change

```python
run("Month-over-Month Revenue Change (LAG)", """
    WITH monthly AS (
        SELECT
            SUBSTR(order_date, 1, 7) AS month,
            ROUND(SUM(amount), 2)    AS monthly_revenue
        FROM orders
        GROUP BY SUBSTR(order_date, 1, 7)
    )
    SELECT
        month,
        monthly_revenue,
        LAG(monthly_revenue, 1, 0) OVER (ORDER BY month) AS prev_month,
        ROUND(monthly_revenue
              - LAG(monthly_revenue, 1, 0) OVER (ORDER BY month), 2) AS change
    FROM monthly
    ORDER BY month
""")
```

**Deliverable 3.3:** Which month had the largest positive change vs. the prior month?

### Task 3.4 — Running total

```python
run("Cumulative Revenue by Order Date", """
    SELECT
        order_date,
        ROUND(SUM(amount), 2)   AS daily_revenue,
        ROUND(SUM(SUM(amount)) OVER (
            ORDER BY order_date
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ), 2)                   AS running_total
    FROM orders
    GROUP BY order_date
    ORDER BY order_date
""")
```

---

## Part 4: CTEs (20 points)

### Task 4.1 — Top customer per region using CTE

```python
run("Top Customer per Region (CTE + RANK)", """
    WITH customer_spend AS (
        SELECT
            o.customer_id,
            c.customer_name,
            o.region,
            ROUND(SUM(o.amount), 2) AS total_spend
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        GROUP BY o.customer_id, c.customer_name, o.region
    ),
    ranked AS (
        SELECT
            customer_id,
            customer_name,
            region,
            total_spend,
            RANK() OVER (PARTITION BY region ORDER BY total_spend DESC) AS rnk
        FROM customer_spend
    )
    SELECT region, customer_name, total_spend
    FROM ranked
    WHERE rnk = 1
    ORDER BY total_spend DESC
""")
```

### Task 4.2 — Product category revenue with CTE

```python
run("Category Revenue Share (CTE)", """
    WITH category_totals AS (
        SELECT
            p.category,
            ROUND(SUM(o.amount), 2) AS category_revenue
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
        GROUP BY p.category
    ),
    grand_total AS (
        SELECT ROUND(SUM(amount), 2) AS total FROM orders
    )
    SELECT
        ct.category,
        ct.category_revenue,
        ROUND(ct.category_revenue * 100.0 / gt.total, 1) AS pct_of_total
    FROM category_totals ct, grand_total gt
    ORDER BY ct.category_revenue DESC
""")
```

**Deliverable 4:** Paste the output of both CTE queries. Which product category contributes the most revenue? Which customer has the highest total spend in the South region?

---

## Part 5: Subqueries (10 points)

### Task 5.1 — Orders above the overall average

```python
run("Orders Above Overall Average (Subquery in WHERE)", """
    SELECT order_id, customer_id, region, amount
    FROM orders
    WHERE amount > (SELECT AVG(amount) FROM orders)
    ORDER BY amount DESC
""")
```

### Task 5.2 — Customers who spent above their own average order value

```python
run("Above-Average Orders per Customer (Correlated Subquery)", """
    SELECT o.order_id, o.customer_id, o.amount
    FROM orders o
    WHERE o.amount > (
        SELECT AVG(o2.amount)
        FROM orders o2
        WHERE o2.customer_id = o.customer_id
    )
    ORDER BY o.customer_id, o.amount DESC
""")

conn.close()
```

**Deliverable 5:** Paste results. Explain the difference between a regular subquery (Task 5.1) and a correlated subquery (Task 5.2) in terms of how many times each executes.

---

## Part 6: Write Your Own Query (10 points)

Write one original SQL query that uses at least THREE of the following features:

- GROUP BY with HAVING
- A window function (ROW_NUMBER, RANK, DENSE_RANK, LAG, or LEAD)
- A CTE
- A subquery

The query must answer a meaningful business question about the retail_analytics dataset. State the business question in plain English, then write and run the query.

**Deliverable 6:** Business question in plain English, the SQL code, and the query output.

---

## Submission Checklist

Submit in a single ZIP file:

- [ ] Python script (`lab11.py` or `lab11.ipynb`)
- [ ] `retail_analytics.db` (the SQLite database file)
- [ ] Lab report (PDF or Word) with all deliverables

---

## Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Part 1 — Database setup | 10 | Database created without errors; row count confirmed |
| Part 2 — Aggregations | 20 | All three queries correct; HAVING explanation accurate |
| Part 3 — Window functions | 30 | ROW_NUMBER, RANK/DENSE_RANK, LAG, and running total all correct |
| Part 4 — CTEs | 20 | Both CTE queries correct; deliverable questions answered |
| Part 5 — Subqueries | 10 | Both subqueries correct; correlated subquery explanation accurate |
| Part 6 — Original query | 10 | Business question stated; three features used; query runs and produces meaningful output |
| **Total** | **100** | |

---

End of Lab 11

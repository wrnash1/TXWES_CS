# Lab Activity: Module 01 — Relational Database Fundamentals and SQL Review

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Total Points: 100

---

### Lab Overview

In this lab you will provision a Cloud SQL for PostgreSQL instance using the Google Cloud Console, connect to it via Cloud Shell, create a normalized schema with integrity constraints, insert sample data, and execute SELECT queries including JOINs, GROUP BY aggregation, and EXPLAIN ANALYZE plan analysis. These skills are directly tested in the Google Cloud Professional Cloud Database Engineer exam.

Estimated completion time: 60–75 minutes.

---

### Prerequisites

Before starting this lab, confirm the following.

- You have access to a Google Cloud student project with billing enabled or Cloud Skills Boost credits active.
- You have reviewed the Module 01 video scripts and reading guide.
- You are logged in to the Google Cloud Console at console.cloud.google.com with your institutional account.

---

### Part 1 — Provision Cloud SQL for PostgreSQL (20 points)

#### Step 1 — Create the Instance

1. In the Google Cloud Console, use the navigation menu to go to Databases, then SQL.
2. Click Create Instance.
3. Select PostgreSQL.
4. Set the configuration values shown in the table below, then click Create Instance and wait 3–5 minutes for provisioning to complete.

| Field | Value |
|---|---|
| Instance ID | txwes-pg-lab01 |
| Password | Choose a strong password and save it |
| Database version | PostgreSQL 15 |
| Edition | Enterprise |
| Preset | Development (saves credits) |
| Region | us-central1 |
| Zonal availability | Single zone |

Expand the Connections section. Under Authorized Networks, click Add Network. In the Network field enter `0.0.0.0/0` and name it `lab-access`. This allows Cloud Shell to connect. In a production environment you would restrict this to specific IP ranges.

**[SHOW CONSOLE: Cloud SQL instance list showing txwes-pg-lab01 with a green checkmark status]**

#### Step 2 — Connect via Cloud Shell

1. In the Cloud Console toolbar, click the Activate Cloud Shell icon at the top right.
2. When the Cloud Shell pane opens, run the command below.

```bash
gcloud sql connect txwes-pg-lab01 --user=postgres --quiet
```

Enter the password you set during instance creation when prompted. You should see the PostgreSQL prompt: `postgres=>`

**Deliverable 1 (5 points)**: Take a screenshot showing the `postgres=>` prompt in Cloud Shell. Save it as `lab01_screenshot_01.png`.

---

### Part 2 — Create Schema and Tables (25 points)

At the `postgres=>` prompt, run the following SQL commands to create a sample e-commerce database.

#### Step 3 — Create the Database

```sql
CREATE DATABASE txwes_ecommerce;
\c txwes_ecommerce
```

The `\c` command switches to the new database.

#### Step 4 — Create Tables with Constraints

```sql
-- Customers table
CREATE TABLE customers (
    customer_id   SERIAL        PRIMARY KEY,
    email         VARCHAR(255)  NOT NULL UNIQUE,
    full_name     VARCHAR(100)  NOT NULL,
    city          VARCHAR(100),
    created_at    TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    product_id    SERIAL        PRIMARY KEY,
    product_name  VARCHAR(200)  NOT NULL,
    category      VARCHAR(100)  NOT NULL,
    unit_price    NUMERIC(10,2) NOT NULL CHECK (unit_price > 0),
    stock_qty     INTEGER       NOT NULL DEFAULT 0 CHECK (stock_qty >= 0)
);

-- Orders table with foreign key to customers
CREATE TABLE orders (
    order_id      SERIAL        PRIMARY KEY,
    customer_id   INTEGER       NOT NULL,
    order_date    DATE          NOT NULL DEFAULT CURRENT_DATE,
    status        VARCHAR(20)   NOT NULL DEFAULT 'pending'
                                CHECK (status IN ('pending','shipped','delivered','cancelled')),
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE RESTRICT
);

-- Order line items with foreign keys to both orders and products
CREATE TABLE order_items (
    item_id       SERIAL        PRIMARY KEY,
    order_id      INTEGER       NOT NULL,
    product_id    INTEGER       NOT NULL,
    quantity      INTEGER       NOT NULL CHECK (quantity > 0),
    unit_price    NUMERIC(10,2) NOT NULL CHECK (unit_price > 0),
    CONSTRAINT fk_items_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_items_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON DELETE RESTRICT
);
```

#### Step 5 — Verify the Schema

```sql
-- List all tables in the current database
\dt

-- Describe the orders table structure
\d orders

-- Describe the order_items table structure
\d order_items
```

**Deliverable 2 (10 points)**: Take a screenshot showing the output of `\dt` listing all four tables and the output of `\d order_items` showing column definitions and constraints. Save as `lab01_screenshot_02.png`.

**Deliverable 3 (5 points)**: Write a one-paragraph explanation in your lab report describing what ON DELETE CASCADE on order_items means and why ON DELETE RESTRICT is used on orders instead.

**Deliverable 4 (10 points)**: Run the statement below, which intentionally violates a foreign key constraint. Copy the error message into your lab report and identify which constraint was violated by name.

```sql
-- This should fail with a foreign key violation
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (9999, 1, 2, 19.99);
```

---

### Part 3 — Insert Sample Data (15 points)

```sql
-- Insert customers
INSERT INTO customers (email, full_name, city) VALUES
    ('alice@example.com',   'Alice Johnson',  'Fort Worth'),
    ('bob@example.com',     'Bob Martinez',   'Dallas'),
    ('carol@example.com',   'Carol Lee',      'Austin'),
    ('david@example.com',   'David Chen',     'Houston'),
    ('elena@example.com',   'Elena Rossi',    'Fort Worth');

-- Insert products
INSERT INTO products (product_name, category, unit_price, stock_qty) VALUES
    ('Wireless Keyboard',   'Electronics',  49.99,  120),
    ('USB-C Hub',           'Electronics',  34.99,   85),
    ('Notebook Set',        'Office',        8.99,  500),
    ('Desk Lamp',           'Office',       24.99,   60),
    ('Laptop Stand',        'Electronics',  39.99,   45),
    ('Sticky Notes Pack',   'Office',        4.99, 1000);

-- Insert orders
INSERT INTO orders (customer_id, order_date, status) VALUES
    (1, '2024-11-01', 'delivered'),
    (1, '2024-12-15', 'delivered'),
    (2, '2024-11-20', 'delivered'),
    (3, '2025-01-05', 'shipped'),
    (3, '2025-01-18', 'pending'),
    (4, '2025-01-22', 'pending'),
    (5, '2024-12-01', 'cancelled');

-- Insert order items
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
    (1, 1, 1, 49.99),
    (1, 3, 2,  8.99),
    (2, 5, 1, 39.99),
    (2, 2, 1, 34.99),
    (3, 4, 2, 24.99),
    (4, 1, 1, 49.99),
    (4, 2, 2, 34.99),
    (5, 3, 5,  8.99),
    (6, 5, 1, 39.99),
    (6, 4, 1, 24.99),
    (7, 6, 3,  4.99);
```

**Deliverable 5 (5 points)**: Run `SELECT COUNT(*) FROM order_items;` and include the result in your lab report.

**Deliverable 6 (10 points)**: Write and run a single INSERT that violates the CHECK constraint on the products table (for example, a negative unit_price). Copy the error message into your lab report and identify which constraint was violated.

---

### Part 4 — SELECT Queries: JOINs and Aggregation (25 points)

Run each of the five queries below. For every query, take a screenshot of the result set.

#### Query 1 — INNER JOIN: Orders with Customer Names

```sql
SELECT
    o.order_id,
    c.full_name       AS customer_name,
    o.order_date,
    o.status
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
ORDER BY o.order_date DESC;
```

#### Query 2 — LEFT JOIN: All Customers Including Those with No Orders

```sql
SELECT
    c.customer_id,
    c.full_name,
    COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.full_name
ORDER BY order_count DESC;
```

#### Query 3 — Multi-Table JOIN: Full Order Details

```sql
SELECT
    c.full_name          AS customer,
    o.order_id,
    o.order_date,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS line_total
FROM customers c
JOIN orders      o  ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id    = oi.order_id
JOIN products    p  ON oi.product_id = p.product_id
ORDER BY o.order_id, p.product_name;
```

#### Query 4 — GROUP BY with HAVING: High-Value Customers

```sql
SELECT
    c.full_name,
    COUNT(DISTINCT o.order_id)                 AS total_orders,
    SUM(oi.quantity * oi.unit_price)           AS lifetime_value,
    ROUND(AVG(oi.quantity * oi.unit_price), 2) AS avg_line_value
FROM customers c
JOIN orders      o  ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id    = oi.order_id
WHERE o.status != 'cancelled'
GROUP BY c.customer_id, c.full_name
HAVING SUM(oi.quantity * oi.unit_price) > 50
ORDER BY lifetime_value DESC;
```

#### Query 5 — Subquery: Products Never Ordered

```sql
SELECT product_id, product_name, category
FROM   products
WHERE  product_id NOT IN (
    SELECT DISTINCT product_id
    FROM   order_items
)
ORDER BY product_name;
```

**Deliverable 7 (25 points)**: Include a screenshot of each query's result set. Below each screenshot, write one sentence explaining the business question that query answers.

---

### Part 5 — EXPLAIN ANALYZE and Index Creation (15 points)

#### Step 6 — View the Query Plan Before Indexing

```sql
EXPLAIN ANALYZE
SELECT c.full_name, o.order_date, o.status
FROM   customers c
JOIN   orders o ON c.customer_id = o.customer_id
WHERE  o.status = 'pending';
```

Note any Seq Scan nodes in the output and record the actual time values.

#### Step 7 — Create Indexes

```sql
-- Index on orders.status for the WHERE filter
CREATE INDEX idx_orders_status
    ON orders (status);

-- Index on orders.customer_id for the JOIN
CREATE INDEX idx_orders_customer_id
    ON orders (customer_id);

-- Index on order_items.order_id for the JOIN
CREATE INDEX idx_order_items_order_id
    ON order_items (order_id);
```

#### Step 8 — Refresh Statistics and Re-run the Plan

```sql
ANALYZE customers;
ANALYZE orders;
ANALYZE order_items;
ANALYZE products;
```

```sql
EXPLAIN ANALYZE
SELECT c.full_name, o.order_date, o.status
FROM   customers c
JOIN   orders o ON c.customer_id = o.customer_id
WHERE  o.status = 'pending';
```

**Deliverable 8 (15 points)**: In your lab report, include the EXPLAIN ANALYZE output from both before and after creating the indexes. Identify at least one difference in the query plan — a change in node type, estimated rows, or actual time. Explain in two to three sentences what the change means for query performance.

---

### Part 6 — Clean Up (Required)

Delete or stop the Cloud SQL instance after saving all deliverables. Leaving instances running incurs charges against your project credits.

To delete the instance:

```bash
gcloud sql instances delete txwes-pg-lab01 --quiet
```

To stop the instance instead of deleting it:

```bash
gcloud sql instances patch txwes-pg-lab01 --activation-policy=NEVER
```

---

### Lab Submission Checklist

Confirm all items are included in your submission before uploading.

- Deliverable 1 (5 pts) — Screenshot of `postgres=>` prompt
- Deliverable 2 (10 pts) — Screenshots of `\dt` and `\d order_items` output
- Deliverable 3 (5 pts) — Written explanation of ON DELETE CASCADE vs. RESTRICT
- Deliverable 4 (10 pts) — Foreign key violation error message and explanation
- Deliverable 5 (5 pts) — COUNT result from order_items
- Deliverable 6 (10 pts) — CHECK constraint violation error message and explanation
- Deliverable 7 (25 pts) — All five query result screenshots with one-sentence explanations
- Deliverable 8 (15 pts) — EXPLAIN ANALYZE before/after comparison and written analysis

---

### Grading Rubric — 100 Points Total

| Deliverable | Points | Criteria |
|---|---|---|
| 1 — Cloud Shell connection | 5 | Clear screenshot showing postgres=> prompt |
| 2 — Schema verification | 10 | Both \dt and \d order_items outputs visible |
| 3 — ON DELETE explanation | 5 | Correct explanation of CASCADE vs. RESTRICT |
| 4 — FK violation error | 10 | Error message copied; constraint identified by name |
| 5 — Row count result | 5 | Correct count shown |
| 6 — CHECK violation error | 10 | Error message copied; constraint identified |
| 7 — Five query results | 25 | All five results shown; one-sentence explanation each |
| 8 — EXPLAIN ANALYZE analysis | 15 | Before/after plans included; difference identified; explanation is accurate |
| Deductions | up to -10 | Instance not deleted or stopped after lab completion |

---

Reference: cloud.google.com/learn

---

## Part 9 — Challenge Exercise

### Challenge 1: Covering Index and Index-Only Scan

1. Add 10,000 additional rows to the `order_items` table using a `generate_series()` INSERT to simulate realistic table volume.
2. Run `EXPLAIN ANALYZE` on a query that selects `order_id` and `unit_price` from `order_items` WHERE `product_id = 2` and observe whether the plan uses a Seq Scan or Index Scan.
3. Create a covering index: `CREATE INDEX idx_oi_product_covering ON order_items (product_id) INCLUDE (order_id, unit_price);`
4. Run `ANALYZE order_items;` then re-run the same `EXPLAIN ANALYZE` and confirm the plan changes to an Index Only Scan, noting the reduction in actual time.

### Challenge 2: Enforcing Business Rules with a CHECK Constraint and Trigger

1. Add a `discount_pct` column to the `order_items` table: `ALTER TABLE order_items ADD COLUMN discount_pct NUMERIC(5,2) NOT NULL DEFAULT 0 CHECK (discount_pct >= 0 AND discount_pct < 100);`
2. Attempt to INSERT a row with `discount_pct = 110` and record the constraint violation error.
3. Write a `CREATE FUNCTION` and `CREATE TRIGGER` in PostgreSQL that automatically sets `discount_pct = 0` whenever a row is inserted with a NULL discount value, and test it with an INSERT that omits the `discount_pct` column.
4. Verify the trigger fired by querying the newly inserted row and confirming `discount_pct = 0`.

### Reflection Questions

1. After adding the covering index in Challenge 1, what specific change appeared in the EXPLAIN ANALYZE output that confirmed the database no longer needed to access the table heap, and why does eliminating heap access improve performance?
2. In a production system with millions of order items, what are the trade-offs of adding many covering indexes — specifically how do they affect INSERT and UPDATE performance, and how would you decide which queries justify a covering index versus a standard index?

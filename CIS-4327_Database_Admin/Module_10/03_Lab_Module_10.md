# Lab Activity: Module 10 — Database Performance Tuning

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Lab Overview

In this lab you will diagnose performance problems in a PostgreSQL database, read execution plans, identify missing indexes, add appropriate indexes, and measure the improvement. You will also use `pg_stat_statements` for aggregated query profiling and enable the MySQL slow query log.

**Estimated Time:** 90 minutes

**Prerequisites:**

- PostgreSQL 15 instance from previous labs (or fresh install)
- MySQL 8.0 instance from Module 07
- `pg_stat_statements` extension available (postgresql-contrib installed)

---

## Part 1 — Set Up the Performance Test Database

### Step 1.1 — Create the Schema

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE perflab;
\c perflab

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    email VARCHAR(150) UNIQUE NOT NULL,
    full_name VARCHAR(100),
    region VARCHAR(20),
    tier VARCHAR(10) DEFAULT 'standard',
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE orders (
    order_id BIGSERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    total_amount NUMERIC(12,2),
    order_date DATE DEFAULT CURRENT_DATE,
    notes JSONB
);

CREATE TABLE order_items (
    item_id BIGSERIAL PRIMARY KEY,
    order_id BIGINT NOT NULL,
    product_name VARCHAR(200),
    quantity INTEGER,
    unit_price NUMERIC(10,2)
);
```

### Step 1.2 — Seed Data (Intentionally No Indexes)

```sql
-- Customers: 50,000 rows
INSERT INTO customers (email, full_name, region, tier)
SELECT
    'user' || i || '@example.com',
    'User ' || i,
    CASE (i % 4)
        WHEN 0 THEN 'West'
        WHEN 1 THEN 'East'
        WHEN 2 THEN 'Central'
        ELSE 'South'
    END,
    CASE WHEN i % 10 = 0 THEN 'premium'
         WHEN i % 5 = 0 THEN 'gold'
         ELSE 'standard' END
FROM generate_series(1, 50000) AS s(i);

-- Orders: 500,000 rows
INSERT INTO orders (customer_id, status, total_amount, order_date, notes)
SELECT
    (random() * 49999 + 1)::int,
    CASE (i % 5)
        WHEN 0 THEN 'completed'
        WHEN 1 THEN 'active'
        WHEN 2 THEN 'cancelled'
        WHEN 3 THEN 'pending'
        ELSE 'active'
    END,
    round((random() * 5000)::numeric, 2),
    CURRENT_DATE - (random() * 730)::int,
    ('{"source": "web", "promo_code": "PROMO' || (i % 100) || '"}')::jsonb
FROM generate_series(1, 500000) AS s(i);

-- Order items: ~1.5M rows
INSERT INTO order_items (order_id, product_name, quantity, unit_price)
SELECT
    (random() * 499999 + 1)::bigint,
    'Product ' || (i % 200),
    (random() * 10 + 1)::int,
    round((random() * 200)::numeric, 2)
FROM generate_series(1, 1500000) AS s(i);

ANALYZE customers;
ANALYZE orders;
ANALYZE order_items;
```

---

## Part 2 — Diagnose with EXPLAIN ANALYZE

### Step 2.1 — Test Query 1: Customer Lookup by Email

Run without index:

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT customer_id, full_name, tier
FROM customers
WHERE email = 'user42000@example.com';
```

Record: plan type, estimated rows, actual time, buffers read.

**Lab Question 2.1:** What plan node is used? How many buffers were read? Is this efficient?

### Step 2.2 — Test Query 2: Orders by Customer

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT order_id, status, total_amount, order_date
FROM orders
WHERE customer_id = 12345
ORDER BY order_date DESC
LIMIT 10;
```

Record: plan node used, execution time.

### Step 2.3 — Test Query 3: Active Orders Above a Threshold

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT o.order_id, c.full_name, o.total_amount
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
WHERE o.status = 'active'
  AND o.total_amount > 4000
ORDER BY o.total_amount DESC
LIMIT 50;
```

Record: execution time, join type used, `Rows Removed by Filter`.

**Lab Question 2.2:** In Query 3, what does a high `Rows Removed by Filter` value tell you about which column would benefit from an index?

---

## Part 3 — Add Indexes and Measure Improvement

### Step 3.1 — Add Indexes

```sql
-- For Query 1: lookup by email (already has UNIQUE constraint index)
-- Verify:
\d customers
-- The UNIQUE constraint creates an implicit B-tree index on email

-- For Query 2: orders by customer_id with date ordering
CREATE INDEX idx_orders_customer_date ON orders (customer_id, order_date DESC);

-- For Query 3: active orders with high amounts
CREATE INDEX idx_orders_active_amount ON orders (status, total_amount DESC)
WHERE status = 'active';

-- General: covering index to avoid heap access for customer tier queries
CREATE INDEX idx_customers_email_tier ON customers (email) INCLUDE (full_name, tier);
```

### Step 3.2 — Re-Run Queries and Compare

```sql
-- Query 1 again
EXPLAIN (ANALYZE, BUFFERS)
SELECT customer_id, full_name, tier
FROM customers
WHERE email = 'user42000@example.com';
```

```sql
-- Query 2 again
EXPLAIN (ANALYZE, BUFFERS)
SELECT order_id, status, total_amount, order_date
FROM orders
WHERE customer_id = 12345
ORDER BY order_date DESC
LIMIT 10;
```

```sql
-- Query 3 again
EXPLAIN (ANALYZE, BUFFERS)
SELECT o.order_id, c.full_name, o.total_amount
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
WHERE o.status = 'active'
  AND o.total_amount > 4000
ORDER BY o.total_amount DESC
LIMIT 50;
```

**Lab Question 3.1:** Create a table in your lab report with the following columns: Query, Before Index (ms), After Index (ms), Speedup Factor. Fill it in with your measured times.

### Step 3.3 — Verify Index Only Scan for Query 1

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT full_name, tier
FROM customers
WHERE email = 'user10000@example.com';
```

**Lab Question 3.2:** Does this query use an Index Only Scan? How many heap blocks were read (`Heap Blocks: exact=`)? What does `exact=0` or a low number indicate?

---

## Part 4 — JSONB Query and GIN Index

### Step 4.1 — JSONB Containment Query Without Index

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT order_id, total_amount
FROM orders
WHERE notes @> '{"source": "web"}';
```

Record execution time.

### Step 4.2 — Add GIN Index

```sql
CREATE INDEX idx_orders_notes_gin ON orders USING GIN (notes);
```

### Step 4.3 — Re-Run JSONB Query

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT order_id, total_amount
FROM orders
WHERE notes @> '{"source": "web"}';
```

**Lab Question 4.1:** What execution time did you observe before and after the GIN index? What node type replaced the Seq Scan?

---

## Part 5 — pg_stat_statements Profiling

### Step 5.1 — Enable pg_stat_statements

```bash
sudo bash -c "echo \"shared_preload_libraries = 'pg_stat_statements'\" >> /etc/postgresql/15/main/postgresql.conf"
sudo systemctl restart postgresql
```

```bash
sudo -u postgres psql -d perflab -c "CREATE EXTENSION pg_stat_statements;"
```

### Step 5.2 — Generate Query Load

```bash
for i in $(seq 1 500); do
  sudo -u postgres psql -d perflab -c \
    "SELECT customer_id, full_name FROM customers WHERE email = 'user${i}@example.com';" \
    > /dev/null 2>&1
done

for i in $(seq 1 200); do
  sudo -u postgres psql -d perflab -c \
    "SELECT order_id, total_amount FROM orders WHERE customer_id = $((RANDOM % 50000 + 1)) ORDER BY order_date DESC LIMIT 5;" \
    > /dev/null 2>&1
done
```

### Step 5.3 — Query pg_stat_statements

```sql
\c perflab

SELECT left(query, 80) AS query,
       calls,
       round(total_exec_time::numeric, 2) AS total_ms,
       round(mean_exec_time::numeric, 2) AS mean_ms,
       rows
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

**Lab Question 5.1:** Which query accounts for the most total execution time? Does this match what you expected based on the indexes you added?

---

## Part 6 — MySQL Slow Query Log

### Step 6.1 — Enable Slow Query Log

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```

Add:

```ini
slow_query_log = ON
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 0.5
log_queries_not_using_indexes = ON
min_examined_row_limit = 100
```

```bash
sudo systemctl restart mysql
```

### Step 6.2 — Generate Some Slow Queries

```bash
mysql -h 127.0.0.1 -u root -p labshop -e "
SELECT * FROM products WHERE product_name LIKE '%Widget%';
SELECT * FROM orders WHERE order_total > 500 ORDER BY order_ts DESC;"
```

### Step 6.3 — Analyze the Slow Log

```bash
mysqldumpslow -s t -t 5 /var/log/mysql/slow.log
```

**Lab Question 6.1:** What queries appeared in the slow log? For each, identify which column would benefit from an index.

---

## Lab Deliverables

Submit a PDF containing:

1. EXPLAIN ANALYZE outputs for all queries before and after indexing.
2. The comparison table from Lab Question 3.1.
3. Written answers to all six Lab Questions.
4. A brief paragraph (4–6 sentences) explaining why a partial index on `(status, total_amount DESC) WHERE status = 'active'` is more efficient than a full index on `(status, total_amount DESC)` for queries that only access active orders.

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 2: EXPLAIN outputs captured with correct interpretation | 20 |
| Part 3: Index additions with before/after timing comparison | 30 |
| Part 4: GIN index demonstration with timing | 15 |
| Part 5: pg_stat_statements query and interpretation | 20 |
| Part 6: MySQL slow query log enabled and analyzed | 15 |
| **Total** | **100** |

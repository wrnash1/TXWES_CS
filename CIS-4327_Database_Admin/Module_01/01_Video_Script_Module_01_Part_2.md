# Video Script: Module 01 — Relational Database Fundamentals and SQL Review (Part 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Estimated Duration: 10–12 minutes

---

### Opening — Part 2 Overview

**[SHOW SLIDE: Module 01 Part 2 — DML, JOINs, GROUP BY, EXPLAIN ANALYZE]**

Welcome back. I am Professor Nash, and this is Part 2 of Module 01.

In Part 1 we covered the relational model, ACID properties, and DDL. Now we are going to work with data — SELECT queries, JOINs, aggregation with GROUP BY, and the EXPLAIN ANALYZE command that is critical for query performance analysis. All of these appear directly in the Google Cloud Professional Cloud Database Engineer exam.

---

### Section 1 — SQL DML: INSERT, UPDATE, DELETE

**[SHOW SLIDE: DML command categories]**

The Data Manipulation Language, or DML, is the set of commands that read and modify data in tables. The four core DML statements are SELECT, INSERT, UPDATE, and DELETE.

**[SHOW CODE]**

```sql
-- Insert a single customer
INSERT INTO customers (email, full_name)
VALUES ('alice@example.com', 'Alice Johnson');

-- Insert multiple rows in one statement
INSERT INTO customers (email, full_name)
VALUES
    ('bob@example.com',   'Bob Martinez'),
    ('carol@example.com', 'Carol Lee');

-- Update a customer's email
UPDATE customers
SET    email = 'alice.johnson@example.com'
WHERE  customer_id = 1;

-- Delete orders with a cancelled status
DELETE FROM orders
WHERE  status = 'cancelled';
```

**[END CODE]**

A critical point about DELETE: if you omit the WHERE clause, you delete every row in the table. The table structure remains, but all data is gone. TRUNCATE is even faster for clearing all rows because it does not generate row-level transaction log entries, but it also cannot be easily rolled back in all configurations.

---

### Section 2 — SELECT and Filtering

**[SHOW CODE]**

```sql
-- Basic SELECT with column projection
SELECT customer_id, full_name, email
FROM   customers
WHERE  created_at >= '2024-01-01'
ORDER  BY full_name ASC;

-- Filtering with multiple conditions
SELECT order_id, order_total, status
FROM   orders
WHERE  status = 'pending'
  AND  order_total > 100.00
ORDER  BY order_date DESC
LIMIT  50;

-- Pattern matching with LIKE
SELECT full_name, email
FROM   customers
WHERE  email LIKE '%@example.com';
```

**[END CODE]**

The WHERE clause filters rows before they are returned. ORDER BY sorts the result set — ASC for ascending, DESC for descending. LIMIT restricts the number of rows returned, which is important for performance when tables are large.

Note the difference between WHERE and HAVING. WHERE filters rows before aggregation. HAVING filters groups after aggregation. This distinction appears in exam questions.

---

### Section 3 — JOIN Types

**[SHOW SLIDE: Venn diagram of INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN]**

JOINs combine rows from two or more tables based on a related column. The exam tests each join type, so I am going to show you all of them with the same schema.

**[SHOW CODE]**

```sql
-- INNER JOIN: only rows where a match exists in both tables
SELECT c.full_name,
       o.order_id,
       o.order_total
FROM   customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;

-- LEFT OUTER JOIN: all customers, with NULLs where no order exists
SELECT c.full_name,
       o.order_id,
       o.order_total
FROM   customers c
LEFT  JOIN orders o ON c.customer_id = o.customer_id;

-- RIGHT OUTER JOIN: all orders, with NULLs where no customer match exists
SELECT c.full_name,
       o.order_id,
       o.order_total
FROM   customers c
RIGHT JOIN orders o ON c.customer_id = o.customer_id;

-- FULL OUTER JOIN: all rows from both tables, NULLs where no match
SELECT c.full_name,
       o.order_id
FROM   customers c
FULL  OUTER JOIN orders o ON c.customer_id = o.customer_id;
```

**[END CODE]**

INNER JOIN is the most common. It returns only rows where the join condition is met in both tables. If a customer has no orders, that customer does not appear in the result.

LEFT JOIN returns every row from the left table — customers in this case — and fills in NULLs for the right table columns where no match exists. This is how you find customers who have never placed an order: add WHERE o.order_id IS NULL.

RIGHT JOIN is the mirror image. Full OUTER JOIN returns everything from both tables.

---

### Section 4 — GROUP BY and Aggregation

**[SHOW CODE]**

```sql
-- Count orders per customer
SELECT   c.full_name,
         COUNT(o.order_id)       AS total_orders,
         SUM(o.order_total)      AS lifetime_value,
         AVG(o.order_total)      AS avg_order_value,
         MAX(o.order_total)      AS largest_order
FROM     customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.full_name
ORDER BY lifetime_value DESC;

-- HAVING filters groups after aggregation
SELECT   c.full_name,
         COUNT(o.order_id) AS total_orders
FROM     customers c
JOIN     orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.full_name
HAVING   COUNT(o.order_id) > 5;
```

**[END CODE]**

GROUP BY collapses multiple rows into a single summary row per unique combination of the grouped columns. Every column in SELECT must either be in the GROUP BY clause or wrapped in an aggregate function like COUNT, SUM, AVG, MAX, or MIN.

HAVING filters after grouping. In the second query, we only return customers who have placed more than five orders. This cannot be done with a WHERE clause because the count does not exist until after GROUP BY runs.

---

### Section 5 — EXPLAIN ANALYZE for Query Performance

**[SHOW SLIDE: Query execution plan output with cost estimates and actual timing]**

EXPLAIN ANALYZE is the tool you use to understand why a query is slow. It shows the query execution plan — the steps the database engine takes to retrieve data — along with actual timing information. This command is tested in the GCP exam's performance tuning domain.

**[SHOW CODE]**

```sql
-- View the query plan without executing
EXPLAIN
SELECT c.full_name, o.order_total
FROM   customers c
JOIN   orders o ON c.customer_id = o.customer_id
WHERE  o.status = 'pending';

-- View the plan AND execute, showing actual timing
EXPLAIN ANALYZE
SELECT c.full_name, o.order_total
FROM   customers c
JOIN   orders o ON c.customer_id = o.customer_id
WHERE  o.status = 'pending';
```

**[END CODE]**

**[SHOW SLIDE: Sample EXPLAIN ANALYZE output with annotations]**

In the output, look for these key indicators.

Seq Scan means the database is reading every row in a table. On large tables, this is a performance warning. It may mean a useful index does not exist for that column.

Index Scan means the database is using an index to find rows directly. This is efficient.

The cost estimate is shown as two numbers separated by two dots. The first number is the startup cost before the first row is returned. The second is the total cost. These are in abstract planner units, not milliseconds.

The actual time shows real milliseconds — this is the actual time column from EXPLAIN ANALYZE. Compare it to the cost estimate to see if the planner's assumptions are accurate.

Rows shows how many rows the planner estimated versus how many were actually returned. A large discrepancy between estimated and actual rows often indicates stale table statistics. Run ANALYZE to refresh statistics.

**[SHOW CODE]**

```sql
-- Refresh table statistics so the planner has accurate data
ANALYZE customers;
ANALYZE orders;

-- Create an index to eliminate a sequential scan on status
CREATE INDEX idx_orders_status
    ON orders (status);
```

**[END CODE]**

After creating the index on status and re-running EXPLAIN ANALYZE, you should see the Seq Scan on orders replaced by an Index Scan. This is how you diagnose and fix slow queries in Cloud SQL for PostgreSQL.

---

### Section 6 — Transactions and Concurrency Control

**[SHOW CODE]**

```sql
-- Explicit transaction block
BEGIN;

UPDATE accounts
SET    balance = balance - 500.00
WHERE  account_id = 101;

UPDATE accounts
SET    balance = balance + 500.00
WHERE  account_id = 202;

-- If both updates succeed, commit
COMMIT;

-- If any error occurs, roll back both updates
-- ROLLBACK;
```

**[END CODE]**

A transaction groups multiple SQL statements into a single atomic unit. If any statement inside the transaction fails, you execute ROLLBACK and the database returns to its state before BEGIN. If all statements succeed, COMMIT makes all changes permanent.

In PostgreSQL, every statement outside an explicit BEGIN/COMMIT block is automatically wrapped in its own implicit transaction. Cloud SQL for PostgreSQL supports the same transaction semantics as standard PostgreSQL.

---

### Section 7 — Exam Tips for Module 01

**[SHOW SLIDE: Exam tip callouts]**

Here are six exam tips specifically for the relational fundamentals domain.

First: when a scenario describes a workload with ACID requirements in a single region, the answer is Cloud SQL. When it adds global distribution, the answer is Cloud Spanner.

Second: know that INNER JOIN returns only matching rows. LEFT JOIN returns all rows from the left table. A WHERE clause filtering for NULL on the right-side column turns a LEFT JOIN into an anti-join — rows with no match.

Third: WHERE filters rows, HAVING filters groups. On an exam question that asks why a HAVING clause is needed, the answer involves filtering on an aggregate function result.

Fourth: EXPLAIN ANALYZE shows actual execution time. EXPLAIN alone shows the plan without running the query. Use EXPLAIN ANALYZE when you need real timing data.

Fifth: a Seq Scan on a large table in an execution plan is a signal to create an index. Not every Seq Scan is bad — on a very small table a sequential scan is faster than an index scan.

Sixth: ON DELETE RESTRICT prevents deletion of a parent row when child rows exist. ON DELETE CASCADE automatically deletes child rows when a parent is deleted. Know the difference — it appears in constraint scenario questions.

---

### Closing — Module 01 Wrap-Up

**[SHOW SLIDE: Module 01 complete — next steps]**

That completes Module 01. You now have the relational database and SQL foundation needed for every module that follows.

Your lab for this module walks you through creating these exact tables in Cloud SQL for PostgreSQL using Cloud Shell, inserting sample data, running JOINs and GROUP BY queries, and reading EXPLAIN ANALYZE output. Complete the lab before you take the quiz.

The discussion prompt asks you to apply relational design principles to a real business scenario. Read through the three scenarios carefully and respond to the one that best connects to your professional or academic experience.

I will see you in Module 02, where we go deep on database design: normalization, functional dependencies, and entity-relationship diagrams.

---

Reference: cloud.google.com/learn

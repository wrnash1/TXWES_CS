# Reading Guide: Module 11 — SQL for Data Analytics

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 3: Data Analysis

---

## Overview

This guide covers the advanced SQL techniques every data analyst must master: aggregations, GROUP BY with HAVING, window functions, CTEs, and subqueries. The CompTIA Data+ exam tests SQL knowledge throughout Domain 3. More importantly, these are the exact techniques you will use in every analytical role. Work through each code example and verify you understand what it produces before moving on.

---

## Section 1: SQL Execution Order

Understanding the logical order SQL executes clauses is essential for debugging and writing correct queries.

| Step | Clause | What Happens |
|------|--------|--------------|
| 1 | FROM | Identifies the source tables |
| 2 | JOIN | Combines rows from joined tables |
| 3 | WHERE | Filters individual rows |
| 4 | GROUP BY | Groups remaining rows by specified columns |
| 5 | HAVING | Filters groups after aggregation |
| 6 | SELECT | Computes output columns including aggregates |
| 7 | ORDER BY | Sorts the final result |
| 8 | LIMIT/TOP | Restricts the number of output rows |

**Key implication:** Because WHERE executes before GROUP BY, you cannot use aggregate functions in a WHERE clause. Use HAVING instead to filter based on aggregate results.

---

## Section 2: Aggregate Functions and GROUP BY

### Core Aggregate Functions

| Function | Description | NULL handling |
|----------|-------------|---------------|
| `COUNT(*)` | Counts all rows including NULLs | Includes NULLs |
| `COUNT(col)` | Counts non-null values in a column | Excludes NULLs |
| `SUM(col)` | Sums numeric values | Ignores NULLs |
| `AVG(col)` | Arithmetic mean of non-null values | Ignores NULLs |
| `MIN(col)` | Smallest value | Ignores NULLs |
| `MAX(col)` | Largest value | Ignores NULLs |

### GROUP BY Rules

- Every non-aggregated column in SELECT must appear in GROUP BY
- GROUP BY can reference multiple columns — each unique combination becomes one group
- You can GROUP BY expressions: `GROUP BY EXTRACT(YEAR FROM order_date)`

```sql
-- Revenue by region and year
SELECT
    region,
    EXTRACT(YEAR FROM order_date) AS order_year,
    COUNT(*)                      AS order_count,
    ROUND(SUM(amount), 2)         AS total_revenue,
    ROUND(AVG(amount), 2)         AS avg_order
FROM orders
GROUP BY region, EXTRACT(YEAR FROM order_date)
ORDER BY order_year, total_revenue DESC;
```

### HAVING Clause

HAVING filters groups after GROUP BY and aggregation. It can use aggregate functions.

```sql
-- Sales reps with total revenue over $200,000
SELECT
    sales_rep,
    COUNT(*)       AS order_count,
    SUM(amount)    AS total_revenue
FROM orders
GROUP BY sales_rep
HAVING SUM(amount) > 200000
ORDER BY total_revenue DESC;
```

### WHERE vs. HAVING

| Clause | Filters | Can Use Aggregates? | Executes |
|--------|---------|---------------------|---------|
| WHERE | Individual rows | No | Before GROUP BY |
| HAVING | Groups | Yes | After GROUP BY |

Common pattern — WHERE and HAVING in the same query:

```sql
-- Revenue by sales rep in 2024 where total revenue > $150,000
SELECT
    sales_rep,
    SUM(amount) AS total_revenue
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2024
GROUP BY sales_rep
HAVING SUM(amount) > 150000
ORDER BY total_revenue DESC;
```

---

## Section 3: Window Functions

Window functions compute values across a set of rows related to the current row without collapsing the result set.

### Syntax

`function_name([args]) OVER ([PARTITION BY col1, col2] [ORDER BY col3] [frame_clause])`

- `OVER` — required; marks this as a window function
- `PARTITION BY` — divides rows into independent partitions; omit to apply across all rows
- `ORDER BY` — defines row order within each partition
- Frame clause — optional; defines the sliding window (e.g., rolling 7-day average)

### ROW_NUMBER

Assigns a unique sequential integer starting at 1 within each partition. Ties receive different numbers.

```sql
-- Rank each customer's orders by amount, highest first
SELECT
    customer_id,
    order_id,
    amount,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY amount DESC
    ) AS customer_order_rank
FROM orders;
```

### RANK

Assigns the same rank to tied rows. After tied rows, the next rank skips numbers equal to the count of tied rows.

```sql
-- Rank all orders by amount (ties share rank; gaps follow)
SELECT
    order_id,
    amount,
    RANK() OVER (ORDER BY amount DESC) AS revenue_rank
FROM orders;
```

Example: If three rows tie for rank 1, the next row receives rank 4 (not 2).

### DENSE_RANK

Same as RANK for ties, but no gaps — the next rank after a tie is always consecutive.

```sql
-- Dense rank: no gaps after ties
SELECT
    order_id,
    amount,
    DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rev_rank
FROM orders;
```

Example: If three rows tie for rank 1, the next row receives rank 2 (not 4).

### ROW_NUMBER vs. RANK vs. DENSE_RANK

| Data: amounts 100, 100, 100, 80 | ROW_NUMBER | RANK | DENSE_RANK |
|---------------------------------|-----------|------|------------|
| First 100 | 1 | 1 | 1 |
| Second 100 | 2 | 1 | 1 |
| Third 100 | 3 | 1 | 1 |
| 80 | 4 | 4 | 2 |

### LAG and LEAD

LAG returns the value from a preceding row in the partition. LEAD returns the value from a following row.

`LAG(column, offset, default) OVER (PARTITION BY ... ORDER BY ...)`

```sql
-- Month-over-month revenue change
SELECT
    order_month,
    monthly_revenue,
    LAG(monthly_revenue, 1, 0) OVER (ORDER BY order_month) AS prev_month,
    monthly_revenue - LAG(monthly_revenue, 1, 0)
        OVER (ORDER BY order_month)                        AS mom_change
FROM (
    SELECT
        DATE_TRUNC('month', order_date) AS order_month,
        SUM(amount)                     AS monthly_revenue
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
) monthly;
```

### Running Total with Frame Clause

```sql
-- Cumulative revenue over time
SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue
FROM orders;
```

Frame clause keywords:

- `UNBOUNDED PRECEDING` — from the start of the partition
- `CURRENT ROW` — the current row
- `n PRECEDING` / `n FOLLOWING` — n rows before/after the current row
- `UNBOUNDED FOLLOWING` — to the end of the partition

---

## Section 4: Common Table Expressions (CTEs)

### CTE Syntax

```sql
WITH cte1 AS (
    SELECT ...
),
cte2 AS (
    SELECT ... FROM cte1 ...
)
SELECT * FROM cte2;
```

CTEs are named temporary result sets that:

- Exist only for the duration of the single query
- Can be referenced multiple times in the main query (computed once)
- Can reference earlier CTEs in the same WITH clause
- Make complex multi-step logic readable and maintainable

### CTE vs. Subquery vs. Temp Table

| Feature | CTE | Subquery | Temp Table |
|---------|-----|----------|-----------|
| Readability | High | Low (nested) | High |
| Reusable in same query | Yes | No | Yes |
| Persists after query | No | No | Yes (session) |
| Recursive queries | Yes | No | No |
| Performance | Usually same as subquery | Same as CTE | Materialized |

### Multi-CTE Example

```sql
-- Top-spending customer per region with their order count
WITH customer_totals AS (
    SELECT
        customer_id,
        region,
        COUNT(*)    AS order_count,
        SUM(amount) AS total_spend
    FROM orders
    GROUP BY customer_id, region
),
ranked_customers AS (
    SELECT
        customer_id,
        region,
        order_count,
        total_spend,
        RANK() OVER (PARTITION BY region ORDER BY total_spend DESC) AS spend_rank
    FROM customer_totals
)
SELECT region, customer_id, order_count, total_spend
FROM ranked_customers
WHERE spend_rank = 1
ORDER BY total_spend DESC;
```

---

## Section 5: Subqueries

### Types of Subqueries

| Type | Location | Description |
|------|----------|-------------|
| Scalar | SELECT or WHERE | Returns exactly one value |
| Table/derived | FROM | Returns a result set used as a table |
| Correlated | WHERE | References outer query; executes per outer row |
| EXISTS | WHERE | Returns true/false based on subquery result |

### Scalar Subquery in WHERE

```sql
-- Orders above the overall average amount
SELECT order_id, customer_id, amount
FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders)
ORDER BY amount DESC;
```

### Derived Table (Subquery in FROM)

```sql
-- Customers with above-average total spend
SELECT c.customer_name, totals.total_spend
FROM customers c
JOIN (
    SELECT customer_id, SUM(amount) AS total_spend
    FROM orders
    GROUP BY customer_id
) totals ON c.customer_id = totals.customer_id
WHERE totals.total_spend > (
    SELECT AVG(rep_total)
    FROM (
        SELECT customer_id, SUM(amount) AS rep_total
        FROM orders GROUP BY customer_id
    ) inner_avg
)
ORDER BY totals.total_spend DESC;
```

This query is significantly cleaner when rewritten with CTEs — which is exactly why CTEs are preferred in modern SQL.

### Correlated Subquery

A correlated subquery references the outer query's alias and executes once per outer row. Use cautiously on large tables due to performance.

```sql
-- Orders where amount exceeds that customer's average
SELECT o.order_id, o.customer_id, o.amount
FROM orders o
WHERE o.amount > (
    SELECT AVG(o2.amount)
    FROM orders o2
    WHERE o2.customer_id = o.customer_id
)
ORDER BY o.customer_id, o.amount DESC;
```

---

## Section 6: Analytical Query Patterns

### Percentile of a Value

```sql
-- What percentile is each order in overall revenue distribution?
SELECT
    order_id,
    amount,
    PERCENT_RANK() OVER (ORDER BY amount) AS pct_rank,
    CUME_DIST()    OVER (ORDER BY amount) AS cumulative_dist
FROM orders;
```

### Moving Average

```sql
-- 3-period rolling average of daily revenue
SELECT
    order_date,
    daily_revenue,
    AVG(daily_revenue) OVER (
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_3day_avg
FROM (
    SELECT order_date, SUM(amount) AS daily_revenue
    FROM orders
    GROUP BY order_date
) daily;
```

### First/Last Value per Group

```sql
-- First and last order date per customer
SELECT DISTINCT
    customer_id,
    FIRST_VALUE(order_date) OVER (
        PARTITION BY customer_id ORDER BY order_date ASC
    ) AS first_order_date,
    LAST_VALUE(order_date) OVER (
        PARTITION BY customer_id ORDER BY order_date ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_order_date
FROM orders;
```

---

## Section 7: Data+ Exam Tips

**Tip 1:** WHERE vs. HAVING — this is one of the most-tested SQL distinctions. WHERE filters rows before GROUP BY; HAVING filters groups after GROUP BY. Aggregate functions cannot appear in WHERE.

**Tip 2:** ROW_NUMBER vs. RANK vs. DENSE_RANK — know the tie-handling behavior for each. Exam scenarios present tied data and ask which function produces which output.

**Tip 3:** LAG and LEAD — know that LAG accesses previous rows and LEAD accesses future rows. Know the three-argument form: `LAG(col, offset, default)`.

**Tip 4:** CTE syntax — know the `WITH cte_name AS (...)` structure and that multiple CTEs are separated by commas, not semicolons.

**Tip 5:** `COUNT(*)` counts all rows including NULLs. `COUNT(column)` counts only non-null values. This distinction appears in exam questions about NULL handling.

**Tip 6:** Window functions use `OVER()` — if you see `OVER (PARTITION BY ...)` in a SQL snippet, it is a window function. If the answer choices discuss "collapsing rows," that is GROUP BY, not a window function.

---

## Practice Problems

**Problem 1:** Write a query that returns each region's total revenue, average order value, and number of orders, but only for regions that had more than 50 orders.

**Problem 2:** Write a CTE-based query that finds the top-3 sales reps by total revenue in each region. Use RANK() and filter to rank <= 3.

**Problem 3:** Write a query using LAG that shows each month's revenue and the change from the prior month, for the year 2024 only.

**Problem 4:** What is the difference in output between `ROW_NUMBER()` and `RANK()` when five rows share the same value in the ORDER BY column?

---

## 9. Supplemental Resources

**1. Mode Analytics SQL Tutorial — Window Functions**
<https://mode.com/sql-tutorial/sql-window-functions>
An interactive, browser-based SQL tutorial covering window functions including ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, and SUM OVER — directly aligned with Module 11 content. Includes live query execution so you can test every example in the browser without local setup.

**2. PostgreSQL Documentation — Window Functions**
<https://www.postgresql.org/docs/current/tutorial-window.html>
The official PostgreSQL tutorial for window functions, covering PARTITION BY, ORDER BY, frame specifications (ROWS BETWEEN), and the difference between window functions and GROUP BY. Authoritative reference for the ANSI SQL standard behavior tested on the Data+ exam.

**3. SQLZoo — SELECT within SELECT (Subqueries)**
<https://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial>
An interactive tutorial covering correlated and non-correlated subqueries with progressively complex exercises. Directly supports the subquery and CTE concepts in Module 11 and reinforces the logical execution order of SQL queries.

---

End of Module 11 Reading Guide

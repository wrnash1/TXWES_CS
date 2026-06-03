# Video Script: Module 11 — SQL for Data Analytics

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA Data+ (DA0-001)

---

## Segment 1: Introduction (0:00–1:30)

Welcome back to CIS-4336. I'm Professor Nash. Today we are going deep into SQL — specifically the advanced analytical features that separate a basic SQL user from a true data analyst.

Most people who learn SQL stop at `SELECT`, `WHERE`, and `JOIN`. That covers about 20% of what SQL can do. The features we are covering today — aggregations with GROUP BY and HAVING, window functions, CTEs, and subqueries — are what 80% of real analytical work actually requires.

These features are tested in Domain 3 of the CompTIA Data+ exam, and they come up in almost every data analyst technical interview. More importantly, they are the difference between an analyst who can answer a business question and one who cannot.

We are going to work with a consistent retail sales dataset throughout the entire module — so you will see the same tables in every example, building from simple to complex.

[PAUSE — Slide: Module 11 Objectives]

---

## Segment 2: Dataset and Setup (1:30–2:30)

We will work with three tables throughout this module.

The `orders` table contains one row per order: order_id, customer_id, order_date, region, sales_rep, and amount.

The `customers` table contains customer information: customer_id, customer_name, city, state, and tier (Bronze, Silver, Gold).

The `products` table contains: product_id, product_name, category, and unit_price.

[SHOW CHART — Entity-relationship diagram of the three tables with primary and foreign key connections]

[PAUSE]

These three tables will appear in every example. Keep this diagram in mind as we go.

---

## Segment 3: Aggregations and GROUP BY (2:30–6:00)

Aggregation functions operate on a set of rows and return a single value. The most important ones are COUNT, SUM, AVG, MIN, and MAX.

[PAUSE]

```sql
-- Total revenue and order count by region
SELECT
    region,
    COUNT(*)           AS order_count,
    SUM(amount)        AS total_revenue,
    AVG(amount)        AS avg_order_value,
    MIN(amount)        AS min_order,
    MAX(amount)        AS max_order
FROM orders
GROUP BY region
ORDER BY total_revenue DESC;
```

The `GROUP BY` clause collapses all rows with the same region value into a single output row. The aggregate functions then apply within each group.

[PAUSE]

A critical rule: every column in the SELECT list that is not inside an aggregate function must appear in the GROUP BY clause. If you SELECT `region` and `sales_rep` but only GROUP BY `region`, the database does not know which `sales_rep` value to show — it will throw an error or return undefined behavior.

```sql
-- Multi-column grouping: revenue by region and year
SELECT
    region,
    EXTRACT(YEAR FROM order_date) AS order_year,
    COUNT(*)                      AS order_count,
    ROUND(SUM(amount), 2)         AS total_revenue
FROM orders
GROUP BY region, EXTRACT(YEAR FROM order_date)
ORDER BY order_year, total_revenue DESC;
```

[PAUSE]

### HAVING Clause

The `WHERE` clause filters rows before aggregation. The `HAVING` clause filters groups after aggregation. This is a critical distinction.

You cannot use an aggregate function in a WHERE clause — that is why HAVING exists.

```sql
-- Regions with total revenue over $500,000
SELECT
    region,
    SUM(amount) AS total_revenue
FROM orders
GROUP BY region
HAVING SUM(amount) > 500000
ORDER BY total_revenue DESC;
```

[PAUSE]

Mnemonic for the order of SQL clause execution:

`FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`

Notice that WHERE executes before GROUP BY (filters rows first), but HAVING executes after GROUP BY (filters groups).

---

## Segment 4: Window Functions — ROW_NUMBER and RANK (6:00–11:00)

Window functions are the most powerful feature we are covering today. They perform calculations across a set of rows — called a "window" — that are related to the current row, without collapsing the result set.

Unlike GROUP BY, window functions do not reduce the number of output rows. Every input row still appears in the output, with the window function result added as an additional column.

[SHOW CHART — Visual diagram: regular aggregate collapses rows vs. window function adds a column while keeping all rows]

[PAUSE]

The syntax is:

`function_name() OVER (PARTITION BY column ORDER BY column)`

- `OVER` tells SQL this is a window function
- `PARTITION BY` divides rows into groups (like GROUP BY, but without collapsing)
- `ORDER BY` within the OVER clause defines the order within each partition

### ROW_NUMBER

ROW_NUMBER assigns a unique sequential integer to each row within a partition, starting at 1.

```sql
-- Rank orders within each region by amount (highest first)
SELECT
    order_id,
    region,
    amount,
    ROW_NUMBER() OVER (
        PARTITION BY region
        ORDER BY amount DESC
    ) AS row_num
FROM orders;
```

[PAUSE]

ROW_NUMBER always produces unique values — even if two rows are tied, they receive different numbers. This makes it useful for selecting exactly N rows per group.

```sql
-- Top 3 orders per region
SELECT *
FROM (
    SELECT
        order_id,
        region,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY region ORDER BY amount DESC
        ) AS rn
    FROM orders
) ranked
WHERE rn <= 3;
```

[PAUSE]

### RANK and DENSE_RANK

RANK assigns the same rank to tied values, then skips to leave a gap. If two rows tie for rank 1, the next row gets rank 3 (not 2).

DENSE_RANK also assigns the same rank to ties but does not skip — the next rank after tied rows is the next consecutive number.

```sql
-- RANK vs. DENSE_RANK for tied amounts
SELECT
    order_id,
    amount,
    RANK()       OVER (ORDER BY amount DESC) AS rank_val,
    DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank_val
FROM orders
ORDER BY amount DESC;
```

[PAUSE]

When to use each:

- `ROW_NUMBER` — when you need exactly N rows per group; no ties allowed
- `RANK` — when ties should share a rank and you want position gaps
- `DENSE_RANK` — when ties should share a rank but you do not want gaps

---

## Segment 5: Window Functions — LAG and LEAD (11:00–14:00)

LAG and LEAD allow you to access the value from a previous or following row within the same partition — without a self-join. This makes them invaluable for time-series analysis and calculating period-over-period changes.

```sql
-- Month-over-month revenue change using LAG
SELECT
    order_month,
    monthly_revenue,
    LAG(monthly_revenue, 1) OVER (ORDER BY order_month) AS prev_month_revenue,
    monthly_revenue
      - LAG(monthly_revenue, 1) OVER (ORDER BY order_month) AS revenue_change,
    ROUND(
        (monthly_revenue - LAG(monthly_revenue, 1) OVER (ORDER BY order_month))
        * 100.0
        / LAG(monthly_revenue, 1) OVER (ORDER BY order_month),
        2
    ) AS pct_change
FROM (
    SELECT
        DATE_TRUNC('month', order_date) AS order_month,
        SUM(amount)                     AS monthly_revenue
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
) monthly_agg
ORDER BY order_month;
```

[PAUSE]

`LAG(column, offset)` returns the value from `offset` rows before the current row. `LEAD(column, offset)` returns the value from `offset` rows after.

Both functions accept an optional third argument — the default value to return when the offset goes beyond the partition boundaries (e.g., the first row has no previous row for LAG).

```sql
-- LAG with default value of 0
LAG(monthly_revenue, 1, 0) OVER (ORDER BY order_month)
```

[PAUSE]

### Running Total with SUM OVER

Window functions also support running aggregates — accumulating sums, averages, or counts.

```sql
-- Running total of revenue by date
SELECT
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date
                      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM orders
ORDER BY order_date;
```

---

## Segment 6: Common Table Expressions (CTEs) (14:00–17:00)

A Common Table Expression is a named, temporary result set defined at the top of a query. It exists only for the duration of that query.

CTEs make complex queries dramatically more readable by breaking them into named logical steps — like defining intermediate variables before the main calculation.

Syntax:

```sql
WITH cte_name AS (
    SELECT ...
    FROM ...
    WHERE ...
)
SELECT * FROM cte_name;
```

[PAUSE]

You can chain multiple CTEs in a single query:

```sql
-- Two-CTE example: regional top performers
WITH regional_totals AS (
    SELECT
        region,
        sales_rep,
        SUM(amount) AS rep_revenue
    FROM orders
    GROUP BY region, sales_rep
),
ranked_reps AS (
    SELECT
        region,
        sales_rep,
        rep_revenue,
        RANK() OVER (PARTITION BY region ORDER BY rep_revenue DESC) AS rank_val
    FROM regional_totals
)
SELECT region, sales_rep, rep_revenue
FROM ranked_reps
WHERE rank_val = 1
ORDER BY rep_revenue DESC;
```

[PAUSE]

This query is equivalent to nested subqueries but far more readable. Notice that `ranked_reps` references `regional_totals` — CTEs can reference earlier CTEs in the same WITH clause.

CTEs are also the building block for recursive queries, which can traverse hierarchical data (like an organizational chart) — though that is beyond today's scope.

---

## Segment 7: Subqueries (17:00–19:30)

A subquery is a SELECT statement nested inside another SQL statement. Subqueries can appear in the SELECT, FROM, WHERE, and HAVING clauses.

[PAUSE]

### Subquery in WHERE

```sql
-- Customers who placed orders above the overall average
SELECT customer_id, amount
FROM orders
WHERE amount > (
    SELECT AVG(amount)
    FROM orders
)
ORDER BY amount DESC;
```

The inner query `SELECT AVG(amount) FROM orders` executes first and returns a single value. The outer query then filters using that value.

[PAUSE]

### Correlated Subquery

A correlated subquery references a column from the outer query — it executes once per outer row, which can be slow on large tables.

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

[PAUSE]

### Subquery in FROM (Derived Table)

```sql
-- Average revenue per region for regions with more than 100 orders
SELECT region, avg_revenue
FROM (
    SELECT
        region,
        COUNT(*)       AS order_count,
        AVG(amount)    AS avg_revenue
    FROM orders
    GROUP BY region
) region_stats
WHERE order_count > 100
ORDER BY avg_revenue DESC;
```

This pattern — a subquery in the FROM clause — is sometimes called a derived table or inline view. Modern SQL best practice prefers CTEs over derived tables for readability, but both approaches produce identical results.

---

## Segment 8: Module Summary (19:30–21:00)

Let me wrap up.

[PAUSE]

Aggregations and GROUP BY:

- Aggregate functions: COUNT, SUM, AVG, MIN, MAX
- GROUP BY groups rows and applies aggregates within each group
- WHERE filters rows before aggregation; HAVING filters groups after aggregation
- Execution order: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

Window functions:

- Execute across a window of related rows without collapsing the result
- `OVER (PARTITION BY ... ORDER BY ...)` defines the window
- `ROW_NUMBER` — unique sequential integer per partition
- `RANK` — same rank for ties, gaps after ties
- `DENSE_RANK` — same rank for ties, no gaps
- `LAG` / `LEAD` — access values from preceding or following rows

CTEs:

- Named temporary result sets defined with `WITH cte AS (...)`
- Make complex multi-step queries readable and maintainable
- Multiple CTEs can chain by referencing each other

Subqueries:

- Nested SELECT statements in WHERE, FROM, or SELECT clauses
- Correlated subqueries reference the outer query and run once per outer row

For the Data+ exam: know the difference between WHERE and HAVING, understand when to use ROW_NUMBER vs. RANK vs. DENSE_RANK, and be able to read and interpret a CTE-based query.

Your lab this week writes all of these in a SQLite database. See you in Module 12.

[PAUSE — End card]

---

End of Module 11 Video Script

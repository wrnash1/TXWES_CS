# Video Script — Module 04: Relational Databases and SQL for Analytics

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Runtime:** 20–24 minutes
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 2: Data Mining; Domain 3: Data Analysis

---

## Segment 1 — Introduction (2 minutes)

Welcome back to CIS-4336. I am Professor Nash, and this is Module 04: Relational Databases and SQL for Analytics.

SQL — Structured Query Language — is the most important tool in an analyst's technical toolkit. It is the lingua franca of data: every major database platform, cloud warehouse, and BI tool either uses SQL directly or translates to it behind the scenes. The CompTIA Data+ exam expects you to read, write, and interpret SQL queries, and this module gives you that foundation.

By the end of this module, you will be able to:

- Write SELECT queries with filtering, sorting, and column expressions
- Use GROUP BY and HAVING to aggregate data by category
- Write INNER, LEFT, RIGHT, and FULL OUTER JOINs
- Apply window functions including ROW_NUMBER, RANK, and running totals with SUM OVER
- Recognize when each SQL clause is appropriate for a given analytical question
- Apply SQL knowledge to Data+ exam scenarios in Domains 2 and 3

Let us get started.

---

## Segment 2 — SQL Fundamentals: SELECT, WHERE, ORDER BY (3 minutes)

Every SQL query begins with SELECT. The basic structure is: SELECT columns FROM table WHERE condition ORDER BY column.

[SHOW CHART: Annotated diagram of a SELECT statement with each clause labeled and its purpose described]

Let me walk through a practical example. Suppose we have an ORDERS table with columns: ORDER_ID, CUSTOMER_ID, ORDER_DATE, REGION, PRODUCT_CATEGORY, and TOTAL_AMOUNT.

To retrieve all orders from the North region placed in 2024, ordered by total amount descending:

[SHOW CODE]

```sql
SELECT ORDER_ID, CUSTOMER_ID, ORDER_DATE, TOTAL_AMOUNT
FROM ORDERS
WHERE REGION = 'North'
  AND ORDER_DATE >= '2024-01-01'
  AND ORDER_DATE < '2025-01-01'
ORDER BY TOTAL_AMOUNT DESC;
```

The WHERE clause filters rows before they are returned. Multiple conditions are combined with AND (all must be true) or OR (any must be true).

The ORDER BY clause sorts results. DESC means descending (highest to lowest). ASC is the default (lowest to highest).

Column expressions in SELECT let you compute new values inline:

[SHOW CODE]

```sql
SELECT ORDER_ID,
       TOTAL_AMOUNT,
       TOTAL_AMOUNT * 0.10 AS estimated_tax,
       TOTAL_AMOUNT * 1.10 AS total_with_tax
FROM ORDERS
WHERE REGION = 'North';
```

The AS keyword gives a column or expression an alias — a name for the output column.

---

## Segment 3 — GROUP BY and Aggregation (4 minutes)

Aggregation is where SQL becomes powerful for analytics. The GROUP BY clause groups rows by one or more columns and applies aggregate functions to each group.

The core aggregate functions are COUNT, SUM, AVG, MIN, and MAX.

[SHOW CODE]

```sql
-- Total sales by region
SELECT REGION,
       COUNT(*) AS order_count,
       SUM(TOTAL_AMOUNT) AS total_revenue,
       AVG(TOTAL_AMOUNT) AS avg_order_value,
       MIN(TOTAL_AMOUNT) AS min_order,
       MAX(TOTAL_AMOUNT) AS max_order
FROM ORDERS
GROUP BY REGION
ORDER BY total_revenue DESC;
```

Every column in SELECT that is not inside an aggregate function must appear in the GROUP BY clause. This is one of the most common SQL errors beginners make.

The query execution order in SQL is important to understand: FROM is processed first, then WHERE, then GROUP BY, then HAVING, then SELECT, then ORDER BY. This order explains why you cannot filter on an aggregate in a WHERE clause — the aggregation has not happened yet when WHERE runs.

That is where HAVING comes in.

**HAVING** filters groups after aggregation. It is the GROUP BY equivalent of WHERE.

[SHOW CODE]

```sql
-- Regions where total revenue exceeds $500,000
SELECT REGION,
       SUM(TOTAL_AMOUNT) AS total_revenue
FROM ORDERS
GROUP BY REGION
HAVING SUM(TOTAL_AMOUNT) > 500000
ORDER BY total_revenue DESC;
```

On the Data+ exam, the distinction between WHERE and HAVING is a guaranteed question. Remember: WHERE filters rows before grouping. HAVING filters groups after aggregation.

---

## Segment 4 — JOINs (4 minutes)

Real analytical datasets span multiple tables. JOINs combine rows from two or more tables based on a matching column condition.

**INNER JOIN** returns only rows where the join condition is matched in both tables. Rows with no match in either table are excluded.

[SHOW CODE]

```sql
-- Customers with their orders (excludes customers who have no orders)
SELECT c.CUSTOMER_ID, c.FIRST_NAME, c.REGION,
       o.ORDER_ID, o.ORDER_DATE, o.TOTAL_AMOUNT
FROM CUSTOMERS c
INNER JOIN ORDERS o ON c.CUSTOMER_ID = o.CUSTOMER_ID;
```

**LEFT JOIN** returns all rows from the left table and matched rows from the right. Where there is no match, right-table columns are NULL. This is the most commonly used join in analytics for "include all entities, with or without related records."

[SHOW CODE]

```sql
-- All customers, including those with no orders
SELECT c.CUSTOMER_ID, c.FIRST_NAME,
       o.ORDER_ID,
       COALESCE(o.TOTAL_AMOUNT, 0) AS order_amount
FROM CUSTOMERS c
LEFT JOIN ORDERS o ON c.CUSTOMER_ID = o.CUSTOMER_ID;
```

COALESCE returns the first non-null argument. Here it replaces null TOTAL_AMOUNT values with 0 for customers who have no orders.

**RIGHT JOIN** is the mirror of LEFT JOIN — all rows from the right table plus matches from the left. In practice, RIGHT JOIN is rare; analysts typically rewrite it as a LEFT JOIN by swapping the table order.

**FULL OUTER JOIN** returns all rows from both tables, with NULLs filling gaps where no match exists. Useful for comparing two lists and finding what is in one but not the other.

[SHOW CHART: Four-quadrant Venn diagram showing INNER JOIN (intersection only), LEFT JOIN (all left plus intersection), RIGHT JOIN (all right plus intersection), and FULL OUTER JOIN (all of both circles)]

---

## Segment 5 — Window Functions (4 minutes)

Window functions are among the most powerful tools in SQL for analytics. Unlike GROUP BY — which collapses rows into one row per group — window functions compute aggregate values while keeping every individual row visible.

The syntax is: function() OVER (PARTITION BY column ORDER BY column).

PARTITION BY divides the dataset into groups (like GROUP BY). ORDER BY within OVER defines the sequence for ordered functions.

Let me show three practical window function examples.

**Running total:**

[SHOW CODE]

```sql
SELECT ORDER_DATE,
       REGION,
       TOTAL_AMOUNT,
       SUM(TOTAL_AMOUNT) OVER (
           PARTITION BY REGION
           ORDER BY ORDER_DATE
       ) AS running_total_by_region
FROM ORDERS;
```

This query adds a column showing the cumulative total for each region up to and including the current row's date — without collapsing the rows.

**Rank within group:**

[SHOW CODE]

```sql
SELECT CUSTOMER_ID,
       TOTAL_AMOUNT,
       RANK() OVER (ORDER BY TOTAL_AMOUNT DESC) AS sales_rank
FROM ORDERS;
```

RANK assigns a rank to each row. Tied values receive the same rank, and the next rank after a tie skips the appropriate number. ROW_NUMBER assigns unique sequential numbers regardless of ties.

**Moving average:**

[SHOW CODE]

```sql
SELECT ORDER_DATE,
       TOTAL_AMOUNT,
       AVG(TOTAL_AMOUNT) OVER (
           ORDER BY ORDER_DATE
           ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
       ) AS seven_day_moving_avg
FROM ORDERS;
```

ROWS BETWEEN defines the window frame — here, the current row and the six rows preceding it (a seven-row window). This produces a seven-day moving average.

[SHOW CHART: Table showing ORDER_DATE, TOTAL_AMOUNT, and seven_day_moving_avg columns side by side, illustrating how the moving average lags the raw values]

Window functions appear on the Data+ exam. Know the difference between RANK and ROW_NUMBER, and understand what PARTITION BY and ORDER BY within OVER do.

---

## Segment 6 — Subqueries and CTEs (2 minutes)

For complex analytical queries, SQL provides two tools for building modular logic.

A **subquery** embeds one SELECT inside another. The inner query runs first and its result is used by the outer query.

[SHOW CODE]

```sql
-- Customers whose total spending exceeds the average customer total
SELECT CUSTOMER_ID, total_spent
FROM (
    SELECT CUSTOMER_ID, SUM(TOTAL_AMOUNT) AS total_spent
    FROM ORDERS
    GROUP BY CUSTOMER_ID
) AS customer_totals
WHERE total_spent > (
    SELECT AVG(total_spent)
    FROM (
        SELECT SUM(TOTAL_AMOUNT) AS total_spent
        FROM ORDERS
        GROUP BY CUSTOMER_ID
    ) AS avg_base
);
```

A **Common Table Expression (CTE)** uses the WITH keyword to define named intermediate results before the main query. CTEs are more readable than nested subqueries and are reusable within the same query.

[SHOW CODE]

```sql
WITH customer_totals AS (
    SELECT CUSTOMER_ID, SUM(TOTAL_AMOUNT) AS total_spent
    FROM ORDERS
    GROUP BY CUSTOMER_ID
),
avg_spend AS (
    SELECT AVG(total_spent) AS avg_total FROM customer_totals
)
SELECT ct.CUSTOMER_ID, ct.total_spent
FROM customer_totals ct, avg_spend a
WHERE ct.total_spent > a.avg_total;
```

---

## Segment 7 — Exam Alignment and Closing (2 minutes)

SQL knowledge is tested throughout the Data+ exam — in Domain 2 (Data Mining) and Domain 3 (Data Analysis). The exam expects you to:

- Identify which SQL clause filters rows before grouping versus after grouping
- Interpret the output of a GROUP BY query
- Choose the correct JOIN type for a given requirement
- Explain what a window function does differently from GROUP BY

For additional exam preparation, visit comptia.org for the official objectives and professormesser.com for free study materials.

Your Module 04 assignments:

- Complete the Reading Guide — the SQL analytics query reference and window function table are high-priority
- Complete Lab 04 — you will write GROUP BY, HAVING, and window function queries against a provided SQLite database
- Complete the ten-question quiz
- Post to the Discussion Board by Wednesday and respond to two classmates by Sunday

See you in Module 05, where we tackle the statistical foundations that underpin all quantitative analysis.

---

End of Module 04 Video Script — Estimated runtime: 23 minutes

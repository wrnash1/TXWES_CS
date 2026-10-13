# Reading Guide — Module 04: Relational Databases and SQL for Analytics

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4336 &BULL; DATA ANALYTICS & BUSINESS INTELLIGENCE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 2: Data Mining; Domain 3: Data Analysis

---

## Overview

SQL is the foundational tool of data analytics. This guide provides a complete analytical SQL reference — from SELECT basics through window functions and CTEs. Study each section carefully; the lab and quiz require writing SQL, not just recognizing it.

---

## Section 1 — Core Vocabulary

| Term | Definition |
|---|---|
| SQL | Structured Query Language — the standard language for querying and manipulating relational databases |
| SELECT | The SQL clause that specifies which columns to return |
| FROM | Identifies the table or subquery to retrieve data from |
| WHERE | Filters rows before any grouping or aggregation |
| GROUP BY | Groups rows by one or more columns so aggregate functions can be applied per group |
| HAVING | Filters groups after aggregation — applies to aggregate results, not individual rows |
| ORDER BY | Sorts the result set; ASC (default) or DESC |
| JOIN | Combines rows from two or more tables based on a matching condition |
| INNER JOIN | Returns only rows with a match in both joined tables |
| LEFT JOIN | Returns all rows from the left table; NULLs for non-matching right-table columns |
| FULL OUTER JOIN | Returns all rows from both tables; NULLs fill unmatched sides |
| Aggregate function | A function that computes a single result from a group of rows: COUNT, SUM, AVG, MIN, MAX |
| Window function | A function that computes over a defined "window" of rows while keeping all rows visible |
| OVER | Introduces the window definition for a window function |
| PARTITION BY | Divides data into groups within a window function (similar to GROUP BY but without collapsing rows) |
| CTE | Common Table Expression — a named temporary result defined with the WITH keyword |
| Subquery | A SELECT statement nested inside another query |
| COALESCE | Returns the first non-null argument in a list |
| ALIAS | A temporary name given to a column, expression, or table using the AS keyword |
| NULL | Represents a missing or unknown value in SQL |

---

## Section 2 — SQL Query Execution Order

SQL clauses are processed in a specific order that differs from how they are written. Understanding this order explains why certain references are invalid in certain clauses.

| Execution Step | Clause | What Happens |
|---|---|---|
| 1 | FROM | Identify the source table(s) |
| 2 | JOIN | Combine tables based on join conditions |
| 3 | WHERE | Filter individual rows (before aggregation) |
| 4 | GROUP BY | Group filtered rows |
| 5 | HAVING | Filter groups (after aggregation) |
| 6 | SELECT | Compute output columns and expressions |
| 7 | DISTINCT | Remove duplicate output rows |
| 8 | ORDER BY | Sort the final result |
| 9 | LIMIT / TOP | Restrict the number of output rows |

Key implication: You cannot reference a SELECT alias in a WHERE clause, because WHERE is evaluated before SELECT. You cannot use an aggregate function in a WHERE clause — aggregation has not happened yet when WHERE runs. That is what HAVING is for.

---

## Section 3 — Aggregate Functions Reference

| Function | Syntax | Returns | Handles NULLs |
|---|---|---|---|
| COUNT(*) | `COUNT(*)` | Number of rows in group | Counts all rows including NULLs |
| COUNT(col) | `COUNT(column)` | Number of non-null values in column | Ignores NULLs |
| SUM | `SUM(column)` | Sum of all non-null values | Ignores NULLs |
| AVG | `AVG(column)` | Mean of all non-null values | Ignores NULLs — denominator is non-null count |
| MIN | `MIN(column)` | Smallest value | Ignores NULLs |
| MAX | `MAX(column)` | Largest value | Ignores NULLs |

### GROUP BY Query Template

```sql
SELECT grouping_column,
       COUNT(*) AS row_count,
       SUM(measure) AS total,
       AVG(measure) AS average
FROM table_name
WHERE row_filter_condition
GROUP BY grouping_column
HAVING SUM(measure) > threshold
ORDER BY total DESC;
```

---

## Section 4 — JOIN Types Reference

| JOIN Type | Rows Returned | Use Case |
|---|---|---|
| INNER JOIN | Only rows matched in both tables | Find related records that exist in both tables |
| LEFT JOIN | All left-table rows; NULLs for unmatched right rows | Include all entities with or without related records |
| RIGHT JOIN | All right-table rows; NULLs for unmatched left rows | Rarely used; rewrite as LEFT JOIN by swapping tables |
| FULL OUTER JOIN | All rows from both tables; NULLs fill both sides | Compare two lists; find records only in one set |

### Finding Records with No Match (Anti-Join Pattern)

```sql
-- Customers who have never placed an order
SELECT c.CUSTOMER_ID, c.FIRST_NAME
FROM CUSTOMERS c
LEFT JOIN ORDERS o ON c.CUSTOMER_ID = o.CUSTOMER_ID
WHERE o.ORDER_ID IS NULL;
```

The LEFT JOIN returns NULL for all ORDERS columns when there is no match. Filtering for `WHERE o.ORDER_ID IS NULL` isolates the customers with no orders.

---

## Section 5 — Window Function Reference

Window functions require an OVER clause. PARTITION BY and ORDER BY within OVER are both optional but critical for controlling behavior.

| Function | Description | Requires ORDER BY in OVER? |
|---|---|---|
| ROW_NUMBER() | Unique sequential integer for each row within partition | Yes |
| RANK() | Rank with gaps after ties (1, 2, 2, 4) | Yes |
| DENSE_RANK() | Rank without gaps after ties (1, 2, 2, 3) | Yes |
| SUM() OVER | Running or partitioned sum | Optional (running total requires ORDER BY) |
| AVG() OVER | Running or partitioned average | Optional |
| LAG(col, n) | Value of col from n rows prior | Yes |
| LEAD(col, n) | Value of col from n rows ahead | Yes |
| NTILE(n) | Divides rows into n equal buckets | Yes |

### Window Function Examples

```sql
-- Rank customers by total spend, highest first
SELECT CUSTOMER_ID,
       SUM(TOTAL_AMOUNT) AS total_spent,
       RANK() OVER (ORDER BY SUM(TOTAL_AMOUNT) DESC) AS spend_rank
FROM ORDERS
GROUP BY CUSTOMER_ID;

-- Running total of daily revenue
SELECT ORDER_DATE,
       TOTAL_AMOUNT,
       SUM(TOTAL_AMOUNT) OVER (ORDER BY ORDER_DATE) AS running_total
FROM ORDERS;

-- Compare each order to the previous order amount for the same customer
SELECT CUSTOMER_ID, ORDER_DATE, TOTAL_AMOUNT,
       LAG(TOTAL_AMOUNT, 1) OVER (
           PARTITION BY CUSTOMER_ID
           ORDER BY ORDER_DATE
       ) AS previous_order_amount
FROM ORDERS;
```

---

## Section 6 — Analytical SQL Query Reference

### Sales by Region with HAVING Filter

```sql
SELECT REGION,
       COUNT(*)            AS order_count,
       SUM(TOTAL_AMOUNT)   AS total_revenue,
       AVG(TOTAL_AMOUNT)   AS avg_order_value
FROM ORDERS
GROUP BY REGION
HAVING SUM(TOTAL_AMOUNT) > 100000
ORDER BY total_revenue DESC;
```

### Year-over-Year Comparison

```sql
SELECT EXTRACT(YEAR FROM ORDER_DATE) AS order_year,
       REGION,
       SUM(TOTAL_AMOUNT) AS annual_revenue
FROM ORDERS
GROUP BY order_year, REGION
ORDER BY order_year, REGION;
```

### Top N Per Group Using Window Function

```sql
WITH ranked_orders AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY REGION
               ORDER BY TOTAL_AMOUNT DESC
           ) AS rn
    FROM ORDERS
)
SELECT REGION, ORDER_ID, TOTAL_AMOUNT
FROM ranked_orders
WHERE rn <= 3;
```

### Monthly Revenue Trend

```sql
SELECT EXTRACT(YEAR FROM ORDER_DATE)  AS yr,
       EXTRACT(MONTH FROM ORDER_DATE) AS mo,
       COUNT(*)                       AS order_count,
       SUM(TOTAL_AMOUNT)              AS monthly_revenue
FROM ORDERS
GROUP BY yr, mo
ORDER BY yr, mo;
```

---

## Section 7 — WHERE vs. HAVING Decision Guide

| Scenario | Use |
|---|---|
| Filter rows before any aggregation | WHERE |
| Filter rows where a column equals a specific value | WHERE |
| Filter groups where an aggregate meets a condition | HAVING |
| Exclude groups with fewer than N records | HAVING COUNT(*) >= N |
| Filter on a date range | WHERE |
| Keep only groups where the sum exceeds a threshold | HAVING SUM(col) > threshold |

Key rule: You cannot use an aggregate function (SUM, COUNT, AVG, etc.) in a WHERE clause. You must use HAVING.

---

## Section 8 — Data+ Exam Tips

1. **WHERE vs. HAVING.** This distinction is guaranteed on the exam. WHERE filters rows before grouping. HAVING filters groups after aggregation. Memorize this.

2. **GROUP BY column rule.** Every non-aggregated column in SELECT must appear in GROUP BY. The exam may show a query with a missing GROUP BY column and ask you to identify the error.

3. **NULL behavior in aggregates.** COUNT(*) counts all rows. COUNT(col) counts non-null values. AVG ignores nulls — the denominator is the non-null count, not total row count.

4. **LEFT JOIN for "include all" scenarios.** When an exam scenario says "list all customers, even those with no orders," the answer involves a LEFT JOIN. INNER JOIN would exclude customers with no orders.

5. **Window functions keep all rows.** GROUP BY collapses rows into one per group. Window functions compute group-level values while keeping every individual row. This is a key conceptual distinction the exam tests.

6. **RANK vs. ROW_NUMBER.** RANK skips ranks after ties: 1, 2, 2, 4. ROW_NUMBER assigns unique integers always: 1, 2, 3, 4. Know which to use when the requirement specifies "no ties allowed."

7. **CTEs improve readability.** The exam may ask you to identify the purpose of a WITH clause. CTEs define named temporary result sets that can be referenced in the main query, improving readability and enabling reuse.

8. **COALESCE for null handling.** When a LEFT JOIN produces NULLs for unmatched rows, COALESCE replaces them with a default value. `COALESCE(o.total, 0)` replaces null totals with zero.

---

## Section 9 — Study Checklist

- [ ] Memorize all vocabulary terms in Section 1
- [ ] Reproduce the SQL execution order table from memory
- [ ] Write a GROUP BY query with at least two aggregate functions
- [ ] Write a query using HAVING to filter aggregate results
- [ ] Write an INNER JOIN and LEFT JOIN on the same two tables and explain the difference in results
- [ ] Write a window function using SUM OVER with ORDER BY for a running total
- [ ] Write a window function using RANK OVER for ranking within a partition
- [ ] Explain the difference between WHERE and HAVING without looking at notes
- [ ] Review all eight exam tips
- [ ] Review official CompTIA Data+ objectives at comptia.org
- [ ] Review Professor Messer's free study materials at professormesser.com
- [ ] Complete Lab 04
- [ ] Complete Quiz 04

---

## Additional Resources

- Official exam objectives: comptia.org (search "Data+ DA0-001 exam objectives")
- Professor Messer's free study guides: professormesser.com

## 9. Supplemental Resources

**1. Mode Analytics SQL Tutorial — Advanced SQL**
<https://mode.com/sql-tutorial/sql-window-functions>
Covers window functions (ROW_NUMBER, RANK, LAG, LEAD, NTILE) with interactive exercises using real datasets. Directly supports the window function section of this module.

**2. Use The Index, Luke — SQL Performance for Developers**
<https://use-the-index-luke.com>
A free, database-agnostic guide to writing efficient SQL queries. Covers index usage, JOIN optimization, and execution plans — essential context for analysts who need to write queries that run on large production datasets.

**3. SQLZoo — Interactive SQL Exercises**
<https://sqlzoo.net>
Browser-based SQL practice covering SELECT, JOIN, GROUP BY, subqueries, and window functions. Immediate feedback with no setup required — ideal for drilling SQL syntax before the lab and quiz.

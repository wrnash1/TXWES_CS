# Quiz: Module 11 — SQL for Data Analytics

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 20 (2 points each)

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 3: Data Analysis

---

## Instructions

Select the single best answer for each question. Each question is worth 2 points. No partial credit.

---

## Question 1

An analyst writes the following query and receives an error. What is wrong?

```sql
SELECT region, SUM(amount) AS total
FROM orders
WHERE SUM(amount) > 100000
GROUP BY region;
```

A. SUM() cannot be used with a GROUP BY clause

B. Aggregate functions cannot appear in a WHERE clause — use HAVING instead

C. The WHERE clause must come after GROUP BY in SQL

D. SUM() requires an ORDER BY clause to function correctly

**Correct Answer:** B — Aggregate functions cannot be used in WHERE because WHERE executes before GROUP BY and the aggregation has not yet occurred. The correct clause for filtering on aggregate results is HAVING, which executes after GROUP BY. Option A is false — SUM is designed for use with GROUP BY. Option C reverses the correct clause order. Option D is false — SUM does not require ORDER BY.

---

## Question 2

Which SQL clause filters rows BEFORE aggregation occurs?

A. HAVING

B. GROUP BY

C. WHERE

D. ORDER BY

**Correct Answer:** C — WHERE filters individual rows before GROUP BY processes them into groups. HAVING filters groups after aggregation (A). GROUP BY performs the grouping itself (B). ORDER BY sorts the final output (D).

---

## Question 3

A table has five rows with the amount column values: `500, 500, 500, 300, 200`. If `RANK() OVER (ORDER BY amount DESC)` is applied, what rank does the row with amount = 300 receive?

A. 2

B. 3

C. 4

D. 5

**Correct Answer:** C — The three rows with amount = 500 all receive rank 1. RANK skips to position 4 (accounting for the three tied rows), so amount = 300 receives rank 4. Option A would be DENSE_RANK's output. Option B would be incorrect by either ranking method. Option D is the row number, not the rank.

---

## Question 4

What is the key behavioral difference between ROW_NUMBER() and DENSE_RANK() when rows have tied values?

A. ROW_NUMBER assigns unique integers (no ties); DENSE_RANK assigns the same value to tied rows with no gaps after the tie

B. ROW_NUMBER assigns the same rank to tied rows; DENSE_RANK skips ranks after a tie

C. ROW_NUMBER and DENSE_RANK produce identical results unless an ORDER BY is specified

D. DENSE_RANK is only available in Oracle SQL; ROW_NUMBER works in all databases

**Correct Answer:** A — ROW_NUMBER always assigns a unique sequential integer — tied rows get different numbers based on arbitrary ordering. DENSE_RANK assigns the same number to tied rows, then continues with the next consecutive integer (no gaps). Option B describes the opposite behavior. Option C is false — they differ whenever ties exist. Option D is false — both are ANSI SQL standard functions.

---

## Question 5

Which window function is best suited for calculating month-over-month revenue change in a time-series dataset?

A. ROW_NUMBER()

B. RANK()

C. LAG()

D. DENSE_RANK()

**Correct Answer:** C — LAG() returns the value from a preceding row in the partition, making it ideal for comparing the current period's value to the prior period's value. ROW_NUMBER (A) and RANK/DENSE_RANK (B, D) are ranking functions and do not access values from other rows.

---

## Question 6

What is the purpose of the PARTITION BY clause inside a window function's OVER() specification?

A. It sorts the rows within the window in ascending order

B. It divides rows into independent groups, with the window function restarting for each group

C. It filters rows to include only those matching the partition condition

D. It limits the number of rows returned by the window function

**Correct Answer:** B — PARTITION BY divides the full dataset into independent partitions, and the window function computes separately within each partition. This is analogous to GROUP BY but without collapsing rows. PARTITION BY does not sort (A), filter (C), or limit (D) rows.

---

## Question 7

A data analyst writes the query below. What does the WITH clause define?

```sql
WITH regional_totals AS (
    SELECT region, SUM(amount) AS total
    FROM orders
    GROUP BY region
)
SELECT region, total
FROM regional_totals
WHERE total > 50000;
```

A. A permanent view stored in the database schema

B. A temporary table stored in the session's tempdb

C. A common table expression that exists only for the duration of this query

D. A stored procedure that can be called by name in future queries

**Correct Answer:** C — The WITH clause defines a Common Table Expression (CTE) — a named, temporary result set that exists only for the duration of the single query in which it is defined. It does not create a permanent view (A), a physical temp table (B), or a reusable stored procedure (D).

---

## Question 8

What distinguishes a correlated subquery from a regular (non-correlated) subquery?

A. A correlated subquery uses JOIN syntax; a regular subquery uses WHERE syntax

B. A correlated subquery references a column from the outer query and executes once for each outer row

C. A correlated subquery can only appear in the FROM clause; a regular subquery can appear in WHERE

D. A correlated subquery always returns multiple rows; a regular subquery always returns one row

**Correct Answer:** B — A correlated subquery references a column from the outer query (using the outer query's table alias), which forces it to re-execute for every row processed by the outer query. A non-correlated subquery executes once and returns a value independent of the outer query. Options A, C, and D all misstate the distinction.

---

## Question 9

An analyst needs to find the top-spending customer in each region. Which approach is most appropriate?

A. Use a simple `GROUP BY region` with `MAX(amount)` to find the top customer per region

B. Use `ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_spend DESC)` and filter where row_num = 1

C. Use `HAVING MAX(amount)` to filter the GROUP BY result to one row per region

D. Use a `LIMIT 1` clause on a query sorted by total_spend

**Correct Answer:** B — `ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_spend DESC)` assigns rank 1 to the top customer within each region independently. Filtering on row_num = 1 then returns exactly one customer per region. Option A with MAX(amount) returns the max amount, not the customer identity. Option C misuses HAVING. Option D with LIMIT 1 returns only one row total, not one per region.

---

## Question 10

In SQL logical execution order, which of the following is the correct sequence?

A. SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY

B. FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

C. FROM → GROUP BY → WHERE → HAVING → SELECT → ORDER BY

D. WHERE → FROM → GROUP BY → SELECT → HAVING → ORDER BY

**Correct Answer:** B — The correct logical execution order is: FROM (identify tables) → JOIN → WHERE (filter rows) → GROUP BY (group rows) → HAVING (filter groups) → SELECT (compute output columns) → ORDER BY (sort output) → LIMIT. Option A incorrectly places SELECT first. Option C incorrectly swaps WHERE and GROUP BY. Option D incorrectly places WHERE before FROM.

---

## Question 11 (5 points)

An analyst wants to calculate a 3-month rolling average of revenue. Which SQL window frame clause achieves this when ordered by month?

A. `ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING`

B. `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`

C. `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`

D. `ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING`

**Correct Answer:** B — `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` includes the current row and the two rows before it — a 3-row (3-month) window ending at the current period. Option A looks forward, not backward. Option C is an expanding cumulative window (all rows from the start). Option D is a centered 3-row window that includes a future row, which is inappropriate for a trailing moving average.

---

## Question 12 (5 points)

A query uses `LEFT JOIN` to combine a `customers` table with an `orders` table. What rows appear in the result for customers who have placed no orders?

A. Those customers are excluded from the result entirely

B. Those customers appear with NULL values in all columns from the `orders` table

C. Those customers appear only if they have at least one cancelled order

D. The query returns an error because a customer without orders violates referential integrity

**Correct Answer:** B — A LEFT JOIN returns all rows from the left table (customers) regardless of whether a match exists in the right table (orders). For unmatched rows, all columns from the right table are populated with NULL. Option A describes an INNER JOIN. Options C and D are incorrect.

---

## Question 13 (5 points)

Which SQL function would you use to replace NULL values in a `discount_rate` column with 0 for display in a report?

A. `ISNULL(discount_rate)`

B. `COALESCE(discount_rate, 0)`

C. `NVL2(discount_rate, 0)`

D. `NULLIF(discount_rate, 0)`

**Correct Answer:** B — `COALESCE(discount_rate, 0)` returns the first non-NULL expression in the list — `discount_rate` if it has a value, otherwise 0. It is ANSI SQL standard and works across databases. `ISNULL()` in some databases requires two arguments (A). `NVL2` returns the second argument when the first is NOT NULL — the reverse of what is needed (C). `NULLIF(discount_rate, 0)` returns NULL when `discount_rate = 0`, which is the opposite of the goal (D).

---

## Question 14 (5 points)

What does the `NTILE(4)` window function do when applied to a column of sales values ordered descending?

A. It returns the 4th highest sales value in the dataset

B. It divides rows into 4 equal-sized buckets (quartiles) and assigns each row a bucket number 1–4

C. It computes the 4th percentile of the sales distribution

D. It returns the running total after every 4th row

**Correct Answer:** B — `NTILE(4)` distributes rows as evenly as possible into 4 groups and assigns each row a group number (1 = top quartile if ordered descending). This is used to create quartile or percentile groupings in SQL. It does not return the 4th value (A), compute percentiles as a scalar (C), or produce running totals (D).

---

## Question 15 (5 points)

An analyst runs the following query but it returns no rows despite the table having records. What is the most likely cause?

```sql
SELECT product_id, category
FROM products
WHERE category = NULL;
```

A. The WHERE clause syntax is correct but the column has no NULL values

B. NULL cannot be compared using `=`; the correct syntax is `IS NULL`

C. The query is missing a GROUP BY clause, which prevents the WHERE filter from executing

D. NULL comparison with `=` returns 1 (true) only for exact string matches

**Correct Answer:** B — In SQL, NULL represents an unknown value. Comparing NULL with `=` always evaluates to UNKNOWN (neither TRUE nor FALSE), so no rows are returned. The correct syntax to find NULL values is `WHERE category IS NULL`. The GROUP BY clause has nothing to do with this issue (C). NULL comparisons never return 1/true (D).

---

## Question 16 (5 points)

A table of 1,000 employee records needs to be joined to a table of 500 department records. Which join type returns only the rows where an employee has a matching department AND the department has at least one employee?

A. LEFT JOIN

B. RIGHT JOIN

C. FULL OUTER JOIN

D. INNER JOIN

**Correct Answer:** D — An INNER JOIN returns only rows where a match exists in both tables. Employees without a department and departments without employees are both excluded. LEFT JOIN includes all employees regardless of match (A). RIGHT JOIN includes all departments regardless of match (B). FULL OUTER JOIN includes all rows from both tables with NULLs for non-matching sides (C).

---

## Question 17 (5 points)

Which window function would you use to calculate the percentage contribution of each order to the total sales for the entire dataset (not partitioned)?

A. `SUM(amount) OVER (PARTITION BY order_id)`

B. `amount / SUM(amount) OVER () * 100`

C. `PERCENT_RANK() OVER (ORDER BY amount)`

D. `CUME_DIST() OVER (ORDER BY amount)`

**Correct Answer:** B — `SUM(amount) OVER ()` with an empty OVER clause computes the grand total across all rows, making it possible to divide each row's amount by that total and multiply by 100. `PARTITION BY order_id` computes a sum per order, not the grand total (A). `PERCENT_RANK()` computes a rank-based relative position between 0 and 1, not a revenue contribution percentage (C). `CUME_DIST()` computes the cumulative distribution of a value, not contribution to total (D).

---

## Question 18 (5 points)

An analyst needs to retrieve all products that appear in the `inventory` table but do NOT appear in the `sales` table. Which approach is correct?

A. `INNER JOIN inventory ON inventory.product_id = sales.product_id WHERE sales.product_id IS NULL`

B. `LEFT JOIN sales ON sales.product_id = inventory.product_id WHERE sales.product_id IS NULL`

C. `RIGHT JOIN inventory ON inventory.product_id = sales.product_id`

D. `FULL OUTER JOIN inventory ON inventory.product_id = sales.product_id WHERE inventory.product_id IS NOT NULL`

**Correct Answer:** B — A LEFT JOIN from `inventory` to `sales` returns all inventory products. Where no matching sales record exists, the `sales.product_id` will be NULL. Filtering on `WHERE sales.product_id IS NULL` isolates products in inventory but not in sales. An INNER JOIN (A) would only return matching products. Right JOIN and FULL OUTER JOIN (C, D) do not correctly isolate inventory-only products.

---

## Question 19 (5 points)

What is the output of the following SQL expression for a row where `unit_price = 100` and `discount = NULL`?

```sql
SELECT unit_price * (1 - discount) AS final_price
```

A. 100

B. 0

C. NULL

D. An error — arithmetic operations cannot include NULL values

**Correct Answer:** C — In SQL, any arithmetic operation involving NULL propagates NULL as the result. `1 - NULL = NULL`, and `100 * NULL = NULL`. This is a common source of unintended NULLs in calculated columns. To handle this correctly, use `COALESCE(discount, 0)`. The result is not 100 (A), 0 (B), or an error (D).

---

## Question 20 (5 points)

A query uses `GROUP BY customer_id, region` and the SELECT clause includes `customer_id, region, COUNT(*) AS order_count`. A colleague suggests adding `product_name` to the SELECT clause without adding it to GROUP BY. What will happen?

A. The query will run successfully and show the most recent product_name for each group

B. The query will return an error because every non-aggregate column in SELECT must appear in GROUP BY

C. The query will run successfully and show the product_name of the first row inserted in each group

D. The database will automatically aggregate product_name as a concatenated string

**Correct Answer:** B — Standard SQL requires that every non-aggregated column in the SELECT clause appear in the GROUP BY clause. Adding `product_name` to SELECT without including it in GROUP BY violates this rule and will cause a syntax or semantic error in most databases (PostgreSQL, MySQL strict mode, SQL Server). Some databases (like MySQL in non-strict mode) allow it but return unpredictable values (C), which is not the correct standard behavior (A and D are both incorrect).

---

End of Module 11 Quiz

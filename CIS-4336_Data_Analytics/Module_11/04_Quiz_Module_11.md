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

End of Module 11 Quiz

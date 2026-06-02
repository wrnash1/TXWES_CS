# Quiz — Module 04: Relational Databases and SQL for Analytics

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 20 (2 points each)
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 2 and Domain 3

---

## Question 1

An analyst writes the following SQL query. Which clause is responsible for excluding individual rows with a TOTAL_AMOUNT below $50 before any grouping occurs?

```sql
SELECT REGION, SUM(TOTAL_AMOUNT) AS total
FROM ORDERS
WHERE TOTAL_AMOUNT >= 50
GROUP BY REGION
HAVING SUM(TOTAL_AMOUNT) > 10000;
```

- A) GROUP BY REGION
- B) HAVING SUM(TOTAL_AMOUNT) > 10000
- C) WHERE TOTAL_AMOUNT >= 50
- D) SELECT REGION

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The WHERE clause filters individual rows before the GROUP BY grouping occurs. In SQL execution order, WHERE runs before GROUP BY. Rows with TOTAL_AMOUNT below $50 are excluded from the dataset before any region grouping or summing happens.
- **Why A is incorrect:** GROUP BY groups the remaining rows after WHERE filtering. It does not itself exclude rows.
- **Why B is incorrect:** HAVING filters groups after aggregation. It excludes regions whose sum is below $10,000 — but only after rows have already been grouped and summed.
- **Why D is incorrect:** SELECT defines which columns to return in the output. It does not filter rows.

---

## Question 2

A data analyst needs to find all product categories where the average order total exceeds $200. Which query is correct?

- A) `SELECT category, AVG(total_amount) FROM orders JOIN products ON orders.product_id = products.product_id WHERE AVG(total_amount) > 200 GROUP BY category;`
- B) `SELECT category, AVG(total_amount) AS avg_total FROM orders JOIN products ON orders.product_id = products.product_id GROUP BY category HAVING AVG(total_amount) > 200;`
- C) `SELECT category, AVG(total_amount) FROM orders GROUP BY category WHERE AVG(total_amount) > 200;`
- D) `SELECT category FROM products HAVING AVG(total_amount) > 200;`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** HAVING is the correct clause for filtering on aggregate results. The query properly joins orders to products, groups by category, and uses HAVING to filter categories where the average order exceeds $200.
- **Why A is incorrect:** Using AVG() in a WHERE clause is a SQL syntax error. WHERE runs before aggregation, so aggregate functions cannot be used in WHERE.
- **Why C is incorrect:** WHERE cannot follow GROUP BY in SQL syntax. WHERE must come before GROUP BY. Additionally, aggregate functions cannot be used in WHERE.
- **Why D is incorrect:** This query references AVG(total_amount) but total_amount is not in the products table and no JOIN is used. The query would fail on missing column reference.

---

## Question 3

What is the difference between COUNT(*) and COUNT(column_name) in SQL?

- A) COUNT(*) counts only non-null rows; COUNT(column_name) counts all rows including nulls
- B) COUNT(*) counts all rows in the group including nulls; COUNT(column_name) counts only non-null values in that column
- C) Both produce identical results in all cases
- D) COUNT(column_name) is the only valid syntax in GROUP BY queries

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** COUNT(*) counts every row in the group, regardless of null values in any column. COUNT(column_name) counts only the rows where that specific column is not null. This distinction matters when a column has missing values.
- **Why A is incorrect:** The description is reversed. COUNT(*) includes all rows; COUNT(col) excludes nulls.
- **Why C is incorrect:** They produce different results when the specified column contains null values. COUNT(*) would count those rows; COUNT(col) would not.
- **Why D is incorrect:** Both COUNT(*) and COUNT(col) are valid in GROUP BY queries. There is no restriction that limits one form to GROUP BY contexts.

---

## Question 4

An analyst wants to list all customers, including those who have never placed an order. Which JOIN type is required?

- A) INNER JOIN, because it returns the most complete data
- B) RIGHT JOIN on the orders table
- C) LEFT JOIN from the customers table to the orders table
- D) FULL OUTER JOIN between customers and orders

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** A LEFT JOIN from CUSTOMERS to ORDERS returns all rows from CUSTOMERS (the left table) and matching rows from ORDERS. Customers with no orders will appear with NULL values for all order columns. An INNER JOIN would exclude those customers.
- **Why A is incorrect:** INNER JOIN returns only rows that have a match in both tables. Customers with no orders would be excluded — the opposite of what is required.
- **Why B is incorrect:** A RIGHT JOIN on the orders table returns all rows from ORDERS plus matching customers. This would return all orders (including any with no customer) but still exclude customers who have no orders.
- **Why D is incorrect:** FULL OUTER JOIN returns all rows from both tables and would include customers with no orders, but it would also include orders with no matching customer. The requirement is specifically "all customers," which LEFT JOIN handles correctly and more precisely.

---

## Question 5

What does a window function with PARTITION BY do differently from a GROUP BY query?

- A) PARTITION BY aggregates data into fewer rows, similar to GROUP BY
- B) PARTITION BY computes group-level aggregate values while keeping all individual rows visible in the output
- C) PARTITION BY is only valid with RANK() and ROW_NUMBER()
- D) PARTITION BY requires a JOIN to work correctly

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** This is the core distinction. GROUP BY collapses rows into one row per group. PARTITION BY within an OVER clause divides data into groups for computation but does not collapse rows — every original row remains in the output with the computed window value attached.
- **Why A is incorrect:** PARTITION BY does not reduce rows. GROUP BY reduces rows. PARTITION BY is the opposite behavior.
- **Why C is incorrect:** PARTITION BY is valid with any window function: SUM, AVG, LAG, LEAD, RANK, ROW_NUMBER, NTILE, and others.
- **Why D is incorrect:** Window functions can operate on a single table query with no JOIN. The PARTITION BY clause references columns within the query's result set, not a separate table.

---

## Question 6

An analyst runs the following query. What will the running_total column contain for the third row when ordered by order_date?

```sql
SELECT order_id, order_date, total_amount,
       SUM(total_amount) OVER (ORDER BY order_date) AS running_total
FROM orders;
```

- A) The total_amount of only the third row
- B) The sum of all rows in the entire orders table
- C) The average of the first three rows' total_amount values
- D) The cumulative sum of total_amount from the first row through the third row, ordered by order_date

**Correct Answer:** D

**Distractor Analysis:**

- **Why D is correct:** SUM() OVER with ORDER BY computes a running (cumulative) total. For the third row, the value equals the sum of total_amount for the first row, second row, and third row ordered by order_date.
- **Why A is incorrect:** The window function computes a cumulative sum, not just the current row's value. The current row's value alone would be total_amount — no window function needed.
- **Why B is incorrect:** The grand total of all rows would appear in every row only if the OVER clause had no ORDER BY. Adding ORDER BY creates a running total that grows incrementally.
- **Why C is incorrect:** The AVG window function would compute an average. SUM computes a sum. These are distinct aggregate operations.

---

## Question 7

A query uses RANK() OVER (ORDER BY total_amount DESC). For a dataset where two customers are tied at $500 (both second highest), what rank values will they receive?

- A) 2 and 3
- B) 2 and 2, with the next customer ranked 3
- C) 2 and 2, with the next customer ranked 4
- D) 1 and 2, because ties are broken alphabetically

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** RANK() assigns the same rank to tied rows and then skips the next rank. Two customers tied for second both receive rank 2, and the next distinct value receives rank 4 (skipping rank 3). This is the defined behavior of RANK().
- **Why A is incorrect:** This describes ROW_NUMBER(), which assigns unique sequential integers without regard to ties.
- **Why B is incorrect:** RANK skips ranks after ties. After two values tied at rank 2, the next rank is 4, not 3. DENSE_RANK would give the next value rank 3.
- **Why D is incorrect:** RANK does not break ties alphabetically. All tied values receive the same rank, regardless of any other column.

---

## Question 8

What is the purpose of a Common Table Expression (CTE) defined with the WITH keyword?

- A) It permanently stores the query results as a new table in the database
- B) It defines a named temporary result set that can be referenced within the same query, improving readability
- C) It creates an index on the specified columns to speed up subsequent queries
- D) It restricts which users can run the query based on database permissions

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** A CTE defines a named temporary result set that exists only for the duration of the query. It can be referenced multiple times within the same query and improves readability over deeply nested subqueries.
- **Why A is incorrect:** A CTE does not persist after the query completes. It is not a table and does not create any permanent database object. CREATE TABLE AS SELECT would persist results.
- **Why C is incorrect:** A CTE has no indexing effect. Indexes are separate database objects created with CREATE INDEX.
- **Why D is incorrect:** CTEs have no security or permission functionality. Database access control is managed through GRANT and REVOKE statements, not CTEs.

---

## Question 9

An analyst wants to find products that have never been ordered. Which query pattern correctly implements this requirement?

- A) `SELECT p.product_id FROM products p INNER JOIN orders o ON p.product_id = o.product_id WHERE o.order_id IS NULL;`
- B) `SELECT p.product_id FROM products p LEFT JOIN orders o ON p.product_id = o.product_id WHERE o.order_id IS NULL;`
- C) `SELECT p.product_id FROM products p WHERE p.product_id NOT IN (SELECT product_id FROM orders) AND orders.order_id IS NULL;`
- D) `SELECT p.product_id FROM products p HAVING COUNT(orders.order_id) = 0;`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** A LEFT JOIN returns all rows from the products table. For products with no matching orders, all order columns are NULL. The WHERE clause `o.order_id IS NULL` then isolates exactly those products — the anti-join pattern.
- **Why A is incorrect:** An INNER JOIN only returns rows that match in both tables. If a product has never been ordered, it will not appear in the INNER JOIN result at all, making the WHERE IS NULL filter pointless — it will never find any rows.
- **Why C is incorrect:** The NOT IN subquery is a valid alternative approach, but the additional `AND orders.order_id IS NULL` references orders without a JOIN, which is a syntax error. A clean NOT IN implementation would not include that second condition.
- **Why D is incorrect:** This query references orders without a JOIN, which would be invalid or return incorrect results. HAVING without GROUP BY applies to the entire table as one group.

---

## Question 10

In SQL, what does the COALESCE function do?

- A) It concatenates two string values together
- B) It returns the first non-null argument from a list of expressions
- C) It converts a NULL column to a numeric data type
- D) It joins two tables on a specified column

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** COALESCE(expr1, expr2, ...) evaluates each argument in order and returns the first one that is not null. It is commonly used to replace null values with a default: `COALESCE(total_amount, 0)` returns total_amount if it is not null, and 0 if it is null.
- **Why A is incorrect:** String concatenation in SQL uses the || operator or CONCAT() function, not COALESCE.
- **Why C is incorrect:** COALESCE returns the first non-null value but does not perform type conversion. CAST() or CONVERT() handle type conversion.
- **Why D is incorrect:** JOIN syntax connects tables; COALESCE operates on column values within a row. They are unrelated operations.

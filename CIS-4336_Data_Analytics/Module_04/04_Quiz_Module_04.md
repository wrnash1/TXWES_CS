# Quiz: Module 04 - Relational Databases and SQL for Analytics
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
What is the primary goal of data normalization in a relational database?
*   A) Compressing files to save disk space
*   B) Reducing data redundancy and improving data integrity by organizing data into related tables
*   C) Creating visual charts from tabular data
*   D) Encrypting sensitive columns to meet compliance requirements
*   **Correct Answer:** B) Normalization splits data into smaller related tables to eliminate redundant duplicates and prevent update, insert, and delete anomalies.
*   **Distractor Analysis:**
    *   *Why correct:* Normalization organizes data into related tables with defined keys to eliminate redundancy and anomalies.
    *   Compression, chart creation, and encryption are separate concerns unrelated to normalization.

---

**Question 2**
In SQL analytics, which of the following most accurately defines **an INNER JOIN**?
*   A) A JOIN that returns all rows from both tables, filling NULLs where there is no match on either side.
*   B) A JOIN that returns only the rows where the join condition matches in both tables, excluding rows that have no corresponding record in the other table.
*   C) A JOIN that returns all rows from the left table and only matching rows from the right table, placing NULLs for right-table columns where no match exists.
*   D) A JOIN that combines tables by stacking their rows vertically rather than linking them by a shared key column.
*   **Correct Answer:** B) A JOIN that returns only the rows where the join condition matches in both tables, excluding rows that have no corresponding record in the other table.
*   **Distractor Analysis:**
    *   *Why B is correct:* INNER JOIN is a filtering join — only matched rows from both tables appear in the result set.
    *   *Why A is incorrect:* Returning all rows from both tables with NULLs for non-matches describes a FULL OUTER JOIN.
    *   *Why C is incorrect:* Returning all rows from the left table with NULLs for the right describes a LEFT JOIN, not an INNER JOIN.
    *   *Why D is incorrect:* Stacking rows vertically describes a UNION operation, not a JOIN.

---

**Question 3**
An analyst needs to find the total sales amount per region, but only wants to see regions where total sales exceed $500,000. Which SQL structure correctly accomplishes this?
*   A) `SELECT region, SUM(sales) FROM orders WHERE SUM(sales) > 500000 GROUP BY region;`
*   B) `SELECT region, SUM(sales) FROM orders GROUP BY region HAVING SUM(sales) > 500000;`
*   C) `SELECT region, SUM(sales) FROM orders GROUP BY region WHERE SUM(sales) > 500000;`
*   D) `SELECT region, COUNT(sales) FROM orders HAVING COUNT(sales) > 500000 WHERE region IS NOT NULL;`
*   **Correct Answer:** B) `SELECT region, SUM(sales) FROM orders GROUP BY region HAVING SUM(sales) > 500000;`
*   **Distractor Analysis:**
    *   *Why B is correct:* HAVING filters groups after aggregation. The correct clause order is FROM → WHERE → GROUP BY → HAVING → SELECT.
    *   *Why A is incorrect:* Aggregate functions like SUM() cannot appear in a WHERE clause — WHERE operates on individual rows before grouping.
    *   *Why C is incorrect:* WHERE must appear before GROUP BY in SQL syntax; placing it after GROUP BY causes a syntax error.
    *   *Why D is incorrect:* COUNT(sales) counts rows, not the total dollar amount, and HAVING cannot precede WHERE in valid SQL.

---

**Question 4**
A query against a 10-million-row `transactions` table with `WHERE customer_id = 12345` is running for 45 seconds. No changes to the data are needed. What is the most effective performance improvement?
*   A) Add a database index on the `customer_id` column so the engine can locate matching rows without a full table scan.
*   B) Rewrite the query to use SELECT * instead of selecting specific columns.
*   C) Increase the database server's RAM and reboot to clear the query cache.
*   D) Convert the transactions table from a relational format to a flat CSV file.
*   **Correct Answer:** A) Add a database index on the `customer_id` column so the engine can locate matching rows without a full table scan.
*   **Distractor Analysis:**
    *   *Why A is correct:* Without an index, the database performs a full sequential scan of all 10 million rows for every query. An index on `customer_id` allows direct lookup, reducing scan time from O(n) to O(log n).
    *   *Why B is incorrect:* SELECT * retrieves more data per row, which typically worsens performance rather than improving it.
    *   *Why C is incorrect:* Adding RAM may help with caching but does not address the root cause of a missing index causing a full table scan.
    *   *Why D is incorrect:* Converting to CSV removes database query capabilities entirely and does not solve the performance problem.

---

**Question 5**
A business analyst runs the query: `SELECT department, COUNT(*) as headcount, AVG(salary) as avg_salary FROM employees GROUP BY department;` The result shows the Marketing department with headcount=15 and avg_salary=72000. What do these values represent?
*   A) There are 15 employees company-wide and the overall average salary is $72,000.
*   B) There are 15 employees in the Marketing department and their average salary is $72,000.
*   C) Marketing has 15 salary records and the maximum salary in Marketing is $72,000.
*   D) The query counts NULL salary values and the result is the median, not the mean.
*   **Correct Answer:** B) There are 15 employees in the Marketing department and their average salary is $72,000.
*   **Distractor Analysis:**
    *   *Why B is correct:* GROUP BY department creates a separate result row for each department. COUNT(*) and AVG(salary) are computed within each group, not across the whole table.
    *   *Why A is incorrect:* The query groups by department, so COUNT(*) and AVG() are per-department values, not company-wide totals.
    *   *Why C is incorrect:* AVG() computes the arithmetic mean, not the maximum. COUNT(*) counts all rows in the group regardless of NULL salary values.
    *   *Why D is incorrect:* AVG() in SQL computes the mean (sum/count of non-null values) and ignores NULLs; it does not compute the median.

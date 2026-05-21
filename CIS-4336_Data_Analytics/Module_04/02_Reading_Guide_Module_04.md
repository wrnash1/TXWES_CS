# Reading Guide: Module 04 - Relational Databases and SQL for Analytics
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

### Introduction
Welcome to **Module 04 - Relational Databases and SQL for Analytics**! SQL is the universal language of data — every data analyst, regardless of their tool stack, must be able to query, filter, join, and aggregate relational data. This module covers the SQL statements and database concepts that appear most frequently on the **CompTIA Data+** exam and in real-world analytics roles.

You will learn how to retrieve data with SELECT, filter it with WHERE, combine tables with JOINs, group and summarize with GROUP BY and aggregate functions, and understand how indexes affect query performance.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **SELECT and WHERE**: SELECT specifies which columns to return from a query; WHERE filters which rows are included based on one or more conditions. Together they form the most fundamental query pattern in SQL. The Data+ exam tests your ability to read a SQL statement and predict its output.
*   **JOIN types (INNER, LEFT, RIGHT)**: An INNER JOIN returns only rows where the join condition matches in both tables. A LEFT JOIN returns all rows from the left table and matching rows from the right — unmatched right-table rows appear as NULL. A RIGHT JOIN is the mirror image. Understanding which rows are included or excluded by each join type is a frequent exam topic.
*   **GROUP BY and HAVING**: GROUP BY collapses rows that share the same value in one or more columns into a single summary row. Aggregate functions (COUNT, SUM, AVG, MIN, MAX) are then applied to each group. HAVING filters the resulting groups — it is the equivalent of WHERE but operates after aggregation, not before.
*   **Aggregation functions**: COUNT() counts rows (or non-null values in a column), SUM() adds numeric values, AVG() computes the arithmetic mean, MIN() and MAX() return the smallest and largest values. These functions are central to every analytics SQL query.
*   **Indexes**: A database index is a data structure (typically a B-tree) that allows the database engine to locate rows matching a condition without scanning every row in the table. Indexes dramatically speed up SELECT queries with WHERE clauses on indexed columns but add overhead to INSERT, UPDATE, and DELETE operations.

---

### 2. Certification Exam Tips
*   **Domain weight:** SQL and relational database concepts appear across multiple Data+ domains. Data Mining (Domain 3, ~23%) heavily tests SELECT, JOIN, GROUP BY, and HAVING in scenario questions.
*   **Exam trap — WHERE vs. HAVING:** This is one of the most commonly tested distinctions. WHERE filters individual rows before grouping; HAVING filters groups after aggregation. If a question asks you to "show only departments with more than 10 employees," the answer requires HAVING COUNT(*) > 10, not WHERE.
*   **Exam trap — INNER vs. LEFT JOIN:** When a scenario says "show all customers including those who have never placed an order," the answer is a LEFT JOIN from Customers to Orders, not INNER JOIN. INNER JOIN would exclude customers with no orders.
*   **Exam trap — COUNT(*) vs. COUNT(column):** COUNT(*) counts all rows including NULLs. COUNT(column_name) counts only non-null values in that column. The exam uses this distinction in scenario-based aggregation questions.
*   **Study Resource:** The SQL chapters of [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/) cover database querying with worked examples. The [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) covers SQL integration with Pandas for end-to-end analytics workflows.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the relational databases and SQL chapters in the OER Textbook: [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/). Focus on SELECT, JOIN, GROUP BY, and aggregation function examples.
*   **Required Video:** Watch the database query sections of the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238), which demonstrates how SQL queries connect to Python-based analytics pipelines.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Write a SQL query using SELECT, WHERE, and ORDER BY**: Retrieve student records with a grade of 90 or higher, sorted descending by grade.
*   **Write a query joining students and courses tables**: Use an INNER JOIN to list every student with their enrolled course name, and then modify it to a LEFT JOIN to include students not yet enrolled in any course.
*   **Group results by course and calculate average grade**: Use GROUP BY on the course column and AVG() on the grade column, then use HAVING to show only courses with an average above 75.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the SQL and relational database chapters in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/).
- [ ] Watch the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238).
- [ ] Review the lab instructions and understand what each task requires.
- [ ] Proceed to the weekly hands-on lab activity.

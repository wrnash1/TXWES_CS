# Discussion — Module 04: Relational Databases and SQL for Analytics

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 10 (6 initial post + 4 peer responses)

---

## Overview

This discussion asks you to reason about SQL design choices and interpret query results in business contexts. Choose one of the three scenarios below. Write an initial post of 175–225 words, then respond to at least two classmates by Sunday at 11:59 PM.

Professor Nash's note: Strong posts go beyond syntax — they connect SQL design decisions to business context. A technically correct answer that ignores the business meaning of the result is incomplete.

---

## Scenario A — WHERE vs. HAVING Design Decision

A retail analytics team is writing a query to find all product categories with strong sales performance. One team member writes a WHERE clause to filter categories; another insists HAVING is needed. A third team member is unsure of the difference and proposes using both WHERE and HAVING in the same query.

The final query needs to: (1) exclude all orders under $25 from the analysis (individual row filter), and (2) return only categories where the remaining orders sum to more than $5,000 (group filter).

In 175–225 words, address all three of the following:

1. Write the correct SQL query for this requirement. Use a fictional table named ORDERS with columns: order_id, category, total_amount. Show the query in a code block.
2. Explain in plain language why both WHERE and HAVING are needed in this specific query — what would happen if you used only WHERE, and what would happen if you used only HAVING?
3. A colleague argues that using a subquery instead of HAVING would produce the same result and is easier to understand. Do you agree? Briefly describe the subquery approach and compare its readability to the HAVING approach.

---

## Scenario B — JOIN Type Selection

A hospital analytics team needs to produce two reports from the same two tables: PATIENTS (patient_id, name, department, admitted_date) and LAB_RESULTS (result_id, patient_id, test_name, result_value, test_date).

Report 1: A list of all patients along with the count of lab results each patient has had. Patients with no lab results should appear in the report with a count of 0.

Report 2: A list of all lab results that have no matching patient record (orphaned records that indicate a data quality issue).

In 175–225 words, address all three of the following:

1. State which JOIN type is needed for each report and explain why the other JOIN types would produce incorrect results.
2. Write the SQL for Report 1. Show the query in a code block. Include the JOIN, GROUP BY, and any null-handling needed to show 0 for patients with no results.
3. Write the SQL for Report 2. Show the query in a code block. Explain what a referential integrity constraint would have prevented this data quality issue from occurring in the first place.

---

## Scenario C — Window Functions vs. GROUP BY

A sales manager asks an analyst for two outputs from the same ORDERS table (columns: order_id, salesperson_id, region, order_date, total_amount):

Output 1: A summary table showing each salesperson's total revenue for the year — one row per salesperson.

Output 2: A detailed table showing every individual order, with an additional column showing that salesperson's cumulative revenue up to and including that order's date.

In 175–225 words, address all three of the following:

1. Explain why Output 1 requires GROUP BY and Output 2 requires a window function. Why can't you use GROUP BY for Output 2?
2. Write the SQL for Output 2. Show the query in a code block. Use SUM() OVER with PARTITION BY salesperson_id and ORDER BY order_date.
3. The sales manager then asks for a third output: for each region, identify the top-3 orders by total_amount using ROW_NUMBER. Write that SQL query in a code block and explain what happens if two orders in the same region have an identical total_amount — does ROW_NUMBER or RANK behave better for this use case, and why?

---

## Discussion Rubric

### Initial Post — 6 Points

| Score | Criteria |
|---|---|
| 6 | Addresses all three questions. SQL code blocks are correct and functional. Reasoning connects syntax to business meaning. Within 175–225 words. |
| 4–5 | Addresses most questions. SQL has minor errors or reasoning lacks business context on one item. |
| 2–3 | SQL contains significant errors or only one to two questions are answered. |
| 0–1 | Post is missing, too brief, or does not engage with the scenario. |

### Peer Responses — 4 Points

| Score | Criteria |
|---|---|
| 4 | Responds to at least two classmates with substantive technical feedback — identifies a SQL error, suggests an optimization, or extends the analysis. Minimum 60 words per response. |
| 2–3 | Responses are mostly agreement or restatement. Only one substantive response provided. |
| 0–1 | Only one response submitted or responses are too brief. |

---

## Deadlines

- Initial post: Wednesday at 11:59 PM
- Peer responses: Sunday at 11:59 PM

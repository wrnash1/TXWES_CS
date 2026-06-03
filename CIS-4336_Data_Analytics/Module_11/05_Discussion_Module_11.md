# Discussion: Module 11 — SQL for Data Analytics

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 10 (6 initial post + 4 peer responses)

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 3: Data Analysis

---

## Instructions

Choose ONE of the three scenarios below and write an initial post of 175–225 words. Then respond substantively to at least TWO classmates who chose different scenarios. Peer responses must be at least 75 words — extend the analysis, identify an error in the SQL logic, or propose a more efficient approach.

Initial posts are due by Thursday at 11:59 PM. Peer responses are due by Sunday at 11:59 PM.

---

## Scenario A: The Sales Performance Report

A regional sales director at a distribution company asks for a report that answers the following questions simultaneously:

- Which sales representatives had total revenue above $500,000 in 2024?
- For those representatives, what was their revenue in each quarter?
- How did each quarter compare to the prior quarter (was it up or down)?

The database has a single `orders` table with columns: `order_id`, `sales_rep`, `order_date`, `amount`, `region`, `customer_id`.

In your initial post, address the following:

- Write the SQL query (or series of queries using CTEs) that would answer all three questions. Use at least one CTE, the HAVING clause, and the LAG() window function. Explain your query design in 3–5 sentences — do not just paste code; explain what each CTE or section does.
- The sales director also asks: "Show me the ranking of each rep's quarterly revenue within their region." Which window function would you add, and where in your query structure would it go? Write the additional window function expression (not the full query) and explain why you chose RANK vs. DENSE_RANK vs. ROW_NUMBER for this specific use case.
- One of your colleagues suggests using a subquery instead of CTEs for this query. What is your counterargument? Identify at least one specific readability or maintainability advantage of the CTE approach for this particular query.

---

## Scenario B: The Customer Segmentation Query

An e-commerce analytics team needs to classify customers into behavior tiers based on their total spending and order frequency over the past 12 months. The business rules are:

- Platinum: total spend >= $10,000 AND order count >= 12
- Gold: total spend >= $5,000 AND order count >= 6
- Silver: total spend >= $1,000 AND order count >= 3
- Bronze: all other customers with at least one order

The database has two tables: `orders` (`order_id`, `customer_id`, `order_date`, `amount`) and `customers` (`customer_id`, `customer_name`, `email`).

In your initial post, address the following:

- Write a CTE-based SQL query that calculates each customer's total spend and order count for the past 12 months, then assigns the correct tier using a CASE expression. Include the customer_name and email from the customers table. Walk through your query logic in 3–5 sentences.
- After assigning tiers, the marketing team wants to see the top 5 customers by total spend within each tier. Describe how you would extend your existing CTE query to add this ranking. Write the window function expression that would accomplish this, and explain which ranking function you would choose and why.
- The query must also handle customers who made purchases in prior years but have no orders in the past 12 months. These customers should not appear in the tier report. How does your WHERE clause ensure this? Would you use a subquery, a date filter in the WHERE clause, or a JOIN condition? Justify your choice.

---

## Scenario C: The Inventory Trend Analysis

A supply chain analyst at a manufacturing company wants to use SQL to analyze part inventory movement over time. The database has an `inventory_events` table with columns: `event_id`, `part_id`, `part_name`, `event_date`, `event_type` (RECEIPT or ISSUE), `quantity`. RECEIPTs add to stock; ISSUEs subtract from stock.

The analyst needs to:

- Calculate the running net inventory balance for each part over time
- Flag any dates where the running balance drops below zero (stockout events)
- Find the top 3 parts by total receipts in the last 90 days

In your initial post, address the following:

- Describe the SQL approach for calculating a running net inventory balance. Would you use a window function with a frame clause, a CTE with self-join, or a correlated subquery? Write the core SQL expression (not the full query, but the key SELECT clause logic) and explain your choice.
- To flag stockout events (balance < 0), would you add a HAVING clause, a WHERE clause on a derived table, or a CASE expression in the SELECT? Explain your reasoning with reference to SQL logical execution order — which approach executes at the right time in the query lifecycle?
- For the "top 3 parts by receipts in last 90 days" requirement, write a CTE-based query using `ROW_NUMBER()` that returns exactly 3 rows — even if multiple parts are tied. Then explain: if the business changes the requirement to "top 3 with ties included," which function would you swap in and why?

---

## Peer Response Guidelines

When responding to classmates, consider:

- Is their SQL logic correct? If you spot an error (wrong clause, wrong function, wrong execution order), explain it clearly without being dismissive.
- Is there a simpler or more efficient approach to the same analytical problem?
- Did they correctly explain WHY they chose one SQL feature over another, or did they just describe what the code does?
- Can you extend their query to answer an additional business question not covered in their post?

---

## Grading Rubric (10 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| SQL correctness | 3 | Query logic is syntactically and logically correct for the stated requirement |
| Feature selection justification | 2 | Explains why specific SQL features were chosen over alternatives |
| Business reasoning | 2 | Connects SQL design decisions to the business problem, not just the technical specification |
| Peer response quality | 2 | Substantive engagement; identifies an improvement, catches an error, or extends the analysis |
| Writing clarity | 1 | Clear explanation of query logic; within word count |

---

## Professor Nash Note

Writing SQL for a technical interview or a real job is different from solving a homework problem. The interviewer does not just want correct code — they want to understand how you think. Can you explain why you used DENSE_RANK instead of ROW_NUMBER? Can you articulate why CTEs are better than nested subqueries for this specific query? Can you anticipate edge cases like NULL values or customers with no recent orders? That is the level of reasoning this discussion is designed to build. Practice explaining your SQL decisions in plain English — that skill is as valuable as the SQL itself.

---

End of Module 11 Discussion

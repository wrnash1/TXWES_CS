# Discussion Forum: Module 12 — Python for Data Analysis

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Overview

This discussion asks you to apply Python data analysis concepts to real-world professional scenarios. Choose one of the three scenarios below, write an original post of 175–225 words, then respond to at least two classmates who chose different scenarios from yours. Responses must be 75–100 words and add new reasoning rather than simply agreeing.

---

### Scenario A — The Null Value Decision

A regional retail chain gives you a sales dataset covering 18 months. The `units_sold` column is null for roughly 22% of rows. Your manager says to fill all nulls with zero before running the quarterly revenue report. A colleague argues that 22% missing is too high and the column should be dropped entirely.

Write a post that explains how you would evaluate which approach is correct. Address the following in your response:

* What questions would you ask about why the data is missing?
* What is the risk of filling with zero versus dropping the column?
* How would the choice affect the quarterly revenue calculations?
* What pandas methods would you use to investigate and implement your chosen strategy?

---

### Scenario B — Outlier Judgment Call

You are analyzing customer transaction data for a subscription software company. After running the IQR method on the `contract_value` column, you flag 340 transactions as outliers — all on the high end. A senior analyst tells you to remove them before building the executive dashboard.

Write a post that argues for or against removing those outliers. Address the following:

* What additional context would you need before deciding?
* How does the business context (enterprise software contracts) affect the outlier decision?
* What visualization would you produce to support your argument?
* What is the risk of removing legitimate high-value contracts from an executive dashboard?

---

### Scenario C — Choosing the Right Aggregation

A marketing analyst asks you to produce a single table showing total revenue, average order value, and order count broken down by both region and product category. She needs the result in a format she can paste directly into a PowerPoint slide as a clean matrix.

Write a post that explains which pandas operation you would use and why. Address the following:

* Would you use `groupby().agg()` or `pivot_table()`? Why?
* What would the output structure look like?
* How would `fill_value=0` affect the result and why does it matter for the presentation?
* What one seaborn chart would you pair with this table to make the matrix visually actionable?

---

### Peer Response Requirements

Respond to at least two classmates who chose different scenarios. Each response must:

* Be 75–100 words
* Identify one specific point you agree with and explain why
* Raise one question or alternative perspective the original poster did not consider
* Reference a specific pandas, NumPy, or seaborn function by name

---

### Grading Rubric (10 points total)

| Criterion | Points |
|---|---|
| Original post addresses all four required points | 4 |
| Original post demonstrates accurate technical knowledge of Python tools | 2 |
| Original post is 175–225 words and professionally written | 1 |
| Peer response 1 meets length, adds new reasoning, names a function | 1.5 |
| Peer response 2 meets length, adds new reasoning, names a function | 1.5 |
| **Total** | **10** |

---

### Submission Deadline

Initial post due by Thursday 11:59 PM. Peer responses due by Sunday 11:59 PM of the same week. Late initial posts receive a 20% deduction per day. Peer responses submitted after the Sunday deadline receive zero credit for that component.

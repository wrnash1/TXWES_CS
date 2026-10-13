# Discussion: Module 12 — BigQuery and Data Analytics

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This discussion asks you to design a BigQuery cost optimization strategy for a realistic
data warehouse scenario. You will apply partitioning, clustering, and cost estimation
concepts from Module 12.

**Initial post due**: Thursday at 11:59 PM Central

**Peer responses due**: Sunday at 11:59 PM Central

---

### Scenario

A retail company called TrendMart has migrated its data warehouse to BigQuery. Their
main fact table `transactions` contains 3 years of retail data (approximately 800 GB)
with these columns:

- `transaction_id` (INTEGER)
- `transaction_date` (DATE)
- `store_id` (INTEGER)
- `product_id` (INTEGER)
- `product_category` (STRING) — 12 distinct values
- `customer_id` (INTEGER) — millions of unique customers
- `quantity` (INTEGER)
- `unit_price` (FLOAT)
- `total_amount` (FLOAT)

The analytics team runs these query patterns daily:

- Pattern A: Filter by `transaction_date` range (last 30, 90, or 365 days)
- Pattern B: Filter by `transaction_date` range AND `product_category`
- Pattern C: Aggregate revenue by `product_category` for a given month
- Pattern D: Look up all transactions for a specific `customer_id` (rare, ad-hoc)

Currently the table has no partitioning or clustering. The team spends approximately
$800 per month on BigQuery query costs.

---

### Response Requirements

#### Part 1: Partitioning and Clustering Strategy

Recommend a partitioning and clustering configuration for the `transactions` table.
Specify which column to partition on, which columns to cluster on, and in what order.
Explain in 3–4 sentences how your configuration reduces query cost for each of the four
query patterns.

#### Part 2: Cost Estimation Approach

Describe the step-by-step process the team should use to estimate the cost reduction
from your optimization. What tool or flag would they use, and what specifically would
they measure before and after? Limit to 3–4 sentences.

#### Part 3: Data Sharing Requirement

The finance team in a separate GCP project needs to analyze `total_amount` and
`transaction_date` but must not see `customer_id` or `product_id`. The finance team
should always query live data, not a copy. Describe the specific BigQuery feature you
would use and explain the two steps required to make it work. Limit to 3–4 sentences.

#### Part 4: Reflection

Describe a data analysis task you have performed in any tool (Excel, SQL, Python,
Tableau, etc.). What made the analysis time-consuming or expensive? How might BigQuery's
features have helped? (3–5 sentences; hypothetical scenarios are acceptable.)

---

### Grading Criteria

| Criterion | Points |
|---|---|
| Part 1: Correct partitioning and clustering with justification for all 4 patterns | 35 |
| Part 2: Correct cost estimation approach using dry\_run | 20 |
| Part 3: Correct use of authorized view with both required steps | 25 |
| Part 4: Thoughtful reflection | 5 |
| Peer response 1: Substantive technical engagement | 7 |
| Peer response 2: Substantive technical engagement | 8 |
| **Total** | **100** |

---

### Peer Response Guidelines

A substantive peer response does at least one of the following:

- Challenges the clustering column choice with a technical counter-argument
- Points out a query pattern the original poster's strategy does not optimize well
- Suggests an additional optimization (materialized views, column selection, caching)
- Raises a consideration about authorized view configuration that is often missed

---

### Discussion Hints

For Part 1, clustering benefits queries most when the clustered column appears in the
WHERE clause and has high cardinality within a partition. Product category has only 12
distinct values — consider whether that is a better or worse clustering candidate than
customer\_id for the patterns listed.

For Part 2, the correct tool is `--dry_run`. Run a representative query with `--dry_run`
on the current table, record the bytes estimate, then repeat on the new table to compare.

For Part 3, the authorized view requires two steps: creating the view with the correct
column filter, then authorizing the view to access the source dataset. Both steps are
required or the view will fail with a permission error.

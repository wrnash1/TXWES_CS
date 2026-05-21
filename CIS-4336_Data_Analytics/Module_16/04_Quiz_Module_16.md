# Quiz: Module 16 - Final Exam Prep & CompTIA Data+ DA0-001 Certification
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
A data analyst runs an A/B test on a new product page. The result is p = 0.04 with a pre-set significance level of alpha = 0.05. A colleague says, "There is only a 4% chance the null hypothesis is true." Is this interpretation correct, and why?
*   A) Yes — p = 0.04 means the probability that the null hypothesis is true is 4%, confirming the new page works better.
*   B) No — the p-value is not the probability that H₀ is true. It is the probability of observing data this extreme (or more extreme) assuming H₀ is true. The correct conclusion is to reject H₀ because p < alpha.
*   C) No — a p-value of 0.04 is below 0.05 but so close to the threshold that no conclusion can be drawn and the test should be repeated with a larger sample.
*   D) Yes — a p-value below 0.05 always means the null hypothesis is false with 96% certainty.
*   **Correct Answer:** B) No — the p-value is not the probability that H₀ is true. It is the probability of observing data this extreme (or more extreme) assuming H₀ is true. The correct conclusion is to reject H₀ because p < alpha.
*   **Distractor Analysis:**
    *   *Why correct:* The p-value is a conditional probability: P(data this extreme | H₀ is true). It is not the probability that H₀ is true. When p < alpha, the correct decision is to reject H₀ — the result is statistically significant. This is the most common exam trap on the Data+ certification.
    *   A) Stating p = 0.04 means H₀ is 4% likely is the classic p-value misinterpretation. C) p = 0.04 is clearly below alpha = 0.05 — the decision rule is met and H₀ is rejected. "Too close" is not a valid statistical concept here. D) Rejecting H₀ does not mean it is false with 96% certainty — statistical significance is a decision rule under uncertainty, not a proof of truth.

---

**Question 2**
An analyst is reviewing a dataset of 50,000 customer records. The `email` column contains values like "john.doe@" (missing domain) and "N/A". The `phone` column has values like "555-ABC-1234" (non-numeric characters). Which data quality dimensions are most directly violated?
*   A) Completeness (email) and accuracy (phone) — the email field is incomplete and the phone value is wrong.
*   B) Validity (email) and validity (phone) — both columns contain values that fail to conform to their required format rules.
*   C) Consistency (email) and uniqueness (phone) — the email disagrees with another system and the phone appears multiple times.
*   D) Accuracy (email) and completeness (phone) — the email value is incorrect and the phone field is missing data.
*   **Correct Answer:** B) Validity (email) and validity (phone) — both columns contain values that fail to conform to their required format rules.
*   **Distractor Analysis:**
    *   *Why B is correct:* Validity measures whether values conform to defined format rules and allowable values. "john.doe@" fails the required email format (missing domain). "555-ABC-1234" fails the required phone format (non-numeric characters). Both are format violations — the defining characteristic of a validity problem.
    *   *Why A is incorrect:* Completeness applies when a required field is null or absent — not when it contains a malformed value. "john.doe@" is present but malformed; that is validity, not completeness. Phone "555-ABC-1234" is present but formatted incorrectly — also validity.
    *   *Why C is incorrect:* Consistency requires comparing the same field across two systems for conflicting values. No cross-system comparison is described. Uniqueness applies to duplicate entity records, not format issues.
    *   *Why D is incorrect:* Accuracy means the value is present but factually incorrect (e.g., a wrong birth date). A malformed email is a format violation (validity), not a factual error. The phone field is present — it is not missing (completeness).

---

**Question 3**
In the following SQL query, which clause is in the wrong position and would cause a syntax error?

`SELECT department, AVG(salary) FROM employees WHERE AVG(salary) > 60000 GROUP BY department;`
*   A) The SELECT clause — AVG(salary) cannot appear in SELECT without a GROUP BY.
*   B) The WHERE clause — aggregate functions like AVG() cannot be used in WHERE. The filter on the aggregate must use HAVING, placed after GROUP BY.
*   C) The GROUP BY clause — department cannot be used in GROUP BY if it also appears in SELECT.
*   D) The FROM clause — the employees table must be aliased before being used with AVG().
*   **Correct Answer:** B) The WHERE clause — aggregate functions like AVG() cannot be used in WHERE. The filter on the aggregate must use HAVING, placed after GROUP BY.
*   **Distractor Analysis:**
    *   *Why B is correct:* WHERE operates on individual rows before any grouping occurs — at that stage, aggregate values do not yet exist. Filtering on an aggregate requires HAVING, which executes after GROUP BY. The correct query is: `SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 60000;`
    *   *Why A is incorrect:* AVG(salary) can appear in SELECT when used with GROUP BY. The SELECT clause is syntactically correct.
    *   *Why C is incorrect:* A column used in GROUP BY can also appear in SELECT — that is a standard and required pattern for grouped aggregation queries.
    *   *Why D is incorrect:* Table aliases are optional and have nothing to do with using aggregate functions. The employees table does not need an alias to support AVG().

---

**Question 4**
A business analyst needs to show a non-technical executive how monthly customer acquisition cost (CAC) has changed over the past 18 months, and whether the trend is increasing or decreasing. Which combination of choices is most appropriate?
*   A) A pie chart showing each month's share of total 18-month CAC spend, with a slide title reading "Chart 4: Customer Acquisition Cost Data."
*   B) A line chart showing CAC on the y-axis and month on the x-axis, with a descriptive title stating the trend direction (e.g., "CAC Has Increased 22% Over 18 Months") and an annotation marking the inflection point.
*   C) A box-and-whisker plot comparing the distribution of CAC values across the 18 months, highlighting outlier months.
*   D) A scatter plot with month number on the x-axis and CAC on the y-axis to show whether a correlation exists between time and cost.
*   **Correct Answer:** B) A line chart showing CAC on the y-axis and month on the x-axis, with a descriptive title stating the trend direction (e.g., "CAC Has Increased 22% Over 18 Months") and an annotation marking the inflection point.
*   **Distractor Analysis:**
    *   *Why B is correct:* The question asks for two things: the right chart type for a trend over time, and appropriate communication for an executive audience. Line charts are the standard choice for time-series trends. A title that states the finding (not just "Chart 4") and an annotation on the inflection point deliver the insight immediately without requiring the viewer to interpret the chart themselves.
    *   *Why A is incorrect:* A pie chart shows part-to-whole proportions at a single point in time. It cannot show a trend across 18 months. A neutral title ("Chart 4") forces the executive to do the interpretive work.
    *   *Why C is incorrect:* A box plot shows distribution and spread across a set of values — it answers "how variable is CAC?" not "is CAC trending up or down?" It would not clearly convey directional change over time.
    *   *Why D is incorrect:* A scatter plot reveals correlation between two independent numeric variables. Month is not an independent variable here — it is a time sequence. A line chart connecting sequential data points is the correct choice for ordered time-series data.

---

**Question 5**
A data team is building a pipeline that extracts raw customer clickstream data from an API, loads it into Google Cloud Storage as JSON files, and then uses BigQuery SQL to transform and aggregate it into a clean reporting table. Which pipeline pattern does this describe, and what is its primary advantage?
*   A) ETL — the data is extracted, transformed in a staging server, and then loaded into the warehouse. The advantage is that only clean data enters the target system.
*   B) ELT — raw data is extracted and loaded first, then transformed inside the cloud platform using its elastic compute. The advantage is that raw data is preserved for reprocessing and transformation leverages the platform's scalable SQL engine.
*   C) CDC — only changed records from the API are captured and incrementally loaded to reduce pipeline latency. The advantage is near-real-time data freshness.
*   D) MPP — the transformation is distributed across hundreds of parallel processors simultaneously. The advantage is that query execution is faster than a single-node database.
*   **Correct Answer:** B) ELT — raw data is extracted and loaded first, then transformed inside the cloud platform using its elastic compute. The advantage is that raw data is preserved for reprocessing and transformation leverages the platform's scalable SQL engine.
*   **Distractor Analysis:**
    *   *Why B is correct:* The pipeline sequence is: extract from API → load to Cloud Storage (raw) → transform with BigQuery SQL. This is ELT by definition — Load precedes Transform. The key advantages of ELT on cloud platforms are preservation of raw data (enabling future reprocessing with different logic) and use of the warehouse's elastic compute for transformation rather than an external staging server.
    *   *Why A is incorrect:* ETL transforms data before loading it into the target. In this pipeline, raw JSON is loaded into Cloud Storage first — no transformation occurs before load. The sequence does not match ETL.
    *   *Why C is incorrect:* CDC (Change Data Capture) is an extraction strategy that captures only rows that have changed since the last pipeline run. The scenario describes a full-load pipeline pattern from an API, not an incremental change-capture mechanism.
    *   *Why D is incorrect:* MPP (Massively Parallel Processing) describes a hardware and execution architecture used by systems like BigQuery internally. It is not a pipeline pattern name and does not describe the sequence of extract, load, and transform operations.

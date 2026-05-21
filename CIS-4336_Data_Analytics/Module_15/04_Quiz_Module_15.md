# Quiz: Module 15 - Analytics in Business – Use Cases and KPIs
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
A subscription software company wants to measure whether it is retaining customers effectively. The operations team proposes tracking "number of support tickets closed per day" as the primary KPI for customer retention. Why is this metric a poor choice for a retention KPI?
*   A) Support tickets closed is a quantitative metric, and KPIs must be qualitative.
*   B) Support ticket closure rate is an operational efficiency metric, not directly linked to the strategic goal of customer retention — it does not measure whether customers stay or leave.
*   C) KPIs must be expressed as percentages, and support tickets are counted in whole numbers.
*   D) This metric requires real-time data, which is too expensive to collect for a KPI dashboard.
*   **Correct Answer:** B) Support ticket closure rate is an operational efficiency metric, not directly linked to the strategic goal of customer retention — it does not measure whether customers stay or leave.
*   **Distractor Analysis:**
    *   *Why correct:* A KPI must be directly tied to a strategic objective. Customer retention is measured by whether customers renew, not by how fast tickets are closed. A KPI for retention should be churn rate, renewal rate, or net revenue retention — metrics that directly reflect whether customers are staying.
    *   A) KPIs can be quantitative or qualitative counts — there is no rule requiring them to be qualitative. C) KPIs can use any unit — counts, percentages, dollar values, or ratios. D) Data collection cost is a practical consideration, not the reason this metric fails as a retention KPI. The conceptual mismatch between the metric and the goal is the core problem.

---

**Question 2**
In business analytics, which of the following most accurately defines a **leading indicator**?
*   A) A metric that measures the outcome of a completed business period — such as last quarter's revenue or last month's customer churn rate — confirming what happened but offering no ability to change it.
*   B) A metric that measures current activity or input that is predictive of a future business outcome — such as the number of sales demos scheduled this week as a predictor of next quarter's closed deals.
*   C) A metric that ranks the performance of individual employees or teams relative to each other, used to identify top and bottom performers for management review.
*   D) A financial ratio calculated by dividing net profit by total revenue, used to assess how efficiently a company converts sales into profit.
*   **Correct Answer:** B) A metric that measures current activity or input that is predictive of a future business outcome — such as the number of sales demos scheduled this week as a predictor of next quarter's closed deals.
*   **Distractor Analysis:**
    *   *Why B is correct:* Leading indicators are forward-looking — they measure inputs or activities that influence future results. Their value is that they allow intervention: if demo counts are low this week, a manager can act now rather than waiting for next quarter's revenue to confirm the problem.
    *   *Why A is incorrect:* A metric measuring a completed period's outcome describes a lagging indicator. Lagging indicators confirm results but cannot be changed after the fact.
    *   *Why C is incorrect:* Ranking employees relative to each other describes a performance benchmarking or ranking metric — not the distinction between leading and lagging indicators.
    *   *Why D is incorrect:* Net profit divided by revenue describes profit margin — a specific financial ratio and a lagging indicator. It measures past efficiency, not a forward-looking predictor.

---

**Question 3**
A product team launches a new onboarding experience in March. They want to know whether customers who started in March retained at higher rates after 90 days compared to customers who started in January (who used the old onboarding). Which analytical technique best answers this question?
*   A) Trend analysis — plotting the overall 90-day retention rate as a single line across all months to see if it is increasing.
*   B) Cohort analysis — grouping January customers and March customers into separate cohorts and comparing their 90-day retention rates independently.
*   C) Regression analysis — building a model that predicts 90-day retention based on the month of acquisition as a continuous variable.
*   D) Descriptive statistics — computing the mean and standard deviation of retention rates across all customers to identify outliers.
*   **Correct Answer:** B) Cohort analysis — grouping January customers and March customers into separate cohorts and comparing their 90-day retention rates independently.
*   **Distractor Analysis:**
    *   *Why B is correct:* Cohort analysis isolates groups by a shared start characteristic (acquisition month) and tracks them independently over time. Comparing January vs. March cohorts at 90 days controls for the time variable, making the onboarding change the most plausible explanation for any observed difference.
    *   *Why A is incorrect:* Trend analysis plots a single aggregated metric over time, blending all customer cohorts together. If March customers have higher retention but are only a small portion of total customers, the trend line would barely move — obscuring the cohort-level insight.
    *   *Why C is incorrect:* Regression would predict a continuous retention probability, but the question asks for a direct comparison between two specific groups. Cohort analysis is the more direct and interpretable approach for this business question.
    *   *Why D is incorrect:* Descriptive statistics summarize the distribution of retention across all customers. Computing overall mean and standard deviation merges all cohorts and cannot answer whether a specific onboarding change improved retention for a specific group.

---

**Question 4**
A marketing team spent $80,000 on an email campaign that generated $200,000 in new revenue. Using the standard ROI formula `ROI = (Net Gain / Cost) × 100%`, what is the campaign's ROI, and what does this tell the business?
*   A) ROI = 250% — for every dollar spent, the campaign returned $2.50 in net gain, making it a profitable investment.
*   B) ROI = 150% — the campaign generated $1.50 in net gain for every dollar invested, indicating a positive return.
*   C) ROI = 40% — the campaign recovered 40% of its cost, indicating a partial return on investment.
*   D) ROI = 200% — the campaign revenue was $200,000 and the cost was $80,000, so the ratio is 200/80.
*   **Correct Answer:** B) ROI = 150% — the campaign generated $1.50 in net gain for every dollar invested, indicating a positive return.
*   **Distractor Analysis:**
    *   *Why B is correct:* Net Gain = Revenue − Cost = $200,000 − $80,000 = $120,000. ROI = ($120,000 / $80,000) × 100% = 150%. This means the campaign returned $1.50 for every $1 invested in net profit terms — a positive and meaningful return.
    *   *Why A is incorrect:* 250% would result from dividing revenue by cost ($200,000 / $80,000 = 2.5), which is the revenue-to-cost ratio, not ROI. The ROI formula requires net gain (revenue minus cost) in the numerator, not gross revenue.
    *   *Why C is incorrect:* 40% would result from dividing cost by revenue ($80,000 / $200,000 = 40%), which is the inverse ratio and has no standard business interpretation as an ROI figure.
    *   *Why D is incorrect:* Dividing raw revenue by raw cost ($200,000 / $80,000 = 2.5 or 250%) ignores the cost subtraction required to compute net gain. This overstates the return by counting the invested capital as profit.

---

**Question 5**
A retail chain tracks two metrics to manage inventory performance: (1) current stockout rate (percentage of SKUs out of stock right now) and (2) last quarter's lost sales due to stockouts. An operations analyst says the chain needs to reduce its reliance on the second metric. Why is the second metric less actionable than the first?
*   A) Lost sales is a financial metric, and inventory decisions should only use operational metrics.
*   B) Last quarter's lost sales is a lagging indicator — it confirms damage that has already occurred and cannot be changed. The current stockout rate is a leading indicator that enables intervention before more sales are lost.
*   C) Stockout rate is easier to calculate than lost sales, making it more cost-effective to track.
*   D) Last quarter's lost sales violates data freshness requirements because it is more than 30 days old.
*   **Correct Answer:** B) Last quarter's lost sales is a lagging indicator — it confirms damage that has already occurred and cannot be changed. The current stockout rate is a leading indicator that enables intervention before more sales are lost.
*   **Distractor Analysis:**
    *   *Why B is correct:* Last quarter's lost sales is a lagging indicator — the revenue is gone, the quarter is closed, and no action can recover it. Current stockout rate is a leading indicator that tells managers which SKUs are empty right now, enabling restocking before additional sales are lost. The distinction between leading and lagging determines whether the metric enables intervention or merely records history.
    *   *Why A is incorrect:* There is no rule prohibiting financial metrics in inventory management. Lost sales is entirely relevant to inventory decisions — the issue is its timing (lagging), not its type.
    *   *Why C is incorrect:* Calculation difficulty does not determine whether a metric is actionable. The actionability gap comes from the leading vs. lagging distinction, not from technical complexity.
    *   *Why D is incorrect:* A 30-day freshness threshold is not a universal rule for KPI validity. The fundamental problem is that last quarter's data reflects a past period where intervention is no longer possible — not that it fails an arbitrary freshness threshold.

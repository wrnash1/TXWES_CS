# Quiz: Module 06 - Statistical Analysis – Inferential Statistics and Hypothesis Testing
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Which data quality dimension measures whether all required data fields are populated in a record?
*   A) Accuracy
*   B) Completeness
*   C) Consistency
*   D) Validity
*   **Correct Answer:** B) Completeness confirms that all expected attributes are recorded, leaving no required fields empty.
*   **Distractor Analysis:**
    *   *Why correct:* Completeness specifically addresses whether required data is present — a null value in a required field is a completeness violation.
    *   Accuracy checks whether values are correct. Consistency checks whether values agree across systems. Validity checks whether values conform to defined rules and formats.

---

**Question 2**
In inferential statistics, which of the following most accurately defines **hypothesis testing**?
*   A) A formal statistical procedure that uses sample data to decide whether there is sufficient evidence to reject a null hypothesis (H₀), using a p-value compared against a pre-set significance level (alpha).
*   B) A method of summarizing a dataset by computing its mean, median, and standard deviation to describe the distribution of observed values.
*   C) The process of replacing missing values in a dataset with statistical estimates such as the column mean or median.
*   D) A data profiling technique that counts distinct values, null rates, and frequency distributions to assess data quality before analysis.
*   **Correct Answer:** A) A formal statistical procedure that uses sample data to decide whether there is sufficient evidence to reject a null hypothesis (H₀), using a p-value compared against a pre-set significance level (alpha).
*   **Distractor Analysis:**
    *   *Why A is correct:* Hypothesis testing is a decision framework — it formalizes the question "could this result have occurred by chance?" using probability.
    *   *Why B is incorrect:* Computing mean, median, and standard deviation describes descriptive statistics, not inferential hypothesis testing.
    *   *Why C is incorrect:* Replacing missing values describes imputation, a data cleaning technique.
    *   *Why D is incorrect:* Counting null rates and distinct values describes data profiling, a data quality assessment activity.

---

**Question 3**
A company runs an A/B test on a new checkout page design. The result shows p = 0.03 with a significance level of alpha = 0.05. What is the correct conclusion?
*   A) There is a 3% probability that the null hypothesis is true, confirming the new design always works better.
*   B) Reject the null hypothesis — the observed difference is statistically significant at the 0.05 level, meaning results this extreme would occur less than 3% of the time if there were truly no effect.
*   C) Fail to reject the null hypothesis — p = 0.03 is too small to be meaningful and should be ignored.
*   D) The test is inconclusive because p = 0.03 is between 0 and 0.05, which means no decision can be made.
*   **Correct Answer:** B) Reject the null hypothesis — the observed difference is statistically significant at the 0.05 level.
*   **Distractor Analysis:**
    *   *Why B is correct:* When p < alpha, the result is statistically significant and H₀ is rejected. p = 0.03 < 0.05 satisfies this condition.
    *   *Why A is incorrect:* The p-value is not the probability that H₀ is true. It is the probability of observing the data (or more extreme data) assuming H₀ is true — a critical distinction tested on Data+.
    *   *Why C is incorrect:* A p-value below alpha leads to rejecting H₀, not ignoring the result. Small p-values indicate stronger evidence against H₀.
    *   *Why D is incorrect:* p = 0.03 is clearly below alpha = 0.05, so a decision is straightforward: reject H₀.

---

**Question 4**
A data analyst discovers that the `customer_status` field contains "Active" in the CRM system but "Inactive" for the same customer in the billing system. Which data quality dimension is violated?
*   A) Completeness — the field is missing a value in one of the systems.
*   B) Validity — the value "Active" does not conform to the allowed format for customer status.
*   C) Consistency — the same real-world entity has conflicting values across two systems.
*   D) Uniqueness — the customer record appears more than once across the two systems.
*   **Correct Answer:** C) Consistency — the same real-world entity has conflicting values across two systems.
*   **Distractor Analysis:**
    *   *Why C is correct:* Consistency is the dimension that requires the same fact to have the same representation wherever it appears. Conflicting values for the same entity across systems is a consistency violation.
    *   *Why A is incorrect:* Completeness concerns missing values (NULLs). Both systems have a value — they just disagree.
    *   *Why B is incorrect:* Validity concerns format conformance. Both "Active" and "Inactive" are presumably valid status values; the problem is they contradict each other.
    *   *Why D is incorrect:* Uniqueness concerns duplicate records for the same entity within a system. Cross-system value conflict is a consistency issue.

---

**Question 5**
An analyst is profiling a dataset and finds that 12% of rows in the `postal_code` column contain values like "N/A", "unknown", and "00000" instead of real postal codes. Which two data quality dimensions are most likely violated?
*   A) Accuracy and uniqueness — the values are incorrect and appear multiple times.
*   B) Validity and accuracy — the values do not conform to postal code format rules and do not represent real geographic codes.
*   C) Completeness and consistency — some fields are blank and others disagree across systems.
*   D) Uniqueness and consistency — duplicate postal codes appear and disagree with a reference system.
*   **Correct Answer:** B) Validity and accuracy — the values do not conform to postal code format rules and do not represent real geographic codes.
*   **Distractor Analysis:**
    *   *Why B is correct:* "N/A" and "unknown" fail format validation (validity). "00000" may pass a format check but is not a real postal code (accuracy). Both dimensions are relevant.
    *   *Why A is incorrect:* Uniqueness means no duplicate entities — having "00000" appear multiple times is not a uniqueness violation in this context; the issue is that the values are meaningless placeholders.
    *   *Why C is incorrect:* Completeness concerns NULL fields. These fields are populated — they contain placeholder text. Cross-system disagreement is not described in this scenario.
    *   *Why D is incorrect:* The scenario does not mention duplicate entity records or cross-system comparisons, so uniqueness and consistency are not the primary violations.

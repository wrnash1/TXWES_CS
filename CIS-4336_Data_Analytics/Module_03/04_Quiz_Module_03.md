# Quiz: Module 03 - Data Cleaning and Transformation
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Which SQL clause is used to filter group results after aggregation has occurred?
*   A) WHERE
*   B) HAVING
*   C) GROUP BY
*   D) SELECT
*   **Correct Answer:** B) `HAVING` filters aggregated values (e.g., groups with SUM > 1000). `WHERE` filters individual rows before aggregation occurs.
*   **Distractor Analysis:**
    *   *Why correct:* `HAVING` operates on the result of GROUP BY, filtering out groups that do not meet the aggregate condition.
    *   WHERE filters rows before grouping. SELECT defines the output columns. GROUP BY creates the groups but does not filter them.

---

**Question 2**
In data cleaning, which of the following most accurately defines **deduplication**?
*   A) The process of identifying and removing redundant duplicate records from a dataset so that each real-world entity is represented only once, using key-field matching or fuzzy matching techniques.
*   B) Converting a column from one data type to another — for example, changing a text-format date into a proper date type recognized by the database engine.
*   C) Replacing missing (NULL) values with a calculated substitute such as the column mean, median, or mode to preserve the usable row count for analysis.
*   D) Restructuring a database into smaller, related tables to eliminate redundancy and prevent insert, update, and delete anomalies.
*   **Correct Answer:** A) The process of identifying and removing redundant duplicate records from a dataset so that each real-world entity is represented only once.
*   **Distractor Analysis:**
    *   *Why A is correct:* Deduplication specifically targets duplicate records — its defining characteristic is the removal of redundancy at the row level.
    *   *Why B is incorrect:* This describes type casting, a separate cleaning operation that converts data types.
    *   *Why C is incorrect:* This describes imputation, which addresses missing values rather than duplicate records.
    *   *Why D is incorrect:* This describes schema normalization, a database design operation, not a record-level cleaning step.

---

**Question 3**
A data analyst discovers that a `phone_number` column in a customer table contains values in four different formats: "(555) 123-4567", "555-123-4567", "5551234567", and "+1-555-123-4567". Which cleaning technique is most appropriate to standardize this column?
*   A) Imputation — replace all phone numbers with the column mode.
*   B) Deduplication — remove all rows with non-standard phone number formats.
*   C) Regex-based text transformation — apply a pattern to strip non-numeric characters and reformat all values to a single standard (e.g., "5551234567").
*   D) Type casting — convert the phone number column from VARCHAR to INTEGER.
*   **Correct Answer:** C) Regex-based text transformation — apply a pattern to strip non-numeric characters and reformat all values to a single standard.
*   **Distractor Analysis:**
    *   *Why C is correct:* Inconsistent text formats are precisely what regex transformation is designed to fix. A pattern like `[^0-9]` strips non-numeric characters to produce a uniform 10-digit string.
    *   *Why A is incorrect:* Imputation replaces missing values; phone numbers with different formats are not missing values.
    *   *Why B is incorrect:* Deduplication removes duplicate records; non-standard formats are not duplicate records.
    *   *Why D is incorrect:* Phone numbers should not be stored as integers because leading zeros would be lost and they are not used for arithmetic.

---

**Question 4**
A dataset has 5% missing values in the `annual_salary` column. The salary distribution is strongly right-skewed due to a few executives with very high salaries. Which imputation method is most appropriate?
*   A) Mean imputation, because it uses all available data points to compute the estimate.
*   B) Median imputation, because the median is resistant to the skew caused by extreme high-salary outliers.
*   C) Mode imputation, because the most common salary value is always the best substitute for any missing numeric field.
*   D) Listwise deletion, because 5% missing is always too small to justify any imputation effort.
*   **Correct Answer:** B) Median imputation, because the median is resistant to the skew caused by extreme high-salary outliers.
*   **Distractor Analysis:**
    *   *Why B is correct:* In a right-skewed distribution, the mean is pulled upward by high outliers. The median is the central value that splits the distribution in half and is unaffected by extreme values.
    *   *Why A is incorrect:* Mean imputation in a skewed distribution introduces bias because the inflated mean would overestimate missing salaries for typical employees.
    *   *Why C is incorrect:* Mode imputation applies to categorical variables; using the most frequent exact salary for a continuous variable would be misleading.
    *   *Why D is incorrect:* 5% missing is a moderate rate for which imputation is often preferred over deletion, which would reduce the sample size unnecessarily.

---

**Question 5**
After loading a CSV file, a column labeled `order_date` has dtype `object` (string) instead of `datetime`. SQL date range queries on this column return incorrect results. What is the correct remediation?
*   A) Delete all rows where `order_date` contains a value, since string dates cannot be converted.
*   B) Apply type casting to convert the `order_date` column from string to a proper datetime type using the appropriate parsing function.
*   C) Apply deduplication to remove rows with duplicate date strings.
*   D) Replace all string dates with the column mean using imputation.
*   **Correct Answer:** B) Apply type casting to convert the `order_date` column from string to a proper datetime type using the appropriate parsing function.
*   **Distractor Analysis:**
    *   *Why B is correct:* Type casting (e.g., `pd.to_datetime()` in Pandas or `CAST(order_date AS DATE)` in SQL) is the correct operation to convert string-formatted dates into a recognized date type that supports range queries.
    *   *Why A is incorrect:* String dates can be converted; deleting all date rows would destroy the dataset.
    *   *Why C is incorrect:* Deduplication targets duplicate records, not data type mismatches.
    *   *Why D is incorrect:* Imputation replaces missing values; non-missing string dates need type conversion, not substitution.

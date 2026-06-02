# Quiz — Module 03: Data Cleaning and Transformation

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 20 (2 points each)
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 3: Data Analysis

---

## Question 1

A dataset has 10,000 rows. The `annual_income` column is missing values for 850 rows (8.5%), and investigation shows the missing rows are distributed across all customer segments proportionally. Which missing value technique is most appropriate?

- A) Drop all rows with missing income values, because 8.5% is above the 5% threshold where deletion is safe
- B) Fill all missing values with zero, because income cannot be negative
- C) Apply mean or median imputation, because the missingness appears random and the proportion is manageable
- D) Leave the values as null, because any imputation would introduce bias

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** When missingness appears to be random (missing completely at random) and affects under roughly 10–15% of rows, imputation is appropriate. Mean imputation is suitable when the distribution is symmetric; median is preferred when outliers are present.
- **Why A is incorrect:** There is no fixed threshold that always makes deletion correct. At 8.5% with proportional distribution across segments, deletion would waste usable data and could be replaced effectively with imputation.
- **Why B is incorrect:** Filling income with zero treats missing data as "no income," which would incorrectly set those customers' income to zero and distort mean, sum, and model inputs.
- **Why D is incorrect:** Leaving nulls in place prevents many analyses and statistical operations that cannot handle null values. When imputation is feasible and well-reasoned, it is preferable to leaving nulls.

---

## Question 2

A data engineer is cleaning a customer database and finds that the `email` column contains 240 duplicate values — meaning 240 email addresses each appear twice. Which approach correctly removes these duplicates?

- A) Delete all rows where the email appears more than once
- B) Keep the first occurrence of each email address and drop subsequent duplicates
- C) Merge the two duplicate rows by averaging all numeric columns
- D) Flag duplicates with a Boolean column and leave both records in the dataset

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The standard deduplication approach is to keep one record per business key (email) and drop the others. Keeping "first" or "last" depends on the business rule — here, keeping the first occurrence is a valid default.
- **Why A is incorrect:** Deleting all rows where the email appears more than once would remove both the duplicate and the original, resulting in the loss of 480 rows of valid customer data.
- **Why C is incorrect:** Averaging numeric fields from duplicate rows is a valid merge strategy in some cases, but it is not a standard deduplication approach and can produce nonsensical values for non-numeric fields.
- **Why D is incorrect:** Flagging without removal does not solve the problem. Leaving duplicates in place will cause double-counting in all aggregations and analyses until they are removed.

---

## Question 3

A column called `order_date` contains values in three different formats: "2024-01-15," "January 15, 2024," and "01/15/24." What is the first and most important step for this column?

- A) Convert all values to ISO 8601 datetime format (YYYY-MM-DD) so date arithmetic and sorting are possible
- B) Delete all rows that do not use the YYYY-MM-DD format
- C) Convert all values to a numeric ordinal to enable arithmetic operations
- D) Leave the column as text because date formatting only affects display, not analysis

**Correct Answer:** A

**Distractor Analysis:**

- **Why A is correct:** Converting all date strings to a consistent ISO 8601 datetime type is the correct first step. It enables date arithmetic (days between dates), proper sorting, filtering by date range, and extraction of components like year and month.
- **Why B is incorrect:** Deleting rows with non-standard formats would eliminate valid data. The correct approach is to parse and standardize, not delete, when the underlying values are valid.
- **Why C is incorrect:** Converting dates to numeric ordinals is useful in some modeling contexts but is not the correct standardization step. Ordinal representation discards the semantic meaning of year, month, and day.
- **Why D is incorrect:** Date formatting directly affects analysis. String comparisons on dates do not sort correctly, date arithmetic is impossible on strings, and filtering by date range requires proper datetime type.

---

## Question 4

An analyst applies the IQR method to a `salary` column and finds that 3 values exceed the upper bound of $180,000. The analyst automatically removes these rows. What is the primary risk of this approach?

- A) The IQR method is not valid for detecting outliers in salary data
- B) The three removed values may be legitimate high-salary employees, and removing them introduces bias into the analysis
- C) The upper bound should be Q3 plus 3.0 times IQR, not 1.5 times IQR
- D) Outlier removal always requires manager approval before implementation

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Outlier detection flags values for investigation, not automatic deletion. High salaries may represent valid senior executives, and removing them without investigation introduces survivorship bias — the cleaned dataset would underrepresent the true salary distribution.
- **Why A is incorrect:** The IQR method is a valid and widely used technique for outlier detection in numeric columns including salary. The issue is not the method but the response to the finding.
- **Why C is incorrect:** 1.5 times IQR is the standard threshold for identifying outliers in boxplot methodology. 3.0 times IQR is used for identifying extreme outliers in some contexts. Neither is "wrong" — the threshold is a parameter to be set based on context.
- **Why D is incorrect:** While business approval may be good practice, the primary analytical risk is bias introduction, not a procedural approval requirement.

---

## Question 5

A `country` column contains "united states," "United States," "UNITED STATES," and "US" in different rows. All represent the same country. Which data quality dimension does this violate?

- A) Completeness
- B) Consistency
- C) Uniqueness
- D) Accuracy

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Consistency means the same real-world entity is represented the same way across all records. Four different string representations of the United States in a single column is a consistency violation that will break grouping, joining, and aggregation operations.
- **Why A is incorrect:** Completeness refers to missing or null values. All rows have a value — the problem is the format of the values, not their absence.
- **Why C is incorrect:** Uniqueness refers to duplicate records representing the same entity. Here the issue is inconsistent value formatting for a single attribute, not duplicate entity records.
- **Why D is incorrect:** Accuracy means values reflect real-world truth. All four representations are accurate (they all mean the United States) — the problem is inconsistent formatting, not incorrect information.

---

## Question 6

When should mean imputation be preferred over median imputation for a missing numeric column?

- A) When the column contains categorical values
- B) When the column has a symmetric distribution with few or no outliers
- C) When more than 40% of the column values are missing
- D) When the column contains only integer values

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Mean imputation is most appropriate when the data is roughly symmetrically distributed without significant outliers, because the mean is a good representation of the central tendency in that case. When outliers are present, the mean is pulled away from the center, making it a poor imputation choice.
- **Why A is incorrect:** Mean imputation applies to numeric columns. Categorical columns use mode imputation. A "categorical column" option is a distractor.
- **Why C is incorrect:** When more than 30–40% of values are missing, neither mean nor median imputation is recommended without domain knowledge. High missingness suggests a systemic collection problem that imputation alone cannot fix.
- **Why D is incorrect:** The integer vs. float distinction in storage type does not determine the appropriate imputation method. The shape of the distribution (symmetric vs. skewed) is the determining factor.

---

## Question 7

Which Python pandas method is used to detect exact duplicate rows in a DataFrame?

- A) `df.isnull().sum()`
- B) `df.duplicated().sum()`
- C) `df.describe()`
- D) `df.value_counts()`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** `df.duplicated()` returns a Boolean Series marking each row that is an exact duplicate of an earlier row. Calling `.sum()` on the result counts the total number of duplicate rows.
- **Why A is incorrect:** `df.isnull().sum()` counts null values per column. It detects missing values, not duplicate rows.
- **Why C is incorrect:** `df.describe()` returns summary statistics (count, mean, std, min, percentiles, max) for numeric columns. It does not identify duplicates.
- **Why D is incorrect:** `df.value_counts()` counts unique values in a Series (single column). It does not identify duplicate rows across all columns.

---

## Question 8

A data analyst creates a new column `profit_margin` by computing `(revenue - cost) / revenue` from existing columns. What is this technique called?

- A) Data normalization
- B) Feature engineering
- C) Data imputation
- D) Schema evolution

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Feature engineering (also called derived field creation) is the process of computing new columns from existing data to produce analytically useful information. Profit margin computed from revenue and cost is a classic derived feature.
- **Why A is incorrect:** Data normalization in the feature-engineering context means rescaling values to a 0–1 range. In the database context it means organizing tables to reduce redundancy. Neither meaning describes computing a new column from existing columns.
- **Why C is incorrect:** Imputation fills missing values with estimated replacements. Creating a new column from existing complete data is not imputation.
- **Why D is incorrect:** Schema evolution refers to changes to a database's table structure over time — adding or removing columns from the underlying schema. Computing a derived column in a DataFrame is not a schema change.

---

## Question 9

An analyst is working with daily temperature sensor data. The sensor occasionally fails, leaving gaps of one to three missing readings in the time series. Which missing value handling technique is most appropriate?

- A) Mean imputation using the column mean
- B) Drop all rows with missing sensor values
- C) Forward fill — carry the last valid reading forward to fill the gap
- D) Replace all missing values with zero

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** For time-series data where values are expected to be relatively stable between observations, forward fill (propagating the last valid reading forward) is the most contextually appropriate imputation method. Temperature does not jump dramatically between consecutive readings, so the last known value is a reasonable estimate.
- **Why A is incorrect:** Mean imputation uses the overall column average. For a time-series, the global mean ignores the temporal context — a reading of 72°F at midnight would be imputed with the daily average even if the local trend at that hour is 68°F.
- **Why B is incorrect:** Dropping rows with missing sensor readings discards time-series continuity. For most time-series analyses, preserving the temporal sequence matters, and dropping rows creates gaps that distort trends and aggregations.
- **Why D is incorrect:** Replacing temperature readings with zero would create extreme values that do not represent any plausible temperature, severely distorting distributions and trend calculations.

---

## Question 10

After completing a data cleaning pipeline, an analyst runs the following assertion and it raises an AssertionError. What does this indicate?

```python
assert df_clean["age"].between(0, 120).all(), "Invalid age values remain"
```

- A) The `age` column contains at least one value outside the range 0 to 120
- B) The `age` column contains null values
- C) The DataFrame has zero rows
- D) The `between()` method is not valid for integer columns

**Correct Answer:** A

**Distractor Analysis:**

- **Why A is correct:** `df["age"].between(0, 120)` returns True for each value in the valid range and False for any value outside it. `.all()` returns True only if every value is True. If any age value is below 0 or above 120, `.all()` returns False, and the assertion fails with the specified message.
- **Why B is incorrect:** Null values in the `age` column would cause `between()` to return NaN for those rows. `.all()` treats NaN as False, so nulls would also trigger the assertion — but the question asks what the assertion specifically checks. The assertion message states "Invalid age values remain," pointing to range violations. A separate null check would use `isnull().sum()`.
- **Why C is incorrect:** If the DataFrame had zero rows, `between().all()` would return True (vacuously true over an empty set), and the assertion would pass, not fail.
- **Why D is incorrect:** `between()` is fully valid for integer and float columns. It is a standard pandas method that returns a Boolean Series comparing values against the specified bounds.

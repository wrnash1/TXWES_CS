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

---

### Question 11 (5 points)

An analyst runs `df["purchase_amount"].fillna(df["purchase_amount"].mean())` but then notices the column has three extreme values above $50,000 while most purchases are under $500. What problem does this create?

- A) The mean is not a valid operation on numeric columns
- B) The extreme values inflate the mean, causing imputed values to be unrealistically high relative to the typical purchase
- C) `fillna()` does not work with computed values — only with constants
- D) Mean imputation is only valid when the column has no missing values

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** When a column contains outliers, the mean is pulled toward those extreme values. Imputing missing values with a skewed mean inserts artificially high estimates for typical customers, distorting the distribution. Median imputation is the correct choice when outliers are present.
  - **Why A is incorrect:** Mean is a fully valid arithmetic operation on numeric columns. The issue is not mathematical validity but statistical appropriateness given the distribution shape.
  - **Why C is incorrect:** `fillna()` accepts any scalar, including a dynamically computed value such as `df["col"].mean()`. This is a standard and supported usage.
  - **Why D is incorrect:** Mean imputation is applied specifically to fill missing values. The presence of non-missing values is required to compute the mean, but it does not restrict the use of `fillna()`.

---

### Question 12 (5 points)

Which pandas method removes leading and trailing whitespace from all values in a string column?

- A) `df["col"].strip()`
- B) `df["col"].str.strip()`
- C) `df["col"].replace(" ", "")`
- D) `df["col"].str.split()`

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** The `.str` accessor exposes string methods on a pandas Series element-wise. `.str.strip()` removes leading and trailing whitespace from every string value in the column.
  - **Why A is incorrect:** `.strip()` is a Python built-in string method that works on individual strings. Applied directly to a pandas Series (not a scalar string), it will raise an AttributeError.
  - **Why C is incorrect:** `.replace(" ", "")` replaces an exact substring (a single interior space) with an empty string. It does not specifically target leading or trailing whitespace and will also remove interior spaces.
  - **Why D is incorrect:** `.str.split()` splits each string into a list on whitespace, changing the data type of the column from string to list. It does not strip whitespace.

---

### Question 13 (5 points)

A time-series dataset has sensor readings every 5 minutes. Due to a network outage, readings are missing for a 20-minute window (four consecutive timestamps). The values before and after the gap are 68.2°F and 69.1°F respectively. Which imputation method preserves the most realistic representation of the data?

- A) Drop the four missing rows
- B) Fill all four with the column mean (70.5°F)
- C) Forward fill with 68.2°F for all four missing timestamps
- D) Fill all four with zero

- **Correct Answer:** C
- **Distractor Analysis:**
  - **Why C is correct:** For time-series data with a small, stable gap, forward fill propagates the last valid reading (68.2°F), which is consistent with the actual pre-gap temperature and much closer to the post-gap value (69.1°F) than the global column mean.
  - **Why A is incorrect:** Dropping four consecutive rows breaks the time-series continuity. Downstream analyses that require evenly spaced timestamps (moving averages, resampling) will produce incorrect results.
  - **Why B is incorrect:** The global column mean (70.5°F) may reflect a different time of day or season and is not representative of the conditions during this specific 20-minute gap. It introduces more error than forward fill.
  - **Why D is incorrect:** Zero does not represent any plausible temperature reading and would create extreme outliers that severely distort trend analysis.

---

### Question 14 (5 points)

What does the pandas `pd.cut()` function do?

- A) It splits a DataFrame into two separate DataFrames along a column boundary
- B) It removes rows containing values outside a specified range
- C) It bins a continuous numeric column into labeled categorical intervals
- D) It converts a string column into a numeric column by cutting non-numeric characters

- **Correct Answer:** C
- **Distractor Analysis:**
  - **Why C is correct:** `pd.cut()` assigns each value in a numeric Series to a bin defined by boundary edges and returns a categorical Series with one label per row. It is used for converting continuous data (like age or income) into ordinal groups.
  - **Why A is incorrect:** Splitting a DataFrame by column is done with indexing (e.g., `df[["col1", "col2"]]`). `pd.cut()` operates on a single Series and adds a categorical column.
  - **Why B is incorrect:** Filtering rows by range uses Boolean indexing (e.g., `df[df["age"].between(0, 120)]`). `pd.cut()` assigns bins, it does not remove rows.
  - **Why D is incorrect:** Converting strings to numeric values uses `pd.to_numeric()` or `.astype(float)`. `pd.cut()` works on numeric input, not string input.

---

### Question 15 (5 points)

After a data cleaning pipeline, an analyst runs `assert df["email"].nunique() == len(df)` and the assertion passes. What has been confirmed?

- A) The `email` column contains no null values
- B) Every row has a unique email address — no duplicate records remain
- C) The email format follows a valid pattern (e.g., contains "@")
- D) The number of rows equals the expected total from the source system

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** `nunique()` counts the number of distinct values. If `nunique() == len(df)`, every row has a different email address, confirming no duplicates remain on the email business key.
  - **Why A is incorrect:** `nunique()` by default excludes null values from the count. If there were null emails, `nunique()` would be less than the total rows but not necessarily less than `len(df)` if nulls happened to reduce count precisely. A dedicated null check (`isnull().sum() == 0`) is required.
  - **Why C is incorrect:** `nunique()` counts distinct values regardless of format. An email column full of strings without "@" would still have all unique values. Format validation requires regex pattern checking.
  - **Why D is incorrect:** `len(df)` reflects the current DataFrame row count. Comparing unique email count to current row count checks internal uniqueness, not whether rows are missing relative to a source system.

---

### Question 16 (5 points)

A raw dataset contains a `price` column stored as strings like "$1,299.99" and "$89.00". Which pandas code correctly converts this column to float?

- A) `df["price"].astype(float)`
- B) `df["price"].str.replace(r"[$,]", "", regex=True).astype(float)`
- C) `pd.to_numeric(df["price"])`
- D) `df["price"].str.strip("$").astype(float)`

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** `str.replace(r"[$,]", "", regex=True)` uses a regex character class to remove both the dollar sign and any comma separators in one pass. After removal, the clean numeric strings can be safely cast to float.
  - **Why A is incorrect:** `astype(float)` on a string like "$1,299.99" raises a ValueError because Python cannot directly parse strings containing "$" and "," as floats.
  - **Why C is incorrect:** `pd.to_numeric()` will raise an error or return NaN for strings containing "$" and "," because they are not parseable as numbers without prior cleanup.
  - **Why D is incorrect:** `.str.strip("$")` removes the "$" character from the start and end of the string, but it does not remove the comma separator in numbers like "1,299.99". The result "1,299.99" still cannot be cast to float.

---

### Question 17 (5 points)

A company's customer database has 50,000 rows. After running a deduplication check, an analyst finds 2,300 duplicate rows. She removes all duplicates using `df.drop_duplicates(subset=["customer_id"], keep="first")`. What is the resulting row count?

- A) 47,700
- B) 50,000
- C) 48,600 — because `drop_duplicates` removes one copy of each pair
- D) 45,400 — because all rows involved in any duplication are removed

- **Correct Answer:** A
- **Distractor Analysis:**
  - **Why A is correct:** `drop_duplicates(keep="first")` retains the first occurrence of each duplicated `customer_id` and removes all subsequent duplicates. If 2,300 rows are duplicates of earlier rows, removing them leaves 50,000 − 2,300 = 47,700 rows.
  - **Why B is incorrect:** 50,000 would indicate no rows were removed. The deduplication confirmed 2,300 duplicates, so the row count must decrease.
  - **Why C is incorrect:** 48,600 would result from removing only half of each duplicate pair (1,150 rows). `drop_duplicates(keep="first")` removes all 2,300 duplicate rows — all copies after the first.
  - **Why D is incorrect:** 45,400 would result from removing both the original and the duplicate for each pair (4,600 total rows removed). The `keep="first"` parameter preserves the original, removing only the 2,300 extra copies.

---

### Question 18 (5 points)

Which of the following best describes the purpose of data profiling in the cleaning workflow?

- A) Data profiling applies cleaning transformations to fix identified problems automatically
- B) Data profiling summarizes a dataset's structure, completeness, distributions, and anomalies to inform the cleaning strategy before any changes are made
- C) Data profiling compares a cleaned dataset to the original to verify that transformations were applied correctly
- D) Data profiling is the process of documenting the business rules that define valid data

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** Data profiling is the exploratory phase before cleaning. It involves running `df.shape`, `df.dtypes`, `df.isnull().sum()`, `df.describe()`, and value counts to understand what the data looks like and what problems exist, so that an informed cleaning plan can be designed.
  - **Why A is incorrect:** Profiling observes and reports; it does not apply transformations. Transformation is a separate subsequent step.
  - **Why C is incorrect:** Comparing cleaned data to the original is post-cleaning validation, not profiling. Profiling occurs before cleaning to understand the raw data.
  - **Why D is incorrect:** Documenting business rules is part of requirements gathering and data governance, not data profiling. Profiling is an analytical activity applied to the data itself.

---

### Question 19 (5 points)

A dataset has an `order_date` column with valid dates, but three rows have order dates in the year 2087 — clearly data entry errors. The IQR method is applied to numeric columns but does not flag these dates. What cleaning step is appropriate?

- A) Use `pd.to_datetime()` to convert the column, then apply the IQR method to the resulting float values
- B) Apply a domain-specific range filter: drop or flag rows where `order_date` is after today's date
- C) Ignore the issue because date columns are not subject to outlier detection
- D) Replace the invalid dates with the column median date using `fillna()`

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** Domain knowledge defines the valid range for dates — an order date in the future is impossible for historical data. A business-logic filter (`df[df["order_date"] <= pd.Timestamp.today()]`) is the correct approach for date-range validation.
  - **Why A is incorrect:** Converting dates to float timestamps and applying IQR may work in theory, but the dates in 2087 are by definition impossible — a business-logic range check is clearer and more appropriate than a statistical outlier method for impossible values.
  - **Why C is incorrect:** Date columns absolutely require validation checks. Dates outside the valid business range are as much a data quality problem as out-of-range numeric values.
  - **Why D is incorrect:** `fillna()` fills null values. The rows have non-null dates — the values are present but invalid. The correct action is to filter or flag them, not to fill nulls that don't exist.

---

### Question 20 (5 points)

After running a full cleaning pipeline, an analyst reports: "The original dataset had 15,000 rows. After deduplication, null removal, and outlier filtering, the cleaned dataset has 13,847 rows." What should the analyst include in the data cleaning report to make this statement analytically trustworthy?

- A) The names of all Python functions used in the pipeline
- B) A breakdown of how many rows were removed at each step, the business rule applied at each step, and confirmation that the removed rows were not biased toward a specific customer segment
- C) The exact memory usage of the original and cleaned DataFrames
- D) A list of all column names and their data types before and after cleaning

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** A trustworthy cleaning report documents each removal step's count and rationale, and critically, checks whether the removed rows are systematically different from retained rows (e.g., all removed rows are from one region). Systematic removal introduces bias that distorts downstream analysis.
  - **Why A is incorrect:** Listing function names documents implementation details, not analytical decisions. Stakeholders need to understand what was removed and why, not which Python functions were called.
  - **Why C is incorrect:** Memory usage is an operational concern irrelevant to the analytical validity of the cleaning decisions.
  - **Why D is incorrect:** Documenting column names and types is useful for schema documentation but does not address the key question: why were 1,153 rows removed, and does that removal change what the remaining data represents?

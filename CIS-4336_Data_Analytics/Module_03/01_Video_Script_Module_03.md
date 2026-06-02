# Video Script — Module 03: Data Cleaning and Transformation

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Runtime:** 20–24 minutes
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 3: Data Analysis

---

## Segment 1 — Introduction (2 minutes)

Welcome back to CIS-4336. I am Professor Nash, and this is Module 03: Data Cleaning and Transformation.

Every data analyst will tell you the same thing: the majority of their time is spent not on analysis, but on cleaning. Industry surveys consistently put the proportion of analyst time spent on data preparation at 60 to 80 percent. That is not a complaint — it reflects the reality that real-world data is messy, inconsistent, and incomplete.

By the end of this module, you will be able to:

- Identify and describe the most common data quality problems
- Apply standard techniques for handling missing values
- Remove duplicate records and standardize inconsistent values
- Perform data type conversions and derived field creation
- Validate data after transformation to confirm quality
- Apply these concepts to Data+ DA0-001 Domain 3 exam questions

Let us get started.

---

## Segment 2 — Why Data Quality Problems Happen (3 minutes)

Before we can fix data quality problems, we need to understand where they come from. Data quality issues do not appear randomly — they have systematic causes.

**Manual data entry errors** are the oldest and most persistent source of quality problems. A user types "Unitd States" instead of "United States." A price is entered as 1200 instead of 12.00. Date formats vary by user — some type 01/15/2024, others type January 15, 2024, and others type 2024-01-15.

**System migration artifacts** occur when data is moved from one system to another and the mapping between schemas is imperfect. Duplicate records are especially common after migrations — the same customer may exist in both the old and new system.

**Integration from multiple sources** creates consistency problems. If two systems both track customers but use different formats for phone numbers, email addresses, or names, joining those systems produces a dataset with inconsistent representations.

**Measurement and sensor failures** produce missing readings, out-of-range values, and duplicate timestamps.

**Schema evolution** happens when a system's data model changes over time. Old records may have null values in fields that were added later. New records may have values in fields that old records never captured.

[SHOW CHART: Fishbone (Ishikawa) diagram showing six categories of data quality problem causes: Manual Entry, System Migration, Multi-Source Integration, Sensor/Measurement, Schema Changes, and Business Process Changes — each with two to three example root causes]

Understanding the cause shapes the fix. A null value caused by a missing measurement should be handled differently than a null value caused by a field that did not exist when the record was created.

---

## Segment 3 — Handling Missing Values (4 minutes)

Missing data is the most common quality issue you will encounter. There is no universally correct way to handle it — the right approach depends on the cause and the analysis goal.

**Option 1: Remove rows with missing values.** This is the simplest approach, but it is only appropriate when the missing rows are a small percentage of the total dataset and are missing at random. If certain customers consistently have missing data, removing them introduces bias.

**Option 2: Fill with a constant.** Replace nulls with a designated value — "Unknown" for categorical fields, or 0 for numeric fields. Be careful here: filling a numeric null with 0 will affect statistics like mean and sum. Use this approach only when 0 or "Unknown" is genuinely meaningful in context.

**Option 3: Mean imputation.** Replace missing numeric values with the column mean. This preserves the overall mean of the dataset but reduces variance. It works reasonably when data is missing at random and the proportion is small.

**Option 4: Median imputation.** Replace missing numeric values with the column median. This is more robust than mean imputation when the column has outliers, because the median is not pulled by extreme values.

**Option 5: Mode imputation.** For categorical columns, replace missing values with the most frequent category. Use with caution — this can artificially inflate the frequency of the most common category.

**Option 6: Forward fill or backward fill.** In time-series data, fill missing values by carrying forward the previous valid value, or backward from the next valid value. This is appropriate when values are expected to remain stable between observations.

**Option 7: Predictive imputation.** Use a model to predict the missing value based on other columns. This is the most sophisticated approach and can produce high-quality imputations, but requires care to avoid circular reasoning in the analysis.

[SHOW CHART: Decision flowchart — "What type is the missing column?" branches to Numeric or Categorical. Numeric branches to "Data is time-series?" (yes = forward/backward fill) and "Outliers present?" (yes = median, no = mean). Categorical branches to "Ordered?" (yes = median category, no = mode)]

---

## Segment 4 — Duplicate Records (2 minutes)

Duplicate records artificially inflate counts, distort totals, and invalidate statistical analysis. A dataset that counts one customer twice will overstate customer count, overstate revenue if purchase amounts are also doubled, and skew demographic statistics.

**Exact duplicates** are records where every column value is identical. These are straightforward to detect and remove.

**Near duplicates** are records that represent the same real-world entity but differ slightly — perhaps the name is spelled differently, or the phone number format differs. Resolving near duplicates requires fuzzy matching techniques.

The standard approach to deduplication:

1. Define what makes a record unique — the business key. For customers, this might be email address. For transactions, it might be transaction ID plus timestamp.
2. Sort or hash records by the business key.
3. Identify groups where the business key is duplicated.
4. Apply a retention rule: keep the most recent, keep the most complete, or merge fields from both records.

[SHOW CODE]

```python
import pandas as pd
df = pd.read_csv("customers.csv")
# Remove exact duplicates
df = df.drop_duplicates()
# Remove duplicates based on business key
df = df.drop_duplicates(subset=["email"], keep="last")
print(f"Rows after deduplication: {len(df)}")
```

---

## Segment 5 — Standardization and Consistency (3 minutes)

Standardization transforms data values to a consistent format without changing their meaning.

**String standardization** is one of the most common tasks. Trim leading and trailing whitespace. Normalize case (typically all lowercase or title case). Map synonyms and abbreviations to a canonical form: "US," "USA," "U.S.A.," and "United States" all become "United States."

**Date format standardization** is critical when combining data from multiple sources. The ISO 8601 format — YYYY-MM-DD — is the universal standard for dates in data pipelines. All date values should be converted to this format as early as possible in the pipeline.

**Numeric format standardization** addresses issues like currency symbols, thousands separators, and units. "$1,200.50" must be converted to the float 1200.50 before arithmetic operations.

**Category standardization** addresses value-level inconsistencies in categorical columns. "Full Time," "Full-Time," "full time," and "FT" all mean the same thing and should be mapped to a single canonical value.

[SHOW CODE]

```python
# String standardization
df["country"] = df["country"].str.strip().str.lower()
df["country"] = df["country"].replace({
    "us": "united states",
    "usa": "united states",
    "u.s.a.": "united states"
})

# Date standardization
df["order_date"] = pd.to_datetime(df["order_date"], infer_datetime_format=True)

# Remove currency symbols and convert to float
df["revenue"] = df["revenue"].str.replace("[$,]", "", regex=True).astype(float)
```

---

## Segment 6 — Outlier Detection and Handling (2 minutes)

Outliers are values that fall far outside the expected range of a variable. They may represent genuine extreme events, data entry errors, or sensor malfunctions.

The IQR method is a standard technique for identifying outliers in numeric columns.

Calculate the interquartile range: IQR = Q3 minus Q1. Values below Q1 minus 1.5 times IQR, or above Q3 plus 1.5 times IQR, are flagged as potential outliers.

[SHOW CODE]

```python
Q1 = df["purchase_amount"].quantile(0.25)
Q3 = df["purchase_amount"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df["purchase_amount"] < lower) | (df["purchase_amount"] > upper)]
print(f"Outliers detected: {len(outliers)}")
```

The key decision when outliers are detected: investigate before removing. A $50,000 purchase amount from a corporate customer may be a legitimate transaction, not an error. Remove outliers only when you have confirmed they are errors or noise, not when they are inconvenient.

---

## Segment 7 — Data Type Conversion and Feature Engineering (2 minutes)

After cleaning, analysts often need to reshape data by converting types or computing new fields.

**Data type conversion** corrects cases where a column's storage type does not match its logical type. A date stored as a string must be converted to a datetime type before date arithmetic works. A numeric ID stored as a float should be converted to an integer. A boolean flag stored as "Y"/"N" strings should be converted to True/False.

**Derived fields** (also called feature engineering in machine learning contexts) create new columns computed from existing ones.

- Extracting year, month, or day from a date column
- Computing profit as revenue minus cost
- Creating an age group label from an exact age value
- Computing a price-per-unit from total price and quantity

[SHOW CODE]

```python
# Extract date components
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month

# Compute derived field
df["profit"] = df["revenue"] - df["cost"]

# Bin a continuous variable into categories
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 17, 34, 54, 100],
    labels=["Under 18", "18-34", "35-54", "55+"]
)
```

---

## Segment 8 — Data Validation After Transformation (2 minutes)

Cleaning introduces changes. Validation confirms those changes produced correct results.

A data validation checklist after transformation should include:

- Row count matches expected count after deduplication
- No nulls remain in required fields
- All date columns are in a consistent format
- Numeric columns fall within expected ranges (no negative ages, no revenue over a plausible maximum)
- Categorical columns contain only the expected set of values
- Foreign key relationships are maintained (no orphaned records after filtering)

[SHOW CODE]

```python
# Validate no nulls in required columns
required_cols = ["customer_id", "order_date", "revenue"]
for col in required_cols:
    null_count = df[col].isnull().sum()
    assert null_count == 0, f"Null values found in {col}: {null_count}"

# Validate value ranges
assert df["revenue"].min() >= 0, "Negative revenue values found"
assert df["age"].between(0, 120).all(), "Age values out of valid range"
print("All validation checks passed.")
```

Automated validation like this should be embedded in every production data pipeline.

---

## Segment 9 — Exam Alignment and Closing (2 minutes)

Module 03 content maps primarily to Data+ Domain 3 — Data Analysis — specifically the data preparation and quality subdomains. Exam topics include:

- Identifying data quality issues from a described dataset
- Selecting the appropriate technique for handling missing values
- Recognizing the result of applying or not applying standardization
- Understanding what deduplication achieves and when it is needed

For exam preparation, review the Data+ objectives at comptia.org and Professor Messer's study guides at professormesser.com.

Your Module 03 assignments:

- Complete the Reading Guide — focus on the cleaning technique decision table and the Python pandas cheat sheet
- Complete Lab 03 — you will work through a real cleaning workflow on a provided messy dataset
- Complete the ten-question quiz
- Post to the Discussion Board by Wednesday and respond to two classmates by Sunday

See you in Module 04, where we go deep on relational databases and SQL for analytics.

---

End of Module 03 Video Script — Estimated runtime: 22 minutes

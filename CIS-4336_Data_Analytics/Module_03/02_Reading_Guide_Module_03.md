# Reading Guide — Module 03: Data Cleaning and Transformation

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4336 &BULL; DATA ANALYTICS & BUSINESS INTELLIGENCE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 3: Data Analysis

---

## Overview

Data cleaning is the most time-consuming phase of analytics work. This reading guide provides reference tables, decision frameworks, and Python code patterns for the cleaning and transformation techniques covered in Module 03. Work through every section before attempting the lab or quiz.

---

## Section 1 — Core Vocabulary

| Term | Definition |
|---|---|
| Data cleaning | The process of detecting and correcting errors, inconsistencies, and missing values in a dataset |
| Data transformation | Reshaping, converting, or computing new fields to prepare data for analysis |
| Missing value | A record where no data is present for a required field |
| Null | A database representation of a missing or unknown value |
| Imputation | Filling in missing values using a statistical or model-based estimate |
| Deduplication | The process of identifying and removing duplicate records |
| Outlier | A value that falls far outside the expected distribution of a variable |
| Standardization | Converting values to a consistent format without changing their meaning |
| Normalization | Rescaling numeric values to a common range (e.g., 0–1) — distinct from database normalization |
| Feature engineering | Creating new columns derived from existing ones to support analysis or modeling |
| Data profiling | Summarizing a dataset's structure, completeness, and value distributions before cleaning |
| IQR | Interquartile Range — Q3 minus Q1, used to define outlier boundaries |
| Forward fill | Filling missing time-series values by carrying forward the last known value |
| Backward fill | Filling missing time-series values by using the next known value |
| Data validation | Post-cleaning checks that confirm the transformed dataset meets quality requirements |
| Regex | Regular expressions — pattern-matching syntax used for string cleaning |

---

## Section 2 — Data Quality Problem Reference

| Problem Type | Description | Common Cause | Detection Method |
|---|---|---|---|
| Missing values | Required fields are null or blank | System migration, optional fields, sensor failure | `df.isnull().sum()` |
| Duplicate records | Same entity appears multiple times | Multi-source merge, migration artifacts | `df.duplicated().sum()` |
| Inconsistent formatting | Same value represented differently | Manual entry, multi-system integration | Value count inspection |
| Type mismatch | Column stored as wrong data type | CSV import, legacy system export | `df.dtypes` |
| Out-of-range values | Numeric values outside valid domain | Data entry error, sensor malfunction | `df.describe()`, range checks |
| Referential integrity errors | Foreign key value references no matching primary key | Failed ETL join, orphaned records | JOIN-based null checks |
| Structural inconsistency | Schema varies across records or batches | Schema evolution, optional fields | Column presence checks |
| Stale data | Records are too old for the analytical purpose | Infrequent refresh, archiving errors | Timestamp distribution check |

---

## Section 3 — Missing Value Handling Decision Table

| Scenario | Recommended Method | Why |
|---|---|---|
| Less than 5% missing, appears random | Drop rows with missing values | Minimal bias impact; simplest approach |
| Numeric column, no outliers | Mean imputation | Preserves column mean; appropriate for symmetric distributions |
| Numeric column, outliers present | Median imputation | Median is not distorted by extreme values |
| Categorical column | Mode imputation | Most frequent category is the best single-value estimate |
| Time-series with stable values | Forward fill | Carries last known valid observation forward |
| Time-series with known recovery | Backward fill | Uses next known value to fill gaps |
| More than 30% missing | Flag and investigate | High missingness may indicate a systemic collection problem |
| Missing not at random | Do not impute without domain knowledge | Imputation may mask meaningful absence |

---

## Section 4 — Python Pandas Cleaning Cheat Sheet

### Loading and Profiling

```python
import pandas as pd

df = pd.read_csv("data.csv")

# Basic profiling
print(df.shape)          # (rows, columns)
print(df.dtypes)         # column types
print(df.isnull().sum()) # null counts per column
print(df.describe())     # numeric summary statistics
print(df.nunique())      # unique value counts per column
```

### Handling Missing Values

```python
# Drop rows where any required column is null
df = df.dropna(subset=["customer_id", "order_date"])

# Fill numeric nulls with column mean
df["revenue"] = df["revenue"].fillna(df["revenue"].mean())

# Fill numeric nulls with column median
df["age"] = df["age"].fillna(df["age"].median())

# Fill categorical nulls with mode
df["region"] = df["region"].fillna(df["region"].mode()[0])

# Forward fill for time-series
df["temperature"] = df["temperature"].ffill()
```

### Deduplication

```python
# Remove exact duplicates
df = df.drop_duplicates()

# Remove duplicates on business key, keep most recent
df = df.sort_values("updated_at", ascending=False)
df = df.drop_duplicates(subset=["email"], keep="first")
```

### Standardization

```python
# Strip whitespace and normalize case
df["country"] = df["country"].str.strip().str.upper()

# Map multiple values to canonical form
df["country"] = df["country"].replace({
    "US": "UNITED STATES",
    "USA": "UNITED STATES",
    "U.S.A.": "UNITED STATES"
})

# Standardize date format
df["order_date"] = pd.to_datetime(df["order_date"], infer_datetime_format=True)

# Remove currency symbol and convert
df["price"] = df["price"].str.replace(r"[$,]", "", regex=True).astype(float)
```

### Outlier Detection

```python
Q1 = df["amount"].quantile(0.25)
Q3 = df["amount"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Flag outliers
df["is_outlier"] = (df["amount"] < lower_bound) | (df["amount"] > upper_bound)

# Remove confirmed erroneous outliers
df_clean = df[~df["is_outlier"]]
```

### Feature Engineering

```python
# Date components
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["day_of_week"] = df["order_date"].dt.day_name()

# Computed field
df["profit_margin"] = (df["revenue"] - df["cost"]) / df["revenue"]

# Binning continuous to categorical
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 17, 34, 54, 100],
    labels=["Under 18", "18-34", "35-54", "55+"]
)

# One-hot encoding (for modeling)
df = pd.get_dummies(df, columns=["region"], drop_first=True)
```

### Post-Cleaning Validation

```python
# Check for remaining nulls
assert df["customer_id"].isnull().sum() == 0, "Nulls in customer_id"

# Check value ranges
assert df["age"].between(0, 120).all(), "Invalid age values"
assert df["revenue"].min() >= 0, "Negative revenue"

# Check expected categories
valid_regions = {"North", "South", "East", "West"}
assert set(df["region"].unique()).issubset(valid_regions), "Unexpected region values"
```

---

## Section 5 — Outlier Handling Decision Guide

When an outlier is detected, ask these questions before removing it.

1. Is the value mathematically impossible for this variable (e.g., negative age)? If yes, it is an error — remove or correct.
2. Is the value possible but extreme (e.g., a corporate order for $100,000 when most orders are under $500)? Investigate — it may be legitimate.
3. Does the outlier affect the analysis goal? If you are computing median revenue, outliers have little effect. If you are computing mean revenue, they have significant effect.
4. Is the proportion of outliers large enough to indicate a systemic collection problem rather than isolated noise?

---

## Section 6 — Data Transformation Checklist

Before delivering a cleaned dataset, verify all of the following.

- [ ] All null values in required columns have been addressed
- [ ] Duplicate records have been identified and a retention rule applied
- [ ] All string columns have consistent case and no leading/trailing whitespace
- [ ] Date columns are in a consistent format (ISO 8601 preferred)
- [ ] Numeric columns are the correct type (int, float) — no currency symbols or commas
- [ ] Categorical columns contain only expected values
- [ ] Outliers have been investigated and a documented decision made for each
- [ ] All derived columns are correctly computed
- [ ] Post-cleaning row count is documented and compared to source row count
- [ ] Validation assertions pass without errors

---

## Section 7 — Data+ Exam Tips

1. **Cleaning consumes most analyst time.** A Data+ exam scenario may ask which phase takes the most time in a real analytics project. The answer is data cleaning and preparation — not analysis or visualization.

2. **Imputation vs. deletion tradeoff.** Know when each is appropriate. Deleting rows is appropriate for random small-percentage missingness. Imputation is used when deletion would cause bias or significant data loss.

3. **Mean vs. median imputation.** Use mean when data is roughly symmetric. Use median when the column has outliers, because the median is resistant to extreme values.

4. **Deduplication requires a business key.** The exam may describe a scenario with duplicates and ask how to detect them. Duplicates are found by grouping on the business key — the combination of columns that should uniquely identify each real-world entity.

5. **Outlier removal requires justification.** The exam treats outlier removal as a decision requiring evidence, not a default cleaning step. Removing a statistically extreme but legitimately occurring value introduces bias.

6. **Standardization vs. normalization.** Standardization converts values to a consistent representation (e.g., all dates to YYYY-MM-DD). Normalization in the feature-engineering context rescales values to a 0–1 range. These are different operations.

7. **Validation is part of the pipeline.** The Data+ exam includes data validation as a formal step in the analytics lifecycle. Post-cleaning validation confirms that transformations produced the intended results.

8. **Data profiling precedes cleaning.** Before cleaning, you profile the data — understand its shape, nulls, types, and distributions. Profiling informs the cleaning strategy.

---

## Section 8 — Study Checklist

- [ ] Memorize all vocabulary terms in Section 1
- [ ] Reproduce the missing value decision table from memory
- [ ] Run each code block in Section 4 and confirm expected output
- [ ] Practice applying the outlier decision guide to three example variables
- [ ] Complete the data transformation checklist on a sample dataset
- [ ] Review all eight exam tips
- [ ] Review official CompTIA Data+ objectives at comptia.org
- [ ] Review Professor Messer's free study materials at professormesser.com
- [ ] Complete Lab 03
- [ ] Complete Quiz 03

---

## Additional Resources

- Official exam objectives: comptia.org (search "Data+ DA0-001 exam objectives")
- Professor Messer's free study guides: professormesser.com

## 9. Supplemental Resources

**1. Kaggle Learn — Data Cleaning (Python)**
<https://www.kaggle.com/learn/data-cleaning>
A free, hands-on course covering handling missing values, scaling and normalization, data type parsing, and character encoding using real messy datasets. Directly maps to the techniques in this module.

**2. Towards Data Science — A Practical Guide to Data Imputation**
<https://towardsdatascience.com/6-different-ways-to-compensate-for-missing-values-data-imputation-with-examples-6022d9ca0779>
Covers six imputation strategies with Python examples, including mean, median, mode, forward fill, KNN, and MICE. Essential reading for understanding when each method is appropriate.

**3. pandas Official Documentation — Working with Missing Data**
<https://pandas.pydata.org/docs/user_guide/missing_data.html>
The authoritative reference for all pandas null-handling methods: `isnull()`, `fillna()`, `dropna()`, `ffill()`, `bfill()`, and interpolation. Includes edge cases and performance notes.

# Lab 03 — Data Cleaning and Transformation

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 3: Data Analysis

---

## Objectives

By completing this lab, you will be able to:

- Profile a dataset to identify data quality problems before cleaning
- Apply appropriate techniques for handling missing values
- Detect and remove duplicate records using a business key
- Standardize string, date, and numeric values
- Detect outliers using the IQR method
- Validate a cleaned dataset against defined quality rules

---

## Prerequisites

- Module 03 Reading Guide completed
- Python 3.8 or later (or access to Google Colab)
- pandas library installed: `pip install pandas`

---

## Part A — Dataset Setup and Profiling (15 points)

### Part A Instructions

Run the following code to create the lab dataset. This synthetic dataset deliberately contains data quality problems you will fix in Parts B through E.

```python
import pandas as pd
import numpy as np

data = {
    "customer_id": [101, 102, 103, 104, 105, 102, 106, 107, 108, 109, 110, 111],
    "first_name": ["Alice", "Bob", "Carol", "  David", "Eva", "Bob",
                   "Frank", "Grace", "Hank", None, "Irene", "Jack"],
    "email": ["alice@ex.com", "bob@ex.com", "carol@ex.com", "david@ex.com",
              "eva@ex.com", "bob@ex.com", "frank@ex.com", "grace@ex.com",
              "hank@ex.com", "unknown@ex.com", "irene@ex.com", "jack@ex.com"],
    "region": ["North", "south", "NORTH", "East", "West", "south",
               "East", "North", "West", "East", "  south  ", "N/A"],
    "signup_date": ["2023-01-15", "Jan 20, 2023", "2023/03/05", "2023-04-10",
                    "2023-05-22", "Jan 20, 2023", "2023-06-18", "2023-07-30",
                    "2023-08-14", "2023-09-01", "2023-10-12", "2023-11-05"],
    "purchase_amount": [250.00, 88.50, 3200.00, None, 175.25, 88.50,
                        920.00, 5.00, 310.75, 95.00, 99999.00, 430.00],
    "age": [34, 28, 45, 52, None, 28, 33, 19, 41, 300, 29, 38],
    "loyalty_tier": ["Gold", "Bronze", "Gold", "Silver", "Silver", "Bronze",
                     "Gold", "Bronze", None, "Bronze", "Silver", "Gold"]
}

df = pd.DataFrame(data)
print(df)
```

### Part A Questions

**Question A1 (5 points):** Run the following profiling commands and report the output. Identify at least five distinct data quality problems visible in the output.

```python
print("Shape:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nNull Counts:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nRegion Value Counts:\n", df["region"].value_counts(dropna=False))
print("\nAge Stats:\n", df["age"].describe())
print("\nPurchase Amount Stats:\n", df["purchase_amount"].describe())
```

**Question A2 (5 points):** For each of the five (or more) problems you identified, state which data quality dimension it violates (Completeness, Accuracy, Consistency, Uniqueness, Validity, or Timeliness) and describe the likely cause.

**Question A3 (5 points):** Before cleaning, what is the row count? After your plan is executed (anticipating Parts B through E), what row count do you expect and why? Write your prediction now; compare to actual after completing all parts.

### Part A Deliverable

Report profiling output, list of problems with quality dimension, and pre-cleaning row count prediction.

---

## Part B — Missing Values and Deduplication (25 points)

### Part B Instructions

Fix the missing value and duplicate problems identified in Part A.

```python
# Step 1: Remove duplicate rows based on the business key (email)
df_clean = df.drop_duplicates(subset=["email"], keep="first")
print(f"Rows after deduplication: {len(df_clean)}")

# Step 2: Fill missing first_name with "Unknown"
df_clean["first_name"] = df_clean["first_name"].fillna("Unknown")

# Step 3: Fill missing loyalty_tier with mode
mode_tier = df_clean["loyalty_tier"].mode()[0]
df_clean["loyalty_tier"] = df_clean["loyalty_tier"].fillna(mode_tier)

# Step 4: Fill missing age with median
df_clean["age"] = df_clean["age"].fillna(df_clean["age"].median())

# Step 5: Fill missing purchase_amount with median
df_clean["purchase_amount"] = df_clean["purchase_amount"].fillna(
    df_clean["purchase_amount"].median()
)

print("\nNull counts after fixes:\n", df_clean.isnull().sum())
```

### Part B Questions

**Question B1 (8 points):** For the `first_name` column, you used the constant "Unknown." For `age` and `purchase_amount`, you used median imputation. Justify why median was chosen over mean for numeric imputation in this dataset. Reference the `describe()` output from Part A in your answer.

**Question B2 (8 points):** The deduplication step used `keep="first"`. Explain what this means and describe a situation where `keep="last"` would be more appropriate. What business rule would justify keeping the most recent duplicate rather than the first?

**Question B3 (9 points):** After running the code, report: (1) the number of rows removed by deduplication, (2) the null count for each column after all fills, and (3) confirm whether your Part A row count prediction was correct.

### Part B Deliverable

Code output screenshots, written answers to B1 through B3.

---

## Part C — Standardization (25 points)

### Part C Instructions

Fix the formatting inconsistencies in the `region`, `first_name`, and `signup_date` columns.

```python
# Standardize region: strip whitespace, title case, replace "N/A" with "Unknown"
df_clean["region"] = df_clean["region"].str.strip().str.title()
df_clean["region"] = df_clean["region"].replace("N/A", "Unknown")

# Standardize first_name: strip whitespace, title case
df_clean["first_name"] = df_clean["first_name"].str.strip().str.title()

# Standardize signup_date to datetime
df_clean["signup_date"] = pd.to_datetime(
    df_clean["signup_date"], infer_datetime_format=True
)

# Extract year and month as derived columns
df_clean["signup_year"] = df_clean["signup_date"].dt.year
df_clean["signup_month"] = df_clean["signup_date"].dt.month

print("Region values after standardization:\n",
      df_clean["region"].value_counts(dropna=False))
print("\nSignup date sample:\n", df_clean[["signup_date", "signup_year", "signup_month"]].head())
```

### Part C Questions

**Question C1 (8 points):** Before standardization, the `region` column contained "North," "south," "NORTH," and "  south  " — all representing the same two regions. What would happen if you tried to count customers per region before standardization? Demonstrate by running `df["region"].value_counts()` on the original dataframe and comparing to the standardized output.

**Question C2 (9 points):** The `signup_date` column originally contained three different date string formats. Why is storing dates as strings rather than datetime objects a problem for analytics? List three specific analytical operations that require proper datetime type, and explain what would go wrong if the column remained a string.

**Question C3 (8 points):** The code extracts `signup_year` and `signup_month` as derived columns. Name two additional derived columns you could create from `signup_date` that would be useful for a retail analytics dashboard, and write the pandas code to create them.

### Part C Deliverable

Code output screenshots and written answers to C1 through C3.

---

## Part D — Outlier Detection (20 points)

### Part D Instructions

Apply the IQR method to detect outliers in the `purchase_amount` and `age` columns.

```python
def flag_outliers(series, col_name):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = series[(series < lower) | (series > upper)]
    print(f"\n{col_name}: Q1={Q1:.2f}, Q3={Q3:.2f}, IQR={IQR:.2f}")
    print(f"  Lower bound: {lower:.2f}, Upper bound: {upper:.2f}")
    print(f"  Outlier values: {outliers.values}")
    return lower, upper

pa_low, pa_high = flag_outliers(df_clean["purchase_amount"], "purchase_amount")
age_low, age_high = flag_outliers(df_clean["age"], "age")
```

### Part D Questions

**Question D1 (7 points):** The `purchase_amount` column contains 99999.00. The IQR method will flag this as an outlier. Is this value likely a data error, or could it represent a legitimate purchase? Explain your reasoning. What additional information would you need to make a confident decision? What action would you take for this lab, and why?

**Question D2 (7 points):** The `age` column contains 300. Apply the IQR formula manually (show your arithmetic) and confirm whether 300 is flagged as an outlier. Is this a legitimate value? What is the appropriate action, and why?

**Question D3 (6 points):** Remove confirmed erroneous outliers and document the final row count. Write the code to filter out rows where `age` exceeds the upper bound. Report the final `purchase_amount` and `age` `describe()` output after removal.

### Part D Deliverable

Code output, manual IQR calculation for D2, and written answers to D1 through D3.

---

## Part E — Validation and Final Report (15 points)

### Part E Instructions

Run the following validation suite on your fully cleaned dataset.

```python
print("=== Final Validation Report ===")

print(f"\nFinal row count: {len(df_clean)}")
print(f"Original row count: {len(df)}")
print(f"Rows removed: {len(df) - len(df_clean)}")

print("\nNull check:")
print(df_clean.isnull().sum())

valid_regions = {"North", "South", "East", "West", "Unknown"}
actual_regions = set(df_clean["region"].unique())
print(f"\nRegion validation: {actual_regions}")
print(f"All regions valid: {actual_regions.issubset(valid_regions)}")

print(f"\nAge range check (0-120): {df_clean['age'].between(0, 120).all()}")
print(f"Min age: {df_clean['age'].min()}, Max age: {df_clean['age'].max()}")

print(f"\nPurchase amount range (>=0): {(df_clean['purchase_amount'] >= 0).all()}")
print(f"\nDuplicate check: {df_clean.duplicated(subset=['email']).sum()} duplicates")

print("\n=== Cleaned Dataset Summary ===")
print(df_clean.describe())
```

### Part E Questions

**Question E1 (7 points):** Write a brief data cleaning summary (150–200 words) as if you were reporting to a project stakeholder — not a technical audience. Describe what problems were found, what actions were taken, and what the analyst can now trust about the cleaned dataset. Do not use Python syntax in this section.

**Question E2 (8 points):** Identify one data quality problem in this dataset that was NOT fixed by the cleaning steps in Parts B through D. Describe the problem, explain why it was not addressed, and propose a fix. Write the Python code that would implement your proposed fix.

### Part E Deliverable

Validation output, written answers to E1 and E2.

---

## Submission Instructions

Compile all parts into a single PDF or Word document. Name your file: `Lab03_LastName_FirstName.pdf`. Submit to Canvas before the stated deadline.

---

## Grading Rubric Summary

| Part | Description | Points |
|---|---|---|
| A | Dataset Profiling | 15 |
| B | Missing Values and Deduplication | 25 |
| C | Standardization | 25 |
| D | Outlier Detection | 20 |
| E | Validation and Final Report | 15 |
| **Total** | | **100** |

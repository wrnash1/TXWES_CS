# Lab: Module 12 — Python for Data Analysis

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Lab Overview

In this lab you will build a complete data analysis pipeline in a Jupyter notebook. You will load a synthetic retail sales dataset, inspect and clean it, answer three business questions using groupby and pivot_table, and produce two publication-quality charts. Each step mirrors the workflow used by professional data analysts.

**Estimated time:** 90 minutes

**Tools required:** Python 3.10+, JupyterLab or VS Code with Jupyter extension, pandas, NumPy, matplotlib, seaborn (all included in Anaconda)

**Dataset:** `sales_data_module12.csv` — download from the course LMS (5,000 rows, 8 columns)

---

### Learning Objectives

By completing this lab you will be able to:

* Load and inspect a CSV dataset with pandas
* Identify and resolve null values and outliers
* Use groupby, merge, and pivot_table to answer business questions
* Produce a bar chart and a correlation heatmap with seaborn
* Document findings in a Jupyter notebook with markdown cells

---

### Dataset Schema

| Column | Type | Description |
|---|---|---|
| order_id | int | Unique order identifier |
| region | str | Sales region (North, South, East, West) |
| product | str | Product category |
| quarter | str | Fiscal quarter (Q1–Q4) |
| units | float | Units sold (contains nulls) |
| revenue | float | Revenue in USD (contains nulls and outliers) |
| cost | float | Cost of goods sold |
| rep_id | int | Sales representative ID |

---

### Part 1: Environment Setup and Data Loading (15 minutes)

#### Step 1.1 — Create a New Notebook

Open JupyterLab and create a new notebook named `module12_lab.ipynb`.

#### Step 1.2 — Import Libraries

In the first code cell, import all required libraries:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)
sns.set_theme(style='whitegrid')
print("Libraries loaded successfully.")
```

#### Step 1.3 — Load the Dataset

```python
df = pd.read_csv('sales_data_module12.csv')
print(f"Shape: {df.shape}")
df.head()
```

**Checkpoint question 1:** How many rows and columns does the dataset have? Record this in a markdown cell below the output.

#### Step 1.4 — Initial Inspection

```python
print("Data types:")
print(df.dtypes)
print("\nDescriptive statistics:")
df.describe()
```

```python
print("Null counts per column:")
print(df.isnull().sum())
print(f"\nDuplicate rows: {df.duplicated().sum()}")
```

**Checkpoint question 2:** Which columns have null values? What percentage of values are missing in each?

---

### Part 2: Data Cleaning (20 minutes)

#### Step 2.1 — Calculate and Document Null Percentages

```python
null_summary = pd.DataFrame({
    'null_count': df.isnull().sum(),
    'null_pct': (df.isnull().sum() / len(df) * 100).round(2)
})
null_summary[null_summary['null_count'] > 0]
```

#### Step 2.2 — Handle Missing Values

Apply the following strategy and add a markdown cell explaining your reasoning for each choice:

```python
# Fill missing units with 0 (structural zero — no units sold)
df['units'] = df['units'].fillna(0)

# Fill missing revenue with the column median
median_revenue = df['revenue'].median()
df['revenue'] = df['revenue'].fillna(median_revenue)

print(f"Remaining nulls: {df.isnull().sum().sum()}")
```

#### Step 2.3 — Remove Duplicate Rows

```python
before = len(df)
df = df.drop_duplicates()
after = len(df)
print(f"Removed {before - after} duplicate rows.")
```

#### Step 2.4 — Detect and Flag Revenue Outliers

```python
Q1 = df['revenue'].quantile(0.25)
Q3 = df['revenue'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df['revenue_outlier'] = (
    (df['revenue'] < lower_bound) | (df['revenue'] > upper_bound)
)

print(f"Outliers detected: {df['revenue_outlier'].sum()}")
print(f"Outlier rate: {df['revenue_outlier'].mean() * 100:.1f}%")
```

**Checkpoint question 3:** How many outliers were detected? Do you think they should be removed or kept? Add a markdown cell with your reasoning.

#### Step 2.5 — Create a Clean Working DataFrame

For analysis, exclude flagged outliers:

```python
df_clean = df[df['revenue_outlier'] == False].copy()
print(f"Clean dataset shape: {df_clean.shape}")
```

---

### Part 3: Business Questions (30 minutes)

#### Step 3.1 — Question 1: Total Revenue by Region

Use groupby to calculate total and average revenue per region, then rank by total:

```python
by_region = df_clean.groupby('region').agg(
    total_revenue=('revenue', 'sum'),
    avg_revenue=('revenue', 'mean'),
    order_count=('order_id', 'count')
).reset_index().sort_values('total_revenue', ascending=False)

by_region['total_revenue'] = by_region['total_revenue'].round(2)
by_region['avg_revenue'] = by_region['avg_revenue'].round(2)
by_region
```

**Checkpoint question 4:** Which region has the highest total revenue? Which has the highest average revenue per order? Are they the same region?

#### Step 3.2 — Question 2: Revenue by Region and Quarter (pivot_table)

```python
pivot = df_clean.pivot_table(
    values='revenue',
    index='region',
    columns='quarter',
    aggfunc='sum',
    fill_value=0
).round(2)

pivot
```

**Checkpoint question 5:** In which quarter did the East region perform best? Which region shows the most consistent revenue across all four quarters?

#### Step 3.3 — Question 3: Profit Margin by Product

Calculate profit (revenue minus cost) and margin percentage:

```python
df_clean['profit'] = df_clean['revenue'] - df_clean['cost']
df_clean['margin_pct'] = (df_clean['profit'] / df_clean['revenue'] * 100).round(2)

by_product = df_clean.groupby('product').agg(
    avg_margin=('margin_pct', 'mean'),
    total_profit=('profit', 'sum'),
    total_revenue=('revenue', 'sum')
).reset_index().sort_values('avg_margin', ascending=False)

by_product
```

**Checkpoint question 6:** Which product has the highest average profit margin? Which has the lowest?

---

### Part 4: Visualization (20 minutes)

#### Step 4.1 — Bar Chart: Total Revenue by Region

```python
fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(
    data=by_region,
    x='region',
    y='total_revenue',
    palette='Blues_d',
    ax=ax
)
ax.set_title('Total Revenue by Region', fontsize=14, fontweight='bold')
ax.set_xlabel('Region')
ax.set_ylabel('Total Revenue ($)')
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'${x:,.0f}')
)
plt.tight_layout()
plt.savefig('revenue_by_region.png', dpi=150)
plt.show()
```

#### Step 4.2 — Correlation Heatmap

```python
numeric_cols = df_clean[['units', 'revenue', 'cost', 'profit', 'margin_pct']]
corr = numeric_cols.corr()

fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(
    corr,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    center=0,
    linewidths=0.5,
    ax=ax
)
ax.set_title('Correlation Matrix — Sales Variables', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=150)
plt.show()
```

**Checkpoint question 7:** What is the correlation between revenue and profit? Is this what you expected? What does the correlation between units and revenue tell you?

---

### Part 5: Summary and Reflection (5 minutes)

Add a final markdown cell to your notebook with the following structure:

```text
## Lab Summary

### Key Findings
- [Finding 1 from regional analysis]
- [Finding 2 from quarterly pivot]
- [Finding 3 from margin analysis]

### Data Quality Issues Addressed
- [Null handling decisions and rationale]
- [Outlier count and treatment decision]

### What I Would Investigate Next
- [One analytical question this lab raised that you did not answer]
```

---

### Submission Instructions

Export your completed notebook as both `.ipynb` and PDF (File > Save and Export Notebook As > PDF). Submit both files to the course LMS by the due date. Ensure all cells have been executed and outputs are visible.

---

### Grading Rubric

| Criterion | Points |
|---|---|
| Libraries imported and dataset loaded correctly | 10 |
| Null handling with correct strategy and markdown justification | 15 |
| Outlier detection with IQR method implemented correctly | 15 |
| groupby aggregation answers business questions correctly | 20 |
| pivot_table output is correct with fill_value=0 | 10 |
| Bar chart rendered with labels, title, and axis formatting | 15 |
| Correlation heatmap rendered with annotations | 10 |
| Summary markdown cell with findings | 5 |
| **Total** | **100** |

---

### Troubleshooting

* If `read_csv` raises a `FileNotFoundError`, verify the CSV is in the same folder as your notebook or provide the full file path.
* If `seaborn` is not found, run `pip install seaborn` in a terminal or `!pip install seaborn` in a notebook cell.
* If the PDF export fails, install `nbconvert` and a LaTeX engine, or export as HTML instead.

---

## Part 9 — Challenge Exercise

### Challenge 1: Automated EDA Report Function

Build a reusable function `eda_report(df)` that produces a standardized exploratory data analysis summary for any pandas DataFrame.

1. The function should print the following sections: (a) Shape and dtypes, (b) Null value counts and percentages per column, (c) Descriptive statistics for all numeric columns via `describe()`, (d) For each numeric column: skewness value and a one-line classification ('symmetric', 'right-skewed', or 'left-skewed' using `|skew| < 0.5` as the symmetric threshold), and (e) For each categorical column: the top 3 most frequent values and their counts.
2. Apply `eda_report()` to the lab dataset. Then add a feature engineering step: create a `revenue_per_unit` column (revenue / units_sold, with `np.nan` where units_sold is 0), and re-run `eda_report()` on just the numeric columns. Write two sentences describing what the skewness of `revenue_per_unit` reveals about the distribution of per-unit revenue in the dataset.

```python
import pandas as pd
import numpy as np

def eda_report(df):
    print(f"=== Shape: {df.shape} ===")
    print(df.dtypes.to_string())

    print("\n=== Null Summary ===")
    null_pct = (df.isnull().sum() / len(df) * 100).round(2)
    null_df = pd.DataFrame({"nulls": df.isnull().sum(), "pct": null_pct})
    print(null_df[null_df["nulls"] > 0].to_string() if null_df["nulls"].sum() > 0
          else "No nulls found.")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(include="object").columns.tolist()

    if numeric_cols:
        print("\n=== Descriptive Statistics (Numeric) ===")
        print(df[numeric_cols].describe().round(2).to_string())
        print("\n=== Skewness ===")
        for col in numeric_cols:
            sk = df[col].skew()
            label = ("symmetric" if abs(sk) < 0.5
                     else "right-skewed" if sk > 0 else "left-skewed")
            print(f"  {col}: {sk:.3f} ({label})")

    if cat_cols:
        print("\n=== Top 3 Categorical Values ===")
        for col in cat_cols:
            print(f"\n  {col}:")
            print(df[col].value_counts().head(3).to_string())
```

### Challenge 2: Time-Series Feature Engineering

Extend the lab dataset with date-based feature engineering and visualize monthly trends with multiple series.

1. If the lab dataset includes an `order_date` column, convert it to datetime and extract: `year`, `month`, `quarter`, `day_of_week` (0=Monday), and `is_weekend` (True/False). If the lab dataset does not have a date column, add a synthetic one by generating 100 random dates in 2024 using `pd.date_range('2024-01-01', '2024-12-31')` randomly sampled. Group by `year` and `month`, computing total revenue and order count per month. Plot a dual-axis line chart: revenue on the left y-axis and order count on the right y-axis. Save as `monthly_trends.png`.
2. Create a `day_of_week_summary` groupby aggregation showing average revenue and order count for each day of the week. Sort by day number (0–6). Plot a bar chart with day names on the x-axis. Save as `dow_revenue.png`. Write two sentences explaining which day of the week appears to be highest-revenue and what a business analyst might do with this insight for staffing or marketing planning.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# If your df already has order_date, skip the synthetic generation
np.random.seed(42)
n = len(df)
df["order_date"] = pd.to_datetime(
    np.random.choice(pd.date_range("2024-01-01", "2024-12-31"), size=n)
)

df["year"]        = df["order_date"].dt.year
df["month"]       = df["order_date"].dt.month
df["quarter"]     = df["order_date"].dt.quarter
df["day_of_week"] = df["order_date"].dt.dayofweek
df["is_weekend"]  = df["day_of_week"] >= 5

monthly = (
    df.groupby(["year", "month"])
    .agg(total_revenue=("revenue", "sum"), order_count=("revenue", "count"))
    .reset_index()
    .sort_values(["year", "month"])
)
monthly["period"] = monthly["year"].astype(str) + "-" + monthly["month"].astype(str).str.zfill(2)

fig, ax1 = plt.subplots(figsize=(11, 5))
ax2 = ax1.twinx()
ax1.plot(monthly["period"], monthly["total_revenue"], color="steelblue",
         marker="o", linewidth=2, label="Revenue")
ax2.plot(monthly["period"], monthly["order_count"], color="darkorange",
         marker="s", linewidth=2, linestyle="--", label="Order Count")
ax1.set_ylabel("Total Revenue ($)", color="steelblue")
ax2.set_ylabel("Order Count", color="darkorange")
ax1.set_title("Monthly Revenue and Order Count (2024)", fontsize=13, fontweight="bold")
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
plt.xticks(rotation=40, ha="right")
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.tight_layout()
plt.savefig("monthly_trends.png", dpi=150)
plt.show()

day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
dow = (
    df.groupby("day_of_week")
    .agg(avg_revenue=("revenue", "mean"), order_count=("revenue", "count"))
    .reset_index()
)
dow["day_name"] = dow["day_of_week"].map(dict(enumerate(day_names)))

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(dow["day_name"], dow["avg_revenue"], color="steelblue")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax.set_title("Average Revenue by Day of Week", fontsize=13, fontweight="bold")
ax.set_xlabel("Day of Week")
ax.set_ylabel("Average Revenue ($)")
plt.tight_layout()
plt.savefig("dow_revenue.png", dpi=150)
plt.show()
```

### Reflection Questions

1. In Challenge 1, the `eda_report()` function uses `|skew| < 0.5` as the threshold for calling a distribution symmetric. Is this threshold universally appropriate? Describe a domain (e.g., financial risk modeling, healthcare) where you would use a stricter threshold and explain why the choice of skewness threshold matters for downstream analytical decisions.
2. In Challenge 2, you created `is_weekend` as a boolean feature. In a machine learning context, boolean features often need to be converted to integers (0/1) before being passed to a model. What pandas method would you use for this conversion, and what is the risk of leaving boolean features unconverted in a scikit-learn pipeline?

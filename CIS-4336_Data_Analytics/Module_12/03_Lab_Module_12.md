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

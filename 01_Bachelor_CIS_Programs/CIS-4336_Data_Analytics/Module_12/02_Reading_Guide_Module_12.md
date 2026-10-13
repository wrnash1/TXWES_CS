# Reading Guide: Module 12 — Python for Data Analysis

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


## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Introduction

Welcome to **Module 12 — Python for Data Analysis**. Python has displaced spreadsheet tools as the primary instrument for professional data work because it combines the expressiveness of a general-purpose programming language with a rich ecosystem of specialized libraries. This reading guide covers the four libraries you must know for the CompTIA Data+ exam and for daily analyst work: **pandas**, **NumPy**, **matplotlib**, and **seaborn**. You will also learn systematic approaches to data cleaning, null handling, and outlier detection — tasks that consume the majority of a real analyst's time.

No prior Python experience is assumed. If you are brand new to Python, work through the optional primer linked in the course LMS before this module. If you have written Python before but not for data analysis, this guide will feel like familiar ground with new vocabulary.

---

### Learning Objectives

By the end of this module you will be able to:

* Create, filter, and transform pandas DataFrames
* Apply groupby, merge, and pivot_table to answer business questions
* Perform vectorized array operations with NumPy
* Produce line, bar, scatter, histogram, and heatmap charts
* Identify and handle missing values using at least two strategies
* Detect outliers using the IQR method and boxplot visualization
* Map Python tools to their corresponding Data+ exam domains

---

### Section 1: The Python Data Analysis Stack

#### Why Python Dominates Analytics

Python succeeded in data analysis for three structural reasons: open-source licensing with no cost barrier, a package ecosystem that grew to cover every analytical task, and a syntax that is readable enough for non-programmers to maintain analysis scripts. The four libraries in this module form the foundation of that ecosystem.

| Library | Primary Purpose | Built On |
|---|---|---|
| NumPy | Fast numerical arrays and math | C extensions |
| pandas | Tabular data manipulation | NumPy |
| matplotlib | Low-level 2D plotting | Rendering backends |
| seaborn | Statistical visualization | matplotlib + pandas |

You install all four with a single command in the Anaconda environment:

```bash
conda install pandas numpy matplotlib seaborn
```

Or with pip:

```bash
pip install pandas numpy matplotlib seaborn
```

#### The Jupyter Notebook Environment

Jupyter notebooks (`.ipynb` files) are the standard environment for exploratory data analysis. A notebook combines code cells, markdown cells, and output — charts, tables, and text — in a single scrollable document. This makes analysis reproducible and shareable. When you export a notebook to PDF or HTML, stakeholders see both the code and the results without needing Python installed.

---

### Section 2: pandas DataFrames

#### Creating DataFrames

A DataFrame is a two-dimensional, labeled data structure with columns of potentially different types. You can create one from a dictionary, a list of lists, or most commonly from an external file:

```python
import pandas as pd

# From a CSV file
df = pd.read_csv('sales.csv')

# From an Excel file
df = pd.read_excel('sales.xlsx', sheet_name='Q1')

# From a dictionary
df = pd.DataFrame({
    'Region': ['North', 'South', 'East'],
    'Revenue': [120000, 95000, 140000]
})
```

#### Exploring a New DataFrame

Before any analysis, run these commands on every new dataset:

```python
df.shape           # (rows, columns)
df.dtypes          # data type of each column
df.head(10)        # first 10 rows
df.describe()      # count, mean, std, min, quartiles, max for numeric cols
df.isnull().sum()  # null count per column
```

This five-step exploration takes under a minute and prevents downstream errors from wrong assumptions about the data.

#### Filtering Rows

Boolean indexing selects rows meeting a condition:

```python
high_revenue = df[df['Revenue'] > 100000]
q1_north = df[(df['Quarter'] == 'Q1') & (df['Region'] == 'North')]
```

The `&` operator combines conditions. Use `|` for OR. Always wrap each condition in parentheses when combining.

#### Adding and Transforming Columns

```python
df['Revenue_Thousands'] = df['Revenue'] / 1000
df['Margin_Pct'] = (df['Profit'] / df['Revenue']) * 100
df['Category'] = df['Revenue'].apply(lambda x: 'High' if x > 100000 else 'Low')
```

`apply()` runs a function on every row, which is useful for custom logic that cannot be expressed as a simple arithmetic operation.

---

### Section 3: groupby, merge, and pivot_table

#### groupby — Aggregate Within a Table

groupby splits a DataFrame into groups based on one or more columns, applies an aggregation function, and combines the results:

```python
# Total revenue by region
by_region = df.groupby('Region')['Revenue'].sum().reset_index()

# Multiple aggregations at once
summary = df.groupby('Region').agg(
    Total_Revenue=('Revenue', 'sum'),
    Avg_Units=('Units', 'mean'),
    Count=('Revenue', 'count')
).reset_index()
```

The `agg()` method with named aggregations is the professional pattern — it produces columns with clear names rather than ambiguous multi-level indexes.

#### merge — Combine Two Tables

merge is equivalent to a SQL JOIN. The most important parameter is `how`:

| how value | SQL equivalent | Behavior |
|---|---|---|
| `'inner'` | INNER JOIN | Keep only rows matching in both tables |
| `'left'` | LEFT OUTER JOIN | Keep all left rows; NaN where no right match |
| `'right'` | RIGHT OUTER JOIN | Keep all right rows; NaN where no left match |
| `'outer'` | FULL OUTER JOIN | Keep all rows from both tables |

```python
orders_with_customer = pd.merge(
    orders,
    customers,
    on='CustomerID',
    how='left'
)
```

A left join is the most common in reporting because it preserves every transaction even when the customer record is incomplete.

#### pivot_table — Reshape from Long to Wide

Long format: one row per observation. Wide format: one row per entity, columns are categories. Reporting usually needs wide format.

```python
wide = df.pivot_table(
    values='Revenue',
    index='Region',
    columns='Quarter',
    aggfunc='sum',
    fill_value=0
)
```

`fill_value=0` is critical: without it, region-quarter combinations with no data become NaN, which breaks subsequent arithmetic.

---

### Section 4: NumPy Arrays

#### ndarray Fundamentals

A NumPy ndarray is a fixed-type, fixed-size array stored in contiguous memory. Because all elements share one type, NumPy can execute operations using compiled C code — orders of magnitude faster than Python loops.

```python
import numpy as np

arr = np.array([1.5, 2.3, 4.1, 0.8, 3.7])
print(arr.dtype)   # float64
print(arr.shape)   # (5,)
```

#### Vectorized Operations

Any arithmetic operator applied to an array applies element-wise with no loop:

```python
arr * 2         # multiply every element by 2
arr + 10        # add 10 to every element
np.sqrt(arr)    # square root of every element
arr > 2.0       # boolean array: True where element > 2.0
```

#### Statistical Functions

```python
np.mean(arr)
np.median(arr)
np.std(arr)
np.var(arr)
np.percentile(arr, [25, 50, 75])
np.min(arr)
np.max(arr)
```

#### np.where — Conditional Replacement

```python
# Replace values above 3.0 with 3.0 (capping outliers)
capped = np.where(arr > 3.0, 3.0, arr)
```

This pattern appears frequently in feature engineering and outlier treatment.

---

### Section 5: Visualization with matplotlib and seaborn

#### matplotlib Basics

matplotlib uses a figure-axes model. A figure is the overall canvas; axes are the individual chart panels inside it. Most code uses the `pyplot` interface, which manages figures implicitly:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Month'], df['Revenue'], color='steelblue', linewidth=2)
ax.set_title('Monthly Revenue')
ax.set_xlabel('Month')
ax.set_ylabel('Revenue ($)')
plt.tight_layout()
plt.savefig('revenue_trend.png', dpi=150)
plt.show()
```

`tight_layout()` prevents axis labels from being clipped. `savefig()` exports the chart as a file.

#### seaborn Chart Types and When to Use Them

| Chart type | seaborn function | Best for |
|---|---|---|
| Bar chart | `sns.barplot()` | Comparing category means |
| Count chart | `sns.countplot()` | Frequency of categories |
| Box plot | `sns.boxplot()` | Distribution and outlier detection |
| Histogram | `sns.histplot()` | Distribution of a numeric variable |
| Scatter plot | `sns.scatterplot()` | Relationship between two numeric variables |
| Heatmap | `sns.heatmap()` | Correlation matrix or pivot table |
| Violin plot | `sns.violinplot()` | Distribution shape across categories |
| Line chart | `sns.lineplot()` | Trends over time |

#### Correlation Heatmap Pattern

```python
import seaborn as sns
import matplotlib.pyplot as plt

corr = df.select_dtypes(include='number').corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0)
plt.title('Feature Correlation Matrix')
plt.tight_layout()
plt.show()
```

`annot=True` prints the coefficient in each cell. `center=0` ensures white represents zero correlation.

---

### Section 6: Data Cleaning

#### The Data Quality Dimensions (Data+ Exam Concept)

The Data+ exam frames data quality along six dimensions:

* **Completeness** — are all required values present?
* **Consistency** — does the data contradict itself?
* **Accuracy** — does the data reflect reality?
* **Validity** — do values conform to the expected format or range?
* **Uniqueness** — are records duplicated?
* **Timeliness** — is the data current enough for the use case?

Null handling addresses completeness. Outlier treatment addresses accuracy and validity.

#### Handling Missing Values

Step 1 — measure the problem:

```python
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
pd.DataFrame({'count': missing, 'pct': missing_pct}).query('count > 0')
```

Step 2 — choose a strategy based on the column and the percentage missing:

| Scenario | Strategy | pandas method |
|---|---|---|
| Less than 5% missing, numeric | Drop the rows | `df.dropna(subset=['col'])` |
| Less than 5% missing, categorical | Fill with mode | `df['col'].fillna(df['col'].mode()[0])` |
| 5–30% missing, numeric | Fill with median | `df['col'].fillna(df['col'].median())` |
| More than 30% missing | Consider dropping the column | `df.drop(columns=['col'])` |
| Structural zero (e.g., no sales) | Fill with 0 | `df['col'].fillna(0)` |

#### Detecting and Handling Outliers

The IQR method:

```python
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return df[(df[column] >= lower) & (df[column] <= upper)]
```

The Z-score method (for normally distributed data):

```python
from scipy import stats
z_scores = np.abs(stats.zscore(df['Revenue']))
df_clean = df[z_scores < 3]
```

Z-scores flag observations more than 3 standard deviations from the mean. Use IQR for skewed distributions; Z-score for roughly normal distributions.

#### Deduplication

```python
print(df.duplicated().sum())
df = df.drop_duplicates()
df = df.drop_duplicates(subset=['OrderID'])
```

---

### Section 7: Data+ Exam Connections

Python-related questions on the DA0-001 exam are conceptual, not syntactic. You will not be asked to read code and execute it mentally. You will be asked:

* Which library is best suited for a described task
* What a described operation does (e.g., "merging on a shared key")
* Why imputation is preferred over dropping in some scenarios
* What a correlation coefficient value indicates
* How to interpret a boxplot

The key mappings for exam preparation are:

| Exam concept | Python tool |
|---|---|
| Data transformation | pandas (rename, apply, astype) |
| Aggregation | pandas groupby and agg |
| Joining datasets | pandas merge |
| Statistical summary | NumPy statistical functions |
| Trend visualization | matplotlib or seaborn line chart |
| Distribution analysis | seaborn histplot or boxplot |
| Correlation analysis | seaborn heatmap of df.corr() |
| Missing value treatment | pandas fillna and dropna |
| Outlier detection | IQR method or Z-score |

---

### Key Terms

* **pandas** — Python library for tabular data manipulation built on NumPy.
* **DataFrame** — pandas' two-dimensional labeled data structure analogous to a database table.
* **groupby** — pandas method that splits a DataFrame by group, applies an aggregation, and returns a summary.
* **merge** — pandas method for combining two DataFrames on a shared key column; equivalent to a SQL JOIN.
* **pivot_table** — reshapes a DataFrame from long format to wide format by spreading category values across columns.
* **NumPy** — Python library for fast numerical array computation using vectorized C operations.
* **ndarray** — NumPy's N-dimensional array; every element shares a single data type.
* **vectorization** — executing an operation on all elements of an array simultaneously without a Python loop.
* **matplotlib** — Python's foundational 2D plotting library; provides low-level control over every chart element.
* **seaborn** — statistical visualization library built on matplotlib; produces polished charts with fewer lines of code.
* **imputation** — replacing missing values with a computed substitute such as mean, median, or mode.
* **IQR (Interquartile Range)** — Q3 minus Q1; the range of the middle 50% of data; used to define outlier boundaries.
* **outlier** — an observation that falls abnormally far from the center of a distribution; may represent an error or a genuine extreme.
* **correlation coefficient** — a number between -1 and 1 measuring the linear relationship between two variables.

---

### Review Questions

1. What is the difference between `df.dropna()` and `df.fillna()`? When would you choose each?

2. Explain the difference between a pandas `merge` with `how='inner'` and `how='left'`. Give a business scenario for each.

3. A colleague says "just remove all outliers before analysis." What is wrong with this blanket rule?

4. You have a correlation coefficient of 0.92 between advertising spend and sales revenue. What does this tell you, and what does it not tell you?

5. Why is NumPy faster than a Python for-loop for the same arithmetic operation?

---

### OER Resources

* **pandas documentation** — [pandas.pydata.org/docs](https://pandas.pydata.org/docs/)
* **NumPy documentation** — [numpy.org/doc](https://numpy.org/doc/)
* **seaborn documentation** — [seaborn.pydata.org](https://seaborn.pydata.org/)
* **Python for Data Analysis (free chapters)** — Wes McKinney, O'Reilly
* **freeCodeCamp Data Analysis with Python** — [freecodecamp.org/learn](https://www.freecodecamp.org/learn/data-analysis-with-python/)

---

## 9. Supplemental Resources

**1. Kaggle Learn — Pandas (Free Interactive Course)**
<https://www.kaggle.com/learn/pandas>
A free, hands-on Kaggle micro-course covering DataFrame creation, indexing, groupby, merging, and data type manipulation with live coding exercises. Directly reinforces the pandas operations covered in Module 12 with immediate feedback in a browser-based environment.

**2. Real Python — Pandas GroupBy: Your Guide to Grouping Data in Python**
<https://realpython.com/pandas-groupby>
An in-depth tutorial covering `groupby`, `agg`, `transform`, and `apply` with practical examples. Essential for understanding the full capabilities of grouped aggregations beyond what a single reference page covers, supporting the groupby-heavy analytical techniques in this module.

**3. Towards Data Science — Exploratory Data Analysis with Python (Seaborn and Matplotlib)**
<https://towardsdatascience.com/exploratory-data-analysis-with-pandas-508a93f8c3c5>
A walkthrough of a complete EDA workflow using pandas, matplotlib, and seaborn — covering histograms, pairplots, correlation heatmaps, and box plots. Bridges the gap between individual function calls and a full analytical workflow, matching the lab deliverables in Module 12.

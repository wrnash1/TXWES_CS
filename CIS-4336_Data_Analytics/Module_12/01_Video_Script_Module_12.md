# Video Script: Module 12 — Python for Data Analysis

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

**Estimated Duration:** 18–22 minutes

---

### [00:00 – 02:00] Introduction

**Visual:** Instructor on camera with title card: **Python for Data Analysis**.

**Audio:** "Welcome to Module 12. This week we move from concepts into code. Python has become the dominant language for data analysis in professional environments, and the CompTIA Data+ exam expects you to understand what Python tools exist and what problems they solve. By the end of this module you will be able to manipulate DataFrames with pandas, perform array math with NumPy, build charts with matplotlib and seaborn, clean messy data, and handle nulls and outliers. Let's get started."

**Study Link:** [Python for Data Analysis — freeCodeCamp Full Course](https://www.youtube.com/watch?v=r-uOLxNrNk8)

---

### [02:00 – 05:00] Why Python for Data Analysis?

**Visual:** Slide comparing Excel, SQL, Python, and R on four axes: scalability, automation, visualization, and statistical depth.

**Alt-text:** A four-quadrant matrix placing Python in the high-scalability and high-automation quadrant alongside R, while Excel sits in the low-scalability zone.

**Audio:** "Before we open a code editor, let's answer the question every new analyst asks — why Python? Excel is excellent for small datasets and ad-hoc exploration. SQL is ideal for querying relational databases. But when you need to automate a monthly report that processes 10 million rows, apply a custom cleaning function across 50 columns, or produce a reproducible chart that updates when the data changes — Python is the right tool. The two core libraries you will use daily are **pandas** for tabular data and **NumPy** for numerical computation. On top of those sit **matplotlib** and **seaborn** for visualization. All four libraries are free, open-source, and included in the Anaconda distribution, which we use in this course."

**Transition:** "Let's look at pandas first."

---

### [05:00 – 09:30] pandas — DataFrames, groupby, merge, pivot

**Visual:** VS Code split-screen showing a Jupyter notebook on the left and a rendered DataFrame table on the right.

**Alt-text:** Jupyter notebook cell output displaying a five-column sales DataFrame with columns Region, Product, Quarter, Units, and Revenue.

**Audio:** "A DataFrame is pandas' core data structure. Think of it as a spreadsheet inside Python — rows and columns, each column typed. You create one from a CSV like this:

```python
import pandas as pd
df = pd.read_csv('sales.csv')
print(df.head())
```

The `head()` method shows the first five rows. That is your first sanity check — does the data look right?

**groupby** answers questions like 'what is total revenue by region?' You chain it with an aggregation:

```python
df.groupby('Region')['Revenue'].sum().reset_index()
```

`reset_index()` turns the grouped result back into a flat DataFrame, which is easier to work with downstream.

**merge** is pandas' version of a SQL JOIN. If you have a customers table and an orders table sharing a CustomerID column:

```python
result = pd.merge(customers, orders, on='CustomerID', how='left')
```

The `how='left'` keeps every customer even if they have no orders — identical to a LEFT OUTER JOIN in SQL.

**pivot_table** reshapes data from long to wide. Imagine you want rows as regions, columns as quarters, and values as total revenue:

```python
df.pivot_table(
    values='Revenue',
    index='Region',
    columns='Quarter',
    aggfunc='sum',
    fill_value=0
)
```

`fill_value=0` replaces NaN with zero for regions that had no sales in a given quarter. This is a very common pattern in reporting pipelines."

**Checkpoint:** "Pause here and think — when would you use merge instead of groupby? Merge combines two tables on a shared key. groupby aggregates within one table. They solve different problems."

---

### [09:30 – 12:30] NumPy — Arrays and Vectorized Math

**Visual:** Side-by-side slide: a Python for-loop timing versus NumPy vectorized operation timing on 1 million numbers.

**Alt-text:** Two code blocks with execution time labels. The loop reads 2.3 seconds; the NumPy version reads 0.004 seconds.

**Audio:** "NumPy stands for Numerical Python. Its core object is the **ndarray** — an n-dimensional array where every element shares the same data type. That constraint is what makes NumPy fast: operations run in compiled C code rather than interpreted Python.

```python
import numpy as np
prices = np.array([10.5, 20.0, 15.75, 8.99])
discounted = prices * 0.9
```

That single line multiplies every element by 0.9 with no loop needed. This is called **vectorized computation**. For a data analyst the most important NumPy operations are:

- `np.mean()`, `np.median()`, `np.std()` for descriptive statistics
- `np.percentile(arr, 75)` used to detect outliers
- `np.where(condition, value_if_true, value_if_false)` for conditional replacement
- `np.nan` as NumPy's representation of a missing numeric value

pandas is built on top of NumPy, so understanding arrays makes you a significantly better pandas user. When you see a pandas Series, you are looking at a NumPy array with an index label attached to it."

---

### [12:30 – 16:30] Visualization — matplotlib and seaborn

**Visual:** Gallery of four chart types rendered in a Jupyter notebook: line, bar, histogram, and heatmap.

**Alt-text:** A two-by-two grid of charts. Top-left is a monthly revenue line chart. Top-right is a bar chart of units by product. Bottom-left is a histogram of order values. Bottom-right is a correlation heatmap with color gradient from red to blue.

**Audio:** "matplotlib is Python's foundational plotting library. seaborn is built on top of it and produces statistically-oriented, visually polished charts with less code.

A basic matplotlib line chart:

```python
import matplotlib.pyplot as plt
plt.plot(df['Month'], df['Revenue'])
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
```

The same data in seaborn requires only:

```python
import seaborn as sns
sns.lineplot(data=df, x='Month', y='Revenue')
```

seaborn handles color palettes, axis formatting, and statistical confidence intervals automatically. Use it for:

- **Distributions** with `sns.histplot()` and `sns.boxplot()`
- **Relationships** with `sns.scatterplot()` and `sns.heatmap()`
- **Categorical comparisons** with `sns.barplot()` and `sns.violinplot()`

A correlation heatmap is especially useful during exploratory analysis:

```python
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
```

This shows every pairwise correlation coefficient. Values close to 1.0 mean the two variables move together. Values close to -1.0 mean they move in opposite directions. This helps you spot multicollinearity before building any model."

---

### [16:30 – 20:30] Data Cleaning — Nulls and Outliers

**Visual:** Notebook showing a raw DataFrame with NaN values side-by-side with the cleaned version.

**Alt-text:** Before-and-after table. The before version has multiple NaN cells in the Revenue and Units columns. The after version has those cells filled or removed.

**Audio:** "Real-world data is messy. Your job as an analyst always includes cleaning before you analyze. The two biggest problems you will encounter are **missing values** — called nulls — and **outliers**.

**Handling nulls:**

```python
df.isnull().sum()                              # count nulls per column
df.dropna(subset=['Revenue'])                  # drop rows where Revenue is null
df['Units'].fillna(0, inplace=True)            # fill nulls with zero
df['Region'].fillna(df['Region'].mode()[0],    # fill with most common value
                    inplace=True)
```

The right strategy depends on the column's role. Revenue nulls might mean the sale never closed — drop those rows. Units nulls might mean zero units were sold — fill with 0.

**Detecting outliers using the IQR method:**

```python
Q1 = df['Revenue'].quantile(0.25)
Q3 = df['Revenue'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['Revenue'] < lower) | (df['Revenue'] > upper)]
```

Values outside 1.5 times the interquartile range are flagged as outliers. You then make a judgment call: are they data entry errors to remove, or legitimate extreme values to keep? A $5 million sale is not an error. A $5 billion sale in a dataset of small retail businesses almost certainly is.

A boxplot gives you a visual complement to the IQR calculation — the whiskers on a boxplot represent exactly the 1.5-IQR boundary."

---

### [20:30 – 22:00] Exam Connection and Wrap-Up

**Visual:** Data+ domain map with Domain 3 — Data Analysis — highlighted.

**Audio:** "For the Data+ exam, Python questions appear in Domain 3, Data Analysis and Statistics. You will not write code on the exam, but you will see questions about what a specific function does, which library is appropriate for a task, and how to interpret the output of a cleaning operation. Focus on knowing the purpose of each library and the difference between dropping and imputing null values. Imputation preserves sample size; dropping removes potentially important rows.

This week's lab has you building a complete analysis pipeline in a Jupyter notebook: load the dataset, clean nulls and flag outliers, aggregate with groupby, and produce two charts. Do not skip it. The hands-on repetition is what moves these concepts into long-term memory. I will see you in the lab. Good luck."

---

### Instructor Notes

- Recommended IDE: JupyterLab or VS Code with the Jupyter extension
- Dataset: Use the provided `sales_data_module12.csv` (synthetic, 5,000 rows)
- Screen resolution for recording: 1920×1080, notebook font size 16
- Pause points suggested at timestamps [09:00] and [16:30] for student reflection
- Data+ exam domains covered: Domain 3 (Data Analysis), Domain 2 (Data Mining) — cleaning segment

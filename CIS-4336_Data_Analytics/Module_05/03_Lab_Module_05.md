# Lab 05 — Statistical Foundations: Descriptive Statistics

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 3: Data Analysis

---

## Objectives

By completing this lab, you will be able to:

- Calculate mean, median, mode, standard deviation, and IQR manually and with Python
- Identify the appropriate measure for a given dataset and distribution shape
- Detect outliers using the IQR method
- Interpret box plots and histograms
- Describe distribution shape using skewness

---

## Prerequisites

- Module 05 Reading Guide completed
- Python 3.8 or later (or Google Colab)
- `pandas`, `numpy`, and `matplotlib` installed: `pip install pandas numpy matplotlib`

---

## Part A — Manual Calculation (25 points)

### Part A Instructions

Do NOT use Python for this part. Calculate all values by hand and show your work step by step. Round to two decimal places where applicable.

### Dataset A

The following values represent the number of customer support tickets resolved per day by an analyst over 11 working days:

23, 17, 31, 28, 19, 45, 22, 18, 24, 16, 42

### Part A Questions

**Question A1 (5 points):** Calculate the mean. Show the sum and division step explicitly.

**Question A2 (5 points):** Sort the dataset and identify the median. Show your sorted list and identify the position of the median.

**Question A3 (3 points):** Identify the mode, or state that no mode exists. Justify your answer.

**Question A4 (6 points):** Calculate Q1, Q3, and IQR. Show which values you split the dataset on. Then compute the outlier lower and upper bounds using the formula: Lower = Q1 minus (1.5 times IQR), Upper = Q3 plus (1.5 times IQR).

**Question A5 (6 points):** Identify any values that fall outside the outlier bounds. For each outlier, state whether you believe it represents a legitimate value or a data error, and explain your reasoning in one to two sentences.

### Part A Deliverable

Handwritten or typed step-by-step calculations. Screenshots of handwritten work are acceptable for A1 through A5.

---

## Part B — Python Descriptive Statistics (30 points)

### Part B Instructions

Run the following code to create Dataset B and compute descriptive statistics.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_b = {
    "employee_id": range(1, 31),
    "annual_salary": [
        48000, 52000, 61000, 47000, 55000, 70000, 49000, 53000,
        58000, 62000, 44000, 51000, 68000, 57000, 46000, 75000,
        50000, 59000, 63000, 48000, 145000, 54000, 67000, 43000,
        56000, 71000, 45000, 60000, 52000, 66000
    ],
    "years_experience": [
        3, 5, 8, 2, 6, 11, 4, 5, 7, 9, 1, 4, 10, 7, 2, 14,
        3, 8, 9, 3, 22, 6, 11, 1, 7, 12, 2, 8, 5, 10
    ],
    "department": [
        "Sales","Sales","IT","HR","Sales","IT","HR","Sales",
        "IT","IT","HR","Sales","IT","Sales","HR","IT",
        "Sales","IT","IT","HR","IT","Sales","IT","HR",
        "Sales","IT","HR","IT","Sales","IT"
    ]
}

df = pd.DataFrame(data_b)
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
```

### Part B Questions

**Question B1 (8 points):** Compute the full descriptive statistics for `annual_salary`. Write and run code to calculate: mean, median, mode, range, sample variance, sample standard deviation, Q1, Q3, and IQR. Present results in a formatted table.

Expected code structure:

```python
s = df["annual_salary"]
stats = {
    "Mean":   s.mean(),
    "Median": s.median(),
    "Mode":   s.mode()[0],
    "Range":  s.max() - s.min(),
    "Variance": s.var(),
    "Std Dev": s.std(),
    "Q1":     s.quantile(0.25),
    "Q3":     s.quantile(0.75),
    "IQR":    s.quantile(0.75) - s.quantile(0.25)
}
for k, v in stats.items():
    print(f"{k}: {v:,.2f}")
```

**Question B2 (7 points):** The dataset contains employee_id 21 with annual_salary of $145,000, while most salaries are in the $43,000–$75,000 range. Apply the IQR outlier method to `annual_salary`. Is $145,000 flagged as an outlier? Show the upper bound calculation. Does removing this value materially change the mean? Report both means. Does it change the median?

**Question B3 (8 points):** Compute the mean and median annual salary grouped by department. Write the pandas code and interpret the results in three to four sentences. Which department shows the largest gap between mean and median? What does that gap suggest about the salary distribution within that department?

```python
dept_stats = df.groupby("department")["annual_salary"].agg(
    mean_salary="mean",
    median_salary="median",
    count="count"
).round(2)
print(dept_stats)
```

**Question B4 (7 points):** Compute the skewness of `annual_salary` using `df["annual_salary"].skew()`. Report the value and classify the distribution as symmetric, right-skewed, or left-skewed. Explain in two to three sentences what this skewness means for which central tendency measure (mean or median) is more appropriate to report to leadership.

### Part B Deliverable

Code, output, and written answers to B1 through B4.

---

## Part C — Visualization (25 points)

### Part C Instructions

Create three visualizations for Dataset B and answer the interpretation questions.

**Visualization C1 — Histogram (8 points):**

```python
plt.figure(figsize=(9, 5))
plt.hist(df["annual_salary"], bins=10, edgecolor="black", color="steelblue")
plt.axvline(df["annual_salary"].mean(), color="red",
            linestyle="--", label=f"Mean: {df['annual_salary'].mean():,.0f}")
plt.axvline(df["annual_salary"].median(), color="green",
            linestyle="-", label=f"Median: {df['annual_salary'].median():,.0f}")
plt.title("Annual Salary Distribution")
plt.xlabel("Annual Salary ($)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("salary_histogram.png", dpi=100)
plt.show()
```

After running this code, answer: Does the histogram confirm the skewness you calculated in B4? Where does the mean appear relative to the median? What does this tell a non-technical reader about the "typical" salary?

**Visualization C2 — Box Plot (9 points):**

```python
fig, ax = plt.subplots(figsize=(7, 5))
ax.boxplot(df["annual_salary"], vert=True, patch_artist=True,
           boxprops=dict(facecolor="lightblue"),
           medianprops=dict(color="red", linewidth=2))
ax.set_title("Annual Salary Box Plot")
ax.set_ylabel("Annual Salary ($)")
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"${x:,.0f}")
)
plt.tight_layout()
plt.savefig("salary_boxplot.png", dpi=100)
plt.show()
```

After running this code, identify: (1) the approximate location of the median line, (2) the approximate Q1 and Q3 values from the box edges, (3) whether any outlier points are visible, and (4) which direction the box is shifted, indicating skew direction.

**Visualization C3 — Department Comparison (8 points):**

```python
fig, axes = plt.subplots(1, 3, figsize=(12, 5), sharey=True)
depts = df["department"].unique()
for i, dept in enumerate(sorted(depts)):
    subset = df[df["department"] == dept]["annual_salary"]
    axes[i].boxplot(subset, patch_artist=True,
                    boxprops=dict(facecolor="lightcoral"))
    axes[i].set_title(dept)
    axes[i].set_xlabel("Department")
    if i == 0:
        axes[i].set_ylabel("Annual Salary ($)")
plt.suptitle("Salary Distribution by Department")
plt.tight_layout()
plt.savefig("salary_by_dept.png", dpi=100)
plt.show()
```

After running this code, answer: Which department has the widest salary spread (largest IQR)? Which has the highest median salary? Does any department show visible skew in its box plot? Justify each answer by referencing specific visual features.

### Part C Deliverable

Three saved PNG charts plus written interpretations for C1, C2, and C3.

---

## Part D — Applied Interpretation (20 points)

### Part D Instructions

Read each scenario and answer the questions using your knowledge of descriptive statistics. No new code is required.

**Scenario D1 (7 points):** A city's annual household income has a mean of $78,000 and a median of $52,000. A local newspaper reports: "The average household in this city earns $78,000." Is this statement accurate and representative? Explain in three to four sentences using the concepts of skewness and the relationship between mean and median.

**Scenario D2 (7 points):** An analyst computes descriptive statistics for two call center teams' daily call resolution counts:

- Team A: Mean = 45, Std Dev = 3.2
- Team B: Mean = 45, Std Dev = 18.7

Both teams have the same mean. Which team is performing more consistently? Explain what the standard deviation difference means operationally and why a manager might care about this distinction even when the means are identical.

**Scenario D3 (6 points):** A dataset has Q1 = 100, Q3 = 140, and IQR = 40. A value of 220 appears in the dataset. Show whether 220 is flagged as an outlier using the 1.5 × IQR rule. Then explain in two sentences: if 220 represents a legitimate business event (an unusually large order), should it be removed? What is the risk of removing it?

### Part D Deliverable

Written answers to D1 through D3 in your submission document.

---

## Submission Instructions

Compile all deliverables into a single PDF: calculations for Part A, code and output for Parts B and C (including chart images), and written answers for Part D. Name your file: `Lab05_LastName_FirstName.pdf`. Submit to Canvas before the stated deadline.

---

## Grading Rubric Summary

| Part | Description | Points |
|---|---|---|
| A | Manual Calculation | 25 |
| B | Python Descriptive Statistics | 30 |
| C | Visualization | 25 |
| D | Applied Interpretation | 20 |
| **Total** | | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Comparative Distribution Analysis

Extend the Dataset B analysis to compare salary distributions across two dimensions simultaneously.

1. Using the `df` DataFrame from Part B, compute a summary table that shows, for each department, the following statistics for `annual_salary`: mean, median, standard deviation, IQR, skewness, and outlier count (values outside 1.5×IQR bounds). Print the table. Then add a `mean_median_gap` column defined as `mean - median` and sort by that column descending.
2. Create a 2×2 subplot figure: top-left shows a histogram of `annual_salary` colored by department (use `plt.hist()` with `alpha=0.5` for each department in a loop); top-right shows side-by-side box plots per department; bottom-left shows a scatter plot of `years_experience` vs `annual_salary` with points colored by department; bottom-right shows a bar chart of mean salary per department with error bars showing ±1 standard deviation. Save the figure as `challenge_distributions.png`.

```python
import matplotlib.pyplot as plt
import numpy as np

dept_summary = df.groupby("department")["annual_salary"].agg(
    mean="mean", median="median", std="std",
    q1=lambda x: x.quantile(0.25), q3=lambda x: x.quantile(0.75)
).assign(
    iqr=lambda d: d["q3"] - d["q1"],
    skewness=df.groupby("department")["annual_salary"].skew()
).round(2)
dept_summary["mean_median_gap"] = dept_summary["mean"] - dept_summary["median"]
print(dept_summary.sort_values("mean_median_gap", ascending=False))

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
depts = sorted(df["department"].unique())
colors = ["steelblue", "coral", "seagreen"]
for dept, color in zip(depts, colors):
    subset = df[df["department"] == dept]["annual_salary"]
    axes[0,0].hist(subset, bins=8, alpha=0.5, label=dept, color=color)
axes[0,0].set_title("Salary Histogram by Dept"); axes[0,0].legend()
dept_data = [df[df["department"]==d]["annual_salary"].values for d in depts]
axes[0,1].boxplot(dept_data, labels=depts, patch_artist=True)
axes[0,1].set_title("Box Plots by Dept")
for dept, color in zip(depts, colors):
    sub = df[df["department"]==dept]
    axes[1,0].scatter(sub["years_experience"], sub["annual_salary"],
                      label=dept, color=color, alpha=0.7)
axes[1,0].set_title("Experience vs Salary"); axes[1,0].legend()
means = [df[df["department"]==d]["annual_salary"].mean() for d in depts]
stds  = [df[df["department"]==d]["annual_salary"].std()  for d in depts]
axes[1,1].bar(depts, means, yerr=stds, capsize=5, color=colors, alpha=0.8)
axes[1,1].set_title("Mean Salary ± 1 SD")
plt.tight_layout()
plt.savefig("challenge_distributions.png", dpi=100)
plt.show()
```

### Challenge 2: Rolling Statistics for Time-Series Salary Trends

Simulate a time-series of monthly revenue figures and apply rolling window statistics.

1. Create a pandas Series of 24 monthly revenue values (simulate realistic data with an upward trend plus random noise using `np.random.seed(42)` and `np.random.normal()`). Compute the 3-month and 6-month rolling mean and standard deviation. Plot all four lines on a single chart with labeled lines. Save as `rolling_stats.png`.
2. Identify the month with the highest 3-month rolling standard deviation (most volatile 3-month window) and the month with the lowest (most stable). Write two sentences interpreting what these windows might indicate in a real business context.

```python
np.random.seed(42)
months = pd.date_range("2022-01", periods=24, freq="MS")
revenue = pd.Series(
    50000 + np.arange(24) * 1000 + np.random.normal(0, 5000, 24),
    index=months
)
r3_mean = revenue.rolling(3).mean()
r6_mean = revenue.rolling(6).mean()
r3_std  = revenue.rolling(3).std()
r6_std  = revenue.rolling(6).std()

plt.figure(figsize=(12, 5))
plt.plot(revenue, label="Monthly Revenue", color="gray", alpha=0.6)
plt.plot(r3_mean, label="3-mo Rolling Mean", color="steelblue")
plt.plot(r6_mean, label="6-mo Rolling Mean", color="coral")
plt.fill_between(revenue.index,
                 r3_mean - r3_std, r3_mean + r3_std,
                 alpha=0.15, color="steelblue", label="3-mo ±1 SD")
plt.title("Monthly Revenue with Rolling Statistics")
plt.xlabel("Month"); plt.ylabel("Revenue ($)")
plt.legend(); plt.tight_layout()
plt.savefig("rolling_stats.png", dpi=100)
plt.show()

print("Most volatile 3-mo window:", r3_std.idxmax())
print("Most stable 3-mo window:", r3_std.dropna().idxmin())
```

### Reflection Questions

1. In Challenge 1, the `mean_median_gap` column measures how much the mean exceeds the median within each department. Which department shows the largest gap, and what specific feature of that department's salary data causes the gap? How should a compensation analyst report that department's "typical" salary?
2. In Challenge 2, a wide rolling standard deviation window signals a volatile period. In a real business context, what external factors might cause a spike in the rolling standard deviation of monthly revenue? What statistical action would you take to decide whether the volatility represents a true trend change or random noise?

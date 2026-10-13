# Lab 07 — Statistical Analysis and Visualization

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 100

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 2: Data Analysis

---

## Lab Overview

In this lab you will compute descriptive statistics and build data visualizations using Python pandas and matplotlib. You will work with a retail sales dataset, apply all the statistical measures from the Module 07 lecture, and produce publication-quality charts.

**Tools required:**

- Python 3.8 or later
- pandas (`pip install pandas`)
- matplotlib (`pip install matplotlib`)
- scipy (`pip install scipy`)

---

## Dataset

Copy the following data into a file named `retail_sales.csv` in your working directory.

```csv
store_id,region,month,sales_amount,ad_spend,customer_count
1,North,Jan,42000,3200,410
2,North,Jan,38000,2900,385
3,South,Jan,55000,4100,530
4,South,Jan,41000,3100,400
5,East,Jan,39000,2800,375
6,East,Jan,44000,3300,425
7,West,Jan,52000,4000,510
8,West,Jan,37000,2700,360
9,Central,Jan,60000,4500,580
10,Central,Jan,47000,3600,460
1,North,Feb,44000,3400,430
2,North,Feb,40000,3100,400
3,South,Feb,58000,4300,555
4,South,Feb,43000,3300,415
5,East,Feb,41000,3000,390
6,East,Feb,46000,3500,440
7,West,Feb,54000,4200,525
8,West,Feb,39000,2900,378
9,Central,Feb,63000,4700,600
10,Central,Feb,49000,3800,475
```

---

## Part 1: Loading and Inspecting Data (15 points)

### Task 1.1 — Load the dataset

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy import stats

# Load data
df = pd.read_csv('retail_sales.csv')

# Inspect
print(df.shape)
print(df.dtypes)
print(df.head())
print(df.isnull().sum())
```

**Deliverable 1.1:** Paste the output of `df.describe()` into your lab report. Identify the column with the highest standard deviation.

### Task 1.2 — Filter to January data only

```python
jan_df = df[df['month'] == 'Jan'].copy()
print(f"January records: {len(jan_df)}")
```

---

## Part 2: Descriptive Statistics (25 points)

### Task 2.1 — Compute central tendency for January sales

```python
mean_sales   = jan_df['sales_amount'].mean()
median_sales = jan_df['sales_amount'].median()
mode_result  = jan_df['sales_amount'].mode()

print(f"Mean:   ${mean_sales:,.0f}")
print(f"Median: ${median_sales:,.0f}")
print(f"Mode:   {mode_result.tolist()}")
```

**Deliverable 2.1:** Record mean, median, and mode. Explain in one sentence why the mean and median differ.

### Task 2.2 — Compute measures of spread

```python
range_sales  = jan_df['sales_amount'].max() - jan_df['sales_amount'].min()
var_sales    = jan_df['sales_amount'].var()        # sample variance (ddof=1 by default)
std_sales    = jan_df['sales_amount'].std()
q1           = jan_df['sales_amount'].quantile(0.25)
q3           = jan_df['sales_amount'].quantile(0.75)
iqr_sales    = q3 - q1
lower_fence  = q1 - 1.5 * iqr_sales
upper_fence  = q3 + 1.5 * iqr_sales

print(f"Range:         ${range_sales:,.0f}")
print(f"Variance:      ${var_sales:,.0f}")
print(f"Std Dev:       ${std_sales:,.0f}")
print(f"IQR:           ${iqr_sales:,.0f}")
print(f"Lower fence:   ${lower_fence:,.0f}")
print(f"Upper fence:   ${upper_fence:,.0f}")

outliers = jan_df[(jan_df['sales_amount'] < lower_fence) |
                  (jan_df['sales_amount'] > upper_fence)]
print(f"Outlier count: {len(outliers)}")
```

**Deliverable 2.2:** Record all six statistics. Are there any outliers? List them if present.

### Task 2.3 — Compare all months

```python
monthly_stats = df.groupby('month')['sales_amount'].agg(
    mean_sales='mean',
    median_sales='median',
    std_dev='std',
    min_sales='min',
    max_sales='max'
).reset_index()

print(monthly_stats.to_string(index=False))
```

**Deliverable 2.3:** Which month had higher average sales? Which had more variability?

---

## Part 3: Correlation Analysis (20 points)

### Task 3.1 — Pearson correlation between sales and ad spend

```python
r_value, p_value = stats.pearsonr(df['sales_amount'], df['ad_spend'])
print(f"Pearson r:  {r_value:.4f}")
print(f"p-value:    {p_value:.4f}")

if p_value < 0.05:
    print("Statistically significant at alpha = 0.05")
else:
    print("Not statistically significant at alpha = 0.05")
```

**Deliverable 3.1:** State the `r` value, interpret its strength and direction, and note whether it is statistically significant.

### Task 3.2 — Correlation matrix for all numeric columns

```python
numeric_cols = ['sales_amount', 'ad_spend', 'customer_count']
corr_matrix = df[numeric_cols].corr()
print(corr_matrix.round(3))
```

**Deliverable 3.2:** Which pair of variables has the strongest correlation? Does this make intuitive business sense?

---

## Part 4: Data Visualization (30 points)

### Task 4.1 — Bar chart: regional sales comparison

```python
regional_sales = df.groupby('region')['sales_amount'].mean().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(regional_sales.index, regional_sales.values, color='steelblue', edgecolor='white')
ax.set_title('Average Monthly Sales by Region', fontsize=14, fontweight='bold')
ax.set_xlabel('Region', fontsize=11)
ax.set_ylabel('Average Sales ($)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'${height:,.0f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 4), textcoords='offset points',
                ha='center', va='bottom', fontsize=9)
plt.tight_layout()
plt.savefig('bar_regional_sales.png', dpi=150)
plt.show()
```

### Task 4.2 — Line chart: sales trend by month

```python
monthly_avg = df.groupby('month')['sales_amount'].mean()
# Force correct month order
month_order = ['Jan', 'Feb']
monthly_avg = monthly_avg.reindex(month_order)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(monthly_avg.index, monthly_avg.values, marker='o', linewidth=2, color='darkgreen')
ax.set_title('Average Sales Trend by Month', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=11)
ax.set_ylabel('Average Sales ($)', fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
plt.savefig('line_sales_trend.png', dpi=150)
plt.show()
```

### Task 4.3 — Scatter plot: ad spend vs. sales

```python
fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(df['ad_spend'], df['sales_amount'], color='darkorange', alpha=0.7, edgecolors='white')

# Add regression line
m, b = stats.linregress(df['ad_spend'], df['sales_amount'])[:2]
x_line = [df['ad_spend'].min(), df['ad_spend'].max()]
y_line = [m * x + b for x in x_line]
ax.plot(x_line, y_line, color='red', linewidth=1.5, linestyle='--', label='Trend line')

ax.set_title('Ad Spend vs. Sales Amount', fontsize=14, fontweight='bold')
ax.set_xlabel('Ad Spend ($)', fontsize=11)
ax.set_ylabel('Sales Amount ($)', fontsize=11)
ax.legend()
plt.tight_layout()
plt.savefig('scatter_ad_vs_sales.png', dpi=150)
plt.show()
```

### Task 4.4 — Histogram: sales distribution

```python
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(df['sales_amount'], bins=8, color='purple', edgecolor='white', alpha=0.85)
ax.axvline(df['sales_amount'].mean(), color='red', linestyle='--', linewidth=1.5, label=f"Mean: ${df['sales_amount'].mean():,.0f}")
ax.axvline(df['sales_amount'].median(), color='blue', linestyle='-', linewidth=1.5, label=f"Median: ${df['sales_amount'].median():,.0f}")
ax.set_title('Distribution of Sales Amounts', fontsize=14, fontweight='bold')
ax.set_xlabel('Sales Amount ($)', fontsize=11)
ax.set_ylabel('Frequency', fontsize=11)
ax.legend()
plt.tight_layout()
plt.savefig('hist_sales_dist.png', dpi=150)
plt.show()
```

**Deliverable 4:** Submit all four chart image files along with your script. For each chart, write one sentence describing the key insight it reveals.

---

## Part 5: Reflection Questions (10 points)

Answer each question in 2–4 sentences in your lab report.

**Question 5.1:** Looking at the histogram, would you describe the sales distribution as symmetric, right-skewed, or left-skewed? What does this tell you about using mean vs. median for this dataset?

**Question 5.2:** The scatter plot shows a strong positive correlation between ad spend and sales. A marketing manager concludes that increasing ad spend causes higher sales. Is this conclusion justified from the correlation alone? Explain.

**Question 5.3:** How would you use the IQR outlier fences from Part 2 in a data cleaning workflow before running a sales forecast model?

---

## Submission Checklist

Submit all of the following in a single ZIP file or folder:

- [ ] Python script (`lab07.py` or `lab07.ipynb`)
- [ ] `bar_regional_sales.png`
- [ ] `line_sales_trend.png`
- [ ] `scatter_ad_vs_sales.png`
- [ ] `hist_sales_dist.png`
- [ ] Lab report (PDF or Word) with all deliverables and reflection answers

---

## Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Part 1 — Data loading and inspection | 15 | Correct output, null check performed, describe() output included |
| Part 2 — Descriptive statistics | 25 | All six statistics correct, outlier analysis complete |
| Part 3 — Correlation analysis | 20 | Correct r value, proper interpretation, correlation matrix complete |
| Part 4 — Visualizations | 30 | All four charts produced, labeled, saved, insight sentences included |
| Part 5 — Reflection questions | 10 | Thoughtful, accurate answers demonstrating conceptual understanding |
| **Total** | **100** | |

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Region Distribution Deep Dive

Extend the regional analysis to include full descriptive statistics and distribution visualization for every region.

1. Compute a grouped summary table for all numeric columns (`sales_amount`, `ad_spend`, `customer_count`) grouped by `region`. Include mean, median, standard deviation, and IQR for each column in each region. Print the result as a formatted DataFrame with two decimal places.
2. Create a 1×5 panel of box plots (one per region) for `sales_amount` using `matplotlib` subplots. Add a horizontal dashed line at the overall median to allow visual comparison. Save the figure as `regional_boxplots.png`. Identify which region has the largest IQR and which has the smallest, and write one sentence explaining the business implication of that difference.

```python
import matplotlib.pyplot as plt
import pandas as pd

regions = sorted(df["region"].unique())
overall_median = df["sales_amount"].median()

fig, axes = plt.subplots(1, len(regions), figsize=(16, 5), sharey=True)
for i, region in enumerate(regions):
    subset = df[df["region"] == region]["sales_amount"]
    axes[i].boxplot(subset, patch_artist=True,
                    boxprops=dict(facecolor="steelblue", alpha=0.7))
    axes[i].axhline(overall_median, color="red", linestyle="--", linewidth=1,
                    label="Overall median" if i == 0 else "")
    axes[i].set_title(region)
    axes[i].set_xlabel("Region")
    if i == 0:
        axes[i].set_ylabel("Sales Amount ($)")
        axes[i].legend(fontsize=8)
plt.suptitle("Sales Distribution by Region", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("regional_boxplots.png", dpi=150)
plt.show()
```

### Challenge 2: Regression Line and Residual Analysis

Build a simple linear regression model from the correlation analysis and examine the residuals.

1. Using `scipy.stats.linregress`, fit a regression of `sales_amount` on `ad_spend` using all 20 rows. Print the slope, intercept, r-value, p-value, and standard error. Interpret the slope in plain language: "For every additional $1 of ad spend, sales change by $___."
2. Compute residuals (actual `sales_amount` minus predicted value for each row). Plot a residual scatter plot with `ad_spend` on the x-axis and residuals on the y-axis. Add a horizontal line at y = 0. Save as `residuals.png`. Write two sentences evaluating whether the residuals appear randomly distributed (which would support the linear model assumption) or show a pattern.

```python
from scipy.stats import linregress
import numpy as np

slope, intercept, r_val, p_val, std_err = linregress(df["ad_spend"], df["sales_amount"])
print(f"Slope: {slope:.2f} | Intercept: {intercept:.2f}")
print(f"r = {r_val:.4f}, p = {p_val:.4f}, SE = {std_err:.4f}")
print(f"Interpretation: For every $1 increase in ad spend, sales change by ${slope:.2f}")

predicted = slope * df["ad_spend"] + intercept
residuals = df["sales_amount"] - predicted

fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(df["ad_spend"], residuals, color="darkorange", alpha=0.8, edgecolors="white")
ax.axhline(0, color="red", linestyle="--", linewidth=1.5)
ax.set_title("Residuals vs. Ad Spend")
ax.set_xlabel("Ad Spend ($)")
ax.set_ylabel("Residual ($)")
plt.tight_layout()
plt.savefig("residuals.png", dpi=150)
plt.show()
```

### Reflection Questions

1. In Challenge 1, the box plot panel shows each region's `sales_amount` distribution side by side. A regional director looks at the plot and says, "Central region is clearly the best performer." What additional context (beyond the box plot) would you need to validate that claim? What other metrics might matter beyond average sales?
2. In Challenge 2, the residual plot shows whether the linear model fits well. If you observed that residuals increased as `ad_spend` increased (a funnel shape), what statistical term describes this pattern, and what would it suggest about the reliability of your regression predictions?

---

End of Lab 07

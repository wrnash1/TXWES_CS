# Reading Guide: Module 07 — Statistical Analysis and Visualization

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 2: Data Analysis

---

## Overview

This reading guide accompanies the Module 07 video lecture. Work through each section in order, complete the practice problems, and pay close attention to the Data+ Exam Tips before your quiz. Statistical analysis and visualization are tested heavily on the CompTIA Data+ exam — typically 15–20% of total questions.

---

## Section 1: Descriptive Statistics

Descriptive statistics summarize a dataset's main characteristics without making predictions or inferences about a larger population. They answer the question: "What does this data look like?"

### The Three Pillars

- **Central tendency** — where the data is centered
- **Spread (dispersion)** — how spread out the data is
- **Shape** — whether the distribution is symmetric or skewed

---

## Section 2: Measures of Central Tendency

### Mean

The arithmetic mean sums all values and divides by the count.

`mean = sum(x) / n`

**Example:** Scores of 85, 90, 78, 92, 88

`mean = (85 + 90 + 78 + 92 + 88) / 5 = 433 / 5 = 86.6`

The mean is the most commonly used average but is pulled toward outliers.

### Median

Sort values in ascending order. The median is the middle value (odd n) or the average of the two middle values (even n).

**Example (odd n=5):** `78, 85, 88, 90, 92` → median = 88

**Example (even n=6):** `78, 85, 88, 90, 92, 95` → `median = (88 + 90) / 2 = 89`

The median is robust to outliers — preferred for skewed distributions such as income or housing prices.

### Mode

The mode is the most frequently occurring value. A dataset can have:

- **No mode** — all values unique
- **One mode** — unimodal
- **Two modes** — bimodal
- **More than two modes** — multimodal

The mode is the only central tendency measure that works for categorical (nominal) data.

### Comparison Table

| Measure | Best For | Sensitive to Outliers? | Works on Categorical? |
|---------|----------|------------------------|----------------------|
| Mean | Symmetric, numeric data | Yes | No |
| Median | Skewed or ordinal data | No | No |
| Mode | Any data type, categorical | No | Yes |

---

## Section 3: Measures of Spread

Two datasets can share the same mean but be completely different in character. Spread measures capture this difference.

### Range

`range = max - min`

Simple and fast, but one extreme value distorts it significantly.

### Variance

Variance calculates the average of squared deviations from the mean.

**Population variance:**

`sigma_sq = sum((x - mu)^2) / N`

**Sample variance (Bessel's correction — divide by n-1):**

`s_sq = sum((x - x_bar)^2) / (n - 1)`

Dividing by `n - 1` corrects for the bias introduced when estimating population variance from a sample.

### Standard Deviation

Standard deviation is the square root of variance — returning the value to original units.

`sigma = sqrt(sigma_sq)` (population)

`s = sqrt(s_sq)` (sample)

**Example:** Exam scores `{70, 75, 80, 85, 90}`, mean = 80

Deviations: `-10, -5, 0, +5, +10`

Squared deviations: `100, 25, 0, 25, 100` → sum = 250

`s_sq = 250 / (5 - 1) = 62.5`

`s = sqrt(62.5) ≈ 7.91`

### The Empirical Rule (68-95-99.7 Rule)

For normally distributed data:

- Approximately 68% of values fall within `mean ± 1 * std_dev`
- Approximately 95% of values fall within `mean ± 2 * std_dev`
- Approximately 99.7% of values fall within `mean ± 3 * std_dev`

This rule is directly tested on the Data+ exam. Memorize all three percentages.

### Interquartile Range (IQR)

The IQR spans from Q1 (25th percentile) to Q3 (75th percentile).

`IQR = Q3 - Q1`

Outlier thresholds:

`lower_fence = Q1 - (1.5 * IQR)`

`upper_fence = Q3 + (1.5 * IQR)`

Values outside these fences are flagged as potential outliers and displayed as individual points on a box plot.

---

## Section 4: Measures of Shape

### Skewness

Skewness measures the asymmetry of a distribution.

- **Symmetric (skewness ≈ 0):** mean ≈ median ≈ mode
- **Right-skewed (positive skewness):** long tail to the right; mean > median
- **Left-skewed (negative skewness):** long tail to the left; mean < median

Real-world right-skewed examples: income data, response times, housing prices.

### Kurtosis

Kurtosis measures the "tail heaviness" of a distribution. High kurtosis means more extreme outliers are likely.

- **Leptokurtic** — heavy tails, sharp peak (kurtosis > 3)
- **Mesokurtic** — normal distribution (kurtosis = 3)
- **Platykurtic** — light tails, flat peak (kurtosis < 3)

---

## Section 5: Correlation

### Pearson Correlation Coefficient

The Pearson coefficient `r` measures the strength and direction of the linear relationship between two numeric variables.

`r = sum((x - mean_x)(y - mean_y)) / sqrt(sum((x - mean_x)^2) * sum((y - mean_y)^2))`

Range: `-1 <= r <= +1`

### Interpretation Scale

| r Value | Interpretation |
|---------|----------------|
| `0.9 to 1.0` | Very strong positive |
| `0.7 to 0.9` | Strong positive |
| `0.5 to 0.7` | Moderate positive |
| `0.3 to 0.5` | Weak positive |
| `0.0 to 0.3` | Negligible |
| `-0.3 to 0.0` | Negligible negative |
| `-0.5 to -0.3` | Weak negative |
| `-0.7 to -0.5` | Moderate negative |
| `-0.9 to -0.7` | Strong negative |
| `-1.0 to -0.9` | Very strong negative |

### Pearson vs. Spearman

Use **Spearman rank correlation** when:

- Data is ordinal (ranked categories)
- The relationship is monotonic but not linear
- Data has significant outliers
- Data is not normally distributed

Spearman ranks each variable first, then applies the Pearson formula to the ranks.

### Correlation vs. Causation

Correlation describes a relationship. It does not establish cause and effect. Always ask:

1. Could a third variable (confounding variable) explain the relationship?
2. Could the relationship be coincidental?
3. Is there a logical mechanism linking the two variables?

---

## Section 6: Data Visualization Selection

### Bar Charts

Use to compare values across discrete categories.

Variants:

- **Vertical (column):** standard category comparison
- **Horizontal:** long category labels or many categories
- **Grouped:** multiple series side-by-side
- **Stacked:** part-to-whole within each category

### Line Charts

Use to show trends over time with continuous data on both axes or when the x-axis is ordered.

Avoid for unordered categorical x-axes — the lines imply false ordering.

### Scatter Plots

Use to show the relationship between two continuous variables. Add a regression (trend) line to highlight the direction of the relationship.

### Histograms

Use to show the frequency distribution of a single continuous variable. Adjacent bars (no gaps) indicate continuous data. Bin width affects the visual — too few bins hides detail; too many bins creates noise.

### Additional Chart Types

| Chart Type | Best Use Case |
|------------|---------------|
| Pie chart | Part-to-whole, few categories (max 5–6) |
| Box plot | Distribution, quartiles, outliers |
| Heatmap | Patterns across two categorical dimensions |
| Bubble chart | Three-variable relationship (x, y, size) |
| Waterfall chart | Incremental change (gains/losses) |
| Gantt chart | Project timelines and scheduling |

---

## Section 7: SQL for Descriptive Statistics

### Core Aggregate Functions

```sql
SELECT
    COUNT(*)             AS total_rows,
    COUNT(sales_amount)  AS non_null_count,
    AVG(sales_amount)    AS mean_value,
    MIN(sales_amount)    AS minimum,
    MAX(sales_amount)    AS maximum,
    STDDEV(sales_amount) AS std_deviation,
    VARIANCE(sales_amount) AS variance_val
FROM sales;
```

### Percentile Functions

```sql
-- ANSI SQL percentile functions
SELECT
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY score) AS q1,
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY score) AS median_val,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY score) AS q3
FROM exam_scores;
```

### Python Equivalent (pandas)

```python
import pandas as pd

df = pd.read_csv('sales_data.csv')

# Summary statistics
print(df['sales_amount'].describe())

# Individual statistics
mean_val  = df['sales_amount'].mean()
median_val = df['sales_amount'].median()
std_val   = df['sales_amount'].std()
iqr_val   = df['sales_amount'].quantile(0.75) - df['sales_amount'].quantile(0.25)

print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Std Dev: {std_val:.2f}")
print(f"IQR: {iqr_val:.2f}")

# Correlation
corr = df['sales_amount'].corr(df['ad_spend'])
print(f"Pearson r: {corr:.4f}")
```

---

## Section 8: Data+ Exam Tips

**Tip 1 — Mean vs. Median:** When a question describes skewed data or mentions outliers, the correct measure of central tendency is the **median**, not the mean.

**Tip 2 — Empirical Rule:** Commit `68 / 95 / 99.7` to memory. Questions frequently ask what percentage of data falls within 1, 2, or 3 standard deviations.

**Tip 3 — Sample vs. Population:** Sample variance divides by `n - 1`. Population variance divides by `N`. Exam questions may explicitly state which to use.

**Tip 4 — Correlation Range:** The Pearson `r` always falls between -1 and +1. If an answer choice shows a value outside this range, eliminate it immediately.

**Tip 5 — Chart Selection:** Match the chart to the data type and question type. Key rules: line charts for time trends, bar charts for categories, scatter plots for relationships, histograms for distributions.

**Tip 6 — Correlation ≠ Causation:** Any exam question about inferring cause from a correlation coefficient is a trap. Correlation alone never establishes causation.

---

## Practice Problems

**Problem 1:** A dataset has values `{10, 12, 11, 13, 100}`. Calculate the mean and median. Which is a better measure of center and why?

**Problem 2:** For a normally distributed dataset with `mean = 50` and `std_dev = 5`, what percentage of values fall between 40 and 60?

**Problem 3:** Two variables have `r = -0.82`. Describe the relationship in plain language.

**Problem 4:** You are analyzing monthly revenue data over 24 months. A stakeholder asks to see the trend. What chart type do you use?

**Problem 5:** A dataset has `Q1 = 25` and `Q3 = 45`. Calculate the IQR, the lower outlier fence, and the upper outlier fence.

---

## Key Formulas Reference

| Formula | Expression |
|---------|-----------|
| Mean | `mean = sum(x) / n` |
| Sample variance | `s_sq = sum((x - x_bar)^2) / (n - 1)` |
| Standard deviation | `s = sqrt(s_sq)` |
| IQR | `IQR = Q3 - Q1` |
| Lower outlier fence | `Q1 - (1.5 * IQR)` |
| Upper outlier fence | `Q3 + (1.5 * IQR)` |
| Pearson r range | `-1 <= r <= +1` |

---

End of Module 07 Reading Guide

# Video Script: Module 07 — Statistical Analysis and Visualization

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA Data+ (DA0-001)

---

## Segment 1: Introduction (0:00–1:30)

Welcome back to CIS-4336 Data Analytics. I'm Professor Nash, and today we are tackling one of the most foundational topics in the field — statistical analysis and data visualization.

Think about it this way: data without statistics is just noise. Statistics give us a language to describe what we see, measure how confident we are, and communicate findings to decision-makers. Visualization takes those statistics and makes them immediately understandable — even to someone who has never opened a spreadsheet.

By the end of today you will be able to calculate and interpret descriptive statistics, understand measures of central tendency and spread, use correlation to describe relationships between variables, and select the right chart type for any given dataset.

These concepts map directly to Domain 2 of the CompTIA Data+ exam, which covers data analysis and statistics. Expect three to five exam questions on this material.

[PAUSE — Slide: Module 07 Learning Objectives]

Let's get started.

---

## Segment 2: Descriptive Statistics Overview (1:30–4:00)

Descriptive statistics summarize and describe the main features of a dataset. They do not make predictions — that is inferential statistics, covered in Module 08. Descriptive statistics simply tell us what the data looks like right now.

There are three categories you need to know.

First: **measures of central tendency** — mean, median, and mode. These describe the center of your data.

Second: **measures of spread** — range, variance, and standard deviation. These describe how spread out or tightly clustered the data is.

Third: **measures of shape** — skewness and kurtosis. These describe the symmetry and peak-ness of your distribution.

[SHOW CHART — Normal distribution bell curve with labels for mean, standard deviation bands]

[PAUSE]

Let me give you a concrete example. Suppose you work for a retail company and you have monthly sales figures for 10 stores:

`42000, 38000, 55000, 41000, 39000, 44000, 52000, 37000, 60000, 47000`

Before you can understand what is happening, you need to summarize this data. That is exactly what descriptive statistics do.

---

## Segment 3: Measures of Central Tendency (4:00–7:30)

### The Mean

The mean — the arithmetic average — sums all values and divides by the count.

`mean = sum(x) / n`

For our store data, the sum is 455,000 and n equals 10, so `mean = 455000 / 10 = 45500`.

The mean is sensitive to outliers. If one store had an extraordinary month at $200,000, the mean would jump dramatically even though nine stores were unchanged.

[PAUSE]

### The Median

The median is the middle value when data is sorted. With an even count, the median is the average of the two middle values.

Sorted: `37000, 38000, 39000, 41000, 42000, 44000, 47000, 52000, 55000, 60000`

The two middle values are 42,000 and 44,000. So `median = (42000 + 44000) / 2 = 43000`.

The median is resistant to outliers. When data is skewed — think income data, where a few billionaires exist — the median is a better representation of the typical value than the mean.

[PAUSE]

### The Mode

The mode is the most frequently occurring value. In our dataset, every value is unique, so there is no mode. But consider survey responses on a 1–5 scale — the mode tells you which rating was given most often. The mode is the only measure of central tendency that applies to categorical data.

[SHOW CHART — Side-by-side: symmetric distribution (mean = median) vs. right-skewed distribution (mean > median)]

**Data+ Exam Tip:** Know when to use each measure. Use mean for symmetric data without outliers. Use median for skewed data or data with outliers. Use mode for categorical data.

---

## Segment 4: Measures of Spread (7:30–11:00)

Understanding the center is only half the picture. Two datasets can have identical means but look completely different if one is tightly clustered and the other is wildly spread out.

### Range

`range = maximum - minimum`

For our sales data: `range = 60000 - 37000 = 23000`.

The range is simple but fragile. One extreme value can make it misleading.

[PAUSE]

### Variance

Variance measures the average squared deviation from the mean. We square deviations so that positive and negative differences do not cancel each other out.

Population variance: `variance = sum((x - mean)^2) / n`

Sample variance uses Bessel's correction — dividing by `n - 1` — to produce an unbiased estimate of population variance.

`sample_variance = sum((x - mean)^2) / (n - 1)`

For our sales data, the sample variance is approximately 72,277,778.

[PAUSE]

### Standard Deviation

Standard deviation is the square root of variance, bringing us back to original units.

`std_dev = sqrt(variance)`

`std_dev = sqrt(72277778) ≈ 8502`

A typical store's sales fall within about $8,502 of the $45,500 mean. That is an actionable number you can use to benchmark low-performing stores.

[SHOW CHART — Bell curve: mean ± 1 SD covers 68%, mean ± 2 SD covers 95%, mean ± 3 SD covers 99.7%]

This is the **68-95-99.7 rule**, also called the empirical rule. It applies to normally distributed data. For the Data+ exam, memorize all three percentages.

[PAUSE]

### Interquartile Range

The IQR spans the middle 50% of data — from the 25th percentile (Q1) to the 75th percentile (Q3).

`IQR = Q3 - Q1`

The IQR is used to detect outliers. Any value below `Q1 - (1.5 * IQR)` or above `Q3 + (1.5 * IQR)` is flagged. You will see this rule illustrated in box plots throughout your analytics career.

---

## Segment 5: Correlation (11:00–13:30)

Correlation measures the strength and direction of the linear relationship between two numeric variables.

The most common measure is the **Pearson correlation coefficient**, denoted `r`.

`r = sum((x - mean_x)(y - mean_y)) / sqrt(sum((x - mean_x)^2) * sum((y - mean_y)^2))`

The value of `r` always falls between -1 and +1.

- `r = +1` — perfect positive linear relationship
- `r = -1` — perfect negative linear relationship
- `r = 0` — no linear relationship

[SHOW CHART — Four scatter plots: r=+1, r=-1, r=+0.7, r=0]

[PAUSE]

General interpretation guidelines:

- `|r| >= 0.9` — very strong
- `0.7 <= |r| < 0.9` — strong
- `0.5 <= |r| < 0.7` — moderate
- `0.3 <= |r| < 0.5` — weak
- `|r| < 0.3` — negligible

**Critical warning:** Correlation does not imply causation. Two variables can move together for entirely unrelated reasons. The classic example: ice cream sales and drowning incidents both rise in summer — but eating ice cream does not cause drowning. Both respond to a third variable: temperature.

[PAUSE]

When data is ordinal or not normally distributed, use **Spearman rank correlation** instead. It ranks each variable first, then computes Pearson correlation on the ranks.

---

## Segment 6: Data Visualization Types (13:30–17:30)

Choosing the right chart is one of the most practical skills in data analytics. A chart that fits the data communicates insight instantly. A chart that mismatches the data confuses and misleads.

[SHOW CHART — Chart selection decision tree]

### Bar Charts

Bar charts compare discrete categories. The length or height of each bar represents a quantity.

- **Vertical bar chart**: comparing values across categories at a single point in time
- **Horizontal bar chart**: when category labels are long or there are many categories
- **Grouped bar chart**: comparing multiple series across categories simultaneously
- **Stacked bar chart**: showing part-to-whole relationships within each category

Example: quarterly sales by region. Each region is a category; bar height is total sales.

[PAUSE]

### Line Charts

Line charts show trends over time. The x-axis is a time dimension; the y-axis is a continuous measure.

Use line charts when:

- You have a continuous time series
- You want to show direction and rate of change
- You are comparing two or more trends on the same scale

Do not use a line chart for unordered categories — the connecting lines imply a false sense of continuity.

[PAUSE]

### Scatter Plots

Scatter plots show the relationship between two continuous variables. Each point represents one observation.

Scatter plots reveal:

- Correlation direction and strength
- Clusters of similar data points
- Outliers that deviate from the main pattern

Adding a trend line — a regression line — helps viewers see the overall direction of the relationship.

[PAUSE]

### Histograms

A histogram shows the distribution of a single numeric variable. The x-axis divides the range into bins (intervals); the y-axis shows the count or frequency within each bin.

Histograms reveal:

- Whether data is symmetric or skewed
- The approximate center and spread
- Multiple peaks, indicating a bimodal distribution
- Outliers on either tail

[SHOW CHART — Histogram with right skew labeled, long tail to the right]

**Do not confuse histograms with bar charts.** Histograms show distributions of continuous data — bars are adjacent with no gaps. Bar charts compare discrete categories — gaps between bars are acceptable and common.

[PAUSE]

### Choosing the Right Chart

Match your analytical question to the correct visual:

- Comparing categories → bar chart
- Showing trends over time → line chart
- Showing relationships between two variables → scatter plot
- Showing the distribution of one variable → histogram
- Showing part-to-whole composition → pie chart or stacked bar
- Showing geographic patterns → map/choropleth chart
- Showing many variables at once → heatmap or parallel coordinates

[SHOW CHART — Summary table of chart types with use cases]

---

## Segment 7: Applying Statistics in SQL (17:30–19:30)

You can compute descriptive statistics directly in SQL — a critical skill for analysts who work in database environments.

[PAUSE]

```sql
-- Descriptive statistics for store sales
SELECT
    COUNT(sales_amount)                   AS record_count,
    AVG(sales_amount)                     AS mean_sales,
    MIN(sales_amount)                     AS min_sales,
    MAX(sales_amount)                     AS max_sales,
    MAX(sales_amount) - MIN(sales_amount) AS sales_range,
    STDDEV(sales_amount)                  AS std_dev_sales,
    VARIANCE(sales_amount)                AS variance_sales
FROM store_monthly_sales
WHERE sale_month = '2024-01';
```

[PAUSE]

Most SQL dialects support `STDDEV()` and `VARIANCE()` as built-in aggregate functions. When working in databases that lack these, compute variance manually:

```sql
-- Manual population variance
SELECT AVG(POWER(sales_amount - avg_sales, 2)) AS pop_variance
FROM (
    SELECT
        sales_amount,
        AVG(sales_amount) OVER () AS avg_sales
    FROM store_monthly_sales
) sub;
```

[PAUSE]

For percentiles — needed for IQR, median, and quartile analysis — use `PERCENTILE_CONT`:

```sql
-- Median and quartiles
SELECT
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY sales_amount) AS q1,
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY sales_amount) AS median_sales,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY sales_amount) AS q3
FROM store_monthly_sales;
```

---

## Segment 8: Module Summary and Exam Prep (19:30–21:00)

Let me bring everything together.

[PAUSE]

Descriptive statistics describe your data. Key measures:

- Central tendency: mean, median, mode
- Spread: range, variance, standard deviation, IQR
- Correlation: Pearson r for linear relationships

Visualization rules:

- Bar chart for category comparison
- Line chart for trends over time
- Scatter plot for relationships between variables
- Histogram for distributions of a single variable

For the CompTIA Data+ exam, focus on:

- When to use median vs. mean (skewed vs. symmetric data)
- The empirical rule: 68-95-99.7
- Correlation coefficient range and interpretation scale
- Chart selection based on data type and analytical question

Your lab this week uses Python pandas to compute these statistics on a real retail dataset and builds visualizations with matplotlib. Your quiz covers all material in this module.

I will see you in Module 08, where we move from describing data to predicting it.

[PAUSE — End card with Texas Wesleyan University branding]

---

End of Module 07 Video Script

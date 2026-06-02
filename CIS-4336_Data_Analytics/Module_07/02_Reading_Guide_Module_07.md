# Reading Guide — Module 07: Data Visualization Principles and Chart Types

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 4: Visualization

---

## Overview

Domain 4 — Visualization — is the largest domain on the Data+ exam at approximately 21 percent. This guide provides chart selection rules, visualization mistake reference, color usage guidelines, and Python matplotlib code for every chart type covered in Module 07.

---

## Section 1 — Core Vocabulary

| Term | Definition |
|---|---|
| Data visualization | The representation of data in a graphical or pictorial format to communicate patterns and insights |
| Chart type | The specific form of a visualization (bar, line, scatter, histogram, etc.) |
| Data-to-ink ratio | Tufte's principle: every mark on a chart should represent data; remove non-data decoration |
| Categorical axis | An axis displaying discrete named categories |
| Continuous axis | An axis displaying a numeric range |
| Legend | A chart key explaining what colors, shapes, or line styles represent |
| Annotation | Text or markers added directly to a chart to highlight specific data points or findings |
| Truncated axis | An axis that does not start at zero, potentially exaggerating differences |
| Color encoding | Using color variation to represent data values or categories |
| Sequential color scale | A single-hue gradient from light to dark, used for numeric magnitude |
| Diverging color scale | A two-hue gradient through a neutral center, used for data with a meaningful midpoint |
| 3D chart | A chart using three-dimensional rendering — generally avoided in analytical work because it distorts perception |
| Sparkline | A small, word-sized chart embedded in a table or text to show trend compactly |
| Heatmap | A matrix visualization where cell color encodes a numeric value |
| Dashboard | A collection of multiple visualizations on a single screen, providing a summary view |

---

## Section 2 — Chart Selection Guide

### By Analytical Question

| Question Type | Recommended Chart(s) | Avoid |
|---|---|---|
| Compare values across categories | Bar chart (vertical or horizontal) | Pie chart with many categories |
| Show trend over time | Line chart, area chart | Bar chart for time series |
| Show distribution shape | Histogram, box plot, violin plot | Bar chart for continuous data |
| Show relationship between two numeric variables | Scatter plot | Line chart (implies order/trend) |
| Show part-to-whole composition | Bar chart (stacked), pie chart (few categories only), treemap | Pie chart with 6+ categories |
| Show change over time with composition | Stacked area chart | 3D anything |
| Show financial bridge / sequential changes | Waterfall chart | Pie chart |
| Show two variables plus a third magnitude | Bubble chart | Pie chart |
| Show correlation matrix or grid values | Heatmap | 3D surface chart |

### By Number of Variables

| Variables | Best Charts |
|---|---|
| 1 categorical | Bar chart, pie chart (few categories) |
| 1 continuous | Histogram, box plot |
| 2 categorical | Grouped bar, stacked bar, heatmap |
| 1 categorical + 1 continuous | Bar chart, box plot |
| 2 continuous | Scatter plot |
| Time + 1 continuous | Line chart |
| Time + 2+ continuous series | Multi-line chart |

---

## Section 3 — Visualization Mistake Reference

| Mistake | Why It Misleads | Correct Approach |
|---|---|---|
| Y-axis not starting at zero (bar charts) | Makes small differences look proportionally large | Always start bar chart y-axis at zero |
| 3D chart effects | Depth perception distorts bar heights and pie slice areas | Use flat 2D charts |
| Pie chart with 7+ categories | Human perception cannot accurately compare angles | Use a bar chart instead |
| Too many colors | Creates visual noise; reader cannot track meaning | Use maximum 6–7 distinct colors; use one color for emphasis |
| Missing axis labels | Reader cannot interpret scale or units | Always label both axes with variable name and unit |
| Missing chart title | Reader must infer the analytical finding | Use a descriptive title stating the finding, not just the topic |
| Dual y-axes | Different scales on the same chart invite false impressions of correlation | Use two separate charts; or use index-normalized values on one axis |
| Sorting by name instead of value | Alphabetical sorting hides rank order information | Sort bar charts by value (descending) unless category order has meaning |
| Using line chart for non-continuous categories | Implies continuity between unrelated categories | Use bar chart for discrete unordered categories |
| Cherry-picked date range | Selecting only the favorable portion of a time series distorts trend | Show the full relevant time period |

---

## Section 4 — Chart Type Reference with Python Code

### Bar Chart

```python
import matplotlib.pyplot as plt
import pandas as pd

data = {"Region": ["North","South","East","West"],
        "Revenue": [420000, 310000, 385000, 270000]}
df = pd.DataFrame(data).sort_values("Revenue", ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(df["Region"], df["Revenue"], color="steelblue", edgecolor="white")
ax.set_title("Total Revenue by Region (2024)")
ax.set_xlabel("Region")
ax.set_ylabel("Revenue ($)")
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"${x/1000:.0f}K")
)
plt.tight_layout()
plt.savefig("bar_chart.png", dpi=100)
plt.show()
```

### Line Chart (Time Series)

```python
months = ["Jan","Feb","Mar","Apr","May","Jun",
          "Jul","Aug","Sep","Oct","Nov","Dec"]
revenue = [310,285,340,365,390,420,410,445,400,460,490,510]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(months, revenue, marker="o", color="steelblue", linewidth=2)
ax.set_title("Monthly Revenue Trend (2024)")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($K)")
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("line_chart.png", dpi=100)
plt.show()
```

### Histogram

```python
import numpy as np

salaries = np.random.normal(loc=65000, scale=15000, size=200)

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(salaries, bins=15, color="steelblue", edgecolor="white")
ax.set_title("Distribution of Employee Salaries")
ax.set_xlabel("Salary ($)")
ax.set_ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png", dpi=100)
plt.show()
```

### Scatter Plot

```python
x = np.random.normal(20, 5, 80)
y = x * 3000 + np.random.normal(0, 8000, 80) + 50000

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(x, y, alpha=0.7, color="steelblue")
m, b = np.polyfit(x, y, 1)
ax.plot(x, m*x + b, color="red", linewidth=1.5, label="Trend")
ax.set_title("Training Hours vs. Quarterly Sales")
ax.set_xlabel("Training Hours")
ax.set_ylabel("Quarterly Sales ($)")
ax.legend()
plt.tight_layout()
plt.savefig("scatter.png", dpi=100)
plt.show()
```

### Box Plot (Multiple Groups)

```python
data_groups = {
    "North": np.random.normal(55000, 8000, 40),
    "South": np.random.normal(48000, 12000, 40),
    "East":  np.random.normal(61000, 7000, 40),
    "West":  np.random.normal(52000, 9000, 40)
}

fig, ax = plt.subplots(figsize=(8, 5))
ax.boxplot(data_groups.values(), labels=data_groups.keys(),
           patch_artist=True,
           boxprops=dict(facecolor="lightblue"))
ax.set_title("Salary Distribution by Region")
ax.set_ylabel("Salary ($)")
plt.tight_layout()
plt.savefig("boxplot.png", dpi=100)
plt.show()
```

---

## Section 5 — Color Usage Guidelines

| Color Purpose | Scale Type | Example |
|---|---|---|
| Distinguish categories | Qualitative (distinct hues) | Four regions: blue, orange, green, red |
| Show numeric magnitude (one direction) | Sequential (single hue, light to dark) | Sales volume: light blue to dark blue |
| Show divergence from a center value | Diverging (two hues through neutral) | Profit vs. loss: red — white — green |
| Emphasize a single category | Single accent color | Highlight one bar in red; all others gray |
| Accessibility | Color-blind safe palette | Blue-orange or blue-red (avoid red-green) |

Rule of thumb: Never use color as the only encoding. Add labels, patterns, or shapes for accessibility.

---

## Section 6 — Visualization Principles Reference Card

The five principles every analyst must apply:

1. Match the chart to the analytical question — what relationship, comparison, or pattern does the viewer need to see?
2. Maximize the data-to-ink ratio — remove all chart elements that do not represent data
3. Use honest scales — start bar chart axes at zero; document any truncation explicitly
4. Use color purposefully and accessibly — color encodes information, not decoration
5. Reduce cognitive load — label data directly, write descriptive titles, annotate key findings

---

## Section 7 — Data+ Exam Tips

1. **Domain 4 is 21 percent of the exam.** This is the highest-weight domain. Chart type selection, visualization mistakes, and dashboard design questions are high-frequency.

2. **Pie charts fail with many categories.** The exam will show a scenario with 8–10 categories and ask which chart is appropriate. The answer is a bar chart, not a pie chart.

3. **Bar charts must start at zero.** A truncated y-axis on a bar chart is a common exam trap — the question describes or shows a chart and asks what is wrong with it.

4. **Line chart implies temporal or ordered sequence.** Using a line chart for non-ordered discrete categories (like product names) is a visualization error.

5. **Scatter plot for two numeric variables.** When the question involves showing the relationship between two continuous numeric variables, the scatter plot is the answer.

6. **3D charts are always wrong on the exam.** 3D effects distort perception. Any exam answer offering a 3D chart type is incorrect.

7. **Box plots are for distribution comparison.** When the scenario asks to compare distributions across multiple groups, box plot is usually the correct answer.

8. **Color encoding: sequential vs. diverging.** Know when to use each. Sequential: one direction of magnitude (revenue amount). Diverging: meaningful center (profit positive vs. negative).

---

## Section 8 — Study Checklist

- [ ] Memorize all vocabulary terms in Section 1
- [ ] Reproduce the chart selection guide from memory for all five question types
- [ ] List five common visualization mistakes and their corrections
- [ ] Run all five Python code blocks in Section 4 and save the output charts
- [ ] Practice the chart selection decision process on five invented scenarios
- [ ] Review all eight exam tips
- [ ] Review official CompTIA Data+ objectives at comptia.org
- [ ] Review Professor Messer's free study materials at professormesser.com
- [ ] Complete Lab 07
- [ ] Complete Quiz 07

---

## Additional Resources

- Official exam objectives: comptia.org (search "Data+ DA0-001 exam objectives")
- Professor Messer's free study guides: professormesser.com

# Lab 07 — Data Visualization Principles and Chart Types

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 4: Visualization

---

## Objectives

By completing this lab, you will be able to:

- Select the most appropriate chart type for five distinct data scenarios
- Create production-quality charts using Python matplotlib and pandas
- Identify and correct common visualization mistakes
- Apply design principles (data-to-ink ratio, honest scales, color encoding)
- Interpret visualizations and derive analytical conclusions

---

## Prerequisites

- Module 07 Reading Guide completed
- Python 3.8 or later (or Google Colab)
- Libraries: `pip install pandas numpy matplotlib seaborn`

---

## Part A — Chart Type Selection (25 points)

### Part A Instructions

For each of the five scenarios below, select the most appropriate chart type and write a justification of 75–100 words. Your justification must address:

1. Why this chart type matches the analytical question
2. Why at least one other chart type would be less appropriate
3. Any design decisions (axis start, sorting, color) that matter for this specific scenario

**Scenario A1:** A retail company wants to show how annual revenue has changed month by month over the past two years. The audience is the executive team. They want to see whether recent months are on an upward or downward trajectory.

**Scenario A2:** A human resources analyst wants to compare the distribution of annual salaries across four departments (Sales, IT, Operations, Finance). The analyst suspects that the IT department has a much wider salary range than others.

**Scenario A3:** A marketing team wants to show what percentage of total annual advertising budget was allocated to each of six channels: Social Media, TV, Search Ads, Email, Print, and Events.

**Scenario A4:** A product team wants to explore whether there is a relationship between the number of features a customer uses per month and their monthly spending on the platform. The dataset has 500 customers.

**Scenario A5:** A finance team wants to present the quarterly revenue breakdown by product line (Hardware, Software, Services, Support) showing both the total revenue per quarter and the contribution of each product line to the total.

### Part A Deliverable

For each scenario: state the chart type selected, then write your 75–100 word justification.

**Grading:** 5 points per scenario (2 points chart selection, 3 points justification quality). 25 points total.

---

## Part B — Creating Charts with Python (40 points)

### Part B Instructions

Create four charts using Python. For each chart: write the code, save the output as a PNG, and answer the interpretation question.

**Chart B1 — Line Chart for Time Series (10 points):**

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(7)
months = pd.date_range("2023-01", periods=24, freq="MS")
base = 280000
trend = np.linspace(0, 120000, 24)
seasonal = 30000 * np.sin(np.linspace(0, 4*np.pi, 24))
noise = np.random.normal(0, 10000, 24)
revenue = base + trend + seasonal + noise

df_ts = pd.DataFrame({"month": months, "revenue": revenue})

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(df_ts["month"], df_ts["revenue"] / 1000,
        marker="o", markersize=4, color="steelblue", linewidth=2)
ax.axhline(df_ts["revenue"].mean() / 1000, color="gray",
           linestyle="--", alpha=0.7, label="2-year average")
ax.set_title("Monthly Revenue Trend — January 2023 to December 2024")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($K)")
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("line_chart_b1.png", dpi=100)
plt.show()
```

After running this code, answer: Describe the overall trend visible in the chart. Is revenue growing, declining, or flat? Does there appear to be a seasonal pattern? What would you tell the executive team in one sentence based on this chart?

**Chart B2 — Box Plot for Distribution Comparison (10 points):**

```python
np.random.seed(12)
departments = {
    "Sales":      np.random.normal(58000, 14000, 50),
    "IT":         np.random.normal(82000, 22000, 50),
    "Operations": np.random.normal(55000, 8000, 50),
    "Finance":    np.random.normal(70000, 11000, 50)
}

fig, ax = plt.subplots(figsize=(9, 5))
ax.boxplot(departments.values(),
           labels=departments.keys(),
           patch_artist=True,
           boxprops=dict(facecolor="lightsteelblue"),
           medianprops=dict(color="red", linewidth=2),
           flierprops=dict(marker="o", markerfacecolor="gray",
                           markersize=5, alpha=0.5))
ax.set_title("Salary Distribution by Department")
ax.set_ylabel("Annual Salary ($)")
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f"${x/1000:.0f}K")
)
ax.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("boxplot_b2.png", dpi=100)
plt.show()
```

After running this code, answer: Which department has the highest median salary? Which has the widest IQR (box height)? Does any department show visible outlier points beyond the whiskers? What does the IT department's wide box tell you about compensation equity in that department?

**Chart B3 — Scatter Plot with Trend Line (10 points):**

```python
np.random.seed(21)
n = 80
features_used = np.random.randint(1, 20, n)
monthly_spend = features_used * 45 + np.random.normal(0, 80, n) + 200

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(features_used, monthly_spend, alpha=0.6,
           color="steelblue", edgecolors="white", s=60)
m, b = np.polyfit(features_used, monthly_spend, 1)
x_line = np.array([features_used.min(), features_used.max()])
ax.plot(x_line, m*x_line + b, color="red", linewidth=2,
        label=f"Trend: y = {m:.1f}x + {b:.0f}")
r = np.corrcoef(features_used, monthly_spend)[0, 1]
ax.set_title(f"Features Used vs. Monthly Spend (r = {r:.2f})")
ax.set_xlabel("Features Used per Month")
ax.set_ylabel("Monthly Spend ($)")
ax.legend()
plt.tight_layout()
plt.savefig("scatter_b3.png", dpi=100)
plt.show()
```

After running this code, answer: Describe the direction and approximate strength of the relationship visible in the chart. Is the correlation positive or negative? Strong, moderate, or weak? What is one business action the product team could take based on this relationship — and what caution should you apply before making a causal recommendation?

**Chart B4 — Stacked Bar Chart for Composition Over Time (10 points):**

```python
quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
hardware  = [420, 390, 410, 450]
software  = [180, 220, 250, 290]
services  = [130, 145, 160, 175]
support   = [70, 75, 80, 85]

x = np.arange(len(quarters))
width = 0.55

fig, ax = plt.subplots(figsize=(9, 5))
p1 = ax.bar(x, hardware, width, label="Hardware", color="#1f77b4")
p2 = ax.bar(x, software, width, bottom=hardware, label="Software", color="#ff7f0e")
p3 = ax.bar(x, services, width,
            bottom=[h+s for h, s in zip(hardware, software)],
            label="Services", color="#2ca02c")
p4 = ax.bar(x, support, width,
            bottom=[h+s+sv for h, s, sv in zip(hardware, software, services)],
            label="Support", color="#d62728")
ax.set_title("Quarterly Revenue by Product Line (2024)")
ax.set_xlabel("Quarter")
ax.set_ylabel("Revenue ($K)")
ax.set_xticks(x)
ax.set_xticklabels(quarters)
ax.legend(loc="upper left")
ax.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("stacked_bar_b4.png", dpi=100)
plt.show()
```

After running this code, answer: Which product line grew the most in absolute dollar terms from Q1 to Q4? Which product line's share of total revenue increased the most over the year? What does the chart reveal about the changing revenue mix that a simple total-revenue line chart would not show?

### Part B Deliverable

Four PNG chart files and written answers to each interpretation question.

---

## Part C — Visualization Critique (20 points)

### Part C Instructions

Each scenario below describes a visualization with at least one design problem. For each scenario, identify the problem(s), explain how they mislead the viewer, and describe the correct approach.

**Critique C1 (5 points):** A sales manager creates a bar chart comparing four regional revenue figures. The y-axis runs from $980,000 to $1,050,000. The bar heights appear dramatically different, with one region's bar appearing to be three times the height of another. The actual revenue figures are: North $1,040,000; South $990,000; East $1,015,000; West $1,000,000.

**Critique C2 (5 points):** A marketing analyst creates a pie chart to show the distribution of website traffic by source. The chart has 11 slices: Direct, Organic Search, Paid Search, Email, Referral, Social — Facebook, Social — Instagram, Social — Twitter, Social — LinkedIn, Display Ads, and Affiliates.

**Critique C3 (5 points):** A business analyst creates a line chart to show annual revenue for six different product categories (Electronics, Apparel, Grocery, Furniture, Sports, Beauty). The six lines are plotted using six different shades of blue, all similar in darkness.

**Critique C4 (5 points):** A data analyst creates a 3D bar chart to compare quarterly sales across three product lines over four quarters. The three-dimensional depth causes the front bars to appear taller than the back bars even when the values are equal.

### Part C Deliverable

For each critique: name the visualization problem(s), explain the misleading effect on the viewer, and describe the corrected design.

---

## Part D — Applied Selection Rationale (15 points)

### Part D Instructions

A nonprofit organization collects the following data about its fundraising campaigns. For each of the three reporting tasks below, recommend a complete visualization solution — chart type, key design decisions, and what story the chart should tell.

**Task D1 (5 points):** The executive director wants a chart showing how total donations changed month by month over the past three years, with a visual indicator of whether each month was above or below the three-year monthly average.

**Task D2 (5 points):** The development team wants to show donors how the $2.4 million in donations was distributed across six program areas (Education 38%, Health 24%, Environment 18%, Housing 12%, Arts 5%, Other 3%).

**Task D3 (5 points):** The research team wants to explore whether there is a relationship between the size of a donor's first gift and their total lifetime giving. The dataset has 1,200 donor records.

### Part D Deliverable

For each task: chart type, three specific design decisions (axis range, color, sorting, etc.), and a one-sentence description of what insight the chart should make immediately visible.

---

## Submission Instructions

Compile all deliverables — written answers, code, and chart PNGs — into a single PDF. Name your file: `Lab07_LastName_FirstName.pdf`. Submit to Canvas before the stated deadline.

---

## Grading Rubric Summary

| Part | Description | Points |
|---|---|---|
| A | Chart Type Selection (5 scenarios) | 25 |
| B | Creating Charts with Python (4 charts) | 40 |
| C | Visualization Critique (4 examples) | 20 |
| D | Applied Selection Rationale | 15 |
| **Total** | | **100** |

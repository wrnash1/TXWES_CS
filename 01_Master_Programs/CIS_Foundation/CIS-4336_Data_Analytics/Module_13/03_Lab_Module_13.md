# Lab: Module 13 — Reporting and Dashboard Design

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Lab Overview

In this lab you will design and critique dashboards without requiring any BI software. You will produce a written dashboard specification, evaluate a provided dashboard using the five design principles, and select appropriate chart types for six business scenarios. This lab builds the design judgment tested on the Data+ exam and required in professional analyst roles.

**Estimated time:** 75–90 minutes

**Tools required:** Word processor or markdown editor (no BI software needed)

**Deliverable:** A single document named `module13_lab_[YourLastName].pdf`

---

### Learning Objectives

By completing this lab you will be able to:

* Apply the five dashboard design principles to evaluate an existing dashboard
* Write a complete dashboard specification for a defined audience and purpose
* Select the correct chart type for six distinct business scenarios
* Define three KPIs with all required properties for a given business context
* Identify and correct three common dashboard design errors

---

### Part 1: Dashboard Critique (20 minutes)

#### Step 1.1 — Access the Sample Dashboard

Open the sample dashboard image provided in the course LMS: `module13_sample_dashboard.png`. This is a deliberately flawed operational dashboard for a regional retail chain.

#### Step 1.2 — Evaluate Against Design Principles

For each of the five dashboard design principles, write two to four sentences describing:

* Whether the sample dashboard follows the principle
* If it violates the principle, describe the specific violation
* What change would fix the violation

Use this structure for each principle:

**Principle 1 — Single Audience, Single Purpose:**

Write your evaluation here.

**Principle 2 — Limit the KPI Count:**

Write your evaluation here.

**Principle 3 — Consistent Color Encoding:**

Write your evaluation here.

**Principle 4 — Remove Chart Junk:**

Write your evaluation here.

**Principle 5 — Proximity and Grouping:**

Write your evaluation here.

#### Step 1.3 — Overall Score

Rate the sample dashboard on a scale of 1 to 10 for overall communication effectiveness and write three sentences justifying your score.

---

### Part 2: Dashboard Specification (30 minutes)

You have been asked to design a new operations dashboard for the regional manager of a mid-size insurance company. The manager oversees 12 agents and is responsible for ensuring claim processing speed, agent productivity, and customer satisfaction.

Write a complete dashboard specification using the template below. Every field must be completed.

#### Dashboard Specification Template

**Dashboard title:** [Your proposed title]

**Primary audience:** [Role and brief description]

**Primary question this dashboard answers:** [One sentence]

**Update frequency:** [Real-time / Hourly / Daily / Weekly]

**Access method:** [Desktop browser / Mobile app / Printed report]

#### KPI Tiles (top of dashboard — maximum 5)

For each KPI tile provide all of the following:

KPI 1:

* Name:
* Definition (exact calculation):
* Unit:
* Target value:
* Direction (higher is better / lower is better / maintain range):
* Data source column(s):

KPI 2:

* Name:
* Definition:
* Unit:
* Target value:
* Direction:
* Data source column(s):

KPI 3:

* Name:
* Definition:
* Unit:
* Target value:
* Direction:
* Data source column(s):

#### Charts Section (below KPI tiles — maximum 4 charts)

For each chart provide:

Chart 1:

* Title:
* Chart type:
* X-axis (or categories):
* Y-axis (or values):
* Why this chart type is correct for this data relationship:

Chart 2:

* Title:
* Chart type:
* X-axis (or categories):
* Y-axis (or values):
* Why this chart type is correct for this data relationship:

Chart 3:

* Title:
* Chart type:
* X-axis (or categories):
* Y-axis (or values):
* Why this chart type is correct for this data relationship:

#### Color Scheme

* On-target color:
* Below-target color:
* Primary data series color:
* Background color:

#### Data Definitions Footnote

Write two to three sentences that would appear at the bottom of the dashboard defining any metric whose calculation might be ambiguous.

---

### Part 3: Chart Type Selection (15 minutes)

For each of the six scenarios below, identify the single most appropriate chart type and write one sentence explaining why.

**Scenario 1:** A marketing analyst wants to show how total monthly website traffic has changed over the past 24 months.

* Chart type:
* Justification:

**Scenario 2:** A finance analyst wants to compare total annual revenue across eight business units for the current year.

* Chart type:
* Justification:

**Scenario 3:** A data scientist wants to show the relationship between customer age and average order value across 10,000 customer records.

* Chart type:
* Justification:

**Scenario 4:** A product manager wants to show what percentage of total revenue comes from each of the company's four product lines.

* Chart type:
* Justification:

**Scenario 5:** An HR analyst wants to show the distribution of employee tenure in years across the organization to identify whether the workforce is heavily weighted toward new hires or long-tenured employees.

* Chart type:
* Justification:

**Scenario 6:** A supply chain analyst wants to show average shipping time (in days) by destination country on a world map so regional differences are immediately visible.

* Chart type:
* Justification:

---

### Part 4: Data Storytelling Draft (10 minutes)

Write a four-part data narrative for the following scenario. Each part must be one to three sentences.

**Scenario:** Your analysis of Q3 sales data reveals that the West region's conversion rate dropped from 18% to 11% between July and September. The drop coincides with the launch of a competitor's promotional campaign in that region. All other regions maintained stable conversion rates above 16%.

**Context (1–3 sentences):**

**Finding (1 sentence — plain language, no jargon):**

**Evidence (1–2 sentences describing what chart you would show and what annotation you would add):**

**Implication (1–2 sentences):**

---

### Submission Instructions

Compile all four parts into a single PDF document named `module13_lab_[YourLastName].pdf`. Submit to the course LMS by the deadline. Ensure all fields are completed — partial submissions receive partial credit only for sections that are complete.

---

### Grading Rubric

| Criterion | Points |
|---|---|
| Part 1: Critique addresses all five principles with specific evidence | 20 |
| Part 2: Dashboard spec has all required fields with complete KPI definitions | 30 |
| Part 2: Chart choices are appropriate for the described metrics | 10 |
| Part 3: All six chart selections are correct and justified | 24 |
| Part 4: All four narrative parts present and clearly written | 16 |
| **Total** | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Dashboard Critique and Redesign Proposal

Apply the five dashboard design principles from Module 13 to evaluate a real-world BI screenshot and produce a structured redesign brief.

1. Find a public Tableau Public or Power BI community dashboard that contains at least 3 charts and 4 KPI tiles (search Tableau Public at <https://public.tableau.com/app/discover> for any topic that interests you). Capture the URL. For each of the five design principles (single audience/purpose, limit KPI count, consistent color encoding, remove chart junk, appropriate chart types), write 2–3 sentences assessing whether the dashboard follows or violates the principle, citing specific elements from the dashboard as evidence.
2. Produce a written redesign brief (minimum 300 words) that: (a) states the target audience and purpose you would assign to the dashboard, (b) names the 3–5 KPIs you would keep or replace and why, (c) describes the color palette you would standardize on and what each color would represent, and (d) identifies at least two chart types you would change and specifies the replacement chart type with justification.

No code is required for this challenge. Submit the dashboard URL, the five-principle critique, and the redesign brief as a written document.

### Challenge 2: Python Dashboard Mock-Up with matplotlib

Build a 2×2 dashboard figure using matplotlib subplots that mirrors the structure of a professional BI dashboard: one KPI scorecard panel, one trend chart, one comparison chart, and one distribution chart.

1. Using the retail sales dataset from Lab 07 (or any dataset from a previous lab), create a `fig, axes = plt.subplots(2, 2, figsize=(14, 9))` layout with: (a) top-left: a text-only "KPI panel" using `ax.text()` displaying total revenue, order count, and average order value as formatted strings with color-coded deltas vs. prior period; (b) top-right: a line chart of monthly revenue trend; (c) bottom-left: a grouped or stacked bar chart comparing revenue by region for two periods; (d) bottom-right: a histogram of order value distribution with mean and median lines.
2. Apply consistent styling: use a single color palette across all four panels, add a `fig.suptitle()` dashboard title, and remove unnecessary spines (use `ax.spines['top'].set_visible(False)` and `ax.spines['right'].set_visible(False)` on all axes). Save as `dashboard_mockup.png` at `dpi=150`. Write two sentences evaluating which of the four panels is most and least effective at communicating a business insight and why.

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Load your dataset (adjust path as needed)
df = pd.read_csv("retail_sales.csv")
df["month_order"] = df["month"].map({"Jan": 1, "Feb": 2})

monthly_rev = df.groupby("month")["sales_amount"].sum().reindex(["Jan", "Feb"])
region_rev  = df.groupby(["region", "month"])["sales_amount"].sum().unstack(fill_value=0)

total_rev  = df["sales_amount"].sum()
order_cnt  = len(df)
avg_order  = total_rev / order_cnt

BLUE  = "#2196F3"
GREEN = "#4CAF50"
GRAY  = "#9E9E9E"

fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle("Sales Performance Dashboard", fontsize=16, fontweight="bold", y=1.01)

# KPI Panel
ax = axes[0, 0]
ax.axis("off")
ax.text(0.5, 0.75, f"Total Revenue\n${total_rev:,.0f}", ha="center", va="center",
        fontsize=14, fontweight="bold", color=BLUE, transform=ax.transAxes)
ax.text(0.5, 0.50, f"Order Count\n{order_cnt}", ha="center", va="center",
        fontsize=14, color=GRAY, transform=ax.transAxes)
ax.text(0.5, 0.25, f"Avg Order Value\n${avg_order:,.0f}", ha="center", va="center",
        fontsize=14, color=GREEN, transform=ax.transAxes)
ax.set_title("KPI Summary", fontsize=11, fontweight="bold")

# Trend chart
ax = axes[0, 1]
ax.plot(monthly_rev.index, monthly_rev.values, marker="o", color=BLUE, linewidth=2)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax.set_title("Monthly Revenue Trend", fontsize=11, fontweight="bold")
for spine in ["top", "right"]: ax.spines[spine].set_visible(False)

# Grouped bar chart
ax = axes[1, 0]
x = np.arange(len(region_rev.index))
w = 0.35
ax.bar(x - w/2, region_rev.get("Jan", 0), w, label="Jan", color=BLUE)
ax.bar(x + w/2, region_rev.get("Feb", 0), w, label="Feb", color=GREEN)
ax.set_xticks(x); ax.set_xticklabels(region_rev.index, rotation=20)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax.legend(fontsize=8)
ax.set_title("Revenue by Region (Jan vs Feb)", fontsize=11, fontweight="bold")
for spine in ["top", "right"]: ax.spines[spine].set_visible(False)

# Histogram
ax = axes[1, 1]
ax.hist(df["sales_amount"], bins=10, color=BLUE, edgecolor="white", alpha=0.85)
ax.axvline(df["sales_amount"].mean(),   color="red",   linestyle="--", linewidth=1.5, label="Mean")
ax.axvline(df["sales_amount"].median(), color="orange", linestyle="-",  linewidth=1.5, label="Median")
ax.set_title("Order Value Distribution", fontsize=11, fontweight="bold")
ax.legend(fontsize=8)
for spine in ["top", "right"]: ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig("dashboard_mockup.png", dpi=150, bbox_inches="tight")
plt.show()
```

### Reflection Questions

1. In Challenge 2, the KPI panel uses `ax.axis("off")` and `ax.text()` to create a text-only scorecard. A colleague suggests using a bar chart for the KPI panel instead to show magnitude. Evaluate this suggestion using the dashboard design principle of appropriate chart type selection — under what circumstances would a bar chart be better, and when is a text-only KPI tile superior?
2. The four-panel dashboard in Challenge 2 is built in Python and saved as a static PNG. A real Power BI or Tableau dashboard would be interactive (filterable, drillable). Describe two specific interactive features that would make this dashboard significantly more useful for a business user, and explain what technical capability (filter, slicer, drill-through, tooltip) each feature represents.

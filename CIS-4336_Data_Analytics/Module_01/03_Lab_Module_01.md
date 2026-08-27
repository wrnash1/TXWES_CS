# Lab 01 — Data Analytics Fundamentals and Data Types

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 1

---

## Objectives

By completing this lab, you will be able to:

- Classify variables by data type and scale of measurement
- Distinguish structured, semi-structured, and unstructured data sources
- Map real-world analyst activities to the correct analytics lifecycle stage
- Identify which analytic type (descriptive, diagnostic, predictive, prescriptive) applies to a given scenario

---

## Prerequisites

- Python 3.8 or later installed, or access to Google Colab
- The pandas library installed (`pip install pandas`)
- Reading Guide Module 01 completed

---

## Part A — Variable Classification (25 points)

### Instructions

The table below contains twelve variables from a fictional retail company dataset. For each variable, provide all of the following:

1. Quantitative or Qualitative
2. If quantitative: Discrete or Continuous
3. If qualitative: Nominal or Ordinal
4. Scale of measurement: Nominal, Ordinal, Interval, or Ratio
5. One valid statistical operation for this variable

### Dataset — Retail Company Variables

| Variable Name | Sample Values |
|---|---|
| Store ID | 1001, 1002, 1003 |
| Region | North, South, East, West |
| Employee Count | 12, 45, 8, 102 |
| Annual Revenue (USD) | 1,200,000 — 8,400,000 |
| Customer Satisfaction | 1, 2, 3, 4, 5 |
| Product Category | Electronics, Apparel, Grocery |
| Return Rate (%) | 2.3%, 5.1%, 0.8% |
| Temperature in Store (C) | 20.1, 21.5, 19.8 |
| Inventory Restock Level | Low, Medium, High |
| Order Timestamp | 2024-01-15 09:32:11 |
| Units Sold per Day | 14, 23, 7, 45 |
| Customer Loyalty Tier | Bronze, Silver, Gold, Platinum |

### Deliverable A

Complete the classification table in your submission document. Example format shown for the first row.

| Variable | Quant/Qual | Sub-Type | Scale | Valid Operation |
|---|---|---|---|---|
| Store ID | Qualitative | Nominal | Nominal | Count / Mode |
| Region | | | | |
| Employee Count | | | | |
| Annual Revenue | | | | |
| Customer Satisfaction | | | | |
| Product Category | | | | |
| Return Rate | | | | |
| Temperature in Store | | | | |
| Inventory Restock Level | | | | |
| Order Timestamp | | | | |
| Units Sold per Day | | | | |
| Customer Loyalty Tier | | | | |

**Grading:** 2 points per variable (1 point type classification, 1 point scale). 24 points total for Part A rows 2–12, plus 1 point for completing the header row correctly.

---

## Part B — Data Source Classification (20 points)

### Part B Instructions

Examine the five data sources described below. For each source, identify:

1. Structure type: Structured, Semi-Structured, or Unstructured
2. Likely file format
3. First preprocessing step required before analysis

### Data Source Descriptions

**Source 1:** A nightly export from a point-of-sale system containing transaction ID, item SKU, quantity, unit price, and timestamp in fixed columns. Delivered as a flat text file where fields are separated by commas.

**Source 2:** An API response from a weather service returning JSON objects with nested keys for location, current conditions, and hourly forecasts. Some records include an optional "alerts" array; others do not.

**Source 3:** A folder of 2,400 customer support emails saved as plain text (.txt) files. Each email contains a subject line, body text of variable length, and the customer's email address in the body.

**Source 4:** A database table in a SQL Server instance containing employee records with columns for EMPLOYEE_ID, NAME, DEPARTMENT, HIRE_DATE, and SALARY.

**Source 5:** Scanned images of paper purchase orders from 2019, stored as JPEG files in a shared drive folder.

### Part B Deliverable

Complete this table in your submission document.

| Source | Structure Type | Likely Format | First Preprocessing Step |
|---|---|---|---|
| Source 1 | | | |
| Source 2 | | | |
| Source 3 | | | |
| Source 4 | | | |
| Source 5 | | | |

**Grading:** 4 points per source (1 structure type, 1 format, 2 preprocessing justification). 20 points total.

---

## Part C — Analytics Lifecycle Mapping (20 points)

### Part C Instructions

The scenario below describes ten activities performed by an analytics team at a healthcare company. For each activity, identify which lifecycle stage it belongs to.

Lifecycle stages: Define the Question, Collect Data, Clean and Transform, Analyze, Visualize and Communicate, Act and Monitor.

### Activities

1. The VP of Operations asks: "Why did patient readmission rates increase 12 percent in Q2?"
2. A data engineer writes a Python script to pull records from the hospital EHR system via API.
3. An analyst discovers 340 records with null values in the DISCHARGE_DATE column and fills them using median imputation.
4. An analyst runs a logistic regression to identify which patient attributes predict 30-day readmission.
5. A BI developer builds a Power BI dashboard showing readmission trends by unit and physician.
6. The analytics team presents findings to the Chief Medical Officer with a slide deck of charts and recommendations.
7. The hospital updates its discharge protocol based on the analysis and begins tracking the new protocol's impact.
8. An analyst removes 15 duplicate patient records caused by a system migration error.
9. A data engineer creates a schedule to pull updated data from the EHR system daily.
10. The analytics team reviews KPIs after 60 days to measure whether readmissions declined.

### Part C Deliverable

Complete this table in your submission document.

| Activity | Lifecycle Stage |
|---|---|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |
| 10 | |

**Grading:** 2 points per activity. 20 points total.

---

## Part D — Analytics Type Identification (15 points)

### Part D Instructions

For each of the five business scenarios below, identify the analytics type and write two to three sentences explaining your reasoning.

Analytics types: Descriptive, Diagnostic, Predictive, Prescriptive.

**Scenario 1:** A telecommunications company runs a monthly report showing the number of customer service calls by category (billing, technical support, cancellation) over the past year.

**Scenario 2:** An e-commerce company builds a model that assigns each customer a probability score (0–100) representing their likelihood of making a purchase in the next 30 days.

**Scenario 3:** After noticing a spike in product returns in March, a retail analyst compares returns data against weather records, shipping carrier reports, and product reviews to determine the cause.

**Scenario 4:** A hospital uses an optimization algorithm that, given a patient's risk profile and available treatments, recommends the specific combination of interventions most likely to prevent readmission.

**Scenario 5:** An airline generates a weekly executive summary showing on-time departure rates, average load factor, and fuel cost per seat mile for the prior week.

### Part D Deliverable

For each scenario, write:

- Analytics type
- Two to three sentences of reasoning

**Grading:** 3 points per scenario (1 point correct type, 2 points reasoning quality). 15 points total.

---

## Part E — Python Data Inspection Exercise (20 points)

### Part E Instructions

Run the following Python code block in your local Python environment or Google Colab. Answer the four questions that follow based on the output.

```python
import pandas as pd

data = {
    "customer_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "region": ["North", "South", "North", "East", "West", "South", "East", "North"],
    "satisfaction_score": [4, 2, 5, 3, 4, 1, 5, 3],
    "purchase_amount": [125.50, 88.00, 210.75, 45.20, 300.00, 67.80, 155.00, 90.25],
    "loyalty_tier": ["Silver", "Bronze", "Gold", "Bronze", "Gold", "Bronze", "Gold", "Silver"],
    "items_purchased": [3, 1, 5, 1, 7, 2, 4, 2]
}

df = pd.DataFrame(data)

print("--- Shape ---")
print(df.shape)

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Region Value Counts ---")
print(df["region"].value_counts())
```

### Questions

**Question E1 (5 points):** The `satisfaction_score` column is stored as `int64` in pandas. Should you treat this column as quantitative (ratio) or ordinal qualitative? Explain your answer in three to four sentences, referencing the scale of measurement.

**Question E2 (5 points):** Which columns in this dataset should be converted to a categorical data type in pandas before performing analytics? List each column and state whether it is nominal or ordinal.

**Question E3 (5 points):** `df.describe()` by default only shows statistics for numeric columns. What does this tell you about how pandas handles qualitative columns? What additional pandas method would you use to get frequency statistics for the `region` column?

**Question E4 (5 points):** A colleague proposes computing the average `satisfaction_score` to report "mean customer satisfaction." Using your knowledge of measurement scales, evaluate whether this is a valid operation. Provide your answer in three to five sentences.

### Part E Deliverable

Submit a document containing:

1. A screenshot or copy-paste of your Python output
2. Written answers to Questions E1 through E4

**Grading:** 5 points per question. 20 points total.

---

## Submission Instructions

Compile your completed tables and written answers into a single PDF or Word document. Name your file: `Lab01_LastName_FirstName.pdf`.

Submit to the Canvas assignment portal before the stated deadline.

---

## Grading Rubric Summary

| Part | Description | Points |
|---|---|---|
| A | Variable Classification Table | 25 |
| B | Data Source Classification | 20 |
| C | Analytics Lifecycle Mapping | 20 |
| D | Analytics Type Identification | 15 |
| E | Python Data Inspection | 20 |
| **Total** | | **100** |

---

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Source Data Inventory

Build a mini data inventory for a fictional e-commerce company by performing the following steps.

1. Create a Python dictionary representing three data sources: a SQL orders table (columns: order_id, customer_id, amount, order_date, status), a JSON product review API response with optional nested "media" arrays, and a folder of product photo JPEG files. For each source, record its structure type, file format, and the pandas read function or preprocessing step required to load it.
2. Load the orders table simulation into a pandas DataFrame with at least 10 rows of realistic sample data. Assign correct dtypes — use `pd.Categorical` for `status` (ordinal: Pending, Processing, Shipped, Delivered) and ensure `order_date` is `datetime64`.
3. Call `df.dtypes`, `df.describe()`, and `df["status"].value_counts()` on your DataFrame. For each output, write one sentence explaining what the output reveals and which scale of measurement applies to each column.

```python
import pandas as pd

orders = {
    "order_id": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "customer_id": [201,202,203,201,204,205,202,206,207,201],
    "amount": [59.99,120.00,34.50,89.95,210.00,15.00,77.50,300.00,45.25,130.00],
    "order_date": pd.date_range("2024-01-01", periods=10, freq="3D"),
    "status": pd.Categorical(
        ["Delivered","Shipped","Processing","Delivered","Pending",
         "Delivered","Shipped","Processing","Delivered","Pending"],
        categories=["Pending","Processing","Shipped","Delivered"],
        ordered=True
    )
}
df = pd.DataFrame(orders)
print(df.dtypes)
print(df.describe())
print(df["status"].value_counts())
```

### Challenge 2: Analytics Type Classification Report

Using the same orders DataFrame from Challenge 1, produce a written analytics-type classification for four derived questions.

1. Write Python code to answer each of the following questions about the data, then label each answer as Descriptive, Diagnostic, Predictive, or Prescriptive: (a) What is the total revenue and average order value? (b) Which customer places the most orders? (c) What percentage of orders are still Pending or Processing? (d) If you were to sort customers by total spend and flag the top 20% for a loyalty offer, what analytics type does that action represent?
2. For question (d), extend the DataFrame to add a `high_value` boolean flag using `pd.qcut` or a manual threshold on `amount`. Print the flagged customers.

```python
# (a) Descriptive
print("Total revenue:", df["amount"].sum())
print("Average order value:", df["amount"].mean())

# (b) Descriptive
print("Top customer:", df["customer_id"].value_counts().idxmax())

# (c) Descriptive
pct_open = (df["status"].isin(["Pending","Processing"]).sum() / len(df)) * 100
print(f"Open orders: {pct_open:.1f}%")

# (d) Prescriptive — flagging customers for action
customer_spend = df.groupby("customer_id")["amount"].sum()
threshold = customer_spend.quantile(0.80)
high_value = customer_spend[customer_spend >= threshold].index
print("High-value customers:", high_value.tolist())
```

### Reflection Questions

1. When you called `df.describe()`, the `status` column was excluded from the default output. What does this tell you about how pandas treats ordered categorical variables, and how would you obtain a summary of that column?
2. A marketing manager asks you to "find the average customer satisfaction rating and use it to target unhappy customers." Using what you know about ordinal measurement scales, evaluate whether this request is statistically valid and suggest a more appropriate approach.

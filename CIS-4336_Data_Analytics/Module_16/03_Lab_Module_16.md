# Lab: Module 16 — Data+ DA0-001 Exam Preparation and Capstone

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Lab Overview

This lab has two components. Part 1 is an exam readiness self-assessment — you will map your confidence level against every Data+ domain objective and create a targeted study plan. Part 2 is the capstone project — you will complete an end-to-end analysis using a dataset of your choosing, produce a one-page executive summary, and submit a Jupyter notebook documenting your methodology.

**Estimated time:** 3–4 hours total (self-assessment: 30 minutes; capstone: 2.5–3.5 hours)

**Tools required:** Python 3.10+, JupyterLab or VS Code with Jupyter, pandas, NumPy, matplotlib, seaborn; word processor for executive summary

**Deliverables:**

* `module16_selfassessment_[YourLastName].pdf` — completed self-assessment and study plan
* `module16_capstone_[YourLastName].ipynb` — completed Jupyter notebook
* `module16_executive_summary_[YourLastName].pdf` — one-page executive summary

---

### Part 1: Exam Readiness Self-Assessment (30 minutes)

#### Step 1.1 — Domain Confidence Rating

Rate your current confidence for each topic on a 1–5 scale:

* 1 — I do not know this topic at all
* 2 — I have heard of it but cannot explain it
* 3 — I understand it but am not sure about edge cases
* 4 — I understand it well and can apply it
* 5 — I am confident and could teach this to someone else

#### Domain 1 — Data Concepts and Environments

| Topic | Confidence (1–5) | Notes / Gap |
|---|---|---|
| Structured vs. semi-structured vs. unstructured data | | |
| Quantitative vs. qualitative data types | | |
| First-, second-, and third-party data sources | | |
| Relational vs. non-relational databases | | |
| OLTP vs. OLAP | | |
| Star schema vs. snowflake schema | | |
| ETL vs. ELT | | |
| Data lake vs. data warehouse vs. data mart | | |

#### Domain 2 — Data Mining

| Topic | Confidence (1–5) | Notes / Gap |
|---|---|---|
| SQL query structure (SELECT, WHERE, GROUP BY, JOIN types) | | |
| Null handling: imputation vs. deletion strategies | | |
| Outlier detection: IQR method and Z-score | | |
| Data quality dimensions (all six) | | |
| Deduplication techniques | | |
| Data transformation: aggregation, parsing, deriving | | |
| ETL pipeline stages | | |
| Metadata and data catalogs | | |

#### Domain 3 — Data Analysis and Statistics

| Topic | Confidence (1–5) | Notes / Gap |
|---|---|---|
| Mean, median, mode — when to use each | | |
| Variance and standard deviation | | |
| Normal distribution and the 68-95-99.7 rule | | |
| Skewness (left and right) and effect on mean vs. median | | |
| Correlation coefficient interpretation | | |
| Correlation vs. causation | | |
| Linear regression and R² | | |
| Hypothesis testing: p-value, Type I error, Type II error | | |
| Supervised vs. unsupervised learning | | |
| Overfitting vs. underfitting | | |
| Train/test split purpose | | |
| Feature engineering techniques | | |
| Analysis types: trend, cohort, root cause, gap, what-if | | |

#### Domain 4 — Data Visualization and Reporting

| Topic | Confidence (1–5) | Notes / Gap |
|---|---|---|
| Chart type selection for each data relationship | | |
| Dashboard design five principles | | |
| KPI vs. metric vs. benchmark | | |
| Leading vs. lagging indicator | | |
| Vanity metric vs. actionable KPI | | |
| Tableau, Power BI, Looker — key differences | | |
| Report types: operational, analytical, executive | | |
| Data storytelling four-part structure | | |

#### Domain 5 — Data Governance

| Topic | Confidence (1–5) | Notes / Gap |
|---|---|---|
| GDPR scope, rights, and penalties | | |
| CCPA scope and key rights | | |
| HIPAA Privacy Rule and Security Rule | | |
| PII direct identifiers vs. quasi-identifiers | | |
| Anonymization techniques: masking, pseudonymization, generalization, k-anonymity | | |
| Algorithmic bias types | | |
| Data minimization and purpose limitation | | |

#### Step 1.2 — Study Priority Plan

Review your ratings. For any topic rated 1 or 2:

* List the topic
* Identify which module reading guide covers it
* Write two to three sentences describing what you need to review

Create a study schedule for the remaining time before the exam. Be specific about which days and topics.

---

### Part 2: Capstone Project

#### Step 2.1 — Dataset Selection

Choose one of the following options:

* **Option A — Provided dataset**: Use `capstone_sales_module16.csv` from the course LMS (10,000 rows, 14 columns, retail sales data)
* **Option B — Public dataset**: Choose any dataset from Kaggle, the US government data portal (data.gov), or the Texas Tribune's data portal, minimum 1,000 rows and 6 columns
* **Option C — Your own data**: Use a dataset from your workplace or personal project, minimum 1,000 rows and 6 columns; remove any real PII before submission

Document your choice in a markdown cell at the top of your notebook, including: dataset name and source, number of rows and columns, and the business question you will answer.

#### Step 2.2 — Business Question

Define one clear, answerable business question. Examples:

* "Which product categories generate the highest profit margin and how has this changed over the last four quarters?"
* "Which customer segments have the highest churn risk based on purchase frequency and support ticket history?"
* "What factors are most strongly correlated with employee tenure at this organization?"

Your question must be answerable from the data you have selected. Write it in a markdown cell.

#### Step 2.3 — Data Loading and Inspection

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('your_dataset.csv')
print(f"Shape: {df.shape}")
print(df.dtypes)
print(df.isnull().sum())
df.describe()
```

#### Step 2.4 — Data Cleaning

Apply appropriate cleaning steps for your dataset. Document each step with a markdown cell explaining:

* What the issue was
* What strategy you chose
* Why you chose that strategy over alternatives

Minimum requirements:

* Handle all null values (imputation or deletion with justification)
* Remove or flag any duplicate rows
* Identify and address at least one outlier column using IQR or Z-score

#### Step 2.5 — Analysis

Perform the analysis required to answer your business question. Minimum requirements:

* At least two groupby aggregations
* At least one pivot_table or merge operation
* At least two descriptive statistics (mean, median, standard deviation, percentile)

All results must be displayed in the notebook with outputs visible.

#### Step 2.6 — Visualization

Produce at least three charts that directly support the answer to your business question. Requirements:

* All charts must have titles, labeled axes, and units
* Charts must use appropriate types for the data relationship (refer to Domain 4 review)
* At least one chart must include a text annotation highlighting the most important finding

Save all charts as PNG files using `plt.savefig()`.

#### Step 2.7 — One-Page Executive Summary

Produce a separate PDF document (one page maximum) structured as follows:

#### Section 1 — Business Question (1 sentence)

#### Section 2 — Key Finding (2–3 sentences in plain language, no jargon)

#### Section 3 — Supporting Evidence (include your most compelling chart and 1–2 sentences explaining it)

#### Section 4 — Recommendation (2–3 sentences stating what action the finding supports)

#### Section 5 — Data Notes (2–3 sentences: data source, time period, key limitations)

---

### Submission Instructions

Submit all three deliverables to the course LMS by the posted deadline:

* `module16_selfassessment_[YourLastName].pdf`
* `module16_capstone_[YourLastName].ipynb` (all cells executed, outputs visible)
* `module16_executive_summary_[YourLastName].pdf`

---

### Grading Rubric

| Criterion | Points |
|---|---|
| Self-assessment: all domain topics rated with gap notes | 10 |
| Self-assessment: study plan is specific and actionable | 5 |
| Capstone: business question is clear and answerable | 5 |
| Capstone: data loading and inspection complete | 5 |
| Capstone: cleaning steps with markdown justification | 15 |
| Capstone: analysis answers the business question with groupby and stats | 20 |
| Capstone: three charts correct for data type with titles and labels | 20 |
| Capstone: at least one annotated chart highlighting key finding | 5 |
| Executive summary: follows four-part structure, plain language, one page | 15 |
| **Total** | **100** |

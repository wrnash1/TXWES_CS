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

---

## Part 9 — Challenge Exercise

### Challenge 1: Domain-by-Domain Diagnostic Practice Exam

Build a self-scoring practice exam tool in Python that simulates a timed Data+ domain diagnostic.

1. Create a Python dictionary `exam_bank` with at least 15 questions distributed across all 5 Data+ domains (3 per domain minimum). Each entry should be a dictionary with keys: `domain`, `question`, `options` (list of 4 strings), `answer` (correct letter A/B/C/D), and `explanation`. Write a function `run_exam(questions, time_limit_minutes=20)` that presents each question, accepts user input, tracks time elapsed, and at the end prints a domain-by-domain score breakdown (correct / total per domain) with the explanation for each missed question.
2. After running the exam (or simulating it with pre-filled answers), produce a radar/spider chart using matplotlib that shows the percentage score per domain as a filled polygon. Save as `domain_radar.png`. Write two sentences identifying which domain your simulated score was weakest in and what specific Module reading guide sections you would revisit based on that result.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

exam_bank = [
    {"domain": "Domain 1", "question": "Which schema uses a central fact table with denormalized dimensions?",
     "options": ["A) Snowflake schema","B) Star schema","C) Third normal form","D) Entity-relationship model"],
     "answer": "B", "explanation": "Star schema: fact table + denormalized dimension tables."},
    {"domain": "Domain 2", "question": "Which imputation is best for right-skewed salary data with nulls?",
     "options": ["A) Mean","B) Median","C) Drop rows","D) Zero fill"],
     "answer": "B", "explanation": "Median is resistant to outlier distortion in skewed distributions."},
    {"domain": "Domain 3", "question": "A p-value of 0.03 at alpha=0.05 means:",
     "options": ["A) Accept H0","B) Reject H0","C) Inconclusive","D) 97% certain"],
     "answer": "B", "explanation": "p < alpha → reject null hypothesis."},
    {"domain": "Domain 4", "question": "Best chart to show distribution and outliers across regions?",
     "options": ["A) Pie chart","B) Line chart","C) Box plot","D) Scatter plot"],
     "answer": "C", "explanation": "Box plots show median, IQR, and outliers per category."},
    {"domain": "Domain 5", "question": "GDPR right to erasure response window?",
     "options": ["A) 15 days","B) 30 days","C) 45 days","D) 90 days"],
     "answer": "B", "explanation": "GDPR requires response within one calendar month."},
]

def run_exam(questions, time_limit_minutes=20, auto_answers=None):
    domain_scores = {}
    missed = []
    start = time.time()

    for i, q in enumerate(questions):
        print(f"\nQ{i+1} [{q['domain']}]: {q['question']}")
        for opt in q["options"]:
            print(f"  {opt}")

        if auto_answers:
            answer = auto_answers[i]
            print(f"  Your answer: {answer}")
        else:
            answer = input("  Your answer (A/B/C/D): ").strip().upper()

        elapsed = (time.time() - start) / 60
        if elapsed > time_limit_minutes:
            print("\nTime limit reached.")
            break

        d = q["domain"]
        domain_scores.setdefault(d, {"correct": 0, "total": 0})
        domain_scores[d]["total"] += 1
        if answer == q["answer"]:
            domain_scores[d]["correct"] += 1
        else:
            missed.append(q)

    print("\n=== RESULTS BY DOMAIN ===")
    for d, s in sorted(domain_scores.items()):
        pct = s["correct"] / s["total"] * 100 if s["total"] else 0
        print(f"  {d}: {s['correct']}/{s['total']} ({pct:.0f}%)")
    if missed:
        print("\n=== MISSED QUESTIONS ===")
        for q in missed:
            print(f"  [{q['domain']}] {q['question']}")
            print(f"  Explanation: {q['explanation']}")

    return domain_scores

# Simulate with pre-filled answers
simulated = ["B", "B", "B", "C", "A"]
scores = run_exam(exam_bank, auto_answers=simulated)

domains = sorted(scores.keys())
pcts = [scores[d]["correct"] / scores[d]["total"] * 100 for d in domains]
angles = np.linspace(0, 2 * np.pi, len(domains), endpoint=False).tolist()
pcts_plot = pcts + [pcts[0]]
angles += [angles[0]]
labels = [d.replace("Domain ", "D") for d in domains]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.plot(angles, pcts_plot, "o-", linewidth=2, color="steelblue")
ax.fill(angles, pcts_plot, alpha=0.25, color="steelblue")
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_title("Data+ Domain Score Radar", size=13, fontweight="bold", pad=15)
plt.tight_layout()
plt.savefig("domain_radar.png", dpi=150)
plt.show()
```

### Challenge 2: End-to-End Mini Capstone — Dataset Choice

Select one of the following freely available datasets and conduct a complete end-to-end analysis applying all five course skill areas. Submit as a Jupyter notebook.

**Dataset options (choose one):**

* Kaggle — Titanic survival dataset: <https://www.kaggle.com/competitions/titanic/data>
* UCI ML Repository — Adult income dataset: <https://archive.ics.uci.edu/ml/datasets/adult>
* Kaggle — NYC Taxi Trips (sample): <https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data>

**Required deliverables in your notebook:**

1. **Domain 1/2 — Data Loading and Quality Audit:** Load the dataset, inspect shape and dtypes, compute a completeness scorecard, flag at least two data quality issues (validity, uniqueness, or accuracy), and apply appropriate fixes with written justification.
2. **Domain 3 — Statistical Analysis:** Compute descriptive statistics for all numeric columns. Identify and describe one significant correlation. Formulate and execute one hypothesis test (t-test or chi-square) answering a question about the data. State H0, H1, alpha, decision, and conclusion.
3. **Domain 3/4 — Machine Learning:** Train a classification or regression model. Produce a train/test split with stratification if classification. Evaluate with at least two metrics appropriate to the task. Visualize feature importances.
4. **Domain 4 — Visualization and Storytelling:** Produce three publication-quality charts (appropriate types for the analytical question). Write a four-part data story (Context → Finding → Evidence → Implication) summarizing the most important insight.
5. **Domain 5 — Ethics and Governance Review:** Identify any PII or quasi-identifiers in the dataset. State which anonymization technique you applied or would apply. Identify any potential bias source in the data and describe how you would address it.

### Reflection Questions

1. After completing Challenge 1's domain radar chart, which domain had your lowest simulated score? For that domain, list three specific terms or concepts from the course where additional study would most improve your confidence on the real Data+ exam.
2. In Challenge 2, you applied all five Data+ domains to a single dataset. Describe the single most difficult or surprising step in the workflow and explain what knowledge from a specific module reading guide you applied to resolve it. What would you do differently if you were starting the same analysis over?

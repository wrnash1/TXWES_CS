# Reading Guide — Module 01: Data Analytics Fundamentals and Data Types

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 1: Data Concepts and Environments

---

## Overview

This reading guide supports Module 01 and maps directly to Domain 1 of the CompTIA Data+ DA0-001 exam. Work through each section before attempting the lab or quiz. The tables and reference sheets in this guide are designed for both study and on-the-job use.

---

## Section 1 — Core Vocabulary

Mastery of precise terminology is the first requirement for both the exam and professional practice.

| Term | Definition |
|---|---|
| Data analytics | The process of examining raw data to uncover patterns, draw conclusions, and support decisions |
| Descriptive analytics | Summarizes historical data to answer "what happened?" |
| Diagnostic analytics | Investigates root causes to answer "why did it happen?" |
| Predictive analytics | Uses models and statistics to answer "what is likely to happen?" |
| Prescriptive analytics | Recommends actions to answer "what should we do?" |
| Structured data | Data organized into a predefined schema of rows and columns |
| Unstructured data | Data with no predefined format (text, images, audio, video) |
| Semi-structured data | Data with partial organization via tags or keys, but no rigid schema (JSON, XML) |
| Quantitative data | Numeric data supporting arithmetic operations |
| Qualitative data | Categorical data representing labels or groups |
| Discrete data | Quantitative data taking only countable, whole-number values |
| Continuous data | Quantitative data that can take any value within a range |
| Nominal data | Categorical data with no inherent order |
| Ordinal data | Categorical data with a meaningful order but unequal intervals |
| Data literacy | The ability to read, interpret, communicate, and reason with data |
| Analytics lifecycle | The repeatable process from question definition through action and monitoring |

---

## Section 2 — Data Type Classification Table

Use this table to classify any variable you encounter in practice or on the exam.

| Data Type | Sub-Type | Order? | Equal Intervals? | True Zero? | Valid Statistics | Examples |
|---|---|---|---|---|---|---|
| Qualitative | Nominal | No | No | No | Count, mode, frequency | Color, zip code, category |
| Qualitative | Ordinal | Yes | No | No | Median, percentile, mode | Survey ratings, letter grades, rank |
| Quantitative | Interval | Yes | Yes | No | Mean, std dev, range | Temperature (C/F), calendar year |
| Quantitative | Ratio | Yes | Yes | Yes | All operations, ratios | Height, income, weight, duration |
| Quantitative | Discrete | Yes | Yes | Yes | Count, mean, mode | Units sold, ticket count |
| Quantitative | Continuous | Yes | Yes | Yes | Mean, median, std dev, percentile | Revenue, temperature, elapsed time |

---

## Section 3 — Analytics Type Reference

| Analytics Type | Business Question | Complexity | Common Techniques | Example |
|---|---|---|---|---|
| Descriptive | What happened? | Low | Aggregation, summarization | Monthly revenue report |
| Diagnostic | Why did it happen? | Medium | Drill-down, correlation | Q3 sales drop investigation |
| Predictive | What will happen? | High | Regression, classification | Customer churn forecast |
| Prescriptive | What should we do? | Highest | Optimization, simulation | Supply chain routing recommendation |

---

## Section 4 — Data Structure Comparison

| Characteristic | Structured | Semi-Structured | Unstructured |
|---|---|---|---|
| Schema | Predefined, rigid | Partial (tags/keys) | None |
| Examples | Relational database tables, CSV | JSON, XML, log files | Email text, images, video, PDFs |
| Query method | SQL | XPath, JSONPath, SQL variants | NLP, computer vision, manual review |
| Storage | RDBMS, data warehouse | Document stores, NoSQL | Object storage, data lakes |
| Approx. share of enterprise data | 20% | — | 80% |
| Ease of analysis | High | Medium | Low without preprocessing |

---

## Section 5 — Common File Formats Reference

| Format | Type | Structure | Best For | Limitations |
|---|---|---|---|---|
| CSV | Text | Structured (flat) | Data exchange, simple tables | No schema enforcement, no nested data |
| JSON | Text | Semi-structured | API responses, nested data | Verbose at large scale |
| XML | Text | Semi-structured | Enterprise integration, config | Very verbose, complex parsing |
| Parquet | Binary | Structured (columnar) | Big data analytics, Spark/Hadoop | Not human-readable |
| Avro | Binary | Semi-structured | Kafka streaming, Hadoop | Requires schema registry |
| Excel (.xlsx) | Binary | Structured | Business reporting | Not ideal for programmatic processing |
| TSV | Text | Structured (flat) | Data with embedded commas | Less universal than CSV |

---

## Section 6 — Analytics Lifecycle Stage Reference

| Stage | Key Activities | Common Tools | Exam Focus |
|---|---|---|---|
| 1. Define the question | Stakeholder interviews, scope definition | Whiteboarding, project briefs | Recognizing when scope is unclear |
| 2. Collect data | ETL, API calls, web scraping, surveys | Python, SQL, Talend | Source classification, data types |
| 3. Clean and transform | Deduplication, null handling, normalization | Python/pandas, OpenRefine | Data quality dimensions |
| 4. Analyze | Statistical testing, aggregation, modeling | Python, R, SQL | Choosing appropriate methods |
| 5. Visualize and communicate | Charts, dashboards, narratives | Power BI, Tableau, matplotlib | Chart type selection |
| 6. Act and monitor | Deployment, KPI tracking, iteration | Dashboards, alerting | Outcome measurement |

---

## Section 7 — Scales of Measurement Decision Guide

When you encounter a variable, ask these questions in order.

1. Do the values represent named categories with no meaningful order?
   - Yes: **Nominal**
2. Are the categories ordered, but intervals between them are unequal or unknown?
   - Yes: **Ordinal**
3. Are the intervals equal, but there is no true zero point?
   - Yes: **Interval**
4. Are the intervals equal and is zero meaningful (absence of the quantity)?
   - Yes: **Ratio**

---

## Section 8 — Data+ Exam Tips

The following eight tips directly address how these concepts appear on the CompTIA Data+ DA0-001 exam.

1. **The Likert trap.** A five-point satisfaction scale uses numbers, but it is ordinal, not quantitative. The intervals between points are not guaranteed equal. Computing a mean is technically inappropriate, though common in practice. On the exam, classify these as ordinal.

2. **CSV is not always structured.** A CSV exported from a clean relational database is structured. A raw CSV scrape of a web page with inconsistent columns is closer to semi-structured. Context matters — read the question carefully.

3. **Zip codes are nominal.** Even though zip codes are numbers, you cannot average or rank them meaningfully. They are nominal categorical values.

4. **Descriptive vs. diagnostic.** Exam scenarios will describe an analyst activity and ask you to name the analytics type. "Reviewing last quarter's sales figures" is descriptive. "Investigating why last quarter's sales fell short" is diagnostic.

5. **Temperature scale distinction.** The exam may ask whether temperature in Celsius is interval or ratio. The correct answer is interval — 0 degrees Celsius does not mean "no temperature." Temperature in Kelvin is ratio because 0 Kelvin means absolute zero.

6. **Unstructured data requires preprocessing.** Any question involving text mining, NLP, or image analysis begins with an unstructured data source. The first step in the lifecycle for unstructured data is always preprocessing or feature extraction.

7. **Domain 1 is not just definitions.** Expect scenario-based questions that ask you to apply these classifications to business situations — not just recite definitions.

8. **Know the exam blueprint.** The official objectives are publicly available at comptia.org. Domain 1 (Data Concepts and Environments) is approximately 15 percent of the exam. Review the subdomain headings to prioritize study time.

---

## Section 9 — Python Pandas Quick Reference (Preview)

Module 09 covers pandas in depth. This preview introduces the data type concepts in a Python context.

```python
import pandas as pd

# Load a CSV dataset
df = pd.read_csv("sales_data.csv")

# Inspect data types — pandas infers Python types, not measurement scales
print(df.dtypes)

# Common dtype mappings:
# int64   → likely discrete quantitative
# float64 → likely continuous quantitative
# object  → likely nominal or ordinal qualitative
# bool    → binary nominal

# Convert a column to categorical (ordinal) type
df["satisfaction"] = pd.Categorical(
    df["satisfaction"],
    categories=["Poor", "Fair", "Good", "Excellent"],
    ordered=True
)

# Count frequencies for a qualitative variable
print(df["region"].value_counts())
```

---

## Section 10 — Study Checklist

Work through each item before moving to the Lab and Quiz.

- [ ] Memorize all 16 core vocabulary terms in Section 1
- [ ] Practice classifying variables using the Section 2 table
- [ ] Distinguish all four analytics types and supply one example of each
- [ ] Correctly classify at least five file formats by structure type
- [ ] Work through the Scales of Measurement decision guide in Section 7 with five practice variables
- [ ] Review all eight Data+ exam tips in Section 8
- [ ] Review the official CompTIA Data+ exam objectives at comptia.org
- [ ] Explore Professor Messer's Data+ study resources at professormesser.com
- [ ] Complete Lab 01
- [ ] Complete Quiz 01

---

## Additional Resources

- Official exam objectives: comptia.org (search "Data+ DA0-001 exam objectives")
- Professor Messer's free study guides and practice questions: professormesser.com

## 9. Supplemental Resources

**1. Google Data Analytics Certificate — Foundations of Data (Coursera)**
<https://www.coursera.org/learn/foundations-data>
A beginner-friendly introduction to data types, the analytics lifecycle, and the role of a data analyst. Covers structured vs. unstructured data and the four analytics types with real-world examples.

**2. Kaggle Learn — Intro to Machine Learning (Data Types and Exploration)**
<https://www.kaggle.com/learn/intro-to-machine-learning>
Hands-on Python notebooks exploring data classification and feature types in pandas. Exercises reinforce the distinction between nominal, ordinal, and quantitative variables in a practical ML context.

**3. StatQuest with Josh Starmer — Types of Data (YouTube)**
<https://www.youtube.com/watch?v=hZxnzfnt5v8>
A concise visual explanation of the four scales of measurement (nominal, ordinal, interval, ratio) with memorable examples. Highly effective for exam preparation on measurement scale questions.

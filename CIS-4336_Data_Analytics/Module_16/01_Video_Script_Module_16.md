# Video Script: Module 16 — Data+ DA0-001 Exam Preparation and Capstone

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

**Estimated Duration:** 22–28 minutes

---

### [00:00 – 02:30] Introduction

**Visual:** Instructor on camera with title card: **Data+ DA0-001 Exam Preparation and Capstone**.

**Audio:** "Welcome to Module 16 — the final module of CIS-4336. This module has two purposes. First, we do a comprehensive review of all five Data+ exam domains so you leave this course with a clear picture of what the exam tests and how to prepare. Second, you complete a capstone project that integrates the technical and communication skills from the entire course. If you have been working through this course systematically, you are already well-prepared. This module is about consolidating that preparation, filling gaps, and building confidence. Let's start with the exam itself."

**Study Link:** [CompTIA Data+ Exam Objectives DA0-001 — free PDF](https://www.comptia.org/certifications/data)

---

### [02:30 – 06:00] Data+ Exam Structure

**Visual:** Exam overview slide with domain weights, question count, passing score, and format.

**Alt-text:** Table showing: Total questions: 90 maximum; Time: 90 minutes; Passing score: 675 out of 900; Question types: multiple choice and performance-based; Cost: $338 USD; Domains: 5.

**Audio:** "The CompTIA Data+ DA0-001 exam consists of up to 90 questions and gives you 90 minutes to complete it. The passing score is 675 on a scale of 900. Question types include multiple choice with one correct answer — which is what you have been practicing in every module quiz — and performance-based questions that present a scenario or tool interface and ask you to complete a task or identify a correct configuration.

The exam is organized into five domains with these approximate weights:

Domain 1 — Data Concepts and Environments: 15%.
Domain 2 — Data Mining: 25%.
Domain 3 — Data Analysis and Statistics: 23%.
Domain 4 — Data Visualization and Reporting: 22%.
Domain 5 — Data Governance: 15%.

Domain 2, Data Mining, has the highest weight at 25%. Domain 4, Visualization, is the second highest at 22%. Together they account for nearly half the exam. If you are short on preparation time, prioritize those two domains."

---

### [06:00 – 10:00] Domain 1 Review — Data Concepts and Environments

**Visual:** Mind map of Domain 1 topics.

**Alt-text:** A central node labeled Domain 1 with branches for: Data Types, Data Sources, Data Structures, Database Concepts, Data Warehousing, Cloud Concepts.

**Audio:** "Domain 1 tests your understanding of foundational data concepts. The high-frequency topics are:

**Data types** — quantitative versus qualitative; structured, semi-structured, and unstructured; discrete versus continuous.

**Data sources** — first-party data (your own collection), second-party data (another organization's data shared with you), third-party data (purchased from a data broker).

**Database concepts** — relational vs. non-relational; OLTP (transactional processing) vs. OLAP (analytical processing); normalization; primary keys, foreign keys.

**Data warehousing** — star schema, snowflake schema, fact tables, dimension tables, ETL versus ELT.

**Cloud concepts** — IaaS, PaaS, SaaS; shared responsibility model; benefits of cloud analytics: scalability, cost flexibility, managed infrastructure.

Common exam traps: confusing OLTP with OLAP, confusing the star schema with the snowflake schema, and misidentifying data source types. First-party means you collected it directly from your customers. Third-party means a vendor collected it and sold it to you."

---

### [10:00 – 13:30] Domain 2 Review — Data Mining

**Visual:** Flowchart of the data mining process: collect → clean → transform → load.

**Alt-text:** A left-to-right process flow with boxes: Raw Data Sources → Data Extraction → Data Cleaning and Transformation → Data Loading → Analytical System.

**Audio:** "Domain 2 is the largest domain at 25% of the exam. It covers the full data preparation pipeline.

**Data collection** — know the difference between structured query (SQL), web scraping, API calls, and flat file imports. Know what a data catalog does and why metadata matters.

**Data cleaning** — null handling strategies (imputation vs. deletion), outlier detection (IQR, Z-score), deduplication, data type conversion, and standardization of formats (date formats, phone formats).

**Data transformation** — normalization, aggregation, parsing, data merging (joins), transposing, and deriving new columns.

**ETL vs. ELT** — Extract, Transform, Load versus Extract, Load, Transform. In ETL, transformation happens before loading into the target system. In ELT, raw data is loaded first and transformation happens inside the target — common in cloud data warehouses.

**Data quality dimensions** — completeness, consistency, accuracy, validity, uniqueness, and timeliness. These six dimensions appear on the exam frequently.

Exam tip: be able to match a described data problem to its quality dimension. Missing values are a completeness issue. Duplicate records are a uniqueness issue. A value of 200% in a percentage column is a validity issue."

---

### [13:30 – 17:00] Domain 3 Review — Data Analysis and Statistics

**Visual:** Summary table of statistical measures and when to use each.

**Alt-text:** A table with columns: Measure, Formula concept, When to use. Rows include mean, median, mode, standard deviation, variance, correlation coefficient, percentile.

**Audio:** "Domain 3 covers statistical analysis, analytical techniques, and the Python/tool skills from Modules 12 and 14.

**Descriptive statistics** — mean, median, mode, range, variance, standard deviation, percentile, and quartile. Know the difference between population statistics and sample statistics — sample uses n-1 in the denominator (Bessel's correction).

**Distributions** — normal distribution properties (mean equals median, 68-95-99.7 rule), right skew and left skew, and how skew affects the relationship between mean and median.

**Correlation and regression** — correlation coefficient range (-1 to 1), what 0 means, the difference between correlation and causation, and the purpose of simple linear regression.

**Hypothesis testing** — null hypothesis, alternative hypothesis, p-value interpretation (reject the null if p < significance level), Type I error (false positive), Type II error (false negative).

**Machine learning concepts** — supervised vs. unsupervised, classification vs. regression, overfitting vs. underfitting, train-test split purpose.

**Analysis types** — trend analysis, cohort analysis, root cause analysis, gap analysis, and what-if analysis. Know the purpose of each."

---

### [17:00 – 20:30] Domain 4 and Domain 5 Review

**Visual:** Side-by-side summary cards for Domain 4 and Domain 5.

**Alt-text:** Two cards. Domain 4 card lists chart types, dashboard principles, BI tools. Domain 5 card lists GDPR, CCPA, HIPAA, PII, data governance concepts.

**Audio:** "Domain 4 — Visualization — covers everything from Module 13. The highest-frequency topics are:

Chart type selection: line for trends, bar for comparisons, scatter for relationships, histogram for distributions, pie for small-count compositions, heatmap for correlations, choropleth for geographic data.

Dashboard design principles: single audience, limit KPIs, consistent color, remove chart junk, proximity and grouping.

Report types: operational reports (real-time, daily), analytical reports (ad-hoc exploration), executive summaries (strategic, minimal detail).

BI tools: Tableau (drag-and-drop, Tableau Public), Power BI (Microsoft ecosystem, DAX, Power Query), Looker (LookML central model definition).

Domain 5 — Governance — covers Module 15 content. The highest-frequency topics are:

GDPR: EU resident data, right to erasure, 4% global revenue penalty.
CCPA: California residents, right to opt-out of data sale.
HIPAA: Protected Health Information, Privacy Rule and Security Rule.
PII and quasi-identifiers.
Data anonymization techniques: masking, pseudonymization, aggregation, generalization, k-anonymity.
Algorithmic bias types: historical, measurement, sampling, proxy discrimination.
Data governance principles: minimization, purpose limitation, transparency, consent, accountability."

---

### [20:30 – 24:00] Exam Strategy and Capstone Overview

**Visual:** A prioritized study checklist and capstone project overview slide.

**Audio:** "For exam strategy, three rules:

One — read every question completely before looking at the answers. Data+ questions often hinge on one specific word: 'most appropriate,' 'first,' 'best.' Missing that word changes the correct answer.

Two — eliminate clearly wrong answers first. On a four-choice question, you can usually eliminate two answers immediately. That gives you 50/50 on the remaining two even if you are not sure.

Three — flag and move on. If a question is taking more than 90 seconds, mark it, move to the next question, and return at the end. Do not let one hard question cost you time on five easy ones.

For the capstone project, you will select a real or synthetic dataset, define a business question, clean the data, analyze it, visualize the findings, and present a one-page executive summary. The capstone combines every skill from this course: Python analysis, dashboard design thinking, statistical interpretation, and stakeholder communication.

This is the finish line. You have covered all five domains across 16 modules. The tools and the concepts are in your toolkit. Now execute. Good luck on the exam and on the capstone."

---

### Instructor Notes

* Review session before the exam works well as a live quiz using the 20 practice questions in the Module 16 quiz file
* Capstone presentations (5 minutes each) make an effective final class session
* CompTIA exam voucher discount codes are sometimes available through the CertMaster Learn platform — check with department

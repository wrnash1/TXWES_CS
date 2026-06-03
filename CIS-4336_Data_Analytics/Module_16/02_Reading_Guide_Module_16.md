# Reading Guide: Module 16 — Data+ DA0-001 Exam Preparation and Capstone

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Introduction

Welcome to **Module 16 — Data+ DA0-001 Exam Preparation and Capstone**. This reading guide is a comprehensive reference for all five Data+ exam domains. It synthesizes the key concepts from every prior module into a single, exam-focused document. Use this guide as your primary study reference in the days before the exam. Each section includes the most frequently tested concepts, definitions, and exam traps for its domain.

The CompTIA Data+ DA0-001 exam tests practical data analyst competencies. It is not a memorization exam — it is a scenario-based exam where you apply knowledge to realistic situations. Reading this guide builds the conceptual map you need to navigate those scenarios confidently.

---

### Exam Overview

| Feature | Detail |
|---|---|
| Exam code | DA0-001 |
| Total questions | Up to 90 |
| Time limit | 90 minutes |
| Passing score | 675 out of 900 |
| Question format | Multiple choice (single and multiple answer), performance-based |
| Exam cost | $338 USD (discounts available through CertMaster) |
| Validity | 3 years; renewable through continuing education or retake |

#### Domain Weights

| Domain | Title | Exam Weight |
|---|---|---|
| 1 | Data Concepts and Environments | 15% |
| 2 | Data Mining | 25% |
| 3 | Data Analysis and Statistics | 23% |
| 4 | Data Visualization and Reporting | 22% |
| 5 | Data Governance | 15% |

---

### Domain 1 Review — Data Concepts and Environments (15%)

#### Data Types

* **Quantitative (numeric)** — measurable values. Continuous (revenue, temperature) or discrete (headcount, order count).
* **Qualitative (categorical)** — non-numeric labels. Nominal (no order: region, color) or ordinal (ordered: satisfaction ratings, size tiers).
* **Structured** — organized in rows and columns; queryable with SQL. Examples: relational database tables, spreadsheets.
* **Semi-structured** — has some organizational properties but not a rigid schema. Examples: JSON, XML, CSV.
* **Unstructured** — no predefined format. Examples: email text, images, audio, video.

#### Data Sources

* **First-party data** — collected directly from your own customers or operations. Highest quality and accuracy.
* **Second-party data** — another organization's first-party data shared with you through a direct agreement.
* **Third-party data** — purchased from a data aggregator or broker; collected from unknown sources.

Exam trap: confusing first-party and third-party. If your company collects it from your own customers, it is first-party. If you buy it, it is third-party.

#### Database Concepts

* **OLTP (Online Transaction Processing)** — optimized for frequent, fast reads and writes of individual records. Examples: order entry systems, banking transactions.
* **OLAP (Online Analytical Processing)** — optimized for complex queries across large historical datasets. Examples: data warehouses, business intelligence systems.
* **Relational database** — data stored in tables with defined relationships; queried with SQL.
* **Non-relational (NoSQL) database** — flexible schema; stores documents, key-value pairs, graphs, or wide columns. Examples: MongoDB (document), Redis (key-value), Cassandra (wide column).
* **Normalization** — organizing a relational database to reduce redundancy. First, second, and third normal forms progressively eliminate update anomalies.
* **Primary key** — uniquely identifies each row in a table.
* **Foreign key** — a column in one table that references the primary key of another table; enforces referential integrity.

#### Data Warehousing

* **Star schema** — a fact table at the center connected to multiple dimension tables. Denormalized for fast analytical queries.
* **Snowflake schema** — dimension tables are normalized into sub-dimension tables. More storage-efficient but more complex to query.
* **Fact table** — contains measurable events (sales transactions, web clicks) with foreign keys to dimensions.
* **Dimension table** — describes the attributes of facts (date, customer, product, location).
* **ETL** — Extract, Transform, Load. Data is transformed before loading into the warehouse.
* **ELT** — Extract, Load, Transform. Raw data is loaded first; transformation occurs inside the warehouse. Common in cloud platforms.
* **Data mart** — a subset of a data warehouse focused on a single department or subject area.
* **Data lake** — stores raw data in any format at massive scale; schema-on-read rather than schema-on-write.

---

### Domain 2 Review — Data Mining (25%)

#### Data Collection Methods

* **SQL query** — retrieves structured data from relational databases.
* **API call** — retrieves data from a web service using HTTP requests; returns JSON or XML.
* **Web scraping** — programmatically extracts data from HTML web pages.
* **Flat file import** — reads CSV, TSV, Excel, or fixed-width files.
* **Data catalog** — a metadata inventory that documents available datasets, their schemas, owners, and quality attributes.

#### Data Cleaning Techniques

* **Null handling** — imputation (fill with mean, median, mode, or model prediction) versus deletion (drop rows or columns).
* **Outlier detection** — IQR method (1.5× IQR rule), Z-score method (flag values beyond 3 standard deviations).
* **Deduplication** — identifying and removing exact or near-duplicate records.
* **Standardization** — converting inconsistent formats to a common standard (date formats, phone number formats, unit conversions).
* **Data type conversion** — changing a column's data type (string to integer, string to datetime).

#### Data Quality Dimensions

* **Completeness** — are all required values present?
* **Consistency** — does the data agree across sources and time?
* **Accuracy** — does the data correctly represent the real-world entity?
* **Validity** — do values conform to the expected format, range, or set of allowed values?
* **Uniqueness** — are records deduplicated?
* **Timeliness** — is the data current enough for the intended use?

Exam tip: match described problems to their quality dimension. Missing fields → completeness. Contradictory values between systems → consistency. Values outside the valid range → validity.

#### Data Transformation

* **Aggregation** — summarizing data at a higher level (sum, count, average by group).
* **Parsing** — splitting a compound field into components (full name → first name, last name).
* **Merging / joining** — combining data from two sources on a shared key.
* **Transposing** — rotating rows to columns or columns to rows.
* **Deriving** — calculating new columns from existing ones (profit = revenue − cost).

---

### Domain 3 Review — Data Analysis and Statistics (23%)

#### Descriptive Statistics

* **Mean** — arithmetic average; sensitive to outliers.
* **Median** — middle value; resistant to outliers; preferred for skewed distributions.
* **Mode** — most frequent value; useful for categorical data.
* **Range** — max minus min; sensitive to outliers.
* **Variance** — average squared deviation from the mean.
* **Standard deviation** — square root of variance; in the same unit as the data.
* **Percentile** — the value below which a given percentage of observations fall.
* **Interquartile range (IQR)** — Q3 minus Q1; range of the middle 50%.

#### Distributions

* **Normal distribution** — symmetric bell curve; mean equals median equals mode; 68% of data within 1 standard deviation, 95% within 2, 99.7% within 3.
* **Right-skewed (positive skew)** — long tail to the right; mean greater than median.
* **Left-skewed (negative skew)** — long tail to the left; mean less than median.
* **Bimodal** — two distinct peaks in the distribution.

#### Correlation and Regression

* **Correlation coefficient (r)** — ranges from -1 to 1. Values near 1 indicate strong positive linear relationship. Values near -1 indicate strong negative. Values near 0 indicate no linear relationship.
* **Causation vs. correlation** — correlation never implies causation. A third variable (confound) may explain both.
* **Simple linear regression** — models the relationship between one independent variable (x) and one dependent variable (y) as a straight line: y = mx + b.
* **Multiple regression** — extends to multiple independent variables.
* **R² (coefficient of determination)** — proportion of variance in y explained by x(es). Range: 0 to 1.

#### Hypothesis Testing

* **Null hypothesis (H₀)** — assumes no effect or no difference.
* **Alternative hypothesis (H₁)** — asserts there is an effect or difference.
* **p-value** — probability of observing the result if H₀ is true. If p < significance level (commonly 0.05), reject H₀.
* **Type I error** — rejecting a true null hypothesis (false positive).
* **Type II error** — failing to reject a false null hypothesis (false negative).
* **Statistical significance** — p < 0.05 by convention, but this is a threshold, not a guarantee of practical importance.

#### Analysis Types

* **Trend analysis** — examines how a metric changes over time.
* **Cohort analysis** — compares groups defined by a shared characteristic or event (signup month, acquisition channel).
* **Root cause analysis** — investigates the underlying cause of an observed problem.
* **Gap analysis** — compares current state to desired state; identifies what must change.
* **What-if analysis (sensitivity analysis)** — models how outcomes change when input assumptions change.

#### Machine Learning Concepts

* **Supervised learning** — labeled training data; model predicts labels. Classification (category output) or regression (numeric output).
* **Unsupervised learning** — no labels; algorithm finds structure. Clustering (K-means), dimensionality reduction (PCA).
* **Overfitting** — model memorizes training data; poor test performance. Remedies: regularization, more data, simpler model.
* **Underfitting** — model too simple; poor performance on both training and test. Remedies: more complex model, more features.
* **Train/test split** — holds out data unseen during training to estimate real-world performance.
* **Feature engineering** — encoding, scaling, date decomposition, log transformation.

---

### Domain 4 Review — Data Visualization and Reporting (22%)

#### Chart Type Selection

* **Line chart** — trends over continuous time.
* **Bar / column chart** — comparing values across categories.
* **Pie / donut chart** — part-to-whole for five or fewer categories.
* **Scatter plot** — relationship between two numeric variables.
* **Histogram** — distribution of one numeric variable.
* **Box plot** — distribution and outlier visualization by group.
* **Heatmap** — correlation matrix or cross-tabulation.
* **Choropleth map** — geographic distribution by shading regions.
* **Stacked area chart** — composition change over time.
* **Bullet chart** — metric vs. target with qualitative ranges.

#### Dashboard Design Principles

* **Single audience, single purpose** — design for one role answering one question.
* **Limit KPI count** — five or fewer primary KPIs at the top.
* **Consistent color encoding** — one meaning per color across the whole dashboard.
* **Remove chart junk** — eliminate non-data-encoding visual elements.
* **Proximity and grouping** — related metrics together, whitespace as a separator.

#### KPI Concepts

* **Metric** — any quantitative measurement.
* **KPI** — a metric tied to a strategic objective with a target and direction.
* **Benchmark** — a reference value for evaluating metric performance.
* **Leading indicator** — predicts future performance.
* **Lagging indicator** — reflects past outcomes.
* **Vanity metric** — impressive-looking but not actionable.

#### BI Tools

* **Tableau** — drag-and-drop canvas; Tableau Public for free publishing; strong for ad-hoc exploration.
* **Power BI** — Microsoft ecosystem; Power Query for ETL; DAX for calculated measures.
* **Looker** — LookML central metric model; prevents inconsistent metric definitions across teams.

---

### Domain 5 Review — Data Governance (15%)

#### Privacy Regulations

* **GDPR** — EU; any org processing EU resident data; rights include access, erasure, portability, rectification; penalty up to 4% global revenue or €20M.
* **CCPA** — California; qualifying businesses; rights include know, delete, opt-out of sale, non-discrimination.
* **HIPAA** — US healthcare; covered entities and business associates; Privacy Rule and Security Rule; protects PHI.

#### PII and Identifiers

* **Direct identifiers** — SSN, full name, email, phone, biometrics.
* **Quasi-identifiers** — ZIP code, birth date, gender, ethnicity; can re-identify when combined.

#### Anonymization Techniques

* **Data masking** — replace with fictional data; irreversible; no mapping retained.
* **Pseudonymization** — replace with token; mapping retained; still personal data under GDPR.
* **Data generalization** — replace with ranges or categories.
* **Aggregation** — report group statistics instead of individual records.
* **k-anonymity** — each record indistinguishable from at least k-1 others on quasi-identifiers.
* **Data suppression** — remove rows or columns that cannot be protected.

#### Algorithmic Bias Types

* **Historical bias** — training data reflects past inequality.
* **Measurement bias** — outcome measured less accurately for some groups.
* **Sampling bias** — training data not representative of deployment population.
* **Proxy discrimination** — a non-protected variable correlates with a protected attribute and produces disparate impact.

#### Responsible Data Principles

* Data minimization, purpose limitation, transparency, consent, fairness, accountability, security.

---

### Exam Strategy

#### Time Management

At 90 questions in 90 minutes, the budget is 60 seconds per question. Move faster on topics you know well to bank time for harder questions. Flag uncertain questions and return at the end — never sit on one question for more than 90 seconds.

#### Answer Selection Technique

* Read the full question stem before looking at answers
* Identify the key qualifier: "most appropriate," "first step," "primary reason"
* Eliminate options that are clearly wrong
* Of the remaining options, choose the one that is most complete and most directly answers the qualifier

#### Common Exam Traps

* OLTP vs. OLAP — OLTP is for transactions, OLAP is for analysis
* ETL vs. ELT — transform before load vs. load then transform
* Correlation vs. causation — never conflate them
* First-party vs. third-party data — collected by you vs. purchased
* Mean vs. median for skewed data — median is more robust
* Overfitting vs. underfitting — large train-test gap vs. both low

---

### Key Terms — Master List

All key terms from Modules 1–15 are tested on the exam. The most frequently tested are:

* **data warehouse, data lake, data mart** — storage architecture distinctions
* **ETL, ELT** — transformation timing
* **star schema, snowflake schema** — warehouse modeling patterns
* **OLTP, OLAP** — processing paradigms
* **KPI, metric, benchmark** — measurement vocabulary
* **PII, PHI, quasi-identifier** — privacy data types
* **GDPR, CCPA, HIPAA** — regulatory frameworks
* **supervised, unsupervised, classification, regression, clustering** — ML taxonomy
* **overfitting, underfitting, train-test split** — ML evaluation
* **normal distribution, skewness, correlation coefficient** — statistics
* **Type I error, Type II error, p-value** — hypothesis testing
* **data masking, pseudonymization, k-anonymity** — anonymization
* **data minimization, purpose limitation** — governance principles

---

### OER Resources

* **CompTIA Data+ exam objectives (free PDF)** — [comptia.org/certifications/data](https://www.comptia.org/certifications/data)
* **Professor Messer CompTIA study notes** — [professormesser.com](https://www.professormesser.com/)
* **freeCodeCamp Data Analysis with Python** — [freecodecamp.org/learn](https://www.freecodecamp.org/learn/data-analysis-with-python/)
* **Khan Academy Statistics and Probability** — [khanacademy.org/math/statistics-probability](https://www.khanacademy.org/math/statistics-probability)
* **IAPP Privacy Fundamentals** — [iapp.org/resources](https://iapp.org/resources/)

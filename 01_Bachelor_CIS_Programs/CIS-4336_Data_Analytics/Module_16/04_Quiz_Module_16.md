# Quiz: Module 16 — Data+ DA0-001 Exam Preparation and Capstone

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

**Instructions:** This quiz contains 20 practice questions spanning all five Data+ exam domains. Select the single best answer for each question. Each question is worth 5 points.

---

### Question 1 — Domain 1

A company stores customer purchase history in a relational database optimized for fast inserts and updates with thousands of transactions per second. It also maintains a separate system storing years of historical aggregated data used exclusively for quarterly trend analysis. Which terms correctly describe these two systems?

A) The transaction system is OLAP; the historical system is OLTP.

B) The transaction system is OLTP; the historical system is OLAP.

C) Both systems are OLTP because they both store structured relational data.

D) The transaction system is a data lake; the historical system is a data mart.

#### Q1 Correct Answer: B

#### Q1 Distractor Analysis

OLTP handles frequent fast individual transactions. OLAP handles complex queries over large historical datasets. A reverses the definitions. C is incorrect because the two systems serve fundamentally different processing purposes. D is incorrect; neither description matches a data lake or data mart.

---

### Question 2 — Domain 1

A company receives a dataset from a social media data aggregator that collected behavior patterns from millions of users across multiple platforms and sold the compiled dataset. What type of data source is this?

A) First-party data — the company collected it directly from its own customers.

B) Second-party data — another organization's first-party data shared through a direct partnership.

C) Third-party data — purchased from a vendor that aggregated data from multiple external sources.

D) Primary data — collected through original research methods such as surveys or experiments.

#### Q2 Correct Answer: C

#### Q2 Distractor Analysis

A applies only when the company collects data directly from its own customers. B describes a direct sharing agreement with one partner, not an aggregator. D is a research methodology term, not a BI data sourcing classification.

---

### Question 3 — Domain 1

A data warehouse uses a fact table at the center connected directly to six denormalized dimension tables. What schema pattern is this?

A) Snowflake schema — dimension tables are normalized into sub-dimension tables.

B) Star schema — a fact table at the center with denormalized dimension tables radiating outward.

C) Third normal form — the most highly normalized relational database design.

D) Entity-relationship model — a conceptual design tool, not a warehouse pattern.

#### Q3 Correct Answer: B

#### Q3 Distractor Analysis

A describes snowflake schema where dimensions are broken into sub-tables. The scenario states dimensions are denormalized, ruling out snowflake. C is a normalization level for OLTP systems, not a warehouse pattern. D is a design notation, not a schema type.

---

### Question 4 — Domain 2

An analyst discovers 18% of rows in the `annual_salary` column contain null values. The column is right-skewed due to a small number of high executive salaries. Which imputation strategy is most appropriate?

A) Fill nulls with the column mean — the mean is inflated by outliers and overestimates typical salaries.

B) Fill nulls with the column median — the median is resistant to outliers and better represents typical salary in a skewed distribution.

C) Drop all rows with null salary — removing 18% creates substantial sample size reduction and potential selection bias.

D) Fill nulls with zero — implies the employee has no salary, which is factually incorrect.

#### Q4 Correct Answer: B

#### Q4 Distractor Analysis

A uses the mean, which is pulled upward by high earners in right-skewed data. C discards 18% of data unnecessarily. D creates analytically harmful false values by substituting zero for an unknown salary.

---

### Question 5 — Domain 2

An analyst finds the same customer appearing three times with identical name and email but slightly different phone number formats. Which data quality dimension is violated and what is the correct remediation?

A) Accuracy violation; fix by verifying each phone number against the source system.

B) Completeness violation; fix by filling the missing phone digits.

C) Uniqueness violation; fix by deduplicating the records, retaining the most recent or most complete version.

D) Validity violation; fix by standardizing the phone number format to a single pattern.

#### Q5 Correct Answer: C

#### Q5 Distractor Analysis

A applies if values are factually wrong, not if records are duplicated. B applies when values are missing, not when records are duplicated. D addresses format inconsistency as a secondary issue — the primary problem is the duplicate customer record itself.

---

### Question 6 — Domain 2

A data pipeline extracts data from a source system, loads it in raw form into a cloud data warehouse, and then applies transformations using SQL inside the warehouse. Which pipeline pattern does this describe?

A) ETL — Extract, Transform, Load; transformation occurs before loading.

B) ELT — Extract, Load, Transform; raw data is loaded first and transformation happens inside the target system.

C) CDC — Change Data Capture; tracks row-level changes from a source database in real time.

D) Batch ingestion — data collected over a period and loaded at scheduled intervals.

#### Q6 Correct Answer: B

#### Q6 Distractor Analysis

A describes transformation before loading — the scenario states loading happens before transformation. C is a replication technique, not a transformation architecture. D is a scheduling concept, not a transformation architecture.

---

### Question 7 — Domain 3

A dataset of 500 employee salaries has a mean of $87,400 and a median of $62,000. Which conclusion about the distribution is most likely correct?

A) The distribution is approximately normal because the mean and median are within 30% of each other.

B) The distribution is left-skewed because the mean is greater than the median.

C) The distribution is right-skewed because the mean is greater than the median, indicating high-earning outliers pulling the mean upward.

D) The distribution is bimodal because the mean and median differ significantly.

#### Q7 Correct Answer: C

#### Q7 Distractor Analysis

A is incorrect — in a normal distribution mean and median are nearly equal; a $25,000 gap is substantial. B reverses the rule: left skew has mean less than median. D describes two peaks, which is unrelated to the mean-median relationship.

---

### Question 8 — Domain 3

A researcher finds a correlation coefficient of 0.03 between the number of letters in a person's last name and their annual income. What is the correct interpretation?

A) There is a strong positive relationship between name length and income.

B) There is virtually no linear relationship between name length and income.

C) Longer last names cause higher income.

D) The result is statistically significant because the coefficient is positive.

#### Q8 Correct Answer: B

#### Q8 Distractor Analysis

A is incorrect — 0.03 is essentially zero on the -1 to 1 scale. C conflates correlation with causation. D is incorrect — a coefficient near zero indicates no relationship; a positive sign does not imply significance.

---

### Question 9 — Domain 3

A clinical trial tests whether a new drug reduces blood pressure. The null hypothesis states the drug has no effect. The trial produces a p-value of 0.03 against a significance level of 0.05. What is the correct conclusion?

A) Accept the null hypothesis — the drug has no effect because p is greater than zero.

B) Reject the null hypothesis — p < 0.05 means the observed result is unlikely if H₀ is true.

C) The result is inconclusive — more data is required before any conclusion can be drawn.

D) The drug is proven to reduce blood pressure with 97% certainty.

#### Q9 Correct Answer: B

#### Q9 Distractor Analysis

A misapplies the rule — we reject H₀ when p < alpha (0.05). C is incorrect; p < 0.05 is sufficient to reject H₀. D misinterprets p-value as a certainty percentage about the drug's effectiveness.

---

### Question 10 — Domain 3

A machine learning model achieves 94% accuracy on training data and 91% on test data. Which statement best describes this model?

A) The model is severely overfit — a 3-point gap indicates memorization of training data.

B) The model is underfit — both accuracy values are below 95%.

C) The model generalizes well — the small gap between training and test accuracy indicates the model is not memorizing noise.

D) The model has data leakage — 91% test accuracy is a sign of contaminated test data.

#### Q10 Correct Answer: C

#### Q10 Distractor Analysis

A is incorrect — a 3-point gap is modest, not a severe overfitting signature. B is incorrect; underfitting produces low accuracy on both sets, not high accuracy on both. D is incorrect; 91% is not perfect and the scenario shows no evidence of leakage.

---

### Question 11 — Domain 4

An analyst wants to compare the distribution of customer order values across four geographic regions to identify variance and outliers. Which chart type is most appropriate?

A) Pie chart — shows part-to-whole proportions; does not display distribution or variance.

B) Line chart — shows trends over time; not suited for cross-category distribution comparison.

C) Box plot — displays median, IQR, and outliers for each category simultaneously; ideal for cross-region distribution comparison.

D) Scatter plot — shows the relationship between two numeric variables; does not summarize within-group distributions.

#### Q11 Correct Answer: C

#### Q11 Distractor Analysis

A is for proportional composition. B is for time-series trends. D requires two continuous variables and does not show within-group distribution summaries.

---

### Question 12 — Domain 4

A dashboard uses red for "revenue below target" and also uses red for the "Electronics" product category label in a separate chart on the same page. Which design principle is violated?

A) Single audience, single purpose — the dashboard serves too many business functions.

B) Limit KPI count — too many metrics are displayed simultaneously.

C) Consistent color encoding — the same color carries two different meanings within the same dashboard.

D) Remove chart junk — unnecessary visual elements distract from the data.

#### Q12 Correct Answer: C

#### Q12 Distractor Analysis

A is about scope, not color. B is about metric count, not color usage. D is about decorative elements, not contradictory color semantics.

---

### Question 13 — Domain 4

Which statement most accurately describes how Looker's LookML architecture differs from Tableau and Power BI?

A) LookML allows Looker to store raw data inside the BI platform, eliminating the need for a separate database.

B) LookML is a drag-and-drop interface making Looker easier to use than Tableau for non-technical analysts.

C) LookML defines all metrics and data relationships centrally in a versioned repository, ensuring every analyst uses the same metric definitions.

D) LookML automatically generates machine learning models from structured data without any configuration.

#### Q13 Correct Answer: C

#### Q13 Distractor Analysis

A is incorrect — Looker queries external databases and does not store data. B is incorrect; LookML is a code-based modeling language, not a drag-and-drop interface. D is incorrect; LookML defines data models for BI queries, not ML pipelines.

---

### Question 14 — Domain 4

A sales analyst is presenting to the board of directors. Using the data storytelling framework, what is the correct order of the four narrative elements?

A) Evidence then Finding then Context then Implication

B) Finding then Implication then Context then Evidence

C) Context then Finding then Evidence then Implication

D) Implication then Context then Evidence then Finding

#### Q14 Correct Answer: C

#### Q14 Distractor Analysis

A leads with evidence before the audience knows what to look for. B skips context, leaving the audience without background to evaluate the finding. D presents the conclusion before establishing the situation. C follows the logical flow: background, then result, then proof, then action.

---

### Question 15 — Domain 5

A company based in Miami processes personal data of EU residents through its website and receives a written deletion request from a French resident. Under which regulation does this right exist?

A) CCPA — 45-day response window for California residents.

B) HIPAA — covers protected health information, not general website data.

C) GDPR — the right to erasure; response required within one month, extendable to three months for complex requests.

D) FERPA — governs student educational records; not applicable.

#### Q15 Correct Answer: C

#### Q15 Distractor Analysis

A covers California residents, not EU residents. B covers health data, not general website personal data. D governs student records and is entirely inapplicable.

---

### Question 16 — Domain 5

A health insurer shares patient claims data with a third-party analytics vendor to build a fraud detection model. Under HIPAA, what term describes the analytics vendor?

A) Covered entity — organizations directly providing health services or insurance.

B) Business associate — any organization that handles PHI on behalf of a covered entity.

C) Data broker — a company that collects and sells data from multiple sources.

D) Data controller — the GDPR term for the organization that determines the purpose of data processing.

#### Q16 Correct Answer: B

#### Q16 Distractor Analysis

A applies to healthcare providers and health plans, not vendors. C is an informal market term, not a HIPAA designation. D is GDPR terminology; HIPAA uses covered entity and business associate.

---

### Question 17 — Domain 5

An analyst removes patient names and account numbers from a medical dataset but retains exact birth date, 5-digit ZIP code, and gender. A privacy officer flags ongoing re-identification risk. What concept explains this concern?

A) Data masking — the values have been irreversibly replaced with fictional data.

B) Quasi-identifiers — individually non-identifying fields that can uniquely identify individuals when combined; birth date, ZIP, and gender together identify 87% of US individuals.

C) k-anonymity — the dataset does not meet the minimum group size requirement.

D) Pseudonymization — the dataset retains a mapping table allowing re-identification.

#### Q17 Correct Answer: B

#### Q17 Distractor Analysis

A is incorrect; masking would have replaced or removed the remaining fields. C refers to a specific anonymization property, not the general mechanism. D describes retaining a mapping table; the scenario describes removing direct identifiers without addressing indirect ones.

---

### Question 18 — Domain 5

A hiring algorithm trained on five years of historical promotion data recommends male candidates at twice the rate of equally qualified female candidates. The algorithm does not include gender as a feature. Which type of algorithmic bias best explains this disparity?

A) Measurement bias — performance ratings are measured differently for men and women.

B) Historical bias — the training data reflects historical promotion patterns that favored men; the model learned to replicate those patterns.

C) Sampling bias — the training dataset does not include enough records from each gender.

D) Label bias — the promotion decisions used as training labels were randomly assigned.

#### Q18 Correct Answer: B

#### Q18 Distractor Analysis

A may contribute but does not describe the primary mechanism. C addresses sample representation, not learning from biased historical outcomes. D is incorrect — labels were real historical decisions, not random.

---

### Question 19 — Domain 5

Which data governance principle prohibits using customer location data collected for delivery logistics to build a behavioral advertising profile without obtaining new consent?

A) Data minimization — collect only what is necessary.

B) Purpose limitation — data collected for one stated purpose must not be repurposed without new consent.

C) Accuracy — data must be kept correct and up to date.

D) Security — data must be protected with appropriate technical controls.

#### Q19 Correct Answer: B

#### Q19 Distractor Analysis

A governs the quantity collected, not subsequent use. C is about correctness, not permissible use. D is about protection from unauthorized access, not the permissibility of a new use case.

---

### Question 20 — All Domains

A data analyst is asked to produce a report for a logistics operations center showing current shipment delays, real-time driver locations, and packages overdue by more than four hours. Which combination of design decisions is most appropriate?

A) Monthly update; three high-level KPI tiles; a trend chart; distributed as PDF to senior leadership.

B) Real-time or hourly update; operational detail with drill-down by route and driver; alert indicators for overdue packages; displayed on a wall-mounted monitor.

C) Daily update; a correlation heatmap of all 20 operational variables; distributed by weekly email digest.

D) Quarterly update; executive summary format with five KPIs and a year-over-year comparison chart.

#### Q20 Correct Answer: B

#### Q20 Distractor Analysis

A describes an executive-level quarterly format, completely mismatched to a real-time operational audience. C uses the wrong chart type and wrong frequency for operational monitoring. D is a strategic board-level format; the scenario explicitly describes real-time operational needs.

---

### Answer Key

| Question | Domain | Correct Answer |
|---|---|---|
| 1 | Domain 1 | B |
| 2 | Domain 1 | C |
| 3 | Domain 1 | B |
| 4 | Domain 2 | B |
| 5 | Domain 2 | C |
| 6 | Domain 2 | B |
| 7 | Domain 3 | C |
| 8 | Domain 3 | B |
| 9 | Domain 3 | B |
| 10 | Domain 3 | C |
| 11 | Domain 4 | C |
| 12 | Domain 4 | C |
| 13 | Domain 4 | C |
| 14 | Domain 4 | C |
| 15 | Domain 5 | C |
| 16 | Domain 5 | B |
| 17 | Domain 5 | B |
| 18 | Domain 5 | B |
| 19 | Domain 5 | B |
| 20 | All Domains | B |

---

### Score Interpretation

| Score | Percentage | Interpretation |
|---|---|---|
| 18–20 | 90–100% | Excellent — ready to schedule your exam |
| 15–17 | 75–89% | Good — review the domains where you missed questions |
| 12–14 | 60–74% | Near passing threshold — targeted domain review recommended |
| Below 12 | Below 60% | Additional study required — revisit reading guides for missed domains |

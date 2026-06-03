# Quiz: Module 10 — Data Quality and Governance

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 20 (2 points each)

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 5: Data Governance, Quality, and Controls

---

## Instructions

Select the single best answer for each question. Each question is worth 2 points. No partial credit.

---

## Question 1

A customer database contains a record showing a customer's city as "Austin" but the customer actually lives in San Antonio. Which data quality dimension is violated?

A. Completeness

B. Timeliness

C. Accuracy

D. Uniqueness

**Correct Answer:** C — Accuracy is violated because the data value does not correctly reflect the real-world entity (the customer's actual city). Completeness concerns missing values (A). Timeliness concerns data currency (B). Uniqueness concerns duplicate records (D).

---

## Question 2

A hospital patient records system shows that 22% of patient records have a null value in the date_of_birth field. Which data quality dimension does this represent?

A. Validity

B. Completeness

C. Consistency

D. Timeliness

**Correct Answer:** B — Completeness measures whether all required values are present. A 22% null rate in a required field is a completeness problem. Validity concerns whether present values conform to rules (A). Consistency concerns disagreement across systems (C). Timeliness concerns data currency (D).

---

## Question 3

An order management system stores customer addresses as "123 Main St" while the CRM stores the same address as "123 Main Street." Which data quality dimension is violated?

A. Accuracy

B. Uniqueness

C. Validity

D. Consistency

**Correct Answer:** D — Consistency is violated because the same entity is represented differently across two systems. Both values may be factually correct (so accuracy is not violated). No duplicate records are involved (B). The format difference alone does not constitute a validity violation (C).

---

## Question 4

Which of the following best describes the role of a data steward?

A. An executive who has ultimate accountability for a data domain and makes strategic decisions about data use

B. An IT professional who manages database infrastructure, backups, and security implementations

C. A person responsible for day-to-day data quality monitoring, standard definition, and issue resolution for a data domain

D. A business analyst who consumes data to build reports and is responsible for following governance policies

**Correct Answer:** C — A data steward handles operational data quality management: defining standards, monitoring metrics, and resolving issues. Option A describes a data owner. Option B describes a data custodian (DBA). Option D describes a data consumer.

---

## Question 5

A product database contains three records for the same supplier — "Acme Corp," "ACME Corporation," and "Acme Corp, Inc." — each in a different source system. What solution is specifically designed to resolve this type of problem by creating a single authoritative record?

A. Data catalog

B. Data lineage tracking

C. Master Data Management

D. Data lake ingestion

**Correct Answer:** C — Master Data Management (MDM) creates a golden record — a single authoritative representation of each business entity — and resolves conflicting representations across source systems. A data catalog helps discover and describe data but does not merge records (A). Lineage tracks data origin but does not deduplicate (B). Data lake ingestion stores raw data without deduplication (D).

---

## Question 6

A date field in a customer database contains the value "February 30, 2024." Which data quality dimension is violated?

A. Timeliness

B. Completeness

C. Accuracy

D. Validity

**Correct Answer:** D — Validity is violated because "February 30" does not exist — the value fails a basic business rule (valid calendar dates). Timeliness concerns how current data is (A). Completeness concerns nulls (B). Accuracy concerns whether a value correctly represents reality, but "February 30" is not a real date — it cannot even be assessed for accuracy because it is structurally invalid (D is the more precise answer than C).

---

## Question 7

Contact data for a customer was last updated 5 years ago. A marketing team uses this data for a personalized email campaign and experiences a 40% bounce rate. Which data quality dimension caused this problem?

A. Accuracy

B. Uniqueness

C. Timeliness

D. Validity

**Correct Answer:** C — Timeliness is violated because the contact data is not sufficiently current for its intended use (an active marketing campaign). The addresses and emails may have been accurate 5 years ago but are now outdated. Accuracy (A) refers to correctness at a point in time. Uniqueness (B) refers to duplicate records. Validity (D) refers to rule conformance.

---

## Question 8

What is the primary purpose of a data catalog in an organization?

A. To replace the data warehouse with a schema-on-read architecture

B. To enable analysts to discover, understand, evaluate, and trust data assets through metadata management

C. To enforce row-level security so that analysts only see data relevant to their role

D. To store raw data from all source systems in a single centralized location

**Correct Answer:** B — A data catalog is a metadata management tool that helps users find data, understand its meaning and quality, and evaluate whether it is appropriate for their use case. It does not replace the warehouse (A), enforce access security (C), or serve as a raw data store (D).

---

## Question 9

In the DAMA framework, which knowledge area sits at the center of the DMBOK wheel because it provides the enabling policies and accountability structures for all other areas?

A. Data Quality

B. Metadata Management

C. Data Security

D. Data Governance

**Correct Answer:** D — Data Governance is at the center of the DAMA DMBOK wheel. It provides the organizational structures, policies, and accountabilities that enable all other 10 knowledge areas to function effectively. Data Quality (A), Metadata Management (B), and Data Security (C) are all important knowledge areas but are positioned around the wheel, not at its center.

---

## Question 10

A data analyst discovers that a sales report shows 18,400 active customers while the billing system shows 14,200. Both figures claim to represent the same metric. Which governance mechanism is most directly designed to prevent this discrepancy?

A. Data lineage tracking

B. Row-level security

C. Certified datasets and MDM-based golden records

D. Batch processing with nightly reconciliation

**Correct Answer:** C — Certified datasets (official endorsed versions of metrics) and MDM golden records (single authoritative entity representations) directly prevent conflicting metric definitions by establishing organizational agreement on what "active customer" means and which system is authoritative. Lineage helps investigate after the fact (A). Row-level security controls access, not definitions (B). Batch reconciliation may aggregate but does not resolve definitional conflicts (D).

---

End of Module 10 Quiz

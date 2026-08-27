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

## Question 11 (5 points)

A bank's loan application dataset has 150,000 records. A data quality check reveals 4,500 records where the same applicant appears twice with identical names and Social Security numbers but different loan amounts. Which data quality dimension is most directly violated?

A. Accuracy

B. Consistency

C. Uniqueness

D. Validity

**Correct Answer:** C — Uniqueness is violated because the same real-world entity (the applicant) appears as duplicate records. Accuracy concerns whether values correctly represent reality (A). Consistency concerns disagreement across systems (B). Validity concerns whether values conform to defined rules (D).

---

## Question 12 (5 points)

An organization implements a policy that data quality metrics must be measured and reported to the data governance council every month. What governance role is typically responsible for executing these measurements and delivering the reports?

A. Chief Data Officer (CDO)

B. Data Owner

C. Data Steward

D. Data Consumer

**Correct Answer:** C — The data steward performs day-to-day operational quality monitoring, executes data quality checks, and reports metrics to governance bodies. The CDO sets strategy (A). The data owner has accountability for a data domain but typically delegates operational tasks (B). The data consumer uses data but is not responsible for governance reporting (D).

---

## Question 13 (5 points)

A company discovers that its product catalog has items with negative prices (e.g., price = -$25.00). No product should have a negative price under any business rule. Which data quality dimension best classifies this issue?

A. Completeness

B. Timeliness

C. Accuracy

D. Validity

**Correct Answer:** D — Validity is violated because the value (-$25.00) breaks a defined business rule (prices must be non-negative). The value is present (completeness is not the issue), and whether it is "accurate" is moot since a negative price has no real-world referent — it simply violates the rule. Timeliness concerns data currency (B).

---

## Question 14 (5 points)

What does data lineage documentation specifically track?

A. The business definitions and ownership of each data element in the enterprise

B. The origin of data and every transformation, movement, and system it passed through from source to final destination

C. The frequency and severity of data quality violations in a production dataset

D. The access control policies that determine who can view or modify each data asset

**Correct Answer:** B — Data lineage tracks the complete life of a data element: where it came from, how it was transformed, and where it ended up. This is critical for debugging data quality issues and understanding the impact of source system changes. Business definitions are managed in the data dictionary or catalog (A). Quality violation tracking is a data quality scorecard function (C). Access policies are part of data security governance (D).

---

## Question 15 (5 points)

An e-commerce company defines "active customer" as a customer who placed an order in the last 90 days. The sales team defines it as any customer with a non-cancelled account. A report shows different active customer counts depending on which team runs it. What governance artifact would most directly resolve this disagreement?

A. A data catalog with lineage visualization

B. A master data management (MDM) golden record

C. A business glossary with formally approved metric definitions

D. A row-level security policy applied to the customer table

**Correct Answer:** C — A business glossary provides formally agreed-upon definitions for key business terms and metrics. Without a single approved definition of "active customer," different teams will produce different numbers. A data catalog helps discover data but does not resolve definition conflicts (A). MDM creates golden records for entities, not metric definitions (B). Row-level security controls access, not definitions (D).

---

## Question 16 (5 points)

A retailer runs a data quality check and finds that 3% of records in the `email_address` field contain values without the "@" symbol. Which remediation action is most appropriate as a first step?

A. Delete all records with invalid email addresses

B. Flag invalid records with a data quality indicator column and route them to a data steward review queue

C. Replace all invalid email addresses with NULL

D. Archive the affected records in a separate table and exclude them from all reports permanently

**Correct Answer:** B — Best practice is to flag invalid records and route them for review rather than immediately deleting or nullifying data that may be recoverable. Deleting records (A) destroys potentially valuable information. Replacing with NULL (C) loses the original value and may cause its own completeness issues. Permanent exclusion (D) is premature before root cause analysis.

---

## Question 17 (5 points)

Which statement correctly describes the difference between a data dictionary and a data catalog?

A. A data dictionary is an enterprise search platform with business context, lineage, and quality scores; a data catalog is a simple column-level reference document

B. A data dictionary defines column names, data types, and constraints for a specific system; a data catalog is a broader enterprise platform enabling data discovery, lineage, and business context across multiple systems

C. A data dictionary and data catalog are identical tools with different names used by different industries

D. A data catalog is used only in data lakes; a data dictionary is used only in relational databases

**Correct Answer:** B — A data dictionary is system-specific: it documents the technical metadata (column names, types, constraints) for a particular database or application. A data catalog is enterprise-wide: it aggregates metadata from many systems, adds business context, lineage, ownership, and quality scores, and enables self-service data discovery. Options A reverses the definitions. C and D are incorrect.

---

## Question 18 (5 points)

A data governance committee wants to assign formal accountability for the quality and proper use of all customer data across the enterprise. Which role should hold this accountability?

A. Database Administrator (DBA)

B. Data Steward

C. Data Owner

D. Business Analyst

**Correct Answer:** C — The data owner holds formal business accountability for a data domain — including quality, compliance, and appropriate use decisions. The DBA manages physical database infrastructure (A). The data steward executes day-to-day quality management under the owner's authority (B). Business analysts consume data but are not accountable for it (D).

---

## Question 19 (5 points)

An analyst running a report for a marketing campaign discovers that customer phone numbers in the CRM are formatted as "(512) 555-1234" while the same numbers in the billing system are stored as "5125551234". Both values are correct. Which data quality dimension is this an example of?

A. Accuracy

B. Validity

C. Consistency

D. Uniqueness

**Correct Answer:** C — Consistency is violated because the same data is represented in different formats across systems, even though both are factually correct. The inconsistency creates integration and matching challenges. Accuracy concerns factual correctness (A). Validity concerns rule conformance — both formats may be considered valid in their respective systems (B). Uniqueness concerns duplicate records (D).

---

## Question 20 (5 points)

What is the primary purpose of a data quality scorecard in a governance program?

A. To replace the data catalog by providing a single view of all metadata

B. To assign letter grades to individual data analysts based on their data entry accuracy

C. To provide a standardized, repeatable summary of data quality metrics across dimensions so that quality trends can be tracked and remediation prioritized

D. To enforce data retention policies by automatically deleting records that fail quality checks

**Correct Answer:** C — A data quality scorecard aggregates quality metrics across dimensions (completeness, validity, accuracy, etc.) into a repeatable report that lets governance teams track trends and prioritize remediation efforts. It does not replace the catalog (A), grade employees (B), or enforce retention by deleting records (D).

---

End of Module 10 Quiz

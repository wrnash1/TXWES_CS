# Reading Guide: Module 10 — Data Quality and Governance

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4336 &BULL; DATA ANALYTICS & BUSINESS INTELLIGENCE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 5: Data Governance, Quality, and Controls

---

## Overview

This guide covers data quality dimensions, governance frameworks, master data management, and data catalogs. Domain 5 of the CompTIA Data+ exam accounts for approximately 17% of questions. The exam presents scenarios requiring you to identify data quality violations by dimension, select the appropriate governance role, and distinguish MDM approaches.

---

## Section 1: Data Quality — Definition and Importance

Data quality is the degree to which data is **fit for its intended use**. Quality is always context-dependent: the same data may be sufficient for one purpose and insufficient for another.

Poor data quality consequences:

- Inaccurate analytics leading to bad business decisions
- Failed model training (garbage in, garbage out)
- Regulatory compliance failures and fines
- Customer dissatisfaction from incorrect communications
- Wasted operational effort (duplicate mailings, incorrect billing)

Data quality costs organizations an estimated $12.9 million annually on average (Gartner).

---

## Section 2: The Six Dimensions of Data Quality

### Accuracy

**Definition:** Data correctly reflects the real-world entity or event it represents.

**Violation example:** A product record shows a weight of 2.5 lbs but the actual product weighs 5.5 lbs.

**Assessment method:** Compare records to authoritative external sources (address verification APIs, regulatory databases, physical measurements).

**Business impact:** Inaccurate customer data results in returned mail, failed deliveries, incorrect credit checks.

### Completeness

**Definition:** All required data values are present — no required fields are null or missing.

**Violation example:** 23% of customer records are missing a date of birth, making age-based segmentation impossible for those records.

`completeness_pct = (non_null_count / total_count) * 100`

**Assessment method:** Count null values in required fields; compare to completeness thresholds.

**Note:** Completeness and accuracy are independent dimensions. A complete record can be inaccurate; an accurate record can be incomplete.

### Consistency

**Definition:** Data values representing the same entity agree across different systems, tables, or time periods.

**Violation example:** The CRM stores a customer address as "123 Main St" while the billing system stores "123 Main Street." Both may be correct but they are inconsistent — record-matching queries fail.

**Assessment method:** Cross-system record linkage and comparison; standardization checks.

**Common cause:** System integrations where no canonical format was enforced at load time.

### Timeliness

**Definition:** Data is available when needed and sufficiently current for its intended use.

**Violation example:** Customer contact data last updated 4 years ago is stale for a direct mail campaign; many addresses and phone numbers will be outdated.

**Assessment method:** Calculate data age; compare to acceptable freshness thresholds for each use case.

**Context dependency:** A monthly report can tolerate 30-day-old data. A fraud detection system cannot tolerate data more than a few seconds old.

### Validity

**Definition:** Data conforms to defined business rules, acceptable value ranges, and format constraints.

**Violation examples:**

- Date field contains "February 30, 2024" (impossible date)
- Email field contains "john_at_email.com" (missing @ symbol)
- Age field contains -5 (impossible value)
- ZIP code field contains letters instead of digits

**Assessment method:** Range checks, format validation (regex), referential integrity checks, business rule validation.

### Uniqueness

**Definition:** Each real-world entity is represented exactly once in a dataset — no duplicates.

**Violation example:** A customer database contains 4 records for "Maria Garcia" at the same address — created during different customer service interactions over five years.

**Assessment method:** Deduplication analysis; count records sharing the same identifier, name, email, or other unique attributes.

**Business impact:** Duplicate records inflate counts, split customer history, cause duplicate mailings, and undermine analytics reliability.

---

## Section 3: Data Quality Dimension Comparison Table

| Dimension | Question It Answers | Common Violation | Detection Method |
|-----------|--------------------|--------------------|-----------------|
| Accuracy | Is the value correct? | Wrong city in address | Compare to authoritative source |
| Completeness | Are all values present? | NULL in required field | Count NULLs per column |
| Consistency | Do values agree across systems? | Different formats in CRM vs. ERP | Cross-system comparison |
| Timeliness | Is the data current enough? | 4-year-old contact data | Calculate data age |
| Validity | Does the value follow the rules? | Impossible date or invalid format | Range and format checks |
| Uniqueness | Is each entity represented once? | Duplicate customer records | Deduplication analysis |

---

## Section 4: Data Governance Roles

Data governance defines the organizational structures, policies, and responsibilities for managing data as an asset.

### Key Roles

**Data Owner:**

- Typically an executive or senior business leader
- Has ultimate accountability for a data domain (e.g., VP of Sales owns customer data)
- Makes strategic decisions about data use, access, and retention
- Approves policies and resolves escalated issues

**Data Steward:**

- Operational role responsible for day-to-day data quality management
- Defines and documents data standards and business definitions
- Monitors quality metrics and investigates violations
- Coordinates with IT and business units on data issues
- Not necessarily a technical role — may be a business analyst with domain expertise

**Data Custodian (IT/DBA):**

- Responsible for the technical infrastructure that stores and processes data
- Implements the access controls and security policies defined by the owner/steward
- Not responsible for the business meaning or quality of the data itself

**Data Consumer:**

- Analysts, report developers, and business users who use data
- Responsible for using data within defined governance policies
- Should report quality issues to the relevant data steward

### RACI Matrix

| Activity | Data Owner | Data Steward | IT/Custodian | Consumer |
|----------|-----------|-------------|-------------|---------|
| Define data standards | A | R | C | I |
| Monitor data quality | I | R/A | C | I |
| Resolve data issues | A | R | C | I |
| Implement security controls | A | C | R | I |
| Report quality issues | I | A | I | R |

R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## Section 5: Master Data Management

### What Is Master Data?

Master data is the core business data shared and referenced across multiple systems. It represents the key entities of the business — things like customers, products, employees, locations, and suppliers.

Examples:

- **Customer master:** Name, address, contact info, account number
- **Product master:** SKU, description, category, dimensions, price
- **Location master:** Store ID, address, region, manager
- **Supplier master:** Vendor ID, name, payment terms, contact

### The Golden Record Problem

Without MDM, the same entity may have different representations in different systems. Example:

- CRM: "Apple Inc." in San Jose
- ERP: "APPLE INC" in Cupertino
- Billing: "Apple, Inc." in San Jose, CA

These are the same company, but JOIN queries will produce three records instead of one. Analytics show three customers instead of one. Revenue is fragmented.

MDM resolves this by creating a single **golden record** — the definitive, authoritative representation of each entity — with a unique master identifier that all systems reference.

### MDM Implementation Styles

| Style | Description | When to Use |
|-------|-------------|-------------|
| Consolidation | MDM hub aggregates records from source systems; sources unchanged | Low disruption; analytics focus |
| Registry | MDM hub stores only a cross-reference index; sources retain records | Minimal footprint; sources remain authoritative |
| Coexistence | Golden records synchronized back to source systems | Gradual migration; operational and analytical use |
| Centralized | All writes go to MDM hub; source systems replaced | Full transformation; highest consistency |

### Data Stewardship in MDM

Data stewards are responsible for:

- Defining matching and survivorship rules (how to choose the "best" value when sources disagree)
- Approving or rejecting proposed golden record merges
- Investigating and resolving suspected duplicates
- Maintaining the business glossary entries for master data entities

---

## Section 6: Data Catalogs

### Definition and Purpose

A data catalog is a metadata management system that enables analysts and data consumers to discover, understand, evaluate, and trust data assets within an organization.

### Metadata Types in a Data Catalog

| Metadata Type | Description | Examples |
|---------------|-------------|---------|
| Technical metadata | Structure and location of data | Table names, column types, row counts, source database |
| Business metadata | Business meaning and ownership | Plain-language descriptions, data owner, data steward |
| Operational metadata | Currency and usage statistics | Last refresh date, query count, data freshness score |
| Data lineage | Origin, transformations, and downstream usage | Source system → ETL → warehouse → dashboard |
| Data quality metadata | Assessed quality scores | Completeness %, validity rate, duplicate count |

### Data Lineage

Data lineage documents the full journey of data from origin to consumption:

`Source system → ETL pipeline → staging table → warehouse fact table → BI report → executive dashboard`

Lineage supports:

- Impact analysis (what breaks if this source changes?)
- Root cause analysis (why is this dashboard number wrong?)
- Regulatory compliance (prove this metric comes from an auditable source)

### Data Catalog Benefits

- Reduces analyst data discovery time from hours to minutes
- Enables self-service analytics — analysts can evaluate data quality before using it
- Supports governance by surfacing ownership, lineage, and certifications
- Prevents the "data swamp" problem by making metadata explicit

### Popular Data Catalog Tools

Alation, Collibra, Microsoft Purview, AWS Glue Data Catalog, Google Data Catalog, Apache Atlas, Amundsen.

---

## Section 7: The DAMA Framework

DAMA International publishes the **DMBOK** (Data Management Body of Knowledge) — the professional standard for data management. The DAMA framework organizes data management into 11 knowledge areas.

### The 11 DAMA Knowledge Areas

| # | Knowledge Area | Brief Description |
|---|---------------|-------------------|
| 1 | Data Governance | Overarching framework; oversight for all other areas |
| 2 | Data Architecture | Enterprise data design and structure |
| 3 | Data Modeling and Design | Conceptual, logical, and physical data models |
| 4 | Data Storage and Operations | Database administration, backup, recovery |
| 5 | Data Security | Confidentiality, integrity, and availability |
| 6 | Data Integration and Interoperability | ETL, data exchange, API management |
| 7 | Document and Content Management | Unstructured data (documents, images) |
| 8 | Reference and Master Data | Controlled vocabularies, MDM |
| 9 | Data Warehousing and BI | DW architecture, reporting, analytics |
| 10 | Metadata Management | Data catalog, business glossary |
| 11 | Data Quality | Profiling, monitoring, remediation |

Data Governance sits at the center of the DAMA wheel because it provides the policies, standards, and accountability structures that enable all other knowledge areas to function effectively.

---

## Section 8: SQL for Data Quality Assessment

```sql
-- Completeness check
SELECT
    COUNT(*)                                       AS total_records,
    COUNT(email_address)                           AS non_null_emails,
    ROUND(COUNT(email_address) * 100.0 / COUNT(*), 2) AS email_completeness_pct,
    COUNT(phone_number)                            AS non_null_phones,
    ROUND(COUNT(phone_number) * 100.0 / COUNT(*), 2)  AS phone_completeness_pct
FROM customer;

-- Validity check: invalid email format (no @ symbol)
SELECT COUNT(*) AS invalid_email_count
FROM customer
WHERE email_address NOT LIKE '%@%.%';

-- Uniqueness check: duplicate email addresses
SELECT email_address, COUNT(*) AS occurrence_count
FROM customer
GROUP BY email_address
HAVING COUNT(*) > 1
ORDER BY occurrence_count DESC;

-- Timeliness check: records not updated in over 2 years
SELECT COUNT(*) AS stale_record_count
FROM customer
WHERE last_updated_date < CURRENT_DATE - INTERVAL '2 years';

-- Consistency check: mismatched region/state combinations
SELECT COUNT(*) AS inconsistency_count
FROM customer c
JOIN region_state_ref r ON c.region = r.region
WHERE c.state_code != r.expected_state_code;
```

---

## Section 9: Data+ Exam Tips

**Tip 1:** The six quality dimensions — Accuracy, Completeness, Consistency, Timeliness, Validity, Uniqueness — are directly tested. Practice mapping scenario descriptions to the correct dimension.

**Tip 2:** Data owner vs. data steward — the owner has strategic accountability; the steward handles operational quality management. The exam may present scenarios requiring you to identify who is responsible for a given action.

**Tip 3:** A golden record is the single authoritative record for a master data entity, created by MDM. Know that the purpose of MDM is to resolve inconsistent representations of the same entity across systems.

**Tip 4:** Data catalog vs. data dictionary — a data catalog is a searchable, enterprise-wide metadata platform with lineage, quality scores, and business context. A data dictionary is a simpler reference document defining column names and data types.

**Tip 5:** DAMA governance is at the center of the DMBOK wheel. This centrality reflects that governance provides the enabling policies for all 11 knowledge areas.

**Tip 6:** Completeness and accuracy are independent. A field can be filled (complete) with wrong data (inaccurate). Exam distractors frequently conflate these two dimensions.

---

## 9. Supplemental Resources

**1. DAMA International — DMBOK Overview**
<https://www.dama.org/cpages/body-of-knowledge>
The official DAMA Data Management Body of Knowledge overview page, describing all 11 knowledge areas in the DMBOK framework. Essential background for understanding the governance structures, roles (data owner, steward, custodian), and how data quality fits within a broader data management program.

**2. Collibra Data Intelligence — What is a Data Catalog?**
<https://www.collibra.com/us/en/blog/what-is-a-data-catalog>
A practitioner-oriented explanation of data catalogs, data dictionaries, and business glossaries — clarifying when each tool is appropriate and how they work together. Directly supports the Module 10 governance artifact comparisons tested on the Data+ exam.

**3. IBM — Data Quality Dimensions Explained**
<https://www.ibm.com/think/topics/data-quality>
IBM's reference guide covering the six core data quality dimensions (accuracy, completeness, consistency, timeliness, validity, uniqueness) with real-world business examples for each. Useful as a study reference for mapping exam scenarios to the correct dimension.

---

End of Module 10 Reading Guide

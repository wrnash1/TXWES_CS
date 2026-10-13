# Video Script: Module 10 — Data Quality and Governance

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA Data+ (DA0-001)

---

## Segment 1: Introduction (0:00–1:30)

Welcome back to CIS-4336. I'm Professor Nash. Today we are covering a topic that many analysts underestimate until a major crisis forces their attention to it — data quality and data governance.

Here is a sobering statistic: poor data quality costs organizations an average of $12.9 million per year, according to research from Gartner. More importantly, analysts who build models, dashboards, and reports on top of low-quality data produce outputs that are worse than having no analysis at all — because bad analysis breeds misplaced confidence.

Data governance is the organizational discipline that prevents this. It defines who owns data, who is responsible for its quality, how it is defined, and how it is protected.

By the end of this module you will understand the six dimensions of data quality, the role of data stewardship, master data management, data catalogs, and the DAMA framework. These concepts are tested in Domain 5 of the CompTIA Data+ exam — Data Governance, Quality, and Controls.

[PAUSE — Slide: Module 10 Objectives]

---

## Segment 2: What Is Data Quality? (1:30–4:00)

Data quality is the degree to which data is fit for its intended use. Notice that phrase: "fit for its intended use." Perfect data quality in one context may be insufficient in another.

A phone number field in a customer record must have different quality standards depending on how it is used. For a marketing SMS campaign, it must be valid and opted-in. For regulatory reporting, it must be formatted correctly for the jurisdiction. For a fraud detection model, it must be current and not spoofed.

[SHOW CHART — Six dimensions of data quality as a hexagon diagram]

[PAUSE]

Data quality is measured along six dimensions. Let's go through each one.

---

## Segment 3: The Six Dimensions of Data Quality (4:00–9:00)

### Accuracy

Accuracy is the degree to which data correctly reflects the real-world entity or event it represents.

Example: A customer database lists a customer's city as "Dallas" but the customer actually lives in Fort Worth. The data is inaccurate.

How to assess accuracy: compare records against authoritative external sources (address verification services, government registries, third-party data enrichment).

[PAUSE]

### Completeness

Completeness is the degree to which all required data is present.

Example: A patient record is missing the date of birth field in 18% of records. Those records are incomplete for any analysis requiring age calculation.

Completeness is often measured as a percentage: `completeness = non_null_records / total_records * 100`.

Note that completeness and accuracy are independent. A record can be complete (all fields filled) but inaccurate (wrong values). It can also be accurate but incomplete (right values where present, but some required fields missing).

[PAUSE]

### Consistency

Consistency is the degree to which data values across different systems or datasets agree with each other.

Example: The customer address in the CRM system says "123 Main St." The same customer's address in the billing system says "123 Main Street." Both might be correct representations of the same address, but they are inconsistent — queries joining the two systems will fail to match the records.

Consistency issues often arise during system integrations and data migrations.

[PAUSE]

### Timeliness

Timeliness is the degree to which data is available when needed and reflects the current state of the entity it represents.

Example: Customer contact data that was last updated 3 years ago may be outdated. For an outreach campaign, stale contact data results in wasted effort and high bounce rates.

Timeliness is not just about how old the data is — it is about whether the data is current enough for its intended use. A monthly financial report can tolerate month-old data. A real-time fraud detection system cannot tolerate data that is 2 seconds old.

[PAUSE]

### Validity

Validity is the degree to which data conforms to defined business rules, formats, and constraints.

Example: A date field contains the value "February 30, 2024" — that date does not exist. An email field contains "john_at_email.com" — missing the @ symbol. An age field contains -5. All three are invalid.

Validity checks include: range checks, format checks, referential integrity checks, and business rule validation.

[PAUSE]

### Uniqueness

Uniqueness is the degree to which each entity is represented exactly once in a dataset.

Example: A customer database contains 3 records for "John Smith" at the same address — the result of three separate account creations over five years. Each record is technically accurate, but the duplication causes incorrect count metrics and split customer histories.

Uniqueness violations — duplicate records — are one of the most common and damaging data quality problems.

[SHOW CHART — Table showing a dataset with examples of violations for each dimension]

---

## Segment 4: Data Stewardship (9:00–11:30)

Identifying data quality problems is only half the battle. Someone has to own the responsibility for fixing them and preventing them from recurring. That is the role of the **data steward**.

A data steward is a person (or team) assigned responsibility for a specific data domain — such as customer data, product data, or financial data. Their responsibilities include:

- Defining and maintaining data standards and business definitions
- Monitoring data quality metrics and investigating violations
- Resolving data issues and escalating systemic problems
- Coordinating with IT on data source systems
- Training data creators and consumers on standards

[PAUSE]

Data stewardship is distinct from data ownership. A **data owner** is typically an executive or business leader who has ultimate accountability for a data domain — they make strategic decisions about how data is used. A data steward handles the operational execution of those decisions.

[SHOW CHART — RACI matrix: Data Owner, Data Steward, IT (DBA), Data Consumer roles]

Without stewardship, data quality problems accumulate invisibly until they cause a major failure. With stewardship, quality is continuously monitored and maintained.

---

## Segment 5: Master Data Management (11:30–14:00)

Master data is the core business data that is shared across multiple systems — customers, products, employees, locations, suppliers. This data is referenced by operational systems (CRM, ERP, billing) and analytical systems (data warehouses, BI tools) alike.

**Master Data Management** (MDM) is the discipline of creating and maintaining a single, authoritative, consistent record for each master data entity — called the **golden record** or **system of record**.

[SHOW CHART — MDM architecture: multiple source systems → MDM hub → golden records → downstream systems]

[PAUSE]

### Why MDM Matters

Without MDM, a multinational company might have:

- Customer "Acme Corp" in the CRM system
- "ACME Corporation" in the ERP system
- "Acme Corp, Inc." in the billing system

These are the same company — but a database JOIN on the customer name field will not match them. The result: fragmented analytics, duplicate mailings, incorrect revenue reporting.

MDM solves this by establishing a single golden record for "Acme Corporation" with a unique identifier that all systems reference.

### MDM Implementation Styles

- **Consolidation style:** Golden records are created in the MDM hub by merging source system records; source systems are not changed.
- **Registry style:** The MDM hub maintains only a cross-reference index; source systems retain their original records.
- **Coexistence style:** Golden records are created and synchronized back to source systems.
- **Centralized style:** Source systems are replaced; all writes go to the MDM hub.

[PAUSE]

---

## Segment 6: Data Catalogs (14:00–16:30)

A **data catalog** is a metadata management tool that helps analysts find, understand, and trust data assets within an organization. Think of it as a searchable index for all of the organization's data.

A data catalog contains:

- **Technical metadata** — table names, column names, data types, row counts, source system
- **Business metadata** — plain-language descriptions, business owners, data stewards
- **Operational metadata** — last updated, refresh schedule, row count trends
- **Data lineage** — where the data came from and how it has been transformed
- **Data quality scores** — completeness, validity, and freshness metrics
- **Certifications** — which datasets are officially endorsed as authoritative

[SHOW CHART — Data catalog UI screenshot mockup showing search results with metadata, quality scores, and lineage]

[PAUSE]

### Why Data Catalogs Matter

Without a catalog, analysts spend 20–30% of their time searching for data — figuring out which table contains what they need, whether it is current, who to ask when something looks wrong, and whether they can trust the numbers.

A good data catalog reduces this discovery time dramatically, enables data self-service, and supports governance by making ownership and lineage visible to all users.

Popular data catalog tools include: Alation, Collibra, Microsoft Purview, AWS Glue Data Catalog, Apache Atlas.

---

## Segment 7: The DAMA Framework (16:30–18:30)

The **DAMA International** (Data Management Association) framework is the most widely recognized body of knowledge for data management. It is organized around 11 knowledge areas, with **data governance** at the center.

[SHOW CHART — DAMA DMBOK wheel diagram with 11 knowledge areas]

The 11 DAMA knowledge areas are:

1. Data Governance — the center; provides oversight for all other areas
2. Data Architecture
3. Data Modeling and Design
4. Data Storage and Operations
5. Data Security
6. Data Integration and Interoperability
7. Document and Content Management
8. Reference and Master Data
9. Data Warehousing and Business Intelligence
10. Metadata Management
11. Data Quality

[PAUSE]

For the Data+ exam, you do not need to memorize all 11 areas. What you need to know:

- Data governance is the overarching discipline that enables all other data management areas
- DAMA provides the professional framework and vocabulary for data management practitioners
- The DMBOK (Data Management Body of Knowledge) is the primary reference document

---

## Segment 8: Data Quality in SQL (18:30–20:00)

You can assess data quality directly using SQL — checking completeness, validity, uniqueness, and consistency in a database.

[PAUSE]

```sql
-- Completeness check: percentage of non-null email addresses
SELECT
    COUNT(*)                                      AS total_records,
    COUNT(email_address)                          AS non_null_emails,
    ROUND(COUNT(email_address) * 100.0
          / COUNT(*), 2)                          AS completeness_pct
FROM customer;

-- Validity check: invalid date of birth (future dates or impossibly old)
SELECT COUNT(*) AS invalid_dob_count
FROM customer
WHERE date_of_birth > CURRENT_DATE
   OR date_of_birth < DATE '1900-01-01';

-- Uniqueness check: duplicate customer emails
SELECT email_address, COUNT(*) AS occurrence_count
FROM customer
GROUP BY email_address
HAVING COUNT(*) > 1
ORDER BY occurrence_count DESC;
```

[PAUSE]

These simple queries give you an immediate picture of data quality issues in any relational dataset. Real data profiling tools automate these checks across thousands of columns.

---

## Segment 9: Module Summary (20:00–21:30)

Let me wrap up.

[PAUSE]

The six dimensions of data quality:

- **Accuracy** — data correctly reflects reality
- **Completeness** — all required values are present
- **Consistency** — data agrees across systems
- **Timeliness** — data is current enough for its intended use
- **Validity** — data conforms to defined rules and formats
- **Uniqueness** — each entity appears exactly once

Key governance roles:

- **Data owner** — executive accountability for a data domain
- **Data steward** — operational management of data quality standards

Master Data Management creates golden records — single authoritative versions of core business entities.

Data catalogs make data discoverable, understandable, and trustworthy through metadata management and lineage documentation.

The DAMA framework organizes all 11 areas of data management with governance at the center.

For the Data+ exam: know all six quality dimensions, the difference between data owner and data steward, what a golden record is, and the purpose of a data catalog.

See you in Module 11 — SQL for Data Analytics.

[PAUSE — End card]

---

End of Module 10 Video Script

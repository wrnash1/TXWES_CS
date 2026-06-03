# Video Script: Module 12 — Data Migration

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 20–24 minutes

---

## Pre-Production Notes

- Slide deck: 28 slides
- Diagrams: ETL pipeline flow, data migration project phases, data quality dimensions, cutover timeline, Salesforce Data Loader vs. Data Import Wizard comparison
- Key terms on screen: ETL, Extract, Transform, Load, Data Cleansing, Deduplication, Data Profiling, Cutover, Cutback Plan, Upsert, External ID, Staging Area, Reconciliation
- End card: Lab 12, Quiz 12, Discussion Forum 12

---

## [00:00 – 02:00] Opening Hook

[PROFESSOR ON CAMERA]

I want to tell you about a data migration I know of at a consumer goods company. They were moving from a legacy customer database to Salesforce. The legacy system had been running for 14 years. Over 14 years, the sales team had entered customer data freely — no validation rules, no required fields, no standards for anything.

When the migration team extracted the data to analyze it, here is what they found:

1.2 million customer records. Of those, approximately 340,000 were duplicates — the same customer under slightly different names or slightly different addresses. 87,000 records had no email address. 150,000 records had phone numbers in 12 different formats. 22,000 records referenced sales territories that no longer existed. And approximately 60,000 records were what the team called "dead data" — companies that had gone out of business or contacts who had left their companies years ago.

The data migration was supposed to take three months. It took nine. Not because of technical problems. Because of data quality problems.

This is the reality of data migration in enterprise systems. It is not a technical exercise of moving files from point A to point B. It is a data quality project that happens to end with loading data into a new system. And if you do not understand that at the start, you will be explaining to your project sponsor why the go-live date slipped by six months.

[SHOW TITLE SLIDE: Module 12 — Data Migration]

---

## [02:00 – 06:00] The ETL Framework

[SHOW DIAGRAM: ETL Pipeline — Three boxes left to right: Extract, Transform, Load]

Data migration projects follow the ETL framework: Extract, Transform, Load. Let me walk through each stage.

[SHOW SLIDE: Extract]

Extract means pulling data out of the source system. The source might be a legacy ERP, a spreadsheet, a flat file database, an old CRM, or multiple systems simultaneously. Extraction is usually done through SQL queries against the source database, API calls to the source system, or export functions built into the legacy application.

The extract should be a complete, unmodified snapshot of the source data as it exists. Do not filter data during extraction — you want to see everything first, because data profiling during the Transform phase depends on the complete dataset. You will make decisions about what to keep, clean, or discard — but those decisions belong in the Transform phase, not the Extract phase.

The extracted data typically lands in a staging area — a neutral location (often a staging database or set of CSV files) where the data can be inspected, cleaned, and transformed without touching either the source or the target system.

[SHOW SLIDE: Transform]

Transform is the most labor-intensive step and the one most commonly underestimated.

Transform includes data cleansing — identifying and correcting errors, inconsistencies, and missing values. It includes deduplication — finding and merging or removing duplicate records. It includes format normalization — converting phone numbers, dates, addresses, and other fields from legacy formats to the target system's format. It includes code mapping — the source system may use code "1" for status "Active" while the target uses "ACT". And it includes field mapping — determining which source field maps to which target field, including cases where source fields must be split, combined, or derived to create target fields.

Data profiling is the analysis work that happens at the start of the Transform phase. Before you can clean data, you need to understand what is wrong with it. Data profiling runs statistical analysis on the extracted data: how many null values in each field? How many distinct values in each field? What are the outliers? What format variations exist?

[SHOW SLIDE: Load]

Load means writing the transformed data into the target system.

In Salesforce, the Load step uses either the Data Loader (for large volumes — more than 50,000 records) or the Data Import Wizard (for smaller datasets and standard objects). Both tools accept CSV files with column headers matching the Salesforce field API names.

In SAP, the Load step uses LSMW (Legacy System Migration Workbench), BAPI calls in batch programs, or SAP's Data Migration Cockpit in S/4HANA — which provides a guided, template-based migration framework.

The Load step includes post-load validation: comparing record counts between the source dataset and the loaded target to confirm all records migrated successfully. Any failures are logged, corrected, and re-loaded before sign-off.

---

## [06:00 – 10:00] Data Quality Dimensions

[SHOW SLIDE: The Six Dimensions of Data Quality]

Data quality is not a single concept — it has multiple dimensions, and understanding them helps you build a comprehensive data cleansing plan.

Completeness: are all required fields populated? Missing email addresses, missing postal codes, missing phone numbers.

Accuracy: is the data factually correct? An account record showing annual revenue of $500 billion for a local restaurant is inaccurate.

Consistency: is the same data represented the same way across all records? Phone numbers in 12 formats are inconsistent.

Uniqueness: does each real-world entity appear exactly once? A customer database with 340,000 duplicates violates uniqueness.

Timeliness: is the data current? Contacts who left their companies three years ago represent stale data.

Validity: does the data conform to the rules of the target system? A date value of "February 30" is not a valid date.

[SHOW DIAGRAM: Data Quality Assessment Matrix — rows are dimensions, columns are objects (Accounts, Contacts, Opportunities), cells show quality scores]

During data profiling, the team scores each data object against each quality dimension. This analysis drives the cleansing work plan and estimates how long the Transform phase will take. Organizations that skip data profiling almost always discover major quality problems mid-transformation, which is why migrations take longer than planned.

---

## [10:00 – 14:00] SAP Data Migration Architecture

[SHOW SLIDE: SAP Migration Tools]

SAP provides specific tools for data migration, and these appear on SAP certification exams.

LSMW — Legacy System Migration Workbench — is the older, widely used tool for migrating master data and transaction data into SAP ECC and S/4HANA. LSMW works through a series of steps: source structure definition, field mapping, data conversion, and batch input recording. LSMW can run in the foreground or background and produces detailed migration logs.

[SHOW SLIDE: SAP Data Migration Cockpit (S/4HANA)]

In S/4HANA, SAP's recommended tool is the Migration Cockpit, accessible in Fiori. The Migration Cockpit provides pre-delivered migration templates for common objects: vendor master, customer master, GL accounts, open items, material master, purchase orders. Each template specifies the exact fields and format the system expects. The migration team downloads the template, populates it with transformed source data, uploads the file, and runs the migration program. The Migration Cockpit generates a detailed log of successes and errors.

[EXAM TIP ON SCREEN]

For the SAP exam: LSMW is the legacy tool; Migration Cockpit is the S/4HANA tool. Both are used for initial data load from external systems. Know the distinction.

[SHOW SLIDE: SAP Migration Object Sequencing]

In SAP, the order in which objects are migrated matters. Dependent objects cannot be created before the objects they reference.

Master data must be migrated before transactional data. G/L accounts must exist before journal entries can reference them. Vendor master records must exist before purchase orders can be created. Customer master records must exist before sales orders reference them. Material master records must exist before goods movements can be posted.

Within master data, organizational structure must exist before functional data. Company codes must exist before G/L accounts. Plants must exist before material master records. This sequencing requirement is a common exam topic.

---

## [14:00 – 18:00] Salesforce Data Migration Tools

[SHOW SLIDE: Salesforce Data Migration Tools Comparison]

Salesforce provides two primary tools for data migration, and choosing between them is an exam topic.

[SHOW DIAGRAM: Data Import Wizard — screenshot showing the wizard interface]

Data Import Wizard is the browser-based tool in Salesforce Setup. It supports standard objects (Accounts, Contacts, Leads, Solutions, Campaign Members) and custom objects. It handles files up to 50,000 records. It is easy to use and requires no installation. It is appropriate for small to medium migrations by administrators without developer skills.

[SHOW DIAGRAM: Data Loader — screenshot showing the Data Loader desktop application]

Data Loader is a downloadable desktop application. It supports all standard and custom objects, handles files of millions of records, and supports all five operations: insert, update, upsert, delete, and hard delete. Data Loader is the tool of choice for large migrations, complex upsert operations, and automated scheduled data loads.

[SHOW SLIDE: Upsert and External ID]

Upsert is a critical migration operation. An upsert inserts records that do not yet exist in Salesforce and updates records that do exist — in a single operation. This is essential for incremental migrations where the first full load runs, then subsequent smaller loads bring in new or updated records from the source system.

To perform an upsert, Salesforce needs a way to identify whether a record already exists. That identifier is the External ID — a custom field on the Salesforce object that stores the record's unique ID from the source system. When the upsert runs, Salesforce looks up each record by its External ID: if found, update; if not found, insert.

[EXAM TIP ON SCREEN]

For the Salesforce exam: External ID fields enable upsert operations. Without an External ID, the only way to avoid duplicates is to delete and re-load, which is destructive and error-prone. External IDs are also useful for maintaining relationships between migrated objects — a Contact's External ID can reference its parent Account's External ID to establish the relationship without needing the Salesforce-generated Account ID.

---

## [18:00 – 21:30] Migration Project Lifecycle

[SHOW DIAGRAM: Migration Phase Timeline]

A data migration project follows a lifecycle that parallels the broader ERP implementation.

Phase 1 — Discovery and Planning: inventory the source data, identify migration objects, establish data quality requirements, estimate volume.

Phase 2 — Data Profiling: extract source data to a staging environment and analyze it against all six quality dimensions. Produce a data quality assessment report that quantifies the cleansing work needed.

Phase 3 — Rules and Mapping Design: document the transformation rules (field mapping, code mapping, derivation logic) and get business stakeholder sign-off on every mapping decision.

Phase 4 — Iterative ETL Development: build the extraction scripts, transformation rules, and load programs. Run the migration against development/QA environments. Run it multiple times — each run surfaces new data quality problems to resolve.

Phase 5 — Mock Cutover (one or more rehearsals): run the full migration against a production-like environment, measure how long it takes, and resolve any remaining issues. Each mock cutover is a rehearsal for the real thing.

Phase 6 — Production Cutover: execute the final migration against the production system. Freeze source system data during cutover to prevent new records from appearing after the extract. Run validation checks. Sign off on migration completeness before go-live.

Phase 7 — Post-Migration Validation: business users spot-check data in the new system. Compare totals (record counts, financial balances, open item amounts) between source and target. Document any discrepancies and resolve them.

[SHOW SLIDE: Cutover Planning]

The cutover weekend — the 48 or 72 hours when the actual production migration runs — requires detailed minute-by-minute planning. Every step must be timed: how long does the vendor master extract take? How long does the transformation job run? How long does the load take for 50,000 GL open items? If the total time exceeds the available cutover window, the plan must be revised.

Every cutover plan must include a cutback plan — the documented procedure for reversing the migration and returning to the legacy system if critical issues are discovered after go-live. Having a cutback plan does not mean you expect to use it. It means you have thought through the worst-case scenario.

---

## [21:30 – 23:30] Certification Exam Summary

[SHOW SLIDE: Key Exam Points — Data Migration]

ETL sequence: Extract (pull from source), Transform (clean, map, normalize), Load (write to target). Know which activities belong to each phase.

Data quality dimensions: completeness, accuracy, consistency, uniqueness, timeliness, validity. Know what each means.

Upsert requires an External ID — a field on the Salesforce object storing the source system's unique identifier.

Data Import Wizard: browser-based, up to 50,000 records, standard and custom objects, no installation.

Data Loader: desktop application, millions of records, all objects, supports insert/update/upsert/delete/hard delete.

SAP migration tools: LSMW (legacy), Migration Cockpit (S/4HANA recommended). Object sequencing: master data before transactional data.

Mock cutover rehearsals reduce go-live risk. Every production cutover plan needs a cutback plan.

---

## [23:30 – 24:00] Closing and Assignments

[PROFESSOR ON CAMERA]

Data migration is where ERP implementations succeed or fail. The technology is rarely the problem. The data quality is almost always the problem. The organizations that run the best migrations are the ones that invest time in data profiling and cleansing before go-live, not the ones that rush through transformation hoping the problems will sort themselves out during load.

Your Lab 12 has you working through a realistic migration scenario — analyzing source data quality issues, designing transformation rules, and building a migration sequence for a manufacturing company's SAP implementation. Take the data quality analysis seriously.

I will see you in Module 13.

[END CARD: Lab 12 | Quiz 12 | Discussion Forum 12]

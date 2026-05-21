# Reading Guide: Module 12 - Data Migration

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 12 - Data Migration**! Every ERP or CRM implementation eventually reaches the point where the old system's data must be transferred to the new platform — and data migration is consistently cited as one of the highest-risk activities in the entire project. Poor data quality in the new system undermines user trust, causes operational errors, and can force expensive post-go-live remediation.

This module covers the ETL (Extract, Transform, Load) process, data cleaning and deduplication techniques, field mapping templates, and the validation steps that verify migrated data meets quality standards before go-live.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Extract (ETL step 1)**: The process of pulling data out of the source system — a legacy database, flat files, or spreadsheets — in its native format. Extraction must capture all required records without corrupting the source system or its ongoing operations.
* **Transform (ETL step 2)**: The process of cleaning, reformatting, and mapping extracted data to match the target system's data model. Transformations include splitting combined fields, standardizing date formats, looking up code values, deduplicating records, and applying business rules that the source system did not enforce.
* **Load (ETL step 3)**: The process of writing the transformed data into the target ERP or CRM system. In Salesforce, loading uses tools like Data Loader or Salesforce Data Import Wizard. In SAP, loading uses LSMW (Legacy System Migration Workbench), BAPI calls, or SAP Data Services.
* **Data cleaning**: The activities performed during the Transform phase to correct errors, remove duplicates, fill missing required fields, and standardize inconsistent values (e.g., "USA," "U.S.A.," and "United States" all normalized to "US") before loading to the new system.
* **Mapping templates**: Spreadsheet or tool-based documents that define, field by field, how source system data maps to target system fields — including transformation rules, default values for missing data, and rejection rules for records that cannot be mapped.
* **Validation checks**: Post-load verification steps that confirm the migrated data in the target system matches the expected record counts, key field values, and relational integrity from the source. Validation typically includes reconciliation reports comparing source and target totals.

---

### 2. Certification Exam Tips

* **Salesforce data migration tools:** Know the difference between Data Import Wizard (browser-based, up to 50,000 records, limited objects) and Data Loader (desktop app, millions of records, all objects, CSV input). The Associate exam expects you to know when to use each.
* **SAP LSMW:** The Legacy System Migration Workbench is SAP's built-in tool for one-time data loads from legacy systems. It maps source fields to SAP fields and generates batch input sessions or calls BAPIs. Know that LSMW is used for initial data loads, not ongoing interface processing.
* **Data quality gate:** A key exam concept — migration data should pass through a quality gate (validation check) in the staging environment before being loaded to production. Go-live should never proceed with known data quality failures.
* **Deduplication before load:** Duplicate records (two customer accounts for the same company, two vendor records for the same supplier) must be resolved during the Transform phase, not after loading. Post-load deduplication in an ERP is far more expensive and risky.
* **Study Resource:** Complete the Salesforce Trailhead module [Data Management](https://trailhead.salesforce.com/content/learn/modules/lex_implementation_data_management) — a free module covering Salesforce data import tools, deduplication, and data quality best practices.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Complete the Salesforce Trailhead module [Data Management](https://trailhead.salesforce.com/content/learn/modules/lex_implementation_data_management) — a free module explaining data import tools, deduplication, and quality management in Salesforce.
* **Required Video:** Watch the video lecture on **Data Migration** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Clean database records removing duplicate contacts**: Given a CSV file with 50 contact records including duplicates identified by matching email address, write deduplication rules to identify which record to keep and which to discard, then produce a cleaned file.
* **Map field variables from legacy CSV to ERP tables**: Create a field mapping template for migrating customer records from a legacy system (with columns: CustName, CustAddr1, CustCity, CustPhone) to a Salesforce Account object (fields: Name, BillingStreet, BillingCity, Phone), specifying any required transformations.
* **Verify import logs**: Using Salesforce Data Loader's success and error log files from a sample import run, identify the three records that failed to load, determine the cause of each failure (missing required field, invalid format, duplicate), and propose a correction.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to describe what happens in each ETL step with a concrete example.
* [ ] Complete [Data Management](https://trailhead.salesforce.com/content/learn/modules/lex_implementation_data_management) on Trailhead (earn the badge).
* [ ] Watch the video lecture on **Data Migration** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab deduplication exercise, field mapping template, and import log analysis.
* [ ] Proceed to the weekly quiz.

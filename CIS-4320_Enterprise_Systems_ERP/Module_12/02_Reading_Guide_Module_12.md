# Reading Guide: Module 12 — Data Migration

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Introduction

Every ERP implementation begins with a critical challenge: getting data from the old system into the new one. Data migration is the process of extracting data from legacy systems, transforming it to meet the new system's data model and quality standards, and loading it into the target ERP. It is consistently underestimated in project planning and consistently responsible for delays. This module covers the ETL framework, data quality dimensions, SAP and Salesforce migration tools, and the project lifecycle of a production data migration. Both the SAP and Salesforce certification exams test your understanding of migration tools, phases, and validation techniques.

---

## Section 1: High-Yield Glossary

**ETL (Extract, Transform, Load)**
The three-phase framework for data migration. Extract: pull source data as-is into a staging area. Transform: clean, map, normalize, and enrich the data to meet target system requirements. Load: write the transformed data into the target system.

**Data Profiling**
Analysis of extracted source data to identify quality issues: null values, format inconsistencies, duplicates, out-of-range values, and orphaned references. Data profiling happens at the start of the Transform phase and drives the cleansing work plan.

**Data Cleansing**
The process of identifying and correcting data quality issues in the extracted dataset before loading. Includes deduplication, format normalization, field population, and invalid-value remediation.

**Deduplication**
The process of identifying records that represent the same real-world entity (a customer who appears twice under slightly different names or addresses) and merging or removing the duplicate.

**Staging Area**
A neutral environment (database or file storage) where extracted source data is held for profiling, transformation, and validation — separate from both the source system and the target system.

**Field Mapping**
A documented definition of which source system field maps to which target system field. Includes any transformation logic applied to the field value during migration.

**Code Mapping**
A lookup table translating code values from the source system to the target system. Example: source system uses "1" for Active status; target system uses "ACT". Code mapping ensures source values are correctly interpreted in the target.

**External ID**
A custom field on a Salesforce object that stores the record's unique identifier from the source system. Required for upsert operations — allows Salesforce to determine whether an incoming record should be inserted (new) or updated (already exists).

**Upsert**
A combined insert/update operation. If a record with the matching External ID already exists in the target, it is updated. If no match is found, a new record is inserted. Upsert is essential for incremental migrations.

**Data Import Wizard**
Salesforce's browser-based migration tool. Supports standard and custom objects, up to 50,000 records per import, insert and update operations. Accessible from Setup. No installation required.

**Data Loader**
Salesforce's desktop application for data migration. Supports all objects, millions of records, and five operations: insert, update, upsert, delete, hard delete. Required for large-volume migrations.

**LSMW (Legacy System Migration Workbench)**
SAP's legacy tool for migrating data from external systems into SAP ECC and S/4HANA. Works through a step-by-step process: define source structure, define field mapping, convert data, run migration.

**SAP Migration Cockpit**
SAP's recommended S/4HANA migration tool. Provides pre-delivered templates for standard migration objects (vendor master, customer master, GL accounts, open items). Template-based approach simplifies field mapping.

**Mock Cutover**
A rehearsal of the production data migration executed against a production-like test environment. Used to verify the migration process, measure execution time, and identify remaining issues before go-live.

**Cutover Plan**
The minute-by-minute execution plan for the production data migration weekend. Specifies every step, responsible party, expected duration, and pass/fail criteria for each phase.

**Cutback Plan**
The documented procedure for reversing the migration and returning to the legacy system if critical issues are discovered after go-live. Every production cutover plan must have a tested cutback plan.

**Reconciliation**
Post-load validation comparing source system totals to target system totals. Includes record counts, financial balances, open item amounts, and key field spot-checks.

---

## Section 2: The ETL Framework in Detail

### ETL Phase Overview

```text
LEGACY SYSTEM / SOURCE
        |
        | EXTRACT
        | (SQL queries, export functions, API calls)
        v
STAGING AREA
  Raw source data -- unmodified
        |
        | TRANSFORM
        | 1. Data Profiling (analyze quality issues)
        | 2. Deduplication (remove/merge duplicates)
        | 3. Data Cleansing (fix errors, fill gaps)
        | 4. Format Normalization (standardize values)
        | 5. Field Mapping (source field --> target field)
        | 6. Code Mapping (source codes --> target codes)
        | 7. Relationship Resolution (link parent-child records)
        v
TRANSFORMED DATASET
  Validated, cleaned, mapped to target format
        |
        | LOAD
        | (Data Loader, Data Import Wizard, LSMW,
        |  SAP Migration Cockpit, BAPI calls)
        v
TARGET SYSTEM (SAP S/4HANA / Salesforce)
        |
        | POST-LOAD VALIDATION
        | Record count reconciliation
        | Financial balance comparison
        | Spot-check key records
        v
SIGN-OFF
```

### Data Quality Dimensions

| Dimension | Definition | Example Issue | Resolution |
|---|---|---|---|
| Completeness | All required fields populated | Email missing for 12% of contacts | Enrich from CRM, contact vendor, or flag for manual completion |
| Accuracy | Values are factually correct | Annual revenue = $5 trillion for a small business | Research and correct or flag for review |
| Consistency | Same entity represented the same way across all records | Phone in 12 different formats | Normalize all to single format in Transform |
| Uniqueness | Each real-world entity appears exactly once | Customer "Acme Corp" and "Acme Corporation" both in DB | Deduplicate: merge or flag for manual review |
| Timeliness | Data reflects current reality | 40% of contacts left their companies 2+ years ago | Mark stale records; exclude or flag |
| Validity | Values conform to target system rules | Status code "X" not valid in target system | Apply code mapping or default to valid value |

---

## Section 3: SAP Migration Tools

### LSMW vs. SAP Migration Cockpit

| Feature | LSMW | SAP Migration Cockpit |
|---|---|---|
| SAP version | ECC and S/4HANA | S/4HANA (recommended) |
| Approach | Step-by-step development (define structure, map, convert, run) | Template-based (download template, populate, upload) |
| Technical skill | Higher — requires ABAP knowledge for complex mappings | Lower — business users can populate templates |
| Objects covered | Flexible — any object if mapping is built | Pre-delivered templates for standard objects |
| Recommended for | Complex custom objects, large legacy migrations | Standard data objects in S/4HANA implementations |

### SAP Migration Object Sequencing

```text
MANDATORY SEQUENCE: Parent objects before dependent objects

TIER 1 -- Organizational Structure (must exist first)
  Company Codes, Plants, Storage Locations,
  Purchasing Organizations, Chart of Accounts

TIER 2 -- Master Data (depends on org structure)
  G/L Account Master (FI-GL)
  Cost Centers (CO)
  Vendor Master (FI-AP)
  Customer Master (FI-AR)
  Material Master (MM)
  Work Centers and Routings (PP)

TIER 3 -- Transactional Data (depends on master data)
  Open Purchase Orders (MM)
  Open Sales Orders (SD)
  GL Open Items / Balance Carry-Forward (FI)
  Payroll Master Data (HCM)
  Production Orders (PP)

VIOLATION: Loading customer open items (Tier 3) before
the Customer Master (Tier 2) = FOREIGN KEY VIOLATION
```

---

## Section 4: Salesforce Migration Tools

### Data Import Wizard vs. Data Loader

| Feature | Data Import Wizard | Data Loader |
|---|---|---|
| Access | Browser (Salesforce Setup) | Desktop application (download) |
| Volume | Up to 50,000 records | Millions of records |
| Objects | Standard objects + custom objects | All standard and custom objects |
| Operations | Insert, Update, Upsert | Insert, Update, Upsert, Delete, Hard Delete |
| Skill required | Low — guided wizard | Medium — CSV mapping configuration |
| Error log | On-screen summary | CSV error log file |
| Best for | Small migrations, admins | Large migrations, developers, scheduled loads |

### Upsert and External ID Workflow

```text
SETUP (done once):
  1. Add custom field "Source_System_ID__c" (External ID = checked) to Account
  2. Add "Source_System_ID__c" to Contact for Account lookup

FIRST FULL LOAD (insert all records):
  Data Loader operation: Insert
  CSV columns: Name, BillingCity, Source_System_ID__c, ...
  Result: 15,000 Account records created; each has Source_System_ID__c populated

INCREMENTAL LOAD (subsequent loads with new/changed records):
  Data Loader operation: Upsert
  External ID field: Source_System_ID__c
  For each record in CSV:
    - If Source_System_ID__c matches existing record --> UPDATE
    - If Source_System_ID__c not found --> INSERT
  Result: new accounts added, changed accounts updated; no duplicates

PARENT-CHILD LOADING (Contacts linked to Accounts):
  Contact CSV uses Account.Source_System_ID__c as relationship field
  Data Loader resolves Account ID from External ID automatically
```

---

## Section 5: Migration Project Lifecycle

### Phase Timeline

| Phase | Activities | Key Output |
|---|---|---|
| 1 — Discovery | Inventory source systems, identify objects, estimate volumes | Migration scope document |
| 2 — Data Profiling | Extract sample data, analyze quality against all 6 dimensions | Data quality assessment report |
| 3 — Rules Design | Document field mapping, code mapping, transformation rules | Migration specification (signed off by business) |
| 4 — ETL Development | Build extraction scripts, transformation logic, load programs | Tested migration programs |
| 5 — Mock Cutover(s) | Full migration rehearsal against test environment | Migration performance metrics; issue log |
| 6 — Production Cutover | Execute final migration; freeze source data; validate | Signed migration acceptance sign-off |
| 7 — Post-Migration | Business spot-checks; reconciliation; defect resolution | Migration closure report |

### Cutover Planning Factors

```text
CUTOVER WINDOW CALCULATION

Available window: Friday 6PM to Monday 7AM = 61 hours

Migration steps with estimated times:
  Source system freeze and final extract: 2 hours
  Vendor Master migration (8,400 records): 3 hours
  Customer Master migration (24,000 records): 6 hours
  GL Account Master migration (1,200 accounts): 1 hour
  Open GL items balance carry-forward: 8 hours
  Open Purchase Orders (6,200 lines): 5 hours
  Open Sales Orders (3,800 lines): 4 hours
  Post-load validation (automated): 4 hours
  Business spot-check review: 8 hours
  Go/No-Go decision: 1 hour
  TOTAL ESTIMATED: 42 hours

Buffer (15%): 6.3 hours
TOTAL WITH BUFFER: 48.3 hours

Available window (61 hours) > Required time (48.3 hours)
CUTOVER IS FEASIBLE -- within window
```

---

## Section 6: Certification Exam Tips

1. **ETL phase boundaries are tested explicitly.** Know which activities belong to Extract (pull raw data), Transform (clean, map, normalize), and Load (write to target + validate).

2. **Data Import Wizard ceiling is 50,000 records.** Above 50,000, Data Loader is required. Data Loader supports delete and hard delete; Data Import Wizard does not.

3. **External IDs enable upsert.** Without an External ID field, Salesforce cannot distinguish a new record from an update. External IDs store the source system's primary key.

4. **SAP object sequencing: master data before transactional data.** This is a logic-based principle. You cannot post a journal entry to a G/L account that does not exist. You cannot create an open vendor invoice for a vendor who is not in the vendor master.

5. **LSMW is the legacy SAP migration tool; Migration Cockpit is the S/4HANA recommended tool.** Both appear on SAP exams.

6. **Mock cutover is the most important risk-reduction activity.** Running the full migration against a production-like environment before go-live surfaces problems while there is still time to fix them.

7. **Reconciliation validates the load was complete.** Record count comparison is the first check. Financial balance comparison (sum of open items in source = sum of open items in target) is the second check.

8. **Every cutover plan needs a cutback plan.** The cutback plan allows reverting to the legacy system if go-live reveals critical data problems. It must be tested before the production cutover.

---

## Section 7: Required Study Resources

Complete before attempting the quiz:

- **Salesforce Trailhead — Data Management**
  trailhead.salesforce.com — search "Data Management"
  Covers Data Import Wizard, Data Loader, and External IDs tested on the Certified Associate exam.

---

## Section 8: Study Checklist

- Draw the complete ETL pipeline from memory including staging area and post-load validation.
- Memorize all six data quality dimensions with a one-sentence definition for each.
- Know the difference between Data Import Wizard (50K limit, no delete) and Data Loader (millions of records, all operations).
- Understand External IDs and how they enable upsert operations.
- Review SAP migration object sequencing in Section 3.
- Understand the difference between LSMW and SAP Migration Cockpit.
- Review the mock cutover concept and why rehearsal runs are critical.
- Know the components of a cutover plan and why a cutback plan is mandatory.
- Complete Salesforce Trailhead "Data Management" module.
- Watch the Module 12 video lecture.
- Complete Lab 12.
- Post to Discussion Forum 12 by Wednesday at 11:59 PM.
- Complete Quiz 12 (10 questions).

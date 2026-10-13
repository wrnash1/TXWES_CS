# Lab Activity: Module 12 — Data Migration

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Lab Overview

This lab develops your ability to analyze source data quality, design transformation rules, sequence migration objects correctly, select appropriate migration tools, and plan a production cutover. All work is analytical and scenario-based.

**Estimated Time:** 90 minutes

**Submission:** Upload to Canvas under "Lab 12 -- Data Migration."

---

## Learning Objectives

By completing this lab you will be able to:

- Identify and categorize data quality issues across all six quality dimensions
- Design transformation rules to resolve specific data quality problems
- Sequence SAP migration objects in the correct dependency order
- Select the appropriate Salesforce migration tool for given scenarios
- Plan a production cutover within a defined time window

---

## Scenario Background

**Company:** Cascade Medical Devices

**Industry:** Medical device manufacturing and distribution

**Context:** Cascade is implementing SAP S/4HANA for financial accounting, procurement, and materials management, and Salesforce Sales Cloud for customer relationship management. They are replacing a 12-year-old Oracle EBS system and a legacy Access database that the sales team has been using independently. Go-live is scheduled in 14 weeks.

---

## Part A: Data Quality Assessment (25 points)

### A-1: Data Profiling Results

The migration team ran a data profiling analysis on Cascade's legacy Oracle EBS customer master. Here are the findings from 18,400 extracted customer records:

- 3,200 records have no contact email address
- 4,600 records have phone numbers in mixed formats (parenthetical, dashes, dots, plain 10-digit)
- 890 records appear to be duplicates of other records (same company name and address, slightly different phone)
- 2,100 records reference sales territory codes that no longer exist in the current territory structure
- 450 records have annual revenue values exceeding $500 billion (clearly data entry errors)
- 780 records have a "Last Activity Date" of more than 5 years ago with no transactions in EBS during that period
- 1,100 records have a "Customer Type" code of "ZZ" — a code that existed in the old Oracle system but does not exist in SAP or Salesforce

For each finding, identify the data quality dimension it violates and recommend a specific transformation rule or remediation action.

| Finding | Quality Dimension | Transformation Rule / Remediation |
|---|---|---|
| 3,200 records missing email | | |
| Phone numbers in mixed formats | | |
| 890 duplicate records | | |
| 2,100 records with obsolete territory codes | | |
| 450 records with revenue > $500B | | |
| 780 records with no activity in 5+ years | | |
| 1,100 records with "ZZ" customer type code | | |

### A-2: Data Quality Impact Analysis

The project manager reviews the profiling results and says: "The numbers look manageable. Let's just migrate everything as-is and let the business clean up the data in the new system after go-live."

In 100–150 words, explain why this approach is risky. What specific business process failures are likely to occur in SAP or Salesforce if the data is migrated without cleansing? Reference at least two of the specific quality issues identified above and explain the downstream ERP or CRM impact of each.

---

## Part B: Transformation Rule Design (25 points)

### B-1: Field Mapping Design

Design the field mapping from Cascade's Oracle EBS Customer Master to the target SAP and Salesforce systems. For each source field, identify the target field(s), any transformation logic required, and the target system.

| Oracle EBS Field | Sample Value | Target System | Target Field | Transformation Logic |
|---|---|---|---|---|
| CUST_NUMBER | "C-00048291" | Salesforce | | |
| CUST_NAME | "CASCADE MEDICAL DEVICES INC." | Salesforce | Account Name | |
| CUST_NAME | "CASCADE MEDICAL DEVICES INC." | SAP | Customer Master (KNA1): NAME1 | |
| PHONE_PRIMARY | "512.555.0147" | Salesforce | Phone | Normalize to (NXX) NXX-XXXX format |
| COUNTRY_CODE | "US" | SAP | Customer Master: LAND1 | |
| TERRITORY | "SW-LEGACY-04" | Salesforce | Territory (lookup) | Map to new territory structure; default to "Unassigned" if no match |
| ANNUAL_REVENUE | 580000000000 | Salesforce | AnnualRevenue | |
| STATUS | "1" | SAP | Customer Master: KTOKD (Account Group) | Map "1"=Active → "0001", "2"=Inactive → "0002", "ZZ"=Unknown → default "0001" |

### B-2: Code Mapping Table

Cascade's Oracle EBS system uses numeric codes for several fields that Salesforce and SAP use text values for. Complete the code mapping table.

| Source Field | Oracle Code | Oracle Description | Target System | Target Value |
|---|---|---|---|---|
| Customer Status | 1 | Active | Salesforce | |
| Customer Status | 2 | Inactive | Salesforce | |
| Customer Status | 3 | Prospect | Salesforce | |
| Customer Status | 9 | Deceased/Dissolved | Salesforce | |
| Payment Terms | NET30 | Net 30 days | SAP | ZN30 (SAP payment term code) |
| Payment Terms | NET60 | Net 60 days | SAP | ZN60 |
| Payment Terms | CBD | Cash Before Delivery | SAP | |
| Industry Code | MED | Medical Device | Salesforce | Account Industry |
| Industry Code | HOSP | Hospital | Salesforce | |
| Industry Code | PHARM | Pharmaceutical | Salesforce | |

---

## Part C: SAP Migration Object Sequencing (25 points)

### C-1: Dependency Sequencing

Cascade's SAP implementation team has identified the following objects to be migrated. Place them in the correct migration sequence (1 = first, highest number = last) based on SAP dependency rules. Explain the dependency that determines each object's position.

| Migration Object | Sequence Number | Dependency Explanation |
|---|---|---|
| Open vendor invoices (FI-AP open items) | | |
| G/L Account Master (chart of accounts entries) | | |
| Vendor Master Records (LFA1) | | |
| Company Code configuration | | |
| Material Master Records (MM) | | |
| Open Purchase Orders (EKKO/EKPO) | | |
| Cost Center Master Data (CO) | | |
| Plant configuration | | |

### C-2: Migration Tool Selection

For each SAP migration scenario at Cascade, select the appropriate tool (LSMW or SAP Migration Cockpit) and justify your choice.

**Scenario 1:** Cascade needs to migrate 24,000 Vendor Master records from Oracle EBS. SAP provides a standard Migration Cockpit template for Vendor Master. The data has been cleansed and is in the correct format.

**Scenario 2:** Cascade has a custom Z-table in Oracle that stores equipment maintenance contract data with a non-standard structure that does not map to any standard SAP migration template. An ABAP developer is available to build the custom mapping.

**Scenario 3:** Cascade needs to migrate 180,000 GL open line items (balance carry-forward and open items) from Oracle. SAP provides a Migration Cockpit template for GL open items. The volume is large but the structure matches the template.

---

## Part D: Salesforce Migration Tool Selection and Cutover Planning (25 points)

### D-1: Salesforce Tool Selection

For each Cascade migration requirement, identify whether to use the Data Import Wizard or Data Loader and justify your answer.

| Requirement | Tool | Justification |
|---|---|---|
| Load 18,400 Account records (cleaned and transformed) into Salesforce | | |
| Load 45,000 Contact records linked to the migrated Accounts | | |
| After go-live, delete 890 duplicate records that were accidentally loaded before deduplication was complete | | |
| A business analyst (no technical background) needs to import 3,000 new Leads from a trade show CSV file | | |
| Run a weekly automated upsert of updated Account records from the Oracle system during the 6-week parallel run period | | |

### D-2: External ID Design

Cascade's Salesforce team needs to configure External ID fields before the migration begins.

1. What is an External ID in Salesforce, and why is it required for the upsert operation?
2. What field data type should be used for the External ID field on the Account object to store Oracle's customer number (format: "C-XXXXXXXX")?
3. During the Contact migration, each Contact must be linked to the correct Account. The migration file contains Oracle's customer number (not Salesforce's Account ID, which does not exist yet). How does the External ID on Account enable this parent-child relationship to be established correctly during the Contact load?
4. What happens if the migration team loads 18,400 Account records without an External ID field, and then needs to run an incremental upsert 2 weeks later with 500 new or updated accounts?

### D-3: Cutover Plan Review

Cascade's cutover window is Friday 8:00 PM to Sunday 11:59 PM — a 52-hour window. The migration team has estimated the following migration steps:

| Step | Estimated Duration |
|---|---|
| Source system freeze and final extract from Oracle EBS | 3 hours |
| Company Code and Plant configuration verification | 1 hour |
| G/L Account Master load (1,200 accounts) | 1 hour |
| Cost Center Master load (340 cost centers) | 1 hour |
| Vendor Master load (24,000 records) | 4 hours |
| Customer Master load to SAP (24,000 records, via Migration Cockpit) | 4 hours |
| Material Master load (8,600 materials) | 5 hours |
| Open GL items load (180,000 line items) | 10 hours |
| Open Purchase Orders load (6,200 lines) | 4 hours |
| Salesforce Account and Contact load (64,000 records via Data Loader) | 3 hours |
| Automated reconciliation (record counts and financial balances) | 3 hours |
| Business spot-check and sign-off | 8 hours |
| Go/No-Go decision meeting | 1 hour |

1. Calculate the total estimated migration time.
2. Add a 15% buffer for unexpected delays. Does the total fit within the 52-hour cutover window?
3. If the automated reconciliation (step 12) reveals that 280 GL open items did not load correctly, what should happen next? Should the team proceed to go-live, fix and re-load the 280 records, or invoke the cutback plan? Explain your reasoning.
4. Why does the cutover plan include the Go/No-Go decision as a formal step rather than assuming go-live will proceed?

---

## Grading Rubric

| Section | Points | Criteria |
|---|---|---|
| A-1: Data quality assessment table | 14 | All 7 findings correctly classified with specific remediation action |
| A-2: Data quality impact analysis | 11 | 100-150 words; two specific quality issues linked to downstream impacts |
| B-1: Field mapping design | 13 | Fields correctly mapped; transformation logic specified; target system identified |
| B-2: Code mapping table | 12 | All incomplete entries filled correctly with valid target values |
| C-1: Dependency sequencing | 13 | All 8 objects correctly sequenced with valid dependency explanation |
| C-2: Migration tool selection | 12 | All 3 scenarios correctly analyzed with tool identified and justified |
| D-1: Salesforce tool selection | 10 | All 5 requirements correctly classified with valid justification |
| D-2: External ID design | 10 | All 4 questions answered correctly |
| D-3: Cutover plan review | 5 | Arithmetic correct; go/no-go reasoning sound; buffer calculation correct |
| **Total** | **100** | |

---

## Submission Instructions

1. Compile all responses into a single document.
2. Name your file: `Lab12_LastName_FirstName.pdf`
3. Upload to Canvas under "Lab 12 -- Data Migration."
4. Deadline: See course schedule in Canvas. Late submissions lose 10 points per day.

---

## Part 9 — Challenge Exercise

### Challenge 1: Full ETL Pipeline Design for a CRM-to-Salesforce Migration

A regional insurance company (1,800 employees, 42,000 customers) is replacing its legacy on-premise CRM with Salesforce Sales Cloud. The legacy system exports data as pipe-delimited text files. The following data objects must be migrated: Accounts (customers), Contacts (individual policyholders), Opportunities (active policy quotes), and Cases (open claims).

1. Design the complete ETL pipeline for this migration. For each phase (Extract, Transform, Load), specify: the tool or method used, the primary activities performed, and the output artifact produced. Include the staging environment role and explain why data should not be loaded directly from the legacy extract into Salesforce without a Transform stage.
2. The legacy system stores customer names in a single field ("FIRSTNAME LASTNAME" format). Salesforce requires separate FirstName and LastName fields on the Contact object. Design the Transform rule to split the name field. Address edge cases: customers with only one name, customers with three-part names (e.g., "Mary Jo Smith"), and customers with suffixes (e.g., "Robert Jones Jr."). For each case, specify the rule outcome.
3. The migration team must load the four objects in the correct dependency order. Explain the dependency chain (which object must load before which), and identify the External ID strategy that will allow Contact records to reference the correct Account, and Opportunity/Case records to reference the correct Contact, without requiring the team to look up Salesforce-generated IDs between each load wave.
4. After the production load, the reconciliation report shows: Accounts loaded = 42,000 (matches source), Contacts loaded = 41,847 (source had 42,000), Opportunities loaded = 8,901 (source had 9,240), Cases loaded = 3,412 (matches source). For each discrepancy, design the investigation steps the migration team should take to identify root cause and determine whether re-loading is required or whether a data quality explanation is acceptable.

### Challenge 2: SAP Data Migration Sequencing and Quality Gate Design

A manufacturing company is implementing SAP S/4HANA. The migration scope includes the following data objects: Chart of Accounts (G/L Accounts), Vendor Master, Customer Master, Material Master, Open Purchase Orders, Open Sales Orders, Open AP Vendor Invoices, Open AR Customer Invoices, and Inventory Balances. The migration manager needs to design the sequencing plan and quality gates.

1. Place all nine data objects in the correct migration sequence. For each object, identify the object(s) it depends on (its prerequisites) and state the consequence of loading it out of sequence (what error would SAP generate?).
2. Design a quality gate checklist for the Vendor Master migration. Include six specific checks that must pass before the Vendor Master load is declared successful. For each check, specify: what is being verified, the data source for verification, the acceptance criterion, and the action if the criterion is not met.
3. The project team wants to pre-migrate Inventory Balances two weeks before the production cutover to reduce the cutover window duration. A senior consultant flags this as problematic. Explain why inventory balances cannot be pre-migrated the same way historical closed invoices can be, and describe the correct approach for migrating inventory in a manufacturing environment where goods movements occur daily up to the cutover date.
4. After go-live, a controller discovers that 14 G/L accounts have incorrect opening balances. The migration team used LSMW to post balance carry-forwards. Describe the investigation process to identify which accounts are wrong, the SAP transaction to post correcting entries, and the internal control requirement that must be met before any correction is posted to production (who must approve a correction to an opening balance posting?).

### Reflection Questions

1. In Challenge 1, the name-splitting Transform rule exposed edge cases that a simple "split on space" logic cannot handle. In real migration projects, data profiling (analyzing source data before designing Transform rules) is supposed to surface these edge cases before coding begins. What profiling queries or analysis techniques would you run on the 42,000 customer name records to identify all edge case patterns before writing the Transform rules?
2. In Challenge 2, the quality gate for Vendor Master included a count reconciliation check. In a migration with 8,400 vendors, a 99.5% success rate means 42 vendors did not load. Under what business circumstances is a 99.5% load rate acceptable, and under what circumstances does every single record need to be loaded before go-live can be authorized? How should the go/no-go criteria be written to distinguish between these scenarios?

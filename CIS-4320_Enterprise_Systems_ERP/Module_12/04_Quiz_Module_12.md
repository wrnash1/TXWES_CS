# Quiz: Module 12 — Data Migration

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### Question 1

What does the Transform step in the ETL (Extract, Transform, Load) data migration process involve?

- A) Moving exported data files to physical tape drives for offline storage
- B) Cleaning, reformatting, and mapping raw source data to match the target system's data model and business rules
- C) Permanently deleting all records from the legacy system after extraction is complete
- D) Running compiler updates on the target ERP server before loading begins

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The Transform phase is where data quality work happens: Extract pulls raw data as-is from the source, and Load writes data to the target; Transform is the critical middle step that bridges the gap between the two systems' data models.
- *Why A is incorrect:* Moving files to tape drives is a backup/archival operation unrelated to the ETL transformation process.
- *Why C is incorrect:* Deleting source records after extraction is a decommissioning step that may happen after go-live; it is not part of the Transform step.
- *Why D is incorrect:* Server software updates are an infrastructure activity; they are not part of the ETL data transformation process.

---

### Question 2

Which of the following best describes the Load step in a Salesforce CRM data migration?

- A) The process of querying and extracting data from the legacy system into staging files
- B) Applying deduplication rules and field transformations to normalize the extracted data
- C) Writing the cleaned, transformed data into Salesforce using tools like Data Loader or the Data Import Wizard, and verifying record counts match expectations
- D) Running a post-migration report to compare source system totals against the new system's loaded values

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* In a Salesforce migration, the Load step uses Salesforce Data Loader (for large volumes) or the Data Import Wizard (for smaller sets) to insert or upsert records from prepared CSV files into Salesforce objects.
- *Why A is incorrect:* Querying and extracting data from the source system describes the Extract step, not Load.
- *Why B is incorrect:* Applying deduplication rules and field transformations describes the Transform step, not Load.
- *Why D is incorrect:* Running a reconciliation report comparing source and target totals is a validation check that follows the Load step; it is not the Load step itself.

---

### Question 3

A data migration team discovers that the legacy system stores customer phone numbers in five different formats: "(512) 555-1234," "512-555-1234," "5125551234," "+1 512 555 1234," and "512.555.1234." Which migration phase and action addresses this issue?

- A) Extract phase — re-query the legacy database with a filter that excludes non-standard phone formats
- B) Transform phase — apply a data cleaning rule that normalizes all phone numbers to a single standard format before loading
- C) Load phase — configure the target system to accept all five formats by loosening its field validation rules
- D) Validation phase — flag all non-standard phone records as errors and exclude them from the migration

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Data cleaning during Transform is the correct solution — a standardization rule strips non-numeric characters and reformats all values to a single standard before loading, ensuring the target system receives clean, consistent data.
- *Why A is incorrect:* Filtering out records with non-standard phone formats during Extract would lose valid customer records; the formatting issue is a data quality problem, not a validity problem.
- *Why C is incorrect:* Loosening target system validation rules accepts dirty data into the new system, perpetuating the problem and creating reporting inconsistencies downstream.
- *Why D is incorrect:* Excluding all non-standard phone records from the migration would leave the new system without phone data for a large portion of customers, which is worse than loading a standardized format.

---

### Question 4

After completing a Salesforce data migration, a project manager wants to confirm that all records were loaded successfully. The source system had 15,000 Account records. Which post-load validation step should the team perform first?

- A) Ask 10 end users to review their own customer records and report any issues they notice
- B) Run a Salesforce report counting total Account records and compare it to the expected 15,000 from the source system
- C) Delete all loaded records and re-run the load from the beginning to ensure consistency
- D) Check the Salesforce system governor limit usage dashboard to confirm no limits were exceeded

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Record count reconciliation — comparing source system count to target system count — is the baseline post-load validation check. A count mismatch is the trigger for deeper investigation.
- *Why A is incorrect:* Relying on end-user spot-checks is an unreliable, slow, and incomplete validation method; users will only notice records they actively search for, missing many errors.
- *Why C is incorrect:* Deleting and re-running a load without diagnosing and correcting the issues from the first run will produce the same errors again.
- *Why D is incorrect:* Governor limit dashboards monitor API and processing resource usage; they do not validate data completeness or record-count accuracy.

---

### Question 5

A Salesforce administrator uses the Data Import Wizard to load 2,000 new Contact records, but the wizard reports 47 failures. The error messages show "REQUIRED_FIELD_MISSING: Email." What is the correct corrective action?

- A) Lower the Email field's required setting in the Contact object to make it optional, then re-run the import
- B) Return to the source data file, populate the Email field for the 47 failed records with valid email addresses, and re-import only those 47 records
- C) Ignore the 47 errors since 1,953 records loaded successfully and the failure rate is below 5%
- D) Delete all 1,953 successfully loaded records and start the entire import over with the corrected file

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Data Loader and Data Import Wizard generate error logs with row-level details for each failure. The fix is to correct the source data and re-import the failed subset, not re-process records that already loaded correctly.
- *Why A is incorrect:* Removing the required field constraint to accommodate missing data sacrifices data integrity for the entire organization going forward; it does not fix the root problem of missing email addresses.
- *Why C is incorrect:* Accepting data failures as acceptable loss leaves 47 customer contacts without email addresses in the new system, impairing marketing, service, and communication workflows.
- *Why D is incorrect:* Deleting all 1,953 successfully loaded records and re-running the full import is unnecessarily destructive, time-consuming, and risks introducing errors into records that were already correct.

---

### Question 6

An SAP implementation team is migrating data from a legacy system into SAP S/4HANA. They plan to migrate vendor invoices (open AP items) on the first day. A technical consultant flags this as a sequencing error. Which object must exist in SAP before vendor open items can be migrated, and why?

- A) The company code configuration must exist because open items are legally assigned to a company code, which must be configured before any financial data references it
- B) The chart of accounts must be migrated first so that invoice line items have G/L accounts to reference
- C) Both vendor master records and G/L accounts must exist before vendor open items can be migrated, because an open item references the vendor (via the vendor master) and posts to a G/L account
- D) The purchase orders must be migrated first because every open invoice must reference a matching open PO in SAP

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Vendor open items (FI-AP open items) are dependent on two master data objects: the Vendor Master (the item belongs to a specific vendor) and the G/L Account Master (the item posts to a reconciliation account). If either master data object does not exist, the migration load fails with a foreign key validation error.
- *Why A is incorrect:* Company code configuration is also a prerequisite, but it is an organizational structure configured in SPRO before data migration begins — it is not itself a migrated data object. The more precise answer identifies the master data dependencies.
- *Why B is incorrect:* The chart of accounts must exist, but the more specific dependency is the individual G/L account master records that vendor invoices reference. The chart of accounts structure is configured before migration, not migrated as data.
- *Why D is incorrect:* Open FI-AP items can be migrated as standalone balance carry-forward items — they do not require a matching purchase order. Historical open items often have no PO reference.

---

### Question 7

Which Salesforce migration tool supports the delete and hard delete operations, and why is the distinction between delete and hard delete important in a data migration project?

- A) Data Import Wizard — it supports both delete operations through the advanced options menu
- B) Data Loader — it supports both delete (moves records to Recycle Bin) and hard delete (permanently removes records), which matters because records in the Recycle Bin count against storage limits
- C) Both tools support delete operations, but only Data Loader supports hard delete on records over 5 years old
- D) Neither tool supports delete — records can only be deleted manually through the Salesforce user interface

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Data Loader is the only Salesforce tool that supports delete and hard delete operations. Standard delete moves records to the Recycle Bin (still counts toward storage). Hard delete permanently removes records and immediately frees storage — important in large migration projects where test data loads must be cleaned up before the production migration runs.
- *Why A is incorrect:* Data Import Wizard does not support delete or hard delete operations. It is limited to insert, update, and upsert.
- *Why C is incorrect:* There is no age-based restriction on hard delete. Data Loader supports hard delete for any record, and Data Import Wizard does not support delete at all.
- *Why D is incorrect:* Data Loader explicitly supports delete operations. The manual UI delete is not the only option.

---

### Question 8

A project team runs their first mock cutover and discovers that the full migration takes 68 hours — but their production cutover window is only 60 hours (Friday 8 PM to Monday 8 AM). What should the team do before the next mock cutover rehearsal?

- A) Accept the 68-hour migration time and plan to miss the Monday 8 AM deadline, notifying users that go-live will be delayed by 8 hours
- B) Analyze the migration steps to identify which ones can be parallelized, optimized, or reduced in scope to bring the total within the 60-hour window
- C) Negotiate with the business to compress the business spot-check phase from 8 hours to zero hours, removing it from the cutover plan
- D) Switch from SAP Migration Cockpit to LSMW for all objects, which runs significantly faster for large datasets

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* When a mock cutover reveals a timing problem, the correct response is to analyze the plan and find optimizations: running some steps in parallel, tuning the migration programs, reducing reconciliation scope, or pre-migrating historical data before the cutover window. The mock cutover exists precisely to surface these problems before go-live.
- *Why A is incorrect:* Accepting a missed deadline and notifying users of an 8-hour delay after the migration has started is not a professional project management approach. The timing problem must be resolved before the production cutover.
- *Why C is incorrect:* Eliminating the business spot-check phase removes a critical data quality gate. If migrated data has errors that only business users would catch, removing the review phase guarantees those errors survive into the production go-live.
- *Why D is incorrect:* LSMW and Migration Cockpit have different strengths but are not simply interchangeable by speed. Switching tools without analysis may introduce new problems. The correct approach is to optimize the existing plan first.

---

### Question 9

During a data migration, the team identifies 4,200 duplicate customer records in the source system. The project manager proposes migrating all 4,200 duplicates into Salesforce and letting the sales team merge them manually after go-live. Which data quality dimension does this problem violate, and what is the risk of the project manager's proposed approach?

- A) Completeness — the duplicates represent missing data that should be filled in before migration; merging them manually is the correct approach
- B) Uniqueness — each real-world customer should appear exactly once; migrating all duplicates creates 4,200 bad records in the new system that will impair reporting, automation, and user experience if not immediately addressed
- C) Validity — duplicate records fail the target system's validation rules and cannot be loaded anyway
- D) Accuracy — the duplicate records contain incorrect data that must be corrected before loading

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Uniqueness is the data quality dimension that requires each real-world entity to appear exactly once. Migrating duplicates into the new system exports the problem — now sales reps will find two "Acme Corp" accounts, automation rules may trigger twice, and reports will double-count customers. Deduplication must happen in the Transform phase, not post-migration.
- *Why A is incorrect:* Completeness refers to missing required fields, not to the presence of duplicate records. Duplicate records do not represent missing data — they represent excess data representing the same entity.
- *Why C is incorrect:* Salesforce does not have a built-in deduplication rule that blocks duplicate loads as a validation error. Duplicates can be loaded — the system allows them, which is exactly what makes the project manager's proposal possible and problematic.
- *Why D is incorrect:* Accuracy refers to factual correctness of field values (e.g., wrong revenue amount). Duplicates are not inaccurate — they are redundant representations of the same entity, which is a uniqueness problem.

---

### Question 10

In the SAP Migration Cockpit, a migration specialist downloads the standard template for Vendor Master migration, populates it with 8,400 vendor records, and uploads it. The migration program runs and reports 340 errors. The error log shows: "Required field KTOKD (Account Group) is blank for 340 records." What does this tell the specialist, and what is the correct resolution?

- A) The KTOKD field was removed in the latest S/4HANA update and must be removed from the template before re-running
- B) The 340 vendor records are missing their Account Group value in the source data; the specialist must populate this field with the correct account group code before re-running the migration for those records
- C) The Migration Cockpit template is corrupted and must be re-downloaded from SAP; the data is correct
- D) The error means the migration succeeded but the 340 records are in a pending approval status waiting for a manager to assign an account group

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* KTOKD (Account Group) is a required field in SAP's Vendor Master — it determines the screen layout, number range, and reconciliation account assignment. If it is blank in the migration file, those records cannot be created. The data quality issue must be resolved in the source: identify the correct account group for each of the 340 vendors, update the migration file, and re-run only the failed records.
- *Why A is incorrect:* KTOKD is a core SAP Vendor Master field that has not been removed in S/4HANA. Account Group is required in all SAP versions. The template is correct.
- *Why C is incorrect:* Template corruption is extremely rare and would typically cause all records to fail, not a specific subset. A subset failure with a consistent error message indicates a data quality issue in the source data, not a template problem.
- *Why D is incorrect:* SAP migration programs do not create records in a pending approval status waiting for field completion after the fact. A required field failure means the record was rejected and not created. There is no pending state — the records simply do not exist in SAP yet.

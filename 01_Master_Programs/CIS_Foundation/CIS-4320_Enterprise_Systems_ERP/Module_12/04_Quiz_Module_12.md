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

---

### Question 11

(5 points)

A data migration analyst is preparing a legacy CRM file containing 22,000 Account records. The source system stores the country field as a full country name (e.g., "United States") but Salesforce requires a two-letter ISO country code (e.g., "US"). In which ETL phase should this conversion be applied, and what type of transformation is it?

- A) Extract phase — the source system query should be rewritten to output ISO codes directly
- B) Load phase — configure the Salesforce Data Loader to auto-convert country names to codes during import
- C) Transform phase — apply a lookup/mapping table that converts full country names to ISO codes before the file is loaded
- D) Validation phase — flag country name records as errors and exclude them from the load

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* Converting country names to ISO codes is a value mapping transformation — one of the most common Transform operations. A reference lookup table maps each full country name to its two-letter code. This must happen in the Transform phase before loading so that Salesforce receives the correct standardized values.
  - *Why A is incorrect:* Rewriting the source query to output ISO codes assumes the legacy system has that conversion capability built in — most do not. Even if it were possible, the conversion logic belongs in the ETL Transform layer, not embedded in the source extraction query.
  - *Why B is incorrect:* Salesforce Data Loader does not perform value mapping transformations during import. It loads data as provided. Asking the Load tool to convert data that has not been transformed will result in load failures or incorrect values.
  - *Why D is incorrect:* Country name records are valid — they simply use a different format. Excluding them from the migration would remove 22,000 legitimate account records. The correct action is transformation, not exclusion.

---

### Question 12

(5 points)

In a Salesforce data migration, an External ID field is created on the Account object containing the legacy system's account number. After migration, a second wave of data (Contacts) needs to be linked to the correct Account records. How does the External ID enable this relationship?

- A) The External ID is used as a substitute for the Salesforce Record ID during upsert operations — Data Loader matches on the External ID value to find the parent Account without needing the Salesforce-generated 18-digit ID
- B) The External ID automatically imports Contact records and links them to Accounts based on alphabetical name matching
- C) The External ID is required by Salesforce to validate that all records were loaded — it is not used for relationship linking
- D) The External ID replaces the Account Name field to uniquely identify each Account record in reports

- **Correct Answer:** A

- **Distractor Analysis:**
  - *Why A is correct:* External IDs enable upsert operations and relationship resolution across migration waves. When loading Contact records, the migration file contains the legacy account number in a relationship field. Data Loader matches this value against the External ID on the Account object to find the correct Salesforce Account ID and create the Contact-Account relationship — without requiring the migration team to look up each Salesforce record ID manually.
  - *Why B is incorrect:* Salesforce does not perform automatic name-matching to create relationships. Name-based matching is unreliable (many companies share similar names). External IDs provide exact, deterministic matching based on the legacy system's unique identifier.
  - *Why C is incorrect:* External ID fields are not required for validation purposes. They are optional custom fields that serve a specific technical purpose: enabling upsert matching and cross-object relationship resolution during bulk data operations.
  - *Why D is incorrect:* External ID does not replace the Account Name field in reports. It is a behind-the-scenes technical field used during data operations. Account Name remains the standard display field for reporting and user interface purposes.

---

### Question 13

(5 points)

A healthcare company is migrating patient billing history (5.2 million records) from a legacy system into SAP S/4HANA. The data migration manager proposes loading all 5.2 million records during the production cutover weekend. A senior consultant recommends a different approach. What is the most likely recommendation, and why?

- A) Load all 5.2 million records during cutover — there is no alternative since all records must be available at go-live
- B) Pre-migrate historical records (closed/paid invoices older than a defined cutoff date) before the cutover weekend, and migrate only open items and recent history during the actual cutover window to reduce go-live risk and duration
- C) Defer all historical billing records to a data warehouse and exclude them from SAP entirely
- D) Migrate the records in alphabetical order by patient last name to reduce load time

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Pre-migrating historical (closed) records before the cutover weekend is a standard technique to reduce cutover duration and risk. Historical closed invoices do not change in the legacy system after a cutoff date — they can be safely loaded days or weeks early. Only open items (active balances) need to be migrated during the live cutover window, dramatically shrinking the cutover duration.
  - *Why A is incorrect:* Loading 5.2 million records during a cutover weekend is likely to exceed the available window and increase risk. Modern migration projects use pre-migration of static historical data as a best practice to keep the live cutover window manageable.
  - *Why C is incorrect:* Deferring all historical billing records to a data warehouse may be valid for very old archived data, but recent billing history typically must be accessible in the primary ERP system for operational use (dispute resolution, collections, audits).
  - *Why D is incorrect:* Loading records in alphabetical order has no bearing on migration duration or risk. Database load performance is determined by batch size, index handling, and parallelization — not alphabetical sequence.

---

### Question 14

(5 points)

After a Salesforce migration, the business reports that several Opportunity records are missing their related Account. Investigation reveals the migration file had the Account External ID column blank for those Opportunities. Which data quality dimension was violated, and what should the migration team do to fix the affected Opportunity records?

- A) Accuracy — the Account names were spelled incorrectly; the fix is to correct the spelling and re-run the import
- B) Completeness — required relationship data (Account External ID) was missing in the migration file; the fix is to populate the Account External ID for the affected Opportunities in the source file and use Data Loader upsert to update the records in Salesforce
- C) Timeliness — the Account records were loaded after the Opportunity records; the fix is to re-run the migration in the correct order
- D) Consistency — the Account External IDs used different formats across the file; the fix is to standardize formatting and reload

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Completeness is the dimension requiring all required fields and relationships to be present. A blank Account External ID means the parent relationship data was missing from the source file. The fix is to populate the missing values (go back to the legacy system to retrieve the correct account IDs), update the migration file, and run a Data Loader upsert on the affected Opportunity records to set the AccountId.
  - *Why A is incorrect:* Accuracy refers to factual correctness of data values (e.g., wrong dollar amount, incorrect date). A missing relationship link is not an accuracy problem — the field is empty, not wrong.
  - *Why C is incorrect:* Timeliness refers to whether data is current and up-to-date. While loading order matters (Accounts before Opportunities), the problem described is specifically a missing field value, not a sequencing timing issue — the Account records exist in Salesforce, they just were not linked.
  - *Why D is incorrect:* Consistency refers to data using the same format and definition across the system. If the column was blank (not present in different formats), this is a completeness issue, not a consistency issue.

---

### Question 15

(5 points)

The cutover plan for an SAP go-live includes a cutback (rollback) plan. At what point during a production cutover should the project team execute the cutback plan, and what does executing a cutback require?

- A) The cutback plan is executed after go-live if users report performance problems during the first week
- B) The cutback plan is executed during the cutover window if a defined go/no-go decision point is reached and critical data quality or system stability conditions are not met — it requires reverting to the legacy system and invalidating all data loaded into SAP
- C) The cutback plan is executed at the end of every mock cutover rehearsal to reset the environment for the next rehearsal
- D) The cutback plan is executed automatically by SAP if the migration program detects more than a 5% error rate

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The cutback plan is a pre-defined contingency that defines the conditions under which the go-live will be aborted and the legacy system will remain operational. The decision point is built into the cutover plan — if critical validation checks fail before a defined deadline during the cutover window, the team executes the cutback. This requires stopping all SAP activity, notifying stakeholders, reverting legacy system access, and planning a remediation cycle before the next attempt.
  - *Why A is incorrect:* By the time users are live and reporting performance problems, a full cutback is typically not feasible — data has been created in the new system, users have processed transactions. Cutback is a pre-go-live decision, not a post-go-live response.
  - *Why C is incorrect:* Mock cutover environment resets are a technical activity (database restore to clean state) separate from the cutback plan. The cutback plan is specifically for production go-live scenarios — it is not a rehearsal procedure.
  - *Why D is incorrect:* SAP does not automatically execute a rollback based on error rates. The cutback decision is a human project management decision based on pre-defined criteria assessed at specific checkpoints during the live cutover window.

---

### Question 16

(5 points)

A data migration team is preparing to load G/L open items (balance carry-forwards) into SAP S/4HANA. The migration date is December 31 (fiscal year-end). The team loads opening balances using LSMW with document type "SA" and posting date January 1. After the load, the controller runs a trial balance and finds the total of all account balances does not equal zero (the balance sheet does not balance). What is the most likely cause?

- A) LSMW does not support G/L balance migration — the Migration Cockpit must be used instead
- B) One or more migration journal entries do not balance (total debits do not equal total credits), or a migration posting was made to a profit-and-loss account that should only receive balance-sheet carry-forward entries
- C) The posting date of January 1 is invalid — balance carry-forwards must be posted on December 31
- D) The trial balance report requires a 24-hour delay after migration before it reflects the correct balances

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* In SAP, every FI document must balance (total debits = total credits). If a migration document was built incorrectly — a debit without a matching credit, or an entry to a P&L account that should only carry forward balance sheet positions — the resulting account balances will not reconcile. The controller's trial balance imbalance is a symptom of either an unbalanced migration document or incorrect account assignments in the migration file.
  - *Why A is incorrect:* LSMW does support G/L balance migration (it is one of its common use cases). The Migration Cockpit is an alternative, not a requirement. Tool selection is not the cause of a trial balance imbalance.
  - *Why C is incorrect:* Opening balances for the new fiscal year are typically posted on January 1 (or the first day of the new fiscal year). Posting on January 1 is standard practice for balance carry-forwards. The posting date is not the source of the imbalance.
  - *Why D is incorrect:* SAP G/L balances are updated in real time — there is no delay between posting and reporting. The trial balance immediately reflects all posted documents.

---

### Question 17

(5 points)

A Salesforce administrator is testing a data migration by loading 500 Account records into a Full Sandbox. After verifying the results, the administrator needs to delete all 500 test records before loading the production data. Which tool and operation should the administrator use to permanently remove these records and free storage?

- A) Data Import Wizard — Delete operation
- B) Data Loader — Hard Delete operation
- C) Salesforce Setup — Mass Delete Records wizard
- D) SOQL query in Developer Console — DELETE statement

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Data Loader supports the Hard Delete operation, which permanently removes records from Salesforce without sending them to the Recycle Bin. This immediately frees storage — important in a sandbox where storage is limited and test data needs to be fully purged before the production migration load.
  - *Why A is incorrect:* Data Import Wizard does not support delete or hard delete operations. It is limited to insert, update, and upsert. The administrator cannot use Data Import Wizard for bulk record deletion.
  - *Why C is incorrect:* The Mass Delete Records wizard in Salesforce Setup supports deleting records of certain object types, but it sends records to the Recycle Bin (not hard delete) and is limited to specific standard objects. It does not provide the bulk programmatic control needed for migration cleanup.
  - *Why D is incorrect:* SOQL is a query language — it uses SELECT statements to read data. DML (Data Manipulation Language) in Apex uses DELETE, but a SOQL query itself does not delete records. The Developer Console anonymous Apex can delete records, but Data Loader is the purpose-built tool for this scenario.

---

### Question 18

(5 points)

During the data profiling phase of an SAP migration project, the team discovers that 12% of vendor records in the legacy system have duplicate entries (same vendor name and address but different legacy IDs). The team lead suggests loading all duplicates into SAP and merging them later. What is the primary risk of this approach?

- A) SAP will automatically merge duplicate vendor records, making post-migration cleanup unnecessary
- B) Loading duplicate vendors may result in split payment runs — different invoices for the same vendor may post to different vendor accounts, causing payment discrepancies and vendor reconciliation problems
- C) Duplicate vendor records will fail SAP's required uniqueness validation and will not load
- D) The only risk is report aesthetics — duplicate vendors appear in reports but do not affect financial processing

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* In SAP FI-AP, each vendor invoice and payment is associated with a specific Vendor Master record. If the same real-world vendor has two SAP vendor records, payments and invoices can be split across both records. This makes vendor account reconciliation impossible, may trigger duplicate payment risk (paying the same invoice twice to different vendor accounts), and violates the data integrity principle that one vendor = one master record.
  - *Why A is incorrect:* SAP does not automatically merge vendor records. Vendor deduplication and merging is a manual process. Duplicate records will coexist in SAP indefinitely unless a deliberate cleanup is performed.
  - *Why C is incorrect:* SAP does not prevent loading vendors with similar names and addresses — there is no built-in deduplication validation at the database level for vendor master records. The duplicates will load successfully, which is exactly why they must be resolved before migration.
  - *Why D is incorrect:* Duplicate vendor records have direct operational consequences beyond report aesthetics: split payment runs, reconciliation failures, duplicate payment risk, and incorrect aging report balances. These are financial accuracy problems, not cosmetic ones.

---

### Question 19

(5 points)

A project team completes their third and final mock cutover. Results show: total migration duration = 54 hours (within the 60-hour window), error rate = 0.3% (below the 1% threshold), and business spot-check sign-off = obtained from all three business owners. What is the appropriate project management decision at this point?

- A) Run a fourth mock cutover to achieve a 0% error rate before proceeding to production
- B) Issue the go-live green light — all defined go/no-go criteria have been met, and the team should proceed to the production cutover
- C) Delay go-live by two weeks to allow additional user training since some users struggled with the spot-check process
- D) Escalate to the steering committee for a final approval vote before proceeding, even though all criteria are met

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* When all predefined go/no-go criteria are satisfied — duration within window, error rate below threshold, and business sign-off obtained — the correct project management decision is to proceed. Mock cutovers exist to reach this point. Continuing to rehearse after all criteria are met adds cost and delay with no additional risk reduction.
  - *Why A is incorrect:* A 0.3% error rate is below the defined 1% threshold, which means it meets the criterion. Requiring a 0% error rate is an unrealistic standard that no migration achieves. Pursuing perfection beyond the defined acceptance criteria is scope creep.
  - *Why C is incorrect:* User training issues discovered during spot-check should be addressed through accelerated training before go-live, not by delaying the entire cutover. Training struggles do not invalidate data migration quality or system readiness.
  - *Why D is incorrect:* If predefined go/no-go criteria were established with steering committee input, additional steering committee votes are not required when criteria are met. Requiring additional approvals after criteria are satisfied introduces unnecessary bureaucracy and delays.

---

### Question 20

(5 points)

After a production go-live, the migration team runs a post-migration reconciliation report. The report compares source system totals to target system totals for Customer AR open balances. The source total is $4,182,300 and the SAP total is $4,094,700 — a discrepancy of $87,600. What is the correct immediate response?

- A) Accept the $87,600 discrepancy as rounding error — differences under 5% are normal in ERP migrations
- B) Generate a record-level comparison to identify which specific customer account balances differ between the source and SAP, then investigate whether the missing $87,600 represents records that failed to load, records that loaded with incorrect amounts, or records excluded during the Transform phase
- C) Post a manual journal entry in SAP to add $87,600 to AR to force the balances to agree, then close the migration project
- D) Re-run the full AR migration from scratch since the reconciliation failed

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* A $87,600 discrepancy in AR opening balances must be investigated at the record level to determine root cause before any corrective action is taken. The root cause could be: records that failed validation and were excluded, records that loaded with truncated amounts, currency conversion errors, or records that were in the source extract but filtered out in Transform. The investigation drives the correct fix — whether that is a targeted re-load, a correction posting, or a Transform rule adjustment.
  - *Why A is incorrect:* There is no standard "under 5% is acceptable" rule in financial data migration. AR opening balances are the basis for customer billing and collections — a $87,600 discrepancy means real customer balances are wrong, which has immediate business and audit consequences.
  - *Why C is incorrect:* Posting a manual journal entry to force agreement without understanding the root cause masks the problem. The specific customer accounts with incorrect balances remain wrong — the manual entry only affects aggregate totals, not individual customer ledger accuracy.
  - *Why D is incorrect:* Re-running the full migration without diagnosing the root cause will reproduce the same discrepancy. Additionally, if any transactions have already been posted in SAP against the migrated AR balances, a full re-run would create data conflicts.

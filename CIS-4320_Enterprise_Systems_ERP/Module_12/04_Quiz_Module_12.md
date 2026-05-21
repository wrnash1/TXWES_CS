# Quiz: Module 12 - Data Migration

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

What does the Transform step in the ETL (Extract, Transform, Load) data migration process involve?

* A) Moving exported data files to physical tape drives for offline storage
* B) Cleaning, reformatting, and mapping raw source data to match the target system's data model and business rules
* C) Permanently deleting all records from the legacy system after extraction is complete
* D) Running compiler updates on the target ERP server before loading begins

* **Correct Answer:** B) Transform adjusts data structures — splitting combined name fields, standardizing date formats, resolving duplicates, and mapping code values — to match the target system's schema.
* **Distractor Analysis:**
  * *Why B is correct:* The Transform phase is where the data quality work happens: Extract pulls raw data as-is from the source, and Load writes data to the target; Transform is the critical middle step that bridges the gap between the two systems' data models.
  * *Why A is incorrect:* Moving files to tape drives is a backup/archival operation unrelated to the ETL transformation process.
  * *Why C is incorrect:* Deleting source records after extraction is a decommissioning step that may happen after go-live; it is not part of the Transform step.
  * *Why D is incorrect:* Server software updates are an infrastructure activity; they are not part of the ETL data transformation process.

---

### Question 2

Which of the following best describes the **Load (ETL)** step in a Salesforce CRM data migration?

* A) The process of querying and extracting data from the legacy system into staging files
* B) Applying deduplication rules and field transformations to normalize the extracted data
* C) Writing the cleaned, transformed data into Salesforce using tools like Data Loader or the Data Import Wizard, and verifying record counts match expectations
* D) Running a post-migration report to compare source system totals against the new system's loaded values

* **Correct Answer:** C) The Load step writes the transformed data into the target system and includes verification that all expected records were created successfully.
* **Distractor Analysis:**
  * *Why C is correct:* In a Salesforce migration, the Load step uses Salesforce Data Loader (for large volumes) or the Data Import Wizard (for smaller sets) to insert or upsert records from prepared CSV files into Salesforce objects.
  * *Why A is incorrect:* Querying and extracting data from the source system describes the Extract step, not Load.
  * *Why B is incorrect:* Applying deduplication rules and field transformations describes the Transform step, not Load.
  * *Why D is incorrect:* Running a reconciliation report comparing source and target totals is a validation check that follows the Load step; it is not the Load step itself.

---

### Question 3

A data migration team discovers that the legacy system stores customer phone numbers in five different formats: "(512) 555-1234," "512-555-1234," "5125551234," "+1 512 555 1234," and "512.555.1234." Which migration phase and action addresses this issue?

* A) Extract phase — re-query the legacy database with a filter that excludes non-standard phone formats
* B) Transform phase — apply a data cleaning rule that normalizes all phone numbers to a single standard format before loading
* C) Load phase — configure the target system to accept all five formats by loosening its field validation rules
* D) Validation phase — flag all non-standard phone records as errors and exclude them from the migration

* **Correct Answer:** B) The Transform phase is where data cleaning rules normalize inconsistent values to a target standard format before the data is loaded into the new system.
* **Distractor Analysis:**
  * *Why B is correct:* Data cleaning during Transform is the correct solution — a standardization rule strips non-numeric characters and reformats all values to "(NXX) NXX-XXXX" before loading, ensuring the target system receives clean, consistent data.
  * *Why A is incorrect:* Filtering out records with non-standard phone formats during Extract would lose valid customer records; the formatting issue is a data quality problem, not a validity problem.
  * *Why C is incorrect:* Loosening target system validation rules accepts dirty data into the new system, perpetuating the problem and creating reporting inconsistencies downstream.
  * *Why D is incorrect:* Excluding all non-standard phone records from the migration would leave the new system without phone data for a large portion of customers, which is worse than loading a standardized format.

---

### Question 4

After completing a Salesforce data migration, a project manager wants to confirm that all records were loaded successfully. The source system had 15,000 Account records. Which post-load validation step should the team perform first?

* A) Ask 10 end users to review their own customer records and report any issues they notice
* B) Run a Salesforce report counting total Account records and compare it to the expected 15,000 from the source system
* C) Delete all loaded records and re-run the load from the beginning to ensure consistency
* D) Check the Salesforce system governor limit usage dashboard to confirm no limits were exceeded

* **Correct Answer:** B) A record count reconciliation report — comparing source system count (15,000) to target system count — is the first and most fundamental post-load validation step.
* **Distractor Analysis:**
  * *Why B is correct:* Record count matching is the baseline validation check. If 14,850 records loaded successfully and 150 failed, the error log from Data Loader will identify which records need reprocessing. A count mismatch is the trigger for deeper investigation.
  * *Why A is incorrect:* Relying on end-user spot-checks is an unreliable, slow, and incomplete validation method; users will only notice records they actively search for, missing many errors.
  * *Why C is incorrect:* Deleting and re-running a load without diagnosing and correcting the issues from the first run will produce the same errors again; this wastes time and risks data corruption.
  * *Why D is incorrect:* Governor limit dashboards monitor API and processing resource usage; they do not validate data completeness or record-count accuracy.

---

### Question 5

A Salesforce administrator uses the Data Import Wizard to load 2,000 new Contact records, but the wizard reports 47 failures. The error messages show "REQUIRED_FIELD_MISSING: Email." What is the correct corrective action?

* A) Lower the Email field's required setting in the Contact object to make it optional, then re-run the import
* B) Return to the source data file, populate the Email field for the 47 failed records with valid email addresses, and re-import only those 47 records
* C) Ignore the 47 errors since 1,953 records loaded successfully and the failure rate is below 5%
* D) Delete all 1,953 successfully loaded records and start the entire import over with the corrected file

* **Correct Answer:** B) The correct action is to fix the data quality issue in the source file — add valid email values for the 47 records — and re-import only the failed records using their unique external IDs to avoid duplicating the 1,953 that already loaded.
* **Distractor Analysis:**
  * *Why B is correct:* Data Loader and Data Import Wizard generate error logs with row-level details for each failure. The fix is to correct the source data and re-import the failed subset, not re-process records that already loaded correctly.
  * *Why A is incorrect:* Removing the required field constraint to accommodate missing data sacrifices data integrity for the entire organization going forward; it does not fix the root problem of missing email addresses.
  * *Why C is incorrect:* Accepting data failures as "acceptable loss" leaves 47 customer contacts without email addresses in the new system, impairing marketing, service, and communication workflows that depend on email.
  * *Why D is incorrect:* Deleting all 1,953 successfully loaded records and re-running the full import is unnecessarily destructive, time-consuming, and risks introducing errors into records that were already correct.

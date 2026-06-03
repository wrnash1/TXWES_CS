# Lab Activity: Module 12 — Database Normalization for Business Analysts

## Course: CIS-3312 Systems Analysis and Design

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** IIBA ECBA

---

## Lab Overview

In this lab you will practice the complete normalization workflow that a business analyst applies during requirements analysis. You will start with a flat, unnormalized data set provided by a fictional stakeholder, identify functional dependencies, and decompose the data through 1NF, 2NF, and 3NF. You will then document a denormalization decision using a standard BA format.

**Estimated time:** 75–90 minutes

**Deliverable:** Submit your completed worksheet as a single PDF or Word document to the course LMS.

---

## Scenario Background

Rampart Regional Hospital is replacing its paper-based patient appointment system with a new electronic scheduling application. The IT director has handed you a spreadsheet that the front desk staff currently use to track appointments. Your job is to analyze this data, normalize it, and produce a clean logical data model that the development team can use as a starting point for the new database schema.

---

## Source Data — Appointments Spreadsheet

The following table represents a sample of rows from the current spreadsheet. Study it carefully before beginning the exercises.

| ApptID | PatientID | PatientName | PatientPhone | PatientInsuranceID | InsuranceName | ProviderID | ProviderName | ProviderSpecialty | ClinicID | ClinicName | ClinicCity | ApptDate | ApptTime | DiagnosisCode | DiagnosisDesc | CopayAmount |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1001 | P-201 | Maria Santos | 817-555-0101 | INS-44 | BlueCross | DR-09 | Dr. Reyes | Cardiology | C-3 | Westside Clinic | Fort Worth | 2026-03-10 | 09:00 | I10 | Hypertension | 30.00 |
| 1002 | P-201 | Maria Santos | 817-555-0101 | INS-44 | BlueCross | DR-12 | Dr. Patel | Neurology | C-1 | Main Campus | Fort Worth | 2026-03-18 | 14:00 | G43 | Migraine | 30.00 |
| 1003 | P-305 | James Okafor | 817-555-0202 | INS-67 | Aetna | DR-09 | Dr. Reyes | Cardiology | C-3 | Westside Clinic | Fort Worth | 2026-03-20 | 10:30 | I25 | Coronary Artery Disease | 45.00 |
| 1004 | P-412 | Linda Chu | 817-555-0303 | INS-44 | BlueCross | DR-07 | Dr. Obi | Orthopedics | C-2 | North Campus | Keller | 2026-03-22 | 08:00 | M54 | Back Pain | 30.00 |

---

## Part 1 — Identify Functional Dependencies (20 points)

### Instructions

Review the Appointments spreadsheet. For each functional dependency listed below, mark it as Valid or Invalid and briefly explain your reasoning. Then add three additional functional dependencies you identify from the data.

### Provided Dependencies to Evaluate

1. ApptID → PatientID
2. PatientID → PatientName
3. PatientID → ProviderID
4. ProviderID → ProviderSpecialty
5. ClinicID → ClinicCity
6. (ApptID, PatientID) → ApptDate
7. InsuranceName → PatientInsuranceID
8. DiagnosisCode → DiagnosisDesc
9. ApptID → CopayAmount
10. ProviderID → ClinicID

### Your Additional Dependencies

Identify at least three functional dependencies not listed above. Write them using the A → B notation and explain each one.

---

## Part 2 — First Normal Form (15 points)

### Instructions

Examine the Appointments spreadsheet for any 1NF violations. Answer the following questions.

### Part 2A — Violation Assessment

Does the Appointments table contain any multi-valued attributes or repeating column groups? List each violation you find, or state "No 1NF violations found" if the table is already in 1NF.

### Part 2B — Revised Structure

Suppose the hospital wants to track multiple phone numbers per patient (home, mobile, work). Describe how you would modify the table structure to accommodate this requirement while maintaining 1NF compliance. Write out the new table definition(s) with column names and identify the primary key.

### Part 2C — Primary Key Identification

Identify the primary key for the original Appointments table as given. Justify your answer.

---

## Part 3 — Second Normal Form (25 points)

### Instructions

Assume the primary key for the Appointments table is ApptID (a single-column key). With that assumption, determine whether the table is in 2NF and explain your reasoning.

Then answer the following scenario modification:

### Part 3A — Composite Key Scenario

The hospital decides that ApptID alone is not sufficient — they want to use (PatientID, ApptDate, ApptTime) as a composite primary key instead. Under this composite key, identify all partial dependencies in the table. List each one using the format:

AttributeName → partial key component (not the full composite key)

### Part 3B — Decomposed Tables

Decompose the table to reach 2NF under the composite key (PatientID, ApptDate, ApptTime). Write out each resulting table with its columns and primary key. Identify foreign keys where applicable.

### Part 3C — Justification

For each table you created, write one sentence explaining why the attributes in that table belong together from a business perspective.

---

## Part 4 — Third Normal Form (25 points)

### Instructions

Return to using ApptID as the single primary key. The table is already in 2NF under this assumption.

### Part 4A — Transitive Dependency Identification

Identify all transitive dependencies in the Appointments table. For each one, write out the full chain:

ApptID → [intermediate attribute] → [dependent attribute]

### Part 4B — Full 3NF Decomposition

Decompose the Appointments table completely to 3NF. Present your final result as a list of normalized tables, each with:

- Table name
- Column list
- Primary key (underlined or marked with PK)
- Foreign keys (marked with FK)

You should arrive at approximately five to seven tables. If you have more or fewer, briefly explain your reasoning.

### Part 4C — Referential Integrity Check

Draw or describe (in text) how foreign keys connect your normalized tables. Confirm that no orphaned foreign key values exist in the sample data.

---

## Part 5 — Denormalization Decision (15 points)

### Scenario

The hospital's reporting team informs you that their most frequently run query joins the Appointments, Providers, Clinics, and Patients tables to produce a daily appointment roster. This query runs thousands of times per day and is creating performance problems.

The DBA proposes storing ProviderName, ProviderSpecialty, ClinicName, and PatientName directly on the Appointments table even though this violates 3NF.

### Part 5A — Trade-Off Analysis

Create a two-column table listing the pros and cons of accepting this denormalization.

### Part 5B — BA Decision Document

Write a short denormalization decision document (150–200 words) in the following format:

- **Proposed change:** Describe the redundancy being introduced.
- **Business justification:** Explain why performance matters here.
- **Risks accepted:** List the anomaly risks this introduces.
- **Mitigation:** Describe how the application or process will manage consistency.
- **Stakeholder approval:** Name the roles that should sign off (you may use fictional names).

---

## Submission Checklist

Before submitting, verify that your document includes:

- Part 1: Ten evaluated dependencies plus three additions
- Part 2: Violation assessment, revised phone structure, primary key identification
- Part 3: Composite key analysis, decomposed tables, business justifications
- Part 4: Transitive dependency chains, full 3NF tables with keys, referential integrity description
- Part 5: Trade-off table and denormalization decision document

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 1 — Functional Dependencies | 20 |
| Part 2 — First Normal Form | 15 |
| Part 3 — Second Normal Form | 25 |
| Part 4 — Third Normal Form | 25 |
| Part 5 — Denormalization Decision | 15 |
| **Total** | **100** |

---

*Module 12 Lab | CIS-3312 Systems Analysis and Design | Texas Wesleyan University*

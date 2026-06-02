# Lab Activity: Module 02 — Database Design: Normalization and ERDs

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Total Points: 100

---

### Lab Overview

In this lab you will normalize a provided unnormalized relation to Third Normal Form using a structured step-by-step written process, then implement the resulting schema as SQL DDL in Cloud SQL for PostgreSQL. You will also identify and fix functional dependencies and document your decisions in a written analysis.

This lab directly mirrors the normalization reasoning tested on the Google Cloud Professional Cloud Database Engineer exam.

Estimated completion time: 60–75 minutes.

---

### Prerequisites

- Module 02 video scripts and reading guide reviewed
- Cloud SQL for PostgreSQL instance available (use `txwes-pg-lab01` from Module 01, or create a new instance following the same steps)
- Cloud Shell open and connected to the PostgreSQL instance

---

### Part 1 — Normalization Written Analysis (40 points)

You are given the following unnormalized relation representing a hospital appointment scheduling system.

```text
hospital_appointments (
    appointment_id,
    patient_id,
    patient_name,
    patient_dob,
    patient_insurance_id,
    insurance_company_name,
    insurance_phone,
    doctor_id,
    doctor_name,
    doctor_specialty,
    clinic_id,
    clinic_name,
    clinic_address,
    appointment_date,
    appointment_time,
    diagnosis_code,
    diagnosis_description,
    billing_amount
)
```

Primary key: appointment_id

Complete all four steps below. Write your answers in a lab report document.

#### Step 1 — Identify All Functional Dependencies (10 points)

List every functional dependency you can identify in the unnormalized table. Use the notation X → Y. Include at minimum eight functional dependencies. For each one, state whether the right-hand side attribute is a key attribute, a non-key attribute directly dependent on the primary key, or a non-key attribute dependent on a different non-key attribute.

#### Step 2 — First Normal Form Analysis (5 points)

Assess whether the table as given satisfies 1NF. Justify your answer. If any 1NF violation exists, describe what it is and how it would be corrected. If the table already satisfies 1NF, state the reason.

#### Step 3 — Normalize to Second Normal Form (Not applicable here — explain why) (5 points)

The primary key is a single column (appointment_id), not a composite key. Explain in two to three sentences why 2NF violations are impossible in this table given that primary key structure, and what table structure would make 2NF violations possible.

#### Step 4 — Normalize to Third Normal Form (20 points)

Identify every transitive dependency in the unnormalized table. For each transitive dependency, write the full dependency chain in the form: appointment_id → X → Y. Then produce the fully normalized 3NF schema by splitting the table into the correct number of tables. For each resulting table, specify the primary key, all foreign keys, and all non-key attributes.

Present the final 3NF schema using the notation below:

```text
table_name (
    column_name [PK],
    column_name [FK → referenced_table],
    column_name,
    ...
)
```

---

### Part 2 — SQL Implementation in Cloud SQL (45 points)

Connect to your Cloud SQL for PostgreSQL instance via Cloud Shell.

```bash
gcloud sql connect txwes-pg-lab01 --user=postgres --quiet
```

#### Step 5 — Create the Database and Normalized Schema (30 points)

Create a new database and implement your 3NF schema from Step 4 as SQL DDL. Your implementation must include the following.

- All tables from your 3NF schema
- Correct PRIMARY KEY definitions for every table
- FOREIGN KEY constraints with appropriate ON DELETE behavior for every relationship
- At least two NOT NULL constraints beyond primary key columns
- At least one CHECK constraint
- At least one UNIQUE constraint beyond primary key columns

```sql
CREATE DATABASE txwes_hospital;
\c txwes_hospital
```

Write and run your own CREATE TABLE statements based on your 3NF analysis. Do not copy a pre-written solution — the DDL must match the schema you designed in Part 1.

#### Step 6 — Insert Sample Data (10 points)

Insert at least three patients, two doctors, two clinics, two insurance companies, and five appointments into your schema. Write the INSERT statements yourself based on the column definitions you created.

After inserting data, run the following verification queries and include the results in your lab report.

```sql
-- Count rows in each table
SELECT 'patients'    AS tbl, COUNT(*) FROM patients
UNION ALL
SELECT 'doctors',              COUNT(*) FROM doctors
UNION ALL
SELECT 'appointments',         COUNT(*) FROM appointments;
```

Adjust table names to match your actual schema.

#### Step 7 — Verify Referential Integrity (5 points)

Attempt to insert an appointment that references a non-existent patient_id. Copy the resulting error message into your lab report. This confirms your foreign key constraints are active.

---

### Part 3 — ERD Documentation (15 points)

#### Step 8 — Draw the ERD (15 points)

Using any drawing tool — draw.io, Lucidchart, dbdiagram.io, or hand-drawn and photographed — create an ERD for your 3NF hospital schema. The ERD must include the following.

- All entities as labeled rectangles
- Primary key attributes underlined or labeled PK
- Foreign key relationships shown as connecting lines with Crow's Foot cardinality notation
- Correct cardinality on both ends of every relationship line (the mandatory vs. optional participation markers)
- A legend identifying your notation style

Export or photograph the ERD and include it as an image in your lab report labeled as Figure 1.

Write two to three sentences below the ERD explaining the most significant normalization decision you made — which transitive dependency required the most tables to resolve and why.

---

### Lab Submission Checklist

- Part 1 written analysis (Steps 1–4) in your lab report document
- Part 2 SQL implementation: CREATE TABLE statements, INSERT statements, and verification query results
- Part 2 referential integrity violation error message
- Part 3 ERD image labeled Figure 1 with written explanation

---

### Grading Rubric — 100 Points Total

| Deliverable | Points | Criteria |
|---|---|---|
| Step 1 — Functional dependencies | 10 | At least 8 FDs listed with correct notation; each correctly classified |
| Step 2 — 1NF analysis | 5 | Correct assessment with accurate justification |
| Step 3 — 2NF explanation | 5 | Correct explanation of why single-column PK precludes 2NF violations |
| Step 4 — 3NF schema | 20 | All transitive dependencies identified; correct final tables; PKs and FKs labeled |
| Step 5 — DDL implementation | 30 | Schema matches written analysis; all constraints present and syntactically correct |
| Step 6 — Sample data and verification | 10 | Minimum row counts met; verification query results shown |
| Step 7 — Referential integrity check | 5 | Error message shown; correct constraint identified |
| Step 8 — ERD | 15 | All entities present; Crow's Foot notation correct; cardinality accurate; legend present |
| Deductions | up to -10 | DDL does not compile or run without errors |

---

Reference: cloud.google.com/learn

# Lab 10 — Data Quality Assessment and Governance Documentation

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 100

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 5: Data Governance, Quality, and Controls

---

## Lab Overview

In this lab you will perform a structured data quality assessment on a simulated healthcare patient dataset using Python pandas and SQL. You will measure each of the six data quality dimensions, document your findings, and produce a data quality scorecard. You will also complete a governance documentation exercise.

**Tools required:**

- Python 3.8 or later
- pandas (`pip install pandas`)
- SQLite (built into Python standard library — no installation needed)

---

## Dataset

Create a file named `patient_records.csv` in your working directory.

```csv
patient_id,first_name,last_name,dob,email,phone,state,zip_code,diagnosis_code,last_visit_date,insurance_id
P001,John,Smith,1985-03-15,john.smith@email.com,555-1234,TX,75001,I10,2024-01-10,INS001
P002,Maria,Garcia,1990-07-22,maria.garcia@email.com,555-5678,TX,75002,E11,2024-02-14,INS002
P003,Robert,Johnson,,rjohnson@email.com,,TX,75003,J06,2024-01-25,INS003
P004,Lisa,Williams,1978-11-05,lwilliams_at_email.com,555-2345,TX,75004,I25,2023-09-12,INS004
P005,James,Brown,2035-06-01,james.brown@email.com,555-3456,TX,75005,K21,2024-01-30,INS005
P006,Patricia,Davis,1965-04-18,pdavis@email.com,555-4567,TX,75006,M54,2024-02-20,INS006
P007,Michael,Miller,1952-09-30,mmiller@email.com,555-5678,TX,75007,I10,2024-01-05,INS007
P008,Linda,Wilson,1988-02-14,,555-6789,CA,90001,E11,2024-02-28,INS008
P009,William,Moore,1971-08-22,william.moore@email.com,555-7890,TX,75009,J06,2021-05-15,INS009
P010,Barbara,Taylor,1995-12-10,btaylor@email.com,555-8901,TX,75010,I25,2024-02-10,INS010
P001,John,Smith,1985-03-15,john.smith@email.com,555-1234,TX,75001,I10,2024-01-10,INS001
P011,Jennifer,Anderson,1982-05-28,janderson@email.com,555-9012,TX,75011,K21,2024-01-18,INS011
P012,Charles,Thomas,1960-10-03,cthomas@email.com,555-0123,TX,ABCDE,M54,2024-02-05,INS012
P013,Susan,Jackson,1975-07-17,,,,I10,,INS013
P014,Joseph,White,1989-04-22,jwhite@email.com,555-1235,TX,75014,E11,2024-01-22,INS014
P015,Mary,Harris,1955-01-30,mharris@email.com,555-2346,TX,75015,J06,2019-11-08,INS015
```

---

## Part 1: Data Loading and Initial Inspection (10 points)

### Task 1.1 — Load and inspect

```python
import pandas as pd
import sqlite3
from datetime import datetime, date

df = pd.read_csv('patient_records.csv')

print(f"Shape: {df.shape}")
print(f"\nColumn data types:\n{df.dtypes}")
print(f"\nFirst 5 rows:\n{df.head()}")
print(f"\nNull counts per column:\n{df.isnull().sum()}")
```

**Deliverable 1.1:** How many records are in the dataset? How many columns? Which columns have null values?

---

## Part 2: Completeness Assessment (15 points)

### Task 2.1 — Compute completeness for each column

```python
total = len(df)

completeness = pd.DataFrame({
    'column': df.columns,
    'non_null_count': df.count().values,
    'null_count': df.isnull().sum().values,
    'completeness_pct': (df.count().values / total * 100).round(2)
})

completeness = completeness.sort_values('completeness_pct')
print(completeness.to_string(index=False))
```

### Task 2.2 — Identify critical completeness failures

```python
# Define required fields for a valid patient record
required_fields = ['patient_id', 'first_name', 'last_name', 'dob', 'email', 'state']

missing_required = df[required_fields].isnull().any(axis=1)
print(f"\nRecords with at least one missing required field: {missing_required.sum()}")
print(df[missing_required][['patient_id'] + required_fields])
```

**Deliverable 2:** Which columns have less than 90% completeness? Which patient records have missing required fields? State the completeness percentage for `dob`, `email`, and `phone`.

---

## Part 3: Validity Assessment (20 points)

### Task 3.1 — Email format validation

```python
import re

email_pattern = r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'

df['email_valid'] = df['email'].apply(
    lambda x: bool(re.match(email_pattern, str(x))) if pd.notna(x) else None
)

invalid_emails = df[df['email_valid'] == False][['patient_id', 'email']]
print(f"Invalid email addresses found: {len(invalid_emails)}")
print(invalid_emails)
```

### Task 3.2 — Date of birth validation

```python
today = date.today()

def validate_dob(dob_str):
    if pd.isna(dob_str):
        return 'missing'
    try:
        dob = datetime.strptime(str(dob_str), '%Y-%m-%d').date()
        if dob > today:
            return 'future_date'
        if dob.year < 1900:
            return 'too_old'
        return 'valid'
    except ValueError:
        return 'bad_format'

df['dob_status'] = df['dob'].apply(validate_dob)
print(f"\nDOB validity breakdown:\n{df['dob_status'].value_counts()}")
print(df[df['dob_status'] != 'valid'][['patient_id', 'dob', 'dob_status']])
```

### Task 3.3 — ZIP code format validation

```python
df['zip_valid'] = df['zip_code'].apply(
    lambda x: bool(re.match(r'^\d{5}$', str(x))) if pd.notna(x) else None
)

invalid_zips = df[df['zip_valid'] == False][['patient_id', 'zip_code']]
print(f"\nInvalid ZIP codes: {len(invalid_zips)}")
print(invalid_zips)
```

**Deliverable 3:** List all validity violations found — invalid emails, invalid dates of birth, and invalid ZIP codes. For each violation, identify the patient ID and the dimension violated.

---

## Part 4: Uniqueness Assessment (15 points)

### Task 4.1 — Detect duplicate patient IDs

```python
duplicate_ids = df[df.duplicated(subset=['patient_id'], keep=False)] \
                .sort_values('patient_id')

print(f"Duplicate patient_id records: {len(duplicate_ids)}")
print(duplicate_ids[['patient_id', 'first_name', 'last_name', 'dob', 'email']])
```

### Task 4.2 — Detect potential duplicate patients (same name + DOB)

```python
potential_dupes = df[df.duplicated(subset=['first_name', 'last_name', 'dob'], keep=False)] \
                  .sort_values(['last_name', 'first_name'])

print(f"\nPotential duplicate patients (name + DOB match): {len(potential_dupes)}")
print(potential_dupes[['patient_id', 'first_name', 'last_name', 'dob', 'email']])
```

**Deliverable 4:** How many exact duplicate records were found? How would you handle duplicate patient_ids before using this dataset in a clinical analytics model?

---

## Part 5: Timeliness Assessment (10 points)

### Task 5.1 — Assess record staleness

```python
df['last_visit_date'] = pd.to_datetime(df['last_visit_date'], errors='coerce')
today_ts = pd.Timestamp.today()

df['days_since_visit'] = (today_ts - df['last_visit_date']).dt.days

# Timeliness thresholds
df['timeliness_status'] = pd.cut(
    df['days_since_visit'],
    bins=[-1, 365, 730, 1825, float('inf')],
    labels=['Within 1 year', '1-2 years', '2-5 years', 'Over 5 years']
)

print(f"Timeliness distribution:\n{df['timeliness_status'].value_counts().sort_index()}")
print(f"\nStale records (last visit > 2 years ago):")
stale = df[df['days_since_visit'] > 730][['patient_id', 'last_name', 'last_visit_date', 'days_since_visit']]
print(stale)
```

**Deliverable 5:** How many records have not had a visit in over 2 years? For what clinical analytics use cases would timeliness be a critical concern?

---

## Part 6: Data Quality Scorecard (15 points)

### Task 6.1 — Compile the scorecard

```python
total_records = len(df)
unique_records = total_records - df.duplicated(subset=['patient_id']).sum()

scorecard = {
    'Dimension': ['Completeness', 'Completeness', 'Completeness',
                  'Validity', 'Validity', 'Validity',
                  'Uniqueness', 'Timeliness'],
    'Check': ['DOB present', 'Email present', 'Phone present',
              'Email format valid', 'DOB is valid date', 'ZIP format valid',
              'No duplicate patient IDs', 'Last visit within 2 years'],
    'Pass_Count': [
        df['dob'].notna().sum(),
        df['email'].notna().sum(),
        df['phone'].notna().sum(),
        (df['email_valid'] == True).sum(),
        (df['dob_status'] == 'valid').sum(),
        (df['zip_valid'] == True).sum(),
        total_records - df.duplicated(subset=['patient_id']).sum(),
        (df['days_since_visit'] <= 730).sum()
    ],
    'Total': [total_records] * 8
}

scorecard_df = pd.DataFrame(scorecard)
scorecard_df['Pass_Rate_Pct'] = (scorecard_df['Pass_Count'] / scorecard_df['Total'] * 100).round(1)
print(scorecard_df.to_string(index=False))
```

**Deliverable 6:** Paste the full scorecard table. Which dimension has the lowest overall pass rate? What would you recommend to the data steward as the highest-priority remediation action?

---

## Part 7: Governance Documentation Exercise (15 points)

Answer the following questions in your lab report (3–5 sentences each).

**Question 7.1 — Data Steward Assignment:** Based on the quality issues you found in this patient dataset, what specific responsibilities would you assign to the data steward for this dataset? Name at least three concrete actions the steward should take in the next 30 days.

**Question 7.2 — Master Data Management:** Several patients appear as duplicates in this dataset. Describe how an MDM solution would address this problem. What is a golden record in this context, and what survivorship rules would you define to choose the "best" value when two duplicate records have different email addresses?

**Question 7.3 — Data Catalog Entry:** Write a brief data catalog entry for the `patient_records` dataset. Include: a plain-language description of what the dataset contains, the data owner role (e.g., VP of Clinical Operations), the data steward role, data refresh frequency, and the two most critical quality issues found in this lab.

---

## Submission Checklist

Submit in a single ZIP file:

- [ ] Python script (`lab10.py` or `lab10.ipynb`)
- [ ] Lab report (PDF or Word) containing all deliverables and governance answers

---

## Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Part 1 — Data loading | 10 | Correct shape, dtype inspection, null summary |
| Part 2 — Completeness | 15 | Completeness percentages correct; critical fields identified |
| Part 3 — Validity | 20 | All three validity checks implemented and violations listed |
| Part 4 — Uniqueness | 15 | Exact and potential duplicates identified correctly |
| Part 5 — Timeliness | 10 | Stale records correctly identified; use case analysis |
| Part 6 — Scorecard | 15 | All eight checks compiled; priority remediation identified |
| Part 7 — Governance | 15 | Accurate, practical governance documentation |
| **Total** | **100** | |

---

End of Lab 10

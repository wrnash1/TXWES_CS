# Lab Activity: Module 08 - Human Capital Management Modules

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Lab Overview

This lab develops your ability to map HR business scenarios to SuccessFactors modules, trace payroll calculations and GL postings, analyze performance management processes, and evaluate HCM integration architecture. All work is analytical and scenario-based.

**Estimated Time:** 90 minutes

**Submission:** Upload to Canvas under "Lab 08 -- Human Capital Management Modules."

---

## Learning Objectives

By completing this lab you will be able to:

- Map HR business events to the correct SAP SuccessFactors module
- Calculate gross pay, deductions, and net pay for a sample payroll
- Trace the payroll journal entry from HCM to the General Ledger
- Analyze the performance management cycle and identify gaps in a company's current process
- Describe the integration between Employee Central, payroll, and SAP FI cost centers

---

## Scenario Background

**Company:** Lakewood Regional Medical Center

**Industry:** Healthcare -- regional hospital system with three campuses

**Size:** 2,400 employees, $380 million operating budget

**HCM System:** SAP SuccessFactors, implemented 8 months ago (Employee Central and Payroll live; Performance and Goals go-live scheduled next quarter)

**HR team:** CHRO, 4 HR business partners, 2 payroll specialists, 1 LMS administrator

Lakewood's CHRO has identified four problem areas she wants analyzed before the Performance and Goals module goes live.

---

## Part A: SuccessFactors Module Mapping (25 points)

### A-1: Business Event to Module Assignment

For each business event at Lakewood, identify the correct SuccessFactors module that handles the process and explain in one sentence why that module is correct.

| Business Event | SuccessFactors Module | One-Sentence Justification |
|---|---|---|
| A nurse manager submits a request to hire two additional RNs for the night shift | | |
| A newly hired radiologist receives an automated task list to complete HIPAA forms and attend safety orientation | | |
| Lakewood tracks which employees have completed mandatory annual infection control training | | |
| An ICU charge nurse's base salary increases from $95,000 to $102,000 following a promotion | | |
| The CHRO wants to identify which department directors are within 3 years of retirement and who could replace them | | |
| Lakewood distributes merit increases for the fiscal year based on last year's performance scores | | |
| An employee checks their current pay stub and year-to-date earnings | | |

### A-2: System of Record Analysis

The CHRO asks: "We have Employee Central, a legacy payroll system we are sunsetting, and an old on-premise SAP HR module that HR still uses for reporting. Which system should be our authoritative source of truth for employee data going forward?"

In 100-150 words, explain the concept of a system of record and why Employee Central should be designated as Lakewood's authoritative HR data source. What risks arise when multiple systems hold partially overlapping employee data without a clear system of record?

---

## Part B: Payroll Calculation and GL Posting (30 points)

### B-1: Gross to Net Calculation

Calculate the net pay for the following three Lakewood employees for a biweekly pay period. Show all calculations.

#### Employee 1 -- Marcus Webb, RN (Hourly)

- Hourly rate: $38.50
- Regular hours worked: 80 (standard biweekly hours)
- Overtime hours worked: 12 (all hours over 80 in a biweekly period paid at 1.5x)
- Federal income tax withholding: 22% of gross
- FICA (Social Security + Medicare): 7.65% of gross
- Health insurance premium: $185 per pay period
- 401k contribution: 5% of gross

#### Employee 2 -- Dr. Anita Sharma, Radiologist (Salaried)

- Annual salary: $280,000
- Biweekly pay periods: 26 per year
- Federal income tax withholding: 32% of gross
- FICA: 7.65% of gross (applies only to first $160,200 of annual wages -- assume not yet exceeded for this period)
- Health insurance premium: $210 per pay period
- 401k contribution: 6% of gross

#### Employee 3 -- Sandra Kim, Medical Receptionist (Hourly, Part-Time)

- Hourly rate: $18.75
- Regular hours worked: 48 (part-time employee; no overtime threshold applies for this period)
- Federal income tax withholding: 12% of gross
- FICA: 7.65% of gross
- No benefits enrollment (part-time not eligible)
- No 401k contribution

Present your calculations in a table with rows: Gross Pay, Federal Tax, FICA, Health Premium, 401k, Total Deductions, Net Pay.

### B-2: Payroll Journal Entry

Based on the three employees in B-1, create the payroll journal entry that Lakewood's SAP SuccessFactors Payroll system would post to the General Ledger.

Assume the following cost center assignments:

- Marcus Webb (RN) -- Cost Center 3100 (Inpatient Nursing)
- Dr. Anita Sharma -- Cost Center 3400 (Radiology)
- Sandra Kim -- Cost Center 2100 (Patient Registration)

The journal entry should debit Wage Expense by cost center and credit the appropriate liability and clearing accounts. Use the gross pay amounts as wage expense (before the employee deductions, which are balance sheet liabilities, not reductions of wage expense).

Show the complete journal entry in debit/credit format and verify that it balances.

---

## Part C: Performance Management Process Analysis (25 points)

### C-1: Current State Gap Analysis

Lakewood's current performance review process (before SuccessFactors Performance and Goals go-live) works as follows:

- Each department manager receives a paper form in November
- Managers rate employees on a 5-point scale across 6 competencies
- Forms are returned to HR in December
- HR types ratings into a spreadsheet
- Salary recommendations are sent to managers in a separate email from the spreadsheet
- No formal goal-setting occurred at the beginning of the year
- Response rate last year was 71% (29% of employees had no review completed)

Identify four specific problems with this current process and explain how SuccessFactors Performance and Goals would address each problem. Present your analysis in a table with columns: Problem, Current Impact, SuccessFactors Solution.

### C-2: Goal-Setting Design

Lakewood is preparing to implement the Performance and Goals module. The CHRO wants to ensure that employee goals are aligned to the hospital system's three strategic priorities:

- Patient safety and quality outcomes
- Financial sustainability
- Workforce development and retention

Design a sample goal structure for a Nursing Unit Manager that includes one goal aligned to each strategic priority. For each goal, specify: the goal text, the measurable success criterion, and the data source Lakewood would use to verify achievement.

---

## Part D: HCM Integration Analysis (20 points)

### D-1: Integration Trigger Mapping

For each HR event at Lakewood, identify the systems involved, the trigger for the integration, and the downstream effect in the financial or operational ERP modules.

| HR Event | Source System | Target System | Trigger | Downstream Effect |
|---|---|---|---|---|
| A new nurse is hired and added to Employee Central | | | | |
| An employee changes their health insurance plan during open enrollment | | | | |
| Biweekly payroll is processed for all 2,400 employees | | | | |
| A physician is transferred from Campus A to Campus B (different cost center) | | | | |

### D-2: Data Quality Risk Assessment

Lakewood's IT team proposes maintaining two parallel systems for 90 days during the transition from the legacy HR system to Employee Central -- updating both systems with employee changes until the legacy system is fully decommissioned.

In 100-150 words, explain why maintaining parallel systems during transition creates data quality risks. What specific types of errors are likely to occur? What is the preferred approach to managing the transition, and what safeguard should be in place to ensure data integrity in Employee Central before the legacy system is decommissioned?

---

## Grading Rubric

| Section | Points | Criteria |
|---|---|---|
| A-1: Module mapping | 14 | All 7 events mapped to correct module with valid justification |
| A-2: System of record analysis | 11 | 100-150 words; system of record concept explained; risks of multiple partial systems described |
| B-1: Gross to net calculations | 18 | All three employees calculated correctly; all deduction categories included |
| B-2: Payroll journal entry | 12 | Correct debits by cost center; correct credit accounts; entry balances |
| C-1: Gap analysis | 12 | Four problems identified; current impact described; SuccessFactors solution explained for each |
| C-2: Goal-setting design | 13 | Three goals created; each aligned to a strategic priority; measurable criteria and data source specified |
| D-1: Integration trigger mapping | 10 | All four events mapped with source, target, trigger, and downstream effect |
| D-2: Data quality risk assessment | 10 | 100-150 words; specific error types named; preferred approach and data validation safeguard described |
| **Total** | **100** | |

---

## Submission Instructions

1. Compile all responses into a single document.
2. Name your file: `Lab08_LastName_FirstName.pdf`
3. Upload to Canvas under "Lab 08 -- Human Capital Management Modules."
4. Deadline: See course schedule in Canvas. Late submissions lose 10 points per day.

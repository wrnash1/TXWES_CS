# Reading Guide: Module 08 - Human Capital Management Modules

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Introduction

Human Capital Management (HCM) is the ERP domain that manages the workforce -- from recruiting and hiring through performance management, payroll, and eventual offboarding. In large organizations, HCM automation is where ERP saves thousands of hours of manual HR processing annually. SAP's HCM platform is SuccessFactors, a cloud-based suite that covers all phases of the employee lifecycle. This module covers the SuccessFactors suite, Employee Central as the system of record, payroll integration architecture, talent management, and HCM's integration with financial and operational ERP modules.

---

## Section 1: High-Yield Glossary

**Human Capital Management (HCM)**
The ERP domain responsible for managing all workforce processes -- recruiting, onboarding, payroll, benefits, performance, learning, and succession planning. HCM treats employees as strategic assets whose development and performance directly affect organizational outcomes.

**SAP SuccessFactors**
SAP's cloud-based HCM suite. SuccessFactors consists of modular applications including Employee Central (core HR), Recruiting, Onboarding, Learning, Performance and Goals, Succession and Development, and Compensation. All modules share a common data model anchored in Employee Central.

**Employee Central (EC)**
The core HR system of record within SuccessFactors. Employee Central stores all fundamental employee master data: personal information, position, department, manager, compensation, work schedule, and employment status. All other SuccessFactors modules read from and write to Employee Central.

**Recruiting**
The SuccessFactors module that manages the talent acquisition process: job requisition creation, job posting to career sites and job boards, application tracking, interview scheduling and evaluation, and offer letter generation. Recruiting ends when the candidate accepts an offer.

**Onboarding**
The SuccessFactors module that manages the new hire experience from offer acceptance through the early employment period. Onboarding automates task lists for IT provisioning, forms completion, compliance acknowledgments, and manager introductions.

**Performance and Goals**
The SuccessFactors module for employee goal setting and performance evaluation. Employees and managers set SMART goals at the start of the performance year. Progress is tracked mid-year. A formal annual review rates goal achievement and competency demonstration.

**Learning Management System (LMS)**
The SuccessFactors module for delivering, tracking, and reporting on employee training. The LMS manages both mandatory compliance training (with due dates and completion tracking) and elective development courses.

**Succession Planning**
The SuccessFactors module for identifying high-potential employees and building leadership pipelines. Succession Planning maps employees to positions, rates their readiness for advancement, and creates individual development plans to close skill gaps.

**Compensation Planning**
The SuccessFactors module for managing merit increases, bonuses, and equity grants during the annual compensation cycle. Compensation Planning uses performance review scores and budget guidelines to generate recommended pay adjustments for manager review.

**Payroll**
The HCM process that calculates employee wages, applies tax and benefit deductions, and disburses net pay. In SAP, payroll processing is handled by Employee Central Payroll, which integrates with Employee Central for master data and with SAP FI for GL posting.

**Gross Pay**
Total compensation before deductions. Gross pay includes base wages (hours x rate for hourly; fixed salary for salaried employees), overtime (typically 1.5x regular rate for hours over 40), and any additional earnings (commissions, bonuses).

**Net Pay**
Take-home pay after all deductions. Net Pay = Gross Pay minus tax withholdings (federal, state, local) minus benefit contributions (health, dental, 401k) minus other voluntary deductions.

**Position**
A specific job assignment within the organization -- for example, "Marketing Coordinator, Department 120, Grade 8." Positions are distinct from employees; one position can be held by different employees over time. Position management tracks headcount budgets and organizational structure in Employee Central.

**Organizational Unit**
The organizational hierarchy node in SuccessFactors -- typically a department or division. Org units map to financial cost centers in SAP FI/CO, enabling automatic cost allocation when payroll posts to the GL.

**Cost Center**
The SAP CO/FI object to which payroll costs are assigned. Each organizational unit in Employee Central maps to a cost center. When payroll runs, wage expenses post to the GL by cost center automatically.

---

## Section 2: Employee Lifecycle and SuccessFactors Modules

### Complete Employee Lifecycle Flow

```text
[Job Requisition Created]
  (Hiring manager submits request)
          |
[Recruiting]
  Job posting, applications, interviews, offer
          |
[Onboarding]
  IT provisioning, forms, compliance, orientation
          |
[Employee Central]
  Core HR master data record created
  (Position, Org Unit, Compensation, Manager)
          |
    +-----+------+--------+
    |             |        |
    v             v        v
[Performance  [Learning]  [Compensation]
 and Goals]   Training    Merit/Bonus
 Review cycle  delivery    planning
    |
    v
[Succession Planning]
 Talent pipeline
    |
    v
[Offboarding]
 Exit tasks, final pay, access revocation
```

### SuccessFactors Module Reference

| Module | Phase | Primary Function | Key Output |
|---|---|---|---|
| Recruiting | Attract | Source, evaluate, and hire candidates | Offer letter; hire record |
| Onboarding | Start | Integrate new hire with task automation | Completed forms; provisioned access |
| Employee Central | All phases | Core HR system of record | Employee master data |
| Performance and Goals | Develop | Goal setting, tracking, annual review | Review score; calibration data |
| Learning (LMS) | Develop | Deliver and track training courses | Completion records; compliance status |
| Succession and Development | Grow | Identify and develop future leaders | Succession plans; readiness ratings |
| Compensation | Grow | Administer merit and bonus cycles | Pay adjustments; total comp statements |
| Employee Central Payroll | Pay | Calculate wages and post to GL | Payroll journal entries; pay advice |

---

## Section 3: Payroll Integration Architecture

### Payroll Calculation Flow

```text
[Employee Central]
  Current salary, pay grade, work schedule
  Benefits elections, deductions
          |
          v (real-time replication)
[Employee Central Payroll]
  Gross Pay Calculation:
    Regular hours x rate
    + Overtime hours x 1.5 rate
    + Other earnings (bonus, commission)
  = GROSS PAY
          |
  Deductions Applied:
    - Federal/State/Local Tax Withholding
    - FICA (Social Security + Medicare)
    - Health/Dental/Vision premiums
    - 401k/Retirement contribution
    - Other voluntary deductions
  = NET PAY
          |
          v
[Payment Run]
  Bank transfer to employee accounts
  Pay advice/stub generated
          |
          v
[GL Posting to SAP FI]
  Dr: Wage Expense (by Cost Center)
  Dr: Benefit Expense (by Cost Center)
  Cr: Payroll Clearing (net pay)
  Cr: Tax Withholding Liability
  Cr: Benefits Payable
```

### Payroll Journal Entry Example

| Account | Debit | Credit |
|---|---|---|
| Wage Expense -- Marketing (CC 1001) | $42,000 | |
| Wage Expense -- Operations (CC 1002) | $38,000 | |
| Benefit Expense | $12,000 | |
| Payroll Clearing (net pay) | | $72,500 |
| Federal Tax Withholding Liability | | $13,200 |
| Benefits Payable | | $6,300 |
| **Total** | **$92,000** | **$92,000** |

---

## Section 4: Talent Management Concepts

### Performance Management Cycle

| Phase | Timing | Activity | SuccessFactors Tool |
|---|---|---|---|
| Goal Setting | January | Employee and manager set SMART goals | Performance and Goals |
| Progress Check | Q2 | Informal review of goal progress | Continuous Feedback |
| Mid-Year Review | July | Formal mid-year rating discussion | Performance and Goals |
| Year-End Review | December | Final rating; competency assessment | Performance and Goals |
| Calibration | January | Managers compare ratings for fairness | Calibration Sessions |
| Compensation Planning | January | Merit and bonus decisions based on ratings | Compensation module |

### Succession Planning Concepts

| Concept | Definition |
|---|---|
| Succession Plan | A documented plan identifying who is ready to fill a critical position |
| Readiness Rating | Assessment of how quickly an employee could step into a target role (Ready Now, Ready in 1-2 Years, Ready in 3+ Years) |
| Talent Pool | A group of employees identified as high-potential candidates for a category of future roles |
| Position Risk | The risk level associated with a position losing its current occupant (attrition risk, flight risk) |
| 9-Box Grid | A talent assessment matrix plotting employees on two axes: current performance and future potential |

---

## Section 5: HCM Integration with Other ERP Modules

### Cross-Module Integration Points

| Integration | From | To | Trigger | Data Exchanged |
|---|---|---|---|---|
| Payroll to GL | SuccessFactors Payroll | SAP FI-GL | Pay cycle completion | Wage expense by cost center; tax liabilities |
| Employee to Cost Center | Employee Central | SAP CO-CCA | New hire or transfer | Employee-to-cost-center assignment |
| Time to Project | SuccessFactors Time | SAP MM/PS | Time entry approval | Labor hours against project or work order |
| Benefits to AP | Benefit elections | SAP FI-AP | Enrollment change | Benefit deduction amounts for payment to carriers |
| Org structure to FI | EC Org Unit hierarchy | SAP FI company code | Org restructure | Reporting unit to legal entity mapping |

### HCM Module Comparison

| Function | SAP SuccessFactors | Oracle HCM Cloud | Salesforce (limited) |
|---|---|---|---|
| Core HR system of record | Employee Central | Oracle Core HR | Not applicable |
| Recruiting | Recruiting | Oracle Recruiting | Not applicable |
| Onboarding | Onboarding | Oracle Onboarding | Not applicable |
| Learning | Learning | Oracle Learning | Not applicable |
| Performance management | Performance and Goals | Oracle Performance | Not applicable |
| Payroll | Employee Central Payroll | Oracle Payroll | Not applicable |
| Succession planning | Succession and Development | Oracle Succession | Not applicable |
| Compensation | Compensation | Oracle Compensation | Not applicable |

Salesforce does not have a native HCM module. Salesforce focuses on CRM (customer-facing processes). Workforce management is handled by SAP SuccessFactors, Oracle HCM Cloud, Workday, or similar dedicated HCM platforms.

---

## Section 6: Certification Exam Tips

1. **Know the SuccessFactors module names and functions.** Employee Central (core HR record), Recruiting (hiring), Onboarding (new hire tasks), Performance and Goals (reviews), Learning (training), Succession (talent pipeline), Compensation (pay cycles). These are commonly tested on SAP Associate scenario questions.

2. **Employee Central is the system of record.** All other SuccessFactors modules depend on Employee Central data. If the question asks where an employee's position, salary, or department is stored, the answer is Employee Central.

3. **Payroll integration is real-time, not batch.** Changes in Employee Central replicate to Employee Central Payroll automatically. This eliminates manual re-entry and ensures payroll accuracy.

4. **Payroll posts to GL by cost center.** Every payroll run posts wage expenses to the General Ledger assigned to specific cost centers. This automatic posting enables CO department cost reporting without manual allocation.

5. **HCM is SaaS in the SAP SuccessFactors context.** SuccessFactors is a cloud-only solution, unlike some older SAP HR modules that ran on-premise.

6. **Distinguish Performance and Goals from Learning.** Performance and Goals is about employee evaluation and review cycles. Learning is about training course delivery and completion tracking. These are frequently confused in scenario questions.

7. **Succession Planning is not the same as Performance Management.** Succession is forward-looking (who is ready for future roles?). Performance is current-state (how is the employee performing now?).

8. **Payroll deductions reduce gross pay to net pay.** Know the categories: tax withholdings (federal, state, FICA), benefit premiums (health, dental), retirement contributions (401k). Gross minus all deductions equals net pay.

---

## Section 7: Required Trailhead and Study Resources

Complete before attempting the quiz:

- **Salesforce Trailhead -- HR Basics**
  URL: trailhead.salesforce.com -- search "HR Basics"
  Provides context for how HR processes function and how technology supports them.

---

## Section 8: Study Checklist

- Memorize the SuccessFactors module names and what each one does.
- Trace the employee lifecycle flow in Section 2 without looking at labels.
- Study the payroll calculation flow in Section 3. Know the difference between gross pay and net pay.
- Review the payroll journal entry example. Know which accounts are debited and which are credited.
- Study the performance management cycle in Section 4.
- Review the cross-module integration table in Section 5.
- Study the HCM comparison table in Section 5. Know that Salesforce has no native HCM module.
- Complete the Salesforce Trailhead "HR Basics" module.
- Watch the Module 08 video lecture.
- Complete Lab 08.
- Post to Discussion Forum 08 by Wednesday at 11:59 PM.
- Complete Quiz 08 (10 questions).

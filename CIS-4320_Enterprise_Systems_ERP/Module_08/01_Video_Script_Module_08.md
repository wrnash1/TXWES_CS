# Video Script: Module 08 - Human Capital Management Modules

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 22-24 minutes

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### [00:00 - 01:30] Opening

Professor Nash on camera. Title card: "Module 08 - Human Capital Management Modules."

"Welcome back to CIS-4320. In Module 07 we covered CRM -- the front office. Now we move to a module that every employee touches, whether they know it or not: Human Capital Management.

HCM is the ERP domain for your workforce. If you have ever received a paycheck, enrolled in benefits, completed a mandatory compliance training, or had a performance review in a software system, you have used an HCM module. For organizations with hundreds or thousands of employees, HCM automation is where ERP delivers enormous operational value.

Today we cover the SAP SuccessFactors HCM suite, the core HR modules from hiring through retirement, payroll integration, talent management, and how HCM connects to the financial and operations modules. The concepts in this module apply broadly to any enterprise HCM system and support both the SAP Associate exam and general ERP literacy."

---

### [01:30 - 05:30] HCM Module Overview -- The Employee Lifecycle

Cut to slide: "HCM -- Managing the Employee Lifecycle."

"Human Capital Management in ERP covers the complete lifecycle of an employee from the moment they are recruited through the day they retire or leave the company. In SAP's world, this is handled primarily by SAP SuccessFactors -- a cloud-based HCM suite that covers all phases of the employee lifecycle.

Let me walk through the lifecycle stages.

Hire: Recruiting and Onboarding. The cycle begins before the employee even starts. SuccessFactors Recruiting manages the job posting, application, interview evaluation, and offer letter. Once the candidate accepts, SuccessFactors Onboarding takes over -- creating task lists for IT to provision equipment, for HR to send forms, and for the manager to schedule orientation meetings.

Develop: Learning and Performance. Once the employee is onboarded, their development begins. The Learning Management System delivers required compliance training and optional development courses. The Performance and Goals module captures individual goals set at the start of the year, tracks progress, and facilitates the annual review process.

Grow: Succession and Compensation. For employees with high potential, the Succession Planning module helps managers identify and develop future leaders. Compensation Planning ensures that merit increases and bonuses are distributed according to policy and budget.

Retire/Offboard: When an employee leaves -- voluntarily or not -- the offboarding process in SuccessFactors handles exit tasks: revoking system access, processing final paycheck, and capturing knowledge transfer.

[SHOW DIAGRAM: A circular lifecycle diagram with five stages arranged clockwise. Stage 1: Recruit (Recruiting module). Stage 2: Hire/Onboard (Onboarding module). Stage 3: Develop (Learning + Performance). Stage 4: Grow (Succession + Compensation). Stage 5: Offboard (Exit Management). In the center of the circle: 'Employee Central -- Core HR Master Data.' Arrows showing the cyclical flow between stages.]

The hub of all of this is Employee Central -- the core HR system of record that stores the employee's fundamental data: name, position, department, manager, compensation, and employment status. Every other SuccessFactors module reads from and writes to Employee Central."

---

### [05:30 - 10:00] Employee Central and Payroll Integration

Cut to slide: "Employee Central -- The System of Record."

"Employee Central is SAP SuccessFactors' core HR module. Think of it the way we think about a Master Data record in SAP -- Employee Central is the system of record for every piece of information about an employee.

Employee Central stores: the employee's name and personal information, their position and reporting structure, their compensation (base salary, pay grade), their work schedule, their employment status, and their organizational assignment (which company code, cost center, or department they belong to).

The organizational structure in Employee Central maps to the SAP ERP financial structure. An employee assigned to a specific department in SuccessFactors is linked to a specific cost center in SAP FI. When payroll runs and posts wages to the General Ledger, it posts to the correct cost center automatically -- no manual account coding required.

[SHOW DIAGRAM: Employee Central record box showing fields: Employee ID, Name, Position Title, Department (Cost Center 1001), Manager, Base Salary, Employment Status. An arrow from Department field labeled 'Cost Center Mapping' pointing to a box labeled 'SAP FI Cost Center 1001 -- Marketing.' Below that, an arrow labeled 'Payroll Posting' pointing to a GL journal entry box: 'Dr: Payroll Expense (Cost Center 1001) / Cr: Bank.']

The payroll integration works like this: when a salary change is made in Employee Central -- a promotion, a merit increase, a new hire -- that change replicates automatically to Employee Central Payroll. At pay cycle time, the payroll engine uses the current Employee Central data to calculate wages for all active employees, applies tax withholdings and benefit deductions, and posts the net payroll expense to the General Ledger.

Exam note: The integration between Employee Central and payroll is real-time replication in the SuccessFactors architecture. Changes made in Employee Central flow to payroll automatically -- there is no batch file, no manual re-entry, and no risk of the two systems being out of sync."

---

### [10:00 - 14:00] Talent Management -- Performance, Learning, and Succession

Cut to slide: "Talent Management -- Growing Your Workforce."

"Talent management is the umbrella term for the SuccessFactors modules that focus on employee development and retention: Performance and Goals, Learning, Succession Planning, and Compensation.

Performance and Goals is the module that most employees interact with most often. At the start of the performance year, managers and employees collaborate to set goals aligned with the company's strategic objectives. Throughout the year, employees update goal progress and document achievements. At year-end, the manager completes a formal performance review using rating scales configured by HR. The review data feeds directly into compensation planning -- employees with higher ratings receive higher merit increase recommendations.

[SHOW DIAGRAM: A circular performance management cycle. Clockwise: Goal Setting (Jan) then Progress Check-In (Q2) then Mid-Year Review (Q3) then Year-End Review (Dec) then Compensation Planning (Jan of next year). Each stage is a box with arrows connecting them in a cycle. Center label: 'SuccessFactors Performance and Goals.']

The Learning Management System -- LMS -- delivers training content to employees. The LMS supports two types of learning: mandatory compliance training (safety, harassment prevention, data privacy) that must be completed by all employees within required time frames, and elective development training (leadership skills, technical certifications, software training) that employees choose to take.

Succession Planning identifies employees with high leadership potential and creates development plans to prepare them for more senior roles. The Succession module allows HR to identify position gaps -- positions where the current occupant is at risk of leaving -- and see which employees are ready now or ready soon to step into those roles.

Exam tip: On the SAP Associate exam, understand the distinction between these SuccessFactors modules. Performance and Goals is about employee evaluation. Learning is about training delivery. Succession is about talent pipeline and leadership development. Compensation is about pay distribution."

---

### [14:00 - 17:30] Payroll Calculation -- Concepts and GL Impact

Cut to slide: "Payroll -- The Math and the Posting."

"Payroll is one of the largest GL posting events in any company that runs payroll internally. Let me walk through the calculation structure and the financial entries.

A payroll cycle starts with time data -- how many hours did each employee work, including regular time, overtime, and any leave taken. For salaried employees, the regular amount is fixed per pay period. For hourly employees, the system multiplies hours worked by the hourly rate.

From gross pay, the payroll engine applies deductions: federal and state income tax withholding, Social Security and Medicare (FICA), health insurance premiums, 401k contributions, and any other voluntary deductions. The result is net pay -- what the employee actually receives.

The GL journal entry for a payroll run looks like this: Debit Wage Expense and Benefit Expense by cost center. Credit Payroll Clearing Account for the net pay amount. Credit Tax Liability Account for withheld taxes. Credit Benefits Payable for benefit deductions.

[SHOW DIAGRAM: A two-column journal entry table. Left column (Debits): Wage Expense -- Dept A: $45,000 / Wage Expense -- Dept B: $38,000 / Benefit Expense: $12,000. Right column (Credits): Payroll Clearing (net pay): $75,500 / Tax Withholding Liability: $14,200 / Benefits Payable: $5,300. Below: Total Debits = $95,000. Total Credits = $95,000. Note: 'Payroll Clearing is funded when the bank transfer is executed.']

The final step is the payment run -- the actual bank transfer to employee accounts. This is the same concept as the AP payment run we covered in Module 05, except now instead of paying vendors, we are paying employees.

One important feature of ERP payroll integration: every dollar of payroll expense is posted to the correct cost center. This enables the Controlling module to show department managers their actual versus budgeted headcount costs in real time -- without any manual allocation work."

---

### [17:30 - 21:00] HCM Integration Architecture

Cut to slide: "HCM Integration -- The Workforce Fabric."

"HCM integrates with every major ERP module. Let me map the key integration points.

HCM to FI: Payroll posts wage expenses to the General Ledger. Every pay cycle creates a journal entry that flows from SuccessFactors Payroll to SAP FI-GL. The posting assigns costs to the correct cost centers, which enables CO reporting by department.

HCM to MM: When project costing is used, an employee's time can be allocated to a specific project or work order in MM. This links labor costs to the specific project that consumed them.

HCM to SD: In service-based businesses, employees bill their time against customer engagements. HCM time data flows to SD to enable billing of professional services to customers.

HCM to FI-AA: When employees use company-owned assets -- vehicles, laptops -- those assets are linked to the employee assignment in Asset Accounting.

[SHOW DIAGRAM: Central box labeled 'SAP SuccessFactors HCM.' Four arrows going out: Arrow 1 pointing to 'FI-GL: Payroll journal entries by cost center.' Arrow 2 pointing to 'CO: Labor costs by cost center and profit center.' Arrow 3 pointing to 'SD: Time billing for professional services.' Arrow 4 pointing to 'FI-AA: Asset assignment to employee position.' Label at bottom: 'Employee Central is the master data hub -- all integration originates from EC records.']

The critical integration concept for this module: HCM is not an island. In modern SAP implementations, SuccessFactors and SAP S/4HANA operate as an integrated talent-to-transaction system. The same employee record that drives a payroll posting also drives cost center reporting, time billing, and succession planning. That is the enterprise value of an integrated HCM suite."

---

### [21:00 - 23:00] Module Summary and Exam Tips

Cut to slide: "Module 08 Key Takeaways."

"Key takeaways for Module 08:

One: HCM manages the complete employee lifecycle -- recruit, onboard, develop, grow, offboard. SAP's HCM platform is SuccessFactors.

Two: Employee Central is the core HR system of record. All other SuccessFactors modules read from and write to Employee Central.

Three: The Employee Central to Payroll integration is real-time replication. No manual re-entry. Changes made in Employee Central flow to payroll automatically.

Four: Talent management modules -- Performance and Goals, Learning, Succession, Compensation -- are the development and retention layer of HCM.

Five: Payroll posts wage expenses to the GL by cost center, enabling CO department-level cost reporting automatically.

Six: HCM integrates with FI for payroll GL posting, CO for cost center reporting, and SD for professional services time billing.

Exam tips: Know the SuccessFactors module names and their functions. Know that Employee Central is the system of record. Know that payroll integration to the GL is automatic and cost-center-aware. Know the difference between Performance and Goals (evaluation) and Learning (training delivery) -- these are commonly confused on scenario-based exam questions."

---

### [End Card]

Text on screen:

- Complete Reading Guide 08
- Complete Lab 08 (HCM Scenario Analysis)
- Complete Quiz 08 (10 questions)
- Post to Discussion Forum 08 (due Wednesday)
- Peer responses due Sunday
- Trailhead: trailhead.salesforce.com -- search "HR Basics"

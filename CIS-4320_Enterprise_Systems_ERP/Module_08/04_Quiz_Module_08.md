# Quiz: Module 08 - Human Capital Management Modules

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

Which data class is managed inside an ERP Human Capital Management (HCM) module?

* A) Product pricing lists and customer discount schedules
* B) Employee records, payroll, benefits, and timecard logs
* C) Firewall security configuration rules and network access control lists
* D) DNS zone files and domain registration records

* **Correct Answer:** B) HCM modules handle personnel files, payroll calculations, tax filings, benefits enrollment, and organizational structure mappings.
* **Distractor Analysis:**
  * *Why B is correct:* HCM is the ERP domain for workforce data — everything from hire date and job title to monthly pay calculation and leave balances is stored and processed here.
  * *Why A is incorrect:* Product pricing and discount schedules are managed in the Sales and Distribution (SD) or CRM pricing module, not HCM.
  * *Why C is incorrect:* Firewall rules and network access control lists are managed by the IT/network security team in infrastructure management tools, not in HCM.
  * *Why D is incorrect:* DNS records are network infrastructure configuration; they have no connection to HR or workforce management.

---

### Question 2

Which of the following best describes **performance metrics** in an HCM context?

* A) Database query execution statistics showing average response times for HR system reports
* B) Financial ratios used to evaluate the return on investment of the HCM system implementation
* C) Quantifiable measures — such as goal completion rates and 360-degree feedback scores — used to evaluate employee contribution and inform compensation and development decisions
* D) Network bandwidth utilization figures for the HCM application server

* **Correct Answer:** C) HCM performance metrics are employee-level measurements like goal attainment, competency ratings, and learning completions that feed into performance reviews, pay decisions, and succession planning.
* **Distractor Analysis:**
  * *Why C is correct:* SAP SuccessFactors Performance & Goals module captures these metrics and links them to the compensation planning and succession modules to create a data-driven talent management cycle.
  * *Why A is incorrect:* Database query statistics are IT performance metrics for system administrators, not HCM employee performance data.
  * *Why B is incorrect:* ROI analysis is a financial management exercise, not a definition of employee performance metrics within the HCM module.
  * *Why D is incorrect:* Network bandwidth figures are infrastructure metrics unrelated to HCM workforce performance measurement.

---

### Question 3

A new employee joins a company that uses SAP SuccessFactors. Which SuccessFactors module is responsible for managing the employee's initial paperwork completion, IT provisioning tasks, and day-one orientation assignments?

* A) Employee Central — core HR record maintenance and org structure management
* B) Recruiting — sourcing and candidate selection before the job offer
* C) Onboarding — the structured process of integrating a new hire with task assignments and compliance documentation
* D) Learning Management System (LMS) — delivering training courses to existing employees

* **Correct Answer:** C) The SAP SuccessFactors Onboarding module manages the new hire experience from offer acceptance through the first 90 days, automating task lists, document completion, and introductions.
* **Distractor Analysis:**
  * *Why C is correct:* SuccessFactors Onboarding creates task lists for HR, IT, and the hiring manager, sends the new employee forms to complete electronically, and tracks all steps to ensure compliance and a positive first experience.
  * *Why A is incorrect:* Employee Central maintains ongoing employee master data (position, pay grade, manager) after onboarding is complete; it does not manage the new hire task workflow.
  * *Why B is incorrect:* Recruiting manages the candidate pipeline before an offer is made; it ends when the candidate accepts and transitions to Onboarding.
  * *Why D is incorrect:* The LMS delivers ongoing training and certifications to the existing workforce; while new hires may also take courses, the onboarding task workflow is managed in the Onboarding module.

---

### Question 4

An employee works 45 hours in a week with a standard 40-hour work week. Their hourly rate is $20/hour and overtime is paid at 1.5x. Which ERP module calculates the correct gross pay and posts the resulting labor cost to the General Ledger?

* A) Accounts Payable (FI-AP) — which manages all outgoing payments including employee wages
* B) Material Management (MM) — which tracks the cost of all resources consumed in operations
* C) Payroll Processing in HCM — which calculates regular and overtime wages, applies deductions, and posts the net cost to the GL
* D) Sales and Distribution (SD) — which generates revenue transactions to offset employee costs

* **Correct Answer:** C) The HCM Payroll module calculates regular pay (40 × $20 = $800), overtime pay (5 × $30 = $150), applies tax and benefit deductions, and posts the resulting payroll journal entries to the General Ledger.
* **Distractor Analysis:**
  * *Why C is correct:* ERP payroll engines are configured with pay rules, tax tables, and GL account assignments; they automate the full calculation-to-posting cycle that would otherwise require manual spreadsheet work.
  * *Why A is incorrect:* Accounts Payable manages vendor invoice payments; employee payroll is processed through the HCM payroll module and posted separately, not through the AP invoice workflow.
  * *Why B is incorrect:* Material Management tracks physical inventory procurement costs; it does not calculate or post employee wage costs.
  * *Why D is incorrect:* Sales and Distribution generates revenue; it does not calculate or post employee compensation expenses.

---

### Question 5

A company is implementing SAP SuccessFactors and wants to ensure that when an employee is promoted and their salary increases, the change automatically flows to payroll for the next pay cycle without manual re-entry. Which integration capability makes this possible?

* A) Real-time replication from Employee Central (the system of record for employee master data) to Employee Central Payroll
* B) A nightly batch export of a flat CSV file from SuccessFactors emailed to the payroll department for manual entry
* C) A manual data entry step where HR administrators re-type salary changes into a separate payroll system
* D) A monthly reconciliation meeting where HR and payroll teams compare their respective spreadsheets

* **Correct Answer:** A) SAP SuccessFactors Employee Central replicates changes — including salary updates, position changes, and new hires — to Employee Central Payroll in real time, eliminating manual re-entry and ensuring payroll accuracy.
* **Distractor Analysis:**
  * *Why A is correct:* This is the core value proposition of having an integrated HCM suite: one data entry in Employee Central propagates to all downstream modules (payroll, learning, reporting) automatically.
  * *Why B is incorrect:* A manual CSV email process is a legacy integration pattern that creates data lag, errors from manual handling, and no audit trail — the opposite of what ERP integration should achieve.
  * *Why C is incorrect:* Manual re-entry in a separate system is precisely the functional silo problem that integrated ERP is designed to eliminate.
  * *Why D is incorrect:* Monthly reconciliation meetings are a compensating control for systems that do not integrate; they are time-consuming, error-prone, and do not prevent mid-month payroll errors.

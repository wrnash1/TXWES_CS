# Quiz: Module 04 - ERP Implementation Lifecycle

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

Why do ERP implementation projects historically have high failure rates?

* A) Lack of programming compilers compatible with the ERP platform
* B) Failure to manage organizational change and inadequate business process alignment
* C) Insufficient database disk space on the application server
* D) High network latency between the ERP server and client workstations

* **Correct Answer:** B) ERP success requires users to change how they work; resistance to new workflows and poor process design mapping leads to failure.
* **Distractor Analysis:**
  * *Why B is correct:* Research by Gartner and Prosci consistently identifies change management failure — not technical issues — as the leading cause of ERP project failure. Users who resist the new system undermine adoption regardless of how well the software is configured.
  * *Why A is incorrect:* ERP platforms ship with their own runtime environments; compiler compatibility is not a project risk factor.
  * *Why C is incorrect:* Storage is a commodity resource easily scaled; it is almost never the cause of ERP project failure.
  * *Why D is incorrect:* Network performance is a tunable infrastructure parameter; it does not explain strategic project failures.

---

### Question 2

In SAP's Activate methodology, during which phase does the project team hold Fit-to-Standard workshops to identify gaps between SAP standard functionality and the company's business requirements?

* A) Discover — the initial scoping and business case phase
* B) Prepare — the project setup and infrastructure provisioning phase
* C) Explore — the phase dedicated to Fit-to-Standard workshops and design documentation
* D) Realize — the configuration and development build phase

* **Correct Answer:** C) The Explore phase of SAP Activate is specifically dedicated to Fit-to-Standard workshops where the team documents how standard SAP processes cover business requirements and where gaps exist.
* **Distractor Analysis:**
  * *Why C is correct:* Fit-to-Standard is the defining activity of the Explore phase; it produces the delta design document that drives configuration decisions in the Realize phase.
  * *Why A is incorrect:* Discover focuses on evaluating the solution and building the business case; detailed process workshops have not yet started.
  * *Why B is incorrect:* Prepare focuses on project governance, infrastructure setup, and team onboarding, not process design workshops.
  * *Why D is incorrect:* Realize is where the team builds and configures the system based on the design already approved in Explore; gap identification should be complete before Realize begins.

---

### Question 3

A company's ERP go-live is two weeks away. The project manager discovers that 30% of migrated customer records have duplicate entries and missing address fields. Which action is most critical to take before go-live?

* A) Proceed with go-live and fix data quality issues post-launch using the ERP's built-in correction tools
* B) Halt the cutover, remediate the data quality issues in the staging environment, and re-run migration validation tests
* C) Delete all duplicate records and replace them with manually typed entries on go-live day
* D) Postpone go-live indefinitely until a third-party data quality vendor is contracted

* **Correct Answer:** B) Poor data quality is a leading cause of go-live failure; halting to remediate and re-validate migration data is the correct risk management action.
* **Distractor Analysis:**
  * *Why B is correct:* ERP systems depend on clean master data (customers, vendors, materials) from day one. Corrupted records in production create cascading errors in orders, invoices, and reports that are far more expensive to fix post-go-live.
  * *Why A is incorrect:* Going live with known data defects multiplies the problem — every transaction processed against bad records creates additional errors requiring correction.
  * *Why C is incorrect:* Manual data entry on go-live day under time pressure is an extremely high-risk approach that would likely introduce additional errors.
  * *Why D is incorrect:* Indefinite postponement is not proportionate; a structured remediation sprint with clear completion criteria is the appropriate response.

---

### Question 4

Which type of testing involves real business users validating that the configured ERP system meets their operational needs before the system goes live?

* A) Unit testing
* B) Integration testing
* C) Performance testing
* D) User Acceptance Testing (UAT)

* **Correct Answer:** D) User Acceptance Testing (UAT) is conducted by actual business users who execute real business scenarios to confirm the system behaves as expected before go-live sign-off.
* **Distractor Analysis:**
  * *Why D is correct:* UAT is the final quality gate before go-live. Business users — not IT staff — run end-to-end scenarios (e.g., creating a purchase order through to payment) and formally approve the system for production use.
  * *Why A is incorrect:* Unit testing validates individual configuration components or code modules in isolation, typically performed by the technical team, not end users.
  * *Why B is incorrect:* Integration testing validates that multiple modules work correctly together end-to-end; it is performed before UAT and by the technical or functional team.
  * *Why C is incorrect:* Performance testing measures system behavior under load (response time, throughput) and is conducted by technical specialists, not business users.

---

### Question 5

A company goes live on a new ERP system and experiences a critical payroll processing error affecting all employees on the first pay cycle. Which pre-go-live activity most directly should have caught this issue?

* A) Network infrastructure load balancing configuration
* B) End-to-end integration testing of the payroll process in a production-equivalent environment
* C) Vendor contract renegotiation for additional support hours post-go-live
* D) Expanding the hypercare team size after go-live

* **Correct Answer:** B) End-to-end integration testing of the payroll process using realistic data in a production-equivalent environment would have surfaced the error before it affected real employees.
* **Distractor Analysis:**
  * *Why B is correct:* Payroll is a high-stakes, time-sensitive process. Full-cycle integration testing — from timecard submission through payroll calculation to bank disbursement — in a system mirror of production is the standard mitigation for this risk.
  * *Why A is incorrect:* Network load balancing affects system availability and performance, not payroll calculation logic errors.
  * *Why C is incorrect:* Additional support contracts address incident response speed after an error occurs; they do not prevent the error from happening in the first place.
  * *Why D is incorrect:* A larger hypercare team can respond faster to issues post-go-live but cannot substitute for pre-go-live testing that prevents the issue from reaching production.

# Quiz: Module 04 - ERP Implementation Lifecycle

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### Question 1

Why do ERP implementation projects historically have high failure rates?

- A) Lack of programming compilers compatible with the ERP platform
- B) Failure to manage organizational change and inadequate business process alignment
- C) Insufficient database disk space on the application server
- D) High network latency between the ERP server and client workstations

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Research consistently identifies change management failure — not technical issues — as the leading cause of ERP project failure. Users who resist the new system or lack adequate training undermine adoption regardless of software quality.
- *Why A is incorrect:* ERP platforms ship with their own runtime environments; compiler compatibility is not a project risk factor.
- *Why C is incorrect:* Storage is a commodity resource easily scaled; it is almost never a cause of ERP project failure.
- *Why D is incorrect:* Network performance is a tunable infrastructure parameter; it does not explain strategic project failures.

---

### Question 2

In SAP's Activate methodology, during which phase does the project team hold Fit-to-Standard workshops to identify gaps between SAP standard functionality and the company's business requirements?

- A) Discover — the initial scoping and business case phase
- B) Prepare — the project setup and infrastructure provisioning phase
- C) Explore — the phase dedicated to Fit-to-Standard workshops and design documentation
- D) Realize — the configuration and development build phase

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The Explore phase of SAP Activate is specifically dedicated to Fit-to-Standard workshops where the team documents how standard SAP processes cover requirements and identifies gaps.
- *Why A is incorrect:* Discover focuses on evaluating the solution and building the business case; detailed process workshops have not yet started.
- *Why B is incorrect:* Prepare focuses on project governance, infrastructure setup, and team onboarding, not process design workshops.
- *Why D is incorrect:* Realize is where the team builds and configures the system based on the design already approved in Explore; gap identification should be complete before Realize begins.

---

### Question 3

A company's ERP go-live is two weeks away. The project manager discovers that 30% of migrated customer records have duplicate entries and missing address fields. Which action is most critical to take before go-live?

- A) Proceed with go-live and fix data quality issues post-launch using the ERP's built-in correction tools
- B) Halt the cutover, remediate the data quality issues in the staging environment, and re-run migration validation tests
- C) Delete all duplicate records and replace them with manually typed entries on go-live day
- D) Postpone go-live indefinitely until a third-party data quality vendor is contracted

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* ERP systems depend on clean master data from day one. Corrupted records in production create cascading errors in orders, invoices, and reports that are far more expensive to fix post-go-live.
- *Why A is incorrect:* Going live with known data defects multiplies the problem — every transaction processed against bad records creates additional errors.
- *Why C is incorrect:* Manual data entry under time pressure on go-live day is extremely high-risk and would likely introduce additional errors.
- *Why D is incorrect:* Indefinite postponement is disproportionate; a structured remediation sprint with clear completion criteria is the appropriate response.

---

### Question 4

Which type of testing involves real business users validating that the configured ERP system meets their operational needs before the system goes live?

- A) Unit testing
- B) Integration testing
- C) Performance testing
- D) User Acceptance Testing (UAT)

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* UAT is conducted by actual business users who execute real business scenarios to confirm the system behaves as expected. Business user sign-off on UAT is the formal approval to proceed to go-live.
- *Why A is incorrect:* Unit testing validates individual configuration components in isolation, performed by the technical team, not end users.
- *Why B is incorrect:* Integration testing validates that multiple modules work correctly together; it is performed before UAT and by the functional team.
- *Why C is incorrect:* Performance testing measures system behavior under load and is conducted by technical specialists, not business users.

---

### Question 5

A company goes live on a new ERP system and experiences a critical payroll processing error affecting all employees on the first pay cycle. Which pre-go-live activity most directly should have caught this issue?

- A) Network infrastructure load balancing configuration
- B) End-to-end integration testing of the payroll process in a production-equivalent environment
- C) Vendor contract renegotiation for additional support hours post-go-live
- D) Expanding the hypercare team size after go-live

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Payroll is a high-stakes, time-sensitive process. Full-cycle integration testing — from timecard submission through payroll calculation to bank disbursement — in a system mirror of production is the standard mitigation for this risk.
- *Why A is incorrect:* Network load balancing affects availability and performance, not payroll calculation logic errors.
- *Why C is incorrect:* Additional support contracts address response speed after an error occurs; they do not prevent the error from happening.
- *Why D is incorrect:* A larger hypercare team responds faster to issues post-go-live but cannot substitute for pre-go-live testing.

---

### Question 6

A company's AP team of 150 people will transition to a new SAP system in 8 weeks. Surveys show 60% of the team is anxious about learning the new system. The change manager recommends establishing a super-user network. Which description best reflects what super-users do and why they are more effective than IT helpdesk support alone?

- A) Super-users replace the IT helpdesk entirely and handle all technical issues reported by end users
- B) Super-users are frontline colleagues who receive advanced training and provide peer coaching, workflow guidance, and first-line support — they are more trusted by peers than outside consultants and understand the specific business context
- C) Super-users have administrative access to fix system configuration errors discovered after go-live
- D) Super-users monitor system performance dashboards and escalate technical errors to the Basis team

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Super-users' value comes from being trusted peers who understand both the new system and the team's actual job responsibilities. They bridge the gap between formal IT support and frontline employees in a way that outside consultants cannot.
- *Why A is incorrect:* Super-users complement the helpdesk; they do not replace it. Technical issues beyond their scope are escalated to IT.
- *Why C is incorrect:* Super-users are typically not given administrative or configuration access; they support users on process and workflow, not system administration.
- *Why D is incorrect:* System performance monitoring is a technical Basis/infrastructure responsibility, not a super-user function.

---

### Question 7

During an SAP Activate Realize phase, the functional consultant runs a test that validates whether the purchase order creation, goods receipt, and invoice verification transactions all post correct financial documents to the General Ledger when executed in sequence. Which type of testing is this?

- A) Unit testing — because it tests the FI module individually
- B) User Acceptance Testing — because it involves end-to-end business process scenarios
- C) Integration testing — because it validates that multiple modules (MM and FI) work correctly together across a connected sequence of transactions
- D) Performance testing — because it tests transaction response times under concurrent user load

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Integration testing validates that connected modules (in this case MM procurement transactions and FI financial postings) produce correct results when executed in sequence — exactly the scenario described.
- *Why A is incorrect:* Unit testing validates individual components in isolation; this test involves multiple modules interacting, which makes it integration testing.
- *Why B is incorrect:* UAT involves business users validating real business scenarios; this test is conducted by the functional consultant team, not end users — making it integration testing, not UAT.
- *Why D is incorrect:* Performance testing measures system behavior under load; this scenario describes functional correctness validation, not load testing.

---

### Question 8

Three months after an ERP go-live, 45% of the warehouse team still tracks inventory in a spreadsheet instead of the new system. The project post-mortem reveals that warehouse training was delivered in a 2-hour class the week before go-live and focused on navigating system screens rather than executing actual warehouse workflows. Which change management failure does this best illustrate?

- A) The ERP vendor delivered a defective inventory module that does not support the warehouse processes
- B) Training was delivered too late, was too short, and focused on software navigation rather than job-role workflows — causing users to lack ability and revert to familiar tools
- C) The warehouse team was not given administrative access to configure the inventory module for their specific processes
- D) The IT infrastructure was not powerful enough to support the warehouse team's transaction volume

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* This is the classic training failure pattern in ERP implementations: last-minute, screen-click-focused training that leaves users unable to actually perform their job in the new system. The result is reversion to familiar tools. The ADKAR Ability element was never achieved.
- *Why A is incorrect:* There is no evidence of a product defect; the scenario describes a training and adoption failure, not a software malfunction.
- *Why C is incorrect:* Warehouse users should not need administrative access; the issue is that they cannot perform their operational jobs in the system, not that they cannot configure it.
- *Why D is incorrect:* Infrastructure performance is unrelated to the described pattern of spreadsheet workarounds driven by unfamiliarity with the system.

---

### Question 9

A Salesforce implementation team is 3 weeks before go-live. A developer has just built a custom Flow in a Sandbox environment and verified it works correctly. What is the correct next step before the Flow can be used in production?

- A) The developer emails the Flow description to the System Administrator, who manually recreates it in production
- B) The Flow is tested by QA in the Sandbox, then deployed to production using a Change Set
- C) The developer directly edits production Flows using the Setup menu to add the new Flow
- D) The Flow is automatically published to all sandboxes and production simultaneously when saved

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Salesforce follows a Sandbox → Change Set → Production deployment model. Flows and other configuration changes built in Sandbox are packaged in a Change Set and deployed to production through a controlled process after QA review.
- *Why A is incorrect:* Manually recreating a Flow in production introduces errors and bypasses the quality control process; Change Sets exist specifically to prevent this.
- *Why C is incorrect:* Directly editing production configuration is a risk management violation in any enterprise deployment; changes should always come through the sandbox and change set pipeline.
- *Why D is incorrect:* Salesforce does not auto-publish Sandbox changes to production; sandbox and production are separate environments that must be synchronized through deliberate deployment actions.

---

### Question 10

A company's go-live cutover weekend reveals that the final data migration load completed successfully, but post-load validation shows that 8% of vendor master records are missing the bank account field required for electronic payments. The go-live window closes in 4 hours. Which is the correct response?

- A) Proceed with go-live and manually enter the missing bank account data for each affected vendor after go-live
- B) Execute the rollback plan to revert to the legacy system, remediate the missing bank account data in the migration source file, and schedule a new go-live date
- C) Proceed with go-live but disable the electronic payment process entirely until the data is fixed, routing all vendor payments through manual checks
- D) Delete all vendor records with missing bank accounts and recreate them manually during the first business week

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A documented rollback plan exists precisely for this scenario. Eight percent of vendors unable to receive electronic payments is a Critical/High defect that prevents normal AP operations; proceeding would cause payment failures, vendor relationship damage, and potential contractual penalties.
- *Why A is incorrect:* Manually entering bank accounts for potentially thousands of vendors post-go-live under production pressure is error-prone and delays payment operations. The data should be remediated before go-live, not after.
- *Why C is incorrect:* Disabling electronic payments forces all vendor payments to manual checks, creating a massive operational burden on the AP team and likely violating payment terms with vendors.
- *Why D is incorrect:* Deleting and manually recreating vendor records in production on day one is the highest-risk possible approach — every manual entry is a potential error in a live financial system.

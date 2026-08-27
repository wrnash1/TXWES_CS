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

---

### Question 11

(5 points)

Which SAP Activate phase immediately follows the Explore phase and is characterized by system configuration, custom development, and sprint-based build cycles?

- A) Discover
- B) Prepare
- C) Realize
- D) Deploy

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* After Explore (design and gap identification), the team enters the Realize phase where all configuration, custom development, and sprint-based build activities occur. The output of Realize is a fully configured and tested system ready for deployment.
  - *Why A is incorrect:* Discover precedes all other phases; it focuses on evaluating the solution and building the business case before the project is formally started.
  - *Why B is incorrect:* Prepare follows Discover and focuses on project governance, team onboarding, and infrastructure setup — it precedes Explore, not follows it.
  - *Why D is incorrect:* Deploy follows Realize and covers final testing, data migration cutover, training delivery, and go-live — it is the phase after the system is built, not during the build.

---

### Question 12

(5 points)

In the ADKAR change management model, what does the letter "K" represent, and which ERP implementation activity most directly builds this element?

- A) "Knowledge" — built through training programs that teach users how to perform their jobs in the new system
- B) "Kinetics" — built through system performance tuning to ensure the ERP responds fast enough for users
- C) "Keystroke" — built by having users practice keyboard shortcuts during training
- D) "Key-user" — built by designating super-users as the primary knowledge holders in each department

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* In ADKAR, K = Knowledge (knowing how to change). Training programs that teach users how to execute their job-role workflows in the new ERP system directly build the Knowledge element.
  - *Why B is incorrect:* "Kinetics" is not part of the ADKAR model; ADKAR stands for Awareness, Desire, Knowledge, Ability, Reinforcement.
  - *Why C is incorrect:* "Keystroke" is not an ADKAR element. While hands-on practice is part of Ability development, the K element specifically refers to conceptual and procedural knowledge.
  - *Why D is incorrect:* "Key-user" is an implementation role concept, not an ADKAR element. The K in ADKAR is Knowledge, not key-user designation.

---

### Question 13

(5 points)

A company plans to migrate 5 years of historical sales order data from their legacy system to SAP S/4HANA. During the Transform step of the ETL process, the team discovers that the legacy system stores dates in MM/DD/YYYY format but SAP requires YYYY-MM-DD. What is the correct action?

- A) Import the data as-is and let SAP automatically convert the date format during posting
- B) Write a transformation rule in the ETL process to convert all dates from MM/DD/YYYY to YYYY-MM-DD before loading into the target system
- C) Manually retype all date fields in the legacy system before exporting
- D) Remove all date fields from the migration scope to avoid the format conflict

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The Transform step in ETL (Extract, Transform, Load) exists precisely to handle format conversions, data cleansing, and structural mapping between source and target systems. Date format conversion is a standard transformation rule.
  - *Why A is incorrect:* SAP does not auto-convert date formats from incoming data loads; incorrectly formatted dates cause posting errors or silent data corruption.
  - *Why C is incorrect:* Manual retyping of thousands of date fields is impractical, error-prone, and defeats the purpose of automated data migration.
  - *Why D is incorrect:* Removing date fields would eliminate critical data (order dates, delivery dates, payment terms) that is required for historical reporting and compliance.

---

### Question 14

(5 points)

Which of the following describes the primary purpose of a **hypercare period** in an ERP implementation?

- A) A post-go-live phase with elevated support staffing and accelerated issue resolution to stabilize the system and build user confidence during the transition from legacy to new system
- B) A pre-go-live testing phase where the entire user population stress-tests the system simultaneously
- C) A vendor-managed warranty period during which the ERP vendor fixes all software defects at no charge
- D) A period of reduced system availability while the project team performs final configuration changes

- **Correct Answer:** A
- **Distractor Analysis:**
  - *Why A is correct:* Hypercare is the planned post-go-live stabilization period (typically 4-8 weeks) during which the full project team remains available, issues are triaged rapidly, and business users receive intensive on-the-floor support. It has defined exit criteria and transitions to normal IT support when the system is stable.
  - *Why B is incorrect:* Pre-go-live stress testing is performance testing, not hypercare. Hypercare occurs after go-live, not before.
  - *Why C is incorrect:* Hypercare is a project management construct, not a vendor warranty program. Software defect warranties are separate contractual terms.
  - *Why D is incorrect:* Hypercare does not involve reduced availability; the system is live and being actively used. Configuration changes during hypercare are handled through an emergency change process, not as a scheduled maintenance window.

---

### Question 15

(5 points)

A large company is running two ERP systems in parallel for three months after go-live — entering every transaction in both the legacy system and the new SAP system to compare outputs. What is this go-live strategy called, and what is its primary advantage?

- A) Big Bang cutover — all users switch simultaneously on a single date, minimizing the overall transition period
- B) Phased rollout — different business units go live on different dates to reduce risk
- C) Parallel run — both old and new systems operate simultaneously, allowing comparison of results before full decommission of the legacy system
- D) Pilot rollout — a small subset of users goes live first to validate the system before full deployment

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* A parallel run strategy operates both systems simultaneously, allowing the team to compare outputs (e.g., financial balances, inventory counts) and confirm the new system is producing correct results before fully cutting over. Its primary advantage is risk reduction; its primary disadvantage is the cost of double-entry.
  - *Why A is incorrect:* Big Bang cutover switches everyone at once on a single date — there is no parallel period comparing both systems.
  - *Why B is incorrect:* A phased rollout deploys the system to different business units or geographies sequentially, but each unit fully cuts over at its go-live date without running parallel.
  - *Why D is incorrect:* A pilot rollout deploys to a small user group first; the scenario describes all users entering every transaction in two systems, which is a parallel run.

---

### Question 16

(5 points)

Which of the following is the correct order of testing phases in an ERP implementation project?

- A) UAT → Integration Testing → Unit Testing → Performance Testing
- B) Unit Testing → Integration Testing → UAT → Performance Testing
- C) Performance Testing → Unit Testing → UAT → Integration Testing
- D) Integration Testing → UAT → Unit Testing → Performance Testing

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The correct sequence is: Unit Testing (individual components in isolation) → Integration Testing (connected modules working together) → UAT (business users validating real scenarios) → Performance Testing (system under load). Each phase validates a higher level of complexity and builds on the previous.
  - *Why A is incorrect:* UAT cannot precede integration testing; users cannot validate end-to-end scenarios if the modules have not yet been confirmed to work together.
  - *Why C is incorrect:* Performance testing requires a stable, fully integrated system to be meaningful; it cannot precede unit and integration testing.
  - *Why D is incorrect:* Integration testing must precede UAT; end users should not be the first to discover module integration failures.

---

### Question 17

(5 points)

A Salesforce implementation team is deploying changes from a Full Sandbox to Production. Which tool is the standard mechanism for moving configuration changes (custom objects, flows, validation rules) between Salesforce environments?

- A) Data Loader — used to export and import configuration metadata between orgs
- B) Change Sets — packages of metadata components deployed between connected Salesforce environments
- C) Workbench — a command-line tool for running SOQL queries against production
- D) AppExchange — the marketplace for installing third-party packages into production

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Change Sets are Salesforce's built-in tool for packaging and deploying metadata (configuration changes like flows, custom objects, page layouts, validation rules) from one environment to another. They are the standard deployment mechanism in Salesforce implementations.
  - *Why A is incorrect:* Data Loader is used to insert, update, delete, or export data records — not metadata configuration. It cannot move flows or custom objects between environments.
  - *Why C is incorrect:* Workbench is a browser-based tool for running SOQL queries and REST API operations; it is a developer utility, not a deployment mechanism for configuration changes.
  - *Why D is incorrect:* AppExchange installs managed packages (third-party applications) into an org; it does not deploy customer-built configuration changes between that customer's own environments.

---

### Question 18

(5 points)

During a Salesforce CRM implementation, the project team identifies that the company's sales process requires a custom approval workflow for discounts above 20%. This requirement cannot be met by standard Salesforce approval processes due to complex multi-level routing rules. What is the correct next step before building a custom solution?

- A) Immediately begin coding an Apex trigger to handle the multi-level routing
- B) Evaluate whether the requirement can be met through enhanced configuration of standard approval processes (e.g., multi-step approvals, delegated approvers) or an AppExchange managed package before committing to custom code
- C) Document the requirement as out of scope and remove it from the implementation
- D) Escalate to the CIO to request additional budget for custom development before evaluating any other options

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The configuration-before-customization principle requires fully exploring all declarative and packaged options before committing to custom code. Multi-step Salesforce approval processes are highly configurable; AppExchange also offers CPQ and approval routing packages that may meet the requirement without custom development.
  - *Why A is incorrect:* Writing Apex code before exhausting declarative options violates best practices and creates maintenance burden. Custom code should be the last resort.
  - *Why C is incorrect:* A business requirement for discount approval controls is a legitimate and important business need; it should not be removed from scope without fully exploring solutions.
  - *Why D is incorrect:* Budget escalation is premature before the team has determined whether the requirement can be met with existing tools. Cost estimates require a solution design to be meaningful.

---

### Question 19

(5 points)

A company's ERP implementation budget was $4 million. At project completion, the actual spend was $7.2 million and the go-live was 14 months late. Which factor is most strongly associated with ERP project cost overruns and schedule delays based on industry research?

- A) Insufficient server processing power in the hosting data center
- B) Underestimation of customization scope, data migration complexity, and change management effort during initial project planning
- C) The ERP vendor charging higher-than-quoted hourly rates for consulting services
- D) Excessive end-user training time that consumed project budget allocated for configuration

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Industry research (Gartner, McKinsey, SAP user groups) consistently identifies underestimation of scope — particularly customization, data migration, and change management — as the primary driver of ERP cost overruns. These areas are systematically underestimated in initial project plans.
  - *Why A is incorrect:* Infrastructure sizing is a technical problem with clear mitigation options (scale up); it is not the leading cause of major ERP overruns.
  - *Why C is incorrect:* While rate overruns occur, they represent a fraction of typical budget overruns; scope expansion is the dominant driver.
  - *Why D is incorrect:* Training investment is typically a small percentage of the total ERP project budget. Cutting training is more likely to cause adoption failure than to cause budget overruns.

---

### Question 20

(5 points)

What is the primary purpose of a **cutover plan** in an ERP go-live?

- A) To document the training curriculum for end users during the hypercare period
- B) To define the detailed sequence of technical and business tasks — with owners, start/end times, and go/no-go checkpoints — required to switch from the legacy system to the new ERP on go-live weekend
- C) To outline the vendor support contract terms for the first year of ERP operations
- D) To describe the long-term system optimization roadmap for the 3 years following go-live

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A cutover plan is the minute-by-minute (or hour-by-hour) execution playbook for go-live weekend. It sequences every task — final data migration runs, system configuration locks, legacy system freeze, user access provisioning, smoke testing, and go/no-go decision gates — with named owners and checkpoints.
  - *Why A is incorrect:* Training curriculum is managed in the training plan, not the cutover plan. Cutover is focused on technical and operational switching tasks.
  - *Why C is incorrect:* Vendor support terms are contractual documents negotiated well before go-live; they are not part of the cutover plan.
  - *Why D is incorrect:* Post-go-live optimization is managed in the operational roadmap or continuous improvement backlog; the cutover plan covers only the transition weekend activities.

# Video Script: Module 04 - ERP Implementation Lifecycle

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 22-24 minutes

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### [00:00 - 01:30] Opening

Professor Nash on camera. Title card: "Module 04 - ERP Implementation Lifecycle."

"Welcome back to CIS-4320. We've spent three modules understanding what enterprise systems are, how business processes work, and how organizations select vendors. Now comes the most operationally intense topic in this course: how do you actually implement an ERP system?

This is where things go wrong. Gartner estimates that 55 to 75 percent of ERP projects experience significant cost overruns, schedule delays, or fail to deliver expected business value. Companies have spent hundreds of millions of dollars on ERP implementations that never went live. The root causes are rarely technical — they are organizational, process, and data related.

Today we walk through the SAP Activate methodology for SAP implementations, the Salesforce implementation approach, change management, testing, go-live, and hypercare. These concepts are directly tested on both certifications."

---

### [01:30 - 05:30] SAP Activate Methodology

Cut to slide: "SAP Activate — The Six Phases."

"SAP Activate is SAP's official implementation methodology for S/4HANA projects. It replaced the older ASAP methodology and is built around three core principles: Agile delivery, continuous testing, and Fit-to-Standard process design.

SAP Activate has six phases. Let me walk through each one.

[SHOW DIAGRAM: A left-to-right horizontal flow with six labeled phases connected by arrows: Discover → Prepare → Explore → Realize → Deploy → Run. Below each phase, key activities listed.]

Phase one: Discover. This is the business case and scoping phase. The project team evaluates whether SAP S/4HANA meets their needs, reviews the SAP Best Practice content library, and builds the initial project business case. The Discover phase is often done before the contract is signed.

Phase two: Prepare. Project governance is established. The project team is formed, the system landscape is set up (development, quality, production environments), and project management infrastructure — timeline, risk register, communication plan — is put in place. Training for the project team begins.

Phase three: Explore. This is the BPM-intensive phase. The team holds Fit-to-Standard workshops where they walk through each standard SAP process with the business teams to identify how the standard covers requirements and where gaps exist. The output is the delta design document — the list of configurations and exceptions that must be built.

Phase four: Realize. The team configures the system based on the Explore phase design. Custom developments are built. Data migration programs are coded. Integration points are developed and tested. Unit testing and integration testing occur throughout this phase.

Phase five: Deploy. The system is prepared for go-live. User training is delivered. Data migration is executed. User acceptance testing is completed. The go-live cutover is executed — this is the weekend when the team loads production data, runs final validation checks, and flips the switch to go live.

Phase six: Run. This is everything after go-live — hypercare support, ongoing operations, continuous improvement, and eventually future wave releases."

---

### [05:30 - 09:00] Salesforce Implementation Approach

Cut to slide: "Implementing Salesforce — Discovery to Go-Live."

"Salesforce implementations, while generally shorter than SAP implementations, follow a similar lifecycle. The typical phases are:

Discovery: Requirements gathering, stakeholder interviews, process documentation.

Design: Data model design (objects, fields, relationships), security model design (profiles, permission sets, sharing rules), integration architecture.

Build: Configuration (custom objects, validation rules, flows, approval processes), integration development, data migration preparation.

Test: Unit testing of individual components, integration testing of end-to-end flows, user acceptance testing with business users.

Deploy: Production deployment via change sets or CI/CD pipeline, user training, go-live.

Hypercare: Intensive post-go-live support for the first 2-4 weeks.

[SHOW DIAGRAM: A circular lifecycle diagram showing the Salesforce phases: Discovery → Design → Build → Test → Deploy → Hypercare → Ongoing Administration. Arrows looping back from Ongoing Administration to Discovery to represent continuous improvement cycles.]

One key difference between Salesforce and SAP implementations: Salesforce implementations are typically faster — 3 to 6 months for a Sales Cloud deployment versus 12 to 24 months for a large SAP implementation — because Salesforce has less complexity in its standard configuration model and fewer integration requirements in many scenarios. However, large Salesforce implementations with complex integrations can take just as long as ERP projects."

---

### [09:00 - 13:00] Change Management

Cut to slide: "Why ERP Projects Fail — Change Management."

"I said at the opening that most ERP failures are not technical. Let me spend some time on the real cause: change management failure.

An ERP implementation does not just install new software. It changes how every employee does their job. The finance team will process invoices differently. The warehouse team will track inventory using a new system. The sales team may be required to use new CRM processes that feel foreign. If employees resist these changes — if they work around the system, enter data incorrectly, or keep using the old spreadsheets — the ERP investment is wasted.

Change management is the disciplined process of preparing people for change. In ERP projects, change management has four key components.

Stakeholder engagement: Senior leaders must visibly champion the project. When the CFO or CEO publicly communicates that the new system is a strategic priority, employees are more likely to invest in learning it.

Communication: Regular, honest communication about why the system is changing, what benefits employees can expect, and what the timeline looks like. Silence creates rumors and resistance.

Training: Users must be trained on the new processes, not just the software. The most common training mistake in ERP projects is training too late and too technically — showing employees how to click buttons rather than how the system supports their actual job responsibilities.

Super-user network: A team of departmental champions who receive advanced training and serve as peer coaches and first-line support after go-live. Super-users are far more trusted by frontline employees than outside consultants.

[SHOW DIAGRAM: A change management pyramid. Base level: Awareness (why are we changing?). Middle level: Understanding (how does this affect my job?). Upper level: Skill (can I do my job in the new system?). Top: Commitment (I support this change). Arrows indicating that all four levels must be achieved for successful adoption.]

Exam tip: When certification questions describe a scenario where employees are using workarounds or manual processes instead of the new ERP, the answer is almost always change management and/or training failure — not a technical defect."

---

### [13:00 - 16:30] Testing Phases

Cut to slide: "The Testing Ladder."

"Testing is one of the most underinvested activities in ERP projects. Organizations often compress testing timelines under schedule pressure — and pay for it in go-live defects. Let me walk you through the testing progression.

Unit testing: Individual configuration components or custom code are tested in isolation. 'Does this validation rule fire correctly when the Amount field is blank?' A developer or functional consultant runs unit tests. This is the first level of quality assurance.

Integration testing: End-to-end process scenarios are tested across multiple modules or systems. 'Does creating a Sales Order in SAP SD correctly trigger an inventory reservation in MM and create a financial document in FI?' This tests whether the integrated system works as designed. The functional team leads integration testing.

User Acceptance Testing (UAT): Real business users execute their actual business scenarios in the configured system to confirm it meets their operational needs. 'Can the AP clerk process a vendor invoice from receipt to payment?' UAT is the final quality gate before go-live. Business users — not IT — sign off on UAT. UAT sign-off is the formal approval to proceed to go-live.

Performance testing: The system is subjected to peak load conditions to validate that response times remain acceptable under realistic transaction volumes. This is especially important for high-volume processes like payroll runs, MRP planning runs, and end-of-period financial closes.

[SHOW DIAGRAM: A staircase with four steps. Step 1 (bottom): Unit Testing — Developer-led, individual components. Step 2: Integration Testing — Functional team, end-to-end processes. Step 3: UAT — Business users, real scenarios, formal sign-off. Step 4 (top): Performance Testing — Technical team, load and stress validation. Arrow pointing right labeled 'Increasing Business Relevance.']

Exam tip: The distinction between unit testing (IT-led, component-level) and UAT (business-led, end-to-end) is tested on both SAP and Salesforce certifications."

---

### [16:30 - 19:30] Data Migration and Go-Live

Cut to slide: "Data Migration and Cutover."

"Two of the highest-risk activities in any ERP implementation are data migration and go-live cutover. Let me cover each briefly — we dive deep into data migration in Module 12.

Data migration is the process of moving data from legacy systems into the new ERP. The challenge is that legacy data is almost always dirty: duplicate records, missing required fields, inconsistent formats, and outdated reference data. The ETL process — Extract, Transform, Load — is how migration is executed. You extract data from the source, transform it to match the target system's data model and business rules, then load it into the target.

A critical insight: every data defect loaded into the new ERP system on go-live day multiplies. A duplicate vendor record means every invoice processed against that vendor has potential payment errors. There is no such thing as 'we'll fix the data after go-live' — the errors cascade into every transaction before anyone catches them.

Go-live cutover is the precise sequence of steps executed during the final weekend before the new system goes live. Typically: freeze all transactions in the legacy system, complete the final data migration load, execute migration validation checks, obtain UAT sign-off confirmation, disable the legacy system's input, enable the new system for production use.

[SHOW DIAGRAM: A cutover timeline. Friday 5 PM: Legacy system input frozen. Friday 8 PM: Final data extraction. Saturday 2 AM: Data load begins. Saturday 10 AM: Migration validation. Saturday 2 PM: UAT sign-off confirmation. Sunday 6 AM: System available for production use. Sunday 8 AM: First transactions in new system. The timeline spans a 60-hour window.]

If go-live validation reveals critical errors, the team must either fix and re-validate, or execute the rollback plan — reverting to the legacy system and rescheduling go-live."

---

### [19:30 - 21:30] Hypercare and Module Summary

Cut to slide: "Hypercare and Key Takeaways."

"After go-live, the project enters hypercare — an intensive support period where the full project team remains available to resolve issues quickly. Hypercare typically lasts 2 to 8 weeks. During hypercare, defect resolution is prioritized over everything else. The project has a formal exit criteria — a list of conditions that must be met before hypercare ends and the system transitions to normal operations support.

Key takeaways for Module 04:

One: SAP Activate has six phases — Discover, Prepare, Explore, Realize, Deploy, Run. The Explore phase contains Fit-to-Standard workshops.

Two: Salesforce implementations follow Discovery → Design → Build → Test → Deploy → Hypercare.

Three: Change management — stakeholder engagement, communication, training, super-user network — is the most common cause of ERP failure. It is not technical.

Four: Testing follows a progression — unit, integration, UAT, performance. UAT is business-user-led and is the final sign-off before go-live.

Five: Data migration must produce clean data before go-live. Post-go-live data defects cascade.

Six: Go-live cutover follows a timed sequence and requires a rollback plan.

Exam tips: On SAP exams, memorize the phase names and what happens in each. The Explore phase = Fit-to-Standard. On Salesforce exams, know that UAT requires business users and is the final approval gate. On both exams, change management is always the answer when a question describes post-go-live adoption problems."

---

### [End Card]

Text on screen:

- Complete Reading Guide 04
- Complete Lab 04 (Implementation Risk Register)
- Complete Quiz 04 (10 questions)
- Post to Discussion Forum 04 (due Wednesday)
- Peer responses due Sunday
- Trailhead: trailhead.salesforce.com — search "User Acceptance Testing"

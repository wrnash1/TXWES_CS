# Video Script: Module 16 — ERP Certification Exam Preparation

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 24–28 minutes

---

## Pre-Production Notes

- Slide deck: 34 slides
- Diagrams: Salesforce Admin exam topic wheel (weighted categories), SAP S/4HANA Essentials topic map, implementation lifecycle comparison (ASAP vs. Salesforce), security model layers side-by-side, capstone scenario flow chart
- Key terms on screen: Salesforce Administrator Exam, SAP S/4HANA Essentials, Configuration vs. Customization, OWD, Role Hierarchy, Sharing Rules, ASAP, Business Blueprint, Fit-Gap, Cutover, Hypercare, KPI, Report Types, Data Quality
- End card: Lab 16, Quiz 16, Discussion Forum 16, Course Completion

---

## [00:00 – 02:30] Opening — The Finish Line

[PROFESSOR ON CAMERA]

This is Module 16. The last module of CIS-4320.

We have covered sixteen weeks of enterprise systems content: what ERP is and why it exists, how Salesforce and SAP are architected, the full functional landscape from Finance to Supply Chain to HR to CRM, security and roles, reporting and BI, and how these systems get implemented and go live in the real world.

Now we prepare to prove it.

This module has two purposes. First, a comprehensive review of everything covered in the course, organized around the two certification frameworks this class prepares you for: the Salesforce Administrator exam and the SAP S/4HANA Essentials certification. Second, a capstone implementation scenario that asks you to apply everything you have learned to a realistic enterprise decision-making challenge.

Certifications matter. They are the credential that tells an employer — before you walk into an interview — that you have put in the work, that your knowledge has been independently validated, and that you are serious about this field. A Salesforce Administrator certification on your resume gets you past the first resume filter at hundreds of companies. An SAP S/4HANA Essentials cert signals foundational enterprise ERP knowledge that most entry-level candidates do not have.

Let's prepare for both.

[SHOW TITLE SLIDE: Module 16 — ERP Certification Exam Preparation]

---

## [02:30 – 09:00] Salesforce Administrator Exam Review

[SHOW SLIDE: Salesforce Admin Exam — At a Glance]

The Salesforce Certified Administrator exam consists of 60 scored questions plus up to 5 unscored pilot questions, for a total of 65 questions. The passing score is 65%. You have 105 minutes. The exam is available through Webassessor at Trailhead (online proctored or at a testing center).

The exam covers seven weighted topic areas. I will review each one.

[SHOW SLIDE: Topic 1 — Configuration and Setup (20%)]

Configuration and Setup is the largest weighted category at 20% of the exam. Key topics:

Company Settings — fiscal year, business hours, currencies, language, and locale. Know that the default currency is set at the company level and that multi-currency must be enabled to use additional currencies.

User Management — creating users, assigning profiles and permission sets, managing login access, and understanding the difference between deactivating and freezing a user. Deactivating removes login access and reassigns the user's open records. Freezing immediately prevents login while the account remains active (used when you need to act quickly before fully offboarding).

Setup and navigation — understanding the Setup menu structure, using the Quick Find search, and navigating between object manager and setup options.

[SHOW SLIDE: Topic 2 — Object Manager and Lightning App Builder (20%)]

Object Manager and Lightning App Builder is also 20%. Key topics:

Standard vs. custom objects — when to use standard objects (Account, Contact, Lead, Opportunity, Case) and when custom objects are appropriate. Custom objects are used for data that does not fit existing standard objects.

Fields — data types (text, number, currency, date, date/time, checkbox, picklist, multi-select picklist, lookup, master-detail, formula, roll-up summary, auto-number, URL, email, phone). Know the rules: roll-up summary fields only work on master-detail relationships. Formula fields are read-only calculated values.

Page layouts vs. record types — page layouts control which fields appear and in what order on a record page. Record types control which picklist values are available and which page layout is assigned per record type.

Lightning App Builder — used to create and customize Lightning record pages, app pages, and home pages. Drag-and-drop components onto page regions.

[SHOW SLIDE: Topic 3 — Sales and Marketing Applications (12%)]

Sales and Marketing Applications covers 12%. Key topics:

Lead process — leads enter the system, are qualified, and are converted. Conversion creates an Account, Contact, and optionally an Opportunity. Converted leads are not deleted.

Opportunity management — stages, close date, amount, probability, and the sales process configuration. Know that forecast categories are driven by stage.

Campaigns — used to track marketing initiatives and measure ROI. Campaign members are leads or contacts associated with a campaign. Campaign influence tracks which campaigns contributed to closed opportunities.

Products and Price Books — standard and custom price books. A product must be added to a price book before it can be added to an opportunity as a line item.

[SHOW SLIDE: Topic 4 — Service and Support Applications (11%)]

Service and Support covers 11%. Key topics:

Cases — the core service object. Case origin (web, email, phone), status, priority, and escalation rules. Escalation rules automatically change case priority or reassign cases based on age or criteria.

Queues — pools of records that a group of users can work from. Cases can be assigned to a queue. Users take ownership by accepting a case from the queue.

Knowledge — a library of articles used to answer common questions. Knowledge articles have article types and are linked to cases. Agents can share article links with customers via email.

Entitlements — define the level of support a customer is entitled to. Entitlement processes enforce SLA milestones.

[SHOW SLIDE: Topic 5 — Productivity and Collaboration (7%)]

Productivity and Collaboration covers 7%. Key topics:

Activities — tasks and events. Tasks are to-do items with a due date. Events are calendar entries with a start and end time. Activities can be logged against accounts, contacts, leads, and opportunities.

Chatter — the internal collaboration feed. Users follow records, post updates, and tag colleagues. Chatter groups enable team collaboration spaces.

Einstein features — Einstein Activity Capture (syncs email and calendar), Einstein Lead Scoring, Einstein Opportunity Scoring. Know that these require additional licensing beyond base Salesforce.

[SHOW SLIDE: Topic 6 — Data and Analytics Management (14%)]

Data and Analytics Management covers 14%. Key topics:

Report types, formats, and features — covered extensively in Module 14. Know all four report types, dashboard components, dynamic dashboards, cross-filters, conditional highlighting, and subscriptions.

Data management — import tools (Data Import Wizard for up to 50,000 records; Data Loader for larger volumes and automation). Export tools (weekly and full data exports). Duplicate management (matching rules and duplicate rules).

[SHOW SLIDE: Topic 7 — Workflow/Process Automation (16%)]

Workflow and Process Automation covers 16%. Key topics:

Flow Builder — Salesforce's primary automation tool. Screen Flows (user-facing guided processes), Record-Triggered Flows (fire on record create/update/delete), Scheduled Flows (run at a defined time). Know that Workflow Rules and Process Builder are legacy tools being retired in favor of Flow.

Approval Processes — structured workflows where records require one or more approvals before a status change takes effect. Know the entry criteria, approval steps, actions (field updates, email alerts, tasks), and final approval/rejection actions.

Validation Rules — formula-based rules that prevent saving a record when data does not meet defined standards. Know that validation rules fire before record save and that the error message is displayed to the user.

[SHOW SLIDE: Exam Strategy — Salesforce Admin]

Three exam strategy points.

One — read the question twice before looking at the answers. Many questions are designed to test whether you read carefully. "Which of the following is NOT a valid action" requires different reasoning than "Which of the following IS a valid action."

Two — eliminate obviously wrong answers first. On most questions, one or two options are clearly incorrect. Eliminating them improves your odds on uncertain questions.

Three — flag and return. If a question is taking more than two minutes, flag it, move on, and return at the end. You have 105 minutes for 65 questions — about 97 seconds per question average. Do not let one hard question cost you time on five easy ones.

---

## [09:00 – 15:00] SAP S/4HANA Essentials Review

[SHOW SLIDE: SAP S/4HANA Essentials — At a Glance]

The SAP Certified Associate — SAP S/4HANA Essentials exam tests foundational knowledge of the SAP S/4HANA platform. It covers architecture, navigation, core functional modules, and implementation concepts. The exam has approximately 80 questions and requires a passing score of around 71%.

[SHOW SLIDE: SAP Architecture Fundamentals]

Architecture review: SAP S/4HANA runs on the SAP HANA in-memory database. The universal journal (table ACDOCA) consolidates all financial postings. The three-tier architecture separates the presentation layer (Fiori), application layer (SAP NetWeaver/ABAP application server), and database layer (HANA).

The three-system landscape: Development (DEV), Quality Assurance (QAS), and Production (PRD). Configuration changes flow through the transport system from DEV to QAS (for testing) to PRD.

[SHOW SLIDE: SAP Fiori Navigation]

SAP Fiori is the user interface. Fiori apps are categorized as: Transactional (for data entry and processing), Analytical (for reporting and dashboards), and Factsheet (for read-only master data display). The Fiori Launchpad is the starting screen — a tile-based home page where each tile opens an app. Users personalize their launchpad by adding, removing, and organizing tiles.

[SHOW SLIDE: SAP Core Modules — FI/CO]

Financial Accounting (FI): Company code is the central organizational unit for legal financial reporting. Key FI transactions include: FB50 (G/L journal entry), F-43 (vendor invoice), F-28 (customer payment), FA01 (asset creation). The document principle — every financial posting in SAP creates a document with a unique document number that can always be retrieved and reversed.

Controlling (CO): Cost centers collect costs by organizational unit. Profit centers track profitability by product line or division. Internal orders track costs for specific projects or events. The CO module is tightly integrated with FI — every FI posting that carries a cost automatically flows to the relevant CO object.

[SHOW SLIDE: SAP Core Modules — MM and SD]

Materials Management (MM): The procurement cycle runs from Purchase Requisition → Purchase Order (ME21N) → Goods Receipt (MIGO) → Invoice Verification (MIRO) → Payment. The three-way match validates that the PO, goods receipt, and invoice all agree before payment is released.

Sales and Distribution (SD): The order-to-cash cycle runs from Sales Order (VA01) → Delivery (VL01N) → Goods Issue → Billing (VF01) → Payment. Pricing in SD is controlled by condition types in pricing procedures. Credit management can automatically block sales orders that exceed a customer's credit limit.

[SHOW SLIDE: SAP Core Modules — HR and PP]

Human Resources (HCM): Organizational management defines the org structure (positions, jobs, organizational units). Personnel administration manages employee master data. Payroll runs via payroll areas and payroll schemas. Time management tracks work schedules, absences, and attendance.

Production Planning (PP): The production process flows from demand (sales order or forecast) → MRP run (Material Requirements Planning) → Planned Orders → Production Orders → Goods Issue (materials to production) → Goods Receipt (finished goods into inventory) → Settlement.

[SHOW SLIDE: SAP Security Review]

Authorization objects control what users can do in SAP. An authorization object contains up to ten authorization fields. Roles are collections of authorization objects. Users are assigned roles. The Separation of Duties principle requires that no single user has authorizations to perform both sides of a sensitive transaction (e.g., create vendor AND approve vendor payment).

Transaction SU53 shows a user the last failed authorization check — the starting point for access troubleshooting. Transaction SUIM runs reports on role assignments and authorization objects. SM20 is the security audit log.

[SHOW SLIDE: SAP Implementation Review]

ASAP phases: Project Preparation, Business Blueprint, Realization, Final Preparation, Go-Live and Support. The Business Blueprint fit-gap log identifies configuration gaps, development needs, and process changes. Custom development (ABAP) should be minimized. Cutover requires a detailed task list, rehearsal, and explicit go/no-go criteria. Hypercare follows go-live with intensive support.

---

## [15:00 – 19:30] 20 Practice Questions Overview

[SHOW SLIDE: Practice Questions — Format]

Your Quiz 16 and the lab both include practice questions. Let me walk through the logic of the 20 practice questions in the reading guide so you understand what they are testing and why.

The 20 questions cover the full course — not just Modules 14 and 15. Questions 1–7 cover Salesforce Administrator exam topics. Questions 8–14 cover SAP S/4HANA Essentials topics. Questions 15–20 cover implementation methodology and ERP concepts that span both certifications.

Each question is written in the style of the actual certification exams — a scenario followed by four plausible options. When you work through them, do not just check your answer. Read the distractor analysis for every question, including the ones you got right. Understanding why wrong answers are wrong is as important as knowing the right answer.

[SHOW SLIDE: High-Yield Review Topics]

Based on the content structure of both exams, the highest-yield review topics for exam preparation are:

For Salesforce Admin: the four report types and when to use each, the difference between profiles and permission sets, OWD and role hierarchy interaction, Flow vs. Workflow Rule vs. Approval Process, and the import/export tool selection criteria.

For SAP Essentials: the three-system transport landscape, the procure-to-pay document flow, the order-to-cash document flow, authorization objects and the role assignment model, and ASAP methodology phase deliverables.

These topics appear repeatedly across practice exams and are core to both certifications. Master these and you have a strong foundation.

---

## [19:30 – 24:00] Capstone Scenario Overview

[SHOW SLIDE: Capstone — Meridian Health Partners]

Your Lab 16 is a capstone scenario. You will be given a detailed description of a fictional organization — Meridian Health Partners, a regional healthcare network — and asked to make a series of interconnected ERP design and implementation decisions.

The scenario tests whether you can synthesize knowledge from across the full course. It is not a configuration exercise. It does not require you to log into Salesforce or SAP. It requires you to think like an ERP consultant advising a client.

The scenario has five decision points:

Decision 1 — Platform Selection. Given Meridian's business requirements, should they implement Salesforce Health Cloud, SAP S/4HANA, or both? What is the justification?

Decision 2 — Security Design. Meridian has strict data access requirements driven by HIPAA. How would you design the Salesforce security model to meet these requirements?

Decision 3 — Reporting Architecture. Meridian's CFO needs a daily financial dashboard and the VP of Operations needs a real-time patient services dashboard. How would you approach these two very different reporting requirements?

Decision 4 — Implementation Strategy. Meridian operates 14 clinics across three states. Should they use a big bang or phased cutover? What are the go/no-go criteria?

Decision 5 — Change Management. The majority of Meridian's staff are clinical workers — nurses and medical assistants — who have never used an enterprise software system before. What is your change management approach?

[SHOW SLIDE: Capstone Evaluation Criteria]

Your capstone response will be evaluated on: accuracy of your recommendations (do they reflect what was taught in this course?), quality of your justifications (do you explain why, not just what?), integration across topics (do you show how decisions in one area affect decisions in another?), and professional communication (is your response clear, organized, and at the standard of a consulting deliverable?).

There is no single correct answer for every decision. The quality of your reasoning matters as much as the conclusion you reach.

---

## [24:00 – 28:00] Course Closing and Certification Path

[SHOW SLIDE: What Comes Next]

You have completed CIS-4320. Let me tell you what to do with this knowledge.

If you are pursuing the Salesforce Administrator certification: create a free Salesforce Developer Org and a free Trailhead account. Complete the "Admin Beginner" and "Admin Intermediate" Trailhead trails. Schedule your exam through Webassessor. Trailhead Superbadges — especially the "Security Specialist" and "Reports and Dashboards" superbadges — are excellent exam preparation activities.

If you are pursuing the SAP S/4HANA Essentials certification: review the official SAP Training and Certification Shop at training.sap.com. The TS410 (Integrated Business Processes in SAP S/4HANA) is the recommended preparation course. SAP also offers a free Learning Journey on the SAP Learning Hub.

Both certifications are globally recognized, vendor-neutral in the sense that they validate real-world skills, and frequently listed as preferred qualifications in ERP-related job postings. Obtaining one or both certifications early in your career provides a significant advantage.

[SHOW SLIDE: A Final Thought]

One more thing before I close.

ERP systems are the operating infrastructure of the global economy. Every time a hospital orders supplies, a manufacturer ships a product, a paycheck is processed, or a customer service case is resolved at scale — there is almost certainly an ERP system involved. The professionals who configure, implement, and manage these systems are among the most valuable in the technology workforce.

You now have a foundation in this field. The certifications will validate it. Your career will build on it.

Good luck on your exams. It has been a privilege teaching this course.

[SHOW TITLE SLIDE: CIS-4320 — Complete]

[END CARD: Lab 16 | Quiz 16 | Discussion Forum 16]

---

*End of Video Script — Module 16*

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

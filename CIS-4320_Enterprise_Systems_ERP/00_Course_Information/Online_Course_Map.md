# Online Course Map

## CIS-4320 – Enterprise Systems & ERP

### 16-Week Schedule Grouped by Theme

---

## Overview

The course is organized into four thematic blocks. Each block builds on the previous — students must understand ERP foundations before they can make sense of CRM platforms, and they must understand both before tackling integration, security, and post-implementation operations.

| Block | Weeks | Theme | Certification Focus |
|---|---|---|---|
| Block 1 | Weeks 01–04 | ERP Foundations | SAP Certified Associate |
| Block 2 | Weeks 05–07 | SAP Functional Modules | SAP Certified Associate |
| Block 3 | Weeks 08–11 | Salesforce CRM Platform | Salesforce Certified Associate |
| Block 4 | Weeks 12–16 | Enterprise Operations & Cert Prep | Both |

---

## Block 1 — ERP Foundations (Weeks 01–04)

**Thematic goal:** Understand what enterprise systems are, why organizations use them, how to model business processes, how to evaluate and select ERP vendors, and the lifecycle of an ERP implementation project.

### Week 01 — Module 01: Enterprise Systems Overview and Business Process Integration

* **Core topics:** What ERP is; functional silos vs. integrated data; modular architecture; why organizations adopt enterprise platforms
* **Lab focus:** Mapping functional silos at a hypothetical retail company; identifying integration points
* **Trailhead:** Salesforce Platform Basics
* **Cert alignment:** SAP — understanding what ERP covers; Salesforce — understanding the platform's role in the enterprise

### Week 02 — Module 02: ERP Fundamentals – Business Process Management

* **Core topics:** BPMN 2.0 notation; swimlanes; events and gateways; AS-IS vs. TO-BE process mapping; process optimization
* **Lab focus:** Drawing a procurement BPMN diagram; analyzing bottlenecks; defining event gateways
* **Trailhead:** Business Process Automation
* **Cert alignment:** SAP — Fit-to-Standard workshop process modeling; Salesforce — understanding process logic that underlies Flows

### Week 03 — Module 03: ERP Fundamentals – SAP and Oracle Overview / Vendor Landscape

* **Core topics:** Major ERP vendors (SAP, Oracle, Microsoft Dynamics); selection criteria; Total Cost of Ownership (TCO); RFP process; SaaS vs. on-premise comparison
* **Lab focus:** Building a vendor scoring matrix; calculating 5-year TCO comparison
* **Resources:** SAP Product Catalog; Salesforce Platform Basics
* **Cert alignment:** SAP — SAP product portfolio knowledge; Salesforce — understanding SaaS deployment model positioning

### Week 04 — Module 04: ERP Implementation Methodology

* **Core topics:** SAP Activate phases (Discover, Prepare, Explore, Realize, Deploy, Run); Fit-to-Standard; testing types (Unit, Integration, UAT); go-live; change management
* **Lab focus:** Creating a project timeline Gantt chart; analyzing ERP failure case studies; writing a go-live cutover checklist
* **Trailhead:** Salesforce Rollout Strategy
* **Cert alignment:** SAP — SAP Activate methodology is directly tested; Salesforce — implementation lifecycle parallels

---

## Block 2 — SAP Functional Modules (Weeks 05–07)

**Thematic goal:** Understand the three core SAP module families — Financial Accounting, Supply Chain, and Human Capital Management — their internal structure, data flows, and integration points.

### Week 05 — Module 05: Financial Accounting in ERP (FI/CO)

* **Core topics:** General Ledger; Accounts Payable (three-way match); Accounts Receivable; Asset Accounting; Controlling (CO); period-end close sequence
* **Lab focus:** Tracing double-entry journal entries through the procure-to-pay cycle; mapping the three-way match; designing a balance sheet layout
* **Resources:** openSAP Financial Accounting in S/4HANA
* **Cert alignment:** SAP FI/CO — three-way match, Chart of Accounts, GL structure are core exam topics

### Week 06 — Module 06: Supply Chain Management in ERP (MM/WM)

* **Core topics:** Procure-to-pay cycle; Material Requirements Planning (MRP); inventory control; goods receipt (MIGO); vendor evaluation; stock types
* **Lab focus:** Manual MRP net requirements calculation; reorder point mapping; procure-to-pay flow diagram
* **Resources:** openSAP Materials Management
* **Cert alignment:** SAP MM — MRP planning run, three-way match, purchase order lifecycle are core exam topics

### Week 07 — Module 07: Human Resources in ERP (HCM/SuccessFactors)

* **Core topics:** SAP HCM vs. SAP SuccessFactors; Employee Central; payroll processing and GL posting; time tracking; employee onboarding; performance metrics; SuccessFactors module overview
* **Lab focus:** Tracing payroll data flow from timecard to GL; designing an onboarding task workflow; calculating gross pay with overtime
* **Resources:** openSAP SAP SuccessFactors overview
* **Cert alignment:** SAP HCM/SuccessFactors — SuccessFactors module functions and Employee Central integration are exam topics

---

## Block 3 — Salesforce CRM Platform (Weeks 08–11)

**Thematic goal:** Build hands-on proficiency with the Salesforce platform — its data model, objects, automation tools, integration capabilities, and security model — to prepare for the Salesforce Certified Associate exam.

### Week 08 — Module 08: CRM Fundamentals – Salesforce Platform Overview

* **Core topics:** What CRM is; Lead tracking; Lead conversion (Account/Contact/Opportunity); sales pipelines; account management; Cases and ticket systems; Sales Cloud vs. Service Cloud
* **Lab focus:** Creating Leads and converting them in Salesforce Developer org; mapping Lead-to-Opportunity conversion; designing Case escalation rules
* **Trailhead:** CRM for Lightning Experience
* **Cert alignment:** Salesforce Associate — Lead conversion, standard objects, CRM use cases are the highest-weighted exam topics

### Week 09 — Module 09: Salesforce Objects, Fields, and Relationships

* **Core topics:** Normalized tables; ACID properties; Salesforce object model; SOQL; Lookup vs. Master-Detail relationships; Schema Builder; data dictionaries; SAP SE11 ABAP Data Dictionary
* **Lab focus:** Building a custom object with relationships in Schema Builder; writing SOQL queries; analyzing an ERP ER diagram
* **Trailhead:** Data Modeling
* **Cert alignment:** Salesforce Associate — Salesforce data model, object relationships, and basic SOQL are exam topics

### Week 10 — Module 10: Salesforce Automation – Flows and Process Builder

* **Core topics:** Low-code tools (Flow Builder); Apex programming; ABAP; validation rules; database triggers; configuration vs. customization; governor limits; bulkification
* **Lab focus:** Creating a Validation Rule in Salesforce Developer org; writing Apex trigger pseudo-code; documenting test scenarios
* **Trailhead:** Apex Basics & Database
* **Cert alignment:** Salesforce Associate — declarative automation tools, when to use configuration vs. code, and Apex basics are exam topics

### Week 11 — Module 11: Salesforce Reports and Dashboards / Enterprise Application Integration

* **Core topics:** EAI principles; REST vs. SOAP APIs; middleware (MuleSoft); data transformation; point-to-point vs. hub-and-spoke; Remote Site Settings; batch vs. real-time integration; SAP iDoc
* **Lab focus:** Writing a JSON field mapping between SAP and Salesforce objects; drafting a middleware mapping table; tracing a REST API call cycle
* **Trailhead:** Integration Architecture
* **Cert alignment:** Salesforce Associate — Salesforce API access, Connected Apps, and integration patterns are exam topics

---

## Block 4 — Enterprise Operations & Certification Prep (Weeks 12–16)

**Thematic goal:** Master the operational disciplines of enterprise system management — data migration, security, cloud architecture, post-implementation management — and synthesize all course content for certification exam readiness.

### Week 12 — Module 12: ERP Integration – APIs and Middleware / Data Migration and Master Data Management

* **Core topics:** ETL (Extract, Transform, Load); data cleaning; deduplication; field mapping templates; validation checks; Salesforce Data Loader vs. Data Import Wizard; SAP LSMW
* **Lab focus:** Deduplicating a contact CSV; building a field mapping template; analyzing Data Loader error logs
* **Trailhead:** Data Management
* **Cert alignment:** Salesforce Associate — data import tools, deduplication, and data quality are exam topics; SAP — LSMW and data migration concepts

### Week 13 — Module 13: ERP Implementation Methodology / ERP Security and Access Control

* **Core topics:** RBAC; Separation of Duties (SoD); Salesforce security model layers (OWD, Role Hierarchy, Profiles, Permission Sets); SAP authorization objects; audit logs (SM20); SAP GRC
* **Lab focus:** Building a Salesforce role hierarchy; analyzing SoD conflicts; comparing Profile vs. Permission Set configurations
* **Trailhead:** Data Security
* **Cert alignment:** Salesforce Associate — security model layers are heavily tested; SAP — authorization concept and SoD are exam topics

### Week 14 — Module 14: Data Migration and Master Data Management / Cloud ERP Hosting

* **Core topics:** SaaS vs. PaaS vs. IaaS vs. on-premise; multi-tenant architecture; hybrid cloud; Salesforce release cadence (Spring/Summer/Winter); SAP S/4HANA deployment options; shared responsibility model
* **Lab focus:** Analyzing SaaS upgrade impacts; drawing a multi-tenant isolation diagram; creating a deployment model comparison table
* **Trailhead:** Salesforce Releases
* **Cert alignment:** Salesforce Associate — multi-tenancy, release cadence, and shared responsibility are exam topics; SAP — S/4HANA deployment options

### Week 15 — Module 15: ERP Security and Access Control / ERP Post-Implementation

* **Core topics:** Hypercare period; user adoption tracking; system performance reviews; bug severity classification; module upgrades (on-premise vs. SaaS); post-implementation KPIs; support tier model
* **Lab focus:** Designing a post-go-live user survey; analyzing performance metrics; writing a bug triage severity scheme
* **Trailhead:** Salesforce Optimizer
* **Cert alignment:** Both — post-implementation best practices and release management are operational competencies tested on both exams

### Week 16 — Module 16: Final Exam Prep & Salesforce/SAP Certification

* **Core topics:** Synthesis of all 16 modules; Salesforce Certified Associate exam structure and registration; SAP Certified Associate exam structure and registration; targeted gap-based study strategy; certification scheduling
* **Lab focus:** Building a full-course concept map; completing certification readiness checklist; practicing scenario analysis
* **Resources:** Salesforce Certified Associate Exam Guide; Associate Cert Prep Trailmix; openSAP certification prep courses
* **Deliverable:** Scheduled or planned exam date for Salesforce Certified Associate

---

## Cross-Course Certification Milestone Checkpoints

The following checkpoints align Trailhead badge milestones with exam readiness:

| After Week | Recommended Milestone | Exam Readiness Signal |
|---|---|---|
| Week 03 | Complete Salesforce Platform Basics badge | Ready for Module 08 CRM content |
| Week 08 | Complete CRM for Lightning Experience badge | 25% of Associate exam topics covered |
| Week 11 | Complete Data Modeling + Integration Architecture badges | 65% of Associate exam topics covered |
| Week 13 | Complete Data Security badge | 85% of Associate exam topics covered |
| Week 15 | Complete Associate Cert Prep Trailmix | Exam-ready; schedule sitting |
| Week 16 | Score 70%+ on final course practice exam | Clear to sit for Salesforce Certified Associate |

---

## Prerequisites

* CIS-1310 Introduction to Python or equivalent programming experience
* CIS-3312 Systems Analysis & Design (recommended; covers process modeling concepts reinforced in Module 02)
* Basic spreadsheet skills (Excel or Google Sheets) — required for data migration lab in Module 12

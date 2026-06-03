# Video Script: Module 16 — ERP Certification Exam Preparation and Capstone

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Production Notes

**Duration:** Approximately 30–35 minutes
**Format:** Comprehensive review lecture with integrated practice questions
**Segments:** 6 segments — Salesforce Admin review, SAP essentials review, integrated topics, exam strategy, capstone preview, course close

---

## Segment 1: Introduction — The Final Stretch (Lines 1–35)

[SLIDE: Title card — "Module 16: ERP Certification Exam Preparation and Capstone"]

Welcome to Module 16 — the final module of CIS-4320. I am Professor Nash. Congratulations on making it to the end of this course. Today we do something different. Instead of introducing new content, we consolidate everything you have learned across fifteen modules and connect it directly to the certification exam objectives.

[SLIDE: What we cover today]

We have six segments today. First, a targeted review of the Salesforce Administrator exam topic areas. Second, a summary of SAP S/4HANA Essentials exam topics. Third, we discuss cross-platform topics — integration, methodology, security — that appear on both exams and that connect the two systems conceptually. Fourth, exam strategy and logistics. Fifth, a preview of the capstone assignment. And finally, a brief course close.

[SLIDE: Both certifications — why pursue them]

The Salesforce Certified Administrator credential and the SAP Certified Foundation Associate — SAP S/4HANA Cloud Private Edition credentials represent real market value. Salesforce administrators with certification earn on average $92,000 to $115,000 annually in the United States as of 2025 data. SAP functional consultants with S/4HANA certifications are similarly well-compensated. But beyond compensation: these certifications signal to employers that you have validated, standardized knowledge — not just classroom theory.

[PAUSE]

---

## Segment 2: Salesforce Administrator Exam Review (Lines 36–95)

[SLIDE: Exam overview]

The Salesforce Certified Administrator exam contains approximately 60 questions. The passing score is 65%. The exam is available online with remote proctoring or at a Pearson VUE testing center. There is no penalty for guessing — answer every question.

The exam is organized into topic areas with specified percentage weights. Let me walk through each one.

[SLIDE: Organization Setup and Configuration — 20%]

The largest topic area. This covers: creating and managing users, password policies, login hours and IP restrictions, company information settings, fiscal year settings, currency management, and the Salesforce interface itself (App Manager, Lightning Experience).

Key facts: Only System Administrators can create users. Profile is mandatory for every user. The "Username" field must be globally unique across all Salesforce orgs — including sandboxes. Company-wide email settings affect all system-generated emails.

[SLIDE: Object Manager and Lightning App Builder — 20%]

This covers: creating and modifying custom objects, understanding the difference between standard and custom objects, field types and their appropriate use cases, record types, page layouts, compact layouts, and the Lightning App Builder for creating Lightning pages.

Key exam traps: Required fields behave differently from fields marked required on a page layout. A field marked required in the object manager cannot be left blank by any user or API call. A field marked required on a page layout enforces the requirement only through the UI — API calls and workflows can bypass it.

[SLIDE: Sales and Marketing Applications — 12%]

Covers the standard Sales Cloud objects and their relationships. Know: Account, Contact, Lead, Opportunity, Campaign, Campaign Member, Activity (Tasks and Events), and Products/Price Books.

Key relationships: Contact reports to Account. Lead is converted to Account, Contact, and Opportunity. Campaign Member links a Contact or Lead to a Campaign. Opportunity Products link Products to an Opportunity through a Price Book.

Lead conversion: when a lead converts, you can create a new account, new contact, and new opportunity — or match to existing records. Lead fields do not automatically map to converted record fields — you must configure the lead field mapping in Setup.

[SLIDE: Service and Support Applications — 11%]

Cases, Solutions, Knowledge Articles, Entitlements, and Milestones. The Salesforce Service Console is the interface optimized for service agents working multiple cases simultaneously. Entitlement Management defines service level agreements — how quickly cases must be responded to and resolved.

Key concept: Case queues allow cases to be assigned to a group of agents. Escalation Rules automatically reassign or notify if a case sits in a queue too long without being resolved.

[SLIDE: Activity Management and Chatter — 3%]

Tasks (to-do items) and Events (calendar entries) are both Activity records. Activities can be related to any standard object. Chatter is Salesforce's collaboration platform — follow records, post updates, @mention colleagues.

[SLIDE: Data Management — 10%]

Import Wizard, Data Loader, de-duplication rules, validation rules, and field update processes.

Import Wizard: good for up to 50,000 records, supports Accounts, Contacts, Leads, Campaign Members, and custom objects. No delete capability.

Data Loader: supports all standard and custom objects, up to 5 million records per batch, supports insert, update, upsert, delete, and hard delete. Requires Java installation.

Data quality: Duplicate Management uses Matching Rules (define how duplicates are identified) and Duplicate Rules (define what happens when a duplicate is detected — block or alert).

[SLIDE: Workflow / Process Automation — 12%]

Validation Rules, Workflow Rules (legacy), Process Builder (legacy), and Salesforce Flow. Flow is Salesforce's strategic automation platform — Salesforce has announced end-of-life for Workflow Rules and Process Builder, directing all new automation to Flow.

Flow types: Screen Flows (UI-based, user-initiated), Autolaunched Flows (triggered by a record event, schedule, or API), Scheduled Flows (run on a schedule).

Know when to use a Flow vs. a validation rule vs. an Apex trigger (Apex is code — admins should use Flow first).

[SLIDE: Security and Access — 14%]

Already covered in Module 13. Key exam points: FLS overrides page layout; role hierarchy grants upward record visibility; sharing rules can only open access, not restrict it; the running user on a dashboard controls data visibility; Field History Tracking retains 18 months of data.

[SLIDE: Reports and Dashboards — 13%]

Already covered in Module 14. Key exam points: matrix report for two-dimension cross-tab; joined report for combining multiple report types; bucket fields for in-report categorization; running user determines dashboard data visibility; "Manage Dashboards in Public Folders" permission required for public folder dashboard creation.

[PAUSE — transition to SAP review]

---

## Segment 3: SAP S/4HANA Essentials Exam Review (Lines 96–145)

[SLIDE: SAP certification overview]

The SAP Certified Foundation Associate credential for S/4HANA validates entry-level SAP knowledge. It tests conceptual understanding — you are not expected to configure SAP, but you must demonstrate you understand what each module does, how organizational elements are structured, and how key business processes work in SAP.

[SLIDE: SAP Organizational Structure — revisit]

The foundational organizational elements you must know:

**Client:** the highest level — separates tenants in a multi-company SAP system.

**Company Code:** the primary legal entity for financial accounting. Financial statements are produced at the company code level.

**Plant:** a production, storage, or distribution location. Key for Materials Management and Production Planning.

**Sales Organization / Distribution Channel / Division:** the three-level sales area structure for Sales and Distribution.

**Controlling Area:** the organizational unit for internal cost accounting.

**Purchasing Organization:** the unit responsible for procurement negotiations and contracts.

[SLIDE: Financial Accounting (FI) key concepts]

General Ledger: all financial postings aggregate to the G/L. The chart of accounts defines the G/L account structure. Company codes can share a chart of accounts or have their own.

Accounts Payable and Accounts Receivable are sub-ledgers that integrate with the G/L. Every vendor invoice posting in AP also creates a G/L entry. Every customer payment in AR also creates a G/L entry.

Document principle: every financial transaction in SAP creates a document with a document type, posting date, company code, and line items. Documents cannot be changed after posting — they can only be reversed. This is the audit trail.

[SLIDE: Materials Management (MM) key concepts]

The Procure-to-Pay (P2P) cycle: Purchase Requisition → Purchase Order → Goods Receipt → Invoice Verification → Payment.

Material Master: the central repository of all data for a material. Material types (raw material, finished product, trading goods) control which views are relevant. Industry sector affects field selections.

Movement types control goods movements: 101 = Goods Receipt for Purchase Order; 261 = Goods Issue to Production Order; 311 = Transfer Posting within plant.

[SLIDE: Sales and Distribution (SD) key concepts]

The Order-to-Cash (OtC) cycle: Inquiry → Quotation → Sales Order → Delivery → Goods Issue → Billing → Payment Receipt.

Condition technique: SAP's flexible pricing framework. Pricing procedures define the sequence of conditions (base price, discounts, surcharges, taxes) applied to calculate the net price.

Customer master: has three organizational levels — General Data (client level), Company Code Data (accounting), and Sales Area Data (sales-specific).

[SLIDE: Authorization Concept review]

Authorization Objects → Authorizations → Authorization Profiles → Single Roles → Composite Roles → User Master.

Know: PFCG creates and maintains roles. SU01 manages user master records. SU53 diagnoses authorization failures. PFCG Profile Generator creates the authorization profile from role menu entries automatically.

[SLIDE: SAP Integration Suite and IDocs]

IDoc: Intermediate Document — SAP's asynchronous document exchange format. Control Record + Data Records + Status Records.

RFC types: sRFC (synchronous, waits for response), aRFC (asynchronous, fire-and-forget), tRFC (transactional, exactly-once).

SAP Integration Suite: cloud-native integration platform on SAP BTP. Provides Cloud Integration (iFlows), API Management, Event Mesh.

OData: RESTful API standard used by SAP Fiori and S/4HANA API Business Hub.

[SLIDE: ASAP and SAP Activate]

ASAP phases: Project Preparation, Business Blueprint, Realization, Final Preparation, Go-Live and Support.

SAP Activate: Discover, Prepare, Explore, Realize, Deploy, Run. Agile sprints in Realize phase. Fit-to-standard philosophy.

[PAUSE — transition to cross-platform topics]

---

## Segment 4: Cross-Platform Topics and Integration Themes (Lines 146–185)

[SLIDE: The integration exam connection]

Both exams test integration at different depths. The Salesforce Admin exam tests integration from an administrative perspective: which API to use, how Connected Apps work, what Named Credentials do, what a Platform Event is. The SAP essentials exam tests integration from a conceptual perspective: what an IDoc is, what RFC types exist, what SAP Integration Suite does.

At the professional level, integrating SAP and Salesforce in a single enterprise architecture is one of the most common real-world scenarios. MuleSoft — a Salesforce company — is one of the primary tools used for this.

[SLIDE: Security principles across platforms]

Both platforms share the fundamental principle of least privilege. Both use a role-based access control model. Both have audit mechanisms.

Salesforce: Profile + Permission Sets + OWD + Role Hierarchy + Sharing Rules + FLS.

SAP: Authorization Object → Authorization → Profile → Role → User.

Both platforms require SoD enforcement. Both have tools to help: Salesforce through process design and approval workflows; SAP through GRC Access Control.

[SLIDE: Reporting and BI across platforms]

Both platforms produce operational reports for day-to-day management. Salesforce's native reports and dashboards serve CRM operational needs. SAP's Fiori analytical tiles serve operational reporting on S/4HANA data.

Both platforms have a strategic BI layer. Salesforce has CRM Analytics (Einstein Analytics). SAP has SAP Analytics Cloud backed by BW/4HANA.

In many large enterprises, both systems' data is loaded into a neutral data warehouse (Snowflake, BigQuery) for unified reporting.

[SLIDE: Implementation methodology shared principles]

Both ASAP and Salesforce implementation lifecycle share the same fundamental structure: discover requirements, design the solution, build and configure, test, train, go live, support.

The key difference is pace and complexity. SAP S/4HANA full implementations take 12–36 months. Focused Salesforce implementations can deliver in 8–16 weeks. But both involve change management, data migration, cutover planning, and hypercare.

[SLIDE: Data quality is universal]

Data quality issues appear in every ERP implementation regardless of platform. The ETL phases — Extract, Transform, Load — are where data quality problems are discovered and remediated. Both platforms have tools: Salesforce's duplicate management, Data Loader validation, and import rules; SAP's MDG (Master Data Governance) and migration cockpit tools.

[PAUSE]

---

## Segment 5: Exam Strategy and Logistics (Lines 186–215)

[SLIDE: Salesforce exam logistics]

The Salesforce Certified Administrator exam is delivered through Webassessor (now Kryterion). You can schedule at a Pearson VUE testing center or remotely. The exam costs $200. Retake costs $100. Salesforce offers Trailhead — a free, gamified learning platform with modules, projects, and trails specifically designed for certification preparation.

My strong recommendation: complete the "Prepare for Your Salesforce Administrator Credential" Trailmix on Trailhead. It maps directly to exam topic areas and includes hands-on challenges in a free Trailhead Playground org.

[SLIDE: Salesforce exam strategy]

Read every question completely before looking at the answer choices. ERP exam questions frequently include a specific qualifier — "as an administrator," "without writing code," "using the least number of steps" — that determines the correct answer.

Eliminate obviously wrong answers first. For Salesforce Admin questions, if an answer choice involves writing Apex code, it is almost always wrong — admins use declarative tools, not code.

Watch for absolute language: "always," "never," "the only way." ERP questions rarely have only one way to accomplish something.

Time management: 60 questions in 105 minutes = 1 minute 45 seconds per question. Flag uncertain questions and return to them after completing the rest.

[SLIDE: SAP exam logistics]

SAP certification exams are administered through the SAP Training and Certification hub. Exams can be taken online with remote proctoring. Costs vary by certification; expect approximately $500–$600 USD for a professional certification. SAP Learning Hub and the SAP Help Portal provide preparation materials.

[SLIDE: Study strategy for both exams]

Practice questions are the single most effective preparation tool. For the Salesforce Admin exam: Salesforce Ben's practice exams, Focus on Force, and the official Salesforce study guide are all well-regarded. For SAP: the SAP Certification Preparation materials on the SAP Learning Hub are authoritative.

For this course: the 20 practice questions in the capstone lab provide a representative sample. Review each wrong answer and trace it back to the reading guide content that covers the topic.

[PAUSE]

---

## Segment 6: Capstone Preview and Course Close (Lines 216–240)

[SLIDE: The Capstone Assignment]

The Module 16 capstone assignment brings together the entire course. You will receive a detailed business scenario — a company with both SAP S/4HANA and Salesforce environments — and you will produce a written analysis and implementation recommendation covering all major course topics:

- Integration architecture between SAP and Salesforce
- Security model design for both platforms
- Reporting and BI architecture recommendation
- Implementation methodology and change management plan
- TCO analysis

The capstone is worth 25% of your final course grade. Full instructions are in the Lab document.

[SLIDE: Course topics summary — the full arc]

Let me give you the complete view of what we covered in this course.

Modules 1–3 laid the foundation: what ERP is, the major vendors, and the SAP organizational structure.

Modules 4–6 covered Salesforce — the platform, Sales Cloud, and Service Cloud.

Modules 7–9 covered SAP functional modules — Financial Accounting, Materials Management, and Sales and Distribution.

Modules 10–11 covered master data governance and ERP analytics.

Modules 12–13 covered integration, middleware, security, and access control.

Modules 14–15 covered reporting and BI, then implementation methodology.

And now Module 16 brings it all together for certification and the capstone.

[SLIDE: Career paths]

Where does this knowledge take you? The most in-demand roles for CIS graduates with ERP knowledge:

Salesforce Administrator: typically the entry point, $75,000–$95,000.

Salesforce Consultant: 3–5 years experience, $100,000–$140,000.

SAP Functional Analyst (FI, MM, or SD): $90,000–$120,000.

SAP S/4HANA Consultant: $120,000–$160,000 with 5+ years.

ERP Project Manager: broad demand across all platforms, $110,000–$150,000.

[SLIDE: Final message]

ERP systems are the backbone of global commerce. The skills you have developed in this course — understanding how businesses process transactions, how data flows between systems, how security is enforced, how implementations succeed or fail — are skills that remain relevant across technology platforms and across decades.

The certification exams validate a baseline. What you build on top of that baseline through hands-on experience, continuing education, and professional network is what defines a career.

I have genuinely enjoyed teaching this course. Complete the capstone, take the certification exams, and bring what you've learned into the workplace. You're ready.

Good luck. I'll see you at graduation.

[END OF VIDEO SCRIPT]

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*

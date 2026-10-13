# Quiz: Module 01 - Enterprise Systems Concepts

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

### Question 1

What is the primary business value of implementing an Enterprise Resource Planning (ERP) system?

- A) It lets developers write custom Python games
- B) It integrates business data from disparate departments (finance, sales, inventory) into a single database system
- C) It removes the need for web servers
- D) It speeds up local CPU clock cycles

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* ERP consolidates finance, sales, HR, and supply chain data into one shared database, eliminating conflicting records across departments and creating a single source of truth.
- *Why A is incorrect:* ERP targets integration of business logistics, not programming languages or game development.
- *Why C is incorrect:* ERP relies on web and application servers; it does not replace them.
- *Why D is incorrect:* ERP is application-layer software and has no effect on CPU clock speed.

---

### Question 2

In an enterprise system context, which of the following best describes **functional silos**?

- A) Separate departmental systems that store data independently and cannot automatically share information with other departments
- B) A type of database index that improves query performance on large tables
- C) The process of combining multiple company subsidiaries under one legal entity
- D) A network security zone that isolates sensitive servers from the public internet

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Functional silos describe the pre-ERP state where each department runs its own disconnected system, making enterprise-wide reporting difficult and requiring manual reconciliation.
- *Why B is incorrect:* This describes a database index, not an organizational data-sharing problem.
- *Why C is incorrect:* Legal entity consolidation is an accounting concept unrelated to silo architecture.
- *Why D is incorrect:* This describes a network DMZ security pattern, not an organizational data problem.

---

### Question 3

A company's finance department records a customer payment, but the sales team's system still shows the invoice as unpaid. Which ERP design principle directly resolves this inconsistency?

- A) Modular architecture
- B) Integrated data with a shared database layer
- C) Role-based access control
- D) Multi-tenant cloud hosting

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A shared database means one transaction updates one record visible to all modules simultaneously, eliminating the discrepancy between Finance and Sales.
- *Why A is incorrect:* Modular architecture describes how the system is organized into components, not how data is kept consistent across departments.
- *Why C is incorrect:* Role-based access controls who can see data, not whether data is kept consistent.
- *Why D is incorrect:* Multi-tenancy is a cloud hosting model and does not directly determine data consistency within one tenant's system.

---

### Question 4

Which of the following best describes **modular architecture** in the context of SAP or Oracle ERP?

- A) Each business function (Finance, HR, Supply Chain) is a separately activatable component that still shares a common underlying database
- B) The ERP system runs on multiple physical servers in different geographic regions
- C) Users can customize the color theme and layout of the application interface
- D) The vendor releases software updates on a monthly rolling schedule

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* SAP's module structure (FI, MM, SD, HCM) is the textbook example — each handles a distinct function but all read from and write to the same central database.
- *Why B is incorrect:* Geographic distribution describes infrastructure redundancy, not modular software design.
- *Why C is incorrect:* UI personalization is a user preference feature, not an architectural pattern.
- *Why D is incorrect:* Release schedules are a vendor delivery practice, not an architectural design characteristic.

---

### Question 5

A mid-size manufacturer wants to eliminate duplicate supplier records that exist in three separate departmental databases. Which approach represents the best enterprise systems solution?

- A) Ask each department to manually reconcile their spreadsheets quarterly
- B) Implement an ERP system with a centralized vendor master record shared by all departments
- C) Deploy a separate data warehouse that copies records from each system nightly
- D) Grant each department read-only access to one another's separate databases

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* An ERP centralized vendor master record ensures all departments — Procurement, Finance, and Receiving — reference one authoritative supplier record in real time.
- *Why A is incorrect:* Manual quarterly reconciliation is the silo problem ERP is designed to replace; it does not solve the root cause.
- *Why C is incorrect:* A nightly data warehouse copy introduces lag and still allows three systems to diverge during the day.
- *Why D is incorrect:* Read-only cross-access still leaves three separate authoritative records that can diverge; it does not create a single source of truth.

---

### Question 6

Which of the following correctly distinguishes back-office ERP functions from front-office CRM functions?

- A) ERP manages customer sales pipelines; CRM manages vendor payments and inventory
- B) ERP manages internal operations such as accounting, procurement, and payroll; CRM manages customer-facing processes such as sales, marketing, and support
- C) ERP and CRM perform identical functions but are sold by different vendors
- D) ERP is used only by manufacturing companies; CRM is used only by service companies

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The back-office/front-office distinction is one of the most tested concepts in this course. ERP handles internal operations; CRM handles customer interactions. Many enterprises run both, integrated through middleware.
- *Why A is incorrect:* This reverses the definitions entirely. Sales pipeline management belongs to CRM; vendor payments belong to ERP.
- *Why C is incorrect:* ERP and CRM serve fundamentally different parts of the business and have different data models, modules, and processes.
- *Why D is incorrect:* Both ERP and CRM are used across all industries — manufacturing, retail, financial services, healthcare, and more.

---

### Question 7

SAP S/4HANA uses the SAP HANA in-memory database as its technical foundation. What is the primary operational benefit of this architecture for ERP workloads?

- A) It eliminates the need for user authentication and password management
- B) It allows the database to process both transactional (OLTP) and analytical (OLAP) workloads on the same platform with high speed, replacing the need for a separate reporting data warehouse for many use cases
- C) It automatically converts all ABAP code to Java for compatibility with non-SAP systems
- D) It stores all data permanently in the CPU cache, eliminating the need for disk storage

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* SAP HANA's in-memory columnar design allows it to run real-time analytics directly on live transactional data, which previously required a separate data warehouse and overnight batch extracts.
- *Why A is incorrect:* Database architecture has no connection to authentication management; SAP uses separate identity and access management controls.
- *Why C is incorrect:* SAP HANA does not convert ABAP code; ABAP remains the primary language for SAP application logic regardless of the database.
- *Why D is incorrect:* In-memory databases use RAM as the primary working storage layer but still persist data to disk for durability; CPU cache is not a database storage layer.

---

### Question 8

A company currently runs three separate systems: QuickBooks for accounting, Salesforce for CRM, and a custom inventory tool. The CEO wants one system to be the authoritative source for customer credit limits. Which approach best achieves this?

- A) Print the credit limit report from QuickBooks monthly and distribute it by email to all teams
- B) Designate one system as the master for credit limit data and use integration to propagate that value to the other systems, so all three always reflect the same number
- C) Allow each system to maintain its own credit limit value and resolve conflicts at month-end
- D) Remove credit limit tracking from all three systems and manage it in a spreadsheet owned by the finance director

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Establishing a single system of record (master) for each data element and using integration to synchronize downstream systems is the foundational ERP/integration architecture principle for eliminating data conflicts.
- *Why A is incorrect:* Monthly email distribution creates lag and does not prevent the three systems from showing different values between distribution cycles.
- *Why C is incorrect:* Tolerating conflicting values until month-end is exactly the functional silo problem ERP is designed to eliminate; it creates errors in credit decisions made throughout the month.
- *Why D is incorrect:* Moving the data to a spreadsheet removes it from all three systems entirely and introduces all the risks of manual, uncontrolled data management.

---

### Question 9

Which SAP module code corresponds to Financial Accounting — the module responsible for the General Ledger, Accounts Payable, and Accounts Receivable?

- A) MM (Materials Management)
- B) SD (Sales and Distribution)
- C) FI (Financial Accounting)
- D) PP (Production Planning)

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* SAP FI (Financial Accounting) is the core financial module containing the General Ledger (FI-GL), Accounts Payable (FI-AP), Accounts Receivable (FI-AR), and Asset Accounting (FI-AA). Memorizing SAP module codes is directly tested on the SAP Associate exam.
- *Why A is incorrect:* MM (Materials Management) handles procurement and inventory management, not financial accounting.
- *Why B is incorrect:* SD (Sales and Distribution) manages sales orders, pricing, and shipping — not the general ledger.
- *Why D is incorrect:* PP (Production Planning) manages manufacturing orders and capacity planning, not financial transactions.

---

### Question 10

A student is reviewing for the Salesforce Certified Associate exam and reads that Salesforce delivers three major releases per year. Which release names correctly identify Salesforce's annual release schedule?

- A) Version 1, Version 2, Version 3
- B) Q1, Q2, Q3
- C) Spring, Summer, Winter
- D) Alpha, Beta, General Availability

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Salesforce uses seasonal names — Spring, Summer, and Winter — for its three annual releases. This naming convention and the three-per-year cadence are specifically tested on the Salesforce Certified Associate exam as a key characteristic of the SaaS platform model.
- *Why A is incorrect:* Salesforce does not use version numbers in the same way traditional software products do; it uses seasonal release names.
- *Why B is incorrect:* Q1/Q2/Q3 are fiscal quarter labels, not Salesforce release names. Salesforce delivers three releases but they are not named by fiscal quarter.
- *Why D is incorrect:* Alpha/Beta/GA are software development lifecycle stages used during a feature's development, not the names of Salesforce's annual production releases.

---

### Question 11

(5 points)

Which of the following best describes the concept of **Total Cost of Ownership (TCO)** when evaluating an ERP investment?

- A) The one-time software license fee paid to the ERP vendor at contract signing
- B) The full financial cost over the system's useful life, including licenses, implementation labor, training, customization, infrastructure, and ongoing support
- C) The annual subscription fee charged by a SaaS ERP vendor
- D) The hardware cost of servers required to run the ERP system on-premise

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* TCO encompasses all costs over the system's lifetime — not just the initial purchase price. Exam questions on vendor selection and investment justification require understanding that implementation labor and ongoing support often far exceed the license fee.
  - *Why A is incorrect:* The one-time license fee is only one component of TCO; many ERP projects spend 3-5x the license cost on implementation services alone.
  - *Why C is incorrect:* An annual subscription fee is a recurring cost component, but it still excludes implementation, training, customization, and integration costs that are part of TCO.
  - *Why D is incorrect:* Hardware costs are one infrastructure component of TCO but do not represent the full scope of the concept, which includes people, process, and technology costs.

---

### Question 12

(5 points)

An organization's General Ledger, Accounts Payable, and Accounts Receivable are all managed in which SAP S/4HANA module?

- A) CO (Controlling)
- B) MM (Materials Management)
- C) SD (Sales and Distribution)
- D) FI (Financial Accounting)

- **Correct Answer:** D
- **Distractor Analysis:**
  - *Why D is correct:* SAP FI (Financial Accounting) owns external financial reporting — the General Ledger (FI-GL), Accounts Payable (FI-AP), Accounts Receivable (FI-AR), and Asset Accounting (FI-AA). These are legal reporting requirements.
  - *Why A is incorrect:* CO (Controlling) handles internal management accounting — cost centers, profit centers, and internal orders — not external financial statements.
  - *Why B is incorrect:* MM handles procurement and inventory logistics, not financial accounting records.
  - *Why C is incorrect:* SD handles customer-facing sales processes — order entry, pricing, shipping — not the General Ledger or payables/receivables.

---

### Question 13

(5 points)

A company moves from three separate departmental databases to a single ERP system. After go-live, a sales order entered by a sales representative automatically reduces the available inventory count without any additional data entry. This outcome is an example of which ERP characteristic?

- A) Role-based access control
- B) Process integration through a shared data model
- C) Multi-tenant cloud hosting
- D) Customization via configuration tables

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The automatic propagation of a sales order into inventory — with no manual re-entry — demonstrates ERP's core value: integrated processes sharing a common data model so one transaction automatically updates all relevant modules.
  - *Why A is incorrect:* Role-based access control determines who can perform which actions; it does not describe automatic data propagation across modules.
  - *Why C is incorrect:* Multi-tenancy is a cloud architecture model describing how multiple customers share infrastructure; it is unrelated to automatic data propagation between business modules.
  - *Why D is incorrect:* Configuration tables allow system behavior to be adjusted without code changes, but they do not explain why one transaction updates multiple modules simultaneously.

---

### Question 14

(5 points)

Which of the following correctly identifies Salesforce's deployment model?

- A) On-premise only — customers install Salesforce on their own data center servers
- B) Hybrid — customers choose between on-premise and cloud deployment at implementation time
- C) SaaS only — Salesforce has no on-premise deployment option; all customers run on Salesforce's shared cloud infrastructure
- D) Private cloud only — each customer receives a dedicated cloud server managed by Salesforce

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Salesforce is exclusively a SaaS platform. Unlike SAP, which offers on-premise, private cloud, and public cloud options, Salesforce has always been cloud-only. This distinction is frequently tested on the Salesforce Certified Associate exam.
  - *Why A is incorrect:* Salesforce has no on-premise installation option — this is one of its defining architectural characteristics.
  - *Why B is incorrect:* There is no hybrid deployment choice for Salesforce; customers cannot move workloads to their own hardware.
  - *Why D is incorrect:* Salesforce uses a multi-tenant architecture where many customers share infrastructure, not dedicated private servers per customer.

---

### Question 15

(5 points)

**Master data** differs from **transactional data** in which of the following ways?

- A) Master data changes with every business transaction; transactional data rarely changes
- B) Master data is core reference data (vendors, customers, materials) that is reused across many transactions; transactional data is the record of individual business events that reference master data
- C) Master data is stored in a separate database from transactional data in all ERP systems
- D) Master data is created by the ERP vendor during installation; transactional data is created by IT administrators

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Master data (vendor master, customer master, material master) is stable reference information shared across processes. Transactional data (purchase orders, invoices, deliveries) represents individual business events and references master data records.
  - *Why A is incorrect:* This reverses the relationship — master data is relatively stable; transactional data is created continuously as business events occur.
  - *Why C is incorrect:* In an ERP system, master data and transactional data typically reside in the same shared database — separation would reintroduce the silo problem.
  - *Why D is incorrect:* Master data is created and maintained by business users (purchasing managers creating vendor records, etc.), not by the ERP vendor or IT administrators during installation.

---

### Question 16

(5 points)

An enterprise runs SAP S/4HANA for back-office operations and Salesforce for CRM. A salesperson closes a deal in Salesforce and the corresponding sales order must appear in SAP within minutes. Which integration architecture pattern best satisfies this requirement?

- A) Batch/scheduled integration running nightly
- B) Real-time event-driven integration triggered by the Opportunity close event in Salesforce
- C) Manual export from Salesforce to a CSV file imported into SAP each morning
- D) Read-only cross-database access where SAP queries the Salesforce database directly

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A real-time event-driven integration fires when the Salesforce Opportunity is marked Closed-Won, immediately creating the corresponding SAP sales order via middleware (e.g., MuleSoft or SAP BTP). This meets the "within minutes" requirement.
  - *Why A is incorrect:* Nightly batch integration would create a gap of up to 24 hours between the Opportunity close and the SAP sales order — not acceptable for time-sensitive order fulfillment.
  - *Why C is incorrect:* Manual CSV export is a manual, error-prone process that introduces significant lag and human effort, negating the integration benefits.
  - *Why D is incorrect:* Direct cross-database queries between different vendor systems are not a standard or supported integration pattern; each system uses proprietary data structures not designed for external direct access.

---

### Question 17

(5 points)

In the SAP organizational hierarchy, which level represents the highest scope, containing all company codes, plants, and other organizational units within a single SAP installation?

- A) Plant
- B) Company Code
- C) Client
- D) Storage Location

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* In SAP, the Client is the highest organizational level. All data within a Client is logically separate from data in other Clients. A Client can contain multiple Company Codes (legal entities), which contain multiple Plants, which contain multiple Storage Locations.
  - *Why A is incorrect:* A Plant is an operational unit (factory, distribution center) that sits below the Company Code level in the hierarchy.
  - *Why B is incorrect:* A Company Code represents one legal entity (e.g., a subsidiary) and sits below the Client level; one Client can contain many Company Codes.
  - *Why D is incorrect:* A Storage Location is the lowest physical storage unit (a specific warehouse area), sitting below the Plant level.

---

### Question 18

(5 points)

Which of the following describes the role of **middleware** in an enterprise integration architecture?

- A) A database management system that stores ERP master data
- B) Software that sits between two or more systems and handles data mapping, transformation, routing, authentication, and error handling to enable them to communicate
- C) A user interface layer that displays data from multiple ERP modules on one screen
- D) A programming language used to write custom ERP reports

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Middleware (e.g., MuleSoft, SAP Integration Suite, Dell Boomi) acts as a translation and routing layer between systems with different data formats and protocols, handling the technical complexity of connecting SAP to Salesforce, legacy systems, or third-party applications.
  - *Why A is incorrect:* A database management system stores data; middleware manages data movement and transformation between systems, not storage.
  - *Why C is incorrect:* A unified user interface or dashboard is a front-end presentation layer; middleware operates at the system-to-system integration layer, not the display layer.
  - *Why D is incorrect:* ABAP is the programming language for SAP customization; it is not a middleware product. Middleware is a separate category of platform software.

---

### Question 19

(5 points)

A regional hospital uses separate systems for patient scheduling, billing, pharmacy, and lab results. A patient's allergy information recorded at check-in is not visible to the pharmacy when dispensing medication. This scenario illustrates which of the following enterprise systems concepts?

- A) Single source of truth achieved through ERP integration
- B) The functional silo problem — isolated systems that cannot automatically share critical data
- C) Role-based access control preventing the pharmacy from viewing patient data
- D) Master data corruption caused by data migration errors

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The hospital scenario is a classic functional silo problem — each department operates an isolated system, and critical patient safety data (allergies) cannot flow automatically to dependent departments (pharmacy), creating operational and safety risks.
  - *Why A is incorrect:* Single source of truth is the goal of ERP integration — the scenario describes the opposite: a silo problem where there is no shared truth.
  - *Why C is incorrect:* The question says the pharmacy cannot see allergy data, not that it is restricted from seeing it by a security policy. Role-based access control is a designed security restriction, not a system isolation problem.
  - *Why D is incorrect:* Master data corruption describes data quality problems from poor migration; the scenario describes an architectural isolation problem, not corrupted data.

---

### Question 20

(5 points)

Which of the following statements about SAP S/4HANA's in-memory architecture is accurate?

- A) SAP HANA stores all data exclusively in CPU registers, making disk storage unnecessary
- B) SAP HANA uses a columnar in-memory database that allows analytical queries to run on live transactional data, reducing the need for separate overnight batch extracts to a data warehouse
- C) SAP HANA requires all customizations to be rewritten in Java before they can be deployed
- D) SAP HANA is a standalone reporting tool that supplements traditional SAP ECC but does not replace it

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* SAP HANA's columnar in-memory design allows OLTP and OLAP workloads to coexist on the same data, enabling real-time analytics on live business data — a key architectural differentiator from traditional row-based databases that required overnight ETL jobs to populate a separate data warehouse.
  - *Why A is incorrect:* CPU registers are the processor's internal computation space, not a database storage medium. HANA stores data in RAM (main memory) for speed and persists to disk for durability.
  - *Why C is incorrect:* SAP continues to use ABAP as its primary language on HANA; no Java rewrite is required. HANA compatibility required some ABAP optimization but not a language change.
  - *Why D is incorrect:* SAP S/4HANA is the full replacement for SAP ECC (the previous generation ERP), not a supplementary reporting add-on. S/4HANA runs the complete ERP suite on the HANA database.

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

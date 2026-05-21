# Quiz: Module 01 - Enterprise Systems Concepts

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

What is the primary business value of implementing an Enterprise Resource Planning (ERP) system?

* A) It lets developers write custom Python games
* B) It integrates business data from disparate departments (finance, sales, inventory) into a single database system
* C) It removes the need for web servers
* D) It speeds up local CPU clock cycles

* **Correct Answer:** B) ERP breaks down departmental silos by providing a single source of truth for business transaction data.
* **Distractor Analysis:**
  * *Why B is correct:* ERP consolidates finance, sales, HR, and supply chain data into one shared database, eliminating conflicting records across departments.
  * *Why A is incorrect:* ERP targets integration of business logistics, not programming languages or compilers.
  * *Why C is incorrect:* ERP relies on web and application servers; it does not replace them.
  * *Why D is incorrect:* ERP is application-layer software and has no effect on CPU clock speed.

---

### Question 2

In an enterprise system context, which of the following best describes **functional silos**?

* A) Separate departmental systems that store data independently and cannot automatically share information with other departments
* B) A type of database index that improves query performance on large tables
* C) The process of combining multiple company subsidiaries under one legal entity
* D) A network security zone that isolates sensitive servers from the public internet

* **Correct Answer:** A) Functional silos are isolated departmental systems that prevent automatic data sharing, leading to inconsistent reporting and duplicated effort.
* **Distractor Analysis:**
  * *Why A is correct:* Functional silos describe the pre-ERP state where each department runs its own disconnected system, making enterprise-wide reporting difficult.
  * *Why B is incorrect:* This describes a database index, not an organizational data-sharing problem.
  * *Why C is incorrect:* Legal entity consolidation is an accounting concept unrelated to silo architecture.
  * *Why D is incorrect:* This describes a network DMZ security pattern, not an organizational data problem.

---

### Question 3

A company's finance department records a customer payment, but the sales team's system still shows the invoice as unpaid. Which ERP design principle directly resolves this inconsistency?

* A) Modular architecture
* B) Integrated data with a shared database layer
* C) Role-based access control
* D) Multi-tenant cloud hosting

* **Correct Answer:** B) Integrated data with a shared database layer ensures that a payment posted in Finance instantly updates the same record visible to Sales.
* **Distractor Analysis:**
  * *Why B is correct:* A shared database means one transaction updates one record visible to all modules simultaneously, eliminating the discrepancy.
  * *Why A is incorrect:* Modular architecture describes how the system is organized into components, not how data is synchronized.
  * *Why C is incorrect:* Role-based access controls who can see data, not whether data is kept consistent.
  * *Why D is incorrect:* Multi-tenancy is a cloud hosting model and does not directly determine data consistency within one tenant's system.

---

### Question 4

Which of the following best describes **modular architecture** in the context of SAP or Oracle ERP?

* A) Each business function (Finance, HR, Supply Chain) is a separately activatable component that still shares a common underlying database
* B) The ERP system runs on multiple physical servers in different geographic regions
* C) Users can customize the color theme and layout of the application interface
* D) The vendor releases software updates on a monthly rolling schedule

* **Correct Answer:** A) Modular architecture means specialized components for each business function can be independently licensed and activated while sharing one common data layer.
* **Distractor Analysis:**
  * *Why A is correct:* SAP's module structure (FI, MM, SD, HCM) is the textbook example — each handles a distinct function but all read from and write to the same central database.
  * *Why B is incorrect:* Geographic distribution describes infrastructure redundancy, not modular software design.
  * *Why C is incorrect:* UI personalization is a user preference feature, not an architectural pattern.
  * *Why D is incorrect:* Release schedules are a vendor delivery practice, not an architectural design characteristic.

---

### Question 5

A mid-size manufacturer wants to eliminate duplicate supplier records that exist in three separate departmental databases. Which approach represents the best enterprise systems solution?

* A) Ask each department to manually reconcile their spreadsheets quarterly
* B) Implement an ERP system with a centralized vendor master record shared by all departments
* C) Deploy a separate data warehouse that copies records from each system nightly
* D) Grant each department read-only access to one another's separate databases

* **Correct Answer:** B) An ERP centralized vendor master record ensures all departments — Procurement, Finance, and Receiving — reference one authoritative supplier record in real time.
* **Distractor Analysis:**
  * *Why B is correct:* The vendor master in SAP MM/FI is a canonical example of how ERP eliminates duplicate records through a single shared data object.
  * *Why A is incorrect:* Manual quarterly reconciliation is the silo problem ERP is designed to replace; it does not solve the root cause.
  * *Why C is incorrect:* A nightly data warehouse copy introduces lag and still allows three systems to diverge during the day.
  * *Why D is incorrect:* Read-only cross-access still leaves three separate authoritative records that can diverge; it does not create a single source of truth.

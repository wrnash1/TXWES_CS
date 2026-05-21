# Quiz: Module 14 - Cloud ERP Hosting

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

What is a defining characteristic of a multi-tenant cloud database design?

* A) Each customer has their own dedicated physical server and isolated database instance
* B) Multiple customers share the same application infrastructure and database platform, with logical isolation enforcing data privacy between tenants
* C) All customer data is stored in an unencrypted shared table visible to all users of the platform
* D) The database only supports read-only SQL queries and does not allow data modification

* **Correct Answer:** B) Multi-tenancy allows cloud providers to scale infrastructure efficiently by sharing physical resources among customers while enforcing strict logical data isolation between tenants.
* **Distractor Analysis:**
  * *Why B is correct:* Salesforce's multi-tenant architecture is the textbook example — all customers share the same application code, database servers, and platform services, but each org's data is logically separated so no tenant can see another's records.
  * *Why A is incorrect:* Dedicated physical servers per customer describes single-tenant architecture (e.g., a private cloud or dedicated hosting), which is the opposite of multi-tenancy.
  * *Why C is incorrect:* Multi-tenant platforms use robust logical isolation and encryption to ensure tenants cannot access each other's data; the shared infrastructure does not mean shared data visibility.
  * *Why D is incorrect:* Multi-tenant databases support full read/write operations; read-only restrictions describe reporting replicas or data warehouse configurations, not the multi-tenant model itself.

---

### Question 2

Which of the following best describes **Software as a Service (SaaS)** in the context of ERP and CRM deployment?

* A) A model where the customer purchases and installs software on their own servers and manages all infrastructure
* B) A cloud delivery model where the vendor hosts and maintains the complete application stack and the customer accesses it through a web browser, managing only data and configuration
* C) A development platform where customers build custom applications on top of a vendor-provided runtime environment
* D) A model where infrastructure resources (compute, storage, network) are rented from a cloud provider but the customer installs and manages their own software

* **Correct Answer:** B) SaaS means the vendor owns and operates the entire technology stack — hardware through application — and customers pay a subscription fee for access without managing any infrastructure.
* **Distractor Analysis:**
  * *Why B is correct:* Salesforce and SAP S/4HANA Cloud Public Edition are the primary SaaS examples in this course. The customer's IT team configures the application and manages users/data; the vendor handles all infrastructure, patching, and upgrades.
  * *Why A is incorrect:* This describes an on-premise deployment, where the customer owns and operates all infrastructure and software, which is the opposite of SaaS.
  * *Why C is incorrect:* This describes Platform as a Service (PaaS) — Salesforce Platform (Force.com) is a PaaS offering, distinct from the SaaS CRM application layer.
  * *Why D is incorrect:* This describes Infrastructure as a Service (IaaS) — renting compute and storage resources while managing your own OS and software stack, as with AWS EC2 or Azure VMs.

---

### Question 3

A company runs SAP ERP on-premise for their core financial and manufacturing processes, while using Salesforce CRM in the public cloud for their sales team. What cloud architecture pattern does this represent?

* A) Full public cloud — all workloads run on the same public cloud platform
* B) Private cloud — all workloads run on dedicated customer-owned infrastructure
* C) Hybrid cloud — a combination of on-premise or private cloud for some workloads and public cloud services for others
* D) Multi-cloud — multiple competing public cloud platforms used for the same workload simultaneously

* **Correct Answer:** C) Hybrid cloud describes the combination of on-premise (SAP ERP) and public cloud (Salesforce) environments connected through integration middleware.
* **Distractor Analysis:**
  * *Why C is correct:* The hybrid cloud model is extremely common in large enterprises that have invested in on-premise ERP infrastructure but adopted cloud CRM. The two systems are typically integrated through middleware like MuleSoft to exchange customer and order data.
  * *Why A is incorrect:* Full public cloud would require all workloads — including the SAP ERP — to run on a public cloud platform; keeping SAP on-premise disqualifies this classification.
  * *Why B is incorrect:* Private cloud describes workloads on dedicated, customer-controlled infrastructure; Salesforce running on Salesforce's shared public infrastructure is not private cloud.
  * *Why D is incorrect:* Multi-cloud specifically refers to using multiple public cloud providers (e.g., both AWS and Azure) for similar workloads; having one on-premise and one public cloud system is hybrid, not multi-cloud.

---

### Question 4

In Salesforce's SaaS model, how many major release updates does Salesforce deliver per year, and how is this different from on-premise ERP upgrade management?

* A) One major release per year; same as on-premise where customers control upgrade timing
* B) Three major releases per year (Spring, Summer, Winter) delivered automatically to all customers; on-premise customers control their own upgrade schedule and can defer for years
* C) Six monthly releases delivered only to enterprise-tier customers; smaller customers receive annual updates
* D) Continuous deployment with daily updates; on-premise systems receive updates every 5 years

* **Correct Answer:** B) Salesforce delivers three named releases per year to all customers simultaneously; on-premise ERP customers control their own upgrade schedules and frequently run versions that are multiple years behind current.
* **Distractor Analysis:**
  * *Why B is correct:* The Spring/Summer/Winter release cadence is one of the most tested operational facts on the Salesforce Associate exam. All Salesforce customers receive the same update on the same timeline — this is a core characteristic of SaaS multi-tenancy.
  * *Why A is incorrect:* Salesforce delivers three releases per year, not one; and on-premise customers can and often do defer upgrades for 2–5 years, unlike SaaS customers.
  * *Why C is incorrect:* Salesforce releases are delivered to all customers on the same schedule regardless of tier; there is no tier-differentiated release frequency.
  * *Why D is incorrect:* Salesforce does not push daily code changes to production; the three annual named releases are the major delivery cadence, with hotfixes applied transparently when needed.

---

### Question 5

Under the SaaS shared responsibility model, which of the following remains the **customer's** responsibility even when using a cloud-hosted ERP or CRM?

* A) Patching the operating system on the application servers
* B) Upgrading the database engine to the latest supported version
* C) Managing user access, data classification, and ensuring appropriate configuration security within the application
* D) Maintaining physical security of the data center where servers are hosted

* **Correct Answer:** C) Even in SaaS, customers are responsible for managing who has access to the application, classifying and protecting their own data, and configuring the application security settings correctly.
* **Distractor Analysis:**
  * *Why C is correct:* The SaaS shared responsibility model transfers infrastructure security (physical, OS, database, network) to the vendor while the customer retains responsibility for data governance, user access management, configuration security, and application-layer compliance.
  * *Why A is incorrect:* OS patching is entirely the vendor's responsibility in SaaS; the customer has no access to or visibility into the underlying operating system.
  * *Why B is incorrect:* Database engine upgrades are the vendor's responsibility in SaaS; the customer cannot select, defer, or modify the database software version.
  * *Why D is incorrect:* Physical data center security is the vendor's responsibility in any cloud model; customers have no access to the physical facilities.

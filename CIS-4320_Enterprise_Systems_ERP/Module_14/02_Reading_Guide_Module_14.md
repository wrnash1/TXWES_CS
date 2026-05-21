# Reading Guide: Module 14 - Cloud ERP Hosting

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 14 - Cloud ERP Hosting**! The shift from on-premise ERP deployments to cloud-hosted models has been the defining infrastructure trend of the past decade. Understanding the different cloud deployment models — SaaS, PaaS, IaaS, hybrid — and their implications for IT management, cost, upgrade cadence, and data sovereignty is directly tested on both the Salesforce and SAP certification exams.

This module covers the architectural characteristics of multi-tenant SaaS platforms (like Salesforce and SAP S/4HANA Cloud), the tradeoffs of hybrid cloud deployments, and the service responsibilities that shift from the customer to the cloud vendor under each model.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Software as a Service (SaaS)**: A cloud delivery model in which the vendor hosts, maintains, and upgrades the complete application stack — hardware, OS, database, middleware, and application — and the customer accesses the software through a web browser. Salesforce and SAP S/4HANA Cloud Public Edition are SaaS. The customer manages only data and configuration; the vendor handles everything else.
* **Hybrid clouds**: An architecture that combines private cloud or on-premise infrastructure for sensitive or legacy workloads with public cloud services for scalable or modern workloads. Many large enterprises run their core SAP ERP on-premise while using Salesforce CRM in the public cloud, connecting them through middleware — a classic hybrid cloud pattern.
* **Multi-tenant databases**: A database architecture in which multiple customer organizations (tenants) share the same underlying database infrastructure, with logical isolation enforcing that each tenant's data remains invisible and inaccessible to other tenants. Salesforce uses a multi-tenant architecture where all customers share the same application code and database platform, differentiated by their org-specific metadata.
* **Upgrade schedules**: In SaaS, the vendor controls when software upgrades are released and all tenants receive them simultaneously (or on a defined release calendar). Salesforce releases three major updates per year (Spring, Summer, Winter). SAP S/4HANA Cloud Public Edition releases quarterly. Customers cannot defer SaaS upgrades, unlike on-premise systems where upgrade timing is fully customer-controlled.

---

### 2. Certification Exam Tips

* **Salesforce multi-tenant architecture:** The Associate exam tests your understanding that Salesforce's multi-tenant model means all customers share the same code and infrastructure. Governor limits exist specifically to ensure no single tenant monopolizes shared resources. The metadata-driven architecture means customer configuration is stored as metadata, not as modified code, making upgrades safe.
* **Salesforce release cadence:** Know the three annual Salesforce release names (Spring, Summer, Winter) and that Salesforce previews releases in sandbox orgs before the production release date. This is a frequently tested operational knowledge item.
* **SAP deployment options:** SAP offers three S/4HANA deployment options: Public Cloud (SaaS, standardized, quarterly updates), Private Cloud (dedicated infrastructure, SAP-managed, more customization allowed), and On-Premise (customer-managed, maximum customization, customer controls upgrade timing). Know the tradeoffs tested on the SAP exam.
* **Shared responsibility model:** In SaaS, the vendor owns infrastructure, platform, and application security; the customer owns data classification, user access management, and application configuration security. The Salesforce exam tests that customers are responsible for their own data backup strategies even in SaaS.
* **Study Resource:** Review the Salesforce Trailhead module [Salesforce Releases](https://trailhead.salesforce.com/content/learn/modules/sf_releases) — a free module explaining Salesforce's three-times-per-year release cycle and how to prepare for and test upcoming changes.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Complete the Salesforce Trailhead module [Salesforce Releases](https://trailhead.salesforce.com/content/learn/modules/sf_releases) — a free module covering how Salesforce's SaaS upgrade cadence works and how administrators prepare their orgs for each release.
* **Required Video:** Watch the video lecture on **Cloud ERP Hosting** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Analyze SaaS upgrade cycle impacts on custom code**: Given a list of five custom Apex classes and five Flows deployed in a Salesforce org, identify which types of customization are more likely to break during a platform upgrade and explain why declarative tools (Flows) are more upgrade-resilient than code (Apex).
* **Map multi-tenant database design patterns**: Draw a diagram showing how three hypothetical Salesforce customers (Org A, Org B, Org C) share the same database infrastructure while their data remains isolated, labeling the logical isolation layer and the shared physical infrastructure layer.
* **Compare cloud hosting SLA metrics**: Create a comparison table evaluating SaaS, Private Cloud, and On-Premise deployment across five dimensions: upgrade control, infrastructure cost, customization flexibility, data sovereignty, and typical uptime SLA.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to explain the shared responsibility model for SaaS versus on-premise in two sentences each.
* [ ] Complete [Salesforce Releases](https://trailhead.salesforce.com/content/learn/modules/sf_releases) on Trailhead (earn the badge).
* [ ] Watch the video lecture on **Cloud ERP Hosting** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab upgrade impact analysis, multi-tenant diagram, and SLA comparison table.
* [ ] Proceed to the weekly quiz.

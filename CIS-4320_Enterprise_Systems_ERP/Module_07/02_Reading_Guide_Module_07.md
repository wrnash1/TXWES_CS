# Reading Guide: Module 07 - Customer Relationship Management Modules

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 07 - Customer Relationship Management Modules**! While ERP systems manage back-office operations, CRM systems are purpose-built for managing every interaction with customers and prospects. This module marks the course's pivot from SAP back-office modules to the Salesforce CRM platform, which will be the primary focus through Module 11.

You will learn what a CRM system is designed to do, how Salesforce organizes the customer lifecycle into leads, opportunities, and accounts, and how service teams use case management to resolve customer issues. These concepts form the foundation of the Salesforce Certified Associate exam.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Customer Relationship Management (CRM)**: A category of business software that manages all interactions with current and potential customers across marketing, sales, and service functions. A CRM system stores customer contact data, tracks communication history, and helps businesses build and maintain profitable customer relationships.
* **Lead tracking**: The process of capturing information about a potential customer (a lead) and managing their progression through qualification steps until they are determined to be a viable sales opportunity or disqualified. In Salesforce, leads are converted to Contacts, Accounts, and Opportunities when qualified.
* **Sales pipelines**: A visual representation of all active sales opportunities organized by their current stage (e.g., Prospecting, Proposal, Negotiation, Closed Won). Pipelines give sales managers real-time visibility into forecast revenue and help prioritize where to focus team effort.
* **Account management**: The ongoing relationship management of existing customers represented as Account records in Salesforce. Account records store company information, associated contacts, activity history, open opportunities, and service cases — providing a 360-degree view of the customer.
* **Ticket systems**: In CRM service modules, a ticket (called a Case in Salesforce) is a record that tracks a customer's reported issue from initial submission through resolution. Cases are assigned to service queues, escalated by priority, and closed when the customer's issue is resolved.

---

### 2. Certification Exam Tips

* **Salesforce Certified Associate focus:** The exam heavily tests your knowledge of the standard Salesforce objects: Lead, Contact, Account, Opportunity, and Case. Know what each object represents, how they relate to each other, and when leads are converted to the Account/Contact/Opportunity triad.
* **Lead conversion:** In Salesforce, converting a Lead creates three linked records: an Account (the company), a Contact (the person), and optionally an Opportunity (the pending sale). This is one of the most tested processes on the Associate exam.
* **CRM vs. ERP distinction:** The Salesforce Certified Associate exam expects you to understand that Salesforce manages customer-facing data (who you're selling to and how) while ERP manages operational fulfillment (inventory, finance, HR). The two systems are complementary and typically integrated via middleware.
* **Sales Cloud vs. Service Cloud:** Sales Cloud focuses on the sales pipeline — leads, opportunities, quotes. Service Cloud focuses on post-sale customer support — cases, knowledge articles, service contracts. Both are built on the same Salesforce platform.
* **Study Resource:** Complete the free Salesforce Trailhead module [CRM for Lightning Experience](https://trailhead.salesforce.com/content/learn/modules/crm_lightning_experience_basics) — it explains the core CRM objects and navigation on the Salesforce platform that is tested on the Associate exam.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Complete the Salesforce Trailhead module [CRM for Lightning Experience](https://trailhead.salesforce.com/content/learn/modules/crm_lightning_experience_basics) — a free, foundational module covering the Accounts, Contacts, Leads, Opportunities, and Cases that form the core of the Associate exam.
* **Required Video:** Watch the video lecture on **Customer Relationship Management Modules** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Configure a sales lead tracking pipeline**: In your free Salesforce Developer org, create five sample Leads, convert two of them to Accounts/Contacts/Opportunities, and map the resulting object relationships in a diagram.
* **Create customer profile database entries**: Create three Account records with associated Contact records in your Salesforce Developer org and document what fields are stored at the Account level versus the Contact level.
* **Map support ticket escalation paths**: Design a Case escalation rule that automatically reassigns cases unresolved after 24 hours to a senior support queue, and document the trigger condition and action in a flow diagram.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to explain when to use Lead vs. Contact vs. Account in Salesforce.
* [ ] Complete [CRM for Lightning Experience](https://trailhead.salesforce.com/content/learn/modules/crm_lightning_experience_basics) on Trailhead (earn the badge).
* [ ] Watch the video lecture on **Customer Relationship Management Modules** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab Lead conversion exercise and Case escalation design.
* [ ] Proceed to the weekly quiz.

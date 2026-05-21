# Reading Guide: Module 13 - ERP Security & Roles

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 13 - ERP Security & Roles**! Enterprise systems contain the most sensitive operational data in an organization — financial records, employee payroll, customer PII, and supply chain contracts. Securing access to this data through well-designed roles, profiles, and audit controls is both a technical requirement and a regulatory compliance obligation.

This module covers Role-Based Access Control (RBAC) in both SAP and Salesforce, the Separation of Duties principle that prevents fraud, and the audit logging capabilities that provide evidence of who accessed or changed what data and when. These topics appear prominently on both certification exams.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Role-Based Access Control (RBAC)**: An access control model in which permissions are assigned to roles rather than directly to individual users. Users receive permissions by being assigned to one or more roles. This simplifies administration — adding a new employee is as simple as assigning the appropriate role — and makes permission auditing tractable at scale.
* **Separation of Duties (SoD)**: A security control principle that requires critical business transactions to be divided across multiple users so no single individual can complete an entire fraud cycle alone. The classic ERP example: the person who creates a vendor must not be the same person who approves payments to that vendor.
* **Audit profiles**: Configuration settings that define which user actions are recorded in the system's audit log — including who logged in, what records they viewed or changed, what transactions they executed, and what configuration they modified. Audit logs are essential for compliance with SOX, GDPR, and internal control frameworks.
* **Permission sets**: In Salesforce, a Permission Set is an additive collection of object permissions, field permissions, system permissions, and app access settings that can be granted to individual users on top of their base Profile. Permission Sets allow fine-grained, user-specific permission grants without creating new profiles for every permission combination.

---

### 2. Certification Exam Tips

* **Salesforce security model layers:** The Associate exam tests the layered Salesforce security model. Know the sequence: Organization-wide defaults (OWD) set the baseline record visibility → Roles (hierarchy) open up visibility upward → Sharing Rules and Manual Sharing grant additional access → Profiles and Permission Sets control object/field create, read, edit, delete (CRUD) and field-level security (FLS).
* **Profile vs. Permission Set:** A Profile is required and sets the baseline permissions — including login hours, IP restrictions, and default record types. A Permission Set adds permissions on top of the profile. The exam frequently asks: "A user needs access to one additional object that others on their profile don't need — use a Permission Set, not a new Profile."
* **SAP authorization objects:** SAP's security model uses Authorization Objects (technical structures with fields that define specific access conditions), which are grouped into Roles. Roles are assigned to Users. The most commonly tested SAP authorization concept is the difference between a Single Role (one activity area) and a Composite Role (collection of single roles).
* **SoD in ERP context:** SAP GRC (Governance, Risk, and Compliance) is the tool used to detect and manage Separation of Duties conflicts in large SAP environments. Know that SoD analysis compares the set of transactions a user can execute to identify conflict pairs (e.g., can both create and pay vendors).
* **Study Resource:** Complete the Salesforce Trailhead module [Data Security](https://trailhead.salesforce.com/content/learn/modules/data_security) — a free module covering the full Salesforce security model from OWDs through Permission Sets.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Complete the Salesforce Trailhead module [Data Security](https://trailhead.salesforce.com/content/learn/modules/data_security) — a free module covering the layered Salesforce security model that is heavily tested on the Associate exam.
* **Required Video:** Watch the video lecture on **ERP Security & Roles** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Create user roles mapping permissions**: In your Salesforce Developer org, create a role hierarchy with three levels (VP of Sales → Regional Manager → Sales Representative), assign a test user to each level, and verify that the VP can see all records while the Sales Rep can only see their own.
* **Audit roles for Separation of Duties conflicts**: Given a table of five SAP users and the transaction codes each can execute, identify any SoD conflicts where a single user can both create and approve a financial document.
* **Document profile access scopes**: In your Salesforce Developer org, compare the object permissions of the standard "Standard User" profile against a custom profile you create, documenting which objects each profile can Create, Read, Edit, and Delete.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to explain the layered Salesforce security model from OWDs to Permission Sets.
* [ ] Complete [Data Security](https://trailhead.salesforce.com/content/learn/modules/data_security) on Trailhead (earn the badge).
* [ ] Watch the video lecture on **ERP Security & Roles** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab role hierarchy, SoD conflict analysis, and profile comparison exercises.
* [ ] Proceed to the weekly quiz.

# Video Script: Module 13 — ERP Security and Roles

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 20–24 minutes

---

## Pre-Production Notes

- Slide deck: 28 slides
- Diagrams: Salesforce security layers (OWD, Role Hierarchy, Sharing Rules, FLS), SAP authorization object structure, SoD conflict example (vendor-to-payment fraud), audit trail flow, Profile vs. Permission Set comparison
- Key terms on screen: Separation of Duties, Least Privilege, Role, Profile, Permission Set, OWD, Sharing Rule, FLS, SAP Authorization Object, SoD, Audit Log, SM20
- End card: Lab 13, Quiz 13, Discussion Forum 13

---

## [00:00 – 02:00] Opening Hook

[PROFESSOR ON CAMERA]

Here is a fraud scenario. An accounts payable clerk at a mid-sized company has, over three years, stolen $2.3 million from her employer. How did she do it?

She created fictitious vendor records in the ERP system using her own access. She created purchase orders against those fictitious vendors. She approved her own invoices for payment — because her role gave her both create and approve access in the system. And she directed the payments to bank accounts she controlled.

Three years. $2.3 million. No one caught it because no one was checking, and because the system was configured to allow one person to control the entire vendor-to-payment cycle.

This is not a fictional scenario. Variations of it happen every year at organizations of every size. And the control that prevents it is simple: you do not give one person the ability to both create a vendor AND approve payment to that vendor. You split those duties between different people. Separation of duties.

ERP security is not a technical afterthought. It is a fraud prevention framework. And today we are going to cover how SAP and Salesforce implement security — the principles, the architecture, and the specific configuration objects that make it work.

[SHOW TITLE SLIDE: Module 13 — ERP Security and Roles]

---

## [02:00 – 06:00] Security Principles

[SHOW SLIDE: Three Core Security Principles]

Every ERP security design rests on three principles. Know these — they appear on both exams.

[SHOW SLIDE: Principle 1 — Separation of Duties]

Separation of Duties, or SoD, means that no single individual should have complete control over a critical business transaction. The classic example is the vendor-to-payment cycle: one person creates vendors, a different person creates purchase orders, a third person posts invoices, and a fourth person authorizes payments. If any one of those people tries to commit fraud, they need cooperation from the others.

SoD is enforced through role design in SAP and profile/permission design in Salesforce. When you assign roles, you check that any single user's combination of authorizations does not create an SoD conflict.

[SHOW SLIDE: Principle 2 — Least Privilege]

Least Privilege means users should have only the minimum access needed to perform their job. An accounts receivable clerk does not need access to the payroll module. A sales representative does not need access to financial reporting. Least privilege limits the blast radius when an account is compromised — if a phishing attack succeeds and an attacker gains access to a low-privilege user's account, the damage is contained to what that user could do.

[SHOW SLIDE: Principle 3 — Audit Trail]

An audit trail is a logged record of who did what in the system and when. Every change to a financial document, every privileged action, every failed login attempt should be recorded. When a fraud investigation occurs — or when an external auditor asks "who changed this invoice amount on December 14?" — the audit trail provides the answer.

In SAP, the Security Audit Log (transaction SM20) records login events, transaction executions, and authorization failures. Change Documents record field-level before-and-after values for every change to a business document.

In Salesforce, the Setup Audit Trail records all configuration changes. Field History Tracking records field-level changes on objects where it is enabled.

---

## [06:00 – 11:00] SAP Security Architecture

[SHOW DIAGRAM: SAP Authorization Concept]

SAP's security model is built around Authorization Objects. Let me explain how this works.

Every action in SAP — executing a transaction, reading data from a table, posting a document — requires an authorization check. The check evaluates whether the user has permission for the specific activity, for the specific organizational scope (company code, plant, etc.).

[SHOW SLIDE: SAP Authorization Objects]

An Authorization Object is a group of related authorization fields that are checked together. For example, the Authorization Object for Financial Accounting document processing (F_BKPF_BUK) contains fields for:

- Company Code (BUKRS)
- Activity (ACTVT): 01 = Create, 02 = Change, 03 = Display

A user's authorization for this object might specify: Company Code = 1000, Activity = 01 and 03 (Create and Display, but not Change). That user can create and display FI documents in Company Code 1000, but cannot change them.

[SHOW SLIDE: SAP Role Architecture]

Authorization Objects are grouped into Roles. A Role (transaction PFCG — Profile Generator) is a collection of authorization objects that together represent a job function. Examples:

- AP Clerk role: create vendor invoices, display vendor master, display bank master
- AP Manager role: approve invoices, display all AP documents, run AP aging reports
- Vendor Master Administrator role: create and change vendor records

Users are assigned Roles. The role's underlying authorization profile is assigned to the user record in transaction SU01 (User Maintenance). When the user performs an action in SAP, the system checks their profiles for the required authorization object and field values.

[SHOW SLIDE: SAP SoD — The Conflict Example]

Here is the vendor-to-payment SoD conflict as a concrete SAP example.

The authorization to create vendor master records is in Role Z_VENDOR_ADMIN. It includes authorization object F_LFA1_BUK with Activity = Create (01).

The authorization to run the automatic payment program (F110) is in Role Z_AP_PAYMENT_RUN. It includes authorization object F_F110_BUK with Activity = Execute (16).

If these two roles are assigned to the same user, that user can create a fictitious vendor and process a payment to them. The SoD conflict between Z_VENDOR_ADMIN and Z_AP_PAYMENT_RUN must be detected and prevented during role design.

SAP provides tools — most notably SAP GRC (Governance, Risk, and Compliance) — to automatically identify SoD conflicts in role assignments across the entire user base.

---

## [11:00 – 16:00] Salesforce Security Architecture

[SHOW DIAGRAM: Salesforce Security Layers — four concentric rings]

Salesforce uses a layered security architecture. Each layer controls a different dimension of access. Let me walk through all four layers from the outside in.

[SHOW SLIDE: Layer 1 — Organization-Wide Defaults (OWD)]

Organization-Wide Defaults are the baseline for record sharing. OWD answers the question: by default, who can see any given record? There are three settings:

Private — the record owner and users above them in the role hierarchy can see the record. No one else.

Public Read Only — every user in the organization can read all records, but only the owner and authorized users can edit.

Public Read/Write — every user in the organization can read and edit all records.

OWD is set for each object separately. You might set Accounts to Public Read/Write but set custom compensation data to Private. OWD establishes the floor of access — you can only open it up from there.

[SHOW SLIDE: Layer 2 — Role Hierarchy]

The Role Hierarchy determines upward record visibility. If your role is above another role in the hierarchy, you can see all records owned by users in that role and any roles below it — even if the OWD is set to Private.

Example: a Regional Sales Manager role is above the Account Executive roles for their region. The regional manager sees all Account Executive records in their region. The VP of Sales is above all Regional Manager roles and sees all records across the organization.

[EXAM TIP ON SCREEN]

For the Salesforce exam: the Role Hierarchy only affects record visibility — it does not control what a user can do with a record (CRUD permissions). Those are controlled by the Profile.

[SHOW SLIDE: Layer 3 — Profiles and Permission Sets]

A Profile is the required security assignment for every Salesforce user. It controls:

- Object permissions (CRUD: Create, Read, Update, Delete for each object)
- Field-level security (FLS): which fields a user can see and edit
- System permissions (login hours, IP restrictions, password policies)
- Default app assignment

Every user has exactly one Profile. You cannot give a user two Profiles.

A Permission Set is an additive collection of permissions that can be given to specific users on top of their Profile. Use Permission Sets when a small number of users need access to something that the rest of their Profile group does not need.

[EXAM TIP ON SCREEN]

For the exam: when the question is "a few users need extra access that others on the same Profile don't need," the answer is Permission Set — not a new Profile. Creating a new Profile for every edge case creates profile sprawl and maintenance problems.

[SHOW SLIDE: Layer 4 — Sharing Rules]

Sharing Rules extend access to records beyond what OWD and the Role Hierarchy provide. A Sharing Rule says: "Share records owned by users in Role X with users in Role Y." Or: "Share records where the Region field equals Southwest with the Southwest Management Group."

Sharing Rules can only open access — they cannot restrict access more than the OWD already does. If OWD is Private, a Sharing Rule can give additional users Read access. A Sharing Rule cannot block access that OWD already grants.

[SHOW SLIDE: Field-Level Security (FLS)]

Field-Level Security controls which fields a user can see and edit, independently of whether they can see the record. FLS can be configured to:

- Make a field visible and editable
- Make a field visible but read-only
- Make a field completely hidden

Example: all sales reps can see Account records, but only Finance users can see the Credit_Limit__c field. FLS enforces this independently of record-level security.

---

## [16:00 – 20:00] Audit Trails and Compliance

[SHOW SLIDE: SAP Audit Capabilities]

SAP's audit trail for financial documents is built into the core of the application.

Every FI document (journal entry, invoice, payment) has a Document Change History. If an invoice amount is changed after posting, SAP records: the original value, the new value, the user who made the change, and the timestamp. Auditors can pull this for any document or any period.

The Security Audit Log (SM20) records at the system level: every login and logout, every failed login, every blocked authorization attempt, and every sensitive transaction that has been configured for audit logging.

Change Documents in master data (vendor master, customer master, material master) record every field change with the same before/after structure.

[SHOW SLIDE: Salesforce Audit Capabilities]

Salesforce provides two primary audit tools.

Setup Audit Trail records every configuration change made in Setup: new custom fields added, sharing rules modified, permission sets changed, users created or deactivated. It retains 180 days of configuration history.

Field History Tracking, when enabled on an object, records the last 20 field value changes per record. The "History" related list on a record shows who changed each tracked field and from what value to what value. Field History can be enabled for up to 60 fields per object.

---

## [20:00 – 23:00] Certification Exam Summary

[SHOW SLIDE: Key Exam Points — Security Principles]

Separation of Duties: no single user controls a complete transaction cycle (vendor create + payment = SoD conflict). This is the primary fraud prevention control in ERP.

Least Privilege: users have only the access needed for their job. Reduces the impact of compromised accounts.

Audit Trail: logged record of all user actions, changes, and authorization failures. Essential for forensic investigation and regulatory compliance.

[SHOW SLIDE: Key Exam Points — SAP Security]

SAP uses Authorization Objects to control access. Authorization objects contain fields (company code, activity) that are checked at runtime.

Roles (PFCG) group authorization objects into job-function access bundles. Users are assigned roles.

Transaction SM20 is the Security Audit Log — shows login events and authorization failures. Change Documents record field-level document changes.

SAP GRC detects and manages SoD conflicts across role assignments.

[SHOW SLIDE: Key Exam Points — Salesforce Security]

OWD is the floor of record sharing. Private restricts to owner and role hierarchy. Public Read Only and Public Read/Write open access.

Role Hierarchy controls upward record visibility — managers see subordinate records. Does not control CRUD permissions.

Profile is required for every user — controls object CRUD, FLS, system permissions. One Profile per user.

Permission Set is additive — extends access for specific users without a new Profile. Use when a few users need extra access.

Sharing Rules open access beyond OWD and Role Hierarchy. Cannot restrict access.

Field-Level Security controls field visibility and editability per profile.

---

## [23:00 – 24:00] Closing and Assignments

[PROFESSOR ON CAMERA]

ERP security is not just a technology configuration exercise. It is the defense layer that protects financial data, prevents fraud, and satisfies regulatory requirements like SOX and HIPAA. The principles — separation of duties, least privilege, audit trail — are the same regardless of which platform you are working on.

For Lab 13, you are analyzing security configuration for a healthcare company on both SAP and Salesforce, identifying SoD conflicts, and designing the correct security layers for a set of requirements. Pay attention to the OWD, Profile, and Permission Set questions — they represent the most commonly tested Salesforce security content on the Certified Associate exam.

I will see you in Module 14.

[END CARD: Lab 13 | Quiz 13 | Discussion Forum 13]

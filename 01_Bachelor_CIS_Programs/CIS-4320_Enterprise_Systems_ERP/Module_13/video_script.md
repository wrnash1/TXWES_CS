# Video Script: Module 13 — ERP Security and Access Control

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Production Notes

**Duration:** Approximately 25–30 minutes
**Format:** Lecture with slide transitions and demonstration walkthroughs
**Segments:** 6 segments with natural pause points

---

## Segment 1: Introduction — Security as a Business Problem (Lines 1–40)

[SLIDE: Title card — "Module 13: ERP Security and Access Control"]

Welcome to Module 13. I am Professor Nash, and today we are talking about something that keeps enterprise IT teams awake at night: security and access control in ERP systems.

[SLIDE: Newspaper headlines — fictional data breach stories]

Here is a scenario that plays out repeatedly across industries. A mid-level finance employee at a company gains access to approve payments and also gains access to create vendor records. Those are two capabilities that should never exist in the same person's hands at the same time. Over eighteen months, that employee creates fictitious vendors and approves fraudulent invoices. By the time auditors catch it, millions of dollars are gone.

The root cause is not a sophisticated cyberattack. It is a configuration error in the ERP system — a failure to implement Segregation of Duties.

[SLIDE: The three goals of ERP security]

ERP security has three interconnected goals. First, confidentiality: only the right people can see sensitive data. A warehouse picker does not need to see customer credit card information. Second, integrity: data can only be changed by authorized people through authorized processes. A sales rep cannot manually override the price in a completed customer invoice. Third, availability: the system is accessible to authorized users when they need it, and unauthorized access is blocked.

[SLIDE: Learning objectives]

In this module we cover four areas. Salesforce profiles and permission sets — the building blocks of Salesforce access control. SAP authorization objects and roles — how SAP implements access control through a structured authorization concept. Segregation of Duties — what it is, why it matters, and how to enforce it. And audit trails — how both platforms record who did what, when.

[PAUSE]

---

## Segment 2: Salesforce Profiles and Permission Sets (Lines 41–85)

[SLIDE: Salesforce security model — layers]

Salesforce uses a layered security model. The outermost layer is the organization — are you allowed to log in at all? The next layer is the object level — can you see Accounts, Opportunities, Cases? The next is the record level — can you see this specific Account or only the ones you own? The innermost layer is the field level — can you see the Annual Revenue field on Account, or is it hidden?

Understanding this four-layer model is essential for the Salesforce Admin exam.

[SLIDE: Profiles]

A Profile is the foundational access configuration for every user. Every user has exactly one profile. You cannot have zero profiles and you cannot have two.

Profiles control: which objects the user can access, what CRUD permissions they have on each object (create, read, edit, delete), which fields they can see, which page layouts and record types they use, which apps appear in the App Launcher, login hours, and login IP ranges.

Salesforce ships with several standard profiles — Salesforce Administrator, Standard User, Read Only, and others. These standard profiles cannot be deleted, but custom profiles can be created and fully configured.

[SLIDE: The profile limitation problem]

Profiles become complex to manage at scale. If you have fifteen different job roles, you might end up with fifteen different profiles, each a slight variation of another. When business requirements change — such as a new object needing access for everyone — you have to update fifteen profiles individually.

This is the problem that Permission Sets solve.

[SLIDE: Permission Sets]

A Permission Set grants additional access on top of a profile. Users can have multiple permission sets. Permission sets cannot take access away — they can only add it.

Think of it this way: the Profile establishes the baseline, the minimum access for a category of users. Permission Sets layer on top to grant specific additional capabilities to specific individuals.

For example, a Standard User profile grants basic read access to Accounts. A "Account Manager" permission set grants edit access and the ability to run account reports. Sales reps who are account managers get both. Sales reps who are not account managers keep just the profile access.

[SLIDE: Permission Set Groups]

Salesforce added Permission Set Groups to simplify management further. A Permission Set Group bundles multiple permission sets into a single assignable unit. Instead of assigning five individual permission sets to every sales manager, you assign one Permission Set Group. When a permission set inside the group changes, the change applies to all users with the group assigned.

[SLIDE: Record-Level Access — the four mechanisms]

Object-level and field-level access are controlled by profiles and permission sets. Record-level access — which specific records a user can see — is controlled by four mechanisms:

**Organization-Wide Defaults (OWD)** set the baseline. If OWD for Opportunity is set to Private, users can only see opportunities they own unless something grants them more access.

**Role Hierarchy** grants access up the hierarchy. A manager can see their direct reports' records. An executive at the top of the hierarchy can see everything in the hierarchy.

**Sharing Rules** extend access to groups of users. For example, all opportunities owned by users in the West Region role should be readable by users in the East Region role.

**Manual Sharing** allows individual record owners to share a specific record with a specific user or group.

[PAUSE — transition to SAP]

---

## Segment 3: SAP Authorization Concept (Lines 86–130)

[SLIDE: SAP Authorization architecture]

SAP uses a fundamentally different approach to access control that is more granular and more complex than Salesforce. Let me walk you through the hierarchy from the bottom up.

[SLIDE: Authorization Objects and Authorization Fields]

At the foundation of SAP's authorization concept is the **Authorization Object**. An Authorization Object defines a set of activities that can be performed on a specific type of data. For example, the authorization object `F_BKPF_BUK` controls which company codes a user can post financial documents in. The object has fields — in this case, ACTVT (activity: display, change, post) and BUKRS (company code).

There are over 1,000 authorization objects in a standard SAP system. Each one governs a specific functional capability.

[SLIDE: Authorizations]

An **Authorization** is one specific combination of values for an authorization object's fields. So an authorization for `F_BKPF_BUK` might specify: ACTVT = 01 (Create), BUKRS = 1000 (Dallas). That authorization means "can create financial documents in company code 1000."

[SLIDE: Authorization Profiles]

Multiple authorizations are packaged together into an **Authorization Profile**. Profiles are the containers that get assigned to users — but in practice, you rarely create profiles manually. SAP generates them automatically from roles using Profile Generator (transaction SU25).

[SLIDE: Roles — Single and Composite]

A **Single Role** in SAP is a named collection of transaction codes plus the authorization profile generated from the functions included. You create roles in transaction PFCG. When you add a transaction to a role, the system automatically identifies which authorization objects are needed and prompts you to fill in the field values.

A **Composite Role** is a container of single roles. For example, a "Procurement Manager" composite role might contain single roles for "Purchase Order Create," "Goods Receipt," and "Vendor Master Display." Assigning the composite role gives the user all three sets of authorization.

[SLIDE: User master record]

The user master record in SAP (transaction SU01) is where roles are assigned to users. The system reads the user's assigned roles, looks up the authorization profiles generated from those roles, and checks whether the user has the required authorization values every time they attempt a transaction.

[SLIDE: Authorization Check — the SU53 transaction]

When a user is denied access to a transaction, they see an authorization error. Transaction SU53 displays the last failed authorization check for a user, showing exactly which authorization object, which field, and which value was missing. This is your primary diagnostic tool for access issues.

For the SAP exam: know what SU53 does, what PFCG is, and the difference between a single role and a composite role.

[PAUSE]

---

## Segment 4: Segregation of Duties (Lines 131–170)

[SLIDE: What is SoD?]

Segregation of Duties (SoD) is the principle that no single individual should have end-to-end control over a critical business process without oversight. The classic finance example: the person who creates vendors should not be the same person who approves payments. The person who enters transactions should not be the same person who reconciles the accounts.

SoD is not just a best practice — it is a regulatory requirement. SOX (Sarbanes-Oxley Act) compliance for publicly traded companies mandates SoD controls over financial processes. Internal auditors and external auditors both test for SoD violations.

[SLIDE: SoD conflicts in SAP]

In SAP, SoD conflicts arise when a user has roles or authorizations that, in combination, constitute a dangerous capability. SAP has a dedicated tool for detecting these conflicts: GRC (Governance, Risk, and Compliance) Access Control.

SAP GRC Access Control includes a Rulebook — a database of thousands of defined SoD conflicts. It continuously monitors user access, identifies users with conflicting authorizations, and generates reports for compliance teams. Role designers use GRC to simulate what authorizations a new role combination would create before assigning it to users.

[SLIDE: SoD conflicts in Salesforce]

Salesforce does not have a built-in SoD tool equivalent to SAP GRC. SoD in Salesforce is enforced through profile and permission set design:

Approval processes ensure that no single user can create and approve a record. Validation rules enforce data integrity checks. Sharing restrictions prevent cross-functional data access. Third-party AppExchange tools from vendors such as Salesforce Shield, Odaseva, and CloudAlly provide enhanced audit and compliance capabilities.

The Salesforce Shield platform provides three products relevant to security and SoD: Platform Encryption for encrypting data at rest, Event Monitoring for tracking user behavior, and Field Audit Trail for extended field history retention.

[SLIDE: Compensating controls]

In practice, it is sometimes impossible to fully eliminate an SoD conflict — particularly in small organizations where there are not enough people to fully separate duties. In these cases, organizations implement compensating controls: additional manual or automated checks that detect abuse even if prevention is not fully enforced.

Examples of compensating controls include supervisory review of all payment approvals above a threshold, automated reconciliation reports that flag unusual patterns, and monthly access reviews that confirm each user's role assignments are still appropriate.

[PAUSE]

---

## Segment 5: Audit Trails (Lines 171–205)

[SLIDE: Why audit trails matter]

An audit trail is a chronological record of all significant actions taken in a system. Audit trails serve multiple purposes: security forensics (what happened during a breach), compliance evidence (demonstrating to auditors that controls were in place), operational troubleshooting (who changed this configuration and when?), and non-repudiation (proving that a specific user took a specific action).

[SLIDE: Salesforce Setup Audit Trail]

Salesforce's Setup Audit Trail records all changes made to the Salesforce configuration — Setup. It captures who made the change, what they changed, from what old value to what new value, and when. The audit trail retains 180 days of data. For longer retention, you must export the data to an external system.

The Setup Audit Trail does not capture changes to data records — that is the job of Field History Tracking.

[SLIDE: Salesforce Field History Tracking]

Field History Tracking records changes to specific fields on specific objects. You enable it per object and per field in Setup. When a tracked field changes, Salesforce creates a history record showing: the date and time, who made the change, the old value, and the new value.

Standard orgs retain field history for 18 months. With Salesforce Shield Field Audit Trail, retention extends to 10 years — meeting the requirements of regulated industries such as financial services and healthcare.

[SLIDE: SAP Change Documents]

SAP has a similar mechanism called Change Documents. When a business object — a purchase order, a customer master record, a material — is changed, SAP writes a change document to the CDHDR and CDPOS tables. CDHDR holds the change document header (object, date, user, transaction) and CDPOS holds the line-item detail of each field change.

You can view change documents in transaction AUT10 or through the change history button on most SAP master data records.

[SLIDE: SAP Security Audit Log]

Beyond data change documents, SAP has a Security Audit Log (SM20) that records authentication events: logins, logouts, failed login attempts, and access to sensitive transactions. The Security Audit Log is distinct from Change Documents — it records system-level security events, not data changes.

For SOX compliance, SAP Security Audit Log data is exported to a SIEM (Security Information and Event Management) system for long-term retention and anomaly detection.

[PAUSE]

---

## Segment 6: Putting It Together and Summary (Lines 206–240)

[SLIDE: A complete access control scenario]

Let me tie it all together with a scenario. Apex Manufacturing has 300 Salesforce users. The security model works like this.

Profiles define baseline access by job function — Standard User for general staff, Read Only for executives who only need visibility. Permission sets layer on top — a "PO Approver" permission set is assigned to finance users who need to approve purchase requisitions.

Organization-Wide Defaults for Opportunity are set to Private. The role hierarchy mirrors the org chart. Regional managers can see their team's opportunities; national directors see all opportunities under them.

SoD is enforced by requiring that opportunity creation and discount approval are separate permission sets — no one user has both. Approval processes require a manager's sign-off for discounts over 15%.

The Setup Audit Trail is exported weekly to Snowflake. Field History Tracking is enabled on Opportunity Stage, Amount, and Close Date. The compliance team runs monthly reports on all access changes and all stage reversals.

[SLIDE: Certification exam tips]

Salesforce Admin exam: know profiles vs. permission sets vs. permission set groups, the four record-level sharing mechanisms (OWD, role hierarchy, sharing rules, manual sharing), what Field History Tracking does, and what the Setup Audit Trail captures.

SAP essentials: know the authorization object concept, the difference between a single role and a composite role, what PFCG and SU53 are used for, and what SoD means in the context of SAP GRC.

[SLIDE: Key terms]

Profile (Salesforce): the single, mandatory access baseline for every user.

Permission Set: additional access granted on top of a profile; users can have many.

Organization-Wide Default: the baseline record-sharing setting for all users.

Authorization Object (SAP): defines a set of controllable activities on a specific data category.

Single Role (SAP): a named collection of transaction codes and the authorization profile generated from them.

Composite Role (SAP): a container grouping multiple single roles for ease of assignment.

SoD (Segregation of Duties): the principle that critical process steps should be controlled by different individuals.

SAP GRC: Governance, Risk, and Compliance — SAP's tool for detecting and managing SoD conflicts.

Setup Audit Trail (Salesforce): records all Setup configuration changes.

Field History Tracking (Salesforce): records field-level data changes on enabled objects.

Change Documents (SAP): records data changes to business objects in CDHDR/CDPOS.

Security Audit Log (SAP): records authentication and system security events.

[SLIDE: Next module preview]

In Module 14 we turn to reporting and business intelligence — Salesforce reports, dashboards, and Einstein Analytics; SAP Business Intelligence; KPIs; and executive dashboard design. The move from raw data to actionable insight is where ERP systems deliver their most visible value.

Complete the Reading Guide, the Lab, and the Discussion before next class. The quiz goes live Monday.

Thank you. See you in Module 14.

[END OF VIDEO SCRIPT]

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*

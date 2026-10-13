# Reading Guide: Module 13 — ERP Security and Access Control

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Overview

Module 13 covers the security and access control architecture of both Salesforce and SAP S/4HANA. Security configuration is one of the highest-weighted topic areas on the Salesforce Administrator exam and is thoroughly tested on SAP essentials assessments. Allow approximately 90 minutes to complete all sections of this guide.

---

## Section 1: Foundations of ERP Security

### The CIA Triad in ERP Contexts

Every security framework begins with three foundational goals known as the CIA triad: Confidentiality, Integrity, and Availability. In ERP systems, these translate to concrete configuration decisions.

Confidentiality means that sensitive business data — customer pricing, payroll figures, financial projections — is visible only to those with a legitimate business need. Integrity means that data is accurate and can only be modified through authorized, controlled processes. Availability means that the system is accessible to authorized users when needed, and that unauthorized access attempts are blocked without disrupting legitimate access.

ERP systems are attractive targets for both internal fraud and external attackers because they contain the most complete, authoritative record of a company's financial and operational state. A breach or manipulation of ERP data can be more damaging than almost any other IT incident.

### Principle of Least Privilege

The principle of least privilege states that every user should have only the minimum access necessary to perform their job function — nothing more. In ERP terms, this means: read access where the user only needs to see data, no access to functions outside the user's role, and time-limited elevated access for temporary needs.

Least privilege is in constant tension with usability. Users often request more access than they need "just in case," and administrators may grant it to avoid friction. The result is privilege creep — the gradual accumulation of access rights over time. Annual access reviews are the standard countermeasure.

### The Concept of Access Control Models

Three access control models underlie most ERP implementations.

**Discretionary Access Control (DAC):** record owners control who can access their records. Salesforce's manual sharing feature is a DAC mechanism.

**Role-Based Access Control (RBAC):** access is determined by the user's role, not their identity. Both Salesforce permission sets and SAP roles implement RBAC.

**Attribute-Based Access Control (ABAC):** access decisions are made based on attributes of the user, the resource, and the environment. Salesforce's criteria-based sharing rules are an example of ABAC-inspired design.

---

## Section 2: Salesforce Access Control Architecture

### Profile Architecture and Standard Profiles

The Salesforce profile is the mandatory, non-negotiable foundation of every user's access. A user with no profile cannot log in. A user with the Salesforce Administrator profile has access to all Setup functions and typically full CRUD access to all objects.

Standard profiles ship with Salesforce and cannot be deleted:

- **System Administrator:** full access to setup and data. Only administrators should hold this profile.
- **Standard User:** most commonly used baseline for employees. Can create, edit, and delete records they own or have access to on most standard objects.
- **Read Only:** can view records but cannot create, edit, or delete.
- **Solution Manager:** specialized profile for knowledge management functions.
- **Contract Manager:** specialized profile for contract-related objects.
- **Marketing User:** adds access to campaign objects.

Creating custom profiles allows organizations to define precise access configurations. Best practice is to have as few profiles as possible, using permission sets to handle variations.

### Permission Set Architecture

Permission sets were introduced to reduce profile proliferation. The key design principle: the profile defines what users of this type cannot do; permission sets define what specific users additionally can do.

Permission sets support all the same settings as profiles: object permissions, field permissions, app permissions, system permissions, and tab visibility. However, permission sets cannot restrict access below the profile level — they can only expand it.

**Permission Set Groups** bundle multiple permission sets for ease of administration. A permission set group can also include a **Muting Permission Set** — a special construct that removes permissions within the group without modifying the individual permission sets. This allows a group to be more restrictive than the sum of its parts.

### Object-Level Permissions

Object permissions in Salesforce are six flags per object per profile or permission set:

- **Read:** view records
- **Create:** create new records
- **Edit:** modify existing records
- **Delete:** delete records
- **View All:** see all records regardless of sharing settings
- **Modify All:** edit and delete all records regardless of sharing settings

"View All" and "Modify All" are powerful bypasses of record-level sharing. Use them sparingly — only for administrators or specific operational roles that genuinely need system-wide access.

### Field-Level Security

Field-Level Security (FLS) controls whether a field is visible and editable for a given profile or permission set. FLS can make a field:

- **Visible and Editable:** user sees and can change the field
- **Visible but Read-Only:** user sees but cannot change the field
- **Hidden:** field does not appear on page layouts, in reports, or in API responses

FLS applies across all interfaces — Lightning UI, Visualforce, API, and reports. Even if a field is on a page layout, FLS takes precedence: a hidden field will not appear.

For the exam: FLS and page layouts work together but FLS wins. If FLS hides a field, putting it on a page layout does not make it visible.

### Record-Level Access — Deep Dive

**Organization-Wide Defaults (OWD)** are the most restrictive sharing settings for each object. The options vary by object type:

- **Private:** users see only their own records plus records shared to them explicitly.
- **Public Read Only:** all users can see all records but can only edit records they own or have sharing access to.
- **Public Read/Write:** all users can see and edit all records.
- **Controlled by Parent:** for child objects (Contacts, Cases), sharing follows the parent object (Account).

Setting OWD correctly is the most important record-sharing decision an administrator makes. It is much easier to open access than to close it.

**Role Hierarchy** is modeled on the organizational reporting structure. Each user is assigned a role (not to be confused with SAP roles — Salesforce roles are strictly for record sharing). A user's manager, by virtue of being higher in the hierarchy, inherits read access to all records owned by users below them.

**Sharing Rules** automate the granting of access to groups of users. Owner-based sharing rules share records based on the record owner's role or group membership. Criteria-based sharing rules share records based on field values — for example, all opportunities with Stage = "Negotiation" should be shared with the Legal Team public group.

**Manual Sharing** allows individual users to share specific records on an ad-hoc basis. Enabled via the "Sharing" button on record pages. Not scalable — for systematic sharing patterns, use sharing rules.

---

## Section 3: SAP Authorization Architecture

### The Authorization Check Flow

Every time a user attempts to perform an action in SAP — opening a transaction, changing a document, executing a report — SAP performs an authorization check. The system checks whether the user's master record includes an authorization for the relevant authorization object with the relevant field values.

If the authorization check passes, the action proceeds. If it fails, the user receives an error message. The details of the failed check are stored temporarily and viewable via transaction SU53.

### Key Authorization Objects by Functional Area

Learning the most commonly tested authorization objects is valuable for the SAP essentials certification. Here are the important ones by function:

**Financial Accounting:**

- `F_BKPF_BUK` — company code authorization for document posting
- `F_BKPF_KOA` — account type authorization (vendor, customer, G/L)

**Materials Management:**

- `M_EINF_BUK` — purchasing document authorization by company code
- `M_MSEG_BWA` — goods movement authorization

**Sales and Distribution:**

- `V_VBAK_AAT` — sales document type authorization
- `V_VBAK_VKO` — sales organization authorization

**Basis / Cross-Application:**

- `S_TCODE` — transaction code authorization (controls which transactions a user can run)
- `S_DEVELOP` — controls access to ABAP development workbench

The `S_TCODE` object is foundational. Before any functional authorization check runs, SAP checks whether the user is authorized to run the transaction at all.

### Role Design Best Practices

SAP role design follows established best practices to ensure security, maintainability, and auditability.

**Single roles should be function-specific and granular.** A role named "MM_BUYER_CREATE_PO" is better than a role named "MM_ALL" — it conveys exactly what access is granted and makes SoD analysis possible.

**Composite roles map to job positions.** A Procurement Manager composite role might contain single roles for purchase order creation, goods receipt, and vendor inquiry, but not vendor master maintenance (which is a separate control function).

**Testing roles before assignment.** Use the profile generator (PFCG) simulation capability and SU53 to confirm that roles grant exactly the needed access before production assignment.

**User group assignment.** SAP User Groups (SU01 → User Group field) allow administrators to restrict who can manage which users — a form of administrative SoD.

---

## Section 4: Segregation of Duties

### Defining SoD in ERP

Segregation of Duties is the most important internal control concept in enterprise system security. The principle: no individual should be able to initiate, approve, execute, and record a business transaction without oversight.

In procurement, the classic SoD matrix separates:

- Requesting a purchase (can be self-service)
- Creating/maintaining a vendor in the system (Finance/Vendor Management)
- Creating a purchase order (Procurement)
- Receiving goods and posting a goods receipt (Warehouse)
- Entering and approving a vendor invoice (Accounts Payable)
- Making a payment (Treasury)

If one person has access to create vendors and approve payments, they can commit procurement fraud. If one person can create a purchase order and receive goods, they can fictitiously receive goods they never ordered.

### SoD in Salesforce

Salesforce's platform does not natively enforce SoD through a rule engine, but administrators implement it through deliberate design decisions.

**Approval Processes** are the primary SoD enforcement mechanism in Salesforce. An approval process requires that a record submitted for approval be reviewed by a different user before it proceeds. For example, a quote discount over 20% must be approved by a Sales Director before it becomes active.

**Record types and page layouts** can restrict what fields are visible at different stages of a process, preventing users from modifying data they should not touch after certain milestones.

**Validation rules** enforce business rules at the data level — for example, a rule that prevents any user from changing the invoice total after the status is "Approved."

**Third-party tools** such as Salesforce Shield Event Monitoring provide activity-level audit data that compliance teams can use to detect SoD violations after the fact, even when prevention-only controls are not feasible.

### SoD in SAP — GRC Access Control

SAP GRC (Governance, Risk, and Compliance) Access Control is a dedicated module for managing SoD at scale. Its key components are:

**Access Risk Analysis (ARA):** compares users' current role assignments against a Rulebook of SoD conflicts. Generates reports showing each user's conflicts, the risk level (critical, high, medium), and the business process areas affected.

**Emergency Access Management (EAM, or Firefighter):** provides controlled, time-limited elevated access for emergency situations — such as a year-end deadline that requires a single user to perform actions normally split across two roles. All activity during firefighter access is logged and reviewed.

**Business Role Management (BRM):** supports role definition, approval workflows for role changes, and periodic role recertification.

**Access Request Management (ARM):** routes new access requests through approval workflows, automatically checks for SoD conflicts before provisioning.

---

## Section 5: Audit Trails and Compliance Reporting

### Salesforce Audit Capabilities

The four main audit mechanisms in Salesforce are:

**Setup Audit Trail:** records all changes to Salesforce configuration. Accessible at Setup > Security > View Setup Audit Trail. Stores up to 6 months of data by default (Salesforce documentation states 180 days). Export to CSV for longer retention.

**Field History Tracking:** enabled per object, per field. Records old value, new value, changed by, and date. Standard retention is 18 months; Shield Field Audit Trail extends to 10 years. Up to 20 fields per object for standard; Shield extends the limit.

**Login History:** records all login attempts (successful and failed). Accessible at Setup > Security > Login History. Retains 6 months of data.

**Event Monitoring (Shield):** provides detailed telemetry on user behavior — specific reports run, records viewed, data exported, API calls made. Critical for detecting insider threats and unusual access patterns.

### SAP Audit Mechanisms

**Change Documents (CDHDR/CDPOS):** the standard mechanism for recording data changes to SAP business objects. CDHDR stores the change document header; CDPOS stores individual field changes. These tables can grow very large — archiving strategies are needed for long-running systems.

**Security Audit Log (SM20):** records system-level security events. Configured in SM19 — administrators select which events to log (all logins, failed logins, RFC calls, sensitive transaction access). Data can be exported to a SIEM system.

**Table Logging:** specific database tables can be flagged for change logging in transaction SE13. When a record in a logged table changes, SAP writes the change to table DBTABLOG. Useful for compliance monitoring of configuration tables.

**Workflow and document approval logs:** SAP Workflow records every step of an approval process, including who approved or rejected, the timestamp, and any notes provided.

---

## Section 6: Certification Focus Areas

### Salesforce Administrator Exam

The security topic area typically represents 14–15% of the Salesforce Admin exam. High-priority areas include:

- Knowing which access control mechanism to use for a given scenario (profile vs. permission set vs. OWD vs. sharing rule)
- Understanding that FLS overrides page layout visibility
- Knowing what the Setup Audit Trail captures vs. Field History Tracking
- Identifying when to use manual sharing vs. sharing rules
- Recognizing the difference between role hierarchy (record sharing) and profiles (object/field permissions)

### SAP S/4HANA Essentials Exam

Security topics tested include:

- The structure of the authorization concept (object → authorization → profile → role → user)
- The difference between a single role and a composite role
- How to diagnose an authorization failure (SU53)
- Where roles are created and maintained (PFCG)
- What SoD is and why SAP GRC manages it

---

## Key Terms for Module 13

**Profile (Salesforce):** the mandatory, baseline access configuration for every Salesforce user; each user has exactly one.

**Permission Set:** a bundle of additional permissions assigned on top of a profile; users can have multiple.

**Permission Set Group:** a collection of permission sets assigned as a single unit.

**Organization-Wide Default (OWD):** the baseline sharing level for all records of an object type.

**Role Hierarchy:** a Salesforce mechanism that grants managers visibility into their subordinates' records.

**Sharing Rules:** automated rules that extend record access to groups of users based on ownership or field criteria.

**Field-Level Security (FLS):** controls field visibility and editability at the profile or permission set level.

**Authorization Object (SAP):** a structured definition of a controllable business function including its field values.

**Single Role (SAP):** a named collection of transaction codes and the generated authorization profile.

**Composite Role (SAP):** a collection of single roles assigned together to a user.

**PFCG (SAP):** the transaction for creating and maintaining roles and generating authorization profiles.

**SU53 (SAP):** the transaction that displays the last failed authorization check for a user.

**SoD (Segregation of Duties):** the principle that critical process steps must be controlled by different individuals.

**SAP GRC:** Governance, Risk, and Compliance — SAP's platform for managing SoD and access risk.

**Setup Audit Trail (Salesforce):** logs all Salesforce configuration changes.

**Field History Tracking (Salesforce):** logs field-level data changes on configured objects.

**Change Documents (SAP):** logs field-level data changes to business objects in CDHDR/CDPOS.

**Security Audit Log (SAP):** logs authentication and system security events; configured in SM19/SM20.

---

## Study Questions

1. Explain why every Salesforce user must have exactly one profile, and describe the key difference between using profiles versus permission sets for managing access.

2. A user reports they cannot see the "Annual Revenue" field on Account records. You confirmed the field is on the page layout. What is the most likely cause, and how would you fix it?

3. Describe the four record-level access mechanisms in Salesforce. For each one, give a scenario where it is the appropriate tool to use.

4. What is the authorization check flow in SAP? What happens at each step when a user attempts to open a transaction?

5. Explain the difference between a single role and a composite role in SAP. Why is using composite roles considered a best practice for assigning access to job positions?

6. What is Segregation of Duties, and why is it classified as an internal control requirement rather than just a best practice for publicly traded companies?

7. A new procurement analyst needs access to create purchase orders and receive goods in SAP. Your GRC analyst flags this combination as a high-risk SoD conflict. How do you resolve it without denying the analyst the access they need to do their job?

8. Compare the Salesforce Setup Audit Trail to Field History Tracking. What does each capture, and how long is data retained in each?

9. What is SAP's Security Audit Log (SM20) used for, and how does it differ from Change Documents?

10. A Salesforce Administrator finds that a user has accumulated 12 permission sets over three years and now effectively has System Administrator-level access despite having a Standard User profile. What process should prevent this situation, and what immediate steps should the administrator take?

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*

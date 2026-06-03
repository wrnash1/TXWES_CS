# Reading Guide: Module 13 — ERP Security and Roles

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Certification Alignment: Salesforce Certified Associate | SAP Certified Associate

---

## Introduction

ERP security controls who can access data, what they can do with it, and provides a record of all actions taken. Poor security design creates fraud opportunities and compliance failures. Strong security design enforces separation of duties, limits access to the minimum required for each role, and creates an audit trail that supports investigation and regulatory compliance. This module covers the security principles and platform-specific security architectures of SAP and Salesforce — both heavily tested on their respective certification exams.

---

## Section 1: High-Yield Glossary

**Separation of Duties (SoD)**
The security control that prevents one person from having complete control over a critical business transaction. Classic SoD example: the person who creates vendor records should not also be the person who approves payments to vendors.

**Least Privilege**
The principle that users should have only the minimum access necessary to perform their job functions. Reduces the damage that can result from compromised accounts or malicious insiders.

**Audit Trail**
A logged record of user actions, data changes, and security events in the ERP system. Provides evidence for fraud investigations, compliance reviews, and security incident analysis.

**Authorization Object (SAP)**
The fundamental unit of SAP security. An authorization object groups related authorization fields (e.g., company code, activity type) that are checked together when a user performs an action. Users must have matching field values in their profiles to proceed.

**Activity (SAP)**
A field within SAP authorization objects that specifies what the user can do. Common activity codes: 01 = Create, 02 = Change, 03 = Display, 06 = Delete, 16 = Execute.

**Role (SAP — transaction PFCG)**
A collection of authorization objects representing a job function. Users are assigned roles; roles contain the authorization profiles that grant access. Transaction PFCG (Profile Generator) is used to create and maintain roles.

**SU01 — User Maintenance (SAP)**
The SAP transaction for creating and maintaining user accounts. User records in SU01 include assigned roles, login restrictions, password settings, and organizational assignments.

**SAP GRC (Governance, Risk, and Compliance)**
SAP's suite for managing access controls, identifying SoD conflicts across role assignments, and managing compliance workflows. GRC Access Control can run automatic SoD analysis across all user-role assignments.

**Profile (Salesforce)**
The required security assignment for every Salesforce user. Controls object-level CRUD permissions (Create, Read, Update, Delete), field-level security (FLS), login hours, IP restrictions, and default app assignment. Every user has exactly one Profile.

**Permission Set (Salesforce)**
An additive collection of permissions that can be granted to specific users in addition to their Profile. Used to extend access for edge cases without creating a new Profile. A user can have multiple Permission Sets.

**Organization-Wide Defaults (OWD)**
The baseline record sharing setting for each Salesforce object. Determines who can see records by default before role hierarchy and sharing rules are applied. Settings: Private (owner + role hierarchy), Public Read Only (all users can read), Public Read/Write (all users can read and edit).

**Role Hierarchy (Salesforce)**
A hierarchical structure of roles that controls upward record visibility. Users in higher roles automatically see records owned by users in roles below them. Does not control CRUD permissions.

**Sharing Rule (Salesforce)**
A configuration that extends record sharing beyond OWD and role hierarchy. Can be criteria-based (share records where field = value) or owner-based (share records owned by users in role X). Can only open access — cannot restrict access beyond OWD.

**Field-Level Security (FLS)**
Controls whether a specific field on a Salesforce object is visible, read-only, or editable for users with a given Profile or Permission Set. FLS operates independently of record-level access.

**SM20 — Security Audit Log (SAP)**
The SAP transaction that displays the Security Audit Log. Records logon events, failed login attempts, blocked authorization checks, and sensitive transaction calls. Primary tool for security investigation in SAP.

**Setup Audit Trail (Salesforce)**
Records all configuration changes made in Salesforce Setup: custom fields added, sharing rules modified, users created, permission sets changed. Retains 180 days of history.

**Field History Tracking (Salesforce)**
Records the last 20 field value changes per record on enabled objects. Shows who changed each tracked field, from what value, to what value, and when. Enabled per object, up to 60 fields per object.

---

## Section 2: SAP Security Architecture

### Authorization Object Hierarchy

```text
USER (SU01)
  |
  | assigned Roles
  |
ROLE (PFCG)
  |
  | contains Authorization Objects
  |
AUTHORIZATION OBJECT
  |
  | contains field values
  |
FIELD VALUES
  e.g., BUKRS = 1000 (Company Code)
        ACTVT = 01, 03 (Create and Display)

RUNTIME CHECK:
  User executes transaction (e.g., FB01 - Post FI Document)
    --> SAP checks Authorization Object F_BKPF_BUK
    --> Checks: user's BUKRS includes 1000?
    --> Checks: user's ACTVT includes 01?
    --> If both match: access granted
    --> If either missing: access denied (authorization error)
```

### Key SAP Authorization Objects

| Object | Module | Controls |
|---|---|---|
| F_BKPF_BUK | FI | Accounting document posting by company code and activity |
| F_LFA1_BUK | FI-AP | Vendor master maintenance by company code and activity |
| M_MSEG_BWA | MM | Goods movements by movement type |
| M_BEST_BSA | MM | Purchase order creation by document type |
| V_VBAK_AAT | SD | Sales order creation by order type |
| P_ORGIN | HCM | HR master data access by personnel area and infotype |

### SAP Role Design Principles

| Principle | Description |
|---|---|
| Single Role | Contains authorization objects for one specific job function or task |
| Composite Role | A collection of single roles assigned to a user as a package |
| Derived Role | A copy of a parent role with different organizational scope (e.g., same job, different company code) |
| Reference Role | A template role used to create derived roles; never assigned to users directly |

### SoD Conflict Examples

| SoD Conflict | Risk | Prevention |
|---|---|---|
| Vendor create + Payment authorization | Can create fictitious vendor and pay them | Separate roles: Z_VENDOR_ADMIN and Z_AP_PAYMENT never assigned to same user |
| Purchase Order create + GR posting | Can create PO and fake receipt for non-existent goods | Separate buying and receiving functions |
| Customer master create + AR posting | Can create fictitious customer and post fake revenue | Separate customer admin from AR posting |
| User create + Role assignment | Can create new user and grant them elevated access | Separate user admin from security admin |
| Journal entry create + Approval | Can create and approve own journal entries | Require second-person approval for manual JEs |

---

## Section 3: Salesforce Security Architecture

### Four Security Layers

```text
SALESFORCE SECURITY MODEL (inside out = most restrictive first)

LAYER 1: Profile (most fundamental)
  - Object CRUD permissions (Can user Create/Read/Update/Delete?)
  - Field-level security (Can user see/edit this specific field?)
  - System permissions (login hours, IP restrictions)
  - Controls WHAT a user can do with records

LAYER 2: Organization-Wide Defaults (OWD)
  - Private: only record owner + role hierarchy sees records
  - Public Read Only: all users can read all records
  - Public Read/Write: all users can read and edit all records
  - Controls WHO can see records by default

LAYER 3: Role Hierarchy
  - Manager roles see records owned by subordinate roles
  - Only relevant when OWD is Private or Read Only
  - Controls UPWARD record visibility for managers

LAYER 4: Sharing Rules / Manual Shares
  - Extend access beyond OWD + hierarchy
  - Cannot restrict access below OWD
  - Criteria-based or owner-based sharing
  - Controls LATERAL record sharing (peers, cross-team)
```

### Profile vs. Permission Set

| Aspect | Profile | Permission Set |
|---|---|---|
| Required? | Yes — every user must have one | No — optional, additive |
| How many per user? | Exactly one | Multiple allowed |
| Purpose | Baseline permissions for a group of users | Extra permissions for specific users |
| When to use | Standard access for a job role | Edge case access for a few users |
| Exam answer | "A few users need extra access" = Permission Set | "All users of this type need access" = Profile |

### OWD Decision Matrix

| Requirement | OWD Setting |
|---|---|
| All users need to see all records | Public Read/Write or Public Read Only |
| Users should only see their own records by default | Private |
| Managers need to see subordinate records | Private + Role Hierarchy |
| Specific groups need cross-team sharing | Private + Sharing Rules |

### Salesforce Audit Tools

| Tool | Location | What It Records | Retention |
|---|---|---|---|
| Setup Audit Trail | Setup > Security | Configuration changes: fields added, rules modified, users created | 180 days |
| Field History Tracking | Object Manager > Fields | Field value changes on tracked fields per record | Last 20 changes per field |
| Login History | Setup > Users | User login attempts, success/failure, IP address | 6 months |
| Debug Logs | Setup > Logs | Apex execution, SOQL queries, workflow execution | Until deleted or 24 hours |

---

## Section 4: Compliance Frameworks and ERP Security

### Common Regulatory Requirements

| Regulation | Industry | Key ERP Security Requirement |
|---|---|---|
| SOX (Sarbanes-Oxley) | Public companies | SoD enforcement in financial processing; audit trail for financial document changes; access control review |
| HIPAA | Healthcare | Protected health information access restricted to authorized personnel; audit log of all PHI access |
| GDPR | EU data subjects | Personal data access restricted; audit trail of data processing; right to erasure workflows |
| PCI DSS | Payment card processors | Cardholder data access restricted; strong authentication; audit logs retained 1 year |

### SAP GRC Access Control Workflow

```text
USER ACCESS REQUEST
        |
        v
GRC ACCESS REQUEST FORM
  (user requests role assignment)
        |
        v
AUTOMATED SoD CHECK
  Does requested role + current roles = SoD conflict?
  - Yes: Flag for manager and compliance review
  - No: Route to manager approval only
        |
        v
MANAGER APPROVAL
        |
        v
[If SoD conflict] RISK OWNER REVIEW
  Accept risk with documented justification?
  - Yes: Proceed with compensating control
  - No: Role request denied
        |
        v
ROLE ASSIGNED IN SAP (SU01)
        |
        v
PERIODIC ACCESS REVIEW (quarterly/annual)
  Certify all role assignments still appropriate
```

---

## Section 5: Certification Exam Tips

1. **Separation of Duties is the most tested security concept.** Any scenario where one person can create AND approve or create AND pay involves an SoD conflict. The answer is always to split those functions between different roles/users.

2. **Salesforce OWD is the floor, not the ceiling.** OWD can only be opened (made less restrictive) by role hierarchy, sharing rules, and manual shares. It cannot be made more restrictive by those tools. To restrict access, you must change the OWD.

3. **Profile controls CRUD and FLS; Role Hierarchy controls record visibility.** These are different security dimensions. A user can have Read access on an object (Profile) but still not see a specific record if the OWD is Private and they are not the owner or in the owner's role hierarchy.

4. **Permission Set = additive, not replacement.** Permission Sets add to what a Profile already grants. They cannot remove permissions that a Profile grants. Use Permission Sets for "a few users need something extra," not for "a few users should not have what others have."

5. **SAP SM20 = Security Audit Log.** This transaction is always the answer when an auditor asks "who accessed what in SAP?" Combined with Change Documents, SM20 provides the complete audit trail for financial document access and modification.

6. **SAP Roles are created in PFCG.** The Profile Generator (PFCG) is how SAP roles are built — authorization objects are added, field values are set, and profiles are generated. Users are assigned in SU01.

7. **Sharing Rules can only open access, not restrict it.** This is commonly tested. A Sharing Rule cannot make a Public Read Only record visible to fewer people. To restrict visibility, change the OWD.

8. **Field-Level Security is independent of record-level security.** A user can have access to a record but be blocked from seeing a specific field by FLS. These are two separate security layers that must both be configured correctly.

---

## Section 6: Required Study Resources

Complete before attempting the quiz:

- **Salesforce Trailhead — Data Security**
  trailhead.salesforce.com — search "Data Security"
  Covers OWD, Role Hierarchy, Profiles, Permission Sets, and Sharing Rules tested on the Certified Associate exam.

---

## Section 7: Study Checklist

- Memorize the three security principles: Separation of Duties, Least Privilege, Audit Trail.
- Draw the Salesforce four-layer security model from memory (Profile, OWD, Role Hierarchy, Sharing Rules).
- Know the OWD settings (Private, Public Read Only, Public Read/Write) and when each is appropriate.
- Understand the distinction between Profile (CRUD + FLS) and Role Hierarchy (record visibility).
- Know when to use a Permission Set vs. a new Profile — this is a frequently tested Certified Associate question.
- Review the SAP SoD conflict examples in Section 2.
- Know SAP transactions SM20 (Security Audit Log) and SU01 (User Maintenance) and PFCG (Profile Generator).
- Review the Salesforce audit tools table in Section 3.
- Complete Salesforce Trailhead "Data Security" module.
- Watch the Module 13 video lecture.
- Complete Lab 13.
- Post to Discussion Forum 13 by Wednesday at 11:59 PM.
- Complete Quiz 13 (10 questions).

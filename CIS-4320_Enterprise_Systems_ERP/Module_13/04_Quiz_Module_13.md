# Quiz: Module 13 - ERP Security & Roles

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

Which security concept is violated if a single ERP user is authorized to both create vendor records AND approve payments to those vendors?

* A) Least Privilege — the user has more permissions than needed for their job function
* B) Separation of Duties (SoD) — one person controls the full vendor-to-payment transaction cycle, enabling undetected fraud
* C) High Availability — the system cannot remain operational if a single user is unavailable
* D) Single Sign-On — the user should not be required to authenticate twice for two different functions

* **Correct Answer:** B) SoD prevents fraud by requiring that critical transactional tasks — such as creating a vendor and authorizing payment to that vendor — be performed by different people.
* **Distractor Analysis:**
  * *Why B is correct:* A user who can both add a fictitious vendor and approve payments to that vendor can redirect company funds to themselves without any other user needing to act. SoD is the control designed specifically to prevent this fraud scenario.
  * *Why A is incorrect:* Least Privilege is a related concept (users should have only the minimum access needed) but it does not specifically address the fraud risk of one person controlling an entire transaction workflow.
  * *Why C is incorrect:* High Availability refers to system uptime and redundancy; it has no connection to the access control fraud risk described.
  * *Why D is incorrect:* Single Sign-On is an authentication convenience feature; it describes how users log in, not how permissions are divided between people.

---

### Question 2

In Salesforce, which of the following best describes a **Permission Set**?

* A) A mandatory assignment that defines a user's baseline login restrictions, default app, and object-level CRUD permissions
* B) A configuration setting that determines which records all users in the organization can see by default (the record visibility baseline)
* C) An additive collection of permissions granted to specific users on top of their Profile, without requiring a new Profile to be created
* D) A role in the role hierarchy that grants users visibility into records owned by people below them in the org chart

* **Correct Answer:** C) A Permission Set is an additive permission bundle that can be assigned to individual users to extend their access beyond what their Profile provides, without creating a new Profile for every edge case.
* **Distractor Analysis:**
  * *Why C is correct:* Permission Sets are the Salesforce best-practice solution when one or a few users need access to something that others on the same Profile don't. The Associate exam frequently tests this: "use a Permission Set, not a new Profile."
  * *Why A is incorrect:* This describes a Profile — the required baseline security assignment for every Salesforce user that sets login restrictions, default app, and object CRUD permissions.
  * *Why B is incorrect:* This describes Organization-Wide Defaults (OWD) — the baseline record sharing setting (Public Read/Write, Public Read Only, or Private) that determines the floor of record visibility before roles and sharing rules apply.
  * *Why D is incorrect:* This describes the Salesforce Role Hierarchy — roles grant upward record visibility so managers can see subordinates' records, but they do not control object/field permissions (that is Profiles and Permission Sets).

---

### Question 3

A Salesforce administrator receives a request: "Sales reps should not be able to see each other's Opportunity records, but managers should be able to see all records owned by their team." Which security configuration achieves this?

* A) Set Opportunity OWD to Public Read/Write so all users can see all records
* B) Set Opportunity OWD to Private and use the Role Hierarchy so managers' roles are above their reps' roles
* C) Create a Permission Set granting Read access to all Opportunity records and assign it to all sales reps
* D) Create a Sharing Rule that grants all users Read/Write access to Opportunities owned by users in the Sales role

* **Correct Answer:** B) Setting OWD to Private restricts each rep to seeing only their own records, while the Role Hierarchy automatically grants upward visibility so managers see all records owned by subordinate roles.
* **Distractor Analysis:**
  * *Why B is correct:* Private OWD + Role Hierarchy is the standard Salesforce pattern for this requirement. Private ensures reps cannot see peers' records; the hierarchy opening ensures managers see their team's records without any additional configuration.
  * *Why A is incorrect:* Public Read/Write gives all users visibility into all records, which explicitly violates the requirement that reps not see each other's opportunities.
  * *Why C is incorrect:* A Permission Set granting Read to all Opportunities would give every rep visibility into every rep's records — the opposite of what is required.
  * *Why D is incorrect:* A Sharing Rule granting all users access to records in the Sales role would again expose all reps' records to all other reps, violating the requirement.

---

### Question 4

An external auditor asks for evidence of which users accessed the financial module and changed invoice amounts over the past 90 days in the SAP system. Which capability provides this information?

* A) The SAP IMG (Implementation Guide) transaction that shows configuration history
* B) The SAP system audit log (transaction SM20) and change document history, which record user logins, transactions executed, and field-level changes to documents
* C) The SAP job scheduler (transaction SM36) showing which batch jobs ran during the period
* D) The SAP transport log showing which system changes were moved from development to production

* **Correct Answer:** B) SAP's Security Audit Log (SM20) records logon events, transaction calls, and authorization failures; change documents record field-level before/after values for every change to financial documents.
* **Distractor Analysis:**
  * *Why B is correct:* The combination of the Security Audit Log and Change Documents is SAP's primary evidence source for financial audit trails. Change documents on FI documents show who changed what field from what value to what value, with a timestamp.
  * *Why A is incorrect:* The IMG records configuration (customizing) changes to the system setup, not user activity on business documents like invoices.
  * *Why C is incorrect:* The job scheduler log shows scheduled background jobs; it does not track interactive user access to specific financial documents.
  * *Why D is incorrect:* Transport logs record system code and configuration being moved between SAP landscapes (DEV → QAS → PRD); they do not track user document changes in the production system.

---

### Question 5

A company's Salesforce org has sensitive compensation data stored in a custom object. The security requirement states that only HR managers should be able to read this object, and no other user — regardless of their role — should have access. Which combination of settings correctly implements this?

* A) Set the object's OWD to Public Read Only and create a sharing rule granting HR managers Read/Write access
* B) Set the object's OWD to Private, remove Read permission from all Profiles except the HR Manager profile, and confirm no Permission Sets grant Read to other users
* C) Set the object's OWD to Public Read/Write and use field-level security to hide the salary field from non-HR users
* D) Create a role called "HR Restricted" at the top of the role hierarchy so HR managers inherit access to all records in the org

* **Correct Answer:** B) Private OWD restricts record visibility; removing Read permission from all non-HR Profiles at the object level blocks CRUD access; auditing Permission Sets ensures no back-door access exists.
* **Distractor Analysis:**
  * *Why B is correct:* Securing sensitive data in Salesforce requires both record-level visibility control (OWD Private) and object-level permission control (Profile CRUD). Both layers must be configured; either alone is insufficient.
  * *Why A is incorrect:* Public Read Only OWD makes all records visible to all users by default; even with a sharing rule for HR managers, every other user could still read all records — the opposite of the requirement.
  * *Why C is incorrect:* Hiding one field (salary) with FLS still leaves the entire object and all other fields visible to all users; the requirement is to restrict the entire object, not just one field.
  * *Why D is incorrect:* Placing a role at the top of the hierarchy grants the role-holder visibility into all records in the org — which is a system-wide visibility grant, not restricted HR-only access.

---

### Question 6

(5 points)

In SAP, the transaction PFCG is used to maintain Authorization Roles. What is the primary function of an SAP Authorization Role, and how does it differ from a User ID (SU01)?

- A) An Authorization Role stores a user's password policy; a User ID stores the user's transaction history
- B) An Authorization Role is a container of Authorization Objects and values that define what a user can do in SAP; a User ID is the individual login account to which one or more Roles are assigned
- C) An Authorization Role and a User ID are interchangeable terms in SAP — both refer to the login account
- D) An Authorization Role is maintained by end users to customize their menu; a User ID is maintained only by the basis team

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* In SAP, authorization is role-based. PFCG creates Roles that contain Authorization Objects (the technical permission definitions) with specific field values (e.g., which company codes, which transaction codes, which activity types are allowed). SU01 creates the User ID and assigns roles to it. The role defines what is permitted; the user ID determines who holds those permissions.
  - *Why A is incorrect:* Password policy is configured at the client or system level, not stored in an Authorization Role. Transaction history is in the Security Audit Log (SM20), not in the User ID.
  - *Why C is incorrect:* Authorization Roles and User IDs are distinct objects. A single Role can be assigned to hundreds of User IDs. A single User ID can hold multiple Roles. They are not interchangeable.
  - *Why D is incorrect:* End users do not maintain Authorization Roles — PFCG is a basis/security administrator transaction. Users can personalize their SAP menus through favorites, but this is separate from authorization role maintenance.

---

### Question 7

(5 points)

A Salesforce administrator needs to grant a specific set of users the ability to view and edit a custom "Project Budget" field on the Opportunity object, without changing any other permissions for those users. Which combination of tools achieves this with the least administrative overhead?

- A) Create a new Profile with the Budget field visible and editable, and reassign all affected users to the new Profile
- B) Create a Permission Set that grants Read and Edit access to the Project Budget field, and assign it only to the users who need it
- C) Change the Organization-Wide Default for the Opportunity object to Public Read/Write, which will expose all fields to all users
- D) Create a Sharing Rule that grants Read/Write access to Opportunity records owned by users in the affected group

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Permission Sets are the correct tool for granting additive, targeted permissions to a subset of users without creating new Profiles. The administrator creates one Permission Set with the specific field-level security setting and assigns it to the affected users. This is the Salesforce best-practice pattern: "use Permission Sets for exceptions, not new Profiles."
  - *Why A is incorrect:* Creating a new Profile for a single field-level difference violates the Salesforce best practice of minimizing Profile proliferation. If these users otherwise share the same Profile, the correct solution is a Permission Set, not a new Profile.
  - *Why C is incorrect:* Changing OWD affects record-level visibility (who can see which records), not field-level security. OWD to Public Read/Write would open all Opportunity records to all users, which is far broader than the requirement and a security risk.
  - *Why D is incorrect:* Sharing Rules control which records a user can access, not which fields within a record they can see or edit. Field-level security is controlled through Profiles and Permission Sets, not sharing rules.

---

### Question 8

(5 points)

Which of the following correctly describes the Salesforce Field-Level Security (FLS) control and its relationship to object-level permissions?

- A) FLS replaces object-level permissions — if a field is visible, the object is automatically accessible
- B) FLS is a subordinate layer to object-level permissions — a user must have object Read access before FLS settings for individual fields on that object have any effect
- C) FLS only applies to custom fields; standard Salesforce fields (like Account Name) cannot be hidden using FLS
- D) FLS is configured per record and is different for each record instance of the same object

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Salesforce security layers work in sequence. Object-level permissions (Read, Create, Edit, Delete, View All, Modify All) are evaluated first. If a user lacks object-level Read, they cannot access any records or fields on that object regardless of FLS. FLS then applies within the object to restrict which specific fields the user can see or edit. Both layers must grant access for a user to interact with a field.
  - *Why A is incorrect:* FLS does not override or replace object-level permissions. Making a field visible in FLS has no effect if the user lacks the object-level Read permission. The two controls operate at different layers of the security model.
  - *Why C is incorrect:* FLS applies to both standard and custom fields. An administrator can hide standard fields (like Account Revenue, Contact Phone) from users via FLS settings on their Profile or Permission Set.
  - *Why D is incorrect:* FLS is configured at the object-field level globally (per Profile or Permission Set), not per individual record. All records of the same object type present the same field visibility to the same user.

---

### Question 9

(5 points)

An SAP security administrator receives an SoD conflict report showing that user JSMITH has both the "Create Vendor" authorization and the "Post Vendor Payment" authorization. What is the recommended remediation in SAP, and what compensating control could be implemented if role redesign is not immediately feasible?

- A) Remove user JSMITH from the system entirely until the SoD conflict is resolved
- B) Remove one of the conflicting authorizations from JSMITH's role assignment, ideally assigning the payment posting role to a different user; if immediate redesign is not feasible, implement a mitigating control such as requiring a second approver for all payments posted by JSMITH
- C) Create a new composite role that combines both authorizations, which resolves the conflict by officially documenting it
- D) Set JSMITH's password to expire daily so that the fraud window is limited

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The standard SoD remediation is role separation — one person creates vendors, a different person posts payments. In SAP, this means removing one of the conflicting authorization objects from JSMITH's role profile in PFCG. When immediate redesign is not feasible (e.g., staffing constraints), a compensating control (such as a supervisory review of all payments by JSMITH, or a workflow approval step) reduces the fraud risk while the permanent fix is implemented.
  - *Why A is incorrect:* Removing the user from the system is disproportionate and would halt legitimate business activity. SoD remediation is about access restructuring, not user removal.
  - *Why C is incorrect:* Combining conflicting authorizations into a composite role does not resolve the conflict — it formalizes it. The conflict exists because the same person controls a complete fraud cycle; adding a wrapper role does not change that.
  - *Why D is incorrect:* Daily password expiration has no effect on SoD risk. The fraud risk from SoD violations exists during any session when the user is logged in — a short password cycle does not prevent the user from exercising both conflicting permissions.

---

### Question 10

(5 points)

In Salesforce, a sales manager complains that she cannot see the Opportunity records of a sales rep who reports to her. The admin confirms the Opportunity OWD is set to Private and the manager's role is directly above the rep's role in the Role Hierarchy. What is the most likely cause of the issue?

- A) The manager needs a Permission Set that grants Read access to all Opportunity records
- B) The rep's Opportunity records are owned by a different user than the rep — the record owner is not in a role below the manager, so the hierarchy grant does not apply
- C) The OWD needs to be changed to Public Read Only to allow manager visibility
- D) Sharing Rules need to be created for every manager-rep pair to grant visibility

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The Role Hierarchy grants visibility based on record ownership. If the Opportunity records are owned by a user who is NOT in a role subordinate to the manager's role — for example, if the records were created by a different rep, or if a queue or another user is the owner — the hierarchy grant does not activate. The admin should check the Owner field on the specific records the manager cannot see.
  - *Why A is incorrect:* A Permission Set granting Read on all Opportunities would work, but the question asks for the most likely cause of the existing issue given the stated configuration. The correct diagnosis is record ownership, not a missing Permission Set.
  - *Why C is incorrect:* Changing OWD to Public Read Only would expose all Opportunity records to all users — which is broader than needed and violates the stated intent of the Private OWD. The correct fix is to diagnose the ownership issue, not change the OWD.
  - *Why D is incorrect:* If the Role Hierarchy is correctly configured (manager's role above rep's role), Sharing Rules should not be required for the manager to see the rep's records. Sharing Rules are needed when the hierarchy does not cover the case — but first the admin should confirm actual record ownership.

---

### Question 11

(5 points)

A company's internal audit team reviews Salesforce and finds that 15 sales reps all share the same login credentials (username and password) for a shared "team account" because it is "more convenient." Which security principle does this violate, and what specific risk does it create?

- A) High Availability — a shared account creates a single point of failure if the password is changed
- B) Individual Accountability — when multiple users share one login, it is impossible to determine which person performed a specific action in the audit trail, enabling undetected misconduct
- C) Least Privilege — the shared account likely has more permissions than any individual rep needs
- D) Separation of Duties — sharing credentials allows users to perform each other's job functions

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Individual Accountability requires that every action in an ERP or CRM system be traceable to a specific individual. When 15 people share one login, the audit trail shows only the shared account name — investigations into data changes, record deletions, or unauthorized access cannot identify the responsible individual. This nullifies the forensic and compliance value of the audit log entirely.
  - *Why A is incorrect:* High Availability concerns system uptime and redundancy. A shared account does create a single point of failure if the password is lost, but that is a business continuity risk, not the primary security violation described.
  - *Why C is incorrect:* Least Privilege concerns whether a user has more access than their role requires. While the shared account might have excess permissions, the primary violation described is the accountability gap from shared credentials — not the scope of permissions.
  - *Why D is incorrect:* Separation of Duties concerns one person controlling a complete fraud cycle across incompatible functions. Credential sharing is an accountability and audit trail problem, not an SoD problem per se (the reps likely perform the same functions, not incompatible ones).

---

### Question 12

(5 points)

In SAP S/4HANA, a user attempts to execute transaction FB60 (Enter Vendor Invoice) and receives the error "You are not authorized to perform this activity." Which SAP object controls this authorization, and what must the basis administrator do to grant the user access?

- A) The user's password has expired; the administrator must reset it in SU01
- B) The user lacks the required Authorization Object (S_TCODE for FB60, and likely the FI-AP specific authorization objects); the administrator must add the correct authorization to the user's Role in PFCG and regenerate the Profile
- C) The transaction FB60 has been locked by another user; the administrator must wait for the lock to release
- D) The user is in the wrong Company Code; switching to Company Code 1000 will resolve the authorization error

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* SAP authorization errors ("not authorized") mean the user's assigned roles do not contain the required Authorization Object with the correct field values. For FB60, the user needs S_TCODE (transaction code authorization) plus F_BKPF_BUK (Company Code authorization for FI documents) and other FI-AP authorization objects. The fix is to add those authorization objects with appropriate values to the user's Role in PFCG, save, and regenerate the authorization profile.
  - *Why A is incorrect:* A password expiration would prevent login entirely — the user would not reach the point of attempting to execute FB60. An authorization error after successful login is not a password issue.
  - *Why C is incorrect:* Transaction codes cannot be locked by other users. Record-level locks exist in SAP (e.g., a specific document being edited), but the transaction code FB60 itself is always available for authorized users.
  - *Why D is incorrect:* If the user is authorized for FB60 but not for a specific Company Code, they would receive a more specific error about the Company Code. The error "not authorized to perform this activity" at the transaction level indicates a missing S_TCODE authorization — before even entering FB60.

---

### Question 13

(5 points)

A Salesforce administrator needs to grant a third-party integration user (used by an external app) access to read all Account and Contact records but no other objects. The integration should never be able to create, edit, or delete records. Which is the most appropriate security configuration?

- A) Assign the integration user the System Administrator profile, which provides full access — the application itself will enforce read-only behavior
- B) Create a dedicated integration Profile with Read-only access on Account and Contact objects only, set OWD to Public Read Only for those objects, and assign the integration user this Profile
- C) Create a Permission Set with Read access on Account and Contact and assign it to the System Administrator profile user
- D) Grant the integration user a Chatter Free license, which restricts access to read-only by default

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Integration users should follow the principle of Least Privilege. A dedicated Profile granting only the minimum required access (Read on Account and Contact, nothing else) limits the blast radius if the integration credentials are compromised. Relying on the application to enforce restrictions (Answer A) is not a security control — Salesforce security must enforce the access boundary.
  - *Why A is incorrect:* Granting System Administrator access to an integration user violates Least Privilege and creates extreme security risk. If the integration API key is stolen, the attacker has full admin access to the entire Salesforce org.
  - *Why C is incorrect:* You cannot assign a Permission Set to a Profile — Permission Sets are assigned to individual users. Also, assigning a read-only Permission Set to a System Administrator profile user still leaves all System Administrator permissions in place through the Profile.
  - *Why D is incorrect:* Chatter Free licenses provide access only to Chatter (collaboration) features — they do not grant access to standard CRM objects like Account and Contact. This license type is not appropriate for an integration user that needs to read CRM data.

---

### Question 14

(5 points)

During a Salesforce security review, an auditor finds that a Sharing Rule grants Read/Write access to all Account records owned by users in the "Sales East" role, sharing them with users in the "Sales West" role. The business states this sharing was set up for a temporary project two years ago and is no longer needed. What is the risk of leaving this Sharing Rule active, and what should the administrator do?

- A) No risk — Sharing Rules only grant read access and cannot cause data integrity issues
- B) The Sharing Rule may grant Sales West users broader access than their OWD and Role Hierarchy intend, potentially allowing them to edit or delete accounts they should not have access to; the administrator should delete the Sharing Rule after confirming with the business that it is no longer needed
- C) The Sharing Rule will automatically expire after 12 months of inactivity — no action is needed
- D) The risk is only performance-related — extra sharing records slow down query times; delete it for performance reasons only

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Sharing Rules are additive — they can only expand access beyond the OWD floor, never restrict it. A Read/Write Sharing Rule grants the target role users edit access to another team's accounts. If the business no longer needs this sharing, the Sharing Rule represents excess access that violates Least Privilege and could allow unintended data modifications. The administrator should confirm with stakeholders and delete the rule.
  - *Why A is incorrect:* The Sharing Rule in question grants Read/Write access, not just Read. Write access allows users to edit and potentially corrupt or delete records they should not be able to touch.
  - *Why C is incorrect:* Salesforce Sharing Rules do not expire automatically. They remain active indefinitely until an administrator explicitly deletes them. Stale Sharing Rules are a common finding in Salesforce security reviews.
  - *Why D is incorrect:* While excessive sharing rules can impact query performance, the primary risk here is unauthorized access, not performance. Framing this as a performance issue understates the security exposure.

---

### Question 15

(5 points)

An SAP audit shows that production system changes (configuration transports) were applied directly to the production client without going through the standard DEV → QAS → PRD transport path. Why is this a security and compliance violation, and which SAP tool is designed to prevent it?

- A) Direct production changes violate performance standards; the Change and Transport System (CTS) routes transports through the landscape to prevent performance degradation
- B) Direct production changes bypass the required testing and approval cycle, meaning untested configuration changes can corrupt live data; the SAP Change and Transport System (CTS/TMS) enforces the DEV → QAS → PRD path and can be configured to require approval before importing to production
- C) Direct production changes are permitted in emergency situations; SAP provides no technical control to prevent them
- D) The violation is only procedural — SAP's audit log records the change, which satisfies compliance requirements

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The Transport Management System (TMS) is the SAP technical control that enforces the three-system landscape. Configuration changes must be transported from DEV to QAS (for testing and business sign-off) and then to PRD (after approval). Bypassing QAS means changes were never tested — an error in a tax configuration or document posting rule could silently corrupt financial data in production. TMS can require import approval workflows before allowing PRD imports.
  - *Why A is incorrect:* While performance is a consideration in large transports, the primary risk of bypassing the transport path is untested changes reaching production — not performance degradation. The compliance violation is about change management and testing, not system performance.
  - *Why C is incorrect:* SAP TMS does provide technical controls. The basis administrator can configure TMS to require explicit approval for production imports and can lock the production client against direct manual changes (SCC4 — client settings, set to "No changes allowed").
  - *Why D is incorrect:* Logging a change does not authorize or validate it. The audit log records what happened — it does not replace the testing and approval process that the bypass circumvented. Compliance frameworks (SOX, ISO 27001) require tested, approved changes, not just logged ones.

---

### Question 16

(5 points)

A Salesforce administrator is asked to configure security so that Account records in the "Healthcare" industry are only visible to users in the "Healthcare Sales" role, while Account records in all other industries remain visible to the entire sales team (OWD = Public Read Only). Which Salesforce feature should the administrator use?

- A) Criteria-Based Sharing Rules — create a rule that shares Healthcare industry Accounts with the Healthcare Sales role based on a field criteria (Industry = Healthcare)
- B) Record Types — create a Healthcare record type that restricts visibility to the Healthcare Sales profile
- C) Validation Rules — create a rule that prevents users outside the Healthcare Sales role from viewing Healthcare accounts
- D) Set OWD to Private and create a sharing rule for every individual Account record in the Healthcare industry

- **Correct Answer:** A

- **Distractor Analysis:**
  - *Why A is correct:* Criteria-Based Sharing Rules allow an administrator to share records that meet specific field criteria with a designated group. In this case: share Account records where Industry = "Healthcare" with the Healthcare Sales role. This works in conjunction with Public Read Only OWD — all users can see non-Healthcare accounts through OWD, and Healthcare accounts get additional targeted sharing to the appropriate team.
  - *Why B is incorrect:* Record Types control the picklist values and page layouts available on a record — they do not control record visibility. A Record Type does not restrict which users can see records of that type.
  - *Why C is incorrect:* Validation Rules run during record save operations to enforce data entry rules. They cannot control which users can view records — they have no role in the record visibility security model.
  - *Why D is incorrect:* Setting OWD to Private would restrict all Account records by default, which contradicts the requirement that non-Healthcare accounts remain visible to all. Creating individual sharing rules per record is operationally impossible at scale. Criteria-Based Sharing Rules are the correct tool.

---

### Question 17

(5 points)

In Salesforce, the "View All Data" system permission is a powerful override. What does this permission do, and why should it never be granted to regular business users?

- A) View All Data grants the user access to read every record in every object regardless of OWD, Role Hierarchy, and Sharing Rules — it is an admin-level override that bypasses all record-level security and would expose confidential data to any user it is assigned to
- B) View All Data grants the user read access only to their own records plus records shared with them — it is equivalent to the standard user access level
- C) View All Data grants access to Salesforce system configuration settings, allowing users to view but not change Setup options
- D) View All Data grants access to all reports and dashboards but does not expose underlying record data

- **Correct Answer:** A

- **Distractor Analysis:**
  - *Why A is correct:* View All Data is one of the most powerful permissions in Salesforce. It completely overrides the record-level security model — OWD, Role Hierarchy, Sharing Rules, and manual shares are all bypassed. A user with View All Data can read every record in the entire org. This is appropriate only for system administrators performing data audits. Assigning it to business users would expose competitor account data, salary information, sensitive cases, and any other restricted records to that user.
  - *Why B is incorrect:* The description in B describes standard access under a Private OWD with role visibility — not what View All Data does. View All Data is specifically an override of all normal access controls, which makes it far more powerful than standard access.
  - *Why C is incorrect:* Access to Salesforce Setup (configuration) is controlled by the "Customize Application" and "Manage Users" permissions, not View All Data. View All Data specifically pertains to business data records, not configuration settings.
  - *Why D is incorrect:* View All Data grants access to the underlying records themselves, not just reports. Users with this permission can query, view, and export all records across all objects — reports are only one channel through which this access is exercised.

---

### Question 18

(5 points)

A company implements SAP GRC (Governance, Risk, and Compliance) Access Control. What problem does SAP GRC Access Control solve that cannot be addressed by PFCG role assignment alone?

- A) GRC Access Control replaces PFCG entirely — it is a newer, faster way to assign roles without using the PFCG transaction
- B) GRC Access Control provides automated SoD conflict detection across all role assignments in the system, generates risk reports, manages access request workflows, and enforces preventive controls that PFCG (which only manages roles) cannot provide
- C) GRC Access Control manages the physical security of SAP server rooms and hardware access logs
- D) GRC Access Control automatically generates compliant role designs based on job descriptions, eliminating the need for manual PFCG configuration

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* PFCG is a role maintenance tool — it defines what a role contains and assigns it to users. PFCG has no intelligence about whether a user's combination of roles creates SoD conflicts. SAP GRC Access Control adds a layer on top: it analyzes all role assignments across all users, identifies SoD violations against a risk rulebook, manages access request and approval workflows, and generates audit evidence. These are governance capabilities that extend far beyond what PFCG alone can provide.
  - *Why A is incorrect:* GRC Access Control does not replace PFCG. Roles are still maintained in PFCG; GRC provides risk analysis and workflow governance on top of the role structure. Both tools coexist.
  - *Why C is incorrect:* Physical security (server room access, hardware) is managed by physical access control systems (badge readers, security cameras) — not by SAP GRC Access Control, which operates at the application authorization layer.
  - *Why D is incorrect:* GRC Access Control does not auto-generate role designs. Role design (defining which transaction codes and authorization objects go into each role) remains a manual design activity performed in PFCG. GRC analyzes and governs the resulting assignments, it does not design roles.

---

### Question 19

(5 points)

A Salesforce org has the following configuration: Opportunity OWD = Private. A sales rep (User A) owns 50 Opportunity records. User A is in the "Sales Rep" role. The "Sales Manager" role is directly above "Sales Rep" in the hierarchy. Which of the following users can see User A's Opportunity records without any additional configuration?

- A) Any user with the "Salesforce" license type
- B) Only User A (the owner) and users whose role is at or above the "Sales Manager" role in the hierarchy
- C) Only User A (the owner) and the Salesforce System Administrator
- D) Any user who has been assigned the same Profile as User A

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* With Private OWD, record owners always see their own records. The Role Hierarchy grants upward visibility — the Sales Manager (directly above) and every role above Sales Manager in the hierarchy can see User A's records. The System Administrator also sees all records via admin permissions. Profile assignment does not affect record visibility.
  - *Why C is incorrect:* The System Administrator can see all records, but the statement that "only User A and the System Administrator" can see the records is incomplete — it ignores the Role Hierarchy grant to the Sales Manager and higher roles. The hierarchy is a core part of Private OWD sharing.
  - *Why A is incorrect:* License type (Salesforce vs. Salesforce Platform) affects which objects and features a user can access, not which specific records they can see. Private OWD controls record visibility regardless of license type.
  - *Why D is incorrect:* Profile assignment controls object-level permissions (CRUD) and field-level security — not which specific records a user can see. Two users with the same Profile but in different roles will have different record visibility under a Private OWD.

---

### Question 20

(5 points)

A company subject to SOX (Sarbanes-Oxley Act) compliance asks how SAP S/4HANA supports SOX IT general control requirements. Which two SAP capabilities are most directly relevant to SOX ITGC compliance?

- A) SAP Fiori tile layout customization and the SAP BTP integration suite
- B) The SAP Security Audit Log (SM20), which provides evidence of user access and transaction execution, and the Transport Management System (TMS), which enforces the tested-and-approved change management path for system modifications
- C) SAP S/4HANA's in-memory database performance and real-time analytics capabilities
- D) The SAP Activate methodology and its Fit-to-Standard workshop approach

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* SOX IT General Controls (ITGC) cover two primary areas: Access Controls (who can access what in the financial system) and Change Management (how system changes are tested and approved). The Security Audit Log provides the access control evidence auditors require — a trail of who logged in, what transactions they ran, and what authorization failures occurred. TMS provides the change management evidence — that all production system changes were tested in QAS and approved before deployment to PRD.
  - *Why A is incorrect:* Fiori tile layout customization is a UX personalization feature. SAP BTP integration is a technical integration platform. Neither directly addresses SOX ITGC compliance domains of access control and change management.
  - *Why C is incorrect:* In-memory database performance and real-time analytics are technical performance capabilities. SOX compliance is about financial reporting integrity and internal control evidence — not system performance characteristics.
  - *Why D is incorrect:* SAP Activate is an implementation methodology used during the project to deploy SAP. It is relevant during implementation, but SOX ITGC compliance is an ongoing operational concern of the live production system — not the implementation approach.

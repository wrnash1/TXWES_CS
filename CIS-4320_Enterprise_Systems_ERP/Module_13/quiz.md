# Quiz: Module 13 — ERP Security and Access Control

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Instructions

This quiz contains 10 multiple-choice questions worth 10 points each. Select the single best answer. Distractor analysis is provided for instructor and student review.

---

## Question 1

A Salesforce Administrator creates a new user and assigns them the "Standard User" profile. Later, the user reports they cannot see the "Contract Amount" field on Opportunity records even though the field appears on the page layout. What is the most likely cause?

A. The user's role does not include Opportunity access.

B. Organization-Wide Defaults for Opportunity are set to Private.

C. Field-Level Security for "Contract Amount" is set to hidden for the Standard User profile.

D. The user does not have the "View All" object permission on Opportunity.

**Correct Answer: C**

**Distractor Analysis:**

- **A — Role does not include Opportunity access:** Salesforce roles control record sharing, not object or field visibility. The role hierarchy does not determine whether a user can see specific fields on a layout.
- **B — OWD set to Private:** OWD controls which records are visible. It does not hide specific fields. Even with Private OWD, a user with access to a record would still see all fields unless FLS restricts them.
- **C — FLS hidden for Standard User profile (Correct):** Field-Level Security overrides the page layout. Even if a field is placed on the page layout, if FLS for that profile is set to hidden, the field will not display. This is one of the most frequently tested concepts on the Salesforce Admin exam.
- **D — View All permission:** "View All" is a record-level permission that allows seeing all records regardless of sharing. It does not affect field-level visibility. A user missing "View All" would simply not see certain records, but they would see all fields on records they can access.

---

## Question 2

In Salesforce, which of the following CANNOT be accomplished with a Permission Set?

A. Granting a user access to a custom app

B. Removing the Delete permission from an object the user's profile allows deletion on

C. Adding field-level access to a field that is hidden in the user's profile

D. Enabling a system permission such as "Manage Users"

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Permission sets can grant access to specific apps. This is a supported use case.
- **B — Removing Delete permission (Correct):** Permission sets can only ADD permissions on top of a profile. They cannot take away permissions granted by the profile. To remove the Delete permission, the administrator must modify the profile itself. The one exception is the Muting Permission Set within a Permission Set Group, which can suppress permissions — but a standalone permission set cannot remove profile-level permissions.
- **C:** Permission sets can make a field visible that the profile has hidden. Expanding FLS is a valid permission set use case.
- **D:** System permissions like "Manage Users" can be enabled in a permission set. This is explicitly supported and commonly used to delegate specific administrative capabilities without assigning the full System Administrator profile.

---

## Question 3

Pinnacle Company sets the Organization-Wide Default for Opportunity to "Private." A Regional Director needs to see all Opportunities owned by their three direct reports but does not own any of those Opportunities themselves. Without any additional configuration, can the Regional Director see those records?

A. No — Private OWD means no sharing at all.

B. Yes — OWD "Private" still allows managers in the role hierarchy to see subordinates' records.

C. No — the manager needs a sharing rule granting Read access to those Opportunities.

D. Yes — the manager's profile includes "View All" for Opportunity by default.

**Correct Answer: B**

**Distractor Analysis:**

- **A:** This is a common misconception. "Private" OWD does not mean absolutely no sharing. It means that the default access for users who are not the record owner is Private. However, the role hierarchy independently grants upward visibility — managers always see their subordinates' records.
- **B — Role hierarchy grants upward visibility (Correct):** In Salesforce, when OWD is set to Private, the role hierarchy still grants access upward. A user higher in the role hierarchy can see records owned by users below them. The Regional Director, by virtue of being in a parent role, will see their direct reports' Opportunities without any additional sharing configuration.
- **C:** A sharing rule would be needed only if a user outside the direct reporting chain (for example, a peer in a different region) needed access. The role hierarchy handles the direct management chain.
- **D:** "View All" is a profile-level object permission that bypasses all sharing restrictions, but standard manager visibility is handled by the role hierarchy, not by "View All." Assigning "View All" to Regional Directors would give them visibility into ALL Opportunities in the org, not just their team's.

---

## Question 4

In SAP, a user receives an authorization error when attempting to post a financial document. The administrator runs transaction SU53 for that user. What information does SU53 provide?

A. A list of all roles currently assigned to the user

B. The authorization object, activity field values, and field values present in the user's authorizations

C. The last failed authorization check — showing which authorization object was missing and what field value was required

D. The complete authorization trace for all transactions the user has attempted in the past 24 hours

**Correct Answer: C**

**Distractor Analysis:**

- **A:** To see a user's role assignments, the administrator uses transaction SU01 (User Maintenance). SU53 does not list all roles.
- **B:** This is partially true in description but not what SU53 primarily shows. SU53 specifically shows the LAST failed authorization check. It displays the authorization object that failed, the field values that were checked, and what the user currently has. This is subtly different from "all values present."
- **C — SU53 shows the last failed authorization check (Correct):** SU53 is the primary diagnostic tool for authorization failures. It displays: the authorization object that caused the failure, the required field values, and what the user actually has assigned. This allows the administrator to identify exactly which authorization is missing and which role or profile needs to be updated.
- **D:** SU53 only captures the most recent failed authorization check, not a full history of authorization activity. For full authorization tracing, the administrator uses transaction ST01 (System Trace), which must be activated before the transaction is attempted.

---

## Question 5

A Salesforce Administrator is designing the security model for a B2B company. They want all Leads to be visible to all sales reps for prospecting, but only editable by the rep who owns the Lead. Which OWD setting for Lead achieves this?

A. Private

B. Public Read Only

C. Public Read/Write

D. Controlled by Parent

**Correct Answer: B**

**Distractor Analysis:**

- **A — Private:** Private OWD would mean that each sales rep can only see their own Leads unless additional sharing is configured. The requirement is that all Leads are visible to all reps — Private would prevent this.
- **B — Public Read Only (Correct):** Public Read Only allows all users to see all records of that object type. Only the record owner (or users with explicit sharing/role hierarchy access) can edit. This directly matches the requirement: visible to all, editable only by the owner.
- **C — Public Read/Write:** This would allow any sales rep to edit any Lead, not just their own. The requirement specifies that only the owning rep should be able to edit, so Read/Write is too permissive.
- **D — Controlled by Parent:** This setting is only available for objects that have a master-detail relationship to a parent object. Lead does not have a master-detail parent object, so this setting is not applicable.

---

## Question 6

Segregation of Duties (SoD) requires that no single individual controls a complete business process end-to-end. In an SAP procurement scenario, which access combination creates the highest-risk SoD conflict?

A. Creating purchase requisitions and displaying material master records

B. Creating purchase orders and posting goods receipts for the same purchase order

C. Displaying purchase orders and running inventory reports

D. Creating purchase requisitions and running vendor inquiry reports

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Displaying material master records is a read-only activity. Combining requisition creation with material display is standard — any buyer who needs to requisition materials must be able to look up the materials. This is not an SoD conflict.
- **B — Create PO and Post Goods Receipt (Correct):** This is a classic SoD conflict. If one person can create a purchase order for fictitious goods AND post the goods receipt confirming delivery, they can generate the accounting transactions for goods never received. The fraudulent goods receipt triggers a payment obligation without any legitimate delivery occurring. This combination appears on most SAP SoD conflict rulesets at the Critical risk level.
- **C:** Both activities are read-only. No SoD conflict exists between display and reporting functions.
- **D:** Creating requisitions and running vendor inquiry reports are both routine procurement activities. Viewing vendor information is necessary for creating requisitions. This is not an SoD conflict.

---

## Question 7

SAP GRC Access Control's "Emergency Access Management" (Firefighter) feature is used when:

A. A system administrator account is compromised and must be locked immediately

B. A user needs temporary elevated access to complete a time-sensitive task, and the access is logged for post-use review

C. An SoD conflict has been identified and must be automatically remediated

D. A user's access is being revoked and all their active sessions must be terminated

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Locking a compromised administrator account is handled through normal user administration (SU01 — lock user). Emergency Access Management is not a security incident response tool.
- **B — Temporary elevated access with logging (Correct):** Firefighter (EAM) provides a controlled way to grant elevated access for a specific, justified, time-limited purpose — such as a year-end close requiring a user to perform tasks that would normally violate SoD rules. All actions taken under firefighter access are logged, and a designated "owner" reviews the log after access expires. This maintains the audit trail while providing operational flexibility.
- **C:** SoD conflicts are identified and reported by Access Risk Analysis. GRC does not automatically remediate conflicts — remediation requires role redesign by the security team.
- **D:** Session termination for a compromised account is handled through system administration tools, not GRC Emergency Access Management.

---

## Question 8

Salesforce Field History Tracking is enabled on the "Stage" field of the Opportunity object. A sales manager asks how far back in the history they can see stage changes without any additional Salesforce products. What is the standard retention period?

A. 6 months

B. 18 months

C. 5 years

D. 10 years

**Correct Answer: B**

**Distractor Analysis:**

- **A — 6 months:** This is the retention period for the Salesforce Setup Audit Trail and Login History — not for Field History Tracking. Confusing these two is a common error on the Admin exam.
- **B — 18 months (Correct):** Standard Salesforce Field History Tracking retains data for 18 months (approximately 1.5 years). After that, data is automatically purged. For longer retention — up to 10 years — the organization must purchase Salesforce Shield and use the Field Audit Trail feature.
- **C — 5 years:** This retention period does not correspond to any standard Salesforce feature.
- **D — 10 years:** Ten years is the maximum retention period available with Salesforce Shield Field Audit Trail — a premium add-on product. The default, without Shield, is 18 months.

---

## Question 9

In SAP, the transaction PFCG is used to:

A. Display the last authorization check failure for a user

B. Create and maintain roles and generate authorization profiles

C. View the Security Audit Log for login and access events

D. Assign roles directly to user master records

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Displaying the last authorization check failure is the function of transaction SU53, not PFCG.
- **B — Create and maintain roles (Correct):** PFCG is the Role Maintenance transaction in SAP. It is used to create single roles and composite roles, add transaction codes to roles, set authorization object field values, and generate the authorization profile that gets assigned to users. PFCG is one of the most important transactions in SAP security administration.
- **C:** Viewing the Security Audit Log is done through transaction SM20. The audit log is configured in SM19.
- **D:** Roles are assigned to users in transaction SU01 (User Maintenance) or through batch user administration tools. PFCG is for role definition, not user assignment.

---

## Question 10

Pinnacle Company's auditors request evidence that no single Salesforce user both created and approved any contract record over the past year. Which Salesforce features would provide this evidence? (Select the most complete answer.)

A. The Setup Audit Trail, which logs all record creation events

B. Field History Tracking on the "Status" field of Contract, combined with Approval Process history

C. The organization's OWD settings for the Contract object

D. Login History for all users involved in contract workflows

**Correct Answer: B**

**Distractor Analysis:**

- **A — Setup Audit Trail:** The Setup Audit Trail records configuration changes — not data record creation or approval events. It would show if someone changed a profile or permission set, not if they created or approved a specific contract.
- **B — Field History Tracking and Approval Process history (Correct):** Field History Tracking on Contract "Status" would show when the status changed (e.g., from Draft to Approved) and who made the change. The Approval Process history records who submitted the approval request and who approved it. Together these provide evidence that the submitter and approver were different users. This combination is the appropriate audit evidence.
- **C — OWD settings:** OWD is a configuration setting that controls access levels — it is not an event log and provides no evidence about historical transactions.
- **D — Login History:** Login History shows when users logged in, not what they did in the application. It cannot demonstrate whether a user created or approved a contract.

---

## Quiz Summary

| Question | Topic | Correct Answer |
|----------|-------|----------------|
| 1 | FLS overrides page layout | C |
| 2 | Permission set cannot remove profile permissions | B |
| 3 | Role hierarchy grants upward visibility despite Private OWD | B |
| 4 | SU53 shows last failed authorization check | C |
| 5 | Public Read Only OWD for visible-not-editable access | B |
| 6 | Create PO + Post GR is highest-risk SoD conflict | B |
| 7 | SAP GRC Firefighter — temporary elevated access with logging | B |
| 8 | Field History Tracking standard retention is 18 months | B |
| 9 | PFCG is used for role creation and maintenance | B |
| 10 | Field History + Approval Process history as audit evidence | B |

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*

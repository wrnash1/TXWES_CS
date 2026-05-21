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

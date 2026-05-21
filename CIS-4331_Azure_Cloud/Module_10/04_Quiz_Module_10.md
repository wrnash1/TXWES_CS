# Quiz: Module 10 - Azure RBAC and Subscriptions

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What is the scope hierarchy in Azure from largest to smallest?

* A) Subscription -> Resource Group -> Resource -> Management Group
* B) Management Group -> Subscription -> Resource Group -> Resource
* C) Resource -> Resource Group -> Subscription -> Management Group
* D) Tenant -> Resource -> Resource Group -> Subscription
* **Correct Answer:** B) Inheritance flows from Management Groups down to Subscriptions, Resource Groups, and individual Resources.
* **Distractor Analysis:**
  * *Why correct:* Permissions assigned at a higher scope level are inherited by all child scopes below — Management Group is the highest level.
  * *Why A/C/D are incorrect:* These represent incorrect orderings. The correct sequence always flows from broadest (Management Group) to narrowest (Resource).

---

**Question 2**
Which of the following most accurately describes **RBAC scopes** in Azure?

* A) The boundaries at which role assignments apply in Azure, arranged in a four-level hierarchy (Management Group, Subscription, Resource Group, Resource) where permissions assigned at a higher level are inherited by all resources below.
* B) The geographic regions where Azure role assignments are stored and enforced, determining which datacenter processes authorization requests.
* C) Custom permission sets that override Azure's built-in roles, allowing organizations to define unique access rules not available in the default role catalog.
* D) The time windows during which RBAC role assignments are active, used to enforce just-in-time access for privileged operations.
* **Correct Answer:** A) Scopes are the boundaries at which role assignments apply — the four-level hierarchy determines permission inheritance from Management Group down to Resource.
* **Distractor Analysis:**
  * *Why A is correct:* Scope defines where a role assignment takes effect and which child resources inherit those permissions.
  * *Why B is incorrect:* Scopes are not geographic regions — they are logical management boundaries in the Azure resource hierarchy.
  * *Why C is incorrect:* That describes custom role definitions, not scopes. Scopes are where any role (built-in or custom) is assigned.
  * *Why D is incorrect:* Time-bound access is a feature of Privileged Identity Management (PIM), not RBAC scopes.

---

**Question 3**
A junior developer needs to view all resources in a Resource Group but must not be able to create, modify, or delete anything. Which built-in RBAC role should be assigned?

* A) Owner
* B) Contributor
* C) Reader
* D) User Access Administrator
* **Correct Answer:** C) The Reader role grants view-only access to Azure resources within the assigned scope — no create, modify, or delete permissions are included.
* **Distractor Analysis:**
  * *Why C is correct:* Reader is the least-privilege role for view-only access — it matches the requirement exactly.
  * *Why A is incorrect:* Owner grants full access including the ability to assign roles — far exceeds the view-only requirement.
  * *Why B is incorrect:* Contributor grants full create/manage/delete permissions (minus role assignment) — exceeds the view-only requirement.
  * *Why D is incorrect:* User Access Administrator can manage role assignments — this is an elevated role unrelated to resource viewing.

---

**Question 4**
A role assignment is made at the Subscription scope granting a user the Reader role. The subscription contains three Resource Groups, each with multiple resources. What is the effective access?

* A) The user can only view the subscription-level metadata; they cannot see resources within Resource Groups.
* B) The user has Reader access to the subscription and inherits Reader access to all Resource Groups and all resources within those groups.
* C) The user must have the Reader role assigned separately on each Resource Group to view its resources.
* D) The Reader role at the Subscription scope only applies to billing information, not to resource configurations.
* **Correct Answer:** B) Role assignments at a higher scope inherit downward — a Reader assignment at the Subscription scope gives the user Reader access to all Resource Groups and Resources within that subscription.
* **Distractor Analysis:**
  * *Why B is correct:* Azure RBAC inheritance flows downward through the scope hierarchy — subscription-level assignments automatically cover all child resource groups and resources.
  * *Why A is incorrect:* Subscription-scope assignments do propagate to child resources — inheritance is automatic.
  * *Why C is incorrect:* Separate Resource Group assignments would be redundant — the subscription-scope assignment already covers them.
  * *Why D is incorrect:* The Reader role applies to all resource configurations within the assigned scope, not just billing information.

---

**Question 5**
What is the key difference between the **Owner** and **Contributor** built-in RBAC roles in Azure?

* A) Owner can read and write resources; Contributor can only read resources.
* B) Owner can assign roles to other users; Contributor has full resource management permissions but cannot assign roles.
* C) Owner is limited to a single Resource Group; Contributor can be assigned at the Subscription scope.
* D) Owner requires Entra ID P2 licensing; Contributor works with the Free tier.
* **Correct Answer:** B) The only functional difference is role assignment — Owner can grant access to others; Contributor cannot, even though both can fully manage Azure resources.
* **Distractor Analysis:**
  * *Why B is correct:* Both Owner and Contributor can create, manage, and delete resources. The sole distinction is that Owner includes Microsoft.Authorization/roleAssignments/write permission.
  * *Why A is incorrect:* Both Owner and Contributor have full read and write access to resources — Reader is the read-only role.
  * *Why C is incorrect:* Both roles can be assigned at any scope level — Management Group, Subscription, Resource Group, or Resource.
  * *Why D is incorrect:* RBAC role assignments have no dependency on Entra ID license tier.

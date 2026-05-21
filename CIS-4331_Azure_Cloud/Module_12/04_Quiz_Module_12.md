# Quiz: Module 12 - Azure Governance & Compliance

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which resource lock type prevents users from deleting a resource but still allows them to read and modify it?

* A) ReadOnly
* B) CanNotDelete
* C) WriteLock
* D) DeleteLock
* **Correct Answer:** B) The `CanNotDelete` lock allows read and write modifications but blocks deletion requests.
* **Distractor Analysis:**
  * *Why correct:* CanNotDelete permits all read and write operations — it only blocks the delete action.
  * *Why A is incorrect:* ReadOnly is more restrictive — it blocks both write modifications and delete operations, allowing only reads.

---

**Question 2**
Which of the following most accurately describes **Azure Blueprints**?

* A) A service that packages multiple governance artifacts — including ARM templates, RBAC role assignments, and Azure Policy assignments — into a single deployable unit for setting up compliant Azure environments consistently and repeatedly.
* B) A service that evaluates individual Azure resource configurations against defined rules and can deny non-compliant deployments or trigger automatic remediation.
* C) A name-value metadata label applied to Azure resources to organize them by department, environment, or project for cost tracking and resource filtering.
* D) A lock applied at the Resource Group scope that prevents child resources from being modified or deleted, regardless of a user's RBAC permissions.
* **Correct Answer:** A) Azure Blueprints packages ARM templates, RBAC assignments, and Policy assignments together for repeatable, compliant environment deployment.
* **Distractor Analysis:**
  * *Why A is correct:* Blueprints are about packaging and deploying a consistent set of governance artifacts — they are the "environment template" including policies, roles, and infrastructure.
  * *Why B is incorrect:* That describes Azure Policy, which evaluates and enforces individual resource configuration rules.
  * *Why C is incorrect:* That describes Resource Tags, which are metadata labels with no enforcement mechanism of their own.
  * *Why D is incorrect:* That describes Resource Locks, which prevent modification or deletion of specific resources.

---

**Question 3**
An organization wants to ensure that every Azure VM deployed must use an approved VM SKU list and must have a cost-center tag. What is the correct Azure service to automatically enforce and audit these requirements?

* A) Azure Advisor
* B) Azure Blueprints
* C) Azure Policy
* D) Azure Resource Manager templates
* **Correct Answer:** C) Azure Policy can deny VM deployments that use unapproved SKUs and audit or enforce tag requirements at deployment time.
* **Distractor Analysis:**
  * *Why C is correct:* Azure Policy is the enforcement engine for organizational standards — it can block non-compliant deployments in real time and audit existing resources.
  * *Why A is incorrect:* Azure Advisor provides recommendations but cannot enforce or block deployments.
  * *Why B is incorrect:* Azure Blueprints packages multiple governance artifacts together, but the enforcement mechanism within Blueprints is Azure Policy — Policy is the direct answer.
  * *Why D is incorrect:* ARM templates define what to deploy but cannot by themselves enforce organizational standards across all deployments from all methods.

---

**Question 4**
A team accidentally deleted a production virtual network last week. Management wants to prevent this from happening again. Which Azure feature should be applied to protect the VNet going forward?

* A) Azure Policy with a "deny" effect on VNet delete operations
* B) A CanNotDelete resource lock on the VNet resource
* C) RBAC Contributor role removal from all team members
* D) Azure Advisor security recommendation acknowledgment
* **Correct Answer:** B) A CanNotDelete resource lock prevents deletion of the VNet regardless of the user's RBAC permissions — the lock must be explicitly removed before deletion is possible.
* **Distractor Analysis:**
  * *Why B is correct:* Resource locks are the specific mechanism for protecting individual resources from accidental deletion — they operate independently of RBAC.
  * *Why A is incorrect:* Azure Policy can restrict deployment of new resources but is not designed to block deletion of individual existing resources via a deny effect on delete operations.
  * *Why C is incorrect:* Removing Contributor access would prevent the team from managing any resource, not just deleting the VNet — this violates least-privilege and is operationally disruptive.
  * *Why D is incorrect:* Azure Advisor recommendations are informational — acknowledging them does not apply any protection to resources.

---

**Question 5**
What is the purpose of resource tags in Azure, and what is an important limitation of tags to know for AZ-900?

* A) Tags enforce security rules on resources — a resource without a required tag cannot be accessed by users.
* B) Tags are name-value metadata pairs used to organize and filter resources for billing and management. They do not inherit automatically from Resource Groups to child resources — this must be enforced through Azure Policy.
* C) Tags replace resource locks — applying a "protected" tag prevents a resource from being deleted.
* D) Tags are geographic location labels that determine which Azure region a resource's data is stored in.
* **Correct Answer:** B) Tags are metadata for organization and cost tracking. They do not automatically inherit to child resources — Policy is required for enforced inheritance.
* **Distractor Analysis:**
  * *Why B is correct:* Tags are purely organizational metadata and do not enforce access, protect resources, or control data location. The lack of automatic inheritance from Resource Groups is a common AZ-900 exam trap.
  * *Why A is incorrect:* Tags have no security enforcement capability — access is controlled by RBAC and NSGs.
  * *Why C is incorrect:* Tags cannot protect resources from deletion — that requires a resource lock.
  * *Why D is incorrect:* Resource location (region) is a separate property set at creation time — tags do not determine or override data residency.

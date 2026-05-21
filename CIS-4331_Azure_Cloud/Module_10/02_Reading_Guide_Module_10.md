# Reading Guide: Module 10 - Azure RBAC and Subscriptions

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 10 - Azure RBAC and Subscriptions**! This module covers Azure's access control and subscription management as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Role-Based Access Control (RBAC) is how Azure enforces the principle of least privilege — users and applications receive only the permissions they need to perform their job functions.

You will learn how RBAC roles are structured, how scope inheritance works from Management Groups down to individual resources, and how Azure Subscriptions serve as billing and management boundaries. AZ-900 frequently tests the scope hierarchy and the built-in role definitions. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Role-Based Access Control (RBAC)**: An authorization system built into Azure that grants users, groups, and service principals access to Azure resources based on their assigned role. RBAC uses the principle of least privilege — assign only the permissions needed for the task. Role assignments consist of a security principal (who), a role definition (what permissions), and a scope (where).

* **Built-in Roles (Owner, Contributor, Reader)**: Azure provides hundreds of built-in roles. The three fundamental roles are: Owner (full access including the ability to assign roles to others); Contributor (full access to create and manage resources but cannot assign roles); Reader (view-only access, cannot make changes). These roles exist at every scope level.

* **Reader**: A built-in RBAC role that grants read-only access to Azure resources within the assigned scope. A user with Reader can view resource configurations, metrics, and settings but cannot create, modify, or delete resources. AZ-900 tests when Reader is the appropriate role to assign.

* **Scopes**: The boundary at which a role assignment applies. Azure RBAC uses a four-level scope hierarchy: Management Group > Subscription > Resource Group > Resource. Role assignments made at a higher scope are inherited by all child scopes below it (e.g., a Reader role assigned at the Subscription scope applies to all Resource Groups and Resources within that subscription).

* **Azure Subscriptions**: A billing and management boundary within Azure. Each subscription is associated with an Azure account and accumulates charges separately. Subscriptions are also used to organize resources by business unit, environment (dev/test/prod), or project. Multiple subscriptions can be managed together under Management Groups.

---

### 2. Certification Exam Tips

* **Scope Hierarchy Order**: AZ-900 frequently tests the correct hierarchy. Always remember: Management Group → Subscription → Resource Group → Resource. Permissions assigned higher in the hierarchy are inherited downward. There is no way to block inheritance in Azure RBAC (unlike AWS).
* **Owner vs. Contributor**: AZ-900 tests this critical distinction. The only difference is that Owner can assign roles; Contributor cannot. If a scenario asks who can grant access to another user, only Owner (or User Access Administrator) can do this.
* **Least Privilege**: AZ-900 scenario questions about role assignment always favor the least-privilege answer. If a user only needs to view resources, assign Reader — never assign Contributor or Owner for view-only tasks.
* **Role Assignment is Additive**: If a user belongs to two groups with different role assignments, the permissions are combined (union). There are no explicit deny rules in Azure RBAC — unlike NSG rules which have explicit deny.
* **Study Resource**: The Microsoft Learn governance module covers RBAC, scope hierarchy, and subscription management with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers RBAC, scope hierarchy, and Azure subscriptions with hands-on exercises. Access it at [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* **Required Video:** This free freeCodeCamp course covers RBAC and subscription management for AZ-900 — watch the governance section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Assign the Reader role to a user at the Resource Group scope**: In the Azure portal, navigate to a Resource Group → Access control (IAM) → Add role assignment. Assign the Reader role to a test user and confirm the assignment appears in the role assignments list.
* **Verify user cannot delete resources**: Sign in as the test user and attempt to delete a resource in the assigned Resource Group. Confirm that the delete operation is blocked with an "authorization failed" error, demonstrating least-privilege enforcement.
* **Create a custom role template**: Review the JSON structure of a custom role definition using the Azure CLI (`az role definition list --name "Reader"`). Observe how actions, notActions, and assignableScopes are defined.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the RBAC and subscriptions unit in [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* [ ] Watch the governance section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for role assignment and permission verification.
* [ ] Proceed to the weekly hands-on lab activity.

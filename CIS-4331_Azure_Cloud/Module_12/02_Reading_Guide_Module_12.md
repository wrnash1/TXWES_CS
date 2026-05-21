# Reading Guide: Module 12 - Azure Governance & Compliance

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 12 - Azure Governance & Compliance**! This module covers Azure's governance tools as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Governance ensures that Azure resources are deployed and managed in accordance with organizational standards, regulatory requirements, and cost controls.

You will learn how Azure Policy enforces rules automatically, how Azure Blueprints packages governance components for repeatable environment setup, how resource locks protect critical resources from accidental deletion or modification, and how tags organize resources for cost tracking and management. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Azure Policy**: A governance service that evaluates Azure resources against defined rules (policy definitions) and enforces organizational standards at deployment time or on an ongoing basis. Policies can audit existing resources, deny non-compliant deployments, or automatically remediate configurations. Policies are assigned at Management Group, Subscription, or Resource Group scope. Azure Policy is the AZ-900 answer for automatically enforcing standards.

* **Azure Blueprints**: A service that packages multiple governance artifacts — resource group templates, ARM templates, RBAC role assignments, and Azure Policy assignments — into a single deployable unit. Blueprints enable organizations to set up compliant Azure environments repeatedly and consistently. Note: Microsoft is transitioning Blueprints to Azure Deployment Environments, but AZ-900 still covers Blueprints.

* **Resource Tags**: Name-value pairs (metadata) applied to Azure resources for organization and cost tracking. Tags enable filtering resources by department, environment, owner, or project. Tags do not affect resource behavior — they are purely organizational metadata. AZ-900 tests that tags can be applied to resources and that Azure Policy can enforce tagging requirements.

* **Resource Locks (ReadOnly, CanNotDelete)**: Locks prevent accidental or unauthorized modification or deletion of critical Azure resources, regardless of RBAC permissions. ReadOnly lock: allows read operations only — blocks all write and delete operations. CanNotDelete lock: allows read and write modifications but blocks delete operations. Locks can be applied at Resource Group or individual Resource scope and are inherited by child resources.

---

### 2. Certification Exam Tips

* **Lock types distinction**: AZ-900 tests the difference between the two lock types. ReadOnly is more restrictive — no writes allowed. CanNotDelete allows modifications but prevents deletion. Remember: you need to remove the lock before you can delete a locked resource, even if you are the Owner.
* **Policy vs. RBAC**: Both control what users can do but at different layers. RBAC controls who can perform actions (e.g., who can deploy VMs). Azure Policy controls what configurations are allowed (e.g., VMs must use approved SKUs). Use both together for complete governance.
* **Tag Inheritance**: Tags applied to a Resource Group do not automatically inherit to resources within it by default. You need an Azure Policy with the "Inherit a tag from the resource group" effect to enforce tag inheritance.
* **Initiative Definitions**: A Policy Initiative (also called a Policy Set Definition) is a collection of related policy definitions grouped together for a single assignment. AZ-900 may ask what an Initiative is — it is a group of policies assigned together, such as the built-in "Azure Security Benchmark" initiative.
* **Study Resource**: The Microsoft Learn governance module covers Azure Policy, Blueprints, locks, and tags with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers Azure governance including Policy, Blueprints, locks, and tags with knowledge checks. Access it at [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* **Required Video:** This free freeCodeCamp course covers Azure governance for AZ-900 — watch the governance and compliance section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Create a CanNotDelete lock on a virtual network resource**: In the Azure portal, navigate to a VNet resource → Locks → Add. Select "CanNotDelete" as the lock type and add a description. Observe that the lock appears in the resource's lock list.
* **Verify the VNet cannot be deleted**: Attempt to delete the locked VNet. Observe that Azure returns an error stating the resource is locked, even though your RBAC role permits deletion.
* **Apply tag metadata to resources**: Apply a tag (e.g., Environment: Production, Department: IT) to a Resource Group and observe how tags appear in Azure Cost Management for cost filtering and billing analysis.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Azure governance unit in [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* [ ] Watch the governance section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for resource lock creation and tag application.
* [ ] Proceed to the weekly hands-on lab activity.

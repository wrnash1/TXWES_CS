# Reading Guide: Module 02 - Azure Physical Architecture

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 02 - Azure Physical Architecture**! This module covers the geographic and logical building blocks of the Azure global infrastructure as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Understanding how Azure organizes its datacenters into regions, availability zones, and region pairs is essential for answering scenario questions about resilience, data residency, and resource organization.

You will learn how Azure regions are paired for disaster recovery, how Availability Zones protect against datacenter failure, and how Resource Groups and Azure Resource Manager provide the management layer above all Azure resources. Complete the checklist and glossary review before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Azure Regions**: A geographic area containing one or more datacenters that are networked together with a low-latency connection. Azure has 60+ regions worldwide. When deploying resources, you select a region to control where your data physically resides, which matters for compliance and latency.

* **Region Pairs**: Every Azure region is paired with another region at least 300 miles away within the same geopolitical boundary. During planned Azure maintenance, only one region in a pair is updated at a time, providing a fallback for disaster recovery. Example pairs: East US / West US, North Europe / West Europe.

* **Availability Zones**: Physically separate datacenters within a single Azure region, each with independent power, cooling, and networking. A region with Availability Zone support has a minimum of three zones. Deploying resources across multiple zones protects against single-datacenter failure while staying in the same region.

* **Resource Groups**: Logical containers that group Azure resources sharing the same lifecycle, permissions, and billing scope. A resource can belong to only one resource group at a time. Deleting a resource group deletes all resources it contains.

* **Azure Resource Manager (ARM)**: The deployment and management service for Azure. All interactions with Azure resources — via the portal, CLI, PowerShell, or REST API — go through ARM. ARM provides consistent access control, tagging, and template-based deployments. It is the layer that makes Infrastructure as Code possible in Azure.

---

### 2. Certification Exam Tips

* **Region vs. Availability Zone**: AZ-900 frequently tests the difference. A region is a geographic location; an Availability Zone is a separate datacenter within that region. Know that not all regions support Availability Zones — only designated regions offer them.
* **Region Pair Trap**: Do not confuse Region Pairs with Availability Zones. Region Pairs span separate geographic areas (hundreds of miles apart) for large-scale disaster recovery. Availability Zones are within the same region for datacenter-level isolation.
* **ARM as the Control Plane**: Every Azure resource interaction, regardless of tool (portal, CLI, Bicep, SDK), goes through ARM. AZ-900 may ask which service provides consistent management across all Azure resources — ARM is always the answer.
* **Resource Group Scope**: RBAC roles assigned at the Resource Group scope apply to all resources within that group. This is a common AZ-900 governance scenario question — know that role assignments inherit downward through the scope hierarchy.
* **Study Resource**: The Microsoft Learn module on Azure architecture fundamentals walks through regions, availability zones, and resource organization with interactive diagrams. Complete the "Describe Azure architecture and services" path at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn "Describe Azure architecture and services" learning path covers regions, availability zones, resource groups, and ARM with interactive knowledge checks. Start at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* **Required Video:** This free 3-hour course by freeCodeCamp covers Azure physical infrastructure including regions, zones, and ARM — watch the Azure Architecture section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Inspect Azure geography layout**: In the Azure portal, navigate to the region map and identify which regions support Availability Zones. Note a region pair for East US and explain the business continuity benefit.
* **Create a Resource Group in a specific region**: Using the Azure portal or Azure CLI (`az group create --name MyRG --location eastus`), create a resource group and observe how location affects data residency.
* **Review Resource Group lock configurations**: Apply a `CanNotDelete` lock to the resource group, attempt to delete it, and observe that ARM enforces the lock before any resource can be removed.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the "Describe core Azure architectural components" unit in [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* [ ] Watch the Azure Architecture section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for resource group creation and lock configuration.
* [ ] Proceed to the weekly hands-on lab activity.

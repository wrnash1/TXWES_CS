# Video Script: Module 02 - Azure Physical Architecture

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## [00:00 - 01:30] Opening and Learning Objectives

**[INSTRUCTOR ON CAMERA — title card: "Module 02: Azure Physical Architecture"]**

Welcome back. I'm Professor Nash, and this is Module 02. We are moving from the conceptual world of cloud computing into the physical world of Azure — the actual buildings, power systems, fiber networks, and geographic distribution that make Azure work at global scale.

Understanding Azure's physical architecture is not just trivia. It directly determines how you design for high availability, disaster recovery, data residency compliance, and latency. AZ-900 tests this domain heavily — roughly 35 to 40 percent of exam questions come from Azure Architecture and Services content.

By the end of this module you will be able to:

- Describe the hierarchy from Azure datacenters up through regions and geographies
- Explain Availability Zones and their role in protecting against datacenter failure
- Compare region pairs and their use in disaster recovery scenarios
- Define Azure Sovereign Regions and their purpose
- Describe the Azure management hierarchy: resources, resource groups, subscriptions, management groups

---

## [01:30 - 05:00] Azure Datacenters and Regions

**[SLIDE: "Azure Global Infrastructure"]**

Azure's physical foundation is a network of datacenters distributed across the world. As of 2024, Microsoft operates more than 300 physical datacenters across 60-plus regions — more than any other cloud provider.

Let me explain each layer of this geographic hierarchy.

**Datacenters** are the physical buildings. Each datacenter contains thousands of physical servers organized in racks, connected by high-speed networking, and powered by redundant electrical systems and cooling infrastructure. Microsoft does not publicly disclose the exact locations of individual datacenters for security reasons. What you interact with as an Azure customer is not a single datacenter — it is a region.

**[SLIDE: "Azure Regions"]**

An Azure **region** is a geographic area that contains one or more datacenters that are networked together with a low-latency connection, typically less than 2 milliseconds round-trip. When you deploy an Azure Virtual Machine to "East US," you are deploying to one of the datacenters within the East US region boundary, which spans the northern Virginia area.

Why does the region boundary matter? Because Azure makes its SLA guarantees at the region level for many services. The redundancy within a region — across multiple datacenters — is what allows Azure to promise 99.99 percent uptime for services deployed with Availability Zones.

**[SHOW PORTAL — Navigate to portal.azure.com, select any service creation blade and show the Region dropdown]**

Here in the Azure Portal, when you create virtually any resource — a virtual machine, a storage account, a database — the first decision you make is which region to deploy to. You can see the full list of available regions in this dropdown. Notice that regions are grouped by geography: US, Europe, Asia Pacific, and so on.

**[SLIDE: "Region Selection Considerations"]**

Choosing the right region is a four-factor decision that AZ-900 expects you to understand:

First, **latency** — deploy close to your users to minimize network round-trip time. If your users are in Dallas, East US 2 or South Central US will give lower latency than West Europe.

Second, **data residency and compliance** — many regulations (GDPR in Europe, data sovereignty laws in various countries) require that specific types of data remain within defined geographic boundaries. You must select a region in the compliant geography.

Third, **service availability** — not all Azure services are available in all regions. Newer or specialized services often roll out to larger regions first. The Azure Products by Region page at learn.microsoft.com lets you verify service availability by region.

Fourth, **pricing** — Azure pricing varies by region. The same VM size can cost 10-20 percent more in some regions than others, reflecting differences in real estate, power, and labor costs.

---

## [05:00 - 09:00] Availability Zones

**[SLIDE: "Availability Zones — Datacenter-Level Fault Isolation"]**

This is one of the most tested concepts in the Azure Physical Architecture domain. If you deploy a critical workload to a single datacenter and that datacenter experiences a power failure, your application goes down. Availability Zones solve this by distributing your deployment across multiple physically separate datacenters within the same region.

An **Availability Zone** is a physically separate datacenter within an Azure region. Each zone has its own power supply, cooling system, and network infrastructure. Zones within a region are connected by high-speed private fiber links with latency under 2 milliseconds.

Each Azure region that supports Availability Zones has a minimum of three zones, labeled Zone 1, Zone 2, and Zone 3. These numbers are logical — the actual physical datacenter assigned to Zone 1 in the East US region for your subscription may differ from Zone 1 in another subscription, because Microsoft uses zone-mapping to distribute load evenly.

**[SLIDE: "How Availability Zones Raise Your SLA"]**

When you deploy an Azure Virtual Machine to a single zone with no redundancy, the SLA is 99.9 percent. When you deploy two or more VM instances to separate Availability Zones, the SLA increases to 99.99 percent. That difference is roughly 8.5 hours of additional permitted uptime per year.

The tradeoff: deploying across Availability Zones requires designing your application to tolerate a zone failure and redistribute traffic automatically. Azure Load Balancer and Azure Application Gateway both support zone-redundant configurations.

**[SLIDE: "Zone-Redundant vs. Zonal Services"]**

Azure services interact with Availability Zones in two ways:

**Zonal services** let you pin a specific resource to a specific zone. Azure Virtual Machines, Azure Managed Disks, and Azure Standard IP Addresses are zonal services. You explicitly choose Zone 1, Zone 2, or Zone 3 when you deploy.

**Zone-redundant services** automatically replicate data and serve traffic across all zones in a region without you specifying a zone. Azure Storage (Zone-Redundant Storage tier), Azure SQL Database, and Azure Service Bus are examples. With these services, the zone distribution is handled by the service itself.

Not every Azure region has Availability Zones. Regions without zones are typically smaller or newer. Verify zone support for your target region using the Azure documentation at learn.microsoft.com before designing a zone-dependent architecture.

---

## [09:00 - 13:00] Region Pairs and Geographies

**[SLIDE: "Region Pairs"]**

While Availability Zones protect against datacenter failures within a region, what protects you against an entire region becoming unavailable? The answer is **region pairs**.

Microsoft pairs most Azure regions with another region in the same geography, at least 300 miles away. Examples include:

- East US paired with West US
- North Europe paired with West Europe
- East Asia paired with Southeast Asia

Region pairs provide several guarantees. If a planned Azure maintenance update causes an outage, Microsoft staggers the update — the two regions in a pair are never updated simultaneously. If a major outage affects one region in a pair, Microsoft prioritizes recovery of the other region. For Azure Storage with geo-redundant replication enabled, data is automatically replicated to the paired region.

**[SLIDE: "Azure Geographies"]**

Above the region level, Azure organizes the world into **geographies** — large areas that typically correspond to political or legal jurisdictions. Each geography contains at least one Azure region, and data residency, compliance, and sovereignty requirements are usually scoped to a geography.

The major Azure geographies include the Americas, Europe, Asia Pacific, Middle East, and Africa.

**[SLIDE: "Azure Sovereign Regions"]**

Some Azure workloads require complete isolation from the public Azure infrastructure due to government security requirements. For these use cases, Microsoft operates **Azure Sovereign Regions**.

**Azure Government** (US) is operated by screened US citizens and is available only to US federal, state, local, tribal governments and their partners. It meets requirements for FedRAMP High, DoD IL2/4/5, and other US government compliance frameworks.

**Azure China** is operated by 21Vianet under a unique licensing arrangement with Microsoft. It is legally required for serving customers in mainland China and operates under Chinese regulations.

On AZ-900, you should be able to identify that sovereign regions exist and what purpose they serve.

---

## [13:00 - 17:00] Azure Management Hierarchy

**[SLIDE: "Azure Organizational Hierarchy"]**

We have covered the physical geography. Now let's look at the logical management structure that overlays it. Understanding this hierarchy is critical for Module 10 (RBAC and Subscriptions) and Module 12 (Governance), but you need the foundation now.

Azure's management hierarchy has four levels, from bottom to top:

**Resources** are the individual Azure services you create — a virtual machine, a storage account, a virtual network, a database. Every resource belongs to exactly one resource group.

**Resource Groups** are logical containers for related resources. You might put all the resources for a web application — its virtual machine, its database, its storage account, and its virtual network — into a single resource group. Resource groups enable lifecycle management: you can deploy, update, or delete all resources in a group together. Every resource belongs to exactly one resource group, and resource groups cannot be nested.

**Subscriptions** contain resource groups. A subscription is a billing and access boundary. Every Azure deployment requires a subscription, and all costs within a subscription are billed together. Organizations often create multiple subscriptions to separate environments (development vs. production), departments, or compliance boundaries.

**Management Groups** sit at the top of the hierarchy and contain subscriptions. A management group lets you apply policies and access controls to multiple subscriptions simultaneously. A large organization might have a root management group with child management groups for each business division, each containing multiple subscriptions.

**[SHOW PORTAL — Navigate to Management Groups in the Azure Portal]**

Here in the Azure Portal you can see the management group hierarchy. Notice that every subscription eventually rolls up to the Tenant Root Group, which corresponds to your Microsoft Entra ID tenant. This root is the single point from which all Azure management policies can be applied organization-wide.

**[SLIDE: "Hierarchy Summary"]**

To summarize the hierarchy for AZ-900:

- Management Groups contain Subscriptions
- Subscriptions contain Resource Groups
- Resource Groups contain Resources

Policies and access control applied at a higher level cascade down to all lower levels.

---

## [17:00 - 20:30] Lab Preview and Exam Alignment

**[SLIDE: "Key AZ-900 Exam Points for Module 02"]**

Let me highlight the most frequently tested items from this module.

Availability Zones are physically separate datacenters within a single region — not separate regions. If an exam question asks about protecting against a regional failure, the answer involves region pairs or geo-redundant storage, not Availability Zones.

Region pairs are used for disaster recovery and planned maintenance staggering — not for latency optimization. Deploying to a paired region hundreds of miles away increases latency, not reduces it.

Resource Groups are logical containers with no physical significance. Distributing resources across multiple resource groups does not protect against availability events.

The management hierarchy direction: Management Groups are at the top, resources are at the bottom. Policies flow downward.

**[SHOW CODE — Azure CLI listing regions]**

Here is the command to list all available Azure regions from the CLI:

```bash
az account list-locations --output table
```

This returns the full list of Azure regions with their display names. You will use this in the lab to verify region availability for specific services.

---

## [20:30 - 22:00] Closing

**[INSTRUCTOR ON CAMERA]**

You now have a complete mental map of Azure's physical infrastructure — from individual datacenters up through regions, Availability Zones, region pairs, and the management hierarchy of resources, resource groups, subscriptions, and management groups.

This mental map is the spatial context for every Azure service you will learn in Modules 03 through 15. When we deploy a virtual machine in Module 03, you will know exactly what region and availability zone you are choosing, what subscription it belongs to, and how its SLA relates to the zone configuration you select.

In Module 03, we deploy our first Azure Virtual Machines and explore Scale Sets for elastic compute. Bring your Azure Student subscription — we start running real commands.

Complete the reading guide, do the lab, and take the quiz. I will see you in Module 03.

---

**References:**

- learn.microsoft.com/en-us/azure/availability-zones/az-overview
- learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources
- learn.microsoft.com/en-us/azure/reliability/cross-region-replication-azure

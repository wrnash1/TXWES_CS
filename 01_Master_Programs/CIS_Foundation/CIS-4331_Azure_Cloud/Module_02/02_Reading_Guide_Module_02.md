# Reading Guide: Module 02 - Azure Physical Architecture

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4331 &BULL; MICROSOFT AZURE CLOUD ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## Introduction

Module 02 moves from cloud concepts to Azure's concrete physical and organizational infrastructure. Every high-availability design, every disaster recovery plan, every compliance conversation about data residency starts with a precise understanding of where Azure resources physically exist and how Microsoft's management hierarchy organizes them. The AZ-900 "Describe Azure Architecture and Services" domain carries 35-40 percent of exam weight, making this module one of the most impactful for your certification preparation.

---

## Section 1: Azure Datacenters

### 1.1 Physical Foundation

Azure's infrastructure is built on a global network of physical datacenters. Each datacenter is a purpose-built facility containing thousands of physical servers in standardized racks, connected by high-speed intra-datacenter networking. Datacenters include redundant power feeds (utility plus diesel generator backup), uninterruptible power supplies (UPS), precision air conditioning systems, and physical security measures including perimeter fencing, biometric access, and continuous surveillance.

Microsoft does not publicly disclose the exact street addresses of individual datacenters for security reasons. From the customer's perspective, the operational unit is not a datacenter but a region.

### 1.2 How Datacenters Scale

Microsoft estimates it has deployed more than 300 datacenters in over 60 regions worldwide as of 2024. This scale enables the redundancy that underlies Azure's SLA commitments. A single region may contain multiple datacenters, and those datacenters are the physical substrate for Availability Zones.

---

## Section 2: Azure Regions

### 2.1 Region Definition

An Azure **region** is a geographic area containing one or more datacenters networked together with low-latency connections (typically under 2 milliseconds round-trip between datacenters within the same region). Regions are the primary geographic unit Azure customers work with when deploying resources.

When you create a Virtual Machine in East US, you are placing that VM in one of the physical datacenters in the East US region. The specific datacenter is determined by Azure's scheduler — you select the region, not the individual datacenter.

### 2.2 Region Examples by Geography

| Geography | Region Name | Location |
|---|---|---|
| Americas | East US | Northern Virginia |
| Americas | West US 3 | Phoenix, Arizona |
| Americas | South Central US | San Antonio, Texas |
| Americas | Canada Central | Toronto |
| Americas | Brazil South | Sao Paulo |
| Europe | North Europe | Ireland |
| Europe | West Europe | Netherlands |
| Europe | UK South | London |
| Europe | Germany West Central | Frankfurt |
| Asia Pacific | East Asia | Hong Kong |
| Asia Pacific | Southeast Asia | Singapore |
| Asia Pacific | Australia East | New South Wales |
| Asia Pacific | Japan East | Tokyo |
| Middle East | UAE North | Dubai |

### 2.3 Region Selection Criteria

Selecting the appropriate region requires balancing four considerations:

**Latency:** Deploying resources in the region closest to your end users minimizes network round-trip time. For example, a Texas-based university should prefer South Central US over West Europe for student-facing applications.

**Data Residency and Compliance:** Regulations such as GDPR (European Union), data localization laws (Russia, China, India), and industry-specific compliance requirements (HIPAA, FedRAMP) may legally mandate that certain data types remain within specific geographic boundaries. Selecting the correct region ensures compliance.

**Service Availability:** Not all Azure services are available in all regions. Preview services and newer releases typically launch in large regions first (East US, West Europe, Southeast Asia) before expanding globally. The Azure Products by Region reference page at learn.microsoft.com/en-us/azure/availability-zones/az-products-by-region allows verification of service availability by region before architecture decisions are finalized.

**Pricing:** Azure pricing varies by region. Differences reflect local infrastructure costs including real estate, power rates, and operational labor. The same Standard D2s v3 VM can cost 10-20 percent more in some regions than others. The Azure Pricing Calculator allows region-by-region cost comparison.

---

## Section 3: Availability Zones

### 3.1 Definition and Purpose

An **Availability Zone** is a physically separate datacenter within an Azure region. Each Availability Zone has:

- Independent power supply (separate electrical grid feeds)
- Independent cooling infrastructure
- Independent network connectivity

Availability Zones within a region are connected by high-speed, low-latency private fiber links (under 2 milliseconds round-trip). This low latency allows synchronous data replication and load balancing across zones.

The purpose of Availability Zones is to protect applications from datacenter-level failures. If a power event takes down the datacenter hosting Zone 1, resources deployed to Zone 2 and Zone 3 continue operating. An application designed for zone redundancy survives a datacenter failure without downtime.

### 3.2 Zone Count and Naming

Each Availability Zone-enabled region contains a minimum of three zones. Zones are identified as Zone 1, Zone 2, and Zone 3, but these labels are logical, not fixed physical addresses. Microsoft's zone mapping assigns physical datacenters to logical zone numbers differently across subscriptions to distribute load evenly across the physical infrastructure. This means your Zone 1 is not necessarily the same physical building as another customer's Zone 1.

### 3.3 SLA Impact of Availability Zones

| Deployment Configuration | Azure VM SLA |
|---|---|
| Single VM (no zone, no availability set) | 99.9% |
| Single VM on Premium SSD storage | 99.9% |
| Two or more VMs in Availability Set | 99.95% |
| Two or more VMs in separate Availability Zones | 99.99% |

The difference between 99.9% and 99.99% is significant in production environments:

- 99.9% = 8 hours 41 minutes maximum downtime per year
- 99.99% = 52 minutes 35 seconds maximum downtime per year

### 3.4 Zonal vs. Zone-Redundant Service Types

| Service Type | Description | Examples |
|---|---|---|
| Zonal | Deployed to a specific zone; customer chooses zone | Azure VMs, Managed Disks, Standard IP addresses |
| Zone-redundant | Automatically distributed across all zones | Azure Storage (ZRS), Azure SQL Database, Azure Service Bus Premium |
| Non-regional | Global service, no zone/region concept | Microsoft Entra ID, Azure DNS, Azure Traffic Manager |

### 3.5 Availability Sets vs. Availability Zones

AZ-900 sometimes presents both Availability Sets and Availability Zones. Know the distinction:

**Availability Sets** are older technology (pre-Availability Zones). They distribute VMs across fault domains (separate physical racks) and update domains (separate maintenance windows) within a single datacenter. They protect against rack-level hardware failures and planned maintenance, but not against datacenter-level failures.

**Availability Zones** are newer and provide stronger isolation — an entire datacenter can fail and zone-distributed resources remain available. Microsoft recommends Availability Zones over Availability Sets for new deployments in zone-supported regions.

---

## Section 4: Region Pairs

### 4.1 Definition

Azure **region pairs** are two Azure regions in the same geography that Microsoft has designated as partners for disaster recovery purposes. The regions in a pair are at least 300 miles apart to ensure that regional disasters (large hurricanes, major earthquakes, widespread power outages) do not affect both regions simultaneously.

### 4.2 Region Pair Examples

| Region | Paired Region | Geography |
|---|---|---|
| East US | West US | Americas |
| East US 2 | Central US | Americas |
| North Europe | West Europe | Europe |
| UK South | UK West | Europe |
| East Asia | Southeast Asia | Asia Pacific |
| Australia East | Australia Southeast | Asia Pacific |
| Brazil South | South Central US | Americas (cross-geography) |
| Germany West Central | Germany North | Europe |

Note: Brazil South's pair is South Central US (in the Americas geography) because there is currently only one other Brazil region. This cross-geography pairing is an exception to the same-geography rule.

### 4.3 Region Pair Benefits

**Planned maintenance staggering:** Microsoft never applies planned updates to both regions in a pair simultaneously. If the update causes an unexpected outage, the paired region is unaffected and can handle traffic failover.

**Data residency:** With geo-redundant storage, Azure automatically replicates data to the paired region. Both regions are in the same geography, preserving data residency requirements.

**Recovery prioritization:** If a major outage affects multiple regions simultaneously, Microsoft prioritizes restoring at least one region in each pair.

**Geo-redundant storage replication:** Azure Storage with Geo-Redundant Storage (GRS) or Geo-Zone-Redundant Storage (GZRS) replicates data to the paired region asynchronously.

---

## Section 5: Azure Geographies

### 5.1 Definition

An Azure **geography** is a discrete market, typically a country or group of countries, that preserves data residency and compliance boundaries. Each geography contains two or more Azure regions (except very small geographies that may have one with a paired region in a nearby geography).

Geographies ensure that:

- Data remains within the geography unless explicitly configured otherwise
- Compliance certification applies to all regions within the geography
- Region pairs stay within the geography (with limited exceptions like Brazil South)

### 5.2 Geography Examples

| Geography | Included Regions (examples) |
|---|---|
| United States | East US, East US 2, West US, West US 2, West US 3, Central US, North Central US, South Central US, West Central US |
| Europe | North Europe, West Europe, UK South, UK West, France Central, Germany West Central, Switzerland North |
| Asia Pacific | East Asia, Southeast Asia, Japan East, Japan West, Australia East, Korea Central |
| Middle East | UAE North, UAE Central, Qatar Central |
| Africa | South Africa North, South Africa West |

---

## Section 6: Azure Sovereign Regions

### 6.1 Purpose

Sovereign regions are physically and logically isolated Azure instances designed for governments and regulated industries that require complete separation from commercial Azure infrastructure.

### 6.2 Azure Government

Azure Government is a separate Azure cloud instance operated by Microsoft for US government entities. It serves federal, state, local, and tribal governments and their contractors.

Key characteristics:

- Operated by screened US citizens (US persons only policy)
- Physically separate datacenters from commercial Azure
- Separate portal: portal.azure.us
- Compliance certifications: FedRAMP High, DoD Impact Levels 2, 4, 5, ITAR, IRS 1075, CJIS

### 6.3 Azure China

Azure China is operated by 21Vianet, a Chinese internet services company, under a license from Microsoft. It is legally required for organizations serving customers in mainland China under Chinese internet regulations.

Key characteristics:

- Operated by 21Vianet (not Microsoft directly)
- Located entirely within mainland China
- Separate portal: portal.azure.cn
- Subject to Chinese data sovereignty laws

---

## Section 7: Azure Management Hierarchy

### 7.1 The Four-Level Hierarchy

Azure organizes management and billing through a four-level hierarchy:

#### Level 4 (Top): Management Groups

Management groups are containers for subscriptions. An Azure tenant can have up to 10,000 management groups, with a maximum of six levels of depth (not counting root and subscription levels). Every tenant has one root management group. Policies and role assignments applied to a management group cascade to all subscriptions beneath it.

Use case: A large enterprise creates management groups for each business division. Security policies required across the entire company are applied at the root management group level and automatically apply to all divisions.

#### Level 3: Subscriptions

A subscription is both an access boundary and a billing unit. All Azure resources deployed within a subscription are billed to that subscription. A subscription is associated with a single Azure Entra ID tenant.

Common subscription patterns:

- One subscription per environment (dev, staging, prod)
- One subscription per department or business unit
- One subscription per regulatory compliance boundary

#### Level 2: Resource Groups

A resource group is a logical container for Azure resources. Every resource must belong to exactly one resource group. Resource groups enable:

- Unified lifecycle management (deploy, update, delete all resources in a group together)
- Role-based access control scoping (grant a user access to all resources in a group)
- Cost reporting by resource group
- Tagging and policy enforcement at the group level

Resource groups cannot be nested. A resource group cannot contain another resource group.

#### Level 1 (Bottom): Resources

Individual Azure services — virtual machines, storage accounts, databases, virtual networks — are resources. Each resource belongs to exactly one resource group in exactly one subscription.

### 7.2 Hierarchy Visualization

```text
Tenant Root Group (Management Group)
  └── Corp Management Group
        ├── Production Subscription
        │     ├── WebApp-Prod-RG (Resource Group)
        │     │     ├── webvm01 (Virtual Machine)
        │     │     ├── webvm02 (Virtual Machine)
        │     │     └── webapp-vnet (Virtual Network)
        │     └── Database-Prod-RG (Resource Group)
        │           └── sql-prod-01 (SQL Database)
        └── Development Subscription
              └── WebApp-Dev-RG (Resource Group)
                    └── webvm-dev (Virtual Machine)
```

### 7.3 Policy and Access Inheritance

Access control and policy settings cascade from parent to child in the hierarchy:

- A policy applied at a Management Group affects all subscriptions, resource groups, and resources under it
- A role assignment at a Subscription level affects all resource groups and resources in that subscription
- A role assignment at a Resource Group level affects only the resources in that group
- Settings at a lower level can be more restrictive but cannot override deny policies from above

---

## Section 8: Azure CLI Commands for Architecture Exploration

```bash
# List all available Azure regions
az account list-locations --output table

# List regions with Availability Zone support
az account list-locations --query "[?availabilityZoneMappings != null].{Name:name, DisplayName:displayName}" --output table

# Show the current subscription details
az account show --output json

# List all resource groups in the current subscription
az group list --output table

# Create a new resource group
az group create --name MyResourceGroup --location eastus

# Show details of a specific resource group
az group show --name MyResourceGroup

# List all resources in a resource group
az resource list --resource-group MyResourceGroup --output table
```

Reference: learn.microsoft.com/en-us/cli/azure/account

---

## Section 9: AZ-900 Exam Tips

1. **Availability Zones vs. Region Pairs:** Availability Zones protect against datacenter failure within a single region. Region pairs protect against regional failure. If a scenario says "protect against a single datacenter going down," the answer involves Availability Zones. If the scenario says "protect against an entire region going offline," the answer involves region pairs.

2. **Minimum zone count:** Azure regions that support Availability Zones have a minimum of three zones. Do not be misled by answers suggesting two zones — the minimum is always three.

3. **Resource Group rules:** Resource groups cannot be nested. A resource can only belong to one resource group. Deleting a resource group deletes all resources in it.

4. **Management Group depth:** The maximum depth for management groups is six levels beneath the root. The root management group itself counts as level zero. This specificity occasionally appears on the exam.

5. **Sovereign region access:** Azure Government is not accessible to everyone — it requires eligibility verification as a US government entity or contractor. The Azure China portal is also separate from the commercial portal. Do not confuse sovereign regions with standard regions.

6. **Region pair direction:** Data replication in geo-redundant storage goes to the paired region. If your primary region is East US, your paired region is West US. Failover goes to the pair. Know at least two common region pairs for the exam.

7. **Subscription as billing boundary:** All costs within a subscription are billed together. Cost separation between departments or environments is typically achieved through separate subscriptions, not separate resource groups (though resource groups can be used for cost reporting within a subscription).

8. **Not all regions have Availability Zones:** Smaller or newer regions may not have zone support. Always verify before designing a zone-dependent architecture. The AZ-900 exam may test awareness that zone support is not universal.

---

## Section 10: Required Resources

- Azure regions and Availability Zones overview: learn.microsoft.com/en-us/azure/availability-zones/az-overview
- Cross-region replication (region pairs): learn.microsoft.com/en-us/azure/reliability/cross-region-replication-azure
- Azure management hierarchy: learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-setup-guide/organize-resources
- Azure Government overview: learn.microsoft.com/en-us/azure/azure-government/documentation-government-welcome
- Microsoft Learn AZ-900 path (Architecture module): learn.microsoft.com/en-us/training/modules/azure-architecture-fundamentals/

---

## Section 11: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the Availability Zones SLA table (Section 3.3)
- [ ] Review the region pairs table and know at least 4 pairs by memory
- [ ] Complete the Microsoft Learn "Azure architecture fundamentals" module
- [ ] Practice listing Azure regions using the CLI command in Section 8
- [ ] Draw the management hierarchy diagram from memory
- [ ] Understand the difference between Availability Sets and Availability Zones (Section 3.5)
- [ ] Complete Lab Activity Module 02
- [ ] Take Quiz Module 02
- [ ] Post Discussion Module 02 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft Learn — Azure regions and Availability Zones**
https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview
Comprehensive overview of Availability Zones architecture, zone-enabled services, and the SLA improvements achieved by zone-redundant deployments. Includes interactive diagrams of the zone topology.

**2. Microsoft Learn — Cross-region replication in Azure**
https://learn.microsoft.com/en-us/azure/reliability/cross-region-replication-azure
Full list of Azure region pairs, explanation of why region pairs exist, and the benefits they provide for planned maintenance, geo-redundant storage, and disaster recovery prioritization.

**3. Microsoft Learn — Organize and manage multiple Azure subscriptions**
https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/organize-subscriptions
Cloud Adoption Framework guidance on designing subscription and management group hierarchies for enterprise environments, with decision trees for subscription design patterns.

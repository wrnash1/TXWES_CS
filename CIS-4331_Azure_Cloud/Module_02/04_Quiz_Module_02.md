# Quiz: Module 02 - Azure Physical Architecture

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

What is the minimum number of Availability Zones in an Azure region that supports Availability Zones?

- A) One
- B) Two
- C) Three
- D) Five

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure regions that support Availability Zones contain a minimum of three physically separate datacenters, each designated as a zone. Microsoft requires at least three zones to ensure that an application can remain available if one zone fails while still maintaining quorum for distributed workloads.
- *Why A is incorrect:* A single zone provides no redundancy — there would be nothing to fail over to. A region with one zone cannot provide zone-redundant SLAs.
- *Why B is incorrect:* Two zones are insufficient for certain quorum-based distributed systems (such as distributed databases) that require a majority vote. Microsoft's architecture mandates three.
- *Why D is incorrect:* While some regions may eventually have more than three zones, the minimum guarantee — and the number used in AZ-900 exam context — is three.

---

## Question 2

A company requires that its application survive the complete failure of one Azure datacenter without any downtime. The application is deployed in East US. Which deployment approach achieves this?

- A) Deploy all VMs to a single resource group in East US
- B) Deploy VMs across multiple Availability Zones in East US
- C) Deploy VMs to both East US and West US using Azure Paired Regions
- D) Deploy VMs within an Azure Availability Set in East US

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Availability Zones are physically separate datacenters within the same region, each with independent power and cooling. Deploying across multiple zones means one datacenter can fail completely and VMs in the other zones remain available.
- *Why A is incorrect:* Resource groups are logical containers with no physical fault isolation. All VMs in a single resource group could be in the same physical datacenter.
- *Why C is incorrect:* Deploying to a paired region would survive a regional failure, but the scenario asks about a single datacenter failure within East US — Availability Zones address this more precisely without the latency penalty of cross-region deployment.
- *Why D is incorrect:* Availability Sets distribute VMs across fault domains (racks) and update domains within a single datacenter. They do not protect against a complete datacenter failure. Availability Zones provide stronger isolation.

---

## Question 3

Which Azure management hierarchy level serves as both a billing boundary and an access control boundary?

- A) Management Group
- B) Subscription
- C) Resource Group
- D) Resource

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A subscription is the unit at which Azure billing is consolidated — all resource costs within a subscription appear on a single invoice. It is also an access boundary — Entra ID tenant association and subscription-level role assignments are defined here.
- *Why A is incorrect:* Management groups are governance containers for multiple subscriptions. They do not generate separate bills — billing is still at the subscription level.
- *Why C is incorrect:* Resource groups are logical containers for resources within a subscription. They can be used for cost reporting and access scoping, but the billing boundary is the subscription.
- *Why D is incorrect:* Individual resources are not billing boundaries — they are line items within a subscription's bill.

---

## Question 4

Microsoft guarantees that when applying planned maintenance updates to Azure infrastructure, the two regions in a region pair are never updated simultaneously. Which additional benefit do region pairs provide for Azure Storage?

- A) Automatic data replication to the paired region
- B) Reduced storage pricing for data stored in paired regions
- C) Automatic geo-distribution of CDN content to paired regions
- D) Elimination of the need for backup snapshots

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Azure Storage with Geo-Redundant Storage (GRS) or Geo-Zone-Redundant Storage (GZRS) automatically replicates data to the paired region asynchronously. Region pairs define the replication destination for geo-redundant storage tiers.
- *Why B is incorrect:* Region pairs do not provide pricing discounts for storage. Pricing is determined by region, storage tier, and redundancy level — not by the pair relationship.
- *Why C is incorrect:* Azure CDN uses its own edge network distribution, which is independent of region pairs. CDN pop locations are not constrained to paired regions.
- *Why D is incorrect:* Geo-redundant replication does not eliminate the need for backups. Replication copies all data changes including accidental deletions — it is not a substitute for point-in-time backup.

---

## Question 5

An organization needs to apply a security policy that enforces multi-factor authentication across 15 Azure subscriptions spanning three business divisions. What is the most efficient way to apply this policy?

- A) Configure the policy manually in each of the 15 subscriptions
- B) Apply the policy at the root Management Group level
- C) Apply the policy to each Resource Group within every subscription
- D) Configure the policy on each individual resource

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Policies applied at a Management Group cascade to all subscriptions, resource groups, and resources beneath it. Applying the policy at the root Management Group affects all 15 subscriptions simultaneously with a single configuration.
- *Why A is incorrect:* Configuring the policy in 15 separate subscriptions is operationally expensive and creates a maintenance burden — any future policy change must be made in all 15 locations.
- *Why C is incorrect:* Applying policies at the resource group level requires configuration in every resource group across all subscriptions — even more work than option A, and still not a single management point.
- *Why D is incorrect:* Individual resource-level policy configuration is the most granular and most labor-intensive option. It is never appropriate for organization-wide policy enforcement.

---

## Question 6

Which Azure feature specifically addresses the requirement to protect workloads against the failure of an entire Azure region, rather than a single datacenter?

- A) Availability Zones
- B) Availability Sets
- C) Region Pairs with geo-redundant replication
- D) Resource Group tagging

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Region pairs separate two regions by at least 300 miles, ensuring that regional disasters do not affect both regions simultaneously. Geo-redundant storage and cross-region service replication use region pairs to provide regional-failure protection.
- *Why A is incorrect:* Availability Zones protect against a single datacenter failure within a region. They do not protect against an entire region going offline — all zones within a region could be affected by a regional event such as a major regional network outage.
- *Why B is incorrect:* Availability Sets protect against rack-level hardware failures and planned maintenance events within a single datacenter. They provide weaker isolation than Availability Zones and offer no regional protection.
- *Why D is incorrect:* Resource Group tagging is a metadata and cost management feature with no relationship to fault tolerance or geographic distribution.

---

## Question 7

Azure Government is a sovereign region designed for a specific customer segment. Which of the following organizations is eligible to use Azure Government?

- A) Any organization headquartered in the United States
- B) US federal, state, local, and tribal governments and their authorized contractors
- C) Any organization that processes US citizen personal data
- D) International organizations with US operations

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Government is restricted to US government entities — federal, state, local, and tribal — and their authorized contractors and partners. Eligibility requires verification of government affiliation. The environment is operated by screened US citizens only.
- *Why A is incorrect:* US headquarters does not qualify an organization for Azure Government access. Many US-headquartered commercial companies use standard commercial Azure, not Azure Government.
- *Why C is incorrect:* Processing US citizen data does not qualify for Azure Government. Commercial Azure with appropriate compliance configurations (HIPAA, SOC 2, etc.) is used for US citizen data in non-government contexts.
- *Why D is incorrect:* International organizations with US operations do not qualify. Azure Government is specifically for US government entities and their direct contractors — not general international businesses.

---

## Question 8

A resource group in Azure is being deleted. Which of the following accurately describes what happens?

- A) Only empty resource groups can be deleted; resources must be removed manually first
- B) The resource group is deleted but all resources within it are moved to the default resource group
- C) All resources contained in the resource group are deleted along with the group
- D) Resources in the group are retained but the group container is removed

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Deleting a resource group is a destructive action that deletes all resources contained within it simultaneously. This is intentional — resource groups are designed to represent the lifecycle of a set of resources together, so deleting the group deletes the entire workload.
- *Why A is incorrect:* Azure does not require a resource group to be empty before deletion. The Portal and CLI both warn users that all resources will be deleted and require confirmation, but the group does not need to be manually emptied first.
- *Why B is incorrect:* Azure does not have a "default resource group." Resources cannot be orphaned — they must belong to a resource group. Deleting a group does not move resources elsewhere.
- *Why D is incorrect:* The resource group container and its contents are inseparable in this operation. Resources do not persist after their parent resource group is deleted.

---

## Question 9

An Azure region is described as a "geographic area containing one or more datacenters connected with low-latency networking." What latency threshold is typically used to describe the connection between datacenters within the same region?

- A) Less than 1 millisecond
- B) Less than 2 milliseconds
- C) Less than 10 milliseconds
- D) Less than 100 milliseconds

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Microsoft's architecture documentation and the AZ-900 learning materials consistently describe the connection between datacenters within the same region (and between Availability Zones) as having a round-trip latency of under 2 milliseconds. This low latency enables synchronous data replication across zones.
- *Why A is incorrect:* Sub-millisecond latency describes intra-datacenter (same building) connections, not inter-datacenter connections across a metropolitan area.
- *Why C is incorrect:* 10 milliseconds is the typical latency budget for a metropolitan area network or connections within the same country/continent. It is too high to be the Azure intra-region standard.
- *Why D is incorrect:* 100 milliseconds describes typical latency between regions or continents — far too high for the synchronous replication that Availability Zone architecture requires.

---

## Question 10

Which of the following correctly describes the relationship between Resource Groups and subscriptions in Azure?

- A) A resource group can span multiple subscriptions
- B) A subscription can contain multiple resource groups, but a resource group belongs to exactly one subscription
- C) Each subscription can contain only one resource group
- D) Resource groups and subscriptions are the same concept with different names

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A subscription contains resource groups (one to many), and each resource group belongs to exactly one subscription. Resources within a group inherit the subscription context. This is the correct one-to-many relationship between subscriptions and resource groups.
- *Why A is incorrect:* Resource groups cannot span subscriptions. Each resource group exists entirely within one subscription. Cross-subscription resource sharing requires explicit peering or linking, not a shared resource group.
- *Why C is incorrect:* A subscription can contain an unlimited number of resource groups (subject to subscription quotas). Most organizations create many resource groups per subscription to organize workloads, environments, and teams.
- *Why D is incorrect:* Resource groups and subscriptions are distinct hierarchy levels with different purposes. Subscriptions handle billing and top-level access control; resource groups handle lifecycle and operational grouping of related resources.

---

### Question 11 (5 points)

An organization deploys all of its virtual machines without any explicit availability configuration in East US. Azure silently places VMs on whichever physical host has capacity. A rack-level power failure takes down one physical rack. Which Azure feature, if the team had used it, would have protected against this specific failure?

- A) Azure Availability Zones
- B) Azure Availability Sets
- C) Azure Region Pairs
- D) Azure Resource Locks

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Availability Sets distribute VMs across fault domains (separate physical racks with independent power) and update domains. A rack-level power failure affects one fault domain; VMs in other fault domains remain operational. Availability Sets were specifically designed for rack-level hardware failure protection within a single datacenter.
  - *Why A is incorrect:* Availability Zones protect against entire datacenter failures, not rack-level failures. They are a stronger (and more expensive) option, but the specific failure described — a single rack losing power — is exactly what fault domains in an Availability Set address.
  - *Why C is incorrect:* Region Pairs protect against entire regional failures. A rack-level outage is far below the regional failure scale that region pairs address.
  - *Why D is incorrect:* Resource Locks prevent accidental deletion or modification of Azure resources. They have no relationship to physical fault tolerance or hardware failure protection.

---

### Question 12 (5 points)

Which statement accurately describes how Azure assigns physical datacenters to Availability Zone numbers (Zone 1, Zone 2, Zone 3) across different subscriptions?

- A) All Azure customers in a region see the same physical datacenter as Zone 1
- B) Zone numbers are randomly shuffled each time a subscription is created and may not map to the same physical datacenter across subscriptions
- C) Zone numbering is fixed globally — Zone 1 always maps to the oldest datacenter in the region
- D) Zones are only assigned when a resource is deployed; empty subscriptions have no zone mapping

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Microsoft maps physical datacenters to logical zone numbers differently across subscriptions to distribute load evenly across physical infrastructure. Your Zone 1 may be a different physical building than another customer's Zone 1 in the same region. This is intentional load balancing across Azure's physical footprint.
  - *Why A is incorrect:* Zone numbers are not consistent across subscriptions. Two different Azure customers both deploying to "East US Zone 1" may be using different physical buildings.
  - *Why C is incorrect:* Zone numbering is not based on datacenter age or any fixed global mapping. The per-subscription randomization is the documented Microsoft behavior.
  - *Why D is incorrect:* Zone mappings are assigned at the subscription level when the subscription is created and registered in a region, not at resource deployment time.

---

### Question 13 (5 points)

A company wants to move its primary business application from East US to West Europe for latency reasons. The application uses Azure Storage with GRS redundancy. When the storage account is in East US, data is automatically replicated to which secondary region?

- A) East US 2
- B) West US
- C) North Europe
- D) West Europe

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The Azure region pair for East US is West US. GRS replicates data to the paired region, which for East US is West US. This is one of the foundational region pair facts tested on AZ-900.
  - *Why A is incorrect:* East US 2 is paired with Central US, not East US. East US and East US 2 are separate regions with separate pairs.
  - *Why C is incorrect:* North Europe is paired with West Europe. They are both European regions. East US is in the Americas geography and pairs within that geography.
  - *Why D is incorrect:* West Europe is paired with North Europe. It is in a different geography (Europe) from East US (Americas). GRS keeps data within the same geography except for the Brazil South exception.

---

### Question 14 (5 points)

An Azure subscription has the following policy applied at the Root Management Group: "Allowed locations = East US, West US." A developer in a child resource group tries to create a virtual machine in North Europe. What happens?

- A) The VM is created in North Europe and the policy logs a compliance warning
- B) The VM creation is blocked because the policy restricts allowed locations
- C) The policy does not apply to resource groups — only to subscriptions
- D) The developer can override the policy by assigning themselves the Owner role

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Policy with a Deny effect blocks resource creation in non-allowed locations. Policies applied at the Root Management Group cascade to all child management groups, subscriptions, resource groups, and resources. North Europe is not in the allowed list, so the VM creation fails with a policy violation error.
  - *Why A is incorrect:* That describes the Audit effect, not Deny. An Audit policy would allow the creation and flag it as non-compliant. A Deny policy blocks the creation entirely.
  - *Why C is incorrect:* Policies cascade downward through the entire management hierarchy. A policy at the Root Management Group applies to all subscriptions, all resource groups, and all individual resources beneath it.
  - *Why D is incorrect:* Azure RBAC (including Owner role) and Azure Policy are independent evaluation systems. Having Owner role authorizes the action; Policy determines whether the resulting configuration is permitted. A Deny policy blocks the operation regardless of the user's role.

---

### Question 15 (5 points)

What is the maximum depth of management groups beneath the Root Management Group in an Azure tenant?

- A) Two levels
- B) Four levels
- C) Six levels
- D) Ten levels

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Azure Management Groups support a maximum of six levels of depth beneath the Root Management Group (not counting the root itself or the subscription level). This is a specific fact that appears on AZ-900.
  - *Why A is incorrect:* Two levels would severely limit enterprise hierarchy modeling. Azure supports significantly more depth.
  - *Why B is incorrect:* Four levels is below the actual maximum of six. This is a plausible-sounding distractor but is not the documented limit.
  - *Why D is incorrect:* Ten levels exceeds the documented maximum. Azure also limits total management group count to 10,000 per tenant, but depth is capped at six beneath the root.

---

### Question 16 (5 points)

An architect is designing a storage solution that must survive a complete zone failure in the primary region. The data does not need geographic redundancy. Which Azure Storage redundancy option is most cost-effective for this requirement?

- A) LRS (Locally Redundant Storage)
- B) ZRS (Zone-Redundant Storage)
- C) GRS (Geo-Redundant Storage)
- D) GZRS (Geo-Zone-Redundant Storage)

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* ZRS replicates data synchronously across three Availability Zones within the same region. If one entire zone (datacenter) fails, data remains available from the other two zones. ZRS provides zone-level protection without the additional cost of geo-replication.
  - *Why A is incorrect:* LRS stores three copies within a single datacenter. A zone failure (meaning that entire datacenter goes offline) would make all three LRS copies unavailable simultaneously.
  - *Why C is incorrect:* GRS adds geo-replication to a paired region, providing regional failure protection. This exceeds the stated requirement (zone failure only) and costs more than ZRS.
  - *Why D is incorrect:* GZRS combines zone redundancy with geo-replication — the most durable and most expensive option. It exceeds what is needed when geographic redundancy is explicitly not required.

---

### Question 17 (5 points)

A company with operations in the European Union deploys all Azure resources in the West Europe region. They are concerned about GDPR data residency requirements. Which Azure feature ensures that geo-redundant storage keeps EU customer data within the EU geography?

- A) Azure Sovereign Regions
- B) Azure Geographies with same-geography region pairs
- C) Azure Management Groups with location policies
- D) Azure Resource Locks

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Geographies preserve data residency boundaries. West Europe is paired with North Europe — both are within the EU geography. GRS replication stays within the same geography, ensuring EU data never leaves the EU to satisfy GDPR data residency requirements.
  - *Why A is incorrect:* Azure Sovereign Regions (Azure Government, Azure China) are for specific government/regulated cloud instances, not for standard EU commercial data residency. The company's scenario does not require a sovereign cloud.
  - *Why C is incorrect:* Management Groups with location policies can restrict which regions resources are deployed in, but they do not govern where geo-redundant storage replication sends data. Region pairs determine GRS replication destinations.
  - *Why D is incorrect:* Resource Locks prevent deletion or modification of resources. They have no relationship to data replication geography or GDPR data residency compliance.

---

### Question 18 (5 points)

A resource group named "WebApp-RG" contains a VM, a storage account, and a virtual network. An administrator deletes "WebApp-RG." Which resources are deleted?

- A) Only the resource group container is removed; the VM, storage account, and VNet remain as orphaned resources
- B) The VM and storage account are deleted, but the VNet is preserved as it may be used by other resource groups
- C) All three resources — VM, storage account, and VNet — are deleted along with the resource group
- D) Only empty resource groups can be deleted; the operation fails because the group contains resources

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Deleting a resource group is a cascading delete operation that destroys all resources contained within it simultaneously. The Azure Portal and CLI both warn users and require confirmation precisely because all contained resources will be permanently deleted.
  - *Why A is incorrect:* Resources cannot be orphaned in Azure — every resource must belong to exactly one resource group. When the resource group is deleted, its contents are deleted with it; they cannot persist as orphaned objects.
  - *Why B is incorrect:* Azure does not selectively preserve networking resources during a resource group deletion. All resources in the group are deleted equally, regardless of type.
  - *Why D is incorrect:* Azure does not require a resource group to be empty before deletion. The deletion cascade removes all contents automatically after the user confirms the operation.

---

### Question 19 (5 points)

Which of the following correctly describes the purpose of an Azure geography?

- A) A geography is another name for an Azure region and the terms are interchangeable
- B) A geography is a discrete market, typically a country or group of countries, that defines data residency and compliance boundaries containing two or more Azure regions
- C) A geography is the physical building within a region that houses Azure servers
- D) A geography defines the maximum distance allowed between two paired regions

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* An Azure geography is a market-level boundary — typically a country or closely related group of countries — that preserves data residency and compliance. Each geography contains multiple Azure regions, ensuring data can be geo-replicated while staying within the same regulatory jurisdiction.
  - *Why A is incorrect:* Geographies and regions are different levels of the Azure physical hierarchy. A geography contains multiple regions; they are not interchangeable terms.
  - *Why C is incorrect:* That description applies to a datacenter or an Availability Zone. A geography is a much larger, market-level concept that spans multiple cities and regions.
  - *Why D is incorrect:* The minimum distance between paired regions (at least 300 miles) is a region pair characteristic, not a geography definition. Geographies define compliance and data residency boundaries, not distance constraints.

---

### Question 20 (5 points)

A university IT team is planning their first Azure deployment. They need to ensure that student lab resources, faculty research resources, and administrative systems each have separate billing reports and can be managed by separate teams. What is the recommended Azure hierarchy structure?

- A) One subscription with three resource groups named for each area
- B) Three subscriptions (one per area), organized under a Management Group, with appropriate resource groups inside each subscription
- C) Three separate Azure tenants — one per area
- D) One subscription with resource tags to identify each area, relying on tag-based cost filtering

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Separate subscriptions provide separate billing boundaries (each subscription generates its own invoice/cost report) and separate access control boundaries (each team manages their own subscription). A Management Group organizes all three subscriptions for shared university-level governance policies. This is the standard Azure landing zone pattern for multi-team environments.
  - *Why A is incorrect:* A single subscription with three resource groups shares one billing boundary — there is no automatic per-area invoice separation. Cost filtering by resource group is possible but is not as clean or enforceable as a subscription boundary.
  - *Why C is incorrect:* Separate Azure tenants would be entirely separate Azure environments with completely separate Entra ID directories. This creates extreme complexity for any shared services (shared VNets, shared identity) and is not the correct architecture for departments within the same university.
  - *Why D is incorrect:* Tag-based cost filtering requires that all resources be consistently tagged. It provides cost reporting but not billing boundary separation. Tags can be omitted or incorrect; subscription boundaries are structural and always enforced.

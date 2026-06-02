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

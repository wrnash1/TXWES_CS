# Quiz: Module 02 - Azure Physical Architecture

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
How many separate physical datacenters must exist within a single Azure Availability Zone?

* A) At least one
* B) Exactly three
* C) Ten
* D) Availability Zones do not contain physical datacenters
* **Correct Answer:** A) An Availability Zone is made up of one or more physical datacenters equipped with independent power, cooling, and networking.
* **Distractor Analysis:**
  * *Why correct:* An Availability Zone is made up of one or more physical datacenters equipped with independent power, cooling, and networking.
  * *Why B is incorrect:* "Exactly three" is a common misconception — an Azure region with AZ support has at least three zones, not three datacenters per zone.

---

**Question 2**
Which of the following most accurately describes **Azure Resource Manager (ARM)**?

* A) The deployment and management service through which all Azure resource operations — from the portal, CLI, PowerShell, or API — are processed, providing consistent RBAC, tagging, and template-based deployments.
* B) A geographic datacenter location used to place Azure resources close to end users for low latency.
* C) A logical container that groups related Azure resources sharing the same lifecycle and billing scope.
* D) A feature that automatically replicates Azure resources to a secondary region at least 300 miles away.
* **Correct Answer:** A) ARM is the deployment and management service through which all Azure resource operations are processed, providing consistent RBAC, tagging, and template-based deployments.
* **Distractor Analysis:**
  * *Why A is correct:* ARM is the control plane for all Azure resource interactions regardless of which tool is used.
  * *Why B is incorrect:* That describes an Azure Region, not ARM.
  * *Why C is incorrect:* That describes a Resource Group, which is a construct managed by ARM but is not ARM itself.
  * *Why D is incorrect:* That describes Azure Region Pairs / geo-replication, not ARM.

---

**Question 3**
A compliance requirement states that all data must remain within the United States. Which Azure concept directly controls where resource data is physically stored?

* A) Availability Zone selection
* B) Azure Region selection
* C) Resource Group naming convention
* D) Azure Subscription tier
* **Correct Answer:** B) Selecting an Azure Region determines the physical geographic location where your data is stored and processed, satisfying data residency requirements.
* **Distractor Analysis:**
  * *Why B is correct:* Region selection is the primary mechanism for data residency compliance in Azure.
  * *Why A is incorrect:* Availability Zones are within a region and do not change the country where data is stored.
  * *Why C is incorrect:* Resource Group names are metadata labels with no effect on physical data location.
  * *Why D is incorrect:* Subscription tier affects pricing and resource limits, not data residency.

---

**Question 4**
While designing an Azure deployment, you need services that remain available even if an entire Azure datacenter goes offline, without leaving the region. Which architecture pattern achieves this?

* A) Deploy all resources to a single Availability Zone for lowest latency
* B) Use Azure Paired Regions and enable geo-replication for all services
* C) Deploy resources across multiple Availability Zones within the same region
* D) Create multiple Resource Groups in the same datacenter
* **Correct Answer:** C) Deploying resources across multiple Availability Zones within the same region provides datacenter-level fault tolerance while keeping data within the region.
* **Distractor Analysis:**
  * *Why C is correct:* Multiple Availability Zones within one region protects against single-datacenter failure without cross-region replication.
  * *Why A is incorrect:* A single zone provides no fault tolerance against datacenter failure.
  * *Why B is incorrect:* Paired Regions move data to a different geographic region, which may violate data residency requirements.
  * *Why D is incorrect:* Multiple Resource Groups in the same datacenter are logical containers — they provide no physical redundancy.

---

**Question 5**
You want to ensure your Azure subscription follows corporate standards: all VMs must use approved SKUs and all resources must have a cost-center tag. Which Azure service enforces these rules automatically at deployment time?

* A) Azure Advisor
* B) Azure Monitor
* C) Azure Policy
* D) Azure Blueprints
* **Correct Answer:** C) Azure Policy evaluates resources against defined rules and can deny deployments that do not comply with required SKUs, tags, or configurations.
* **Distractor Analysis:**
  * *Why C is correct:* Azure Policy is the governance service that enforces compliance rules and can block non-compliant deployments automatically.
  * *Why A is incorrect:* Azure Advisor provides recommendations but cannot block deployments.
  * *Why B is incorrect:* Azure Monitor collects telemetry data — it does not enforce deployment rules.
  * *Why D is incorrect:* Azure Blueprints packages policies and role assignments for repeatable environment setup but the enforcement mechanism is still Azure Policy inside the blueprint.

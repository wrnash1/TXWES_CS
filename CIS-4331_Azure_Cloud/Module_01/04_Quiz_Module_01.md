# Quiz: Module 01 - Cloud Computing Concepts

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which service model gives the consumer the greatest control over virtual machines and operating systems?

* A) Software as a Service (SaaS)
* B) Platform as a Service (PaaS)
* C) Infrastructure as a Service (IaaS)
* D) Database as a Service (DBaaS)
* **Correct Answer:** C) IaaS provides raw infrastructure (VMs, networking, storage), leaving OS and software management to the customer.
* **Distractor Analysis:**
  * *Why correct:* IaaS provides raw infrastructure (VMs, networking, storage), leaving OS and software management to the customer.
  * *Why A/B/D are incorrect:* PaaS and SaaS manage the OS layer for you, reducing your control. DBaaS is a subcategory of PaaS.

---

**Question 2**
Which of the following most accurately describes the **Public / Private / Hybrid cloud deployment models**?

* A) Public cloud is owned by a third-party provider and shared across tenants; private cloud uses dedicated infrastructure for one organization; hybrid cloud connects both, enabling workload portability between on-premises and public cloud.
* B) Public cloud stores data exclusively on government-owned servers; private cloud is hosted only by the organization's on-premises IT team; hybrid cloud requires a physical VPN device at every branch office.
* C) Public cloud requires a dedicated fiber link from each customer; private cloud allows multiple tenants to share the same physical hardware; hybrid cloud is used only for disaster recovery scenarios.
* D) Public cloud has no SLA guarantees; private cloud is always cheaper than public cloud; hybrid cloud eliminates the need for any on-premises infrastructure.
* **Correct Answer:** A) Public cloud is owned by a third-party provider and shared across tenants; private cloud uses dedicated infrastructure for one organization; hybrid cloud connects both.
* **Distractor Analysis:**
  * *Why A is correct:* This accurately describes all three deployment models as defined by Microsoft for the AZ-900 exam.
  * *Why B is incorrect:* Public cloud is not government-owned, and hybrid cloud does not require physical VPN hardware at every location.
  * *Why C is incorrect:* Private cloud does not mean shared hardware — that describes public cloud. Hybrid cloud is not limited to disaster recovery.
  * *Why D is incorrect:* Public cloud provides strong SLAs, and hybrid cloud does not eliminate on-premises infrastructure — it connects to it.

---

**Question 3**
A company keeps sensitive data on its own servers but bursts workloads into Azure during peak demand. Which deployment model best describes this approach?

* A) Public cloud only
* B) Private cloud only
* C) Hybrid cloud
* D) Community cloud
* **Correct Answer:** C) Hybrid cloud connects on-premises infrastructure with public cloud resources, allowing workloads to move between environments as needed.
* **Distractor Analysis:**
  * *Why C is correct:* Keeping sensitive data on-premises while bursting to Azure is the definition of hybrid cloud.
  * *Why A is incorrect:* Public cloud only would move everything off-premises with no on-premises retention.
  * *Why B is incorrect:* Private cloud only would not use Azure at all.
  * *Why D is incorrect:* Community cloud is shared infrastructure for a specific group of organizations — not the same as on-premises-plus-Azure bursting.

---

**Question 4**
A startup wants to launch a web application without purchasing servers, paying only for compute hours actually used. Which cloud benefit does this scenario demonstrate?

* A) High availability
* B) Geo-redundancy
* C) Consumption-based pricing (OPEX model)
* D) Dedicated hardware ownership
* **Correct Answer:** C) Cloud providers offer consumption-based pricing, shifting costs from capital expenditure (CAPEX) to operational expenditure (OPEX) — you pay only for what you use.
* **Distractor Analysis:**
  * *Why C is correct:* Paying only for actual compute hours consumed is the core OPEX/consumption-based pricing model.
  * *Why A is incorrect:* High availability describes uptime guarantees, not billing structure.
  * *Why B is incorrect:* Geo-redundancy describes geographic data replication, not payment model.
  * *Why D is incorrect:* The startup explicitly avoids owning hardware — this is the opposite of what the scenario describes.

---

**Question 5**
You need to protect against a single datacenter failure in Azure without deploying to a second Azure region. Which Azure feature provides this protection?

* A) Azure Availability Zones — physically separate datacenters within the same region, each with independent power, cooling, and networking.
* B) Azure Paired Regions — replicates data to a geographically distant region automatically.
* C) Azure Resource Groups — distributes resources across multiple physical hosts within a datacenter.
* D) Azure Reservations — guarantees dedicated physical hardware for a 1- or 3-year term.
* **Correct Answer:** A) Azure Availability Zones — physically separate datacenters within the same region, each with independent power, cooling, and networking.
* **Distractor Analysis:**
  * *Why A is correct:* Availability Zones provide datacenter-level fault isolation within a single region — exactly what the scenario requires.
  * *Why B is incorrect:* Paired Regions replicate to a different region, which the scenario explicitly excludes.
  * *Why C is incorrect:* Resource Groups are logical containers for management and provide no physical fault isolation.
  * *Why D is incorrect:* Reservations are a cost-commitment pricing model with no relationship to fault tolerance.

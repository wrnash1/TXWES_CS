# Quiz: Module 01 - Cloud Computing Concepts

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Cloud Concepts (25-30% of exam)
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

Which service model gives the customer the greatest control over virtual machines, operating systems, and installed software?

- A) Software as a Service (SaaS)
- B) Platform as a Service (PaaS)
- C) Infrastructure as a Service (IaaS)
- D) Database as a Service (DBaaS)

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* IaaS provides raw virtualized infrastructure. The customer manages the OS, middleware, and applications, giving maximum control over the full software stack above the hypervisor.
- *Why A is incorrect:* SaaS gives the customer the least control — only data and identity configuration. The provider manages the entire application stack.
- *Why B is incorrect:* PaaS abstracts the OS away from the customer. The customer deploys application code but cannot configure the underlying operating system.
- *Why D is incorrect:* DBaaS is a subset category of PaaS, not a distinct AZ-900 service model. Microsoft's AZ-900 curriculum uses only IaaS, PaaS, and SaaS as the three service model tiers.

---

## Question 2

A company retains sensitive financial records on its own servers but scales compute workloads into Azure during end-of-quarter processing peaks. Which deployment model best describes this architecture?

- A) Public cloud only
- B) Private cloud only
- C) Hybrid cloud
- D) Community cloud

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Hybrid cloud connects on-premises or private infrastructure with a public cloud, allowing workloads and data to move between environments. Keeping sensitive data on-premises while bursting to Azure is the canonical hybrid cloud use case.
- *Why A is incorrect:* Public cloud only would move all resources to Azure with no on-premises retention. The scenario explicitly keeps sensitive data on the company's own servers.
- *Why B is incorrect:* Private cloud only would use no Azure services. The scenario explicitly uses Azure for peak processing.
- *Why D is incorrect:* Community cloud is shared infrastructure for a specific group of organizations with common concerns (such as government agencies or healthcare systems). It is not the same as a single organization spanning on-premises and Azure.

---

## Question 3

A startup wants to deploy a web application and pay only for the compute hours actually consumed — with no upfront server purchase. Which cloud benefit does this scenario primarily illustrate?

- A) High availability
- B) Geo-redundancy
- C) Consumption-based pricing
- D) Dedicated hardware ownership

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Consumption-based pricing — also called the OPEX model — means customers pay only for resources while they are running, with no capital expenditure for hardware. This is a foundational Azure benefit tested on AZ-900.
- *Why A is incorrect:* High availability describes the percentage of time a service remains accessible (SLA uptime), not the billing model. The scenario is about cost structure, not uptime.
- *Why B is incorrect:* Geo-redundancy describes replicating data or services across geographic regions for disaster resilience. It is a reliability feature, not a pricing model.
- *Why D is incorrect:* Dedicated hardware ownership describes the opposite of what the startup wants — it describes on-premises CAPEX purchasing, which the scenario is specifically avoiding.

---

## Question 4

In the Shared Responsibility Model, which of the following is always the customer's responsibility regardless of whether the deployment is IaaS, PaaS, or SaaS?

- A) Operating system patching
- B) Data classification and protection
- C) Runtime environment management
- D) Physical hardware security

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Data classification and protection is always the customer's responsibility across all three service models. Microsoft cannot determine the sensitivity of your data — only the data owner can classify and protect it appropriately.
- *Why A is incorrect:* OS patching responsibility varies by service model. In IaaS it is the customer's responsibility; in PaaS and SaaS it is the provider's responsibility.
- *Why C is incorrect:* Runtime environment management is the customer's responsibility in IaaS, but it is the provider's responsibility in PaaS and SaaS. It is not constant across all models.
- *Why D is incorrect:* Physical hardware security is always the provider's responsibility, not the customer's. This is the opposite of what the question asks.

---

## Question 5

A team needs to protect an Azure application against a single datacenter failure without deploying to a second Azure region. Which Azure feature provides this protection?

- A) Azure Availability Zones — physically separate datacenters within the same region
- B) Azure Paired Regions — automatic data replication to a geographically distant region
- C) Azure Resource Groups — logical containers that distribute resources across hosts
- D) Azure Reservations — dedicated physical hardware for a 1- or 3-year term

**Correct Answer:** A

**Distractor Analysis:**

- *Why A is correct:* Availability Zones are physically separate datacenters within a single Azure region, each with independent power, cooling, and networking. Deploying across Availability Zones protects against a single datacenter failure without leaving the region.
- *Why B is incorrect:* Paired Regions replicate to a geographically different region. The scenario explicitly states the team does not want to deploy to a second region.
- *Why C is incorrect:* Resource Groups are logical management containers. They provide no physical fault isolation and do not distribute resources across hardware.
- *Why D is incorrect:* Reservations are a cost-commitment pricing mechanism. They have no relationship to fault tolerance or datacenter redundancy.

---

## Question 6

An organization moves from purchasing on-premises servers to renting Azure virtual machines and paying monthly based on usage. Which financial shift does this represent?

- A) From OPEX to CAPEX
- B) From CAPEX to OPEX
- C) From variable cost to fixed cost
- D) From depreciation to amortization

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Purchasing physical servers is a capital expenditure (CAPEX) — an upfront asset purchase that depreciates over time. Renting Azure VMs is an operational expenditure (OPEX) — a recurring pay-as-you-go expense with no hardware ownership. Cloud adoption is defined by this CAPEX-to-OPEX shift.
- *Why A is incorrect:* This reverses the direction. Moving to cloud is CAPEX to OPEX, not OPEX to CAPEX.
- *Why C is incorrect:* Cloud consumption-based pricing is variable cost (you pay more when you use more), not fixed cost. Shifting to cloud typically moves from fixed (predictable hardware payments) to variable (usage-based) cost.
- *Why D is incorrect:* Depreciation and amortization are accounting treatments for assets. While cloud eliminates asset depreciation, the correct AZ-900 framework describes the shift as CAPEX to OPEX.

---

## Question 7

A development team deploys their Python application to Azure App Service. They only upload code and set environment variables — they never access or patch a server OS. Which service model does Azure App Service represent?

- A) IaaS
- B) PaaS
- C) SaaS
- D) FaaS (Function as a Service)

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure App Service is a PaaS offering. Microsoft manages the underlying OS, web server infrastructure, and scaling. The customer only provides application code and configuration. The key signal in the scenario is "never access or patch a server OS."
- *Why A is incorrect:* IaaS would require the team to access, configure, and patch the operating system. The scenario explicitly states they do not do this.
- *Why C is incorrect:* SaaS means the provider manages the application logic itself. In this scenario, the team writes their own application code — they are the application developer, not a software consumer.
- *Why D is incorrect:* FaaS (Azure Functions) is a serverless compute model within PaaS. While Azure App Service and Azure Functions are related concepts, FaaS is not the correct AZ-900 service model classification. AZ-900 uses IaaS, PaaS, and SaaS as the three models.

---

## Question 8

Which cloud characteristic means the system automatically provisions additional resources when demand increases and releases them when demand decreases, without manual intervention?

- A) Scalability
- B) High availability
- C) Elasticity
- D) Reliability

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Elasticity is the automatic provisioning and de-provisioning of resources in response to demand changes. The key word in the question is "automatically" — no manual intervention. Azure VM Scale Sets are the primary IaaS elasticity mechanism.
- *Why A is incorrect:* Scalability is the ability to increase or decrease resources. However, scalability does not necessarily imply automatic action — an administrator manually resizing a VM is scaling. Elasticity adds the automatic, demand-driven dimension.
- *Why B is incorrect:* High availability is the guarantee of uptime (expressed as an SLA percentage), not the ability to adjust resource counts dynamically.
- *Why D is incorrect:* Reliability describes the consistency of service performance and the fault-tolerant architecture that prevents single points of failure. It is not the same as demand-driven auto-scaling.

---

## Question 9

An enterprise needs maximum control over hardware configuration and must ensure that no other organization's data resides on the same physical hardware. The organization also has significant existing hardware investments. Which deployment model is most appropriate?

- A) Public cloud
- B) Private cloud
- C) Hybrid cloud
- D) Community cloud

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Private cloud provides dedicated hardware for a single organization, ensuring no multi-tenancy and maximum hardware control. Existing hardware investments can be leveraged as the private cloud substrate. This is consistent with AZ-900's definition of private cloud.
- *Why A is incorrect:* Public cloud uses shared physical infrastructure across multiple tenants. It does not satisfy the requirement that no other organization's data resides on the same physical hardware.
- *Why C is incorrect:* Hybrid cloud combines private/on-premises infrastructure with public cloud. The scenario does not indicate any need for public cloud services, and the concern about multi-tenancy would persist in the public cloud portion.
- *Why D is incorrect:* Community cloud is shared infrastructure for a specific group of organizations. It still involves hardware shared among multiple entities, which violates the scenario's isolation requirement.

---

## Question 10

Which of the following best describes the difference between a private cloud and a traditional on-premises data center, according to AZ-900 definitions?

- A) A private cloud uses public internet connectivity; a traditional data center uses private network connections.
- B) A private cloud implements cloud characteristics such as self-service provisioning and rapid elasticity on dedicated hardware; a traditional data center does not provide these characteristics.
- C) A private cloud is always managed by a third-party hosting provider; a traditional data center is always managed internally.
- D) A private cloud requires more physical servers than a traditional data center to achieve redundancy.

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The AZ-900 definition distinguishes private cloud from traditional data centers by the presence of cloud characteristics: on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service. A traditional data center may be on-premises and dedicated, but it lacks these operational characteristics.
- *Why A is incorrect:* Both private clouds and traditional data centers can use either public internet or private network connections. Network connectivity type is not the distinguishing factor.
- *Why C is incorrect:* Private cloud can be managed internally (on-premises private cloud) or by a third party (hosted private cloud). Location of management is not the defining characteristic. Some traditional data centers are also managed by external providers.
- *Why D is incorrect:* Server count is not the distinguishing factor. A private cloud may run on fewer physical servers than a traditional data center while still qualifying as private cloud through software-defined self-service and elasticity capabilities.

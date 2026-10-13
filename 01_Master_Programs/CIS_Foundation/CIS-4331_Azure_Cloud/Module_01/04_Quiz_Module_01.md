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

---

### Question 11 (5 points)

A retail company's website experiences traffic spikes of 10x normal load every Black Friday. For the remaining 50 weeks of the year, the site runs at low utilization. Which cloud benefit is most valuable for this organization?

- A) High availability
- B) Geo-redundancy
- C) Elasticity
- D) Predictability

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Elasticity is the ability to automatically scale resources up during demand spikes and release them when demand subsides. This perfectly matches the Black Friday scenario: the site scales to 10x capacity for hours then scales back down, paying only for what was used.
  - *Why A is incorrect:* High availability addresses uptime guarantees (SLA percentages) and fault tolerance, not the dynamic matching of resource capacity to variable demand.
  - *Why B is incorrect:* Geo-redundancy means replicating resources across geographic regions for disaster recovery. It does not address the cost-efficiency challenge of variable demand.
  - *Why D is incorrect:* Predictability refers to consistent performance or forecasting cloud spending. The scenario's core need is responsive scaling, not cost forecasting.

---

### Question 12 (5 points)

A government agency mandates that all classified data must be stored on hardware physically controlled by the agency and never shared with any other organization. Which cloud deployment model satisfies this requirement?

- A) Public cloud
- B) Private cloud
- C) Hybrid cloud
- D) Community cloud

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Private cloud uses dedicated hardware for a single organization. The agency controls the physical hardware, ensuring no other organization shares the infrastructure. This directly satisfies the classified data isolation mandate.
  - *Why A is incorrect:* Public cloud uses shared multi-tenant physical infrastructure managed by Microsoft. Workloads from different organizations run on the same physical hardware (logically isolated), which does not satisfy the requirement for agency-controlled hardware.
  - *Why C is incorrect:* Hybrid cloud combines on-premises or private infrastructure with public cloud. The public cloud component would involve Microsoft-managed shared hardware, violating the classified data requirement.
  - *Why D is incorrect:* Community cloud shares infrastructure among a specific group of organizations with common interests. The scenario requires hardware controlled exclusively by one agency — not shared even within a community.

---

### Question 13 (5 points)

An Azure SLA states 99.95% availability. What is the maximum permitted downtime per month under this agreement?

- A) 4 minutes 22 seconds
- B) 21 minutes 54 seconds
- C) 43 minutes 49 seconds
- D) 8 hours 41 minutes

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* 99.95% availability allows 0.05% downtime per month. A 30-day month has 43,200 minutes. 0.05% of 43,200 = 21.6 minutes, or approximately 21 minutes 54 seconds.
  - *Why A is incorrect:* 4 minutes 22 seconds corresponds to the maximum monthly downtime for 99.99% availability — a higher SLA tier than 99.95%.
  - *Why C is incorrect:* 43 minutes 49 seconds corresponds to the maximum monthly downtime for 99.9% availability — a lower SLA tier than 99.95%.
  - *Why D is incorrect:* 8 hours 41 minutes corresponds to the maximum annual downtime for 99.9% SLA. This is an annual figure, not monthly, and for a different SLA tier.

---

### Question 14 (5 points)

According to the Shared Responsibility Model, which of the following tasks is the customer's responsibility when using a SaaS application?

- A) Patching the application's web server software
- B) Managing the network switches in the provider's datacenter
- C) Managing user accounts and access permissions within the application
- D) Upgrading the database engine used by the application

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* In SaaS, the provider manages the entire application stack. The customer retains responsibility for managing their own users — who has accounts, what roles they are assigned, what data they can access. Identity and access management within the application is always the customer's responsibility.
  - *Why A is incorrect:* Web server patching in a SaaS application is the provider's responsibility. The customer has no access to the underlying web server layer.
  - *Why B is incorrect:* Physical datacenter networking, including switches, is always the provider's responsibility across all three service models (IaaS, PaaS, SaaS).
  - *Why D is incorrect:* Database engine upgrades in a SaaS application are managed by the provider. The customer has no visibility or control over the database infrastructure.

---

### Question 15 (5 points)

A cloud architect explains that two services with individual SLAs of 99.9% each are combined in series so that the application fails if either service fails. What is the composite SLA?

- A) 99.9% (unchanged — the higher SLA governs)
- B) 99.99% (combining services improves the SLA)
- C) Approximately 99.8%
- D) 100% (redundant services guarantee perfect availability)

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* When services are combined in series (the application requires both to function), the composite SLA is calculated by multiplying the individual SLAs: 99.9% × 99.9% = 99.8001%, approximately 99.8%. Each additional dependency reduces the effective SLA.
  - *Why A is incorrect:* The composite SLA is not governed by the highest individual SLA. Because both services must be available for the application to function, both uptime guarantees must hold simultaneously — which is statistically less likely than either alone.
  - *Why B is incorrect:* Combining services in series reduces the composite SLA; it does not improve it. Combining services in parallel (redundancy) can improve availability, but this scenario specifies a series dependency.
  - *Why D is incorrect:* No combination of Azure services achieves a 100% SLA. Chaining services in series mathematically reduces availability below either individual SLA.

---

### Question 16 (5 points)

Which cloud computing characteristic allows a company's developer to provision 20 virtual machines in five minutes through a web portal, without calling a salesperson or submitting a purchase order?

- A) Measured service
- B) Broad network access
- C) On-demand self-service
- D) Resource pooling

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* On-demand self-service is one of the five essential characteristics of cloud computing defined by NIST. It means users can provision computing resources unilaterally, without requiring human interaction with each service provider. The Azure Portal exemplifies this — VMs can be created instantly without procurement workflows.
  - *Why A is incorrect:* Measured service means usage is monitored and billed based on consumption. It relates to how billing is tracked, not how quickly resources can be provisioned.
  - *Why B is incorrect:* Broad network access means services are accessible over the network from diverse client devices. It describes connectivity, not the self-service provisioning process.
  - *Why D is incorrect:* Resource pooling means the provider serves multiple customers from shared physical infrastructure. It describes the multi-tenant architecture, not the user's ability to provision instantly without interaction.

---

### Question 17 (5 points)

An organization has 500 users accessing a cloud-hosted HR application. The application vendor manages all updates, servers, and databases. The organization's IT team only manages employee user accounts and configures which data fields each role can view. What service model is this?

- A) IaaS
- B) PaaS
- C) SaaS
- D) CaaS (Containers as a Service)

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* The organization does not manage any infrastructure, OS, middleware, or application code. The vendor manages the complete stack. The organization only manages its own data and user access — the defining customer responsibilities under SaaS. Cloud HR applications like Workday and SAP SuccessFactors are canonical SaaS examples.
  - *Why A is incorrect:* IaaS would require the organization's IT team to manage the OS, middleware, and application installation. The scenario explicitly states the vendor handles all servers and software.
  - *Why B is incorrect:* PaaS would require the organization to deploy and maintain application code. Here, the vendor provides the finished application — the organization is a consumer, not a developer.
  - *Why D is incorrect:* CaaS is not one of the three AZ-900 service model tiers. AZ-900 recognizes IaaS, PaaS, and SaaS as the three models.

---

### Question 18 (5 points)

A company switches from on-premises servers to Azure Virtual Machines. The finance department asks whether the monthly Azure bill will vary. Which aspect of cloud pricing explains why the bill might differ each month?

- A) Fixed monthly pricing — cloud services have a set monthly fee regardless of usage
- B) Consumption-based pricing — the bill reflects actual resource usage, which varies with workload demand
- C) Annual commitment pricing — the total is divided by 12 to produce a fixed monthly figure
- D) Hardware depreciation — the bill decreases each month as hardware age increases

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure uses a consumption-based pricing model. Each month's bill reflects actual usage: how many hours VMs ran, how many gigabytes were stored, how many transactions processed. If demand fluctuates, the bill fluctuates accordingly.
  - *Why A is incorrect:* Azure does not have a fixed monthly fee model for most services. Pay-as-you-go billing varies with consumption.
  - *Why C is incorrect:* Annual commitment pricing (Reserved Instances) creates a consistent monthly equivalent payment, but this applies only when reservations are purchased. The default is consumption-based variable billing.
  - *Why D is incorrect:* Hardware depreciation is an accounting concept for physical asset ownership. In cloud computing, the customer does not own hardware and incurs no depreciation expense.

---

### Question 19 (5 points)

What distinguishes Azure's definition of "reliability" from "high availability"?

- A) Reliability and high availability are identical concepts in Azure
- B) High availability is expressed as an SLA uptime percentage; reliability refers to the architectural distribution of infrastructure across locations to prevent single points of failure
- C) Reliability is higher than high availability — it guarantees 100% uptime while high availability only guarantees 99.99%
- D) High availability applies to VMs; reliability applies only to Azure networking services

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* On AZ-900, high availability is the uptime commitment expressed as a percentage SLA. Reliability is an architectural concept — the infrastructure is designed and distributed globally so that a failure in one location does not cause a system-wide outage. Reliability is achieved through redundancy; high availability is measured and guaranteed through SLAs.
  - *Why A is incorrect:* These are distinct concepts on AZ-900. High availability is quantitative (an SLA number); reliability is qualitative/architectural (global distribution, fault isolation).
  - *Why C is incorrect:* No Azure concept guarantees 100% uptime. Reliability is not a higher tier of high availability — it is a different dimension describing architecture rather than uptime percentages.
  - *Why D is incorrect:* Both high availability and reliability apply across all Azure service types, not just VMs or networking.

---

### Question 20 (5 points)

A financial analyst asks why a company should pay for Azure Reserved Instances when the pay-as-you-go model offers maximum flexibility. Which is the most accurate response?

- A) Reserved Instances offer hardware ownership, providing the same CAPEX benefits as on-premises servers
- B) Reserved Instances can save up to 72% compared to pay-as-you-go for resources with predictable, continuous usage, while still being classified as OPEX with no hardware to manage
- C) Reserved Instances are only available for virtual machines and cannot be used for other Azure services
- D) Reserved Instances require a 5-year commitment and are only cost-effective for workloads running more than 10 years

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Reserved Instances offer discounts up to 72% for 3-year commitments compared to pay-as-you-go pricing. Critically, they remain OPEX — the customer commits to paying for the service but does not purchase hardware. For predictable, long-running workloads, the cost savings far exceed the loss of flexibility.
  - *Why A is incorrect:* Reserved Instances do not involve hardware ownership. The customer is committing to a cloud service billing arrangement, not buying physical assets. This is still OPEX, not CAPEX.
  - *Why C is incorrect:* Azure Reservations apply to multiple services beyond VMs — including Azure SQL Database, Cosmos DB, Azure App Service, and more.
  - *Why D is incorrect:* Azure Reserved Instances are available in 1-year and 3-year terms — not 5 years. The break-even point against pay-as-you-go is typically reached within a few months.

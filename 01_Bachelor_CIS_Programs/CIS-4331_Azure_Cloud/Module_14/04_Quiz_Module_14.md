# Quiz: Module 14 — Azure Cost Management and Pricing

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. This quiz is aligned to AZ-900 exam objectives in the Management and Governance domain.

---

## Question 1

A solutions architect needs to estimate the monthly cost of deploying 10 virtual machines, an Azure SQL Database, and a storage account before any resources are created. Which Azure tool should they use?

A. Azure Cost Management + Billing
B. Azure TCO Calculator
C. Azure Pricing Calculator
D. Azure Advisor

**Correct Answer: C**

### Distractor Analysis

**A — Incorrect.** Azure Cost Management + Billing shows actual costs for resources that have already been deployed. It cannot estimate costs for resources that do not yet exist.

**B — Incorrect.** The TCO Calculator compares total on-premises cost to total Azure cost to support a migration business case. It is not designed to estimate the cost of specific Azure resources you plan to deploy.

**C — Correct.** The Azure Pricing Calculator is specifically designed for pre-deployment cost estimation. You configure the exact services and settings you plan to deploy and receive a monthly cost estimate before spending any money.

**D — Incorrect.** Azure Advisor provides recommendations to optimize existing deployed resources. It does not estimate costs for resources that have not yet been deployed.

---

## Question 2

An IT director wants to build a financial case for migrating 40 on-premises servers to Azure. They need to show the CFO how current data center costs — including hardware, electricity, and labor — compare to projected Azure costs over three years. Which tool should they use?

A. Azure Pricing Calculator
B. Azure Cost Management + Billing
C. Azure Monitor
D. Azure TCO Calculator

**Correct Answer: D**

### Distractor Analysis

**A — Incorrect.** The Pricing Calculator estimates Azure resource costs but does not capture or model on-premises costs. It cannot produce a three-year comparison between the two environments.

**B — Incorrect.** Cost Management + Billing monitors and analyzes actual Azure spending. It has no capability to model on-premises costs or produce migration business cases.

**C — Incorrect.** Azure Monitor collects and analyzes telemetry data such as metrics and logs for operational health. It is not a cost comparison or financial planning tool.

**D — Correct.** The TCO Calculator is specifically built to compare total on-premises cost to total Azure cost over a three-year period, including hardware, software, facilities, and labor. It is the correct tool for a migration business case.

---

## Question 3

A company has 20 Linux virtual machines that have run continuously for three years and are expected to continue running for at least two more years. CPU utilization averages 75%. Which pricing option would most significantly reduce the cost of these VMs?

A. Spot VMs
B. Dev/Test pricing
C. Azure Reservations (3-year)
D. Pay-as-you-go

**Correct Answer: C**

### Distractor Analysis

**A — Incorrect.** Spot VMs offer the deepest discount (up to 90%) but are subject to eviction with 30 seconds notice when Azure needs the capacity. Production VMs running business workloads 24/7 cannot tolerate eviction.

**B — Incorrect.** Dev/Test pricing is only available for non-production development and testing workloads and carries no SLA. Production workloads do not qualify.

**C — Correct.** Azure Reservations for 3 years offer up to 66% savings compared to pay-as-you-go. The workload is continuously running, predictable, and long-lived — exactly the use case reservations are designed for.

**D — Incorrect.** Pay-as-you-go is the highest-cost option and provides no discount for predictable, long-running workloads. It is the baseline, not an optimization strategy.

---

## Question 4

A data science team wants to run a GPU cluster for 20 hours to train a machine learning model. The training job supports checkpointing and can resume if interrupted. The team wants the lowest possible compute cost. Which VM pricing option is most appropriate?

A. Reserved instances (1-year)
B. Spot VMs
C. Dev/Test pricing
D. Pay-as-you-go with auto-shutdown

**Correct Answer: B**

### Distractor Analysis

**A — Incorrect.** Reserved instances make sense for workloads running continuously for months or years. A 20-hour training job does not justify a 1-year commitment, and the reservation discount applies to hourly usage that must accumulate over time to break even.

**B — Correct.** Spot VMs offer up to 90% off pay-as-you-go and are ideal for interruptible, fault-tolerant workloads. Because the training job supports checkpointing and can resume after eviction, spot VMs provide the maximum cost reduction with acceptable risk.

**C — Incorrect.** Dev/Test pricing requires a Visual Studio subscription or Enterprise Agreement, is for non-production use only, and does not offer the same depth of discount as spot pricing for GPU instances.

**D — Incorrect.** Pay-as-you-go with auto-shutdown stops the VM after a scheduled time but pays full PAYG rates while running. It does not reduce the per-hour cost. For a 20-hour GPU job, this results in a significantly higher bill than spot pricing.

---

## Question 5

A cloud administrator configures a monthly budget of $500 in Azure Cost Management with alert thresholds at 80% and 100%. The current month's actual spend reaches $400. What action does Azure take?

A. Azure automatically stops all running resources to prevent exceeding the budget.
B. Azure sends an alert notification because the 80% threshold ($400) has been reached.
C. Azure pauses billing for the remainder of the month.
D. No action is taken until the $500 limit is fully exceeded.

**Correct Answer: B**

### Distractor Analysis

**A — Incorrect.** Budget alerts in Azure Cost Management are notifications by default. Azure does not automatically stop resources when a budget threshold is reached unless an Action Group with an automation runbook is explicitly configured to do so.

**B — Correct.** $400 is 80% of the $500 budget. When the actual spend crosses the 80% threshold, Azure Cost Management sends the configured alert notification (email and/or Action Group trigger).

**C — Incorrect.** Azure does not pause billing at any point. Cloud resources continue to accrue charges regardless of budget configuration. Budgets are monitoring and alerting tools, not hard spending caps.

**D — Incorrect.** The 80% threshold is set to trigger before the budget is fully exhausted. The alert fires when the threshold percentage is crossed, not only at 100%.

---

## Question 6

Which Azure service provides personalized recommendations to resize underutilized virtual machines, purchase reserved instances, and delete unattached managed disks?

A. Azure Policy
B. Azure Monitor
C. Azure Advisor
D. Azure Cost Management + Billing

**Correct Answer: C**

### Distractor Analysis

**A — Incorrect.** Azure Policy enforces organizational rules on resource configurations. It does not analyze utilization data or make recommendations about VM sizing or purchasing strategies.

**B — Incorrect.** Azure Monitor collects metrics, logs, and traces for operational visibility. While it provides utilization data, it does not generate cost optimization recommendations or suggest purchasing strategies.

**C — Correct.** Azure Advisor is specifically designed to provide personalized best-practice recommendations across five pillars: Cost, Security, Reliability, Performance, and Operational Excellence. The Cost pillar includes VM right-sizing, reserved instance purchasing, and unattached disk cleanup.

**D — Incorrect.** Cost Management + Billing shows spending data and allows you to set budgets. It integrates with Advisor recommendations but does not generate the recommendations itself.

---

## Question 7

A company has Windows Server 2022 licenses with active Software Assurance. They are planning to deploy 50 Windows Server VMs in Azure. Which feature should they use to reduce the cost of the Windows OS license in their Azure VM pricing?

A. Azure Reservations
B. Azure Hybrid Benefit
C. Spot VMs
D. Dev/Test pricing

**Correct Answer: B**

### Distractor Analysis

**A — Incorrect.** Azure Reservations reduce the compute (hardware) portion of VM costs through a commitment discount. They do not address or reduce the Windows Server license cost embedded in the VM hourly rate.

**B — Correct.** Azure Hybrid Benefit allows organizations with Windows Server licenses covered by Software Assurance to bring those licenses to Azure, eliminating the Windows OS license cost from the VM hourly rate. This can save up to 49% on Windows VM costs.

**C — Incorrect.** Spot VMs reduce overall VM cost by using surplus capacity but are subject to eviction. They do not specifically address the Windows license cost component and are not appropriate for production workloads.

**D — Incorrect.** Dev/Test pricing eliminates the Windows Server license cost only for non-production development and testing workloads under a qualifying Visual Studio or Enterprise Agreement subscription. Production workloads do not qualify.

---

## Question 8

An organization wants to automatically move Azure Blob Storage data to a lower-cost tier after it has not been accessed for 60 days. Which Azure feature enables this?

A. Azure Backup policies
B. Blob Storage Lifecycle Management
C. Azure Site Recovery
D. Azure Blob versioning

**Correct Answer: B**

### Distractor Analysis

**A — Incorrect.** Azure Backup policies define how often backups are taken and how long they are retained. They do not automate the movement of production data between storage tiers based on access patterns.

**B — Correct.** Blob Storage Lifecycle Management policies define rules that automatically transition blobs to cooler tiers (Cool or Archive) or delete them based on last-modified date or last-accessed date after a specified number of days.

**C — Incorrect.** Azure Site Recovery is a disaster recovery service that replicates VMs and workloads to a secondary region. It has no function related to storage tier management or cost optimization.

**D — Incorrect.** Blob versioning automatically maintains previous versions of a blob when it is modified or deleted. It is a data protection feature, not a tiering or cost optimization mechanism.

---

## Question 9

An Azure administrator opens the Azure Pricing Calculator and sees three pricing options for a virtual machine: Pay-as-you-go, 1-Year Reserved, and 3-Year Reserved. The administrator is planning a VM that will be used intermittently for testing over the next two months and then decommissioned. Which pricing option is most cost-effective?

A. 3-Year Reserved
B. 1-Year Reserved
C. Pay-as-you-go
D. Spot VM pricing

**Correct Answer: C**

### Distractor Analysis

**A — Incorrect.** A 3-year reservation commits the organization to paying for 36 months of usage. For a VM used only 2 months, the organization would pay for 34 months of unused reservation — a significantly worse outcome than pay-as-you-go.

**B — Incorrect.** A 1-year reservation similarly commits the organization to 12 months. For a 2-month workload, paying 10 months of unused reservation cost would far exceed the pay-as-you-go total.

**C — Correct.** Pay-as-you-go charges only for the hours the VM actually runs. For a short-term, intermittent workload with a defined end date, there is no benefit to committing to a reservation. PAYG provides the flexibility to stop paying when the VM is decommissioned.

**D — Incorrect.** Spot VMs are not among the three calculator options described in the question. Additionally, while spot pricing could reduce hourly cost, testing VMs typically require consistent availability and may not tolerate the eviction risk of spot instances.

---

## Question 10

A company is reviewing its Azure Cost Management + Billing data and wants to break down costs by department. Each department's resources are deployed in a shared subscription. What must have been configured on the resources in advance for this type of reporting to be possible?

A. Separate resource groups per department
B. Azure Policy assignments
C. Resource tags with a Department key
D. Management group hierarchy

**Correct Answer: C**

### Distractor Analysis

**A — Incorrect.** Separate resource groups per department would enable filtering by resource group, but the question specifies that resources are in a shared subscription and does not state they are in separate resource groups. Resource groups alone do not inherently represent department boundaries.

**B — Incorrect.** Azure Policy enforces rules on resource configurations but does not directly enable cost reporting breakdowns. Policies can require tags to be applied, but the tags themselves are what enable the cost reporting.

**C — Correct.** Resource tags with a consistent key such as "Department" allow Azure Cost Management to group and filter spending by department. Tags must be applied to resources before costs are incurred — retroactive tagging does not apply tags to historical spending data.

**D — Incorrect.** Management groups organize subscriptions for governance purposes and can be used to scope budgets, but they do not enable cost breakdowns by department within a shared subscription unless combined with tag-based filtering.

---

*Texas Wesleyan University — CIS-4331 Azure Cloud Computing — Module 14 Quiz*

---

### Question 11 (5 points)

A company is evaluating whether to migrate their on-premises data center to Azure. They want to see a financial comparison showing the total cost of ownership for their current on-premises environment versus the projected Azure cost over three years. Which Azure tool is designed specifically for this analysis?

- A) Azure Pricing Calculator
- B) Azure Cost Management + Billing
- C) Azure TCO Calculator
- D) Azure Advisor Cost recommendations

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* The Azure Total Cost of Ownership (TCO) Calculator is specifically designed to compare the cost of running workloads on-premises versus on Azure over a multi-year period. It accepts inputs for on-premises servers, storage, networking, and labor costs, then generates a report showing the estimated savings from migrating to Azure. The three-year comparison view is a core output of the TCO Calculator.
  - *Why A is incorrect:* The Azure Pricing Calculator estimates the cost of specific Azure resources and configurations. It is used to plan Azure spending, not to compare Azure costs against on-premises infrastructure. It does not accept on-premises infrastructure inputs for a comparative analysis.
  - *Why B is incorrect:* Azure Cost Management + Billing analyzes and reports on actual Azure spending that has already occurred. It is for managing and optimizing existing Azure costs, not for pre-migration comparison with on-premises costs.
  - *Why D is incorrect:* Azure Advisor Cost recommendations identify cost optimization opportunities within an existing Azure deployment (rightsizing VMs, identifying unused resources, recommending reservations). It requires existing Azure resources to analyze and does not perform on-premises vs. Azure comparisons.

---

### Question 12 (5 points)

A company purchases a 3-year Reserved Instance for a D4s_v3 virtual machine in East US. After 14 months, the workload this VM supports is migrated to a containerized environment and the VM is no longer needed. What happens to the reserved instance?

- A) The reservation is automatically cancelled and the company is refunded the remaining prepaid amount
- B) The reservation discount continues to apply to any other VM of the same size and region in the subscription, or can be exchanged or refunded subject to early termination fees
- C) The company must continue running the D4s_v3 VM until the reservation expires to avoid penalties
- D) Azure Advisor automatically reassigns the reservation to the next most expensive VM in the subscription

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Reserved Instances are a billing discount applied to matching compute usage — they are not tied to a specific VM instance. If the original VM is deleted, the reservation discount automatically applies to any other VM of the same SKU, region, and scope. The company can also exchange the reservation for a different size or region, or cancel it for a partial refund (subject to Microsoft's early termination policy, which allows up to $50,000 in refunds per 12-month rolling window).
  - *Why A is incorrect:* Reservations are not automatically cancelled when the original VM is deleted. They continue as a billing discount that applies to matching usage. Cancellation is a manual action and involves early termination fees if the reservation has remaining term.
  - *Why C is incorrect:* The company does not need to keep the original VM running. If no matching VM exists, the reservation goes unused (wasted cost), but there is no penalty for not using it beyond the opportunity cost. The correct response is to exchange it or find another use for the discount.
  - *Why D is incorrect:* Azure Advisor does not automatically reassign reservation discounts. Advisor may recommend purchasing reservations but does not manage or reassign existing reservations. Reservation management is done through the Azure portal under Cost Management + Billing.

---

### Question 13 (5 points)

An Azure Advisor report shows a recommendation to "Right-size or shutdown underutilized virtual machines." The report identifies a Standard_D8s_v3 VM (8 vCPUs) with an average CPU utilization of 3% over the past 30 days. What does this Advisor recommendation suggest, and under which Advisor pillar does it appear?

- A) Migrate the VM to a different Azure region for better performance; Performance pillar
- B) Downsize the VM to a smaller SKU or shut it down if unused; Cost pillar
- C) Enable Accelerated Networking to improve CPU efficiency; Reliability pillar
- D) Add a second VM for redundancy to prevent single points of failure; Operational Excellence pillar

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Advisor's Cost pillar analyzes VM utilization metrics over 30 days. When a VM shows consistently low CPU utilization (the threshold is typically below 5%), Advisor recommends downsizing to a smaller VM SKU (using fewer CPUs and less memory) or shutting down the VM if it is not needed. This reduces the hourly compute cost while maintaining the capability needed for the actual workload.
  - *Why A is incorrect:* Region migration does not address underutilization. Advisor does not recommend moving resources to different regions to improve CPU efficiency. Region recommendations (if any) appear in the Reliability or Performance pillars related to availability, not cost.
  - *Why C is incorrect:* Accelerated Networking improves network performance, not CPU efficiency. Accelerated Networking recommendations appear in the Performance pillar. It does not address the cost concern of an underutilized VM.
  - *Why D is incorrect:* Adding a second VM for redundancy would increase cost, not reduce it. Redundancy recommendations appear in the Reliability pillar, not the Cost pillar. Advisor's Cost recommendations focus on eliminating waste.

---

### Question 14 (5 points)

A company sets up an Azure Budget for their production subscription with a monthly limit of $10,000. They configure three alerts: at 50% ($5,000 forecast), at 90% ($9,000 actual), and at 100% ($10,000 actual). When the 100% actual threshold is reached, the linked Action Group sends an email. What else does Azure automatically do when the budget threshold is reached?

- A) Azure automatically suspends all running VMs in the subscription to prevent further charges
- B) Azure automatically moves all storage blobs to the Archive tier to reduce costs
- C) Nothing additional — the budget only sends the notification; it does not automatically restrict or stop resources
- D) Azure automatically removes Contributor access from all users in the subscription until the next billing period

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* Azure Budgets are monitoring and alerting tools, not enforcement mechanisms. When a budget threshold is reached, Azure sends the configured notification (email, webhook, Action Group). Azure does not automatically stop, restrict, or modify resources when a budget is exceeded. Additional automated responses (such as running an Azure Automation runbook to stop non-critical VMs) require the team to configure the Action Group to trigger automation — it does not happen automatically.
  - *Why A is incorrect:* Azure does not automatically suspend VMs when a budget is reached. Budget alerts are informational. Automatically stopping VMs would disrupt production workloads and is not Azure's default behavior. The team would need to explicitly configure automation in the Action Group to perform this action.
  - *Why B is incorrect:* Azure does not automatically move blobs to Archive tier when a budget threshold is reached. Lifecycle Management policies can move blobs based on age or access patterns, but these are separate configurations with no connection to budget thresholds.
  - *Why D is incorrect:* Azure does not remove RBAC access when a budget is exceeded. This would be highly disruptive and is not a default behavior. Budget alerts are notifications, not access control mechanisms.

---

### Question 15 (5 points)

A company's development team has 15 developers each with an Azure subscription for development and testing. The subscriptions use pay-as-you-go pricing. A manager learns that Azure offers a Dev/Test pricing option. What is the primary benefit and the key requirement for Dev/Test pricing?

- A) Dev/Test pricing provides free Azure services with no usage limits; requires an Azure free account
- B) Dev/Test pricing provides discounted rates on Windows VMs, SQL Database, and other services by eliminating Microsoft software license costs; requires an active Visual Studio subscription for each developer
- C) Dev/Test pricing provides a 50% flat discount on all Azure services; requires a minimum 12-month commitment
- D) Dev/Test pricing provides the same discount as 3-year Reserved Instances; requires an Enterprise Agreement

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Dev/Test pricing eliminates the cost of Windows Server and SQL Server licenses bundled into Azure VM pricing (similar to Azure Hybrid Benefit). This significantly reduces VM costs for development workloads. The key requirement is that each user accessing the Dev/Test subscription must have an active Visual Studio subscription (any tier). Dev/Test subscriptions are available under Visual Studio subscriptions, MSDN, and Enterprise Agreement Dev/Test offers.
  - *Why A is incorrect:* Dev/Test pricing is not free — it applies discounted rates. It is not available through the Azure free account. Free accounts have a separate set of free services and spending credits for 12 months.
  - *Why C is incorrect:* Dev/Test pricing is not a flat 50% discount on all services. The discount applies specifically to software license costs (Windows, SQL Server) embedded in VM pricing, and the savings vary by VM size and OS. There is no minimum 12-month commitment requirement.
  - *Why D is incorrect:* Dev/Test pricing is available through Visual Studio subscriptions, not only Enterprise Agreements. The savings are different from Reserved Instance pricing — they eliminate software license costs rather than providing a compute commitment discount. The two can actually be combined.

---

### Question 16 (5 points)

An organization wants to apply Azure Hybrid Benefit to reduce the cost of their Azure Virtual Machines. Which of the following is a prerequisite for using Azure Hybrid Benefit for Windows Server VMs?

- A) The VMs must be running in the East US region
- B) The organization must have Windows Server licenses covered by Software Assurance or qualifying Windows Server subscriptions
- C) The VMs must be a minimum of Standard_D4s_v3 size
- D) The organization must have an active Azure Reserved Instance for each VM

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Hybrid Benefit for Windows Server allows organizations to use their existing on-premises Windows Server licenses (covered by Software Assurance, or with qualifying Windows Server subscriptions) to run Windows Server VMs in Azure without paying the Windows Server license component of the VM price. This can reduce Windows Server VM costs by up to 40%. Software Assurance or the qualifying subscription is the core prerequisite.
  - *Why A is incorrect:* Azure Hybrid Benefit is available in all Azure regions, not only East US. There is no regional restriction on applying Hybrid Benefit.
  - *Why C is incorrect:* Azure Hybrid Benefit applies to any VM size that can run Windows Server. There is no minimum size requirement. The benefit can be applied to small B-series development VMs as well as large M-series production VMs.
  - *Why D is incorrect:* Azure Hybrid Benefit and Reserved Instances are independent discounts that can be combined (stacked) for greater savings. A Reserved Instance is not required to use Hybrid Benefit; they are separate purchasing mechanisms.

---

### Question 17 (5 points)

An organization uses Azure Cost Management to analyze spending. They notice that $8,000 of their monthly $25,000 Azure bill is categorized under an unknown cost center because resources were deployed without tags. Going forward, they want to ensure every new resource has a "CostCenter" tag. Which combination of Azure services enforces this going forward AND improves visibility into the untagged existing costs?

- A) Azure Advisor (Cost pillar) to identify untagged resources; Azure Budgets to block untagged spending
- B) Azure Policy with the "Require a tag on resources" Deny effect for new resources; Azure Cost Management tag inheritance or manual tagging for existing resources
- C) Azure Blueprints to redeploy all existing resources with tags; Azure Monitor alerts to detect new resources without tags
- D) Azure Security Center to flag untagged resources; resource locks to prevent modification of tagged resources

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Policy with the "Require a tag on resources" definition using the Deny effect blocks any new resource creation without the required tag, enforcing compliance going forward. For existing untagged resources, Azure Cost Management supports tag inheritance (subscription and resource group tags can be inherited by child resources for cost reporting), and the team can manually apply tags to existing resources or use the Modify policy effect with a remediation task to add tags automatically.
  - *Why A is incorrect:* Azure Advisor identifies optimization opportunities but does not enforce governance. Azure Budgets alert when spending thresholds are reached but cannot block individual resource deployments based on missing tags. Neither enforces tag requirements at resource creation time.
  - *Why C is incorrect:* Azure Blueprints is deprecated and would not redeploy existing resources. Azure Monitor cannot block resource creation; it can only alert after resources are created. This combination does not enforce tag requirements at deployment time.
  - *Why D is incorrect:* Azure Security Center (now Defender for Cloud) monitors security posture, not tag compliance. Resource locks prevent deletion or modification of resources, not their creation. Locks on tagged resources would actually prevent the team from later modifying those resources. This is the wrong combination of tools.

---

### Question 18 (5 points)

A company has been running the same set of Azure VMs for 18 months at pay-as-you-go rates. Azure Advisor's Cost pillar shows a recommendation to purchase 1-year Reserved Instances for these VMs with an estimated savings of 38%. The team is hesitant because they worry the workload might change. What is the primary risk of purchasing Reserved Instances, and what flexibility options does Azure provide to mitigate this risk?

- A) The primary risk is VM performance degradation; Azure provides performance guarantees with reservations
- B) The primary risk is committing to pay for capacity that may go unused if workloads change; Azure provides exchange and cancellation options (subject to limits) to mitigate this
- C) The primary risk is regional availability; Azure guarantees capacity in the selected region for reserved instances
- D) The primary risk is losing pay-as-you-go pricing benefits; Azure provides a hybrid billing mode that applies both discounts simultaneously

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The core risk of a Reserved Instance is the commitment — paying for capacity whether or not it is used. If a workload is decommissioned, migrated, or significantly reduced in scale, the reservation cost continues. Azure mitigates this through: (1) reservation exchanges — swap a reservation for a different size or region; (2) reservation cancellation — return a reservation for a prorated refund up to the $50,000 annual limit; and (3) reservation scope flexibility — the discount applies to any matching VM in the scope (subscription or shared), not just the original VM.
  - *Why A is incorrect:* Reserved Instances are a billing construct, not a compute performance tier. Reservations provide the same VM performance as pay-as-you-go instances of the same SKU. There is no performance risk or guarantee difference.
  - *Why C is incorrect:* Reserved Instances do provide a capacity reservation benefit (ensuring capacity in the specified region), but this is a benefit, not a risk. Regional availability risk is typically mitigated by reservations, not introduced by them.
  - *Why D is incorrect:* "Hybrid billing mode" is not an Azure concept. Pay-as-you-go and Reserved Instance discounts are mutually exclusive for the same usage — the reserved instance discount replaces the pay-as-you-go rate (not combined with it). Azure Hybrid Benefit (a different program) can be stacked on top of reservations.

---

### Question 19 (5 points)

An organization's Azure Cost Management analysis shows that their Azure SQL Database is the largest cost item at $2,400 per month, followed by Azure Blob Storage at $800 per month and Azure Virtual Machines at $600 per month. The CFO asks whether the database cost can be reduced. Which Azure Advisor pillar and what specific recommendation type would most directly address potential SQL Database overprovisioning?

- A) Security pillar — recommendation to enable Advanced Threat Protection on the SQL Database
- B) Cost pillar — recommendation to rightsize the database to a lower service tier or DTU count based on actual utilization
- C) Reliability pillar — recommendation to enable geo-replication for the SQL Database
- D) Performance pillar — recommendation to add more DTUs to improve query response time

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Advisor's Cost pillar analyzes Azure SQL Database usage metrics and compares them to the provisioned tier. If the database is consistently using only a fraction of its provisioned DTUs or vCores, Advisor recommends downgrading to a lower service tier or compute size that matches actual utilization. This is the direct cost reduction recommendation for an overprovisioned SQL Database.
  - *Why A is incorrect:* Advanced Threat Protection is a security feature that increases cost by adding the Defender for SQL plan. The Security pillar recommends enabling security features, not reducing costs. This recommendation would increase the SQL Database bill.
  - *Why C is incorrect:* Geo-replication adds a secondary database in another region, which doubles the SQL Database cost. This is a Reliability recommendation that increases cost for higher availability. It does not reduce the $2,400 monthly cost.
  - *Why D is incorrect:* Adding more DTUs increases the SQL Database tier, which increases cost. Performance pillar recommendations address response time and throughput, not cost reduction. The CFO's request is for cost reduction, making the Cost pillar the correct source.

---

### Question 20 (5 points)

A startup is building their first Azure environment and wants to estimate costs before deploying anything. They have identified specific services they need: 2 Standard_D2s_v3 VMs running Linux 24/7, 500 GB Azure SQL Database (General Purpose, 4 vCores), and 10 TB Azure Blob Storage (Hot tier) in East US. Which tool do they use to estimate the monthly cost, and what information do they need to provide to get an accurate estimate?

- A) Azure TCO Calculator; they provide their current on-premises server specifications and Azure automatically calculates equivalent Azure costs
- B) Azure Pricing Calculator; they select each service, configure the SKU, region, and usage quantities, then read the monthly estimate from the calculator output
- C) Azure Cost Management + Billing; they enable cost forecasting which projects future spending based on current resource configurations
- D) Azure Advisor; they run a cost analysis scan which estimates the cost of the described architecture before deployment

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The Azure Pricing Calculator is the tool for estimating Azure costs before any resources are deployed. The team selects each service from the catalog (VMs, SQL Database, Blob Storage), configures the specific SKU (Standard_D2s_v3, 2 instances), operating hours (730 hours/month for 24/7), region (East US), and quantities (10 TB storage, 500 GB database). The calculator produces a monthly cost estimate that can be saved, shared, and exported to Excel.
  - *Why A is incorrect:* The TCO Calculator is for comparing on-premises vs. Azure costs. The startup is building their first Azure environment and has no on-premises infrastructure to compare against. The TCO Calculator requires on-premises server specifications as input and is not designed for estimating the cost of a specific Azure architecture from scratch.
  - *Why C is incorrect:* Azure Cost Management + Billing requires existing Azure resources generating actual cost data before it can forecast future spending. The startup has not deployed anything yet, so Cost Management has no data to analyze or forecast from.
  - *Why D is incorrect:* Azure Advisor requires deployed Azure resources to analyze and make recommendations. It cannot estimate costs for a hypothetical architecture that has not been deployed. Advisor makes recommendations about existing resources, not pre-deployment cost estimates.

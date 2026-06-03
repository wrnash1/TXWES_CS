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

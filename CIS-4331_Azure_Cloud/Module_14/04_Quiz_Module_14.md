# Quiz: Module 14 - Azure Cost Management

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What purchase option allows you to reduce VM costs by up to 72% by committing to a 1-year or 3-year term?

* A) Pay-as-you-go
* B) Spot Instances
* C) Azure Reservations
* D) Azure Hybrid Benefit
* **Correct Answer:** C) Reservations provide significant discounts in exchange for a committed usage duration.
* **Distractor Analysis:**
  * *Why correct:* Azure Reservations commit to a resource type in a specific region for 1 or 3 years, yielding up to 72% savings over pay-as-you-go.
  * *Why B is incorrect:* Spot Instances offer deeper discounts (up to 90%) but can be evicted with 30-second notice — not suitable for workloads requiring guaranteed availability.

---

**Question 2**
Which of the following most accurately describes the **Azure TCO (Total Cost of Ownership) Calculator**?

* A) A free web tool that compares the total cost of running workloads on-premises versus in Azure over a multi-year period, accounting for hardware, software, facilities, and IT labor costs to build a business case for cloud migration.
* B) A web tool that estimates the monthly Azure bill for specific services based on configured specifications such as VM size, region, and storage type.
* C) A dashboard within the Azure portal that shows current and historical spending by resource, service, and subscription with budget alerts.
* D) A cost optimization feature that automatically shuts down idle Azure VMs outside of business hours to reduce compute spending.
* **Correct Answer:** A) The TCO Calculator compares multi-year on-premises total costs versus Azure costs to justify cloud migration with financial analysis.
* **Distractor Analysis:**
  * *Why A is correct:* The TCO Calculator's purpose is migration justification — it models total cost of ownership including hidden on-premises costs like facilities and IT labor.
  * *Why B is incorrect:* That describes the Azure Pricing Calculator, which estimates costs for specific Azure services before deployment.
  * *Why C is incorrect:* That describes Azure Cost Management + Billing, which monitors and analyzes actual spending after deployment.
  * *Why D is incorrect:* That describes Azure Automation or VM auto-shutdown features — not the TCO Calculator.

---

**Question 3**
A finance manager created an Azure Cost Management budget set at $5,000 per month for a subscription. The current month's spending just reached $5,001. What happens automatically?

* A) All Azure VMs in the subscription are automatically stopped to prevent further charges.
* B) The subscription is locked and no new resources can be deployed until the next billing cycle.
* C) A notification email is sent to the configured alert recipients, but Azure resources continue running.
* D) Azure automatically moves all resources to lower-cost service tiers to reduce spending.
* **Correct Answer:** C) Budget alerts in Azure Cost Management send notifications when thresholds are reached, but do not automatically stop or modify Azure resources.
* **Distractor Analysis:**
  * *Why C is correct:* Budgets are notification tools — they alert you when spending reaches defined thresholds but take no automatic action on resources.
  * *Why A is incorrect:* Budgets do not stop VMs — you must configure separate automation (e.g., Azure Automation runbook triggered by the budget alert) to take action.
  * *Why B is incorrect:* Exceeding a budget does not lock the subscription or prevent new deployments.
  * *Why D is incorrect:* Azure does not automatically downgrade service tiers based on budget thresholds.

---

**Question 4**
A company wants to estimate the cost of migrating its entire on-premises server infrastructure to Azure before making the migration decision. Which Azure tool is most appropriate?

* A) Azure Pricing Calculator
* B) Azure Cost Management + Billing
* C) Azure TCO Calculator
* D) Azure Advisor cost recommendations
* **Correct Answer:** C) The Azure TCO Calculator models the full cost comparison between on-premises and Azure over multiple years, accounting for all infrastructure and operational costs.
* **Distractor Analysis:**
  * *Why C is correct:* The TCO Calculator is designed specifically for pre-migration cost analysis — it compares on-premises TCO (hardware, power, cooling, labor) against projected Azure costs.
  * *Why A is incorrect:* The Pricing Calculator estimates Azure service costs but does not model current on-premises costs for comparison.
  * *Why B is incorrect:* Cost Management shows actual Azure spending — it cannot model on-premises costs since those resources are not yet in Azure.
  * *Why D is incorrect:* Azure Advisor cost recommendations optimize existing Azure spending — the company's workloads are not yet in Azure.

---

**Question 5**
Which of the following factors does NOT directly affect the cost of an Azure Virtual Machine?

* A) The Azure region where the VM is deployed
* B) The VM size (number of vCPUs and RAM)
* C) The Azure Resource Group the VM belongs to
* D) Whether the VM uses pay-as-you-go or a Reserved Instance commitment
* **Correct Answer:** C) Resource Groups are logical management containers — they do not affect the price of resources within them.
* **Distractor Analysis:**
  * *Why C is correct:* Resource Groups are organizational containers with no pricing implications. Moving a VM to a different Resource Group does not change its cost.
  * *Why A is incorrect:* Region directly affects VM pricing — the same VM size costs different amounts in different Azure regions.
  * *Why B is incorrect:* VM size is a primary cost driver — more vCPUs and RAM means higher hourly cost.
  * *Why D is incorrect:* Pricing commitment model is a major cost factor — Reserved Instances can reduce the same VM's cost by up to 72% compared to pay-as-you-go.

# Reading Guide: Module 14 - Azure Cost Management

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 14 - Azure Cost Management**! This module covers Azure's pricing model and cost management tools as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Understanding how Azure charges for services and how to estimate, monitor, and optimize spending is one of the highest-weighted topic areas in AZ-900.

You will learn how the Azure Pricing Calculator estimates costs before deployment, how the Total Cost of Ownership (TCO) Calculator compares on-premises versus Azure costs, how Azure Cost Management monitors and controls spending after deployment, and which factors — region, tier, bandwidth, and commitment — most affect your Azure bill. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Azure Pricing Calculator**: A free, interactive web tool at [azure.microsoft.com/en-us/pricing/calculator/](https://azure.microsoft.com/en-us/pricing/calculator/) that allows you to estimate the monthly cost of Azure services before you deploy them. You configure service specifications (VM size, region, storage type, hours) and the calculator provides an estimated price. Use it during planning phases to compare configuration options.

* **TCO Calculator (Total Cost of Ownership)**: A free tool at [azure.microsoft.com/en-us/pricing/tco/calculator/](https://azure.microsoft.com/en-us/pricing/tco/calculator/) that compares the cost of running workloads on-premises versus in Azure over a 3-to-5 year period. It factors in hardware, software, facilities, IT labor, and other operational costs. AZ-900 tests that the TCO Calculator is used to justify cloud migration by demonstrating cost savings.

* **Cost Alerts and Budgets**: Azure Cost Management allows you to set spending budgets at the Subscription or Resource Group scope. When spending reaches defined thresholds (e.g., 80% and 100% of budget), Cost Management sends email alerts to designated recipients. Budgets do not automatically stop spending — they only notify.

* **Factors Affecting Azure Cost**: Key cost factors include: the Azure region (prices vary by region); resource type and tier (e.g., Premium SSD costs more than Standard HDD); bandwidth (inbound data to Azure is typically free; outbound data transfer is charged); licensing (Azure Hybrid Benefit uses existing Windows Server or SQL Server licenses to reduce costs); and reservation commitment (1-year or 3-year Reserved Instances reduce VM costs up to 72%).

* **Azure Reservations (Reserved Instances)**: A commitment to use a specific Azure resource type in a specific region for a 1-year or 3-year term, in exchange for discounts of up to 72% compared to pay-as-you-go pricing. Reservations are prepaid or paid monthly. They are the correct AZ-900 answer for reducing costs on predictable, steady-state workloads.

---

### 2. Certification Exam Tips

* **Pricing Calculator vs. TCO Calculator**: AZ-900 tests which tool is appropriate for which scenario. Pricing Calculator = estimate cost of specific Azure services before deployment. TCO Calculator = compare on-premises total cost vs. Azure over multiple years to build a business case for migration. Know both tools and their distinct purposes.
* **Budgets do not stop spending**: A common AZ-900 trap is assuming that creating a budget automatically stops Azure resource consumption when the limit is reached. Budgets only send notifications — you must configure automation (e.g., Azure Automation runbook) to act on budget alerts if you want automatic shutdown.
* **Outbound data transfer costs**: Data going INTO Azure (ingress) is free. Data going OUT of Azure (egress) incurs charges. Transferring data between regions within Azure also incurs egress charges. This is a common exam question about what drives unexpected cost increases.
* **Spot VMs vs. Reservations**: Spot VMs offer the deepest discounts (up to 90%) but can be evicted with 30-second notice when Azure needs the capacity. Reservations offer up to 72% discount with guaranteed capacity. AZ-900 tests that Spot VMs are not suitable for workloads requiring reliability.
* **Study Resource**: The Microsoft Learn cost management module covers the Pricing Calculator, TCO Calculator, and Cost Management with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers Azure pricing, the Pricing Calculator, TCO Calculator, and Cost Management tools. Access it at [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* **Required Video:** This free freeCodeCamp course covers Azure cost management for AZ-900 — watch the pricing and cost management section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Configure a cost budget and warning alert**: In Azure Cost Management + Billing, create a monthly budget for a Subscription or Resource Group. Set alert thresholds at 80% and 100% of the budget and configure an email notification recipient.
* **Compare on-demand vs. reserved instance pricing**: Use the [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/) to estimate the monthly cost of a D2s_v3 VM on pay-as-you-go. Then switch to 1-year Reserved pricing and note the percentage savings.
* **Check billing reports**: In Azure Cost Management, review the cost breakdown by resource type for the past 30 days. Identify the top three cost-generating services and explore which region and resource tier is driving the most spending.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Azure cost management unit in [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* [ ] Watch the pricing section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for budget configuration and pricing calculator comparison.
* [ ] Proceed to the weekly hands-on lab activity.

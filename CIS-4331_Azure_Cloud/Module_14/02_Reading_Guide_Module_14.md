# Reading Guide: Module 14 — Azure Cost Management and Pricing

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Overview

Cloud computing shifts IT spending from capital expenditure — buying servers and hardware upfront — to operational expenditure — paying for services as you consume them. This model offers tremendous flexibility but introduces a new discipline: cloud financial management, commonly called FinOps. Azure provides a suite of tools to estimate, monitor, and optimize cloud spending. Mastery of these tools is tested in the Management and Governance domain of the AZ-900 exam.

---

## Section 1 — Understanding Azure Pricing Models

### 1.1 Pay-As-You-Go

Pay-as-you-go (PAYG) is the default Azure pricing model. You are billed for what you consume with no upfront commitment and no cancellation fees. PAYG rates are the highest per-unit rates Azure offers because they include full flexibility — you can stop using a resource at any moment.

PAYG is appropriate for unpredictable workloads, new deployments where usage patterns are unknown, development and testing, and short-term projects.

### 1.2 Consumption-Based vs Fixed Pricing

Some Azure services follow a consumption-based model — you pay per request, per gigabyte processed, or per execution. Azure Functions, Azure Logic Apps, and Azure Cosmos DB serverless mode follow this pattern. Other services follow a fixed model — you pay a flat rate per hour for a provisioned resource regardless of actual utilization. Virtual machines are the primary example.

Understanding which model applies to a service helps you predict costs and choose the right tier.

### 1.3 Free Services and Free Tier

Azure offers several categories of free resources.

**Always-free services** include Azure Active Directory Free, Azure DevOps (5 users), Azure App Service F1 tier, and select monitoring features.

**Free trial** provides $200 in credit for the first 30 days for new accounts, plus 12 months of popular services at free quantities.

**Free quantities within paid services** — Azure Functions includes 1 million free executions per month even on paid accounts.

Knowing the difference between always-free and trial-free is important for exam questions about cost planning.

---

## Section 2 — Azure Pricing Calculator

### 2.1 Purpose and Access

The Azure Pricing Calculator at azure.microsoft.com/en-us/pricing/calculator allows anyone to estimate the monthly cost of Azure services before deployment. No Azure account is required. The tool is used by architects, project managers, and finance teams to produce cost proposals.

### 2.2 Building an Estimate

An estimate is built by adding service tiles to a workspace. Each tile represents one Azure service configured with specific parameters:

- **Virtual Machines** — Region, OS, instance size, hours per month, storage, software
- **Azure SQL Database** — Service tier, compute tier, storage, backup retention
- **Azure Blob Storage** — Redundancy option, storage capacity, operations, data retrieval
- **Azure Kubernetes Service** — Node pool size, node count, uptime hours

Multiple services can be added to a single estimate to produce a total monthly projection.

### 2.3 Pricing Options in the Calculator

For compute-intensive services the calculator exposes multiple pricing options.

| Option | Description |
|---|---|
| Pay-as-you-go | No commitment, highest per-hour rate |
| 1-Year Reserved | 12-month commitment, typically 20–40% savings |
| 3-Year Reserved | 36-month commitment, up to 66% savings |
| Spot | Interruptible, up to 90% off PAYG |
| Dev/Test | Reduced rate, no Windows license, no SLA |

### 2.4 Azure Hybrid Benefit in the Calculator

The Hybrid Benefit toggle applies when your organization has Windows Server or SQL Server licenses with active Software Assurance. Enabling it removes the Windows or SQL license cost from the hourly rate. For a standard D-series Windows VM the savings are approximately 40–49%.

### 2.5 Saving, Exporting, and Sharing

Estimates can be saved to a Microsoft account for later retrieval, exported to Microsoft Excel (.xlsx) for business proposals, or shared via a unique URL for collaboration.

### 2.6 Limitations

The Pricing Calculator provides estimates based on list prices and configured parameters. It does not account for actual usage patterns, burst behavior, or regional price fluctuations. Use it as a planning tool, not a guarantee.

---

## Section 3 — Total Cost of Ownership Calculator

### 3.1 Purpose

The TCO Calculator at azure.microsoft.com/en-us/pricing/tco/calculator is designed for organizations evaluating a migration from on-premises infrastructure to Azure. It quantifies the full cost of running on-premises — including hardware, software, facilities, and labor — and compares it to the projected Azure cost over three years.

### 3.2 Three-Step Process

**Step 1 — Define Workloads**

Enter the current on-premises environment: Windows and Linux servers (number, type, cores, RAM), databases (SQL Server, Oracle, MySQL), storage (primary and backup volumes), and networking (outbound bandwidth).

**Step 2 — Adjust Assumptions**

Customize the financial assumptions the calculator uses: electricity cost per kWh, IT labor cost per hour, hardware amortization, software licensing costs, storage administration costs, virtualization host ratio, and data center overhead percentage (Power Usage Effectiveness).

These assumptions are pre-populated with industry averages but should be adjusted to reflect your organization's actual costs for an accurate comparison.

**Step 3 — View Report**

The report produces a three-year cost comparison showing total on-premises cost versus total Azure cost, dollar savings, percentage savings, and a breakdown by category: compute, storage, networking, IT labor, and facilities.

### 3.3 Interpreting TCO Results

The TCO Calculator consistently shows savings for most organizations because it captures hidden on-premises costs that IT teams rarely attribute to individual workloads — floor space, cooling, power redundancy, and staff time spent on hardware maintenance. These costs disappear in Azure.

### 3.4 TCO vs Pricing Calculator — Exam Distinction

| Tool | Question It Answers | Primary Audience |
|---|---|---|
| Pricing Calculator | What will Azure resources cost? | Architects, DevOps, Finance |
| TCO Calculator | Is migrating to Azure cheaper than staying on-premises? | IT Leadership, CFO, CIO |

---

## Section 4 — Azure Cost Management plus Billing

### 4.1 Overview

Azure Cost Management plus Billing is built into the Azure portal and is the primary tool for monitoring and managing actual cloud spend after resources are deployed. It is available at no additional cost to Azure subscribers.

Access it from the Azure portal by searching "Cost Management + Billing" or navigating to the service directly.

### 4.2 Cost Analysis

Cost Analysis provides interactive visualizations of your spending. Key options include view by service, resource group, location, subscription, or tag; time range options of current month, last month, last 3 months, or custom; granularity of daily, monthly, or cumulative; and visualization types of area chart, bar chart, table, or donut chart.

The table view lists individual resources with accumulated costs, enabling rapid identification of the most expensive resources.

### 4.3 The Role of Tags in Cost Analysis

Tags are key-value metadata pairs attached to Azure resources. When applied consistently, tags enable cost reporting by business dimension:

- `Department: Finance` — show all Finance department spend
- `Project: ProjectAlpha` — show all spend attributed to a project
- `Environment: Production` vs `Environment: Dev` — compare environments

Tags must be applied during resource creation or added afterward. Cost Management can filter and group costs by any tag defined in your environment.

### 4.4 Invoices and Payment

The Billing section displays monthly invoices in PDF format, usage detail files in CSV format for per-resource breakdown, payment methods management, and billing period history. Enterprise Agreement customers see additional views for commitment drawdown and department-level billing.

### 4.5 Cost Allocation

Cost allocation rules distribute shared resource costs — such as a shared Virtual Network or Azure Monitor workspace — across multiple subscriptions or resource groups using percentage or proportional rules. This supports internal chargeback and showback models.

---

## Section 5 — Budgets and Alerts

### 5.1 Budget Scope and Configuration

Budgets can be set at four scopes: Management Group (spans multiple subscriptions), Subscription (entire subscription), Resource Group (subset of a subscription), and individual Resource (limited support).

Each budget specifies a name, reset period (Monthly, Quarterly, or Annually), budget amount in USD, and optional start and expiration dates.

### 5.2 Alert Thresholds

Each budget can have up to five alert conditions. Each condition specifies a threshold type of Actual (money already spent) or Forecasted (projected to be spent by end of period), a threshold percentage, alert recipient email addresses, and an optional Action Group for automated response.

A common pattern is Actual 80%, Actual 100%, and Forecasted 110%.

### 5.3 Action Groups and Automation

Azure Action Groups define a set of notification and automation actions triggered by an alert. When linked to a budget alert, an Action Group can send email or SMS to on-call teams, call a webhook to trigger an external system, run an Azure Automation runbook, or trigger an Azure Logic App.

This enables budget-driven automation — for example, a Logic App that sends a Teams message or an Automation runbook that deallocates non-critical VMs when spend reaches a threshold.

### 5.4 Anomaly Detection

Cost anomaly alerts use machine learning to detect unusual spending patterns. A sudden spike in a service that normally has steady costs triggers an alert within 24 hours of the detected anomaly, sent by email.

---

## Section 6 — Cost Optimization Strategies

### 6.1 Right-Sizing

Right-sizing aligns the deployed resource size to actual workload requirements. Over-provisioning is the most common waste pattern. Steps to right-size include collecting CPU and memory utilization data over 7–30 days, identifying resources with average CPU below 5–10%, evaluating the next smaller SKU, testing performance at the smaller size, and resizing in production during a maintenance window.

Azure Advisor automates the analysis and produces actionable recommendations with estimated savings.

### 6.2 Reserved Instances

Azure Reservations provide discounted pricing in exchange for a one-year or three-year commitment.

Key facts:

- **Scope:** Single subscription or shared across a billing account
- **Flexibility:** Many reservations are instance-size flexible within a VM family
- **Payment:** Pay upfront (maximum discount) or monthly
- **Cancellation:** You can cancel for a fee and receive a prorated refund

Reservations apply to Virtual Machines, Azure SQL Database, Azure Cosmos DB, Azure Synapse Analytics, Azure Blob Storage, and more.

### 6.3 Spot Virtual Machines

Spot VMs access Azure's unused capacity at up to 90% discount. Key characteristics:

- **Eviction:** Azure can evict spot VMs with a 30-second notice when capacity is needed
- **Eviction policy:** Delete (VM deleted on eviction) or Deallocate (VM stopped, disk preserved)
- **Max price:** You can set a maximum price; if the spot price exceeds your max, the VM is evicted
- **Availability:** Not available in all VM sizes or regions at all times

Best use cases: batch processing, large-scale rendering, machine learning training with checkpointing, non-time-critical data processing.

### 6.4 Azure Hybrid Benefit

Azure Hybrid Benefit allows organizations with qualifying licenses to bring them to Azure. Windows Server licenses (with Software Assurance) eliminate the Windows OS cost in VM hourly rates. SQL Server licenses reduce Azure SQL costs. Qualifying Red Hat Enterprise Linux or SUSE subscriptions can also be ported. Savings range from 30% to 49% depending on license type and tier.

### 6.5 Dev/Test Pricing

Organizations with Visual Studio subscriptions or an Enterprise Agreement can access Dev/Test pricing for non-production environments: no Windows Server license charge on Windows VMs, discounted rates on selected services, and no SLA. Workloads must be for development, testing, or demonstration only.

### 6.6 Auto-Shutdown

Auto-shutdown is configured per VM under Operations > Auto-shutdown. Specify a daily shutdown time and an optional email notification. When triggered, the VM is deallocated — compute billing stops while disk billing continues.

For developer VMs that only need to be active during business hours (8 AM–6 PM), auto-shutdown saves approximately 58% of compute costs.

### 6.7 Storage Lifecycle Management

Lifecycle Management policies automatically move blobs through storage tiers based on age or last-accessed date. Hot tier is for frequently accessed data. Cool tier is for infrequently accessed data. Archive tier is for rarely accessed data with the lowest storage cost and highest retrieval latency. Moving aging data from Hot to Cool after 30 days and to Archive after 90 days can reduce storage costs by 60–80% for large data workloads.

---

## Section 7 — Azure Advisor

### 7.1 Overview

Azure Advisor is an intelligent recommendation service that analyzes your Azure usage and configurations and makes personalized recommendations across five pillars: Cost, Security, Reliability, Operational Excellence, and Performance.

### 7.2 Accessing Advisor

Navigate to Azure Advisor from the Azure portal search bar or the portal home page. The dashboard shows a score for each pillar (0–100) and a prioritized list of recommendations with estimated impact.

### 7.3 Cost Recommendations

Common Advisor cost recommendations include resizing or shutting down underutilized VMs (CPU below 5% average), buying reserved instances for VMs that have been running continuously, deleting unattached managed disks sitting idle, reducing ExpressRoute circuit sizes with low utilization, and moving cold blob storage to Cool or Archive tier.

### 7.4 Advisor Scores and Impact

Each recommendation is rated High, Medium, or Low impact. High-impact recommendations typically have estimated savings exceeding $100/month. The Advisor Cost Score increases as you implement recommendations.

### 7.5 Dismissing and Postponing Recommendations

If a recommendation is not applicable — for example, a VM is intentionally idle as a standby — you can dismiss it permanently or postpone it for 14 or 90 days. Dismissed recommendations are tracked and can be restored.

---

## Key Terms Glossary

**Azure Pricing Calculator** — Web tool for estimating Azure resource costs before deployment.

**TCO Calculator** — Tool comparing on-premises total cost to Azure total cost over three years.

**Azure Cost Management + Billing** — Portal service for monitoring, analyzing, and optimizing actual Azure spending.

**Budget** — A spending threshold in Cost Management that triggers alerts when approached or exceeded.

**Reserved Instance / Azure Reservation** — A 1-year or 3-year pricing commitment that reduces Azure resource costs.

**Spot VM** — A VM using interruptible Azure surplus capacity at up to 90% discount.

**Azure Hybrid Benefit** — License portability allowing organizations to bring Windows Server or SQL Server licenses to Azure.

**Right-Sizing** — Adjusting deployed resource capacity to match actual workload requirements.

**Azure Advisor** — Personalized recommendation engine covering cost, security, reliability, performance, and operational excellence.

**Cost Allocation** — Distribution of shared Azure costs across business units for chargeback or showback.

**Dev/Test Pricing** — Reduced Azure pricing for non-production workloads under qualifying subscription types.

---

## AZ-900 Exam Key Distinctions

- Pricing Calculator estimates future costs. TCO Calculator compares on-premises to cloud costs.
- Reserved instances require a 1-year or 3-year commitment. Spot VMs can be evicted anytime.
- Azure Advisor covers 5 pillars: Cost, Security, Reliability, Performance, Operational Excellence.
- Budget alerts can trigger Action Groups for automated responses.
- Azure Hybrid Benefit requires Software Assurance (Windows/SQL) or qualifying Linux subscriptions.
- Cost Management + Billing core features are free; multi-cloud capabilities require the premium tier.

---

## Review Questions

1. What is the primary difference between the Azure Pricing Calculator and the TCO Calculator?
2. Name three types of information you must provide in the TCO Calculator's "Define Workloads" step.
3. What is a spot VM and what type of workload is it appropriate for?
4. How does Azure Hybrid Benefit reduce VM costs?
5. What are the five pillars of Azure Advisor?
6. How do tags support cost management and reporting in Azure?
7. What happens when a budget's 100% threshold is reached and an Action Group is configured?
8. What is the difference between a one-year and three-year Azure reservation?
9. Name two blob storage lifecycle management tiers and when each is appropriate.
10. Why might an organization use Dev/Test pricing, and what is the trade-off?

---

*Texas Wesleyan University — CIS-4331 Azure Cloud Computing — Module 14 Reading Guide*

---

## 9. Supplemental Resources

1. Azure Pricing Calculator — interactive tool for estimating Azure service costs before deployment: https://azure.microsoft.com/en-us/pricing/calculator/

2. Azure Cost Management + Billing documentation — analyzing, monitoring, and optimizing Azure spending with budgets, cost analysis, and recommendations: https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview

3. Azure Reserved Virtual Machine Instances documentation — understanding reservation discounts, scope, exchange, and cancellation policies: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/save-compute-costs-reservations

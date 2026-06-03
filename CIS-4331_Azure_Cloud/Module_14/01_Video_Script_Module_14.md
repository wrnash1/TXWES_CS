# Video Script: Module 14 — Azure Cost Management and Pricing

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Production Notes

**Estimated Runtime:** 28–32 minutes
**Slide Deck:** Module_14_Slides.pptx
**Visual Aids:** Pricing Calculator screenshot, TCO Calculator walkthrough, Cost Management dashboard, budget alert workflow

---

## SEGMENT 1 — Introduction and Why Cost Management Matters (3 minutes)

[SLIDE: Module 14 Title Card]

Welcome back to CIS-4331. I'm Professor Nash, and this is Module 14: Azure Cost Management and Pricing.

We have spent the last thirteen modules building real technical skills — deploying virtual machines, configuring networks, setting up databases, and designing resilient architectures. All of that work lives inside a bill. Every resource you deploy costs money, and one of the most critical skills for any cloud professional is understanding where that money goes and how to control it.

[SLIDE: "The Cloud Bill Surprise"]

Here is a scenario that happens more often than people admit. A developer spins up a GPU-backed virtual machine to run a machine learning experiment. They finish for the day and forget to deallocate the machine. Four days later the monthly bill arrives, and leadership is asking questions. That single forgotten VM can cost hundreds of dollars. At enterprise scale, unmanaged cloud spend runs into millions.

The AZ-900 exam tests your understanding of Azure's cost tools in the Management and Governance domain, which represents thirty to thirty-five percent of your exam score. This is not a topic you can afford to skip.

[SLIDE: Module Learning Objectives]

By the end of this module you will be able to use the Azure Pricing Calculator to estimate resource costs before deployment, use the Total Cost of Ownership Calculator to compare on-premises versus cloud costs, navigate Azure Cost Management plus Billing to monitor and analyze actual spend, configure budget alerts that fire before you exceed spending thresholds, and identify cost optimization strategies including reserved instances, spot VMs, and Azure Advisor recommendations.

Let's get started.

---

## SEGMENT 2 — Azure Pricing Calculator (6 minutes)

[SLIDE: Azure Pricing Calculator Overview]

The Azure Pricing Calculator is a free web tool available at azure.microsoft.com/en-us/pricing/calculator. You do not need an Azure subscription to use it. You can access it right now in your browser.

The calculator lets you build a hypothetical Azure configuration and see the estimated monthly cost before you deploy anything. Think of it as a shopping cart for cloud resources.

[SLIDE: Calculator Interface Walkthrough]

When you open the calculator you see a product catalog on the left. You click a service — Virtual Machines, for example — and it adds a tile to your estimate on the right. Inside that tile you configure the specifics: region, operating system, VM size, number of hours per month.

Let me walk through a concrete example. Suppose you need a Windows Server virtual machine running in East US, a D2s v3 size which is two vCPUs and eight gigabytes of RAM, running twenty-four hours a day for thirty days. The calculator shows you the compute cost, then lets you add managed disk storage, outbound data transfer, and a public IP address. Each component adds to the total.

[SLIDE: Key Calculator Features]

There are three pricing options the calculator exposes for compute. Pay-as-you-go is the default — you pay per hour with no commitment. One-year reserved shows the price if you commit to that VM size for twelve months. Three-year reserved shows the deepest discount.

You can also toggle Azure Hybrid Benefit on or off. If your organization has existing Windows Server or SQL Server licenses with Software Assurance, Hybrid Benefit lets you bring those licenses to Azure and avoid paying for the Windows component in the hourly rate. This can save up to forty-nine percent on Windows VMs.

[SLIDE: Saving and Sharing Estimates]

Once your estimate is complete you can save it to your account, export it as an Excel spreadsheet, or share a link. This is useful for presenting cost proposals to management before a project is approved.

[SLIDE: Calculator Limitations]

Important caveat: the Pricing Calculator gives you estimates, not guarantees. Actual costs depend on runtime behavior, data transfer patterns, and feature flags you may not account for upfront. Use calculator estimates as a planning baseline, then monitor actual costs with Cost Management once resources are deployed.

---

## SEGMENT 3 — Total Cost of Ownership Calculator (5 minutes)

[SLIDE: What is the TCO Calculator?]

The Total Cost of Ownership Calculator serves a different purpose than the Pricing Calculator. The TCO Calculator is designed to help you make the business case for migrating from on-premises infrastructure to Azure. It answers the question: what am I actually spending today on-premises, and what would I spend in Azure?

You find it at azure.microsoft.com/en-us/pricing/tco/calculator.

[SLIDE: TCO Calculator — Three-Step Process]

The TCO Calculator works in three steps. Step one is Define Workloads. You enter your current on-premises environment: how many Windows and Linux servers, how much storage, how much database capacity, and how much network bandwidth. You can be as granular as you like.

Step two is Adjust Assumptions. This is where the calculator gets interesting. It asks about your current electricity costs, labor rates, data center overhead, software licensing, and hardware refresh cycles. These assumptions are editable because every organization is different. A hospital in Dallas pays different electricity rates than a startup in Seattle.

Step three is View Report. The calculator produces a detailed report showing your estimated on-premises cost over three years versus your estimated Azure cost over three years, then calculates the savings. It breaks down the savings by category: compute, storage, IT labor, hardware, and facilities.

[SLIDE: Interpreting TCO Results]

A typical TCO report might show that an organization running thirty on-premises servers saves forty percent over three years by migrating to Azure. The savings come from eliminating hardware refresh costs, reducing data center facility expenses, and paying only for the compute you use rather than maintaining idle capacity for peak loads.

[SLIDE: TCO vs Pricing Calculator — Key Difference]

Let me be clear about the distinction the AZ-900 exam tests. The Pricing Calculator estimates the cost of specific Azure resources you plan to deploy. The TCO Calculator compares total on-premises cost against total Azure cost to support a migration business case. They are different tools for different conversations.

---

## SEGMENT 4 — Azure Cost Management plus Billing (7 minutes)

[SLIDE: Azure Cost Management + Billing]

Once your resources are deployed and running, the Pricing Calculator is no longer your tool. Now you need Azure Cost Management plus Billing, which is built into the Azure portal.

Cost Management plus Billing is a suite of tools that lets you analyze where money is being spent, set spending limits, and receive alerts when costs approach thresholds.

[SLIDE: Cost Analysis]

Cost Analysis is the first major feature. You navigate to it in the Azure portal by searching for Cost Management plus Billing, then selecting Cost Analysis from the left menu.

The default view shows your spending over the current billing period broken down by service, resource group, or location. You can change the granularity to daily, monthly, or cumulative. You can filter by subscription, resource group, tag, or service category.

Tags are especially important for cost analysis. When you tag resources with metadata like Department, Project, or Environment, you can slice your cost reports along those dimensions. A Finance tag on all financial-system resources lets you produce a report showing exactly what the finance team's cloud footprint costs each month.

[SLIDE: Cost Breakdown Views]

Beyond the line chart there is a table view that lists every resource and its accumulated cost. You can sort by cost descending to immediately identify your most expensive resources. This is often surprising. Many teams discover that data transfer costs or load balancer hours account for more spend than the VMs themselves.

[SLIDE: Invoices and Billing]

The Billing section of Cost Management shows your actual invoices — the documents you actually pay. You can download PDF invoices, review usage details in CSV format, and manage payment methods. For enterprise agreements there is additional reporting around commitment usage and drawdown.

[SLIDE: Cost Management Free vs Premium]

Here is an important AZ-900 detail. The core Cost Management features — cost analysis, budgets, and alerts — are available at no extra charge for Azure customers. There is a premium version called Microsoft Cost Management that adds capabilities for multi-cloud cost management across AWS and GCP, but for this exam focus on the free Azure-native features.

[SLIDE: Cost Allocation and Chargebacks]

In larger organizations Cost Management supports cost allocation, where you distribute shared resource costs across business units using rules you define. This enables IT chargebacks, where departments are billed for their actual cloud usage rather than receiving cloud costs as a pooled overhead expense.

---

## SEGMENT 5 — Budgets and Alerts (4 minutes)

[SLIDE: Creating a Budget]

Budgets in Azure Cost Management are spending targets you set at the subscription or resource group level. When your actual spend approaches or crosses the budget threshold, Azure sends you an alert.

To create a budget, navigate to Cost Management plus Billing, select Budgets from the left menu, and click Add. You define the budget scope — the subscription or resource group you want to monitor — the budget amount in dollars, and the reset period — monthly, quarterly, or annually.

[SLIDE: Alert Conditions]

Each budget can have multiple alert conditions. A common pattern is to set three alerts: one at fifty percent of budget, one at ninety percent, and one at one hundred percent. The alerts can send email notifications to a list of recipients and can also trigger Azure Action Groups, which can run automation — for example, shutting down non-critical VMs when the budget is exceeded.

[SLIDE: Anomaly Alerts]

Beyond budget alerts, Cost Management also supports anomaly detection. If your daily spending suddenly spikes significantly above your normal pattern — for example a misconfigured service starts generating millions of API calls — Cost Management can alert you within twenty-four hours rather than waiting for you to notice on your next manual review.

[SLIDE: Budget Actions and Automation]

The integration between budget alerts and Action Groups enables a powerful pattern for development and test environments. You can configure a budget that, when the monthly spend hits one hundred percent, automatically sends an Azure Automation runbook that deallocates all non-production VMs. This provides a hard safety net against runaway costs in environments where people might forget to clean up.

---

## SEGMENT 6 — Cost Optimization Strategies (7 minutes)

[SLIDE: The Four Pillars of Azure Cost Optimization]

Now let's talk strategy. There are four major levers for reducing Azure costs: right-sizing, commitment discounts, spot pricing, and architectural efficiency. We will cover each one.

[SLIDE: Right-Sizing]

Right-sizing means deploying resources at the appropriate scale for the actual workload. The most common waste pattern is over-provisioning — deploying a D8s v3 VM with eight vCPUs when the application uses an average of twelve percent CPU and could run comfortably on a D2s v3.

Azure Advisor analyzes your VM CPU and memory utilization and recommends downsizing underutilized machines. Accepting these recommendations is often the single fastest way to cut an Azure bill.

[SLIDE: Reserved Instances]

Reserved instances, also called Azure Reservations, offer significant discounts in exchange for a one-year or three-year commitment to a specific VM family and region. You are not reserving a specific machine — you are committing to pay for a certain number of hours per month at a discounted rate, and Azure automatically applies that discount to matching VMs in your subscription.

The discount compared to pay-as-you-go pricing varies by VM series and region but typically ranges from twenty to sixty percent for one-year reservations and up to sixty-six percent for three-year reservations.

Reserved instances are ideal for production workloads that run continuously. You know the workload will exist for at least a year, so you commit and save.

[SLIDE: Spot VMs]

Spot virtual machines are a completely different model. Azure has data center capacity that is idle at any given moment. Spot VMs let you purchase that idle capacity at up to ninety percent off pay-as-you-go prices. The catch is that Azure can evict your spot VM with a thirty-second warning when it needs the capacity back for higher-priority workloads.

Spot VMs are perfect for fault-tolerant, interruptible workloads: batch processing jobs, rendering pipelines, large-scale testing, and machine learning training jobs that support checkpointing. They are completely inappropriate for production web servers, databases, or any workload that cannot tolerate interruption.

[SLIDE: Azure Hybrid Benefit]

If your organization has Windows Server, SQL Server, or Linux subscriptions with active Software Assurance or qualifying Red Hat or SUSE subscriptions, Azure Hybrid Benefit lets you bring those licenses to Azure rather than paying for a new license embedded in the hourly VM rate. This applies to VMs, Azure SQL Database, and Azure SQL Managed Instance.

[SLIDE: Dev/Test Pricing]

For development and test environments, Azure offers Dev/Test pricing under an Enterprise Agreement or through Visual Studio subscriptions. Dev/Test pricing provides reduced rates on Windows VMs and eliminates the Windows Server license charge entirely in some cases. The trade-off is that Dev/Test resources carry no SLA — acceptable for non-production.

[SLIDE: Auto-Shutdown and Deallocate]

A simple but powerful cost control for development and test VMs is auto-shutdown. In the Azure portal you can configure a VM to automatically shut down and deallocate at a specified time each day. When a VM is deallocated you stop paying for compute. You still pay for the managed disk, but disk costs are typically a small fraction of total VM cost. For a team of ten developers who each have a dev VM running unnecessarily, auto-shutdown can cut compute costs by thirty percent or more.

---

## SEGMENT 7 — Azure Advisor Cost Recommendations (3 minutes)

[SLIDE: Azure Advisor Overview]

Azure Advisor is a personalized recommendation engine built into the Azure portal. It analyzes your deployed resources against Microsoft best practices and produces recommendations across five categories: Cost, Security, Reliability, Operational Excellence, and Performance.

The Cost category is directly relevant to this module.

[SLIDE: Types of Cost Recommendations]

Advisor's cost recommendations include: shut down or resize underutilized virtual machines based on CPU and memory telemetry from the past seven or thirty days; purchase reserved instances for VMs that have been running continuously; eliminate unattached managed disks that are sitting idle; remove idle load balancer rules; and right-size ExpressRoute circuits with insufficient utilization.

[SLIDE: Estimated Savings]

Each Advisor recommendation shows an estimated monthly savings in dollars. This makes it easy to prioritize which recommendations to act on first. Advisor also tracks your historical savings from recommendations you have implemented.

[SLIDE: Advisor and Cost Management Integration]

Advisor integrates with Cost Management so that recommendations appear in your Cost Analysis view as well. You can configure Advisor to send recommendation summaries by email on a weekly or monthly schedule, which is useful for keeping cost hygiene top of mind without requiring daily portal visits.

---

## SEGMENT 8 — Exam Tips and Module Summary (2 minutes)

[SLIDE: AZ-900 Exam Focus — Cost Management]

Before we close, here are the key exam-ready distinctions for Module 14.

The Pricing Calculator estimates future Azure costs. The TCO Calculator compares on-premises total cost to Azure total cost. Do not confuse these two.

Budget alerts notify you when spend approaches or exceeds a threshold. They can trigger Action Groups for automation.

Reserved instances offer discounts for one-year or three-year commitments on consistent workloads. Spot VMs offer deep discounts — up to ninety percent — for interruptible workloads.

Azure Advisor provides cost, security, reliability, performance, and operational excellence recommendations. The Cost recommendations include VM right-sizing and reserved instance purchase suggestions.

[SLIDE: Module Summary]

In this module we covered the Pricing Calculator for pre-deployment estimates, the TCO Calculator for migration business cases, Cost Management plus Billing for ongoing monitoring and analysis, budget alerts and automation, and optimization strategies including right-sizing, reserved instances, spot VMs, Hybrid Benefit, and Azure Advisor.

Next up is Module 15, where we shift from money to compliance and governance — Microsoft Trust Center, Azure Policy, Blueprints, and regulatory frameworks like HIPAA and FedRAMP.

See you there.

---

## End of Script — Module 14

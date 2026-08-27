# Lab Activity: Module 14 — Azure Cost Management and Pricing

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Lab Overview

**Estimated Time:** 60–75 minutes
**Difficulty:** Beginner
**Azure Account Required:** Yes — Free Trial or Azure for Students account
**Prerequisites:** Module 13 completed; Azure portal access confirmed

In this lab you will use the Azure Pricing Calculator to build a multi-service cost estimate, use the TCO Calculator to compare on-premises and cloud costs, explore Azure Cost Management plus Billing features including Cost Analysis and Budgets, and review Azure Advisor cost recommendations. All tasks can be completed within the Azure free tier limits.

---

## Learning Objectives

By completing this lab you will be able to:

- Build a realistic multi-service estimate in the Azure Pricing Calculator
- Interpret a TCO Calculator report and identify the largest cost categories
- Navigate Cost Analysis to view spending breakdowns and apply filters
- Create a budget with multiple alert thresholds
- Identify and interpret Azure Advisor cost recommendations

---

## Part 1 — Azure Pricing Calculator (20 minutes)

### Task 1.1 — Open the Pricing Calculator

1. Open a browser and navigate to `https://azure.microsoft.com/en-us/pricing/calculator/`
2. No sign-in is required for this step.
3. Take a screenshot of the calculator home page for your lab report.

### Task 1.2 — Add a Virtual Machine

1. Under the Products tab, locate **Virtual Machines** and click it. A VM configuration tile appears in the estimate panel below.
2. Configure the tile with the following settings:

   - **Region:** East US
   - **Operating System:** Windows
   - **Type:** OS Only
   - **Tier:** Standard
   - **Instance:** D2s v3 (2 vCores, 8 GB RAM)
   - **Hours:** 730 (full month)
   - **Pricing Option:** Pay as you go

3. Record the estimated monthly VM cost: **$___________**
4. Change Pricing Option to **1 Year Reserved**. Record the new cost: **$___________**
5. Calculate the savings percentage: **$___________**

### Task 1.3 — Toggle Azure Hybrid Benefit

1. With the D2s v3 VM tile open, locate the **Azure Hybrid Benefit** toggle.
2. Enable Hybrid Benefit.
3. Record the new Pay-as-you-go cost with Hybrid Benefit: **$___________**
4. Compare this to the original PAYG cost. What is the difference? **$___________**

### Task 1.4 — Add Azure SQL Database

1. In the Products catalog, locate **Azure SQL Database** and click it to add a tile.
2. Configure with the following:

   - **Region:** East US
   - **Type:** Single Database
   - **Purchasing Model:** vCore
   - **Service Tier:** General Purpose
   - **Compute Tier:** Provisioned
   - **Generation:** Gen5
   - **vCores:** 4
   - **Storage:** 100 GB

3. Record the estimated monthly SQL Database cost: **$___________**

### Task 1.5 — Add Azure Blob Storage

1. Add a **Storage Accounts** tile to your estimate.
2. Configure with:

   - **Region:** East US
   - **Type:** Block Blob Storage
   - **Redundancy:** LRS
   - **Capacity:** 1 TB
   - **Write operations:** 10,000 per month
   - **Read operations:** 100,000 per month

3. Record the estimated monthly storage cost: **$___________**

### Task 1.6 — Review and Export Your Estimate

1. Review the total estimated monthly cost for all three services: **$___________**
2. Click **Export** and download the Excel file.
3. Open the Excel file and confirm it contains line items for each service.
4. Take a screenshot of the Excel export for your lab report.

### Reflection Question 1

> Which service is the largest cost driver in your estimate? What change to the configuration would most significantly reduce that service's cost?

---

## Part 2 — TCO Calculator (15 minutes)

### Task 2.1 — Open the TCO Calculator

1. Navigate to `https://azure.microsoft.com/en-us/pricing/tco/calculator/`
2. Click **Get Started**.

### Task 2.2 — Define Workloads

1. Under **Servers**, click **Add server workload**.
2. Enter the following:

   - **Name:** Web Servers
   - **Workload:** Windows/Linux Server
   - **Environment:** Virtual Machines
   - **Operating System:** Windows
   - **VMs:** 5
   - **CPU Utilization:** 50%
   - **RAM per server:** 8 GB
   - **Storage per server:** 500 GB

3. Click **Add server workload** again and add:

   - **Name:** Database Server
   - **Workload:** SQL Server
   - **Environment:** Virtual Machines
   - **Operating System:** Windows
   - **VMs:** 2
   - **CPU Utilization:** 70%
   - **RAM per server:** 32 GB
   - **Storage per server:** 2000 GB

4. Click **Next** to proceed to Adjust Assumptions.

### Task 2.3 — Adjust Assumptions

1. Review the pre-populated assumptions. Note the following fields:

   - Electricity cost per kWh: **$___________**
   - IT labor cost per hour: **$___________**
   - Server hardware cost: **$___________**

2. Change the electricity cost to **$0.12** per kWh to reflect a Texas average.
3. Leave all other assumptions at their defaults.
4. Click **Next** to view the report.

### Task 2.4 — Interpret the Report

1. Record the following from the TCO report:

   - Total on-premises 3-year cost: **$___________**
   - Total Azure 3-year cost: **$___________**
   - Total savings: **$___________**
   - Savings percentage: **$___________**

2. Identify the largest on-premises cost category: **$___________**
3. Take a screenshot of the three-year comparison chart.

### Reflection Question 2

> The TCO report shows IT labor savings. Why might migrating to Azure reduce IT labor costs? What on-premises tasks are eliminated in the cloud model?

---

## Part 3 — Azure Cost Management plus Billing (15 minutes)

### Task 3.1 — Navigate to Cost Management

1. Sign in to the Azure portal at `https://portal.azure.com/`
2. In the search bar, type **Cost Management + Billing** and select it.
3. In the left navigation, click **Cost Analysis**.

### Task 3.2 — Explore Cost Analysis Views

1. Observe the default view (accumulated cost for current billing period).
2. Change the **Granularity** to **Daily**. Observe how the chart changes.
3. Change the **View** dropdown to **Cost by Service**. Record the top three services by cost:

   - Service 1: **_________________** Cost: **$___________**
   - Service 2: **_________________** Cost: **$___________**
   - Service 3: **_________________** Cost: **$___________**

4. Change the **Group by** field to **Resource Group**. Note how spending distributes across resource groups.
5. Take a screenshot of Cost Analysis for your lab report.

*Note: If your subscription has no spending, the chart may show $0.00 across all services. In that case, examine the chart structure and navigation options and document what you observe.*

### Task 3.3 — Create a Budget

1. In the Cost Management left navigation, click **Budgets**.
2. Click **+ Add**.
3. Configure the budget:

   - **Name:** Lab14-MonthlyBudget
   - **Reset period:** Monthly
   - **Amount:** $10.00 (appropriate for a free trial account)

4. Click **Next: Alerts**.
5. Add three alert conditions:

   - Condition 1: Actual — 50% — your university email address
   - Condition 2: Actual — 90% — your university email address
   - Condition 3: Forecasted — 110% — your university email address

6. Click **Create**.
7. Confirm the budget appears in the Budgets list.
8. Take a screenshot of the completed budget configuration.

### Reflection Question 3

> What is the difference between an Actual alert threshold and a Forecasted alert threshold? In what scenario would a Forecasted alert be more valuable?

---

## Part 4 — Azure Advisor Cost Recommendations (10 minutes)

### Task 4.1 — Open Azure Advisor

1. In the Azure portal search bar, type **Advisor** and select it.
2. On the Advisor overview page, observe the five pillar scores.
3. Record the Cost score: **___________**

### Task 4.2 — Review Cost Recommendations

1. Click the **Cost** tile to open cost recommendations.
2. For each recommendation listed (or if none exist, note that the subscription has no cost recommendations and describe what each recommendation type would look like based on your reading):

   - Recommendation 1: **_________________**
   - Estimated savings: **$___________**
   - Recommended action: **_________________**

3. If a recommendation exists, click on it to see the details page. Note what data Advisor uses to make the recommendation.
4. Take a screenshot of the Advisor Cost recommendations page.

### Task 4.3 — Configure Advisor Digest

1. In Azure Advisor, click **Configuration** in the left navigation.
2. Click the **Digest** tab.
3. Click **Add Advisor digest**.
4. Configure:

   - **Name:** Lab14-AdvisorDigest
   - **Subscription:** Your subscription
   - **Frequency:** Weekly
   - **Email:** Your university email address

5. Click **Create**.
6. Take a screenshot of the completed digest configuration.

### Reflection Question 4

> Azure Advisor identified your VM as underutilized. What additional information would you want before resizing the VM? Who else in an organization might need to approve a resize decision?

---

## Part 5 — Cost Optimization Scenario Analysis (10 minutes)

For each scenario below, identify the best cost optimization strategy from the module and justify your answer in 2–3 sentences.

### Scenario A

A company runs 50 Linux VMs that process payroll calculations. The VMs run 24/7, have been in production for two years, and will continue running for at least two more years. Average CPU utilization is 65%.

Best strategy: **_________________**

Justification: **_________________**

### Scenario B

A research team needs to train a machine learning model using a cluster of GPU VMs. The training run takes approximately 18 hours. If the job is interrupted it can resume from the last checkpoint.

Best strategy: **_________________**

Justification: **_________________**

### Scenario C

A software company has 20 developer VMs that are used only during business hours Monday through Friday. The VMs are currently running 24/7. The company has a Visual Studio Enterprise subscription.

Best strategy: **_________________**

Justification: **_________________**

### Scenario D

A retail company has 500 TB of transaction logs stored in Azure Blob Storage Hot tier. The logs are older than 90 days and are only accessed during annual audits.

Best strategy: **_________________**

Justification: **_________________**

---

## Lab Deliverables

Submit the following to the course LMS:

1. **Screenshots** (minimum 6): Pricing Calculator estimate, Excel export, TCO three-year chart, Cost Analysis view, Budget configuration, Advisor Cost page
2. **Reflection responses** for all four reflection questions (3–5 sentences each)
3. **Scenario analysis** for all four scenarios (A through D)
4. **Cost summary table** with all recorded dollar amounts filled in

---

## Grading Rubric

| Component | Points |
|---|---|
| Pricing Calculator estimate with all values recorded | 20 |
| TCO Calculator report interpreted with correct values | 20 |
| Budget created with three alert conditions | 20 |
| Advisor recommendations page screenshot | 10 |
| Reflection questions answered thoroughly | 20 |
| Scenario analysis with justified strategies | 10 |
| **Total** | **100** |

---

*Texas Wesleyan University — CIS-4331 Azure Cloud Computing — Module 14 Lab*

---

## Part 9 — Challenge Exercise

### Challenge 1: Reserved Instance Savings Analysis
Using the Azure Pricing Calculator, build two separate estimates for the same workload: (1) three Standard_D4s_v3 Windows Server VMs running 24/7 in East US at pay-as-you-go rates, and (2) the same three VMs using 1-year Reserved Instance pricing with Azure Hybrid Benefit applied (assuming the organization has Software Assurance). Record the monthly and annual cost for each estimate. Calculate the dollar savings and percentage savings from combining reservations with Hybrid Benefit compared to pay-as-you-go. Export both estimates to Excel and include them in your submission. Then write a 3–4 sentence recommendation memo addressed to a fictional CFO explaining whether the organization should purchase reservations for these VMs, referencing the specific savings figures, the break-even timeline, and the flexibility risk if the workload changes.

### Challenge 2: Cost Anomaly Detection and Budget Automation
In the Azure Portal, navigate to Cost Management + Billing > Cost Alerts and review the Anomaly Alerts tab (if your subscription has generated any spending). Then create a new Budget for your lab resource group with a $50 monthly limit and three alert thresholds: 25% forecasted, 75% actual, and 100% actual. For the 100% threshold, configure the Action Group to send an email AND trigger an Azure Automation webhook URL (use a placeholder URL if no Automation account exists). Document screenshots of the budget configuration, all three threshold settings, and the Action Group configuration. Write a 2–3 sentence explanation of why configuring the Action Group to trigger automation (rather than just sending email) is important for controlling cloud spend in a large organization where individual engineers may not respond quickly to budget notifications.

### Reflection Questions
1. Azure Advisor shows five pillars: Cost, Security, Reliability, Performance, and Operational Excellence. A team receives three Advisor recommendations simultaneously: (a) rightsize an underutilized VM (Cost), (b) enable soft delete on a storage account (Reliability), and (c) add a health probe to a load balancer (Reliability). If the team can only act on one recommendation today, describe the framework they should use to prioritize between cost savings and reliability improvements. Include in your answer: the business context variables that would shift the priority toward cost vs. reliability, and a specific example of when implementing a cost recommendation before a reliability recommendation would be the wrong decision.
2. A company uses pay-as-you-go pricing and their Azure bill has grown from $15,000/month to $42,000/month over 18 months as new teams adopted Azure. The CFO asks the cloud team to reduce costs by 25% without decommissioning any production workloads. Describe a step-by-step cost optimization process using Azure Cost Management, Azure Advisor, Reserved Instances, Blob Lifecycle Management, and tags. For each tool in the process, specify what action it enables and what information it provides that the next step in the process depends on.

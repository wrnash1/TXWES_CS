# Lab Activity: Module 01 - Cloud Computing Concepts

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Estimated Time:** 60-75 minutes
**Submission:** Canvas LMS — Module 01 Lab Assignment

---

## Learning Objectives

By completing this lab you will be able to:

- Correctly classify management responsibilities under IaaS, PaaS, and SaaS using the Shared Responsibility Model
- Identify which party (customer or provider) is accountable for each infrastructure layer in each service model
- Use the Azure Total Cost of Ownership (TCO) Calculator to quantify the CAPEX-to-OPEX shift
- Explain cloud deployment model selection using a real-world business scenario

---

## Prerequisites

- No Azure account is required for this lab
- A modern web browser (Chrome, Firefox, Edge) with internet access
- Access to learn.microsoft.com (no login required for the TCO Calculator)
- This lab guide printed or open on a second screen while completing tasks

---

## Part A: Shared Responsibility Model Classification (40 Points)

### Background

The Shared Responsibility Model defines which security and operational tasks belong to the cloud provider (Microsoft Azure) and which belong to the customer. Your ability to apply this model is tested directly on the AZ-900 exam and is critical for real-world cloud security architecture.

### Instructions

Complete the table below by writing either **"Customer"**, **"Provider"**, or **"Shared"** in each cell. Use the definitions from your reading guide to guide your answers.

After completing the table, write a brief justification (2-3 sentences) for the three rows that students most commonly answer incorrectly (marked with an asterisk).

### Shared Responsibility Classification Table

Copy this table into your submission document and fill in each blank cell:

| Infrastructure Layer | IaaS | PaaS | SaaS |
|---|---|---|---|
| Physical datacenter building and security | | | |
| Physical server hardware | | | |
| Physical network hardware | | | |
| Hypervisor / virtualization layer | | | |
| Operating system | | | |
| * Network controls (virtual firewall / NSG) | | | |
| Middleware and runtime environment | | | |
| * Application code and logic | | | |
| * Data classification and protection | | | |
| Identity and access management | | | |
| Client endpoint devices | | | |

### Answer Key (Instructor Reference — Do Not Publish to Students)

| Infrastructure Layer | IaaS | PaaS | SaaS |
|---|---|---|---|
| Physical datacenter building and security | Provider | Provider | Provider |
| Physical server hardware | Provider | Provider | Provider |
| Physical network hardware | Provider | Provider | Provider |
| Hypervisor / virtualization layer | Provider | Provider | Provider |
| Operating system | Customer | Provider | Provider |
| Network controls (virtual firewall / NSG) | Customer | Shared | Provider |
| Middleware and runtime environment | Customer | Provider | Provider |
| Application code and logic | Customer | Customer | Provider |
| Data classification and protection | Customer | Customer | Customer |
| Identity and access management | Shared | Shared | Shared |
| Client endpoint devices | Customer | Customer | Customer |

### Justification Requirement (10 Points of Part A)

Write 2-3 sentences justifying your answers for the three asterisked rows. Your justification should explain *why* responsibility shifts or stays constant across service models for that layer. Use your own words — do not copy from the reading guide.

---

## Part B: Service Model Scenario Classification (25 Points)

### Part B Instructions

Read each scenario below. Identify whether the described deployment uses **IaaS**, **PaaS**, or **SaaS**. Write the service model name and provide a 2-3 sentence explanation citing the specific responsibility indicators in the scenario that led to your classification.

### Scenario 1 (5 Points)

Contoso Manufacturing needs to run a third-party inventory management application. The vendor delivers the application as a website that employees access through their browser. Contoso's IT team only manages user accounts and configures which employees have access to which inventory records. The vendor handles all software updates, servers, and database maintenance.

**Your classification:**

**Your explanation:**

### Scenario 2 (5 Points)

Woodgrove Bank is migrating a legacy lending application from an on-premises server to Azure. The application requires a specific version of Red Hat Enterprise Linux and a custom kernel module for a hardware security module integration. The bank's infrastructure team will continue to apply OS patches and manage the file system.

**Your classification:**

**Your explanation:**

### Scenario 3 (5 Points)

Tailwind Traders wants to launch a new e-commerce website. Their development team will write the application in Node.js and deploy it to Azure. They do not want to manage web servers, OS patches, or load balancers. The Azure service will automatically scale the application based on traffic.

**Your classification:**

**Your explanation:**

### Scenario 4 (5 Points)

Northwind Pharmaceuticals uses a cloud-hosted CRM system to manage customer relationships. Their sales team logs in through a browser to track customer contacts and sales pipeline. Northwind's IT team manages user provisioning and password policies. The CRM vendor handles all software releases and infrastructure.

**Your classification:**

**Your explanation:**

### Scenario 5 (5 Points)

Adventure Works needs to run a high-performance computing cluster for molecular simulation. They require full control over CPU affinity settings, NUMA topology configuration, and custom network drivers. The cluster software must be installed and configured by their HPC team.

**Your classification:**

**Your explanation:**

---

## Part C: Azure TCO Calculator Exercise (25 Points)

### TCO Calculator Overview

The Azure Total Cost of Ownership (TCO) Calculator allows organizations to estimate the cost savings of migrating on-premises infrastructure to Azure. It accounts for hardware depreciation, software licensing, data center costs, IT labor, and other factors. This tool is referenced in the official AZ-900 study materials.

### TCO Calculator Instructions

Navigate to: learn.microsoft.com/en-us/azure/pricing/tco/calculator/

Note: The TCO Calculator is available at azure.microsoft.com/en-us/pricing/tco/calculator/ — no Azure account is required.

Complete the following steps and document your findings.

### Step 1: Define Workloads (5 Points)

Click "Add a workload" and enter the following hypothetical on-premises server environment for a mid-sized organization:

**Workload Name:** Corporate Web Servers

- Workload type: Windows/Linux Server
- Number of VMs: 8
- Cores per VM: 4
- RAM per VM (GB): 16
- Storage per VM (GB): 512
- Operating system: Windows Server

Take a screenshot of your completed workload entry and include it in your submission.

### Step 2: Adjust Assumptions (5 Points)

Click "Next" to reach the Assumptions screen. Review the default values for:

- Software assurance coverage (Windows Server licensing)
- Electricity cost per kilowatt hour
- Network bandwidth cost per GB

Answer the following questions in your submission document:

1. What is the default assumption for hours per year that on-premises servers run at peak utilization? Why might this assumption favor the cloud cost estimate?
2. The calculator includes a "Virtual machine costs" savings percentage. What is the default value, and what does this represent?

### Step 3: Review the Report (10 Points)

Click "Next" to generate the 5-year TCO report. Document the following in your submission:

1. What is the estimated 5-year on-premises cost for your defined workload?
2. What is the estimated 5-year Azure cost for the equivalent workload?
3. What is the calculated cost savings amount and percentage?
4. The report breaks costs into categories (compute, data center, networking, storage, IT labor). Which category shows the largest on-premises cost? Which shows the largest Azure savings?

### Step 4: Analysis (5 Points)

Write a 150-200 word analysis addressing both of the following:

- Based on your TCO results, explain in financial terms why the OPEX model (cloud) shows lower total cost than the CAPEX model (on-premises) for this scenario. Reference at least two specific cost categories from the report.
- Identify one scenario where on-premises infrastructure might still be less expensive than Azure despite these results. What characteristic of that scenario changes the calculation?

---

## Part D: Deployment Model Selection (10 Points)

### Scenario

Your university's IT department is evaluating three infrastructure scenarios. For each scenario below, recommend a cloud deployment model (public, private, or hybrid) and provide a 3-4 sentence justification. Your justification must address cost, control, and compliance considerations.

### Scenario A (3 Points)

A small liberal arts university wants to provide email, calendar, and word processing tools to 2,000 students and 200 faculty members. The university has no dedicated IT infrastructure team and a limited budget.

**Your recommendation and justification:**

### Scenario B (4 Points)

A large research university handles sensitive federally funded research data under NIST SP 800-171 compliance requirements. Some research workloads require significant computing power that the university cannot afford to own permanently, but the research data itself must never leave university-controlled infrastructure.

**Your recommendation and justification:**

### Scenario C (3 Points)

A startup university with no existing infrastructure wants to launch a new online degree program. They need a learning management system, video streaming platform, and student database. They expect enrollment to grow rapidly and unpredictably over the next three years.

**Your recommendation and justification:**

---

## Submission Requirements

Your submission must include:

1. Completed Shared Responsibility table (Part A)
2. Three justification paragraphs for asterisked rows (Part A)
3. Service model classification and explanation for all five scenarios (Part B)
4. Screenshot of TCO Calculator workload entry (Part C Step 1)
5. Answers to TCO assumption questions (Part C Step 2)
6. TCO report findings documentation (Part C Step 3)
7. TCO analysis paragraph (Part C Step 4)
8. Deployment model recommendations for all three scenarios (Part D)

Format your submission as a single PDF or Word document. Include your full name, student ID, and "CIS-4331 Module 01 Lab" in the document header.

---

## Grading Rubric

| Component | Points Available | Criteria |
|---|---|---|
| Part A: Classification table — all 33 cells correct | 30 | 1 point per correct cell minus asterisked justification |
| Part A: Justification for 3 asterisked rows | 10 | 3-4 pts per justification: accuracy, depth, own words |
| Part B: Scenario 1 classification + explanation | 5 | 2 pts classification, 3 pts explanation quality |
| Part B: Scenario 2 classification + explanation | 5 | 2 pts classification, 3 pts explanation quality |
| Part B: Scenario 3 classification + explanation | 5 | 2 pts classification, 3 pts explanation quality |
| Part B: Scenario 4 classification + explanation | 5 | 2 pts classification, 3 pts explanation quality |
| Part B: Scenario 5 classification + explanation | 5 | 2 pts classification, 3 pts explanation quality |
| Part C: TCO workload entry + screenshot | 5 | Screenshot present and correctly configured |
| Part C: Assumption questions | 5 | Both questions answered accurately |
| Part C: Report findings documentation | 10 | All 4 data points documented accurately |
| Part C: Analysis paragraph | 5 | Addresses both prompts, 150-200 words, 2 cost categories cited |
| Part D: Scenario A recommendation | 3 | Correct model, justification covers cost/control/compliance |
| Part D: Scenario B recommendation | 4 | Correct model, justification covers cost/control/compliance |
| Part D: Scenario C recommendation | 3 | Correct model, justification covers cost/control/compliance |
| **Total** | **100** | |

---

## Troubleshooting

**TCO Calculator does not load:** Try a different browser. The calculator requires JavaScript. Disable ad blockers if present. The URL is azure.microsoft.com/en-us/pricing/tco/calculator/

**TCO Calculator results seem unrealistic:** Verify your workload configuration. Eight VMs with 4 cores and 16 GB RAM is a modest workload — results showing $50,000 or more in 5-year on-premises costs are reasonable when data center, licensing, and IT labor are included.

**Unsure about a Shared Responsibility cell:** Re-read Section 2.4 of the Reading Guide (service model comparison table). Focus on which party manages the OS — that is the dividing line between IaaS and PaaS for most layers.

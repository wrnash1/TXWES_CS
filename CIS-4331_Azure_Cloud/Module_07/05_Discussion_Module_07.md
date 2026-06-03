# Discussion Forum: Module 07 — Azure Compute Services

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Points: 10 | Initial Post Due: Wednesday 11:59 PM | Peer Responses Due: Sunday 11:59 PM

---

## Instructions

Read all three scenarios below. Choose **one** scenario that interests you most and write your initial post responding to that scenario. Your initial post must be 175–225 words. Then respond to **two classmates** who chose different scenarios. Each peer response must be at least 75 words and add substantive insight beyond agreement.

---

## Scenario 1: Startup Web Application Architecture

A three-person startup is building a customer-facing e-commerce web application using Python and Flask. They expect low to moderate traffic initially, but their marketing team believes a viral social media campaign could spike traffic to 50 times the baseline on short notice. The CTO wants to minimize infrastructure management overhead so the team can focus on product development. The lead developer is familiar with GitHub and wants a simple deployment workflow. The company has a tight budget and cannot afford to pay for idle compute capacity.

**Discussion Prompt:** Which Azure compute service would you recommend for this startup, and which pricing tier would you select? How would you handle the potential traffic spike scenario? What are the tradeoffs of your recommendation versus deploying to a VM? Would your recommendation change if the application required a custom OS-level library that is not available in standard runtimes?

---

## Scenario 2: Enterprise Workload Modernization

A large regional bank is modernizing its on-premises infrastructure. It currently runs 47 Windows Server VMs in its own data center, hosting a mix of internal web portals, SQL Server databases, batch processing jobs, and a custom .NET 4.8 application that uses Windows Services and requires Task Scheduler for nightly data exports. The IT director wants to move to Azure but must maintain strict uptime requirements and cannot afford downtime during the migration. The security team requires all workloads to remain on dedicated hardware with no shared tenancy.

**Discussion Prompt:** Which Azure compute services would you recommend for the different workload types in this environment? How would you handle the .NET 4.8 application with Windows Services and Task Scheduler? What availability options would you configure to meet uptime requirements? Is there any workload in this scenario that might NOT be suitable for a simple lift-and-shift to Azure VMs, and why?

---

## Scenario 3: Serverless Event Processing Pipeline

A media company uploads hundreds of video files to Azure Blob Storage each day. Immediately after each upload, the company needs to: (1) extract metadata from the video file, (2) generate a thumbnail image, (3) write a record to a database, and (4) send a notification to a queue for downstream processing. Each step currently takes 10–30 seconds and must complete within 5 minutes of upload. The team wants to minimize cost and avoid managing servers. They are evaluating Azure Functions versus Azure Container Instances for this pipeline.

**Discussion Prompt:** Would you recommend Azure Functions or Azure Container Instances for this pipeline, and why? Which trigger type would you use for Azure Functions in this scenario? What hosting plan would you select, and why does that choice matter for a workload that processes hundreds of files per day? What would be the consequence if one of the steps — such as thumbnail generation — exceeded the default Functions timeout on the Consumption plan?

---

## Peer Response Guidelines

When responding to a classmate:

- Acknowledge the service they chose and their reasoning
- Add at least one consideration they may not have addressed (cost, security, scalability, compliance)
- If you disagree with their recommendation, respectfully explain your alternative with specific reasoning
- Reference a specific Azure feature, pricing tier, or SLA figure to support your point

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post demonstrates understanding of the chosen scenario and Azure service capabilities | 4 |
| Initial post references specific Azure features, pricing tiers, or SLA figures | 2 |
| Peer response 1: substantive, adds new insight (75+ words) | 2 |
| Peer response 2: substantive, adds new insight (75+ words) | 2 |
| **Total** | **10** |

---

## Professor Nash Note

The scenarios in this discussion reflect real architectural decisions that cloud architects make regularly. There is rarely one single "correct" answer — the best recommendation depends on constraints like budget, team skills, compliance requirements, and time-to-market. In your initial post, I am looking for evidence that you understand the tradeoffs between IaaS and PaaS, not just the ability to name a service. In your peer responses, push each other to think more deeply. If a classmate recommends App Service and you think AKS is more appropriate at scale, make that case constructively with evidence from this module's content.

---

*Discussion 07 — Module 07: Azure Compute Services | CIS-4331 | Texas Wesleyan University*

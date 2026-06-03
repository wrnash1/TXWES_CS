# Video Script: Module 16 — AZ-900 Exam Preparation and Capstone

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Production Notes

**Estimated Runtime:** 30–35 minutes
**Slide Deck:** Module_16_Slides.pptx
**Visual Aids:** AZ-900 domain breakdown chart, exam interface screenshot, question stem analysis examples, answer elimination walkthrough

---

## SEGMENT 1 — Introduction: The Finish Line (3 minutes)

[SLIDE: Module 16 Title Card]

Welcome to Module 16 — the final module of CIS-4331 Azure Cloud Computing. I'm Professor Nash, and this is both an exam preparation session and a capstone review of everything we have covered across this course.

You have earned this moment. Over the past fifteen modules you built a genuine understanding of cloud computing from the ground up. You started with the fundamental question of what the cloud is and why it exists. You moved through core Azure services — compute, networking, storage, databases — and then into the architectural patterns that make those services reliable, secure, and cost-efficient. You finished with the governance and compliance layer that makes Azure deployable in regulated industries.

[SLIDE: What This Module Covers]

In this module we will do four things. First, we will review all three AZ-900 exam domains and the percentage weight each carries. Second, we will discuss proven exam strategy — how to approach questions, eliminate distractors, and manage your time. Third, we will work through twenty practice questions that mirror the real exam format. Fourth, I will give you a final study plan for the two weeks before your exam date.

Let's get started.

---

## SEGMENT 2 — The AZ-900 Exam: Structure and Domains (5 minutes)

[SLIDE: AZ-900 Exam Overview]

The AZ-900 Microsoft Azure Fundamentals exam tests foundational knowledge of cloud concepts and Azure services. It is designed for candidates who are new to cloud computing or Azure, including business stakeholders, students, and IT professionals who want a validated credential for cloud literacy.

Here are the key facts about the exam format.

The exam consists of 40 to 60 questions. Question types include multiple choice (select one), multiple select (select all that apply), drag and drop, and hotspot. The passing score is 700 on a scale of 1 to 1000. The exam duration is 45 minutes for the timed portion, plus additional time for survey questions and instructions. The exam is proctored and can be taken online from home or at a Pearson VUE test center.

[SLIDE: Three Exam Domains]

The AZ-900 exam is organized into three skill domains, each with a defined percentage weight.

Domain 1 is Describe Cloud Concepts, weighted at 25 to 30 percent of the exam. This domain covers the definition of cloud computing, cloud service models (IaaS, PaaS, SaaS), cloud deployment models (public, private, hybrid), shared responsibility, the consumption-based model, and the benefits of cloud computing — high availability, scalability, elasticity, agility, geo-distribution, and disaster recovery.

Domain 2 is Describe Azure Architecture and Services, weighted at 35 to 40 percent. This is the largest domain. It covers Azure regions, availability zones, resource groups, subscriptions, management groups, Azure Resource Manager, compute services (VMs, containers, App Service, Azure Functions), networking (VNet, VPN Gateway, ExpressRoute, DNS), storage (Blob, Files, Queues, Tables, Disks, tiers), databases (Cosmos DB, Azure SQL, Azure Database for PostgreSQL/MySQL), and identity (Azure Active Directory, MFA, conditional access, RBAC, Zero Trust, Defense in Depth).

Domain 3 is Describe Azure Management and Governance, weighted at 30 to 35 percent. This domain covers cost management (Pricing Calculator, TCO Calculator, Cost Management, reservations, spot VMs, Advisor), governance (Azure Policy, Blueprints, Purview), monitoring (Azure Monitor, Azure Service Health, Log Analytics), and compliance (Trust Center, Service Trust Portal, compliance frameworks).

[SLIDE: Domain Weight Implications]

Notice that Domain 2 is the largest, but Domain 3 is nearly as large and is the area many candidates underestimate. If you have been focused only on technical services and have not studied governance, compliance, and cost tools, you are walking into 30 to 35 percent of the exam underprepared.

---

## SEGMENT 3 — Domain 1 Review: Cloud Concepts (5 minutes)

[SLIDE: Domain 1 — Cloud Concepts Core Review]

Let me walk you through the most heavily tested concepts in each domain.

[SLIDE: Cloud Service Models]

For service models, know the clear dividing lines of responsibility.

IaaS — Infrastructure as a Service — the cloud provider manages physical hardware, network fabric, and hypervisor. You manage the operating system, middleware, applications, and data. Azure Virtual Machines is IaaS.

PaaS — Platform as a Service — the cloud provider manages the OS and middleware. You manage the application and data. Azure App Service and Azure SQL Database are PaaS.

SaaS — Software as a Service — the cloud provider manages everything. You manage only your data and user settings. Microsoft 365 is SaaS.

[SLIDE: Cloud Deployment Models]

Public cloud — resources owned and operated by the cloud provider, shared across multiple customers on the same physical infrastructure, accessed over the internet. Azure is a public cloud.

Private cloud — resources dedicated to a single organization, either on-premises or hosted by a third party. The organization controls everything.

Hybrid cloud — a combination of public and private cloud connected by a private network (VPN or ExpressRoute), allowing workloads to move between environments. Azure Arc extends Azure management to on-premises and multi-cloud environments.

[SLIDE: Shared Responsibility Model]

The shared responsibility model defines what Microsoft is responsible for versus what you as the customer are responsible for. Physical security, the network, and the host hardware — always Microsoft. Applications, user access, data — always the customer. The middle layer — OS, network controls, identity — shifts depending on the service model. IaaS gives you more control and more responsibility. SaaS gives Microsoft more control and more responsibility.

[SLIDE: Cloud Benefits — The Six]

The AZ-900 exam tests six specific cloud benefit terms. High availability means services stay operational despite component failures, backed by SLAs. Scalability means increasing resources to handle more load — either vertically (bigger VM) or horizontally (more VMs). Elasticity means automatically scaling up and scaling back down as demand changes. Agility means quickly deploying and configuring services. Geo-distribution means deploying near users worldwide to reduce latency. Disaster recovery means replicating systems to secondary regions so failures in one region do not take down the service.

---

## SEGMENT 4 — Domain 2 Review: Azure Architecture and Services (8 minutes)

[SLIDE: Domain 2 Core Areas]

Domain 2 is broad. I will focus on the areas most heavily tested.

[SLIDE: Global Infrastructure]

Azure Regions are geographic locations containing one or more data centers. Each region is a set of data centers connected by a dedicated low-latency network. Not all services are available in all regions.

Availability Zones are physically separate data centers within a single region, each with independent power, cooling, and networking. Deploying across zones protects against single data center failure. Availability Zones provide the highest level of intra-region redundancy.

Region Pairs are two Azure regions within the same geography that Microsoft pairs for disaster recovery. Geo-redundant storage replicates within the region pair. Planned maintenance is staggered so both regions in a pair are never down simultaneously.

[SLIDE: Azure Resource Hierarchy]

The management hierarchy from broadest to narrowest is: Azure AD Tenant → Management Groups → Subscriptions → Resource Groups → Resources.

Management Groups organize subscriptions for governance — applying policies and RBAC assignments across multiple subscriptions at once. Subscriptions are billing boundaries and trust boundaries. Resource Groups are logical containers for resources within a subscription. Resources are the actual Azure services.

[SLIDE: Compute Services]

Azure Virtual Machines — IaaS, full OS control, you manage patching and configuration.

Azure App Service — PaaS web hosting for HTTP applications. You deploy code or containers; Azure manages the OS and runtime.

Azure Container Instances — Run containers without managing VMs or orchestrators. Fast startup, per-second billing.

Azure Kubernetes Service — Managed Kubernetes for orchestrating containerized workloads at scale.

Azure Functions — Serverless event-driven compute. You write a function; Azure runs it when triggered. You pay per execution.

[SLIDE: Networking Services]

Azure Virtual Network — Private network in Azure. VMs and services communicate within a VNet without going over the internet.

VPN Gateway — Encrypted tunnel over the public internet connecting on-premises to Azure. Lower cost, tolerates some latency.

ExpressRoute — Dedicated private connection from on-premises to Azure bypassing the internet. Higher bandwidth, lower latency, higher cost.

Azure DNS — Hosts DNS zones, resolves names for Azure and custom domains.

Azure Firewall — Managed, stateful firewall service for VNets.

Network Security Groups — Filter inbound and outbound traffic at subnet or NIC level using rules.

[SLIDE: Storage Services]

Blob Storage — Unstructured data: images, videos, backups, log files. Three access tiers: Hot (frequent access), Cool (infrequent), Archive (rare, offline retrieval).

Azure Files — Fully managed file shares accessible via SMB protocol. Mountable by Windows, Linux, macOS.

Azure Queues — Message queuing for decoupling applications.

Azure Disk Storage — Managed disks attached to VMs.

Storage redundancy options: LRS (3 copies in one data center), ZRS (3 copies across 3 zones), GRS (LRS plus async replication to a paired region), GZRS (ZRS plus replication to a paired region).

[SLIDE: Identity and Security]

Azure Active Directory — Cloud identity provider. Users, groups, service principals, app registrations.

Multi-Factor Authentication — Requires two or more verification methods. Something you know plus something you have or are.

Conditional Access — Policy-driven access decisions based on user, device, location, and application signals.

Role-Based Access Control (RBAC) — Grant specific permissions to specific identities at specific scopes. Built-in roles: Owner, Contributor, Reader.

Zero Trust — Never trust, always verify. Verify identity, validate device, limit access to only what is needed.

Defense in Depth — Multiple layers of security so that if one layer is breached, others remain. Physical, identity, perimeter, network, compute, application, data.

---

## SEGMENT 5 — Domain 3 Review: Management and Governance (5 minutes)

[SLIDE: Domain 3 Core Areas]

Domain 3 maps to Modules 14 and 15 directly. Here is the condensed review.

[SLIDE: Cost Management Tools]

Pricing Calculator — Estimate Azure costs before deployment. azure.microsoft.com/pricing/calculator.

TCO Calculator — Compare on-premises total cost to Azure over three years. Business case for migration.

Cost Management plus Billing — Monitor and analyze actual Azure spend. Cost Analysis, budgets, invoices.

Budgets — Spending thresholds that trigger alerts and optionally trigger Action Groups for automation.

Reserved Instances — One-year or three-year commitment for discounts up to 66%.

Spot VMs — Surplus capacity at up to 90% off. Interruptible workloads only.

Azure Advisor — Recommendations across Cost, Security, Reliability, Performance, and Operational Excellence.

[SLIDE: Governance Tools]

Azure Policy — Rules assigned to scopes that enforce resource configurations. Effects: Deny, Audit, AuditIfNotExists, DeployIfNotExists, Modify.

Initiative Definition — A group of policies assigned as one unit for compliance framework coverage.

Azure Blueprints — Packages policies, role assignments, resource groups, and ARM templates for consistent environment deployment. Maintains a live assignment relationship. Supports versioning and locking.

Microsoft Purview — Data governance: Data Map, automated classification, Data Catalog, data lineage. Compliance Manager provides a compliance score against regulatory frameworks.

[SLIDE: Monitoring Tools]

Azure Monitor — Collects metrics and logs from Azure resources. Basis for alerts, dashboards, and workbooks.

Log Analytics — Query and analyze log data using Kusto Query Language (KQL).

Azure Service Health — Shows status of Azure services and regions, planned maintenance, and service advisories. Three components: Azure Status (global), Service Health (personalized), Resource Health (per-resource).

[SLIDE: Compliance]

Microsoft Trust Center — Public transparency portal. Security, privacy, compliance documentation.

Service Trust Portal — Downloadable audit reports (SOC, ISO, FedRAMP, etc.). Requires sign-in.

Key certifications: ISO 27001 (international ISMS), SOC 2 Type II (operating effectiveness of controls), FedRAMP High (US federal), HIPAA BAA (healthcare PHI).

GDPR — EU personal data protection law. Applies globally. Data residency, data subject rights, breach notification within 72 hours, lawful basis for processing.

---

## SEGMENT 6 — Exam Strategy (4 minutes)

[SLIDE: Exam Strategy Overview]

Knowing the content is necessary but not sufficient. You also need a strategy for how to approach the exam itself.

[SLIDE: Strategy 1 — Read the Full Question Before Reading Answers]

Read the entire question stem before looking at the answer choices. Many candidates skim the question and jump to answers, then get tripped up by a qualifier they missed — words like "only," "always," "never," "most cost-effective," "which would NOT," and "which is the minimum."

These qualifiers completely change the correct answer. Highlight them mentally before evaluating choices.

[SLIDE: Strategy 2 — Eliminate Distractors]

Most AZ-900 questions have one clearly wrong answer, one plausible wrong answer, and one correct answer (with possibly a fourth close option). Start by eliminating the option that is most clearly wrong. This improves your odds immediately. Then compare the remaining options against the specific question the stem is asking.

[SLIDE: Strategy 3 — Answer What is Asked, Not What You Know]

The most common error pattern is answering a more complex version of the question than what was asked. If the question asks which tool estimates Azure costs before deployment, the answer is the Pricing Calculator — not Cost Management plus Billing, even though you know Cost Management is a more sophisticated cost tool. Answer the question, not a related question.

[SLIDE: Strategy 4 — Flag and Move]

If you are not confident on a question, flag it and move on. Do not spend more than 60–90 seconds on any single question the first time through. Complete the entire exam, then return to flagged questions. Under time pressure, your subconscious often produces the right answer after you have had time to process other questions.

[SLIDE: Strategy 5 — Multiple Select Questions]

When the question says "select all that apply" or specifies "select two" or "select three," each correct answer is an independent credit decision. If you know two out of three correct answers, choose those two. Guessing a third incorrect option may not penalize you more than leaving it blank depending on the scoring model — read the instruction carefully.

[SLIDE: Time Management]

With 40 to 60 questions in 45 minutes, you have approximately 45 to 67 seconds per question. This is enough time if you do not overthink. First-pass answers that feel right are usually right. Second-guessing in the final minutes rarely improves your score.

---

## SEGMENT 7 — Two-Week Study Plan (3 minutes)

[SLIDE: Week 1 — Reinforce Weak Areas]

In the two weeks before your exam, follow this structure.

Days 1 through 3: Take a full-length practice exam (available on Microsoft Learn or through MeasureUp). Score it honestly. Identify your weakest domain.

Days 4 through 7: For your weakest domain, revisit the relevant module reading guides and re-watch the video segments for that domain's topics. Do not re-read everything — focus on what you missed.

[SLIDE: Week 2 — Simulate Exam Conditions]

Days 8 through 10: Take a second full-length practice exam under timed conditions. No notes, no references. Simulate the real exam environment exactly.

Days 11 through 13: Review any incorrect answers from practice exams. Focus on understanding why the correct answer is correct, not just memorizing the answer.

Day 14: Light review only. Go over the key distinctions list from Module 16's reading guide. Rest, hydrate, and sleep well. Your brain consolidates learning during sleep — cramming the night before degrades performance.

[SLIDE: Microsoft Learn Resources]

The official free study resource is the Microsoft Learn AZ-900 learning path at learn.microsoft.com. Search for "AZ-900" and you will find a structured learning path with interactive modules, knowledge checks, and sandbox exercises. The Microsoft Learn content is directly aligned to the exam objectives.

---

## SEGMENT 8 — Closing and Encouragement (2 minutes)

[SLIDE: What You Have Built]

Before I let you go, I want to reflect on what you have actually built over this course.

You started not knowing what a resource group was. Now you can design a highly available multi-tier application using availability zones, configure RBAC for least-privilege access, build a cost estimate with the Pricing Calculator, assign Azure Policy to enforce governance rules, and explain to a compliance officer what HIPAA BAA means for an Azure deployment.

That is real knowledge. That is the foundation of a cloud career.

[SLIDE: The Certification is a Marker, Not the Destination]

The AZ-900 certification validates that you have this foundation. It is the beginning of a path, not the end. After AZ-900, the natural next steps in Azure are the AZ-104 Administrator, AZ-204 Developer, and AZ-305 Solutions Architect certifications depending on your career direction. Each one builds directly on what you have learned in this course.

[SLIDE: Final Message]

You are ready. Trust the work you have put in. Go pass your exam.

It has been a privilege to be your instructor for CIS-4331 Azure Cloud Computing. Good luck.

---

## End of Script — Module 16

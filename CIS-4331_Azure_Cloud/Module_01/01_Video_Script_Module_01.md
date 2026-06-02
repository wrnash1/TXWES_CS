# Video Script: Module 01 - Cloud Computing Concepts

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AZ-900 Domain:** Describe Cloud Concepts (25-30% of exam)

---

## [00:00 - 01:30] Opening and Learning Objectives

**[INSTRUCTOR ON CAMERA — title card: "Module 01: Cloud Computing Concepts"]**

Welcome to CIS-4331 Azure Cloud. I am Professor Nash, and this is Module 01, where we lay the entire foundation for everything that follows in this course and on the AZ-900 certification exam.

Before we look at a single Azure service, we need to understand *why cloud computing exists*, what problem it solves, and the vocabulary that Microsoft expects you to command on exam day. The AZ-900 domain called "Describe Cloud Concepts" accounts for roughly 25 to 30 percent of your exam score. If you master this module, you start your exam with a significant head start.

By the end of this session you will be able to:

- Define cloud computing and articulate its core benefits
- Compare IaaS, PaaS, and SaaS with concrete examples
- Contrast public, private, and hybrid cloud deployment models
- Explain the Shared Responsibility Model layer by layer
- Distinguish CAPEX from OPEX and explain why organizations migrate to cloud

Let's get started.

---

## [01:30 - 04:30] What Is Cloud Computing?

**[SLIDE: "Cloud Computing Definition"]**

The official Microsoft definition, which you should memorize for AZ-900, is: cloud computing is the delivery of computing services over the internet, including virtual machines, storage, databases, networking, software, analytics, and intelligence.

But let me give you the real-world translation. Before cloud computing, if your company needed a new server, you had to submit a purchase order, wait 4-8 weeks for delivery, rack the hardware, install an operating system, configure networking, and then finally run your application. The entire process could take months, and if your demand forecast was wrong, you were stuck with either too much hardware sitting idle or too little hardware causing outages.

Cloud computing solves this by treating compute infrastructure the same way your city treats electricity — you plug in, you consume what you need, and you pay for what you used. You do not own the power plant. You do not maintain the turbines. You just consume the service.

**[SLIDE: "Core Cloud Benefits — AZ-900 Exam List"]**

Microsoft identifies several core benefits that AZ-900 tests specifically. Let me walk through each one:

**High Availability** means the cloud provider guarantees that services remain accessible for a defined percentage of time, documented in a Service Level Agreement or SLA. Azure's SLA for Virtual Machines in Availability Zones is 99.99 percent, meaning you can tolerate less than 53 minutes of downtime per year. We will explore SLAs in depth in Module 02.

**Scalability** comes in two forms. Vertical scaling, sometimes called "scaling up," means adding more CPU or RAM to an existing resource. Horizontal scaling, called "scaling out," means adding more instances of a resource. Azure supports both, and the choice depends on your application architecture.

**Elasticity** means the cloud can automatically provision and de-provision resources in response to demand changes. Think of a retail website during Black Friday — Azure can spin up 50 additional virtual machine instances when traffic spikes, then release them when traffic normalizes, and you only pay for the hours those instances ran.

**Reliability** and **Predictability** relate to consistent performance and consistent cost. The cloud's global distribution of infrastructure means a regional failure does not have to be your application's failure.

**Security** in the cloud is a shared responsibility — we will spend significant time on this in a moment.

**Governance** means tools and policies that enforce organizational standards across all cloud resources.

**Manageability** means the ability to control and operate your cloud environment through multiple interfaces: a web portal, command-line tools, APIs, and PowerShell.

---

## [04:30 - 08:30] Service Models: IaaS, PaaS, and SaaS

**[SLIDE: "The Three Cloud Service Models"]**

This is one of the highest-frequency topic areas on AZ-900. Microsoft will give you a business scenario and expect you to identify which service model applies. Let me build a framework you can use on every such question.

**[SLIDE: "IaaS — Infrastructure as a Service"]**

Infrastructure as a Service gives you the raw building blocks: virtual machines, virtual networks, and storage. You manage the operating system, all software installed on that OS, and your application. The provider manages everything below the OS — the physical hardware, the hypervisor, and the physical network.

Think of IaaS as renting an unfurnished apartment. The landlord provides the walls, plumbing, and electricity. You bring your furniture, set up your kitchen, and arrange everything the way you want. You have maximum control, but you also have maximum responsibility.

The primary IaaS example on AZ-900 is **Azure Virtual Machines**. When you deploy a VM, you choose the OS image, you install your own software, and you are responsible for applying security patches to that OS.

**[SLIDE: "PaaS — Platform as a Service"]**

Platform as a Service removes OS management from your responsibilities. The provider manages infrastructure, operating system, and middleware. You are responsible for your application code and your data.

Think of PaaS as a fully equipped commercial kitchen in a food hall. The facilities management team maintains the ovens, refrigerators, ventilation, and plumbing. You bring your recipes and ingredients, cook, and serve. You focus entirely on the cooking, not on appliance maintenance.

AZ-900 PaaS examples include **Azure App Service**, **Azure SQL Database**, and **Azure Functions**. When you deploy to App Service, you upload your code — you never SSH into a server, you never patch an OS, you never configure a web server binary.

**[SLIDE: "SaaS — Software as a Service"]**

Software as a Service means the entire stack — hardware, OS, runtime, and application — is managed by the provider. You configure the application through its user interface and manage your data and user access, but nothing else.

Think of SaaS as dining at a restaurant. You pick a table, choose from the menu, and eat. You do not see the kitchen, you do not operate the equipment, and you are not responsible if the refrigerator breaks down.

AZ-900 SaaS examples include **Microsoft 365**, **Microsoft Teams**, and **Dynamics 365**. Users access these through a browser or thin client with no installation of runtime infrastructure.

**[SLIDE: "Service Model Comparison Table"]**

Here is the decision framework for exam scenarios:

| Responsibility | IaaS | PaaS | SaaS |
|---|---|---|---|
| Applications | Customer | Customer | Provider |
| Data | Customer | Customer | Customer |
| Runtime | Customer | Provider | Provider |
| Operating System | Customer | Provider | Provider |
| Virtualization | Provider | Provider | Provider |
| Physical Hardware | Provider | Provider | Provider |

The key question to ask yourself: does the scenario mention managing an OS? If yes, IaaS. Does it mention deploying only application code? If yes, PaaS. Does it mention only using an application? If yes, SaaS.

---

## [08:30 - 11:30] Deployment Models: Public, Private, and Hybrid Cloud

**[SLIDE: "Cloud Deployment Models"]**

Knowing service models tells you *what* is managed. Knowing deployment models tells you *where* the infrastructure lives and *who* operates it.

**Public Cloud** is infrastructure owned and operated by a third-party provider — Microsoft, in Azure's case — and made available to multiple customers over the public internet. All Azure services you access through portal.azure.com are public cloud. The key benefits are no upfront hardware cost, global reach, and pay-as-you-go pricing. The concern some organizations have is multi-tenancy — your virtual machines share physical hosts with other customers' virtual machines, though isolation is enforced at the hypervisor level.

**Private Cloud** is infrastructure that is operated exclusively for a single organization. It may be hosted on-premises in the organization's own data center, or it may be hosted by a third party, but the hardware and software are dedicated to that single tenant. Private cloud provides the greatest control and isolation, but it requires the organization to own or contract for the hardware and bear the CAPEX cost.

**Hybrid Cloud** connects a private cloud or on-premises infrastructure to a public cloud, allowing data and applications to move between the two environments. This is the most complex model but the most common in large enterprises. A hospital might keep patient records on a private on-premises server for regulatory compliance while using Azure public cloud for analytics workloads.

**[SLIDE: "A Common Exam Trap"]**

AZ-900 sometimes asks whether "on-premises data center" is the same as "private cloud." It is not. A traditional on-premises data center does not meet the cloud definition because it lacks characteristics like self-service provisioning, rapid elasticity, and broad network access. Private cloud uses cloud principles on dedicated hardware. On-premises is legacy infrastructure.

---

## [11:30 - 15:30] The Shared Responsibility Model

**[SHOW PORTAL — navigate to learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility]**

The Shared Responsibility Model is one of the most tested concepts on AZ-900. Microsoft publishes a diagram that clearly shows which security responsibilities belong to the customer and which belong to the provider across each service model. Let me walk you through it layer by layer.

**Physical security** — the data center building, biometric access controls, security cameras, and physical server hardware — is always the cloud provider's responsibility in all three service models. Microsoft invests billions of dollars annually in physical data center security. This is never your responsibility when you are a cloud customer.

**Hypervisor and virtualization layer** — the software that creates and manages virtual machines — is always Microsoft's responsibility. You cannot access the hypervisor as an Azure customer.

**Operating system** — here is where responsibility shifts. In IaaS, the OS is your responsibility. In PaaS and SaaS, it is Microsoft's responsibility.

**Network controls** — in IaaS, you configure virtual network security groups and firewall rules. In PaaS, the provider manages the underlying network but you configure application-level access controls. In SaaS, the provider manages all networking.

**Application** — in IaaS and PaaS, your application code is always your responsibility. In SaaS, the provider manages the application.

**Data, identities, and devices** — regardless of service model, you are always responsible for your data classification and management, your user identities and access controls, and the devices your users connect from. Microsoft cannot know what data sensitivity your files contain. You must classify and protect your own data.

This framework is critical because it defines accountability. When a breach occurs, the Shared Responsibility Model determines whether Microsoft failed (unauthorized physical access to a data center) or the customer failed (weak password policy that allowed account compromise).

---

## [15:30 - 18:30] CAPEX vs. OPEX and the Cloud Economics Model

**[SLIDE: "Capital Expenditure vs. Operational Expenditure"]**

Understanding the financial motivation for cloud adoption is tested on AZ-900 and is fundamental to justifying cloud projects in any organization.

**CAPEX — Capital Expenditure** is money spent to acquire or upgrade physical assets. When a company buys servers, networking equipment, and data center real estate, that is CAPEX. These purchases appear on the balance sheet as assets that depreciate over time. The problem: you must predict future demand accurately before buying the hardware. If you over-buy, you have idle assets wasting money. If you under-buy, you have capacity constraints during peak demand.

**OPEX — Operational Expenditure** is money spent on ongoing operational costs — it shows up as an expense in the current period. Cloud computing converts server costs from CAPEX to OPEX. Instead of buying a server for $20,000, you rent compute capacity for a few cents per hour. This has significant accounting and cash flow benefits, and it removes the demand forecasting problem entirely.

**[SLIDE: "Consumption-Based Pricing"]**

Azure uses a consumption-based model. You pay for compute, storage, and network resources only while they are running. This means:

- No upfront infrastructure cost
- Ability to scale instantly based on actual demand
- Costs align directly to business activity
- The ability to stop paying for resources when they are not needed

**[SLIDE: "Reserved Instances — A Nuance"]**

AZ-900 occasionally tests awareness of Reserved Instances. If you know you will need a specific VM type continuously for one or three years, you can pre-commit to that capacity and receive a discount of up to 72 percent compared to pay-as-you-go pricing. This is still OPEX — you do not own hardware — but it introduces a commitment in exchange for cost savings. The tradeoff is reduced flexibility.

---

## [18:30 - 21:00] Putting It Together — Scenario Walkthroughs

**[SLIDE: "Scenario Practice"]**

Let me walk through three scenarios the way AZ-900 might present them.

**Scenario 1:** A financial services company needs to run a legacy application that requires a specific Windows Server version and custom kernel drivers. The IT team must maintain full control of the operating system. Which service model is appropriate?

The answer is **IaaS**. The signal is "full control of the operating system" and "custom kernel drivers." Only IaaS gives you OS-level access.

**Scenario 2:** A development team wants to deploy a Python web application. They want Microsoft to handle OS patching, server maintenance, and scaling. They only want to push code and configure environment variables. Which service model is appropriate?

The answer is **PaaS**. The signals are "handle OS patching," "handle scaling," and "only push code." Azure App Service is the specific PaaS service that matches this scenario.

**Scenario 3:** A company wants to provide email and calendar services to employees without managing any servers, operating systems, or software installations. Which service model applies?

The answer is **SaaS**. The signal is "without managing any servers, operating systems, or software." Microsoft 365 is the canonical AZ-900 SaaS example.

---

## [21:00 - 23:30] Lab Preview and Exam Alignment

**[SLIDE: "This Week's Lab"]**

In Module 01's lab, you will work through the **Shared Responsibility Model classification exercise**. You will be given a table of management layers — physical host, hypervisor, operating system, runtime, application, data — and for each layer you will identify whether the customer or provider is responsible across IaaS, PaaS, and SaaS. This exercise directly mirrors how AZ-900 frames its scenario questions.

You will also use the **Azure Total Cost of Ownership Calculator** at learn.microsoft.com to estimate the cost difference between running a set of on-premises servers versus migrating them to Azure. This calculator is free, requires no Azure account, and is referenced in the official AZ-900 study materials.

**[SLIDE: "AZ-900 Exam Connection"]**

The AZ-900 "Describe Cloud Concepts" domain covers everything in this module plus the high-availability and reliability features we previewed. Review the official Microsoft Learn learning path at learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/ — it includes interactive knowledge checks that mirror exam question format.

---

## [23:30 - 24:00] Closing

**[INSTRUCTOR ON CAMERA]**

That wraps up Module 01. You now have the vocabulary and conceptual framework to speak confidently about cloud computing, and you have the analytical tools to classify service models and deployment models on the AZ-900 exam.

In Module 02, we go physical — we will look at the actual buildings, regions, and availability zones that make up Azure's global infrastructure. Understanding that physical architecture is what makes high availability, disaster recovery, and compliance possible.

Complete the reading guide, do the lab, and take the quiz before our next session. I will see you in Module 02.

---

**References:**

- learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/
- learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility

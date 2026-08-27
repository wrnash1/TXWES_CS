# Reading Guide: Module 01 - Cloud Computing Concepts

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Cloud Concepts (25-30% of exam)

---

## Introduction

Module 01 establishes the conceptual foundation for the entire course and for the AZ-900 certification. Every subsequent Azure service — virtual machines, databases, networking, security — exists within the framework of cloud computing models you will learn here. Investors, architects, compliance officers, and developers all speak this vocabulary. Master it now and every future module becomes easier.

The AZ-900 "Describe Cloud Concepts" domain carries roughly 25-30 percent of the exam weight. This reading guide is structured to give you the depth required for both the exam and practical professional conversations.

---

## Section 1: Core Cloud Computing Definitions

### 1.1 What Cloud Computing Is

Cloud computing is the delivery of computing services over the internet. Those services include, but are not limited to: compute (virtual machines, containers), storage (blobs, file shares, databases), networking (virtual networks, load balancers, DNS), analytics, artificial intelligence, developer tools, and management tools.

The critical word in the definition is "delivery over the internet." Cloud computing is not simply virtualization — an organization can run virtual machines on its own hardware without that being cloud computing. Cloud computing additionally requires:

- **On-demand self-service:** Users can provision resources without requiring human interaction with the provider.
- **Broad network access:** Services are available over the network from diverse client platforms.
- **Resource pooling:** The provider serves multiple customers using shared physical infrastructure.
- **Rapid elasticity:** Resources can be scaled out and released quickly, often automatically.
- **Measured service:** Usage is monitored, controlled, and reported, enabling the pay-as-you-go model.

### 1.2 Cloud Computing Benefits for AZ-900

The following benefits appear on the AZ-900 exam. Know each definition and be able to identify which benefit a scenario is describing.

**High Availability** refers to the guarantee, backed by an SLA, that a service will be accessible for a defined percentage of time. Azure expresses this as a percentage uptime commitment. For example, the Azure Virtual Machines SLA for instances deployed across Availability Zones is 99.99 percent, which translates to less than 53 minutes of permitted downtime per year.

**Scalability** is the ability to increase or decrease resources in response to demand. Vertical scaling (scaling up/down) changes the size of an existing resource — adding more CPU cores or RAM to a single virtual machine. Horizontal scaling (scaling out/in) changes the number of instances — adding more virtual machines to a pool.

**Elasticity** extends scalability with automation. Elastic systems detect load changes and provision or de-provision resources automatically, without manual intervention. Azure Virtual Machine Scale Sets are the primary IaaS elasticity mechanism on AZ-900.

**Reliability** in Azure context means the infrastructure is distributed across many physical locations globally, so that a failure in one location does not automatically cause a customer-visible outage. Reliability is architectural — it is built through redundancy at the hardware, data center, and regional levels.

**Predictability** has two forms on AZ-900. Performance predictability means consistent response time and throughput for a workload. Cost predictability means you can forecast cloud spending based on consumption patterns, using tools like the Azure Pricing Calculator and Cost Management.

**Security** in the cloud is shared between the provider and customer, as detailed in the Shared Responsibility Model. Microsoft handles physical security and hypervisor security. Customers are responsible for network configuration, identity management, and data classification.

**Governance** refers to the enforcement of organizational standards across cloud resources using tools like Azure Policy, Management Groups, and Blueprints (covered in Module 12).

**Manageability** in the cloud means multiple interfaces exist to control resources: the Azure Portal (web browser), Azure CLI (command-line), Azure PowerShell, REST APIs, and Infrastructure as Code templates. This module's lab preview introduces the TCO Calculator, a management-adjacent tool.

---

## Section 2: Service Models — IaaS, PaaS, and SaaS

### 2.1 Infrastructure as a Service (IaaS)

IaaS provides virtualized compute, storage, and network infrastructure. The customer manages everything from the operating system upward. The provider manages the physical hardware, hypervisor, and physical network.

**Customer responsibilities in IaaS:**

- Operating system installation, configuration, and patching
- Middleware installation (web servers, application runtimes)
- Application deployment and management
- Data backup and security
- Network security group and firewall rule configuration

**Provider responsibilities in IaaS:**

- Physical data center security
- Physical servers and storage hardware
- Physical networking and datacenter connectivity
- Virtualization/hypervisor layer

**Primary Azure IaaS service on AZ-900:** Azure Virtual Machines

**When to choose IaaS:** When you need full OS control, when running legacy applications with specific kernel requirements, when lift-and-shift migrating an on-premises server to the cloud, or when regulatory requirements mandate that you control the OS configuration.

### 2.2 Platform as a Service (PaaS)

PaaS provides a managed environment for application development and deployment. The provider manages infrastructure and the operating system. The customer deploys and manages application code and data.

**Customer responsibilities in PaaS:**

- Application code and configuration
- Data management and security
- Application-level access controls

**Provider responsibilities in PaaS:**

- All IaaS responsibilities (hardware, hypervisor, network)
- Operating system installation, patching, and management
- Runtime environment (web server, language interpreter, middleware)
- Scaling and load balancing infrastructure

**Primary Azure PaaS services on AZ-900:** Azure App Service, Azure SQL Database, Azure Functions, Azure Kubernetes Service (managed control plane)

**When to choose PaaS:** When your team wants to focus on application development without OS management overhead, when you need automatic scaling, or when you want managed database services without DBA overhead for engine patching.

### 2.3 Software as a Service (SaaS)

SaaS provides fully managed software applications delivered over the internet. The provider manages the entire stack. The customer uses the software and manages their own data and user access configuration.

**Customer responsibilities in SaaS:**

- Data input and management within the application
- User account provisioning and access permissions
- Device and endpoint security for client devices

**Provider responsibilities in SaaS:**

- Everything from IaaS and PaaS responsibilities
- Application logic, features, and software updates
- Data storage infrastructure

**Primary Azure/Microsoft SaaS examples on AZ-900:** Microsoft 365 (Word, Excel, Teams, Outlook), Dynamics 365, Power BI (cloud service tier)

**When to choose SaaS:** When off-the-shelf software meets business requirements, when you need rapid deployment without development effort, or when minimizing operational overhead is the priority.

### 2.4 Service Model Comparison Table

| Management Layer | IaaS | PaaS | SaaS |
|---|---|---|---|
| Physical hardware | Provider | Provider | Provider |
| Physical network | Provider | Provider | Provider |
| Hypervisor | Provider | Provider | Provider |
| Operating system | **Customer** | Provider | Provider |
| Network controls (virtual) | Customer | Shared | Provider |
| Middleware / runtime | **Customer** | Provider | Provider |
| Application | **Customer** | **Customer** | Provider |
| Data | **Customer** | **Customer** | **Customer** |
| Identity and access | **Customer** | **Customer** | **Customer** |
| Client devices | **Customer** | **Customer** | **Customer** |

Bold entries indicate layers that students most frequently miss on exams.

---

## Section 3: Deployment Models

### 3.1 Public Cloud

Public cloud infrastructure is owned and operated by a third-party cloud provider (Microsoft, Amazon, Google) and made available to multiple customers simultaneously. All Azure services accessed through portal.azure.com are public cloud.

**Characteristics:**

- No upfront capital investment for hardware
- Pay-as-you-go consumption pricing
- On-demand self-service provisioning
- Shared multi-tenant physical infrastructure (logically isolated)
- Global reach through provider's distributed data centers
- Provider responsible for hardware refresh and maintenance

**Best for:** Startups and organizations without legacy infrastructure, workloads with variable demand, applications requiring global distribution.

### 3.2 Private Cloud

Private cloud is cloud infrastructure operated exclusively for a single organization. The hardware may be owned by the organization (on-premises private cloud) or hosted by a third party in a dedicated environment.

The key distinction between a private cloud and a traditional on-premises data center: a private cloud implements cloud characteristics (self-service provisioning, elasticity, measured service) on dedicated hardware. A traditional data center does not provide those cloud characteristics.

**Characteristics:**

- Dedicated hardware for a single organization
- Greater control over hardware configuration
- Can meet strict regulatory or compliance requirements
- Higher CAPEX or dedicated-hosting cost
- Organization responsible for hardware maintenance (if on-premises)

**Best for:** Organizations with strict data sovereignty requirements, regulated industries (government, healthcare, financial services), organizations with existing hardware investments.

### 3.3 Hybrid Cloud

Hybrid cloud connects on-premises or private cloud resources to a public cloud, enabling workloads and data to move between the two environments.

**Characteristics:**

- Combines benefits of public and private models
- Enables "cloud bursting" — scaling into public cloud during peak demand
- Keeps sensitive data on-premises while using public cloud for scalable workloads
- Requires connectivity infrastructure (Azure ExpressRoute or VPN Gateway)
- More complex to architect and manage

**Best for:** Organizations with legacy applications that cannot be moved to public cloud, organizations with regulatory requirements for specific data, organizations in transition migrating to public cloud over time.

### 3.4 Deployment Model Comparison Table

| Characteristic | Public Cloud | Private Cloud | Hybrid Cloud |
|---|---|---|---|
| Hardware ownership | Provider | Customer or dedicated 3rd party | Mixed |
| CAPEX required | No | Yes (or dedicated contract) | Partial |
| Multi-tenant | Yes | No | Partial |
| Regulatory control | Standard (certifications available) | Maximum | Flexible |
| Setup complexity | Low | High | Highest |
| Elasticity | Full | Limited by hardware | Partial |
| Azure example | All standard Azure services | Azure Stack Hub | Azure Arc, Azure VPN Gateway |

---

## Section 4: The Shared Responsibility Model

### 4.1 Layer-by-Layer Breakdown

The Shared Responsibility Model defines accountability for security and operations across the cloud stack. Microsoft publishes this model at learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility.

**Always the provider's responsibility (all service models):**

- Physical datacenter security (building access, surveillance, guards)
- Physical compute hardware
- Physical network infrastructure
- Hypervisor layer

**Responsibility varies by service model:**

| Layer | IaaS | PaaS | SaaS |
|---|---|---|---|
| Operating system | Customer | Provider | Provider |
| Network controls | Customer | Shared | Provider |
| Applications | Customer | Customer | Provider |
| Identity infrastructure | Shared | Shared | Shared |

**Always the customer's responsibility (all service models):**

- Data classification and accountability
- User account management and access permissions
- Client endpoint devices
- Information and data protection

### 4.2 Why This Matters Professionally

The Shared Responsibility Model is not just an exam topic — it defines the scope of security obligations in cloud contracts and regulatory audits. When a healthcare organization stores patient data in Azure Blob Storage (an IaaS-adjacent service), Microsoft secures the physical storage and the service interface. The healthcare organization is responsible for encrypting the data, controlling who has access, and ensuring the retention policies comply with HIPAA. A breach caused by a misconfigured access policy is the customer's responsibility, not Microsoft's.

---

## Section 5: CAPEX vs. OPEX

### 5.1 Capital Expenditure (CAPEX)

CAPEX involves purchasing physical assets that appear on the balance sheet and depreciate over time. Server hardware, storage arrays, networking equipment, and data center construction are all CAPEX.

**CAPEX challenges in traditional IT:**

- Requires accurate demand forecasting years in advance
- Creates idle capacity when over-provisioned
- Creates outages when under-provisioned
- Ties up capital that could be used for business operations
- Long procurement lead times (weeks to months)
- Hardware lifecycle management and refresh cycles

### 5.2 Operational Expenditure (OPEX)

OPEX involves ongoing operational costs expensed in the current period. Cloud computing converts infrastructure cost to OPEX. You rent compute by the hour, storage by the gigabyte-month, and network by the gigabyte transferred.

**OPEX advantages in cloud computing:**

- No upfront investment
- Pay only for what you use
- Scales instantly with business demand
- Predictable per-unit pricing
- Provider handles hardware refresh
- IT team refocuses from hardware maintenance to business value

### 5.3 Consumption-Based Pricing Model

Azure's consumption-based pricing is the foundational financial model for the exam. Key points:

- Resources are billed while running, not purchased in advance
- Stopping a virtual machine ends the compute billing (storage continues)
- Different resources have different pricing units (per hour, per GB, per request, per execution)
- The Azure Pricing Calculator helps estimate costs before deployment
- Cost Management and Billing tools track and optimize actual spending

### 5.4 Reserved Instances — The Exam Nuance

AZ-900 occasionally tests knowledge of Reserved Instances (also called Reserved Capacity or Azure Reservations). These are 1-year or 3-year commitments to a specific resource type in exchange for a discount up to 72 percent compared to pay-as-you-go rates. Reserved Instances are still OPEX — no hardware is purchased — but they introduce a financial commitment. The flexibility tradeoff is that you pay for the reservation even if you stop using the resource.

---

## Section 6: SLA Tiers and Availability Math

### 6.1 SLA Basics

Azure Service Level Agreements specify the uptime percentage Microsoft commits to for each service. These percentages translate to specific maximum downtime per year.

| SLA Percentage | Max Downtime Per Week | Max Downtime Per Month | Max Downtime Per Year |
|---|---|---|---|
| 99.0% | 1 hr 41 min | 7 hr 18 min | 3 days 15 hr |
| 99.5% | 50 min | 3 hr 39 min | 1 day 19 hr |
| 99.9% | 10 min 4 sec | 43 min 49 sec | 8 hr 41 min |
| 99.95% | 5 min 2 sec | 21 min 54 sec | 4 hr 21 min |
| 99.99% | 1 min | 4 min 22 sec | 52 min 35 sec |

### 6.2 Composite SLA

When an application depends on multiple services, the effective SLA is the product of each individual SLA. For example, if a VM (99.9%) depends on a SQL Database (99.99%), the composite SLA is 99.9% x 99.99% = approximately 99.89%. This is lower than either individual SLA.

The implication: adding redundancy (multiple VMs, multiple regions) can increase the effective application SLA above the single-service SLA.

---

## Section 7: Azure CLI Command Reference (Module 01 Preview)

While Module 01 is conceptual, you will use Azure CLI throughout this course. Here are the foundational commands to verify your environment is configured.

```bash
# Verify Azure CLI installation
az --version

# Log in to Azure
az login

# List available subscriptions
az account list --output table

# Set the active subscription
az account set --subscription "Subscription Name or ID"

# Show current account details
az account show
```

Reference: learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli

---

## Section 8: AZ-900 Exam Tips

1. **Service model identification:** The exam will describe a management responsibility pattern and ask you to name the model. Memorize the exact layer where customer responsibility begins in each model: OS and above for IaaS, application and data for PaaS, data and identity only for SaaS.

2. **Deployment model trap:** "On-premises" is not the same as "private cloud." On-premises is traditional IT. Private cloud requires cloud characteristics (self-service, elasticity, measured service) on dedicated hardware. The exam may try to get you to confuse these.

3. **Shared responsibility absolutes:** The customer is always responsible for data classification and user/identity management regardless of service model. The provider is always responsible for physical security. These never change regardless of IaaS/PaaS/SaaS.

4. **CAPEX vs. OPEX keyword:** When an exam question describes "eliminating upfront costs" or "paying only for what you use," the answer relates to OPEX and consumption-based pricing. When a question describes "purchasing dedicated hardware," that is CAPEX.

5. **Hybrid cloud requirements:** Hybrid cloud requires a connectivity mechanism between the private and public environments. On AZ-900, the relevant Azure services are VPN Gateway and Azure ExpressRoute. The exam may reference these in deployment model context.

6. **High availability vs. disaster recovery:** High availability addresses uptime through redundancy within a region. Disaster recovery addresses business continuity after a catastrophic regional failure. These are related but distinct concepts on AZ-900.

7. **Elasticity is automatic:** Distinguish elasticity from manual scaling. If a scenario describes automatic resource adjustment without human intervention, that is elasticity. If it describes an administrator manually resizing a VM, that is scaling but not elasticity.

8. **Reserved Instances are still OPEX:** A common distractor describes Reserved Instances as if they involve hardware ownership. They do not. Reservations are financial commitments to cloud services — OPEX, not CAPEX.

---

## Section 9: Required Resources

Complete all of the following before taking the quiz:

- Microsoft Learn path: learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/
- Microsoft Shared Responsibility documentation: learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility
- Azure Total Cost of Ownership Calculator: learn.microsoft.com/en-us/azure/pricing/tco/calculator/ (used in this module's lab)
- Azure Pricing Calculator: learn.microsoft.com/en-us/azure/pricing/calculator/ (referenced in exam tips)

---

## Section 10: Study Checklist

Complete each item before moving to the quiz:

- [ ] Read Sections 1-5 of this guide completely
- [ ] Memorize the Shared Responsibility Model table (Section 4.1)
- [ ] Memorize the SLA percentage / downtime table (Section 6.1)
- [ ] Complete the Microsoft Learn "Describe cloud computing" unit
- [ ] Complete the Microsoft Learn "Describe benefits of using cloud services" unit
- [ ] Complete the Microsoft Learn "Describe cloud service types" unit
- [ ] Review the IaaS/PaaS/SaaS comparison table until you can reproduce it from memory
- [ ] Review the deployment model comparison table
- [ ] Read the 8 AZ-900 exam tips in Section 8
- [ ] Complete Lab Activity Module 01 (Shared Responsibility classification + TCO Calculator)
- [ ] Take Quiz Module 01 (10 questions)
- [ ] Post your Module 01 Discussion initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft Learn — Describe cloud computing**
https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/
The official AZ-900 learning module covering cloud definitions, the shared responsibility model, and deployment models with interactive knowledge checks.

**2. Microsoft Learn — Describe the benefits of using cloud services**
https://learn.microsoft.com/en-us/training/modules/describe-benefits-use-cloud-services/
Covers high availability, scalability, elasticity, reliability, security, governance, and manageability in depth with scenario-based practice questions aligned directly to AZ-900 exam objectives.

**3. Microsoft Azure Shared Responsibility in the Cloud**
https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility
The official Microsoft documentation defining the shared responsibility model with a layer-by-layer breakdown for IaaS, PaaS, and SaaS. Recommended reading for both the AZ-900 exam and real-world cloud security conversations.

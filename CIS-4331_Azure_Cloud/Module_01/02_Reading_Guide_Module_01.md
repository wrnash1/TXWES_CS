# Reading Guide: Module 01 - Cloud Computing Concepts

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 01 - Cloud Computing Concepts**! This module covers the foundational cloud service models and deployment models that form the bedrock of the **Microsoft Azure Fundamentals (AZ-900)** certification. Understanding these distinctions is critical — AZ-900 exam questions consistently test whether you can classify real-world scenarios into the correct service model or deployment model.

You will learn how IaaS, PaaS, and SaaS differ in terms of customer responsibility, how public, private, and hybrid clouds compare, and why the shift from capital expenditure (CAPEX) to operational expenditure (OPEX) is a primary driver for cloud adoption. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **IaaS (Infrastructure as a Service)**: A cloud service model in which the provider supplies virtualized compute, networking, and storage resources, while the customer is responsible for the operating system, middleware, and applications. Azure Virtual Machines is the primary IaaS example on AZ-900. The customer retains the most control but also the most responsibility.

* **PaaS (Platform as a Service)**: A cloud service model where the provider manages the underlying infrastructure and operating system, and the customer deploys and manages their applications and data. Azure App Service and Azure SQL Database are PaaS offerings. PaaS eliminates OS patching and server maintenance for developers.

* **SaaS (Software as a Service)**: A fully managed service model in which the provider hosts, operates, and maintains the entire stack — infrastructure, OS, runtime, and application. The customer only configures and uses the software. Microsoft 365 and Dynamics 365 are SaaS products frequently cited on AZ-900.

* **Public / Private / Hybrid Cloud**: Public cloud (like Azure) is owned and operated by a third-party provider and shared across multiple tenants, offering the lowest upfront cost. Private cloud runs on dedicated infrastructure for a single organization, providing greater control and isolation. Hybrid cloud connects on-premises or private cloud resources with public cloud services, enabling data and workload portability.

* **Shared Responsibility Model**: A framework defining which security and operational tasks belong to the cloud provider versus the customer. For IaaS, customers manage the OS and up; for PaaS, customers manage applications and data; for SaaS, customers manage only identity and data access. The provider always owns physical security and hypervisor layers.

* **CAPEX vs. OPEX**: Capital Expenditure (CAPEX) refers to upfront investment in physical infrastructure such as servers and data centers, which depreciate over time. Operational Expenditure (OPEX) refers to ongoing pay-as-you-go costs for cloud services. Cloud adoption shifts spending from CAPEX to OPEX, enabling organizations to scale without large upfront investments.

---

### 2. Certification Exam Tips

* **AZ-900 Service Model Focus**: The exam frequently presents a business scenario and asks you to identify whether it is IaaS, PaaS, or SaaS. Key signal: if the question mentions the customer managing the OS, it is IaaS. If the customer only deploys code, it is PaaS. If the customer just uses the application, it is SaaS.
* **Deployment Model Trap**: Do not confuse "private cloud" with "on-premises." A private cloud uses cloud principles (self-service, elasticity) on dedicated hardware. Traditional on-premises data centers are not considered a cloud deployment model on AZ-900.
* **Shared Responsibility Specifics**: AZ-900 tests whether you know that the customer is always responsible for data classification and account/identity management regardless of service model. The provider is always responsible for physical host security.
* **CAPEX vs. OPEX**: Expect at least one scenario question asking which model reduces upfront hardware costs. The correct answer is always cloud/OPEX. Know that Reserved Instances shift some OPEX back toward a committed spend but still avoid hardware ownership.
* **Study Resource**: The Microsoft Learn learning path for AZ-900 includes free, browser-based exercises with no Azure account required. Work through the "Describe cloud concepts" module at [Microsoft Learn – AZ-900 Cloud Concepts](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/) to reinforce these distinctions with interactive knowledge checks.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The official Microsoft Learn path covers all AZ-900 cloud concept objectives with interactive modules, knowledge checks, and sandbox exercises. Begin with the "Describe cloud computing" unit at [Microsoft Learn – AZ-900 Cloud Concepts](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/).
* **Required Video:** This free 3-hour course by freeCodeCamp covers the full AZ-900 exam curriculum including cloud models, service types, and Azure-specific services — watch the Cloud Concepts section (first ~45 minutes): [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Classify hosting scenarios into IaaS, PaaS, or SaaS**: Review a set of Azure service descriptions and categorize each by service model, explaining which management responsibilities shift to the customer in each case.
* **Determine operational ownership for virtualization layers**: Using the shared responsibility model diagram, identify which party (provider or customer) owns the OS, hypervisor, network controls, and physical host for each service model.
* **Estimate costs using the TCO Calculator**: Use the [Azure Total Cost of Ownership Calculator](https://azure.microsoft.com/en-us/pricing/tco/calculator/) to compare on-premises infrastructure costs versus Azure equivalents, demonstrating the CAPEX-to-OPEX shift.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the "Describe cloud computing" unit in [Microsoft Learn – AZ-900 Cloud Concepts](https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/).
* [ ] Watch the Cloud Concepts section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for the TCO Calculator and service model classification exercise.
* [ ] Proceed to the weekly hands-on lab activity.

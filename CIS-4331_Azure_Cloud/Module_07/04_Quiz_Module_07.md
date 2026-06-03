# Quiz: Module 07 — Azure Compute Services

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Domain: Describe Azure Architecture and Services (35–40% of exam)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points. Total: 100 points.

---

### Question 1

A company is migrating a legacy Windows application to Azure. The application requires a specific version of the .NET Framework and has custom Windows registry configurations. Which Azure compute service is most appropriate?

A. Azure App Service

B. Azure Virtual Machines

C. Azure Functions

D. Azure Container Instances

**Correct Answer: B**

**Distractor Analysis:**

- **A (App Service):** App Service is a PaaS service that manages the underlying OS. Custom OS-level configurations like registry edits are not possible. Incorrect.
- **B (Virtual Machines) — CORRECT:** VMs provide full OS access, allowing the customer to install specific .NET versions and modify registry settings. This is an IaaS lift-and-shift scenario.
- **C (Azure Functions):** Functions is serverless compute. There is no access to the OS or ability to install dependencies at the OS level. Incorrect.
- **D (Container Instances):** ACI runs containers, which share the host OS kernel and do not provide Windows registry access. Incorrect.

---

### Question 2

Your team deploys two VMs to an Availability Set. The Availability Set has two fault domains and five update domains. During a planned Azure maintenance event, how many VMs will be restarted simultaneously?

A. Both VMs, because they are in the same Availability Set

B. Neither VM — Availability Sets prevent all restarts

C. One VM — Azure updates one update domain at a time

D. One VM — Azure updates one fault domain at a time

**Correct Answer: C**

**Distractor Analysis:**

- **A:** Incorrect. The purpose of an Availability Set is to distribute VMs across update domains so they are NOT all restarted at the same time.
- **B:** Incorrect. Availability Sets do not prevent maintenance restarts — they stagger them across update domains.
- **C — CORRECT:** Update domains control planned maintenance. Azure restarts VMs in one update domain at a time. With two VMs spread across five update domains, only one VM restarts during any maintenance window.
- **D:** Incorrect. Fault domains protect against unplanned hardware failures (power/network), not planned maintenance. Update domains control maintenance scheduling.

---

### Question 3

A startup wants to host a Python web API on Azure. They want automatic scaling, no OS management, and the ability to deploy from GitHub. Which service is the best fit?

A. Azure Virtual Machine Scale Sets

B. Azure Kubernetes Service

C. Azure App Service

D. Azure Container Instances

**Correct Answer: C**

**Distractor Analysis:**

- **A (VM Scale Sets):** Scale Sets provide auto-scaling but still require OS management (IaaS). Not the best fit for a team that wants no OS management. Incorrect.
- **B (AKS):** AKS is designed for container orchestration of microservices. It requires containerizing the app and managing cluster configuration — significantly more complexity than needed for a simple Python API. Incorrect.
- **C (App Service) — CORRECT:** App Service natively supports Python, provides auto-scaling on Standard+ tiers, manages the OS, and supports GitHub continuous deployment. This is the ideal PaaS match for the scenario.
- **D (ACI):** ACI runs containers but does not provide built-in GitHub integration or the managed PaaS experience of App Service. Incorrect.

---

### Question 4

An e-commerce company needs to process order confirmation emails whenever a new order is written to an Azure Storage Queue. The processing takes 2–3 seconds per order. Processing only happens during business hours. Which Azure compute service minimizes cost?

A. Azure Virtual Machine (always on)

B. Azure App Service (Standard plan)

C. Azure Functions (Consumption plan)

D. Azure Kubernetes Service

**Correct Answer: C**

**Distractor Analysis:**

- **A (VM always on):** A VM running 24/7 incurs continuous cost even when idle outside business hours. Not cost-efficient for intermittent event-driven processing. Incorrect.
- **B (App Service Standard):** App Service plans bill continuously based on plan size, regardless of workload. For infrequent, short-duration processing, this is more expensive than serverless. Incorrect.
- **C (Functions Consumption) — CORRECT:** The Consumption plan scales to zero when idle and bills only when code executes. A queue trigger fires the function on each new message. For short tasks (2–3 seconds) that happen intermittently, this is the most cost-efficient option.
- **D (AKS):** AKS is designed for multi-container orchestration. It requires worker nodes that incur VM costs continuously. Far too complex and expensive for this simple queue-processing scenario. Incorrect.

---

### Question 5

Which Azure Virtual Machine size series is specifically designed for memory-intensive workloads such as large in-memory databases and SAP HANA?

A. F-series

B. B-series

C. N-series

D. E-series and M-series

**Correct Answer: D**

**Distractor Analysis:**

- **A (F-series):** F-series is compute optimized — high CPU-to-memory ratio. Best for CPU-bound workloads, not memory-intensive. Incorrect.
- **B (B-series):** B-series is burstable general purpose — low baseline CPU that can burst. Not designed for high memory workloads. Incorrect.
- **C (N-series):** N-series includes GPU-enabled VMs for machine learning and graphics rendering. Not memory optimized. Incorrect.
- **D (E-series and M-series) — CORRECT:** E-series and M-series are memory optimized. E-series suits mid-range in-memory databases; M-series provides the highest memory-to-CPU ratios in Azure (up to 4 TB RAM) for workloads like SAP HANA.

---

### Question 6

A development team wants to use blue/green deployments for their Azure App Service application to enable zero-downtime releases. Which App Service feature supports this pattern?

A. App Service Environments

B. Deployment slots

C. Scale-out rules

D. Availability Zones

**Correct Answer: B**

**Distractor Analysis:**

- **A (App Service Environments):** ASE is the Isolated tier offering — it provides network isolation in a VNet. It is not specifically a zero-downtime deployment tool. Incorrect.
- **B (Deployment slots) — CORRECT:** Deployment slots allow deploying a new version to a staging slot, validating it, then swapping staging and production with zero downtime. This is the blue/green deployment pattern for App Service.
- **C (Scale-out rules):** Scale-out rules add more instances for traffic capacity — they do not address deployment strategy or downtime. Incorrect.
- **D (Availability Zones):** Availability Zones provide datacenter-level fault tolerance for infrastructure. They do not address deployment patterns or application release strategy. Incorrect.

---

### Question 7

You need to run a containerized batch job that processes uploaded images. The job takes 90 seconds to complete and is triggered a few times per day. There are no inter-container communication requirements. Which service best fits this workload?

A. Azure Kubernetes Service

B. Azure App Service

C. Azure Container Instances

D. Azure Virtual Machine Scale Sets

**Correct Answer: C**

**Distractor Analysis:**

- **A (AKS):** AKS is designed for long-running, multi-container applications. For a simple, occasional 90-second batch job, the cluster overhead is excessive and unnecessarily expensive. Incorrect.
- **B (App Service):** App Service is optimized for web applications and APIs. While it can run containers, it is not designed for triggered batch container execution. Incorrect.
- **C (ACI) — CORRECT:** ACI is purpose-built for short-lived, simple container workloads. It starts in seconds, bills per-second, supports "Never" restart policy for one-shot jobs, and requires no orchestration configuration. Perfect for this scenario.
- **D (VM Scale Sets):** Scale Sets involve managing VMs, not containers directly, and are designed for long-running auto-scaling workloads — not short batch jobs. Incorrect.

---

### Question 8

What is the maximum number of VM instances that a Virtual Machine Scale Set can support in Uniform orchestration mode?

A. 100

B. 500

C. 1,000

D. 10,000

**Correct Answer: C**

**Distractor Analysis:**

- **A (100):** Incorrect. This is far below the actual limit and would not support large-scale auto-scaling architectures.
- **B (500):** Incorrect. While this may seem reasonable, it is not the documented Azure limit for VMSS uniform mode.
- **C (1,000) — CORRECT:** Azure Virtual Machine Scale Sets in Uniform orchestration mode support up to 1,000 VM instances when using platform images. Custom images support up to 600 instances.
- **D (10,000):** Incorrect. This exceeds the Azure limit for a single Scale Set. Larger deployments require multiple Scale Sets behind a common load balancer.

---

### Question 9

Which of the following correctly describes the Azure Kubernetes Service (AKS) cost model?

A. You pay for both the Kubernetes control plane and the worker nodes

B. The Kubernetes control plane is free; you pay only for worker node VMs

C. AKS charges are based on the number of containers deployed

D. AKS uses a per-second billing model similar to Azure Container Instances

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Incorrect. Microsoft manages the AKS control plane (API server, etcd, scheduler) at no charge. This is a key differentiator that makes AKS cost-competitive.
- **B — CORRECT:** The AKS control plane is provided free of charge. Customers pay for the worker node VMs (standard Azure VM pricing), storage, and networking. An optional Uptime SLA add-on costs $0.10/cluster/hour for 99.95% control plane SLA.
- **C:** Incorrect. AKS does not charge based on container count. Billing is based on the underlying VM sizes and counts of the node pools.
- **D:** Incorrect. Per-second billing is the model for Azure Container Instances, not AKS. AKS node VMs bill by the hour like standard VMs.

---

### Question 10

A company needs to ensure their Azure App Service web application is isolated in a dedicated Virtual Network for compliance with financial regulations. Which App Service tier provides this level of network isolation?

A. Standard (S1)

B. Premium (P1v3)

C. Isolated (I1v2) — App Service Environment

D. Basic (B1)

**Correct Answer: C**

**Distractor Analysis:**

- **A (Standard):** Standard tier supports auto-scaling and deployment slots but does not provide dedicated VNet isolation. It runs on shared infrastructure from Azure's perspective of network isolation. Incorrect.
- **B (Premium):** Premium tier adds VNet integration (outbound traffic through a VNet) and enhanced performance but does not place the App Service Environment itself in a dedicated, isolated VNet. Incorrect.
- **C (Isolated — ASE) — CORRECT:** The Isolated tier runs on an App Service Environment (ASE), which is deployed into a customer-controlled Azure Virtual Network. All inbound and outbound traffic flows through the customer's VNet. This provides the highest level of network isolation and is designed for regulated industries requiring private network compliance.
- **D (Basic):** Basic tier provides dedicated compute but no VNet isolation whatsoever. Incorrect.

---

*Quiz 07 — Module 07: Azure Compute Services | CIS-4331 | Texas Wesleyan University*

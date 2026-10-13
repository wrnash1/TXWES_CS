# Reading Guide: Module 07 — Azure Compute Services

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4331 &BULL; MICROSOFT AZURE CLOUD ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Domain: Describe Azure Architecture and Services (35–40% of exam)

---

## Introduction

Azure compute services form the execution engine of cloud architectures. From full virtual machines to serverless functions, Azure provides a spectrum of compute options mapped to different control, responsibility, and pricing models. Understanding when to use each service — and why — is one of the most heavily tested competency areas on the AZ-900 exam. This guide provides the conceptual depth and comparison tables needed for both the exam and real-world architectural decision-making.

---

## Section 1: Azure Virtual Machines

### 1.1 What Is a Virtual Machine?

An Azure Virtual Machine (VM) is an IaaS (Infrastructure-as-a-Service) offering. Microsoft manages the physical hardware, networking, and data center facilities. The customer manages the operating system, runtime, middleware, and applications.

The shared responsibility model for VMs:

| Layer | Responsibility |
|---|---|
| Physical hosts, network, datacenter | Microsoft |
| Hypervisor / virtualization | Microsoft |
| Operating system | Customer |
| Network configuration (NSGs, firewall) | Customer |
| Runtime and middleware | Customer |
| Application code and data | Customer |

### 1.2 VM Size Families

Azure organizes VMs into size families based on workload profile. The family name appears in the VM SKU — for example, Standard_D4s_v3 is a D-series (General Purpose) VM with 4 vCPUs.

| Family | Characteristic | Primary Use Cases | Example Series |
|---|---|---|---|
| General Purpose | Balanced CPU:memory | Dev/test, small databases, web servers | B, D, Dv4, Dav4 |
| Compute Optimized | High CPU:memory | Batch workloads, web servers, analytics | F, Fx |
| Memory Optimized | High memory:CPU | Large relational DBs, in-memory caches | E, Ev4, M |
| Storage Optimized | High disk IOPS | Big Data, NoSQL databases, data warehouses | L, Lsv2 |
| GPU | Dedicated GPU hardware | ML training, graphics rendering, HPC | N, NC, NV |
| High Performance Compute | Fastest CPU + RDMA networking | Scientific simulations, financial modeling | H, HB |

### 1.3 Availability Sets

An Availability Set is a logical grouping of VMs that protects against hardware failures and planned maintenance. VMs in an Availability Set are distributed across:

**Fault Domains (FDs)** — Racks sharing common power and network switch. Azure supports up to 3 fault domains. If a rack loses power, only VMs in that fault domain are affected.

**Update Domains (UDs)** — Groups of VMs Azure updates one at a time during planned maintenance. Azure supports up to 20 update domains.

SLA for Availability Sets: 99.95% uptime.

Rules for Availability Sets:

- All VMs must be in the same Azure region
- All VMs must be in the same datacenter
- VMs must be added to the Availability Set at creation time (cannot add later)
- Availability Sets do NOT protect against datacenter-level failures

### 1.4 Availability Zones

Availability Zones are physically separate datacenters within the same Azure region, each with independent power, cooling, and networking. Azure regions that support zones have a minimum of three zones.

| Feature | Availability Set | Availability Zone |
|---|---|---|
| Protects against | Rack failure, planned maintenance | Datacenter failure |
| VM placement | Same datacenter | Different datacenters (zones) |
| SLA | 99.95% | 99.99% |
| Supported regions | All regions | Regions with zone support |

### 1.5 Virtual Machine Scale Sets

Virtual Machine Scale Sets (VMSS) enable deploying and managing a group of identical, auto-scaling load-balanced VMs.

Key VMSS capabilities:

- **Auto-scaling** based on metrics: CPU percentage, memory, custom Azure Monitor metrics, or schedules
- **Uniform mode**: All VMs are identical; scale to 1,000 instances
- **Flexible orchestration mode**: Mix VM sizes; combine with regular VMs
- **Integrated load balancing**: Works with Azure Load Balancer or Application Gateway
- **Rolling upgrades**: Update a percentage of VMs at a time without full downtime
- **Spot instances**: Use Azure Spot VMs in a scale set for significant cost savings on interruptible workloads

---

## Section 2: Azure App Service

### 2.1 Overview

Azure App Service is a PaaS (Platform-as-a-Service) compute service for hosting web applications, REST APIs, and mobile app backends. Developers deploy code or containers; Azure manages the operating system, runtime, patching, load balancing, and auto-scaling infrastructure.

Supported code runtimes: .NET, Java, Node.js, Python, PHP, Ruby.

### 2.2 App Service Plan Tiers

| Tier | Category | Auto-Scale | Deployment Slots | Custom Domain/SSL | VNet Integration | Use Case |
|---|---|---|---|---|---|---|
| Free (F1) | Dev/Test | No | No | No | No | Learning, prototyping |
| Shared (D1) | Dev/Test | No | No | Yes | No | Low-traffic testing |
| Basic (B1-B3) | Prod | No | No | Yes | No | Low-traffic production |
| Standard (S1-S3) | Prod | Yes (10 instances) | Yes (5) | Yes | No | Most production apps |
| Premium (P1v3-P3v3) | Prod | Yes (30 instances) | Yes (20) | Yes | Yes | High-scale, regulated |
| Isolated (I1v2-I3v2) | Prod | Yes (100 instances) | Yes (20) | Yes | Dedicated VNet | Maximum isolation, compliance |

### 2.3 Deployment Slots

Deployment slots are live environments within an App Service app. Each slot has its own hostname and settings. The primary use pattern:

1. Deploy new version to **staging** slot
2. Warm up the staging slot (run integration tests)
3. **Swap** staging with production — zero downtime
4. Production now runs the new version; staging holds the previous version
5. If issues are detected, swap back immediately

Slot settings can be "sticky" (slot-specific) or swapped with the slot. Connection strings, environment variables, and feature flags can be configured per-slot.

### 2.4 AZ-900 Exam Signal for App Service

Scenario signals that indicate App Service is the correct answer:

- "Host a web application without managing servers"
- "Deploy a REST API with auto-scaling"
- "Zero-downtime deployment for a web app"
- "PaaS hosting for .NET / Java / Node.js / Python web app"

---

## Section 3: Azure Functions

### 3.1 Serverless Model

Azure Functions is a serverless, event-driven compute service. The developer writes small units of code (functions). Azure provisions, scales, and manages all infrastructure. Billing is based on execution count and execution duration — when code is not running, you pay nothing (on the Consumption plan).

### 3.2 Trigger Types

Every Azure Function is triggered by a specific event type.

| Trigger Type | Event | Example Use Case |
|---|---|---|
| HTTP | Incoming HTTP request | REST API endpoint, webhook |
| Timer | Scheduled CRON expression | Nightly report generation |
| Blob Storage | New blob added to container | Image resizing pipeline |
| Queue Storage | New message in a queue | Order processing worker |
| Service Bus | Message from Service Bus queue/topic | Enterprise messaging |
| Event Hub | Stream event received | IoT telemetry processing |
| Cosmos DB | Document change in Cosmos DB | Change feed processing |

### 3.3 Hosting Plans

| Plan | Scale | Cold Start | VNet Support | Timeout | Best For |
|---|---|---|---|---|---|
| Consumption | Serverless, 0–N | Yes | No | 5 min (max 10) | Cost-sensitive, irregular traffic |
| Premium | Pre-warmed, 1–N | No | Yes | Unlimited | Latency-sensitive, private networking |
| Dedicated (App Service) | Fixed | No | Yes | Unlimited | Predictable cost, existing plan |

### 3.4 AZ-900 Exam Signal for Functions

Scenario signals for Azure Functions:

- "Execute code in response to an event"
- "Serverless" or "pay only when code runs"
- "HTTP trigger / timer trigger / queue trigger"
- "No infrastructure to manage"
- "Short-lived code execution"

---

## Section 4: Azure Container Instances

### 4.1 Container Fundamentals

Containers package an application with its dependencies (libraries, runtime, configurations) into a portable, isolated unit. Containers share the host OS kernel — they are faster to start and more resource-efficient than VMs. Docker is the dominant container runtime.

### 4.2 ACI Characteristics

| Feature | Detail |
|---|---|
| Startup time | Seconds |
| OS support | Linux and Windows |
| Billing | Per-second (CPU and memory allocated) |
| Networking | Public IP with DNS label, or private VNet deployment |
| Storage | Azure Files mount for persistent storage |
| Orchestration | None (single container or container group) |
| Restart policy | Always / On Failure / Never |

### 4.3 ACI vs. AKS

| Factor | Azure Container Instances | Azure Kubernetes Service |
|---|---|---|
| Orchestration | None | Full (Kubernetes) |
| Setup complexity | Minimal | High (cluster configuration) |
| Use case | Single container, batch jobs, CI agents | Multi-container microservices |
| Scaling | Manual or Azure Container Apps | Auto-scaling, HPA, KEDA |
| Cost model | Per-second | Node VM cost (control plane free) |
| Best for | Simple, short-lived workloads | Production microservices |

---

## Section 5: Azure Kubernetes Service

### 5.1 Kubernetes Concepts

| Concept | Definition |
|---|---|
| Cluster | The entire AKS deployment (control plane + node pools) |
| Control Plane | API server, scheduler, etcd, controller manager — managed by Microsoft |
| Node Pool | A group of VMs (nodes) that run pods |
| Node | A single VM in a node pool |
| Pod | Smallest deployable unit; wraps one or more containers |
| Deployment | Kubernetes object managing desired replica count of pods |
| Service | Network abstraction that exposes pods; types: ClusterIP, NodePort, LoadBalancer |
| Namespace | Logical partition within a cluster for multi-tenant workload isolation |

### 5.2 AKS Cost Model

The AKS control plane (Kubernetes master) is free — Microsoft manages and hosts it at no charge. You pay for:

- Worker node VMs (standard Azure VM pricing)
- Persistent volumes (Azure Managed Disks or Azure Files)
- Load Balancers, Public IPs, and egress traffic
- Optional: Uptime SLA ($0.10/cluster/hour for 99.95% SLA on control plane)

### 5.3 AZ-900 Exam Signal for AKS

Scenario signals for AKS:

- "Container orchestration"
- "Microservices with multiple containers"
- "Auto-scale containers based on demand"
- "Rolling deployment of containerized application"
- "Managed Kubernetes"

---

## Section 6: Compute Service Comparison

### 6.1 Full Service Comparison Table

| Service | Category | OS Management | Scaling | Billing Model | AZ-900 Trigger Words |
|---|---|---|---|---|---|
| Virtual Machines | IaaS | Customer | Manual / Scale Sets | Per hour, VM size | "OS control," "lift-and-shift," "custom software" |
| App Service | PaaS | Microsoft | Auto (plan-based) | Per App Service Plan tier | "Web app," "REST API," "PaaS hosting" |
| Azure Functions | Serverless | Microsoft | Automatic (0 to N) | Per execution + duration | "Serverless," "event-driven," "trigger" |
| Container Instances | PaaS (Container) | Microsoft | Manual | Per-second (CPU+mem) | "Run a container fast," "batch container job" |
| Azure Kubernetes Service | PaaS (Orchestration) | Microsoft (control plane) | Auto (HPA) | Node VM cost | "Container orchestration," "microservices," "K8s" |

### 6.2 Decision Framework

**Step 1:** Does the workload require full OS control or non-standard system-level software?

- Yes → Virtual Machines

**Step 2:** Is it a web application, API, or mobile backend with standard runtimes?

- Yes → App Service

**Step 3:** Is the workload short-lived and event-driven (HTTP, timer, queue)?

- Yes → Azure Functions (Consumption plan for minimal cost)

**Step 4:** Is it a single container or small batch job requiring fast startup?

- Yes → Azure Container Instances

**Step 5:** Is it a multi-container microservices application needing orchestration?

- Yes → Azure Kubernetes Service

---

## Section 7: Azure CLI Reference

```bash
# Create a VM
az vm create \
  --resource-group lab07-rg \
  --name lab07vm \
  --image UbuntuLTS \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B1s

# Create an App Service Plan
az appservice plan create \
  --name lab07plan \
  --resource-group lab07-rg \
  --sku S1 \
  --is-linux

# Create a Web App on the plan
az webapp create \
  --name lab07webapp \
  --resource-group lab07-rg \
  --plan lab07plan \
  --runtime "NODE|18-lts"

# Create a Function App (Consumption plan)
az functionapp create \
  --name lab07func \
  --resource-group lab07-rg \
  --consumption-plan-location eastus \
  --runtime node \
  --runtime-version 18 \
  --functions-version 4 \
  --storage-account lab07storage

# Create a Container Instance
az container create \
  --resource-group lab07-rg \
  --name lab07aci \
  --image mcr.microsoft.com/azuredocs/aci-helloworld \
  --cpu 1 --memory 1.5 \
  --dns-name-label lab07demo \
  --ports 80

# Create an AKS cluster
az aks create \
  --resource-group lab07-rg \
  --name lab07aks \
  --node-count 1 \
  --generate-ssh-keys
```

---

## Section 8: AZ-900 Exam Tips

1. **IaaS vs. PaaS boundary for VMs:** If a scenario says the customer manages the OS — that is IaaS (VMs). If the scenario says Microsoft manages the OS and the customer only manages the application — that is PaaS (App Service, Functions).

2. **Availability Set numbers:** Fault domains = up to 3 (rack-level). Update domains = up to 20 (maintenance batches). SLA = 99.95%.

3. **Availability Zone SLA:** Deploying VMs across Availability Zones achieves 99.99% SLA — higher than Availability Sets (99.95%). The difference is datacenter-level protection.

4. **Scale Sets are for auto-scaling identical VMs.** If a scenario mentions "automatically add or remove VMs based on demand," the answer is Virtual Machine Scale Sets, not a single VM.

5. **Functions cold start:** The Consumption plan may have a cold start delay after idle periods. The Premium plan uses pre-warmed instances to eliminate this. If a scenario mentions "eliminate cold starts," the answer is the Premium plan.

6. **ACI vs. AKS decision:** ACI for simple, fast, single-container execution. AKS for orchestration of multiple containers with scaling and self-healing. If a scenario uses the word "orchestration," the answer is AKS.

7. **App Service deployment slots:** Available on Standard tier and above. Used for zero-downtime deployments (swap staging to production). If a scenario mentions "zero-downtime deployment of a web app," deployment slots are the mechanism.

8. **Serverless = no infrastructure management + pay-per-use.** Azure Functions on the Consumption plan is the primary serverless compute offering in Azure.

---

## Section 9: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the VM size family table (Section 1.2)
- [ ] Understand the difference between Availability Sets and Availability Zones (Section 1.3 and 1.4)
- [ ] Memorize the App Service plan tiers table (Section 2.2)
- [ ] Understand the three Functions hosting plans (Section 3.3)
- [ ] Memorize the compute service comparison table (Section 6.1)
- [ ] Work through the decision framework in Section 6.2 using your own scenarios
- [ ] Complete the Microsoft Learn "Describe Azure compute and networking services" module
- [ ] Complete Lab Module 07
- [ ] Take Quiz Module 07
- [ ] Post Discussion Module 07 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft Learn — Azure App Service overview**
https://learn.microsoft.com/en-us/azure/app-service/overview
Covers App Service plan tiers, supported language runtimes, deployment methods (GitHub Actions, zip deploy, FTP), deployment slots, auto-scaling rules, and VNet integration — essential for both AZ-900 and AZ-104 exam prep.

**2. Microsoft Learn — Azure Functions hosting options**
https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale
Detailed comparison of the Consumption, Flex Consumption, Premium, and Dedicated (App Service) hosting plans — including cold start behavior, pre-warmed instances, scale limits, and cost model for each plan.

**3. Microsoft Learn — Choose an Azure compute service**
https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree
Azure Architecture Center decision tree for selecting between VMs, App Service, Functions, Container Apps, AKS, and other compute services based on workload characteristics — the authoritative reference for compute service selection questions.

---

## Required Reading Resources

- Azure Virtual Machines overview: learn.microsoft.com/en-us/azure/virtual-machines/overview
- App Service overview: learn.microsoft.com/en-us/azure/app-service/overview
- Azure Functions overview: learn.microsoft.com/en-us/azure/azure-functions/functions-overview
- Azure Container Instances: learn.microsoft.com/en-us/azure/container-instances/container-instances-overview
- Azure Kubernetes Service: learn.microsoft.com/en-us/azure/aks/intro-kubernetes
- Microsoft Learn AZ-900 compute module: learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/

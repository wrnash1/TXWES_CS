# Video Script: Module 07 — Azure Compute Services

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Microsoft Azure Fundamentals (AZ-900)

---

## Opening (0:00–1:00)

Welcome back to CIS-4331 Azure Cloud Computing at Texas Wesleyan University. I'm Professor Nash, and today we are covering Module 07: Azure Compute Services.

Compute is at the heart of everything you do in the cloud. Whether you are running a web application, processing data, containerizing microservices, or writing serverless event-driven functions — Azure compute services are what make it possible. By the end of this session, you will understand the major compute options available in Azure, when to use each one, and how they map to real-world scenarios you will encounter on the AZ-900 exam.

Let's get into it.

---

## Section 1: Azure Virtual Machines (1:00–5:30)

### What Is a Virtual Machine?

An Azure Virtual Machine, or VM, is an Infrastructure-as-a-Service offering. That means Microsoft manages the physical hardware — the servers, the networking, the data center — but you are responsible for the operating system, the runtime, the middleware, and your applications.

Think of it like renting an apartment. The building owner handles plumbing, roofing, and the foundation. You are responsible for what is inside your unit.

VMs are ideal when you need:

- Full control over the operating system configuration
- Custom software that cannot run in a managed service
- Lift-and-shift migrations from on-premises environments

### VM Sizing

Azure organizes VMs into families or series based on workload type. Here are the major ones you need to know.

**General Purpose** — Balanced CPU-to-memory ratio. Use these for development, testing, and small-to-medium databases. Examples: D-series, B-series (burstable).

**Compute Optimized** — High CPU-to-memory ratio. Use for batch processing, web servers, analytics. Example: F-series.

**Memory Optimized** — High memory-to-CPU ratio. Use for large relational databases, in-memory caches. Examples: E-series, M-series.

**Storage Optimized** — High disk throughput and I/O. Use for Big Data, SQL, and NoSQL databases. Example: L-series.

**GPU** — Specialized for graphics rendering and machine learning training. Example: N-series.

[SHOW AZURE PORTAL] Navigate to Virtual Machines > Create. Point out the Size selector, show the filter by workload type, and highlight the vCPU/RAM/cost columns. Filter to show only D-series. Point out the cost-per-hour estimate.

### Availability Sets

One of the most critical topics for the AZ-900 exam is high availability. What happens if the physical server hosting your VM fails?

An Availability Set protects against two types of failures.

**Fault Domains** — A fault domain is a group of hardware that shares a common power source and network switch. Azure spreads your VMs across up to 3 fault domains. If one rack loses power, your other VMs are unaffected.

**Update Domains** — When Azure performs planned maintenance, it restarts VMs in one update domain at a time. Your VMs are spread across up to 20 update domains, so your application stays running during maintenance windows.

Key rule: VMs in an Availability Set must be in the same region and same datacenter. This provides rack-level fault isolation but not geographic redundancy.

[SHOW AZURE PORTAL] Navigate to Virtual Machines > Create > Availability Options dropdown. Show the difference between Availability Set, Availability Zone, and No Infrastructure Redundancy options.

### Availability Zones

Availability Zones are physically separate datacenters within the same Azure region. Each zone has its own power, cooling, and networking. Azure recommends at least three zones per region.

When you deploy a VM to an Availability Zone, you are protected against an entire datacenter failure — not just a rack failure.

The SLA for VMs deployed across Availability Zones is 99.99%, versus 99.95% for VMs in an Availability Set.

### Virtual Machine Scale Sets

What happens when your application gets too much traffic for a single VM? You need to scale out — add more VMs automatically. That is what Scale Sets do.

An Azure Virtual Machine Scale Set allows you to deploy and manage a group of identical, load-balanced VMs. Key features include:

- Auto-scaling based on CPU, memory, or custom metrics
- Support for up to 1,000 VM instances (or 600 for custom images)
- Integration with Azure Load Balancer and Application Gateway
- Rolling upgrades — update VMs in batches without downtime

[SHOW AZURE PORTAL] Navigate to Virtual Machine Scale Sets > Create. Show the scaling policy tab. Point out the minimum, maximum, and default instance counts. Show the scale-out rule builder using CPU percentage threshold.

---

## Section 2: Azure App Service (5:30–9:00)

### What Is App Service?

Azure App Service is a Platform-as-a-Service compute option for hosting web applications, REST APIs, and mobile backends. With App Service, you do not manage the underlying VMs, operating systems, or runtime patches. You deploy your code and Azure handles the rest.

Supported runtimes include .NET, Java, Node.js, Python, PHP, and Ruby. You can deploy from GitHub, Azure DevOps, local Git, or a container image.

### App Service Plans

Your App Service app runs on an App Service Plan, which defines the underlying compute resources. Plans are organized into pricing tiers.

**Free and Shared tiers** — Development and testing only. Your app shares resources with other customers. No SLA is provided.

**Basic tier** — Dedicated compute. Supports custom domains and SSL. No auto-scaling.

**Standard tier** — Production workloads. Adds auto-scaling, deployment slots, and daily backups.

**Premium tier** — Enhanced performance, more scale instances, VNet integration, and larger storage.

**Isolated tier** — Maximum isolation. The app runs in a dedicated Azure Virtual Network called an App Service Environment. Used for highly regulated industries that require private network isolation.

[SHOW AZURE PORTAL] Navigate to App Service > Create. Walk through the runtime stack dropdown. Show the App Service Plan selector and the pricing tiers comparison view. Point out the SKU and size selection. Highlight the monthly cost estimate.

### Deployment Slots

Deployment slots are a powerful feature available on Standard tier and above. They allow you to deploy a new version of your application to a staging slot, test it in a production-like environment, and then swap the staging slot with production — with zero downtime.

If something goes wrong after the swap, you can swap back immediately. This is called a blue/green deployment pattern.

---

## Section 3: Azure Functions (9:00–12:00)

### Serverless Compute

Azure Functions is a serverless compute service. You write a function — a small piece of code — and Azure handles provisioning, scaling, and infrastructure. You are billed only for the time your function is executing and the number of executions.

This is the extreme end of the managed service spectrum. Functions are event-driven: they run in response to HTTP requests, timer schedules, messages from a queue, changes in a database, or new files uploaded to storage.

### When to Use Functions

Azure Functions are ideal for:

- Short-lived tasks that complete in seconds or minutes
- Event processing pipelines
- Scheduled automation tasks such as nightly report generation
- Lightweight APIs where you pay per request

Azure Functions are NOT ideal for:

- Long-running processes that exceed the default execution timeout
- Applications requiring complex state management
- Workloads requiring persistent connections or real-time sockets

### Hosting Plans for Functions

Azure Functions has three hosting plans you should know for AZ-900.

**Consumption Plan** — Fully serverless. Scales to zero when idle. You pay only when code runs. One million free executions per month are included. This is the default and most cost-effective option for unpredictable workloads.

**Premium Plan** — Pre-warmed instances eliminate cold starts. Supports VNet integration and longer execution timeouts. Best for latency-sensitive functions.

**Dedicated (App Service) Plan** — Functions run on your existing App Service plan. Useful when you want predictable costs and already pay for idle App Service capacity.

[SHOW AZURE PORTAL] Navigate to Function App > Create. Show the Hosting Plan dropdown. Point out the Runtime Stack options. Show the region selector. After creation, show the Functions list and the code + test editor for an HTTP trigger function. Run a test request and show the response in the portal.

---

## Section 4: Azure Container Instances (12:00–15:00)

### Containers vs. Virtual Machines

Before we talk about Azure Container Instances, let's ground ourselves on what a container is. Containers package application code with its dependencies — libraries, frameworks, and runtime — into a portable unit. Unlike VMs, containers share the host operating system kernel, which makes them much lighter and faster to start.

The leading container runtime is Docker. Container images are stored in registries such as Azure Container Registry or Docker Hub.

### Azure Container Instances

Azure Container Instances, or ACI, is the fastest and simplest way to run a container in Azure — with no virtual machine management required.

ACI is ideal for:

- Simple tasks and batch jobs
- Build agents in CI/CD pipelines
- Development and testing environments
- Short-lived workloads that need an isolated container environment

Key characteristics of ACI:

- Containers start in seconds
- Billed per second of execution
- Supports both Linux and Windows containers
- Can mount Azure File Shares for persistent storage
- No orchestration complexity — just run one container or a small group

What ACI does NOT provide: it does not orchestrate containers across multiple hosts, does not manage failover across nodes, and does not provide advanced networking between dozens of microservices. For those needs, you require Kubernetes.

[SHOW AZURE PORTAL] Navigate to Container Instances > Create. Show the image source options: Docker Hub, Azure Container Registry, and private registry. Show the CPU and memory allocation fields. Show the networking tab and the DNS name label option. Point out Restart Policy options: Always, On Failure, and Never.

---

## Section 5: Azure Kubernetes Service Overview (15:00–18:30)

### What Is Kubernetes?

Kubernetes — often abbreviated K8s — is an open-source container orchestration platform. It automates deploying, scaling, and operating containerized applications across a cluster of machines.

When you have dozens or hundreds of containers that need to communicate, self-heal, scale independently, and receive rolling updates — that is when you need Kubernetes.

### Azure Kubernetes Service

Azure Kubernetes Service, or AKS, is Microsoft's managed Kubernetes offering. Azure manages the Kubernetes control plane — the scheduler, API server, and etcd database — at no additional cost. You pay only for the worker node VMs that run your containers.

Key AKS concepts for AZ-900:

**Cluster** — The entire AKS deployment, consisting of a control plane and one or more node pools.

**Node** — A VM in the cluster that runs your workloads.

**Pod** — The smallest deployable unit in Kubernetes. A pod wraps one or more containers that share networking and storage.

**Deployment** — A Kubernetes object that manages a desired state for a set of replicated pods.

**Service** — Exposes pods to network traffic, either internally within the cluster or externally via a public load balancer.

### When to Use AKS vs. ACI

Use ACI when you have a simple, short-lived container job with no orchestration requirements and you need fast startup with minimal configuration.

Use AKS when you are running a microservices architecture, need auto-scaling across a fleet of containers, require rolling deployments with zero downtime, or need production-grade container orchestration.

[SHOW AZURE PORTAL] Navigate to Kubernetes Services > Create. Show the cluster preset configurations: Dev/Test versus Production. Show the node pool configuration — VM size, node count, and auto-scaling range. Point out the Networking tab showing Container Network Interface plugin options. Show the Monitoring tab with Azure Monitor and Container Insights integration.

---

## Section 6: Choosing the Right Compute Service (18:30–20:30)

One of the most common AZ-900 exam question patterns is: given a scenario, which compute service should be used? Here is a simple decision framework.

**Do you need full OS control or custom software with special OS-level configuration?** Use Virtual Machines.

**Are you deploying a web app, REST API, or mobile backend and do NOT want to manage infrastructure?** Use App Service.

**Do you have event-driven, short-lived code triggered by HTTP requests, timers, or messages?** Use Azure Functions.

**Do you need to quickly run a single container without managing infrastructure?** Use Azure Container Instances.

**Are you running a complex multi-container microservices application that needs orchestration, auto-scaling, and self-healing?** Use Azure Kubernetes Service.

Memorize this decision framework. It will help you on both the exam and in your career when advising stakeholders on the right architecture.

---

## Closing (20:30–21:30)

Let's recap what we covered today. We walked through Azure Virtual Machines — sizing families, availability sets, availability zones, and scale sets. We explored Azure App Service as a PaaS web hosting platform with deployment slots for zero-downtime releases. We covered Azure Functions for serverless, event-driven workloads. We introduced Azure Container Instances for fast, simple container execution. And we got an overview of Azure Kubernetes Service for production container orchestration.

In your lab this week, you will create a virtual machine using the Azure portal and deploy a simple web app using Azure App Service — hands-on practice with the two most foundational compute services.

In your quiz, watch for questions about the difference between fault domains and update domains, the SLA percentages for availability options, and the right compute service for a given scenario.

See you in Module 08, where we cover Azure Networking. Take care.

---

*End of Script — Module 07*

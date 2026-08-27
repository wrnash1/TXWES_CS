# Reading Guide: Module 04 - Azure Container Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## Introduction

Containers have become the dominant application packaging and deployment mechanism in cloud computing. Understanding containers and Azure's container services is essential for AZ-900 and for any cloud practitioner role. This module covers the conceptual foundation of containers and the specific Azure services that run, orchestrate, and store them.

---

## Section 1: Container Fundamentals

### 1.1 What Is a Container?

A container is a standard unit of software that packages an application's code along with all its dependencies — libraries, configuration files, environment variables, and runtime — into a portable, self-contained bundle. Unlike a virtual machine, a container does not include a complete operating system. Instead, containers share the host OS kernel while being isolated from each other using Linux kernel features (namespaces and cgroups).

The result: containers are significantly lighter and faster than VMs while still providing process isolation.

### 1.2 VM vs. Container Architecture

| Characteristic | Virtual Machine | Container |
|---|---|---|
| OS included | Full guest OS | No — shares host OS kernel |
| Startup time | 1-5 minutes | 1-10 seconds |
| Image size | Gigabytes (10-100+ GB) | Megabytes (50-500 MB typical) |
| Isolation | Hypervisor-level | OS namespace/cgroup level |
| Density per host | Tens | Hundreds |
| Portability | Limited (OS version specific) | High (runs anywhere Docker runs) |
| Overhead | High (full OS per VM) | Low (shared kernel) |

### 1.3 Docker Terminology

| Term | Definition |
|---|---|
| Docker | The most common container platform; defines the container image format and runtime |
| Dockerfile | A text file containing build instructions for creating a container image |
| Image | A read-only template for creating containers; built from a Dockerfile |
| Container | A running instance of an image |
| Registry | A storage service for container images (Docker Hub, Azure Container Registry) |
| Repository | A collection of related images with different tags within a registry |
| Tag | A label on an image indicating a version (e.g., myapp:v2.1) |

### 1.4 Container Lifecycle

A container follows this lifecycle:

- Build: Create an image from a Dockerfile
- Push: Upload the image to a registry
- Pull: Download the image from a registry to a runtime environment
- Run: Start a container instance from the image
- Stop: Halt the running container process
- Remove: Delete the container instance (image remains in registry)

---

## Section 2: Azure Container Instances (ACI)

### 2.1 Overview

Azure Container Instances is the fastest, simplest way to run containers in Azure. It is a serverless container service — Microsoft manages all underlying infrastructure. You specify a container image, resource requirements (CPU, memory), and network configuration, and Azure runs the container within seconds.

### 2.2 ACI Key Characteristics

- Serverless: no VM or cluster to provision or manage
- Per-second billing (vCPU-seconds and GB-seconds of memory)
- Supports both Linux and Windows containers
- Public or private networking
- Persistent storage through Azure File Shares (SMB mount)
- Container groups: run multiple containers on the same host, sharing IP and storage
- Maximum resources per container group: 4 vCPUs, 16 GB RAM (region-dependent)

### 2.3 When to Use ACI

Appropriate use cases:

- Single container deployments without orchestration requirements
- Batch processing and data transformation jobs
- CI/CD pipeline steps (build agents, test runners)
- Rapid prototyping and development testing
- Short-lived background tasks
- Event-driven tasks that need to scale rapidly

Not appropriate for:

- Applications requiring automatic container restart and self-healing at scale
- Multi-container microservices with complex networking
- Production workloads requiring rolling updates and zero-downtime deployment
- Long-running services requiring SLA guarantees

### 2.4 ACI Pricing Model

ACI charges based on actual resource consumption:

- vCPU billed per second of usage
- Memory billed per GB per second
- No minimum charge — if the container runs for 10 seconds, you pay for 10 seconds

This makes ACI extremely cost-effective for short-running workloads that would be expensive on a VM billed by the hour.

---

## Section 3: Azure Kubernetes Service (AKS)

### 3.1 Kubernetes Concepts

Kubernetes (K8s) is the industry-standard open-source container orchestration platform, originally developed by Google and now maintained by the Cloud Native Computing Foundation (CNCF).

| Concept | Definition |
|---|---|
| Cluster | A set of worker nodes managed by a control plane |
| Control Plane | Manages cluster state: API server, scheduler, etcd, controller manager |
| Node | A VM running the Kubernetes kubelet agent and container runtime |
| Pod | Smallest deployable unit; one or more containers sharing network and storage |
| Deployment | Declares desired state (e.g., run 3 replicas of this pod) |
| Service | Stable network endpoint for a set of pods |
| Namespace | Virtual cluster within a cluster for resource isolation |
| Ingress | HTTP/S routing rules for external access to services |
| ConfigMap | Key-value store for non-secret configuration data |
| Secret | Encrypted storage for sensitive configuration data |

### 3.2 AKS Architecture

Azure Kubernetes Service provides a managed Kubernetes control plane.

Microsoft manages (free of charge):

- Kubernetes API server
- etcd cluster state database
- Kubernetes scheduler
- Controller manager
- Health monitoring and automatic repair of control plane components

Customer manages (billed):

- Worker node VMs (node pools)
- Container images and deployments
- Network configuration
- Storage provisioning
- RBAC policies

### 3.3 AKS Key Features

- Node pools: Groups of VMs with the same configuration. A cluster can have multiple node pools.
- Cluster Autoscaler: Automatically adds nodes when pods cannot be scheduled due to insufficient capacity, and removes nodes when utilization is low.
- Horizontal Pod Autoscaler: Automatically scales pod replicas based on CPU, memory, or custom metrics.
- Azure CNI networking: Integrates pods directly into Azure Virtual Network.
- Entra ID integration: Authentication for kubectl access.
- Azure Monitor for containers: Metrics and log collection for pods and nodes.

### 3.4 When to Use AKS

Appropriate use cases:

- Microservices architectures with many interdependent services
- Applications requiring zero-downtime rolling updates
- Workloads needing fine-grained resource management across many containers
- Organizations adopting a Kubernetes-standard platform
- Production applications requiring strong availability guarantees

Not appropriate for:

- Simple single-container deployments (use ACI instead)
- Teams without Kubernetes expertise or time to learn it
- Small applications where AKS management overhead exceeds the benefit

---

## Section 4: Azure Container Apps

### 4.1 Overview

Azure Container Apps is a fully managed serverless container platform built on Kubernetes, KEDA (Kubernetes Event-Driven Autoscaling), and Envoy proxy. It provides Kubernetes-level capabilities without requiring users to manage or interact with Kubernetes directly.

### 4.2 Container Apps Key Features

| Feature | Description |
|---|---|
| Scale-to-zero | No containers run when there is no traffic; billing stops completely |
| Event-driven scaling | Scale based on queue depth, topic subscriptions, HTTP requests |
| Dapr integration | Built-in support for Dapr sidecar pattern |
| Traffic splitting | Route a percentage of traffic to different container versions |
| Revision management | Each deployment creates a new revision with easy rollback |
| Environment | Shared boundary for multiple container apps with shared networking |

### 4.3 Container Apps vs. AKS vs. ACI

| Feature | ACI | Container Apps | AKS |
|---|---|---|---|
| Kubernetes knowledge needed | None | None | Required |
| Scale to zero | Not native | Yes | Yes (with KEDA) |
| Multi-container orchestration | Container groups | Yes | Yes |
| Custom Kubernetes objects | No | No | Yes |
| Maximum flexibility | Low | Medium | High |
| Management overhead | Minimal | Low | High |

---

## Section 5: Azure App Service for Containers

### 5.1 Container Support in App Service

Azure App Service supports running Docker containers as an alternative to deploying application code directly. App Service manages the OS, web server infrastructure, TLS, auto-scaling, and deployment slots.

Supported container configurations:

- Single Docker container from a public registry or ACR
- Docker Compose (multi-container) configurations
- Windows containers for legacy .NET Framework workloads

### 5.2 App Service Containers vs. AKS

| Factor | App Service with Container | AKS |
|---|---|---|
| Single web app or API | Excellent fit | Overkill |
| Familiar App Service features | Preserved | Requires separate tooling |
| Multiple microservices | Poor fit | Excellent fit |
| Kubernetes-native features | Not available | Available |
| Teams new to containers | Good transition path | Steep learning curve |

---

## Section 6: Azure Container Registry (ACR)

### 6.1 Purpose

Azure Container Registry is a private, managed Docker-compatible container image registry. It serves as a secure, centralized repository for container images used in Azure deployments.

### 6.2 ACR Key Features

| Feature | Description |
|---|---|
| Private registry | Images are not publicly accessible; requires authentication |
| Geo-replication | Replicate image repositories to multiple Azure regions |
| Azure AD integration | Entra ID service principals and managed identities for access |
| Vulnerability scanning | Microsoft Defender for Containers scans images for known CVEs |
| Webhooks | Trigger CI/CD pipelines on image push events |
| Build tasks | Build container images in Azure from source code or Dockerfiles |
| Content trust | Sign images for verification before deployment |

### 6.3 ACR Service Tiers

| Tier | Storage | Features |
|---|---|---|
| Basic | 10 GB | Development, testing |
| Standard | 100 GB | Production most cases |
| Premium | 500 GB | Geo-replication, private link, content trust |

---

## Section 7: Azure CLI Commands for Containers

```bash
# Create a resource group for container labs
az group create --name "lab04-rg" --location "eastus"

# Deploy a container instance
az container create \
  --resource-group "lab04-rg" \
  --name "mycontainer" \
  --image "mcr.microsoft.com/azuredocs/aci-helloworld" \
  --dns-name-label "myapp-uniquesuffix" \
  --ports 80

# Show container status and FQDN
az container show \
  --resource-group "lab04-rg" \
  --name "mycontainer" \
  --query "{Status:instanceView.state,FQDN:ipAddress.fqdn}" \
  --output table

# View container logs
az container logs \
  --resource-group "lab04-rg" \
  --name "mycontainer"

# Restart a container
az container restart \
  --resource-group "lab04-rg" \
  --name "mycontainer"

# Delete a container instance
az container delete \
  --resource-group "lab04-rg" \
  --name "mycontainer" \
  --yes

# Create an Azure Container Registry
az acr create \
  --resource-group "lab04-rg" \
  --name "myacrlab04" \
  --sku Basic

# List repositories in ACR
az acr repository list \
  --name "myacrlab04" \
  --output table
```

Reference: learn.microsoft.com/en-us/cli/azure/container

---

## Section 8: Container Services Summary Table

| Service | Type | Managed Components | Customer Manages | Best For |
|---|---|---|---|---|
| Azure Container Instances | Serverless | Everything | Container image, config | Simple, fast container runs |
| Azure Container Apps | Serverless | K8s, KEDA, networking | App config, scaling rules | Microservices, event-driven |
| Azure App Service (container) | PaaS | OS, web server, scaling | Container image, app config | Web apps/APIs in containers |
| Azure Kubernetes Service | Managed K8s | Control plane | Worker nodes, deployments | Complex orchestration |
| Azure Container Registry | Registry | Storage, geo-replication | Images, access policies | Private image storage |

---

## Section 9: AZ-900 Exam Tips

1. **ACI for simplicity:** When an exam scenario describes running a single container without managing infrastructure, the answer is Azure Container Instances. Key signals: "simple," "no orchestration," "quick," "batch."

2. **AKS for orchestration:** When a scenario describes multiple interdependent microservices, rolling updates, or Kubernetes-native features, the answer is AKS. Key signals: "microservices," "orchestration," "zero-downtime updates."

3. **Container Apps in scenarios:** Container Apps answers scenarios involving event-driven scaling and scale-to-zero without Kubernetes management. Key signals: "scale to zero," "no Kubernetes management," "event-driven."

4. **ACR is not a compute service:** ACR stores images — it does not run containers. Do not select ACR as the answer for a container deployment scenario.

5. **AKS control plane cost:** AKS does not charge for the managed control plane. You pay only for worker node VMs. This makes AKS cost-competitive with self-managed Kubernetes.

6. **Container vs. VM service model:** ACI and Container Apps are PaaS — you do not manage the OS. AKS worker nodes are IaaS — you choose and manage the VM size for nodes.

7. **Container isolation vs. VM isolation:** Containers provide OS-level isolation (shared kernel). VMs provide hardware-level isolation (separate kernel per VM). VMs provide stronger security isolation for multi-tenant environments.

8. **Immutability principle:** A container best practice is immutability — never modify a running container; build a new image instead. The exam may test awareness of this principle.

---

## Section 10: Required Resources

- Azure Container Instances: learn.microsoft.com/en-us/azure/container-instances/container-instances-overview
- Azure Kubernetes Service: learn.microsoft.com/en-us/azure/aks/intro-kubernetes
- Azure Container Apps: learn.microsoft.com/en-us/azure/container-apps/overview
- Azure Container Registry: learn.microsoft.com/en-us/azure/container-registry/container-registry-intro
- Microsoft Learn AZ-900 compute module: learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/

---

## Section 11: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the Container Services Summary Table (Section 8)
- [ ] Understand all CLI commands in Section 7
- [ ] Complete the Microsoft Learn "Describe Azure compute and networking services" module
- [ ] Complete Lab Activity Module 04
- [ ] Take Quiz Module 04
- [ ] Post Discussion Module 04 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft Learn — Azure Container Instances documentation**
https://learn.microsoft.com/en-us/azure/container-instances/container-instances-overview
Complete ACI reference including container group concepts, restart policies, VNet integration, persistent volume mounts, and per-second billing details.

**2. Microsoft Learn — Azure Kubernetes Service core concepts**
https://learn.microsoft.com/en-us/azure/aks/concepts-clusters-workloads
In-depth explanation of AKS clusters, node pools, pods, Deployments, Services, and the free managed control plane — the foundational concepts for understanding AKS architecture and cost model.

**3. Microsoft Learn — Azure Container Apps overview**
https://learn.microsoft.com/en-us/azure/container-apps/overview
Covers Container Apps environments, scale rules, KEDA-based event-driven autoscaling, scale-to-zero behavior, and the distinction between Container Apps and AKS for teams choosing between managed and unmanaged Kubernetes.

# Video Script: Module 04 - Azure Container Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 20-24 minutes
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## [00:00 - 01:30] Opening and Learning Objectives

**[INSTRUCTOR ON CAMERA — title card: "Module 04: Azure Container Services"]**

Welcome to Module 04. I'm Professor Nash. Today we cover containers — one of the most transformative technologies in modern cloud computing. If virtual machines from Module 03 are like renting a full apartment, containers are like renting a single furnished room. They are faster to start, more efficient to run, and perfectly portable between environments.

Azure provides multiple container services targeting different use cases, from running a single container to orchestrating thousands of microservices. AZ-900 tests your ability to distinguish these services and match them to scenarios.

By the end of this module you will be able to:

- Explain what a container is and how it differs from a virtual machine
- Describe Azure Container Instances and when to use it
- Describe Azure Kubernetes Service and its purpose
- Identify Azure App Service as a container-capable PaaS platform
- Explain the purpose of Azure Container Registry
- Choose between container services based on a scenario

---

## [01:30 - 05:00] What Is a Container?

**[SLIDE: "Containers vs. Virtual Machines"]**

A container is a lightweight, isolated package containing an application and all its dependencies — libraries, configuration files, and runtime — but sharing the host operating system's kernel. Containers do not include a full OS; they borrow the OS from the host. This makes them dramatically smaller and faster to start than VMs.

Here is the key comparison:

A virtual machine virtualizes hardware. It runs a complete guest OS on top of a hypervisor. A VM image for Ubuntu might be 20 GB. Starting a VM takes 1-5 minutes.

A container virtualizes the operating system runtime. It runs a process directly on the host OS kernel, isolated using Linux namespaces and cgroups. A container image for a Python web application might be 200 MB. Starting a container takes 1-5 seconds.

**[SLIDE: "Container Benefits"]**

The operational benefits that drive container adoption:

**Portability:** A container image built on a developer's laptop runs identically on a test server, in Azure Container Instances, or in Azure Kubernetes Service. The container packages the application and its dependencies — the classic "works on my machine" problem is eliminated.

**Density:** Because containers share the host OS, a single physical server or VM can run hundreds of containers simultaneously. VMs would be limited to tens of instances on the same hardware.

**Fast startup:** Containers start in seconds. This enables rapid scaling, rapid deployment, and rapid recovery from failures.

**Immutability:** Container images are built from a Dockerfile — a declarative script. Every instance of the image is identical. Updating means building a new image and deploying it, not patching individual servers.

**[SLIDE: "Docker — The Container Standard"]**

Docker is the technology that standardized the container format. A **Docker image** is the read-only template from which containers are run. A **Dockerfile** is the build script that defines the image. A **container registry** stores and serves Docker images.

You do not need deep Docker expertise for AZ-900, but you should understand these three terms.

---

## [05:00 - 09:00] Azure Container Instances

**[SLIDE: "Azure Container Instances (ACI)"]**

Azure Container Instances is the simplest way to run a single container in Azure. It is a serverless container service — you provide a container image, and Azure runs it without you managing any VMs, orchestrators, or clusters.

ACI is ideal for:

- Quick, on-demand container execution
- Simple applications that consist of a single container
- Batch jobs or scheduled tasks that need to run in a container
- Development and testing of container images
- Scenarios where you need a container running in seconds, not minutes

ACI is not suitable for:

- Multi-container applications with complex inter-service communication
- Applications requiring persistent storage that survives container restarts
- Production workloads requiring self-healing, auto-scaling, and rolling updates

**[SHOW CODE — Azure CLI: az container create]**

Here is how to deploy a container using Azure CLI:

```bash
az container create \
  --resource-group "lab04-rg" \
  --name "mycontainer" \
  --image "mcr.microsoft.com/azuredocs/aci-helloworld" \
  --dns-name-label "lab04-[your-initials]" \
  --ports 80
```

This deploys Microsoft's sample "Hello World" container, assigns a DNS name, and exposes port 80. The container is publicly accessible within about 30 seconds.

To check the status:

```bash
az container show \
  --resource-group "lab04-rg" \
  --name "mycontainer" \
  --query "{Status:instanceView.state, FQDN:ipAddress.fqdn}" \
  --output table
```

To view container logs:

```bash
az container logs \
  --resource-group "lab04-rg" \
  --name "mycontainer"
```

**[SLIDE: "ACI Billing Model"]**

ACI uses per-second billing based on vCPU and memory consumed while the container is running. There is no VM to manage and no hourly minimum. This makes ACI very cost-effective for short-running or burst workloads.

---

## [09:00 - 14:00] Azure Kubernetes Service

**[SLIDE: "The Problem ACI Cannot Solve"]**

Azure Container Instances works well for single containers. But modern applications are typically composed of multiple services — a web frontend, an API backend, a cache, a message queue, a worker process. Managing these containers manually — knowing when to restart failed containers, how to route traffic between them, how to roll out updates without downtime — becomes operationally complex very quickly.

Container orchestration solves this. And Kubernetes is the industry-standard orchestration platform.

**[SLIDE: "Kubernetes Concepts"]**

Kubernetes is an open-source platform for automating container deployment, scaling, and management. Key Kubernetes concepts you need for AZ-900:

**Pod:** The smallest deployable unit in Kubernetes. A pod contains one or more containers that share network and storage. Typically, one container per pod.

**Node:** A virtual machine (or physical server) that runs pods. Nodes form a cluster.

**Cluster:** A group of nodes managed by a Kubernetes control plane.

**Control Plane:** The management layer that makes scheduling decisions, monitors cluster state, and responds to events (like a pod crashing). In AKS, Microsoft manages the control plane for you.

**Deployment:** A Kubernetes object that declares how many replicas of a pod should run. Kubernetes maintains that replica count automatically.

**Service:** A stable network endpoint that routes traffic to pods. Pods are ephemeral; Services provide a consistent IP address for accessing them.

**[SLIDE: "Azure Kubernetes Service (AKS)"]**

Azure Kubernetes Service is a managed Kubernetes offering. Microsoft manages the control plane — the API server, scheduler, and etcd database — at no additional charge. You pay only for the worker node VMs that run your application containers.

AKS benefits:

- No control plane management overhead
- Integrated with Azure Active Directory (Entra ID) for authentication
- Integrated with Azure Monitor for container health monitoring
- Supports cluster autoscaling (automatically adds/removes worker nodes)
- Zone-redundant node pools for high availability

AKS is the right choice for:

- Microservices architectures with many interdependent containers
- Production workloads requiring self-healing, auto-scaling, and zero-downtime deployments
- Teams with Kubernetes expertise or a desire to build it

**[SHOW PORTAL — Navigate to AKS in Azure Portal, show cluster creation overview]**

In the Portal, creating an AKS cluster requires selecting a node pool configuration — you are choosing the VM size and count for the worker nodes. Microsoft creates and manages the control plane nodes automatically, outside the worker node pool.

---

## [14:00 - 17:00] Azure Container Apps and Azure App Service

**[SLIDE: "Azure Container Apps"]**

Azure Container Apps is a newer service that sits between ACI and AKS in complexity. It is a fully managed Kubernetes-based environment, but you do not interact with Kubernetes directly. Container Apps provides:

- Automatic scaling to zero (no containers running when there is no traffic)
- Built-in traffic routing and load balancing
- Support for microservices communication (Dapr integration)
- Event-driven scaling (scale based on queue depth, HTTP requests, etc.)

Container Apps is the right choice for teams who want Kubernetes-level orchestration without Kubernetes expertise.

**[SLIDE: "Azure App Service for Containers"]**

Azure App Service, which we introduced as a PaaS service in Module 01, also supports container deployment. You can deploy a Docker container to App Service instead of (or alongside) deploying application code directly. App Service provides:

- Managed OS, TLS certificates, autoscaling, and deployment slots
- Custom domains and built-in authentication
- Familiar App Service management interface

App Service containers are suitable for web applications and APIs packaged as single containers where you want App Service's management features.

---

## [17:00 - 19:30] Azure Container Registry

**[SLIDE: "Azure Container Registry (ACR)"]**

Azure Container Registry is a private Docker container image registry hosted in Azure. Think of it as a private version of Docker Hub — a secure repository for your organization's container images.

Why use ACR instead of Docker Hub?

- Images stay within your Azure tenant — no public exposure
- Integrates with Azure Active Directory for access control
- Geo-replication replicates images to multiple regions for low-latency pulls
- Integrates directly with AKS and ACI — deploy directly from the registry
- Vulnerability scanning (using Microsoft Defender for Containers)

**[SLIDE: "Container Services Summary Table"]**

| Service | Complexity | Use Case | Kubernetes Knowledge Needed |
|---|---|---|---|
| Azure Container Instances | Lowest | Single container, dev/test, batch | None |
| Azure Container Apps | Low-Medium | Microservices, event-driven, scale-to-zero | None |
| Azure App Service (containers) | Low | Web apps packaged as containers | None |
| Azure Kubernetes Service | High | Complex microservices, enterprise production | Required |
| Azure Container Registry | N/A (registry) | Private image storage for any service | None |

---

## [19:30 - 22:00] Lab Preview and AZ-900 Alignment

**[SLIDE: "Module 04 Lab"]**

In today's lab you will:

1. Create an Azure Container Instance using Azure CLI
2. Verify the container is running using `az container show`
3. Access the container's web endpoint through a browser
4. View container logs using `az container logs`
5. Delete the container and clean up resources

The entire lab takes less than 10 minutes to deploy because containers start in seconds rather than minutes. This speed is the core reason containers have become so dominant in modern cloud architecture.

**[SLIDE: "AZ-900 Exam Tips for Containers"]**

Remember these distinctions for exam day:

- ACI: single containers, no orchestration, serverless, per-second billing
- AKS: multi-container orchestration, managed control plane, worker nodes are customer-managed VMs
- Container Apps: serverless Kubernetes, scale-to-zero, no Kubernetes knowledge needed
- ACR: private image registry — not a compute service

The exam will give you scenarios and ask which service is appropriate. Match the complexity of the scenario to the complexity of the service.

---

## [22:00 - 24:00] Closing

**[INSTRUCTOR ON CAMERA]**

You now understand Azure's container landscape — from the simplicity of Azure Container Instances to the power of Azure Kubernetes Service. Containers are a fundamental skill in modern cloud computing, and understanding when to use each service is exactly the kind of architectural judgment that AZ-900 tests.

In Module 05, we cover Azure Virtual Networking — virtual networks, subnets, Network Security Groups, and how Azure connects resources to each other and to the internet. Networking is the connective tissue that makes all these compute services work together.

I will see you in Module 05.

---

**References:**

- learn.microsoft.com/en-us/azure/container-instances/container-instances-overview
- learn.microsoft.com/en-us/azure/aks/intro-kubernetes
- learn.microsoft.com/en-us/azure/container-apps/overview
- learn.microsoft.com/en-us/azure/container-registry/container-registry-intro

# Quiz: Module 04 - Azure Container Services

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A developer needs to run a single Docker container in Azure for a 10-minute batch processing job. No infrastructure management is required. Which Azure service is most appropriate?

- A) Azure Kubernetes Service
- B) Azure Container Instances
- C) Azure Virtual Machines
- D) Azure App Service

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Container Instances is the serverless container service designed for exactly this use case — running a single container quickly without managing infrastructure. Its per-second billing makes it cost-effective for short-duration jobs like a 10-minute batch task.
- *Why A is incorrect:* AKS requires creating and managing a cluster of worker node VMs. The overhead of setting up a cluster for a single 10-minute job far exceeds the benefit. AKS is designed for long-running, multi-container production workloads.
- *Why C is incorrect:* A VM requires OS management, takes 1-5 minutes to start, and is billed by the hour. Running a 10-minute job on a VM is operationally heavy and cost-inefficient compared to ACI.
- *Why D is incorrect:* App Service is designed for web applications and APIs with continuous availability. It is not suited for on-demand batch container execution and does not offer per-second billing for short jobs.

---

## Question 2

Which component in Kubernetes represents the smallest deployable unit and can contain one or more containers sharing network and storage?

- A) Node
- B) Deployment
- C) Service
- D) Pod

**Correct Answer:** D

**Distractor Analysis:**

- *Why D is correct:* A Pod is the smallest deployable unit in Kubernetes. It represents one or more tightly coupled containers that share an IP address, port space, and storage volumes. Kubernetes schedules and manages pods as a single unit.
- *Why A is incorrect:* A Node is a VM (or physical machine) that hosts pods. Nodes are not deployable application units — they are the compute infrastructure that runs pods.
- *Why B is incorrect:* A Deployment is a Kubernetes controller that manages the desired state for a set of pods (e.g., "keep 3 replicas of this pod running"). It is a higher-level construct, not the smallest unit.
- *Why C is incorrect:* A Service is a stable network endpoint that routes traffic to a set of pods. It provides a consistent IP address for accessing pods, which are ephemeral. A Service is a networking construct, not a deployable unit.

---

## Question 3

In Azure Kubernetes Service, which component does Microsoft manage at no additional charge to the customer?

- A) Worker node virtual machines
- B) Container images stored in the registry
- C) The Kubernetes control plane (API server, scheduler, etcd)
- D) Network security groups for the cluster

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* AKS provides a managed Kubernetes control plane — the API server, scheduler, controller manager, and etcd — at no charge. Microsoft is responsible for maintaining, updating, and repairing these control plane components. This is the key differentiator of AKS compared to self-managed Kubernetes.
- *Why A is incorrect:* Worker node VMs are the customer's responsibility and are billed based on the VM size and count selected for node pools. These are the primary AKS cost component.
- *Why B is incorrect:* Container images are stored in Azure Container Registry or another registry — this is outside the scope of AKS management. The customer manages image builds, pushes, and access policies.
- *Why D is incorrect:* Network Security Groups for the cluster and its subnets are managed by the customer as part of the Azure Virtual Network configuration. Microsoft does not manage customer networking resources.

---

## Question 4

A team wants to run a containerized application that automatically scales from zero instances (during off-hours with no traffic) to multiple instances during business hours, without managing Kubernetes clusters. Which Azure service is most appropriate?

- A) Azure Container Instances
- B) Azure Virtual Machine Scale Sets
- C) Azure Container Apps
- D) Azure Kubernetes Service

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Container Apps supports scale-to-zero natively — no containers run and no compute costs are incurred when there is no traffic. It is built on Kubernetes and KEDA but the customer does not interact with Kubernetes directly. This combines the operational simplicity of ACI with the orchestration capabilities of AKS.
- *Why A is incorrect:* Azure Container Instances does not natively support scale-to-zero with event-driven scaling. ACI runs containers on-demand but does not provide automatic scaling rules based on traffic — each container must be manually created and deleted.
- *Why B is incorrect:* VM Scale Sets scale VM instances, not containers. They also cannot scale to zero (minimum instance count is typically 1 for continuously available workloads). VMs also take minutes to start, unlike container seconds.
- *Why D is incorrect:* AKS can support scale-to-zero with KEDA, but it requires managing Kubernetes clusters. The scenario explicitly states no Kubernetes cluster management is desired.

---

## Question 5

How does container isolation differ from virtual machine isolation in terms of security boundaries?

- A) Containers provide stronger isolation because they include their own kernel
- B) VMs provide stronger isolation because each VM runs a separate OS kernel on a hypervisor; containers share the host OS kernel
- C) Containers and VMs provide identical isolation because both use hardware virtualization
- D) VMs provide weaker isolation because they are managed by a hypervisor, while containers run directly on hardware

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* VMs each run a separate, isolated OS kernel on top of a hypervisor. Compromising one VM's kernel does not affect other VMs. Containers share the host OS kernel — a kernel vulnerability in the host could potentially affect all containers on that host. VMs provide a stronger security boundary for multi-tenant workloads.
- *Why A is incorrect:* This reverses the correct relationship. Containers do not include their own kernel — sharing the host kernel is precisely what makes containers faster and lighter than VMs, but also what makes their isolation weaker.
- *Why C is incorrect:* Containers and VMs do not use identical isolation. VMs use hardware virtualization (hypervisor). Containers use OS-level isolation (Linux namespaces and cgroups), which is a fundamentally different and less complete isolation boundary.
- *Why D is incorrect:* The hypervisor provides strong isolation between VMs — it is a security strength, not a weakness. VMs do not run "directly on hardware" in the sense that would weaken security; the hypervisor enforces the isolation.

---

## Question 6

A company wants to store its internally developed container images privately and prevent unauthorized access. They also want images scanned for vulnerabilities before deployment. Which Azure service addresses these requirements?

- A) Azure Container Instances
- B) Azure Kubernetes Service
- C) Azure Container Registry
- D) Azure App Service

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Container Registry is a private Docker-compatible image registry. It stores images securely with Azure AD-based access control (preventing unauthorized access), supports geo-replication, and integrates with Microsoft Defender for Containers for vulnerability scanning. ACR is the Azure answer for private image storage and management.
- *Why A is incorrect:* ACI is a container runtime service — it runs containers from images. It does not store or scan images. To use ACI with a private image, you pull from ACR.
- *Why B is incorrect:* AKS is a container orchestration service. While AKS can pull from ACR, AKS itself does not store images or provide vulnerability scanning. The storage and scanning function belongs to ACR.
- *Why D is incorrect:* App Service is a web application hosting service. While it can deploy containers, it does not provide private image registry functionality or vulnerability scanning.

---

## Question 7

What is the primary billing advantage of Azure Container Instances compared to Azure Virtual Machines for short-duration workloads?

- A) ACI is always cheaper than VMs regardless of workload duration
- B) ACI charges per second of actual container execution, while VMs charge per hour of allocation
- C) ACI does not charge for network bandwidth, while VMs do
- D) ACI provides free storage, while VMs charge for managed disks

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* ACI bills per vCPU-second and GB-second of actual container execution. For a 10-minute batch job, you pay for exactly 600 seconds of compute. A VM billed hourly (even with per-minute granularity on Azure) and requiring minutes to start would cost significantly more for the same short workload.
- *Why A is incorrect:* ACI is not always cheaper. For long-running, continuously operating workloads, a VM with Reserved Instance pricing may be significantly cheaper than ACI's consumption billing. The advantage is specific to short-duration and variable workloads.
- *Why C is incorrect:* ACI does charge for outbound network bandwidth. The billing advantage is compute (per-second vs. per-hour), not network bandwidth.
- *Why D is incorrect:* ACI does not provide free storage. Container files stored in Azure Files mounts incur storage billing. The key billing advantage is the compute model, not storage.

---

## Question 8

Which Azure container service is built on Kubernetes and KEDA (Kubernetes Event-Driven Autoscaling) but does not require users to manage Kubernetes directly?

- A) Azure Container Instances
- B) Azure Kubernetes Service
- C) Azure Container Apps
- D) Azure Container Registry

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Container Apps is explicitly built on Kubernetes and KEDA as its underlying technology, but exposes a simplified abstraction layer. Users configure applications, scaling rules, and networking through the Container Apps interface without ever interacting with Kubernetes objects, kubectl, or cluster management.
- *Why A is incorrect:* Azure Container Instances is not built on Kubernetes. ACI is a separate, simpler serverless container service with no Kubernetes substrate.
- *Why B is incorrect:* AKS is Kubernetes — users interact with Kubernetes directly through kubectl, YAML manifests, and Helm charts. AKS is the managed Kubernetes service, not an abstraction over Kubernetes.
- *Why D is incorrect:* Azure Container Registry is a container image storage service with no runtime or orchestration capabilities. It is not based on Kubernetes.

---

## Question 9

A Dockerfile is used to define the instructions for building a container image. Which of the following best describes the relationship between a Dockerfile, an image, and a running container?

- A) A Dockerfile is a running container; an image is a stopped container; there is no distinction between image and container
- B) A Dockerfile is the build script; an image is the read-only template built from the Dockerfile; a container is a running instance of the image
- C) An image is the build script; a Dockerfile is the stored artifact; a container is the deployed version
- D) A container can exist without an image; images are optional optimizations for faster startup

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* This correctly describes the three-layer relationship. A Dockerfile contains build instructions (FROM, RUN, COPY, CMD directives). Building the Dockerfile produces an immutable image. Running the image creates a container — a live, isolated process. Multiple containers can be started from the same image simultaneously.
- *Why A is incorrect:* These are three distinct, separate things with different purposes. Conflating them shows a fundamental misunderstanding of the container model.
- *Why C is incorrect:* This reverses the roles of Dockerfile and image. The Dockerfile is the source/build script. The image is the built artifact stored in a registry.
- *Why D is incorrect:* Every container is started from an image. There is no way to run a container without an image — the image is the container's file system and startup configuration.

---

## Question 10

An organization is migrating a monolithic .NET Framework 4.7 application to Azure. The application requires the Windows Server operating system and cannot be refactored. The team wants to use containers for deployment consistency but does not need Kubernetes orchestration. Which deployment approach is most appropriate?

- A) Azure Container Instances with a Linux image
- B) Azure App Service with a Windows container
- C) Azure Kubernetes Service with a Linux node pool
- D) Azure Container Apps

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure App Service supports Windows containers, which can run .NET Framework 4.7 applications that require the Windows Server OS. App Service provides managed scaling, deployment slots, custom domains, and SSL — all without requiring Kubernetes knowledge. This is the right fit for a single containerized Windows web application.
- *Why A is incorrect:* A Linux container cannot run .NET Framework 4.7 applications that depend on Windows-specific APIs. ACI does support Windows containers, but App Service provides richer management features (deployment slots, custom domains, SSL) that align better with a production web application.
- *Why C is incorrect:* AKS Linux node pools cannot run Windows containers. While AKS supports Windows node pools, the scenario specifically says no Kubernetes orchestration is needed — AKS would be an over-engineered solution.
- *Why D is incorrect:* Azure Container Apps runs on Linux-based infrastructure and does not support Windows containers. It also requires Kubernetes-style configuration, adding unnecessary complexity for a single application migration.

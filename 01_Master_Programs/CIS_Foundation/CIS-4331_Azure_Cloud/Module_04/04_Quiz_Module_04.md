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

---

### Question 11 (5 points)

A company stores its container images in a public Docker Hub repository. Their security team requires all images to be stored privately and scanned for known vulnerabilities (CVEs) before deployment to production. Which Azure service satisfies both requirements?

- A) Azure Container Instances with a private DNS zone
- B) Azure Kubernetes Service with network policies
- C) Azure Container Registry with Microsoft Defender for Containers enabled
- D) Azure App Service with access restrictions

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Azure Container Registry is a private Docker-compatible image registry. Enabling Microsoft Defender for Containers on the registry adds continuous vulnerability scanning that evaluates images against CVE databases. This combination provides both private storage and automated security scanning before deployment.
  - *Why A is incorrect:* ACI is a container runtime — it executes containers but does not store or scan images. Private DNS zones control name resolution, not image storage or scanning.
  - *Why B is incorrect:* AKS is an orchestration platform. Network policies control traffic between pods. Neither AKS nor network policies provide image storage or pre-deployment vulnerability scanning.
  - *Why D is incorrect:* App Service access restrictions control inbound HTTP/HTTPS traffic to a web application. They have no relationship to container image storage or vulnerability scanning.

---

### Question 12 (5 points)

An organization runs a three-tier application: a web frontend, an API layer, and a database tier. Each tier must be able to scale independently and communicate over a private network. Which Azure container service provides the necessary orchestration and private networking for this architecture?

- A) Azure Container Instances with a virtual network integration
- B) Azure Container Apps with an internal environment
- C) Azure Kubernetes Service with a VNet-integrated cluster
- D) Azure Container Registry with geo-replication

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* AKS supports VNet integration where the cluster nodes and pods run inside a customer-controlled Azure Virtual Network. Each tier can be deployed as a separate Kubernetes Deployment with independent scaling rules, and pod-to-pod communication stays private within the VNet. This is the standard architecture for multi-tier containerized applications requiring network isolation.
  - *Why A is incorrect:* ACI supports VNet deployment for single containers, but it provides no orchestration, service discovery, or independent scaling across multiple tiers. Managing three independent ACI groups with private networking requires custom work that AKS handles natively.
  - *Why B is incorrect:* Container Apps with an internal environment is a valid option for event-driven microservices, but it abstracts Kubernetes and has limitations for complex stateful applications like a database tier. AKS provides more control for a traditional three-tier architecture.
  - *Why D is incorrect:* ACR geo-replication distributes container images to multiple regions. It is an image storage feature with no compute or networking capabilities for running application tiers.

---

### Question 13 (5 points)

What is the key architectural difference between a container and a virtual machine in terms of how the operating system is used?

- A) Containers include a full guest OS; VMs share the host OS kernel
- B) Containers share the host OS kernel; VMs each run a separate guest OS on a hypervisor
- C) Containers use hardware virtualization; VMs use OS-level isolation
- D) Containers and VMs both require a hypervisor layer between the hardware and the workload

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* This is the fundamental architectural distinction. Containers use Linux namespaces and cgroups to isolate processes within the same OS kernel — no separate OS is needed. VMs use a hypervisor (like Hyper-V) to provide each VM with a complete, independent guest OS. This difference drives container advantages in startup time, image size, and density.
  - *Why A is incorrect:* This reverses the correct relationship. Containers do not include a full guest OS — that is precisely what makes them lightweight. Including a full OS is the characteristic of VMs.
  - *Why C is incorrect:* This also reverses the relationship. VMs use hardware virtualization (hypervisor). Containers use OS-level isolation (namespaces/cgroups). The statement as written is backward.
  - *Why D is incorrect:* Containers do not require a hypervisor. Containers run directly on the host OS using kernel features. The hypervisor is specific to VM architecture, not containers.

---

### Question 14 (5 points)

An AKS cluster has three node pools: a system node pool with 2 nodes and two user node pools with 3 nodes each. A developer deletes the system node pool. What happens?

- A) The cluster continues operating normally using the user node pools as system nodes
- B) The deletion fails because AKS requires at least one system node pool at all times
- C) The cluster is automatically deleted along with all workloads
- D) All user node pools are paused until a new system node pool is created

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* AKS requires at least one system node pool in every cluster. The system node pool runs critical system pods including CoreDNS, kube-proxy, and metrics-server. Azure enforces this constraint and will reject a deletion request that would leave the cluster without a system node pool.
  - *Why A is incorrect:* User node pools cannot automatically become system node pools. The node pool mode (System vs. User) is an explicit configuration. User node pools run workload pods and are not designed to host system components.
  - *Why C is incorrect:* AKS does not automatically delete the entire cluster when a node pool deletion fails or is blocked. The deletion is simply rejected and the cluster continues operating unchanged.
  - *Why D is incorrect:* User node pools are not automatically paused based on system node pool operations. Each node pool operates independently within the cluster.

---

### Question 15 (5 points)

A developer pushes a new container image to Azure Container Registry. A production AKS cluster should automatically deploy this new image without manual intervention. Which Kubernetes/AKS feature or pattern enables this automated deployment pipeline?

- A) AKS node pool autoscaling
- B) Kubernetes rolling update triggered by a CI/CD pipeline updating the Deployment manifest
- C) ACI restart policy set to Always
- D) Azure Container Apps scale-to-zero configuration

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The standard pattern for automated deployment is a CI/CD pipeline (Azure DevOps, GitHub Actions) that builds the image, pushes to ACR, then updates the Kubernetes Deployment manifest with the new image tag using `kubectl set image` or by applying an updated YAML. Kubernetes then performs a rolling update automatically, replacing pods with the new image with no downtime.
  - *Why A is incorrect:* Node pool autoscaling adds or removes worker nodes based on pod resource requests. It does not trigger application deployments or update container images.
  - *Why C is incorrect:* ACI restart policy applies to Azure Container Instances, not AKS. Setting it to "Always" means a stopped container restarts automatically — it does not enable automated image deployments.
  - *Why D is incorrect:* Container Apps scale-to-zero is about instance count management for idle applications. It does not trigger image updates or deployments in AKS.

---

### Question 16 (5 points)

Which ACI container group restart policy should be used for a container that runs a one-time database migration script and should not restart after the script completes successfully?

- A) Always
- B) OnFailure
- C) Never
- D) Once

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* The `Never` restart policy means the container runs once and is not restarted regardless of its exit code (success or failure). For a one-time migration script that must run exactly once and then stop, `Never` is the correct policy. ACI will bill only for the execution duration.
  - *Why A is incorrect:* `Always` restarts the container every time it exits, whether successfully or not. A migration script with `Always` would run the migration repeatedly after each completion — potentially corrupting the database on subsequent runs.
  - *Why B is incorrect:* `OnFailure` restarts the container only if it exits with a non-zero (error) exit code. While this might be appropriate for retrying a failed migration, it still allows unintended re-runs if the exit code is misreported. `Never` is safer for a destructive one-time operation.
  - *Why D is incorrect:* `Once` is not a valid Azure Container Instances restart policy. The three valid ACI restart policies are `Always`, `OnFailure`, and `Never`.

---

### Question 17 (5 points)

A Kubernetes Service of type `LoadBalancer` is created in an AKS cluster. What Azure resource does AKS automatically provision when this Service is created?

- A) An Azure Application Gateway with WAF enabled
- B) An Azure Public IP address and an Azure Load Balancer
- C) An Azure VPN Gateway for external connectivity
- D) An Azure DNS zone with an A record for the service

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* When a Kubernetes Service of type `LoadBalancer` is created in AKS, the AKS cloud controller manager automatically provisions an Azure Public IP address and configures an Azure Load Balancer rule to route traffic from that IP to the matching pods. This is the standard way to expose AKS services to the internet.
  - *Why A is incorrect:* An Application Gateway with WAF is provisioned separately using the Application Gateway Ingress Controller (AGIC) add-on, not automatically by a LoadBalancer service type. Standard LoadBalancer services use Azure Load Balancer, not Application Gateway.
  - *Why C is incorrect:* VPN Gateways establish encrypted network tunnels between on-premises and Azure. Creating a Kubernetes Service does not trigger VPN Gateway provisioning — these are completely unrelated operations.
  - *Why D is incorrect:* AKS does not automatically create Azure DNS zones or records for LoadBalancer services. External DNS integration requires explicit configuration of the External-DNS controller, which is not enabled by default.

---

### Question 18 (5 points)

An organization wants to use containers but their security policy requires that each container must have complete OS kernel isolation equivalent to a virtual machine. Which Azure service or configuration meets this requirement?

- A) AKS with confidential computing node pools
- B) Azure Container Instances with hypervisor-isolated containers
- C) Azure Container Apps with dedicated workload profiles
- D) AKS with network policies enabled

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Container Instances supports hypervisor-isolated containers — each container group runs in its own dedicated virtual machine with a separate kernel, providing VM-equivalent isolation. This is ACI's isolation model by default: each container group gets a dedicated hypervisor-isolated compute allocation, not a shared host kernel.
  - *Why A is incorrect:* AKS confidential computing nodes use AMD SEV-SNP or Intel SGX for hardware-based memory encryption and attestation. While they provide strong security, they are about data confidentiality in memory, not about providing each container with a separate OS kernel.
  - *Why C is incorrect:* Container Apps dedicated workload profiles provide dedicated compute capacity for better performance predictability, but they still run containers on a shared Linux host without VM-equivalent kernel isolation per container.
  - *Why D is incorrect:* AKS network policies control network traffic between pods (which pods can communicate with which). They are a network security feature and do not provide OS kernel isolation between containers.

---

### Question 19 (5 points)

A data engineer wants to run a containerized Apache Spark job that processes 500 GB of data. The job runs once per night and takes approximately 2 hours. The engineer wants the lowest possible cost and does not need persistent infrastructure. Which Azure container service is best suited?

- A) AKS with a dedicated node pool running 24/7
- B) Azure Container Instances with sufficient CPU and memory configuration
- C) Azure Container Apps with scale-to-zero enabled
- D) Azure App Service with always-on disabled

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* ACI is purpose-built for short-duration, on-demand container workloads. The engineer can configure a container group with the required vCPU and memory for the Spark job, run it for the 2-hour nightly window, and ACI bills only for those 2 hours of execution. There is no cluster to maintain and no idle infrastructure costs between nightly runs.
  - *Why A is incorrect:* An AKS cluster with a dedicated node pool running 24/7 incurs VM costs around the clock even when the Spark job is not running. For a 2-hour nightly job, this means paying for 22 hours of idle node time per day — very cost-inefficient.
  - *Why C is incorrect:* Container Apps with scale-to-zero is excellent for event-driven web workloads, but it is not designed for large, long-running batch compute jobs. Container Apps has resource limits and is optimized for request-driven workloads, not 2-hour sustained Spark computations.
  - *Why D is incorrect:* App Service always-on setting prevents the app from being idled after inactivity — it is a web hosting feature with no relevance to batch Spark job execution. App Service does not provide the per-second billing or on-demand compute model needed here.

---

### Question 20 (5 points)

In Docker container architecture, what is the correct sequence of steps to go from application source code to a running container in Azure Container Instances?

- A) Source code → Container → Image → Dockerfile → ACI
- B) Dockerfile → Image (docker build) → Registry push (ACR) → ACI pull and run
- C) Source code → ACI → Image → Registry → Dockerfile
- D) Image → Dockerfile → Registry → Container → ACI

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The correct sequence is: write a Dockerfile that describes how to build the application image; run `docker build` to produce the image; push the image to a registry (Azure Container Registry); then ACI pulls the image from the registry and creates a running container. This is the standard container CI/CD pipeline.
  - *Why A is incorrect:* This sequence is backward. You cannot create a container before building an image, and a Dockerfile is the starting point (before the image), not a step after the container exists.
  - *Why C is incorrect:* Source code does not go directly to ACI. ACI runs container images — the source code must first be packaged into an image via a Dockerfile build process.
  - *Why D is incorrect:* The Image and Dockerfile order is reversed. A Dockerfile is the source/build script that produces the image. The image is the artifact that results from building the Dockerfile, not the starting point.

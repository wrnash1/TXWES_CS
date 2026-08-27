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

---

### Question 11 (5 points)

A media company runs a video transcoding workload that processes uploaded videos in large parallel batches. The workload is CPU-bound, requires no persistent storage on the compute nodes, and runs only when a batch is queued. Which Azure VM series is optimized for this high-throughput CPU-bound workload?

- A) B-series (burstable)
- B) F-series (compute optimized)
- C) M-series (memory optimized)
- D) N-series (GPU enabled)

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The F-series is compute-optimized with a high CPU-to-memory ratio, making it ideal for CPU-bound workloads like video transcoding, batch processing, and web servers with high request rates. It delivers more CPU performance per dollar than general-purpose D-series for compute-heavy work.
  - *Why A is incorrect:* B-series VMs have a low baseline CPU with the ability to burst to full CPU for short periods using accumulated credits. Sustained high-CPU transcoding workloads would exhaust CPU credits quickly, causing the VM to throttle back to its low baseline — exactly the wrong choice for continuous high-CPU batch work.
  - *Why C is incorrect:* M-series is memory-optimized for workloads requiring very large amounts of RAM (SAP HANA, in-memory databases). Video transcoding is CPU-bound and does not require the extremely high memory-to-CPU ratio of M-series.
  - *Why D is incorrect:* N-series provides GPU acceleration, which benefits machine learning inference, 3D rendering, and GPU-accelerated video encoding (NVENC). Standard CPU-based transcoding pipelines do not use GPU hardware and would not benefit from N-series.

---

### Question 12 (5 points)

An Azure Functions app on the Consumption plan processes messages from an Azure Service Bus queue. During off-hours the queue is empty and no messages arrive. What is the billing behavior during these idle periods?

- A) The function app is billed at a reduced idle rate of 50% of the execution rate
- B) The function app incurs no charges — the Consumption plan bills only when functions execute
- C) The function app is billed at a minimum of one execution per minute to maintain warm state
- D) The function app must be manually paused to stop billing during idle periods

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The Azure Functions Consumption plan charges only for actual function executions — billed per execution and per GB-second of memory used during execution. When no messages arrive and no functions execute, there are zero charges. The platform scales to zero automatically.
  - *Why A is incorrect:* There is no "reduced idle rate" in the Consumption plan. The plan has no concept of an idle billing state — either a function executes (and is billed) or it does not (and is not billed).
  - *Why C is incorrect:* There is no minimum execution charge in the Consumption plan. The platform does maintain warm instances internally, but this does not translate to a minimum billing charge to the customer.
  - *Why D is incorrect:* The Consumption plan requires no manual intervention to pause or stop billing. Scale-to-zero is automatic — the customer does not need to manage the idle state.

---

### Question 13 (5 points)

A developer deploys an Azure App Service web app on a Free (F1) tier plan and later discovers that the app cannot use custom domains or TLS/SSL certificates. What is the minimum tier required to add a custom domain?

- A) Free (F1)
- B) Shared (D1)
- C) Basic (B1)
- D) Standard (S1)

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Custom domain binding is supported starting at the Basic tier (B1) and above. The Free and Shared tiers only support the default `*.azurewebsites.net` subdomain. Basic tier also includes 10 GB storage and up to 3 deployment slots.
  - *Why A is incorrect:* The Free tier (F1) does not support custom domain names. It is limited to the `*.azurewebsites.net` subdomain and has significant compute and storage restrictions.
  - *Why B is incorrect:* The Shared (D1) tier allows custom domain names but does not include custom SSL/TLS certificate binding. It is a partial improvement over Free but still insufficient for HTTPS on a custom domain.
  - *Why D is incorrect:* Standard (S1) does support custom domains and SSL, but it is not the minimum tier required. Basic (B1) already supports custom domains. Standard adds auto-scaling and deployment slots beyond what Basic provides.

---

### Question 14 (5 points)

A company runs a stateful .NET web application on Azure App Service. Sessions store shopping cart data in application memory. The team enables auto-scaling to add instances during peak traffic. What problem will users experience, and what is the correct solution?

- A) No problem — App Service automatically synchronizes in-memory session state across all instances
- B) Users may lose their shopping cart data when requests are routed to a different instance; use Azure Cache for Redis to store session state externally
- C) Auto-scaling is not supported for stateful applications — use a single large VM instead
- D) The application must be rewritten as stateless before deploying to App Service

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* When multiple App Service instances run the same app, in-memory session state is local to each instance. If a user's request is routed to a different instance (which happens with load balancing), that instance has no knowledge of the previous instance's memory state — the shopping cart is lost. The solution is to externalize session state to a shared store like Azure Cache for Redis, where all instances can read and write session data.
  - *Why A is incorrect:* App Service does not automatically synchronize in-memory state between instances. Each instance maintains its own separate memory space. Azure provides ARR Affinity (sticky sessions) as a workaround, but this reduces the effectiveness of load balancing and is not recommended for production.
  - *Why C is incorrect:* Auto-scaling is fully supported for stateful applications — however, the stateful components must be moved out of instance memory to an external store. The auto-scaling capability itself is not the constraint.
  - *Why D is incorrect:* The application does not need to be rewritten as fully stateless — it needs its state externalized. Many existing stateful applications can be updated to use Redis for session storage without a full rewrite.

---

### Question 15 (5 points)

Which orchestration mode for Azure Virtual Machine Scale Sets allows each VM instance to have a unique configuration and does not require all instances to be identical, enabling mixed workloads within a single Scale Set?

- A) Uniform orchestration mode
- B) Flexible orchestration mode
- C) Manual orchestration mode
- D) Stateful orchestration mode

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Flexible orchestration mode allows each VM instance in a Scale Set to have a different configuration — different VM sizes, different images, different extensions. It supports up to 1,000 VMs and enables heterogeneous workloads. It also provides integration with Availability Zones and supports mixing Spot and regular VMs.
  - *Why A is incorrect:* Uniform orchestration mode requires all instances to be identical — same VM size, same image, same configuration. This is optimal for stateless, homogeneous workloads like web servers where every instance is equivalent.
  - *Why C is incorrect:* "Manual orchestration mode" is not a real Azure Scale Set mode. This is a distractor.
  - *Why D is incorrect:* "Stateful orchestration mode" is not a real Azure Scale Set mode. This is a distractor.

---

### Question 16 (5 points)

A team deploys an Azure Function on the Premium plan. After deployment, they notice the function responds to the first request of the day with a 10-15 second delay, but subsequent requests respond in milliseconds. What is the cause of this cold start, and how does the Premium plan address it?

- A) The Premium plan does not address cold starts — they are inherent to all serverless functions
- B) Cold starts occur when no warm instance is available; the Premium plan maintains at least one pre-warmed instance to eliminate cold starts
- C) Cold starts are caused by network latency to the Azure region; the Premium plan uses CDN to cache function code globally
- D) Cold starts only occur in the Consumption plan; the Premium plan uses dedicated VMs that never cold start

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A cold start occurs when a function request arrives and no warm (initialized) instance is available — the runtime must load the function app, restore dependencies, and initialize the execution environment before handling the request. The Premium plan's "pre-warmed instances" feature keeps at least one instance always ready to handle requests, eliminating cold starts for incoming traffic.
  - *Why A is incorrect:* The Premium plan specifically advertises "no cold starts" as a key feature over the Consumption plan. Pre-warmed instances are the mechanism that eliminates cold starts.
  - *Why C is incorrect:* CDN caches static content (web assets), not serverless function execution environments. Cold starts are not caused by network latency — they are caused by instance initialization time.
  - *Why D is incorrect:* Cold starts can occur in both Consumption and Premium plans without pre-warming. However, the Premium plan's pre-warmed instances feature eliminates them. The Premium plan does not use "dedicated VMs" in the same sense as IaaS — it uses pre-allocated managed compute.

---

### Question 17 (5 points)

An organization wants to deploy a web application to Azure App Service and enable deployment slots for staging. They also require auto-scaling based on CPU utilization. What is the minimum App Service plan tier that supports both deployment slots and auto-scaling?

- A) Basic (B1)
- B) Standard (S1)
- C) Premium (P1v3)
- D) Isolated (I1v2)

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The Standard tier (S1) is the minimum tier that supports both auto-scaling (scale out based on metrics) and deployment slots (up to 5 slots). Basic supports custom domains but does not include auto-scaling or deployment slots. Standard is the entry point for production-grade App Service features.
  - *Why A is incorrect:* The Basic tier supports up to 3 instances via manual scale-out but does not support automatic metric-based scaling rules. It also does not include deployment slots.
  - *Why C is incorrect:* Premium tier does support both features (with up to 20 slots and more scale-out options), but it is not the minimum tier. Standard already provides both capabilities at lower cost.
  - *Why D is incorrect:* Isolated tier (App Service Environment) provides the highest isolation and supports all features, but it is the most expensive option and far exceeds the minimum requirement.

---

### Question 18 (5 points)

What is the key architectural difference between Azure Functions Durable Functions and standard Azure Functions triggers?

- A) Durable Functions support only HTTP triggers; standard Functions support all trigger types
- B) Durable Functions enable stateful workflows that can wait for external events, fan-out/fan-in, and chain function calls; standard Functions are stateless and short-lived
- C) Durable Functions run on dedicated VMs; standard Functions run on shared serverless infrastructure
- D) Durable Functions are limited to 5-minute execution timeouts; standard Functions have no timeout

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Durable Functions extend standard Functions by providing durable, stateful orchestration patterns. An orchestrator function can call activity functions in sequence (chaining), run them in parallel and wait for all results (fan-out/fan-in), and pause execution waiting for an external event (human approval workflows). The state is persisted automatically in Azure Storage between executions.
  - *Why A is incorrect:* Standard Azure Functions support many trigger types (HTTP, Timer, Queue, Blob, Service Bus, Event Hub, etc.) — they are not limited to HTTP. Durable Functions use an orchestration trigger, not exclusively HTTP.
  - *Why C is incorrect:* Both standard Functions and Durable Functions run on the same underlying serverless infrastructure when using Consumption or Premium plans. Durable Functions do not require dedicated VMs.
  - *Why D is incorrect:* Standard Functions on the Consumption plan have a default 5-minute timeout (maximum 10 minutes). Durable Functions can run for days or months because they persist state between executions — the orchestrator itself yields while waiting. This is the opposite of the statement in option D.

---

### Question 19 (5 points)

A company is evaluating whether to use Azure App Service or Azure Kubernetes Service for a new microservices application with eight services. Each service is independently deployed and scaled, communicates via REST APIs, and requires zero-downtime rolling updates. Which service is the better fit and why?

- A) App Service — it supports multiple apps and is simpler to configure than AKS
- B) AKS — it provides per-service independent scaling, rolling update deployments, and service mesh capabilities suitable for microservices
- C) App Service — deployment slots provide zero-downtime updates equivalent to Kubernetes rolling updates
- D) AKS — it is always cheaper than running eight separate App Service plans

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* AKS is purpose-built for microservices orchestration. Each service runs as a separate Kubernetes Deployment with its own replica count, resource limits, and scaling rules. Kubernetes rolling updates replace pods incrementally with zero downtime. Service-to-service communication, network policies, and health checks are all native features of Kubernetes.
  - *Why A is incorrect:* While multiple App Service apps can be deployed to the same plan, App Service does not have native service discovery, inter-service network policies, or per-service independent scaling that microservices require. Managing eight separate App Service deployments with coordination is operationally complex compared to AKS.
  - *Why C is incorrect:* App Service deployment slots perform blue/green swaps — the traffic switches instantly from one slot to another. This is different from Kubernetes rolling updates that gradually replace pods one at a time. Both achieve zero-downtime, but deployment slots are designed for single-service deployments, not eight independent microservices.
  - *Why D is incorrect:* AKS may or may not be cheaper than eight separate App Service plans — the cost comparison depends on traffic volume, instance sizes, and usage patterns. Cost is not the primary reason to choose AKS for microservices; architectural fit is.

---

### Question 20 (5 points)

A development team wants to test whether their Azure App Service application handles production traffic correctly before releasing it to all users. They deploy a new version to a staging slot and want to send 10% of production traffic to the staging slot while 90% continues going to the production slot. Which App Service feature enables this traffic distribution?

- A) Azure Front Door with weighted routing
- B) App Service deployment slot traffic splitting (Traffic %setting)
- C) Azure Load Balancer with weighted backend pool
- D) Azure Traffic Manager with weighted routing profiles

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure App Service deployment slots support traffic splitting natively. In the Azure Portal (or via CLI with `az webapp traffic-routing set`), you can configure what percentage of traffic routes to each slot. Setting staging to 10% and production to 90% allows gradual testing (also called canary deployments) without any external routing service.
  - *Why A is incorrect:* Azure Front Door can perform weighted routing across backends, but it is an external CDN/load balancing service that would require additional configuration and cost. App Service has this capability built-in at no additional charge via slot traffic splitting.
  - *Why C is incorrect:* Azure Load Balancer is a Layer 4 (TCP/UDP) load balancer for VMs and scale sets. App Service deployments do not use Azure Load Balancer directly — they use the App Service built-in routing infrastructure. Load Balancer also does not understand App Service deployment slots.
  - *Why D is incorrect:* Azure Traffic Manager is a DNS-based global traffic manager for routing between Azure regions or endpoints. It is not designed for splitting traffic between two slots of the same App Service application in the same region.

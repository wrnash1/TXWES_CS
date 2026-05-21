# Quiz: Module 04 - Azure Container Services

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
What is the fastest way to run a single Docker container in Azure without provisioning virtual machines?

* A) Azure Kubernetes Service (AKS)
* B) Azure Container Instances (ACI)
* C) Azure Functions
* D) Windows Server container host
* **Correct Answer:** B) ACI is a serverless container solution designed to quickly run single containers without VM management overhead.
* **Distractor Analysis:**
  * *Why correct:* ACI is a serverless container solution designed to quickly run single containers without VM management overhead.
  * *Why A is incorrect:* AKS is for full container orchestration and requires cluster provisioning.

---

**Question 2**
Which of the following most accurately describes **serverless computing** in the context of Azure?

* A) A cloud execution model where the provider dynamically allocates and manages all underlying infrastructure, and the customer is billed only for actual execution time rather than reserved capacity.
* B) A deployment model where no servers are used at all — workloads run entirely on client devices.
* C) A licensing model where servers are provided free of charge by the cloud provider to qualifying startups.
* D) An on-premises architecture where physical servers are replaced with software-defined virtual servers managed by the customer.
* **Correct Answer:** A) Serverless computing means the provider manages all infrastructure dynamically; billing is based on execution time, not reserved capacity.
* **Distractor Analysis:**
  * *Why A is correct:* Serverless abstracts infrastructure management — servers exist but are fully managed by the provider. Azure Functions and ACI are examples.
  * *Why B is incorrect:* Serverless does not mean no servers exist — it means the customer does not manage them.
  * *Why C is incorrect:* Serverless is not a licensing model; it is a deployment and billing model tied to execution-based pricing.
  * *Why D is incorrect:* That describes on-premises virtualization, which is the opposite of cloud serverless.

---

**Question 3**
A development team needs to run a microservices application composed of 15 interdependent containers with service discovery, rolling deployments, and auto-healing. Which Azure service best addresses these requirements?

* A) Azure Container Instances
* B) Azure Kubernetes Service
* C) Azure App Service
* D) Azure Virtual Machine Scale Sets
* **Correct Answer:** B) Azure Kubernetes Service provides full container orchestration including service discovery, rolling updates, and self-healing for complex multi-container applications.
* **Distractor Analysis:**
  * *Why B is correct:* AKS is purpose-built for orchestrating multiple interdependent containers with advanced features like rolling deployments and service mesh.
  * *Why A is incorrect:* ACI runs individual containers without orchestration — it does not support service discovery or rolling deployments across containers.
  * *Why C is incorrect:* App Service is PaaS for web apps; it does not provide Kubernetes-style container orchestration.
  * *Why D is incorrect:* VMSS scales identical VMs, not containers, and does not provide container service discovery.

---

**Question 4**
A company stores container image configurations and source code in public GitHub repositories. They accidentally committed a production Azure storage connection string. Which action most directly mitigates the immediate risk?

* A) Enable Azure Defender for Containers on the AKS cluster
* B) Rotate the storage account key immediately and update the application to use Azure Key Vault for secret retrieval
* C) Move the container registry from public to private network access
* D) Enable read-only locks on the storage account resource
* **Correct Answer:** B) Rotating the compromised key immediately invalidates the exposed credential, and using Azure Key Vault prevents future hardcoded secrets.
* **Distractor Analysis:**
  * *Why B is correct:* The exposed connection string must be invalidated immediately by rotating the key. Key Vault then provides a secure, audited way to store and retrieve secrets without hardcoding.
  * *Why A is incorrect:* Defender for Containers monitors runtime threats — it does not revoke already-exposed credentials.
  * *Why C is incorrect:* Making the registry private does not help since the connection string, not the registry, is compromised.
  * *Why D is incorrect:* A ReadOnly lock prevents deletion and configuration changes but does not revoke an already-exposed access key.

---

**Question 5**
When choosing between Azure Container Instances and Azure Kubernetes Service, which scenario is ACI the more appropriate choice?

* A) Running 50 microservices with interdependencies, persistent volumes, and blue-green deployments
* B) Orchestrating a containerized application that requires automatic certificate renewal and service mesh
* C) Quickly running a one-off batch processing container that completes and terminates within minutes
* D) Hosting a production application requiring 99.99% uptime across multiple availability zones
* **Correct Answer:** C) ACI is ideal for short-lived, single-container workloads like batch jobs that run to completion — no cluster management required.
* **Distractor Analysis:**
  * *Why C is correct:* ACI's serverless, per-second billing and instant startup make it perfect for burst or batch workloads without persistent orchestration needs.
  * *Why A is incorrect:* Fifty interdependent microservices require AKS's orchestration capabilities, not ACI's single-container model.
  * *Why B is incorrect:* Certificate management and service mesh are AKS features — ACI does not provide these.
  * *Why D is incorrect:* High-availability production workloads spanning zones require AKS cluster configuration, not ACI's ephemeral model.

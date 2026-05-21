# Reading Guide: Module 04 - Azure Container Services

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 04 - Azure Container Services**! This module covers Azure's container and serverless compute offerings as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Containers package applications and their dependencies into portable units that run consistently across environments. Azure provides multiple services for running containers, from single-container deployment to full Kubernetes orchestration.

You will learn when to use Azure Container Instances for rapid single-container deployment, when Azure Kubernetes Service is appropriate for orchestrated workloads, and what "serverless computing" means in the context of AZ-900. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Azure Container Instances (ACI)**: A serverless container service that lets you run a Docker container in Azure without provisioning or managing virtual machines. ACI is billed per second of container execution and is ideal for burst workloads, batch jobs, or quickly testing a containerized application. It is the fastest path from image to running container in Azure.

* **Azure Kubernetes Service (AKS)**: A managed Kubernetes orchestration service that automates deployment, scaling, and operations of containerized applications across a cluster of VMs. AKS handles Kubernetes control-plane management for you (free of charge) while you manage the worker node VMs. Use AKS when you need multi-container orchestration, service discovery, rolling deployments, or complex scaling logic.

* **Serverless Computing**: A cloud execution model where the provider dynamically allocates compute resources on demand. The customer provides code or a container; the platform handles all infrastructure provisioning, scaling, and patching. Billing is based on actual execution (per call or per second) rather than reserved capacity. Azure Functions and Azure Container Instances are both examples of serverless models on AZ-900.

---

### 2. Certification Exam Tips

* **ACI vs. AKS distinction**: AZ-900 tests when to use each. ACI = single container, no cluster management, fast startup, serverless billing. AKS = multi-container orchestration, full Kubernetes feature set, cluster of VMs. If a scenario mentions "without managing VMs" and "single container," ACI is the answer.
* **Serverless does not mean no servers**: AZ-900 may ask what "serverless" means. The correct answer is that the provider manages all infrastructure — servers still exist, but they are abstracted away. The customer is not responsible for provisioning, patching, or managing the underlying compute.
* **Container vs. VM**: Containers share the host OS kernel and are lighter-weight than VMs. VMs include a full OS. AZ-900 may test this distinction in terms of startup time and resource density.
* **Azure Functions vs. ACI**: Azure Functions is event-driven and runs individual code snippets. ACI runs full container images. Both are serverless but for different use cases. Functions = small event-triggered code; ACI = containerized application workloads.
* **Study Resource**: The Microsoft Learn module on Azure containers and serverless covers ACI, AKS, and Azure Functions with knowledge checks. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers container services including ACI, AKS, and serverless computing with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* **Required Video:** This free freeCodeCamp course covers Azure container and serverless concepts for AZ-900 — watch the containers section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Deploy a container using Azure Container Instances**: Use the Azure portal or Azure CLI (`az container create`) to deploy a public Docker image (e.g., nginx) as an ACI instance. Observe how no VM provisioning is required.
* **Verify the container running state**: Check the container's status, public IP address, and logs in the portal. Access the container's web endpoint to confirm it is serving traffic.
* **Examine Kubernetes orchestration structures in AKS**: Review an existing AKS cluster in the portal, exploring the node pool, namespace, and workload sections. Identify how AKS abstracts the Kubernetes control plane from the customer.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Azure containers unit in [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* [ ] Watch the containers section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for ACI deployment and AKS exploration.
* [ ] Proceed to the weekly hands-on lab activity.

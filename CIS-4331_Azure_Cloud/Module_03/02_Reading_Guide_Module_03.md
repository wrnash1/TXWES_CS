# Reading Guide: Module 03 - Azure Virtual Machines & Scale Sets

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 03 - Azure Virtual Machines & Scale Sets**! This module covers Azure's core compute offerings as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Virtual Machines are the flagship IaaS service in Azure, giving you full control over the OS and installed software. Scale Sets extend VMs with automatic scaling capabilities.

You will learn how VMs differ from PaaS compute options like Azure App Service, when to choose VM Scale Sets for autoscaling workloads, and how the AZ-900 exam distinguishes between compute service types by management responsibility and use case. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Azure Compute Services**: The collection of Azure services for running workloads in the cloud, including Virtual Machines (IaaS), Azure App Service (PaaS), Azure Functions (serverless), Azure Container Instances, and Azure Kubernetes Service. AZ-900 tests your ability to match workload requirements to the correct compute service.

* **Virtual Machines (VMs)**: An IaaS offering that provides a full virtualized operating system environment. The customer selects the VM size, OS image, and is responsible for OS patching, security configuration, and installed software. Azure VMs support Windows and Linux. VMs are the right choice when you need OS-level control.

* **Virtual Machine Scale Sets (VMSS)**: An Azure service that deploys and manages a set of identical VMs, automatically scaling the number of instances up or down based on demand metrics (such as CPU usage) or a schedule. VMSS is used for large-scale, high-availability workloads and is the AZ-900 answer for "auto-scaling identical VMs."

* **Azure App Service**: A fully managed PaaS platform for hosting web applications, REST APIs, and mobile backends. Developers deploy code or containers; Azure handles the OS, runtime, patching, and scaling infrastructure. App Service supports .NET, Java, Node.js, Python, and PHP. It is the correct choice when you want to focus on app code, not server management.

---

### 2. Certification Exam Tips

* **VM vs. App Service vs. Functions**: AZ-900 consistently tests service model classification. VMs = IaaS (you manage OS). App Service = PaaS (provider manages OS, you manage app). Azure Functions = serverless PaaS (you manage only code, billed per execution). Know which layer each service owns.
* **VMSS is not the same as VMs**: VMSS provides orchestration and autoscaling for identical VMs. A standalone VM does not autoscale. If an AZ-900 scenario asks about automatically handling demand spikes across many identical servers, the answer is VMSS.
* **VM SLA requires two or more instances**: A single VM has a lower SLA than a VM deployed across Availability Zones or in an Availability Set. AZ-900 scenarios about achieving a 99.99% SLA for VMs require at least two instances across zones.
* **App Service Plans**: App Service pricing is based on the Plan tier (Free, Shared, Basic, Standard, Premium, Isolated). AZ-900 may ask which tier supports custom domain names or auto-scaling — Standard and above support autoscale.
* **Study Resource**: The Microsoft Learn compute module covers VMs, Scale Sets, App Service, and Azure Functions with sandbox exercises. Work through the Azure compute unit at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers Azure compute services including VMs, Scale Sets, and App Service with hands-on sandbox activities. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* **Required Video:** This free 3-hour freeCodeCamp course covers Azure compute services in detail — watch the VM and App Service sections: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Provision an Azure Linux VM using portal template**: Create a VM through the Azure portal, selecting a region, size (e.g., B1s), OS image (Ubuntu), and authentication method. Observe the associated resources (NIC, disk, NSG) created automatically.
* **Set up auto-scaling properties on a VM Scale Set**: Create a VMSS and configure a scale-out rule triggered when average CPU exceeds 75% for 5 minutes. Confirm the scaling policy settings in the portal.
* **Verify VM SSH access**: Connect to the VM using SSH (Linux) or RDP (Windows) to confirm the instance is running and accessible, demonstrating the IaaS management responsibility you hold for the OS.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Azure compute unit in [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* [ ] Watch the VM and App Service sections of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for VM provisioning and Scale Set autoscale configuration.
* [ ] Proceed to the weekly hands-on lab activity.

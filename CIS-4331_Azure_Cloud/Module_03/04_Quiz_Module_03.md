# Quiz: Module 03 - Azure Virtual Machines & Scale Sets

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure compute service allows you to automatically deploy and manage a set of identical, auto-scaling VMs?

* A) Azure App Service
* B) Azure Functions
* C) Virtual Machine Scale Sets
* D) Azure Container Instances
* **Correct Answer:** C) VMSS enables automatic scaling of identical VMs based on CPU load or schedules.
* **Distractor Analysis:**
  * *Why correct:* VMSS enables automatic scaling of identical VMs based on CPU load or schedules.
  * *Why A/B/D are incorrect:* App Service is for web apps (PaaS). Functions is serverless. Container Instances runs containers, not VMs.

---

**Question 2**
Which of the following most accurately describes **Azure App Service**?

* A) A fully managed PaaS platform for hosting web applications and APIs where Azure handles the underlying OS, runtime, and scaling infrastructure, and developers deploy only their application code.
* B) An IaaS service that provides a full virtual machine with a customer-managed operating system and all installed software.
* C) A serverless compute service that runs individual functions in response to events, billing only for execution time consumed.
* D) A container orchestration service that manages clusters of Docker containers using Kubernetes.
* **Correct Answer:** A) Azure App Service is a fully managed PaaS platform for hosting web applications and APIs where Azure handles the underlying OS, runtime, and scaling infrastructure.
* **Distractor Analysis:**
  * *Why A is correct:* App Service is PaaS — the provider manages OS and runtime, the customer deploys code.
  * *Why B is incorrect:* That describes Azure Virtual Machines (IaaS), not App Service.
  * *Why C is incorrect:* That describes Azure Functions (serverless), not App Service.
  * *Why D is incorrect:* That describes Azure Kubernetes Service (AKS), not App Service.

---

**Question 3**
A development team needs to host a web API in Azure. They want zero server management — no OS patching, no infrastructure provisioning — and they need automatic scaling. Which Azure service best fits?

* A) Azure Virtual Machine with manual scaling scripts
* B) Azure App Service on a Standard or Premium plan
* C) Azure Virtual Machine Scale Set with manual OS management
* D) Azure Dedicated Host with reserved capacity
* **Correct Answer:** B) Azure App Service on a Standard or Premium plan provides fully managed PaaS hosting with built-in autoscaling and no OS management responsibility for the customer.
* **Distractor Analysis:**
  * *Why B is correct:* App Service eliminates OS management and supports autoscaling on Standard/Premium tiers — exactly matching the requirements.
  * *Why A is incorrect:* A standalone VM requires manual OS patching and manual scaling scripts.
  * *Why C is incorrect:* VMSS scales VMs automatically but the customer is still responsible for OS management on each instance.
  * *Why D is incorrect:* Azure Dedicated Host provides physical isolation but the customer still manages the OS on VMs.

---

**Question 4**
Your e-commerce platform experiences unpredictable traffic spikes during promotions. The backend consists of identical stateless web servers. Which Azure service should you use to automatically add or remove instances based on CPU metrics?

* A) Azure App Service Environment
* B) Azure Virtual Machine Scale Sets
* C) Azure Load Balancer alone
* D) Azure Availability Sets
* **Correct Answer:** B) Azure Virtual Machine Scale Sets automatically increases or decreases the number of identical VM instances based on defined metrics such as CPU utilization.
* **Distractor Analysis:**
  * *Why B is correct:* VMSS is designed precisely for autoscaling identical stateless VM workloads based on demand metrics.
  * *Why A is incorrect:* App Service Environment is a dedicated hosting environment for App Service apps, not VM-based workloads.
  * *Why C is incorrect:* Azure Load Balancer distributes traffic but does not create or remove VM instances.
  * *Why D is incorrect:* Availability Sets distribute VMs across fault and update domains for high availability but do not autoscale.

---

**Question 5**
You need to achieve a 99.99% SLA for a VM-based workload in Azure. Which configuration meets this requirement?

* A) A single VM with Premium SSD managed disk
* B) Two or more VMs deployed across different Availability Zones in the same region
* C) A single VM in an Availability Set with one fault domain
* D) One VM deployed with Azure Backup enabled
* **Correct Answer:** B) Two or more VMs deployed across different Availability Zones in the same region achieves the 99.99% uptime SLA for virtual machines.
* **Distractor Analysis:**
  * *Why B is correct:* Microsoft's SLA for VMs reaches 99.99% only when two or more instances are deployed across separate Availability Zones.
  * *Why A is incorrect:* A single VM, even with Premium SSD, achieves only a 99.9% SLA — not 99.99%.
  * *Why C is incorrect:* A single-VM Availability Set provides no redundancy and does not meet 99.99% SLA.
  * *Why D is incorrect:* Azure Backup enables recovery after failure but does not improve uptime SLA.

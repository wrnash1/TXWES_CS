# Reading Guide: Module 05 - Azure Virtual Networking

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 05 - Azure Virtual Networking**! This module covers Azure's core networking services as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Azure Virtual Networks (VNets) provide the foundational connectivity layer for all Azure resources, and understanding how to isolate, connect, and secure them is essential for AZ-900.

You will learn how VNets and subnets segment network traffic, how Network Security Groups control traffic flow with rules, how VPN Gateways and ExpressRoute connect on-premises networks to Azure, and when to use each connectivity option. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Virtual Networks (VNet)**: An isolated, private network in Azure that enables Azure resources such as VMs and App Services to communicate securely with each other, the internet, and on-premises networks. A VNet is scoped to a single Azure region. VNets can be peered across regions. They are the foundation of Azure network architecture.

* **Subnets**: Subdivisions within a VNet that segment address space into smaller ranges, allowing you to organize resources and apply different security policies to each segment. For example, a web subnet can have different NSG rules than a database subnet. Subnets cannot span VNets; they exist entirely within one VNet.

* **Network Security Groups (NSGs)**: A firewall-like service containing inbound and outbound security rules that control which network traffic is allowed or denied to Azure resources. NSGs can be associated with subnets or individual network interfaces. Rules are evaluated in priority order (lower number = higher priority). Default rules allow VNet-internal and Azure Load Balancer traffic.

* **Azure ExpressRoute**: A service that provides a dedicated, private fiber-optic connection from an on-premises network directly to Azure, bypassing the public internet entirely. ExpressRoute offers higher reliability, faster speeds, lower latency, and higher security than internet-based VPN connections. It is the correct answer for enterprise-grade private connectivity to Azure.

* **VPN Gateways**: A service that creates an encrypted tunnel over the public internet between an on-premises network (or another VNet) and an Azure VNet. VPN Gateway is less expensive than ExpressRoute but shares public internet bandwidth. Use VPN Gateway when cost is the priority and public internet traversal is acceptable.

---

### 2. Certification Exam Tips

* **ExpressRoute vs. VPN Gateway**: AZ-900 frequently tests this distinction. ExpressRoute = private connection, no public internet, higher cost, better SLA. VPN Gateway = encrypted tunnel over public internet, lower cost. If a scenario mentions "private," "dedicated," or "fiber," the answer is ExpressRoute.
* **NSG rule evaluation**: Rules are processed in priority order from lowest number to highest. The first matching rule wins. There is always a default deny-all rule at the end. AZ-900 may test what happens when a specific allow rule and a deny rule conflict — lower priority number wins.
* **VNet Peering**: Two VNets can be connected using VNet Peering, allowing resources in each VNet to communicate as if they were on the same network. Peering is not transitive — if VNet A is peered with B, and B with C, A cannot reach C without a direct peering or hub-spoke configuration.
* **Azure Bastion**: A PaaS service that provides secure RDP/SSH access to VMs through the Azure portal without exposing VMs to a public IP address. AZ-900 may ask which service eliminates the need for a public IP on a VM for administrative access — the answer is Azure Bastion.
* **Study Resource**: The Microsoft Learn networking module covers VNets, NSGs, VPN Gateway, and ExpressRoute with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers Azure networking including VNets, subnets, NSGs, and connectivity options with hands-on exercises. Access it at [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* **Required Video:** This free freeCodeCamp course covers Azure networking concepts for AZ-900 — watch the networking section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Create a VNet with public and private subnets**: Define a VNet address space (e.g., 10.0.0.0/16) and create two subnets — one for web-tier resources (10.0.1.0/24) and one for data-tier resources (10.0.2.0/24).
* **Configure an NSG rule to block port 80 traffic**: Create an NSG, add an inbound deny rule for port 80 (HTTP), associate it with the web subnet, and confirm that HTTP traffic is blocked while HTTPS (port 443) remains permitted.
* **Trace VPN routing tables**: Review the effective routes on a VM network interface to understand how traffic flows through subnets, peered VNets, and gateway routes.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Azure networking unit in [Microsoft Learn – AZ-900 Azure Architecture](https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/).
* [ ] Watch the networking section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for VNet creation and NSG rule configuration.
* [ ] Proceed to the weekly hands-on lab activity.

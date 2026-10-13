# Video Script: Module 05 - Azure Virtual Networking

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Duration:** 22-24 minutes
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## [00:00 - 01:30] Opening and Learning Objectives

**[INSTRUCTOR ON CAMERA — title card: "Module 05: Azure Virtual Networking"]**

Welcome to Module 05. I'm Professor Nash. Today we cover Azure Virtual Networking — the connective tissue that links every Azure service together and connects your cloud resources to your on-premises environment and the internet.

Networking is one of the largest topic areas in the AZ-900 "Describe Azure Architecture and Services" domain. Understanding virtual networks, subnets, Network Security Groups, DNS, and connectivity options is essential for passing the exam and for any real cloud infrastructure work.

By the end of this module you will be able to:

- Create and configure Azure Virtual Networks and subnets
- Explain the purpose of Network Security Groups and create inbound/outbound rules
- Describe Azure Firewall and its differences from NSGs
- Explain Azure DNS and how it resolves names
- Compare Azure VPN Gateway and Azure ExpressRoute for hybrid connectivity
- Describe VNet peering and its use for connecting virtual networks

---

## [01:30 - 06:00] Azure Virtual Networks and Subnets

**[SLIDE: "Azure Virtual Network (VNet)"]**

An Azure Virtual Network is the fundamental network building block in Azure. It is a logically isolated network within Azure that your resources — virtual machines, databases, containers — communicate through. Think of a VNet as your private network in the cloud, analogous to a corporate LAN, but implemented entirely in software.

Key VNet characteristics:

Every VNet is scoped to a single Azure region. A VNet created in East US cannot extend into West Europe. If you need connectivity between regions, you use VNet peering or a VPN.

Every VNet has an address space — a range of IP addresses defined using CIDR notation. For example, `10.0.0.0/16` defines a private address space containing 65,536 possible IP addresses.

Resources within the same VNet can communicate with each other by default with no additional configuration.

**[SLIDE: "Subnets"]**

Subnets divide a VNet's address space into smaller segments. This serves two purposes:

First, organizational clarity — you can separate resources by function. A common pattern: one subnet for web servers, one for application servers, one for databases. Traffic between subnets is controlled by Network Security Groups.

Second, security isolation — each subnet can have its own NSG, creating network-level security boundaries between tiers of an application.

Example VNet design:

```text
VNet: 10.0.0.0/16
  ├── Web Subnet:    10.0.1.0/24  (256 addresses)
  ├── App Subnet:    10.0.2.0/24  (256 addresses)
  └── DB Subnet:     10.0.3.0/24  (256 addresses)
```

**[SHOW CODE — Creating a VNet and subnets with Azure CLI]**

```bash
# Create a VNet
az network vnet create \
  --resource-group "lab05-rg" \
  --name "lab05-vnet" \
  --address-prefix "10.0.0.0/16" \
  --subnet-name "web-subnet" \
  --subnet-prefix "10.0.1.0/24"

# Add a second subnet
az network vnet subnet create \
  --resource-group "lab05-rg" \
  --vnet-name "lab05-vnet" \
  --name "db-subnet" \
  --address-prefix "10.0.2.0/24"
```

**[SLIDE: "Private IP vs. Public IP"]**

Resources in a VNet communicate using private IP addresses. These addresses are only reachable within the VNet (and any connected networks).

For resources that need to be reachable from the internet, a public IP address is assigned. Azure VMs, Load Balancers, and Application Gateways can have public IPs.

Public IP address types:

**Basic SKU:** Dynamic or static. No zone redundancy. Legacy — Microsoft recommends Standard for new deployments.

**Standard SKU:** Always static. Zone-redundant. Required for Availability Zone deployments. Supports Azure DDoS protection integration.

---

## [06:00 - 11:00] Network Security Groups

**[SLIDE: "Network Security Groups (NSGs)"]**

A Network Security Group is a virtual firewall that filters network traffic to and from Azure resources. An NSG contains a list of security rules, each defining whether to allow or deny traffic based on:

- Source IP address or range
- Source port
- Destination IP address or range
- Destination port
- Protocol (TCP, UDP, ICMP, or Any)
- Direction (Inbound or Outbound)
- Priority (lower number = higher priority, evaluated first)

NSGs can be associated with:

- Individual network interfaces (NIC-level NSG)
- Entire subnets (subnet-level NSG)

Both can be applied simultaneously. When both are present, traffic must pass through both NSGs.

**[SLIDE: "Default NSG Rules"]**

Every NSG contains default rules that cannot be deleted (only overridden with higher-priority custom rules):

Default inbound rules:

- Priority 65000: Allow traffic from VNet (any source in the VNet, any destination in the VNet)
- Priority 65001: Allow inbound from Azure Load Balancer health probe
- Priority 65500: Deny all inbound traffic

Default outbound rules:

- Priority 65000: Allow traffic to VNet
- Priority 65001: Allow outbound to Internet
- Priority 65500: Deny all outbound traffic

These defaults mean that within a VNet, resources can communicate freely, and resources can reach the internet outbound — but no inbound internet traffic is allowed unless you create an explicit allow rule.

**[SHOW CODE — Creating NSG rules with Azure CLI]**

```bash
# Create an NSG
az network nsg create \
  --resource-group "lab05-rg" \
  --name "web-nsg"

# Allow inbound HTTP (port 80)
az network nsg rule create \
  --resource-group "lab05-rg" \
  --nsg-name "web-nsg" \
  --name "allow-http" \
  --priority 100 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefix "*" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 80 \
  --access Allow

# Allow inbound HTTPS (port 443)
az network nsg rule create \
  --resource-group "lab05-rg" \
  --nsg-name "web-nsg" \
  --name "allow-https" \
  --priority 110 \
  --protocol Tcp \
  --direction Inbound \
  --source-address-prefix "*" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 443 \
  --access Allow

# Associate NSG with a subnet
az network vnet subnet update \
  --resource-group "lab05-rg" \
  --vnet-name "lab05-vnet" \
  --name "web-subnet" \
  --network-security-group "web-nsg"
```

**[SLIDE: "NSG vs. Azure Firewall"]**

A common exam question: what is the difference between an NSG and Azure Firewall?

NSG is a basic Layer 3/4 packet filter. It operates on IP addresses and ports. It is free (no charge for the NSG itself — only associated resource charges). NSGs are suitable for subnet-level and NIC-level traffic control.

Azure Firewall is a fully stateful, managed Layer 3-7 firewall service. It provides application-layer filtering (FQDN filtering), threat intelligence integration, TLS inspection, and centralized logging. Azure Firewall is a premium service with an hourly charge plus data processing fees. It is used for hub-and-spoke network architectures where centralized traffic inspection is required.

For AZ-900: NSGs are free, basic, subnet/NIC level. Azure Firewall is paid, advanced, centralized.

---

## [11:00 - 15:00] Azure DNS and Name Resolution

**[SLIDE: "Azure DNS"]**

Azure DNS is a hosting service for DNS domains, providing name resolution using Microsoft Azure's infrastructure. Azure DNS allows you to manage your DNS records using the same Azure credentials, APIs, tools, and billing as your other Azure services.

Key features:

- Host your public domain (like `contoso.com`) in Azure
- Create A, CNAME, MX, TXT, and other DNS record types
- Ultra-low latency using Azure's anycast network
- 100% SLA uptime commitment (all DNS queries receive responses)
- No support for domain registration — Azure DNS hosts zones, it does not register domain names

**[SLIDE: "Private DNS Zones"]**

Azure Private DNS zones provide name resolution for resources within Azure Virtual Networks without requiring a custom DNS server.

Use case: instead of having VMs communicate using IP addresses like `10.0.1.4`, you can create a private DNS zone `internal.contoso.com` and register VMs as `webserver01.internal.contoso.com`. The name resolves to the private IP automatically.

Private DNS zones can be linked to multiple VNets, enabling name resolution across peered networks.

---

## [15:00 - 19:00] Hybrid Connectivity: VPN Gateway and ExpressRoute

**[SLIDE: "Connecting On-Premises to Azure"]**

Many organizations need connectivity between their on-premises data centers and Azure — to extend their network into the cloud, to access Azure resources from on-premises systems, or to implement a hybrid cloud deployment model.

Azure provides two primary connectivity options for this.

**[SLIDE: "Azure VPN Gateway"]**

A VPN Gateway creates an encrypted tunnel over the public internet between an on-premises network and an Azure Virtual Network. This is a Site-to-Site VPN — the same technology used for corporate remote access, applied at the network level.

Key characteristics:

- Encrypted with IPsec/IKE protocols
- Runs over the public internet (not dedicated bandwidth)
- Bandwidth up to 10 Gbps depending on gateway SKU
- Lower cost — starts at approximately $27/month per gateway
- Setup time: hours to days
- Suitable for: smaller organizations, development environments, backup connectivity

**[SLIDE: "Azure ExpressRoute"]**

ExpressRoute is a dedicated private network connection between your on-premises infrastructure and Azure, established through a connectivity provider's network — it does not use the public internet at all.

Key characteristics:

- Not encrypted by default (connection is private, not encrypted — add encryption if needed)
- Private dedicated bandwidth: 50 Mbps to 100 Gbps
- Lower latency than internet-based VPN
- Higher reliability (uptime SLA)
- Higher cost — circuit fees plus provider fees; can be thousands per month
- Setup time: weeks to months (physical circuit provisioning)
- Suitable for: enterprises with large data transfer requirements, financial services, healthcare, compliance requirements prohibiting public internet data transit

**[SLIDE: "VPN vs. ExpressRoute Comparison"]**

| Factor | VPN Gateway | ExpressRoute |
|---|---|---|
| Connection path | Public internet (encrypted) | Private dedicated circuit |
| Bandwidth | Up to 10 Gbps | 50 Mbps to 100 Gbps |
| Latency | Variable (internet) | Consistent (dedicated) |
| Cost | Lower | Higher |
| Setup time | Hours-days | Weeks-months |
| SLA | 99.9% | 99.95% |
| Encryption | Yes (IPsec) | Not by default |
| Best for | Small-medium, dev/test | Enterprise, compliance-sensitive |

---

## [19:00 - 21:30] VNet Peering and Service Endpoints

**[SLIDE: "VNet Peering"]**

VNet peering connects two Azure Virtual Networks so that resources in both networks can communicate as if they are on the same private network. Peered VNets can be in the same region (local peering) or different regions (global peering).

Key characteristics:

- Traffic stays on Azure's private backbone — never crosses the public internet
- Very low latency — comparable to traffic within a single VNet
- Not transitive: if VNet A is peered with VNet B, and VNet B is peered with VNet C, VNet A cannot communicate with VNet C through that indirect path. VNet A and C must be directly peered.
- Bidirectional peering must be established from both sides

**[SLIDE: "Service Endpoints and Private Endpoints"]**

**Service Endpoints** extend a VNet's identity to Azure services (like Azure Storage and Azure SQL) over the Azure backbone network, so that traffic to those services does not traverse the public internet.

**Private Endpoints** create a private IP address within your VNet for a specific Azure service instance. This makes the Azure service appear as if it is part of your VNet, with a private IP that only your VNet resources can reach.

---

## [21:30 - 23:30] Lab Preview

**[SLIDE: "Module 05 Lab"]**

In today's lab you will:

1. Create a Virtual Network with two subnets using `az network vnet create`
2. Create a Network Security Group using `az network nsg create`
3. Add inbound rules allowing HTTP and SSH using `az network nsg rule create`
4. Associate the NSG with a subnet
5. List NSG rules and verify configuration
6. Deploy a VM into the VNet and test connectivity

This is a foundational lab — every real Azure deployment involves VNet and NSG configuration. The commands you practice today are used in nearly every module going forward.

---

## [23:30 - 24:00] Closing

**[INSTRUCTOR ON CAMERA]**

You now understand Azure Virtual Networking — VNets, subnets, NSGs, DNS, VPN Gateway, ExpressRoute, and VNet peering. These concepts appear throughout AZ-900 and are fundamental to any cloud infrastructure role.

In Module 06, we cover Azure Storage Services — Blob Storage, File Storage, Queue Storage, and Table Storage. Storage is the foundation for data persistence in the cloud. See you there.

---

**References:**

- learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
- learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview
- learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways
- learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction

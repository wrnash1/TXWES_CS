# Reading Guide: Module 08 — Azure Networking

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Domain: Describe Azure Architecture and Services (35–40% of exam)

---

## Introduction

Azure networking services connect your cloud resources to each other, to end users, and to your on-premises environments. Networking is the infrastructure layer that all application services depend on. AZ-900 tests your ability to identify the correct networking service for a given scenario and to explain the key differences between similar services. This guide covers the nine core Azure networking topics: VNets, subnets, NSGs, Azure Firewall, VPN Gateway, ExpressRoute, Azure DNS, Application Gateway, and Azure Load Balancer.

---

## Section 1: Azure Virtual Networks and Subnets

### 1.1 Virtual Network Fundamentals

An Azure Virtual Network (VNet) is a logically isolated, private network within Azure. It is the foundational component for networking all Azure resources.

Core VNet properties:

| Property | Description |
|---|---|
| Address space | One or more CIDR ranges defining the private IP space (e.g., 10.0.0.0/16) |
| Region scope | A VNet exists in a single Azure region |
| Isolation | VNets are isolated from each other by default |
| DNS | Uses Azure-provided DNS by default; custom DNS servers configurable |
| Peering | Connect VNets with VNet Peering for private cross-VNet communication |

### 1.2 Subnets

Subnets segment a VNet's address space into smaller, distinct networks.

| Subnet Concept | Detail |
|---|---|
| Address range | Must be within the VNet's address space |
| Reserved addresses | Azure reserves 5 IPs per subnet: network address, default gateway, Azure DNS IPs (2), and broadcast address |
| NSG association | Each subnet can have one NSG; each NIC can also have one NSG |
| Service delegation | Subnets can be delegated to specific Azure services (e.g., Azure SQL Managed Instance) |
| Route table | Custom route tables (User-Defined Routes) can override Azure's default routing |

Example subnet design for a three-tier app:

| Subnet Name | CIDR | Purpose |
|---|---|---|
| frontend-subnet | 10.0.1.0/24 | Web servers, Application Gateway |
| backend-subnet | 10.0.2.0/24 | Application servers |
| db-subnet | 10.0.3.0/24 | Database servers |
| AzureFirewallSubnet | 10.0.4.0/26 | Required name for Azure Firewall (minimum /26) |
| GatewaySubnet | 10.0.5.0/27 | Required name for VPN/ExpressRoute gateway |

### 1.3 VNet Peering

VNet Peering connects two VNets, enabling private IP communication between resources in each VNet.

| Feature | Regional Peering | Global Peering |
|---|---|---|
| Scope | Same Azure region | Different Azure regions |
| Latency | Lowest | Low (varies by distance) |
| Cost | Ingress/egress fees within region | Peering charges apply |
| Transitivity | Non-transitive by default | Non-transitive by default |

Non-transitive means: if A peers with B and B peers with C, A cannot reach C through B without direct peering or a network virtual appliance acting as a hub.

---

## Section 2: Network Security Groups

### 2.1 NSG Structure

An NSG is a list of access control rules (allow/deny) applied to inbound and outbound network traffic.

| Rule Property | Description |
|---|---|
| Priority | 100–4096; lower numbers processed first; rules stop at first match |
| Protocol | TCP, UDP, ICMP, or Any |
| Source | IP address, CIDR, service tag, or application security group |
| Destination | IP address, CIDR, service tag, or application security group |
| Port | Single port, range, or Any |
| Action | Allow or Deny |

### 2.2 Default NSG Rules

Every NSG includes default rules that cannot be deleted:

| Rule Name | Priority | Direction | Action | Description |
|---|---|---|---|---|
| AllowVnetInBound | 65000 | Inbound | Allow | All VNet-to-VNet inbound traffic |
| AllowAzureLoadBalancerInBound | 65001 | Inbound | Allow | Azure Load Balancer health probes |
| DenyAllInBound | 65500 | Inbound | Deny | Deny all other inbound traffic |
| AllowVnetOutBound | 65000 | Outbound | Allow | All VNet-to-VNet outbound traffic |
| AllowInternetOutBound | 65001 | Outbound | Allow | All outbound internet traffic |
| DenyAllOutBound | 65500 | Outbound | Deny | Deny all other outbound traffic |

### 2.3 Service Tags

Service tags are named groups of IP address prefixes for Azure services. Using service tags in NSG rules avoids hardcoding IP ranges that change over time.

Common service tags:

| Tag | Represents |
|---|---|
| Internet | Public internet IP space |
| AzureLoadBalancer | Azure Load Balancer probe source IPs |
| VirtualNetwork | All VNet address spaces (current and peered) |
| Storage | Azure Storage service IP ranges |
| Sql | Azure SQL service IP ranges |
| AzureCloud | All Azure datacenter IP ranges |

---

## Section 3: Azure Firewall

### 3.1 Overview

Azure Firewall is a managed, stateful, cloud-native Layer 7 network security service. It is deployed as a dedicated resource in a VNet and provides centralized traffic control for all resources.

### 3.2 Rule Types

| Rule Collection Type | OSI Layer | Filters On | Example Use |
|---|---|---|---|
| Application rules | Layer 7 | FQDN, URL, HTTP/HTTPS | Allow *.windowsupdate.com outbound |
| Network rules | Layer 3/4 | IP address, port, protocol | Allow 10.0.2.0/24 to reach 10.0.3.5:1433 |
| NAT rules | Layer 3/4 | Inbound public IP → private IP mapping | Forward public:80 to 10.0.1.5:80 |

### 3.3 NSG vs. Azure Firewall

| Feature | Network Security Group | Azure Firewall |
|---|---|---|
| OSI layer | Layer 3/4 | Layer 3/4/7 |
| FQDN filtering | No | Yes |
| Threat intelligence | No | Yes |
| Centralized management | Per VNet/subnet | Single instance, hub VNet |
| Cost | Free | Per-hour + per-GB |
| Deployment | Attached to subnet or NIC | Dedicated subnet in VNet |
| Best for | Fine-grained subnet/NIC rules | Enterprise-wide traffic policy |

---

## Section 4: Hybrid Connectivity — VPN Gateway and ExpressRoute

### 4.1 VPN Gateway

VPN Gateway enables encrypted connectivity between Azure VNets and on-premises networks over the public internet.

| Connection Type | Description | Use Case |
|---|---|---|
| Site-to-Site (S2S) | On-premises VPN device to Azure VPN Gateway | Connect entire on-premises network |
| Point-to-Site (P2S) | Individual client device to Azure VNet | Remote worker VPN access |
| VNet-to-VNet | Azure VNet to Azure VNet via gateway | Cross-subscription or cross-region VNet connectivity with gateway |

VPN Gateway SKUs:

| SKU | Max Throughput | Max S2S Tunnels |
|---|---|---|
| Basic | 100 Mbps | 10 |
| VpnGw1 | 650 Mbps | 30 |
| VpnGw2 | 1 Gbps | 30 |
| VpnGw3 | 1.25 Gbps | 30 |
| VpnGw4 | 5 Gbps | 100 |
| VpnGw5 | 10 Gbps | 100 |

Deployment note: VPN Gateway requires a dedicated subnet named exactly `GatewaySubnet`. It cannot be shared with other resources.

### 4.2 ExpressRoute

ExpressRoute creates a private, dedicated Layer 3 connection between on-premises infrastructure and Azure, bypassing the public internet entirely.

| Feature | VPN Gateway | ExpressRoute |
|---|---|---|
| Path | Public internet (encrypted) | Private dedicated circuit |
| Bandwidth | Up to 10 Gbps | Up to 100 Gbps |
| Latency | Variable (internet dependent) | Consistent, low latency |
| Cost | Lower | Higher (circuit + provider fees) |
| SLA | 99.9% | 99.95% |
| Setup time | Hours | Weeks (physical circuit provisioning) |
| Use case | General hybrid connectivity | High-bandwidth, low-latency, regulated |

ExpressRoute connection models:

- **CloudExchange co-location** — At a facility where your equipment and Microsoft's meet (e.g., Equinix)
- **Point-to-point Ethernet** — Dedicated circuit from your site to Azure
- **Any-to-any (IPVPN)** — Integrate Azure into your existing MPLS WAN

### 4.3 AZ-900 Exam Signal for Hybrid Connectivity

Use these signals to identify the correct answer:

- "Encrypted connection over internet" → VPN Gateway
- "Private, dedicated, bypasses internet" → ExpressRoute
- "Remote workers connecting to Azure resources" → Point-to-Site VPN
- "Connect entire on-premises datacenter to Azure" → Site-to-Site VPN or ExpressRoute

---

## Section 5: Azure DNS

### 5.1 Public DNS Zones

Azure DNS hosts public DNS zones and responds to DNS queries from the internet. You delegate a domain (e.g., contoso.com) to Azure DNS name servers and manage all DNS records (A, CNAME, MX, TXT, etc.) from the Azure Portal or CLI.

### 5.2 Private DNS Zones

Azure Private DNS provides name resolution within VNets without internet exposure. Private zones can be linked to one or more VNets for automatic registration and resolution of VM hostnames.

| Feature | Public DNS Zone | Private DNS Zone |
|---|---|---|
| Resolvable from | Internet | Linked VNets only |
| Auto-registration | No | Optional (registers VM hostnames) |
| Use case | External-facing domains | Internal resource name resolution |

---

## Section 6: Azure Load Balancer and Application Gateway

### 6.1 Azure Load Balancer

Azure Load Balancer operates at OSI Layer 4 (transport layer), distributing TCP and UDP traffic across backend resources.

| Feature | Detail |
|---|---|
| OSI Layer | Layer 4 (TCP/UDP) |
| Type | Public (internet-facing) or Internal (VNet-only) |
| Algorithm | 5-tuple hash (source IP, source port, destination IP, destination port, protocol) |
| Health probes | TCP, HTTP, HTTPS — removes unhealthy backends |
| SLA | 99.99% |
| Tier | Basic (free, limited) or Standard (recommended, more features) |

### 6.2 Application Gateway

Azure Application Gateway operates at OSI Layer 7 (application layer), making routing decisions based on HTTP/HTTPS attributes.

| Feature | Detail |
|---|---|
| OSI Layer | Layer 7 (HTTP/HTTPS) |
| Routing options | URL path-based, hostname-based, header-based |
| SSL/TLS termination | Yes — decrypts at gateway, backends see plain HTTP |
| Web Application Firewall | Available as WAF tier (OWASP 3.2 rules) |
| Session affinity | Cookie-based sticky sessions |
| Autoscaling | Available in v2 SKU |

### 6.3 Load Balancer vs. Application Gateway

| Factor | Azure Load Balancer | Application Gateway |
|---|---|---|
| OSI Layer | 4 | 7 |
| Protocol awareness | TCP/UDP | HTTP/HTTPS |
| Routing decisions | IP/port | URL path, hostname, headers |
| SSL termination | No | Yes |
| WAF protection | No | Yes (WAF tier) |
| Cost | Lower | Higher |
| AZ-900 trigger words | "Distribute TCP traffic," "Layer 4" | "URL routing," "SSL termination," "WAF," "Layer 7" |

---

## Section 7: Networking Service Summary Table

| Service | Purpose | OSI Layer | AZ-900 Trigger Words |
|---|---|---|---|
| Virtual Network (VNet) | Private IP network in Azure | N/A | "Isolate resources," "private network in Azure" |
| Subnet | Segment a VNet | N/A | "Divide network," "separate tiers" |
| Network Security Group | IP/port traffic filtering | 3/4 | "Allow/deny traffic," "port filter," "inbound rules" |
| Azure Firewall | Centralized FQDN + threat-aware filtering | 3/4/7 | "FQDN filtering," "enterprise firewall," "threat intelligence" |
| VPN Gateway | Encrypted on-prem to Azure over internet | 3 | "Site-to-Site VPN," "Point-to-Site VPN," "IPsec" |
| ExpressRoute | Private dedicated on-prem to Azure circuit | 3 | "Private connection," "bypass internet," "dedicated circuit" |
| Azure DNS | DNS hosting (public and private) | Application | "Host DNS records," "name resolution," "private DNS" |
| Azure Load Balancer | Layer 4 TCP/UDP load distribution | 4 | "Distribute TCP traffic," "Layer 4 LB" |
| Application Gateway | Layer 7 HTTP/HTTPS routing + WAF | 7 | "URL-based routing," "WAF," "SSL termination" |

---

## Section 8: Azure CLI Reference

```bash
# Create a Virtual Network with a subnet
az network vnet create \
  --resource-group lab08-rg \
  --name lab08-vnet \
  --address-prefix 10.0.0.0/16 \
  --subnet-name frontend-subnet \
  --subnet-prefix 10.0.1.0/24

# Add a second subnet
az network vnet subnet create \
  --resource-group lab08-rg \
  --vnet-name lab08-vnet \
  --name backend-subnet \
  --address-prefix 10.0.2.0/24

# Create an NSG
az network nsg create \
  --resource-group lab08-rg \
  --name lab08-nsg

# Add an inbound HTTP allow rule
az network nsg rule create \
  --resource-group lab08-rg \
  --nsg-name lab08-nsg \
  --name AllowHTTP \
  --protocol tcp \
  --direction inbound \
  --priority 100 \
  --source-address-prefix "*" \
  --source-port-range "*" \
  --destination-address-prefix "*" \
  --destination-port-range 80 \
  --access allow

# Associate NSG with a subnet
az network vnet subnet update \
  --resource-group lab08-rg \
  --vnet-name lab08-vnet \
  --name frontend-subnet \
  --network-security-group lab08-nsg

# Show VNet details
az network vnet show \
  --resource-group lab08-rg \
  --name lab08-vnet
```

---

## Section 9: AZ-900 Exam Tips

1. **VPN Gateway vs. ExpressRoute:** VPN uses the public internet (encrypted with IPsec). ExpressRoute uses a private dedicated circuit that never touches the public internet. If a scenario mentions "private," "dedicated," or "bypass internet," the answer is ExpressRoute.

2. **NSG scope:** NSGs can be associated with subnets (affecting all resources in the subnet) or with individual network interface cards (affecting only that specific VM). Both can be applied simultaneously — traffic must pass both NSGs.

3. **Load Balancer Layer 4 vs. Application Gateway Layer 7:** If a scenario mentions routing based on URL path (e.g., `/api` goes to different servers than `/web`), the answer is Application Gateway. If it simply says "distribute traffic across multiple VMs," Load Balancer is sufficient.

4. **WAF is on Application Gateway:** Web Application Firewall (WAF) is a tier of Application Gateway, not a separate service. If a scenario mentions protecting against SQL injection or XSS attacks at the load balancing layer, Application Gateway with WAF is the answer.

5. **VNet is region-scoped:** A single VNet cannot span regions. To connect resources across regions, use VNet Peering (Global) or VPN Gateway.

6. **GatewaySubnet is reserved:** The subnet named `GatewaySubnet` is reserved for VPN and ExpressRoute gateways. It cannot contain other resources. The AzureFirewallSubnet is similarly reserved for Azure Firewall.

7. **Site-to-Site vs. Point-to-Site:** S2S connects an entire on-premises network to Azure using a VPN device. P2S connects individual computers to Azure (used for remote workers). If a scenario mentions connecting an entire office to Azure, S2S is correct.

8. **Azure DNS is not a domain registrar:** Azure DNS hosts DNS zones and records but does not register domain names. You register elsewhere and delegate DNS management to Azure.

---

## Section 10: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the VPN Gateway vs. ExpressRoute comparison table (Section 4.2)
- [ ] Memorize the Load Balancer vs. Application Gateway comparison table (Section 6.3)
- [ ] Understand the NSG default rules (Section 2.2)
- [ ] Memorize the networking service summary table (Section 7)
- [ ] Complete the Microsoft Learn "Describe Azure networking services" module
- [ ] Complete Lab Module 08
- [ ] Take Quiz Module 08
- [ ] Post Discussion Module 08 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## Required Reading Resources

- Azure VNet overview: learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
- Azure NSG overview: learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview
- Azure Firewall overview: learn.microsoft.com/en-us/azure/firewall/overview
- VPN Gateway overview: learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways
- ExpressRoute overview: learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction
- Application Gateway overview: learn.microsoft.com/en-us/azure/application-gateway/overview
- Azure Load Balancer overview: learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview

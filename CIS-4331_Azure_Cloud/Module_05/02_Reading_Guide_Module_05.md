# Reading Guide: Module 05 - Azure Virtual Networking

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)

---

## Introduction

Azure Virtual Networking is the foundation for all communication between Azure resources, between Azure and on-premises environments, and between Azure and the internet. Every VM, database, container, and app service lives within or connects through a virtual network. This module covers the networking services that AZ-900 tests most frequently.

---

## Section 1: Azure Virtual Networks (VNets)

### 1.1 VNet Definition and Purpose

An Azure Virtual Network (VNet) is a logically isolated network within Azure. It provides the communication infrastructure for Azure resources, enabling secure communication between VMs, PaaS services, and on-premises networks.

A VNet:

- Is scoped to a single Azure region
- Has an address space defined in CIDR notation (e.g., `10.0.0.0/16`)
- Can be divided into subnets
- Provides isolation from other Azure customers' networks
- Can be connected to other VNets through peering
- Can be connected to on-premises networks through VPN Gateway or ExpressRoute

### 1.2 VNet Address Space

The address space defines the range of private IP addresses available within the VNet. Azure recommends using private IP address ranges:

- 10.0.0.0/8 (10.x.x.x)
- 172.16.0.0/12 (172.16.x.x - 172.31.x.x)
- 192.168.0.0/16 (192.168.x.x)

CIDR notation refresher: `/16` means 16 bits are fixed (the network portion) and the remaining 16 bits are host addresses — giving 65,536 addresses. `/24` gives 256 addresses. `/28` gives 16 addresses.

Azure reserves 5 IP addresses in each subnet (first 4 and last 1) for its own use. A `/28` subnet has 16 addresses minus 5 reserved = 11 usable addresses.

### 1.3 Subnets

Subnets divide a VNet's address space into smaller segments. Each subnet:

- Must have a unique, non-overlapping address range within the VNet
- Can have its own Network Security Group
- Can have its own route table
- Belongs to exactly one VNet

Common subnet patterns:

| Subnet Name | Purpose | Example Range |
|---|---|---|
| GatewaySubnet | Reserved for VPN/ExpressRoute gateway (name is mandatory) | 10.0.0.0/27 |
| AzureFirewallSubnet | Reserved for Azure Firewall (name is mandatory) | 10.0.1.0/26 |
| web-subnet | Internet-facing web servers | 10.0.2.0/24 |
| app-subnet | Internal application servers | 10.0.3.0/24 |
| db-subnet | Database servers | 10.0.4.0/24 |

Some Azure services require their own dedicated subnet with specific names (GatewaySubnet, AzureFirewallSubnet, AzureBastionSubnet).

### 1.4 Public and Private IP Addresses

| Type | Allocation | Scope | Use Case |
|---|---|---|---|
| Private IP | Dynamic (DHCP) or Static | Within VNet only | VM-to-VM, internal services |
| Public IP (Basic) | Dynamic or Static | Internet-reachable | Legacy, not zone-redundant |
| Public IP (Standard) | Always Static | Internet-reachable, zone-redundant | New deployments |

Dynamic public IPs change when the VM is deallocated. Static public IPs retain the same address regardless of VM state.

---

## Section 2: Network Security Groups

### 2.1 NSG Purpose and Scope

A Network Security Group (NSG) is a virtual firewall that filters network traffic using security rules. NSGs operate at Layer 3 and Layer 4 of the network stack (IP, TCP/UDP) — they are not application-aware.

NSGs can be associated with:

- **Subnets:** Rules apply to all resources in the subnet
- **Network Interfaces (NICs):** Rules apply to the specific VM's NIC

Both can be applied simultaneously. Inbound traffic is evaluated by the subnet NSG first, then the NIC NSG. Outbound traffic is evaluated by the NIC NSG first, then the subnet NSG.

### 2.2 NSG Rule Properties

Each NSG rule has the following properties:

| Property | Description | Values |
|---|---|---|
| Name | Descriptive identifier | Text string |
| Priority | Evaluation order — lower = higher priority | 100-4096 |
| Source | Source IP, range, Service Tag, or Application Security Group | IP/CIDR/Tag |
| Source Port Range | Source port(s) | Port number, range, or * |
| Destination | Destination IP, range, Service Tag | IP/CIDR/Tag |
| Destination Port Range | Destination port(s) | Port number, range, or * |
| Protocol | TCP, UDP, ICMP, or Any | Dropdown |
| Direction | Inbound or Outbound | |
| Action | Allow or Deny | |

### 2.3 Default NSG Rules

Azure adds these default rules to every NSG. They cannot be deleted but can be overridden with lower priority numbers (higher priority):

**Default inbound rules:**

| Priority | Name | Source | Destination | Port | Protocol | Action |
|---|---|---|---|---|---|---|
| 65000 | AllowVnetInBound | VirtualNetwork | VirtualNetwork | Any | Any | Allow |
| 65001 | AllowAzureLoadBalancerInBound | AzureLoadBalancer | Any | Any | Any | Allow |
| 65500 | DenyAllInBound | Any | Any | Any | Any | Deny |

**Default outbound rules:**

| Priority | Name | Source | Destination | Port | Protocol | Action |
|---|---|---|---|---|---|---|
| 65000 | AllowVnetOutBound | VirtualNetwork | VirtualNetwork | Any | Any | Allow |
| 65001 | AllowInternetOutBound | Any | Internet | Any | Any | Allow |
| 65500 | DenyAllOutBound | Any | Any | Any | Any | Deny |

### 2.4 Service Tags

Service tags are named groups of IP address ranges for specific Azure services. Using service tags in NSG rules avoids the need to maintain lists of IP addresses manually.

Common service tags:

| Tag | Represents |
|---|---|
| VirtualNetwork | All IP addresses in the VNet and peered VNets |
| AzureLoadBalancer | Azure Load Balancer health probe source IPs |
| Internet | All public internet IP addresses |
| Storage | Azure Storage service IP ranges |
| Sql | Azure SQL and Azure Synapse IP ranges |
| AzureActiveDirectory | Microsoft Entra ID IP ranges |
| AppService | Azure App Service outbound IPs |

### 2.5 NSG vs. Azure Firewall

| Feature | NSG | Azure Firewall |
|---|---|---|
| Layer | Layer 3/4 (IP/port) | Layer 3-7 (including FQDN, TLS) |
| Cost | Free (resource charges only) | Hourly + data processing fees |
| Placement | Subnet or NIC | Dedicated subnet, hub VNet |
| FQDN filtering | No | Yes |
| Threat intelligence | No | Yes |
| Centralized management | No (per-subnet/NIC) | Yes (single managed service) |
| Logging | NSG Flow Logs (optional) | Built-in structured logging |
| Best for | Basic subnet/NIC security rules | Enterprise centralized network security |

---

## Section 3: Azure Load Balancer and Application Gateway

### 3.1 Azure Load Balancer

Azure Load Balancer operates at Layer 4 (TCP/UDP). It distributes inbound traffic across multiple backend VMs based on a hash of the source IP, source port, destination IP, destination port, and protocol.

Use cases: Load balancing TCP/UDP traffic to VMs. Load balancing internal service-to-service traffic. Supporting VM Scale Sets.

SLA: 99.99% for Standard SKU.

### 3.2 Azure Application Gateway

Azure Application Gateway operates at Layer 7 (HTTP/HTTPS). It provides:

- URL-based routing (route /api requests to one VM group, /images to another)
- SSL/TLS termination
- Web Application Firewall (WAF) capability
- Session affinity (sticky sessions)
- Header rewriting

Use cases: HTTP/HTTPS load balancing, centralized SSL termination, protecting web apps from OWASP vulnerabilities.

---

## Section 4: Azure DNS

### 4.1 Public DNS Zones

Azure DNS hosts public DNS zones, providing name resolution for internet-facing domains. You can host your domain (e.g., `contoso.com`) in Azure DNS and create records using the Azure Portal or CLI.

Supported record types: A, AAAA, CNAME, MX, NS, PTR, SRV, TXT, CAA, SOA.

Azure DNS uses anycast routing to serve DNS queries from the closest Azure DNS server globally, minimizing resolution latency.

### 4.2 Private DNS Zones

Azure Private DNS zones provide name resolution within Azure Virtual Networks without requiring a custom DNS server.

Key features:

- Register VM names automatically when linked to a VNet with auto-registration enabled
- Name resolution spans peered VNets when the zone is linked to multiple VNets
- DNS names resolve to private IP addresses — not publicly accessible

Example: A private zone `internal.corp` is linked to VNet A and VNet B. A VM in VNet A registers as `webserver01.internal.corp`. A VM in VNet B can resolve `webserver01.internal.corp` to its private IP.

### 4.3 DNS Resolution in Azure VMs

By default, Azure VMs use Azure-provided DNS, which resolves:

- Azure internal names (e.g., `webserver01.internal.cloudapp.azure.com`)
- Public internet domain names

When a Private DNS zone is linked to the VNet, Azure uses the Private DNS zone for names in that zone's domain.

---

## Section 5: Hybrid Connectivity

### 5.1 Azure VPN Gateway

A VPN Gateway creates encrypted tunnels between an Azure VNet and an on-premises network (Site-to-Site) or individual client computers (Point-to-Site).

Types of VPN connections:

| Connection Type | Description |
|---|---|
| Site-to-Site (S2S) | Connects on-premises network to Azure VNet over IPsec/IKE tunnel |
| Point-to-Site (P2S) | Connects individual computers to Azure VNet (remote worker scenario) |
| VNet-to-VNet | Connects two Azure VNets using VPN (alternative to VNet peering) |

VPN Gateway SKUs and bandwidth:

| SKU | Max Throughput | Notes |
|---|---|---|
| Basic | 100 Mbps | Legacy — not recommended for new deployments |
| VpnGw1 | 650 Mbps | Entry production |
| VpnGw2 | 1 Gbps | Mid-range |
| VpnGw3 | 1.25 Gbps | High throughput |
| VpnGw4/5 | Up to 10 Gbps | Premium |

VPN Gateway requires the `GatewaySubnet` subnet in the VNet. This subnet must be named exactly `GatewaySubnet` — Azure enforces this naming.

### 5.2 Azure ExpressRoute

ExpressRoute is a dedicated private connection between an on-premises network and Azure datacenters, provided by a connectivity partner (AT&T, Equinix, Verizon, etc.). Traffic does not traverse the public internet.

ExpressRoute connection models:

| Model | Description |
|---|---|
| Co-location at cloud exchange | Direct connectivity at a partner facility with Azure |
| Point-to-point Ethernet | Dedicated Ethernet circuit from your site to Azure |
| Any-to-any (IPVPN) | Connectivity through an MPLS network |
| ExpressRoute Direct | Direct physical connection to Microsoft's global network (10/100 Gbps) |

### 5.3 VPN Gateway vs. ExpressRoute

| Characteristic | VPN Gateway | ExpressRoute |
|---|---|---|
| Path | Public internet (encrypted) | Private circuit (not encrypted by default) |
| Bandwidth | Up to 10 Gbps | 50 Mbps to 100 Gbps |
| Latency | Variable | Consistent, low |
| Cost | ~$27/month + data | Provider fees + Azure fees (high) |
| Setup time | Hours to days | Weeks to months |
| Uptime SLA | 99.9% (zone-redundant: 99.99%) | 99.95% |
| Best for | SMB, dev/test, backup | Enterprise, compliance, high-volume data |

---

## Section 6: VNet Peering and Private Endpoints

### 6.1 VNet Peering

VNet peering connects two VNets so that resources communicate as if they are on the same network. Peering types:

- **Local (regional) peering:** Both VNets in the same region. Lowest latency.
- **Global peering:** VNets in different regions. Slightly higher latency but traffic stays on Azure backbone.

Peering characteristics:

- Not transitive: A-B peering + B-C peering does not give A-C connectivity
- Bidirectional: must be configured from both VNets
- No encryption: traffic on Azure's private backbone is not encrypted in transit (add encryption if required)

### 6.2 Service Endpoints

Service endpoints extend a VNet's address space to Azure PaaS services (Storage, SQL, etc.) over the Azure backbone. Traffic to the service stays on the Microsoft network rather than traversing the public internet.

Limitation: The service endpoint extends VNet access, but the service still has a public IP. Network rules on the service are used to restrict access to the VNet.

### 6.3 Private Endpoints

Private endpoints create a network interface with a private IP address within your VNet for a specific Azure service instance. The service appears as a private resource:

- Accessible only from within the VNet (or connected on-premises networks)
- No public IP required for the service
- DNS resolution returns the private IP address

Private endpoints provide stronger isolation than service endpoints and are the recommended approach for production workloads.

---

## Section 7: Azure CLI Commands for Networking

```bash
# Create a Virtual Network
az network vnet create \
  --resource-group "lab05-rg" \
  --name "lab05-vnet" \
  --address-prefix "10.0.0.0/16" \
  --subnet-name "web-subnet" \
  --subnet-prefix "10.0.1.0/24"

# Add a subnet to an existing VNet
az network vnet subnet create \
  --resource-group "lab05-rg" \
  --vnet-name "lab05-vnet" \
  --name "db-subnet" \
  --address-prefix "10.0.2.0/24"

# List subnets in a VNet
az network vnet subnet list \
  --resource-group "lab05-rg" \
  --vnet-name "lab05-vnet" \
  --output table

# Create an NSG
az network nsg create \
  --resource-group "lab05-rg" \
  --name "web-nsg"

# Add an inbound NSG rule
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

# List NSG rules
az network nsg rule list \
  --resource-group "lab05-rg" \
  --nsg-name "web-nsg" \
  --output table

# Associate NSG with subnet
az network vnet subnet update \
  --resource-group "lab05-rg" \
  --vnet-name "lab05-vnet" \
  --name "web-subnet" \
  --network-security-group "web-nsg"

# Create a public IP address
az network public-ip create \
  --resource-group "lab05-rg" \
  --name "lab05-pip" \
  --sku Standard \
  --allocation-method Static
```

Reference: learn.microsoft.com/en-us/cli/azure/network

---

## Section 8: Azure Networking Service Comparison

| Service | Layer | Purpose | Cost |
|---|---|---|---|
| Virtual Network | L3 | Provides private network space for Azure resources | Free |
| Network Security Group | L3/4 | Filters traffic by IP/port | Free |
| Azure Firewall | L3-7 | Centralized network security with app-layer filtering | Paid (hourly) |
| Azure Load Balancer | L4 | Distributes TCP/UDP traffic across VMs | Paid (Standard SKU) |
| Application Gateway | L7 | HTTP/HTTPS load balancing with WAF | Paid |
| Azure DNS | DNS | Hosts DNS zones and records | Paid (per zone + queries) |
| VPN Gateway | VPN | Encrypted internet tunnel to on-premises | Paid (hourly per gateway) |
| ExpressRoute | Private circuit | Dedicated private connection to on-premises | High (provider + Azure) |
| VNet Peering | L3 | Connects two VNets privately | Paid (per GB transferred) |

---

## Section 9: AZ-900 Exam Tips

1. **NSG evaluation order:** Rules are evaluated from lowest priority number to highest. The first matching rule is applied and evaluation stops. Always design with this in mind — a low-priority (high-number) allow rule will never be reached if a higher-priority deny rule matches first.

2. **Default deny:** The NSG default rule at priority 65500 denies all inbound traffic from the internet. This means no traffic reaches your VM from the internet unless you explicitly add an allow rule with priority lower than 65500.

3. **VNet is region-scoped:** A VNet exists in one region. Connecting resources in different regions requires VNet peering or a VPN. The exam may test whether you understand that VNets cannot span regions.

4. **VPN vs. ExpressRoute key difference:** VPN uses the public internet (encrypted). ExpressRoute uses a private circuit (not encrypted by default). The exam asks this frequently in compliance and security scenarios. If data must not traverse the public internet, ExpressRoute is the answer.

5. **GatewaySubnet naming:** The subnet used by VPN Gateway must be named exactly `GatewaySubnet`. This is a frequently tested specific requirement.

6. **VNet peering is not transitive:** A peer to B and B peer to C does not give A connectivity to C. This is a common exam trap. Transitivity requires configuring A-C peering directly or using a hub-and-spoke topology with a network virtual appliance.

7. **Service Endpoint vs. Private Endpoint:** Service endpoints extend VNet identity to services but do not give private IPs. Private endpoints create actual private IP addresses within your VNet for specific service instances. Private endpoints are more secure and recommended for production.

8. **NSG vs. Azure Firewall:** NSGs are free and operate at L3/4. Azure Firewall is paid and operates at L3-7 with application-layer filtering. For basic port-based traffic filtering, use NSGs. For centralized, application-aware filtering, use Azure Firewall.

---

## Section 10: Required Resources

- Azure Virtual Network: learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
- Network Security Groups: learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview
- VPN Gateway: learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways
- ExpressRoute: learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction
- Azure DNS: learn.microsoft.com/en-us/azure/dns/dns-overview
- Microsoft Learn AZ-900 networking module: learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/

---

## Section 11: Study Checklist

- [ ] Read all sections of this guide
- [ ] Memorize the NSG default rules table (Section 2.3)
- [ ] Memorize the VPN vs. ExpressRoute comparison table (Section 5.3)
- [ ] Understand all CLI commands in Section 7
- [ ] Complete Lab Activity Module 05
- [ ] Take Quiz Module 05
- [ ] Post Discussion Module 05 initial post by Wednesday 11:59 PM
- [ ] Respond to two classmates by Sunday 11:59 PM

---

## 9. Supplemental Resources

**1. Microsoft Learn — Azure Virtual Network overview**
https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
Comprehensive reference covering VNet concepts, address spaces, subnets, DNS settings, peering, and service endpoints — foundational reading for all AZ-900 and AZ-104 networking questions.

**2. Microsoft Learn — Network security groups overview**
https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview
Deep dive into NSG rule structure, default rules, priority evaluation, effective security rules, and the difference between inbound and outbound rule processing.

**3. Microsoft Learn — Azure VPN Gateway documentation**
https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways
Explains Site-to-Site, Point-to-Site, and VNet-to-VNet gateway types, SKU tiers, BGP routing, and the distinction between VPN Gateway and ExpressRoute for hybrid connectivity.

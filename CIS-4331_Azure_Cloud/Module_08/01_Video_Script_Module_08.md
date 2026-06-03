# Video Script: Module 08 — Azure Networking

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Microsoft Azure Fundamentals (AZ-900)

---

## Opening (0:00–1:00)

Welcome to Module 08 of CIS-4331 Azure Cloud Computing. I'm Professor Nash. Today we are covering Azure Networking — one of the largest and most important topic areas in AZ-900 and in real-world cloud architecture.

Networking in Azure is what ties everything together. VMs, databases, App Services, and containers all need to communicate — with each other, with users, and with your on-premises data center. Azure provides a rich portfolio of networking services that give you control over traffic, security, connectivity, and performance. By the end of this module, you will understand how Azure networks are structured, how traffic is secured and routed, and how Azure connects to the internet and to on-premises environments.

---

## Section 1: Azure Virtual Networks (1:00–5:00)

### What Is a Virtual Network?

An Azure Virtual Network, or VNet, is the foundational networking building block in Azure. A VNet is a logically isolated network in the Azure cloud. It is your private IP address space in Azure — similar to a traditional on-premises network, but running in Microsoft's infrastructure.

Resources deployed into a VNet can communicate with each other privately, connect to the internet, and connect to on-premises networks — all in a controlled and secure way.

Key properties of a VNet:

- Defined by an IP address space using CIDR notation (for example, 10.0.0.0/16)
- Scoped to a single Azure region
- Isolated from all other VNets by default — no cross-VNet traffic without explicit configuration
- Can be divided into subnets for network segmentation

### Subnets

A subnet is a range of IP addresses within a VNet's address space. Subnets allow you to organize and segment your resources. For example, a three-tier application might have:

- A frontend subnet (10.0.1.0/24) for web servers
- A backend subnet (10.0.2.0/24) for application servers
- A database subnet (10.0.3.0/24) for database servers

Each subnet can have its own Network Security Group controlling which traffic enters and exits.

Azure reserves 5 IP addresses in each subnet: the first four and the last. For example, in a /24 subnet with 256 addresses, only 251 are usable.

[SHOW AZURE PORTAL] Navigate to Virtual Networks > Create. Walk through the IP Addresses tab. Show the default address space and how to add subnets. Create a VNet with address space 10.0.0.0/16 and two subnets: frontend (10.0.1.0/24) and backend (10.0.2.0/24).

### VNet Peering

By default, VNets are isolated from each other. VNet Peering connects two VNets so resources in each can communicate as if they were on the same network — using private IP addresses, with low latency and no gateway required.

Two types of peering:

**Regional VNet Peering** — Connects VNets in the same Azure region.

**Global VNet Peering** — Connects VNets across different Azure regions.

Peering is non-transitive: if VNet A is peered with VNet B and VNet B is peered with VNet C, VNet A and VNet C cannot communicate through VNet B without additional configuration.

---

## Section 2: Network Security Groups (5:00–8:00)

### What Is an NSG?

A Network Security Group, or NSG, is Azure's primary tool for controlling network traffic. An NSG contains a list of security rules that allow or deny inbound and outbound network traffic based on:

- Source and destination IP address (or CIDR range)
- Source and destination port
- Protocol (TCP, UDP, Any)
- Direction (inbound or outbound)

NSGs can be associated with:

- A **subnet** — applies to all resources in the subnet
- A **network interface card (NIC)** — applies only to the specific VM

Rules are processed in priority order — lower numbers are processed first. There are default rules you cannot remove that allow VNet-to-VNet traffic and Azure Load Balancer probes, and that deny all other internet traffic by default.

[SHOW AZURE PORTAL] Navigate to Network Security Groups > Create. Show the default inbound and outbound rules. Add a rule allowing inbound HTTP (port 80) from Any source. Show the priority field and explain ordering.

### NSG vs. Azure Firewall

NSGs operate at Layer 3/4 (IP and transport layer) — they filter based on IP addresses and ports. Azure Firewall, which we will discuss shortly, operates at Layer 7 (application layer) and can filter based on FQDNs (fully qualified domain names), URL patterns, and application protocols.

---

## Section 3: Azure Firewall (8:00–10:00)

### What Is Azure Firewall?

Azure Firewall is a managed, cloud-native network security service that protects your Azure Virtual Network resources. It is a stateful firewall-as-a-service with built-in high availability and unrestricted cloud scalability.

Key capabilities of Azure Firewall:

- **FQDN filtering** — Allow or deny traffic to specific domain names like *.microsoft.com
- **Application rules** — Allow or deny outbound HTTP/HTTPS based on FQDNs
- **Network rules** — Layer 3/4 filtering similar to NSGs
- **NAT rules** — Translate inbound internet traffic to private VNet addresses
- **Threat intelligence** — Block traffic from known malicious IPs and FQDNs
- **Centralized management** — One firewall for an entire hub VNet in a hub-and-spoke topology

Azure Firewall is deployed into a dedicated subnet in a VNet — typically named `AzureFirewallSubnet` — and requires at least a /26 subnet.

Use NSGs for simple subnet-level and NIC-level filtering. Use Azure Firewall for centralized, enterprise-grade, application-layer traffic control across your entire network.

---

## Section 4: Azure VPN Gateway and ExpressRoute (10:00–14:00)

### Connecting to On-Premises Networks

Most organizations have both on-premises infrastructure and cloud resources. Azure provides two primary methods for connecting your on-premises network to Azure: VPN Gateway and ExpressRoute.

### VPN Gateway

Azure VPN Gateway sends encrypted traffic between your Azure Virtual Network and your on-premises network over the public internet.

Two types of VPN connections:

**Site-to-Site VPN** — Connects an entire on-premises network to an Azure VNet. Requires a VPN device (physical or software) on the on-premises side. Traffic travels over the public internet, encrypted using IPsec/IKE.

**Point-to-Site VPN** — Connects individual client computers to an Azure VNet. Used for remote workers who need to access Azure resources securely from anywhere.

VPN Gateway SKUs range from Basic to VpnGw5, with higher SKUs providing more throughput, more tunnels, and better availability.

[SHOW AZURE PORTAL] Navigate to Virtual Network Gateways > Create. Show the gateway type selection (VPN vs. ExpressRoute). Show the SKU dropdown. Point out that VPN Gateway requires its own dedicated subnet named `GatewaySubnet`.

### ExpressRoute

ExpressRoute creates a private, dedicated connection between your on-premises network and Azure — without going over the public internet. This connection goes through a connectivity provider such as AT&T, Verizon, or Equinix.

Key advantages of ExpressRoute over VPN Gateway:

- Higher bandwidth (up to 100 Gbps)
- Lower, more consistent latency
- Private connection — traffic never traverses the public internet
- Higher availability SLA (99.95%)

ExpressRoute is significantly more expensive than VPN Gateway and requires working with a connectivity provider to establish the physical or virtual circuit. It is used by organizations with high bandwidth requirements, strict latency requirements, or regulatory mandates against internet-routed cloud connectivity.

**The AZ-900 distinction:** VPN Gateway = encrypted connection over internet. ExpressRoute = private dedicated connection bypassing the internet entirely.

---

## Section 5: Azure DNS (14:00–15:30)

### What Is Azure DNS?

Azure DNS is a hosting service for DNS domains that provides name resolution using Azure's global infrastructure. You can host your domain's DNS zones in Azure and manage DNS records using the Azure Portal, Azure CLI, or Azure PowerShell.

Azure DNS is not a domain registrar — you still register domain names through a registrar like GoDaddy or Namecheap. But you can delegate DNS management to Azure DNS for integrated management.

**Private DNS Zones** — Azure Private DNS allows name resolution within VNets without exposing DNS records to the public internet. You can link private DNS zones to VNets to resolve hostnames for private resources.

---

## Section 6: Application Gateway and Load Balancer (15:30–19:00)

### Azure Load Balancer

Azure Load Balancer operates at Layer 4 — it distributes inbound TCP and UDP traffic across backend VMs based on a hash of the source IP, source port, destination IP, and destination port.

Two types:

**Public Load Balancer** — Distributes internet-facing traffic to VMs in a backend pool.

**Internal Load Balancer** — Distributes traffic within a VNet or from on-premises to private endpoints.

Load Balancer provides 99.99% SLA and integrates with Availability Zones for zone-redundant deployments.

[SHOW AZURE PORTAL] Navigate to Load Balancers > Create. Show the Public vs. Internal type selection. Show the backend pool and health probe configuration.

### Azure Application Gateway

Application Gateway operates at Layer 7 — it understands HTTP/HTTPS traffic and makes routing decisions based on URL path, hostname, or HTTP headers.

Key Application Gateway features:

- **URL-based routing** — Route `/api` to one backend pool, `/images` to another
- **SSL/TLS termination** — Decrypt HTTPS at the gateway, reducing compute on backend VMs
- **Web Application Firewall (WAF)** — Protection against OWASP Top 10 threats (SQL injection, XSS, etc.)
- **Session affinity** — Route a user's requests to the same backend VM for sticky sessions
- **Autoscaling** — Automatically scale gateway capacity with traffic

Use Load Balancer for simple Layer 4 load balancing. Use Application Gateway when you need Layer 7 intelligent routing, SSL termination, or WAF protection.

[SHOW AZURE PORTAL] Navigate to Application Gateways > Create. Show the WAF tier option. Show the routing rules configuration — point out the path-based routing option.

---

## Section 7: Networking Decision Framework (19:00–21:00)

Let me close with a quick decision framework for the exam.

**Need to filter IP/port traffic for a subnet or VM?** Use Network Security Groups.

**Need centralized enterprise firewall with FQDN filtering and threat intelligence?** Use Azure Firewall.

**Need to connect your on-premises network to Azure over the internet with encryption?** Use VPN Gateway.

**Need a private, dedicated, high-bandwidth connection from on-premises to Azure?** Use ExpressRoute.

**Need to distribute TCP/UDP traffic (Layer 4) across VMs?** Use Azure Load Balancer.

**Need intelligent HTTP/HTTPS routing with WAF and SSL termination?** Use Azure Application Gateway.

**Need to host DNS records in Azure?** Use Azure DNS.

---

## Closing (21:00–22:00)

Azure Networking is a broad topic, but the AZ-900 exam focuses on the conceptual understanding of each service — what it does, when to use it, and how it differs from similar services. The VPN Gateway vs. ExpressRoute comparison and the Load Balancer vs. Application Gateway comparison are the most common exam question patterns.

In your lab this week, you will create a Virtual Network with subnets, deploy VMs into those subnets, and configure a Network Security Group. This is foundational to every real Azure architecture you will build.

In Module 09, we move to Azure Storage. Take care and I'll see you there.

---

*End of Script — Module 08*

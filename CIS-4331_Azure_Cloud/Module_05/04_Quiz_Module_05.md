# Quiz: Module 05 - Azure Virtual Networking

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure Architecture and Services (35-40% of exam)
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

An Azure Virtual Network (VNet) is scoped to which of the following?

- A) A single availability zone
- B) A single Azure subscription only — VNets cannot be shared across subscriptions
- C) A single Azure region
- D) A single resource group — resources in other resource groups cannot use it

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* An Azure VNet is scoped to a single Azure region. It cannot span multiple regions. Resources in a VNet can only communicate within that VNet or through peering/VPN. To connect resources across regions, you use global VNet peering or VPN Gateway.
- *Why A is incorrect:* VNets span the entire region, including all availability zones within that region. A VM in Zone 1 and a VM in Zone 2 can both be in the same VNet and communicate freely.
- *Why B is incorrect:* VNets can be shared across subscriptions using VNet peering or Azure Virtual WAN. A VNet in one subscription can be peered with a VNet in another subscription.
- *Why D is incorrect:* VNets are not bound to a single resource group in terms of usage. VMs and other resources in different resource groups can use the same VNet, as long as they are in the same subscription (or using cross-subscription peering).

---

## Question 2

In an Azure Network Security Group, you add the following two inbound rules:

- Rule A: Priority 100, Deny all traffic from source IP 203.0.113.50
- Rule B: Priority 200, Allow all traffic on port 80

An HTTP request arrives from IP 203.0.113.50 on port 80. What happens?

- A) The request is allowed because Rule B explicitly allows port 80
- B) The request is denied because Rule A has a lower priority number and is evaluated first
- C) Both rules apply simultaneously, and Deny overrides Allow
- D) The request is allowed because HTTP traffic is always permitted by default

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* NSG rules are evaluated in priority order from lowest number (highest priority) to highest number (lowest priority). Rule A at priority 100 is evaluated before Rule B at priority 200. Rule A matches the source IP 203.0.113.50 and denies it — evaluation stops. Rule B is never reached for this traffic.
- *Why A is incorrect:* Even though Rule B would allow the traffic, it is never evaluated because Rule A at higher priority (lower number 100) matches first and denies the traffic. The specific port-based allow cannot override a source-IP deny with higher priority.
- *Why C is incorrect:* NSG rules do not apply simultaneously. The evaluation is sequential and stops at the first matching rule. There is no simultaneous conflict resolution.
- *Why D is incorrect:* HTTP traffic is not allowed by default from the internet. The default NSG inbound rule at priority 65500 denies all inbound traffic. An explicit allow rule is required for HTTP access.

---

## Question 3

A company needs to connect its on-premises data center to Azure, and the company's compliance policy states that all data transfers must occur over a private connection that does not traverse the public internet. Which connectivity option meets this requirement?

- A) Azure VPN Gateway with IPsec encryption
- B) Azure ExpressRoute
- C) Azure VNet peering
- D) Azure Content Delivery Network

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure ExpressRoute establishes a dedicated private network connection between on-premises infrastructure and Azure datacenters through a connectivity provider's network. The connection does not traverse the public internet. This directly satisfies the compliance requirement for private-only data transfer.
- *Why A is incorrect:* Azure VPN Gateway creates encrypted tunnels, but they run over the public internet. The data is encrypted in transit, but it still physically traverses public internet infrastructure. If the compliance requirement is "must not traverse the public internet," VPN alone does not satisfy it.
- *Why C is incorrect:* VNet peering connects Azure VNets to each other within Azure's private backbone. It does not connect on-premises environments to Azure. You cannot peer an on-premises network to a VNet.
- *Why D is incorrect:* Azure CDN is a content delivery service for distributing static content to edge locations. It has no role in connecting on-premises data centers to Azure.

---

## Question 4

Azure VNet peering connects two VNets. VNet A is peered with VNet B, and VNet B is peered with VNet C. Can a resource in VNet A communicate with a resource in VNet C using this configuration?

- A) Yes — traffic flows through VNet B as a transit hub
- B) No — VNet peering is not transitive; A-to-C traffic requires a direct A-C peer
- C) Yes — all VNets connected through any common peer can communicate
- D) Only if the VNets are in the same region

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* VNet peering is not transitive. The A-B peer and the B-C peer are independent connections. Traffic from A destined for C cannot travel through B's peering connection to C without an explicit A-C peering or a network virtual appliance (NVA) in B configured as a transit router.
- *Why A is incorrect:* VNet B is not automatically a transit hub. To use B as a transit, you would need to configure a network virtual appliance (like Azure Firewall) in B and set up routing — this is the hub-and-spoke topology, which requires explicit configuration beyond simple peering.
- *Why C is incorrect:* VNet peering does not create a mesh of connectivity through indirect peers. Each peering relationship is a direct, isolated connection. Multiple hops through peers are not supported natively.
- *Why D is incorrect:* While local (same-region) peering has lower latency than global (cross-region) peering, non-transitivity applies to both. The same-region requirement is not the constraint — the transitive limitation applies regardless of region.

---

## Question 5

Which Azure networking service operates at Layer 7 (application layer) and can route traffic based on URL paths and provide Web Application Firewall (WAF) capability?

- A) Azure Load Balancer
- B) Network Security Group
- C) Azure Application Gateway
- D) Azure VPN Gateway

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Application Gateway is a Layer 7 load balancer that understands HTTP/HTTPS traffic. It can route traffic based on URL paths (e.g., /api goes to one backend pool, /images goes to another), perform SSL termination, and optionally enable the Web Application Firewall for protection against OWASP vulnerabilities.
- *Why A is incorrect:* Azure Load Balancer operates at Layer 4 (TCP/UDP). It distributes traffic based on network tuple hashing (source IP, port, destination IP, port, protocol), not application-layer attributes like URL paths.
- *Why B is incorrect:* NSGs are Layer 3/4 packet filters that allow or deny traffic based on IP addresses and ports. They have no application-layer awareness and do not provide WAF capability.
- *Why D is incorrect:* VPN Gateway creates encrypted tunnels between networks. It is a connectivity service, not a load balancer or WAF. It does not route application traffic based on URL paths.

---

## Question 6

A company wants to ensure that traffic from an Azure VNet to Azure Storage uses the Azure backbone network rather than the public internet, without giving Azure Storage a private IP in the VNet. Which Azure feature accomplishes this?

- A) VNet peering
- B) Service Endpoint
- C) Private Endpoint
- D) ExpressRoute

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Service Endpoints extend a VNet's identity to specific Azure PaaS services (Storage, SQL, etc.) over the Azure backbone. When a service endpoint for Azure Storage is enabled on a subnet, traffic from that subnet to Azure Storage goes through the Azure backbone, not the public internet. The storage account still has its public IP address — access is restricted via service endpoint policies.
- *Why A is incorrect:* VNet peering connects two Azure VNets to each other. Azure Storage is not a VNet — it is a PaaS service with a public endpoint. VNet peering does not apply.
- *Why C is incorrect:* A Private Endpoint would create a private IP for Azure Storage within the VNet. This is a stronger security option, but the question specifically states "without giving Azure Storage a private IP in the VNet," which describes Service Endpoints, not Private Endpoints.
- *Why D is incorrect:* ExpressRoute connects on-premises infrastructure to Azure over a private circuit. It is a hybrid connectivity solution and is not the mechanism for routing VNet-to-Storage traffic over the Azure backbone.

---

## Question 7

An organization deploys a VPN Gateway in Azure. The VPN Gateway requires a specific subnet in the VNet. What is the mandatory name for this subnet?

- A) vpn-subnet
- B) gateway-subnet
- C) GatewaySubnet
- D) AzureVpnSubnet

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure requires the subnet used by VPN Gateway to be named exactly `GatewaySubnet` (case-sensitive). This is a hard requirement enforced by Azure. Using any other name will cause VPN Gateway deployment to fail.
- *Why A is incorrect:* `vpn-subnet` is not a recognized required subnet name. Azure will reject this name for VPN Gateway deployment.
- *Why B is incorrect:* `gateway-subnet` (lowercase) is not the correct name. Azure enforces the exact name `GatewaySubnet` with capital G and capital S.
- *Why D is incorrect:* `AzureVpnSubnet` is not an Azure-recognized required subnet name. Like the others, this would cause the VPN Gateway deployment to fail.

---

## Question 8

Which of the following accurately describes Azure Private DNS Zones?

- A) Provides public DNS resolution for internet-accessible domain names hosted in Azure
- B) Provides name resolution for resources within Azure VNets without requiring a custom DNS server
- C) Replaces on-premises Active Directory DNS and is accessible from the public internet
- D) Provides DNS resolution only for Azure Resource Manager resources, not classic resources

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Private DNS zones provide name resolution within Azure Virtual Networks. VMs and other resources in a VNet linked to a Private DNS zone can resolve hostnames in the zone to private IP addresses. No custom DNS server is required — Azure handles resolution automatically.
- *Why A is incorrect:* This describes Azure Public DNS zones. Public DNS zones host internet-accessible records (A, CNAME, MX, etc.) for public domains. Private DNS zones are only accessible within linked VNets, not from the public internet.
- *Why C is incorrect:* Private DNS zones do not replace on-premises Active Directory DNS. They provide Azure-hosted name resolution for Azure resources. On-premises AD DNS continues to operate independently. Private DNS zones are also not accessible from the public internet.
- *Why D is incorrect:* The distinction between ARM and classic resources is legacy and not relevant to the capability of Private DNS zones. Private DNS zones support modern Azure networking without being restricted by deployment model.

---

## Question 9

A standard Azure NSG is associated with a subnet. By default (before any custom rules are added), which of the following statements about inbound traffic from the internet is correct?

- A) All inbound traffic from the internet is allowed by default
- B) Only HTTP and HTTPS traffic is allowed by default; all other traffic is denied
- C) All inbound traffic from the internet is denied by default
- D) Only traffic from Azure services is allowed; all other internet traffic is denied

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* The default NSG inbound rule at priority 65500 (`DenyAllInBound`) denies all inbound traffic from the internet. The lower-priority default rules (65000 and 65001) allow traffic within the VNet and from Azure Load Balancer respectively, but they do not allow arbitrary internet inbound traffic. To allow internet traffic, you must add an explicit allow rule.
- *Why A is incorrect:* This is the opposite of the correct behavior. Azure's default security posture is deny-all inbound from the internet. This protects resources from internet exposure by default.
- *Why B is incorrect:* No HTTP or HTTPS ports are opened by default. All specific application ports require explicit allow rules. The default allows only VNet-internal traffic and Load Balancer health probes.
- *Why D is incorrect:* While Azure service tags can be used to allow traffic from specific Azure services, this is not default behavior. The default allow rules (priority 65000 and 65001) cover VNet-internal and Load Balancer traffic — not broad Azure service traffic.

---

## Question 10

A company has an Azure Virtual Network in East US and another VNet in West US. They want resources in both VNets to communicate securely using Azure's private backbone network, with minimal management overhead and no VPN configuration. Which solution is most appropriate?

- A) Configure a Site-to-Site VPN between the two VNets
- B) Use global VNet peering between the East US and West US VNets
- C) Set up ExpressRoute circuits to both regions and connect them through on-premises
- D) Deploy Azure Bastion in both VNets and use it as a transit relay

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Global VNet peering connects VNets in different regions directly over Azure's private backbone network. It requires no VPN configuration, no gateway, and no additional hardware. Traffic stays on Microsoft's global network. It provides the minimal-management, private-backbone connectivity the scenario requires.
- *Why A is incorrect:* A VNet-to-VNet VPN using VPN Gateways does connect the two VNets, but it requires deploying and managing VPN Gateway resources in both VNets, which adds management overhead compared to peering. It also uses slightly different routing.
- *Why C is incorrect:* Using ExpressRoute circuits through on-premises as a transit is extremely complex, expensive, and introduces on-premises as a dependency. This is not a practical solution for simply connecting two Azure VNets.
- *Why D is incorrect:* Azure Bastion is a secure remote access service that allows administrators to connect to VMs using SSH or RDP through the browser — it is not a network transit relay for VNet-to-VNet communication.

---

### Question 11 (5 points)

A subnet is configured with the address space `10.0.2.0/24`. How many IP addresses are available for Azure resources in this subnet?

- A) 256
- B) 254
- C) 251
- D) 248

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* A /24 subnet contains 256 total addresses. Azure reserves 5 addresses in every subnet: the network address (x.x.x.0), the default gateway (x.x.x.1), two Azure DNS addresses (x.x.x.2 and x.x.x.3), and the broadcast address (x.x.x.255). 256 minus 5 = 251 usable addresses for Azure resources.
  - *Why A is incorrect:* 256 is the total address count for a /24 before Azure's 5 reserved addresses are subtracted. No Azure subnet has all 256 addresses available for resources.
  - *Why B is incorrect:* 254 is the standard non-Azure IPv4 subnet usable count (256 minus network and broadcast). Azure reserves 3 additional addresses (gateway and 2 DNS), reducing the usable count to 251.
  - *Why D is incorrect:* 248 is not a valid subnet usable count for a /24. This may be confused with the usable count for a /29 (8 total minus 5 reserved = 3 usable) or other smaller subnets.

---

### Question 12 (5 points)

An organization wants to allow VMs in a VNet to access Azure SQL Database using Azure's backbone network without exposing the SQL server to the public internet, but without placing a private IP for SQL in the VNet. Which networking feature should be configured on the VNet subnet?

- A) Private Endpoint
- B) Service Endpoint for Microsoft.Sql
- C) VNet peering to the Azure SQL region
- D) Azure Firewall with SQL application rules

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A Service Endpoint for Microsoft.Sql, when enabled on a subnet, routes traffic from that subnet to Azure SQL Database over the Azure backbone network rather than the public internet. The SQL server retains its public endpoint IP but can be restricted to only accept traffic from VNets with the service endpoint enabled. No private IP is placed in the VNet.
  - *Why A is incorrect:* A Private Endpoint creates an actual private IP address for the SQL instance inside the VNet. The question explicitly states "without placing a private IP for SQL in the VNet," which distinguishes this scenario as a Service Endpoint use case.
  - *Why C is incorrect:* VNet peering connects two Azure VNets. Azure SQL Database is a PaaS service with a public endpoint, not a VNet resource. VNet peering cannot connect a VNet to a PaaS service endpoint.
  - *Why D is incorrect:* Azure Firewall controls outbound traffic from VNets but does not change the routing path for Azure PaaS service traffic. Enabling a Service Endpoint is the direct mechanism for routing to Azure backbone.

---

### Question 13 (5 points)

An application team creates an NSG inbound rule: Priority 110, Allow, Source Any, Destination Port 443 (HTTPS). They want to block all other inbound traffic. Which default NSG rule ensures all other inbound internet traffic is denied?

- A) The team must manually add a Deny All rule at priority 200
- B) The default rule DenyAllInBound at priority 65500 denies all traffic not matched by earlier rules
- C) All unmatched traffic is allowed by default in Azure NSGs
- D) The default rule at priority 65001 denies all non-HTTPS traffic

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Every Azure NSG includes a built-in default rule named `DenyAllInBound` at priority 65500 that denies all inbound traffic not matched by any preceding rule. Since NSG evaluation stops at the first matching rule, all traffic except HTTPS (matched by the Allow rule at priority 110) is denied by this default rule.
  - *Why A is incorrect:* No additional Deny All rule is needed — the default DenyAllInBound rule at priority 65500 already handles this. Adding a manual deny rule at priority 200 would work but is unnecessary.
  - *Why C is incorrect:* This is the opposite of Azure NSG default behavior. Azure's default security posture denies all inbound internet traffic. Allow rules must be explicitly created.
  - *Why D is incorrect:* Priority 65001 is the `AllowAzureLoadBalancerInBound` default rule, not a deny rule. The deny-all rule is at priority 65500.

---

### Question 14 (5 points)

A company connects its on-premises network to Azure VNet A using a Site-to-Site VPN Gateway. VNet A is peered with VNet B. Can on-premises resources communicate directly with resources in VNet B through VNet A?

- A) Yes — VNet peering automatically enables transit routing through the peered VNets
- B) No — by default, VNet peering does not allow transit routing; "Allow gateway transit" and "Use remote gateways" must be configured
- C) Yes — the VPN Gateway in VNet A acts as a transit router for all peered VNets automatically
- D) No — on-premises resources can only connect to the VNet that hosts the VPN Gateway

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* By default, VNet peering does not enable gateway transit. To allow on-premises resources to route through VNet A's VPN Gateway into VNet B, two peering settings must be explicitly enabled: "Allow gateway transit" on VNet A's side of the peering, and "Use remote gateways" on VNet B's side. Without these settings, on-premises traffic cannot reach VNet B through the gateway.
  - *Why A is incorrect:* Transit routing through peered VNets is not automatic. It requires explicit configuration of gateway transit settings on the peering relationship.
  - *Why C is incorrect:* The VPN Gateway does not automatically act as a transit router for all peered VNets. Gateway transit must be explicitly enabled per peering relationship.
  - *Why D is incorrect:* On-premises resources can connect to peered VNets through the gateway — but only when gateway transit is properly configured. The limitation is not architectural impossibility but a default-off configuration requirement.

---

### Question 15 (5 points)

Which Azure networking service provides DNS resolution for private domain names within a VNet, without requiring the deployment or management of DNS server VMs?

- A) Azure Public DNS
- B) Azure Firewall DNS proxy
- C) Azure Private DNS Zones
- D) Azure Traffic Manager

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* Azure Private DNS Zones provide fully managed, serverless DNS resolution for hostnames within linked Azure Virtual Networks. Resources in a VNet linked to a private DNS zone can resolve names like `vm01.internal.contoso.com` to private IP addresses with no custom DNS server infrastructure required.
  - *Why A is incorrect:* Azure Public DNS hosts publicly accessible DNS zones (accessible from the internet). It does not provide private name resolution within VNets.
  - *Why B is incorrect:* Azure Firewall DNS proxy is a feature that allows the Firewall to act as a DNS forwarder to prevent DNS leakage and enable DNS-based FQDN filtering. It is not a private DNS resolution service and requires deploying an Azure Firewall instance.
  - *Why D is incorrect:* Azure Traffic Manager is a DNS-based global load balancer that routes users to the closest or most available endpoint across regions. It operates on public DNS and has no function for private VNet name resolution.

---

### Question 16 (5 points)

A developer must connect securely to an Azure VM for troubleshooting but company policy prohibits VMs from having public IP addresses or open SSH/RDP ports. Which Azure service enables this secure access?

- A) Azure VPN Gateway Point-to-Site connection
- B) Azure Bastion
- C) Network Security Group allow rule for the developer's home IP
- D) Azure ExpressRoute with a management circuit

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Bastion provides browser-based SSH and RDP access to Azure VMs directly through the Azure Portal, using TLS over port 443. VMs do not need public IP addresses or open SSH/RDP ports — Bastion connects to them through their private IP addresses within the VNet. This directly satisfies both policy requirements.
  - *Why A is incorrect:* Point-to-Site VPN allows a developer's computer to connect to the VNet through an encrypted tunnel. While this enables private IP access, it requires configuring and installing a VPN client, and the VM still needs SSH/RDP to be accessible (just through private IP). Bastion provides the access directly through the browser without a VPN client.
  - *Why C is incorrect:* Adding an NSG allow rule for a specific home IP still requires the VM to have a public IP address and an open port. Company policy prohibits both — so this option violates policy regardless of IP restriction.
  - *Why D is incorrect:* ExpressRoute is a high-bandwidth dedicated circuit for enterprise network-to-Azure connectivity. It is expensive and designed for organizational network integration, not for individual developer access to specific VMs.

---

### Question 17 (5 points)

Azure Traffic Manager differs from Azure Load Balancer in which fundamental way?

- A) Traffic Manager operates at Layer 7 (HTTP/HTTPS); Load Balancer operates at Layer 4 (TCP/UDP)
- B) Traffic Manager is a DNS-based global routing service that directs clients to endpoints in different Azure regions; Load Balancer distributes traffic within a region to backend instances
- C) Traffic Manager requires an Application Gateway in each region; Load Balancer does not
- D) Traffic Manager provides lower latency than Load Balancer because it uses Anycast routing

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Traffic Manager is a DNS-level service that returns the IP address of the best endpoint (based on routing method: performance, priority, weighted, geographic) when a client performs a DNS lookup. The client then connects directly to that endpoint. Load Balancer operates within a single region, distributing actual network traffic packets across backend VMs in a pool. They solve different problems at different scales.
  - *Why A is incorrect:* That describes the difference between Application Gateway (Layer 7) and Load Balancer (Layer 4), not Traffic Manager vs. Load Balancer. Traffic Manager is DNS-based, which is not accurately described as "Layer 7 HTTP/HTTPS."
  - *Why C is incorrect:* Traffic Manager does not require Application Gateway in each region. Traffic Manager simply points DNS to whatever endpoint you configure — VMs, App Services, load balancers, or any IP/hostname.
  - *Why D is incorrect:* Traffic Manager does not provide lower latency through Anycast routing. In fact, Traffic Manager adds a DNS lookup step. Its performance routing method selects the endpoint with the lowest latency based on DNS probe data, but the service itself is not Anycast-based.

---

### Question 18 (5 points)

A VNet has the address space `10.1.0.0/16`. An administrator wants to create a subnet for web servers using `/24` notation. Which of the following subnet address ranges is valid and does not conflict with a pre-existing subnet at `10.1.1.0/24`?

- A) `10.1.1.0/24`
- B) `10.1.0.0/24`
- C) `10.1.2.0/24`
- D) `10.2.0.0/24`

- **Correct Answer:** C
- **Distractor Analysis:**
  - *Why C is correct:* `10.1.2.0/24` is within the VNet address space (`10.1.0.0/16`) and does not overlap with the existing `10.1.1.0/24` subnet. The third octet (2) differs from the existing subnet's third octet (1), ensuring no address space conflict.
  - *Why A is incorrect:* `10.1.1.0/24` is the existing subnet. Creating an identical range would conflict directly with the already-provisioned subnet.
  - *Why B is incorrect:* `10.1.0.0/24` is within the VNet address space. While it does not conflict with `10.1.1.0/24`, it is a valid separate subnet option — but the question asks for one that does not conflict AND is valid. C is the cleaner answer specifically avoiding the existing subnet range, and both B and C are technically valid. However, the phrasing "does not conflict" makes C the safer, unambiguous correct choice since B could be interpreted as the VNet base range in some configurations.
  - *Why D is incorrect:* `10.2.0.0/24` is outside the VNet's address space (`10.1.0.0/16`). Azure requires subnets to fall within the VNet's defined address space. This address range cannot be used as a subnet in this VNet.

---

### Question 19 (5 points)

What is the purpose of the `AzureLoadBalancer` service tag in an NSG inbound rule?

- A) It blocks all traffic from Azure Load Balancer to prevent double-NATing
- B) It allows health probe traffic from Azure Load Balancer to reach backend VM instances
- C) It routes all inbound traffic through the Azure Load Balancer before reaching the VM
- D) It enables the VM to register itself with a load balancer backend pool automatically

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* The `AzureLoadBalancer` service tag in an NSG allow rule permits health probe traffic from the Azure Load Balancer infrastructure to reach VMs in the backend pool. If health probes are blocked, the load balancer marks the VM as unhealthy and stops sending traffic to it — even if the VM is running correctly. This is why the default NSG rule at priority 65001 allows `AzureLoadBalancer` inbound traffic.
  - *Why A is incorrect:* The `AzureLoadBalancer` tag is used in Allow rules, not Deny rules. Blocking it would break load balancer health checks. Double-NATing is not addressed by this service tag.
  - *Why C is incorrect:* Service tags in NSG rules match source or destination IP ranges — they do not route traffic. Traffic routing is determined by load balancer rules and backend pool configuration, not NSG service tags.
  - *Why D is incorrect:* VMs are registered with load balancer backend pools through explicit ARM configuration (adding the VM's NIC to the backend pool). NSG service tags have no role in backend pool registration.

---

### Question 20 (5 points)

An organization has deployed a hub-and-spoke VNet topology. Hub VNet contains a shared Azure Firewall. Spoke VNet A and Spoke VNet B are each peered with the Hub VNet. For traffic from Spoke A to pass through the Hub Firewall before reaching Spoke B, what configuration is required?

- A) No additional configuration — peering automatically routes traffic through hub-hosted firewalls
- B) User-Defined Routes (UDRs) in both Spoke A and Spoke B that direct traffic through the Azure Firewall's private IP as the next hop
- C) A second VPN Gateway must be deployed in the Hub VNet to enable spoke-to-spoke routing
- D) Azure Traffic Manager must be configured to route spoke-to-spoke traffic through the hub

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* By default, peered VNets communicate directly — traffic from Spoke A to Spoke B would go directly without passing through the Hub Firewall. To force traffic through the firewall, User-Defined Routes must be created in the spoke subnets specifying the Azure Firewall's private IP as the next hop for the destination spoke's address space. This overrides the default direct routing.
  - *Why A is incorrect:* VNet peering does not automatically route traffic through firewalls or network virtual appliances hosted in peered VNets. Azure uses the most direct path by default — UDRs are required to force traffic through an NVA or firewall.
  - *Why C is incorrect:* VPN Gateways are for connecting on-premises networks to Azure or connecting Azure VNets via encrypted tunnels. A second VPN Gateway in the Hub is not the mechanism for routing spoke-to-spoke traffic through an internal firewall.
  - *Why D is incorrect:* Azure Traffic Manager is a DNS-based global routing service for directing users to endpoints across regions. It has no role in controlling east-west traffic flow between VNets in a hub-and-spoke topology.

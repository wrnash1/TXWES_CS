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

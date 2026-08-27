# Quiz: Module 08 — Azure Networking

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

## AZ-900 Domain: Describe Azure Architecture and Services (35–40% of exam)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points. Total: 100 points.

---

### Question 1

A company wants to connect all of its Azure Virtual Networks in three different Azure regions so resources can communicate privately across regions. Which Azure networking feature enables this?

A. Azure VPN Gateway with Site-to-Site connections

B. Global VNet Peering

C. Azure ExpressRoute circuits

D. Network Security Groups with VNet service tags

**Correct Answer: B**

**Distractor Analysis:**

- **A (VPN Gateway):** VPN Gateway can connect VNets via VNet-to-VNet connections, but VNet Peering is the simpler, lower-latency, lower-cost method for cross-region VNet connectivity without gateway overhead. Not the best answer.
- **B (Global VNet Peering) — CORRECT:** Global VNet Peering connects VNets in different Azure regions, enabling private IP communication with low latency and without routing through the public internet or a gateway. It is the recommended method for cross-region VNet connectivity.
- **C (ExpressRoute):** ExpressRoute connects on-premises networks to Azure — not Azure VNets to each other. It requires a connectivity provider circuit. Not applicable here.
- **D (NSG with VNet service tags):** NSGs control traffic filtering, not VNet connectivity. Service tags are used in NSG rules to reference IP ranges — they do not enable cross-VNet communication. Incorrect.

---

### Question 2

An NSG has the following inbound rules: AllowHTTP (priority 100, Allow, port 80), DenyWeb (priority 90, Deny, port 80). A request arrives on port 80. What happens?

A. The request is allowed because AllowHTTP has a lower priority number

B. The request is denied because DenyWeb has a lower priority number and is processed first

C. Both rules apply and the request is allowed because Allow takes precedence over Deny

D. Azure generates an error because two rules target the same port

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Incorrect. Lower priority numbers are processed FIRST. Priority 90 is lower than 100, so DenyWeb is processed before AllowHTTP.
- **B — CORRECT:** NSG rules are processed in ascending priority order — lowest number first. Priority 90 (DenyWeb) is evaluated before priority 100 (AllowHTTP). The request matches the Deny rule at priority 90 and is blocked. Processing stops there.
- **C:** Incorrect. NSG rules stop processing at the first match. There is no "Allow overrides Deny" logic — the first matching rule wins.
- **D:** Incorrect. Azure allows multiple NSG rules targeting the same port. Priority ordering determines which rule is applied.

---

### Question 3

A financial services company requires a dedicated, private network connection from its on-premises data center to Azure with guaranteed bandwidth of 10 Gbps and no traffic exposure to the public internet. Which service meets these requirements?

A. Azure VPN Gateway (VpnGw5 SKU)

B. Azure ExpressRoute

C. Azure Virtual WAN

D. Azure Application Gateway

**Correct Answer: B**

**Distractor Analysis:**

- **A (VPN Gateway VpnGw5):** VpnGw5 supports up to 10 Gbps throughput, but VPN Gateway traffic travels over the public internet (encrypted via IPsec). The requirement explicitly states "no traffic exposure to the public internet." Incorrect.
- **B (ExpressRoute) — CORRECT:** ExpressRoute provides a private, dedicated circuit between on-premises and Azure that bypasses the public internet entirely. It supports up to 100 Gbps and provides consistent, low latency. This is the correct answer for "private dedicated" and "no public internet."
- **C (Azure Virtual WAN):** Virtual WAN is a networking service for connecting branches and VNets at scale. It does not itself provide a private dedicated circuit from on-premises to Azure. Incorrect.
- **D (Application Gateway):** Application Gateway is a Layer 7 load balancer and WAF — it handles inbound HTTP/HTTPS traffic from the internet to backend resources, not on-premises to Azure connectivity. Incorrect.

---

### Question 4

A web application team needs to route requests to `/api/` endpoints to one backend VM pool and all other requests to a different backend VM pool. Which Azure networking service supports this URL path-based routing?

A. Azure Load Balancer

B. Azure Traffic Manager

C. Azure Application Gateway

D. Azure VPN Gateway

**Correct Answer: C**

**Distractor Analysis:**

- **A (Azure Load Balancer):** Azure Load Balancer operates at Layer 4 and uses a 5-tuple hash for distribution. It has no awareness of URL paths or HTTP content. It cannot route based on `/api/` vs. other paths. Incorrect.
- **B (Azure Traffic Manager):** Traffic Manager is a DNS-based global load balancer for routing users to different Azure endpoints across regions. It does not inspect URL paths for routing within a single application. Incorrect.
- **C (Application Gateway) — CORRECT:** Application Gateway operates at Layer 7 and supports path-based routing rules. You can configure routing rules to send requests with `/api/` to one backend pool and all other requests to a different backend pool.
- **D (VPN Gateway):** VPN Gateway is for hybrid network connectivity between on-premises and Azure. It has no role in web traffic routing or HTTP load balancing. Incorrect.

---

### Question 5

How many IP addresses does Azure reserve in each subnet, and why?

A. 3 — network address, gateway, broadcast

B. 5 — network address, default gateway, two Azure DNS IPs, and broadcast

C. 4 — network address, gateway, DNS, and broadcast

D. 2 — network address and broadcast only

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Incorrect. Azure reserves 5 addresses, not 3. The count matches CIDR standard plus Azure-specific reservations.
- **B — CORRECT:** Azure reserves 5 IP addresses in every subnet: (1) the network address (x.x.x.0), (2) the default gateway (x.x.x.1), (3) Azure DNS mapping (x.x.x.2), (4) Azure DNS mapping (x.x.x.3), and (5) the broadcast address (x.x.x.255 for a /24). This means a /24 subnet has 251 usable addresses, not 256.
- **C:** Incorrect. The count is 5, not 4.
- **D:** Incorrect. Standard CIDR reserves network address and broadcast (2), but Azure adds 3 more for gateway and DNS, totaling 5.

---

### Question 6

A company wants to protect its web applications from OWASP Top 10 threats such as SQL injection and cross-site scripting. Which Azure networking service provides this protection?

A. Azure Firewall with FQDN filtering

B. Network Security Group with custom rules

C. Azure Application Gateway with Web Application Firewall tier

D. Azure Load Balancer Standard tier

**Correct Answer: C**

**Distractor Analysis:**

- **A (Azure Firewall):** Azure Firewall provides FQDN filtering and threat intelligence but is designed for controlling outbound traffic from VNets and network-level filtering, not for protecting web applications from OWASP application-layer attacks. Incorrect.
- **B (NSG with custom rules):** NSGs filter traffic based on IP addresses and ports. They have no awareness of HTTP payload content such as SQL injection patterns in query strings. Incorrect.
- **C (Application Gateway with WAF) — CORRECT:** The Web Application Firewall (WAF) tier of Azure Application Gateway provides managed rules based on OWASP Core Rule Sets (CRS). It inspects HTTP/HTTPS payloads and blocks SQL injection, XSS, and other OWASP Top 10 attacks.
- **D (Load Balancer Standard):** Azure Load Balancer Standard provides enhanced networking features but operates at Layer 4 and has no application-layer inspection capability. It does not include a WAF. Incorrect.

---

### Question 7

Which subnet name is required when deploying an Azure VPN Gateway, and which subnet name is required for Azure Firewall?

A. VpnGatewaySubnet and FirewallSubnet

B. GatewaySubnet and AzureFirewallSubnet

C. AzureGateway and AzureFirewall

D. VPNSubnet and FWSubnet

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Incorrect. The exact names are GatewaySubnet and AzureFirewallSubnet. Azure will reject gateway or firewall deployment if the subnet names are different.
- **B — CORRECT:** Azure VPN Gateway and ExpressRoute Gateway require a subnet named exactly `GatewaySubnet`. Azure Firewall requires a subnet named exactly `AzureFirewallSubnet` (minimum /26). These names are enforced by the Azure platform.
- **C:** Incorrect. These are not valid Azure reserved subnet names.
- **D:** Incorrect. These are not valid Azure reserved subnet names.

---

### Question 8

Remote employees need to securely access Azure Virtual Network resources from their home computers. Which VPN connection type is designed for this individual client-to-VNet scenario?

A. Site-to-Site VPN

B. VNet-to-VNet VPN

C. Point-to-Site VPN

D. ExpressRoute Direct

**Correct Answer: C**

**Distractor Analysis:**

- **A (Site-to-Site VPN):** S2S VPN connects an entire on-premises network to Azure via a VPN device. It is designed for network-to-network connectivity, not individual client devices. Incorrect.
- **B (VNet-to-VNet VPN):** VNet-to-VNet connects Azure VNets to each other — not client computers to Azure. Incorrect.
- **C (Point-to-Site VPN) — CORRECT:** P2S VPN connects individual client computers to an Azure VNet using a software VPN client. It is specifically designed for remote workers who need to access Azure resources securely from home or other locations.
- **D (ExpressRoute Direct):** ExpressRoute Direct is a high-bandwidth dedicated circuit option for ExpressRoute. It connects data centers and large enterprise networks to Azure — not individual client computers. Incorrect.

---

### Question 9

A team needs to prevent resources in a specific subnet from initiating any outbound connections to the internet, while still allowing inbound responses to connection requests that originated within the VNet. Which Azure service can most precisely enforce this at the subnet level?

A. Azure Firewall with application rules

B. A Network Security Group with an outbound Deny rule for the Internet service tag

C. VNet Peering with no route to the internet

D. Azure Private Endpoints for all services

**Correct Answer: B**

**Distractor Analysis:**

- **A (Azure Firewall):** While Azure Firewall can achieve this, it requires deploying a firewall instance and routing all traffic through it — significantly more infrastructure and cost for a simple subnet-level outbound block. An NSG is the direct, simpler, correct answer for subnet-level control.
- **B — CORRECT:** An NSG outbound rule with Deny action targeting the Internet service tag (or destination * with port Any) at a priority lower than 65001 (the AllowInternetOutBound default) will block outbound internet traffic from the subnet. NSG outbound rules are applied at the subnet level and are the direct mechanism for this requirement.
- **C (VNet Peering):** Peering connects VNets but does not control outbound internet access from subnets. Removing a route to the internet would require User-Defined Routes with a black hole, not peering. Incorrect.
- **D (Private Endpoints):** Private Endpoints give resources a private IP in the VNet for specific Azure services. They do not prevent internet outbound traffic from a subnet. Incorrect.

---

### Question 10

Azure DNS Private Zones are used for which primary purpose?

A. Registering public domain names for Azure web applications

B. Providing name resolution for resources within Azure Virtual Networks without exposing DNS to the public internet

C. Filtering DNS requests to block access to malicious websites

D. Routing users to the closest Azure region based on DNS latency

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Incorrect. Azure DNS does not register domain names. It hosts DNS zones. Public registration is done through a domain registrar. Private DNS zones are specifically for internal VNet name resolution, not public domain registration.
- **B — CORRECT:** Azure Private DNS Zones provide name resolution for resources within VNets. Private zones can be linked to VNets for automatic VM hostname registration and internal service discovery without any public internet exposure.
- **C (DNS filtering for malicious sites):** DNS-based threat protection is available through Azure Firewall's DNS proxy with threat intelligence, not Azure DNS Private Zones. Incorrect.
- **D (Route users to closest region):** Routing users based on latency is the function of Azure Traffic Manager (DNS-based global routing). Azure DNS Private Zones are for internal VNet resolution only. Incorrect.

---

*Quiz 08 — Module 08: Azure Networking | CIS-4331 | Texas Wesleyan University*

---

### Question 11 (5 points)

A company has a VNet in East US (VNet-A) and a VNet in West Europe (VNet-B). They establish Global VNet Peering between them. A VM in VNet-A sends data to a VM in VNet-B. Which statement correctly describes how the traffic is routed?

- A) Traffic traverses the public internet encrypted with TLS between the two regions
- B) Traffic travels over Microsoft's private global backbone network without exposure to the public internet
- C) Traffic is routed through an Azure VPN Gateway in each region before crossing regions
- D) Traffic must pass through an ExpressRoute circuit to cross regional boundaries

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Global VNet Peering routes traffic over Microsoft's private global backbone network — the same physical infrastructure that interconnects Azure regions. The traffic never traverses the public internet, providing lower latency and higher reliability than internet routing. This is a key security and performance benefit of VNet Peering.
  - *Why A is incorrect:* VNet Peering traffic does not traverse the public internet at all. It stays within Microsoft's private network infrastructure. TLS encryption is not applied at the network level for peered VNet traffic (applications may use TLS, but the peering itself does not add it).
  - *Why C is incorrect:* VNet Peering bypasses VPN Gateways — it does not route through them. VPN Gateways add latency and cost. One advantage of VNet Peering over VNet-to-VNet VPN is the absence of gateway overhead.
  - *Why D is incorrect:* ExpressRoute is for connecting on-premises networks to Azure. It is not involved in cross-region Azure-to-Azure VNet communication. Global VNet Peering handles cross-region Azure VNet connectivity directly.

---

### Question 12 (5 points)

An organization deploys Azure Firewall in a hub VNet to inspect all traffic between spoke VNets and the internet. The spoke VNets are peered to the hub. After deployment, spoke VMs can still reach the internet directly without going through the firewall. What additional configuration is required?

- A) Create an Application Security Group in each spoke subnet
- B) Create User-Defined Routes (UDRs) in the spoke subnets with the next hop set to the Azure Firewall's private IP
- C) Enable Azure Firewall Premium SKU to support spoke-to-internet routing
- D) Add an NSG outbound deny rule on each spoke subnet to block direct internet access

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Firewall in a hub VNet does not automatically intercept traffic from peered spoke VNets. By default, VMs in spoke subnets use their own subnet's default route to reach the internet. User-Defined Routes (UDRs) must be applied to each spoke subnet, overriding the default internet route with a route pointing to the Azure Firewall's private IP as the next hop. Only then does traffic flow through the firewall for inspection.
  - *Why A is incorrect:* Application Security Groups (ASGs) are used to group VMs for simplified NSG rule authoring. They do not control routing decisions or force traffic through a firewall.
  - *Why C is incorrect:* The Azure Firewall SKU (Standard vs. Premium) affects inspection capabilities (TLS inspection, IDPS in Premium), not whether routing works between spokes and the internet. Both SKUs require UDRs to intercept spoke traffic.
  - *Why D is incorrect:* Adding an NSG deny rule on spoke subnets would block internet access entirely, but it would not redirect traffic through the firewall. The goal is forced inspection via the firewall, not simple blocking.

---

### Question 13 (5 points)

A development team creates an Azure Virtual Network with address space `10.0.0.0/16`. They want to create a subnet for web servers and a subnet for databases. The web subnet needs to support at least 100 VM IP addresses. Which subnet size is the smallest that provides 100 usable addresses (accounting for Azure's 5 reserved IPs per subnet)?

- A) /26 (64 addresses total, 59 usable)
- B) /25 (128 addresses total, 123 usable)
- C) /24 (256 addresses total, 251 usable)
- D) /27 (32 addresses total, 27 usable)

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* A /25 subnet provides 128 total IP addresses. Subtracting Azure's 5 reserved addresses (network, gateway, two DNS, broadcast) leaves 123 usable addresses. This is the smallest CIDR block that provides at least 100 usable IPs. A /26 only provides 59 usable addresses, which is insufficient.
  - *Why A is incorrect:* A /26 provides 64 total addresses minus 5 reserved = 59 usable. This is below the 100 minimum requirement.
  - *Why C is incorrect:* A /24 provides 251 usable addresses, which satisfies the requirement but is not the smallest size that does. The question asks for the smallest sufficient size, making /25 the correct answer.
  - *Why D is incorrect:* A /27 provides 32 total addresses minus 5 reserved = 27 usable. This is far below the 100 minimum requirement.

---

### Question 14 (5 points)

A company connects its on-premises network to Azure via a Site-to-Site VPN Gateway. They later add a new Azure VNet (VNet-C) peered to their original VNet (VNet-A, which has the VPN Gateway). On-premises users cannot reach VNet-C. What setting on the VNet Peering must be enabled to allow on-premises traffic to flow through VNet-A's gateway to reach VNet-C?

- A) Enable "Allow forwarded traffic" on VNet-C's peering with VNet-A
- B) Enable "Allow gateway transit" on VNet-A's side of the peering, and "Use remote gateways" on VNet-C's side
- C) Enable "Allow virtual network access" on both sides of the peering
- D) Deploy a second VPN Gateway in VNet-C and connect it to the same on-premises device

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* For on-premises traffic to reach VNet-C through VNet-A's existing VPN Gateway, two peering settings must be configured: "Allow gateway transit" must be enabled on VNet-A's side (the VNet that contains the gateway), and "Use remote gateways" must be enabled on VNet-C's side (the VNet that wants to use the remote gateway). Together these settings allow VNet-C to use VNet-A's gateway for on-premises connectivity.
  - *Why A is incorrect:* "Allow forwarded traffic" permits traffic that did not originate in the peered VNet to pass through. It addresses a different scenario (traffic forwarded from a third VNet or NVA) and is not sufficient by itself for gateway transit.
  - *Why C is incorrect:* "Allow virtual network access" is enabled by default on all peerings and enables basic VNet-to-VNet communication. It does not enable gateway transit for on-premises routing.
  - *Why D is incorrect:* Deploying a second gateway in VNet-C is unnecessary and expensive. The gateway transit feature exists precisely to avoid requiring a gateway in every VNet by allowing VNets to share a gateway through peering.

---

### Question 15 (5 points)

Azure Traffic Manager and Azure Load Balancer both distribute incoming traffic across multiple endpoints. What is the fundamental architectural difference between them?

- A) Traffic Manager operates at Layer 7 (HTTP); Load Balancer operates at Layer 4 (TCP/UDP)
- B) Traffic Manager is DNS-based and routes users globally to different Azure regions or endpoints; Load Balancer is network-based and distributes traffic to backend instances within a region
- C) Traffic Manager supports health probes; Load Balancer does not
- D) Load Balancer can route to on-premises endpoints; Traffic Manager is limited to Azure endpoints

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Traffic Manager works at the DNS layer — it returns the IP address of the best endpoint based on the configured routing method (performance, weighted, priority, geographic). Clients connect directly to the endpoint. It is designed for global routing across regions. Azure Load Balancer distributes TCP/UDP connections within a region to backend instances and is not DNS-based.
  - *Why A is incorrect:* Layer 7 HTTP routing is the domain of Azure Application Gateway (not Traffic Manager). Traffic Manager is DNS-based, which is above the traditional OSI layers. Load Balancer operates at Layer 4.
  - *Why C is incorrect:* Both Traffic Manager and Load Balancer support health probes/endpoints. Traffic Manager monitors endpoint health using HTTP/HTTPS/TCP probes. Load Balancer uses health probes to determine backend instance availability.
  - *Why D is incorrect:* Both Traffic Manager and Load Balancer support various endpoint types. Traffic Manager explicitly supports external endpoints (including on-premises IPs) as well as Azure endpoints. Load Balancer is regional and backends must be in the same region's VNet.

---

### Question 16 (5 points)

An organization wants Azure PaaS services (Azure SQL Database, Azure Storage) to be accessible from their VNet resources over a private IP address in the VNet — not through a public endpoint on the Microsoft backbone. Which Azure networking feature achieves this?

- A) Service Endpoints — route VNet traffic to PaaS services over the Microsoft backbone using service tags
- B) Private Endpoints — provision a private IP address in the VNet for the PaaS service, accessible only within the VNet
- C) VNet Peering — connect the VNet to the PaaS service's VNet for private access
- D) Azure Firewall with FQDN rules allowing only the PaaS service FQDNs

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Private Endpoints create a network interface with a private IP address in the VNet that maps to a specific PaaS service resource. Traffic to the PaaS service travels entirely within the VNet and Microsoft's network — the public endpoint of the service can be disabled. The service appears as a private IP address on the VNet, satisfying the requirement for private IP access.
  - *Why A is incorrect:* Service Endpoints improve routing for VNet traffic to PaaS services by keeping the traffic on the Microsoft backbone, but the PaaS service still uses its public IP address as the destination. Service Endpoints do not assign a private IP to the service within the VNet.
  - *Why C is incorrect:* PaaS services like Azure SQL Database and Azure Storage are not deployed into customer-managed VNets — they are multi-tenant managed services. You cannot peer to their internal VNet. Private Endpoints solve this by projecting a private interface into the customer VNet.
  - *Why D is incorrect:* Azure Firewall with FQDN rules controls which fully qualified domain names are allowed for outbound traffic. This does not assign private IPs to PaaS services or prevent traffic from using public endpoints.

---

### Question 17 (5 points)

A company deploys Azure Bastion to access VMs in their VNet. What two resources does Azure Bastion eliminate the need for, compared to traditional SSH/RDP access?

- A) A VPN Gateway and a public IP on the VNet
- B) A public IP address on the VM and an inbound NSG rule for SSH (port 22) or RDP (port 3389)
- C) A Network Security Group and a VNet Peering connection
- D) An ExpressRoute circuit and an application gateway

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Bastion provides browser-based SSH and RDP access to VMs through the Azure Portal over TLS port 443. Because Bastion handles the connectivity, VMs do not need public IP addresses, and inbound NSG rules for port 22 (SSH) or 3389 (RDP) are not required. This significantly reduces the attack surface.
  - *Why A is incorrect:* Azure Bastion does not replace a VPN Gateway. Bastion is specifically for administrative access (SSH/RDP) to individual VMs via the Azure Portal. VPN Gateway is for network-to-network connectivity. These are separate use cases.
  - *Why C is incorrect:* Azure Bastion does not replace NSGs or VNet Peering. NSGs can still be used alongside Bastion (and are recommended). Bastion replaces the need for specific inbound SSH/RDP rules, not the NSG itself.
  - *Why D is incorrect:* Azure Bastion has no relationship to ExpressRoute or Application Gateway. These serve entirely different purposes (hybrid connectivity and web traffic load balancing, respectively).

---

### Question 18 (5 points)

An organization uses Azure Application Gateway with WAF to protect their web application. The security team notices that the WAF is blocking some legitimate requests from a trusted partner IP range. What is the correct way to allow these requests while keeping WAF protection active for all other traffic?

- A) Disable WAF mode and switch to Detection mode permanently
- B) Add the partner IP range to the WAF exclusion list or create a custom allow rule with higher priority than the blocking rule
- C) Create a new Application Gateway without WAF for traffic from the partner IP range
- D) Add an NSG allow rule for the partner IP range to bypass the Application Gateway

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure WAF supports exclusion lists and custom rules. An exclusion list can be configured to skip specific WAF rule checks for requests from a trusted IP range. Alternatively, a custom WAF rule with a higher priority (lower number) can allow traffic from the partner IP range before the managed blocking rules are evaluated. Both approaches maintain WAF protection for all other traffic.
  - *Why A is incorrect:* Switching to Detection mode globally disables WAF blocking for ALL traffic, not just the partner IP range. Detection mode only logs threats without blocking them — this removes protection from the entire application, not just the partner exemption.
  - *Why C is incorrect:* Deploying a second Application Gateway without WAF creates operational complexity and bypasses security controls entirely for the partner traffic. It also means managing two separate gateway configurations.
  - *Why D is incorrect:* NSG rules cannot bypass Application Gateway inspection. The Application Gateway receives the traffic first regardless of NSG source rules. NSG allow rules for the partner IP would allow traffic to reach the gateway but would not bypass WAF inspection within the gateway.

---

### Question 19 (5 points)

A company needs to expose an internal web application running on VMs in a private VNet to the internet with SSL termination, automatic certificate management, and auto-scaling. The application does not require global traffic routing. Which Azure service combination is most appropriate?

- A) Azure Load Balancer (Standard) with a public IP address
- B) Azure Application Gateway with SSL termination and autoscaling
- C) Azure Traffic Manager with a weighted routing profile
- D) Azure Front Door with WAF policies

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* Azure Application Gateway is a Layer 7 load balancer that supports SSL/TLS termination (offloading encryption from backend VMs), automatic certificate management (via integration with Key Vault), and autoscaling (v2 SKU). It is a regional service designed exactly for exposing internal web applications to the internet with advanced HTTP features.
  - *Why A is incorrect:* Azure Load Balancer Standard operates at Layer 4 (TCP/UDP) and does not support SSL termination. SSL certificates cannot be configured on a Load Balancer — it passes through encrypted traffic to backend VMs, which must handle SSL themselves. It has no application-layer routing or certificate management.
  - *Why C is incorrect:* Azure Traffic Manager is DNS-based global routing. It does not handle SSL termination, certificate management, or autoscaling of backends. It routes DNS queries to endpoints in different regions but does not proxy traffic.
  - *Why D is incorrect:* Azure Front Door is a global CDN and load balancer designed for multi-region applications. While it does support SSL termination, it is optimized for globally distributed applications. For a single-region internal application, Application Gateway is the more appropriate and cost-effective choice.

---

### Question 20 (5 points)

A network administrator creates the following NSG outbound rules on a subnet hosting VMs:
- Rule 1: Priority 100, Allow, Destination: `Storage` service tag, Port: 443
- Rule 2: Priority 200, Deny, Destination: `*`, Port: `*`
- Default rule: AllowInternetOutBound (Priority 65001)

A VM attempts to connect to `https://myaccount.blob.core.windows.net` on port 443. What is the result?

- A) Denied — Rule 2 (Deny All) is processed before Rule 1 because Deny rules take precedence over Allow rules
- B) Allowed — Rule 1 matches first (priority 100) because the Storage service tag includes Azure Blob Storage endpoints
- C) Allowed — The default AllowInternetOutBound rule allows all outbound internet traffic regardless of custom rules
- D) Denied — Service tags cannot be used in outbound rules, only in inbound rules

- **Correct Answer:** B
- **Distractor Analysis:**
  - *Why B is correct:* NSG rules are processed in ascending priority order — lowest number first. Rule 1 (priority 100, Allow Storage tag) is evaluated before Rule 2 (priority 200, Deny All). The `Storage` service tag includes the IP ranges for all Azure Storage endpoints, including Blob Storage. The connection to `myaccount.blob.core.windows.net:443` matches Rule 1 and is allowed. Processing stops at the first match.
  - *Why A is incorrect:* Azure NSGs do not have a "Deny overrides Allow" logic. Rules are processed strictly in priority order (lowest number first). There is no priority override for deny rules.
  - *Why C is incorrect:* The default AllowInternetOutBound rule has priority 65001. Custom rules with lower priority numbers (100, 200) are processed first. If Rule 2 (priority 200, Deny All) matched before the default rule, the traffic would be denied. However, Rule 1 matches first, allowing the Storage traffic before Rule 2 is evaluated.
  - *Why D is incorrect:* Azure service tags can be used in both inbound and outbound NSG rules for both source and destination fields. The Storage service tag is commonly used in outbound rules to allow traffic to Azure Storage endpoints.

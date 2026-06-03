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

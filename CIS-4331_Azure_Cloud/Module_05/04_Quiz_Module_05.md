# Quiz: Module 05 - Azure Virtual Networking

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure service allows secure, dedicated, private fiber-optic connection from an on-premises datacenter directly to Azure?

* A) Azure VPN Gateway
* B) Azure ExpressRoute
* C) Azure Bastion
* D) VNet Peering
* **Correct Answer:** B) ExpressRoute bypasses the public internet completely to provide high-speed, private connections to Azure.
* **Distractor Analysis:**
  * *Why correct:* ExpressRoute bypasses the public internet completely to provide high-speed, private connections to Azure.
  * *Why A is incorrect:* VPN Gateway travels over the public internet using encryption — not a private dedicated link.

---

**Question 2**
Which of the following most accurately describes **subnets** within an Azure Virtual Network?

* A) Subdivisions of a VNet's address space that segment resources into smaller IP ranges, allowing different Network Security Group rules to apply to each segment.
* B) Isolated virtual networks that are completely separate from each other, requiring VNet Peering to communicate.
* C) Encrypted tunnels that connect an Azure VNet to an on-premises network over the public internet.
* D) Load balancing rules that distribute incoming traffic across multiple backend virtual machines.
* **Correct Answer:** A) Subnets are subdivisions of a VNet's address space that segment resources into smaller IP ranges, allowing different NSG rules to apply to each segment.
* **Distractor Analysis:**
  * *Why A is correct:* Subnets divide a VNet's address space and are the unit to which NSGs are applied for traffic control.
  * *Why B is incorrect:* That describes separate VNets, not subnets. Subnets exist within a single VNet.
  * *Why C is incorrect:* That describes a VPN Gateway connection, not a subnet.
  * *Why D is incorrect:* That describes Azure Load Balancer rules, not subnets.

---

**Question 3**
An Azure VM in a private subnet cannot be reached over the internet. A network engineer suspects the Network Security Group is blocking traffic. Which is the correct first troubleshooting step?

* A) Delete and recreate the VM in a public subnet
* B) Review the NSG's inbound security rules and verify that the required port is allowed with a priority lower than any conflicting deny rule
* C) Upgrade the VM to a larger SKU to increase its network throughput
* D) Enable Azure DDoS Protection Standard on the VNet
* **Correct Answer:** B) Review the NSG's inbound security rules and verify that the required port is allowed with a priority lower than any conflicting deny rule.
* **Distractor Analysis:**
  * *Why B is correct:* NSG rules are evaluated in priority order — a deny rule with a lower number than an allow rule will block traffic. Reviewing rule priorities is the correct first step.
  * *Why A is incorrect:* Moving the VM is disruptive and unnecessary; the NSG config should be checked first.
  * *Why C is incorrect:* VM SKU size affects compute performance, not NSG-controlled network access.
  * *Why D is incorrect:* DDoS Protection defends against volumetric attacks — it does not resolve NSG misconfiguration blocking legitimate traffic.

---

**Question 4**
A company needs to connect its on-premises datacenter to Azure with guaranteed bandwidth, sub-10ms latency, and no traffic traversing the public internet. Which Azure connectivity option meets all three requirements?

* A) Azure VPN Gateway with active-active configuration
* B) Azure ExpressRoute with a connectivity provider
* C) VNet Peering between on-premises and Azure VNets
* D) Azure Bastion with jump-server configuration
* **Correct Answer:** B) Azure ExpressRoute provides a dedicated private connection with guaranteed bandwidth, low latency, and no public internet traversal.
* **Distractor Analysis:**
  * *Why B is correct:* ExpressRoute is the only Azure option providing a private, dedicated connection with guaranteed SLAs that does not traverse the public internet.
  * *Why A is incorrect:* VPN Gateway always traverses the public internet, even in active-active mode, which violates the no-public-internet requirement.
  * *Why C is incorrect:* VNet Peering connects Azure VNets to each other — it cannot connect on-premises networks to Azure.
  * *Why D is incorrect:* Azure Bastion provides secure browser-based RDP/SSH access to VMs — it is not a site-to-site connectivity solution.

---

**Question 5**
You want administrators to access Azure VMs via RDP and SSH through the Azure portal without exposing those VMs to public IP addresses or opening RDP/SSH ports in NSGs. Which Azure service provides this capability?

* A) Azure VPN Gateway point-to-site connection
* B) Azure Bastion
* C) Azure Application Gateway with SSL offloading
* D) Azure Front Door
* **Correct Answer:** B) Azure Bastion provides browser-based RDP/SSH access to VMs directly from the Azure portal without requiring a public IP on the VM or open RDP/SSH NSG rules.
* **Distractor Analysis:**
  * *Why B is correct:* Bastion is a managed PaaS service that proxies RDP/SSH through the portal — VMs need no public IP and no open RDP/SSH ports.
  * *Why A is incorrect:* VPN point-to-site still requires open RDP/SSH ports and a VPN client on each administrator's machine.
  * *Why C is incorrect:* Application Gateway handles HTTP/HTTPS web traffic routing — it is not an administrative RDP/SSH access solution.
  * *Why D is incorrect:* Azure Front Door is a global HTTP load balancer and CDN — it does not provide VM administrative access.

# Quiz: Module 16 - Final Exam Preparation
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A network engineer is designing the IP addressing scheme for a new office. The office requires exactly 6 separate subnets, with the largest subnet needing to support 28 hosts. The engineer has been allocated the 192.168.10.0/24 address block. Which subnet mask provides the correct number of host addresses per subnet while using address space efficiently, and how many usable host addresses does it provide?

A) /25 (255.255.255.128) — provides 126 usable hosts per subnet; efficiently supports 28 hosts but wastes address space compared to smaller options
B) /27 (255.255.255.224) — provides 30 usable hosts per subnet; the smallest subnet mask that supports 28 hosts while leaving enough subnets for all 6 networks within the /24 block
C) /28 (255.255.255.240) — provides 14 usable hosts per subnet; sufficient for the 28-host requirement with 2 usable addresses to spare per subnet
D) /26 (255.255.255.192) — provides 62 usable hosts per subnet; required because the 28-host subnet must account for the network address, broadcast address, and 2 reserved gateway addresses, reducing usable hosts below 30

*   **Correct Answer:** B) /27 (255.255.255.224) — provides 30 usable hosts per subnet; the smallest subnet mask that supports 28 hosts while leaving enough subnets for all 6 networks within the /24 block
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A /25 mask provides 126 usable hosts per subnet (128 total addresses minus 2 for network and broadcast). While it supports 28 hosts, it only creates 2 subnets from a /24 block — not enough for the 6 required subnets. A /25 is also far oversized for a 28-host requirement and wastes address space unnecessarily.
    *   *Why C is incorrect:* A /28 mask provides only 14 usable hosts per subnet (16 total addresses minus 2). This does not support 28 hosts — it falls 14 addresses short of the requirement. A /28 would require at least two subnets to accommodate 28 hosts, which defeats the purpose of a single subnet.
    *   *Why D is incorrect:* A /26 mask provides 62 usable hosts per subnet, which is more than sufficient but not the most efficient choice. The claim that 4 addresses must be reserved (network + broadcast + 2 gateway addresses) is incorrect — only the network address and broadcast address are reserved in every subnet; gateway addresses are simply regular host addresses assigned to a router interface and count within the 30 usable addresses provided by /27.

---

**Question 2**
A user reports that their workstation can access file shares on the local network (192.168.1.x) by both IP address and hostname, but cannot reach any external websites or remote servers either by IP address or by hostname. The workstation is configured with a static IP address. Which is the most likely cause, and which command confirms it?

A) DNS failure — the local DNS server is not resolving external hostnames; confirmed by running `nslookup www.google.com`, which would return a timeout or server failure error while local hostname resolution continues to work
B) Default gateway misconfiguration — the workstation has no route to send traffic beyond the local subnet; confirmed by running `ipconfig /all` to verify the gateway address, then `ping` to the gateway IP to test reachability
C) Duplicate IP address conflict — another device on the network is using the same static IP, causing intermittent connectivity; confirmed by running `arp -a` to check whether the workstation's IP maps to two different MAC addresses in the ARP cache
D) MTU mismatch — the workstation's NIC is configured with a 9000-byte jumbo frame MTU that the upstream router does not support, causing large packets to be silently dropped while small packets (local file share traffic) pass successfully

*   **Correct Answer:** B) Default gateway misconfiguration — the workstation has no route to send traffic beyond the local subnet; confirmed by running `ipconfig /all` to verify the gateway address, then `ping` to the gateway IP to test reachability
*   **Distractor Analysis:**
    *   *Why A is incorrect:* DNS failure would cause hostname resolution to fail, but the user would still be able to reach external servers by IP address — the question states that IP address access to external servers also fails. Since even direct IP access to external destinations fails, DNS is not the root cause. DNS failure only explains hostname failures, not IP-based failures.
    *   *Why C is incorrect:* A duplicate IP address would cause intermittent connectivity failures on the local network — ARP conflicts typically disrupt local communication, not just external routing. The scenario describes consistent local access (both IP and hostname work locally) with consistent external failure, which is the classic symptom of a missing or incorrect default gateway, not an IP conflict.
    *   *Why D is incorrect:* An MTU mismatch causing jumbo frame issues would typically manifest as large transfers failing while small packets (like ping) succeed — it would not cause a complete failure to reach all external destinations by IP. Additionally, jumbo frames (9000 bytes) must be explicitly configured; the default Ethernet MTU is 1500 bytes, and a standard workstation would not be set to 9000 bytes by default.

---

**Question 3**
An organization's security policy requires that all remote access VPN connections use certificate-based mutual authentication, that VPN traffic is able to pass through public Wi-Fi hotspots and hotel networks that block non-standard ports, and that split tunneling is disabled so that all internet traffic from remote workers routes through the corporate security stack. Which VPN technology and configuration meets all three requirements?

A) IPsec IKEv2 VPN using pre-shared key (PSK) authentication on UDP port 500 with split tunneling disabled — PSK provides strong authentication, and UDP 500 is used by all corporate hotspots and hotels because it is the standard IKE negotiation port
B) SSL/TLS VPN client using certificate-based mutual authentication on TCP port 443 with full-tunnel mode configured — port 443 passes through virtually all firewalls and captive portals, certificates provide mutual authentication, and full-tunnel routes all traffic through the corporate gateway
C) GRE tunnel over IPsec using certificate authentication with full-tunnel routing — GRE encapsulation allows multicast and broadcast traffic that plain IPsec cannot carry, and port 443 can be configured as the GRE destination port to pass through restrictive networks
D) L2TP/IPsec VPN using certificate authentication on UDP port 1701 with split tunneling disabled — L2TP/IPsec is the most widely supported VPN protocol and port 1701 is universally permitted through hotel and hotspot firewalls because it is the standard L2TP port

*   **Correct Answer:** B) SSL/TLS VPN client using certificate-based mutual authentication on TCP port 443 with full-tunnel mode configured — port 443 passes through virtually all firewalls and captive portals, certificates provide mutual authentication, and full-tunnel routes all traffic through the corporate gateway
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IPsec IKEv2 uses UDP port 500 for IKE negotiation and UDP port 4500 for NAT-traversal. These ports are frequently blocked by hotel and public Wi-Fi firewalls, which is precisely why SSL/TLS VPN on port 443 was developed as the firewall-traversal solution. PSK authentication also does not meet the certificate-based mutual authentication requirement.
    *   *Why C is incorrect:* GRE is an encapsulation protocol that adds a GRE header to packets — it does not natively use port 443. While GRE over IPsec is a valid site-to-site VPN design, it does not change the underlying IPsec port requirements that cause hotel/hotspot firewall traversal problems. This answer contains a technically inaccurate claim about GRE port configuration.
    *   *Why D is incorrect:* L2TP/IPsec uses UDP port 1701 (L2TP) plus UDP 500/4500 (IPsec). UDP port 1701 is commonly blocked by restrictive firewalls — it is not "universally permitted." L2TP/IPsec has the same firewall-traversal problems as standard IPsec. Hotel and public Wi-Fi networks almost universally permit TCP 443 (HTTPS) while often blocking UDP 500, 1701, and 4500.

---

**Question 4**
A network operations center analyst receives an automated alert that a core router has been unreachable via SNMP for 15 minutes. The analyst opens a terminal and attempts to ping the router's management IP address — ping succeeds with normal latency. The analyst then attempts to SSH into the router — SSH times out. Which is the most likely cause, and what is the appropriate next troubleshooting action?

A) The router has failed completely — ping succeeds because ICMP is processed by a separate hardware path from the management plane; the analyst should dispatch a technician to physically inspect and power cycle the router
B) The SNMP agent process or SSH daemon on the router has crashed or the management ACL is blocking the NMS and the analyst's IP — the analyst should check whether the router's control plane processes are running by attempting access via an out-of-band console connection or by checking the syslog server for related error messages
C) The network monitoring system (NMS) has a software bug causing false SNMP timeout alerts — since ping succeeds, the router is healthy; the analyst should restart the NMS polling process and mark the alert as a false positive without further investigation
D) The router's uplink interface has failed, isolating it from the rest of the network — ping works because ICMP is handled locally by the router CPU, while SNMP and SSH traffic is forwarded through the failed uplink interface to reach the NMS and analyst's workstation

*   **Correct Answer:** B) The SNMP agent process or SSH daemon on the router has crashed or the management ACL is blocking the NMS and the analyst's IP — the analyst should check whether the router's control plane processes are running by attempting access via an out-of-band console connection or by checking the syslog server for related error messages
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A completely failed router would not respond to ping. The fact that ping succeeds confirms the router's data plane (forwarding) is operational and the IP stack is responding. A failed router is ruled out by the successful ping — hardware failure does not explain selective failure of SNMP and SSH while ICMP continues to function.
    *   *Why C is incorrect:* While NMS software bugs do occur, dismissing an alert as a false positive without verifying the underlying cause is poor troubleshooting practice and violates the CompTIA methodology (Step 2: establish a theory; Step 3: test the theory). The simultaneous failure of both SNMP (UDP 161) and SSH (TCP 22) from independent sources makes a software bug unlikely and warrants investigation. Marking without investigation is negligent.
    *   *Why D is incorrect:* If the router's uplink interface had failed, the ping from the analyst's workstation would also fail — because the ping itself must traverse the same network path as SNMP and SSH traffic to reach the router's management IP. A failed uplink would cause ping to fail, not succeed. The scenario describes selective management-plane failure (SNMP/SSH down) while the data plane responds to ICMP, which is a control plane process or ACL issue.

---

**Question 5**
A company is preparing for its CompTIA Network+ N10-009 certification audit and must verify that its network documentation, security controls, and operational practices align with exam domain objectives. The security team presents the following four configurations: (1) SNMPv3 authPriv mode for all network device monitoring, (2) 802.1Q trunk ports with native VLAN set to VLAN 999 (unused, carries no data), (3) All workstation switch ports configured with PortFast and BPDU Guard enabled, (4) Inter-VLAN routing handled by a Layer 3 switch using SVIs rather than a Router-on-a-Stick configuration. Which evaluation of all four configurations is correct?

A) Configuration 1 is the only fully correct choice — SNMPv3 authPriv is definitively best practice. Configurations 2, 3, and 4 each contain a security or design flaw: native VLAN should always be VLAN 1, BPDU Guard should not be used with PortFast, and Router-on-a-Stick is the preferred inter-VLAN method for enterprise networks
B) All four configurations represent current best practices — SNMPv3 authPriv provides encrypted monitoring, a non-default unused native VLAN prevents double-tagging attacks, PortFast with BPDU Guard is the recommended access port configuration, and Layer 3 switch SVIs provide more scalable inter-VLAN routing than Router-on-a-Stick
C) Configuration 4 is incorrect — Router-on-a-Stick using a single trunk link with 802.1Q sub-interfaces is always preferred over Layer 3 SVIs because sub-interfaces provide hardware-level forwarding while SVIs are processed in software, making SVIs slower and unsuitable for production inter-VLAN routing
D) Configuration 3 is incorrect — PortFast should only be enabled on uplink ports connecting to other switches, not on workstation access ports; enabling PortFast on end-device ports introduces a Spanning Tree loop risk because the port skips the Listening and Learning states that normally prevent loops during link initialization

*   **Correct Answer:** B) All four configurations represent current best practices — SNMPv3 authPriv provides encrypted monitoring, a non-default unused native VLAN prevents double-tagging attacks, PortFast with BPDU Guard is the recommended access port configuration, and Layer 3 switch SVIs provide more scalable inter-VLAN routing than Router-on-a-Stick
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This distractor contains three false claims. (1) The native VLAN should NOT always be VLAN 1 — changing it to an unused VLAN is explicit security best practice to prevent VLAN-hopping double-tagging attacks. (2) BPDU Guard is specifically designed to work with PortFast on access ports — they are a complementary security pair, not incompatible options. (3) Router-on-a-Stick is an older design that uses a single physical link as a bottleneck; Layer 3 SVIs on a multilayer switch are the modern, scalable enterprise best practice.
    *   *Why C is incorrect:* Modern Layer 3 switches use ASICs (Application-Specific Integrated Circuits) to forward inter-VLAN traffic at line rate in hardware — SVIs are not processed in software at reduced speed on enterprise-grade switches. Router-on-a-Stick is actually the design with a performance limitation (all inter-VLAN traffic must traverse a single physical trunk link twice — in and out), making it unsuitable for high-traffic environments. Layer 3 SVIs are the preferred enterprise inter-VLAN routing method.
    *   *Why D is incorrect:* PortFast is specifically designed for end-device access ports — workstation, printer, and server ports — not uplink ports between switches. Enabling PortFast on a switch uplink port is dangerous because it would skip STP's Listening and Learning states on a port that could create a loop. BPDU Guard mitigates the PortFast loop risk on access ports by immediately disabling any port that receives a BPDU, which would only occur if a switch (not a workstation) were incorrectly connected to an access port.

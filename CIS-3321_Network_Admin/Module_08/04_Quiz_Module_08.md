# Quiz: Module 08 - Network Security – Firewalls, IDS/IPS, and VPNs
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A security administrator wants to place a web server so it is accessible from the internet while ensuring that compromised web server cannot directly access internal HR or finance systems. Which network architecture accomplishes this?
A) Place the web server on the internal LAN in its own VLAN, with inter-VLAN routing permitted through the core switch
B) Place the web server in a DMZ segment connected to a dedicated firewall interface, with deny rules blocking DMZ-to-LAN traffic
C) Place the web server on the internet-facing router interface with a static NAT entry pointing to a private IP address
D) Place the web server directly on the ISP connection and use a host-based firewall on the server itself for protection
*   **Correct Answer:** B) Place the web server in a DMZ segment connected to a dedicated firewall interface, with deny rules blocking DMZ-to-LAN traffic
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Placing a public-facing server on the internal LAN — even in its own VLAN — means a compromised server has a Layer 3 path to internal systems. The DMZ specifically exists to prevent this by inserting a firewall boundary between public servers and private resources.
    *   *Why C is incorrect:* Placing a server directly on a router interface with NAT provides no DMZ isolation. The server would be fully internet-exposed with only its own host security, and no firewall boundary separates it from internal systems.
    *   *Why D is incorrect:* A server directly on the ISP link bypasses all network-layer security devices. A host-based firewall alone is insufficient to protect a public-facing server, and there is no isolation from the internal network.

---

**Question 2**
A network security team receives an alert from their monitoring system showing a signature match for a known SQL injection attack pattern. The system generated the alert and logged the event but did not stop the attack traffic from reaching the web server. Which type of security system is in use?
A) NGFW (Next-Generation Firewall) — deep packet inspection blocked the connection at the perimeter
B) IPS (Intrusion Prevention System) — inline blocking prevented the payload from reaching the server
C) IDS (Intrusion Detection System) — passive monitoring detected the signature and generated an alert without blocking traffic
D) WAF (Web Application Firewall) — application-layer inspection identified and dropped the HTTP request
*   **Correct Answer:** C) IDS (Intrusion Detection System) — passive monitoring detected the signature and generated an alert without blocking traffic
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An NGFW with active rules would have blocked the connection at the firewall before it reached the web server. The traffic was not blocked, eliminating NGFW as the active device.
    *   *Why B is incorrect:* An IPS is an inline active system that blocks matching traffic in real time. If the attack traffic reached the server, the device is not acting as an IPS — it generated an alert only, which is IDS behavior.
    *   *Why D is incorrect:* A WAF inspects and can block HTTP/HTTPS application-layer attacks including SQL injection. If the WAF were in active blocking mode, the attack would have been dropped before reaching the server.

---

**Question 3**
A network administrator notices that the ARP table on a workstation has an entry mapping the default gateway's IP address to an unexpected MAC address belonging to another workstation on the same subnet. Which attack is most likely occurring, and which tool on a managed switch can mitigate it?
A) VLAN hopping attack — mitigated by disabling DTP on all access ports and configuring explicit trunk ports
B) ARP poisoning (ARP spoofing) attack — mitigated by enabling Dynamic ARP Inspection (DAI) on the switch
C) MAC flooding attack — mitigated by configuring Port Security with a maximum MAC address limit per port
D) IP spoofing attack — mitigated by enabling Unicast Reverse Path Forwarding (uRPF) on the router
*   **Correct Answer:** B) ARP poisoning (ARP spoofing) attack — mitigated by enabling Dynamic ARP Inspection (DAI) on the switch
*   **Distractor Analysis:**
    *   *Why A is incorrect:* VLAN hopping exploits trunk negotiation (DTP) to access unauthorized VLANs — it does not result in incorrect IP-to-MAC mappings in an ARP table. The symptom described is specific to ARP poisoning.
    *   *Why C is incorrect:* MAC flooding overwhelms the switch's CAM table to force it into hub mode, causing all traffic to be broadcast out all ports. It does not alter ARP table entries on workstations.
    *   *Why D is incorrect:* IP spoofing involves forging the source IP address in packet headers — it does not produce a rogue MAC-to-IP mapping in a workstation's ARP cache. uRPF is a router-level control, not a switch-level ARP mitigation.

---

**Question 4**
A company's website becomes unavailable for 45 minutes after receiving millions of HTTP requests per second from thousands of different source IP addresses worldwide. Internal systems remain unaffected. Which type of attack best describes this event?
A) Man-in-the-Middle (MitM) — an attacker intercepts traffic between users and the web server
B) ARP poisoning — the attacker poisons ARP caches on the local network segment to redirect traffic
C) Distributed Denial of Service (DDoS) — a botnet of compromised hosts floods the target with traffic to exhaust its resources
D) VLAN hopping — the attacker sends double-tagged frames to reach a restricted network segment
*   **Correct Answer:** C) Distributed Denial of Service (DDoS) — a botnet of compromised hosts floods the target with traffic to exhaust its resources
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A MitM attack intercepts communications between two parties — it does not cause an availability outage from thousands of external sources. The symptom is unavailability from massive traffic volume, not data interception.
    *   *Why B is incorrect:* ARP poisoning is a local network attack that redirects traffic on the same subnet — it requires the attacker to be on the same network segment and does not generate millions of requests from worldwide sources.
    *   *Why D is incorrect:* VLAN hopping is a Layer 2 attack targeting switch misconfiguration to access restricted VLANs — it does not cause a service availability outage and cannot originate from thousands of external internet hosts.

---

**Question 5**
A security engineer is hardening a corporate network. The requirements are: (1) prevent unauthorized devices from plugging into switch ports, (2) block traffic from reaching internal systems from the DMZ web server, and (3) protect against known exploit payloads crossing the network boundary. Which combination of controls satisfies all three requirements?
A) Enable Port Security with sticky MAC on access ports, configure firewall deny rules for DMZ-to-LAN traffic, and deploy an IPS inline at the network perimeter.
B) Configure WPA3-SAE on all wireless APs, enable VLAN tagging on all trunk ports, and deploy an IDS sensor on the core switch.
C) Enable SNMP monitoring on all switches, configure NAT on the perimeter router, and deploy a host-based antivirus on all servers.
D) Implement 802.1Q VLAN segmentation on the core switch, enable spanning tree PortFast on access ports, and configure static ARP entries on all workstations.
*   **Correct Answer:** A) Enable Port Security with sticky MAC on access ports, configure firewall deny rules for DMZ-to-LAN traffic, and deploy an IPS inline at the network perimeter.
*   **Distractor Analysis:**
    *   *Why A is correct:* Port Security prevents unauthorized device connections (requirement 1); firewall deny rules block DMZ-to-LAN traffic (requirement 2); an inline IPS detects and blocks known exploit payloads at the network boundary (requirement 3). Each control maps directly to one requirement.
    *   *Why B is incorrect:* WPA3-SAE secures wireless association but does not control wired switch port access. An IDS detects but does not block exploit payloads — failing requirement 3. VLAN tagging on trunk ports is a switching configuration, not a security control for DMZ isolation.
    *   *Why C is incorrect:* SNMP monitoring provides visibility but no access control. NAT translates addresses but does not control which devices can plug into switch ports or block exploit payloads inline. Antivirus protects hosts after infection but does not satisfy any of the three network-layer requirements.
    *   *Why D is incorrect:* VLAN segmentation improves network organization but does not prevent unauthorized devices from connecting to switch ports without authentication. PortFast speeds STP convergence on access ports — it is not a security control. Static ARP entries mitigate ARP poisoning but do not address the three stated requirements.

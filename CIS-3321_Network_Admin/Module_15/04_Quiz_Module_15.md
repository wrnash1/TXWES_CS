# Quiz: Module 15 - CompTIA Network+ Acronym Mastery
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

**Question 1**
A network analyst is troubleshooting a wireless network where multiple devices are transmitting simultaneously and causing communication failures. The analyst explains to a junior technician that the wireless standard uses a different media access method than wired Ethernet specifically because collisions cannot be reliably detected on a wireless medium. Which media access control method does IEEE 802.11 Wi-Fi use, and how does it differ from the method used by IEEE 802.3 wired Ethernet?

A) Wi-Fi uses CSMA/CD (Carrier Sense Multiple Access with Collision Detection) — the same method as wired Ethernet — but wireless NICs use a faster back-off timer to compensate for the higher collision rate on shared wireless channels
B) Wi-Fi uses CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance), which waits a random back-off interval before transmitting to avoid collisions, because wireless devices cannot reliably detect collisions mid-transmission the way wired Ethernet can
C) Wi-Fi uses TDMA (Time Division Multiple Access), which assigns fixed time slots to each device so that only one device transmits per slot, eliminating the need for collision detection or avoidance mechanisms
D) Wired Ethernet uses CSMA/CA while Wi-Fi uses CSMA/CD — wireless networks require collision detection because the open air medium makes simultaneous transmission more likely than on a shielded copper cable

*   **Correct Answer:** B) Wi-Fi uses CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance), which waits a random back-off interval before transmitting to avoid collisions, because wireless devices cannot reliably detect collisions mid-transmission the way wired Ethernet can
*   **Distractor Analysis:**
    *   *Why A is incorrect:* IEEE 802.11 Wi-Fi does NOT use CSMA/CD. CSMA/CD is the media access method for wired Ethernet (IEEE 802.3). The fundamental difference is that wireless devices cannot detect collisions during their own transmission because the transmitted signal overwhelms the received signal on the same antenna — hence the switch to collision avoidance (CA) rather than detection (CD). A faster back-off timer does not substitute for this architectural difference.
    *   *Why C is incorrect:* TDMA (Time Division Multiple Access) is used in cellular networks (GSM) and some satellite communications — it is not the media access method for IEEE 802.11 Wi-Fi. Wi-Fi does not use fixed time slots assigned in advance; it uses CSMA/CA with random back-off periods.
    *   *Why D is incorrect:* This reverses the two standards. Wired Ethernet (IEEE 802.3) uses CSMA/CD, and Wi-Fi (IEEE 802.11) uses CSMA/CA. This is one of the most commonly tested acronym confusion traps on the CompTIA Network+ exam — the correct pairing is: 802.3 Ethernet = CSMA/CD, 802.11 Wi-Fi = CSMA/CA.

---

**Question 2**
A security operations center receives an alert that a monitoring device on the network detected a SQL injection attempt against a web application server but did not block the attack. The attacker successfully retrieved database records. The security team wants to replace this device with one that would have blocked the attack in real time. Which acronym correctly identifies the current device and the replacement device?

A) The current device is an IPS (Intrusion Prevention System); the replacement should be an IDS (Intrusion Detection System) configured in aggressive blocking mode to stop attacks before they reach the server
B) The current device is a SIEM (Security Information and Event Management) platform; the replacement should be a WAF (Web Application Firewall) because SIEMs only correlate logs and cannot inspect or block Layer 7 application traffic
C) The current device is an IDS (Intrusion Detection System), which is passive and out-of-band — it monitors a copy of traffic and alerts but does not block; the replacement should be an IPS (Intrusion Prevention System), which sits inline and actively blocks detected threats
D) The current device is a stateless firewall using ACLs; the replacement should be a stateful firewall that tracks connection state and can detect application-layer SQL injection patterns within established TCP sessions

*   **Correct Answer:** C) The current device is an IDS (Intrusion Detection System), which is passive and out-of-band — it monitors a copy of traffic and alerts but does not block; the replacement should be an IPS (Intrusion Prevention System), which sits inline and actively blocks detected threats
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This reverses the roles. An IPS (Intrusion Prevention System) is the inline active-blocking device, not the passive monitoring device. An IDS cannot be configured into "aggressive blocking mode" — the fundamental architectural difference is that IDS receives a copy of traffic (via SPAN port or tap) and cannot intercept or block it. An IPS is physically in the traffic path and can drop packets.
    *   *Why B is incorrect:* A SIEM aggregates and correlates log data from multiple sources — it does not inspect live network traffic at all. A SIEM would not generate a real-time alert about an active SQL injection mid-session in the way described. While a WAF does block web application attacks, the scenario describes a network monitoring device that detected but didn't block — this is the IDS/IPS distinction, not SIEM/WAF.
    *   *Why D is incorrect:* A stateless ACL-based firewall filters packets based on IP address and port without tracking connection state. A stateful firewall tracks TCP sessions but still operates primarily at Layer 3/4. Neither stateless nor stateful firewalls perform deep packet inspection for application-layer SQL injection patterns — that is the function of an IPS or WAF. The described behavior (detected but did not block) matches IDS architecture, not a firewall limitation.

---

**Question 3**
A network administrator is configuring a new managed switch for remote management. The security policy requires that all management traffic be encrypted in transit and that the management protocol authenticate with a username and password rather than a shared community string. Which protocol and version satisfies both requirements for managing the switch via the network management station?

A) SNMPv2c with a strong read-write community string of at least 16 characters — the length of the community string determines encryption strength, and SNMPv2c supports MD5 hashing when configured on Cisco IOS devices
B) SNMPv3 with authentication and privacy mode (authPriv) — SNMPv3 supports per-user authentication using MD5 or SHA hashing and encrypts SNMP messages using AES or DES, replacing the shared plaintext community string model
C) SNMPv1 with SNMP over TLS (Transport Layer Security) — wrapping SNMPv1 in a TLS tunnel provides the encryption that SNMPv1 lacks natively while retaining backward compatibility with legacy management software
D) Syslog with TCP transport on port 514 — TCP syslog provides reliable delivery and encrypts management traffic between the switch and the NMS, satisfying both the encryption and authentication requirements

*   **Correct Answer:** B) SNMPv3 with authentication and privacy mode (authPriv) — SNMPv3 supports per-user authentication using MD5 or SHA hashing and encrypts SNMP messages using AES or DES, replacing the shared plaintext community string model
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SNMPv2c uses plaintext community strings regardless of their length. Community string length has no effect on encryption — SNMPv2c does not support encryption at all. SNMPv2c community strings are transmitted in cleartext on the network and can be captured with a packet sniffer. This fails the encryption requirement.
    *   *Why C is incorrect:* SNMPv1 wrapped in TLS is not a standard, widely-supported configuration on enterprise network devices. More importantly, the scenario requires a protocol that uses username/password authentication rather than a shared community string — SNMPv1 does not have a per-user authentication model regardless of transport. SNMPv3 natively addresses both authentication and encryption without requiring a transport wrapper.
    *   *Why D is incorrect:* Syslog is a log-forwarding protocol — it sends log messages from devices to a central syslog server. Syslog does not provide a management interface for polling device statistics, setting configuration parameters, or receiving SNMP traps. TCP syslog on port 514 provides reliable delivery but does not encrypt syslog messages. This answers neither the management protocol requirement nor the encryption requirement correctly.

---

**Question 4**
A network engineer is reviewing the routing table on a router that has learned routes via three different sources: a directly connected interface, a static route configured by the administrator, and OSPF dynamic routing. All three sources have learned a route to the same destination network 192.168.50.0/24. The engineer needs to determine which route will be installed in the routing table and used to forward packets. Which source wins and why?

A) The OSPF route wins because OSPF uses Dijkstra's algorithm to calculate the mathematically optimal path, making it more accurate than a manually configured static route or a directly connected interface with no calculation
B) The static route wins because administrator-configured routes always take precedence over both dynamic routing protocols and directly connected interfaces, since static routes represent intentional administrative decisions
C) The directly connected route wins because a connected interface has an Administrative Distance of 0, which is lower than the Administrative Distance of any static route (AD=1) or dynamic routing protocol (OSPF AD=110), and the lowest AD wins
D) All three routes are installed in the routing table simultaneously, and the router load-balances traffic across all three paths using ECMP (Equal-Cost Multi-Path) regardless of their Administrative Distance values

*   **Correct Answer:** C) The directly connected route wins because a connected interface has an Administrative Distance of 0, which is lower than the Administrative Distance of any static route (AD=1) or dynamic routing protocol (OSPF AD=110), and the lowest AD wins
*   **Distractor Analysis:**
    *   *Why A is incorrect:* OSPF's use of Dijkstra's algorithm determines the best path within the OSPF routing domain — it does not override Administrative Distance. OSPF has an AD of 110, which is higher than both connected interfaces (AD=0) and static routes (AD=1). OSPF routes lose to both connected routes and static routes when all three exist for the same destination.
    *   *Why B is incorrect:* Static routes have an AD of 1, which is lower than dynamic routing protocols but higher than directly connected interfaces (AD=0). Static routes do not override connected interfaces. The hierarchy is: Connected (0) > Static (1) > OSPF (110) > RIP (120).
    *   *Why D is incorrect:* ECMP load-balancing applies only when multiple routes to the same destination have identical Administrative Distance AND identical metric — it does not apply when routes from different sources with different ADs exist for the same destination. Only the route with the lowest AD is installed in the routing table; the others are not used.

---

**Question 5**
A network architect is reviewing a design proposal for a new enterprise campus network. The proposal includes the following design decisions: (1) all workstation-facing switch ports have PortFast and BPDU Guard enabled, (2) inter-VLAN routing is handled by a Layer 3 switch with SVIs, (3) redundant uplinks use LACP with one Active and one Passive port on each side, and (4) 802.1Q trunks between distribution and core switches carry all VLANs with a dedicated native VLAN that carries no user data. Which of the following statements correctly evaluates ALL FOUR design decisions?

A) Decision 1 is incorrect — PortFast should never be combined with BPDU Guard because BPDU Guard disables ports that receive BPDUs, which means any PortFast port connected to a legitimate access switch would be immediately shut down; Decision 2 is correct; Decision 3 is correct; Decision 4 is correct
B) All four decisions are correct — PortFast+BPDU Guard is best practice for access ports, Layer 3 SVIs correctly handle inter-VLAN routing, LACP Active/Passive forms an EtherChannel, and a dedicated native VLAN carrying no user data prevents native VLAN VLAN-hopping attacks
C) Decision 3 is incorrect — LACP requires both ends to be configured as Active; one Active and one Passive port will not negotiate an EtherChannel because LACP Passive mode waits for the remote end to initiate, and two waiting ports cannot form a bundle
D) Decision 4 is incorrect — the native VLAN on 802.1Q trunks must always be VLAN 1 to maintain IEEE 802.1Q standard compliance; changing the native VLAN to a dedicated unused VLAN is not permitted by the standard and will cause trunk negotiation failures

*   **Correct Answer:** B) All four decisions are correct — PortFast+BPDU Guard is best practice for access ports, Layer 3 SVIs correctly handle inter-VLAN routing, LACP Active/Passive forms an EtherChannel, and a dedicated native VLAN carrying no user data prevents native VLAN VLAN-hopping attacks
*   **Distractor Analysis:**
    *   *Why A is incorrect:* PortFast and BPDU Guard are explicitly designed to work together — they are a security best-practice pair for access ports. BPDU Guard shuts down a PortFast port only if a BPDU is received, which indicates a switch has been connected to what should be an end-device port (rogue switch detection). Legitimate access switches connected to distribution ports do not use PortFast. This distractor misrepresents the purpose of BPDU Guard.
    *   *Why C is incorrect:* LACP Active/Passive is a valid and functional combination. Active mode initiates LACP negotiation by sending LACP PDUs; Passive mode responds to LACP PDUs but does not initiate. One Active and one Passive port on opposing sides will successfully negotiate an EtherChannel. The only combination that fails is Passive/Passive on both ends — two Passive ports both wait for the other to initiate and never form the bundle.
    *   *Why D is incorrect:* The IEEE 802.1Q standard does not require the native VLAN to be VLAN 1. VLAN 1 is the default native VLAN on most switches, but best practice explicitly recommends changing it to an unused VLAN that carries no user traffic. This prevents double-tagging VLAN-hopping attacks, which exploit the fact that the native VLAN's traffic is transmitted untagged on the trunk. Changing the native VLAN is standard enterprise security hardening, not a standards violation.

# Quiz: Module 16 — CCNA 200-301 Exam Preparation and Capstone

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Instructions

This capstone quiz covers all six CCNA 200-301 exam domains. Select the single best answer for each question. Each question is worth 5 points (20 questions, 100 points total).

---

## Question 1

A host at 172.16.5.200/20 needs to communicate with a host at 172.16.14.100/20. Are these hosts on the same subnet?

A. Yes — both are within the 172.16.0.0/20 network.

B. No — 172.16.5.200/20 is in 172.16.0.0/20 but 172.16.14.100/20 is in 172.16.0.0/12.

C. No — they are in different /20 blocks and require inter-VLAN routing.

D. Yes — /20 masks always place all 172.16.x.x addresses in the same subnet.

Correct Answer: A — A /20 mask is 255.255.240.0. For 172.16.x.x/20, the block size in the third octet is 16. Starting at 172.16.0.0/20, the block covers 172.16.0.x through 172.16.15.x. Both 172.16.5.200 and 172.16.14.100 fall within this range. Both are in 172.16.0.0/20.

Distractor Analysis:

* B — /12 is a much larger block (172.16.0.0–172.31.255.255). This mixes up CIDR prefix lengths.
* C — Both hosts are in the same /20 block (0–15 in the third octet). A second /20 block would start at 172.16.16.0.
* D — /20 does not cover all 172.16.x.x. That range requires /16.

---

## Question 2

Four switches participate in STP. Switch A has priority 28672. Switches B, C, and D each have the default priority 32768. Switch C has the lowest MAC address among B, C, and D. Which switch becomes the root bridge?

A. Switch A

B. Switch B

C. Switch C

D. Switch D

Correct Answer: A — The root bridge is elected by the lowest bridge ID. Bridge ID equals priority plus VLAN ID plus MAC. Switch A has priority 28672 versus 32768 for all others. A lower priority always wins regardless of MAC address. Switch A becomes the root bridge.

Distractor Analysis:

* B, C, D — These switches all have priority 32768. Among them Switch C would win (lowest MAC), but Switch A's lower priority takes precedence over all three.

---

## Question 3

An OSPF adjacency between two routers is stuck in the EXSTART state. What is the most likely cause?

A. Mismatched hello and dead intervals between the two routers.

B. Duplicate OSPF router IDs on both routers.

C. Mismatched area IDs on the connected interfaces.

D. The interface toward the neighbor is in the passive-interface state.

Correct Answer: B — EXSTART is the state where master/slave negotiation and initial sequence number exchange occurs. If both routers have the same router ID, they cannot resolve the negotiation and the adjacency freezes in EXSTART.

Distractor Analysis:

* A — Mismatched hello/dead intervals prevent the neighbor from progressing past the INIT state, not EXSTART.
* C — Mismatched area IDs would prevent full adjacency but typically manifest differently. Routers in different areas can still form adjacencies on the boundary.
* D — A passive interface would not send or receive hellos. The neighbor would never appear at all.

---

## Question 4

The output of `show ip nat translations` shows: Inside local 10.0.0.50 — Inside global 203.0.113.5. What does the inside global address represent?

A. The private IP of the internal host assigned by DHCP.

B. The public IP representing the internal host as seen from the Internet.

C. The IP address of the NAT router's inside interface.

D. The actual IP of the external destination server.

Correct Answer: B — Inside global is the public IP address that represents the inside host to external parties. When 10.0.0.50 sends traffic outbound, NAT replaces the source address with 203.0.113.5. The inside local (10.0.0.50) is the actual private IP assigned to the host.

Distractor Analysis:

* A — The private IP of the host is the inside local address.
* C — The router's inside interface IP is typically the default gateway for inside hosts, not the inside global address.
* D — The external destination's IP is the outside global address, which is a separate NAT concept.

---

## Question 5

A routing table entry reads: `O 192.168.5.0/24 [110/2] via 10.0.0.2`. What does the value 110 represent?

A. The OSPF process ID

B. The administrative distance of OSPF

C. The OSPF cost (metric) to reach 192.168.5.0/24

D. The OSPF hello interval in seconds

Correct Answer: B — In routing table entries, the format is `[AD/metric]`. The first number is administrative distance; the second is the metric. OSPF has a default administrative distance of 110. The metric (cost) is 2 in this entry.

Distractor Analysis:

* A — OSPF process ID is configured with `router ospf X` and does not appear in routing table entries.
* C — The OSPF cost (metric) is the second number in brackets, which is 2 here.
* D — Hello intervals are OSPF operational timers and do not appear in routing table entries.

---

## Question 6

Which syslog severity level indicates a condition requiring immediate action while the system remains operational?

A. Level 0 — Emergencies

B. Level 1 — Alerts

C. Level 2 — Critical

D. Level 3 — Errors

Correct Answer: B — Level 1 Alerts requires immediate action. Level 0 Emergencies indicates the system is unusable. The key distinction is that Alerts are urgent but the system can still function, while Emergencies indicate system failure.

Distractor Analysis:

* A — Level 0 Emergencies means the system itself is unusable, which is more severe than Alerts.
* C — Level 2 Critical indicates critical conditions but is less urgent than Alerts.
* D — Level 3 Errors needs attention but is not immediate like Alerts.

---

## Question 7

A switch port is in err-disabled state after a port-security violation. Which of the following are valid methods to restore port operation?

A. `no switchport port-security` removes and re-adds security.

B. `shutdown` followed by `no shutdown` on the interface.

C. `errdisable recovery cause psecure-violation` with a recovery interval.

D. Both B and C are valid methods.

Correct Answer: D — Both the manual shutdown/no shutdown method and the configured automatic recovery method are valid. The shutdown/no shutdown immediately restores the port; automatic recovery restores it after the configured timer expires.

Distractor Analysis:

* A — Removing port-security clears all sticky MAC entries, which is destructive and not the standard recovery method.
* B alone — Correct but incomplete since C is also valid.
* C alone — Correct but incomplete since B is also valid.

---

## Question 8

An HSRP group is configured. Router A has priority 120 and Router B has priority 100. Router A fails and Router B becomes active. When Router A recovers, what must be configured on Router A to ensure it reclaims the active role?

A. `standby 1 priority 120`

B. `standby 1 preempt`

C. `standby 1 track 1 decrement 30`

D. `standby 1 timers 1 3`

Correct Answer: B — `standby 1 preempt` allows a higher-priority router to reclaim the active role after returning from a failure. Without preempt, the router that became active during the outage (Router B) remains active regardless of Router A's higher priority.

Distractor Analysis:

* A — Setting priority is required but insufficient alone. Preempt must be separately configured to trigger role recovery.
* C — Interface tracking adjusts priority dynamically when a tracked interface fails. It does not control post-recovery role reclamation.
* D — HSRP timers control failover detection speed, not role recovery after restoration.

---

## Question 9

Which command displays the current DHCP snooping status including trusted ports and active VLANs?

A. `show ip dhcp server`

B. `show ip dhcp snooping`

C. `show ip arp inspection`

D. `show dhcp lease`

Correct Answer: B — `show ip dhcp snooping` displays whether snooping is globally enabled, which VLANs are protected, which ports are trusted, and the Option 82 setting. This is the primary verification command for DHCP snooping configuration.

Distractor Analysis:

* A — `show ip dhcp server` is not a valid Cisco IOS command.
* C — `show ip arp inspection` verifies DAI status, not DHCP snooping.
* D — `show dhcp lease` is not a standard Cisco IOS command; lease info is shown with `show ip dhcp binding`.

---

## Question 10

In an 802.1X deployment, which device communicates directly with the RADIUS server using RADIUS protocol?

A. The user's laptop (supplicant)

B. The switch port (authenticator)

C. The default gateway router

D. The DHCP server

Correct Answer: B — The switch port (authenticator) communicates with the RADIUS server using the RADIUS protocol. The supplicant communicates with the authenticator using EAPOL (EAP over LAN). The authenticator encapsulates EAPOL messages in RADIUS packets and forwards them to the authentication server.

Distractor Analysis:

* A — The supplicant communicates with the switch using EAPOL, not directly with the RADIUS server.
* C — The default gateway has no role in 802.1X authentication.
* D — The DHCP server provides IP addressing after authentication. It is not part of the 802.1X authentication exchange.

---

## Question 11

Which IPv6 address type is automatically assigned to every IPv6-capable interface and is only valid for local-link communication?

A. Global unicast (2000::/3)

B. Unique local (FC00::/7)

C. Link-local (FE80::/10)

D. Multicast (FF00::/8)

Correct Answer: C — Link-local addresses in the FE80::/10 range are automatically configured on every IPv6-enabled interface. They are valid only within a single network segment and are never routed beyond the local link. They are essential for neighbor discovery and routing protocol exchanges.

Distractor Analysis:

* A — Global unicast addresses are routable on the Internet and are not automatically assigned to every interface.
* B — Unique local addresses are private-scope and not automatically assigned.
* D — Multicast addresses represent delivery groups, not individual interface addresses.

---

## Question 12

Which combination of evidence most directly confirms a full OSPF adjacency with a neighbor?

A. `show ip route ospf` shows routes from the neighbor only.

B. `show ip ospf neighbor` shows the neighbor in FULL state only.

C. `show ip interface brief` shows the neighbor-facing interface as Up/Up only.

D. Both A and B together confirm full adjacency.

Correct Answer: D — `show ip ospf neighbor` showing FULL is the direct confirmation of adjacency state. Routes appearing in `show ip route ospf` also confirm that OSPF has exchanged LSAs and completed SPF. Together they provide definitive confirmation.

Distractor Analysis:

* A alone — Routes in the table imply full adjacency but do not explicitly show the adjacency state.
* B alone — Correct and most direct, but D is more complete.
* C — An Up/Up interface is required for OSPF to run but does not confirm that adjacency was established.

---

## Question 13

Which command configures a floating static route to 192.168.5.0/24 via 10.0.0.2 that will only be used if the OSPF-learned route disappears?

A. `ip route 192.168.5.0 255.255.255.0 10.0.0.2 111`

B. `ip route 192.168.5.0 255.255.255.0 10.0.0.2 1`

C. `ip route 192.168.5.0 255.255.255.0 10.0.0.2`

D. `ip route 0.0.0.0 0.0.0.0 10.0.0.2 111`

Correct Answer: A — A floating static route requires an administrative distance higher than the backing dynamic protocol. OSPF has AD 110. Setting the static route to AD 111 makes it install only when no OSPF route exists. The syntax appends the AD after the next-hop: `ip route network mask next-hop AD`.

Distractor Analysis:

* B — AD 1 would permanently prefer this static route over OSPF (AD 110), defeating the floating purpose.
* C — Default static route AD is 1, which always overrides OSPF. Not a floating static.
* D — This configures a default route, not a specific /24 prefix.

---

## Question 14

A Python script calls the DNA Center REST API and receives HTTP status code 403. What is the correct interpretation?

A. The authentication token has expired.

B. The URL endpoint does not exist.

C. The authenticated user lacks permission for the requested operation.

D. The server encountered an internal processing error.

Correct Answer: C — HTTP 403 Forbidden means the client is authenticated but not authorized. The server knows who the client is but the client's role does not permit the requested operation. This is distinct from 401 (not authenticated at all).

Distractor Analysis:

* A — An expired token returns 401 Unauthorized. 401 vs. 403 is a common exam distinction.
* B — A non-existent endpoint returns 404 Not Found.
* D — A server internal error returns 500 Internal Server Error.

---

## Question 15

Which transport protocol and port does NETCONF use?

A. HTTPS, TCP 443

B. SSH, TCP 830

C. HTTPS, TCP 8443

D. SSH, TCP 22

Correct Answer: B — NETCONF is transported over SSH on TCP port 830, as defined in RFC 4742. Port 830 is dedicated to NETCONF to allow firewalls to differentiate it from standard SSH management sessions on port 22.

Distractor Analysis:

* A — RESTCONF uses HTTPS on port 443. This is a common NETCONF/RESTCONF confusion trap.
* C — Port 8443 is sometimes used for RESTCONF in non-standard configurations, not NETCONF.
* D — Port 22 is standard SSH for CLI management. NETCONF uses the dedicated port 830.

---

## Question 16

A network engineer is configuring a Cisco WLC and needs traffic on SSID "CORP" to be placed in VLAN 10. What must she create on the WLC to map this WLAN to VLAN 10?

A. A VLAN access map

B. A dynamic interface

C. A service port interface

D. A virtual interface

Correct Answer: B — A dynamic interface on the Cisco WLC defines the VLAN ID, IP address, and DHCP server for a given WLAN. The CORP WLAN configuration references this dynamic interface to ensure client traffic is tagged with VLAN 10 when it reaches the wired network.

Distractor Analysis:

* A — VLAN access maps are a Catalyst switch security feature unrelated to WLC WLAN mapping.
* C — The service port is for out-of-band management of the WLC hardware, not for WLAN-to-VLAN mapping.
* D — The virtual interface handles DHCP relay and web authentication portal functions, not WLAN-to-VLAN mapping.

---

## Question 17

A network manager needs to automate configuration of 300 Cisco IOS switches. No software may be installed on the switches. Which tool meets this requirement?

A. Puppet — uses a declarative language

B. Chef — uses Ruby Cookbooks

C. Ansible — agentless, communicates over SSH

D. NETCONF — uses SSH port 830

Correct Answer: C — Ansible is agentless and requires no software on managed devices. It uses SSH to communicate with Cisco IOS devices via the cisco.ios Ansible collection. This is the only tool listed that operates without an agent on the managed switch.

Distractor Analysis:

* A — Puppet requires a Puppet agent on managed nodes. Network switches typically cannot run a Puppet agent.
* B — Chef requires a Chef client on managed nodes. Same limitation as Puppet.
* D — NETCONF is a configuration protocol, not an automation framework. It does not replace Ansible's orchestration capabilities.

---

## Question 18

Which two 2.4 GHz channels should adjacent access points use to avoid channel overlap?

A. Channels 1 and 2

B. Channels 1 and 6

C. Channels 6 and 7

D. Channels 3 and 9

Correct Answer: B — Only channels 1, 6, and 11 are non-overlapping in the US 2.4 GHz band. Adjacent APs must use different channels from this set. Channels 1 and 6 are non-overlapping and are a correct assignment for two adjacent APs.

Distractor Analysis:

* A — Channels 1 and 2 overlap significantly. Their centers are only 5 MHz apart but each channel is 22 MHz wide.
* C — Channels 6 and 7 overlap in the same way as channels 1 and 2.
* D — Channels 3 and 9 are partially overlapping and neither is in the standard non-overlapping set.

---

## Question 19

A switch port has sticky port security with violation shutdown and a maximum of 1 MAC address. One sticky MAC is already learned. A second device is connected. What happens?

A. The second MAC is added since the default maximum is 2.

B. The port enters err-disabled state immediately.

C. The second device's frames are silently dropped; the port stays up.

D. A syslog message is generated and the second device communicates normally.

Correct Answer: B — The default port-security maximum is 1. With violation shutdown, any frame from a second MAC exceeds the maximum and triggers err-disabled state immediately.

Distractor Analysis:

* A — The default maximum is 1, not 2. A second device violates the policy unless maximum is explicitly raised.
* C — Silent dropping describes the protect violation mode, not shutdown.
* D — Logging with continued connectivity describes the restrict violation mode, not shutdown.

---

## Question 20

Hosts in VLAN 10 cannot ping hosts in VLAN 20. The Layer 3 switch has correctly addressed SVIs for both VLANs. Which single command is most likely missing?

A. `spanning-tree vlan 10 priority 4096`

B. `ip routing`

C. `ip default-gateway 192.168.10.1`

D. `switchport trunk allowed vlan 10,20`

Correct Answer: B — On a Layer 3 switch, `ip routing` must be explicitly enabled to activate the routing engine. Without it, SVIs are configured but the switch does not route between them. This is the single most common omission in inter-VLAN routing configurations.

Distractor Analysis:

* A — Spanning Tree priority affects root bridge election and has no effect on routing between VLANs.
* C — `ip default-gateway` is for Layer 2 switches without ip routing enabled. It does not enable inter-VLAN routing.
* D — Trunk allowed VLANs affect which VLANs cross uplinks. If hosts on each VLAN can reach their default gateway, VLAN trunking is already working.

---

End of Quiz — Module 16 | 20 Questions | 100 Points

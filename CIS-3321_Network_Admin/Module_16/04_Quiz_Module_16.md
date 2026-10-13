# Quiz: Module 16 — Network+ N10-008 Exam Preparation

## Course: CIS-3321 Network Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA Network+ (N10-008)

**Questions:** 20 | **Format:** Multiple choice | **Scope:** All five N10-008 domains

---

### Question 1

A host receives the IP address 169.254.45.12 automatically. Which service has most likely failed?

- A. DNS
- B. DHCP
- C. NTP
- D. NAT

Correct Answer: B

Explanation: 169.254.0.0/16 is the APIPA range. Windows and other operating systems assign an APIPA address when a DHCP server cannot be reached.

---

### Question 2

Which OSI layer is responsible for logical addressing and routing packets between networks?

- A. Layer 2 (Data Link)
- B. Layer 3 (Network)
- C. Layer 4 (Transport)
- D. Layer 5 (Session)

Correct Answer: B

Explanation: IP addressing and routing decisions occur at Layer 3, the Network layer. Layer 2 handles MAC addressing within a single network segment.

---

### Question 3

A network administrator wants to bundle four physical links between two switches into a single logical link to maximize available bandwidth and prevent STP from blocking redundant ports. Which technology should be configured?

- A. RSTP
- B. PortFast
- C. EtherChannel
- D. BPDU Guard

Correct Answer: C

Explanation: EtherChannel bundles multiple physical links into one logical link. STP treats the bundle as a single link, so no ports are blocked, and all physical links carry traffic simultaneously.

---

### Question 4

Which wireless security standard uses Simultaneous Authentication of Equals (SAE) and is resistant to offline dictionary attacks?

- A. WEP
- B. WPA/TKIP
- C. WPA2/AES-CCMP
- D. WPA3/SAE

Correct Answer: D

Explanation: WPA3 introduced SAE to replace the PSK handshake used in WPA2 Personal. SAE is resistant to offline dictionary attacks because the handshake does not expose enough information for offline cracking.

---

### Question 5

A company uses MPLS for its WAN. Which statement about MPLS is accurate?

- A. MPLS routes packets using IP addresses at each hop
- B. MPLS uses labels to forward traffic, enabling traffic engineering and any-to-any connectivity
- C. MPLS is limited to point-to-point connections between two sites
- D. MPLS operates only over fiber optic transport media

Correct Answer: B

Explanation: MPLS uses short fixed-length labels instead of IP addresses to make forwarding decisions. It supports any-to-any VPN connectivity and allows traffic engineering — choosing paths based on QoS policies, bandwidth, or latency requirements.

---

### Question 6

Which port and protocol combination is used by SNMP traps?

- A. TCP 161
- B. UDP 161
- C. UDP 162
- D. TCP 162

Correct Answer: C

Explanation: SNMP queries are sent to port 161 (UDP). SNMP traps — unsolicited notifications from a device to the management station — are sent to port 162 (UDP).

---

### Question 7

A technician runs `tracert` from a Windows workstation to a remote server. The output shows that hops 3 through 6 are responding but hop 7 shows three asterisks (***) for all three probes, and all subsequent hops also show asterisks. What does this indicate?

- A. The remote server is unreachable due to a DNS failure
- B. The connection is being encrypted at hop 7
- C. Traffic is being dropped or a device at hop 7 is not responding to TTL-expired packets
- D. The workstation has an incorrect default gateway

Correct Answer: C

Explanation: Three asterisks in tracert output indicate the device at that hop is not returning ICMP TTL-exceeded messages, or packets are being dropped. This may be a firewall dropping ICMP, a router configured not to respond to traceroute probes, or a routing loop. The gateway issue would be visible at hop 1.

---

### Question 8

Which authentication protocol uses TCP port 49, encrypts the entire authentication payload, and is Cisco's preferred protocol for network device administration?

- A. RADIUS
- B. TACACS+
- C. 802.1X
- D. LDAP

Correct Answer: B

Explanation: TACACS+ uses TCP port 49 and encrypts the entire body of every authentication packet. This makes it more secure than RADIUS, which only encrypts the password field. TACACS+ is preferred for administering network devices (switches, routers) because it also fully separates authentication, authorization, and accounting.

---

### Question 9

A host with IP address 192.168.50.75 and subnet mask 255.255.255.192 needs to communicate with a host at 192.168.50.130. A network technician reports the hosts cannot reach each other without routing. Why?

- A. Both hosts are in the same /26 subnet and should communicate directly
- B. 192.168.50.75 is in the 192.168.50.64/26 subnet; 192.168.50.130 is in the 192.168.50.128/26 subnet
- C. The subnet mask 255.255.255.192 is not a valid mask
- D. The hosts need an ARP proxy to communicate across subnets

Correct Answer: B

Explanation: /26 (255.255.255.192) creates subnets of 64 addresses each. The first host is in 192.168.50.64–127; the second is in 192.168.50.128–191. They are in different subnets and require a Layer 3 router to communicate.

---

### Question 10

Which VPN type encrypts only the payload of the original IP packet, preserving the original IP header in the clear?

- A. IPsec Tunnel mode
- B. IPsec Transport mode
- C. SSL/TLS VPN
- D. GRE tunnel

Correct Answer: B

Explanation: IPsec Transport mode encrypts only the data payload and leaves the original IP header intact. It is used for end-to-end encryption between two hosts. Tunnel mode wraps the entire original packet in a new IP packet with a new header, making it suitable for site-to-site VPNs.

---

### Question 11

A network administrator is configuring RSTP on a switch. An access port connected to a workstation is taking 30 seconds to start forwarding traffic after the workstation boots. Which RSTP feature should be enabled to eliminate this delay?

- A. BPDU Guard
- B. Root Guard
- C. PortFast
- D. Loop Guard

Correct Answer: C

Explanation: PortFast instructs the switch to immediately move the port to Forwarding state, bypassing the Listening and Learning states. It should only be enabled on access ports connected to end devices, never on ports connected to switches. BPDU Guard is a companion feature that err-disables a PortFast port if a BPDU is received.

---

### Question 12

A company has two ISP circuits: fiber at 1 Gbps and cable broadband at 100 Mbps. They want to automatically route latency-sensitive VoIP traffic over the fiber link and route bulk file transfers over cable broadband. Which WAN technology provides this application-aware path selection?

- A. MPLS
- B. SD-WAN
- C. Metro Ethernet E-Line
- D. DMVPN

Correct Answer: B

Explanation: SD-WAN uses application-aware routing policies to direct different traffic types across different WAN transports. VoIP traffic can be assigned to the low-latency fiber path; bulk transfers can use the less expensive cable broadband circuit. MPLS alone does not provide multi-transport application-aware selection at this level.

---

### Question 13

Which step in the CompTIA seven-step troubleshooting model immediately follows "Implement the solution or escalate"?

- A. Establish a theory of probable cause
- B. Establish a plan of action
- C. Verify full system functionality
- D. Document findings, actions, and outcomes

Correct Answer: C

Explanation: The seven steps in order are: Identify the problem → Establish theory → Test the theory → Establish a plan → Implement or escalate → Verify full system functionality → Document. After implementing the fix, the technician must verify that the problem is fully resolved — not just the specific symptom but the entire affected system.

---

### Question 14

A security analyst discovers that an attacker has sent gratuitous ARP replies associating the attacker's MAC address with the default gateway's IP address. What type of attack is this and what is the likely goal?

- A. MAC flooding; to fill the CAM table and cause the switch to broadcast all traffic
- B. ARP poisoning; to redirect traffic through the attacker's device for interception
- C. VLAN hopping; to gain access to a restricted VLAN segment
- D. DNS poisoning; to redirect users to a malicious web server

Correct Answer: B

Explanation: ARP poisoning (also called ARP spoofing) involves sending fraudulent ARP replies to associate the attacker's MAC address with a legitimate IP, typically the default gateway. Hosts update their ARP cache and send gateway-destined traffic to the attacker instead, enabling a man-in-the-middle attack.

---

### Question 15

An administrator runs `show spanning-tree` on a Cisco switch and observes that one port is in "BLK" (Blocking) state. What does this indicate?

- A. The port is err-disabled due to a security violation
- B. The port is forwarding traffic normally but not learning MAC addresses
- C. STP has placed the port in Blocking state to prevent a Layer 2 loop
- D. The port has lost physical connectivity

Correct Answer: C

Explanation: STP Blocking state means the port is receiving BPDUs to monitor for topology changes but is not forwarding frames. STP intentionally blocks redundant ports to prevent loops. A blocked port is not err-disabled — err-disabled is a separate condition caused by security violations or other errors.

---

### Question 16

Which IPv6 address type is automatically configured on every IPv6-enabled interface and is used for communication within a single network link only?

- A. Global unicast (2000::/3)
- B. Multicast (ff00::/8)
- C. Link-local (fe80::/10)
- D. Unique local (fc00::/7)

Correct Answer: C

Explanation: Link-local addresses in the fe80::/10 range are automatically assigned to every IPv6 interface during address autoconfiguration. They are non-routable — valid only on a single link segment. Routers will not forward packets with a link-local source or destination address.

---

### Question 17

A network technician is troubleshooting a fiber connection. The receiving end of the link reports very low signal strength despite a short run. Which tool should the technician use to test for a physical break or severe bend in the fiber strand?

- A. TDR (Time Domain Reflectometer)
- B. Basic cable tester
- C. Visual fault locator (VFL)
- D. Protocol analyzer

Correct Answer: C

Explanation: A visual fault locator injects red laser light into the fiber. Physical breaks, sharp bends, or connector defects scatter the light visibly. For copper cables, a TDR measures the distance to a fault using reflected electrical signals. A basic cable tester only tests continuity on copper.

---

### Question 18

A user can successfully ping a server by its IP address but cannot connect to it using its hostname. All other users in the organization can connect by hostname without issues. Which service should be investigated first?

- A. DHCP
- B. DNS
- C. Default gateway
- D. Firewall

Correct Answer: B

Explanation: The ability to ping by IP but not hostname is the classic DNS failure symptom. The Layer 3 path works (ping by IP succeeds), but name resolution is failing. Since other users work normally, this is likely a DNS configuration issue on the affected workstation (wrong DNS server address or stale/missing DNS cache entry).

---

### Question 19

What is the administrative distance of OSPF routes on a Cisco router?

- A. 90
- B. 100
- C. 110
- D. 120

Correct Answer: C

Explanation: OSPF has an administrative distance of 110. Administrative distance represents the trustworthiness of a routing source — lower values are more preferred. EIGRP (internal) = 90, OSPF = 110, RIP = 120. If a router learns a route to the same destination via both EIGRP and OSPF, the EIGRP route wins because 90 < 110.

---

### Question 20

A company's SLA with its ISP guarantees 99.99% availability. Approximately how much total downtime per year is permitted under this SLA?

- A. 87.6 hours
- B. 8.76 hours
- C. 52.6 minutes
- D. 5.26 minutes

Correct Answer: C

Explanation: 99.99% availability (four nines) permits approximately 52.6 minutes of downtime per year. 99.9% (three nines) allows 8.76 hours. 99% allows 87.6 hours. 99.999% (five nines) allows only 5.26 minutes per year. These values are commonly tested on Network+ and are important for SLA negotiation and DR planning.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash

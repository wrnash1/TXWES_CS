# Quiz: Module 09 - WAN Technologies and VPNs

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 4: IP Services / Domain 5: Security Fundamentals)
**Questions:** 10 | **Points:** 10 (1 point each)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Question 1

Which IPsec component provides data integrity and origin authentication without providing encryption?

- A) ESP (Encapsulating Security Payload)
- B) AH (Authentication Header)
- C) IKE (Internet Key Exchange)
- D) Diffie-Hellman

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: ESP provides encryption in addition to integrity and authentication. ESP is the IPsec protocol that encrypts the payload, making traffic unreadable by eavesdroppers.
- B is correct: AH (Authentication Header) provides data integrity verification and origin authentication, confirming that the packet has not been modified and came from the expected source. AH does not provide encryption — the payload remains readable in cleartext.
- C is incorrect: IKE (Internet Key Exchange) is the protocol responsible for negotiating IPsec security associations and exchanging encryption keys between peers. It is the setup mechanism, not a data security protocol.
- D is incorrect: Diffie-Hellman is a key exchange algorithm used within IKE to securely derive shared encryption keys. It is not itself an IPsec security protocol.

---

## Question 2

Which of the following most accurately describes GRE (Generic Routing Encapsulation) tunnels?

- A) A tunneling protocol that encapsulates any Layer 3 protocol within IP packets, enabling routing protocols and multicast traffic to traverse WAN links but providing no native encryption
- B) An IPsec transport-mode framework that encrypts only the IP payload between two hosts while preserving the original IP header for routing across the public internet
- C) A carrier WAN service that extends Ethernet frames over a metropolitan area network, offering point-to-point and multipoint connectivity to enterprise customers
- D) A Cisco VPN technology that uses NHRP and IPsec to create dynamic spoke-to-spoke tunnels in a hub-and-spoke architecture

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: GRE encapsulates a wide range of protocols and supports multicast and broadcast — which is why it is used to run OSPF and EIGRP across WAN links. GRE provides no encryption by design and must be combined with IPsec when security is required.
- B is incorrect: This describes IPsec in transport mode. IPsec transport mode encrypts the payload while preserving the original IP header. GRE does not involve encryption.
- C is incorrect: This describes Metro Ethernet, a carrier-provided WAN service. Metro Ethernet is a WAN connectivity product, not a tunneling protocol.
- D is incorrect: This describes DMVPN (Dynamic Multipoint VPN), which uses GRE as one component but is a distinct advanced technology. DMVPN adds NHRP for dynamic spoke-to-spoke tunnel creation — that functionality is not part of basic GRE.

---

## Question 3

A network engineer needs to trace the Layer 3 hop-by-hop path that packets follow through a WAN to verify GRE tunnel routing is working correctly. Which command is most appropriate?

- A) `traceroute`
- B) `ping`
- C) `netstat -ano`
- D) `nslookup`

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: `traceroute` reveals each router hop along the path by sending packets with incrementing TTL values. In a GRE tunnel scenario, it confirms whether traffic is traversing the tunnel or using a different path.
- B is incorrect: `ping` confirms end-to-end reachability and measures round-trip time but does not identify the intermediate hops or confirm the routing path taken.
- C is incorrect: `netstat -ano` lists active TCP/UDP connections and listening ports on a local host. It does not test routing paths.
- D is incorrect: `nslookup` resolves DNS names to IP addresses. It is unrelated to routing path analysis.

---

## Question 4

A network engineer configures a GRE tunnel between R1 and R2. After configuration, `show interface Tunnel0` on R1 shows the tunnel as `up/down`. What is the most likely cause?

- A) The tunnel source and destination IP addresses are transposed on R1
- B) R1 has no route to reach the IP address configured as the tunnel destination
- C) R1's physical WAN interface is administratively down
- D) The GRE tunnel mode is not set to `gre ip`

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Transposing source and destination would cause the tunnel on both ends to be misconfigured, but this would typically result in the tunnel failing to send traffic rather than specifically causing the `up/down` line protocol state. The `up/down` state specifically indicates a routing problem.
- B is correct: The GRE tunnel line protocol (second status) is `down` when the router has no route to the tunnel destination IP address. The router cannot forward GRE-encapsulated packets to the remote endpoint, so the line protocol fails. Fix: ensure a route to the tunnel destination exists in the routing table.
- C is incorrect: If the physical WAN interface is administratively down, the router has no connectivity to the WAN at all. This would likely cause the tunnel to show `down/down` rather than `up/down`, and would have been caught earlier when testing WAN reachability.
- D is incorrect: `tunnel mode gre ip` is the default mode for tunnel interfaces. If it were missing, Packet Tracer and most IOS versions still default to GRE. This would not specifically cause the `up/down` state.

---

## Question 5

Which Metro Ethernet service type connects multiple customer sites in a multipoint-to-multipoint topology where any site can communicate directly with any other site?

- A) E-Line
- B) E-Tree
- C) E-LAN
- D) E-Access

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: E-Line is a point-to-point Metro Ethernet service connecting exactly two customer sites. It is equivalent to a leased line using Ethernet interfaces.
- B is incorrect: E-Tree is a hub-and-spoke Metro Ethernet service. Spoke sites can communicate with the hub but not directly with other spokes.
- C is correct: E-LAN is the multipoint-to-multipoint Metro Ethernet service. All connected sites appear on the same Ethernet segment, enabling any-to-any communication without requiring traffic to traverse a hub.
- D is incorrect: E-Access is not a standard Metro Ethernet service type tested on the CCNA. The three testable service types are E-Line, E-LAN, and E-Tree.

---

## Question 6

An engineer needs to run OSPF between two remote sites over the internet. The engineer configures an IPsec site-to-site VPN between the two routers. OSPF neighbor relationships fail to form across the IPsec tunnel. What is the most likely reason?

- A) IPsec tunnels do not support multicast traffic by default, and OSPF uses multicast Hello packets
- B) OSPF requires the tunnel interface to have an IP address in the same subnet as the remote router's LAN
- C) IPsec transport mode must be changed to tunnel mode before OSPF can function
- D) The OSPF process IDs must match across the IPsec tunnel endpoints

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: OSPF uses multicast addresses (224.0.0.5 and 224.0.0.6) for Hello packets and LSA flooding. IPsec tunnels do not support multicast by default. This is why GRE is added on top of IPsec when dynamic routing protocols are needed — GRE supports multicast, and IPsec provides encryption.
- B is incorrect: OSPF tunnel interfaces do need an IP address, but that address should be in the tunnel subnet, not the LAN subnet. Misunderstanding this does not explain the OSPF failure over IPsec.
- C is incorrect: IPsec tunnel mode is the correct mode for site-to-site VPNs and would already be in use. Changing to transport mode would be incorrect and would not resolve the multicast issue.
- D is incorrect: OSPF process IDs are locally significant and do not need to match between routers. This is not a cause of OSPF neighbor failure.

---

## Question 7

In a site-to-site IPsec VPN, which mode encrypts the entire original IP packet and adds a new outer IP header pointing to the VPN endpoints?

- A) Transport mode
- B) Tunnel mode
- C) AH mode
- D) IKE phase 1

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Transport mode encrypts only the payload of the original IP packet while preserving the original IP header. It is used for host-to-host encryption, not site-to-site VPNs between routers.
- B is correct: Tunnel mode encrypts the entire original IP packet (header and payload) and encapsulates it inside a new outer IP packet with the VPN router addresses as source and destination. This hides the internal LAN IP addresses from the public internet.
- C is incorrect: AH mode is not an IPsec operational mode. AH (Authentication Header) is an IPsec protocol that provides integrity and authentication. The operational modes are Transport and Tunnel.
- D is incorrect: IKE Phase 1 is the first phase of IPsec negotiation where peers authenticate and establish a secure channel for key exchange. It is not a data encryption mode.

---

## Question 8

A network administrator needs to protect management sessions on a WAN router from plaintext credential capture. Which configuration directly addresses this threat?

- A) Configure SSH for terminal access and HTTPS for web management, disabling Telnet and HTTP
- B) Configure IPsec ESP tunnel mode between all WAN sites to encrypt inter-site traffic
- C) Enable passive-interface on all WAN-facing interfaces to prevent OSPF hello exposure
- D) Deploy a site-to-site GRE tunnel to encapsulate all management traffic

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: SSH and HTTPS encrypt the interactive management session in transit, preventing password capture by packet sniffers. Configure with `transport input ssh` on VTY lines and disable Telnet.
- B is incorrect: IPsec ESP encrypts data traffic between sites but does not protect local management sessions where an administrator uses Telnet to the router's VTY lines or HTTP to the web interface.
- C is incorrect: Passive interfaces control OSPF Hello behavior and have no relevance to management session security.
- D is incorrect: A GRE tunnel encapsulates routed traffic between sites but does not encrypt interactive management sessions conducted locally or over VTY lines.

---

## Question 9

Which of the following is NOT a function of IKE in an IPsec VPN deployment?

- A) Authenticating the identity of each VPN peer
- B) Negotiating and establishing security associations
- C) Encrypting the data payload of each IP packet
- D) Exchanging encryption keys using Diffie-Hellman

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect (IKE does perform this): IKE Phase 1 authenticates VPN peers using pre-shared keys, certificates, or other methods. Peer authentication is a core IKE function.
- B is incorrect (IKE does perform this): IKE negotiates IPsec security associations — the set of parameters (algorithms, keys, lifetime) governing how traffic is encrypted. This is the primary purpose of IKE.
- C is correct (IKE does NOT perform this): IKE is responsible for key exchange and security association setup. The actual encryption of data packets is performed by ESP (Encapsulating Security Payload), not IKE. IKE establishes the keys and parameters that ESP then uses.
- D is incorrect (IKE does perform this): IKE uses the Diffie-Hellman algorithm to securely derive shared encryption keys between peers without transmitting the keys in plaintext.

---

## Question 10

An engineer configures a GRE tunnel and wants to run OSPF across it. The OSPF network statement on R1 is `network 172.16.0.0 0.0.0.3 area 0` where 172.16.0.0/30 is the tunnel subnet. The same statement is on R2. After five minutes, `show ip ospf neighbor` on R1 shows no neighbors. The tunnel is up/up. Which is the most likely cause?

- A) The OSPF area IDs do not match — one router uses area 0 and the other uses area 1
- B) passive-interface is configured on Tunnel0 on one of the routers
- C) The GRE tunnel IP addresses are not in the same /30 subnet
- D) OSPF requires a separate network statement for the physical WAN interface

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: If area IDs mismatched, the neighbor relationship would partially form (reaching 2-Way) and then fail. A complete absence of neighbors more often points to hellos not being sent or received at all.
- B is correct: If `passive-interface Tunnel0` is configured, OSPF hello packets are suppressed on the tunnel interface. No hellos means no neighbor discovery. Check `show ip ospf interface brief` — if Tunnel0 shows as passive, remove it with `no passive-interface Tunnel0`.
- C is incorrect: If tunnel IP addresses are in different /30 subnets, OSPF would reject the neighbor due to subnet mask mismatch. This is a possible cause but the scenario states the same network statement is used on both routers, suggesting matching tunnel IPs.
- D is incorrect: OSPF does not need a network statement for the physical WAN interface to form a neighbor relationship across the tunnel. OSPF only needs to run on the tunnel interface subnet. Including the WAN interface in OSPF would advertise it unnecessarily.

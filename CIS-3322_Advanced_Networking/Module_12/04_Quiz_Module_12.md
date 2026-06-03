# Quiz: Module 12 — WAN Technologies and Remote Access

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

## Questions: 10 | Points: 10 (1 point each)

---

## Question 1

In an MPLS network, which device is responsible for removing (popping) the MPLS label from a packet as it exits the provider network and enters the customer site?

- A) P router (Label Switch Router)
- B) CE router (Customer Edge)
- C) Egress PE router (Label Edge Router)
- D) vSmart controller

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: P routers (LSRs) are the core label-switching routers in the MPLS provider network. They forward packets based on labels and perform label swapping but do not push or pop labels at the network boundary. Label push and pop operations happen at the edge.
- B is incorrect: The CE router is the customer-managed edge router that connects to the provider PE router. The CE router operates in normal IP routing mode and is not aware of MPLS labels. It receives packets after the label has already been removed by the PE.
- C is correct: The egress LER (Label Edge Router), also called the egress PE router, removes the MPLS label from the packet as it exits the provider MPLS network and returns to normal IP forwarding before delivering to the CE router. This is the "pop" operation.
- D is incorrect: vSmart is an SD-WAN control plane component, not an MPLS routing device. It distributes SD-WAN policy and routing information to vEdge routers and has no role in MPLS label operations.

---

## Question 2

An enterprise is deploying SD-WAN across 50 branch offices. A new branch office receives its vEdge router. Which SD-WAN component does the new vEdge contact first to authenticate and establish connectivity to the rest of the SD-WAN fabric?

- A) vManage
- B) vSmart
- C) vBond
- D) Another vEdge at the nearest branch

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: vManage is the management plane where administrators configure policies. While vEdge eventually communicates with vManage to download its configuration, it does not authenticate through vManage first. vManage requires the vEdge to already be authenticated before accepting its connection.
- B is incorrect: vSmart is the control plane that distributes routing and policy information to all vEdge routers. Before a vEdge can receive information from vSmart, it must first be authenticated and orchestrated. vBond performs that step.
- C is correct: vBond is the orchestration component specifically responsible for authenticating new WAN edge devices when they first connect to the SD-WAN fabric. vBond validates the vEdge's identity and then directs it to connect to the appropriate vManage and vSmart controllers. This is zero-touch provisioning — the branch router self-registers without manual intervention.
- D is incorrect: vEdge routers communicate with the controller plane (vBond, vSmart, vManage) not with each other for initial authentication. Peer vEdge devices form data plane connections after the control plane is established.

---

## Question 3

A network engineer needs to run OSPF between a headquarters router and a branch router across an IPsec site-to-site VPN. After configuring IPsec, OSPF neighbor relationships fail to form. What is the most likely reason, and what is the correct solution?

- A) OSPF area IDs do not match across the IPsec tunnel — change both to area 0
- B) IPsec does not support multicast by default — add a GRE tunnel over IPsec to carry OSPF Hello packets
- C) The IPsec security association must be renegotiated before OSPF can run — clear the IPsec SA
- D) OSPF requires a dedicated physical interface — a virtual IPsec tunnel interface cannot carry OSPF

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: OSPF area IDs are a valid concern but are not the root cause of the neighbor failure in this scenario. The more fundamental issue is that OSPF relies on multicast (224.0.0.5 and 224.0.0.6) for Hello packets and LSA flooding, and IPsec does not forward multicast traffic by default.
- B is correct: OSPF uses multicast addresses for neighbor discovery. IPsec tunnels do not support multicast by default — they can only carry unicast traffic. Adding a GRE tunnel provides a virtual point-to-point link that supports multicast, allowing OSPF Hello packets to traverse the WAN. IPsec then encrypts the GRE-encapsulated traffic. This combination — GRE over IPsec — is the standard solution for running dynamic routing protocols over an encrypted WAN.
- C is incorrect: Clearing the IPsec SA forces renegotiation, which might resolve a broken security association, but the fundamental barrier here is multicast support. Even with a functioning IPsec SA, OSPF Hellos will still fail without GRE.
- D is incorrect: OSPF runs on tunnel interfaces routinely in production. Virtual interfaces including GRE tunnels, loopbacks, and VLAN interfaces all support OSPF. The interface type is not the barrier.

---

## Question 4

Which IPsec protocol provides both encryption and authentication for VPN traffic, making it the standard choice for production site-to-site VPN deployments?

- A) IKE (Internet Key Exchange)
- B) AH (Authentication Header)
- C) ESP (Encapsulating Security Payload)
- D) GRE (Generic Routing Encapsulation)

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: IKE is the key negotiation and peer authentication protocol. It establishes the security association and exchanges encryption keys before any data is sent. IKE does not encrypt actual data packets — that is ESP's role.
- B is incorrect: AH provides data integrity and origin authentication but does not encrypt the payload. Traffic protected by AH alone is readable in plaintext. AH is insufficient for deployments requiring data confidentiality.
- C is correct: ESP (Encapsulating Security Payload) provides encryption of the data payload in addition to integrity verification and origin authentication. Because it provides confidentiality — making traffic unreadable to eavesdroppers — ESP is used in virtually all production VPN deployments. It is the correct choice whenever "encryption" appears in the requirements.
- D is incorrect: GRE is a tunneling protocol, not a security protocol. It provides encapsulation that supports multicast but offers no encryption, authentication, or integrity protection.

---

## Question 5

A network engineer configures a GRE tunnel and runs `show interface Tunnel0`. The output shows `Tunnel0 is up, line protocol is down`. What is the most likely cause?

- A) The `tunnel mode gre ip` command was not configured on the interface
- B) The tunnel source and destination addresses are reversed on one of the routers
- C) The router does not have a route to the IP address specified as the tunnel destination
- D) OSPF must be configured before the GRE tunnel line protocol can come up

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `tunnel mode gre ip` is the default tunnel mode in Cisco IOS. If it were missing, the tunnel would still attempt to use GRE. The `up/down` state is specifically a routing condition, not a mode configuration condition.
- B is incorrect: Reversed source and destination would cause both ends to be misconfigured, but this would more likely result in GRE packets being sent to wrong endpoints and traffic failing, rather than specifically causing the `up/down` state. The `up/down` state has a well-known specific cause related to routing.
- C is correct: The GRE tunnel line protocol (`line protocol is down`) specifically indicates that the router has no route to the tunnel destination IP address. The router cannot forward GRE-encapsulated packets to the remote endpoint without a routing entry pointing to that destination. The fix is to add a static route or ensure a dynamic routing protocol covers the path to the tunnel destination. Once a route exists, the line protocol comes up.
- D is incorrect: OSPF is typically run over the tunnel, not as a prerequisite for the tunnel to function. The GRE tunnel must come up first before OSPF can use it. OSPF has no relationship to the tunnel's line protocol state.

---

## Question 6

Which SD-WAN component is responsible for distributing routing information and security policies to all WAN edge routers across the enterprise?

- A) vBond
- B) vManage
- C) vEdge
- D) vSmart

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect: vBond handles orchestration and initial device authentication. It connects new vEdge devices to the fabric but does not distribute routing or security policies to running vEdge routers.
- B is incorrect: vManage is the management plane where administrators define policies and configuration. Policies are created in vManage but distributed by vSmart. vManage is the configuration interface; vSmart is the distribution mechanism.
- C is incorrect: vEdge is the WAN edge router that receives and enforces policies. It is the target of policy distribution, not the distributor.
- D is correct: vSmart is the SD-WAN control plane. It receives policies from vManage and distributes routing information and security policies to all vEdge routers in the fabric. vSmart acts similarly to a route reflector in BGP — it centralizes control plane information and pushes it to all edge devices.

---

## Question 7

An enterprise currently uses a full-mesh MPLS WAN connecting 20 branch offices. The company wants to reduce WAN costs by replacing MPLS with broadband internet connections at each branch while maintaining encrypted connectivity and the ability to route voice traffic preferentially to the highest-quality link. Which WAN solution best meets these requirements?

- A) Point-to-point GRE tunnels between each branch and headquarters
- B) SD-WAN with application-aware routing across multiple broadband transport links
- C) Remote access VPN with AnyConnect client at each branch
- D) Static site-to-site IPsec VPN tunnels between headquarters and each branch

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: GRE tunnels provide a point-to-point overlay but do not provide application-aware routing, performance monitoring across multiple paths, or centralized management. Scaling 20 separate GRE tunnels with manual configuration also does not reduce operational complexity.
- B is correct: SD-WAN directly addresses all stated requirements. It operates over any transport type including broadband internet, provides application-aware routing that steers voice traffic to the best-performing path based on real-time jitter and latency measurements, includes built-in encryption, and centrally manages all sites from vManage. This replaces MPLS with a cost-effective, intelligent alternative.
- C is incorrect: Remote access VPN is designed for individual user connections, not site-to-site branch connectivity. It does not provide always-on network-to-network tunnels or application-aware path selection.
- D is incorrect: Static site-to-site IPsec VPNs provide encryption but do not offer application-aware routing or automatic path selection between multiple links. Manual management of 20 static VPN tunnels does not reduce operational complexity and cannot optimize voice traffic quality.

---

## Question 8

A network engineer configures the following on a Cisco router:

```text
interface Dialer1
  ip address negotiated
  encapsulation ppp
  ppp chap hostname user@isp.com
  ppp chap password 0 secret123
  dialer pool 1

interface GigabitEthernet0/0
  no ip address
  pppoe enable
  pppoe-client dial-pool-number 1
```

What technology is being configured, and what is the purpose of the `ip address negotiated` command?

- A) GRE tunnel — `ip address negotiated` tells the router to use the tunnel source IP
- B) PPPoE client — `ip address negotiated` tells the router to accept an IP address assigned by the ISP via PPP IPCP
- C) SD-WAN vEdge — `ip address negotiated` enables zero-touch provisioning with vBond
- D) Dynamic NAT — `ip address negotiated` maps inside addresses to the ISP-assigned pool

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: GRE tunnel configuration uses `tunnel source` and `tunnel destination` commands, not `ip address negotiated`. The presence of `encapsulation ppp`, `ppp chap`, and `pppoe-client` clearly indicates PPPoE, not GRE.
- B is correct: This configuration is a Cisco IOS PPPoE client. The Dialer interface represents the PPP session. `ip address negotiated` instructs the router to accept an IP address dynamically assigned by the ISP's access concentrator during PPP IPCP (IP Control Protocol) negotiation, rather than using a statically configured address. The physical Gi0/0 has `no ip address` because it just carries PPPoE frames.
- C is incorrect: SD-WAN vEdge configuration does not use Dialer interfaces, PPP encapsulation, or CHAP authentication. Zero-touch provisioning in SD-WAN involves the vEdge device connecting to vBond automatically, not configuring dial interfaces.
- D is incorrect: Dynamic NAT uses `ip nat inside source list ... pool` commands. It does not involve Dialer interfaces or PPP authentication.

---

## Question 9

Which statement correctly describes the difference between IPsec Transport mode and IPsec Tunnel mode?

- A) Transport mode encrypts only the IP header; Tunnel mode encrypts only the data payload
- B) Transport mode encrypts the payload and preserves the original IP header; Tunnel mode encrypts the entire original IP packet and adds a new outer IP header
- C) Transport mode is used for site-to-site VPNs between routers; Tunnel mode is used for host-to-host encryption
- D) Transport mode uses AH for authentication; Tunnel mode uses ESP for encryption

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: IPsec does not encrypt only the IP header in any mode — that would not protect data. Transport mode encrypts the payload while preserving the original IP header. This is reversed from what option A describes.
- B is correct: In Transport mode, only the data payload is encrypted. The original IP source and destination remain visible in the header. In Tunnel mode, the entire original IP packet (header and payload) is encrypted and encapsulated inside a new outer IP packet that points to the VPN endpoints. Tunnel mode hides the original source and destination from the public internet.
- C is incorrect: This is backwards. Tunnel mode is used for site-to-site VPNs because it hides internal LAN IP addresses. Transport mode is used for host-to-host encryption where preserving the original IP header is acceptable because both endpoints are the final communicating parties.
- D is incorrect: Both AH and ESP can operate in either Transport or Tunnel mode. The mode and the protocol are independent choices. AH in Tunnel mode encrypts the original header for integrity only (no payload encryption). ESP in Tunnel mode provides full encryption. The association of AH with Transport and ESP with Tunnel is not a fixed rule.

---

## Question 10

A network administrator reviews the WAN requirements for a new branch office located in a rural area. The requirements are: internet access for 15 users, ability to connect back to headquarters securely, no availability of fiber or cable service, and the branch must be operational within 24 hours. Which combination of WAN technologies best meets all requirements?

- A) MPLS circuit with a dedicated PE router and SLA
- B) 4G LTE broadband with a site-to-site IPsec VPN to headquarters
- C) DSL with PPPoE and a static GRE tunnel (no encryption)
- D) Metro Ethernet E-Line from the local carrier

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: MPLS provisioning typically takes weeks to months, not 24 hours. It also requires fiber or copper carrier infrastructure at the site. Both the availability and deployment timeline requirements are violated.
- B is correct: 4G LTE is available in rural areas where fiber and cable are not, can be activated with a cellular data plan almost immediately (within hours), and supports standard routing and IPsec for secure site-to-site VPN connectivity to headquarters. All four requirements are met: internet access, HQ connectivity, available technology in rural areas, and 24-hour deployment.
- C is incorrect: DSL requires existing telephone copper infrastructure and a CO (central office) within approximately 5.5 km. Rural areas frequently lack both the physical infrastructure and the distance requirement for reliable DSL. Additionally, GRE without encryption does not meet the secure connectivity requirement.
- D is incorrect: Metro Ethernet E-Line is a carrier-provided point-to-point service requiring the carrier to provision the service from the nearest point of presence to the branch location. Like MPLS, this cannot be deployed within 24 hours, and availability in rural areas is limited.

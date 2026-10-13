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

---

## Question 11

An enterprise network engineer configures a GRE tunnel between R1 (WAN IP 203.0.113.1) and R2 (WAN IP 203.0.113.5). After configuration, `show interface Tunnel0` on R1 shows `Tunnel0 is up, line protocol is up`. However, pings from R1's tunnel IP to R2's tunnel IP fail. What is the most likely cause?

- A) GRE does not support ICMP — use TCP to test tunnel connectivity
- B) The tunnel IP addresses on R1 and R2 are in different subnets
- C) The tunnel source and destination physical WAN addresses are misconfigured
- D) OSPF must be running over the tunnel before IP connectivity is available

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: GRE is a Layer 3 encapsulation protocol and supports any Layer 3 protocol including ICMP. Pinging the tunnel IP is the standard method to verify GRE tunnel connectivity.
- B is correct: The tunnel line protocol being `up` confirms routing to the tunnel destination exists (the physical WAN path works). If pings between tunnel IPs fail, the most likely cause is mismatched tunnel IP subnets — for example, R1 configured with 172.16.0.1/30 and R2 configured with 172.16.0.5/30 (different /30 blocks). The tunnel endpoints must share the same subnet for layer 3 communication across the tunnel to succeed.
- C is incorrect: If the physical WAN addresses were misconfigured, the tunnel line protocol would be `down` because the router would have no route to the tunnel destination. The scenario states the line protocol is `up`, ruling out this cause.
- D is incorrect: OSPF and other routing protocols run over an already-functioning GRE tunnel. The tunnel must be functional first. GRE tunnel IP-to-IP reachability is independent of OSPF.

---

## Question 12

In the Cisco SD-WAN architecture, which component manages the data plane and forwards traffic between enterprise sites?

- A) vManage
- B) vSmart
- C) vBond
- D) vEdge

**Correct Answer:** D

**Distractor Analysis:**

- A is incorrect: vManage is the management plane — the NMS (network management system) where administrators configure policies, monitor the fabric, and manage devices. It does not forward data traffic.
- B is incorrect: vSmart is the control plane. It distributes routing tables, policies, and keys to vEdge devices but does not itself forward user data traffic.
- C is incorrect: vBond is the orchestration plane responsible for initial device authentication and directing new devices to the controllers. It has no role in data forwarding.
- D is correct: vEdge (also called WAN Edge) devices form the data plane. They are physical or virtual routers deployed at each branch, data center, and campus site. vEdge devices establish encrypted BFD-monitored tunnels with each other and forward actual enterprise traffic based on policies received from vSmart.

---

## Question 13

Which statement correctly describes MPLS VPN operation from a customer perspective?

- A) The customer must configure MPLS labels manually on their CE router
- B) The customer sees the MPLS network as a fully meshed IP VPN — any CE can communicate with any other CE without knowing about the provider's label infrastructure
- C) MPLS VPNs require static routing between all CE routers because MPLS does not support dynamic routing protocols
- D) The customer must assign a VPN ID to each CE router's interface facing the provider

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Customers do not configure MPLS labels. Label operations (push, swap, pop) are entirely managed by the provider's PE and P routers. The CE router uses standard IP routing and has no knowledge of MPLS.
- B is correct: From the customer's perspective, MPLS VPN appears as a fully meshed private IP network. Each CE router can communicate with every other CE router in the VPN as if they were directly connected. The provider's MPLS label switching infrastructure is transparent to the customer. This is the key business value of MPLS — any-to-any connectivity without the customer managing individual tunnels.
- C is incorrect: MPLS VPN fully supports dynamic routing protocols (OSPF, EIGRP, BGP) between CE and PE routers. In fact, BGP (specifically IBGP with VPNv4) is used internally within the provider network to distribute VPN routes between PE routers.
- D is incorrect: VPN configuration in MPLS is done entirely on the provider's PE routers using VRF (Virtual Routing and Forwarding) instances. Customers configure their CE routers with normal IP routing — no VPN IDs are required from the customer side.

---

## Question 14

A network engineer needs to configure IPsec between two Cisco routers. Phase 1 (IKE) completes successfully, but Phase 2 (IPsec SA) fails to establish. What is the most likely cause?

- A) The pre-shared key used in Phase 1 does not match
- B) The transform set (encryption and hashing algorithm) parameters do not match between the peers
- C) The IPsec access list is missing from one of the routers
- D) The `crypto map` is not applied to the correct interface

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: Pre-shared key mismatch causes Phase 1 to fail, not Phase 2. If Phase 1 completed successfully, the pre-shared key matched and ISAKMP SA was established.
- B is correct: Phase 2 (IPsec SA) uses a transform set to negotiate the encryption algorithm (AES, 3DES), hashing (SHA, MD5), and mode (tunnel or transport). If the transform set parameters do not match on both peers, Phase 2 negotiation fails. Both routers must have identical transform set configurations (same algorithms, same mode).
- C is incorrect: A missing crypto ACL would prevent interesting traffic from triggering the VPN, but the Phase 2 SA itself could still negotiate if one side initiates. However, the most direct cause of Phase 2 failure is a transform set mismatch.
- D is incorrect: If the crypto map were not applied to the interface, the VPN would never trigger at all — Phase 1 would not even initiate. Since Phase 1 succeeded, the crypto map is correctly applied.

---

## Question 15

A remote worker uses Cisco AnyConnect to connect to the corporate VPN. After connecting successfully, the worker can access corporate resources but cannot browse the internet. What VPN configuration is causing this behavior?

- A) The AnyConnect client version is incompatible with the ASA's SSL certificate
- B) Full-tunnel VPN is configured — all traffic including internet-bound traffic is routed through the corporate VPN
- C) Split-tunnel VPN is configured — internet traffic is being blocked by the corporate firewall
- D) The VPN session has a bandwidth limit that restricts simultaneous corporate and internet access

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: A version incompatibility would cause the connection to fail entirely, not selectively block internet while allowing corporate access. The scenario states the connection was successful.
- B is correct: Full-tunnel VPN routes all client traffic — both corporate and internet — through the VPN gateway. Internet traffic is sent through the VPN to the corporate network, then out the corporate internet connection. If the corporate firewall blocks or does not route the worker's internet traffic, the worker loses internet access while connected. The solution is to configure split-tunnel, which only routes corporate-destined traffic through the VPN and sends internet traffic directly from the client.
- C is incorrect: Split-tunnel does the opposite of what is described. With split-tunnel, only traffic destined for corporate networks goes through the VPN — internet traffic goes directly from the client's local network. Split-tunnel would allow internet access, not block it.
- D is incorrect: VPN sessions do not have per-user bandwidth configurations that would selectively restrict internet while allowing corporate access. Bandwidth policies on VPN gateways are aggregate, not selective by traffic type.

---

## Question 16

What is the purpose of the `keepalive` command on a GRE tunnel interface?

- A) It sends periodic OSPF Hello packets to verify that the remote OSPF neighbor is still active
- B) It sends periodic probe packets through the GRE tunnel to detect if the tunnel path has failed, allowing faster reconvergence
- C) It negotiates the GRE tunnel's MTU value with the remote endpoint to prevent fragmentation
- D) It enables CHAP authentication on the GRE tunnel to verify the remote router's identity

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: OSPF Hello packets are separate from GRE tunnel keepalives. OSPF manages its own neighbor liveliness independently. Tunnel keepalives and OSPF Hellos are parallel but separate mechanisms.
- B is correct: GRE tunnel keepalives are probe packets sent periodically by the local router into the tunnel. If the remote end does not respond within the keepalive timeout, the local router marks the tunnel interface as down, allowing routing protocols to reconverge to an alternative path. Without keepalives, a GRE tunnel stays `up/up` even if the underlying path has failed — routing protocols would continue using it and traffic would blackhole.
- C is incorrect: GRE tunnel MTU is controlled separately using `ip mtu` and `ip tcp adjust-mss` on the tunnel interface. Keepalives do not negotiate MTU values.
- D is incorrect: GRE does not support CHAP authentication. GRE is a simple encapsulation protocol with no built-in authentication mechanism. Authentication for GRE tunnels is provided by the underlying IPsec layer when GRE over IPsec is configured.

---

## Question 17

An organization has four branch offices, each with a 100 Mbps broadband internet connection. They want to use SD-WAN to connect all branches to a central data center. They also want to add a 4G LTE backup link at each branch for resiliency. Which SD-WAN capability handles automatic failover from broadband to LTE when the primary link degrades?

- A) vSmart policy distribution
- B) Application-aware routing with BFD (Bidirectional Forwarding Detection)
- C) vBond zero-touch provisioning
- D) OSPF redistribution from CE routers

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: vSmart distributes the policies that define how application-aware routing works, but the detection of link failure and the actual failover decision are made by the vEdge router using BFD probes on each transport link.
- B is correct: SD-WAN vEdge routers continuously monitor each WAN path (broadband and LTE) using BFD probes, measuring latency, jitter, and packet loss. Application-aware routing policies define thresholds for each application class. When broadband metrics exceed the configured thresholds or the link fails BFD probes, the vEdge automatically switches the affected application traffic to the LTE link. This is real-time, policy-driven path selection.
- C is incorrect: vBond zero-touch provisioning handles initial device onboarding — connecting new vEdge devices to the fabric for the first time. It has no role in runtime link failover decisions.
- D is incorrect: OSPF redistribution is not part of SD-WAN link failover. SD-WAN uses its own OMP (Overlay Management Protocol) for route distribution, not OSPF from CE routers.

---

## Question 18

Which command on a Cisco router verifies whether a GRE tunnel is currently forwarding packets and shows the tunnel source and destination addresses?

- A) `show ip route`
- B) `show crypto ipsec sa`
- C) `show interface Tunnel0`
- D) `show ip ospf neighbor`

**Correct Answer:** C

**Distractor Analysis:**

- A is incorrect: `show ip route` shows the routing table, which may include a route pointing to the tunnel interface. However, it does not show tunnel-specific details like source/destination addresses, tunnel state, or packet counters.
- B is incorrect: `show crypto ipsec sa` shows IPsec security association details — encrypted packets sent/received and SA parameters. It applies to IPsec, not plain GRE. If the tunnel is GRE without IPsec, this command returns no relevant output.
- C is correct: `show interface Tunnel0` displays the tunnel's operational state (up/up or up/down), the tunnel source and destination IP addresses, the tunnel protocol, and input/output packet counters. This is the primary command for verifying GRE tunnel operation and is always the first command to run when troubleshooting tunnel issues.
- D is incorrect: `show ip ospf neighbor` shows OSPF adjacency state with neighboring routers. It confirms whether OSPF is functioning over the tunnel but does not show tunnel configuration details or verify GRE operation directly.

---

## Question 19

A network engineer configures IPsec using IKEv2 instead of IKEv1. Which statement correctly describes an advantage of IKEv2 over IKEv1?

- A) IKEv2 requires only one exchange to establish the IKE SA, reducing the number of messages compared to IKEv1
- B) IKEv2 uses AH instead of ESP, providing stronger encryption than IKEv1
- C) IKEv2 eliminates the need for a pre-shared key or certificate — identity is verified by IP address alone
- D) IKEv2 is Cisco-proprietary and only works between two Cisco devices

**Correct Answer:** A

**Distractor Analysis:**

- A is correct: IKEv2 reduces the number of messages required to establish an IKE SA from 6 (IKEv1 Main Mode) or 3 (IKEv1 Aggressive Mode) to 4 messages in a single exchange. IKEv2 also supports MOBIKE (mobility), EAP authentication for remote access, and built-in NAT traversal. It is more efficient and more resilient than IKEv1.
- B is incorrect: IKEv2 is a key exchange protocol — it does not change whether AH or ESP is used for actual data encryption. Both IKEv1 and IKEv2 can negotiate IPsec with ESP or AH in Phase 2. The choice of AH vs ESP is independent of the IKE version.
- C is incorrect: IKEv2, like IKEv1, requires strong peer authentication using pre-shared keys, digital certificates, or EAP. Authentication by IP address alone (used in older IKEv1 "identity protection" mode) is not a feature of IKEv2.
- D is incorrect: IKEv2 is standardized by the IETF (RFC 7296) and is vendor-neutral. It operates between Cisco and non-Cisco devices, including Juniper, Palo Alto, pfSense, and Linux strongSwan implementations.

---

## Question 20

A company uses MPLS L3VPN to connect 10 branch offices. The network architect wants to add a new branch. What configuration is required on the customer's CE router to integrate into the existing MPLS VPN?

- A) Configure MPLS labels and an LDP (Label Distribution Protocol) neighbor on the CE router
- B) Configure normal IP routing (static or dynamic routing protocol) between the CE and the provider's PE router — no MPLS configuration is required on the CE
- C) Configure a GRE tunnel from the CE router to every other CE router in the VPN
- D) Configure a VRF on the CE router matching the VRF name used on the PE router

**Correct Answer:** B

**Distractor Analysis:**

- A is incorrect: CE routers do not participate in MPLS label exchange. LDP and label operations are entirely within the provider network (between PE and P routers). The CE router operates in standard IP mode with no knowledge of MPLS.
- B is correct: A new CE router in an MPLS L3VPN only needs standard IP connectivity and routing configuration to the provider's PE router. This is typically a routing protocol (OSPF, EIGRP, or BGP peering with the PE) or static routes. The provider handles all MPLS-related configuration on their PE router, including VRF assignment. This is a key advantage of MPLS — minimal customer configuration.
- C is incorrect: MPLS VPN provides any-to-any connectivity without the customer configuring point-to-point tunnels. Configuring GRE tunnels to each branch would negate the operational simplicity that MPLS provides and is not how MPLS L3VPN works.
- D is incorrect: VRF configuration is done on the provider's PE router, not the customer's CE router. The CE router has no VRF context — it connects to the PE using a normal routed interface.

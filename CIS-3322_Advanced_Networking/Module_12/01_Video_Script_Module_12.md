# Video Script: Module 12 — WAN Technologies and Remote Access

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: Cisco CCNA 200-301

---

## Introduction (0:00–1:30)

Welcome back to CIS-3322 Advanced Networking. I'm Professor Nash. Module 12 covers WAN technologies and remote access — the connectivity fabric that ties together geographically distributed networks.

[SHOW SLIDE: "Module 12 — WAN Technologies and Remote Access"]

Modern organizations operate across campuses, cities, and continents. The WAN layer connects these separated sites. Today's WAN landscape spans a wide range of technologies from legacy MPLS circuits to cutting-edge SD-WAN, from site-to-site VPN tunnels to broadband last-mile connectivity.

By the end of this module you will be able to:

- Describe MPLS architecture and label-switched paths

- Explain SD-WAN components, benefits, and use cases

- Distinguish site-to-site VPN from remote access VPN

- Configure and verify GRE tunnels on Cisco IOS

- Explain PPPoE operation and configuration

- Identify broadband access technologies and their characteristics

[PAUSE — 3 seconds]

Let's start with MPLS — the technology that powers many enterprise WAN backbones today.

---

## Section 1: MPLS — Multiprotocol Label Switching (1:30–5:00)

[SHOW SLIDE: "MPLS — Label-Switched Paths"]

MPLS is a WAN forwarding mechanism used by service providers to carry customer traffic across their networks. Instead of making IP routing decisions at every hop, MPLS assigns short fixed-length labels to packets at the network edge and forwards them through pre-established paths called Label-Switched Paths, or LSPs.

Key MPLS roles:

**Label Edge Router (LER)**: the router at the edge of the MPLS network that assigns labels to incoming packets (ingress) or removes them (egress). Also called the Provider Edge router — PE.

**Label Switch Router (LSR)**: the core routers that forward packets based solely on the label without examining the IP header. Also called Provider routers — P routers.

**MPLS labels**: 32-bit identifiers inserted between the Layer 2 header and the IP header — the "shim layer" between Layer 2 and Layer 3.

[SHOW TOPOLOGY: Customer site A → CE router → PE ingress → P core routers → PE egress → CE router → Customer site B]

The customer's edge router is the CE — Customer Edge. The customer manages only CE routers. The provider manages PE and P routers. From the customer's perspective, all sites appear directly connected through the MPLS cloud.

[SHOW SLIDE: "MPLS Benefits"]

MPLS provides:

- Traffic engineering: provider controls forwarding paths, avoiding congestion

- QoS support: labels carry traffic class markings for voice and video priority

- Any-to-any connectivity: sites communicate without requiring full-mesh VPNs

- VRF isolation: customer networks are logically separated even over shared provider infrastructure

For the CCNA, understand MPLS at the conceptual level: label forwarding, PE/P/CE roles, and service provider ownership boundaries.

[PAUSE — 3 seconds]

---

## Section 2: SD-WAN (5:00–9:00)

[SHOW SLIDE: "SD-WAN — Software-Defined WAN"]

SD-WAN applies software-defined networking principles to enterprise WAN management. The core idea: separate the control plane from the data plane so that WAN policies are managed centrally rather than configured on individual routers.

In a traditional WAN, every router is configured independently. Adding a new site requires provisioning circuits, manually configuring routers at the new site and at headquarters, and manually adjusting routing and security policies across the network. This is slow and error-prone.

In an SD-WAN, a controller pushes policy to all edge devices automatically. A new site comes online, the edge device connects to the controller, downloads its policy, and is operational — often without a technician touching the configuration directly.

[SHOW SLIDE: "Cisco SD-WAN — Four Components"]

Cisco's SD-WAN solution (formerly Viptela) has four key components:

**vManage**: the centralized management console. Network administrators configure all policies, routing rules, QoS, and security settings here.

**vSmart**: the control plane controller. Distributes routing information and policies to all WAN edge routers.

**vBond**: the orchestration component. Authenticates new WAN edge devices when they first connect and establishes their initial connection to vManage and vSmart.

**vEdge (WAN Edge)**: the physical or virtual router at each customer site. Receives policy from vSmart and enforces it on all traffic.

[SHOW SLIDE: "SD-WAN Key Features"]

SD-WAN advantages over traditional WAN:

- **Transport independence**: simultaneously uses MPLS, broadband internet, and LTE. Fails over automatically between transports.

- **Application-aware routing**: measures jitter, latency, and loss on each path. Routes voice over the best path, bulk data over the cheapest path.

- **Zero-touch provisioning**: new sites self-configure when the vEdge device connects to vBond. No manual CLI configuration required.

- **Centralized visibility**: one dashboard for all sites, all links, all applications.

[PAUSE — 3 seconds]

---

## Section 3: VPN Types — Site-to-Site and Remote Access (9:00–12:30)

[SHOW SLIDE: "VPN Types Compared"]

A VPN creates a secure encrypted connection through an untrusted network. Two deployment models:

**Site-to-Site VPN**: permanently connects two networks. Endpoints are routers or firewalls at each site. The VPN is always on. Users access remote resources transparently — they do not launch VPN software. Used for branch-to-headquarters connectivity.

**Remote Access VPN**: connects individual users to the corporate network on demand. Each user runs client software. The tunnel is created when the user connects and torn down when they disconnect. Used for remote workers and travelers.

[SHOW SLIDE: "IPsec Protocol Overview"]

IPsec is the security framework used for site-to-site VPNs:

**IKE (Internet Key Exchange)**: negotiates the security association between peers. Authenticates both sides and exchanges encryption keys. IKEv2 is the current standard.

**AH (Authentication Header)**: provides integrity and origin authentication. Does NOT provide encryption. Payload is readable. AH alone is rarely used in production.

**ESP (Encapsulating Security Payload)**: provides integrity, authentication, AND encryption. This is what makes traffic unreadable to eavesdroppers. ESP is used in virtually all production VPNs.

[SHOW SLIDE: "IPsec Modes"]

- Transport mode: encrypts only the data payload. Original IP header preserved. Host-to-host use case.
- Tunnel mode: encrypts the entire original packet and adds a new outer IP header. Site-to-site VPN use case.

The CCNA exam consistently tests AH vs ESP. Remember: AH = authentication only, no confidentiality. ESP = authentication plus confidentiality.

---

## Section 4: GRE Tunnels (12:30–15:30)

[SHOW SLIDE: "GRE — Why It Exists"]

GRE (Generic Routing Encapsulation) solves a specific problem: IPsec tunnels do not support multicast traffic by default. OSPF and EIGRP rely on multicast Hello packets to form neighbor relationships. If you want to run a dynamic routing protocol across an encrypted WAN, you need GRE on top of IPsec.

GRE creates a virtual point-to-point link between two routers. OSPF sees the GRE tunnel as a directly connected link and forms a neighbor relationship across it. IPsec can then encrypt the GRE-encapsulated traffic.

[SHOW SLIDE: "GRE Configuration"]

Configuration on R1 (WAN interface 203.0.113.1):

```text
R1(config)# interface Tunnel0
R1(config-if)# tunnel mode gre ip
R1(config-if)# tunnel source GigabitEthernet0/1
R1(config-if)# tunnel destination 203.0.114.2
R1(config-if)# ip address 172.16.0.1 255.255.255.252
R1(config-if)# no shutdown
```

Configuration on R2 (WAN interface 203.0.114.2):

```text
R2(config)# interface Tunnel0
R2(config-if)# tunnel mode gre ip
R2(config-if)# tunnel source GigabitEthernet0/1
R2(config-if)# tunnel destination 203.0.113.1
R2(config-if)# ip address 172.16.0.2 255.255.255.252
R2(config-if)# no shutdown
```

Note that `tunnel source` references the interface name. The router pulls the current IP from that interface automatically.

[SHOW SLIDE: "GRE Troubleshooting"]

The tunnel is `up/up` when the router has a route to the tunnel destination. The tunnel is `up/down` when that route is missing. Always verify:

```text
Router# show interface Tunnel0
Router# show ip route
```

If the route to the tunnel destination disappears (due to a WAN failure), the tunnel line protocol drops.

---

## Section 5: PPPoE (15:30–17:30)

[SHOW SLIDE: "PPPoE — DSL Authentication Protocol"]

PPPoE (Point-to-Point Protocol over Ethernet) is used by ISPs to authenticate DSL subscribers. It runs PPP over Ethernet, allowing each subscriber session to be individually authenticated and billed.

PPPoE operation has two phases:

**Discovery**: the client broadcasts on Ethernet to discover PPPoE servers. The ISP's access concentrator responds. A session ID is established.

**Session**: PPP negotiates the connection, authenticates the user, and assigns an IP address.

[SHOW SLIDE: "Cisco PPPoE Client Configuration"]

On a Cisco router acting as a PPPoE client:

```text
Router(config)# interface Dialer1
Router(config-if)# ip address negotiated
Router(config-if)# encapsulation ppp
Router(config-if)# ppp authentication chap callin
Router(config-if)# ppp chap hostname subscriber@isp.net
Router(config-if)# ppp chap password 0 secretpassword
Router(config-if)# dialer pool 1
Router(config-if)# exit

Router(config)# interface GigabitEthernet0/0
Router(config-if)# pppoe enable
Router(config-if)# pppoe-client dial-pool-number 1
Router(config-if)# no ip address
```

The Dialer interface is a virtual interface that represents the PPP session. The physical Ethernet interface just transports the PPPoE frames.

---

## Section 6: Broadband Technologies (17:30–20:00)

[SHOW SLIDE: "Broadband Access — Technology Overview"]

Broadband technologies connect branch offices and remote workers to the corporate network. Key technologies:

**DSL**: runs over telephone copper wire. ADSL is asymmetric — faster download than upload. Distance-limited (typically under 5.5 km from the exchange). PPPoE is the authentication method.

**Cable**: uses the cable television DOCSIS infrastructure. Higher speeds than DSL. Shared medium — performance degrades in peak hours when many subscribers are active.

**Fiber (FTTH/FTTX)**: fiber optic to the home or building. Symmetrical speeds, low latency. Gold standard for branch connectivity but not universally available.

**4G LTE / 5G cellular**: wireless broadband. Used for branch backup links, remote temporary sites, and mobile workers. 5G brings very high speeds in covered areas.

[SHOW SLIDE: "Broadband in WAN Design"]

Broadband is rarely used as a standalone WAN solution for enterprise. It is combined with:

- Site-to-site IPsec VPN for encryption and network extension
- SD-WAN for intelligent path selection across multiple broadband links
- Cellular backup for failover when the primary broadband link fails

The cost advantage over MPLS is significant. A 100 Mbps fiber broadband connection with SD-WAN and IPsec can replace a much more expensive dedicated MPLS circuit for many branch applications.

[PAUSE — 3 seconds]

---

## Conclusion (20:00–22:00)

[SHOW SLIDE: "Module 12 Summary"]

Let's wrap up Module 12. Today you learned:

- MPLS uses label-switched paths with LER and LSR roles — PE and P routers in provider terms

- SD-WAN uses four components: vManage (management), vSmart (control plane), vBond (orchestration), vEdge (data plane)

- Site-to-site VPN is permanent network-to-network; remote access VPN is on-demand user-to-network

- AH provides authentication without encryption; ESP provides both

- GRE tunnels support multicast routing protocols over WAN using `tunnel mode gre ip`

- PPPoE provides ISP subscriber authentication for DSL using Dialer interfaces

- Broadband technologies (DSL, cable, fiber, LTE) each have distinct speed, cost, and availability trade-offs

[SHOW SLIDE: "CCNA Exam Focus Areas"]

For the CCNA exam: focus on SD-WAN component names, GRE tunnel configuration and the `up/down` troubleshooting scenario, VPN type distinctions, and AH vs ESP. These are the most consistently tested WAN topics.

Your lab this module builds a GRE tunnel, runs OSPF across it, and verifies connectivity. Thank you for joining me for Module 12. Take care.

---

*End of Module 12 Video Script*

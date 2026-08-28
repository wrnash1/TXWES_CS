# Reading Guide: Module 12 — Wide Area Networks

## Course: CIS-3321 Network Administration

**Certification Alignment:** CompTIA Network+ (N10-008)

---

## Overview

This reading guide supports Module 12 video lectures and prepares you for the Module 12 Quiz and the CompTIA Network+ N10-008 exam. WAN technologies appear throughout Domain 1 (Networking Concepts) and Domain 2 (Infrastructure). Focus especially on identifying the correct WAN technology for a given scenario — a frequent exam question type.

**Estimated Reading Time:** 60–75 minutes

---

## Part 1: WAN Fundamentals

### 1.1 WAN Terminology Reference

Understanding WAN requires a precise vocabulary. The following terms appear frequently on the Network+ exam.

| Term | Definition |
|---|---|
| CPE | Customer Premises Equipment — network gear at the customer site |
| Demarc | Demarcation point — boundary between carrier and customer responsibility |
| Local loop | Connection from customer demarc to carrier Central Office |
| Central Office (CO) | Carrier facility where local loops terminate |
| Last mile | Informal term for the local loop |
| CSU/DSU | Channel Service Unit / Data Service Unit — interface between T-carrier line and router |
| Latency | Time for data to travel source to destination |
| Jitter | Variation in latency; harmful to real-time applications |
| Bandwidth | Data capacity of a link (Kbps, Mbps, Gbps) |

### 1.2 Circuit-Switched vs. Packet-Switched

#### Circuit-Switched Networks

In circuit switching, a dedicated physical path is reserved for the entire duration of a connection. All capacity on that path is reserved even when no data is transmitting.

Characteristics:

- Guaranteed, consistent bandwidth
- Predictable performance
- Inefficient — idle circuits waste capacity
- Legacy technology (PSTN, ISDN)

Historical WAN example — ISDN (Integrated Services Digital Network):

- BRI (Basic Rate Interface): 2 × 64 Kbps B-channels + 1 × 16 Kbps D-channel = 128 Kbps usable data
- PRI (Primary Rate Interface): 23 × B-channels + 1 D-channel (T1 equivalent) in North America

#### Packet-Switched Networks

In packet switching, data is divided into packets that are routed independently through shared network infrastructure.

Characteristics:

- Efficient — bandwidth shared across users
- Variable latency possible (congestion, different paths)
- Dominant modern WAN model

---

## Part 2: Dedicated WAN Technologies

### 2.1 T-Carrier and E-Carrier Leased Lines

T-carrier lines use Time Division Multiplexing (TDM) to divide a digital circuit into 24 DS0 channels of 64 Kbps each.

| Line | Bandwidth | DS0 Channels |
|---|---|---|
| DS0 | 64 Kbps | 1 |
| T1 (DS1) | 1.544 Mbps | 24 |
| T3 (DS3) | 44.736 Mbps | 672 (28 × T1) |

European E-carrier equivalents:

- E1: 2.048 Mbps (32 channels)
- E3: 34.368 Mbps

A CSU/DSU is required to connect a router to a T-carrier line. The CSU terminates the carrier signal; the DSU converts it to a format the router can use.

### 2.2 SONET/SDH and Optical Carrier Lines

Synchronous Optical Network (SONET) in North America and Synchronous Digital Hierarchy (SDH) in Europe define optical carrier standards.

| OC Level | Bandwidth |
|---|---|
| OC-1 | 51.84 Mbps |
| OC-3 | 155.52 Mbps |
| OC-12 | 622.08 Mbps |
| OC-48 | 2.488 Gbps |
| OC-192 | 9.953 Gbps |
| OC-768 | 39.813 Gbps |

SONET uses a self-healing ring topology. If a link fails, traffic automatically reroutes in the opposite direction around the ring — recovery time under 50 ms.

### 2.3 MPLS — Multiprotocol Label Switching

#### MPLS Architecture and Label Forwarding

MPLS operates between Layer 2 and Layer 3 — sometimes called Layer 2.5. It inserts a label stack between the Layer 2 frame header and the Layer 3 IP header.

Key MPLS components:

- **Label Edge Router (LER) / Provider Edge (PE) router**: Adds labels at ingress, removes at egress.
- **Label Switch Router (LSR) / Provider (P) router**: Forwards based on label only — never examines IP header.
- **Label Switched Path (LSP)**: Predetermined path through the MPLS network for a traffic flow.
- **Forwarding Equivalence Class (FEC)**: A group of packets forwarded the same way (same label, same path).

Label operations:

- Push: Add a label (ingress PE)
- Swap: Replace label with new label (P router)
- Pop: Remove label (egress PE)

#### MPLS VPN (L3VPN)

MPLS Layer 3 VPN uses Virtual Routing and Forwarding (VRF) instances to separate customer routing tables on shared PE routers. Each customer has a dedicated VRF — routes are completely isolated from other customers.

The carrier uses BGP with VPN extensions (VPNv4/VPNv6 address families) to distribute customer routes between PE routers across the MPLS backbone.

#### MPLS QoS and Traffic Engineering

MPLS supports differentiated QoS through the EXP (Experimental) bits in the label header — 3 bits providing 8 classes of service.

MPLS-TE uses RSVP-TE or CR-LDP to establish LSPs along explicit paths, allowing operators to route around congestion and guarantee bandwidth for specific traffic types.

---

## Part 3: Metro and Broadband WAN

### 3.1 Metro Ethernet

Metro Ethernet Forum (MEF) service definitions:

| Service | Topology | Description |
|---|---|---|
| E-Line | Point-to-point | Single virtual connection between two sites |
| E-LAN | Multipoint-to-multipoint | All sites communicate with all others |
| E-Tree | Hub-and-spoke | Root communicates with all leaves; leaves isolated from each other |

Metro Ethernet uses Provider Bridging (802.1ad — Q-in-Q) or MPLS/VPLS to carry customer 802.1Q VLANs across the carrier network. The outer S-tag identifies the service; the inner C-tag identifies the customer VLAN.

### 3.2 Broadband Internet WAN Technologies

#### DSL Technologies

| Type | Max Download | Notes |
|---|---|---|
| ADSL | 8 Mbps | Asymmetric, legacy |
| ADSL2+ | 24 Mbps | Improved ADSL |
| VDSL2 | 100 Mbps | Short range — under 1 km |
| G.fast | 1 Gbps | Very short range — under 100 m |

DSL uses existing copper telephone infrastructure. A DSLAM (Digital Subscriber Line Access Multiplexer) at the CO aggregates multiple DSL connections.

#### Cable (DOCSIS)

- DOCSIS 3.0: 1 Gbps downstream / 200 Mbps upstream (channel bonding)
- DOCSIS 3.1: 10 Gbps downstream / 1–2 Gbps upstream
- Shared medium: bandwidth shared in the cable node neighborhood

#### Fiber to the Premises (FTTP/FTTH)

GPON (Gigabit Passive Optical Network) characteristics:

- 2.488 Gbps downstream / 1.244 Gbps upstream shared among up to 64 ONUs
- Passive splitters — no powered equipment between CO and customer
- Low latency, high reliability

---

## Part 4: Wireless and Satellite WAN

### 4.1 Cellular WAN Technologies

| Generation | Typical Speed | Latency | Notes |
|---|---|---|---|
| 4G LTE | 20–150 Mbps | 30–50 ms | Widely deployed WAN option |
| 4G LTE-A | Up to 300 Mbps | 15–30 ms | Carrier aggregation |
| 5G Sub-6 GHz | 100–400 Mbps | 10–30 ms | Broad coverage nationwide |
| 5G mmWave | 1–4 Gbps | Under 10 ms | Dense urban, limited range |

Cellular WAN hardware: LTE/5G routers with enterprise features — dual-SIM, failover, VPN, QoS.

### 4.2 Satellite WAN

#### Geostationary (GEO) Satellite

- Altitude: 35,786 km
- Round-trip latency: 600–700 ms (physics-limited)
- Throughput: 10–100 Mbps
- Not suitable for VoIP, interactive gaming, or real-time trading
- Suitable for remote monitoring, email, periodic data sync, backup

#### Low Earth Orbit (LEO) Satellite

- Altitude: 550–1,200 km
- Round-trip latency: 20–40 ms (Starlink typical)
- Throughput: 100–300 Mbps typical
- Near-global coverage including polar regions
- Use cases: Remote enterprise sites, maritime, aviation, rural broadband

---

## Part 5: SD-WAN

### 5.1 SD-WAN Architecture

SD-WAN decouples WAN management from the physical transport, using a centralized controller to manage all WAN edge devices.

Key components:

- **SD-WAN Controller/Orchestrator**: Centralized management plane. Pushes policies to all edge devices. Provides single-pane-of-glass visibility.
- **SD-WAN Edge Device (vCPE)**: Deployed at each branch. Connects to multiple WAN transports. Executes policies received from the controller.
- **WAN Transports**: Any combination of MPLS, broadband internet, 4G/5G, satellite.

### 5.2 SD-WAN Key Capabilities

Application-aware routing identifies applications using deep packet inspection (DPI) and routes based on policy:

- Real-time traffic (VoIP, video) routes via lowest-latency link
- SaaS traffic routes via direct internet breakout
- Sensitive data routes via MPLS or encrypted tunnel
- Bulk transfers use least-cost link

Dynamic path selection continuously monitors link quality (latency, jitter, packet loss) and steers traffic away from degraded links in real time — sub-second failover.

Zero-touch provisioning: New branch devices self-configure by contacting the cloud controller on first boot.

### 5.3 SD-WAN vs. Traditional WAN

| Factor | Traditional MPLS WAN | SD-WAN |
|---|---|---|
| Cost | High (dedicated circuits) | Lower (broadband + policy) |
| Flexibility | Low (long provisioning) | High (software-defined) |
| Cloud optimization | Poor (backhaul to DC) | Excellent (direct breakout) |
| Visibility | Limited | Rich per-app analytics |
| Management | Per-device CLI | Centralized dashboard |

---

## Part 6: WAN Optimization

### 6.1 WAN Optimization Techniques

#### Data Deduplication

Operates at the byte level. The optimizer builds a dictionary of data patterns seen across all traffic. When a pattern recurs, only a short reference token is sent instead of the full data. Particularly effective for file transfers and backups — may reduce data volume by 90–99%.

#### Compression

Standard algorithms (LZ77/LZ78) compress the WAN stream in real time. Effective for text-heavy protocols. Limited benefit for already-compressed or encrypted data.

#### Protocol Optimization

The optimizer proxies WAN-unfriendly protocols:

- SMB/CIFS: Predictive prefetching replaces chatty acknowledge cycles.
- Exchange MAPI: Local caching serves repeated email/attachment requests.
- HTTP: Web object caching reduces repeat WAN traversal.

#### TCP Optimization

On high-latency WAN links, TCP congestion control throttles throughput unnecessarily. WAN optimizers use large TCP window scaling, SACK improvements, and local TCP termination to maximize throughput.

#### QoS and Traffic Shaping

- Voice/video: Strict priority queue
- Business-critical applications: Guaranteed minimum bandwidth
- Bulk transfers: Best-effort, rate-limited during business hours

---

## Key Terms Glossary

- **ADSL**: Asymmetric DSL — download faster than upload.
- **Backhaul**: Routing WAN-bound traffic back to a central site before forwarding.
- **CO**: Central Office — carrier switching facility.
- **CSU/DSU**: Interface device for T-carrier lines.
- **DOCSIS**: Data Over Cable Service Interface Specification.
- **FEC**: Forwarding Equivalence Class — group of MPLS packets forwarded identically.
- **GPON**: Gigabit Passive Optical Network.
- **GEO**: Geostationary orbit satellite — approximately 36,000 km altitude, high latency.
- **Jitter**: Variation in packet delay — harmful to real-time applications.
- **LER**: Label Edge Router — adds/removes MPLS labels at network edge.
- **LEO**: Low Earth Orbit satellite — approximately 550–1200 km altitude, low latency.
- **Local loop**: Physical connection from customer to carrier CO.
- **LSP**: Label Switched Path — predetermined MPLS forwarding route.
- **LSR**: Label Switch Router — forwards based on label only.
- **MPLS**: Multiprotocol Label Switching.
- **OC-x**: Optical Carrier — SONET bandwidth designation.
- **SD-WAN**: Software-Defined WAN.
- **SONET**: Synchronous Optical Network.
- **T1**: 1.544 Mbps T-carrier leased line.
- **vCPE**: Virtual Customer Premises Equipment — SD-WAN edge device.
- **VRF**: Virtual Routing and Forwarding — MPLS customer isolation mechanism.

---

## Review Questions

1. What is the demarcation point and who is responsible for equipment on each side?

2. Compare circuit-switched and packet-switched WAN technologies. Which is more efficient for bursty data traffic and why?

3. A company has three offices and needs any-to-any connectivity with guaranteed performance for voice traffic. The company wants carrier-managed routing. Which WAN technology is most appropriate?

4. What is the difference between a T1 and a T3 leased line in terms of bandwidth and channel count?

5. Describe the MPLS label forwarding process: what happens at the ingress PE router, P routers, and egress PE router?

6. What is SD-WAN application-aware routing? Give two examples of how different applications might be routed differently.

7. A remote mining site needs WAN access but no terrestrial connectivity is available. What WAN option should be considered, and what latency limitations apply?

8. What is data deduplication in WAN optimization and why is it particularly effective for backup traffic?

9. What is zero-touch provisioning in SD-WAN and what operational benefit does it provide?

10. Compare GEO satellite and LEO satellite WAN in terms of latency and suitability for real-time applications.

---

## 9. Supplemental Resources

The following free resources extend Module 12 content on WAN technologies, MPLS, SD-WAN, and broadband connectivity.

**1. Professor Messer — WAN Technologies Free Videos (N10-008)**
URL: https://www.professormesser.com/network-plus/n10-008/n10-008-video/
Relevance: Professor Messer covers WAN types (T1, MPLS, Metro Ethernet, satellite, broadband), SD-WAN concepts, and WAN optimization in videos aligned to Network+ exam objectives.

**2. Cisco — MPLS Configuration Guide (Free)**
URL: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/mp_l3_vpns/configuration/xe-16-12/mp-l3-vpns-xe-16-12-book.html
Relevance: Cisco's free MPLS L3 VPN configuration guide covers PE/P/CE router roles, VRF configuration, label distribution, and MPLS VPN troubleshooting. Directly applicable to understanding the MPLS architecture described in this module.

**3. MEF Forum — Carrier Ethernet Education (Free)**
URL: https://www.mef.net/education/
Relevance: The Metro Ethernet Forum provides free educational resources on Carrier Ethernet service types (E-Line, E-LAN, E-Tree), MEF certification, and Carrier Ethernet 2.0 specifications. The definitive source for Metro Ethernet service definitions.

**4. Cisco SD-WAN (Viptela) Architecture Overview (Free)**
URL: https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/index.html
Relevance: Cisco's free SD-WAN product documentation and architecture overview covering the SD-WAN controller (vManage), edge device (vEdge), orchestration (vBond), and application-aware routing policies — directly mapped to the SD-WAN content in this module.

**5. FCC Broadband Speed Guide (Free)**
URL: https://www.fcc.gov/consumers/guides/broadband-speed-guide
Relevance: The FCC's free consumer broadband guide explains DSL, cable, fiber, satellite, and cellular broadband technologies including typical speeds and use cases — useful reference for comparing WAN access technology characteristics.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*

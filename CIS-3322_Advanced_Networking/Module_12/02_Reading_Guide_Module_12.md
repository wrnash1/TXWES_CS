# Reading Guide: Module 12 — WAN Technologies and Remote Access

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Cisco CCNA 200-301

---

## Overview

WAN technologies and remote access are tested on the CCNA 200-301 primarily at the conceptual and configuration levels. This module covers MPLS, SD-WAN, VPN types, GRE tunnels, PPPoE, and broadband access technologies. The CCNA expects you to identify correct WAN technology for a given scenario, configure and troubleshoot GRE tunnels, distinguish IPsec protocols, and describe SD-WAN component roles. This guide provides comparison tables, configuration references, troubleshooting flowcharts, and exam tips for every testable topic.

---

## 1. High-Yield Glossary

**MPLS (Multiprotocol Label Switching)**: A provider WAN technology that forwards packets using short fixed-length labels rather than IP routing decisions at each hop. Labels are inserted between Layer 2 and Layer 3 headers (the shim layer).

**LER (Label Edge Router)**: The router at the boundary of an MPLS network that pushes (assigns) or pops (removes) labels. Called the Provider Edge (PE) router in service provider terminology.

**LSR (Label Switch Router)**: Core MPLS routers that forward packets based on labels without examining the IP header. Called Provider (P) routers in service provider terminology.

**CE router (Customer Edge)**: The customer-managed router that connects to the provider's PE router. The customer owns and configures CE routers.

**LSP (Label-Switched Path)**: The predetermined path through an MPLS network along which packets with a specific label are forwarded.

**VRF (Virtual Routing and Forwarding)**: Logical isolation mechanism on PE routers that keeps each customer's routing table separate from other customers sharing the same provider infrastructure.

**SD-WAN (Software-Defined WAN)**: A WAN architecture that centralizes management and control of WAN edge devices using a software controller, enabling policy-based routing across multiple transport types.

**vManage**: The SD-WAN centralized management plane. Administrators configure all policies, routing, security, and site provisioning here.

**vSmart**: The SD-WAN control plane controller. Distributes routing and policy information to all WAN edge routers.

**vBond**: The SD-WAN orchestration component. Authenticates new WAN edge devices and establishes their initial connection to vManage and vSmart.

**vEdge**: The physical or virtual WAN edge router at each customer site that enforces policies from vSmart.

**Site-to-Site VPN**: A permanent, always-on encrypted tunnel connecting two networks. Configured on routers or firewalls. Users access remote resources transparently.

**Remote Access VPN**: An on-demand encrypted tunnel connecting individual users to the corporate network via client software such as Cisco AnyConnect.

**IKE (Internet Key Exchange)**: The IPsec protocol that negotiates security associations, authenticates VPN peers, and exchanges encryption keys before data transmission.

**AH (Authentication Header)**: An IPsec protocol providing data integrity and origin authentication without encryption. Payload is readable.

**ESP (Encapsulating Security Payload)**: An IPsec protocol providing encryption in addition to integrity and authentication. Used in virtually all production VPN deployments.

**GRE (Generic Routing Encapsulation)**: A tunneling protocol that encapsulates any Layer 3 protocol in IP. Supports multicast, enabling dynamic routing protocols over WAN. Provides no encryption.

**PPPoE (Point-to-Point Protocol over Ethernet)**: An authentication protocol used by ISPs to authenticate DSL subscribers. Runs PPP sessions over Ethernet infrastructure.

**ADSL (Asymmetric DSL)**: DSL technology with faster download than upload speeds. Runs over telephone copper wiring. Distance-limited to approximately 5.5 km from the exchange.

---

## 2. MPLS Architecture

### Router Role Comparison

| Role | Provider Term | Customer Term | Function                                         |
|------|---------------|---------------|--------------------------------------------------|
| LER  | PE (Provider Edge) | N/A      | Pushes labels inbound; pops labels outbound      |
| LSR  | P (Provider core)  | N/A      | Forwards packets by label; does not read IP      |
| CE   | N/A           | CE (Customer Edge) | Customer router; connects to PE router     |

### MPLS Label

The MPLS label is a 32-bit field composed of:

- 20-bit label value
- 3-bit Traffic Class (formerly EXP) field for QoS
- 1-bit Stack bit (S) — indicates the last label in a stack
- 8-bit TTL field

---

## 3. SD-WAN Architecture

### Component Roles

| Component | Plane        | Function                                                        |
|-----------|--------------|-----------------------------------------------------------------|
| vManage   | Management   | Central dashboard; configure policies, sites, routing, security |
| vSmart    | Control      | Distributes routing and policy to vEdge routers                 |
| vBond     | Orchestration| Authenticates new vEdge devices; connects them to vManage/vSmart|
| vEdge     | Data         | WAN edge router at each site; enforces distributed policies     |

### SD-WAN vs Traditional WAN

| Characteristic       | Traditional WAN            | SD-WAN                                    |
|----------------------|----------------------------|--------------------------------------------|
| Configuration method | Per-device CLI             | Centralized policy via vManage             |
| Transport types      | Single (MPLS or internet)  | Multiple simultaneous (MPLS + broadband + LTE) |
| New site provisioning| Manual per-device config   | Zero-touch provisioning via vBond          |
| Path selection       | Routing protocol metrics   | Application-aware, performance-based       |
| Visibility           | Per-device monitoring      | Centralized dashboard, all sites           |
| Encryption           | Optional, manual IPsec     | Built-in, policy-driven                    |

---

## 4. VPN Type Comparison

| Feature              | Site-to-Site VPN               | Remote Access VPN                     |
|----------------------|--------------------------------|---------------------------------------|
| Endpoints            | Router or firewall at each site| Individual user's device              |
| Duration             | Always-on permanent tunnel     | On-demand, per session                |
| User experience      | Transparent — no client needed | Requires VPN client software          |
| Common protocols     | IPsec IKEv2                    | SSL/TLS (AnyConnect), IPsec IKEv2     |
| Scale                | Network-to-network             | User-to-network                       |
| Use case             | Branch-to-HQ connectivity      | Remote workers, travelers             |

---

## 5. IPsec Protocol Comparison

| Protocol | Authentication | Integrity | Encryption | CCNA Key Word  |
|----------|----------------|-----------|------------|----------------|
| AH       | Yes            | Yes       | No         | No encryption  |
| ESP      | Yes            | Yes       | Yes        | Encryption     |

### IPsec Modes

| Mode      | What Is Encrypted         | New Outer Header | Use Case                    |
|-----------|---------------------------|------------------|-----------------------------|
| Transport | Payload only              | No               | Host-to-host encryption     |
| Tunnel    | Entire original IP packet | Yes              | Site-to-site VPN (routers)  |

---

## 6. GRE Tunnel Configuration Reference

### Configuration on Both Endpoints

```text
! Router R1 — WAN interface IP 203.0.113.1
R1(config)# interface Tunnel0
R1(config-if)# tunnel mode gre ip
R1(config-if)# tunnel source GigabitEthernet0/1
R1(config-if)# tunnel destination 203.0.114.2
R1(config-if)# ip address 172.16.0.1 255.255.255.252
R1(config-if)# no shutdown

! Router R2 — WAN interface IP 203.0.114.2
R2(config)# interface Tunnel0
R2(config-if)# tunnel mode gre ip
R2(config-if)# tunnel source GigabitEthernet0/1
R2(config-if)# tunnel destination 203.0.113.1
R2(config-if)# ip address 172.16.0.2 255.255.255.252
R2(config-if)# no shutdown
```

### Key Configuration Rules

- R1's `tunnel destination` must equal R2's WAN address and vice versa
- The tunnel interface IP address must be in a subnet different from all physical interfaces
- `tunnel mode gre ip` is the default and may be omitted but is explicit best practice
- `tunnel source` can specify an interface name (pulls the current IP automatically) or an explicit IP address

### GRE Verification Commands

| Command                        | Purpose                                                  |
|--------------------------------|----------------------------------------------------------|
| `show interface Tunnel0`       | Shows tunnel state (up/up or up/down) and encapsulation  |
| `show ip interface brief`      | Quick view of all interfaces including tunnel state      |
| `show ip route`                | Confirms routes learned via the tunnel interface         |
| `show ip ospf neighbor`        | Verifies OSPF neighbor formed via tunnel                 |
| `ping <tunnel-peer-ip>`        | Tests GRE tunnel forwarding between endpoints            |

---

## 7. GRE Troubleshooting Flowchart

```text
SYMPTOM: GRE Tunnel is up/down
         |
         v
Does a route exist to the tunnel destination IP?
  Run: show ip route <tunnel-destination-ip>
  NO  --> Add static route or ensure routing protocol covers the WAN subnet
  YES --> Continue
         |
         v
SYMPTOM: GRE Tunnel is up/up but OSPF neighbor not forming
         |
         v
Is passive-interface configured on Tunnel0?
  Run: show ip ospf interface Tunnel0
  YES --> Remove with: no passive-interface Tunnel0
  NO  --> Continue
         |
         v
Are OSPF network statements including the tunnel subnet?
  Example: network 172.16.0.0 0.0.0.3 area 0 must match tunnel IP /30
  NO  --> Add correct network statement
         |
         v
SYMPTOM: Tunnel is up/up, OSPF forms, but LAN-to-LAN traffic fails
         |
         v
Are routes to remote LANs in the routing table?
  Run: show ip route ospf
  NO  --> Verify OSPF network statements include both LAN subnets
         |
         v
Issue resolved
```

---

## 8. PPPoE Configuration Reference

### Cisco Router as PPPoE Client

```text
! Physical interface — no IP, just carries PPPoE frames
interface GigabitEthernet0/0
  no ip address
  pppoe enable
  pppoe-client dial-pool-number 1

! Virtual Dialer interface — carries the PPP session
interface Dialer1
  ip address negotiated
  encapsulation ppp
  ppp authentication chap callin
  ppp chap hostname subscriber@isp.com
  ppp chap password 0 mypassword
  dialer pool 1
  ip nat outside
```

### PPPoE Key Points

- The physical Ethernet interface gets `no ip address` — it carries only PPPoE frames
- The Dialer interface is the logical PPP session endpoint and receives the IP from the ISP
- `ip address negotiated` means the ISP assigns the IP via IPCP (PPP IP Control Protocol)
- `dialer pool 1` links the Dialer interface to the physical interface's PPPoE pool
- CHAP is the authentication method used by most ISPs

---

## 9. Broadband Technology Comparison

| Technology    | Medium            | Speed           | Symmetrical | Distance Limited | Authentication |
|---------------|-------------------|-----------------|-------------|------------------|----------------|
| ADSL          | Copper phone wire | Up to ~24 Mbps  | No          | Yes (~5.5 km)    | PPPoE          |
| VDSL          | Copper phone wire | Up to ~100 Mbps | Partial     | Yes (~1 km)      | PPPoE          |
| Cable (DOCSIS)| Coax cable TV     | Up to ~1 Gbps   | No          | No               | DHCP           |
| FTTH Fiber    | Optical fiber     | Up to 10 Gbps   | Yes         | No               | PPPoE or DHCP  |
| 4G LTE        | Cellular radio    | ~50–150 Mbps    | No          | Coverage-based   | SIM/carrier    |
| 5G NR         | Cellular radio    | Up to ~1 Gbps   | Partial     | Coverage-based   | SIM/carrier    |

---

## 10. WAN Technology Selection Guide

| Requirement                                | Recommended Technology                    |
|--------------------------------------------|-------------------------------------------|
| Maximum QoS and reliability, budget flexible | MPLS with SLA                            |
| Multiple transport types with central management | SD-WAN                              |
| Low-cost branch internet with encryption   | Broadband + Site-to-Site IPsec VPN        |
| Dynamic routing protocol over WAN          | GRE (or GRE over IPsec)                  |
| DSL ISP authentication                     | PPPoE                                     |
| Remote workers needing corporate access    | Remote Access VPN (AnyConnect)            |
| Branch backup link                         | 4G/5G LTE with automatic failover         |

---

## 11. CCNA Exam Tips

**Tip 1 — SD-WAN component names.** The CCNA tests all four names: vManage, vSmart, vBond, vEdge. Know each component's plane (management, control, orchestration, data) and function. vBond authenticates new devices — this is the most commonly missed detail.

**Tip 2 — GRE tunnel up/down.** A GRE tunnel in the `up/down` state means the line protocol is down. The specific cause is always the same: the router has no route to the tunnel destination IP address. The fix is always the same: add a route.

**Tip 3 — AH vs ESP.** AH = no encryption (authentication only). ESP = encryption plus authentication. The word "confidentiality" in any VPN question points to ESP. AH alone is never sufficient for regulated data.

**Tip 4 — IPsec modes.** Tunnel mode encrypts the entire original packet and adds a new IP header. This hides internal LAN addresses from the public internet. Transport mode only encrypts the payload and is used for host-to-host. Site-to-site VPNs always use Tunnel mode.

**Tip 5 — GRE multicast support.** GRE supports multicast. IPsec alone does not. OSPF uses multicast Hello packets (224.0.0.5 and 224.0.0.6). Therefore: GRE over IPsec = dynamic routing protocol over encrypted WAN. IPsec alone = encrypted WAN but no dynamic routing protocols.

**Tip 6 — PPPoE Dialer interface.** PPPoE uses a virtual Dialer interface to represent the PPP session. The physical Ethernet interface has no IP address. The Dialer interface receives `ip address negotiated` from the ISP. This architecture is a common point of confusion on the exam.

**Tip 7 — CE router ownership.** In MPLS, the customer owns and configures only CE routers. PE and P routers are provider-owned. If an exam question asks what the customer configures, the answer is always the CE router.

**Tip 8 — SD-WAN zero-touch provisioning.** New vEdge devices automatically discover and authenticate with vBond when connected to the internet. They then download their configuration from vManage. No manual CLI is required at the branch site.

---

## 12. Study Checklist

Work through each item before taking the Module 12 quiz.

- [ ] Name all four SD-WAN components and describe each component's plane and function
- [ ] Explain the difference between site-to-site and remote access VPN
- [ ] Identify AH vs ESP on the exam including what each provides and lacks
- [ ] Write GRE tunnel configuration from memory for two routers
- [ ] Explain what causes a GRE tunnel to show up/down and how to fix it
- [ ] Identify the PPPoE Dialer interface configuration pattern
- [ ] Compare at least four broadband technologies by speed, symmetry, and medium
- [ ] Complete the Module 12 Packet Tracer lab
- [ ] Post your Module 12 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: [Cisco Training](https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html)
- Free CCNA study notes and practice questions: [Professor Messer](https://www.professormesser.com)
- Cisco SD-WAN architecture overview: [Cisco SD-WAN](https://www.cisco.com/c/en/us/solutions/enterprise-networks/sd-wan/index.html)

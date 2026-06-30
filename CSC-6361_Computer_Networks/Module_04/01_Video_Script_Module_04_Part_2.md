# Video Script: Module 04 – Enterprise Security & Infrastructure Hardening
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 2 of 2 | Estimated Duration: 15–18 minutes
## Week 4: November 9–15, 2026 | Due: Sunday, November 15, 2026
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide
[SHOW SLIDE: "CSC-6361 — Module 04 Part 2: Layer 2 Security, BGP Hardening & Infrastructure Baseline | Texas Wesleyan University"]

---

### Section 1: Layer 2 Security — The Overlooked Attack Surface

[00:00 – 07:00]
[SHOW DIAGRAM: Layer 2 attack vectors — ARP spoofing, DHCP starvation, rogue DHCP, MAC flooding]

Layer 2 security is one of the most overlooked areas in enterprise networks. Because Layer 2 operates inside the trusted campus, many organizations assume it is inherently safe. It is not. A device that gains access to the physical or wireless network can execute Layer 2 attacks with devastating effect.

**DHCP Snooping:**
DHCP Snooping creates a binding table that maps MAC addresses to IP addresses, VLANs, and switch ports. Ports are classified as trusted (uplinks to DHCP server/other switches) or untrusted (access ports to end devices).

*Problem it solves:* A rogue DHCP server connected to an access port can hand out incorrect IP addresses and gateway information, performing a man-in-the-middle attack.

```
! Enable DHCP Snooping globally and per VLAN
ip dhcp snooping
ip dhcp snooping vlan 10,20,30

! Trust the uplink to the DHCP server (only)
interface GigabitEthernet0/1
 ip dhcp snooping trust

! All other ports are untrusted by default — rate limit DHCP on untrusted ports
interface range FastEthernet0/1-24
 ip dhcp snooping limit rate 15
```
Untrusted ports will drop DHCP Offer and DHCP Ack messages (server responses) — only the trusted uplink can deliver them.

**Dynamic ARP Inspection (DAI):**
DAI validates ARP packets against the DHCP Snooping binding table. If an ARP reply does not match a known MAC-to-IP binding, the packet is dropped.

*Problem it solves:* ARP spoofing / ARP poisoning — an attacker sends gratuitous ARP replies claiming to be the default gateway, redirecting all traffic through the attacker's device.

```
! Enable DAI on the VLAN (requires DHCP Snooping to be configured first)
ip arp inspection vlan 10,20,30

! Trust uplink interfaces (DAI trusts the same ports as DHCP Snooping)
interface GigabitEthernet0/1
 ip arp inspection trust
```

**IP Source Guard:**
IP Source Guard goes further than DAI — it filters IP packets (not just ARP) against the DHCP Snooping binding table. An untrusted port will only forward IP packets if the source IP and MAC match an entry in the binding table.

```
interface FastEthernet0/5
 ip verify source
```
This prevents an attacker from manually assigning a false IP address to their machine to bypass DHCP Snooping.

**Port Security:**
Port Security limits the number of MAC addresses allowed on an access port and takes action when a violation occurs:
```
interface FastEthernet0/3
 switchport mode access
 switchport port-security maximum 2
 switchport port-security mac-address sticky
 switchport port-security violation restrict
```
- **Maximum:** How many MAC addresses are allowed.
- **Sticky:** Dynamically learn MAC addresses and save them to running config.
- **Violation modes:** `protect` (drop, no log), `restrict` (drop + log + increment counter), `shutdown` (err-disable port + log). Enterprise standard: `restrict` for detection without taking down the port.

**802.1X — Port-Based Network Access Control:**
802.1X authenticates devices before they are granted network access. When a device connects to a switch port, it is placed in an **unauthorized state** (no network access) until it successfully authenticates via EAP (Extensible Authentication Protocol) to a RADIUS server (e.g., Cisco ISE).

Roles:
- **Supplicant:** The end device (PC, phone) — runs 802.1X client software.
- **Authenticator:** The network switch — enforces access based on RADIUS decision.
- **Authentication Server:** RADIUS server (ISE) — verifies credentials.

```
! Global 802.1X config
dot1x system-auth-control
aaa authentication dot1x default group radius

! Per-interface
interface FastEthernet0/5
 switchport mode access
 dot1x port-control auto
```

---

### Section 2: BGP Security — Route Filtering and Hardening

[07:00 – 12:00]
[SHOW DIAGRAM: BGP route filtering — inbound prefix list blocking unwanted advertisements]

BGP is the routing protocol of the internet and is increasingly used inside enterprises (especially with SD-WAN and cloud connectivity). Misconfigured or unprotected BGP can have catastrophic consequences — BGP route leaks have caused major internet outages.

**BGP Prefix Filtering — Inbound:**
Never accept unlimited routes from a BGP peer. Always apply an inbound prefix list:
```
! Define a prefix list — only accept specific routes from the ISP
ip prefix-list ISP-INBOUND seq 10 permit 0.0.0.0/0       ! Default route
ip prefix-list ISP-INBOUND seq 20 deny 0.0.0.0/0 le 32   ! Block everything else

router bgp 65001
 neighbor 203.0.113.1 prefix-list ISP-INBOUND in
```

**BGP Max-Prefix:**
Limit the number of prefixes accepted from a peer. If exceeded, the BGP session is torn down (or generates a warning):
```
router bgp 65001
 neighbor 203.0.113.1 maximum-prefix 750000 80
! 80% threshold triggers a warning; exceeding 750,000 prefixes tears down the session
```
This prevents a BGP route leak (where a peer accidentally advertises the full internet routing table as its own) from filling your routing table and crashing your router.

**BGP Route Filtering — Outbound:**
Never advertise more than your own prefixes to an ISP:
```
ip prefix-list MY-PREFIXES seq 10 permit 198.51.100.0/24
ip prefix-list MY-PREFIXES seq 20 deny 0.0.0.0/0 le 32

router bgp 65001
 neighbor 203.0.113.1 prefix-list MY-PREFIXES out
```

**BGP MD5 Authentication:**
Authenticate BGP sessions to prevent session hijacking:
```
router bgp 65001
 neighbor 203.0.113.1 password BGP-SECRET-KEY
```

> **Graduate Note:** BGP MD5 authentication has weaknesses (MD5 is no longer considered cryptographically strong). RFC 5925 defines the TCP Authentication Option (TCP-AO) as a stronger replacement. However, MD5 authentication remains the most widely deployed BGP security mechanism in production today.

---

### Section 3: Module 04 Lab Preview

[12:00 – 14:00]
[SHOW SLIDE: Module 04 Lab Topology]

In the Module 04 lab, you will:
1. Configure AAA with local authentication (TACACS+ server is simulated via local username database in Packet Tracer).
2. Configure named extended ACLs to permit only HTTP/HTTPS and SSH traffic, deny everything else, and log denied packets.
3. Enable DHCP Snooping, DAI, and Port Security on access switch ports.
4. Apply management plane hardening (SSH only, source IP restriction, session timeout).
5. Verify that attacks are blocked — attempt ARP spoofing and observe DAI dropping the packets.

**Assignments due: Sunday, November 15, 2026 at 11:59 PM CST**

---
*End of Part 2 — Module 04*

# Video Script: Module 04 – Enterprise Security & Infrastructure Hardening
## CSC-6361 Advanced Computer Networks | Graduate Level
## Part 1 of 2 | Estimated Duration: 15–18 minutes
## Week 4: November 9–15, 2026 | Due: Sunday, November 15, 2026
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide
[SHOW SLIDE: "CSC-6361 — Module 04 Part 1: Enterprise Security — AAA, ACLs & Control Plane Protection | Texas Wesleyan University | Graduate Level"]

---

### Section 1: The Security Mindset at CCNP Level

[00:00 – 02:00]
[SHOW SLIDE: Professor Nash on camera, security framework diagram visible]

Welcome to Module 04. This module shifts focus from network *design* to network *hardening*. Every device we have configured so far — routers, switches, VPN gateways — has a default configuration that is not secure. CCNP-level network engineers understand that configuring protocols correctly is only half the job. Securing the infrastructure against attack is the other half.

This module covers four critical security domains: **AAA (Authentication, Authorization, Accounting)**, **Access Control Lists**, **Control Plane and Management Plane protection**, and **Layer 2 security features**. These are all directly tested on the CCNP ENCOR exam.

---

### Section 2: AAA — Authentication, Authorization, Accounting

[02:00 – 06:30]
[SHOW DIAGRAM: AAA architecture — network device → TACACS+/RADIUS server → Active Directory]

[Alt-text: A diagram showing a network administrator's laptop attempting to SSH into a router. An arrow goes from the router to a box labeled "TACACS+ Server (Cisco ISE)" with text "Authentication Request." Another arrow returns labeled "Access Permitted." The TACACS+ server connects to a box labeled "Active Directory — Corp LDAP" showing backend identity source.]

**AAA Framework:**
- **Authentication:** Who are you? (Identity verification — username/password, certificate, MFA)
- **Authorization:** What can you do? (Command-level privileges, VPN access rights, network segment access)
- **Accounting:** What did you do? (Audit trail — log all commands executed, session duration, bytes transferred)

**TACACS+ vs. RADIUS:**

| Feature | TACACS+ | RADIUS |
|---|---|---|
| Transport | TCP (port 49) | UDP (port 1812/1813) |
| Encryption | Entire payload encrypted | Only password field encrypted |
| Granularity | Per-command authorization | Per-session authorization |
| Typical use | **Network device administration (Cisco preferred)** | Network access (VPN, Wi-Fi, 802.1X) |
| Separation | AAA functions fully separated | Authentication & Authorization combined |

> **CCNP Design Principle:** Use **TACACS+** for managing network devices (routers, switches, firewalls) because of its per-command authorization capability. Use **RADIUS** for end-user network access (802.1X, VPN authentication) because of its industry-wide support.

**AAA Configuration on IOS:**
```
! Enable AAA
aaa new-model

! Define the TACACS+ server
tacacs server ISE-PRIMARY
 address ipv4 10.10.10.100
 key MyTACACS+Key

! Create an AAA server group
aaa group server tacacs+ NETWORK-ADMIN
 server name ISE-PRIMARY

! Authentication: use TACACS+; fall back to local if server unavailable
aaa authentication login default group NETWORK-ADMIN local

! Authorization: command authorization at privilege level 15
aaa authorization commands 15 default group NETWORK-ADMIN local

! Accounting: log all EXEC sessions and commands
aaa accounting exec default start-stop group NETWORK-ADMIN
aaa accounting commands 15 default start-stop group NETWORK-ADMIN
```

**Local fallback — critical design decision:** Always configure `local` as the fallback in AAA statements. If the TACACS+ server is unreachable and you have no local fallback, you are locked out of your own device. This is a real-world production incident that has occurred at major organizations.

---

### Section 3: Access Control Lists at CCNP Depth

[06:30 – 11:00]
[SHOW DIAGRAM: ACL packet flow — router with inbound ACL on Gi0/0, outbound ACL on Gi0/1]

ACLs are a fundamental security tool, but CCNP-level knowledge requires understanding beyond just permit/deny:

**Standard vs. Extended ACLs:**
- **Standard ACLs** (numbered 1–99, 1300–1999): Match only on **source IP address**. Apply as close to the destination as possible.
- **Extended ACLs** (numbered 100–199, 2000–2699): Match on source IP, destination IP, protocol, port numbers. Apply as close to the **source** as possible.
- **Named ACLs:** Preferred — human-readable names, easier to edit, supports individual line deletion.

**Named Extended ACL — Enterprise Pattern:**
```
ip access-list extended ALLOW-WEB-ONLY
 ! Permit HTTP and HTTPS from the inside network to any destination
 permit tcp 192.168.10.0 0.0.0.255 any eq 80
 permit tcp 192.168.10.0 0.0.0.255 any eq 443
 ! Permit established return traffic (TCP with ACK or RST set)
 permit tcp any 192.168.10.0 0.0.0.255 established
 ! Permit ICMP for diagnostics
 permit icmp 192.168.10.0 0.0.0.255 any
 ! Implicit deny all — everything else is dropped
 deny ip any any log
```

**The `established` keyword:** This is CCNP-critical. `permit tcp any 192.168.10.0 0.0.0.255 established` allows return TCP traffic only if the ACK or RST bit is set — meaning the connection was *initiated* from inside. This is a stateless approximation of stateful inspection for TCP.

**ACL Placement Rules:**
- Extended ACLs: Apply **inbound** on the **source interface** to drop traffic before it traverses the network.
- Standard ACLs: Apply **outbound** on the interface closest to the **destination**.
- Never apply an ACL that blocks your SSH/management traffic without verifying you have console access.

**Reflexive ACLs and Dynamic ACLs:**
For true stateful traffic filtering on a router (without a firewall), **Reflexive ACLs** dynamically create temporary permit entries when an outbound session is initiated, allowing the return traffic. This is more secure than the `established` keyword because it tracks individual sessions.

---

### Section 4: Control Plane and Management Plane Protection

[11:00 – 14:30]
[SHOW DIAGRAM: Router planes — Data Plane, Control Plane, Management Plane — with traffic types]

A network device operates at three planes:
- **Data Plane:** Forwarding user traffic — fast-path, hardware-accelerated (ASICs).
- **Control Plane:** Running routing protocols, STP, ARP, CDP — software-processed by the CPU.
- **Management Plane:** SSH, SNMP, NETCONF, syslog — administrative access to the device.

> **Attack Insight:** Control plane and management plane traffic is processed by the router's CPU. A **Control Plane Policing (CoPP)** attack deliberately floods the router with control traffic (forged OSPF hello floods, ARP floods, ICMP floods) to exhaust CPU, causing routing protocol adjacencies to drop and effectively taking down the network.

**Control Plane Policing (CoPP):**
CoPP applies rate-limiting policies to traffic destined for the router's CPU:
```
! Class map: identify OSPF traffic
class-map match-all OSPF-TRAFFIC
 match protocol ospf

! Policy map: rate-limit OSPF to 1 Mbps
policy-map COPP-POLICY
 class OSPF-TRAFFIC
  police rate 1000000 bps conform-action transmit exceed-action drop

! Apply to the control plane
control-plane
 service-policy input COPP-POLICY
```

**Management Plane Protection — Hardening Checklist:**
```
! SSH only — disable Telnet
line vty 0 15
 transport input ssh
 login authentication default   ! Use AAA

! Set SSH version 2 (minimum)
ip ssh version 2

! Generate RSA keys (minimum 2048 bits)
crypto key generate rsa modulus 2048

! Disable HTTP server (use HTTPS only)
no ip http server
ip http secure-server

! Restrict management access to specific source IPs via ACL
ip access-list standard MGMT-ACCESS
 permit 10.99.99.0 0.0.0.255  ! Management VLAN only
 deny any log

line vty 0 15
 access-class MGMT-ACCESS in

! Set timeout for inactive sessions
line vty 0 15
 exec-timeout 10 0
```

---

### Section 5: Part 1 Summary

[14:30 – 16:00]
[SHOW SLIDE: Security hardening checklist]

In Part 1 you learned:
- **AAA** with TACACS+/RADIUS — authentication, authorization, accounting and fallback design.
- **ACLs** — standard vs. extended, placement rules, the `established` keyword, and reflexive ACLs.
- **Control Plane Policing (CoPP)** — protecting the router CPU from exhaustion attacks.
- **Management Plane Hardening** — SSH only, key length, session timeouts, source IP restrictions.

In Part 2 we cover **Layer 2 Security** (DHCP Snooping, Dynamic ARP Inspection, IP Source Guard, 802.1X), and **BGP Security** (prefix filtering, route maps, max-prefix limits).

---
*End of Part 1 — Module 04*

# Reading Guide: Module 13 — Network Security Fundamentals

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Overview

This reading guide supports Module 13: Network Security Fundamentals. Network security is one of the largest exam domains on the CCNA 200-301 exam, accounting for 15% of exam questions. This guide provides conceptual reinforcement, command reference tables, and configuration examples for AAA, RADIUS, TACACS+, port security, DHCP snooping, Dynamic ARP Inspection, and 802.1X.

---

## Section 1: AAA Framework

### Core Concepts

AAA — Authentication, Authorization, and Accounting — is the industry-standard framework for controlling access to network resources and devices. Cisco's implementation is activated with the `aaa new-model` global configuration command.

Without AAA, Cisco IOS uses a simple line-based password system (enable password, vty password). Once `aaa new-model` is entered, those line passwords are bypassed and AAA method lists govern all access.

### Method Lists

A method list defines the ordered sequence of authentication methods to try. If the first method fails due to a server timeout (not a bad password), the next method is tried. A bad password immediately returns a failure and does not try the next method.

Syntax:

```ios
aaa authentication login {default | list-name} method1 [method2...]
```

Common methods:

* `group radius` — use defined RADIUS servers
* `group tacacs+` — use defined TACACS+ servers
* `local` — use local username database
* `none` — no authentication required (avoid in production)

### RADIUS Configuration Reference

```ios
! Step 1: Enable AAA
aaa new-model

! Step 2: Define the RADIUS server
radius server SERVER-NAME
 address ipv4 10.0.0.10 auth-port 1812 acct-port 1813
 key SharedSecret123

! Step 3: Create method lists
aaa authentication login default group radius local
aaa authorization exec default group radius local
aaa accounting exec default start-stop group radius

! Step 4: Apply to VTY lines
line vty 0 15
 login authentication default
```

### TACACS+ Configuration Reference

```ios
! Step 1: Enable AAA
aaa new-model

! Step 2: Define the TACACS+ server
tacacs server SERVER-NAME
 address ipv4 10.0.0.20
 key SharedSecret456

! Step 3: Create method lists
aaa authentication login default group tacacs+ local
aaa authorization exec default group tacacs+ local
aaa authorization commands 15 default group tacacs+ local
aaa accounting exec default start-stop group tacacs+
aaa accounting commands 15 default start-stop group tacacs+
```

The `aaa authorization commands 15` command is a TACACS+-exclusive feature. It requires the AAA server to authorize each privilege-level 15 command before execution. RADIUS cannot do this.

### AAA Protocol Comparison Table

| Attribute | RADIUS | TACACS+ |
|---|---|---|
| RFC/Standard | RFC 2865, 2866 | Cisco proprietary |
| Transport | UDP | TCP |
| Auth port | 1812 | 49 |
| Acct port | 1813 | 49 |
| Encryption scope | Password field only | Entire payload |
| AuthN + AuthZ | Combined | Separated |
| Command authorization | Not supported | Supported |
| Best use case | Network access (Wi-Fi, VPN) | Device administration |
| Multi-vendor support | Excellent | Limited (Cisco focus) |

---

## Section 2: Port Security

### Conceptual Foundation

Port security is a switchport feature that limits the number of MAC addresses allowed on an interface. It protects against:

* **MAC flooding** — Attackers send frames with thousands of spoofed source MACs, filling the CAM table and forcing the switch to flood all frames (turning it into a hub).
* **Unauthorized device access** — Prevents unmanaged devices such as personal laptops or rogue APs from connecting.

Port security is only valid on access ports, not trunk ports. Attempting to enable it on a trunk port results in an error.

### Violation Mode Comparison

| Mode | Drop frames? | Log/Trap? | Port state | Use case |
|---|---|---|---|---|
| Protect | Yes | No | Up | Silent blocking; low visibility |
| Restrict | Yes | Yes (syslog + SNMP) | Up | Balanced; recommended |
| Shutdown | Yes | Yes | Err-disabled | Maximum security |

### Port Security Configuration Reference

```ios
! Minimal configuration (shutdown violation, max 1 MAC)
interface gigabitethernet 0/1
 switchport mode access
 switchport port-security

! Full sticky configuration
interface gigabitethernet 0/1
 switchport mode access
 switchport access vlan 20
 switchport port-security
 switchport port-security maximum 3
 switchport port-security mac-address sticky
 switchport port-security violation restrict

! Manually add a specific MAC address
interface gigabitethernet 0/2
 switchport port-security mac-address 00AA.BBCC.DD01
```

### Verification Commands

```ios
! Summary of all secure ports
show port-security

! Detail for a specific interface
show port-security interface gigabitethernet 0/1

! All secure MAC addresses in the table
show port-security address

! Check if port is in err-disabled state
show interfaces gigabitethernet 0/1 status

! View err-disable recovery settings
show errdisable recovery
```

### Err-Disable Recovery

When a port enters err-disabled state due to a port-security violation, it does not recover automatically unless configured to do so.

```ios
! Automatic recovery
errdisable recovery cause psecure-violation
errdisable recovery interval 300

! Manual recovery (shutdown then no shutdown)
interface gigabitethernet 0/1
 shutdown
 no shutdown
```

---

## Section 3: DHCP Snooping

### The Rogue DHCP Attack

In an unsecured switched environment, any device can run a DHCP server. An attacker's rogue DHCP server can respond to client DISCOVER messages faster than the legitimate server and assign:

* Its own IP as the default gateway (traffic redirection / man-in-the-middle)
* Its own IP as the DNS server (DNS poisoning)
* Incorrect subnet masks or lease times

DHCP snooping defeats this attack by enforcing which ports are allowed to send DHCP server messages.

### Trusted vs. Untrusted Ports

| Port type | Allowed DHCP messages | Typical connection |
|---|---|---|
| Trusted | DISCOVER, OFFER, REQUEST, ACK, NAK | Uplinks, real DHCP servers |
| Untrusted | DISCOVER, REQUEST only | End-user access ports |

If a DHCP OFFER or ACK arrives on an untrusted port, the switch drops the packet silently.

### The Binding Table

The DHCP snooping binding table records:

* Client MAC address
* Assigned IP address
* VLAN
* Interface
* Lease duration

This table can persist across reboots if written to NVRAM:

```ios
ip dhcp snooping database flash:dhcp-snooping.db
```

### DHCP Snooping Configuration Reference

```ios
! Enable globally and per VLAN
ip dhcp snooping
ip dhcp snooping vlan 10,20,30,40

! Disable Option 82 insertion
no ip dhcp snooping information option

! Trust the uplink port
interface gigabitethernet 0/48
 ip dhcp snooping trust

! Rate-limit DHCP on access ports (protect against starvation)
interface range gigabitethernet 0/1 - 47
 ip dhcp snooping limit rate 10

! Optional: persist binding table to flash
ip dhcp snooping database flash:dhcp-binding.db
```

### DHCP Snooping Verification Commands

```ios
show ip dhcp snooping
show ip dhcp snooping binding
show ip dhcp snooping statistics
show ip dhcp snooping database
```

---

## Section 4: Dynamic ARP Inspection

### ARP Poisoning Background

ARP operates without authentication. Any host can send a gratuitous ARP reply claiming any IP-to-MAC mapping. An attacker exploits this to:

1. Send a gratuitous ARP claiming their MAC owns the default gateway IP.
2. Victim hosts update their ARP cache with the attacker's MAC.
3. All traffic destined for the gateway is sent to the attacker (man-in-the-middle).

### DAI Operation

DAI validates ARP packets on untrusted ports by comparing the sender's IP-MAC pair against the DHCP snooping binding table. If the binding is valid, the packet is forwarded. If not, it is dropped.

Key dependencies:

* DHCP snooping must be enabled and the binding table populated before DAI can validate dynamic hosts.
* Static hosts with no DHCP binding must be covered with ARP ACLs.

### DAI Configuration Reference

```ios
! Enable DAI per VLAN
ip arp inspection vlan 10,20,30

! Trust the uplink (same logic as DHCP snooping)
interface gigabitethernet 0/48
 ip arp inspection trust

! Rate-limit ARP on access ports
interface range gigabitethernet 0/1 - 47
 ip arp inspection limit rate 100

! ARP ACL for static IP hosts
arp access-list SERVERS
 permit ip host 10.0.0.1 mac host 0050.56AB.0001
 permit ip host 10.0.0.2 mac host 0050.56AB.0002

ip arp inspection filter SERVERS vlan 10
```

### DAI Verification Commands

```ios
show ip arp inspection
show ip arp inspection vlan 10
show ip arp inspection statistics
show ip arp inspection interfaces
```

### DHCP Snooping and DAI Dependency Flow

```text
DHCP Snooping enabled on VLAN
         |
         v
Binding table built (MAC -> IP -> VLAN -> port)
         |
         v
DAI validates ARP packets against binding table
         |
         v
ARP poisoning attacks are dropped at the port
```

---

## Section 5: 802.1X Port-Based Access Control

### Authentication Flow

1. Device connects to switch port — port is in unauthorized state, only EAP traffic allowed.
2. Switch sends EAP-Request/Identity to the supplicant.
3. Supplicant responds with EAP-Response/Identity (username).
4. Switch relays identity to RADIUS server via RADIUS Access-Request.
5. RADIUS server challenges the supplicant using the configured EAP method.
6. Supplicant responds with credentials.
7. RADIUS server sends Access-Accept or Access-Reject.
8. Switch opens port (authorized state) or keeps it closed (unauthorized state).

### Port Control Modes

| Mode | Behavior |
|---|---|
| `force-authorized` | Port always authorized; bypasses 802.1X. Default state. |
| `force-unauthorized` | Port always unauthorized; no access permitted. |
| `auto` | 802.1X authentication required. Port starts unauthorized. |

### 802.1X Configuration Reference

```ios
! Global prerequisites
aaa new-model
radius server RADIUS-SRV
 address ipv4 10.0.0.50 auth-port 1812 acct-port 1813
 key RadiusKey789
aaa authentication dot1x default group radius
aaa authorization network default group radius
dot1x system-auth-control

! Per-interface 802.1X
interface gigabitethernet 0/5
 switchport mode access
 switchport access vlan 30
 authentication port-control auto
 dot1x pae authenticator

! Allow voice VLAN without 802.1X
interface gigabitethernet 0/5
 authentication host-mode multi-domain
 dot1x pae authenticator
```

### 802.1X Verification Commands

```ios
show dot1x all
show dot1x interface gigabitethernet 0/5 detail
show authentication sessions
show authentication sessions interface gigabitethernet 0/5 detail
```

---

## Section 6: Integrated Security Command Reference

### Master Command Quick-Reference

| Feature | Key Command | Purpose |
|---|---|---|
| AAA | `aaa new-model` | Enable AAA globally |
| RADIUS | `radius server NAME` | Define RADIUS server |
| TACACS+ | `tacacs server NAME` | Define TACACS+ server |
| Port Security | `switchport port-security` | Enable port security |
| Port Security | `switchport port-security mac-address sticky` | Enable sticky MAC learning |
| DHCP Snooping | `ip dhcp snooping` | Enable globally |
| DHCP Snooping | `ip dhcp snooping vlan X` | Enable per VLAN |
| DHCP Snooping | `ip dhcp snooping trust` | Trust an uplink port |
| DAI | `ip arp inspection vlan X` | Enable DAI per VLAN |
| DAI | `ip arp inspection trust` | Trust an uplink port |
| 802.1X | `dot1x system-auth-control` | Enable 802.1X globally |
| 802.1X | `authentication port-control auto` | Require auth on port |

---

## Section 7: Key Terms Glossary

* **AAA** — Authentication, Authorization, and Accounting framework
* **RADIUS** — Remote Authentication Dial-In User Service; UDP-based AAA protocol
* **TACACS+** — Terminal Access Controller Access-Control System Plus; TCP-based, full-packet-encrypted AAA protocol
* **Port Security** — Layer 2 feature limiting MAC addresses on a switch port
* **Sticky MAC** — Dynamically learned MAC addresses saved to running-config
* **Err-disabled** — Switch port state indicating a policy violation; port passes no traffic
* **DHCP Snooping** — Layer 2 feature dropping DHCP server messages on untrusted ports
* **Binding Table** — DHCP snooping record of MAC-to-IP-to-port-to-VLAN mappings
* **DAI** — Dynamic ARP Inspection; validates ARP packets against the binding table
* **802.1X** — IEEE standard for port-based network access control
* **Supplicant** — End device requesting network access in 802.1X
* **Authenticator** — Switch or AP enforcing 802.1X access control
* **EAP** — Extensible Authentication Protocol; framework used by 802.1X
* **PEAP** — Protected EAP; server-side certificate only, tunnels client credentials
* **EAP-TLS** — Certificate-based EAP; most secure; requires mutual certificates
* **Cisco ISE** — Identity Services Engine; Cisco's enterprise RADIUS/policy server

---

## CCNA Exam Tips — Module 13

* RADIUS combines authentication and authorization; TACACS+ separates them. This distinction appears repeatedly on the exam.
* TACACS+ uses TCP port 49 and encrypts the entire packet. RADIUS uses UDP and encrypts only the password.
* The default port-security violation mode is **shutdown**. Know all three modes and their behaviors.
* DHCP snooping must be enabled before DAI can function. DAI depends on the snooping binding table.
* The `no ip dhcp snooping information option` command is commonly needed and appears in lab scenarios.
* 802.1X has three roles: supplicant, authenticator, and authentication server. Know which device plays which role.
* `dot1x system-auth-control` is required globally; `authentication port-control auto` is required per interface.

---

## Study Checkpoint Questions

1. What two ports does RADIUS use and for what purpose?
2. Which AAA protocol supports command-level authorization and why?
3. What is the difference between sticky and dynamic MAC address learning?
4. What happens when a DHCP OFFER arrives on an untrusted DHCP snooping port?
5. What must be configured before DAI can validate ARP for DHCP clients?
6. In 802.1X, what is the role of the authenticator and which device typically fills this role?

Answers are found in the module video and this reading guide. Bring questions to the next synchronous session.

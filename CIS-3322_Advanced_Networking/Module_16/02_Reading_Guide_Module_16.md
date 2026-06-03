# Reading Guide: Module 16 — CCNA 200-301 Exam Preparation and Capstone

## Course: CIS-3322 Advanced Networking

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Cisco CCNA 200-301

---

## Overview

This reading guide is your comprehensive review reference for the CCNA 200-301 exam. It synthesizes the highest-frequency testable facts from all six exam domains, provides quick-reference tables, and includes an exam strategy checklist. Use this guide as your primary study document in the final week before your exam.

---

## Section 1: Exam Domain Weights

| Domain | Title | Weight |
|---|---|---|
| 1.0 | Network Fundamentals | 20% |
| 2.0 | Network Access | 20% |
| 3.0 | IP Connectivity | 25% |
| 4.0 | IP Services | 10% |
| 5.0 | Security Fundamentals | 15% |
| 6.0 | Automation and Programmability | 15% |
| **Total** | | **105%** |

Note: Totals may exceed 100% due to Cisco's published rounding. Domain 3.0 is the largest and warrants proportionally more study time.

---

## Section 2: Domain 1 — Network Fundamentals

### OSI Model Quick Reference

| Layer | Number | Name | PDU | Key Protocols/Devices |
|---|---|---|---|---|
| Application | 7 | Application | Data | HTTP, HTTPS, FTP, DNS, SNMP, DHCP |
| Presentation | 6 | Presentation | Data | SSL/TLS, JPEG, MPEG |
| Session | 5 | Session | Data | NetBIOS, RPC |
| Transport | 4 | Transport | Segment | TCP, UDP |
| Network | 3 | Network | Packet | IP, ICMP, OSPF, routers |
| Data Link | 2 | Data Link | Frame | Ethernet, 802.11, switches, bridges |
| Physical | 1 | Physical | Bit | Cables, hubs, repeaters, NICs |

### IPv4 Subnetting Reference

| CIDR | Subnet Mask | Hosts per Subnet | Subnets from /24 |
|---|---|---|---|
| /24 | 255.255.255.0 | 254 | 1 |
| /25 | 255.255.255.128 | 126 | 2 |
| /26 | 255.255.255.192 | 62 | 4 |
| /27 | 255.255.255.224 | 30 | 8 |
| /28 | 255.255.255.240 | 14 | 16 |
| /29 | 255.255.255.248 | 6 | 32 |
| /30 | 255.255.255.252 | 2 | 64 |

### IPv6 Address Type Reference

| Type | Prefix | Scope | Example |
|---|---|---|---|
| Global Unicast | 2000::/3 | Internet-routable | 2001:db8::1 |
| Link-Local | FE80::/10 | Single link only | FE80::1 |
| Unique Local | FC00::/7 | Organization-private | FD00::1 |
| Multicast | FF00::/8 | Group delivery | FF02::1 (all nodes) |
| Loopback | ::1/128 | Local host | ::1 |

### TCP vs. UDP

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Reliability | Guaranteed delivery | Best-effort |
| Flow control | Yes (windowing) | No |
| Error recovery | Yes (retransmission) | No |
| Overhead | Higher | Lower |
| Use cases | HTTP, FTP, SSH, Telnet | DNS, DHCP, SNMP, VoIP, video |

---

## Section 3: Domain 2 — Network Access

### VLAN and Trunking Commands

```ios
! Create VLAN
vlan 10
 name SALES

! Assign access port
interface gigabitethernet 0/1
 switchport mode access
 switchport access vlan 10

! Configure trunk port
interface gigabitethernet 0/24
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 10,20,30
 switchport trunk native vlan 999

! Verify
show vlan brief
show interfaces trunk
show interfaces gigabitethernet 0/1 switchport
```

### STP Port States

| State | Duration | MAC Learning? | Frames Forwarded? |
|---|---|---|---|
| Blocking | Up to 20 sec | No | No |
| Listening | 15 sec | No | No |
| Learning | 15 sec | Yes | No |
| Forwarding | Until topology change | Yes | Yes |
| Disabled | Indefinite | No | No |

### RSTP Port Roles

| Role | Description |
|---|---|
| Root Port | Best path toward the root bridge |
| Designated Port | Best path away from root on each segment |
| Alternate Port | Backup path to root bridge (RSTP only; replaces blocking) |
| Backup Port | Backup on same segment (RSTP only) |
| Disabled | Administratively down |

### 802.11 Standards Quick Reference

| Standard | Band | Max Speed | Wi-Fi Name | Key Feature |
|---|---|---|---|---|
| 802.11b | 2.4 GHz | 11 Mbps | — | DSSS |
| 802.11a | 5 GHz | 54 Mbps | — | OFDM, 5 GHz |
| 802.11g | 2.4 GHz | 54 Mbps | — | OFDM, backward compat |
| 802.11n | 2.4/5 GHz | 600 Mbps | Wi-Fi 4 | MIMO |
| 802.11ac | 5 GHz | 6.9 Gbps | Wi-Fi 5 | MU-MIMO |
| 802.11ax | 2.4/5/6 GHz | 9.6 Gbps | Wi-Fi 6 | OFDMA |

---

## Section 4: Domain 3 — IP Connectivity

### Administrative Distance Reference

| Routing Source | Default AD |
|---|---|
| Connected interface | 0 |
| Static route | 1 |
| EIGRP summary route | 5 |
| External BGP | 20 |
| OSPF | 110 |
| IS-IS | 115 |
| RIP | 120 |
| EIGRP external | 170 |
| Internal BGP | 200 |
| Unknown / unreachable | 255 |

### OSPF Key Facts

```ios
! Enable OSPF process
router ospf 1

! Advertise networks
network 10.0.0.0 0.0.0.255 area 0
network 192.168.1.0 0.0.0.3 area 0

! Set router ID explicitly
router-id 1.1.1.1

! Adjust cost
interface gigabitethernet 0/0
 ip ospf cost 10

! Verify
show ip ospf neighbor
show ip ospf interface brief
show ip route ospf
```

### OSPF Neighbor States

| State | Description |
|---|---|
| Down | No hellos received |
| Attempt | Sending hellos (NBMA only) |
| Init | Hello received; our router ID not in it |
| 2-Way | Bidirectional communication established; DR/BDR election here |
| ExStart | Master/slave relationship determined |
| Exchange | Database description packets exchanged |
| Loading | LSR/LSU/LSAck exchange |
| Full | Full adjacency — routes can be installed |

### HSRP Configuration Reference

```ios
interface gigabitethernet 0/0
 ip address 10.0.0.2 255.255.255.0
 standby 1 ip 10.0.0.1
 standby 1 priority 110
 standby 1 preempt
 standby 1 authentication md5 key-string StandbyKey1

! Verify
show standby
show standby brief
```

---

## Section 5: Domain 4 — IP Services

### NAT Address Types

| Term | Definition | Example |
|---|---|---|
| Inside local | Private IP of the inside host | 192.168.1.10 |
| Inside global | Public IP representing the inside host to the outside | 203.0.113.5 |
| Outside local | IP of the outside host as seen from inside | 8.8.8.8 (usually same as outside global) |
| Outside global | Actual IP of the outside host | 8.8.8.8 |

### PAT Configuration Reference

```ios
! Define inside and outside interfaces
interface gigabitethernet 0/0
 ip nat inside
interface gigabitethernet 0/1
 ip nat outside

! Create ACL for inside addresses
ip access-list standard NAT-ACL
 permit 192.168.0.0 0.0.255.255

! Enable PAT using outside interface IP
ip nat inside source list NAT-ACL interface gigabitethernet 0/1 overload

! Verify
show ip nat translations
show ip nat statistics
```

### Syslog Severity Levels

| Level | Keyword | Description | Memory aid |
|---|---|---|---|
| 0 | Emergencies | System unusable | Every |
| 1 | Alerts | Immediate action needed | Administrator |
| 2 | Critical | Critical conditions | Should |
| 3 | Errors | Error conditions | Know |
| 4 | Warnings | Warning conditions | What |
| 5 | Notifications | Normal but significant | Numbers |
| 6 | Informational | Informational messages | I |
| 7 | Debugging | Debugging messages | Debug |

Memory aid: "Every Administrator Should Know What Numbers I Debug"

### NTP Stratum Levels

* Stratum 0 — atomic clock, GPS (reference clock; not networked)
* Stratum 1 — server directly connected to stratum 0 source
* Stratum 2 — server synchronized to a stratum 1 server
* Each hop adds one stratum number
* Stratum 15 — maximum usable (higher = less accurate)
* Stratum 16 — unsynchronized / unreachable

---

## Section 6: Domain 5 — Security Fundamentals

### AAA Protocol Comparison

| Feature | RADIUS | TACACS+ |
|---|---|---|
| Transport | UDP | TCP |
| Ports | 1812 (auth), 1813 (acct) | 49 |
| Encryption | Password only | Full packet |
| AuthN + AuthZ | Combined | Separated |
| Command authorization | No | Yes |
| Best use | Network access | Device admin |

### Port Security Violation Modes

| Mode | Drop frames? | Log? | Port state |
|---|---|---|---|
| Protect | Yes | No | Up |
| Restrict | Yes | Yes | Up |
| Shutdown | Yes | Yes | Err-disabled |

### Security Feature Dependencies

```text
Enable DHCP Snooping
    |
    v
Binding table built (MAC + IP + VLAN + port)
    |
    v
Enable Dynamic ARP Inspection (uses binding table)
    |
    v
ARP poisoning attacks blocked
```

---

## Section 7: Domain 6 — Automation and Programmability

### API Direction Reference

| Direction | Connects | Protocols | Example |
|---|---|---|---|
| Northbound | Applications to controller | REST/HTTPS/JSON | Python script calls DNA Center API |
| Southbound | Controller to devices | OpenFlow, NETCONF, RESTCONF | DNA Center configures IOS-XE switch |
| East-west | Controller to controller | Varies | WAN controller talks to campus controller |

### HTTP Method to CRUD Mapping

| Method | CRUD | Purpose |
|---|---|---|
| GET | Read | Retrieve data |
| POST | Create | Create new resource |
| PUT | Update | Replace existing resource |
| DELETE | Delete | Remove resource |

### HTTP Status Codes

| Code | Meaning | Triggered by |
|---|---|---|
| 200 | OK | Successful GET or PUT |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Malformed syntax |
| 401 | Unauthorized | Missing credentials |
| 403 | Forbidden | Insufficient privilege |
| 404 | Not Found | Wrong URL or resource ID |
| 500 | Server Error | Backend failure |

### Automation Tool Comparison

| Feature | Ansible | Puppet | Chef |
|---|---|---|---|
| Agent required | No | Yes | Yes |
| Model | Push | Pull | Pull |
| Language | YAML | Puppet DSL | Ruby |
| Network focus | Strong | Limited | Limited |

---

## Section 8: Exam Preparation Checklist

Work through each item in the week before your exam.

* Subnetting: calculate network, broadcast, and host range for 10 random subnets in under 45 seconds each
* OSI model: identify the layer for 20 different protocols and devices without reference material
* OSPF: explain DR/BDR election, neighbor states, and cost calculation from memory
* HSRP: configure active router, standby router, and preemption on a lab topology
* NAT: identify inside local vs. inside global from a `show ip nat translations` output
* Security: configure port security, DHCP snooping, and DAI on a lab switch from memory
* 802.1X: explain the three roles (supplicant, authenticator, authentication server) and their devices
* REST API: write the correct HTTP method for five different scenarios without reference
* Ansible: explain why Ansible does not require an agent on network devices
* NETCONF: state the transport protocol and port number from memory

---

## Section 9: Recommended Final Study Resources

* Cisco official exam topics: cisco.com/c/en/us/training-events/training-certifications
* Exam registration (Pearson VUE): certiport.pearsonvue.com
* Professor Messer CCNA 200-301 course (free): professormesser.com
* Cisco DevNet sandbox for API labs: developer.cisco.com/site/sandbox
* Cisco Packet Tracer (free): skillsforall.com

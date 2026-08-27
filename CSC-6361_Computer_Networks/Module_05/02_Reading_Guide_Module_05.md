# Reading Guide: Module 05 – QoS, High Availability & Network Automation
## CSC-6361 Advanced Computer Networks | Graduate Level
## Week 5: November 16–22, 2026

---

## Learning Objectives
By completing this reading guide, you will be able to:
1. Configure DiffServ QoS using MQC — class maps, policy maps, and service policies with LLQ and CBWFQ.
2. Distinguish traffic policing from traffic shaping and apply each correctly to an enterprise WAN design.
3. Configure HSRP and VRRP with preemption and verify Active/Standby state transitions.
4. Explain the role of BFD in accelerating FHRP failover and configure it on an HSRP-enabled interface.
5. Write a Python script using Netmiko to connect to a Cisco IOS device, gather information, and push configuration.
6. Describe an Ansible playbook structure and explain what makes Ansible suitable for network automation.
7. Explain RESTCONF and NETCONF/YANG at a conceptual level for the CCNP ENCOR exam.

---

## Required Free Readings

### 1. IETF RFC 2474 — DiffServ Field in the IPv4 and IPv6 Headers (Free)
**URL:** https://datatracker.ietf.org/doc/html/rfc2474
**Focus:** Section 1 (Introduction), Section 3 (DS Field), Section 4 (DSCP codepoints). This is the foundation of all DiffServ QoS.

### 2. IETF RFC 2475 — An Architecture for Differentiated Services (Free)
**URL:** https://datatracker.ietf.org/doc/html/rfc2475
**Focus:** Section 1 (Introduction), Section 2 (DiffServ concepts and model), Section 3 (PHBs — Per-Hop Behaviors). Read alongside RFC 2474.

### 3. IETF RFC 5798 — Virtual Router Redundancy Protocol (VRRP) Version 3 (Free)
**URL:** https://datatracker.ietf.org/doc/html/rfc5798
**Focus:** Section 1 (Introduction), Section 3 (Protocol Overview), Section 5 (Router Priority and Preemption).

### 4. Cisco QoS Configuration Guide — IOS XE (Free)
**URL:** https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/qos_classn/configuration/xe-16/qos-classn-xe-16-book.html
**Focus:** MQC configuration (class-map, policy-map, service-policy), LLQ (priority), CBWFQ (bandwidth), policing, and shaping.

### 5. Netmiko Documentation (Free)
**URL:** https://ktbyers.github.io/netmiko/
**Focus:** Getting started guide, supported device types (cisco_ios), `send_command`, `send_config_set` usage.

### 6. Ansible Network Automation Documentation (Free)
**URL:** https://docs.ansible.com/ansible/latest/network/index.html
**Focus:** "Getting Started with Network Automation," Cisco IOS collection (`cisco.ios`), playbook structure.

### 7. Cisco DevNet — Python for Network Engineers (Free Lab)
**URL:** https://developer.cisco.com/learning/
Search: "Python for Network Engineers" — complete the free learning lab that covers Netmiko and RESTCONF basics.

---

## Key Concepts Reference Card

### DSCP to Queue Mapping — Enterprise Design Pattern
| Traffic Type | Application Examples | DSCP | Queue |
|---|---|---|---|
| Voice (RTP) | VoIP, WebEx audio | EF (46) | LLQ (strict priority) |
| Interactive Video | Webex video, Zoom | AF41 (34) | CBWFQ (30% BW) |
| Call Control | SIP, H.323 signaling | CS3 (24) | CBWFQ (5% BW) |
| Critical Data | SAP ERP, financial apps | AF31 (26) | CBWFQ (20% BW) |
| Default | HTTP, email, web | BE (0) | Fair Queue (remaining) |
| Network Control | OSPF, BGP, STP | CS6 (48) | CBWFQ (5% BW) — or trust |

### HSRP State Machine
| State | Description |
|---|---|
| Initial | HSRP process starting |
| Listen | Listening for HSRP Hello messages |
| Speak | Sending Hello messages, participating in election |
| Standby | The backup router — monitoring Active |
| Active | Actively forwarding traffic for the virtual IP |

### HSRP vs. VRRP vs. GLBP Quick Reference
| Feature | HSRP | VRRP | GLBP |
|---|---|---|---|
| Standard | Cisco proprietary | IEEE (RFC 5798) | Cisco proprietary |
| Default priority | 100 | 100 | 100 |
| Load balancing | ❌ (only Active forwards) | ❌ | ✅ (multiple AVFs) |
| Preemption | Configurable | Configurable | Configurable |
| Terminology | Active/Standby | Master/Backup | AVG/AVF |
| BFD support | ✅ | ✅ | ✅ |

### MQC Skeleton (Copy to Every Lab)
```
class-map match-any [CLASS-NAME]
 match [criterion]    ! dscp, access-group, protocol, cos

policy-map [POLICY-NAME]
 class [CLASS-NAME]
  [action]           ! priority / bandwidth / police / set

interface [INTERFACE]
 service-policy [input | output] [POLICY-NAME]
```

---

## Python Automation Exercise (No Packet Tracer Required)
Complete the following exercises using Python (install Netmiko via `pip install netmiko`). If you do not have a physical device, use GNS3 (free) or download a Cisco IOS image for EVE-NG. Alternatively, use the Cisco DevNet Sandbox (free lab environment at https://developer.cisco.com/site/sandbox/).

**Exercise 1:** Write a Python script using Netmiko that:
- Connects to a Cisco IOS router via SSH.
- Runs `show version` and prints only the IOS version line.
- Runs `show ip interface brief` and prints only interfaces that are UP/UP.

**Exercise 2:** Extend the script to:
- Push a configuration to add a loopback interface (Loopback99: 99.99.99.1/32).
- Verify the interface appears in `show ip interface brief`.
- Save the configuration (`write memory`).

**Submit:** Your Python script file (`.py`) as an attachment to the Lab assignment, along with screenshots of the output (from your terminal or DevNet Sandbox).

---

## Verification Commands Quick Reference
```
! QoS
show policy-map interface GigabitEthernet0/0 output  ! Class stats, drops, queue depth
show class-map                                         ! View all class maps
show policy-map                                        ! View all policy maps

! HSRP
show standby                                           ! All HSRP groups, state, priority, virtual IP
show standby brief                                     ! Summary table
show standby vlan 10                                   ! Specific VLAN/interface
debug standby events                                   ! Real-time HSRP state transitions

! BFD
show bfd neighbors                                     ! BFD neighbor sessions, state, intervals
show bfd neighbors details                             ! Full BFD diagnostic info
```

---

## Graduate Discussion Prompt (Due Sunday, November 22, 2026, 11:59 PM CST)

**Scenario:** You are a senior network engineer at a hospital network. The hospital has just deployed a new telehealth platform that streams live HD video between patient rooms and remote doctors. The platform requires:
- Maximum end-to-end latency: 100ms
- Maximum packet loss: 0.1%
- Minimum bandwidth per concurrent session: 2 Mbps

The hospital's WAN is 100 Mbps shared between all applications. At peak hours, bandwidth utilization hits 95%. The network team has observed that telehealth video quality degrades severely during peak periods while a backup software tool performs large data transfers.

**Write a graduate-level post (400+ words) addressing:**
1. **QoS Design:** Design a DiffServ QoS policy for this hospital's WAN link. Specify: which DSCP value you would use for telehealth video, what queue type (LLQ or CBWFQ), and what bandwidth percentage you would allocate. How many concurrent telehealth sessions can this design support simultaneously?
2. **Traffic Policing Recommendation:** The backup software is consuming excessive bandwidth. Would you use policing or shaping to control it, and why? What DSCP value would you assign to backup traffic?
3. **FHRP for Telehealth Availability:** The hospital's core switch is a single point of failure for the telehealth VLAN's default gateway. Design an HSRP or GLBP solution for this scenario. Would you use HSRP or GLBP, and what would you set the hello/dead timers to? Would you configure BFD, and why?
4. **Automation Argument:** The hospital IT director asks why you want to spend time learning Python scripting instead of using the GUI. Write a concise but technically substantive argument for why network automation is valuable specifically in a healthcare network environment.

**Citation:** Cite RFC 2474 (DiffServ), RFC 5798 (VRRP), or Cisco QoS Design Guide.

---

## 9. Supplemental Resources

**1. Cisco QoS Design Guide**
https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/WAN_and_MAN/QoS_SRND/QoS-SRND-Book.html
Comprehensive Cisco QoS design reference covering classification, marking, queuing, and congestion management for enterprise WAN.

**2. RFC 3246 — Expedited Forwarding PHB**
https://datatracker.ietf.org/doc/html/rfc3246
The definitive specification for EF (DSCP 46) behavior, including the strict rate contract requirement.

**3. Ansible Network Automation Documentation**
https://docs.ansible.com/ansible/latest/network/index.html
Official Ansible documentation for network automation modules including ios_config, ios_command, and resource modules.

**4. Cisco DevNet — NETCONF/YANG Learning Lab**
https://developer.cisco.com/learning/modules/intro-device-level-interfaces/
Hands-on labs for NETCONF, RESTCONF, and YANG model-driven programmability on Cisco IOS-XE.

# Reading Guide: Module 05 – QoS, High Availability & Network Automation

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CSC-6361 &BULL; ADVANCED COMPUTER NETWORKS (GRADUATE LEVEL)</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>

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

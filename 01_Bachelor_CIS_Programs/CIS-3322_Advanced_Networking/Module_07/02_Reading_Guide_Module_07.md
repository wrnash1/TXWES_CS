# Reading Guide: Module 07 - Inter-VLAN Routing Solutions

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3322 &BULL; ADVANCED NETWORKING & INFRASTRUCTURE</text>
    
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


**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 3: IP Connectivity - 25%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

Inter-VLAN routing is tested on the CCNA 200-301 through configuration scenarios and troubleshooting questions. The exam frequently presents a topology where hosts in different VLANs cannot communicate and asks you to identify the missing or incorrect configuration. This guide covers both router-on-a-stick and Layer 3 switch SVI methods with full command references and common failure analysis.

---

## 1. High-Yield Glossary

- **Inter-VLAN routing:** The process of forwarding IP traffic between different VLANs using a Layer 3 device. Required because VLANs are separate Layer 2 broadcast domains and cannot exchange traffic without a router or Layer 3 switch.

- **Router-on-a-stick (ROAS):** An inter-VLAN routing method using a single physical router interface connected to a trunk port. Logical subinterfaces are created on the physical interface — one per VLAN — each configured with an IP address serving as the default gateway for that VLAN.

- **Subinterface:** A logical division of a physical router interface. Created using the syntax `interface [type][slot/port].[number]`. Each subinterface is independently configured with 802.1Q encapsulation and an IP address.

- **encapsulation dot1Q:** The IOS command applied to a router subinterface to associate it with a specific VLAN. Syntax: `encapsulation dot1Q [vlan-id]`. Must be entered before the IP address command.

- **Switched Virtual Interface (SVI):** A virtual Layer 3 interface on a multilayer switch that represents an entire VLAN. Configured with `interface vlan [vlan-id]` and assigned an IP address. Hosts in that VLAN use the SVI IP address as their default gateway.

- **Multilayer switch:** A switch capable of both Layer 2 switching and Layer 3 routing. Also called a Layer 3 switch. Requires the global command `ip routing` to enable the routing function.

- **ip routing:** The global Cisco IOS command that enables Layer 3 routing on a multilayer switch. Without this command, SVIs are created but do not route traffic between VLANs.

- **Default gateway:** The IP address that a host sends traffic to when the destination is in a different subnet. In inter-VLAN routing, the default gateway for each VLAN is the IP address of the router subinterface or SVI assigned to that VLAN.

- **up/down SVI state:** The condition of an SVI when the interface itself is administratively up but has no active access ports assigned to its VLAN. The SVI will not pass traffic until at least one port in that VLAN is connected and active.

- **Native VLAN subinterface:** On a ROAS configuration, the subinterface handling the native VLAN is configured with `encapsulation dot1Q [vlan-id] native` to accept untagged frames from the switch trunk port.

---

## 2. Inter-VLAN Routing Method Comparison

| Criteria | Router-on-a-Stick | Layer 3 Switch SVIs |
|---|---|---|
| Hardware required | External router + Layer 2 switch | Multilayer (Layer 3) switch only |
| Traffic path | Exits switch, traverses physical router, returns | Stays entirely within switch hardware |
| Bandwidth bottleneck | Single trunk uplink shared by all inter-VLAN traffic | No external bottleneck — hardware-assisted routing |
| Scalability | Limited — one physical link carries all routed traffic | High — suitable for campus enterprise deployments |
| Configuration complexity | Moderate — subinterfaces, encapsulation, trunk required | Moderate — ip routing, SVIs, VLANs required |
| Best use case | Small networks, labs, CCNA practice | Enterprise campus distribution and core layer |
| CCNA exam frequency | Frequently tested — configuration and troubleshooting | Frequently tested — SVI state and ip routing requirement |

---

## 3. Router-on-a-Stick Configuration Reference

### Switch Trunk Port Configuration

```ios
SW1(config)# interface GigabitEthernet0/1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 10,20,30
SW1(config-if)# end
```

### Router Subinterface Configuration

```ios
R1(config)# interface GigabitEthernet0/0
R1(config-if)# no shutdown

R1(config)# interface GigabitEthernet0/0.10
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip address 192.168.10.1 255.255.255.0

R1(config)# interface GigabitEthernet0/0.20
R1(config-subif)# encapsulation dot1Q 20
R1(config-subif)# ip address 192.168.20.1 255.255.255.0

R1(config)# interface GigabitEthernet0/0.30
R1(config-subif)# encapsulation dot1Q 30
R1(config-subif)# ip address 192.168.30.1 255.255.255.0
R1(config)# end
```

Key rules:

- The parent physical interface must be up (`no shutdown`) but receives no IP address
- `encapsulation dot1Q` must be entered before `ip address` on each subinterface
- The subinterface number does not need to match the VLAN ID, but matching is universal best practice

---

## 4. Layer 3 Switch SVI Configuration Reference

### Enable Routing and Create VLANs

```ios
MLS1(config)# ip routing

MLS1(config)# vlan 10
MLS1(config-vlan)# name ENGINEERING
MLS1(config-vlan)# vlan 20
MLS1(config-vlan)# name SALES
MLS1(config-vlan)# vlan 30
MLS1(config-vlan)# name MANAGEMENT
MLS1(config-vlan)# exit
```

### Create SVIs

```ios
MLS1(config)# interface vlan 10
MLS1(config-if)# ip address 192.168.10.1 255.255.255.0
MLS1(config-if)# no shutdown

MLS1(config)# interface vlan 20
MLS1(config-if)# ip address 192.168.20.1 255.255.255.0
MLS1(config-if)# no shutdown

MLS1(config)# interface vlan 30
MLS1(config-if)# ip address 192.168.30.1 255.255.255.0
MLS1(config-if)# no shutdown
```

### Assign Access Ports to VLANs

```ios
MLS1(config)# interface FastEthernet0/1
MLS1(config-if)# switchport mode access
MLS1(config-if)# switchport access vlan 10

MLS1(config)# interface FastEthernet0/2
MLS1(config-if)# switchport mode access
MLS1(config-if)# switchport access vlan 20
```

---

## 5. IOS Command Reference

| Task | Command | Mode |
|---|---|---|
| Enable IP routing on multilayer switch | `ip routing` | Global config |
| Create subinterface on router | `interface Gi0/0.10` | Global config |
| Set 802.1Q encapsulation on subinterface | `encapsulation dot1Q 10` | Subinterface config |
| Assign IP to subinterface or SVI | `ip address 192.168.10.1 255.255.255.0` | Interface config |
| Enable parent physical interface | `no shutdown` | Interface config |
| Create SVI for a VLAN | `interface vlan 10` | Global config |
| Verify interface states and IPs | `show ip interface brief` | Privileged EXEC |
| Verify SVI state and counters | `show interfaces vlan 10` | Privileged EXEC |
| Verify routing table | `show ip route` | Privileged EXEC |
| Verify subinterface encapsulation | `show interfaces GigabitEthernet0/0.10` | Privileged EXEC |
| Verify VLAN-to-port mapping | `show vlan brief` | Privileged EXEC |
| Verify trunk configuration | `show interfaces trunk` | Privileged EXEC |
| Verify running configuration | `show running-config` | Privileged EXEC |

---

## 6. SVI State Reference

| SVI State | Meaning | Common Cause |
|---|---|---|
| up / up | SVI is active and routing | At least one access port in the VLAN is connected and up |
| up / down | Administratively up but no active port in VLAN | No ports assigned to VLAN, or all assigned ports are down |
| administratively down / down | SVI manually shut down | `shutdown` command applied to the SVI |

The most common exam trap: an SVI is configured with an IP address but no port in that VLAN is active. The SVI shows `up/down` and does not route. Run `show vlan brief` to confirm port assignment, and `show ip interface brief` to confirm SVI state.

---

## 7. Troubleshooting Reference

### Router-on-a-Stick Common Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| Subinterface is down/down | Parent physical interface is administratively down | `no shutdown` on the parent interface (not the subinterface) |
| Hosts cannot ping router subinterface | `encapsulation dot1Q` missing or wrong VLAN ID | Add correct `encapsulation dot1Q [vlan-id]` before ip address |
| Only one VLAN can reach the router | Switch port not configured as trunk | `switchport mode trunk` on the switch port facing the router |
| One VLAN cannot reach the router | VLAN missing from trunk allowed list | `switchport trunk allowed vlan add [vlan-id]` |
| Native VLAN hosts cannot route | Subinterface does not handle untagged frames | `encapsulation dot1Q [vlan-id] native` on native VLAN subinterface |

### Layer 3 SVI Common Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| SVIs exist but traffic is not routed | `ip routing` not enabled | Add `ip routing` in global config |
| SVI is up/down | No active access ports in the VLAN | Assign at least one port to the VLAN and confirm it is up |
| SVI shows up/up but hosts cannot reach other VLANs | Host default gateway is wrong | Set host gateway to the SVI IP address of its own VLAN |
| SVI shows up/down despite port being connected | VLAN not created in VLAN database | Create the VLAN with `vlan [id]` in global config |

---

## 8. CCNA Exam Tips

1. On a router-on-a-stick configuration, `encapsulation dot1Q [vlan-id]` must come before `ip address` on the subinterface. The IOS rejects the IP address command if encapsulation is not configured first.

2. The parent physical interface in ROAS receives `no shutdown` but no IP address. Only subinterfaces receive IP addresses. A common distractor shows an IP address on the parent interface.

3. `ip routing` is the single most important command for Layer 3 switch SVI routing. Without it, the switch operates as a pure Layer 2 device regardless of how many SVIs are configured.

4. An SVI is `up/down` when no active access ports exist in that VLAN. This is not a misconfiguration on the SVI itself — it is a Layer 1 or VLAN membership issue on the access ports.

5. In ROAS, all inter-VLAN traffic physically travels out the trunk link to the router and returns on the same trunk. This creates a bottleneck at the single physical link. SVIs route internally and have no such bottleneck.

6. The subinterface number does not need to match the VLAN ID, but matching them is best practice and all exam examples use matching numbers.

7. When a VLAN is deleted from the VLAN database, its SVI goes `up/down`. Recreating the VLAN and ensuring at least one port is in it brings the SVI back up.

8. A Layer 3 switch can also use routed ports (`no switchport` on a physical interface) instead of SVIs for point-to-point Layer 3 links. SVIs are used for VLAN-to-VLAN routing; routed ports are used for uplinks.

---

## 9. Study Checklist

Work through each item before taking the quiz.

- [ ] Write the complete ROAS configuration from memory for three VLANs on R1 Gi0/0
- [ ] Write the complete SVI configuration from memory for three VLANs on MLS1
- [ ] Explain why `ip routing` is required and what happens without it
- [ ] Describe the three possible SVI states and what causes each
- [ ] Explain why the parent physical interface in ROAS does not get an IP address
- [ ] List the two most common ROAS configuration failures and how to fix each
- [ ] Compare the traffic path for inter-VLAN routing via ROAS versus SVIs
- [ ] Complete the Module 07 Packet Tracer lab activity
- [ ] Post your Module 07 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and video summaries: professormesser.com

---

## 10. Supplemental Resources

The following open educational resources extend inter-VLAN routing concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Switching, Routing, and Wireless Essentials, Chapter 4 (Inter-VLAN Routing)** (skillsforall.com): This free chapter covers all three inter-VLAN routing methods (legacy, ROAS, and SVI) with interactive Packet Tracer activities for configuring and troubleshooting each method.

2. **Jeremy's IT Lab — Inter-VLAN Routing (Days 17–19)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): These video lessons provide side-by-side configuration demonstrations for ROAS and SVI routing, including the `ip routing` requirement, SVI state troubleshooting, and the traffic path comparison.

3. **Cisco Learning Network — Inter-VLAN Routing Study Group** (learningnetwork.cisco.com): Community discussions include configuration scenario questions comparing ROAS and SVI performance trade-offs, common SVI down/down troubleshooting scenarios, and CCNA exam-style inter-VLAN routing questions.

4. **Cisco Packet Tracer — Inter-VLAN Routing Lab Files** (skillsforall.com): Pre-built Packet Tracer activities are available for both ROAS and SVI configurations. These labs guide students through complete configurations and verification steps matching the Module 07 lab objectives.

5. **Cisco IOS Configuration Guide — Configuring SVIs** (cisco.com): Cisco's official documentation for configuring Switched Virtual Interfaces on Catalyst multilayer switches, covering SVI state requirements, IP address assignment, and `ip routing` interaction.

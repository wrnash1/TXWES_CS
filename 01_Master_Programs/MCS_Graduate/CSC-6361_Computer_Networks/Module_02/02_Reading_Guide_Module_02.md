# Reading Guide: Module 02 – Campus Network Design: VLANs, STP & EtherChannel

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
## Week 2: October 26 – November 1, 2026

---

## Learning Objectives
By completing this reading guide, you will be able to:
1. Design a three-tier campus network and justify the role of each layer.
2. Configure VLANs, 802.1Q trunks, VTP, and inter-VLAN routing using SVIs on a multilayer switch.
3. Explain STP root election, port roles, and port states for both 802.1D and 802.1W (RSTP/Rapid PVST+).
4. Configure and verify EtherChannel using LACP and troubleshoot common formation failures.
5. Configure MST (802.1S) and map VLANs to instances.
6. Diagnose and resolve common STP and EtherChannel failures from show command output.

---

## Required Free Readings

### 1. Cisco Campus LAN and Wireless LAN Design Guide (Free)
**URL:** https://www.cisco.com/c/en/us/solutions/enterprise-networks/index.html
Search: "Campus LAN Design Guide" → Download the current validated design guide PDF (free with registration).
**Focus:** Three-tier hierarchy, distribution layer design, collapsed core vs. three-tier trade-offs.

### 2. IEEE 802.1Q — VLAN Tagging Overview (via Cisco documentation)
**URL:** https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41860-howto-L3-intervlanrouting.html
**Focus:** 802.1Q frame format, native VLAN, inter-VLAN routing options (router-on-a-stick vs. SVI).

### 3. IEEE 802.1W — Rapid Spanning Tree (via Cisco documentation)
**URL:** https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html
**Focus:** RSTP port roles, port states, proposal/agreement mechanism, edge ports.

### 4. Cisco EtherChannel Configuration Guide (Free)
**URL:** https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/lanswitch/configuration/xe-16/lanswitch-xe-16-book/lsw-etherchannel.html
**Focus:** LACP vs. PAgP modes, load balancing, verification commands.

### 5. Cisco MST Configuration Guide (Free)
**URL:** https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24248-147.html
**Focus:** MST region configuration, VLAN-to-instance mapping, interoperability with PVST+.

### 6. Cisco Learning Network — CCNP ENCOR Study Materials
**URL:** https://learningnetwork.cisco.com/s/encor-study-materials
Review the "Layer 2" and "Infrastructure" sections of the ENCOR blueprint.

---

## Key Concepts Reference Card

### VTP Risk Summary
| VTP Mode | Creates VLANs | Propagates Ads | Risk Level |
|---|---|---|---|
| Server | Yes | Yes | ⚠ High (revision number danger) |
| Client | No | Yes | ⚠ Medium |
| Transparent | Local only | Forwards only | ✅ Safe (recommended) |
| Off (VTPv3) | Local only | No | ✅ Safest |

**Best Practice:** Set all switches to VTP Transparent or use VTPv3 with explicit server designation.

### STP Port State Summary (Rapid PVST+)
| State | Sends/Receives BPDUs? | Learns MACs? | Forwards Traffic? |
|---|---|---|---|
| Discarding | Yes / Yes | No | No |
| Learning | Yes / Yes | Yes | No |
| Forwarding | Yes / Yes | Yes | Yes |

### EtherChannel Mode Compatibility Quick Reference
| Side A | Side B | Forms Channel? |
|---|---|---|
| active (LACP) | active (LACP) | ✅ Yes |
| active (LACP) | passive (LACP) | ✅ Yes |
| passive (LACP) | passive (LACP) | ❌ No |
| desirable (PAgP) | desirable (PAgP) | ✅ Yes |
| desirable (PAgP) | auto (PAgP) | ✅ Yes |
| auto (PAgP) | auto (PAgP) | ❌ No |
| on | on | ✅ Yes (static) |
| on | active/passive | ❌ No |

### Critical STP Security Commands
```
! PortFast — only on end-device ports
spanning-tree portfast                           ! Per-interface
spanning-tree portfast default                   ! Global (all access ports)

! BPDU Guard — shuts down port if BPDU received
spanning-tree bpduguard enable                   ! Per-interface
spanning-tree portfast bpduguard default         ! Global (all PortFast ports)

! Root Guard — prevents downstream switch from becoming root
spanning-tree guard root                         ! Per-interface (toward access layer)

! Loop Guard — prevents a port from transitioning to forwarding if BPDUs stop
spanning-tree guard loop                         ! Per-interface (on non-designated ports)
```

---

## Verification Commands Quick Reference
```
! VLAN
show vlan brief                        ! All VLANs and port assignments
show interfaces trunk                  ! All trunk links, native VLANs, allowed VLANs
show interfaces GigabitEthernet0/1 trunk

! STP
show spanning-tree vlan 10             ! Full STP detail for VLAN 10
show spanning-tree vlan 10 detail      ! Includes timers, topology change count
show spanning-tree summary             ! All VLANs, root/not-root status

! EtherChannel
show etherchannel summary              ! All port-channels, member status
show etherchannel 1 detail             ! Detail for Port-Channel 1
show lacp neighbor                     ! LACP partner info
show interfaces port-channel 1         ! Logical interface statistics
```

---

## Graduate Discussion Prompt (Due Sunday, November 1, 2026, 11:59 PM CST)

**Scenario:** You are the network architect for a regional hospital system with 3 buildings (main campus, medical office building, and a remote clinic connected via fiber). The main campus has ~800 network devices. The medical office building has ~200. The remote clinic has ~50. All three buildings must share VLANs for specific applications: VLAN 10 (Clinical Staff), VLAN 20 (Guest/Patient Wi-Fi), VLAN 30 (Medical Devices / IoT), VLAN 40 (Voice/IP Phones), and VLAN 99 (Management).

**Write a graduate-level post (400+ words) addressing:**
1. **Campus Architecture:** Would you use a three-tier or two-tier (collapsed core) design for the main campus? For the remote clinic? Justify your choice based on scale and cost factors.
2. **VLAN Design Decision:** VLAN 30 (Medical Devices) must be strictly isolated from VLAN 20 (Guest/Patient Wi-Fi) for HIPAA compliance and patient safety. How would you enforce this isolation at the network layer while still allowing medical devices to reach specific hospital servers? (Hint: consider inter-VLAN routing policy and ACLs.)
3. **STP Design:** Which spanning tree variant (PVST+, Rapid PVST+, or MST) would you choose for this environment, and why? Would you use the same variant in all three buildings?
4. **EtherChannel vs. Single Uplink:** The main campus distribution switches currently have a single 10G uplink to the core. A junior engineer proposes adding a second 10G link in an EtherChannel for redundancy. A senior engineer argues that two 10G routed L3 links with OSPF would be better. Evaluate both arguments and state which you would choose.

**Citation Requirement:** Cite at least one Cisco design guide, IEEE standard reference, or HIPAA/NIST networking security publication.

---

## 9. Supplemental Resources

**1. IEEE 802.1D-2004 — Spanning Tree Protocol Standard (Overview via Cisco)**
https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/5234-5.html
Cisco's comprehensive STP overview document covers the original 802.1D standard, the election algorithm, port states, and timer interactions. Essential for understanding why RSTP was designed as an improvement and what specific problems it solved.

**2. Cisco VTP Best Practices and Version 3 Overview**
https://www.cisco.com/c/en/us/support/docs/lan-switching/vtp/98154-conf-vtp.html
Covers VTP version 1, 2, and 3 configuration with emphasis on the revision-number risk that destroyed countless production networks. Explains why VTPv3 primary server design and VTP Transparent mode are now the recommended enterprise practices.

**3. NIST SP 800-125B — Secure Virtual Network Configuration for Virtual Machine (VM) Protection**
https://csrc.nist.gov/publications/detail/sp/800-125b/final
While focused on virtualization, this NIST publication covers VLAN segmentation security requirements including VLAN hopping attack mitigations, native VLAN risks, and network isolation principles — directly applicable to the HIPAA medical device isolation requirement in this module's discussion prompt.

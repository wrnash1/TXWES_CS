# Reading Guide: Module 02 – Campus Network Design: VLANs, STP & EtherChannel
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

# Reading Guide: Module 04 - Switching Concepts & VLANs

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
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Prepared by:** Professor Nash | Texas Wesleyan University

---

## Overview

VLANs are one of the most heavily tested topics in the CCNA 200-301 Network Access domain. This guide covers MAC address learning, VLAN concepts, 802.1Q trunking, the native VLAN, DTP, and the full Cisco IOS command set for VLAN configuration and verification. Work through the DTP negotiation table and `show vlan brief` interpretation exercises before the quiz.

---

## 1. High-Yield Glossary

- **VLAN (Virtual Local Area Network):** A logical broadcast domain created within a switch or across multiple switches. Devices in the same VLAN communicate at Layer 2 without a router. Devices in different VLANs require Layer 3 routing to communicate.

- **Access port:** A switch port configured to belong to exactly one VLAN. End devices (PCs, printers) connect to access ports. Frames arrive untagged and depart untagged. The switch internally tags the frame for forwarding.

- **Trunk port:** A switch port configured to carry traffic for multiple VLANs simultaneously using 802.1Q tagging. Used on switch-to-switch and switch-to-router uplinks.

- **802.1Q:** The IEEE standard for VLAN frame tagging. A 4-byte tag is inserted into the Ethernet frame between the source MAC address and the EtherType field. The tag contains the Tag Protocol Identifier (0x8100), priority bits (802.1p), and a 12-bit VLAN ID supporting VLANs 1-4094.

- **Native VLAN:** The VLAN on an 802.1Q trunk whose frames travel untagged. Both ends of a trunk must agree on the native VLAN. Default is VLAN 1. Best practice is to change native VLAN to an unused VLAN to prevent VLAN hopping attacks.

- **DTP (Dynamic Trunking Protocol):** A Cisco-proprietary protocol that negotiates trunk formation between adjacent Cisco switches. DTP modes include trunk, access, dynamic desirable, and dynamic auto. Best practice: disable DTP on user-facing ports with `switchport nonegotiate`.

- **MAC address table:** The Layer 2 forwarding database on a switch that maps MAC addresses to switch ports. Also called the CAM table (Content Addressable Memory). Built dynamically as frames arrive; entries age out after 300 seconds by default.

- **Unicast flooding:** When a switch receives a frame with a destination MAC not in its MAC address table, it floods the frame out all ports in the VLAN except the source port. This is normal behavior for unknown unicast.

- **Broadcast domain:** The set of all devices that receive a Layer 2 broadcast frame. Each VLAN is its own broadcast domain. Routing is required to cross broadcast domain boundaries.

- **VTP (VLAN Trunking Protocol):** A Cisco protocol that propagates VLAN database information from a VTP server to VTP client switches in the same management domain. VTP can be dangerous — a new switch inserted as a VTP server can overwrite all VLAN configurations. VTP transparent mode is the safer choice.

- **VLAN hopping:** A Layer 2 security attack where an attacker crafts double-tagged 802.1Q frames to send traffic across VLAN boundaries without a router. Mitigated by changing the native VLAN to an unused VLAN and disabling DTP.

- **Port security:** A switch feature that restricts which MAC addresses can use a port. Can be configured to allow a maximum number of MACs, or to restrict to a specific set of approved MACs.

- **PVID (Port VLAN ID):** The VLAN ID assigned to an access port. This is the VLAN that untagged frames on that port are associated with.

---

## 2. VLAN Ranges Reference

| Range | VLAN IDs | Purpose |
|---|---|---|
| Normal VLANs | 1-1005 | General purpose; VLANs 1-1005 stored in flash:vlan.dat |
| Extended VLANs | 1006-4094 | Requires VTP transparent mode or VTPv3; stored in running-config |
| VLAN 1 | 1 | Default VLAN; all ports assigned here by default; avoid using for data traffic |
| Reserved | 1002-1005 | Legacy Token Ring and FDDI; cannot be deleted |

---

## 3. DTP Negotiation Matrix

| Side A Mode | Side B Mode | Result |
|---|---|---|
| trunk | trunk | Trunk |
| trunk | dynamic desirable | Trunk |
| trunk | dynamic auto | Trunk |
| trunk | access | Does not trunk (misconfiguration) |
| dynamic desirable | dynamic desirable | Trunk |
| dynamic desirable | dynamic auto | Trunk |
| dynamic auto | dynamic auto | Access (NO trunk formed) |
| access | access | Access |
| access | dynamic desirable | Access |
| access | dynamic auto | Access |

Key point: Two ports in `dynamic auto` will never form a trunk. This is tested frequently on the CCNA.

---

## 4. Cisco IOS VLAN Configuration Command Reference

| Task | Command | Mode |
|---|---|---|
| Create a VLAN | `vlan 10` | Global config |
| Name a VLAN | `name ENGINEERING` | VLAN config |
| Assign access port to VLAN | `switchport access vlan 10` | Interface config |
| Force port to access mode | `switchport mode access` | Interface config |
| Configure trunk port | `switchport mode trunk` | Interface config |
| Set allowed VLANs on trunk | `switchport trunk allowed vlan 10,20,30` | Interface config |
| Change native VLAN | `switchport trunk native vlan 999` | Interface config |
| Disable DTP | `switchport nonegotiate` | Interface config |
| Verify VLAN assignments | `show vlan brief` | Privileged EXEC |
| Verify trunk ports | `show interfaces trunk` | Privileged EXEC |
| Verify single interface | `show interfaces Fa0/1 switchport` | Privileged EXEC |
| View MAC address table | `show mac address-table` | Privileged EXEC |
| View MAC entries for VLAN | `show mac address-table vlan 10` | Privileged EXEC |

---

## 5. Interpreting show vlan brief Output

Sample output:

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- ----------------------------
1    default                          active    Fa0/5, Fa0/6, Fa0/7
10   ENGINEERING                      active    Fa0/1, Fa0/2
20   SALES                            active    Fa0/3, Fa0/4
999  NATIVE_UNUSED                    active
1002 fddi-default                     act/unsup
1003 token-ring-default               act/unsup
```

Key interpretation points:

- Trunk ports do NOT appear in the port list. They carry all allowed VLANs and are shown only in `show interfaces trunk`.
- Ports listed under VLAN 1 default that should be in other VLANs indicate a misconfigured access VLAN assignment.
- A VLAN that exists with no ports assigned is normal — the VLAN is created but no ports are currently using it.
- VLANs 1002-1005 are always present and cannot be removed; they are legacy FDDI/Token Ring VLANs.

---

## 6. Interpreting show interfaces trunk Output

Sample output:

```text
Port      Mode         Encapsulation  Status        Native vlan
Gi0/1     on           802.1q         trunking      1

Port      Vlans allowed on trunk
Gi0/1     1-4094

Port      Vlans allowed and active in management domain
Gi0/1     1,10,20

Port      Vlans in spanning tree forwarding state and not pruned
Gi0/1     1,10,20
```

Key interpretation points:

- "Vlans allowed on trunk" shows what was configured with `switchport trunk allowed vlan`.
- "Vlans allowed and active" shows which of those VLANs exist in the VLAN database.
- "Vlans in spanning tree forwarding state" shows which VLANs are actively forwarding. A VLAN missing here is being blocked by STP.

---

## 7. VLAN Security Best Practices

| Threat | Mitigation |
|---|---|
| VLAN hopping via double-tagging | Change native VLAN to unused VLAN (not VLAN 1); apply `switchport trunk native vlan 999` |
| Unauthorized trunk formation | Disable DTP with `switchport nonegotiate` on all access ports |
| Rogue DHCP server on wrong VLAN | Enable DHCP snooping per-VLAN; trust only uplink ports |
| MAC flooding attack (fill CAM table) | Configure port security to limit maximum MAC addresses per port |
| Unauthorized switch insertion | Use 802.1X port authentication; disable CDP/LLDP on user ports |

---

## 8. CCNA Exam Tips

1. Two switch ports both set to `dynamic auto` will NOT form a trunk. This combination produces an access port on both sides. The CCNA tests this in negotiation table questions.

2. Trunk ports do not appear in `show vlan brief`. If you configure a trunk port and then check `show vlan brief`, you will not see it listed under any VLAN. Use `show interfaces trunk` to verify trunk ports.

3. The native VLAN mismatch CDP warning (`%CDP-4-NATIVE_VLAN_MISMATCH`) is a classic CCNA troubleshooting question. If you see this log message, both ends of the trunk have different native VLANs configured.

4. VLAN 1 is the default native VLAN and the default management VLAN on Cisco switches. Best practice is to move management traffic to a different VLAN and change the native VLAN to an unused number.

5. The `show interfaces [id] switchport` command shows the full switchport configuration including operational mode, administrative mode, access VLAN, trunk encapsulation, and trunking status for a single interface.

6. When a port is in `trunk` mode but the allowed VLAN list does not include a specific VLAN, traffic for that VLAN will not cross the trunk. Use `switchport trunk allowed vlan add [id]` to add a VLAN without replacing the existing list.

7. VLANs must exist in the VLAN database on both switches for traffic to pass across a trunk. If a VLAN is configured on one switch but not the other, the VLAN will not appear in the "active" section of `show interfaces trunk`.

8. Port security with `switchport port-security maximum 1` allows only one MAC address per port. If a second MAC is detected, the port can be configured to shut down, restrict, or protect.

---

## 9. Study Checklist

Work through each item before taking the quiz.

- [ ] Define all 13 glossary terms from memory
- [ ] Complete the DTP negotiation matrix from memory and verify against the reference table
- [ ] Configure a VLAN, assign two access ports, and configure a trunk in Packet Tracer without referring to notes
- [ ] Interpret a sample `show vlan brief` output and identify which ports are configured incorrectly
- [ ] Explain native VLAN mismatch: what causes it, what log message it produces, and how to fix it
- [ ] List the two commands needed to harden a user-facing access port against DTP attacks
- [ ] Review the security best practices table and understand the mitigation for each threat
- [ ] Complete the Module 04 Packet Tracer lab activity
- [ ] Post your Module 04 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and video summaries: professormesser.com

---

## 10. Supplemental Resources

The following open educational resources extend VLAN and switching concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Switching, Routing, and Wireless Essentials** (skillsforall.com): Chapters 1–3 of this free course cover VLAN concepts, trunk configuration, DTP behavior, and VTP operation with interactive Packet Tracer labs.

2. **Jeremy's IT Lab — VLANs and Trunking (Days 16–18)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): These lessons cover VLAN creation, 802.1Q trunking, DTP negotiation modes, native VLAN configuration, and the `show interfaces trunk` output interpretation at CCNA exam depth.

3. **Cisco Learning Network — VLAN and Switching Study Group** (learningnetwork.cisco.com): Community forums and study group resources for VLANs, trunking, and switching concepts include hundreds of practice questions and configuration scenario discussions.

4. **Cisco Packet Tracer Labs — VLAN Configuration Activities** (skillsforall.com/course/getting-started-cisco-packet-tracer): Pre-built Packet Tracer activities for VLAN configuration, trunk verification, and access port troubleshooting are available through the Cisco Networking Academy, all aligned with CCNA Domain 2 objectives.

5. **GNS3 Documentation — Ethernet Switching Labs** (docs.gns3.com): GNS3 provides free virtual lab guides for switch configuration including VLAN trunking, DTP, and VTP lab topologies that can be run without physical hardware.

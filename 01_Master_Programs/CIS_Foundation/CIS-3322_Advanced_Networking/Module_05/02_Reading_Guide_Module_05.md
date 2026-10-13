# Reading Guide: Module 05 - Spanning Tree Protocol (STP & RSTP)

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

STP is one of the most diagram-intensive topics on the CCNA 200-301 exam. You will be given a multi-switch topology and asked to identify port roles, predict which ports are blocking, determine the root bridge, and calculate path costs. This guide provides all reference tables, calculation rules, state machine details, and Cisco IOS commands you need.

---

## 1. High-Yield Glossary

- **STP (Spanning Tree Protocol):** IEEE 802.1D protocol that prevents Layer 2 switching loops in networks with redundant paths. STP creates a loop-free logical topology by placing select ports in a Blocking state.

- **RSTP (Rapid Spanning Tree Protocol):** IEEE 802.1w protocol that improves on STP by converging in 1-2 seconds instead of 30-50 seconds. Cisco's implementation is called Rapid PVST+.

- **PVST+ (Per-VLAN Spanning Tree Plus):** Cisco enhancement to 802.1D that runs a separate STP instance per VLAN. Allows different VLANs to have different root bridges for load balancing.

- **Rapid PVST+:** Cisco's per-VLAN implementation of 802.1w (RSTP). Default STP mode on modern Cisco Catalyst switches.

- **Bridge ID (BID):** A unique identifier for each switch in an STP domain. Composed of Bridge Priority (2 bytes) + Extended System ID (12-bit VLAN ID embedded in priority) + MAC Address (6 bytes).

- **Bridge Priority:** A configurable value that determines which switch becomes root. Default is 32768. Must be set in increments of 4096. Lower value = higher priority = more likely to be root.

- **Root bridge:** The switch elected as the center of the STP tree. All traffic paths radiate outward from the root bridge. The switch with the lowest BID becomes root.

- **Root Port (RP):** The port on each non-root switch that offers the lowest-cost path to the root bridge. Every non-root switch has exactly one Root Port. It is always in Forwarding state.

- **Designated Port (DP):** On each network segment, the port on the switch offering the lowest-cost path to root. Always in Forwarding state. The root bridge has all ports as Designated Ports.

- **Non-Designated Port:** A port that is neither Root nor Designated. Placed in Blocking state to prevent loops. Called Alternate Port in RSTP.

- **BPDU (Bridge Protocol Data Unit):** The STP control message used for root bridge election, topology change notification, and maintaining the STP topology. Hello BPDUs are sent every 2 seconds by default.

- **Path cost:** A value assigned to each switch port based on link speed. Lower cost = preferred path. Used to determine Root Ports and Designated Ports.

- **PortFast:** A Cisco feature that allows access ports to skip the Listening and Learning states and go directly to Forwarding. Use only on ports connected to end devices.

- **BPDU Guard:** Places a PortFast-enabled port in err-disabled state if any BPDU is received. Protects against accidental or malicious switch connections on end-device ports.

- **Root Guard:** Prevents a port from becoming a Root Port if a superior BPDU is received, protecting the intended root bridge placement.

- **Err-disabled:** A port state where the switch has automatically shut down the port due to a security violation (such as BPDU Guard triggering). The port must be manually recovered or auto-recovery configured.

---

## 2. STP Path Cost Reference Table

| Link Speed | IEEE 802.1D Cost (Revised) | Older IEEE Cost |
|---|---|---|
| 10 Gbps | 2 | N/A |
| 1 Gbps | 4 | 1 |
| 100 Mbps | 19 | 10 |
| 10 Mbps | 100 | 100 |

Cumulative path cost is the sum of the costs of all switch ports between a given switch and the root bridge, counting only the receiving ports (not the transmitting ports).

---

## 3. 802.1D Port State Reference

| State | Duration | Frame Forwarding | BPDU Processing | MAC Learning |
|---|---|---|---|---|
| Blocking | Until topology change | No | Yes (receive only) | No |
| Listening | 15 sec (Forward Delay) | No | Yes | No |
| Learning | 15 sec (Forward Delay) | No | Yes | Yes |
| Forwarding | Indefinite | Yes | Yes | Yes |
| Disabled | Administratively set | No | No | No |

Total convergence from Blocking to Forwarding = 30 seconds minimum.

---

## 4. RSTP Port State and Role Reference

RSTP Port States (802.1w):

| RSTP State | 802.1D Equivalent |
|---|---|
| Discarding | Blocking + Listening + Disabled |
| Learning | Learning |
| Forwarding | Forwarding |

RSTP Port Roles:

| Role | Description |
|---|---|
| Root Port | Best path to root bridge (same as 802.1D) |
| Designated Port | Best path on a segment to root (same as 802.1D) |
| Alternate Port | Second-best path to root; replaces Root Port if it fails |
| Backup Port | Second Designated Port on the same shared segment |

---

## 5. STP Root Bridge Election Process

Step-by-step determination:

1. All switches start with their default Bridge Priority (32768 + VLAN ID)
2. Each switch sends Hello BPDUs advertising its BID
3. Switches compare received BIDs to their own
4. The switch with the lowest priority wins
5. If priorities tie, the switch with the lowest MAC address wins
6. The winning switch becomes the root bridge for that VLAN

Example (VLAN 1, all default priority):

| Switch | Priority | MAC Address | BID |
|---|---|---|---|
| SW1 | 32769 | 0011.1111.1111 | 32769:0011.1111.1111 |
| SW2 | 32769 | 00AA.BBBB.1111 | 32769:00AA.BBBB.1111 |
| SW3 | 32769 | 0055.6666.7777 | 32769:0055.6666.7777 |

SW1 wins because 0011.1111.1111 is the lowest MAC address.

---

## 6. Cisco IOS STP Command Reference

| Task | Command | Mode |
|---|---|---|
| View STP for all VLANs | `show spanning-tree` | Privileged EXEC |
| View STP for specific VLAN | `show spanning-tree vlan 10` | Privileged EXEC |
| View interface STP detail | `show spanning-tree interface Gi0/1 detail` | Privileged EXEC |
| Set priority to become root | `spanning-tree vlan 10 priority 4096` | Global config |
| Use macro to set root | `spanning-tree vlan 10 root primary` | Global config |
| Use macro for secondary root | `spanning-tree vlan 10 root secondary` | Global config |
| Enable PortFast on port | `spanning-tree portfast` | Interface config |
| Enable PortFast globally | `spanning-tree portfast default` | Global config |
| Enable BPDU Guard on port | `spanning-tree bpduguard enable` | Interface config |
| Enable BPDU Guard globally | `spanning-tree portfast bpduguard default` | Global config |
| Enable Root Guard | `spanning-tree guard root` | Interface config |
| Recover from err-disabled | `shutdown` then `no shutdown` | Interface config |

---

## 7. STP Diagram Analysis Method

Use this method on any CCNA STP diagram question:

1. Identify the root bridge — find the switch with the lowest BID (priority first, then MAC)
2. Mark all root bridge ports as Designated Ports (DP)
3. For each non-root switch, calculate the cumulative path cost to root on each uplink; the port with the lowest cost is the Root Port (RP)
4. For each segment connecting two non-root switches, determine which switch is closer to root (lower cumulative cost); that switch's port is Designated (DP)
5. All remaining ports that are not RP or DP are Non-Designated and go into Blocking state

---

## 8. CCNA Exam Tips

1. When all switches have the same Bridge Priority, the root bridge is elected by lowest MAC address. The exam frequently tests this tiebreaker scenario.

2. 802.1D STP has five port states; 802.1w RSTP has three. The most common mistake is confusing these. RSTP combines Blocking, Listening, and Disabled into the single Discarding state.

3. PortFast is for end-device ports only. The exam always tests whether a student knows not to enable PortFast on switch-to-switch uplinks.

4. BPDU Guard puts a port into err-disabled state when a BPDU is received on a PortFast-enabled port. The port must be manually recovered by `shutdown` and `no shutdown`.

5. The `spanning-tree vlan 10 root primary` macro sets priority to 24576 (or lower if needed). It does NOT set priority to 0. This is a common exam distractor.

6. Root Guard is configured on ports where you do NOT want a Root Port to form. It is placed on Designated Ports facing downstream to prevent an unauthorized switch from claiming the root bridge role.

7. In PVST+, a separate STP instance runs per VLAN. This allows engineering to make SW1 root for VLAN 10 and SW2 root for VLAN 20, distributing traffic across redundant uplinks.

8. The cost to the root in `show spanning-tree` output is the cumulative cost from that switch to root. Check that the Root Port has the lowest cumulative cost among all uplinks on that switch.

---

## 9. Study Checklist

Work through each item before taking the quiz.

- [ ] Define all 14 glossary terms without notes
- [ ] Memorize the path costs for 10G, 1G, 100M, and 10M interfaces
- [ ] Draw a three-switch STP topology from memory and label all port roles (RP, DP, Blocked)
- [ ] Explain the root bridge election process with a tie-break example using MAC addresses
- [ ] List all five 802.1D port states and all three RSTP port states
- [ ] Write the commands to force SW1 to become root for VLAN 10 and VLAN 20
- [ ] Explain when PortFast should and should not be used
- [ ] Complete the Module 05 Packet Tracer lab activity
- [ ] Post your Module 05 discussion response by Wednesday at 11:59 PM

---

## Required Study Resources

- Cisco CCNA certification training information: cisco.com/c/en/us/training-events/training-certifications
- Free CCNA study notes and video summaries: professormesser.com

---

## 10. Supplemental Resources

The following open educational resources extend STP and RSTP concepts to CCNA exam depth. All resources are freely available.

1. **Cisco Networking Academy — CCNA: Switching, Routing, and Wireless Essentials, Chapter 5 (STP)** (skillsforall.com): This free chapter provides interactive STP topology simulations where students can visually observe port state transitions and root bridge election outcomes in animated Packet Tracer activities.

2. **Jeremy's IT Lab — Spanning Tree Protocol (Days 20–22)** (youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ): Three comprehensive video lessons cover 802.1D STP election process, PVST+ per-VLAN operation, RSTP port roles and states, and PortFast/BPDU Guard configuration with CLI walkthroughs.

3. **Cisco Learning Network — STP and RSTP Study Resources** (learningnetwork.cisco.com): The Cisco Learning Network community includes detailed STP troubleshooting threads, practice topology diagrams with port role labeling exercises, and exam-focused STP/RSTP comparison questions.

4. **Cisco Packet Tracer — STP Lab Activities** (skillsforall.com): The Cisco Networking Academy provides dedicated Packet Tracer labs for observing root bridge election, blocking port determination, and BPDU Guard trigger behavior — all directly applicable to the Module 05 lab.

5. **IEEE 802.1D Standard Overview — Wikipedia** (en.wikipedia.org/wiki/Spanning_Tree_Protocol): A freely accessible reference summarizing the IEEE 802.1D and 802.1w RSTP standards, port states comparison, and timer definitions. Useful for quick reference when reviewing exam prep materials.

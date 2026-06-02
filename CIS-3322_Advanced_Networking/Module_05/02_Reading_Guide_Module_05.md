# Reading Guide: Module 05 - Spanning Tree Protocol (STP & RSTP)

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

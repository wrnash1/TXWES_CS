# Video Script: Module 05 - Spanning Tree Protocol (STP & RSTP)

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Estimated Duration:** 22 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Record in 1080p with a clean slide backdrop
- Use Packet Tracer 8.x for all STP topology demonstrations
- Animate port state transitions with color changes: orange for blocking/learning, green for forwarding
- Insert [SHOW DIAGRAM] markers as full-screen overlays
- Pause 2 seconds after each CCNA Exam Tip callout

---

## Section 1: Why STP Exists [00:00 - 03:30]

Welcome to Module 05. I am Professor Nash. Today we cover Spanning Tree Protocol — the mechanism that keeps Layer 2 networks from destroying themselves.

Here is the problem STP solves. Ethernet networks with redundant paths have no built-in TTL like IP packets do. If a switch forwards a broadcast frame and there are multiple paths between switches, the frame will loop indefinitely — each switch forwarding it to the next, growing exponentially. Within seconds, a broadcast storm can consume 100% of bandwidth and crash the entire network.

[SHOW DIAGRAM: Three switches connected in a triangle with no STP. An ARP broadcast enters at SW1, is forwarded by SW2 and SW3, arrives back at SW1, and the loop continues indefinitely with frame count growing rapidly]

STP solves this by selectively blocking one or more switch ports to create a loop-free tree topology while keeping the redundant paths available for failover.

Today's topics:

- STP root bridge election process and Bridge ID calculation
- Port roles: Root Port, Designated Port, Non-Designated (Blocked) Port
- STP port states: Blocking, Listening, Learning, Forwarding
- 802.1D classic STP versus 802.1w RSTP convergence comparison
- Cisco-specific features: PVST+, Rapid PVST+, PortFast, BPDU Guard, Root Guard
- Cisco IOS STP configuration and verification commands

---

## Section 2: Root Bridge Election and Bridge ID [03:30 - 08:30]

[SHOW DIAGRAM: Four switches in a partial mesh. Each switch labeled with its Bridge ID showing Priority + MAC. The switch with the lowest BID is highlighted as the Root Bridge]

STP elects a single root bridge per VLAN. Every switch participates in the election by exchanging Bridge Protocol Data Units (BPDUs). The switch with the lowest Bridge ID (BID) wins.

The Bridge ID is composed of two parts:

- Bridge Priority: a 2-byte value defaulting to 32768. Must be set in increments of 4096.
- MAC Address: the 6-byte burned-in MAC of the switch. Used as a tiebreaker when priorities are equal.

The full BID format includes a 12-bit Extended System ID (the VLAN ID) combined with the priority, producing values like 32768 + VLAN 1 = 32769.

BID comparison rules:

1. Compare Bridge Priority values first — lowest wins
2. If priorities are equal, compare MAC addresses — lowest wins

CCNA Exam Tip: The exam frequently presents a tie-break scenario with all switches at default priority 32768. In that case, the switch with the lowest MAC address becomes root. MAC address is the tiebreaker, not hostname or any other value.

To force a specific switch to become root:

```ios
SW-DIST-1(config)# spanning-tree vlan 10 priority 4096
```

Or use the macro:

```ios
SW-DIST-1(config)# spanning-tree vlan 10 root primary
```

The `root primary` macro sets the priority to 24576 (or lower if another switch has a priority below 24576, in which case it subtracts 4096 until it wins).

---

## Section 3: Port Roles and Path Cost [08:30 - 13:00]

[SHOW DIAGRAM: Three-switch topology with one root bridge (SW1) and two non-root switches (SW2 and SW3). Ports labeled as Root Port (RP), Designated Port (DP), or Blocked (B) based on path costs]

Once the root bridge is elected, every other switch determines how to reach it by calculating path costs.

Cisco STP port costs are based on link speed:

- 10 Gbps: cost 2
- 1 Gbps: cost 4
- 100 Mbps: cost 19
- 10 Mbps: cost 100

### Root Port

Every non-root switch selects the port with the lowest cumulative path cost to the root bridge as its Root Port. There is exactly one Root Port per non-root switch.

### Designated Port

On each network segment (link), the switch offering the best path to the root is the Designated Switch, and its port on that segment is the Designated Port. The root bridge has all of its ports as Designated Ports.

### Non-Designated Port

Any port that is neither a Root Port nor a Designated Port is placed in the Blocking state to break the loop. This is the port that STP selectively shuts down.

CCNA Exam Tip: In any STP diagram, identify the root bridge first (lowest BID). Then every other switch's Root Port points toward root. On each segment, the switch closer to root has the Designated Port. The remaining port is Blocked.

---

## Section 4: STP Port States and 802.1D vs RSTP [13:00 - 18:00]

[SHOW DIAGRAM: STP state machine showing the transition path from Blocking to Forwarding for 802.1D, with timers labeled at each transition]

### 802.1D STP Port States

Classic 802.1D STP has five port states:

- Blocking: receives BPDUs but does not forward frames. Initial state after topology change.
- Listening: sends and receives BPDUs. Does not forward frames. Lasts 15 seconds (Forward Delay).
- Learning: builds MAC address table. Does not forward frames. Lasts 15 seconds (Forward Delay).
- Forwarding: normal operation — forwards frames and builds MAC table.
- Disabled: administratively shut down.

Total 802.1D convergence: 15 + 15 = 30 seconds minimum from Blocking to Forwarding. In a worst case with max age timer: up to 50 seconds.

### 802.1w RSTP Port States

RSTP (Rapid Spanning Tree Protocol) reduces convergence to 1-2 seconds by introducing proposal/agreement handshakes between neighboring switches. RSTP uses only three port states:

- Discarding: combines Blocking, Listening, and Disabled
- Learning: same as 802.1D
- Forwarding: same as 802.1D

RSTP also introduces two new port roles:

- Alternate Port: the best alternative path to root (replaces Blocked port in 802.1D)
- Backup Port: a redundant path to the same segment as an existing Designated Port

CCNA Exam Tip: Know both state sets. The exam tests you on the number of STP port states (802.1D has five, RSTP has three) and which states are combined in RSTP. The most common mistake is stating RSTP has five states.

---

## Section 5: PortFast, BPDU Guard, Root Guard, and Lab Preview [18:00 - 22:00]

### PortFast

PortFast allows an access port connected to an end device to skip the Listening and Learning states and go directly to Forwarding. This eliminates the 30-second delay that would otherwise prevent a PC from getting a DHCP address quickly.

PortFast should ONLY be used on access ports. Never enable PortFast on ports connected to other switches.

```ios
SW1(config-if)# spanning-tree portfast
```

Enable globally for all access ports:

```ios
SW1(config)# spanning-tree portfast default
```

### BPDU Guard

BPDU Guard protects PortFast-enabled ports from rogue switch connections. If any BPDU is received on a BPDU Guard-protected port, the port is immediately placed in err-disabled state.

```ios
SW1(config-if)# spanning-tree bpduguard enable
```

### Root Guard

Root Guard prevents an unauthorized switch from claiming the root bridge role. When configured on a port, if a superior BPDU (a BPDU that would make the connected switch the new root) is received, the port is placed in root-inconsistent (blocking) state.

```ios
SW1(config-if)# spanning-tree guard root
```

Verify STP configuration:

```ios
SW1# show spanning-tree
SW1# show spanning-tree vlan 10
SW1# show spanning-tree interface GigabitEthernet0/1 detail
```

[SHOW DIAGRAM: Terminal output of show spanning-tree showing root bridge BID, local bridge BID, and per-port roles and states]

For additional study, visit cisco.com/c/en/us/training-events/training-certifications and professormesser.com.

---

## End Card

Module 05 Complete
Next: Module 06 - EtherChannel Link Aggregation
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash

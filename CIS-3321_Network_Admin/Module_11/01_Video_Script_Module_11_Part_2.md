# Video Script: Module 11 — Switching: VLANs, STP, and EtherChannel (Part 2)

## Course: CIS-3321 Network Administration | CompTIA Network+ (N10-008)

## Texas Wesleyan University | Professor Nash

Estimated Runtime: 11–13 minutes

---

### [INTRO]

Welcome back. In Part 1 we covered how switches work, VLANs, 802.1Q trunking, and Spanning Tree Protocol through RSTP and PortFast. In Part 2, we cover EtherChannel link aggregation, the specific Cisco IOS commands for VLAN and trunk configuration, and how to interpret the output of the key show commands for troubleshooting.

---

### [SECTION 1: ETHERCHANNEL — THE PROBLEM IT SOLVES]

[SHOW DIAGRAM: Two switches connected by four physical links — STP blocking three of them, only one active]

Here is a common scenario: you have two distribution switches connected by four physical links. You want to use all four links for throughput. The problem is STP. With four links between the same two switches, STP sees a loop and blocks three of the four ports. Only one link is active. You have four times the hardware but one-quarter the potential bandwidth.

EtherChannel solves this. EtherChannel bundles multiple physical links into a single logical link. STP sees the bundle as one link, so no ports are blocked. All physical links are active and carry traffic simultaneously.

Additional benefits: if one physical link in the bundle fails, EtherChannel automatically redistributes traffic across the remaining links. The logical link stays up. STP reconvergence is not triggered.

---

### [SECTION 2: ETHERCHANNEL LOAD BALANCING]

[SHOW DIAGRAM: EtherChannel bundle with four physical links — traffic flows shown distributed across links based on source/destination MAC hash]

EtherChannel does not send each frame down all four links at once. It selects which physical link to use for each flow based on a hashing algorithm. The hash can be based on:

- Source MAC address
- Destination MAC address
- Source and destination MAC address (XOR hash)
- Source IP address
- Destination IP address
- Source and destination IP address

The specific hash method is configurable and affects load distribution. If all traffic comes from the same source MAC, all traffic flows down the same physical link regardless of how many are in the bundle. The goal is to configure the hash so traffic is spread across links.

EtherChannel does not load-balance on a per-packet basis — it load-balances on a per-flow basis. All packets in the same conversation (same source/destination pair) follow the same physical link. This preserves packet ordering.

---

### [SECTION 3: LACP AND PAGP]

[SHOW DIAGRAM: Two switches with LACP messages being exchanged to negotiate the EtherChannel bundle]

Two protocols negotiate EtherChannel formation:

LACP (Link Aggregation Control Protocol) — IEEE 802.3ad standard. Works between devices from any vendor. Preferred in multi-vendor environments. Port modes: Active (sends LACP negotiation messages) and Passive (responds but does not initiate). Both sides cannot be Passive — at least one must be Active.

PAgP (Port Aggregation Protocol) — Cisco proprietary. Only works between Cisco devices. Port modes: Desirable (actively negotiates) and Auto (responds but does not initiate). Both sides cannot be Auto.

Static (On mode) — No negotiation protocol. Both sides are forced to form an EtherChannel without LACP or PAgP. Both sides must be set to On. Risk: if one side is misconfigured, no protocol detects the error.

For the CompTIA Network+ exam, know that LACP is the open-standard protocol and that an Active/Active or Active/Passive combination forms the channel.

---

### [SECTION 4: CISCO VLAN CONFIGURATION COMMANDS]

[SHOW DIAGRAM: Cisco IOS CLI window with VLAN configuration commands]

Now let's look at the actual commands for configuring VLANs on a Cisco switch.

Creating a VLAN and naming it:

```cisco
vlan 10
 name Finance
!
vlan 20
 name HR
!
vlan 30
 name Engineering
```

Assigning a port as an access port in VLAN 10:

```cisco
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 10
```

Configuring a trunk port:

```cisco
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 10,20,30
 switchport trunk native vlan 999
```

Note: On older Cisco switches you must specify the encapsulation (`dot1q`) before setting the mode to trunk. On newer switches, dot1Q is the only option and this step may be automatic.

Verifying VLAN configuration:

```cisco
show vlan brief
show interfaces trunk
show interfaces FastEthernet0/1 switchport
```

---

### [SECTION 5: CISCO STP CONFIGURATION AND VERIFICATION]

[SHOW DIAGRAM: show spanning-tree output with Root Bridge, port roles, and port states highlighted]

Viewing STP topology:

```cisco
show spanning-tree
show spanning-tree vlan 10
show spanning-tree summary
```

The output shows the Root Bridge ID, each port's role (Root, Designated, Alternate), and each port's state (Forwarding, Blocking, Discarding).

Configuring the Root Bridge — set the priority lower than the default 32768:

```cisco
spanning-tree vlan 10 priority 4096
```

Or use the macro that sets it automatically:

```cisco
spanning-tree vlan 10 root primary
spanning-tree vlan 10 root secondary
```

Enabling PortFast and BPDU Guard on an access port:

```cisco
interface FastEthernet0/5
 spanning-tree portfast
 spanning-tree bpduguard enable
```

Enabling BPDU Guard globally on all PortFast-enabled ports:

```cisco
spanning-tree portfast bpduguard default
```

---

### [SECTION 6: CISCO ETHERCHANNEL CONFIGURATION]

[SHOW DIAGRAM: Two switches — EtherChannel bundle using four Fa0/1–Fa0/4 ports, configured with LACP]

Configuring an LACP EtherChannel on interfaces Fa0/1 through Fa0/4:

```cisco
interface range FastEthernet0/1 - 4
 switchport mode trunk
 channel-group 1 mode active
```

This creates a logical Port-Channel interface (Port-Channel1). Configure VLAN and trunk settings on the Port-Channel interface, not on the individual physical interfaces:

```cisco
interface Port-Channel1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

Verifying EtherChannel:

```cisco
show etherchannel summary
show etherchannel port-channel
show interfaces Port-Channel1
```

The summary output shows the channel group number, protocol (LACP/PAgP), and whether each physical port is bundled (P) or standalone (I). A port shown as (D) is down.

---

### [SECTION 7: STP MANIPULATION ATTACKS]

[SHOW DIAGRAM: Attacker injecting superior BPDUs to become Root Bridge — traffic redirected through attacker's device]

Just as DHCP has rogue server attacks and OSPF has rogue route injection, STP has its own attack: Root Bridge manipulation.

An attacker connects a device to the network and sends BPDU packets with a very low Bridge Priority — lower than the legitimate Root Bridge. Other switches accept these as superior BPDUs and elect the attacker's device as the new Root Bridge.

The impact: switches recalculate their port roles based on the new Root Bridge. Traffic paths change. If the attacker is now in the forwarding path, traffic passes through their device — enabling interception, modification, or denial of service.

Mitigations:

BPDU Guard — On all access ports using PortFast. If a BPDU is received on a PortFast-enabled port, the port err-disables immediately.

Root Guard — Prevents a port from becoming a Root Port. If a superior BPDU is received on a Root Guard-enabled port, the port is placed in root-inconsistent state (not forwarding). Appropriate for ports facing downstream switches where you want to ensure the upstream root never changes.

BPDU Filter — Suppresses BPDUs on PortFast ports (use with caution — disabling BPDUs entirely on a port means no STP protection at all if a switch is connected).

---

### [SECTION 8: LAYER 2 SWITCH SECURITY — PORT SECURITY]

[SHOW DIAGRAM: MAC flooding attack — attacker generating thousands of fake MAC addresses, filling the CAM table, causing the switch to flood like a hub]

MAC address flooding is a Layer 2 attack. An attacker sends frames with thousands of fake source MAC addresses. The switch's MAC address table fills up. When the table is full, the switch can no longer learn new addresses and begins flooding all traffic to all ports — essentially turning the switch into a hub. The attacker receives a copy of all traffic.

Port Security prevents this. Port Security limits the number of MAC addresses allowed on a switch port. When the limit is exceeded, the port takes a security action:

Shutdown (default) — Port is placed in err-disabled state.

Restrict — Frames from unauthorized MACs are dropped; a security violation counter increments; an SNMP trap can be sent.

Protect — Frames from unauthorized MACs are dropped silently; no counter or trap.

Port Security configuration:

```cisco
interface FastEthernet0/3
 switchport mode access
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation shutdown
 switchport port-security mac-address sticky
```

The `sticky` keyword causes the switch to automatically learn and permanently record the MAC addresses seen on that port, saving them to running configuration.

---

### [SECTION 9: TROUBLESHOOTING VLAN AND TRUNK ISSUES]

[SHOW DIAGRAM: Flowchart — troubleshooting a VLAN connectivity problem step by step]

Common VLAN and trunk issues and the commands to diagnose them:

Issue 1: Host cannot communicate with others in same VLAN.

- Run `show vlan brief` — verify the port is assigned to the correct VLAN and the VLAN is active.
- Run `show interfaces FastEthernetX switchport` — verify the port is in access mode.

Issue 2: Traffic between switches on a VLAN fails.

- Run `show interfaces trunk` — verify the trunk is up, the encapsulation is 802.1Q, and the VLAN is in the "VLANs allowed and active" list.
- Check that the native VLAN matches on both ends — a native VLAN mismatch causes STP issues and traffic errors.

Issue 3: VLAN not passing over trunk.

- Verify the VLAN is in the allowed VLAN list: `switchport trunk allowed vlan add 20`
- Verify the VLAN exists in the VLAN database on both switches.

Issue 4: Port stuck in err-disabled state.

- Show the reason: `show interfaces FastEthernetX status` — shows "err-disabled" and reason.
- Common causes: BPDU Guard triggered, Port Security violation, loopback detection.
- Recovery: Fix the root cause, then `shutdown` and `no shutdown` to re-enable.

---

### [SUMMARY — PART 2]

In Part 2 we covered:

- EtherChannel: purpose, load balancing by flow, LACP vs. PAgP, static On mode
- Cisco VLAN configuration: creating VLANs, access ports, trunk ports
- STP configuration: setting Root Bridge priority, PortFast, BPDU Guard, Root Guard
- EtherChannel configuration with LACP, the Port-Channel interface, and verification commands
- STP manipulation attacks and mitigations
- Port Security: MAC flooding defense, violation modes, sticky MAC learning
- Troubleshooting VLANs and trunks using show vlan, show interfaces trunk, and show spanning-tree

Module 11 topics cover a significant portion of CompTIA Network+ Domain 2 (Network Implementation). Make sure you understand VLAN tagging, the STP election process, RSTP port roles, and EtherChannel negotiation protocols before the exam.

See you in the lab.

---

CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash

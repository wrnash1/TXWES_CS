# Video Script: Module 04 - Switching Concepts & VLANs

**Course:** CIS-3322 Advanced Networking
**Certification Alignment:** Cisco CCNA 200-301 (Domain 2: Network Access - 20%)
**Estimated Duration:** 22 minutes
**Recorded by:** Professor Nash | Texas Wesleyan University

---

## Production Notes

- Record in 1080p with a clean slide backdrop
- Use Packet Tracer 8.x for all VLAN and trunk demonstrations
- Show `show vlan brief` and `show interfaces trunk` output as full-screen overlays
- Insert [SHOW DIAGRAM] markers as full-screen overlays
- Pause 2 seconds after each CCNA Exam Tip callout

---

## Section 1: Introduction - Why VLANs Matter [00:00 - 03:00]

Welcome to Module 04. I am Professor Nash. Today we cover VLANs and switching concepts — topics that account for a significant portion of the CCNA 200-301 Network Access domain.

Without VLANs, every device on a switch shares the same broadcast domain. A 200-port switch with no VLANs means that every broadcast — ARP requests, DHCP discovery, STP BPDUs — reaches all 200 devices simultaneously. That creates performance problems and security risks. VLANs solve both.

[SHOW DIAGRAM: A flat switch with 6 devices all receiving a broadcast wave, versus a VLAN-segmented switch where the broadcast is contained within VLAN 10 only, not reaching VLAN 20 devices]

Today's topics:

- How switches build and use MAC address tables
- VLAN concepts and port types (access and trunk)
- 802.1Q frame tagging
- Native VLAN configuration and security
- DTP (Dynamic Trunking Protocol) and when to disable it
- Full Cisco IOS VLAN and trunk configuration walkthrough

---

## Section 2: Layer 2 Switching Fundamentals [03:00 - 07:30]

Before we configure VLANs, let us briefly review how switches forward frames at Layer 2.

When a frame arrives on a switch port, the switch reads the source MAC address and records it in the MAC address table along with the incoming port number. This is called MAC address learning. When a frame arrives with a destination MAC that is already in the table, the switch forwards it only to the correct port — this is unicast forwarding. When the destination MAC is unknown, the switch floods the frame out all ports except the source port — this is unknown unicast flooding.

[SHOW DIAGRAM: Switch MAC address table with 4 entries showing MAC address, VLAN, and port columns. A new frame arrives showing the learning process and selective forwarding]

Key MAC address table behaviors:

- Entries age out after 300 seconds by default (configurable)
- Broadcast frames (destination FF:FF:FF:FF:FF:FF) are always flooded within the VLAN
- Multicast frames are flooded unless IGMP snooping is enabled

CCNA Exam Tip: A switch that receives a frame with a destination MAC that is not in its MAC address table will flood the frame. This is not a failure — it is expected behavior for unknown unicast destinations.

---

## Section 3: VLANs and Port Types [07:30 - 13:00]

A VLAN is a logical broadcast domain created within a switch. Devices in the same VLAN communicate at Layer 2 as if they are on the same physical segment, regardless of which physical ports or switches they connect to. Devices in different VLANs cannot communicate without a Layer 3 device (a router or multilayer switch) routing between them.

[SHOW DIAGRAM: A switch with 8 ports: ports 1-4 in VLAN 10 (labeled Engineering) and ports 5-8 in VLAN 20 (labeled Sales). Broadcast within VLAN 10 stops at the VLAN boundary]

### Access Ports

An access port belongs to exactly one VLAN. When a PC connects to a switch access port, the PC sends untagged Ethernet frames. The switch internally associates those frames with the assigned VLAN. When the switch forwards the frame to a trunk port, it adds an 802.1Q tag identifying the VLAN.

Configure an access port:

```ios
SW1(config)# interface FastEthernet0/1
SW1(config-if)# switchport mode access
SW1(config-if)# switchport access vlan 10
```

### Trunk Ports

A trunk port carries traffic for multiple VLANs simultaneously. Trunk ports are used on uplinks between switches and between switches and routers (for Router-on-a-Stick inter-VLAN routing). Each frame on a trunk has an 802.1Q tag identifying its VLAN.

[SHOW DIAGRAM: Two switches connected via a trunk link. VLAN 10 frames shown with a blue 802.1Q tag, VLAN 20 frames shown with a green tag traveling across the same physical trunk link]

Configure a trunk port:

```ios
SW1(config)# interface GigabitEthernet0/1
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 10,20,30
```

CCNA Exam Tip: Access ports strip the 802.1Q tag before delivering frames to end devices. End devices (PCs, printers) never see the VLAN tag. Only switches and routers handle tagged frames on trunk links.

---

## Section 4: Native VLAN and DTP [13:00 - 18:00]

### Native VLAN

The native VLAN is the one VLAN on an 802.1Q trunk that sends frames without a tag. By default, the native VLAN is VLAN 1 on Cisco switches. Both ends of a trunk must agree on the native VLAN — a mismatch generates a CDP warning:

```text
%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/1
```

The security concern: if the native VLAN on a trunk is also the access VLAN of a connected end device, an attacker can craft double-tagged frames to "hop" from one VLAN to another. Best practice is to change the native VLAN to an unused VLAN number (such as VLAN 999) that no end devices belong to.

```ios
SW1(config-if)# switchport trunk native vlan 999
```

### DTP - Dynamic Trunking Protocol

DTP is Cisco-proprietary and allows two switches to automatically negotiate whether to form a trunk. The four DTP modes are:

- `switchport mode trunk` — always a trunk; sends DTP frames
- `switchport mode access` — never a trunk; sends DTP frames
- `switchport mode dynamic desirable` — actively tries to form a trunk
- `switchport mode dynamic auto` — forms a trunk only if the other side actively requests it

[SHOW DIAGRAM: DTP negotiation matrix table showing which combinations of modes result in trunk or access ports]

Two ports set to `dynamic auto` will NOT form a trunk — both sides are passive. This is a common CCNA exam trap.

Security best practice: disable DTP on all user-facing ports and any port that should not form a trunk:

```ios
SW1(config-if)# switchport mode access
SW1(config-if)# switchport nonegotiate
```

CCNA Exam Tip: On user-facing access ports, always use `switchport mode access` plus `switchport nonegotiate`. This hard-codes the port as an access port and disables DTP, preventing a rogue switch from establishing an unauthorized trunk.

---

## Section 5: Verification Commands and Lab Preview [18:00 - 22:00]

These commands verify your VLAN and trunk configuration:

```ios
SW1# show vlan brief
SW1# show interfaces trunk
SW1# show interfaces FastEthernet0/1 switchport
SW1# show mac address-table
```

[SHOW DIAGRAM: Terminal output of show vlan brief showing VLAN IDs 1, 10, 20 with their names and port assignments in a clean tabular format]

`show vlan brief` shows all VLANs and their assigned ports but does not show trunk ports — trunk ports do not appear in VLAN assignments because they carry multiple VLANs.

`show interfaces trunk` shows only trunk ports, their 802.1Q encapsulation status, native VLAN, and the VLANs allowed and active on each trunk.

This week's Packet Tracer lab walks you through creating VLANs, assigning access ports, configuring trunks, and verifying the full configuration on a two-switch topology. You will also interpret `show vlan brief` output to identify misconfigured ports.

For additional study, visit cisco.com/c/en/us/training-events/training-certifications and professormesser.com.

---

## End Card

Module 04 Complete
Next: Module 05 - Spanning Tree Protocol (STP and RSTP)
Resources: cisco.com/c/en/us/training-events/training-certifications | professormesser.com
Texas Wesleyan University | CIS-3322 Advanced Networking | Professor Nash
